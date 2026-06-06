---
name: unified-species-search
version: "3.1.0"
last_updated: "2026-06-06"
description: 统一物种文献搜索——OCR 变体预生成 + 多 query 并行 + 引用回溯 + 新论文检测。5 步全覆盖，零遗漏。
runAs: subagent
allowed-tools: web_fetch, web_search, read_file, ncbi_ncbi_esearch, ncbi_ncbi_esummary, ncbi_ncbi_efetch, scholar_search_literature_graph, scholar_search_google_scholar_key_words, article_search_literature
---
# Unified Species Search v3.1

> **核心理念**：OCR 变体预生成 + 多 query 并行 + 引用回溯 + 新论文检测。禁止只搜精确学名一次。

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

## 1. 多引擎并行搜索 [v3.1 强制并行]

**所有 query 同时发出，不等待前面的结果：**

```
FOR EACH query IN all_queries:
  PARALLEL:
    ncbi_esearch(query, maxResults=50)
    scholar_search_literature_graph(query, limit=20)
    article_search_literature(keyword=query, max_results=10)

# 额外：中文名只搜 scholar
FOR EACH chinese_alias:
  scholar_search_google_scholar_key_words(chinese_alias, num_results=10)
```

合并所有 PMID + DOI，去重。

---

## 2. ESummary + EFetch（批量拉元数据 + 单位）

```
# 批量拉元数据
ncbi_esummary(pmids=all_pmids_csv)

# 逐篇拉单位 + 引用回溯
FOR EACH pmid IN relevant_pmids:
  ncbi_efetch(pmid=pmid)
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

## 4. DOI 去重 + 合并

```
all_papers = merge(ncbi_results, scholar_results, article_search_results)
deduped = doi_dedup(all_papers)  # DOI 优先；无 DOI 则 title 模糊匹配
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

## 关键提示
- **Step 0 不可跳过** — 必须先读 config 才能开始搜索
- **多 query 必须并行** — 禁止"先搜精确名，看结果再搜变体"
- **拼写变体** — Ochetobius ≠ Ochetobibus，config + OCR 模型双保险
- **分类学异名** — Luciobrama macrocephalus 曾为鳤的同义名，必须同步搜索
- **引用回溯** — 中文论文不在 PubMed 中，但会被英文论文引用，从 References 抓
- **分类标准** — 正标题含 Ochetobius/鳤/Luciobrama = 专项；仅材料中出现 = 附带提及
- **新论文标记** — year >= 2025 且无 PMID → flag + 推荐直接查 DOI
