---
name: fuzzy-species-search
version: "1.0.0"
last_updated: "2026-06-06"
description: Multi-layer fuzzy species literature search — exact→variant→substring→Chinese name→cross-engine, auto-dedup
runAs: subagent
allowed-tools:
  - scholar_search_literature_graph
  - article_search_literature
  - scholar_search_google_scholar_key_words
  - tavily_tavily_search
---
# Fuzzy Species Search

> **Problem solved**: Species name typos in academic publishing (0.5-2%) cause exact-match search to miss papers.
> **Gemini's advantage**: Semantic/fuzzy matching catches "Ochetobibus" when searching "Ochetobius".
> **Our solution**: Multi-layer protocol that replicates and exceeds Gemini's fuzzy matching by brute-force variant coverage.

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

OUTPUT: unified paper list with:
  - dedup_count: N duplicates removed
  - engine_coverage: which engines found each paper
  - gap_warnings: papers found by only 1 engine
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
