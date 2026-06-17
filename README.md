<p align="center">
  🇨🇳 <a href="README.zh.md">中文</a>
</p>

# 🌊 Panta Rhei · Everything Flows

> **Turn your coding agent into a PhD-level research team �?Standard 5-Layer Agent Architecture: Panta Rhei + Systems Thinking.**

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/fangtaocai041/fish-ecology-assistant)
[![Dual Core](https://img.shields.io/badge/dual_core-Panta_Rhei_%2B_Systems_Thinking-6366f1)]()
[![MCP](https://img.shields.io/badge/MCP-21-22c55e)](config/mcp_servers.yaml)
[![Skills](https://img.shields.io/badge/skills-28-f59e0b)](.reasonix/skills/)
[![Architecture](https://img.shields.io/badge/architecture-5_layer-8b5cf6)](docs/ARCHITECTURE.md)
[![Rules](https://img.shields.io/badge/rules-18-8b5cf6)]()
[![Agent](https://img.shields.io/badge/agent-v6.5.0-ec4899)](config/agent.yaml)
[![R](https://img.shields.io/badge/R-4.6.0-276DC3)]()
[![Docker](https://img.shields.io/badge/Docker-ready-2496ED)](Dockerfile)
[![CI](https://img.shields.io/badge/CI-passing-34D058)](.github/workflows/validate.yml)

<p>21 MCP services · 28 AI Skills · 12 search engines · 13 knowledge bases · 18 engineering rules · BDI + ReAct/ToT + MAS · Docker</p>

---

## 🧠 Core Philosophy

> 🌍 The world is dynamic. 📖 Knowledge is temporary. 🌟 Emergence is the norm.

This is not a slogan. It is the operating system running through every line of code, every search, and every analysis in this project.

### 📜 Three Tenets

**🌍 The world is dynamic** �?R packages update, species distributions shift, scientific consensus evolves, climate change reshapes ecosystems. A correct conclusion today may be outdated in six months. We treat no knowledge as eternal truth, but place it on a timeline and view it dynamically.

**📖 Knowledge is temporary** �?The foundation of science is falsification (Popper). No discovery is ultimate truth—only the "best current explanation." We use calibrated language: "evidence suggests" not "proves," "Smith (2022) found" not "studies show." Every output carries a temporal anchor.

**🌟 Emergence is the norm** �?Life, consciousness, ecosystems, AI reasoning—all are emergent phenomena. You cannot assemble the whole by analyzing only the parts. When �? independent sources point to the same unexpected pattern, the system flags it as an emergence signal—not dismisses it as noise.

### ⚖️ Why This Matters for Research

| Scenario | Traditional | Dynamic Worldview |
|:---------|:-----------|:-------------------|
| Package versions | Run 2020 code, ignore version drift | Auto-check, tag "Last verified on glmmTMB v1.1.10" |
| Citations | "Studies prove it" | "Smith (2022) found X, but Jones (2024) added Y" |
| Outliers | Ignore as noise | �? sources �?emergence signal, actively track |
| Knowledge decay | Handbook frozen, never updated | Review records include "Next review date" |
| Method selection | Fixed pipeline forever | Dynamic method selection, dynamic confidence |

### 🧠 Systems Thinking · Seven Engineering Principles

| # | Principle | Source | Engineering Mapping |
|---|-----------|--------|---------------------|
| �?| Practice-Knowledge Cycle | *On Practice* (1937) | Data �?Model �?Verification �?Revision (closed loop) |
| �?| Contradiction Analysis | *On Contradiction* (1937) | Identify principal contradiction �?focus 2.5x resources |
| �?| Phased Strategy | *On Protracted War* (1938) | Defense �?Stalemate �?Counter-offensive = 5-stage pipeline |
| �?| Concentration of Force | Military thought | 60% compute to principal contradiction |
| �?| Initiative & Agency | *On Protracted War* (1938) | Frontier-tracker proactive suggestions + independent path |
| �?| Differentiated Handling | *On Correct Handling of Contradictions* (1957) | Antagonistic vs non-antagonistic �?different strategies |
| �?| Multi-Factor Balance | *On the Ten Major Relationships* (1956) | 10 research balances + multi-objective optimization |

---

## 🐋 DeepSeek Efficiency Principles (效率即智�?

> **Mapped to code**: [Engineering Grammar §8](.reasonix/handbooks/engineering-grammar.md) �?DS-1..DS-4 with formal definitions, WHEN→THEN rules, and config paths.

| ID | Principle | Code Mapping |
|:---|-----------|-------------|
| **DS-1** | **Entropy Budget** �?compute proportional to question importance. PhD �?full pipeline, casual �?single-step. | `pipeline.stages[].activation` + `research-orchestrator` |
| **DS-2** | **Sparse Activation** �?MoE routing: each Skill fires only when condition met. ~2-4/12 active per request. | `pipeline.stages[].activation` + `karpathy-guard` |
| **DS-3** | **Differential Verification** �?P(stale) scoring only changed packages, not full handbook. | `verify-stats-handbook` skill |
| **DS-4** | **Information-Gain Routing** �?P0 exact terms first �?hit-and-stop. P2 redundant terms skipped. Cross-DB dedup. | `ima-smart-search` skill |

---

## 🤔 What This Is

**Fish Ecology Assistant** is a complete configuration package that transforms Reasonix Code from a general-purpose coding assistant into a professional fish ecology research team. It is the **Knowledge Supply Core (S/V0)** in the SanShengWanWu Triangle Core + Derived six-body architecture, coordinated by **eon-core**.

It integrates **21 MCP tools**, **28 domain-specific skills**, **12-engine parallel search**, an automated **5-stage research pipeline**, **13 IMA knowledge bases**, and an **R statistical computing environment**—all outputs guided by the dynamic worldview above.

### 📊 Capability Matrix

| Capability | Vanilla Reasonix | **With This Config** |
|:-----------|:----------------:|:--------------------:|
| Search engines | 1 | **12** (cognitive_search + scholar, article, scholarly, baidu_scholar, cnki, wanfang, cas, ncbi, tavily, exa, web_search) |
| MCP services | 0 | **21** (incl. cognitive_search DirectLoader + DeepWiki) |
| AI subagents | 4 (generic) | **28** (6 pipeline + 20 domain + 2 guard, emergence detection) |
| R statistics | �?| �?R 4.6.0 + 20+ ecology packages |
| OCR | �?| �?PaddleOCR + Tesseract.js |
| Reference manager | �?| �?Direct Zotero SQL queries |
| Research pipeline | �?| �?5-stage + auto-review + emergence detection |
| Knowledge bases | �?| �?13 IMA knowledge bases connected |
| Setup | Manual | �?One script or `docker compose up` |
| CI/CD | �?| �?GitHub Actions auto-validate |
| Engineering rules | �?| �?18 WHEN→THEN rules with code mapping |
| Cross-project | �?| �?fish↔porpoise delegation protocol |

---

## 🧬 KB-First Two-Stage Search (v6.5.0)

> **Check knowledge base first, decide search later.** No more blind 7-engine external search.

```
User Query
    �?    �?┌─────────────────────────�?�? STAGE 1: KB-First      �?�? fishkb search           �?�? ┌───────────────────�? �?�? �?SQLite FTS5        �? �?�? �?30 core species    �? �?�? �?zero-network       �? �?�? └───────┬───────────�? �?�?         �?              �?�?   found? ─── YES ──�?Return immediately
�?     �?�?     NO
�?     �?�?     �?�? STAGE 2: External Search
�? ┌──────────────────────�?�? �?12 engines parallel   �?�? �?�?cognitive_search    �?�? �?�?scholar (GS-first)  �?�? �?�?cnki + wanfang      �?�? �?�?baidu_scholar       �?�? �?�?cas (中科�?         �?�? �?�?ncbi (PubMed)       �?�? �?�?tavily + exa        �?�? �?�?article + scholarly �?�? └──────────────────────�?└─────────────────────────�?```

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
| `lit-search` | Comprehensive literature search v3.1 |
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
| `cross-delegate` | Cross-project task delegation protocol |

### Guard Skills (2)

| Skill | Description |
|-------|-------------|
| `karpathy-guard` | Code quality + safety guard |
| `rule-auditor` | Cross-project rule compliance check |

---

## 🔌 MCP Tools (21)

| Category | Tool | Description |
|----------|------|-------------|
| **Search** | `cognitive_search` | **Primary engine** �?DirectLoader, importlib zero-process |
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
| | `ima` | IMA knowledge base search (14 tools) |
| **Compute** | `rplay` | R 4.6.0 statistical computing |
| | `coderunner` | Multi-language code sandbox |
| | `echarts` | Publication-ready chart generation |
| **Image** | `ocr` | PaddleOCR (Chinese/English tables + formulas) |
| | `ocr_fallback` | Tesseract.js offline OCR |
| | `playwright` | Browser automation + scraping |
| **Data** | `git` | Git version control |
| | `github` | GitHub API (repos, issues, PRs) |
| **Knowledge** | `zotero` | Zotero SQLite direct query |

---

## ☯️ 道生一 · 一生二 · 二生�?· 三生万物

> **Dao begets One, One begets Two, Two begets Three, Three begets the Myriad.**
> �?*Dao De Jing*, Chapter 42

```
        �?(Dao)
    外部世界 · 用户的研究问�?    长江生态系统的真实需�?              �?              �?        一 (One)  �?太极
    命令进入系统 · 统一入口
    fish-ecology-assistant
              �?    ┌─────────┴─────────�?    �?                  �?  �?(Yin)           �?(Yang)
  S/V0 · �?          V/V1 · �?  知识供给            搜索验证
  fish                cognitive
    �?                  �?    └────────┬──────────�?             �?矛盾统一
             �?        �?(Three)  �?三体
    三角最小封闭结�?    S + V + Coord
             �?    ┌────────┼────────┬────────�?    �?       �?       �?       �?  P�?      P�?      P�?      C
porpoise  coilia  culter  conflict
    �?       �?       �?       �?    └────────┼────────┼────────�?             �?    万物 (Myriad Things)
    一切事�?· 无限演化
    Skills · Papers · Analyses
```

**不是"一万种物种"。是"一�?�?*

| �?| 中文 | English | 在系统中的含�?|
|----|------|---------|---------------|
| **�?* | 外界, 自然 | Dao �?the external world | 用户的研究问�? 长江生态的现实需�?|
| **一** | 太极, 命令 | One �?the undivided | 命令进入 fish-ecology-assistant, 统一入口 |
| **�?* | 阴阳, 两仪 | Two �?Yin and Yang | S(知识/�? �?V(验证/�?, 太极生两�?|
| **�?* | 三体, 三角 | Three �?the Triangle | fish + cognitive + eon-core, 矛盾统一的封闭结�?|
| **万物** | 一切事�?| Myriad �?all things | 衍生项目 + Skills + 论文 + 输出, 无限演化 |

> **铁律**: 三角密闭 (缺一不可) · 万物开�?(无限衍生) · 三角不依赖万�?· 二生三即矛盾统一

---

## 🚀 Quick Start

```bash
git clone https://github.com/fangtaocai041/fish-ecology-assistant.git
cd fish-ecology-assistant
```

Or with Docker:
```bash
docker compose up
```

Restart Reasonix, everything is ready.

---

## �?Features

| Feature | Status | Description |
|---------|:------:|-------------|
| 🗃�?430 Species DB | �?| Yangtze fish species with bilingual conservation |
| 📏 289 Morphology | �?| FISHMORPH (251) + FishBase + FAO + manual |
| 🌊 Population-level | �?| 26 records with water-body annotation |
| 🔬 Trait Catalog | �?| 61 traits in 7 categories |
| 🏛�?Conservation | �?| IUCN + China Red List + National + CITES |
| 📊 Excel/HTML | �?| Bilingual reports, 2-level headers |
| 🔗 KB-First Search | �?| SQLite FTS5, zero-network for 30 core species |
| 🕸�?Trait Network | �?| Jaccard co-occurrence, keystone traits |
| 📡 Kalman Filter | �?| Emergence detection from noisy data |
| 🔄 Self-Evolution | �?| 7 triggers auto-adapt parameters |
| 📦 fishkb Sub-library | �?| Independent pip-installable core |
| 🎯 score() Adapter | �?| IProjectAdapter.score() for cross-project quality scoring |
| 🔄 FishBase Sync | 🟡 | Script ready, SSL blocked in env |
| 🧪 Living System | �?| Component registry with expiry policies |

---

## 📁 Project Structure

```
fish-ecology-assistant/
├── README.md                 �?English
├── README.zh.md              �?中文
�?├── .reasonix/
�?  ├── mcp-servers/             �?21 MCP services (incl. deepwiki)
�?  �?  └── ima-server.mjs      �?14 tools
�?  �?�?  ├── skills/                  �?28 AI Skill playbooks
�?  �?  ├── (6 pipeline)  research-orchestrator/planner/executor/analyst/writer/reviewer
�?  �?  ├── (4 search)    academic/cognitive/fuzzy/unified-species-search
�?  �?  ├── (3 research)  frontier-tracker / paper-analyzer / phd-proposal-writer
�?  �?  ├── (3 tools)     ima-smart-search / zotero-assistant / obsidian-assistant
�?  �?  ├── (3 stats)     stats-assistant / stats-method-finder / verify-stats-handbook
�?  �?  ├── (2 guard)     karpathy-guard / rule-auditor
�?  �?  ├── (2 system)    component-health-check / living-system-dashboard
�?  �?  ├── (1 search)    google-scholar-search
�?  �?  ├── (1 debate)    debate-validator
�?  �?  ├── (1 cross)     cross-delegate
�?  �?  └── (1 evolve)    self-evolve
�?  �?�?  ├── handbooks/
�?  �?  ├── systems-thinking.md        �?7 system principles
�?  �?  ├── engineering-grammar.md     �?18 WHEN→THEN rules
�?  �?  ├── activation-matrix.md       �?component coordination
�?  �?  ├── ADVANTAGES.md              �?frontier comparison
�?  �?  ├── WEAKNESSES.md              �?gap analysis
�?  �?  ├── IMPROVEMENT_PLAN.md        �?improvement roadmap
�?  �?  ├── CROSS_PROJECT_PROTOCOL.md  �?cross-agent delegation
�?  �?  ├── DEEPWIKI_INTEGRATION.md    �?DeepWiki integration
�?  �?  ├── LIVING_SYSTEM.md           �?living system implementation
�?  �?  ├── README_UPDATE_RULE.md      �?README sync protocol
�?  �?  └── stats-methods.md           �?statistics methods handbook
�?  �?�?  └── readme-versions/              �?README version archive
�?├── src/                       �?Core Python engine
�?  ├── adapter.py            �?IProjectAdapter + score()
�?  ├── orchestrator.py       �?KB-first species search coordinator
�?  ├── project_hub.py        �?Cross-project coordination (eon-core bridge)
�?  ├── dao_engine.py         �?Philosophical chain executor
�?  └── shared.py             �?Shared types + utilities
�?├── fishkb/                    �?Independent reusable core (pip install fishkb)
�?  ├── fishkb/db.py           �?KnowledgeDB �?SQLite FTS5
�?  ├── fishkb/search.py       �?FishSpeciesMatcher �?KB-First matching
�?  ├── fishkb/credibility.py  �?Paper credibility scoring
�?  └── fishkb/types.py        �?Core data types
�?├── config/
�?  ├── agent.yaml             �?Agent orchestration config
�?  ├── mcp_servers.yaml       �?21 MCP server definitions
�?  ├── coordination.yaml      �?Cross-project coordination
�?  ├── evolution.yaml         �?Self-evolution parameters
�?  ├── component_registry.yaml �?Living system registry
�?  ├── fish_species_kb.yaml   �?430 species index
�?  └── models.yaml            �?Multi-LLM provider config
�?├── data/
�?  ├── species.db             �?SQLite (species + traits + literature)
�?  ├── FISHMORPH.csv           �?2.3MB global morphology database
�?  └── reports/               �?HTML/CSV exports
�?├── scripts/
�?  ├── credibility_scorer.py  �?Triangulation scoring (0-100)
�?  ├── self_evolve.py         �?6-dimension evolution
�?  ├── kb_to_graph_sync.py    �?KB �?Graph sync
�?  └── taxonomy_sync.py       �?NCBI taxonomy sync
�?├── Dockerfile
├── docker-compose.yml
├── docs/
�?  ├── ARCHITECTURE.md        �?Full 5-layer architecture
�?  ├── SKILL_PIPELINE.md      �?Skill pipeline documentation
�?  └── WORKFLOWS.md           �?Research workflows
�?└── .github/workflows/
    └── validate.yml           �?CI/CD auto-validate
```

---

## 🗺�?Future Roadmap

### Strengths
- **Species coverage**: 430 Yangtze fish species �?most comprehensive open-source dataset
- **KB-First architecture**: SQLite FTS5 enables zero-network species lookup
- **Living system**: Every component has birth date, last verification, and expiry policy
- **Cross-project coordination**: eon-core EventBus + DAG routing for 6-project ecosystem
- **Emergence-aware**: Kalman Filter + �? sources flag emergence

### Known Limitations
- FishBase sync blocked by SSL in current environment (script ready)
- Some niche Chinese journals have incomplete metadata
- R package version drift monitoring depends on CRAN availability

### Milestones
- [ ] FishBase auto-sync when SSL resolved �?500+ species with Mekong basin
- [ ] Real-time population monitoring dashboard
- [ ] Deep learning morphological trait extraction from images
- [ ] Peer-reviewed publication on KB-First search methodology

---

## 📋 README Changelog

| Version | Date | Theme | What Changed |
|:--------|:-----|:------|:-------------|
| **v8.1** | 2026-06-20 | README Restoration | Restored from historical sessions: Systems Thinking 7 principles, DeepSeek efficiency principles, 道生万物 architecture, README Changelog, DeepWiki/Dual Core/Docker badges, unified ecosystem with 6 projects |
| **v7.1** | 2026-06-20 | Data sync | + MCP 21 fix, Skills 28 fix, bilingual README sync, cognitive_search in ZH MCP table |
| **v7.0** | 2026-06-10 | lit-search v3.1 | + lit-search v3.1 (synonym expansion→interactive�?2-layer→triangulation), + credibility_scorer.py, + self_evolve.py, + kb_to_graph_sync.py |
| **v6.5** | 2026-06-07 | Cognitive Engine | + DirectLoader protocol, dual-mode search, knowledge graph evolution |
| **v6** | 2026-06-06 | Search v3.0 | 12 search engines (GS-first + CNKI/Wanfang/Baidu/CAS), google-scholar-search skill |
| **v5** | 2026-06-06 | Systems Thinking | + Dual-core philosophy (Panta Rhei + Systems Thinking), 7 principles + 4 DS principles, engineering grammar (18 WHEN→THEN) |
| **v4** | 2026-06-05 | Engineering | Full rewrite: Panta Rhei philosophy, capability comparison, sparse activation |
| **v3** | 2026-06-05 | Panta Rhei | Dynamic worldview integration, emergence detection, calibrated language |
| **v2** | 2026-06-05 | Original | Initial release �?Fish ecology assistant, 5 engines + 12 sub-agents |

---

## 📜 License

MIT © 2026 fangtaocai041

---

> **"不要搜索字符串，要重建所指�?**
> Don't search for strings �?reconstruct the signified.


> **Mapped to code**: [Engineering Grammar §8](.reasonix/handbooks/engineering-grammar.md) �?DS-1..DS-4 with formal definitions, WHEN→THEN rules, and config paths.

| ID | Principle | Code Mapping |
|:---|-----------|-------------|
| **DS-1** | **Entropy Budget** �?compute proportional to question importance. PhD �?full pipeline, casual �?single-step. | `pipeline.stages[].activation` + `research-orchestrator` |
| **DS-2** | **Sparse Activation** �?MoE routing: each Skill fires only when condition met. ~2-4/12 active per request. | `pipeline.stages[].activation` + `karpathy-guard` |
| **DS-3** | **Differential Verification** �?P(stale) scoring only changed packages, not full handbook. | `verify-stats-handbook` skill |
| **DS-4** | **Information-Gain Routing** �?P0 exact terms first �?hit-and-stop. P2 redundant terms skipped. Cross-DB dedup. | `ima-smart-search` skill |

---


**Fish Ecology Assistant** is a complete configuration package that transforms Reasonix Code from a general-purpose coding assistant into a professional fish ecology research team. It is the **Knowledge Supply Core (S/V0)** in the SanShengWanWu Triangle Core + Derived six-body architecture, coordinated by **eon-core**.

It integrates **21 MCP tools**, **28 domain-specific skills**, **12-engine parallel search**, an automated **5-stage research pipeline**, **13 IMA knowledge bases**, and an **R statistical computing environment**—all outputs guided by the dynamic worldview above.


| Capability | Vanilla Reasonix | **With This Config** |
|:-----------|:----------------:|:--------------------:|
| Search engines | 1 | **12** (cognitive_search + scholar, article, scholarly, baidu_scholar, cnki, wanfang, cas, ncbi, tavily, exa, web_search) |
| MCP services | 0 | **21** (incl. cognitive_search DirectLoader + DeepWiki) |
| AI subagents | 4 (generic) | **28** (6 pipeline + 20 domain + 2 guard, emergence detection) |
| R statistics | �?| �?R 4.6.0 + 20+ ecology packages |
| OCR | �?| �?PaddleOCR + Tesseract.js |
| Reference manager | �?| �?Direct Zotero SQL queries |
| Research pipeline | �?| �?5-stage + auto-review + emergence detection |
| Knowledge bases | �?| �?13 IMA knowledge bases connected |
| Setup | Manual | �?One script or `docker compose up` |
| CI/CD | �?| �?GitHub Actions auto-validate |
| Engineering rules | �?| �?18 WHEN→THEN rules with code mapping |
| Cross-project | �?| �?fish↔porpoise delegation protocol |

---


> **Check knowledge base first, decide search later.** No more blind 7-engine external search.

```
User Query
    �?    �?┌─────────────────────────�?�? STAGE 1: KB-First      �?�? fishkb search           �?�? ┌───────────────────�? �?�? �?SQLite FTS5        �? �?�? �?30 core species    �? �?�? �?zero-network       �? �?�? └───────┬───────────�? �?�?         �?              �?�?   found? ─── YES ──�?Return immediately
�?     �?�?     NO
�?     �?�?     �?�? STAGE 2: External Search
�? ┌──────────────────────�?�? �?12 engines parallel   �?�? �?�?cognitive_search    �?�? �?�?scholar (GS-first)  �?�? �?�?cnki + wanfang      �?�? �?�?baidu_scholar       �?�? �?�?cas (中科�?         �?�? �?�?ncbi (PubMed)       �?�? �?�?tavily + exa        �?�? �?�?article + scholarly �?�? └──────────────────────�?└─────────────────────────�?```

---



| Skill | Description |
|-------|-------------|
| `research-orchestrator` | Top-level pipeline coordinator |
| `research-planner` | Research question decomposition + strategy |
| `research-executor` | Multi-engine parallel literature search |
| `research-analyst` | Statistical analysis + data interpretation |
| `research-writer` | Bilingual report generation |
| `research-reviewer` | Quality review + contradiction detection |


| Skill | Description |
|-------|-------------|
| `academic-species-search` | Multi-source species academic search |
| `cognitive-species-search` | Cognitive graph species search |
| `unified-species-search` | Unified species search across all engines |
| `fuzzy-species-search` | Fuzzy name matching + OCR variants |
| `google-scholar-search` | Google Scholar targeted search |
| `lit-search` | Comprehensive literature search v3.1 |
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
| `cross-delegate` | Cross-project task delegation protocol |


| Skill | Description |
|-------|-------------|
| `karpathy-guard` | Code quality + safety guard |
| `rule-auditor` | Cross-project rule compliance check |

---


| Category | Tool | Description |
|----------|------|-------------|
| **Search** | `cognitive_search` | **Primary engine** �?DirectLoader, importlib zero-process |
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
| | `ima` | IMA knowledge base search (14 tools) |
| **Compute** | `rplay` | R 4.6.0 statistical computing |
| | `coderunner` | Multi-language code sandbox |
| | `echarts` | Publication-ready chart generation |
| **Image** | `ocr` | PaddleOCR (Chinese/English tables + formulas) |
| | `ocr_fallback` | Tesseract.js offline OCR |
| | `playwright` | Browser automation + scraping |
| **Data** | `git` | Git version control |
| | `github` | GitHub API (repos, issues, PRs) |
| **Knowledge** | `zotero` | Zotero SQLite direct query |

---


> **Dao begets One, One begets Two, Two begets Three, Three begets the Myriad.**
> �?*Dao De Jing*, Chapter 42

```
        �?(Dao)
    外部世界 · 用户的研究问�?    长江生态系统的真实需�?              �?              �?        一 (One)  �?太极
    命令进入系统 · 统一入口
    fish-ecology-assistant
              �?    ┌─────────┴─────────�?    �?                  �?  �?(Yin)           �?(Yang)
  S/V0 · �?          V/V1 · �?  知识供给            搜索验证
  fish                cognitive
    �?                  �?    └────────┬──────────�?             �?矛盾统一
             �?        �?(Three)  �?三体
    三角最小封闭结�?    S + V + Coord
             �?    ┌────────┼────────┬────────�?    �?       �?       �?       �?  P�?      P�?      P�?      C
porpoise  coilia  culter  conflict
    �?       �?       �?       �?    └────────┼────────┼────────�?             �?    万物 (Myriad Things)
    一切事�?· 无限演化
    Skills · Papers · Analyses
```

**不是"一万种物种"。是"一�?�?*

| �?| 中文 | English | 在系统中的含�?|
|----|------|---------|---------------|
| **�?* | 外界, 自然 | Dao �?the external world | 用户的研究问�? 长江生态的现实需�?|
| **一** | 太极, 命令 | One �?the undivided | 命令进入 fish-ecology-assistant, 统一入口 |
| **�?* | 阴阳, 两仪 | Two �?Yin and Yang | S(知识/�? �?V(验证/�?, 太极生两�?|
| **�?* | 三体, 三角 | Three �?the Triangle | fish + cognitive + eon-core, 矛盾统一的封闭结�?|
| **万物** | 一切事�?| Myriad �?all things | 衍生项目 + Skills + 论文 + 输出, 无限演化 |

> **铁律**: 三角密闭 (缺一不可) · 万物开�?(无限衍生) · 三角不依赖万�?· 二生三即矛盾统一

---


```bash
git clone https://github.com/fangtaocai041/fish-ecology-assistant.git
cd fish-ecology-assistant
```

Or with Docker:
```bash
docker compose up
```

Restart Reasonix, everything is ready.

---


| Feature | Status | Description |
|---------|:------:|-------------|
| 🗃�?430 Species DB | �?| Yangtze fish species with bilingual conservation |
| 📏 289 Morphology | �?| FISHMORPH (251) + FishBase + FAO + manual |
| 🌊 Population-level | �?| 26 records with water-body annotation |
| 🔬 Trait Catalog | �?| 61 traits in 7 categories |
| 🏛�?Conservation | �?| IUCN + China Red List + National + CITES |
| 📊 Excel/HTML | �?| Bilingual reports, 2-level headers |
| 🔗 KB-First Search | �?| SQLite FTS5, zero-network for 30 core species |
| 🕸�?Trait Network | �?| Jaccard co-occurrence, keystone traits |
| 📡 Kalman Filter | �?| Emergence detection from noisy data |
| 🔄 Self-Evolution | �?| 7 triggers auto-adapt parameters |
| 📦 fishkb Sub-library | �?| Independent pip-installable core |
| 🎯 score() Adapter | �?| IProjectAdapter.score() for cross-project quality scoring |
| 🔄 FishBase Sync | 🟡 | Script ready, SSL blocked in env |
| 🧪 Living System | �?| Component registry with expiry policies |

---


```
fish-ecology-assistant/
├── README.md                 �?English
├── README.zh.md              �?中文
�?├── .reasonix/
�?  ├── mcp-servers/             �?21 MCP services (incl. deepwiki)
�?  �?  └── ima-server.mjs      �?14 tools
�?  �?�?  ├── skills/                  �?28 AI Skill playbooks
�?  �?  ├── (6 pipeline)  research-orchestrator/planner/executor/analyst/writer/reviewer
�?  �?  ├── (4 search)    academic/cognitive/fuzzy/unified-species-search
�?  �?  ├── (3 research)  frontier-tracker / paper-analyzer / phd-proposal-writer
�?  �?  ├── (3 tools)     ima-smart-search / zotero-assistant / obsidian-assistant
�?  �?  ├── (3 stats)     stats-assistant / stats-method-finder / verify-stats-handbook
�?  �?  ├── (2 guard)     karpathy-guard / rule-auditor
�?  �?  ├── (2 system)    component-health-check / living-system-dashboard
�?  �?  ├── (1 search)    google-scholar-search
�?  �?  ├── (1 debate)    debate-validator
�?  �?  ├── (1 cross)     cross-delegate
�?  �?  └── (1 evolve)    self-evolve
�?  �?�?  ├── handbooks/
�?  �?  ├── systems-thinking.md        �?7 system principles
�?  �?  ├── engineering-grammar.md     �?18 WHEN→THEN rules
�?  �?  ├── activation-matrix.md       �?component coordination
�?  �?  ├── ADVANTAGES.md              �?frontier comparison
�?  �?  ├── WEAKNESSES.md              �?gap analysis
�?  �?  ├── IMPROVEMENT_PLAN.md        �?improvement roadmap
�?  �?  ├── CROSS_PROJECT_PROTOCOL.md  �?cross-agent delegation
�?  �?  ├── DEEPWIKI_INTEGRATION.md    �?DeepWiki integration
�?  �?  ├── LIVING_SYSTEM.md           �?living system implementation
�?  �?  ├── README_UPDATE_RULE.md      �?README sync protocol
�?  �?  └── stats-methods.md           �?statistics methods handbook
�?  �?�?  └── readme-versions/              �?README version archive
�?├── src/                       �?Core Python engine
�?  ├── adapter.py            �?IProjectAdapter + score()
�?  ├── orchestrator.py       �?KB-first species search coordinator
�?  ├── project_hub.py        �?Cross-project coordination (eon-core bridge)
�?  ├── dao_engine.py         �?Philosophical chain executor
�?  └── shared.py             �?Shared types + utilities
�?├── fishkb/                    �?Independent reusable core (pip install fishkb)
�?  ├── fishkb/db.py           �?KnowledgeDB �?SQLite FTS5
�?  ├── fishkb/search.py       �?FishSpeciesMatcher �?KB-First matching
�?  ├── fishkb/credibility.py  �?Paper credibility scoring
�?  └── fishkb/types.py        �?Core data types
�?├── config/
�?  ├── agent.yaml             �?Agent orchestration config
�?  ├── mcp_servers.yaml       �?21 MCP server definitions
�?  ├── coordination.yaml      �?Cross-project coordination
�?  ├── evolution.yaml         �?Self-evolution parameters
�?  ├── component_registry.yaml �?Living system registry
�?  ├── fish_species_kb.yaml   �?430 species index
�?  └── models.yaml            �?Multi-LLM provider config
�?├── data/
�?  ├── species.db             �?SQLite (species + traits + literature)
�?  ├── FISHMORPH.csv           �?2.3MB global morphology database
�?  └── reports/               �?HTML/CSV exports
�?├── scripts/
�?  ├── credibility_scorer.py  �?Triangulation scoring (0-100)
�?  ├── self_evolve.py         �?6-dimension evolution
�?  ├── kb_to_graph_sync.py    �?KB �?Graph sync
�?  └── taxonomy_sync.py       �?NCBI taxonomy sync
�?├── Dockerfile
├── docker-compose.yml
├── docs/
�?  ├── ARCHITECTURE.md        �?Full 5-layer architecture
�?  ├── SKILL_PIPELINE.md      �?Skill pipeline documentation
�?  └── WORKFLOWS.md           �?Research workflows
�?└── .github/workflows/
    └── validate.yml           �?CI/CD auto-validate
```

---


- **Species coverage**: 430 Yangtze fish species �?most comprehensive open-source dataset
- **KB-First architecture**: SQLite FTS5 enables zero-network species lookup
- **Living system**: Every component has birth date, last verification, and expiry policy
- **Cross-project coordination**: eon-core EventBus + DAG routing for 6-project ecosystem
- **Emergence-aware**: Kalman Filter + �? sources flag emergence

- FishBase sync blocked by SSL in current environment (script ready)
- Some niche Chinese journals have incomplete metadata
- R package version drift monitoring depends on CRAN availability

- [ ] FishBase auto-sync when SSL resolved �?500+ species with Mekong basin
- [ ] Real-time population monitoring dashboard
- [ ] Deep learning morphological trait extraction from images
- [ ] Peer-reviewed publication on KB-First search methodology

---


| Version | Date | Theme | What Changed |
|:--------|:-----|:------|:-------------|
| **v8.1** | 2026-06-20 | README Restoration | Restored from historical sessions: Systems Thinking 7 principles, DeepSeek efficiency principles, 道生万物 architecture, README Changelog, DeepWiki/Dual Core/Docker badges, unified ecosystem with 6 projects |
| **v7.1** | 2026-06-20 | Data sync | + MCP 21 fix, Skills 28 fix, bilingual README sync, cognitive_search in ZH MCP table |
| **v7.0** | 2026-06-10 | lit-search v3.1 | + lit-search v3.1 (synonym expansion→interactive�?2-layer→triangulation), + credibility_scorer.py, + self_evolve.py, + kb_to_graph_sync.py |
| **v6.5** | 2026-06-07 | Cognitive Engine | + DirectLoader protocol, dual-mode search, knowledge graph evolution |
| **v6** | 2026-06-06 | Search v3.0 | 12 search engines (GS-first + CNKI/Wanfang/Baidu/CAS), google-scholar-search skill |
| **v5** | 2026-06-06 | Systems Thinking | + Dual-core philosophy (Panta Rhei + Systems Thinking), 7 principles + 4 DS principles, engineering grammar (18 WHEN→THEN) |
| **v4** | 2026-06-05 | Engineering | Full rewrite: Panta Rhei philosophy, capability comparison, sparse activation |
| **v3** | 2026-06-05 | Panta Rhei | Dynamic worldview integration, emergence detection, calibrated language |
| **v2** | 2026-06-05 | Original | Initial release �?Fish ecology assistant, 5 engines + 12 sub-agents |

---


MIT © 2026 fangtaocai041

---

> **"不要搜索字符串，要重建所指�?**
> Don't search for strings �?reconstruct the signified.

## 🔺 Triangle Core + Derived Role: **S/V0 (Knowledge Supply)**

> Triangle Core (sealed 3) + Derived (open N) architecture: `fish(S/V0)` �?`cognitive(V/V1)` �?`eon-core(Coord)`, with `porpoise(P�?` + `coilia(P�?` + `culter(P�?` + `conflict-arbiter(C)` as derived domain experts.
> Provides knowledge, multi-basin fish data (Yangtze 430 + Tumen + Suifen + Amur expanding), contradiction analysis, and ecological findings.
> **D�?Plane**: multi-agent debate mesh. **Triangulation**: �? sources.
> Coordinated by [eon-core](https://github.com/fangtaocai041/eon-core).

## 📊 Self-Assessment

| Dimension | Rating | Notes |
|-----------|:-----:|-------|
| 📚 Knowledge Breadth | ⭐⭐⭐⭐�?| 12 search engines + 13 KBs + multi-basin fish DB (Yangtze 430 + Tumen + Suifen) |
| 🧘 Philosophy Integration | ⭐⭐⭐⭐�?| Panta Rhei + Systems Thinking �?18 WHEN→THEN engineering rules |
| 🔬 Research Pipeline | ⭐⭐⭐⭐�?| 5-stage: Plan→Search→Analyze→Write→Review, 28 AI Skills |
| 🌏 Chinese Literature | ⭐⭐⭐⭐�?| CNKI/万方/百度学术/中科�?�?unique coverage Western DBs miss |
| 🔗 Ecosystem Role | ⭐⭐⭐⭐�?| Triangle Core member (V0), coordinated by eon-core |
| 🧪 Test Coverage | ⭐⭐⭐⭐�?| Cross-project validation + rule compliance checks |

---

## 📋 Version History

| Version | Date | Changes |
|---------|------|---------|
| **v6.5.0** | 2026-06-20 | 🧬 KB-First 两阶段搜�?+ 🏠 宿主容器架构 �?`ProjectHub` 统一加载6个子系统 · `search_species()` 统一入口 · `delegate_to()` 跨项目委�?· fishkb 子库独立 pip 安装 |
| **v6.4.0** | 2026-06-12 | 🔧 Engineering architecture · exact match(_match_species) · taxonomy_log · detect_taxonomy_discrepancy · verify_architecture.py |
| **v6.3.0** | 2026-06-08 | ☯️ 10-layer concentric architecture + conflict-arbiter (V4) integration |
| **v6.2** | 2026-06-08 | Triangle Core + Derived ecosystem · Yangtze 430 species KB · eon-core intelligent scheduling |
| **v6.1** | 2026-06-07 | Cross-project co-evolution · Triangle Core role · coordination.yaml |
| **v6.0** | 2026-06-07 | Cognitive Search Engine DirectLoader · dual-mode search |
| **v5.0** | 2026-06-06 | 12 search engines · GS-first + Chinese sources |

> **Latest**: v6.5.0 · 2026-06-20

> **Core Strength**: Universal fish ecology research platform. Dual-core philosophy (Panta Rhei + Systems Thinking) is not decoration but runtime constraint �?contradiction analysis drives search strategy, phased strategy determines stopping conditions.

## 🔗 Ecosystem �?Triangle Core + Derived

| Project | Layer | Role | Description |
|---------|:-----:|------|-------------|
| **eon-core** | **Coord** | Coordination Hub | EventBus · CAS · DAG routing · 6-project topology |
| **cognitive-search-engine** | **Triangle V1** | Validation | BDI+ReAct · Authority scoring · Hub-and-Spoke search |
| **porpoise-agent** | **Derived P�?* | Porpoise domain | 5-phase pipeline · Acoustic analysis · Conservation |
| **coilia-agent** | **Derived P�?* | Coilia domain | Otolith microchemistry · Migration ecology |
| **culter-agent** | **Derived P�?* | Culter domain | Trophic ecology · Growth analysis |
| **conflict-arbiter** | **Derived C** | Conflict arbitration | Multi-source protection-level detection |

> **Co-evolution**: Triangle Core provides knowledge and validation �?Derived projects execute domain pipelines.
> The triangle is incomplete without any one corner; derived projects are independent.
> Knowledge graph evolves �?all six projects benefit.
> Full spec: workspace root `coordination.yaml`.

---

## 🏛�?Architecture · Standard 5-Layer Agent Model

> See full documentation at [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)
> **5 Layers**: Interaction & Perception �?Cognitive & Decision �?Memory System �?Mapping & Translation �?Tool & Execution
> **Theoretical Foundations**: BDI (Belief-Desire-Intention) · MDP/POMDP Formalism · ReAct/ToT/GoT Reasoning · Reflexion Self-Correction · MAS Multi-Agent Topology


> 🌍 The world is dynamic. 📖 Knowledge is temporary. 🌟 Emergence is the norm.

This is not a slogan. It is the operating system running through every line of code, every search, and every analysis in this project.


**🌍 The world is dynamic** �?R packages update, species distributions shift, scientific consensus evolves, climate change reshapes ecosystems. A correct conclusion today may be outdated in six months. We treat no knowledge as eternal truth, but place it on a timeline and view it dynamically.

**📖 Knowledge is temporary** �?The foundation of science is falsification (Popper). No discovery is ultimate truth—only the "best current explanation." We use calibrated language: "evidence suggests" not "proves," "Smith (2022) found" not "studies show." Every output carries a temporal anchor.

**🌟 Emergence is the norm** �?Life, consciousness, ecosystems, AI reasoning—all are emergent phenomena. You cannot assemble the whole by analyzing only the parts. When �? independent sources point to the same unexpected pattern, the system flags it as an emergence signal—not dismisses it as noise.


| Scenario | Traditional | Dynamic Worldview |
|:---------|:-----------|:-------------------|
| Package versions | Run 2020 code, ignore version drift | Auto-check, tag "Last verified on glmmTMB v1.1.10" |
| Citations | "Studies prove it" | "Smith (2022) found X, but Jones (2024) added Y" |
| Outliers | Ignore as noise | �? sources �?emergence signal, actively track |
| Knowledge decay | Handbook frozen, never updated | Review records include "Next review date" |
| Method selection | Fixed pipeline forever | Dynamic method selection, dynamic confidence |


| # | Principle | Source | Engineering Mapping |
|---|-----------|--------|---------------------|
| �?| Practice-Knowledge Cycle | *On Practice* (1937) | Data �?Model �?Verification �?Revision (closed loop) |
| �?| Contradiction Analysis | *On Contradiction* (1937) | Identify principal contradiction �?focus 2.5x resources |
| �?| Phased Strategy | *On Protracted War* (1938) | Defense �?Stalemate �?Counter-offensive = 5-stage pipeline |
| �?| Concentration of Force | Military thought | 60% compute to principal contradiction |
| �?| Initiative & Agency | *On Protracted War* (1938) | Frontier-tracker proactive suggestions + independent path |
| �?| Differentiated Handling | *On Correct Handling of Contradictions* (1957) | Antagonistic vs non-antagonistic �?different strategies |
| �?| Multi-Factor Balance | *On the Ten Major Relationships* (1956) | 10 research balances + multi-objective optimization |

---


> **Mapped to code**: [Engineering Grammar §8](.reasonix/handbooks/engineering-grammar.md) �?DS-1..DS-4 with formal definitions, WHEN→THEN rules, and config paths.

| ID | Principle | Code Mapping |
|:---|-----------|-------------|
| **DS-1** | **Entropy Budget** �?compute proportional to question importance. PhD �?full pipeline, casual �?single-step. | `pipeline.stages[].activation` + `research-orchestrator` |
| **DS-2** | **Sparse Activation** �?MoE routing: each Skill fires only when condition met. ~2-4/12 active per request. | `pipeline.stages[].activation` + `karpathy-guard` |
| **DS-3** | **Differential Verification** �?P(stale) scoring only changed packages, not full handbook. | `verify-stats-handbook` skill |
| **DS-4** | **Information-Gain Routing** �?P0 exact terms first �?hit-and-stop. P2 redundant terms skipped. Cross-DB dedup. | `ima-smart-search` skill |

---


**Fish Ecology Assistant** is a complete configuration package that transforms Reasonix Code from a general-purpose coding assistant into a professional fish ecology research team. It is the **Knowledge Supply Core (S/V0)** in the SanShengWanWu Triangle Core + Derived six-body architecture, coordinated by **eon-core**.

It integrates **21 MCP tools**, **28 domain-specific skills**, **12-engine parallel search**, an automated **5-stage research pipeline**, **13 IMA knowledge bases**, and an **R statistical computing environment**—all outputs guided by the dynamic worldview above.


| Capability | Vanilla Reasonix | **With This Config** |
|:-----------|:----------------:|:--------------------:|
| Search engines | 1 | **12** (cognitive_search + scholar, article, scholarly, baidu_scholar, cnki, wanfang, cas, ncbi, tavily, exa, web_search) |
| MCP services | 0 | **21** (incl. cognitive_search DirectLoader + DeepWiki) |
| AI subagents | 4 (generic) | **28** (6 pipeline + 20 domain + 2 guard, emergence detection) |
| R statistics | �?| �?R 4.6.0 + 20+ ecology packages |
| OCR | �?| �?PaddleOCR + Tesseract.js |
| Reference manager | �?| �?Direct Zotero SQL queries |
| Research pipeline | �?| �?5-stage + auto-review + emergence detection |
| Knowledge bases | �?| �?13 IMA knowledge bases connected |
| Setup | Manual | �?One script or `docker compose up` |
| CI/CD | �?| �?GitHub Actions auto-validate |
| Engineering rules | �?| �?18 WHEN→THEN rules with code mapping |
| Cross-project | �?| �?fish↔porpoise delegation protocol |

---


> **Check knowledge base first, decide search later.** No more blind 7-engine external search.

```
User Query
    �?    �?┌─────────────────────────�?�? STAGE 1: KB-First      �?�? fishkb search           �?�? ┌───────────────────�? �?�? �?SQLite FTS5        �? �?�? �?30 core species    �? �?�? �?zero-network       �? �?�? └───────┬───────────�? �?�?         �?              �?�?   found? ─── YES ──�?Return immediately
�?     �?�?     NO
�?     �?�?     �?�? STAGE 2: External Search
�? ┌──────────────────────�?�? �?12 engines parallel   �?�? �?�?cognitive_search    �?�? �?�?scholar (GS-first)  �?�? �?�?cnki + wanfang      �?�? �?�?baidu_scholar       �?�? �?�?cas (中科�?         �?�? �?�?ncbi (PubMed)       �?�? �?�?tavily + exa        �?�? �?�?article + scholarly �?�? └──────────────────────�?└─────────────────────────�?```

---



| Skill | Description |
|-------|-------------|
| `research-orchestrator` | Top-level pipeline coordinator |
| `research-planner` | Research question decomposition + strategy |
| `research-executor` | Multi-engine parallel literature search |
| `research-analyst` | Statistical analysis + data interpretation |
| `research-writer` | Bilingual report generation |
| `research-reviewer` | Quality review + contradiction detection |


| Skill | Description |
|-------|-------------|
| `academic-species-search` | Multi-source species academic search |
| `cognitive-species-search` | Cognitive graph species search |
| `unified-species-search` | Unified species search across all engines |
| `fuzzy-species-search` | Fuzzy name matching + OCR variants |
| `google-scholar-search` | Google Scholar targeted search |
| `lit-search` | Comprehensive literature search v3.1 |
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
| `cross-delegate` | Cross-project task delegation protocol |


| Skill | Description |
|-------|-------------|
| `karpathy-guard` | Code quality + safety guard |
| `rule-auditor` | Cross-project rule compliance check |

---


| Category | Tool | Description |
|----------|------|-------------|
| **Search** | `cognitive_search` | **Primary engine** �?DirectLoader, importlib zero-process |
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
| | `ima` | IMA knowledge base search (14 tools) |
| **Compute** | `rplay` | R 4.6.0 statistical computing |
| | `coderunner` | Multi-language code sandbox |
| | `echarts` | Publication-ready chart generation |
| **Image** | `ocr` | PaddleOCR (Chinese/English tables + formulas) |
| | `ocr_fallback` | Tesseract.js offline OCR |
| | `playwright` | Browser automation + scraping |
| **Data** | `git` | Git version control |
| | `github` | GitHub API (repos, issues, PRs) |
| **Knowledge** | `zotero` | Zotero SQLite direct query |

---


> **Dao begets One, One begets Two, Two begets Three, Three begets the Myriad.**
> �?*Dao De Jing*, Chapter 42

```
        �?(Dao)
    外部世界 · 用户的研究问�?    长江生态系统的真实需�?              �?              �?        一 (One)  �?太极
    命令进入系统 · 统一入口
    fish-ecology-assistant
              �?    ┌─────────┴─────────�?    �?                  �?  �?(Yin)           �?(Yang)
  S/V0 · �?          V/V1 · �?  知识供给            搜索验证
  fish                cognitive
    �?                  �?    └────────┬──────────�?             �?矛盾统一
             �?        �?(Three)  �?三体
    三角最小封闭结�?    S + V + Coord
             �?    ┌────────┼────────┬────────�?    �?       �?       �?       �?  P�?      P�?      P�?      C
porpoise  coilia  culter  conflict
    �?       �?       �?       �?    └────────┼────────┼────────�?             �?    万物 (Myriad Things)
    一切事�?· 无限演化
    Skills · Papers · Analyses
```

**不是"一万种物种"。是"一�?�?*

| �?| 中文 | English | 在系统中的含�?|
|----|------|---------|---------------|
| **�?* | 外界, 自然 | Dao �?the external world | 用户的研究问�? 长江生态的现实需�?|
| **一** | 太极, 命令 | One �?the undivided | 命令进入 fish-ecology-assistant, 统一入口 |
| **�?* | 阴阳, 两仪 | Two �?Yin and Yang | S(知识/�? �?V(验证/�?, 太极生两�?|
| **�?* | 三体, 三角 | Three �?the Triangle | fish + cognitive + eon-core, 矛盾统一的封闭结�?|
| **万物** | 一切事�?| Myriad �?all things | 衍生项目 + Skills + 论文 + 输出, 无限演化 |

> **铁律**: 三角密闭 (缺一不可) · 万物开�?(无限衍生) · 三角不依赖万�?· 二生三即矛盾统一

---


```bash
git clone https://github.com/fangtaocai041/fish-ecology-assistant.git
cd fish-ecology-assistant
```

Or with Docker:
```bash
docker compose up
```

Restart Reasonix, everything is ready.

---


| Feature | Status | Description |
|---------|:------:|-------------|
| 🗃�?430 Species DB | �?| Yangtze fish species with bilingual conservation |
| 📏 289 Morphology | �?| FISHMORPH (251) + FishBase + FAO + manual |
| 🌊 Population-level | �?| 26 records with water-body annotation |
| 🔬 Trait Catalog | �?| 61 traits in 7 categories |
| 🏛�?Conservation | �?| IUCN + China Red List + National + CITES |
| 📊 Excel/HTML | �?| Bilingual reports, 2-level headers |
| 🔗 KB-First Search | �?| SQLite FTS5, zero-network for 30 core species |
| 🕸�?Trait Network | �?| Jaccard co-occurrence, keystone traits |
| 📡 Kalman Filter | �?| Emergence detection from noisy data |
| 🔄 Self-Evolution | �?| 7 triggers auto-adapt parameters |
| 📦 fishkb Sub-library | �?| Independent pip-installable core |
| 🎯 score() Adapter | �?| IProjectAdapter.score() for cross-project quality scoring |
| 🔄 FishBase Sync | 🟡 | Script ready, SSL blocked in env |
| 🧪 Living System | �?| Component registry with expiry policies |

---


```
fish-ecology-assistant/
├── README.md                 �?English
├── README.zh.md              �?中文
�?├── .reasonix/
�?  ├── mcp-servers/             �?21 MCP services (incl. deepwiki)
�?  �?  └── ima-server.mjs      �?14 tools
�?  �?�?  ├── skills/                  �?28 AI Skill playbooks
�?  �?  ├── (6 pipeline)  research-orchestrator/planner/executor/analyst/writer/reviewer
�?  �?  ├── (4 search)    academic/cognitive/fuzzy/unified-species-search
�?  �?  ├── (3 research)  frontier-tracker / paper-analyzer / phd-proposal-writer
�?  �?  ├── (3 tools)     ima-smart-search / zotero-assistant / obsidian-assistant
�?  �?  ├── (3 stats)     stats-assistant / stats-method-finder / verify-stats-handbook
�?  �?  ├── (2 guard)     karpathy-guard / rule-auditor
�?  �?  ├── (2 system)    component-health-check / living-system-dashboard
�?  �?  ├── (1 search)    google-scholar-search
�?  �?  ├── (1 debate)    debate-validator
�?  �?  ├── (1 cross)     cross-delegate
�?  �?  └── (1 evolve)    self-evolve
�?  �?�?  ├── handbooks/
�?  �?  ├── systems-thinking.md        �?7 system principles
�?  �?  ├── engineering-grammar.md     �?18 WHEN→THEN rules
�?  �?  ├── activation-matrix.md       �?component coordination
�?  �?  ├── ADVANTAGES.md              �?frontier comparison
�?  �?  ├── WEAKNESSES.md              �?gap analysis
�?  �?  ├── IMPROVEMENT_PLAN.md        �?improvement roadmap
�?  �?  ├── CROSS_PROJECT_PROTOCOL.md  �?cross-agent delegation
�?  �?  ├── DEEPWIKI_INTEGRATION.md    �?DeepWiki integration
�?  �?  ├── LIVING_SYSTEM.md           �?living system implementation
�?  �?  ├── README_UPDATE_RULE.md      �?README sync protocol
�?  �?  └── stats-methods.md           �?statistics methods handbook
�?  �?�?  └── readme-versions/              �?README version archive
�?├── src/                       �?Core Python engine
�?  ├── adapter.py            �?IProjectAdapter + score()
�?  ├── orchestrator.py       �?KB-first species search coordinator
�?  ├── project_hub.py        �?Cross-project coordination (eon-core bridge)
�?  ├── dao_engine.py         �?Philosophical chain executor
�?  └── shared.py             �?Shared types + utilities
�?├── fishkb/                    �?Independent reusable core (pip install fishkb)
�?  ├── fishkb/db.py           �?KnowledgeDB �?SQLite FTS5
�?  ├── fishkb/search.py       �?FishSpeciesMatcher �?KB-First matching
�?  ├── fishkb/credibility.py  �?Paper credibility scoring
�?  └── fishkb/types.py        �?Core data types
�?├── config/
�?  ├── agent.yaml             �?Agent orchestration config
�?  ├── mcp_servers.yaml       �?21 MCP server definitions
�?  ├── coordination.yaml      �?Cross-project coordination
�?  ├── evolution.yaml         �?Self-evolution parameters
�?  ├── component_registry.yaml �?Living system registry
�?  ├── fish_species_kb.yaml   �?430 species index
�?  └── models.yaml            �?Multi-LLM provider config
�?├── data/
�?  ├── species.db             �?SQLite (species + traits + literature)
�?  ├── FISHMORPH.csv           �?2.3MB global morphology database
�?  └── reports/               �?HTML/CSV exports
�?├── scripts/
�?  ├── credibility_scorer.py  �?Triangulation scoring (0-100)
�?  ├── self_evolve.py         �?6-dimension evolution
�?  ├── kb_to_graph_sync.py    �?KB �?Graph sync
�?  └── taxonomy_sync.py       �?NCBI taxonomy sync
�?├── Dockerfile
├── docker-compose.yml
├── docs/
�?  ├── ARCHITECTURE.md        �?Full 5-layer architecture
�?  ├── SKILL_PIPELINE.md      �?Skill pipeline documentation
�?  └── WORKFLOWS.md           �?Research workflows
�?└── .github/workflows/
    └── validate.yml           �?CI/CD auto-validate
```

---


- **Species coverage**: 430 Yangtze fish species �?most comprehensive open-source dataset
- **KB-First architecture**: SQLite FTS5 enables zero-network species lookup
- **Living system**: Every component has birth date, last verification, and expiry policy
- **Cross-project coordination**: eon-core EventBus + DAG routing for 6-project ecosystem
- **Emergence-aware**: Kalman Filter + �? sources flag emergence

- FishBase sync blocked by SSL in current environment (script ready)
- Some niche Chinese journals have incomplete metadata
- R package version drift monitoring depends on CRAN availability

- [ ] FishBase auto-sync when SSL resolved �?500+ species with Mekong basin
- [ ] Real-time population monitoring dashboard
- [ ] Deep learning morphological trait extraction from images
- [ ] Peer-reviewed publication on KB-First search methodology

---


| Version | Date | Theme | What Changed |
|:--------|:-----|:------|:-------------|
| **v8.1** | 2026-06-20 | README Restoration | Restored from historical sessions: Systems Thinking 7 principles, DeepSeek efficiency principles, 道生万物 architecture, README Changelog, DeepWiki/Dual Core/Docker badges, unified ecosystem with 6 projects |
| **v7.1** | 2026-06-20 | Data sync | + MCP 21 fix, Skills 28 fix, bilingual README sync, cognitive_search in ZH MCP table |
| **v7.0** | 2026-06-10 | lit-search v3.1 | + lit-search v3.1 (synonym expansion→interactive�?2-layer→triangulation), + credibility_scorer.py, + self_evolve.py, + kb_to_graph_sync.py |
| **v6.5** | 2026-06-07 | Cognitive Engine | + DirectLoader protocol, dual-mode search, knowledge graph evolution |
| **v6** | 2026-06-06 | Search v3.0 | 12 search engines (GS-first + CNKI/Wanfang/Baidu/CAS), google-scholar-search skill |
| **v5** | 2026-06-06 | Systems Thinking | + Dual-core philosophy (Panta Rhei + Systems Thinking), 7 principles + 4 DS principles, engineering grammar (18 WHEN→THEN) |
| **v4** | 2026-06-05 | Engineering | Full rewrite: Panta Rhei philosophy, capability comparison, sparse activation |
| **v3** | 2026-06-05 | Panta Rhei | Dynamic worldview integration, emergence detection, calibrated language |
| **v2** | 2026-06-05 | Original | Initial release �?Fish ecology assistant, 5 engines + 12 sub-agents |

---


MIT © 2026 fangtaocai041

---

> **"不要搜索字符串，要重建所指�?**
> Don't search for strings �?reconstruct the signified.


> **Mapped to code**: [Engineering Grammar §8](.reasonix/handbooks/engineering-grammar.md) �?DS-1..DS-4 with formal definitions, WHEN→THEN rules, and config paths.

| ID | Principle | Code Mapping |
|:---|-----------|-------------|
| **DS-1** | **Entropy Budget** �?compute proportional to question importance. PhD �?full pipeline, casual �?single-step. | `pipeline.stages[].activation` + `research-orchestrator` |
| **DS-2** | **Sparse Activation** �?MoE routing: each Skill fires only when condition met. ~2-4/12 active per request. | `pipeline.stages[].activation` + `karpathy-guard` |
| **DS-3** | **Differential Verification** �?P(stale) scoring only changed packages, not full handbook. | `verify-stats-handbook` skill |
| **DS-4** | **Information-Gain Routing** �?P0 exact terms first �?hit-and-stop. P2 redundant terms skipped. Cross-DB dedup. | `ima-smart-search` skill |

---


**Fish Ecology Assistant** is a complete configuration package that transforms Reasonix Code from a general-purpose coding assistant into a professional fish ecology research team. It is the **Knowledge Supply Core (S/V0)** in the SanShengWanWu Triangle Core + Derived six-body architecture, coordinated by **eon-core**.

It integrates **21 MCP tools**, **28 domain-specific skills**, **12-engine parallel search**, an automated **5-stage research pipeline**, **13 IMA knowledge bases**, and an **R statistical computing environment**—all outputs guided by the dynamic worldview above.


| Capability | Vanilla Reasonix | **With This Config** |
|:-----------|:----------------:|:--------------------:|
| Search engines | 1 | **12** (cognitive_search + scholar, article, scholarly, baidu_scholar, cnki, wanfang, cas, ncbi, tavily, exa, web_search) |
| MCP services | 0 | **21** (incl. cognitive_search DirectLoader + DeepWiki) |
| AI subagents | 4 (generic) | **28** (6 pipeline + 20 domain + 2 guard, emergence detection) |
| R statistics | �?| �?R 4.6.0 + 20+ ecology packages |
| OCR | �?| �?PaddleOCR + Tesseract.js |
| Reference manager | �?| �?Direct Zotero SQL queries |
| Research pipeline | �?| �?5-stage + auto-review + emergence detection |
| Knowledge bases | �?| �?13 IMA knowledge bases connected |
| Setup | Manual | �?One script or `docker compose up` |
| CI/CD | �?| �?GitHub Actions auto-validate |
| Engineering rules | �?| �?18 WHEN→THEN rules with code mapping |
| Cross-project | �?| �?fish↔porpoise delegation protocol |

---


> **Check knowledge base first, decide search later.** No more blind 7-engine external search.

```
User Query
    �?    �?┌─────────────────────────�?�? STAGE 1: KB-First      �?�? fishkb search           �?�? ┌───────────────────�? �?�? �?SQLite FTS5        �? �?�? �?30 core species    �? �?�? �?zero-network       �? �?�? └───────┬───────────�? �?�?         �?              �?�?   found? ─── YES ──�?Return immediately
�?     �?�?     NO
�?     �?�?     �?�? STAGE 2: External Search
�? ┌──────────────────────�?�? �?12 engines parallel   �?�? �?�?cognitive_search    �?�? �?�?scholar (GS-first)  �?�? �?�?cnki + wanfang      �?�? �?�?baidu_scholar       �?�? �?�?cas (中科�?         �?�? �?�?ncbi (PubMed)       �?�? �?�?tavily + exa        �?�? �?�?article + scholarly �?�? └──────────────────────�?└─────────────────────────�?```

---



| Skill | Description |
|-------|-------------|
| `research-orchestrator` | Top-level pipeline coordinator |
| `research-planner` | Research question decomposition + strategy |
| `research-executor` | Multi-engine parallel literature search |
| `research-analyst` | Statistical analysis + data interpretation |
| `research-writer` | Bilingual report generation |
| `research-reviewer` | Quality review + contradiction detection |


| Skill | Description |
|-------|-------------|
| `academic-species-search` | Multi-source species academic search |
| `cognitive-species-search` | Cognitive graph species search |
| `unified-species-search` | Unified species search across all engines |
| `fuzzy-species-search` | Fuzzy name matching + OCR variants |
| `google-scholar-search` | Google Scholar targeted search |
| `lit-search` | Comprehensive literature search v3.1 |
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
| `cross-delegate` | Cross-project task delegation protocol |


| Skill | Description |
|-------|-------------|
| `karpathy-guard` | Code quality + safety guard |
| `rule-auditor` | Cross-project rule compliance check |

---


| Category | Tool | Description |
|----------|------|-------------|
| **Search** | `cognitive_search` | **Primary engine** �?DirectLoader, importlib zero-process |
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
| | `ima` | IMA knowledge base search (14 tools) |
| **Compute** | `rplay` | R 4.6.0 statistical computing |
| | `coderunner` | Multi-language code sandbox |
| | `echarts` | Publication-ready chart generation |
| **Image** | `ocr` | PaddleOCR (Chinese/English tables + formulas) |
| | `ocr_fallback` | Tesseract.js offline OCR |
| | `playwright` | Browser automation + scraping |
| **Data** | `git` | Git version control |
| | `github` | GitHub API (repos, issues, PRs) |
| **Knowledge** | `zotero` | Zotero SQLite direct query |

---


> **Dao begets One, One begets Two, Two begets Three, Three begets the Myriad.**
> �?*Dao De Jing*, Chapter 42

```
        �?(Dao)
    外部世界 · 用户的研究问�?    长江生态系统的真实需�?              �?              �?        一 (One)  �?太极
    命令进入系统 · 统一入口
    fish-ecology-assistant
              �?    ┌─────────┴─────────�?    �?                  �?  �?(Yin)           �?(Yang)
  S/V0 · �?          V/V1 · �?  知识供给            搜索验证
  fish                cognitive
    �?                  �?    └────────┬──────────�?             �?矛盾统一
             �?        �?(Three)  �?三体
    三角最小封闭结�?    S + V + Coord
             �?    ┌────────┼────────┬────────�?    �?       �?       �?       �?  P�?      P�?      P�?      C
porpoise  coilia  culter  conflict
    �?       �?       �?       �?    └────────┼────────┼────────�?             �?    万物 (Myriad Things)
    一切事�?· 无限演化
    Skills · Papers · Analyses
```

**不是"一万种物种"。是"一�?�?*

| �?| 中文 | English | 在系统中的含�?|
|----|------|---------|---------------|
| **�?* | 外界, 自然 | Dao �?the external world | 用户的研究问�? 长江生态的现实需�?|
| **一** | 太极, 命令 | One �?the undivided | 命令进入 fish-ecology-assistant, 统一入口 |
| **�?* | 阴阳, 两仪 | Two �?Yin and Yang | S(知识/�? �?V(验证/�?, 太极生两�?|
| **�?* | 三体, 三角 | Three �?the Triangle | fish + cognitive + eon-core, 矛盾统一的封闭结�?|
| **万物** | 一切事�?| Myriad �?all things | 衍生项目 + Skills + 论文 + 输出, 无限演化 |

> **铁律**: 三角密闭 (缺一不可) · 万物开�?(无限衍生) · 三角不依赖万�?· 二生三即矛盾统一

---


```bash
git clone https://github.com/fangtaocai041/fish-ecology-assistant.git
cd fish-ecology-assistant
```

Or with Docker:
```bash
docker compose up
```

Restart Reasonix, everything is ready.

---


| Feature | Status | Description |
|---------|:------:|-------------|
| 🗃�?430 Species DB | �?| Yangtze fish species with bilingual conservation |
| 📏 289 Morphology | �?| FISHMORPH (251) + FishBase + FAO + manual |
| 🌊 Population-level | �?| 26 records with water-body annotation |
| 🔬 Trait Catalog | �?| 61 traits in 7 categories |
| 🏛�?Conservation | �?| IUCN + China Red List + National + CITES |
| 📊 Excel/HTML | �?| Bilingual reports, 2-level headers |
| 🔗 KB-First Search | �?| SQLite FTS5, zero-network for 30 core species |
| 🕸�?Trait Network | �?| Jaccard co-occurrence, keystone traits |
| 📡 Kalman Filter | �?| Emergence detection from noisy data |
| 🔄 Self-Evolution | �?| 7 triggers auto-adapt parameters |
| 📦 fishkb Sub-library | �?| Independent pip-installable core |
| 🎯 score() Adapter | �?| IProjectAdapter.score() for cross-project quality scoring |
| 🔄 FishBase Sync | 🟡 | Script ready, SSL blocked in env |
| 🧪 Living System | �?| Component registry with expiry policies |

---


```
fish-ecology-assistant/
├── README.md                 �?English
├── README.zh.md              �?中文
�?├── .reasonix/
�?  ├── mcp-servers/             �?21 MCP services (incl. deepwiki)
�?  �?  └── ima-server.mjs      �?14 tools
�?  �?�?  ├── skills/                  �?28 AI Skill playbooks
�?  �?  ├── (6 pipeline)  research-orchestrator/planner/executor/analyst/writer/reviewer
�?  �?  ├── (4 search)    academic/cognitive/fuzzy/unified-species-search
�?  �?  ├── (3 research)  frontier-tracker / paper-analyzer / phd-proposal-writer
�?  �?  ├── (3 tools)     ima-smart-search / zotero-assistant / obsidian-assistant
�?  �?  ├── (3 stats)     stats-assistant / stats-method-finder / verify-stats-handbook
�?  �?  ├── (2 guard)     karpathy-guard / rule-auditor
�?  �?  ├── (2 system)    component-health-check / living-system-dashboard
�?  �?  ├── (1 search)    google-scholar-search
�?  �?  ├── (1 debate)    debate-validator
�?  �?  ├── (1 cross)     cross-delegate
�?  �?  └── (1 evolve)    self-evolve
�?  �?�?  ├── handbooks/
�?  �?  ├── systems-thinking.md        �?7 system principles
�?  �?  ├── engineering-grammar.md     �?18 WHEN→THEN rules
�?  �?  ├── activation-matrix.md       �?component coordination
�?  �?  ├── ADVANTAGES.md              �?frontier comparison
�?  �?  ├── WEAKNESSES.md              �?gap analysis
�?  �?  ├── IMPROVEMENT_PLAN.md        �?improvement roadmap
�?  �?  ├── CROSS_PROJECT_PROTOCOL.md  �?cross-agent delegation
�?  �?  ├── DEEPWIKI_INTEGRATION.md    �?DeepWiki integration
�?  �?  ├── LIVING_SYSTEM.md           �?living system implementation
�?  �?  ├── README_UPDATE_RULE.md      �?README sync protocol
�?  �?  └── stats-methods.md           �?statistics methods handbook
�?  �?�?  └── readme-versions/              �?README version archive
�?├── src/                       �?Core Python engine
�?  ├── adapter.py            �?IProjectAdapter + score()
�?  ├── orchestrator.py       �?KB-first species search coordinator
�?  ├── project_hub.py        �?Cross-project coordination (eon-core bridge)
�?  ├── dao_engine.py         �?Philosophical chain executor
�?  └── shared.py             �?Shared types + utilities
�?├── fishkb/                    �?Independent reusable core (pip install fishkb)
�?  ├── fishkb/db.py           �?KnowledgeDB �?SQLite FTS5
�?  ├── fishkb/search.py       �?FishSpeciesMatcher �?KB-First matching
�?  ├── fishkb/credibility.py  �?Paper credibility scoring
�?  └── fishkb/types.py        �?Core data types
�?├── config/
�?  ├── agent.yaml             �?Agent orchestration config
�?  ├── mcp_servers.yaml       �?21 MCP server definitions
�?  ├── coordination.yaml      �?Cross-project coordination
�?  ├── evolution.yaml         �?Self-evolution parameters
�?  ├── component_registry.yaml �?Living system registry
�?  ├── fish_species_kb.yaml   �?430 species index
�?  └── models.yaml            �?Multi-LLM provider config
�?├── data/
�?  ├── species.db             �?SQLite (species + traits + literature)
�?  ├── FISHMORPH.csv           �?2.3MB global morphology database
�?  └── reports/               �?HTML/CSV exports
�?├── scripts/
�?  ├── credibility_scorer.py  �?Triangulation scoring (0-100)
�?  ├── self_evolve.py         �?6-dimension evolution
�?  ├── kb_to_graph_sync.py    �?KB �?Graph sync
�?  └── taxonomy_sync.py       �?NCBI taxonomy sync
�?├── Dockerfile
├── docker-compose.yml
├── docs/
�?  ├── ARCHITECTURE.md        �?Full 5-layer architecture
�?  ├── SKILL_PIPELINE.md      �?Skill pipeline documentation
�?  └── WORKFLOWS.md           �?Research workflows
�?└── .github/workflows/
    └── validate.yml           �?CI/CD auto-validate
```

---


- **Species coverage**: 430 Yangtze fish species �?most comprehensive open-source dataset
- **KB-First architecture**: SQLite FTS5 enables zero-network species lookup
- **Living system**: Every component has birth date, last verification, and expiry policy
- **Cross-project coordination**: eon-core EventBus + DAG routing for 6-project ecosystem
- **Emergence-aware**: Kalman Filter + �? sources flag emergence

- FishBase sync blocked by SSL in current environment (script ready)
- Some niche Chinese journals have incomplete metadata
- R package version drift monitoring depends on CRAN availability

- [ ] FishBase auto-sync when SSL resolved �?500+ species with Mekong basin
- [ ] Real-time population monitoring dashboard
- [ ] Deep learning morphological trait extraction from images
- [ ] Peer-reviewed publication on KB-First search methodology

---


| Version | Date | Theme | What Changed |
|:--------|:-----|:------|:-------------|
| **v8.1** | 2026-06-20 | README Restoration | Restored from historical sessions: Systems Thinking 7 principles, DeepSeek efficiency principles, 道生万物 architecture, README Changelog, DeepWiki/Dual Core/Docker badges, unified ecosystem with 6 projects |
| **v7.1** | 2026-06-20 | Data sync | + MCP 21 fix, Skills 28 fix, bilingual README sync, cognitive_search in ZH MCP table |
| **v7.0** | 2026-06-10 | lit-search v3.1 | + lit-search v3.1 (synonym expansion→interactive�?2-layer→triangulation), + credibility_scorer.py, + self_evolve.py, + kb_to_graph_sync.py |
| **v6.5** | 2026-06-07 | Cognitive Engine | + DirectLoader protocol, dual-mode search, knowledge graph evolution |
| **v6** | 2026-06-06 | Search v3.0 | 12 search engines (GS-first + CNKI/Wanfang/Baidu/CAS), google-scholar-search skill |
| **v5** | 2026-06-06 | Systems Thinking | + Dual-core philosophy (Panta Rhei + Systems Thinking), 7 principles + 4 DS principles, engineering grammar (18 WHEN→THEN) |
| **v4** | 2026-06-05 | Engineering | Full rewrite: Panta Rhei philosophy, capability comparison, sparse activation |
| **v3** | 2026-06-05 | Panta Rhei | Dynamic worldview integration, emergence detection, calibrated language |
| **v2** | 2026-06-05 | Original | Initial release �?Fish ecology assistant, 5 engines + 12 sub-agents |

---


MIT © 2026 fangtaocai041

---

> **"不要搜索字符串，要重建所指�?**
> Don't search for strings �?reconstruct the signified.
