<p align="center">
  🇨🇳 <a href="README.zh.md">中文</a>
</p>

<div align="center">
  <h1>🌊 Panta Rhei · Everything Flows</h1>
  <p><strong>Turn your coding agent into a PhD-level research team with a dynamic worldview and DeepSeek-grade engineering.</strong></p>
  <p>16 MCP tools · 12 AI subagents · 5 search engines · 13 knowledge bases</p>
</div>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square" alt="License"></a>
  <a href="#"><img src="https://img.shields.io/badge/Panta_Rhei-core-6366f1?style=flat-square" alt="Panta Rhei"></a>
  <a href="#"><img src="https://img.shields.io/badge/entropy_aware-efficient-22c55e?style=flat-square" alt="Entropy Aware"></a>
  <a href="#"><img src="https://img.shields.io/badge/MoE_routing-sparse-f59e0b?style=flat-square" alt="MoE Routing"></a>
  <a href="USERGUIDE.md"><img src="https://img.shields.io/badge/docs-guide-0ea5e9?style=flat-square" alt="Docs"></a>
</p>

---

## 🏛️ Philosophy + Engineering

This project is built on two pillars: **dynamic worldview** (what we know) and **sparse computation** (how we compute).

### 🌊 Panta Rhei — The World Is Dynamic

> The world is dynamic. Knowledge is provisional. Emergence is the norm.

Every output carries a timestamp. Every claim uses calibrated language. Every analysis checks for emergence signals. Nothing is treated as eternal truth.

### ⚡ DeepSeek Engineering — Efficiency Is Intelligence

> Energy is finite. Computation has a cost. Smarter algorithms beat bigger models.

Unlike brute-force parameter scaling, this project follows DeepSeek's engineering philosophy: **Mixture of Experts routing, sparse activation, entropy-budgeted computation**. Modules only fire when their activation condition is met — never compute what you don't need.

| Risk | Traditional Approach | Our Approach |
|:-----|:--------------------|:-------------|
| Stale knowledge | Run old code on new data | **Probabilistic stale score** P(stale) = w·freq + w·breaking + w·dep |
| Overconfidence | "Research shows X" | **Calibrated language**: "Smith (2022) found X, Jones (2024) added Y" |
| Ignoring signals | Dismiss outliers | **Emergence detection**: ≥3 independent sources → active tracking |
| Wasted compute | Full pipeline on every query | **MoE sparse activation**: modules fire only on explicit triggers |
| Frozen docs | Handbook never updated | **Differential verification**: only check what changed |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 🤔 What This Is

**Fish Ecology Assistant** transforms [Reasonix Code](https://github.com/esengine/deepseek-reasonix) into a domain-specialized fish ecology research team with 16 tools, 12 subagents, 5-engine search, R statistics, and 13 knowledge bases.

| Capability | Vanilla Reasonix | **With This Config** |
|:-----------|:----------------:|:--------------------:|
| Search engines | 1 | **5** (tavily, exa, scholar, article, scholarly) |
| MCP services | 0 | **16** |
| AI subagents | 4 (generic) | **12** (emergence-aware, calibrated language) |
| R statistics | — | ✅ R 4.6.0 + 20+ ecology packages |
| Knowledge bases | — | ✅ 13 ima KBs (dynamic discovery, MoE routing) |
| Verification | — | ✅ Probabilistic stale scoring + differential checks |
| Setup | Manual | ✅ One script, 5 minutes |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## ⚡ Quick Start

```bash
git clone https://github.com/fangtaocai041/fish-ecology-assistant.git
cd fish-ecology-assistant
powershell -ExecutionPolicy Bypass -File .reasonix\setup-migrate.ps1
```

### Say This, Get That

| Say this | What happens | Budget used |
|:---------|:-------------|:------------|
| `"Research Yangtze fishing ban — run pipeline"` | 5 stages with emergence detection | Full |
| `"Verify handbook 2.2"` | Auto-check CRAN, probabilistic stale score, differential verification | Medium |
| `"Search ima for stable isotope niche"` | IG-keyword routing, cross-KB dedup, MoE activation | Light |
| `"Quick question: NMDS stress value threshold?"` | Single-stage lookup, no heavy compute | Minimal |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 🧠 Skills (Subagents)

### Research Pipeline — Sparse Activation

| # | Agent | Activation Condition |
|:-:|:------|:---------------------|
| ① | `research-planner` | **Always** (lightweight routing) |
| ② | `research-executor` | Planner returns ≥1 query |
| ③ | `research-analyst` | Executor returns ≥1 result |
| ④ | `research-writer` | Analyst returns ≥1 finding |
| ⑤ | `research-reviewer` | Writer output ≥500 words |

### Domain Specialists

| Agent | Trigger |
|:------|:--------|
| 📖 `paper-analyzer` | Paper DOI or abstract provided |
| 📊 `stats-assistant` | Code/methods/packages involved |
| 🔍 `stats-method-finder` | Unfamiliar method requested |
| 🧠 `ima-smart-search` | Domain maps to ≥1 ima KB |
| ✅ `verify-stats-handbook` | Handbook chapter explicitly requested |
| 🔭 `frontier-tracker` | Lab tracking explicitly requested |
| 🎓 `phd-proposal-writer` | PhD proposal explicitly requested |
| 📚 `zotero-assistant` | Zotero query involved |
| 📝 `obsidian-assistant` | Obsidian write/read involved |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 📡 MCP Services (16 Tools)

| Service | Engine | Best For |
|:--------|:-------|:---------|
| `tavily` / `exa` / `scholar` / `article` / `scholarly` | Multi-engine search | 5-source parallel |
| `ima` | ima OpenAPI | 13 KBs, IG-keyword routing, MoE discovery |
| `rplay` | R 4.6.0 | Morphometrics, isotopes, community ecology |
| `coderunner` | Sandbox | Multi-language execution |
| `echarts` / `ocr` / `ocr-fallback` / `playwright` | Viz + extraction | Charts, OCR, scraping |
| `git` / `github` | Version control | Repo management |
| `zotero` | SQLite | Reference library |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 📁 Project Structure

```
fish-ecology-assistant/
├── README.md · README.zh.md
├── .reasonix/
│   ├── mcp-servers/          ← 16 MCP wrappers
│   │   └── ima-server.mjs   ← 14 tools (KB + MoE discovery + IG routing)
│   ├── skills/               ← 12 AI subagents
│   │   ├── karpathy-guard.md        ← Entropy Budget + Panta Rhei
│   │   ├── research-orchestrator.md ← Sparse activation scheduler
│   │   ├── verify-stats-handbook.md ← P(stale) scoring + differential verification
│   │   ├── ima-smart-search.md      ← IG keyword optimization + dedup
│   │   └── ... (8 more)
│   ├── handbooks/
│   │   ├── stats-methods.md   ← Version-tracked R templates
│   │   └── learning-guide.md  ← Learning paths
│   └── setup-migrate.ps1     ← One-click setup
└── research_output/
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 🌱 Panta Rhei · Powered by DeepSeek

> Heraclitus: No man ever steps in the same river twice.
> DeepSeek: Smarter algorithms beat bigger models.

**Last updated: 2026-06-05**
**Runtime: Reasonix Code · Powered by DeepSeek**

<p align="right">(<a href="#readme-top">back to top</a>)</p>
