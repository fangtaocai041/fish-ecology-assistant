# Complete Guide

> This document explains the full system architecture, how to use every skill, and best practices.

---

## System Overview

### What You Have

| Component | Count | Details |
|-----------|:-----:|---------|
| MCP Services | **16** | Search · Academia · Compute · OCR · Browser · Git |
| Subagent Skills | **12** | Research pipeline (5) + Domain specialists (7) |
| Search Engines | **5** | tavily, exa, scholar, article, scholarly |
| OCR Systems | **2** | PaddleOCR (online) + Tesseract.js (offline) |

### Architecture

```
            User
              │
              ▼
    ┌──────────────────────────┐
    │   Orchestrator            │  ← AI Project Manager
    │   research-orchestrator   │
    └──────────┬───────────────┘
               │  dispatches
    ┌──────────┼──────────┐
    ▼          ▼          ▼
┌──────┐  ┌──────┐  ┌──────────┐
│Pipeline│  │Domain │  │  Direct  │
│Research│  │Skills │  │MCP Tools │
└──────┘  └──────┘  └──────────┘
```

---

## Using the System

### Mode 1: Full Research Pipeline (Recommended)

Simply say to Reasonix Code:

> **"Research [your topic] for me, run the full pipeline"**

Or explicitly:

> `/skill research-orchestrator My research question is: [topic]`

This triggers the 5-stage pipeline + up to 3 review iterations:

```
Stage 1: Planner    → Decompose research question
Stage 2: Researcher → 5-engine parallel search
Stage 3: Analyst    → Classify, pattern recognition, synthesize
Stage 4: Writer     → Write review/report
Stage 5: Reviewer   → 4-dimension score review
         └── 🔄 Needs revision → Return to Writer (≤3 rounds)
         └── ✅ Pass → Output final report to research_output/
```

### Mode 2: Call a Specific Subagent

| Skill | Command Example |
|-------|----------------|
| Planner | `/skill research-planner Research question: effects of Yangtze fishing ban on fish communities` |
| Researcher | `/skill research-executor <full research plan>` |
| Analyst | `/skill research-analyst <full source database>` |
| Writer | `/skill research-writer <full analysis report>` |
| Reviewer | `/skill research-reviewer <full draft>` |

### Mode 3: Domain Skills

| Skill | Command Example |
|-------|----------------|
| PhD Proposal | `/skill phd-proposal-writer Research direction: drivers of sympatric coexistence of Culter species in lower Yangtze` |
| R Stats | `/skill stats-assistant Generate complete Procrustes PCA R code for 5-population landmark data` |
| Paper Analysis | `/skill paper-analyzer Analyze this paper: [DOI or title+abstract]` |
| Frontier Tracking | `/skill frontier-tracker Check recent activity from Oberdorff group` |
| Stats Method | `/skill stats-method-finder Explain MaxEnt model R implementation and parameter tuning` |
| Zotero Query | `/skill zotero-assistant Search my library for recent stable isotope papers` |
| Obsidian Notes | `/skill obsidian-assistant Read my research notes about Ochetobius` |

### Mode 4: Direct MCP Tools

| Scenario | Say This |
|----------|----------|
| Deep search | "Search with tavily: XXX" |
| Academic search | "Search with scholar: Culter alburnus genetic diversity" |
| OCR | "OCR this image with paddleocr" |
| Charts | "Draw a bar chart with echarts showing..." |
| Web scraping | "Open this webpage with playwright..." |
| R code | "Run this R code with coderunner" |
| Sequential thinking | "Analyze this problem with thinking..." |

---

## Best Practices

### 1. Be Specific

```
❌ "Research deep learning for me"
✅ "Compare CNN, Transformer, and Mamba architectures for fish image recognition tasks"
```

### 2. Split Large Topics

```
❌ "Research all of fish ecology for me"
✅ Split into 3 sessions:
   1. "Effects of Yangtze fishing ban on fish community structure"
   2. "Advances in stable isotope applications for niche research"
   3. "Methodological review of eDNA for fish monitoring"
```

### 3. Use Domain Terminology

The system understands these terms naturally:

- **niche partitioning**
- **stable isotopes** (δ¹³C, δ¹⁵N)
- **geometric morphometrics**
- **sympatric coexistence**
- **RAD-seq**
- **species distribution models** (MaxEnt)

### 4. Results Are Saved

All research outputs are saved to `research_output/`:

```
research_output/
├── 2026-06-03-yangtze-fishing-ban-ecological-assessment.md
└── ...
```

---

## Skills Architecture

### Subagent Prompt Optimization Principles

All 12 skills have been optimized with the following principles:

| Principle | What Changed |
|-----------|-------------|
| **Output budget** | Every skill has explicit token limits to prevent context overflow |
| **Fallback chain** | MCP tool failures don't break the pipeline — auto fallback |
| **Citation validation** | Core findings require ≥2 independent sources |
| **Anti-hallucination** | Empty results must be reported as "no results", never fabricated |
| **Cache-friendly** | Stable frontmatter, variable content at bottom |

---

## Security Notes

| Item | Status |
|------|:------:|
| API keys (tavily, exa, github) | In `.gitignore` |
| SSH key for GitHub push | `~/.ssh/id_ed25519` |
| Zotero database path | Configured in `zotero.bat` |
| OCR-Fallback auto install | Built-in (npm install on first run) |

---

## File Locations

| File | Path |
|------|------|
| MCP wrapper scripts | `.reasonix/mcp-servers/` |
| Skills playbooks | `.reasonix/skills/` |
| Research outputs | `research_output/` |
| Reasonix config | `%USERPROFILE%\.reasonix\config.json` |
| Project memory | `%USERPROFILE%\.reasonix\memory\` |

---

## Philosophy

> **You are the captain. I am the engine room, the navigation system, and all the cables.**

The tool can search 50 papers in seconds, write a draft in minutes, and run R code instantly.

But only **you** can decide:
- What is a good research question?
- What is meaningful science?
- Where should we go next?

*The stronger the tool, the more irreplaceable the person using it.*
