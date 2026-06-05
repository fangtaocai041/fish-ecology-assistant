<p align="center">
  🇨🇳 <a href="README.zh.md">中文</a>
</p>

<p align="center">
  <em>"We both step and do not step into the same rivers."</em><br>
  <sub>Heraclitus, Fragment B49a · ~500 BCE</sub>
</p>

<div align="center">
  <h1>🌊 Panta Rhei</h1>
  <p><strong>Your coding agent, with a sense of time.</strong></p>
  <p>16 MCP tools &nbsp;·&nbsp; 12 subagents &nbsp;·&nbsp; 5 engines &nbsp;·&nbsp; 13 knowledge bases</p>
</div>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue?style=flat-square" alt="License"></a>
  <a href="#"><img src="https://img.shields.io/badge/panta_rhei-6366f1?style=flat-square" alt="Panta Rhei"></a>
  <a href="#"><img src="https://img.shields.io/badge/tools-16-22c55e?style=flat-square" alt="16 tools"></a>
  <a href="#"><img src="https://img.shields.io/badge/agents-12-f59e0b?style=flat-square" alt="12 agents"></a>
</p>

---

## Philosophy

> The world is dynamic. Knowledge is provisional. Emergence is the norm.

Research is not about collecting answers. It is about **seeing the world as it is, asking what hasn't been asked, and changing what can be changed.** Knowledge is the footprint. The question is the path.

**The world moves.**
R packages update. Species ranges shift. Scientific consensus evolves. A correct answer today may be wrong in six months. We anchor everything to time — no conclusion treated as final.

**Knowledge is provisional.**
Falsifiability is the bedrock of science. Every finding is only "the best current explanation." We use calibrated language: "evidence suggests" not "proves." "Smith (2022) found" not "studies show." Every output carries a timestamp.

**Emergence is everywhere.**
Life, consciousness, ecosystems — none can be understood by analyzing parts alone. When three or more independent sources converge on an unexpected pattern, we flag it as an **emergence signal**. Not noise. A message.

| Without this | With this |
|:-------------|:----------|
| Run 2020 code on 2026 data | Auto-check CRAN, mark "verified on glmmTMB v1.1.10" |
| "Research shows X" | "Smith (2022) found X; Jones (2024) added Y" |
| Dismiss outliers as noise | ≥3 independent sources → actively tracked |
| Frozen documentation | Dynamic review dates, probabilistic stale scoring |

---

## What This Is

**Fish Ecology Assistant** — a configuration that turns a general-purpose coding agent into a fish ecology research team governed by the principles above.

| | Before | After |
|:--|:-----:|:-----:|
| Search engines | 1 | **5** |
| MCP services | 0 | **16** |
| AI subagents | 4 generic | **12** (emergence-aware) |
| R statistics | — | 20+ ecology packages |
| Knowledge bases | — | 13 ima KBs, dynamic discovery |

---

## Quick Start

```bash
git clone https://github.com/fangtaocai041/fish-ecology-assistant.git
cd fish-ecology-assistant
powershell -ExecutionPolicy Bypass -File .reasonix\setup-migrate.ps1
```

| You say | It does |
|:--------|:--------|
| `Research Yangtze fishing ban — run pipeline` | 5 stages · plan → search → analyze → write → review · bilingual · emergence-aware |
| `Verify handbook chapter 2.2` | Auto-check CRAN · probabilistic stale scoring · differential verification |
| `Search ima for stable isotope niche` | Auto-route to correct KBs · multi-KB parallel · IG-keyword ordering |
| `Help me with a mixed effects model` | R code · method selection · diagnostics · version-annotated |

---

## Subagents

| Agent | Does | Activates |
|:------|:-----|:----------|
| 🎯 Research Pipeline (×5) | Plan → Search → Analyze → Write → Review | Stage-by-stage trigger |
| 📖 Paper Analyzer | Timeline analysis + emergence signals | DOI or abstract given |
| 📊 Stats Assistant | R code + method selection | Code or methods involved |
| 🔍 Method Finder | Search CRAN, journals, textbooks | Unfamiliar method requested |
| 🧠 ima Smart Search | Cross-13-KB intelligent search | Domain maps to ≥1 KB |
| ✅ Handbook Verifier | Auto CRAN check + stale scoring | Explicitly requested |
| 🎓 Proposal Writer | PhD research proposal | Explicitly requested |

---

## Tools

| Category | Services |
|:---------|:---------|
| Search | `tavily` · `exa` · `scholar` · `article` · `scholarly` |
| Knowledge | `ima` (13 KBs · 14 tools · MoE routing) |
| Compute | `rplay` (R 4.6.0) · `coderunner` |
| Visual | `echarts` · `ocr` · `ocr-fallback` · `playwright` |
| System | `git` · `github` · `zotero` |

---

## How It Works

Philosophy is the soul. Engineering is the body. **Energy is finite — smarter algorithms beat brute force.**

**Entropy budget** — PhD topic: full pipeline. Quick question: single step. No wasted compute.

**Sparse activation** — Planner always runs. Executor only with search queries. Analyst only with results. Writer only with findings. Modules don't idle.

**Differential verification** — Only check packages that actually changed since last review.

**Information gain routing** — P0 exact terms first. Stop on hit. P2 redundant terms skip.

---

## Structure

```
fish-ecology-assistant/
├── README.md · README.zh.md
├── .reasonix/
│   ├── mcp-servers/    ← 16 wrappers
│   ├── skills/         ← 12 subagent playbooks
│   ├── handbooks/      ← stats + learning
│   ├── readme-versions/ ← all historical READMEs
│   └── setup-migrate.ps1
└── research_output/
```

---

<p align="center">
  <em>"The sun is new each day."</em> — Heraclitus, Fragment B6<br>
  <em>"Upon those who step into the same rivers, different and again different waters flow."</em> — Fragment B12<br>
  <br>
  Understand the world. Ask what hasn't been asked. Change what can be changed.<br>
  No answer lasts forever. But a good question can.
</p>

<p align="center">
  <sub>Built with Reasonix Code · Powered by DeepSeek · 2026</sub>
</p>
