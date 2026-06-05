<p align="center">
  🇨🇳 <a href="README.zh.md">中文</a>
</p>

<p align="center">
  <em>"No man ever steps in the same river twice."</em> — Heraclitus
</p>

<div align="center">
  <h1>🌊 Everything Flows · Panta Rhei</h1>
  <p><strong>Turn your coding agent into a PhD-level research team with a dynamic worldview.</strong></p>
  <p>16 MCP tools · 12 AI subagents · 5 search engines · 13 knowledge bases</p>
</div>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square" alt="License"></a>
  <a href="#"><img src="https://img.shields.io/badge/Panta_Rhei-core-6366f1?style=flat-square" alt="Panta Rhei"></a>
  <a href="#"><img src="https://img.shields.io/badge/MCP-16-22c55e?style=flat-square" alt="MCP:16"></a>
  <a href="#"><img src="https://img.shields.io/badge/subagents-12-f59e0b?style=flat-square" alt="Subagents:12"></a>
</p>

---

## 🏛️ Core Philosophy

> **The world is dynamic. Knowledge is provisional. Emergence is the norm.**

This is the operating system that runs through every line of code, every search query, every paper analysis.

The purpose of research is not to accumulate knowledge — it is to **understand the world, ask better questions, and in doing so, change it.** Knowledge is only the footprint. The question is the path.

### Three Tenets

**🌍 The World Is Dynamic**
R packages update. Species distributions shift. Scientific consensus evolves. A correct conclusion today may be obsolete in six months. We treat no knowledge as eternal truth — everything is anchored on a timeline.

**📖 Knowledge Is Provisional**
The bedrock of science is falsifiability (Popper). No finding is final — only "the best current explanation." We use **calibrated language**: say "evidence suggests" not "proves," say "Smith (2022) found" not "studies show." Every output carries a timestamp.

**🔬 Emergence Is the Norm**
Life, consciousness, ecosystems, AI reasoning — all are **emergent** phenomena. Analyzing parts in isolation never reveals the whole. When ≥3 independent sources point to the same unexpected pattern, the system flags it as an **emergence signal** — not dismisses it as noise.

### Why This Matters

| Risk | Traditional Approach | Dynamic Worldview |
|:-----|:--------------------|:------------------|
| Stale knowledge | Run 2020 code on 2026 data | Auto-check CRAN, mark "verified on glmmTMB v1.1.10" |
| Overconfidence | "Research shows X" | "Smith (2022) found X; Jones (2024) added Y" |
| Ignoring signals | Dismiss outliers | ≥3 independent sources → emergence signal, actively tracked |
| Frozen docs | Handbook never updated | Verification log with dynamic review dates |

---

## 🤔 What This Is

**Fish Ecology Assistant** transforms [Reasonix Code](https://github.com/esengine/deepseek-reasonix) into a domain-specialized fish ecology research team. 16 tools, 12 subagents, 5-engine search, 5-stage pipeline, R statistics — all governed by the dynamic worldview.

| Capability | Before | **After** |
|:-----------|:------:|:---------:|
| Search engines | 1 | **5** |
| MCP services | 0 | **16** |
| AI subagents | 4 generic | **12** (emergence-aware) |
| R statistics | — | ✅ 20+ ecology packages |
| Reference manager | — | ✅ Direct Zotero |
| Research pipeline | — | ✅ 5-stage + emergence detection |
| Knowledge bases | — | ✅ 13 ima KBs |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## ⚡ Quick Start

```bash
git clone https://github.com/fangtaocai041/fish-ecology-assistant.git
cd fish-ecology-assistant
powershell -ExecutionPolicy Bypass -File .reasonix\setup-migrate.ps1
```

### You Say, It Does

| You say | It does |
|:--------|:--------|
| `"Research Yangtze fishing ban effects — run pipeline"` | 5 stages: plan → search → analyze → write → review (bilingual, emergence detection) |
| `"Verify handbook 2.2"` | Auto-check CRAN, probabilistic stale scoring, differential verification |
| `"Search ima KBs for stable isotope niche"` | Auto-route, multi-KB parallel, IG-keyword ordering |
| `"Help me with a mixed effects model"` | R code + method selection + diagnostics, version-annotated |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 🧠 AI Subagents

### Research Pipeline (5-stage · Sparse Activation)

| # | Agent | Role | Dynamic Worldview Feature |
|:-:|:------|:-----|:--------------------------|
| ① | `research-planner` | 🧑‍💼 Plan | Bilingual EN/CN keywords |
| ② | `research-executor` | 🔍 Search | 5 engines, annotated publication years |
| ③ | `research-analyst` | 📊 Analyze | **Consensus timeline** + **emergence detection** |
| ④ | `research-writer` | ✍️ Write | **Calibrated language**, temporal anchoring |
| ⑤ | `research-reviewer` | ✅ Review | 4-dimension scoring, ≤3 rounds |

### Domain Specialists

| Agent | Does | Philosophical Feature |
|:------|:------|:----------------------|
| 📖 `paper-analyzer` | Deep paper analysis | Timeline (at publication → since → today) + emergence |
| 📊 `stats-assistant` | R code + method selection | Version-annotated, verification-dated |
| 🔍 `stats-method-finder` | Search CRAN/journals | Timestamped methods |
| 🧠 `ima-smart-search` | Cross-13-KB intelligent search | Dynamic discovery, IG routing |
| ✅ `verify-stats-handbook` | Validate handbook code | Auto CRAN check, probabilistic stale scoring |
| 🔭 `frontier-tracker` | Track 15+ frontier labs | Time-sorted findings |
| 🎓 `phd-proposal-writer` | PhD proposal | Dynamic reference coverage |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 📡 MCP Services (16 Tools)

| Service | Best For |
|:--------|:---------|
| `tavily` · `exa` · `scholar` · `article` · `scholarly` | 5-engine parallel search |
| `ima` | 13 knowledge bases + notes (14 tools) |
| `rplay` · `coderunner` | R statistics + sandbox execution |
| `echarts` · `ocr` · `ocr-fallback` · `playwright` | Charts, OCR, scraping |
| `git` · `github` · `zotero` | Version control + reference library |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## ⚡ Engineering Principles

Philosophy is the soul. Engineering is the body. DeepSeek taught us: **energy is finite — smarter algorithms beat brute force.**

| Principle | Application |
|:----------|:------------|
| **Entropy budget** | PhD thesis → full pipeline. Quick question → single-step. Don't waste compute |
| **Sparse activation** | Planner always runs. Executor only with queries. Analyst only with results. No idle fire |
| **Differential update** | Verify only changed packages, not the entire handbook |
| **Information gain** | P0 exact terms first, stop on hit. P2 redundant terms skip |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 📁 Project Structure

```
fish-ecology-assistant/
├── README.md · README.zh.md
├── .reasonix/
│   ├── mcp-servers/    ← 16 MCP wrappers
│   ├── skills/         ← 12 AI subagent playbooks
│   ├── handbooks/      ← Stats handbook + learning guide
│   └── setup-migrate.ps1
└── research_output/
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 🌱

> Heraclitus: No man ever steps in the same river twice.
>
> We say: You can't analyze today's ecological data with last month's R packages.
>
> Understand the world. Ask better questions. Change it.
>
> No answer lasts forever. But a good question can.

**Everything flows. Nothing stands still. The sun is new each day.**

<p align="right">— Heraclitus, ~500 BCE</p>

---

<sub>Built with Reasonix Code · Powered by DeepSeek · 2026</sub>
