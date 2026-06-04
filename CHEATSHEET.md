# Reasonix Quick Reference

---

## One-Shot Research

> **"Research [topic], run the full pipeline"**

---

## 12 Skills — Quick Reference

| # | Skill | Command |
|:-:|-------|---------|
| 🎯 | Full pipeline | `/skill research-orchestrator Research question: [topic]` |
| 🧑‍💼 | Planner | `/skill research-planner Research question: [topic]` |
| 🔍 | Researcher | `/skill research-executor [full research plan]` |
| 📊 | Analyst | `/skill research-analyst [full source database]` |
| ✍️ | Writer | `/skill research-writer [full analysis report]` |
| ✅ | Reviewer | `/skill research-reviewer [full draft]` |
| 🎓 | PhD proposal | `/skill phd-proposal-writer Research direction: [topic]` |
| 📊 | R stats | `/skill stats-assistant Analysis need: [need]` |
| 🔍 | Stats method | `/skill stats-method-finder Method: [method name]` |
| 📖 | Paper analysis | `/skill paper-analyzer Analyze: [DOI/abstract]` |
| 🔭 | Frontier tracking | `/skill frontier-tracker [team name]` |
| 📚 | Zotero query | `/skill zotero-assistant [query]` |
| 📝 | Obsidian notes | `/skill obsidian-assistant [action]` |

---

## 16 MCP Tools — Quick Reference

| Tool | Say | Purpose |
|------|-----|---------|
| `tavily` | "Search tavily: XXX" | Deep web search |
| `exa` | "Search exa: XXX" | Semantic search |
| `scholar` | "Search scholar: XXX" | Academic papers |
| `article` | "Fetch article: XXX" | Paper details |
| `scholarly` | "Search scholarly: XXX" | Multi-source academic |
| `playwright` | "Open URL with playwright" | Browser automation |
| `ocr` | "OCR this image with paddleocr" | Chinese OCR |
| `ocr-fallback` | "OCR with ocr-fallback" | Offline OCR |
| `echarts` | "Draw chart with echarts" | Data visualization |
| `coderunner` | "Run code with coderunner" | Sandbox execution |
| `rplay` | "Run R code with rplay" | R environment |
| `thinking` | "Analyze with thinking" | Multi-step reasoning |
| `git` | "Check git log" | Version control |
| `github` | "Search GitHub repos" | GitHub API |
| `zotero` | "Query my Zotero library" | Reference manager |
| `fs` | "Read my Obsidian notes" | Filesystem |

---

## R Analysis Decision Tree

```
Data type → Method → R package
─────────────────────────────────
Linear morphology → PCA/LDA/MANOVA → stats / MASS
Landmark data     → Procrustes+CVA → geomorph
Stable isotopes   → SIBER ellipses → SIBER
Stomach contents  → NMDS/PERMANOVA → vegan
Genetics          → PCA/DAPC/Fst   → adegenet / hierfstat
Community matrix  → RDA/dbRDA      → vegan
Distribution      → MaxEnt         → dismo / ENMeval
```

---

## Key Domain Terms

| Chinese | English |
|---------|---------|
| 生态位分化 | Niche partitioning |
| 同域共存 | Sympatric coexistence |
| 稳定同位素 | Stable isotope (δ¹³C, δ¹⁵N) |
| 几何形态测量 | Geometric morphometrics |
| 环境DNA | Environmental DNA (eDNA) |
| 简化基因组 | RAD-seq |
| 物种分布模型 | Species distribution model (SDM) |
| 长江十年禁渔 | Yangtze 10-year fishing ban (2021-2030) |
| 功能多样性 | Functional diversity |
| 保护遗传学 | Conservation genetics |

---

## PhD Proposal Template

```
/skill phd-proposal-writer Research direction: [your topic]

Produces:
├── 1. Background & Significance
├── 2. Objectives & Content
├── 3. Methodology & Workflow
├── 4. Innovation & Expected Results
├── 5. Timeline (4 academic years)
└── References (≤40, last 5 years)
```

---

## Tips

- **Be specific** — the more precise your question, the better the output
- **Split big topics** — decompose large questions into smaller sessions
- **Results auto-save** — reports land in `research_output/`
- **Cache bonus** — long sessions get 90%+ token caching → cheaper over time
