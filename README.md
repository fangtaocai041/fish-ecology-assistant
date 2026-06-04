<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)">
    <img alt="Reasonix Research Assistant" src="https://img.shields.io/badge/🧠-Reasonix_Research_Assistant-6366f1?style=for-the-badge" height="48">
  </picture>
</p>

<p align="center">
  <strong>Turn your coding agent into a PhD-level research team.</strong><br>
  <sub>16 MCP tools · 12 AI subagents · 5-engine parallel search · One-click migration</sub>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License: MIT"></a>
  <a href="#"><img src="https://img.shields.io/badge/Reasonix_Code-compatible-6366f1" alt="Reasonix Code"></a>
  <a href="#"><img src="https://img.shields.io/badge/MCP_services-16-22c55e" alt="MCP: 16"></a>
  <a href="#"><img src="https://img.shields.io/badge/subagents-12-f59e0b" alt="Subagents: 12"></a>
  <a href="USERGUIDE.md"><img src="https://img.shields.io/badge/docs-user_guide-0ea5e9" alt="Docs"></a>
</p>

---

## What is this?

**reasonix-data** is a complete, portable configuration for [Reasonix Code](https://github.com/esengine/deepseek-reasonix) that transforms it from a generic coding assistant into a **domain-specialized research powerhouse** — with 16 integrated tools, 12 specialized AI subagents, and a 5-stage auto-orchestrated research pipeline.

> 💬 *"Research the effects of the Yangtze fishing ban on fish communities — run the full pipeline."*  
> → 5 engines search in parallel → AI analyzes & cross-validates → writes a structured review → self-reviews with a 4-dimension scorecard → saves to `research_output/`. **All in one command.**

**Who is this for?** Researchers in ecology, conservation genetics, fisheries science — or anyone who wants a template for building their own domain-specialized AI research assistant.

---

## Table of Contents

- [Why This Exists](#-why-this-exists)
- [What You Get](#-what-you-get)
- [Architecture](#-architecture)
- [Quick Start](#-quick-start)
- [Getting Started (New Machine)](#-getting-started-new-machine)
- [Skills — AI Subagents](#-skills--ai-subagents)
- [MCP Services — Tools](#-mcp-services--tools)
- [Design Principles](#-design-principles)
- [Project Structure](#-project-structure)
- [Comparison: Before vs After](#-comparison-before-vs-after)
- [Documentation](#-documentation)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🤔 Why This Exists

Out of the box, coding agents like Reasonix Code can write code. But research isn't just coding — it's **searching across 5 academic engines, decomposing questions, cross-validating sources, running statistical models, OCR-ing scanned papers, querying your Zotero library, and iterating through drafts with a reviewer.**

This repo gives you all of that. It's the difference between:

| Before | After |
|:-------|:------|
| 0 MCP services | **16** specialized tools |
| 4 generic built-in subagents | **12** domain-specialized AI agents |
| 1 search engine (`web_search`) | **5** (tavily, exa, scholar, article, scholarly) |
| No R environment | Full R 4.6.0 with geomorph, vegan, SIBER, adegenet |
| No OCR | PaddleOCR + Tesseract.js fallback |
| No reference manager | Direct Zotero SQLite queries |
| No pipeline | Auto-orchestrated 5-stage research pipeline |

---

## 🎁 What You Get

| Category | What | Why You'd Want It |
|:---------|:-----|:------------------|
| 🔍 **5 Search Engines** | tavily, exa, scholar, article, scholarly | Find anything — from deep web to Google Scholar |
| 📊 **R Statistics Engine** | Full R environment with 20+ ecology packages | Run morphometrics, isotopes, community analysis inline |
| 🖼️ **Dual OCR** | PaddleOCR (online) + Tesseract.js (offline) | Extract text from papers, tables, screenshots |
| 📚 **Zotero Integration** | Direct SQL query to your Zotero database | Search your library without leaving the chat |
| 📝 **Obsidian Integration** | Read/write your Obsidian vault | Research notes stay in your knowledge base |
| 🌐 **Browser Automation** | Playwright-powered web scraping | Extract data from websites, take screenshots |
| 📈 **Chart Generation** | ECharts visualization | Turn data into publication-ready charts |
| 🎓 **PhD Proposal Writer** | Structured proposal generation | From topic → full proposal with references |
| 🔄 **Self-Review Pipeline** | 4-dimension scoring + up to 3 revision rounds | Quality-controlled output, every time |
| 🚀 **One-Click Migration** | `setup-migrate.ps1` | Clone repo → run script → fully configured |

---

## 🏗 Architecture

```
                          ┌─────────────────────────┐
     "Research X,         │     Orchestrator         │
      run full pipeline"  │   (Master Scheduler)     │
           │              │   12 skills · 16 tools   │
           ▼              └──────┬──────┬───────────┘
    ┌──────────────┐            │      │
    │   Stage 1    │   Planner  │      │  "What sub-topics?
    │   🧑‍💼 Plan    │◄───────────┘      │   Which keywords?"
    └──────┬───────┘                   │
           │                           │
    ┌──────▼───────┐                   │  "Searching 5 engines
    │   Stage 2    │   Researcher      │   in parallel..."
    │   🔍 Search   │◄──────────────────┘
    └──────┬───────┘
           │
    ┌──────▼───────┐
    │   Stage 3    │   Analyst         "Classification, patterns,
    │   📊 Analyze  │                   contradictions..."
    └──────┬───────┘
           │
    ┌──────▼───────┐
    │   Stage 4    │   Writer          "Writing structured review
    │   ✍️ Write    │                   with citations..."
    └──────┬───────┘
           │
    ┌──────▼───────┐     ┌─────────────┐
    │   Stage 5    │──✅─│  Pass → Save │
    │   ✅ Review   │     └─────────────┘
    └──────┬───────┘     ┌─────────────┐
           └────🔄───────│  Revise (≤3) │
                         └─────────────┘
```

**Pipeline modes:**

- **Prompt Chaining**: Each stage feeds into the next — clean, predictable, debuggable
- **Evaluator-Optimizer**: Stage 5 scores the output on 4 dimensions; if it doesn't pass, loop back to writing
- **Parallel Search**: When sub-topics are independent, Stage 2 runs all 5 engines simultaneously

---

## ⚡ Quick Start

Once configured, just talk to Reasonix naturally:

| You want to... | Say this |
|:---------------|:---------|
| Full research pipeline | `"Research [topic] for me — run the full pipeline"` |
| Write a PhD proposal | `/skill phd-proposal-writer Research direction: [topic]` |
| Run R statistical analysis | `/skill stats-assistant Help me with: [analysis need]` |
| Deep-analyze a paper | `/skill paper-analyzer Analyze: [DOI or abstract]` |
| Track what top labs are doing | `/skill frontier-tracker Check recent activity from [team]` |
| Query your Zotero library | `"Search my Zotero for papers on stable isotopes"` |
| OCR a scanned document | `"Use paddleocr to extract text from this image"` |
| Generate a chart | `"Use echarts to plot a bar chart showing [data]"` |

> 💡 **Pro tip**: Be specific. "*Find ≥8 peer-reviewed papers (2022–2025) on Yangtze fishing ban effects, with ≥2 from Q1 journals*" beats "*Search for fishing ban papers*."

---

## 🚀 Getting Started (New Machine)

```bash
# 1. Clone this repo
git clone https://github.com/fangtaocai041/reasonix-data.git
cd reasonix-data

# 2. Run the one-click migration script
powershell -ExecutionPolicy Bypass -File .reasonix\setup-migrate.ps1
```

The script will:
- ✅ Check Node.js, R, uvx dependencies — with install links if missing
- ✅ Install OCR fallback dependencies
- ✅ Generate your global Reasonix `config.json` with all 13 MCP services
- ✅ Verify API key files exist (or show you how to create them)
- ✅ Flag any path mismatches (R_HOME, uvx, Zotero db)

**After running the script**, restart Reasonix. The 13 MCP services and 12 skills will be available immediately.

> ⚠️ **API Keys**: The script creates the config structure, but you need to copy your API key files (`tavily.bat`, `exa.bat`, `github.bat`, `paddleocr-server.mjs`) from your original machine. These are git-ignored — they never leave your computer.

---

## 🧠 Skills — AI Subagents

### Research Pipeline (auto-orchestrated)

These 6 agents form a complete 5-stage research pipeline. Call the Orchestrator to run all stages automatically, or invoke any stage individually.

| # | Agent | Role | Does |
|:-:|:------|:-----|:-----|
| 🎯 | `research-orchestrator` | **Master Scheduler** | Dispatches all 5 stages, handles retries & fallbacks |
| 1 | `research-planner` | 🧑‍💼 Planner | Decomposes questions → keywords + sub-topics + search strategy |
| 2 | `research-executor` | 🔍 Researcher | 5-engine parallel search → source database with citations |
| 3 | `research-analyst` | 📊 Analyst | Classifies, pattern-matches, cross-validates (≥2 sources) |
| 4 | `research-writer` | ✍️ Writer | Structured review/report with author-year citations |
| 5 | `research-reviewer` | ✅ Reviewer | 4-dimension score + revision notes (max 3 rounds) |

### Domain Specialists

| Agent | Does | When to use |
|:------|:-----|:------------|
| 🎓 `phd-proposal-writer` | Structured PhD proposal with references | Applying to grad school |
| 📊 `stats-assistant` | R code + method selection + interpretation | "Help me analyze my morphometric data" |
| 🔍 `stats-method-finder` | Searches CRAN, journals, textbooks for unfamiliar methods | "What's the R package for MaxEnt?" |
| 📖 `paper-analyzer` | Deep dissection: methods, innovation, reproducibility | "Analyze this paper for me" |
| 🔭 `frontier-tracker` | Tracks 15+ top fish ecology labs globally | "What's new from Oberdorff's group?" |
| 📚 `zotero-assistant` | Direct SQL queries to your Zotero database | "How many papers do I have on stable isotopes?" |
| 📝 `obsidian-assistant` | Read/write your Obsidian vault | "Create a research note from these findings" |

---

## 📡 MCP Services — Tools

### 🔍 Search & Academia
| Service | Engine | Best For |
|:--------|:-------|:---------|
| `tavily` | AI deep search | Broad web research, 15 results, advanced depth |
| `exa` | Semantic search | Meaning-aware, not keyword-matched |
| `scholar` | Google Scholar | Academic papers, citation counts |
| `article` | Article metadata | Full abstracts, author lists, references |
| `scholarly` | Multi-source | Cross-database scholarly search |

### 🧮 Compute & Visualization
| Service | What It Runs | Use Case |
|:--------|:-------------|:---------|
| `rplay` | R 4.6.0 (geomorph, vegan, SIBER, adegenet...) | Morphometrics, community ecology, genetics |
| `coderunner` | R / Python / JS / Bash | Isolated code execution sandbox |
| `echarts` | ECharts | Publication-ready charts and graphs |
| `thinking` | Chain-of-thought | Multi-step complex reasoning |

### 🖼️ Image & Browser
| Service | Engine | Use Case |
|:--------|:-------|:---------|
| `ocr` | PaddleOCR | Chinese text, tables, formulas, handwriting |
| `ocr-fallback` | Tesseract.js | Offline OCR (works without network) |
| `playwright` | Chromium | Web scraping, screenshots, form interaction |

### 🗄️ System & Data
| Service | Interface | Use Case |
|:--------|:----------|:---------|
| `fs` | Filesystem | Read/write files (mounts your Obsidian vault) |
| `git` | Git CLI | Version control operations |
| `github` | GitHub API | Repository, issue, PR access |
| `zotero` | SQLite (read-only) | Query your Zotero library |

---

## 🧩 Design Principles

| Principle | What It Means | Why |
|:----------|:--------------|:----|
| **Subagent Isolation** | Each agent runs in its own context — zero token sharing | Prevents context pollution; each agent focuses on one job |
| **Cache-Aligned Prompts** | Stable frontmatter, variable content at the bottom | 90%+ cache hit rate on DeepSeek → cheaper long sessions |
| **Graceful Degradation** | If a tool fails, the pipeline doesn't | Auto-fallback: scholar → tavily → web_search |
| **Citation Validation** | Core claims require ≥2 independent sources | Anti-hallucination; every claim is traceable |
| **Output Budgets** | Every skill has an explicit token cap | No 5000-word rambles; focused, scannable output |
| **Self-Healing** | Auto-retry + engine switching on failure | You don't debug the pipeline — it debugs itself |

---

## 📁 Project Structure

```
reasonix-data/
├── README.md                       ← You are here
├── USERGUIDE.md                    ← Full usage guide with examples
├── GUIDE.md                        ← Architecture deep-dive
├── CHEATSHEET.md                   ← Quick-reference card
├── LICENSE                         ← MIT
│
├── .reasonix/
│   ├── mcp-servers/                ← MCP wrapper scripts
│   │   ├── tavily.bat              ← Tavily search (git-ignored)
│   │   ├── exa.bat                 ← Exa semantic search (git-ignored)
│   │   ├── github.bat              ← GitHub API (git-ignored)
│   │   ├── rplay.bat               ← R environment launcher
│   │   ├── paddleocr.bat           ← PaddleOCR launcher
│   │   ├── paddleocr-server.mjs    ← PaddleOCR MCP server (git-ignored)
│   │   ├── ocr-fallback/           ← Tesseract.js MCP server
│   │   ├── zotero.bat              ← Zotero SQLite launcher
│   │   └── README.md               ← MCP server details
│   │
│   ├── skills/                     ← 12 AI subagent playbooks
│   │   ├── research-orchestrator.md
│   │   ├── research-planner.md
│   │   ├── research-executor.md
│   │   ├── research-analyst.md
│   │   ├── research-writer.md
│   │   ├── research-reviewer.md
│   │   ├── phd-proposal-writer.md
│   │   ├── stats-assistant.md
│   │   ├── stats-method-finder.md
│   │   ├── paper-analyzer.md
│   │   ├── frontier-tracker.md
│   │   ├── zotero-assistant.md
│   │   └── obsidian-assistant.md
│   │
│   └── setup-migrate.ps1           ← One-click new-machine setup
│
└── research_output/                ← Generated reports land here
```

---

## 📊 Comparison: Before vs After

| Capability | Vanilla Reasonix | **With reasonix-data** |
|:-----------|:----------------:|:----------------------:|
| Search engines | 1 (`web_search`) | **5** (tavily, exa, scholar, article, scholarly) |
| MCP services | 0 | **16** |
| AI subagents | 4 (generic) | **12** (domain-specialized) |
| R statistics | — | ✅ R 4.6.0 + 20+ ecology packages |
| OCR (text from images) | — | ✅ PaddleOCR + offline Tesseract.js |
| Reference manager | — | ✅ Direct Zotero SQL queries |
| Research pipeline | — | ✅ 5-stage + auto-review (≤3 rounds) |
| PhD proposal generation | — | ✅ Structured proposal + references |
| New-machine migration | Manual | ✅ One script, 5 minutes |
| Domain knowledge | Generic | Fish ecology · Conservation genetics · Stable isotopes |

---

## 📖 Documentation

| Document | What's Inside |
|:---------|:--------------|
| **[USERGUIDE.md](USERGUIDE.md)** | Complete usage guide — every skill, every tool, with example commands |
| **[GUIDE.md](GUIDE.md)** | Architecture deep-dive, design decisions, best practices |
| **[CHEATSHEET.md](CHEATSHEET.md)** | One-page quick reference — skill commands, tool shortcuts, R decision tree |
| **[.reasonix/mcp-servers/README.md](.reasonix/mcp-servers/README.md)** | MCP server technical details — which wrapper does what |

---

## 🤝 Contributing

This is a personal configuration turned open-source template. If you:

- Adapted it for a different domain (e.g., physics, medicine, law)
- Added new skills or MCP services
- Found a better way to structure the pipeline
- Have ideas for improvement

...**PRs and issues are welcome!** See the [issues page](https://github.com/fangtaocai041/reasonix-data/issues) for ideas.

### Quick contribution ideas
- [ ] Port to Linux/macOS (replace `.bat` wrappers with shell scripts)
- [ ] Add domain templates for other fields (biomedical, CS, social science)
- [ ] Add example research outputs as showcase
- [ ] Docker-based setup for zero-dependency migration

---

## 📄 License

MIT — see [LICENSE](LICENSE).

Built with [Reasonix Code](https://github.com/esengine/deepseek-reasonix) · Powered by DeepSeek
