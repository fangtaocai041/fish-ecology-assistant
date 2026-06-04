# Multi-Agent Research Assistant

> A complete scientific research assistant system powered by Reasonix Code + 16 MCP services + 12 specialized subagents (Skills), tailored for **aquatic ecology / conservation genetics / fisheries science**.

---

## Architecture Overview

```
User Query
    │
    ▼
┌──────────────────────────────┐
│  Orchestrator (Master Scheduler)│  ← You interact with this one
│  12 skills · 16 MCP tools       │
└──┬──────┬──────┬──────┬─────┘
   │      │      │      │
   ▼      ▼      ▼      ▼
┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐
│Plan │→│Srch │→│Analy│→│Write│→ 🔄(≤3 rounds)
└─────┘ └─────┘ └─────┘ └──┬──┘
                           │
                     ┌─────▼─────┐
                     │  ✅ Review  │
                     └───────────┘
```

---

## Quick Start

| Scenario | Command |
|----------|---------|
| Full research pipeline | "Research [topic] for me, run the full pipeline" |
| Write PhD proposal | `/skill phd-proposal-writer Research direction: [topic]` |
| R statistical analysis | `/skill stats-assistant Help me with: [analysis need]` |
| Analyze a paper | `/skill paper-analyzer Analyze: [DOI/abstract]` |
| Frontier tracking | `/skill frontier-tracker Check recent activity from [team name]` |
| Write a review | `/skill research-orchestrator Research topic: [topic]` |

---

## Skills (12)

### Research Pipeline (5-stage auto-orchestration)

| Role | Name | Type | Input → Output |
|------|------|------|----------------|
| Planner | `research-planner` | subagent | Question → Research Plan |
| Researcher | `research-executor` | subagent | Plan → Source Database |
| Analyst | `research-analyst` | subagent | Sources → Analysis Report |
| Writer | `research-writer` | subagent | Report → Draft Document |
| Reviewer | `research-reviewer` | subagent | Draft → Review Score |
| Orchestrator | `research-orchestrator` | inline | Schedules all 5 above |

### Domain Specialists

| Name | Purpose |
|------|---------|
| `frontier-tracker` | Track top fish ecology labs globally |
| `paper-analyzer` | Deep paper dissection (methods / innovation / reproducibility) |
| `phd-proposal-writer` | Write PhD application proposals |
| `stats-assistant` | R biostatistics (morphometrics / isotopes / genetics / community) |
| `stats-method-finder` | Expand unfamiliar statistical methods |
| `zotero-assistant` | Query Zotero library via SQL |
| `obsidian-assistant` | Read/write Obsidian notes |

---

## MCP Services (16)

### Search & Academia

| Service | Type | Purpose |
|---------|------|---------|
| `tavily` | Deep search | AI-powered deep web search (15 results, advanced depth) |
| `exa` | Semantic search | Meaning-aware, not keyword matching |
| `scholar` | Academic | Google Scholar search for papers |
| `article` | Article fetch | Full article metadata & abstract |
| `scholarly` | Scholarly research | Multi-source scholarly search |

### System & Data

| Service | Type | Purpose |
|---------|------|---------|
| `fs` | Filesystem | Mounts Obsidian Vault & server files |
| `git` | Version control | git operations |
| `github` | GitHub API | Repository/issue/PR access |
| `zotero` | Zotero | SQL query against Zotero database |

### Compute & Visualization

| Service | Type | Purpose |
|---------|------|---------|
| `rplay` | R language | R environment via uvx |
| `coderunner` | Code sandbox | Isolated code execution (R/Python/JS etc.) |
| `echarts` | Charts | ECharts data visualization |
| `thinking` | Chain-of-thought | Sequential multi-step reasoning |

### Image & Browser

| Service | Type | Purpose |
|---------|------|---------|
| `ocr` | PaddleOCR | Chinese OCR (tables, formulas, handwriting) |
| `ocr-fallback` | Tesseract.js | Offline OCR (no network needed) |
| `playwright` | Browser automation | Web scraping, screenshots, form fill |

---

## Project Structure

```
your-project/
├── .gitignore                    ← Excludes secret key files
├── LICENSE                       ← MIT License
├── README.md                     ← This file
├── GUIDE.md                      ← Full guide
│
├── .reasonix/
│   ├── mcp-servers/              ← MCP wrapper scripts
│   │   ├── tavily.bat / exa.bat  ← Search (git-ignored)
│   │   ├── github.bat            ← GitHub API (git-ignored)
│   │   ├── rplay.bat             ← R environment
│   │   ├── paddleocr.bat         ← OCR Plan A
│   │   ├── ocr-fallback/         ← OCR Plan B (Tesseract.js)
│   │   ├── zotero.bat            ← Zotero SQLite
│   │   ├── setup-migrate.ps1     ← One-click migration script
│   │   └── README.md             ← MCP server details
│   │
│   └── skills/                   ← 12 skill playbooks
│       ├── research-planner.md
│       ├── research-executor.md
│       ├── research-analyst.md
│       ├── research-writer.md
│       ├── research-reviewer.md
│       ├── research-orchestrator.md
│       ├── frontier-tracker.md
│       ├── paper-analyzer.md
│       ├── phd-proposal-writer.md
│       ├── stats-assistant.md
│       ├── stats-method-finder.md
│       ├── zotero-assistant.md
│       └── obsidian-assistant.md
│
├── research_output/              ← Research reports output
│
└── [external] %USERPROFILE%\.reasonix\
    └── config.json               ← MCP registry + settings
```

---

## Design Principles

| Principle | Implementation |
|-----------|---------------|
| **Subagent isolation** | Each subagent runs in its own context — they never share token space |
| **Prefix-cache aligned** | Stable prompt prefix → 90%+ cache hit on DeepSeek |
| **Graceful degradation** | MCP fails → auto fallback chain |
| **Output budget** | Every skill has explicit token limits per stage |
| **Self-healing** | Built-in retry logic for transient failures |

---

## Comparison

| Feature | Standard Reasonix | This Setup |
|---------|:-----------------:|:-----------:|
| MCP services | 0 (code only) | **16** |
| Subagent Skills | 4 built-in | **12** |
| Search engines | 1 (web_search) | **5** (tavily/exa/scholar/article/scholarly) |
| R environment | ✗ | ✅ via rplay |
| OCR | ✗ | ✅ PaddleOCR + Tesseract.js |
| Zotero | ✗ | ✅ Direct SQL query |
| PhD proposal writer | ✗ | ✅ Customized |
| Domain expertise | Generic | **Fish ecology / Conservation genetics / Stable isotopes** |

---

## Security

- API keys (TAVILY, EXA, GITHUB) are stored in **git-ignored** `.bat` files
- SSH key for GitHub push: `~/.ssh/id_ed25519`
- Zotero database: configure path in `zotero.bat`

---

## License

MIT

Built with [Reasonix Code](https://github.com/esengine/deepseek-reasonix) · DeepSeek-native coding agent
