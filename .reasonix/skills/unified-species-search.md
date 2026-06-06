---
name: unified-species-search
version: "3.3.0"
last_updated: "2026-06-20"
description: 统一物种文献搜索——7 引擎并行 (ncbi+scholar+article+scholarly+tavily+exa+web) + OCR 变体预生成 + 引用回溯 + 新论文检测。零遗漏。
runAs: subagent
allowed-tools: web_fetch, web_search, read_file, ncbi_ncbi_esearch, ncbi_ncbi_esummary, ncbi_ncbi_efetch, scholar_search_literature_graph, scholar_search_google_scholar_key_words, article_search_literature, scholarly_search, tavily_search, exa_web_search
---
# Unified Species Search v3.3

> **核心理念**：7 引擎并行 (ncbi + scholar + article + scholarly + tavily + exa + web_search) + OCR 变体预生成 + 引用回溯 + 新论文检测。禁止只搜精确学名一次。

---

## 0. 前处理（强制执行，不可跳过）

### 0.1 读取物种变体配置 [必须]
```
read_file "config/species_variants.yaml"
```
提取该物种的：`scientific_name`, `known_misspellings[]`, `taxonomic_synonyms[]`, `chinese_aliases[]`, `target_journals[]`。

**若 config 不存在：使用 OCR 错误模型自动生成变体（见 0.3）**

### 0.2 解析 arguments
收到格式如 `"中文名：鳤，学名：Ochetobius elongatus"`，解析出 `chinese_name` 和 `scientific_name`。

### 0.3 OCR 错误模型自动生成变体 [v3.1 新增]

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

### 0.4 构建搜索词列表
```
base_queries = [scientific_name] + known_misspellings + taxonomic_synonyms + chinese_aliases

# v3.1 新增：生态关键词组合
ecology_keywords = ["diet", "feeding", "habitat", "reproduction", "conservation", "genome", "morphology"]
keyword_queries = [scientific_name + " " + kw for kw in ecology_keywords]

all_queries = base_queries + keyword_queries
```

### 0.5 预估文献量 + 自适应策略
```
count = ncbi_esearch(scientific_name).total_count
IF count < 20: mode = "exhaustive"      # 穷举，100% recall，12层全开
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

### 1.2 7 引擎全并行 [v3.3]

**所有 query 同时发出，不等待前面的结果：**

```
FOR EACH query IN all_queries:
  PARALLEL (只调用 available 中的工具):
    ncbi_esearch(query, maxResults=50)               # PubMed 免费
    scholar_search_literature_graph(query, limit=20)  # Google Scholar
    article_search_literature(keyword=query, max_results=10)  # Europe PMC
    scholarly_search(query, limit=15)                 # Semantic Scholar
    tavily_search(query, max_results=15)              # AI 深度搜索
    exa_web_search(query, num_results=10)             # 语义搜索
    web_search(query, topK=10)                        # Reasonix 内置

# 额外：中文名搜索
FOR EACH chinese_alias:
  PARALLEL:
    scholar_search_google_scholar_key_words(chinese_alias, num_results=10)
    web_search(chinese_alias, topK=10)
```

### 1.3 Fallback 链 [v3.2 新增]

```
学术搜索: scholar → article → scholarly → ncbi → web_search → web_fetch(DOI)
网页搜索: tavily → exa → web_search
中文搜索: web_search(chinese) → 引用回溯(从英文论文 References)
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

## 关键提示 [v3.3]
- **Step 0 不可跳过** — 必须先读 config 才能开始搜索
- **多 query 必须并行** — 禁止"先搜精确名，看结果再搜变体"
- **7 引擎并行** — ncbi + scholar + article + scholarly + tavily + exa + web_search 同时发出
- **工具自检** — 先探测可用工具，区分免费/付费；仅调 available 的，静默跳过不可用的
- **Fallback 链** — 学术搜索不可用 → 降级 web_search + web_fetch(DOI)；中文不可用 → 引用回溯
- **拼写变体** — Ochetobius ≠ Ochetobibus，config + OCR 模型双保险
- **分类学异名** — Luciobrama macrocephalus 曾为鳤的同义名，必须同步搜索
- **引用回溯** — 中文论文不在 PubMed 中，但会被英文论文引用，从 References 抓
- **分类标准** — 正标题含 Ochetobius/鳤/Luciobrama = 专项；仅材料中出现 = 附带提及
- **新论文标记** — year >= 2025 且无 PMID → flag + 推荐直接查 DOI
- **MCP 激活提醒** — scholar/article/scholarly/tavily/exa 需在 Reasonix 下次启动后生效
