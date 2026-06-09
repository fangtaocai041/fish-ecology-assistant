---
name: unified-species-search
version: "5.0.0"
last_updated: "2026-06-20"
description: KB-First 两阶段搜索 —— 先查 f项目KB → 询问用户 → c项目 agent (coordinated_search) → P7 taxonomy feedback 写回
runAs: subagent
allowed-tools: web_fetch, web_search, read_file, ncbi_ncbi_esearch, ncbi_ncbi_esummary, ncbi_ncbi_efetch, scholar_search_literature_graph, scholar_search_google_scholar_key_words, article_search_literature, scholarly_search, tavily_search, exa_web_search
---
# Unified Species Search v5.0 — Agent-Native · P7 Feedback

> **v5.0 关键变更**: 不再自行调用 MCP 搜索工具。KB命中后暂停询问用户；若继续，**委托给 c项目 agent** (`search_coordinator.continue_full_search`)，搜索完成后自动运行 **P7 taxonomy feedback** (c项目发现的分类变更 → 写回 f项目知识库)。

---

## 0. KB-FIRST: 知识库优先检查（强制执行，不可跳过）⚠️ v4.0 核心变更

### 0.1 解析用户查询
从 arguments 或用户消息中提取：
- `scientific_name`: 学名（如 "Tribolodon hakonensis"）
- `chinese_name`: 中文名（如 "珠星三块鱼"）
- `query`: 通用查询字符串（兜底）

### 0.2 调用 f项目知识库 [必须]

**必须使用 `search_content` 在 f项目知识库中搜索**：

```
search_content "species_name_or_chinese_name" path="fish-ecology-assistant/config/fish_species_kb.yaml"
```

搜索关键词依次尝试（任一命中即停止）：
1. 完整中文名（如 "珠星三块鱼"）
2. 学名（如 "Tribolodon"）
3. 学名关键词（如 "hakonensis"）

### 0.3 读取命中的物种条目

若 `search_content` 在 `fish_species_kb.yaml` 中返回结果，使用 `read_file` 读取该条目周围的完整 YAML 内容（前后约 50 行），提取：
- `name` (中文名)
- `scientific` (学名)
- `aliases` (别名列表)
- `synonyms` (同义名)
- `family` (科属)
- `order` (目)
- `ecology` (生态描述)
- `distribution` (分布)
- `economic_value` (经济价值)
- `conservation` (保护等级)

### 0.4 呈现 KB 结果 + 询问用户 [强制暂停]

**组装 KB 摘要并以明确的询问格式输出给用户**：

```
📚 **f项目知识库检索结果**

物种：{chinese_name}（*{scientific_name}*）
科属：{family}
生态：{ecology}
分布：{basins} / {countries}
别名：{aliases}
同义名：{synonyms[:5]}
...

───
**下一步？**
- 🅰️ **留步** — 仅使用知识库数据（已获取到基本信息）
- 🅱️ **继续搜索** — 启动 c项目全量文献搜索
  （PubMed/Google Scholar/Europe PMC/Crossref + 引用回溯 + OCR变体安全网）
```

**⚠️ 此时必须 STOP 并等待用户回复。不要自动继续。**

### 0.5 根据用户选择分支

```
IF 用户选择 "留步" / "A" / "stay" / "够了":
    → 返回 KB 数据作为最终输出，标注 `source: fish-ecology-assistant KB`
    → 结束

IF 用户选择 "继续搜索" / "B" / "continue" / "搜索":
    → 继续执行下面的 §1-§6（7引擎并行搜索管线）
    → 最终输出标注 `source: cognitive-search-engine (enriched by f-KB)`
```

### 0.6 若 KB 未命中

若 `search_content` 未在 `fish_species_kb.yaml` 中找到匹配：

```
🔍 **f项目知识库未收录**: {species_name}

是否启动 c项目全量文献搜索？
（多引擎并行 + 引用回溯 + 变体安全网 — 但无 KB 预填数据加速）
```

等待用户确认后，继续执行 §1-§6。

### 0.7 变体来源（若进入全量搜索）

若用户选择继续搜索，变体/别名/同义名从 KB 已读取的数据中获取，**无需再读 species_graph.yaml**（KB 已提供）。仅当 KB 未命中时，才回退到：

```
read_file "cognitive-search-engine/config/species_graph.yaml"
```

提取 `variants[]`, `aliases[]`。

---

## P7. 分类反馈（c项目发现 → f项目知识库写回）⚠️ v5.0 新增

### P7.1 触发条件

当 c项目 `coordinated_search()` 完成后，检查返回的 `taxonomy_warning` 字段。

```
IF result.full_search.taxonomy_warning IS NOT None:
  运行 P7 反馈
```

### P7.2 执行写回

```
from fish_ecology_assistant.src.adapter import FishEcologyAdapter
adapter = FishEcologyAdapter()
result = adapter.update_taxonomy(
    species_name=taxonomy_warning.species,
    discrepancy=taxonomy_warning
)
```

### P7.3 回写内容

- **字段**: `family` (科级变更), `genus` (属级变更)
- **目标文件**: `fish-ecology-assistant/config/fish_species_kb.yaml`
- **去重**: 相同 note 不重复追加 `taxonomy_log` 条目
- **示例**: c项目发现 `Tribolodon → Pseudaspius`, 自动在 KB 条目的 `synonyms` 中追加 `Pseudaspius hakonensis`

### P7.4 阴阳闭环

```
阴(S/知识) → 阳(V/搜索) → 发现变更 → P7反馈 → 阴(S/知识更新) → 下次查询自动命中
```

**P7 是二生三的关键闭环: 阳的发现反馈给阴, 阴阳统一于三。**

---

## 1. 前处理（KB-first 之后，仅在「继续搜索」时执行）

### 1.1 解析 arguments
收到格式如 `"中文名：鳤，学名：Ochetobius elongatus"`，解析出 `chinese_name` 和 `scientific_name`。

### 1.2 OCR 错误模型自动生成变体

基于拉丁学名字符特征自动生成：
```
genus = "Ochetobius"
species = "elongatus"

# 字母插入 (每个辅音后插入相邻辅音)
variants += insert_adjacent_consonant(genus)     # "Ochetobibus"

# 字母删除 (逐个删除每个字母)
variants += delete_each_char(genus)              # "Ochetobus", "Ohetobius"

# 元音混淆 (替换每个元音)
variants += vowel_confusion(genus)                # e↔i, a↔o, u↔o

# 尾字母脱落 (删除末尾1-2字符)
variants += tail_drop(species)                   # "elongatu", "elongates"
```

### 1.3 构建搜索词列表
```
base_queries = [scientific_name] + known_misspellings + taxonomic_synonyms + chinese_aliases

# 生态关键词组合
ecology_keywords = ["diet", "feeding", "habitat", "reproduction", "conservation", "genome", "morphology"]
keyword_queries = [scientific_name + " " + kw for kw in ecology_keywords]

all_queries = base_queries + keyword_queries
```

### 1.4 预估文献量 + 自适应策略
```
count = ncbi_esearch(scientific_name).total_count
IF count < 20: mode = "exhaustive"      # 穷举，100% recall
ELSE IF count 20-200: mode = "classified"   # 先分类
ELSE: mode = "satisficing"              # 满意即止
```

---

## 1. 7 引擎并行搜索 [v3.3 强制并行]

### 1.1 工具可用性自检 [v3.3]

启动时先执行一次探测，记录可用工具：
```
available = []
FOR tool_name IN [scholar_search_literature_graph, article_search_literature, scholarly_search,
                   tavily_search, exa_web_search, ncbi_ncbi_esearch, web_search]:
    TRY tool_name("test", maxResults=1)
        available.add(tool_name)
    CATCH:
        skip  # 静默跳过不可用工具；若为 API-key 型工具，config 中标注 requires_api_key

# 分类统计
free_available = filter(available, λt: t in [scholar_*, article_*, scholarly_*, ncbi_*, web_search])
paid_available = filter(available, λt: t in [tavily_*, exa_*])
```

若无任何学术搜索工具可用→降级为 `web_search` + `web_fetch` 手动抓取。

### 1.2 11 引擎全并行 [v3.3.2 — 新增国内源]

**所有 query 同时发出，不等待前面的结果：**

```
FOR EACH query IN all_queries:
  PARALLEL (只调用 available 中的工具):
    scholar_search_literature_graph(query, limit=20)  # Google Scholar ← 首选
    article_search_literature(keyword=query, max_results=10)  # Europe PMC
    scholarly_search(query, limit=15)                 # Semantic Scholar
    ncbi_esearch(query, maxResults=50)                # PubMed
    tavily_search(query, max_results=15)              # AI 深度搜索
    exa_web_search(query, num_results=10)             # 语义搜索
    web_search(query, topK=10)                        # Reasonix 内置

# 额外：中文名搜索 + 国内学术源
FOR EACH chinese_alias:
  PARALLEL:
    scholar_search_google_scholar_key_words(chinese_alias, num_results=10)
    web_search("site:xueshu.baidu.com " + chinese_alias, topK=10)  # 百度学术
    web_search("site:cnki.net " + chinese_alias, topK=10)           # 知网
    web_search("site:wanfangdata.com.cn " + chinese_alias, topK=10) # 万方
    web_search("site:ihb.ac.cn " + chinese_alias, topK=10)          # 中科院水生所
```

### 1.3 Fallback 链 [v3.3.2 — 新增国内源]

```
学术搜索: scholar → article → scholarly → ncbi → web_search → web_fetch(DOI)
网页搜索: tavily → exa → web_search
中文搜索: scholar(也覆盖中文) → 百度学术(site:xueshu.baidu.com) → 知网(site:cnki.net) → 万方(site:wanfangdata.com.cn) → 中科院(site:ihb.ac.cn) → 引用回溯(从英文论文 References)
```

合并所有 PMID + DOI + URL，去重。

---

## 2. 元数据提取 + 全文拉取 [v3.3]

```
# NCBI: 批量拉 PubMed 元数据
ncbi_esummary(pmids=all_pmids_csv)

# 逐篇拉单位 + 引用回溯
FOR EACH pmid IN relevant_pmids:
  ncbi_efetch(pmid=pmid)

# 非 PubMed 来源: 用 web_fetch 拉 DOI 页面
FOR EACH paper WITH doi AND no pmid:
  web_fetch("https://doi.org/" + paper.doi)
  # 提取标题、作者、摘要
```

从 EFetch XML 提取：
- `Author/AffiliationInfo/Affiliation` — **精确单位，实验室级别**
- `Abstract/AbstractText` — 摘要前 300 字
- `ReferenceList/Reference[ArticleTitle 含 Ochetob/鳤]` — 引用回溯

---

## 3. 引用回溯（发现中文论文的关键）

对已找到论文的 `ReferenceList`，逐一检查：
```
IF ref.title 含 "Ochetob" OR ref.title 含 "鳤" OR ref.title 含 variant:
  提取: ref.title, ref.journal, ref.year, ref.doi
  标记来源: [从{PMID}引用回溯发现]
```

---

## 4. 多源去重 + 合并 [v3.3]

```
all_papers = merge(ncbi_results, scholar_results, article_results,
                   scholarly_results, tavily_results, exa_results, web_results)
deduped = doi_dedup(all_papers)   # DOI 优先
deduped = title_dedup(deduped)    # 无 DOI 则 title 模糊匹配 (阈值 0.85)
```

---

## 5. 分类输出

### 专项研究论文（鳤为第一/正标题核心对象）
| 序号 | 论文名 | 期刊 | 年份 | 作者 | 单位 | DOI | 来源 |

### 附带提及论文（鳤在大型调查中顺带记录）
单独列出。

### 置信度标注
- ✅ = 从 PubMed Affiliation 直接提取
- 📎 = 从引用回溯发现
- 📚 = Crossref/OpenAlex 元数据
- ❓ = 需人工核实

---

## 6. 新论文检测 [v3.1 新增]

```
current_year = 2026
FOR EACH paper IN deduped:
  IF paper.year >= current_year - 1 AND paper.pmid IS NULL:
    paper.flag = "⚠️ 新论文，PubMed 尚未索引"
    paper.action = "直接通过 DOI 访问: https://doi.org/" + paper.doi
    paper.verification_status = "DOI 已注册但未进入 PubMed 索引管道"
```

**输出时显式列出这些标记论文**，方便用户手动验证。

---

## 关键提示 [v3.3.2]
- **Step 0 不可跳过** — 必须先读 config 才能开始搜索
- **多 query 必须并行** — 禁止"先搜精确名，看结果再搜变体"
- **11 引擎并行** — scholar + article + scholarly + ncbi + baidu_scholar + cnki + wanfang + cas + tavily + exa + web_search
- **GS 优先** — scholar 排在第一位，结果 ≥ 5 篇就不换引擎
- **国内源** — 中文名搜索自动走百度学术 + 知网 + 万方 + 中科院
- **工具自检** — 先探测可用工具，区分免费/付费；仅调 available 的，静默跳过不可用的
- **Fallback 链** — 学术搜索不可用 → 降级 web_search + web_fetch(DOI)；中文不可用 → 百度学术 → 引用回溯
- **拼写变体** — Ochetobius ≠ Ochetobibus，config + OCR 模型双保险
- **分类学异名** — Luciobrama macrocephalus 曾为鳤的同义名，必须同步搜索
- **引用回溯** — 中文论文不在 PubMed 中，但会被英文论文引用，从 References 抓
- **分类标准** — 正标题含 Ochetobius/鳤/Luciobrama = 专项；仅材料中出现 = 附带提及
- **新论文标记** — year >= 2025 且无 PMID → flag + 推荐直接查 DOI
- **MCP 激活提醒** — scholar/article/scholarly/tavily/exa 需在 Reasonix 下次启动后生效
