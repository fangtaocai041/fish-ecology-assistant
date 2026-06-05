<p align="center">
  🇨🇳 <a href="README.zh.md">中文</a>
</p>

<p align="center">
  <em>"No man ever steps in the same river twice."</em> — Heraclitus
</p>

---

## 🌊 Why This Exists

I'm a graduate student in fish ecology. My days are reading papers, analyzing data, writing reviews, tracking frontiers.

Then I noticed something. My coding agent could write code, but it didn't know glmmTMB's API changed last month. It could search literature, but it never asked "does this 2020 paper's conclusion still hold after the fishing ban?" It could run statistics, but it couldn't spot when five independent papers were all pointing to the same strange pattern — an **emergence signal** that might reshape our understanding of Yangtze fish recovery.

So I built this. Not to make a faster tool. To teach the machine the most precious instinct a researcher has: **knowing when to doubt what you think you know.**

---

## 🏛️ Two Pillars

<div align="center">
<table>
<tr>
<td width="50%" align="center">
<h3>🌊 Panta Rhei</h3>
<em>Everything Flows</em>
<p>The world is dynamic<br>Knowledge is provisional<br>Emergence is the norm</p>
</td>
<td width="50%" align="center">
<h3>⚡ Engineering as Restraint</h3>
<em>The DeepSeek Way</em>
<p>Energy is finite<br>Algorithms beat brute force<br>Don't compute what you don't need</p>
</td>
</tr>
</table>
</div>

**Panta Rhei** is epistemic humility. No conclusion is final. Every sentence carries a timestamp. Every method tracks its version. Every analysis leaves room for "check again later."

**Engineering as Restraint** is respect for limits. Not every module should fire at once. MoE sparse routing. Entropy-budgeted compute. Activation on explicit conditions — the way a brain doesn't fire all neurons while sleeping.

> Popper: Science is not about finding truth; it's about approaching it.
> Shannon: Information is the elimination of uncertainty.
>
> So what this project really does is **approach an ever-changing world with the least possible error — and know how much error remains.**

---

## ⚡ Quick Start

```bash
git clone https://github.com/fangtaocai041/fish-ecology-assistant.git
cd fish-ecology-assistant
powershell -ExecutionPolicy Bypass -File .reasonix\setup-migrate.ps1
```

### How you talk to it

| You say | It does |
|:--------|:--------|
| `"Research Yangtze fishing ban effects — run pipeline"` | 5-stage pipeline, bilingual EN/CN, emergence detection |
| `"Verify handbook chapter 2.2"` | Auto-check CRAN, probabilistic stale scoring, differential verify |
| `"Search ima KBs for stable isotope niche"` | IG-keyword routing, cross-KB dedup |

---

## 🧠 What's Inside

**12 subagents**, each activated only when needed:

| Agent | Does | Activates when |
|:------|:-----|:---------------|
| Research Pipeline (×5) | Plan → Search → Analyze → Write → Review | Stage-by-stage trigger |
| Paper Analyzer | Timeline analysis + emergence signals | DOI or abstract given |
| Stats Assistant | R code + method selection | Code/methods involved |
| ima Smart Search | Cross-13-knowledge-base search | Domain maps to ≥1 KB |
| Handbook Verifier | Auto CRAN version check | Explicitly requested |

**16 MCP tools** — search, R stats, OCR, reference management, knowledge base access.

| Capability | Before | **After** |
|:-----------|:------:|:---------:|
| Search engines | 1 | **5** |
| AI subagents | 4 generic | **12 specialized** |
| R statistics | — | ✅ 20+ ecology packages |
| Knowledge bases | — | ✅ 13 ima KBs |
| Setup | Manual | ✅ One command |

---

## 🌱

> Heraclitus: Everything flows; nothing stands still.
>
> So we never stamp anything "final." Only "best understanding as of now."

This is not a fixed toolset. It's a living system. When R packages update, it reminds you. When new patterns emerge, it notices. When your research deepens, it evolves with you.

---

<p align="center">
  <em>"The sun is new each day."</em> — Heraclitus<br>
  <sub>Built with Reasonix Code · Powered by DeepSeek · 2026</sub>
</p>
