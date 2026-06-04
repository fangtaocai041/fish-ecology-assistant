# Reasonix Research Assistant — User Guide

> When you don't know "what this thing can do" or "how to command it", open this file.

---

## Overview

| Category | Count | Description |
|----------|:-----:|-------------|
| Skills (subagents) | 13 | AI experts that auto-execute complex tasks |
| MCP tools | 16 | The subagents' "hands and eyes" (search/OCR/charts/R/browser etc.) |
| Behavior guard | 1 | Karpathy 4 Principles (anti-hallucination / anti-complexity / anti-overreach) |

---

## 1. Skills (13 subagents)

### Research Pipeline (one-click full workflow)

> **"Research [topic] for me, run the full pipeline"**

Auto-orchestrates 5 stages:

| Stage | Skill | Function | Time |
|:-----:|-------|----------|:----:|
| 1 | `research-planner` | Decompose question → keywords + sub-topics + search strategy | ~30s |
| 2 | `research-executor` | 5-engine parallel search → source database (English-first) | ~2-5min |
| 3 | `research-analyst` | Classify & synthesize → core findings (≥2 source cross-validation) | ~1min |
| 4 | `research-writer` | Write review/report (auto-save to research_output/) | ~1-2min |
| 5 | `research-reviewer` | 4-dimension score review → pass/revise/fail (max 3 iterations) | ~30s |

### Quick Reference

| What you want | How to say it |
|---------------|---------------|
| Full research | "Research [topic] for me, run the full pipeline" |
| Plan only | `/skill research-planner Research question: [topic]` |
| Search only | `/skill research-executor [full research plan]` |
| Analyze only | `/skill research-analyst [full source database]` |
| Write only | `/skill research-writer [full analysis report]` |
| Review only | `/skill research-reviewer [full draft]` |

### PhD & Domain Specialists

| What you want | How to say it |
|---------------|---------------|
| Write PhD proposal | `/skill phd-proposal-writer Research direction: [your topic]` |
| Generate R analysis code | `/skill stats-assistant Help me with: [analysis need]` |
| Learn unfamiliar stats method | `/skill stats-method-finder Method: [method name]` |
| Dissect a paper | `/skill paper-analyzer Analyze: [DOI or title+abstract]` |
| Track top labs | `/skill frontier-tracker Check recent activity from [team name/keyword]` |
| Query Zotero library | `/skill zotero-assistant Search for: [keyword/author]` |
| Manage Obsidian notes | `/skill obsidian-assistant Help me: [read/write/search] notes` |

---

## 2. MCP Tools (16)

> Use directly in conversation — no `/skill` prefix needed.

### Search (5)

| Tool | Example Command | Best For |
|------|----------------|----------|
| `tavily` | "Search with tavily: effects of Yangtze fishing ban on fish communities" | AI deep search, 15 results, advanced mode |
| `exa` | "Search with exa: stable isotope niche freshwater fish" | Semantic search, meaning-aware |
| `scholar` | "Search with scholar: Culter alburnus genetic diversity" | Academic paper search |
| `article` | "Fetch full text of this paper with article" | Full paper text/abstract/references |
| `scholarly` | "Search scholarly for: [keyword]" | Multi-source academic search |

### Data & Files (3)

| Tool | Example Command | Best For |
|------|----------------|----------|
| `fs` | "Read my Obsidian note about Ochetobius" | Read/write files (mounts your Obsidian Vault) |
| `git` | "Check git log for me" | Version control |
| `github` | "Search GitHub for fish ecology repos" | GitHub API (repos/issues/PRs) |

### Compute & Visualization (4)

| Tool | Example Command | Best For |
|------|----------------|----------|
| `rplay` | "Run this R code with rplay" | R environment (geomorph/vegan/SIBER etc.) |
| `coderunner` | "Run this Python with coderunner" | Code sandbox (R/Python/JS/multi-language) |
| `echarts` | "Draw a bar chart with echarts: [data]" | Charts (bar/line/pie/heatmap etc.) |
| `thinking` | "Analyze this complex problem with thinking" | Multi-step chain-of-thought reasoning |

### Image & Browser (3)

| Tool | Example Command | Best For |
|------|----------------|----------|
| `ocr` | "OCR this image with paddleocr" | Chinese OCR (tables/formulas/handwriting) |
| `ocr-fallback` | "OCR this image with ocr-fallback" | Offline OCR (Tesseract.js, no network) |
| `playwright` | "Open this webpage with playwright" | Browser automation (screenshots/scraping/forms) |

### Library (1)

| Tool | Example Command | Best For |
|------|----------------|----------|
| `zotero` | "Query my Zotero database for stable isotope papers" | Direct SQL query to Zotero |

---

## 3. Karpathy Behavior Guard

All subagents follow `karpathy-guard` 4 principles:

| Principle | Meaning | Prevents |
|-----------|---------|----------|
| **Think First** | State hypothesis before acting | Fabrication, hiding uncertainty |
| **Simplicity** | Minimum output, don't stack volume | 5000-word bloated reports |
| **Surgical** | Only change what was asked, don't touch the rest | Auto-"polishing" that destroys existing content |
| **Goal-Driven** | Provide verifiable criteria, not vague instructions | "Search for X" → results can't be quality-judged |

---

## 4. Common Workflows

### Scenario 1: Write an academic review

```
1. "Research effects of the Yangtze ten-year fishing ban on fish community structure, run full pipeline"
2. "Use echarts to chart the data from the report"
3. → auto review iterations → final report saved to research_output/
```

### Scenario 2: PhD proposal

```
1. "/skill phd-proposal-writer Research direction: drivers of sympatric coexistence of Culter species in lower Yangtze after fishing ban"
2. "Search scholar: Culter sympatric coexistence stable isotope"
3. "/skill stats-assistant Generate SIBER ellipse competition analysis R code"
4. → integrate into proposal
```

### Scenario 3: Deep paper reading

```
1. "/skill paper-analyzer Analyze: [DOI]"
2. "Check citation count for this paper with scholar"
3. "Check if I have similar papers in my Zotero library"
```

### Scenario 4: Frontier tracking

```
1. "/skill frontier-tracker Check recent activity from Oberdorff group"
2. "Search scholar for full text of key papers mentioned in the report"
```

---

## 5. Output Locations

| Output | Saved To |
|--------|----------|
| Research reports | `research_output/` |
| Obsidian notes | Your Obsidian Vault (configured path) |
| Zotero references | Your Zotero database (configured path) |

---

## 6. TL;DR

> **"Research [topic] for me, run the full pipeline"** — most common
>
> **"/skill [skill-name] [your need]"** — invoke a specific subagent
>
> **"Use [tool-name] to [action]"** — directly invoke MCP tool
>
> **English-first** — academic search auto-uses English, Chinese supplements

---

*Last updated: 2026-06*
