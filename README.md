<div align="center">

```
╔══════════════════════════════════════════════════════════════╗
║  🐟  FISH ECOLOGY ASSISTANT  ·  S/V0 Knowledge Supply Core  ║
║  ──────────────────────────────────────────────────────────  ║
║     Panta Rhei + Systems Thinking  ·  Triangle Core  ·  S   ║
╚══════════════════════════════════════════════════════════════╝
```

🇨🇳 [中文](README.zh.md)

# 🌊 万物皆流 · Panta Rhei

**将您的编码代理变成博士级别的研究团队 — 标准5层代理架构：Panta Rhei + 系统思维。**

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/fangtaocai041/fish-ecology-assistant)
[![Dual Core](https://img.shields.io/badge/dual_core-Panta_Rhei_%2B_Systems_Thinking-6366f1)]()
[![MCP](https://img.shields.io/badge/MCP-21-22c55e)](config/mcp_servers.yaml)
[![Skills](https://img.shields.io/badge/skills-28-f59e0b)](.reasonix/skills/)
[![Architecture](https://img.shields.io/badge/architecture-5_layer-8b5cf6)](docs/ARCHITECTURE.md)
[![Rules](https://img.shields.io/badge/rules-18-8b5cf6)]()
[![Agent](https://img.shields.io/badge/agent-v6.6.0-ec4899)](config/agent.yaml)
[![R](https://img.shields.io/badge/R-4.6.0-276DC3)]()
[![Docker](https://img.shields.io/badge/Docker-ready-2496ED)](Dockerfile)
[![CI](https://img.shields.io/badge/CI-passing-34D058)](.github/workflows/validate.yml)

<p>21 MCP services · 28 AI Skills · 12 search engines · 13 knowledge bases · 18 engineering rules · BDI + ReAct/ToT + MAS · Docker</p>

<p align="center">
  <a href="https://github.com/fangtaocai041/fish-ecology-assistant/stargazers"><img src="https://img.shields.io/github/stars/fangtaocai041/fish-ecology-assistant?style=social" alt="Stars"></a>
  <a href="https://github.com/fangtaocai041/fish-ecology-assistant/network/members"><img src="https://img.shields.io/github/forks/fangtaocai041/fish-ecology-assistant?style=social" alt="Forks"></a>
</p>

</div>

---

## 📑 Table of Contents

- [🧠 Core Philosophy](#-core-philosophy)
- [🐋 DeepSeek Efficiency Principles](#-deepseek-efficiency-principles-效率即智)
- [🔺 Triangle Core Architecture](#-triangle-core--derived-role-sv0-knowledge-supply)
- [🤔 What This Is](#-what-this-is)
- [🧬 KB-First Two-Stage Search](#-kb-first-two-stage-search-v650)
- [🎯 Skills](#-skills)
- [🔌 MCP Tools](#-mcp-tools-21)
- [☯ 道生一 · 一生二 · 二生三 · 三生万物](#-道生一--一生二--二生三--三生万物)
- [🚀 Quick Start](#-quick-start)
- [✨ Features](#-features)
- [📁 Project Structure](#-project-structure)
- [🗺️ Future Roadmap](#-future-roadmap)
- [📋 README Changelog](#-readme-changelog)
- [📜 License](#-license)
- [🌱 Panta Rhei](#-万物皆流--panta-rhei)

---

## 🧠 Core Philosophy

> 🌍 The world is dynamic. 📖 Knowledge is temporary. 🌟 Emergence is the norm.

This is not a slogan. It is the operating system running through every line of code, every search, and every analysis in this project.

### 📜 Three Tenets

**🌍 The world is dynamic** —R packages update, species distributions shift, scientific consensus evolves, climate change reshapes ecosystems. A correct conclusion today may be outdated in six months. We treat no knowledge as eternal truth, but place it on a timeline and view it dynamically.

**📖 Knowledge is temporary** —The foundation of science is falsification (Popper). No discovery is ultimate truth—only the "best current explanation." We use calibrated language: "evidence suggests" not "proves," "Smith (2022) found" not "studies show." Every output carries a temporal anchor.

**🌟 Emergence is the norm** —Life, consciousness, ecosystems, AI reasoning—all are emergent phenomena. You cannot assemble the whole by analyzing only the parts. When ≥3 independent sources point to the same unexpected pattern, the system flags it as an emergence signal—not dismisses it as noise.

### ⚖ Why This Matters for Research

| Scenario | Traditional | Dynamic Worldview |
|:---------|:-----------|:-------------------|
| Package versions | Run 2020 code, ignore version drift | Auto-check, tag "Last verified on glmmTMB v1.1.10" |
| Citations | "Studies prove it" | "Smith (2022) found X, but Jones (2024) added Y" |
| Outliers | Ignore as noise | ≥3 sources → emergence signal, actively track |
| Knowledge decay | Handbook frozen, never updated | Review records include "Next review date" |
| Method selection | Fixed pipeline forever | Dynamic method selection, dynamic confidence |

### 🧠 Systems Thinking · Seven Engineering Principles

| # | Principle | Source | Engineering Mapping |
|---|-----------|--------|---------------------|
| ① | Practice-Knowledge Cycle | *On Practice* (1937) | Data → Model → Verification → Revision (closed loop) |
| ② | Contradiction Analysis | *On Contradiction* (1937) | Identify principal contradiction → focus 2.5x resources |
| ③ | Phased Strategy | *On Protracted War* (1938) | Defense → Stalemate → Counter-offensive = 5-stage pipeline |
| ④ | Concentration of Force | Military thought | 60% compute to principal contradiction |
| ⑤ | Initiative & Agency | *On Protracted War* (1938) | Frontier-tracker proactive suggestions + independent path |
| ⑥ | Differentiated Handling | *On Correct Handling of Contradictions* (1957) | Antagonistic vs non-antagonistic → different strategies |
| ⑦ | Multi-Factor Balance | *On the Ten Major Relationships* (1956) | 10 research balances + multi-objective optimization |

<p align="right"><a href="#-table-of-contents">↑ Back to top</a></p>

---

## 🐋 DeepSeek Efficiency Principles (效率即智

> **Mapped to code**: [Engineering Grammar §8](.reasonix/handbooks/engineering-grammar.md) → DS-1..DS-4 with formal definitions, WHEN→THEN rules, and config paths.

| ID | Principle | Code Mapping |
|:---|-----------|-------------|
| **DS-1** | **Entropy Budget** → compute proportional to question importance. PhD → full pipeline, casual → single-step. | `pipeline.stages[].activation` + `research-orchestrator` |
| **DS-2** | **Sparse Activation** → MoE routing: each Skill fires only when condition met. ~2-4/12 active per request. | `pipeline.stages[].activation` + `karpathy-guard` |
| **DS-3** | **Differential Verification** → P(stale) scoring only changed packages, not full handbook. | `verify-stats-handbook` skill |
| **DS-4** | **Information-Gain Routing** → P0 exact terms first → hit-and-stop. P2 redundant terms skipped. Cross-DB dedup. | `ima-smart-search` skill |

<p align="right"><a href="#-table-of-contents">↑ Back to top</a></p>

---

## 🔺 Triangle Core + Derived Role: **S/V0 (Knowledge Supply)**

> Triangle Core (sealed 3) + Derived (open N) architecture: `fish(S/V0)` →`cognitive(V/V1)` →`eon-core(Coord)`, with `porpoise(P₁` + `coilia(P₂` + `culter(P₃` + `conflict-arbiter(C)` as derived domain experts.
> Provides knowledge, multi-basin fish data (Yangtze 430 + Tumen + Suifen + Amur expanding), contradiction analysis, and ecological findings.
> **D² Plane**: multi-agent debate mesh. **Triangulation**: ≥3 sources.
> Coordinated by [eon-core](https://github.com/fangtaocai041/eon-core).

## 🤔 What This Is

**Fish Ecology Assistant** is a complete configuration package that transforms Reasonix Code from a general-purpose coding assistant into a professional fish ecology research team. It is the **Knowledge Supply Core (S/V0)** in the SanShengWanWu Triangle Core + Derived six-body architecture, coordinated by **eon-core**.

It integrates **21 MCP tools**, **28 domain-specific skills**, **12-engine parallel search**, an automated **5-stage research pipeline**, **13 IMA knowledge bases**, and an **R statistical computing environment**—all outputs guided by the dynamic worldview above.

### 📊 Capability Matrix

| Capability | Vanilla Reasonix | **With This Config** |
|:-----------|:----------------:|:--------------------:|
| Search engines | 1 | **12** (cognitive_search + scholar, article, scholarly, baidu_scholar, cnki, wanfang, cas, ncbi, tavily, exa, web_search) |
| MCP services | 0 | **21** (incl. cognitive_search DirectLoader + DeepWiki) |
| AI subagents | 4 (generic) | **28** (6 pipeline + 20 domain + 2 guard, emergence detection) |
| R statistics | ✅ | ✅ R 4.6.0 + 20+ ecology packages |
| OCR | ✅ | ✅ PaddleOCR + Tesseract.js |
| Reference manager | ✅ | ✅ Direct Zotero SQL queries |
| Research pipeline | ✅ | ✅ 5-stage + auto-review + emergence detection |
| MAGMA 4D memory | ✅ | ✅ 正交图谱 + NetworkX 图分析 |
| China conservation | ✅ | ✅ IUCN + 中国红色名录双对照 |
| Knowledge bases | ✅ | ✅ 13 IMA knowledge bases connected |
| Setup | Manual | ✅ One script or `docker compose up` |
| CI/CD | ✅ | ✅ GitHub Actions auto-validate |
| Engineering rules | ✅ | ✅ 18 WHEN→THEN rules with code mapping |
| Cross-project | ✅ | ✅ fish↔porpoise delegation protocol |

<p align="right"><a href="#-table-of-contents">↑ Back to top</a></p>

---

## 🧬 KB-First Two-Stage Search (v6.5.0)

> **Check knowledge base first, decide search later.** No more blind 7-engine external search.

```
User Query
    ?    ?┌─────────────────────────?? STAGE 1: KB-First      ?? fishkb search           ?? ┌───────────────────? ?? → SQLite FTS5        ? ?? ?30 core species    ? ?? ?zero-network       ? ?? └───────┬───────────? ??         ?              ??   found? ─── YES ──?Return immediately
?     ??     NO
?     ??     ?? STAGE 2: External Search
? ┌──────────────────────?? ?12 engines parallel   ?? ??cognitive_search    ?? ??scholar (GS-first)  ?? ??cnki + wanfang      ?? ??baidu_scholar       ?? ??cas (中科?         ?? ??ncbi (PubMed)       ?? ??tavily + exa        ?? ??article + scholarly ?? └──────────────────────?└─────────────────────────?```
```

---

## 🎯 Skills

<details open>
<summary><b>📋 Pipeline Skills (6)</b></summary>

| Skill | Description |
|-------|-------------|
| `research-orchestrator` | Top-level pipeline coordinator |
| `research-planner` | Research question decomposition + strategy |
| `research-executor` | Multi-engine parallel literature search |
| `research-analyst` | Statistical analysis + data interpretation |
| `research-writer` | Bilingual report generation |
| `research-reviewer` | Quality review + contradiction detection |

</details>

<details>
<summary><b>🌐 Domain Skills (20)</b></summary>

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

</details>

<details>
<summary><b>🛡️ Guard Skills (2)</b></summary>

| Skill | Description |
|-------|-------------|
| `karpathy-guard` | Code quality + safety guard |
| `rule-auditor` | Cross-project rule compliance check |

</details>

<p align="right"><a href="#-table-of-contents">↑ Back to top</a></p>

---

## 🔌 MCP Tools (21)

<details>
<summary><b>🔍 Search (12 tools)</b></summary>

| Tool | Description |
|------|-------------|
| `cognitive_search` | **Primary engine** ✅ DirectLoader, importlib zero-process |
| `scholar` | Google Scholar literature search |
| `article` | PMC full-text + journal quality (EasyScholar/OpenAlex) |
| `scholarly` | Multi-source academic cross-database search |
| `baidu_scholar` | Baidu Scholar Chinese academic search |
| `cnki` | CNKI Chinese journal database |
| `wanfang` | Wanfang Chinese academic database |
| `cas` | CAS (Chinese Academy of Sciences) literature |
| `ncbi` | NCBI PubMed + Europe PMC |
| `tavily` | AI-powered deep web search |
| `exa` | Semantic web search |
| `ima` | IMA knowledge base search (14 tools) |

</details>

<details>
<summary><b>⚡ Compute & Image & Data (9 tools)</b></summary>

| Category | Tool | Description |
|----------|------|-------------|
| **Compute** | `rplay` | R 4.6.0 statistical computing |
| | `coderunner` | Multi-language code sandbox |
| | `echarts` | Publication-ready chart generation |
| **Image** | `ocr` | PaddleOCR (Chinese/English tables + formulas) |
| | `ocr_fallback` | Tesseract.js offline OCR |
| | `playwright` | Browser automation + scraping |
| **Data** | `git` | Git version control |
| | `github` | GitHub API (repos, issues, PRs) |
| **Knowledge** | `zotero` | Zotero SQLite direct query |

</details>

<p align="right"><a href="#-table-of-contents">↑ Back to top</a></p>

---

## ☯ 道生一 · 一生二 · 二生三 · 三生万物

> **Dao begets One, One begets Two, Two begets Three, Three begets the Myriad.**
> — *Dao De Jing*, Chapter 42

```
        道(Dao)
    外部世界 · 用户的研究问题    长江生态系统的真实需求              ?              ?        一 (One)  ?太极
    命令进入系统 · 统一入口
    fish-ecology-assistant
              ?    ┌─────────┴─────────?    ?                  ?  陰(Yin)           陽(Yang)
  S/V0 · ?          V/V1 · ?  知识供给            搜索验证
  fish                cognitive
    ?                  ?    └────────┬──────────?             ?矛盾统一
             ?        三(Three)  ?三体
    三角最小封闭结构    S + V + Coord
             ?    ┌────────┼────────┬────────?    ?       ?       ?       ?  P?      P?      P?      C
porpoise  coilia  culter  conflict
    ?       ?       ?       ?    └────────┼────────┼────────?             ?    万物 (Myriad Things)
    一切事物· 无限演化
    Skills · Papers · Analyses
```

**不是"一万种物种"。是"一"。**

| 道 | 中文 | English | 在系统中的含义 |
|----|------|---------|---------------|
| **道** | 外界, 自然 | Dao — the external world | 用户的研究问题 长江生态的现实需求 |
| **一** | 太极, 命令 | One — the undivided | 命令进入 fish-ecology-assistant, 统一入口 |
| **二** | 阴阳, 两仪 | Two — Yin and Yang | S(知识/阴) ?V(验证/阳), 太极生两仪|
| **三** | 三体, 三角 | Three — the Triangle | fish + cognitive + eon-core, 矛盾统一的封闭结构|
| **万物** | 一切事物| Myriad — all things | 衍生项目 + Skills + 论文 + 输出, 无限演化 |

> **铁律**: 三角密闭 (缺一不可) · 万物开放(无限衍生) · 三角不依赖万物· 二生三即矛盾统一

<p align="right"><a href="#-table-of-contents">↑ Back to top</a></p>

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

<p align="right"><a href="#-table-of-contents">↑ Back to top</a></p>

---

## ✨ Features

| Feature | Status | Description |
|---------|:------:|-------------|
| 🗃?430 Species DB | ✅ | Yangtze fish species with bilingual conservation |
| 📏 289 Morphology | ✅ | FISHMORPH (251) + FishBase + FAO + manual |
| 🌊 Population-level | ✅ | 26 records with water-body annotation |
| 🔬 Trait Catalog | ✅ | 61 traits in 7 categories |
| 🏛?Conservation | ✅ | IUCN + China Red List + National + CITES |
| 📊 Excel/HTML | ✅ | Bilingual reports, 2-level headers |
| 🔗 KB-First Search | ✅ | SQLite FTS5, zero-network for 30 core species |
| 🕸?Trait Network | ✅ | Jaccard co-occurrence, keystone traits |
| 📡 Kalman Filter | ✅ | Emergence detection from noisy data |
| 🔄 Self-Evolution | ✅ | 7 triggers auto-adapt parameters |
| 📦 fishkb Sub-library | ✅ | Independent pip-installable core |
| 🎯 score() Adapter | ✅ | IProjectAdapter.score() for cross-project quality scoring |
| 🔄 FishBase Sync | 🟡 | Script ready, SSL blocked in env |
| 🧪 Living System | ✅ | Component registry with expiry policies |

<p align="right"><a href="#-table-of-contents">↑ Back to top</a></p>

---

## 📁 Project Structure

```
fish-ecology-assistant/
├── README.md                 📄 English
├── README.zh.md              📄 中文
│   ├── .reasonix/
│   ├── mcp-servers/             📡 21 MCP services (incl. deepwiki)
│   │   └── ima-server.mjs      🔧 14 tools
│   │   ├── skills/                  📚 28 AI Skill playbooks
│   │   ├── (6 pipeline)  research-orchestrator/planner/executor/analyst/writer/reviewer
│   │   ├── (4 search)    academic/cognitive/fuzzy/unified-species-search
│   │   ├── (3 research)  frontier-tracker / paper-analyzer / phd-proposal-writer
│   │   ├── (3 tools)     ima-smart-search / zotero-assistant / obsidian-assistant
│   │   ├── (3 stats)     stats-assistant / stats-method-finder / verify-stats-handbook
│   │   ├── (2 guard)     karpathy-guard / rule-auditor
│   │   ├── (2 system)    component-health-check / living-system-dashboard
│   │   ├── (1 search)    google-scholar-search
│   │   ├── (1 debate)    debate-validator
│   │   ├── (1 cross)     cross-delegate
│   │   └── (1 evolve)    self-evolve
│   │   ├── handbooks/
│   │   ├── systems-thinking.md        📋 7 system principles
│   │   ├── engineering-grammar.md     → 18 WHEN→THEN rules
│   │   ├── activation-matrix.md       📋 component coordination
│   │   ├── ADVANTAGES.md              📋 frontier comparison
│   │   ├── WEAKNESSES.md              📋 gap analysis
│   │   ├── IMPROVEMENT_PLAN.md        📋 improvement roadmap
│   │   ├── CROSS_PROJECT_PROTOCOL.md  📋 cross-agent delegation
│   │   ├── DEEPWIKI_INTEGRATION.md    📋 DeepWiki integration
│   │   ├── LIVING_SYSTEM.md           📋 living system implementation
│   │   ├── README_UPDATE_RULE.md      📋 README sync protocol
│   │   └── stats-methods.md           📋 statistics methods handbook
│   │   └── readme-versions/              📋 README version archive
│   ├── src/                       🐍 Core Python engine
│   ├── adapter.py            🔌 IProjectAdapter + score()
│   ├── orchestrator.py       🔍 KB-first species search coordinator
│   ├── project_hub.py        🔗 Cross-project coordination (eon-core bridge)
│   ├── dao_engine.py         ☯ Philosophical chain executor
│   └── shared.py             📦 Shared types + utilities
│   ├── fishkb/                    📦 Independent reusable core (pip install fishkb)
│   ├── fishkb/db.py           🗄️ KnowledgeDB → SQLite FTS5
│   ├── fishkb/search.py       🔍 FishSpeciesMatcher → KB-First matching
│   ├── fishkb/credibility.py  📊 Paper credibility scoring
│   └── fishkb/types.py        📋 Core data types
│   ├── config/
│   ├── agent.yaml             🎯 Agent orchestration config
│   ├── mcp_servers.yaml       📡 21 MCP server definitions
│   ├── coordination.yaml      🔗 Cross-project coordination
│   ├── evolution.yaml         🔄 Self-evolution parameters
│   ├── component_registry.yaml 🧪 Living system registry
│   ├── fish_species_kb.yaml   📋 430 species index
│   └── models.yaml            🤖 Multi-LLM provider config
│   ├── data/
│   ├── species.db             🗄️ SQLite (species + traits + literature)
│   ├── FISHMORPH.csv           📦 2.3MB global morphology database
│   └── reports/               📊 HTML/CSV exports
│   ├── scripts/
│   ├── credibility_scorer.py  📊 Triangulation scoring (0-100)
│   ├── self_evolve.py         🔄 6-dimension evolution
│   ├── kb_to_graph_sync.py    🔗 KB → Graph sync
│   └── taxonomy_sync.py       🧬 NCBI taxonomy sync
│   ├── Dockerfile
├── docker-compose.yml
├── docs/
│   ├── ARCHITECTURE.md        🏗️ Full 5-layer architecture
│   ├── SKILL_PIPELINE.md      📚 Skill pipeline documentation
│   └── WORKFLOWS.md           🔬 Research workflows
│   └── .github/workflows/
    └── validate.yml           ✅ CI/CD auto-validate
```

<p align="right"><a href="#-table-of-contents">↑ Back to top</a></p>

---

## 🗺️ Future Roadmap

### 💪 Strengths
- **Species coverage**: 430 Yangtze fish species  — most comprehensive open-source dataset
- **KB-First architecture**: SQLite FTS5 enables zero-network species lookup
- **Living system**: Every component has birth date, last verification, and expiry policy
- **Cross-project coordination**: eon-core EventBus + DAG routing for 6-project ecosystem
- **Emergence-aware**: Kalman Filter + ≥3 sources flag emergence

### ⚠️ Known Limitations
- FishBase sync blocked by SSL in current environment (script ready)
- Some niche Chinese journals have incomplete metadata
- R package version drift monitoring depends on CRAN availability

### 🎯 Milestones
- [ ] FishBase auto-sync when SSL resolved → 500+ species with Mekong basin
- [ ] Real-time population monitoring dashboard
- [ ] Deep learning morphological trait extraction from images
- [ ] Peer-reviewed publication on KB-First search methodology

<p align="right"><a href="#-table-of-contents">↑ Back to top</a></p>

---

## 📋 README Changelog

| Version | Date | Theme | What Changed |
|:--------|:-----|:------|:-------------|
| **v8.1** | 2026-06-18 | README Restoration | Restored from historical sessions: Systems Thinking 7 principles, DeepSeek efficiency principles, 道生万物 architecture, README Changelog, DeepWiki/Dual Core/Docker badges, unified ecosystem with 6 projects |
| **v7.1** | 2026-06-18 | Data sync | + MCP 21 fix, Skills 28 fix, bilingual README sync, cognitive_search in ZH MCP table |
| **v7.0** | 2026-06-10 | lit-search v3.1 | + lit-search v3.1 (synonym expansion→interactive → 2-layer→triangulation), + credibility_scorer.py, + self_evolve.py, + kb_to_graph_sync.py |
| **v6.5** | 2026-06-07 | Cognitive Engine | + DirectLoader protocol, dual-mode search, knowledge graph evolution |
| **v6** | 2026-06-06 | Search v3.0 | 12 search engines (GS-first + CNKI/Wanfang/Baidu/CAS), google-scholar-search skill |
| **v5** | 2026-06-06 | Systems Thinking | + Dual-core philosophy (Panta Rhei + Systems Thinking), 7 principles + 4 DS principles, engineering grammar (18 WHEN→THEN) |
| **v4** | 2026-06-05 | Engineering | Full rewrite: Panta Rhei philosophy, capability comparison, sparse activation |
| **v3** | 2026-06-05 | Panta Rhei | Dynamic worldview integration, emergence detection, calibrated language |
| **v2** | 2026-06-05 | Original | Initial release  — Fish ecology assistant, 5 engines + 12 sub-agents |

<p align="right"><a href="#-table-of-contents">↑ Back to top</a></p>

---

## 📜 License

MIT © 2026 fangtaocai041

---

## 🌱 万物皆流 · Panta Rhei

> **"不要搜索字符串，要重建所指。"**
> *Don't search for strings — reconstruct the signified.*

> Heraclitus said: No man ever steps in the same river twice.
>
> We say: Knowledge ages, but humanity's quest to understand the world never ends. Yesterday's truth becomes today's foundation. Today's unknown becomes tomorrow's journey. Our gaze is never confined to the known; our steps will one day tread upon that vast, star-lit frontier.

This project is not a fixed toolkit — it is a **living system**. Every component has built-in expiry mechanisms, version tracking, and emergence awareness. As your research deepens, R packages update, and new methods emerge, it evolves with you.


> 🔧 Agent constraints: [AGENTS.md](../AGENTS.md) · [core-constitution.md](../.reasonix/core-constitution.md) · [research-first](../skills/research-first.md) · [retro-session](../skills/retro-session.md)

*Last updated: 2026-06-18 | Environment: Reasonix Code · DeepSeek-powered*

---

<div align="center">

### 🏷️ Tech & Topics

`research` `ecology` `fisheries` `ai-agent` `llm` `reasonix` `mcp` `r-stats` `docker` `panta-rhei` `systems-thinking`

<br>

<sub>🐟 Part of the **SanShengWanWu** ecosystem · Coordinated by [eon-core](https://github.com/fangtaocai041/eon-core)</sub>

</div>


---

## 🧬 RCCA 集成 (v2.1.0 便携核心)

本项目已集成 [san-sheng-wanwu-core](https://github.com/fangtaocai041/san-sheng-wanwu-core) 的便携 RCCA 核心模块。

### 已部署的核心能力

| 模块 | 类名 | 用途 |
|:-----|:-----|:-----|
| 阻尼自我模型 | `SelfModelEngine` | 预测误差滑动窗口 → 稳定性检测 |
| 资源分配策略 | `EmotionEngine` | 事件驱动策略选择 → 行为倾向 |
| 概念转座层 | `TranspositionLayer` | 跳跃基因逻辑: 跨域推理模式迁移 |
| 反思循环 | `ReflectionLoop` | 递归思考→转座→自我适应闭环 |

### 快速开始

```python
from src.rcca_core import SelfModelEngine, EmotionEngine, TranspositionLayer, ReflectionLoop

# 初始化自我模型
sm = SelfModelEngine()
state = sm.reflect()  # 稳定性自检

# 情感驱动的转座
tl = TranspositionLayer()
e = EmotionEngine(transposition_layer=tl)
e.stimulate("discovery", 0.8)  # 发现新知识 → 自动推送到转座层

# 跨域转座：将搜索策略从 A 通道迁移到 B 通道
result = tl.transpose("search", "verify", {"concept": "cross_domain", "confidence": 0.9})

# 反思循环
loop = ReflectionLoop()
report = loop.run(["scholar", "cnki", "ncbi"], transposition=tl)
```

### 版本

核心版本: **RCCA v2.1.0** (2026-06-20) · 零外部依赖 · 即插即用
