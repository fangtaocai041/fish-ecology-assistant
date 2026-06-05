<p align=center>
  🇨🇳 <a href=README.zh.md>中文</a>
</p>

<div align=center>
  <h1>🧠 Reasonix Research Assistant</h1>
  <p><strong>Turn your coding agent into a PhD-level research team.</strong></p>
  <p>16 MCP tools · 12 AI subagents · 5-engine search · One-click migration</p>
</div>

<p align=center>
  <a href=LICENSE><img src=https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square alt=License></a>
  <a href=#><img src=https://img.shields.io/badge/Reasonix_Code-compatible-6366f1?style=flat-square alt=Reasonix Code></a>
  <a href=#><img src=https://img.shields.io/badge/MCP_services-16-22c55e?style=flat-square alt=MCP: 16></a>
  <a href=#><img src=https://img.shields.io/badge/subagents-12-f59e0b?style=flat-square alt=Subagents: 12></a>
  <a href=USERGUIDE.md><img src=https://img.shields.io/badge/docs-user_guide-0ea5e9?style=flat-square alt=Docs></a>
</p>

<details>
  <summary>📖 Table of Contents</summary>
  <ol>
    <li><a href=#-why-this-exists>Why This Exists</a></li>
    <li><a href=#-what-you-get>What You Get</a></li>
    <li><a href=#-architecture>Architecture</a></li>
    <li><a href=#-quick-start>Quick Start</a></li>
    <li><a href=#-getting-started>Getting Started</a></li>
    <li><a href=#-skills--ai-subagents>Skills — AI Subagents</a></li>
    <li><a href=#-mcp-services--tools>MCP Services — Tools</a></li>
    <li><a href=#-project-structure>Project Structure</a></li>
    <li><a href=#-contributing>Contributing</a></li>
    <li><a href=#-license>License</a></li>
  </ol>
</details>

---

## 🤔 Why This Exists

Out of the box, coding agents can write code. But research isn't just coding — it's searching academic databases, decomposing questions, cross-validating sources, running statistical models, OCR-ing papers, querying reference managers, and iterating drafts with a reviewer.

This repo gives you all of that in one portable config.

| Capability | Vanilla Reasonix | **With reasonix-data** |
|:-----------|:----------------:|:----------------------:|
| Search engines | 1 (`web_search`) | **5** (tavily, exa, scholar, article, scholarly) |
| MCP services | 0 | **16** |
| AI subagents | 4 (generic) | **12** (domain-specialized) |
| R statistics | — | ✅ R 4.6.0 + 20+ ecology packages |
| OCR (text from images) | — | ✅ PaddleOCR + Tesseract.js |
| Reference manager | — | ✅ Direct Zotero SQL queries |
| Research pipeline | — | ✅ 5-stage + auto-review |
| Knowledge bases | — | ✅ 13 ima knowledge bases connected |
| New-machine setup | Manual | ✅ One script, 5 minutes |

<p align=right>(<a href=#readme-top>back to top</a>)</p>

---

## 🎁 What You Get

| Category | What | Why |
|:---------|:-----|:----|
| 🔍 **5 Search Engines** | tavily, exa, scholar, article, scholarly | Find anything from deep web to Google Scholar |
| 📊 **R Statistics** | Full R 4.6.0 + 20+ ecology packages | Run morphometrics, isotopes, community analysis inline |
| 🧠 **13 Knowledge Bases** | ima knowledge base integration | Query your private + subscribed KBs via MCP |
| 🖼️ **Dual OCR** | PaddleOCR + Tesseract.js fallback | Extract text from scanned papers and screenshots |
| 📚 **Zotero Integration** | Direct SQL to your Zotero database | Search your library without leaving the chat |
| 📝 **Obsidian Integration** | Read/write your Obsidian vault | Research notes stay in your knowledge base |
| 🌐 **Browser Automation** | Playwright-powered web scraping | Extract data from websites, take screenshots |
| 📈 **Chart Generation** | ECharts visualization | Turn data into publication-ready charts |
| 🎓 **PhD Proposal Writer** | Structured proposal with references | From topic → full proposal |
| 🔄 **Self-Review Pipeline** | 4-dimension scoring + 3 revision rounds | Quality-controlled output, every time |
| 🚀 **One-Click Migration** | `setup-migrate.ps1` | Clone → run → fully configured |

<p align=right>(<a href=#readme-top>back to top</a>)</p>

---

## 🏗 Architecture

<pre>
┌──────────────────────────┐
│  Research X, │
│ run full pipeline      │     Orchestrator
│                           │   (Master Scheduler)
└──────────┬───────────────┘   12 skills · 16 tools
           │
    ┌──────▼───────┐    ┌─────────────────┐
    │ ① Planner    │───▶│ Sub-topics      │
    │  🧑‍💼 Plan    │    │  Keywords       │
    └──────┬───────┘    │  Search strategy │
           │            └─────────────────┘
    ┌──────▼───────┐
    │ ② Researcher │    5 engines in parallel
    │  🔍 Search   │    tavily · exa · scholar
    └──────┬───────┘    article · scholarly
           │
    ┌──────▼───────┐
    │ ③ Analyst    │    Classification, patterns,
    │  📊 Analyze  │    contradictions, emergence
    └──────┬───────┘
           │
    ┌──────▼───────┐
    │ ④ Writer     │    Structured review
    │  ✍️ Write    │    with citations
    └──────┬───────┘
           │
    ┌──────▼───────┐    ┌──────────────┐
    │ ⑤ Reviewer   │───▶│ ✅ Pass→Save │
    │  ✅ Review   │    └──────────────┘
    └──────┬───────┘    ┌──────────────┐
           └────────────│ 🔄 Revise(≤3) │
                        └──────────────┘
</pre>

<p align=right>(<a href=#readme-top>back to top</a>)</p>

---

## ⚡ Quick Start

Once configured, talk to Reasonix naturally:

| Say this | What happens |
|:---------|:-------------|
| `Research [topic] — run the full pipeline` | 5 stages: plan → search → analyze → write → review |
| `Search my ima knowledge bases for [query]` | Auto-routes to correct KB, searches all, synthesizes results |
| `Help me with [statistical analysis]` | R code + method selection + diagnostics |
| `Analyze this paper: [DOI]` | Deep dissection: methods, quality, reproducibility |
| `Query my Zotero for [topic]` | Direct SQL to your reference database |
| `Use paddleocr to extract text from this image` | OCR Chinese/English text from scan |
| `Plot a chart showing [data]` | ECharts visualization |

> 💡 **Be specific.** `Find ≥8 peer-reviewed papers (2022–2025) on Yangtze fishing ban` beats `Search fishing ban`.

<p align=right>(<a href=#readme-top>back to top</a>)</p>

---

## 🚀 Getting Started

```bash
# 1. Clone
git clone https://github.com/fangtaocai041/reasonix-data.git
cd reasonix-data

# 2. Run one-click migration
powershell -ExecutionPolicy Bypass -File .reasonix\setup-migrate.ps1

# 3. Restart Reasonix — all 16 tools + 12 skills ready
```

The script handles: dependency checks → config generation → API key verification → path detection.

> ⚠️ API key files (`tavily.bat`, `exa.bat`, etc.) are git-ignored — copy from your original machine.

<p align=right>(<a href=#readme-top>back to top</a>)</p>

---

## 🧠 Skills — AI Subagents

### Research Pipeline (5-stage auto-orchestrated)

| # | Agent | Role | Does |
|:-:|:------|:-----|:-----|
| 🎯 | `research-orchestrator` | **Scheduler** | Dispatches all 5 stages, retries & fallbacks |
| ① | `research-planner` | 🧑‍💼 Plan | Decomposes → keywords + strategy, **bilingual** EN/CN |
| ② | `research-executor` | 🔍 Search | 5-engine parallel search, **bilingual** EN/CN queries |
| ③ | `research-analyst` | 📊 Analyze | Classification, patterns, contradictions, **emergence** |
| ④ | `research-writer` | ✍️ Write | Structured review with temporal awareness |
| ⑤ | `research-reviewer` | ✅ Review | 4-dimension scoring, ≤3 revision rounds |

### Domain Specialists

| Agent | Does |
|:------|:------|
| 🎓 `phd-proposal-writer` | Structured PhD proposal with references |
| 📊 `stats-assistant` | R code + method selection + interpretation |
| 🔍 `stats-method-finder` | Searches CRAN, journals, textbooks |
| 📖 `paper-analyzer` | Deep dissection: quality scoring + reproducibility + emergence |
| 🔭 `frontier-tracker` | Tracks 15+ top fish ecology labs |
| 📚 `zotero-assistant` | Direct SQL queries to Zotero |
| 📝 `obsidian-assistant` | Read/write Obsidian vault |
| 🧠 `ima-smart-search` | Cross-KB intelligent search (routes to correct KB) |
| ✅ `verify-stats-handbook` | Validate handbook code against CRAN + ima sources |

> 🌱 **Dynamic worldview**: All outputs are timestamped, use calibrated language, and flag emergent patterns. Science evolves — knowledge is provisional.

<p align=right>(<a href=#readme-top>back to top</a>)</p>

---

## 📡 MCP Services — Tools

| Service | Engine | Best For |
|:--------|:-------|:---------|
| `tavily` | AI deep search | Broad web, 15 results, advanced depth |
| `exa` | Semantic search | Meaning-aware, not keyword-matched |
| `scholar` | Google Scholar | Academic papers, citation counts |
| `article` | Article metadata | Full abstracts, references |
| `scholarly` | Multi-source | Cross-database scholarly search |
| `ima` | ima OpenAPI | 13 knowledge bases + notes (12 tools) |
| `rplay` | R 4.6.0 | Morphometrics, isotopes, community ecology |
| `coderunner` | Sandbox | R / Python / JS / Bash execution |
| `echarts` | ECharts | Publication-ready charts & graphs |
| `ocr` | PaddleOCR | Chinese/English text, tables |
| `ocr-fallback` | Tesseract.js | Offline OCR fallback |
| `playwright` | Chromium | Web scraping, screenshots |
| `git` | Git CLI | Version control |
| `github` | GitHub API | Repository access |
| `zotero` | SQLite (read-only) | Zotero library query |

<p align=right>(<a href=#readme-top>back to top</a>)</p>

---

## 📁 Project Structure

<pre>
reasonix-data/
├── README.md                 ← English
├── README.zh.md              ← 中文
├── USERGUIDE.md / GUIDE.md / CHEATSHEET.md
│
├── .reasonix/
│   ├── mcp-servers/          ← 16 MCP wrappers (ima, tavily, exa, R, zotero...)
│   ├── skills/               ← 12 AI subagent playbooks
│   ├── handbooks/            ← stats-methods.md + learning-guide.md
│   └── setup-migrate.ps1     ← One-click setup
│
└── research_output/          ← Generated reports
</pre>

<p align=right>(<a href=#readme-top>back to top</a>)</p>

---

## 🤝 Contributing

Adapted this for physics, medicine, or law? PRs welcome!

**Quick ideas:** Linux/macOS port · Domain templates · Docker setup

See [issues page](https://github.com/fangtaocai041/reasonix-data/issues).

<p align=right>(<a href=#readme-top>back to top</a>)</p>

---

## 📄 License

MIT — see [LICENSE](LICENSE).

Built with Reasonix Code · Powered by DeepSeek

<p align=right>(<a href=#readme-top>back to top</a>)</p>
