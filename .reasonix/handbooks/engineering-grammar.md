# 🔧 Engineering Grammar — 工程语法

> **Purpose**: Translate philosophical principles (Systems Thinking) into **precise, machine-actionable engineering language**.
> Each rule is expressed as `WHEN condition THEN action WITH confidence`, mapped to concrete config paths and code methods.
>
> **Notation**: FOL (first-order logic) · Temporal logic · State-machine semantics · Control-theory idioms

---

## 0. Semantic Layer Overview

```
Philosophical Language          Engineering Language           Code Artifact
──────────────────────          ────────────────────           ─────────────
认识论循环 (Practice-Knowledge)  → Feedback Loop              → VerificationTag + cycle_triggers
矛盾分析 (Contradiction)         → Critical-Path Detection    → _analyze_contradiction()
阶段论   (Phased Strategy)       → State Machine              → PROTRACTED_WAR_STAGES + phase_gating
集中兵力 (Force Concentration)   → Weighted Resource Scheduler → contradiction_budget_multiplier
主动权   (Initiative)            → Proactive Trigger System   → frontier-tracker + _check_independent_path()
分类处理 (Differentiation)       → Severity-Based Exception Handler → ContradictionType enum
系统平衡 (Multi-Factor Balance)  → Pareto Multi-Objective     → research_balance.priorities
```

---

## 1. Feedback Loop (认识论循环)

**Philosophical source**: 《实践论》— "实践、认识、再实践、再认识，循环往复以至无穷"

**Engineering translation**:
> A **closed-loop control system** where output (conclusion) is fed back as input for the next iteration.
> The system maintains a **verification setpoint**: every claim must have `|sources| ≥ min_sources_core_claim`.
> The **error signal** is `error = min_sources_core_claim - |actual_sources|`. When `error > 0`, the claim is downgraded or blocked.

### Formal Definition

```
Let C be a claim.
Let S(C) = {s₁, s₂, ..., sₙ} be the set of independent sources for C.
Let τ_core = min_sources_core_claim  (default = 2)

VerificationStatus(C) :=
  |S(C)| ≥ τ_core                    → VERIFIED   (✅)
  |S(C)| = 1                         → PENDING    (⚠️)
  |S(C)| = 0                         → UNVERIFIABLE (🚫, blocked from output)
  ∃ inference_chain but |S(C)| < τ_core → HYPOTHESIS (❓)
```

### Control Loop (PID Analogy)

```
Setpoint:    every claim has ≥ τ_core sources
Process:     research pipeline (search → analyze → write)
Feedback:    Reviewer scores + source count
Controller:  revision loop (max_iterations = 3)
Actuator:    Writer revision or output gate

┌──────────┐    error     ┌────────────┐    action    ┌──────────┐
│ Setpoint ├─────────────→│ Controller  ├────────────→│ Process   │
│ τ_core=2 │              │ max_iter=3  │             │ pipeline  │
└──────────┘              └────────────┘             └─────┬─────┘
                                                           │
                                                     ┌─────▼─────┐
                                                     │ Feedback   │
                                                     │ Reviewer   │
                                                     └───────────┘
```

### WHEN → THEN

```
WHEN claim.produced()
THEN
  sources = claim.extract_sources()
  IF |sources| >= config.verification_loop.investigation_first.min_sources_core_claim
    THEN tag(VERIFIED) → allow_output
  ELSE IF |sources| == 1
    THEN tag(PENDING) → allow_output_with_warning
  ELSE IF |sources| == 0
    THEN tag(UNVERIFIABLE) → block_output → log "没有调查就没有发言权"
  ELSE
    THEN tag(HYPOTHESIS) → allow_output_in_discussion_only
```

### Code Mapping

| Level | Path |
|-------|------|
| Config | `verification_loop.verification_status.*` |
| Config | `verification_loop.investigation_first.*` |
| Config | `verification_loop.cycle_triggers.*` |
| Method | `Orchestrator._tag_verification()` |
| Type | `VerificationStatus` enum |
| Dataclass | `VerificationTag` |

---

## 2. Critical-Path Detection (矛盾分析)

**Philosophical source**: 《矛盾论》— "在复杂事物中，必有一种是主要的矛盾，规定或影响着其他矛盾"

**Engineering translation**:
> A **constraint-satisfaction problem** where the system must identify the **binding constraint** (principal contradiction) and allocate resources accordingly.
> This is equivalent to **critical path analysis** in project management: find the node whose delay delays the entire project, and assign it maximum priority.

### Formal Definition

```
Let Q be a research question.
Let Contradictions(Q) = {c₁, c₂, ..., cₙ} be the set of identified constraints.
Let Weight(c) ∈ {PRIMARY, SECONDARY, PERIPHERAL} be the priority class.

Principal(Q) := argmax_{c ∈ Contradictions(Q)} Impact(c) × Urgency(c)

BudgetAllocation(c) :=
  Weight(c) = PRIMARY    → 0.60 × TotalBudget
  Weight(c) = SECONDARY  → 0.30 × TotalBudget
  Weight(c) = PERIPHERAL → 0.10 × TotalBudget

ConstraintClass(c) :=
  c is data-logic-conflict    → ANTAGONISTIC  (BLOCKING)
  c is perspective-difference → NON_ANTAGONISTIC (NON_BLOCKING)
  c is resource/time-bound    → STRUCTURAL
  c is phase-specific         → PHASIC
```

### Transformation Detection (矛盾转化)

```
WHEN |EmergenceSignals| ≥ config.contradiction_analysis.transformation_threshold
  AND ∃ new_pattern ∉ existing_contradictions
THEN
  trigger(REANALYZE_PRINCIPAL_CONTRADICTION)
  log("涌现信号累积 → 主要矛盾可能已转化")
```

### WHEN → THEN

```
WHEN question.received(Q)
THEN
  contradictions = classify(Q)  // keyword-heuristic → LLM-powered in production
  principal = argmax(contradictions, key=impact × urgency)
  principal_aspect = dominant_factor(principal)
  ctype = classify_type(principal)  // ANTAGONISTIC | NON_ANTAGONISTIC | STRUCTURAL | PHASIC

  SET budget_multiplier = config.contradiction_analysis.contradiction_budget_multiplier
  ALLOCATE resources:
    primary_direction   ← 0.60 × budget × budget_multiplier
    secondary_direction ← 0.30 × budget
    peripheral_direction ← 0.10 × budget
```

### Code Mapping

| Level | Path |
|-------|------|
| Config | `contradiction_analysis.contradiction_levels.*` |
| Config | `contradiction_analysis.contradiction_types.*` |
| Config | `contradiction_analysis.contradiction_budget_multiplier` |
| Config | `contradiction_analysis.transformation_threshold` |
| Method | `Orchestrator._analyze_contradiction()` |
| Type | `ContradictionType` enum |
| Dataclass | `ContradictionSignal` |

---

## 3. State Machine (阶段论)

**Philosophical source**: 《论持久战》— "战略防御→战略相持→战略反攻"

**Engineering translation**:
> A **finite state machine (FSM)** with three macro-states and gated transitions.
> Each state has a three-layer goal hierarchy: `strategic → operational → tactical`.
> Transitions are guarded: no skip (¬skip), retreat allowed on dead-end.

### Formal Definition (FSM)

```
States S = {DEFENSIVE, STALEMATE, COUNTER_OFFENSIVE}

Initial state: DEFENSIVE  (Phase 1: Literature Review)

Transition function δ:
  δ(DEFENSIVE, phase_complete)        = STALEMATE
  δ(STALEMATE, phase_complete)        = COUNTER_OFFENSIVE
  δ(any, dead_end_detected)           = previous_state  // 战略退却 (strategic retreat)

Guard conditions:
  G(s → s'):  s'.predecessor.is_complete = true   // no skip
  G(s → s'):  human_approved(s') if s' ∈ APPROVAL_PHASES

Three-layer goal structure per state:
  State.goal.strategic   : Why  (root cause)
  State.goal.operational : What (deliverable)
  State.goal.tactical[]  : How  (concrete actions)
```

### State Transition Diagram

```
     ┌──────────┐    phase_complete    ┌──────────┐    phase_complete    ┌──────────────────┐
     │DEFENSIVE │─────────────────────→│STALEMATE │─────────────────────→│COUNTER_OFFENSIVE │
     │(Lit Rev) │←─────────────────────│(Analysis)│←─────────────────────│(Publish)         │
     └──────────┘   dead_end_detected  └──────────┘   dead_end_detected  └──────────────────┘
          │                                   │
          │  human_approval_required          │  human_approval_required
          ▼                                   ▼
     Field Survey                        Conservation
     (Phase 3)                           Assessment (Phase 4)
```

### WHEN → THEN

```
WHEN phase.transition_requested(current_phase, next_phase)
THEN
  IF current_phase.is_complete == false
    THEN reject("no_skip: complete current phase first")
  ELSE IF next_phase ∈ APPROVAL_PHASES AND human_approval == false
    THEN reject("approval_required")
  ELSE IF dead_end_detected(current_phase)
    THEN retreat_to ← previous_phase
         log("strategic_retreat: returning to planner")
  ELSE
    THEN advance_to(next_phase)
         annotate_strategic_layers(next_phase)
         log("phase_advanced: {current} → {next}")
```

### Code Mapping

| Level | Path |
|-------|------|
| Config | `phased_strategy.target_layers.*` |
| Config | `phased_strategy.phase_gating.*` |
| Config | `phased_strategy.protracted_war_mapping.*` |
| Method | `Orchestrator._annotate_strategic_layers()` |
| Method | `Orchestrator._should_continue()` |
| Class attribute | `Orchestrator.PROTRACTED_WAR_STAGES` |
| Dataclass | `PhaseStrategy` |

---

## 4. Weighted Resource Scheduler (集中兵力)

**Philosophical source**: 军事思想 — "集中优势兵力，各个歼灭敌人"

**Engineering translation**:
> A **priority-based weighted fair queuing (WFQ) scheduler**.
> Resources (token budget, compute time) are allocated by contradiction weight class,
> not uniformly. The principal contradiction gets `budget_multiplier × base_share`.

### Formal Definition

```
Let Budget be total available compute resources.
Let Classes = {PRIMARY, SECONDARY, PERIPHERAL}.
Let multiplier ∈ ℝ⁺ (default = 2.5).
Let base_share: Classes → [0,1] where Σ base_share = 1.0.

base_share = {PRIMARY: 0.60, SECONDARY: 0.30, PERIPHERAL: 0.10}

EffectiveAllocation(c) :=
  base_share(c) × multiplier    if c = PRIMARY
  base_share(c)                  otherwise

Constraint: Σ EffectiveAllocation ≤ Budget × (1 + (multiplier - 1) × base_share(PRIMARY))

"各个歼灭" (destroy one by one):
  ∀t₁, t₂ ∈ Tasks: execute(t₁) before execute(t₂) if priority(t₁) > priority(t₂)
  ¬parallel(PRIMARY, PRIMARY)  // never parallelize two primary tasks
```

### Independent Path Rule ("你打你的，我打我的")

```
WHEN method_selection(m)
THEN
  evaluate(m, context) independently
  DO NOT default_to(mainstream_method)
  IF mainstream_method ≠ m
    THEN annotate_output("主流方法: {mainstream}, 本研究选择: {m}, 理由: {context_specific_reason}")
```

### WHEN → THEN

```
WHEN resource_allocation(phase, contradictions)
THEN
  principal = contradictions.principal
  budget = estimate_budget(phase)
  allocation = {
    principal:   budget × 0.60 × config.contradiction_analysis.contradiction_budget_multiplier,
    secondary:   budget × 0.30,
    peripheral:  budget × 0.10,
  }
  schedule_serial(contradictions, order_by=weight, descending)
  log("budget_allocated", allocation)
```

### Code Mapping

| Level | Path |
|-------|------|
| Config | `contradiction_analysis.contradiction_budget_multiplier` |
| Config | `contradiction_analysis.contradiction_levels.*.budget_share` |
| Config | `research_balance.independent_path` |
| Method | `Orchestrator._check_independent_path()` |
| Pipeline | Serial execution (non-parallel primary tasks) |

---

## 5. Proactive Trigger System (主动权)

**Philosophical source**: 《论持久战》— "主动性，说的是军队行动的自由权"

**Engineering translation**:
> A **proactive event-driven trigger system** rather than purely reactive request-response.
> The system autonomously generates suggestions (frontier-tracker), asks clarifying questions (reverse-questioning), and evaluates methods independently (independent path).

### Formal Definition

```
Reactive mode:  user_request → system_response
Proactive mode: background_monitor → event_detected → suggestion_generated → user_notified

ProactiveTriggers := {
  frontier_tracker:     ◇(new_publication from tracked_labs) → suggest("研究方向: {topic}")
  contradiction_shift:  |EmergenceSignals| ≥ τ_transform → alert("主要矛盾可能已转化")
  method_obsolescence:  method.last_verified + expiry_period < now → alert("方法需重新验证")
  knowledge_gap:        |S(search_results)| < τ_min → ask_clarification("问题过于宽泛，建议聚焦: ...")
}

StrategicContemptTacticalRespect:
  strategic_layer:   assume_solvable(problem)        // bold goal-setting
  tactical_layer:    ∀ action: require_evidence()     // strict verification per step
```

### WHEN → THEN

```
WHEN background_monitor.idle()
THEN
  suggestions = frontier_tracker.poll()
  IF suggestions ≠ ∅
    THEN push(suggestions) to user
         tag each with contradiction_level

WHEN user_question.is_too_broad()  // undirected, no specific keywords
THEN
  ask_clarification("建议聚焦以下方向之一: ...")

WHEN method.selected(m)
THEN
  _check_independent_path(m, context)
  IF mainstream_uses_different_method
    THEN annotate_justification(m)
```

### Code Mapping

| Level | Path |
|-------|------|
| Config | `research_balance.independent_path` |
| Skill | `frontier-tracker` (periodic polling) |
| Method | `Orchestrator._check_independent_path()` |
| Method | `Orchestrator._understand_question()` (reverse-questioning hook) |

---

## 6. Severity-Based Exception Handler (矛盾分类处理)

**Philosophical source**: 《关于正确处理人民内部矛盾的问题》— "不同性质的矛盾，解决方法不同"

**Engineering translation**:
> A **severity-based exception handling taxonomy**, analogous to `BLOCKER / CRITICAL / WARNING / INFO` in bug trackers.
> Each contradiction type maps to a specific handling strategy and escalation path.

### Formal Definition

```
ExceptionClass = {BLOCKER, WARNING, CONSTRAINT, TRANSIENT}

Handler(ExceptionClass):
  BLOCKER (ANTAGONISTIC):
    → escalate to reasoning_model
    → increase token_budget
    → block subsequent phases until resolved
    → log level: ERROR

  WARNING (NON_ANTAGONISTIC):
    → annotate and continue
    → include in uncertainty_output
    → log level: WARN

  CONSTRAINT (STRUCTURAL):
    → record constraint
    → optimize within bounds
    → log level: INFO

  TRANSIENT (PHASIC):
    → tag for review at phase_boundary
    → do not block current phase
    → log level: DEBUG
```

### WHEN → THEN

```
WHEN contradiction.detected(c)
THEN
  class = classify(c)
  SWITCH class:
    CASE BLOCKER:
      force_resolve(c)           // invoke reasoning model, increase budget
      gate = BLOCK               // block downstream
      audit.log(ERROR, c)
    CASE WARNING:
      annotate(c)
      gate = PASS_WITH_NOTE      // continue with annotation
      audit.log(WARN, c)
    CASE CONSTRAINT:
      record(c)
      gate = PASS                // continue, note constraint
      audit.log(INFO, c)
    CASE TRANSIENT:
      tag(c, review_at=next_phase_boundary)
      gate = PASS                // continue, review later
      audit.log(DEBUG, c)
```

### Code Mapping

| Level | Path |
|-------|------|
| Config | `contradiction_analysis.contradiction_types.*` |
| Type | `ContradictionType` enum (ANTAGONISTIC, NON_ANTAGONISTIC, STRUCTURAL, PHASIC) |
| Method | `Orchestrator._analyze_contradiction()` |

---

## 7. Pareto Multi-Objective Optimizer (系统平衡)

**Philosophical source**: 《论十大关系》— "统筹兼顾"

**Engineering translation**:
> A **multi-objective optimization problem** with a partial order (priority chain).
> When objectives conflict, the system applies a **lexicographic preference**: scientific_rigor ≻ speed, ecological_significance ≻ statistical_significance, local_knowledge ≽ international_literature.

### Formal Definition

```
Let Objectives = {scientific_rigor, speed, ecological_significance,
                  statistical_significance, local_knowledge, international_literature,
                  depth, breadth, ...}

Priority chain (lexicographic ordering):
  scientific_rigor        ≻ speed
  ecological_significance ≻ statistical_significance
  local_knowledge         ≽ international_literature
  depth(primary)          ≻ breadth(secondary)

Pareto-optimal solution:
  A solution x is pareto-optimal iff
    ¬∃ y: (∀ obj ∈ Objectives: obj(y) ≥ obj(x)) ∧ (∃ obj: obj(y) > obj(x))

Balance check per phase:
  ∀ pair ∈ priority_pairs:
    IF phase_output.bias_toward(pair.lhs) > threshold
      THEN warn("过度偏向 {pair.lhs}, 检查 {pair.rhs} 是否被忽略")
```

### Ten Research Balances (十大研究平衡)

```
B₁: breadth        ⇄ depth            // 多引擎搜索 vs 单篇深入
B₂: speed          ⇄ scientific_rigor  // 快速产出 vs 严格验证
B₃: english_lit    ⇄ chinese_lit      // 国际文献 vs 国内灰色文献
B₄: quantitative   ⇄ qualitative      // 统计显著 vs 生态意义
B₅: new_method     ⇄ classic_method   // 前沿技术 vs 验证标准
B₆: compute        ⇄ human_judgment   // AI 自动 vs 人类判断
B₇: publish_speed  ⇄ rigor            // 发表压力 vs 科学严谨
B₈: local_scope    ⇄ global_scope     // 单点 vs 全流域
B₉: recent         ⇄ historical       // 最新 vs 经典基础
B₁₀: known         ⇄ unknown          // 确定性 vs 不确定性
```

### WHEN → THEN

```
WHEN phase.completed()
THEN
  FOR EACH balance_pair in config.research_balance.priorities:
    bias = measure_bias(phase_output, balance_pair)
    IF bias > imbalance_threshold
      THEN warn("imbalance: {balance_pair.pair}, bias={bias}")
           suggest_correction()

WHEN conflict(objective_A, objective_B)
THEN
  resolve by config.research_balance.priorities ordering
  // lexicographic: higher-priority objective wins
```

### Code Mapping

| Level | Path |
|-------|------|
| Config | `research_balance.priorities[]` |
| Config | `research_balance.independent_path` |
| Type | `ResearchBalance` dataclass |

---

## 8. Metarules (元规则)

Rules about how rules are applied:

```
M1: Specificity wins.
    WHEN ruleₐ and rule_b both match
    THEN apply the more specific rule.

M2: Evidence threshold is non-negotiable.
    ∀ claim ∈ output: |sources(claim)| ≥ 1  // "没有调查就没有发言权"
    ∀ core_claim ∈ output: |sources(claim)| ≥ 2

M3: Human gate for irreversible actions.
    ∀ action ∈ {field_survey, conservation_recommendation, publication_draft, data_deletion, external_api_write}:
      require(human_approval)

M4: Audit everything.
    ∀ state_change: log(state_before, state_after, trigger, timestamp)

M5: Fail loudly, recover gracefully.
    IF error.detected()
      THEN log(ERROR, details)
      IF recoverable THEN retreat_to_safe_state()
      ELSE alert_user()
```

---

## 📋 Rule Index (Quick Reference)

| ID | Engineering Name | Trigger | Action | Config Path |
|----|-----------------|---------|--------|-------------|
| FB-1 | Feedback Loop | claim.produced() | tag verification status | `verification_loop.verification_status` |
| FB-2 | Source Gate | claim.sources < 1 | block_output | `verification_loop.investigation_first` |
| CP-1 | Critical Path | question.received() | identify principal contradiction | `contradiction_analysis.contradiction_levels` |
| CP-2 | Budget Alloc | resource_allocation() | weighted allocation | `contradiction_analysis.contradiction_budget_multiplier` |
| SM-1 | State Advance | phase.complete() | advance to next state | `phased_strategy.phase_gating` |
| SM-2 | Strategic Retreat | dead_end_detected() | return to previous state | `phased_strategy.phase_gating.allow_retreat` |
| WF-1 | Weighted Schedule | resource_allocation() | allocate by weight class | `contradiction_analysis.contradiction_levels.*.budget_share` |
| WF-2 | Independent Path | method.selected() | evaluate independently | `research_balance.independent_path` |
| PT-1 | Proactive Suggest | monitor.idle() | push suggestions | `frontier-tracker` skill |
| PT-2 | Reverse Question | question.too_broad() | ask clarification | `_understand_question()` |
| EH-1 | Blocker Handler | contradiction = ANTAGONISTIC | force_resolve + block | `contradiction_analysis.contradiction_types.antagonistic` |
| EH-2 | Warning Handler | contradiction = NON_ANTAGONISTIC | annotate + continue | `contradiction_analysis.contradiction_types.non_antagonistic` |
| MO-1 | Pareto Check | phase.completed() | check imbalance | `research_balance.priorities` |
| MO-2 | Lexicographic | objective conflict | higher-priority wins | `research_balance.priorities[].rule` |

---

> **"实事求是" in engineering terms = `assert(evidence.exists())`.**
> No evidence → no claim. No investigation → no output.

**Last updated: 2026-06-06**
