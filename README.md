<p align="center">
  🇨🇳 <a href="README.zh.md">中文</a>
</p>

<div align="center">
  <h1>🌊 Panta Rhei · Everything Flows</h1>
  <p><strong>Turn your coding agent into a PhD-level research team — dual-core philosophy: Panta Rhei + Systems Thinking.</strong></p>
  <p>18 MCP tools · 14 AI subagents · 5 search engines · 13 knowledge bases · 18 engineering rules · Docker</p>
</div>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square" alt="License"></a>
  <a href="https://deepwiki.com/fangtaocai041/fish-ecology-assistant"><img src="https://devin.ai/assets/askdeepwiki.png" alt="Ask DeepWiki" height="20"></a>
  <a href="#"><img src="https://img.shields.io/badge/dual_core-Panta_Rhei_%2B_Systems_Thinking-6366f1?style=flat-square" alt="Dual Core"></a>
  <a href="#"><img src="https://img.shields.io/badge/MCP-18-22c55e?style=flat-square" alt="MCP:18"></a>
  <a href="#"><img src="https://img.shields.io/badge/subagents-14-f59e0b?style=flat-square" alt="Subagents:14"></a>
  <a href="#"><img src="https://img.shields.io/badge/rules-18-8b5cf6?style=flat-square" alt="Rules:18"></a>
</p>

---

## 🏛️ Core Philosophy

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
| Search engines | 1 | **5** (tavily, exa, scholar, article, scholarly) |
| MCP services | 0 | **18** (incl. DeepWiki) |
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
| 🛡️ `karpathy-guard` | Behavior guardrails | Entropy budget + sparse activation, MoE routing |
| 🔍 `rule-auditor` | Rule compliance audit | Scans all Skills for 18-rule coverage |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 📡 MCP Services (18 Tools)

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
│   ├── mcp-servers/             ← 18 MCP wrappers (incl. deepwiki)
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

**Last updated: 2026-06-06**
**Running on Reasonix Code · Powered by DeepSeek**

---

## 📋 README Changelog

> Versioned copies preserved in `.reasonix/readme-versions/`

| Version | Date | Theme | What Changed |
|:--------|:-----|:------|:-------------|
| **v4** | 2026-06-06 | Systems Thinking | + Dual-core philosophy (Panta Rhei + Maoist systems thinking), 7 system + 4 DeepSeek efficiency principles, Engineering Grammar (18 WHEN→THEN rules), full code mapping |
| **v3** | 2026-06-05 | Engineering | Complete rewrite: Panta Rhei philosophy, capability comparison, engineering efficiency principles, sparse activation |
| **v2** | 2026-06-05 | Panta Rhei | Dynamic worldview integration, emergence detection, calibrated language |
| **v1** | 2026-06-05 | Original | Initial release — fish ecology research assistant with 5 search engines + 12 subagents |

<p align=right>(<a href=#readme-top>back to top</a>)</p>
