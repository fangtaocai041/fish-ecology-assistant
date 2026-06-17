![Python 3.10+](https://img.shields.io/badge/Python%203.10%2B-3776AB?style=flat-square)
  ![MIT](https://img.shields.io/badge/MIT-34D058?style=flat-square)
  ![v6.5.0](https://img.shields.io/badge/v6.5.0-8A4FCE?style=flat-square)
  ![430 species](https://img.shields.io/badge/430%20species-007EC6?style=flat-square)
  ![289 traits](https://img.shields.io/badge/289%20traits-FE7D37?style=flat-square)
  ![21 MCP](https://img.shields.io/badge/21%20MCP-0EA5E9?style=flat-square)
  ![28 skills](https://img.shields.io/badge/28%20skills-D73A4A?style=flat-square)
  ![12 engines](https://img.shields.io/badge/12%20engines-EC4899?style=flat-square)
  ![13 KBs](https://img.shields.io/badge/13%20KBs-F59E0B?style=flat-square)
  ![CN-EN](https://img.shields.io/badge/CN-EN-6B7280?style=flat-square)
</p>

[English](README.md) · [中文](README.zh.md)

<div align="center"><h3>🌊 Everything flows.</h3></div>

The world is dynamic, knowledge is temporary, emergence is the norm.

---

## 📖 Table of Contents

- [Philosophy](#-philosophy)
- [Quick Start](#-quick-start)
- [Architecture](#-architecture)
- [Features](#-features)
- [Skills](#-skills)
- [MCP Tools](#-mcp-tools)
- [Project Structure](#-project-structure)
- [Version History](#-version-history)
- [Self-Assessment](#-self-assessment)
- [Ecosystem](#-ecosystem)

---

## 🎯 Core Philosophy

> 🌍 The world is dynamic. 📖 Knowledge is temporary. 🌟 Emergence is the norm.

This is not a slogan. It is the operating system running through every line of code, every search, and every analysis in this project.

### 📜 Three Tenets

**🌍 The world is dynamic** — R packages update, species distributions shift, scientific consensus evolves, climate change reshapes ecosystems. A correct conclusion today may be outdated in six months. We treat no knowledge as eternal truth, but place it on a timeline and view it dynamically.

**📖 Knowledge is temporary** — The foundation of science is falsification (Popper). No discovery is ultimate truth—only the "best current explanation." We use calibrated language: "evidence suggests" not "proves," "Smith (2022) found" not "studies show." Every output carries a temporal anchor.

**🌟 Emergence is the norm** — Life, consciousness, ecosystems, AI reasoning—all are emergent phenomena. You cannot assemble the whole by analyzing only the parts. When ≥3 independent sources point to the same unexpected pattern, the system flags it as an emergence signal—not dismisses it as noise.

### ⚖️ Why This Matters for Research

| 🎯 Scenario | ❌ Traditional | ✅ Dynamic Worldview |
|:------------|:--------------|:--------------------|
| 📦 Package versions | Run 2020 code, ignore version drift | Auto-check, tag "Last verified on glmmTMB v1.1.10" |
| 📝 Citations | "Studies prove it" | "Smith (2022) found X, but Jones (2024) added Y" |
| 📊 Outliers | Ignore as noise | ≥3 sources → emergence signal, actively track |
| ⏰ Knowledge decay | Handbook frozen, never updated | Review records include "Next review date," computed by package activity |
| 🔧 Method selection | Fixed pipeline forever | Dynamic method selection, dynamic confidence |

> 道生一，一生二，二生三，三生万物。

From One comes Two, from Two comes Three, from Three come all things.

---

## 🧩 What This Is

**Fish Ecology Assistant** is a complete configuration package that transforms Reasonix Code from a general-purpose coding assistant into a professional fish ecology research team. It is the **Knowledge Supply Core (S/V0)** in the SanShengWanWu S-T-V-P₁-P₂ five-body architecture, coordinated by **eon-core**.

It integrates **21 MCP tools**, **28 domain-specific skills**, **12-engine parallel search**, an automated **5-stage research pipeline**, **13 IMA knowledge bases**, and an **R statistical computing environment**—all outputs guided by the dynamic worldview above.

### 📊 Capability Matrix

| 🚀 Capability | ✨ With This Config | 💭 Vanilla Reasonix |
|:--------------|:-------------------|:-------------------|
| 🔍 Search | 12 engines (tavily, exa, scholar, article, scholarly, baidu_scholar, cnki, wanfang, cas, ncbi, ima, deepwiki) | 1 (web_search) |
| 🤖 AI Skills | 28 (6 pipeline + 20 domain + 2 guard) | 4 (general) |
| 📊 R Statistics | R 4.6.0 + 20+ ecology packages | — |
| 👁️ OCR | PaddleOCR + Tesseract.js fallback | — |
| 📚 References | Direct Zotero SQLite query | — |
| ✍️ Writing | 5-stage + auto-review + emergence detection | — |
| 🏛️ Knowledge Bases | 13 IMA knowledge bases | — |
| ⚡ Setup | One script, 5 minutes | — |

---

## 🚀 Quick Start

```bash
# Clone
git clone git@github.com:fangtaocai041/fish-ecology-assistant.git
cd fish-ecology-assistant

# Install
pip install -e .

# Run
python src/main.py search --species "Coilia nasus"
```

---

## 🏗️ Architecture

### S-T-V-P₁-P₂ Five-Body Architecture

```
S-T-V-P₁-P₂ (SanShengWanWu)
  │
  ├── S/V0  fish-ecology-assistant    ← Knowledge Supply (this project)
  │         Panta Rhei + Systems Theory worldview
  │         430 species, 289 traits, KB-First search
  │
  ├── T     (future: Theory Engine)
  │
  ├── V/V1  cognitive-search-engine   → Search Verification
  │         12 engines, validator.py, evolution_executor
  │
  ├── Coord  eon-core                  → Coordination Hub
  │         EventBus, DAG routing, CAS core
  │
  ├── P₁    porpoise-agent            → Porpoise Expert (derived)
  └── P₂    coilia-agent              → Coilia Expert (derived)
```

### 5-Layer Internal Architecture

```
fish-ecology-assistant/
  src/           Core Python engine
  ├── adapter.py            IProjectAdapter (V0 canonical) + score() method
  ├── orchestrator.py       KB-first species search coordinator
  ├── project_hub.py        Cross-project coordination (eon-core bridge)
  ├── dao_engine.py         Philosophical chain executor (Panta Rhei → Dao)
  ├── types.py              8 dataclasses + 4 enums
  └── kalman_emergence.py   Kalman Filter emergence detection
  fishkb/         Independent reusable fish knowledge base (pip install fishkb)
  ├── fishkb/db.py           KnowledgeDB — SQLite FTS5 knowledge base
  ├── fishkb/search.py       FishSpeciesMatcher — KB-First species matching
  ├── fishkb/credibility.py  Paper credibility scoring
  └── fishkb/types.py        Core data types
  config/
  ├── agent.yaml             Agent orchestration config
  ├── mcp_servers.yaml       21 MCP server definitions
  ├── coordination.yaml      Cross-project coordination
  ├── evolution.yaml         Self-evolution parameters
  ├── component_registry.yaml Living system component registry
  ├── knowledge_base/        30 species .md profiles
  └── fish_species_kb.yaml   430 species index
  data/
  ├── species.db             SQLite (species + traits + literature)
  ├── FISHMORPH.csv          2.3MB global morphology database
  └── reports/               HTML/CSV exports
  scripts/
  ├── fishbase_pull.py       FishBase API auto-sync
  ├── trait_network.py       Network Science trait analysis
  └── gen_report.py          Bilingual HTML report generator
```

### Research Pipeline (5 Stages)

```
Planner → Executor → Analyst → Writer → Reviewer
   ↑                                       │
   └─────────── feedback loop ─────────────┘
```

All stages coordinated by **eon-core** via `project_hub.py` and `coordination.yaml`.

---

## ✨ Features

| Feature | Status | Description |
|---------|:------:|-------------|
| 🗃️ 430 Species DB | ✅ | Yangtze fish species with bilingual conservation |
| 📏 289 Morphology | ✅ | FISHMORPH (251) + FishBase + FAO + manual |
| 🌊 Population-level | ✅ | 26 records with water-body annotation |
| 🔬 Trait Catalog | ✅ | 61 traits in 7 categories |
| 🏛️ Conservation | ✅ | IUCN + China Red List + National + CITES |
| 📊 Excel/HTML | ✅ | Bilingual reports, 2-level headers |
| 🔗 KB-First Search | ✅ | SQLite FTS5, zero-network for 30 core species |
| 🕸️ Trait Network | ✅ | Jaccard co-occurrence, keystone traits |
| 📡 Kalman Filter | ✅ | Emergence detection from noisy data |
| 🔄 Self-Evolution | ✅ | 7 triggers auto-adapt parameters |
| 📦 fishkb Sub-library | ✅ | Independent pip-installable core (KnowledgeDB + Matcher) |
| 🎯 score() Adapter | ✅ | IProjectAdapter.score() for cross-project quality scoring |
| 🔄 FishBase Sync | 🟡 | Script ready, SSL blocked in env |
| 🧪 Living System | ✅ | Component registry with expiry policies |

---

## 🎯 Skills

### Pipeline Skills (6)

| Skill | Description |
|-------|-------------|
| `research-orchestrator` | Top-level pipeline coordinator |
| `research-planner` | Research question decomposition + strategy |
| `research-executor` | Multi-engine parallel literature search |
| `research-analyst` | Statistical analysis + data interpretation |
| `research-writer` | Bilingual report generation |
| `research-reviewer` | Quality review + contradiction detection |

### Domain Skills (20)

| Skill | Description |
|-------|-------------|
| `academic-species-search` | Multi-source species academic search |
| `cognitive-species-search` | Cognitive graph species search |
| `unified-species-search` | Unified species search across all engines |
| `fuzzy-species-search` | Fuzzy name matching + OCR variants |
| `google-scholar-search` | Google Scholar targeted search |
| `lit-search` | Comprehensive literature search |
| `frontier-tracker` | Research frontier monitoring |
| `paper-analyzer` | Deep paper analysis |
| `stats-assistant` | R statistical computing assistant |
| `stats-method-finder` | Statistical method recommendation |
| `verify-stats-handbook` | Handbook verification against current stats |
| `phd-proposal-writer` | PhD proposal drafting |
| `ima-smart-search` | IMA knowledge base smart search |
| `zotero-assistant` | Zotero reference management |
| `obsidian-assistant` | Obsidian vault integration |
| `component-health-check` | Living system health monitoring |
| `living-system-dashboard` | Real-time system status dashboard |
| `debate-validator` | Multi-perspective debate validation |
| `self-evolve` | Autonomous parameter evolution |
| `rule-auditor` | Research rule compliance audit |

### Guard Skills (2)

| Skill | Description |
|-------|-------------|
| `karpathy-guard` | Code quality + safety guard |
| `rule-auditor` | Cross-project rule compliance check |

---

## 🔌 MCP Tools (21)

| Category | Tool | Description |
|----------|------|-------------|
| **Search** | `cognitive_search` | Cognitive graph search engine (primary) |
| | `scholar` | Google Scholar literature search |
| | `article` | PMC full-text + journal quality (EasyScholar/OpenAlex) |
| | `scholarly` | Multi-source academic cross-database search |
| | `baidu_scholar` | Baidu Scholar Chinese academic search |
| | `cnki` | CNKI Chinese journal database |
| | `wanfang` | Wanfang Chinese academic database |
| | `cas` | CAS (Chinese Academy of Sciences) literature |
| | `ncbi` | NCBI PubMed + Europe PMC |
| | `tavily` | AI-powered deep web search |
| | `exa` | Semantic web search |
| | `ima` | IMA knowledge base search |
| **Compute** | `rplay` | R 4.6.0 statistical computing |
| | `coderunner` | Multi-language code sandbox |
| | `echarts` | Publication-ready chart generation |
| **Image** | `ocr` | PaddleOCR (Chinese/English tables + formulas) |
| | `ocr_fallback` | Tesseract.js offline OCR |
| | `playwright` | Browser automation + scraping |
| **Data** | `git` | Git version control |
| | `github` | GitHub API (repos, issues, PRs) |
| **Knowledge** | `zotero` | Zotero SQLite direct query |
| | `obsidian` | Obsidian vault read/write |

---

## 📁 Project Structure

```
fish-ecology-assistant/
  (see Architecture section above)
```

---

## 📜 Version History

| Version | Date | Highlights |
|---------|------|------------|
| **v6.5.0** | 2026-06-17 | KB-First search strategy, 21 MCP integration, living system component registry |
| v6.4.0 | 2026-06-12 | ProjectHub cross-project coordination, eon-core bridge |
| v6.3.0 | 2026-06-09 | Self-evolution engine (7 triggers), evolution.yaml |
| v6.2.0 | 2026-06-07 | Cross-project evolution propagation, component_registry.yaml |
| v6.1.0 | 2026-06-06 | 28 skills (6 pipeline + 20 domain + 2 guard), rule-auditor |
| v6.0.0 | 2026-06-05 | S-T-V-P₁-P₂ five-body architecture, coordination.yaml |
| v5.0.0 | 2026-06-01 | 5-stage pipeline, fishkb sub-library, 430 species |

---

## 🪞 Self-Assessment

### Strengths
- **Species coverage**: 430 Yangtze fish species with bilingual conservation status — the most comprehensive open-source dataset
- **KB-First architecture**: SQLite FTS5 enables zero-network species lookup for 30 core species
- **Living system**: Every component has birth date, last verification, and expiry policy
- **Cross-project coordination**: eon-core EventBus + DAG routing for 6-project ecosystem
- **Emergence-aware**: Kalman Filter detects patterns from noisy data; ≥3 sources flag emergence

### Current Limitations
- FishBase sync blocked by SSL in current environment (script ready)
- Some niche Chinese journals have incomplete metadata
- R package version drift monitoring depends on CRAN availability
- Deep species genetic analysis requires manual expert review

### Roadmap
- [ ] FishBase auto-sync when SSL resolved
- [ ] Expand to 500+ species with Mekong basin coverage
- [ ] Real-time population monitoring dashboard
- [ ] Deep learning morphological trait extraction from images

---

## 🔗 Ecosystem

This project is the **Knowledge Supply Core (S/V0)** in the SanShengWanWu ecosystem.

```
S-T-V-P₁-P₂ Architecture (coordinated by eon-core):

  S/V0  📦 fish-ecology-assistant    → Knowledge Supply
  V/V1  🔍 cognitive-search-engine   → Search Verification
  Coord ⚙️ eon-core                  → Coordination Hub

  Derived:
    P₁  🐬 porpoise-agent    → Porpoise Domain Expert
    P₂  🐟 coilia-agent      → Coilia Domain Expert
    P₃  🐟 culter-agent      → Culter Domain Expert
    C   🔥 conflict-arbiter  → Conflict Arbitration
```

> 🔥 Together infinite power, apart top expert engines.

---

🌱 **Everything Flows · Panta Rhei**

> Heraclitus said: No man ever steps in the same river twice.
>
> We say: You cannot analyze today's ecological data with last month's code.

This project is not a fixed toolset — it is a **living system**. Every component has built-in expiration mechanisms, version tracking, and emergence awareness. As your research deepens, packages update, and new methods emerge, it evolves with you.

*Last updated: 2026-06-20　|　Environment: Reasonix Code · DeepSeek Powered*
