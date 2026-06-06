---
name: fuzzy-species-search
version: "2.0.0"
last_updated: "2026-06-06"
description: "[已弃用] 请使用 unified-species-search — 多层模糊搜索逻辑已迁移至统一搜索"
runAs: subagent
allowed-tools: web_fetch, web_search, read_file
---
# Fuzzy Species Search

> **Problem solved**: Species name typos in academic publishing (0.5-2%) cause exact-match search to miss papers.
> **Gemini's advantage**: Semantic/fuzzy matching catches "Ochetobibus" when searching "Ochetobius".
> **Our solution**: Multi-layer protocol that replicates and exceeds Gemini's fuzzy matching by brute-force variant coverage.
>
> ⚠️ **v3 available**: [cognitive-species-search](cognitive-species-search.md) — adds semiotics, linguistics, phonetics, logic, and DeepSeek chain-of-thought. Use cognitive-species-search for maximum coverage.

## PREFLIGHT (MANDATORY)

1. READ `config/species_variants.yaml` → pre-computed variants for target species
2. EXTRACT: `{genus, species, chinese_name, known_misspellings, target_journals}`

## Search Protocol (7 layers)

### Layer 1: Exact Search (baseline)

```
SEARCH scholar_search_literature_graph:
  query = "{genus} {species}"
  limit = 20

SEARCH article_search_literature:
  keyword = "{genus} {species}"
  max_results = 20
```

### Layer 2: Variant Search (catch typos)

```
FOR EACH variant IN known_misspellings:
  SEARCH scholar_search_literature_graph:
    query = "{variant}"
    limit = 10

ALSO: generate common typos algorithmically:
  - Single char insertions (e.g., Ochetobius → Ochetobibus)
  - Single char deletions (Ochetobius → Ochetobus)
  - Adjacent swaps (Ochetobius → Ochtoebius)
  FOR EACH generated_variant (top 5):
    SEARCH article_search_literature:
      keyword = "{generated_variant}"
      max_results = 5
```

### Layer 3: Substring Search (catch all)

```
SEARCH scholar_search_literature_graph:
  query = "{genus前6字符} {species}"
  limit = 10
```

### Layer 4: Chinese Name Search (不受英文拼写影响)

```
SEARCH scholar_search_literature_graph:
  query = "{chinese_name} {species}"
  limit = 10

SEARCH tavily_tavily_search:
  query = "{chinese_name} 研究 论文 {current_year}"
```

### Layer 5: Journal + Year Range Scan (兜底)

```
FOR EACH journal IN target_journals:
  SEARCH scholar_search_literature_graph:
    query = "{journal} {chinese_name}"
    limit = 5
```

### Layer 6: Cross-Engine Verification

```
COMPARE results across engines:
  - scholar_search_literature_graph (Crossref + OpenAlex + Semantic Scholar)
  - article_search_literature (Europe PMC + PubMed + arXiv)
  - tavily_tavily_search (web search)
  - scholar_search_google_scholar_key_words (Google Scholar, strongest fuzzy match)

FLAG any paper found by only ONE engine → possible search gap
```

### Layer 7: Deduplicate & Merge

```
MERGE all results
DEDUPLICATE by DOI (primary) then title similarity (secondary, threshold > 0.90)
SORT by year (descending), then citation count
```

### Layer 8: Phonetic Search (Soundex — 借鉴语音匹配)

> **来源**: 语音识别系统的 Phonetic Matching 算法。物种名即使拼错，发音通常相近。

```
GENERATE Soundex code for genus name:
  Ochetobius → O231 (Soundex)
  Ochetobibus → O231 (same Soundex — typo doesn't change phonetics!)

SEARCH with phonetic-tolerant queries:
  - "{Soundex(genus)} {species}"  → catches phonetic equivalents
  - "Ochetob* elongatus"          → wildcard variant
```

### Layer 9: Author + Year Cross-Reference (借鉴 Google Scholar 引用图)

> **来源**: Google Scholar 的引用网络。已知论文的作者很可能在同一物种上发表多篇。

```
FROM known papers (Layers 1-7):
  EXTRACT: {authors, years, journals}

FOR EACH known_author:
  SEARCH scholar_search_google_scholar_key_words:
    query = "{author} {genus或中文名}"
    → catches papers where species name is misspelled but author is consistent

FOR EACH known_author:
  SEARCH scholar_search_literature_graph:
    query = "{author}" (不限制物种名)
    year_range = [min_year_from_known - 2, current_year]
    → catches all papers by this author in the relevant time window

MANUAL FILTER: check titles for species relevance
```

### Layer 10: Citation Graph Traversal (借鉴 Semantic Scholar 引用图)

> **来源**: Semantic Scholar 的 SPECTER2 嵌入 — 相似论文在向量空间中靠近。
> 我们用引用图遍历来模拟：已知论文 → 引用它的论文 → 它引用的论文。

```
FROM known papers (≥3 papers with DOIs):
  FOR EACH known_paper:
    GET references (article_get_references, identifier=DOI)
    GET citing papers (article_get_literature_relations, relation_types=["citing"])

  FILTER: papers that mention {genus} OR {chinese_name} in title/abstract
  ADD to results with label "citation_graph 🕸️"
```

### Layer 11: LLM-Powered Query Expansion (借鉴 Claude/Gemini 推理)

> **来源**: Claude/Gemini 的 LLM 原生模糊理解。LLM 知道 "Ochetobibus" 可能是 "Ochetobius" 的拼写错误。
> 我们用 LLM 在搜索前生成可能的错误变体和替代搜索词。

```
USE reasoning to generate search strategy:
  Prompt: "A paper about {genus} {species} might have the genus misspelled.
           Generate 5 realistic misspellings that a non-native English speaker
           or OCR error might produce. Also generate 3 alternative search
           queries that would find this paper without using the genus name."

  OUTPUT:
    - misspellings: ["Ochetobibus", "Ochetobus", "Ochetoibus", "Ochetobious", "Ochetobiuss"]
    - alternative_queries: [
        "critically endangered elongate fish Yangtze digestive system",
        "鳤 消化系统 组织学 2024 2025 2026",
        "Kner 1867 elongate Cyprinidae intestine morphology"
      ]

  SEARCH each alternative query in scholar + tavily
```

### Layer 7b: Merge All Layers

```
MERGE results from ALL 11 layers
DEDUPLICATE by DOI (primary) then title similarity (secondary, threshold > 0.90)
SORT by year (descending), then citation count

OUTPUT: unified paper list with:
  - dedup_count: N duplicates removed
  - engine_coverage: which engines found each paper
  - layer_coverage: which layer found each paper
  - gap_warnings: papers found by only 1 method
```

## Output Format

```markdown
## Fuzzy Species Search Report: {genus} {species} ({chinese_name})

### Summary
- Total unique papers: {N}
- Found by exact match: {E}
- Found by variant match: {V} 🆕
- Found by Chinese name: {C}
- Found by journal scan: {J}
- Found by phonetic match: {P} 🔊
- Found by author cross-ref: {A} 👤
- Found by citation graph: {CG} 🕸️
- Found by LLM query expansion: {LLM} 🤖
- Cross-engine gaps: {G} papers found by only 1 engine ⚠️

### Paper List
| # | Year | Title | Journal | Authors | Unit | Found By |
|:--|:-----|------|------|------|------|----------|
| 1 | 2026 | Digestive System... | Animals | Gao F et al. | 湖南水产所 | variant 🆕 |
| ... | ... | ... | ... | ... | ... | ... |

### Gap Warnings
⚠️ Paper "{title}" (DOI) found ONLY by Google Scholar —可能被其他引擎遗漏
```

## Decision Points
- Any paper found ONLY by variant search → 🆕 flag as "previously missed due to typo"
- Any paper found by only 1 engine → ⚠️ flag as "verify independently"
- Zero variant-only results → ✅ species name is consistently spelled in literature
