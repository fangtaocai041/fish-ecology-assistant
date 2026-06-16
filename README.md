# Fish Ecology Assistant 🐟

> Everything Flows · Panta Rhei
>
> Turn your coding agent into a PhD-level research team
> with a dynamic worldview.
>
> **16 MCP Tools · 12 AI Sub-agents · 5 Search Engines · 13 Knowledge Bases**

[中文版](README.zh.md) · [Changelog](CHANGELOG.md) · [Engineering Record](RE.md)

---

## Core Philosophy

> The world is dynamic. Knowledge is temporary. Emergence is the norm.

This is not a slogan. It is the operating system running through every line of code, every search, and every analysis in this project.

### Three Tenets

**The world is dynamic** — R packages update, species distributions shift, scientific consensus evolves, climate change reshapes ecosystems. A correct conclusion today may be outdated in six months. We treat no knowledge as eternal truth, but place it on a timeline and view it dynamically.

**Knowledge is temporary** — The foundation of science is falsification (Popper). No discovery is ultimate truth—only the "best current explanation." We use calibrated language: "evidence suggests" not "proves," "Smith (2022) found" not "studies show." Every output carries a temporal anchor.

**Emergence is the norm** — Life, consciousness, ecosystems, AI reasoning—all are emergent phenomena. You cannot assemble the whole by analyzing only the parts. When ≥3 independent sources point to the same unexpected pattern, the system flags it as an emergence signal—not dismisses it as noise.

### Why This Matters for Research

| Scenario | Traditional Approach | Dynamic Worldview Approach |
|:---------|:--------------------|:--------------------------|
| Package versions | "It runs" | Auto-check, tag "Last verified on glmmTMB v1.1.10" |
| Citations | "Studies prove X" | "Smith (2022) found X, but Jones (2024) added Y" |
| Outliers | Ignore as noise | ≥3 sources → emergence signal, actively track |
| Knowledge decay | "It's written down" | Verification record includes "Next review: 2026-12" |
| Method choice | Fixed pipeline | Dynamic method selection, dynamic confidence |

---

## What This Is

**Fish Ecology Assistant** is a complete configuration package that transforms Reasonix Code from a general-purpose coding assistant into a professional fish ecology research team.

It integrates **16 MCP tools**, **12 domain-specific AI sub-agents**, **5-engine parallel search**, an automated **5-stage research pipeline**, and an **R statistical computing environment**—all outputs guided by the dynamic worldview above.

### Capability Matrix

| Capability | This Config | Vanilla Reasonix |
|:-----------|:------------|:-----------------|
| Search | 5 engines (tavily, exa, google-scholar, article, scholarly) | 1 (web_search) |
| AI Sub-agents | 12 (domain-specific, incl. emergence detection) | 4 (general) |
| R Statistics | R 4.6.0 + 20+ ecology packages | — |
| OCR | PaddleOCR + Tesseract.js | — |
| References | Direct Zotero query | — |
| Writing | 5-stage + auto-review + emergence detection | — |
| Knowledge Bases | 13 IMA knowledge bases | — |
| Setup | One script, 5 minutes | — |

---

## Quick Start

```bash
git clone https://github.com/fangtaocai041/fish-ecology-assistant
cd fish-ecology-assistant
powershell -ExecutionPolicy Bypass -File setup.ps1
```

Restart Reasonix. You speak, it does.

| You Say | It Does |
|:--------|:--------|
| "Research the impact of Yangtze fishing ban on fish communities, run pipeline" | 5-stage: Plan → Search → Analyze → Write → Review (bilingual search, auto emergence detection) |
| "Verify handbook chapter 2.2" | Auto-check CRAN package versions, diff against handbook, compute review date |
| "Search for Ochetobius elongatus literature" | Route to correct knowledge bases, parallel search, synthesize results |
| "Run a stable isotope analysis" | R code + method selection + diagnostics, tagged with YYYY-MM best practice |

---

## AI Sub-agents

### Research Pipeline (5-stage auto-orchestration · Dynamic worldview throughout)

| Agent | Role | Function | Philosophical Anchor |
|:------|:-----|:---------|:---------------------|
| **research-orchestrator** | 🎯 Director | Orchestrates all 5 stages | — |
| **research-planner** | 📋 Planner | Generates keywords, decomposes problems | Full coverage CN + EN |
| **research-executor** | 🔍 Searcher | 5-engine parallel, annotates publication year | Timeline-aware |
| **research-analyst** | 🧠 Analyst | Consensus timeline + emergence detection | Dynamic consensus · emergence |
| **research-writer** | ✍️ Writer | Calibrated language, temporal anchoring, uncertainty marking | Calibrated language · provisional knowledge |
| **research-reviewer** | ✅ Reviewer | 4-dimension scoring, up to 3 revision rounds | Quality闭环 |

### Domain Expert Agents

| Agent | Function | Philosophical Anchor |
|:------|:---------|:---------------------|
| **paper-analyzer** | Deep single-paper analysis | Timeline · emergence signals |
| **stats-assistant** | R code + method selection | Version tagging · method verification dates |
| **stats-method-finder** | Search CRAN/journals for methods | "Last verified" timestamps |
| **ima-smart-search** | Cross-knowledge-base search | Dynamic discovery, no hardcoded expiration |
| **verify-stats-handbook** | Auto-check CRAN versions | Review cycles based on activity |
| **frontier-tracker** | Chronological latest discoveries | Never out of date |
| **phd-proposal-writer** | PhD proposal generation | Timeliness annotations |
| **zotero-assistant** | Zotero library queries | — |
| **obsidian-assistant** | Obsidian note export | — |

---

## MCP Services (16 Tools)

| Service | Purpose |
|:--------|:--------|
| **tavily** | AI deep search |
| **exa** | Semantic search |
| **google-scholar** | Academic papers |
| **article** | Literature metadata |
| **scholarly** | Multi-source aggregation |
| **ima** | 13 knowledge bases + OpenAPI tools |
| **rplay** | R 4.6.0 (morphometrics, isotopes, community ecology) |
| **coderunner** | Multi-language sandbox execution |
| **echarts** | ECharts visualization |
| **PaddleOCR** | Chinese OCR |
| **Tesseract.js** | OCR fallback |
| **playwright** | Chromium screenshot/scrape |
| **git** | Git CLI |
| **github** | GitHub API |
| **Zotero** | SQLite reference library |

---

> Everything Flows · Panta Rhei
>
> Heraclitus said: No man ever steps in the same river twice.
>
> We say: You can't analyze today's ecological data with last month's code.
>
> This project is not a fixed toolset—it is a living system. Every component has built-in expiration mechanisms, version tracking, and emergence awareness. As your research deepens, R packages update, and new methods emerge, it evolves with you.
>
> **Last updated: 2026-06-04 · Environment: Reasonix Code · Powered by DeepSeek**
