<p align="center">
  🇨🇳 <a href="README.zh.md">中文</a>
</p>

<div align="center">
  <h1>🌊 Panta Rhei · Everything Flows</h1>
  <p><strong>Turn your coding agent into a PhD-level research team — Standard 5-Layer Agent Architecture: Panta Rhei + Systems Thinking.</strong></p>
  <p>21 MCP services · 25 AI Skills · 11 search engines · 13 knowledge bases · 18 engineering rules · BDI + ReAct/ToT + MAS · Docker</p>
</div>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square" alt="License"></a>
  <a href="https://deepwiki.com/fangtaocai041/fish-ecology-assistant"><img src="https://devin.ai/assets/askdeepwiki.png" alt="Ask DeepWiki" height="20"></a>
  <a href="#"><img src="https://img.shields.io/badge/dual_core-Panta_Rhei_%2B_Systems_Thinking-6366f1?style=flat-square" alt="Dual Core"></a>
  <a href="#"><img src="https://img.shields.io/badge/MCP-21-22c55e?style=flat-square" alt="MCP:21"></a>
  <a href="#"><img src="https://img.shields.io/badge/skills-25-f59e0b?style=flat-square" alt="Skills:25"></a>
  <a href="docs/ARCHITECTURE.md"><img src="https://img.shields.io/badge/architecture-5_layer-8b5cf6?style=flat-square" alt="Architecture:5-Layer"></a>
  <a href="#"><img src="https://img.shields.io/badge/rules-18-8b5cf6?style=flat-square" alt="Rules:18"></a>
</p>

---

## 🔺 S-T-V Triangle Role: **State (S)**

> Part of the S-T-V rigid triangle: `fish(S) → porpoise(T) → cognitive(V) → fish(S)`
> Provides knowledge, data, contradiction analysis, and findings to the pipeline.
> **D₂ Plane**: multi-agent debate mesh (`debate-validator`). **Triangulation**: ≥3 sources.

## 🏛️ Architecture · Standard 5-Layer Agent Model

> See full documentation at [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)
> **5 Layers**: Interaction & Perception → Cognitive & Decision → Memory System → Mapping & Translation → Tool & Execution
> **Theoretical Foundations**: BDI (Belief-Desire-Intention) · MDP/POMDP Formalism · ReAct/ToT/GoT Reasoning · Reflexion Self-Correction · MAS Multi-Agent Topology

## 🧠 Core Philosophy

> 🧠 **Dual-Core Engine**: Panta Rhei (worldview) + Systems Thinking (methodology)
> What the world IS — dynamic, provisional, emergent. How we ACT — analyze contradictions, verify through practice, advance in phases, concentrate force.
> **All philosophy mapped to executable code** via [Engineering Grammar](.reasonix/handbooks/engineering-grammar.md) — every principle has a precise `WHEN→THEN` rule, config path, and Skill trigger.
> See `.reasonix/handbooks/systems-thinking.md` (philosophy) + `.reasonix/handbooks/engineering-grammar.md` (code mapping)

---

### 🌍 Panta Rhei · Dynamic Worldview

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

<p align=right>(<a href=#readme-top>back to top</a>)</p>

---

## 🐋 DeepSeek Efficiency Principles (效率即智能)

> **Mapped to code**: [Engineering Grammar §8](.reasonix/handbooks/engineering-grammar.md) — DS-1..DS-4 with formal definitions, WHEN→THEN rules, and config paths.

Energy is finite. Computation has a cost. DeepSeek does not scale parameters — it scales algorithms.

| ID | Principle | Code Mapping |
|:---|-----------|-------------|
| **DS-1** | **Entropy Budget** — compute proportional to question importance. PhD → full pipeline, casual → single-step. | `pipeline.stages[].activation` + `research-orchestrator` |
| **DS-2** | **Sparse Activation** — MoE routing: each Skill fires only when condition met. ~2-4/12 active per request. | `pipeline.stages[].activation` + `karpathy-guard` |
| **DS-3** | **Differential Verification** — P(stale) scoring only changed packages, not full handbook. Review cycle = f(update_freq, risk, dependency). | `verify-stats-handbook` skill |
| **DS-4** | **Information-Gain Routing** — P0 exact terms first → stop on hit. P2 redundant skipped. Cross-KB dedup. | `ima-smart-search` skill |

## 🤔 What Is This

**Fish Ecology Assistant** transforms [Reasonix Code](https://github.com/esengine/deepseek-reasonix) from a general-purpose coding agent into a **domain-specialized fish ecology research team** — with 18 MCP tools, 14 AI subagents, a 5-stage auto-orchestrated research pipeline, R statistics, 13 knowledge bases, and 18 engineering rules. All outputs follow the dual-core philosophy above.

| Capability | Vanilla Reasonix | **With This Config** |
|:-----------|:----------------:|:--------------------:|
| Search engines | 1 | **12** (cognitive_search + scholar, article, scholarly, baidu_scholar, cnki, wanfang, cas, ncbi, tavily, exa, web_search) |
| MCP services | 0 | **19** (incl. DeepWiki + cognitive-search-mcp) |
| AI subagents | 4 (generic) | **14** (domain-specialized, rule-auditor, emergence detection) |
| R statistics | — | ✅ R 4.6.0 + 20+ ecology packages |
| OCR | — | ✅ PaddleOCR + Tesseract.js |
| Reference manager | — | ✅ Direct Zotero SQL queries |
| Research pipeline | — | ✅ 5-stage + auto-review + emergence detection |
| Knowledge bases | — | ✅ 13 ima knowledge bases connected |
| Setup on new machine | Manual | ✅ One script or `docker compose up` |
| CI/CD | — | ✅ GitHub Actions auto-validate |
| Engineering rules | — | ✅ 18 WHEN→THEN rules with code mapping |
| Cross-project | — | ✅ fish↔porpoise delegation protocol |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## ⚡ Quick Start

```bash
git clone https://github.com/fangtaocai041/fish-ecology-assistant.git
cd fish-ecology-assistant
powershell -ExecutionPolicy Bypass -File .reasonix\setup-migrate.ps1
```

Or with Docker:
```bash
docker compose up
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
| ② | `research-executor` | 🔍 Search | 11 engines parallel (GS priority + 4 Chinese sources), annotates publication year |
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
| 🛡️ `karpathy-guard` | Behavior guardrails | Entropy budget + sparse activation, MoE routing |
| 🔍 `rule-auditor` | Rule compliance audit | Scans all Skills for 18-rule coverage |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 📡 MCP Services (18 Tools)

| Service | Engine | Best For |
|:--------|:-------|:---------|
| `cognitive_search` | **CognitiveSearch (DirectLoader)** | **核心搜索引擎** · importlib 加载, 引擎更新自动生效, 双模式(轻量/完整) |
| `scholar` | **Google Scholar** | **优先搜索引擎** · 学术论文 |
| `article` | Article metadata | 全文摘要 |
| `scholarly` | Multi-source | 跨数据库搜索 |
| `baidu_scholar` | 百度学术 (site:) | 中文论文 |
| `cnki` | 知网 CNKI (site:) | 中文核心期刊 |
| `wanfang` | 万方数据 (site:) | 中文学位论文 |
| `cas` | 中科院 IHBCAS (site:) | 水生所/动物所出版物 |
| `ncbi` | PubMed | 生物医学文献 |
| `tavily` | AI deep search | 广泛网页内容 |
| `exa` | Semantic search | 语义级搜索 |
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

---

## 🧠 Cognitive Search Engine · DirectLoader Protocol

> **Core search infrastructure shared across all three projects** under `D:\Reasonix\`

The cognitive-search-engine is the **central perception layer** — not a remote MCP server, but a local Python module loaded via `importlib`:

### Architecture

```
LiteratureAgent (Reasonix)
  └─ CognitiveSearchAdapter.search(genus, species, full_pipeline=True|False)
       ├─ importlib → D:\Reasonix\cognitive-search-engine\src\   ← 引擎更新自动生效
       │
       ├─ full_pipeline=False (轻量模式)
       │   ├─ variant_generator.generate()    → OCR 变体列表 (Ochetobius→Ochetobibus)
       │   ├─ build_search_queries()          → 精确名 + 变体 + 中文名
       │   └─ ParallelSearch.search_all()     → PubMed × Crossref × OpenAlex 并行
       │
       └─ full_pipeline=True (完整管线)
           └─ CognitiveAgent.search()
               ├─ Layer 1 (Perception)   → 输入 + query 形成
               ├─ Layer 2 (Cognitive)    → BDI phase 选择 (Think)
               ├─ Layer 3 (Memory)       → graph_lookup (0 token) + 轨迹记录
               ├─ Layer 4 (Mapping)      → 意图 → 搜索工具映射
               └─ Layer 5 (Execution)    → Act + Observe + Reflect
                   └─ 循环: Think → Act → Observe → Reflect
                       停止条件: Desire满足 / budget耗尽 / diminishing returns
```

### Dual-Mode Selection

| 场景 | 模式 | 原因 |
|------|:----:|------|
| 文献量 > 200（满意模式） | `full_pipeline=False` | `ParallelSearch` 8-12 篇即够 |
| 文献量 20-200（分类归纳） | `full_pipeline=True` | 需要 Phase 分类 + 用户选方向 |
| 文献量 < 20（穷举法） | `full_pipeline=True` | 全 12 层 + 引用遍历 + 作者回溯 |
| 需要引用图遍历 | `full_pipeline=True` | 轻量模式无 `citation_traversal` |

### Three Breakthroughs

| # | 特性 | 说明 |
|---|------|------|
| ① | **DirectLoader (零进程)** | `importlib` 直接从 `D:\Reasonix\cognitive-search-engine\src\` 加载 `.py` 模块，引擎更新后下次导入自动生效，无 MCP 进程开销 |
| ② | **Dual-Mode Search** | 轻量 `ParallelSearch` 覆盖 80% 场景；完整 `CognitiveAgent` 提供 5 层 BDI ReAct 循环，包括 phase 选择、IG 追踪、自适应停止 |
| ③ | **知识图谱进化** | `species_graph.yaml` 积累已知论文、变体、作者、引用边；graph_lookup 阶段 0 token 复用；图谱在三项目间共享 |

### Cross-Project Sharing

```
D:\Reasonix\
├── cognitive-search-engine\    ← 引擎唯一代码源（配置 + 源码 + 图谱）
├── fish-ecology-assistant\     ← submodule 引用
└── porpoise-agent\             ← submodule 引用
```

引擎进化一次，三个项目同步受益。

### Quick Reference

- 引擎源码: `D:\Reasonix\cognitive-search-engine\src\`
- 搜索协议: `config/search_rules.yaml`
- 物种图谱: `config/species_graph.yaml`
- 适配器入口: `CognitiveSearchAdapter.search(genus, species, full_pipeline)`

---

## 📁 Project Structure

```
fish-ecology-assistant/
├── README.md                 ← English
├── README.zh.md              ← 中文
│
├── .reasonix/
│   ├── mcp-servers/             ← 21 MCP services (incl. deepwiki)
│   │   └── ima-server.mjs      ← 14 tools (KB + notes + discovery + multi-search)
│   │
│   ├── skills/                  ← 14 AI subagent playbooks
│   │   ├── karpathy-guard.md          ← Sparse activation + MoE routing
│   │   ├── rule-auditor.md            ← 18-rule compliance checker
│   │   ├── ima-smart-search.md        ← Cross-KB intelligent search
│   │   ├── verify-stats-handbook.md   ← Auto CRAN version check
│   │   ├── research-orchestrator.md   ← 5-stage pipeline coordinator
│   │   └── ... (9 more skills)
│   │
│   ├── handbooks/
│   │   ├── systems-thinking.md        ← 7 system principles
│   │   ├── engineering-grammar.md     ← 18 WHEN→THEN rules
│   │   ├── activation-matrix.md       ← Component coordination
│   │   ├── ADVANTAGES.md              ← Frontier comparison
│   │   ├── WEAKNESSES.md              ← Gap analysis
│   │   ├── IMPROVEMENT_PLAN.md        ← Improvement roadmap
│   │   ├── CROSS_PROJECT_PROTOCOL.md  ← Cross-agent delegation
│   │   ├── DEEPWIKI_INTEGRATION.md    ← DeepWiki adoption
│   │   ├── README_UPDATE_RULE.md      ← README sync protocol
│   │   ├── stats-methods.md           ← Stats handbook
│   │   └── learning-guide.md          ← Learning path
│   │
│   ├── .github/workflows/validate.yml ← CI/CD auto-validation
│   ├── Dockerfile                     ← Docker deployment
│   └── setup-migrate.ps1              ← One-click setup
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

**Last updated: 2026-06-07**
**Running on Reasonix Code · Powered by DeepSeek**

---

## 📋 README Changelog

> Versioned copies preserved in `.reasonix/readme-versions/`

| Version | Date | Theme | What Changed |
|:--------|:-----|:------|:-------------|
| **v6** | 2026-06-07 | Cognitive Search Engine | + DirectLoader 协议 (importlib 零进程加载), 双模式搜索 (ParallelSearch 轻量 / CognitiveAgent 完整 BDI ReAct), 知识图谱进化, 三项目共享引擎\n| **v5** | 2026-06-06 | Search v3.0 | 11 搜索引擎 (GS优先 + 知网/万方/百度学术/中科院), google-scholar-search skill, 鳤文献全面检索 |\n| **v4** | 2026-06-06 | Systems Thinking | + Dual-core philosophy (Panta Rhei + Maoist systems thinking), 7 system + 4 DeepSeek efficiency principles, Engineering Grammar (18 WHEN→THEN rules), full code mapping |
| **v3** | 2026-06-05 | Engineering | Complete rewrite: Panta Rhei philosophy, capability comparison, engineering efficiency principles, sparse activation |
| **v2** | 2026-06-05 | Panta Rhei | Dynamic worldview integration, emergence detection, calibrated language |
| **v1** | 2026-06-05 | Original | Initial release — fish ecology research assistant with 5 search engines + 12 subagents |

<p align=right>(<a href=#readme-top>back to top</a>)</p>
