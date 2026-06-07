# 🔍 Weaknesses & Improvement Roadmap

> **Honest self-assessment**: Every strength has a corresponding weakness. This document catalogs the gaps — the necessary precondition for improvement.
> **Updated 2026-06-07**: Cross-project audit — several items fixed, new gaps identified.

---

## 0. Fixed Since 2026-06-06

| # | Item | Status | Detail |
|---|------|:------:|--------|
| ✅ | Phase handlers stubs (porpoise) | Fixed | 16 SKILL.md files created in `src/skills/`, orchestrator `not_implemented` stubs removed |
| ✅ | CI/CD missing (both projects) | Fixed | `.github/workflows/validate.yml` deployed on all three projects |
| ✅ | Cross-project integration isolation | Partial | `coordination.yaml` v3.1.0 with S-T-V triangle, cross_delegation protocol defined. Code-level call_remote_skill() still pending |
| ✅ | porpoise agent.version 0.1.0 vs fish 2.0.0 | Fixed | porpoise: 1.0.0; fish: 2.0.0 (independent semver, shared coordination) |
| ✅ | README.zh.md v3→v4 (porpoise) | Fixed | Chinese README now at v4.1, fully aligned with English |
| ✅ | MCP count mismatches in READMEs | Verified | All three projects: badge counts match actual config |

---

## 1. Critical Gaps

### 1.1 Skill→Config Link is Instructional, Not Programmatic (fish-ecology-assistant)

**Problem**: The 25 Skills have "Config Reference" sections instructing the AI to read agent.yaml. But Skills are **markdown playbooks** — the AI follows them as natural language instructions, not as programmatic bindings.

**Impact**: The philosophy→code mapping is documented but not enforced. If the AI skips the config reference step, the rules become decorative.

**Fix**: Implement a **config injection mechanism** in Reasonix that auto-appends relevant config sections to Skill prompts before execution. Or: move to a Python orchestrator (like porpoise-agent).

### 1.2 Contradiction Analysis is Keyword-Heuristic, Not Analytical

**Problem**: Both fish and porpoise projects use hardcoded keyword matching for contradiction analysis. 5 fixed patterns cannot capture real research nuance.

**Impact**: The "principal contradiction" is selected from a fixed menu. The system claims contradiction analysis but implements pattern matching.

**Fix**: Replace keyword heuristic with **LLM-powered contradiction analysis**.

### 1.3 No Self-Evolution Engine (fish + porpoise)

**Problem**: cognitive-search-engine has `evolution.yaml` (4 adaptive params: satisfice_threshold, ig_prune_threshold, trust_score_threshold, max_graph_depth) with post-search feedback loop. Neither fish nor porpoise has equivalent self-evolution.

**Impact**: The "Panta Rhei — everything flows" philosophy says the system evolves, but only cognitive actually auto-adjusts parameters.

**Fix**: Add `config/evolution.yaml` + `self-evolve` skill to fish and porpoise. Share evolution data via coordination.yaml.

---

## 2. Structural Weaknesses

### 2.1 No Automated Rule Enforcement Verification

**Problem**: 18 rules (FB-1..DS-4) documented in 5+ places but no test verifies each rule is actually enforced at runtime.

**Fix**: Create a **rule compliance test suite** that programmatically verifies each rule ID maps to an active code path.

### 2.2 Two Architectures, One Philosophy — Synchronization Cost

**Problem**: fish-ecology-assistant (Reasonix Skills / markdown) and porpoise-agent (Python orchestrator) share the same philosophy but implement differently. Changes must be manually synced.

**Fix**: Extract shared philosophy/config/rule definitions into a **common submodule** or generate project-specific files from a single source of truth.

### 2.3 Cross-Project Delegation: Protocol Exists, Code Missing

**Problem**: `coordination.yaml` §cross_delegation defines DELEGATE protocol format. `agent.yaml` in both fish and porpoise defines `export_skills` / `import_skills`. But no `call_remote_skill()` function exists in either orchestrator.

**Fix**: Implement cross-project delegation in both orchestrators. First target: fish delegating stats-assistant to porpoise, porpoise delegating species-search to cognitive.

---

## 3. Implementation Gaps (porpoise-agent)

### 3.1 MCP Client Not Called in Orchestrator

**Problem**: 16 MCP servers defined, 16 SKILL.md files exist. But the Python orchestrator (`orchestrator.py`) does not directly call MCP tools — it routes to phases that rely on Reasonix to invoke SKILL.md files.

**Impact**: The Python orchestrator is a coordination framework; actual tool execution happens via Reasonix reading SKILL.md instructions.

**Fix**: (Two paths) A) Add MCP client calls directly in orchestrator phase handlers. B) Keep current architecture and document clearly that Reasonix is the execution runtime.

### 3.2 No LLM Call in Orchestrator Core

**Problem**: The orchestrator (`orchestrator.py`, 1380 lines) routes phases and classifies contradictions without calling any LLM. Core logic is deterministic rule-based.

**Fix**: Add LLM call hooks for dynamic contradiction analysis and phase planning.

---

## 4. Operational Gaps

### 4.1 No Performance Benchmarks

**Problem**: Claims about "2-4 active Skills per request" and "sparse activation reducing cost" are unmeasured.

**Fix**: Create a benchmark suite measuring token consumption, Skill activation count, response latency, source verification accuracy.

### 4.2 No Cross-Project CI/CD

**Problem**: Each project has its own `.github/workflows/validate.yml` but no unified cross-project validation (e.g. checking coordination.yaml consistency across all three).

**Fix**: Add cross-project validation step to CI.

---

## 5. Design Limitations

### 5.1 The 18 Rules Are Fixed — No Learning (fish + porpoise)

**Problem**: Rule framework is static. cognitive has self-evolve; fish and porpoise don't.

**Fix**: See §1.3 — add evolution.yaml to both fish and porpoise.

### 5.2 Tight Coupling to DeepSeek

**Problem**: All three projects designed for DeepSeek models. Vendor lock-in risk.

**Fix**: Abstract model layer behind provider-agnostic interface (already partially done via Gemini/OpenAI config stubs).

---

## 6. Improvement Priority Matrix (Updated)

| Priority | Gap | Effort | Impact | Who |
|:--------:|-----|:------:|:------:|:---:|
| 🔴 P0 | MCP client integration (porpoise orchestrator) | High | Critical | porpoise |
| 🟡 P1 | LLM-driven contradiction analysis (both) | Medium | High | fish + porpoise |
| 🟡 P1 | Self-evolution engine (fish + porpoise) | Medium | High | fish + porpoise |
| 🟡 P1 | Skill→config programmatic binding | Medium | High | fish |
| 🟡 P1 | Cross-delegation implementation (call_remote_skill) | Medium | High | fish + porpoise |
| 🟢 P2 | Rule enforcement verification tests | Medium | Medium | all |
| 🟢 P2 | Performance benchmarks | Medium | Low | all |
| 🟢 P2 | Cross-project CI/CD validation | Low | Medium | all |
| ⚪ P3 | Common submodule for shared philosophy | High | Long-term | all |
| ⚪ P3 | Model layer abstraction (multi-provider) | High | Long-term | all |

---

> **Honesty is the precondition for improvement.**
> v6.1 (2026-06-07) closed the documentation gap: all READMEs aligned, all badge counts verified, WEAKNESSES.md refreshed on both ends. The next major milestone is **code-level cross-delegation** and **self-evolution for fish + porpoise**.

**Last updated: 2026-06-07**
