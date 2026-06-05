<p align="center">
  🇨🇳 <a href="README.zh.md">中文</a>
</p>

<div align="center">
  <h1>🌊 Panta Rhei · Everything Flows</h1>
  <p><strong>Turn your coding agent into a PhD-level research team with a dynamic worldview and DeepSeek-grade engineering efficiency.</strong></p>
  <p>16 MCP tools · 12 AI subagents · 5 search engines · 13 knowledge bases</p>
</div>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square" alt="License"></a>
  <a href="#"><img src="https://img.shields.io/badge/dynamic_worldview-core-6366f1?style=flat-square" alt="Dynamic Worldview"></a>
  <a href="#"><img src="https://img.shields.io/badge/MCP-16-22c55e?style=flat-square" alt="MCP:16"></a>
  <a href="#"><img src="https://img.shields.io/badge/subagents-12-f59e0b?style=flat-square" alt="Subagents:12"></a>
</p>

---

## 🏛️ Core Philosophy

> **The world is dynamic. Knowledge is provisional. Emergence is the norm.**

This isn't a slogan. It's the operating system that runs through every line of code, every search query, and every paper analysis in this project.

### Three Tenets

**🌍 The World Is Dynamic**
R packages update. Species distributions shift. Scientific consensus evolves. Climate change reshapes ecosystems. A correct conclusion today may be obsolete in six months. **We treat no knowledge as eternal truth** — everything is anchored on a timeline.

**📖 Knowledge Is Provisional**
The bedrock of science is falsifiability (Popper). No finding is final — only "the best current explanation." We use **calibrated language**: say "evidence suggests" not "proves," say "Smith (2022) found" not "studies show." Every output carries a timestamp.

**🔬 Emergence Is the Norm**
Life, consciousness, ecosystems, AI reasoning — all are **emergent** phenomena. Analyzing parts in isolation never reveals the whole. When ≥3 independent sources point to the same unexpected pattern, the system flags it as an **emergence signal** — not dismisses it as noise.

### Why This Matters for Research

| Risk | Traditional Approach | Dynamic Worldview Approach |
|:-----|:--------------------|:---------------------------|
| **Stale knowledge** | Run 2020 code on 2026 data | Auto-check CRAN versions, mark "verified on glmmTMB v1.1.10" |
| **Overconfidence** | "Research shows X" | "Smith (2022) found X, but Jones (2024) added Y" |
| **Ignoring signals** | Dismiss outliers as noise | ≥3 independent sources → emergence signal, actively tracked |
| **Frozen docs** | Handbook never updated | Verification log with "next review" date, calculated from package activity |

## 🐋 One Engineering Principle: Efficiency Is Intelligence

Energy is finite. Computation has a cost. DeepSeek does not scale parameters — it scales algorithms. This project applies the same engineering philosophy in four concrete implementations:

**Entropy budget** — In research-orchestrator, every pipeline stage has an explicit activation condition. PhD thesis: full pipeline. Casual query: single-step search. Compute is allocated proportionally to question importance.

**Sparse activation** — karpathy-guard defines MoE-style routing rules. Planner always runs (lightweight). Executor only with queries. Analyst only with results. Writer only with findings. Each module is a silent neuron — it fires only when the signal crosses threshold.

**Differential verification** — verify-stats-handbook never runs full checks. Probabilistic stale scoring P(stale) targets only changed packages. Review cycles are jointly determined by update frequency, breaking-change probability, and user dependency — not a fixed 3 months.

**Information-gain routing** — ima-smart-search orders keywords by information gain. P0 exact terms (e.g., glmmTMB) searched first, stops on hit. P2 redundant terms (e.g., data analysis) skipped. Cross-KB deduplication eliminates wasted reads.

## 🤔 What Is This

**Fish Ecology Assistant** transforms [Reasonix Code](https://github.com/esengine/deepseek-reasonix) from a general-purpose coding agent into a **domain-specialized fish ecology research team** — with 16 integrated MCP tools, 12 AI subagents, a 5-stage auto-orchestrated research pipeline, R statistics, and 13 connected knowledge bases. All outputs follow the dynamic worldview above.

| Capability | Vanilla Reasonix | **With This Config** |
|:-----------|:----------------:|:--------------------:|
| Search engines | 1 | **5** (tavily, exa, scholar, article, scholarly) |
| MCP services | 0 | **16** |
| AI subagents | 4 (generic) | **12** (domain-specialized, with emergence detection) |
| R statistics | — | ✅ R 4.6.0 + 20+ ecology packages |
| OCR | — | ✅ PaddleOCR + Tesseract.js |
| Reference manager | — | ✅ Direct Zotero SQL queries |
| Research pipeline | — | ✅ 5-stage + auto-review + emergence detection |
| Knowledge bases | — | ✅ 13 ima knowledge bases connected |
| Setup on new machine | Manual | ✅ One script, 5 minutes |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## ⚡ Quick Start

```bash
git clone https://github.com/fangtaocai041/fish-ecology-assistant.git
cd fish-ecology-assistant
powershell -ExecutionPolicy Bypass -File .reasonix\setup-migrate.ps1
```

Restart Reasonix — everything is ready.

### Say This, Get That

| Say this | What happens |
|:---------|:-------------|
| `"Research Yangtze fishing ban effects on fish — run full pipeline"` | 5 stages: plan → search → analyze → write → review (bilingual EN/CN, auto emergence signals) |
| `"Verify handbook chapter 2.2"` | Auto-check CRAN versions, compare with handbook, calculate next review date |
| `"Search my ima knowledge bases for stable isotope niche"` | Auto-route to correct KBs, parallel search, synthesize results |
| `"Help me with a mixed effects model"` | R code + method selection + diagnostics, annotated "as of YYYY-MM recommended practice" |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 🧠 AI Subagents

### Research Pipeline (5-stage auto-orchestrated)

| # | Agent | Role | Dynamic Worldview Feature |
|:-:|:------|:-----|:--------------------------|
| 🎯 | `research-orchestrator` | **Scheduler** | Coordinates all 5 stages |
| ① | `research-planner` | 🧑‍💼 Plan | Bilingual EN/CN keywords, covers local + international lit |
| ② | `research-executor` | 🔍 Search | 5 engines parallel, annotates publication year |
| ③ | `research-analyst` | 📊 Analyze | **Consensus evolution timeline** + **emergence signal detection** |
| ④ | `research-writer` | ✍️ Write | **Calibrated language**, temporal anchoring, uncertainty markers |
| ⑤ | `research-reviewer` | ✅ Review | 4-dimension scoring, ≤3 revision rounds |

### Domain Specialists

| Agent | Does | Philosophical Feature |
|:------|:------|:----------------------|
| 📖 `paper-analyzer` | Deep paper analysis | **Timeline** (at publication → since → today) + **emergence signals** |
| 📊 `stats-assistant` | R code + method selection | Code annotated with version, method with verification date |
| 🔍 `stats-method-finder` | Search CRAN/journals | Marks "last verified" timestamp on methods |
| 🧠 `ima-smart-search` | Cross-KB intelligent search | Dynamic KB discovery, no hardcoded IDs |
| ✅ `verify-stats-handbook` | Validate handbook code | Auto-check CRAN versions, calculates review cycle from activity |
| 🔭 `frontier-tracker` | Track frontier labs | Time-sorted latest findings |
| 🎓 `phd-proposal-writer` | PhD proposal writing | Dynamic reference coverage, timeliness annotations |
| 📚 `zotero-assistant` | Query Zotero | — |
| 📝 `obsidian-assistant` | Read/write Obsidian | — |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 📡 MCP Services (16 Tools)

| Service | Engine | Best For |
|:--------|:-------|:---------|
| `tavily` | AI deep search | Broad web |
| `exa` | Semantic search | Meaning-aware search |
| `scholar` | Google Scholar | Academic papers |
| `article` | Article metadata | Full abstracts |
| `scholarly` | Multi-source | Cross-database search |
| `ima` | ima OpenAPI | **13 knowledge bases + notes (14 tools)** |
| `rplay` | R 4.6.0 | Morphometrics, isotopes, community ecology |
| `coderunner` | Sandbox | Multi-language execution |
| `echarts` | ECharts | Publication-ready charts |
| `ocr` | PaddleOCR | Chinese/English OCR |
| `ocr-fallback` | Tesseract.js | Offline OCR |
| `playwright` | Chromium | Web scraping |
| `git` | Git CLI | Version control |
| `github` | GitHub API | Repository management |
| `zotero` | SQLite | Zotero library query |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 📁 Project Structure

```
fish-ecology-assistant/
├── README.md                 ← English
├── README.zh.md              ← 中文
│
├── .reasonix/
│   ├── mcp-servers/          ← 16 MCP wrappers
│   │   └── ima-server.mjs   ← 14 tools (KB + notes + discovery + multi-search)
│   │
│   ├── skills/               ← 12 AI subagent playbooks
│   │   ├── ima-smart-search.md       ← Cross-KB intelligent search
│   │   ├── verify-stats-handbook.md  ← Auto CRAN version check
│   │   ├── paper-analyzer.md         ← Timeline + emergence detection
│   │   ├── research-analyst.md       ← Consensus evolution + emergence signals
│   │   ├── research-writer.md        ← Calibrated language
│   │   └── ... (7 more skills)
│   │
│   ├── handbooks/
│   │   ├── stats-methods.md   ← Stats handbook (version-tracked + review dates)
│   │   └── learning-guide.md  ← Learning path guide
│   │
│   └── setup-migrate.ps1     ← One-click setup script
│
└── research_output/          ← Generated reports
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

---

## 🤝 Human-AI Responsibility Boundary

> Execution is mine. Final judgment is yours.

AI does: search · analyze · generate · flag emergence · suggest revisions
Human does: judge truth · choose methods · set direction · own published results

Tools evolve. Algorithms improve. But **academic responsibility and research taste can never be outsourced.**
This system is an amplifier, not an author.

## 🌱 Panta Rhei · Everything Flows

> Heraclitus: No man ever steps in the same river twice.
>
> We say:
> Knowledge ages. But humanity will never stop asking.
> Yesterday's truth is today's foundation. Today's unknown is tomorrow's frontier.
> Our eyes never rest on what is already known.
> Our steps will reach the vast expanse where the stars gather.

This project is not a fixed toolset. It is a **living system**. Every component has built-in expiry awareness, version tracking, and emergence detection. As your research deepens, R packages update, and new methods emerge, it evolves with you.

**Last updated: 2026-06-05**
**Running on Reasonix Code · Powered by DeepSeek**

<p align=right>(<a href=#readme-top>back to top</a>)</p>
