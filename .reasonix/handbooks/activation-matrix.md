# ⚡ Activation Matrix — 激活矩阵

> **Purpose**: Define precisely WHEN each component activates, the dependency chain between components, and joint-activation coordination rules.
> This is the **runtime scheduling specification** — the bridge between static config (agent.yaml) and dynamic execution (Skill routing).

---

## 0. Activation Dependency Graph

```
User Question
    │
    ▼
┌─────────────────────────────────────────────────────┐
│ Phase 0: karpathy-guard (ALWAYS — inline guard)      │
│   → Apply DS-1..DS-4, FB-1..FB-2 metarules          │
│   → Read: pipeline.stages[].activation               │
└──────────────┬──────────────────────────────────────┘
               │
    ┌──────────▼──────────┐
    │ CP-1: Contradiction  │  ← research-planner reads contradiction_analysis.*
    │ Analysis             │     ALWAYS active (lightweight)
    └──────────┬──────────┘
               │
    ┌──────────▼──────────┐
    │ Stage 1: Planner     │  ← research-planner
    │ Activation: ALWAYS    │     Reads: contradiction_analysis.*
    │ Output: research plan │     Rule: CP-1, CP-2
    └──────────┬──────────┘
               │ IF planner_returns_queries
    ┌──────────▼──────────┐
    │ Stage 2: Executor    │  ← research-executor
    │ Activation: COND      │     5 engines parallel
    │ Output: source DB     │     DS-4: Info-Gain Routing via ima-smart-search
    └──────────┬──────────┘
               │ IF executor_returns_results
    ┌──────────▼──────────┐
    │ Stage 3: Analyst     │  ← research-analyst
    │ Activation: COND      │     Reads: contradiction_types (EH-1, EH-2)
    │ Output: findings      │     Emergence detection (≥3 sources)
    └──────────┬──────────┘
               │ IF analyst_returns_findings
    ┌──────────▼──────────┐
    │ Stage 4: Writer      │  ← research-writer
    │ Activation: COND      │     Reads: research_balance.* (WF-2, MO-1)
    │ Output: draft         │     Calibrated language + time-anchoring
    └──────────┬──────────┘
               │ IF |writer_output| ≥ 500 chars
    ┌──────────▼──────────┐
    │ Stage 5: Reviewer    │  ← research-reviewer
    │ Activation: COND      │     Reads: verification_loop.* (FB-1, FB-2)
    │ Output: pass/revise   │     Reads: research_balance.priorities (MO-1)
    └──────────┬──────────┘
               │
    ┌──────────▼──────────┐
    │ Revision Loop        │  IF needs_revision AND iteration < max_iterations
    │ max_iterations = 3    │     → Return to Writer
    └──────────────────────┘
```

---

## 1. Component Activation Table

### Pipeline Stages (sequential, gated)

| Stage | Skill | Activation Condition | Reads Config | Rules | Model |
|:-----:|-------|---------------------|-------------|-------|:-----:|
| 0 | `karpathy-guard` | ALWAYS (inline) | `pipeline.stages[].activation` | DS-1..4, FB-1..2 | — |
| 1 | `research-planner` | ALWAYS | `contradiction_analysis.*` | CP-1, CP-2 | default |
| 2 | `research-executor` | `planner_returns_queries ≠ ∅` | — | DS-4 | default |
| 3 | `research-analyst` | `executor_returns_results ≠ ∅` | `contradiction_analysis.contradiction_types` | EH-1, EH-2, emergence | reasoning |
| 4 | `research-writer` | `analyst_returns_findings ≠ ∅` | `research_balance.*`, `verification_loop.verification_status` | WF-2, MO-1 | default |
| 5 | `research-reviewer` | `|writer_output| ≥ 500` | `verification_loop.*`, `research_balance.priorities` | FB-1, FB-2, MO-1 | reasoning |

### Domain Skills (on-demand, parallel-capable)

| Skill | Activation Condition | Reads Config | Rules |
|-------|---------------------|-------------|-------|
| `frontier-tracker` | background_poll OR user_request | — | PT-1 |
| `paper-analyzer` | user_requests_deep_analysis | — | — |
| `stats-assistant` | analysis_involves_R_or_statistics | — | — |
| `stats-method-finder` | method_lookup_requested | — | — |
| `ima-smart-search` | domain_matches_knowledge_base | `knowledge_bases.ima` | DS-4 |
| `verify-stats-handbook` | code_or_method_referenced | — | DS-3 |
| `phd-proposal-writer` | user_requests_proposal | — | — |
| `zotero-assistant` | zotero_query_requested | — | — |
| `obsidian-assistant` | obsidian_action_requested | — | — |

---

## 2. Joint Activation Rules (联合激活)

### Parallel Activation

```
WHEN Stage 2 (Executor) activates:
  → 5 engines parallel: tavily ‖ exa ‖ scholar ‖ article ‖ scholarly
  → ima-smart-search parallel IF domain_matches_knowledge_base

WHEN Stage 3 (Analyst) activates:
  → emergence_detection ‖ contradiction_classification  (parallel sub-tasks)

WHEN frontier-tracker polls:
  → independent of pipeline (background, non-blocking)
```

### Serial Activation (Gated Chain)

```
Stage 1 → Stage 2: gate = planner_returns_queries
Stage 2 → Stage 3: gate = executor_returns_results
Stage 3 → Stage 4: gate = analyst_returns_findings
Stage 4 → Stage 5: gate = |writer_output| ≥ 500
Stage 5 → Revision: gate = needs_revision AND iterations < max_iterations
Revision → Stage 4: gate = reviewer_provided_notes
```

### Mutual Exclusion

```
¬parallel(Stage_4, Stage_5)         // Reviewer only after Writer
¬parallel(Stage_3, Stage_4)         // Writer only after Analyst
¬parallel(PRIMARY, PRIMARY)         // Never two primary tasks in parallel (WF-1)
```

---

## 3. Config→Skill Read Mapping

| Config Section | Read By | When |
|---------------|---------|------|
| `pipeline.stages[].activation` | `karpathy-guard`, `research-orchestrator` | Every request |
| `contradiction_analysis.contradiction_levels` | `research-planner` | Stage 1 |
| `contradiction_analysis.contradiction_budget_multiplier` | `research-planner`, `karpathy-guard` | Stage 1 |
| `contradiction_analysis.contradiction_types` | `research-analyst` | Stage 3 |
| `contradiction_analysis.transformation_threshold` | `research-analyst` | Stage 3 (emergence check) |
| `verification_loop.verification_status` | `research-reviewer`, `research-writer` | Stage 4-5 |
| `verification_loop.investigation_first` | `research-reviewer` | Stage 5 |
| `verification_loop.max_iterations` | `research-reviewer` | Stage 5 (revision loop) |
| `phased_strategy.phase_gating` | `research-orchestrator` | Between stages |
| `phased_strategy.protracted_war_mapping` | `research-orchestrator` | Stage labeling |
| `research_balance.priorities` | `research-writer`, `research-reviewer` | Stage 4-5 |
| `research_balance.independent_path` | `research-writer` | Stage 4 |

---

## 4. Contradiction Gate Coordination

```
Stage 1 (Planner):
  → Identify principal contradiction (CP-1)
  → Output: {primary_contradiction, contradiction_type, budget_multiplier}

Stage 3 (Analyst):
  → IF contradiction_type = ANTAGONISTIC:
      → EH-1: BLOCK downstream, escalate to reasoning model
      → _detect_dead_end() returns True → SM-2 strategic retreat
  → IF contradiction_type = NON_ANTAGONISTIC:
      → EH-2: annotate, PASS_WITH_NOTE

Stage 3→4 transition:
  → IF EH-1 BLOCK active: stop pipeline, alert user
  → IF EH-2 active: pass findings with warning annotations
```

---

## 5. Revision Loop Coordination

```
Reviewer scores → decision:
  ✅ Pass (0 critical, ≤2 moderate) → output final report
  🔄 Revise (1-2 critical, ≤5 moderate) → return to Writer with notes
  ❌ Fail (≥3 critical) → present issues to user

Max iterations: verification_loop.max_iterations (=3)
After max_iterations: force-output with uncertainty annotations

Coordination:
  Writer ← Reviewer notes (surgical: only fix flagged items)
  Reviewer ← Writer revision (full re-evaluation, not incremental)
```

---

## 6. Dynamic Model Routing

```
Stage 1 (Planner):   default model   (cheap, fast)
Stage 2 (Executor):  default model   (I/O bound)
Stage 3 (Analyst):   reasoning model (complex pattern recognition)
Stage 4 (Writer):    default model   (generation)
Stage 5 (Reviewer):  reasoning model (validation + scoring)

Switch to reasoning model WHEN:
  - contradiction_type = ANTAGONISTIC (EH-1 force-resolve)
  - emergence signal detected (≥3 independent sources)
  - dead-end detected (SM-2 strategic retreat analysis)
```

---

## 7. Idle/Background Activation

```
frontier-tracker:
  Activation: periodic (background poll)
  Frequency: user-defined or default daily
  Output: push suggestions to user (PT-1)
  Non-blocking: does not interfere with pipeline

verify-stats-handbook:
  Activation: on-demand (when code/method referenced)
  DS-3: P(stale) differential check, not full verification
```

---

> **Coordination Principle**: Inactive components cost zero. Only the active path consumes resources.
> **Sparse Activation (DS-2)**: ~2-4 of 12 Skills active per typical request.

**Last updated: 2026-06-06**
