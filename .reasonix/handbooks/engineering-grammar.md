# 🔧 Engineering Grammar — 工程语法

> **Architecture Note**: fish-ecology-assistant runs on the **Reasonix Skill runtime** (Markdown playbooks + config-driven routing), not a Python orchestrator. The 18 WHEN→THEN rules execute at the Skill routing layer — Reasonix reads `agent.yaml` → matches rules → invokes Skills. There is no Python `orchestrator.py`; the "orchestrator" is Reasonix itself. For Python-level contradiction-driven execution, see porpoise-agent (`src/agent/orchestrator.py`) and cognitive-search-engine (`src/meso_agent._analyze_contradiction()`).
>
> **Purpose**: Translate philosophical principles into **precise, machine-actionable engineering language**.
> Each rule is expressed as `WHEN condition THEN action WITH confidence`, mapped to concrete `config/agent.yaml` paths and Reasonix Skill names.
>
> **Architecture**: Reasonix Skills (Markdown playbooks) — no Python orchestrator. All execution flows through agent.yaml config → Skill routing → MCP tools.
>
> **Notation**: FOL (first-order logic) · Temporal logic · State-machine semantics · Control-theory idioms

---

## 0. Semantic Layer Overview

```
Philosophical Language          Engineering Language           Executable Artifact
──────────────────────          ────────────────────           ───────────────────
认识论循环 (Practice-Knowledge)  → Feedback Loop              → verification_loop config + research-reviewer skill
矛盾分析 (Contradiction)         → Critical-Path Detection    → contradiction_analysis config + research-planner skill
阶段论   (Phased Strategy)       → State Machine              → phased_strategy config + research-orchestrator skill
集中兵力 (Force Concentration)   → Weighted Resource Scheduler → contradiction_levels.budget_share + karpathy-guard skill
主动权   (Initiative)            → Proactive Trigger System   → research_balance.independent_path + frontier-tracker skill
分类处理 (Differentiation)       → Severity-Based Exception Handler → contradiction_types config
系统平衡 (Multi-Factor Balance)  → Pareto Multi-Objective     → research_balance.priorities config
```

---

## 1. Feedback Loop (认识论循环)

**Source**: 《实践论》— "实践、认识、再实践、再认识，循环往复以至无穷"

**Engineering translation**:
> A **closed-loop control system**. Setpoint: every claim must have `|sources| ≥ min_sources_core_claim` (default 2).
> The **error signal** is `error = τ - |actual_sources|`. When `error > 0`, the claim is downgraded or blocked.
> The **controller** is the `research-reviewer` skill with `max_iterations = 3`.

### Formal Definition

```
Let C be a claim, S(C) its independent source set.
Let τ_core = verification_loop.investigation_first.min_sources_core_claim  (default 2)

VerificationStatus(C) :=
  |S(C)| ≥ τ_core  → VERIFIED      (✅, allow output)
  |S(C)| = 1       → PENDING       (⚠️, allow with warning)
  |S(C)| = 0       → UNVERIFIABLE  (🚫, block — "没有调查就没有发言权")
  inference_only   → HYPOTHESIS    (❓, discussion only)
```

### Control Loop

```
Setpoint (τ=2) → Controller (research-reviewer, max 3 rounds) → Process (pipeline) → Feedback (Reviewer scores)
```

### WHEN → THEN

```
WHEN research-writer.produces_output()
THEN
  research-reviewer evaluates:
    IF |sources| >= verification_loop.investigation_first.min_sources_core_claim
      THEN tag(VERIFIED) → allow_output
    ELSE IF |sources| == 1 THEN tag(PENDING) → allow with warning
    ELSE IF |sources| == 0 THEN tag(UNVERIFIABLE) → BLOCK → log "没有调查就没有发言权"
    ELSE tag(HYPOTHESIS) → allow in Discussion only
  IF score < threshold AND iteration < max_iterations THEN revise (return to writer)
```

### Code Mapping

| Level | Path | Runtime |
|-------|------|---------|
| Config | `verification_loop.verification_status.{verified,pending,hypothesis,unverifiable}` | Read by research-reviewer skill |
| Config | `verification_loop.investigation_first.{min_sources_per_claim, min_sources_core_claim}` | Gate check before output |
| Config | `verification_loop.max_iterations` (=3) | Binds research-reviewer revision rounds |
| Skill | `research-reviewer` | Executes 4-dimension scoring + revision gate |
| Skill | `research-writer` | Produces calibrated-language output |

---

## 2. Critical-Path Detection (矛盾分析)

**Source**: 《矛盾论》— "在复杂事物中，必有一种是主要的矛盾，规定或影响着其他矛盾"

**Engineering translation**:
> A **constraint-satisfaction problem**: find `argmax(Impact × Urgency)` across all identified constraints.
> The principal contradiction gets 2.5× resource multiplier and 60% budget share.
> Classify each constraint as `ANTAGONISTIC | NON_ANTAGONISTIC | STRUCTURAL | PHASIC`.

### Formal Definition

```
Principal(Q) := argmax_{c ∈ Contradictions(Q)} Impact(c) × Urgency(c)

BudgetAllocation(c) :=
  c.class = PRIMARY    → 0.60 × Budget × contradiction_budget_multiplier
  c.class = SECONDARY  → 0.30 × Budget
  c.class = PERIPHERAL → 0.10 × Budget

ConstraintClass(c) :=
  data_logic_conflict    → ANTAGONISTIC     (BLOCKING)
  perspective_difference → NON_ANTAGONISTIC (NON_BLOCKING)
  resource_bound         → STRUCTURAL
  phase_specific         → PHASIC
```

### WHEN → THEN

```
WHEN research-planner.activated(question)
THEN
  // Planner identifies principal contradiction as part of research plan
  principal = classify(question) via keyword-heuristic
  principal_aspect = dominant_factor(principal)
  annotate plan with {primary_contradiction, primary_aspect, secondary_contradictions, contradiction_type}

  // Resource allocation flows to pipeline config
  SET budget_multiplier = config.contradiction_analysis.contradiction_budget_multiplier
  ALLOCATE: primary(0.60 × multiplier), secondary(0.30), peripheral(0.10)

WHEN research-analyst detects |emergence_signals| >= transformation_threshold
THEN
  trigger(REANALYZE) → log "矛盾转化警告"
```

### Code Mapping

| Level | Path | Runtime |
|-------|------|---------|
| Config | `contradiction_analysis.contradiction_levels.{primary,secondary,peripheral}` | Priority classes |
| Config | `contradiction_analysis.contradiction_types.{antagonistic,non_antagonistic,structural,phasic}` | Exception taxonomy |
| Config | `contradiction_analysis.contradiction_budget_multiplier` (=2.5) | Resource multiplier |
| Config | `contradiction_analysis.transformation_threshold` (=5) | Emergence → contradiction shift |
| Skill | `research-planner` | Identifies principal contradiction in plan phase |
| Skill | `research-analyst` | Detects emergence signals → triggers transformation check |

---

## 3. State Machine (阶段论)

**Source**: 《论持久战》— "战略防御→战略相持→战略反攻"

**Engineering translation**:
> A **finite state machine (FSM)** with 3 macro-states. Each state has a three-layer goal hierarchy: `strategic → operational → tactical`.
> Transitions are gated: `no_skip = true`, `allow_retreat = true`, approval required for irreversible phases.

### Formal Definition (FSM)

```
States S = {DEFENSIVE, STALEMATE, COUNTER_OFFENSIVE}
Initial: DEFENSIVE (Planner → Executor)

δ(DEFENSIVE, complete) → STALEMATE    // Analyst activated
δ(STALEMATE, complete) → COUNTER_OFFENSIVE  // Writer → Reviewer
δ(any, dead_end)       → previous      // strategic retreat → back to Planner

Guards:
  G(s→s'): s.predecessor.is_complete ∧ (s' ∉ APPROVAL_PHASES ∨ human_approved)
  G(retreat): config.phased_strategy.phase_gating.allow_retreat = true

Pipeline mapping:
  DEFENSIVE         → Stage 1 (Planner) + Stage 2 (Executor)
  STALEMATE          → Stage 3 (Analyst)
  COUNTER_OFFENSIVE  → Stage 4 (Writer) + Stage 5 (Reviewer)
```

### WHEN → THEN

```
WHEN research-orchestrator.routes(current_stage, next_stage)
THEN
  IF current_stage.output == None THEN reject("no_skip")
  IF next_stage in {field_survey, conservation} AND !human_approved THEN reject
  IF dead_end THEN retreat_to(previous_stage)
  ELSE advance_to(next_stage)
```

### Code Mapping

| Level | Path | Runtime |
|-------|------|---------|
| Config | `phased_strategy.target_layers.{strategic,operational,tactical}` | Three-layer goal structure |
| Config | `phased_strategy.phase_gating.{no_skip,allow_retreat,retreat_strategy}` | Transition guards |
| Config | `phased_strategy.protracted_war_mapping.{defensive,stalemate,counter_offensive}` | State labels |
| Skill | `research-orchestrator` | Coordinates 5-stage pipeline, manages state transitions |
| Skill | `karpathy-guard` | Enforces sparse activation (only active stages fire) |

---

## 4. Weighted Resource Scheduler (集中兵力)

**Source**: Military thought — "集中优势兵力，各个歼灭敌人"

**Engineering translation**:
> A **priority-based weighted fair queuing (WFQ) scheduler**. PRIMARY gets `multiplier × base_share`.
> Serial execution (¬parallel for PRIMARY tasks). Independent method evaluation ("你打你的，我打我的").

### Formal Definition

```
base_share = {PRIMARY: 0.60, SECONDARY: 0.30, PERIPHERAL: 0.10}
EffectiveAllocation(c) := base_share(c) × multiplier if c=PRIMARY else base_share(c)
Serial: ∀ t₁,t₂ with priority(t₁) > priority(t₂): execute(t₁) before execute(t₂)
Independent: evaluate(method, context), NOT default_to(mainstream)
```

### WHEN → THEN

```
WHEN pipeline.stage_activation(contradiction_level)
THEN
  karpathy-guard allocates entropy budget:
    primary_direction   ← budget × 0.60 × contradiction_budget_multiplier
    secondary_direction ← budget × 0.30
    peripheral          ← budget × 0.10
  // Sparse activation: only active contradiction class fires

WHEN method_selection(m)
THEN
  evaluate(m, context) independently — do NOT default to mainstream
  IF mainstream ≠ m THEN annotate justification
```

### Code Mapping

| Level | Path | Runtime |
|-------|------|---------|
| Config | `contradiction_analysis.contradiction_budget_multiplier` (=2.5) | PRIMARY boost |
| Config | `contradiction_analysis.contradiction_levels.*.budget_share` | {0.60, 0.30, 0.10} |
| Config | `research_balance.independent_path` | "你打你的，我打我的" |
| Skill | `karpathy-guard` | Entropy budget + sparse activation (MoE-style routing) |
| Pipeline | `pipeline.stages[].activation` | Conditional stage activation (e.g. "executor_returns_results") |

---

## 5. Proactive Trigger System (主动权)

**Source**: 《论持久战》— "主动性，说的是军队行动的自由权"

**Engineering translation**:
> A **proactive event-driven trigger system**. Background monitors (frontier-tracker) push suggestions;
> system asks clarifying questions when input is too broad.

### Formal Definition

```
ProactiveTriggers := {
  frontier_tracker:     ◇(new_publication) → suggest("研究方向")
  contradiction_shift:  |Emergence| ≥ τ → alert("矛盾转化")
  method_obsolescence:  method.age > expiry → alert("重新验证")
  knowledge_gap:        |results| < τ_min → ask_clarification()
}
StrategicContemptTacticalRespect: bold goals (strategy), strict verification (tactics)
```

### WHEN → THEN

```
WHEN frontier-tracker detects new publication THEN push_suggestion(topic)
WHEN user question too broad (no specific keywords) THEN ask_clarification
WHEN method selected THEN evaluate_independently (not default to mainstream)
```

### Code Mapping

| Level | Path | Runtime |
|-------|------|---------|
| Config | `research_balance.independent_path` | Enable independent evaluation |
| Skill | `frontier-tracker` | Periodic polling of tracked labs/authors |
| Skill | `research-planner` | Reverse-questioning: narrows broad questions |

---

## 6. Severity-Based Exception Handler (矛盾分类处理)

**Source**: 《关于正确处理人民内部矛盾的问题》— "不同性质的矛盾，解决方法不同"

**Engineering translation**:
> **Exception taxonomy**: `BLOCKER | WARNING | CONSTRAINT | TRANSIENT`, each with distinct escalation path.

### Formal Definition

```
ExceptionClass = {BLOCKER, WARNING, CONSTRAINT, TRANSIENT}

Handler:
  BLOCKER (ANTAGONISTIC)     → escalate to reasoning model, ↑budget, BLOCK downstream
  WARNING (NON_ANTAGONISTIC) → annotate, PASS_WITH_NOTE
  CONSTRAINT (STRUCTURAL)    → record, PASS
  TRANSIENT (PHASIC)          → tag(phase_boundary), PASS
```

### WHEN → THEN

```
WHEN research-analyst classifies finding
THEN
  SWITCH contradiction_type:
    ANTAGONISTIC     → force_resolve, block downstream, log ERROR
    NON_ANTAGONISTIC → annotate, continue with note, log WARN
    STRUCTURAL        → record constraint, continue, log INFO
    PHASIC            → tag for next-phase review, continue, log DEBUG
```

### Code Mapping

| Level | Path | Runtime |
|-------|------|---------|
| Config | `contradiction_analysis.contradiction_types.{antagonistic,non_antagonistic,structural,phasic}` | Strategy + trigger per type |
| Skill | `research-analyst` | Classifies findings, detects contradiction type |

---

## 7. Pareto Multi-Objective Optimizer (系统平衡)

**Source**: 《论十大关系》— "统筹兼顾"

**Engineering translation**:
> **Lexicographic multi-objective optimization**. Priority chain: `scientific_rigor ≻ speed`, `ecological_significance ≻ statistical_significance`, `local_knowledge ≽ international_literature`.

### Lexicographic Priority Chain

```
scientific_rigor        ≻ speed
ecological_significance ≻ statistical_significance
local_knowledge         ≽ international_literature
depth(primary)          ≻ breadth(secondary)
```

### Ten Research Balances

```
B₁: breadth ⇄ depth    B₂: speed ⇄ rigor    B₃: EN ⇄ CN lit
B₄: quantitative ⇄ qualitative    B₅: new_method ⇄ classic
B₆: compute ⇄ human    B₇: publish ⇄ rigor   B₈: local ⇄ global
B₉: recent ⇄ historical    B₁₀: known ⇄ unknown
```

### WHEN → THEN

```
WHEN research-reviewer evaluates output
THEN
  FOR EACH pair in research_balance.priorities:
    IF bias > threshold THEN warn + suggest correction
WHEN conflict(A, B) THEN resolve by lexicographic order
```

### Code Mapping

| Level | Path | Runtime |
|-------|------|---------|
| Config | `research_balance.priorities[]` | Ordered priority pairs with rules |
| Config | `research_balance.independent_path` | Independent method evaluation |
| Skill | `research-reviewer` | 4-dimension scoring implicitly checks balance |

---

## 8. DeepSeek Efficiency Principles (效率即智能)

**Source**: DeepSeek engineering philosophy — "Efficiency Is Intelligence"

These 4 principles are the **runtime optimization layer** — they govern HOW compute is spent, not just WHAT to do. They complement the 7 Systems Thinking principles by providing concrete execution efficiency.

---

### D1. Entropy Budget (熵预算)

**Engineering translation**:
> Compute resources are allocated **proportionally to question importance**, not uniformly.
> PhD thesis → full pipeline. Casual query → single-step search. Each stage has an explicit `activation` condition.

#### Formal Definition

```
Let Q be a question.
Let Importance(Q) ∈ {LOW, MEDIUM, HIGH}.
Let Pipeline = {planner, executor, analyst, writer, reviewer}.

StageActivation(s, Q) :=
  s = planner                           → ALWAYS (lightweight, always-on)
  s = executor                          → planner_returns_queries(Q) ≠ ∅
  s = analyst                           → executor_returns_results(Q) ≠ ∅
  s = writer                            → analyst_returns_findings(Q) ≠ ∅
  s = reviewer                          → |writer_output(Q)| ≥ 500 chars

Budget(Q) :=
  Importance(Q) = LOW    → single-stage (executor only)
  Importance(Q) = MEDIUM → 3-stage (planner → executor → analyst)
  Importance(Q) = HIGH   → full 5-stage pipeline
```

#### WHEN → THEN

```
WHEN question.received(Q)
THEN
  importance = classify_importance(Q)
  SWITCH importance:
    LOW:    route_to(executor) only
    MEDIUM: route_to(planner → executor → analyst)
    HIGH:   route_to(full_pipeline)
  // Each stage uses its activation condition as a gate
  // Inactive stages = zero compute cost
```

#### Code Mapping

| Level | Path | Runtime |
|-------|------|---------|
| Config | `pipeline.stages[].activation` | Conditional gate per stage |
| Config | `pipeline.stages[].model` | Model routing (default vs reasoning) |
| Skill | `research-orchestrator` | Routes question → pipeline depth |
| Skill | `karpathy-guard` | Enforces activation conditions |

---

### D2. Sparse Activation (稀疏激活)

**Engineering translation**:
> **MoE (Mixture of Experts) routing**: each Skill/module is a silent neuron — fires only when its signal crosses threshold.
> Planner always runs (lightweight, 先头部队). All other stages are conditionally activated.

#### Formal Definition

```
Let Skills = {planner, executor, analyst, writer, reviewer,
              paper_analyzer, frontier_tracker, stats_assistant,
              ima_smart_search, verify_stats_handbook, ...}

Activation(s) :=
  s = planner                  → ALWAYS (∀ Q)
  s = executor                 → planner.produced_queries()
  s = analyst                  → executor.produced_results()
  s = writer                   → analyst.produced_findings()
  s = reviewer                 → writer.produced_output() ∧ |output| ≥ 500
  s = paper_analyzer           → user_requests_deep_analysis()
  s = frontier_tracker         → background_poll_interval_elapsed()
  s = stats_assistant          → analysis_involves_R_or_statistics()
  s = ima_smart_search         → domain_matches_knowledge_base()
  s = verify_stats_handbook    → code_or_method_referenced()

Silent neurons: ∀ s ∉ ActiveSet(Q): s.cost = 0
```

#### WHEN → THEN

```
WHEN pipeline.routes_to_stage(s)
THEN
  karpathy-guard checks activation(s):
    IF activation_condition_met THEN fire(s) → execute
    ELSE skip(s) → zero_cost
  // Result: only ~2-4 Skills active per request (not all 12+)
```

#### Code Mapping

| Level | Path | Runtime |
|-------|------|---------|
| Config | `pipeline.stages[].activation` | Per-stage activation condition |
| Config | `agents.*.enabled` | Agent enable/disable flags |
| Skill | `karpathy-guard` | MoE-style routing: entropy budget + sparse activation |
| Skill | `research-orchestrator` | Pipeline coordinator, activates stages per conditions |

---

### D3. Differential Verification (差分验证)

**Engineering translation**:
> **Probabilistic stale scoring**: never run full checks. Compute `P(stale)` only for changed packages.
> Review cycle = f(update_frequency, breaking_change_probability, user_dependency) — not fixed 3 months.

#### Formal Definition

```
Let H be a handbook chapter with R packages P = {p₁, ..., pₙ}.

For each p ∈ P:
  days_since_verify = now - p.last_verified
  update_frequency = mean_days_between_releases(p)
  breaking_change_risk = P(major_version_bump | update)

  P_stale(p) := 1 - exp(-λ × days_since_verify)
    where λ = f(update_frequency, breaking_change_risk, user_dependency)

  IF P_stale(p) > config.staleness_threshold
    THEN mark_for_review(p)
    ELSE skip(p)

ReviewCycle(p) := max(
  base_interval,
  min(update_frequency(p), user_dependency(p) × base_interval)
)
// NOT a fixed 3-month cycle — jointly determined
```

#### WHEN → THEN

```
WHEN verify_stats_handbook.triggered(chapter)
THEN
  packages = extract_dependencies(chapter)
  FOR EACH p IN packages:
    P_stale = compute_stale_probability(p)
    IF P_stale > threshold THEN verify_and_update(p)
    ELSE skip(p)
  // Only changed/unstable packages are checked
  // Stable packages are trusted until expiry

  next_review = compute_review_cycle(packages)  // dynamic, not fixed
  annotate chapter with {verified_date, next_review, packages_checked}
```

#### Code Mapping

| Level | Path | Runtime |
|-------|------|---------|
| Skill | `verify-stats-handbook` | Probabilistic stale scoring + differential verification |
| Config | (implicit in skill) | Staleness threshold, CRAN version check |
| Handbook | `.reasonix/handbooks/stats-methods.md` | Version-tracked method templates |

---

### D4. Information-Gain Routing (信息增益路由)

**Engineering translation**:
> Keywords ordered by **information gain**. P0 exact terms searched first → stop on hit.
> P2 redundant terms skipped. Cross-KB deduplication eliminates wasted reads.

#### Formal Definition

```
Let Q be a search query with keywords K = {k₁, ..., kₙ}.

InformationGain(k) := specificity(k) × rareness(k) / frequency_in_corpus(k)

Priority classes:
  P0 (exact):   specificity = high, unambiguous   → e.g. "glmmTMB", "SIBER"
  P1 (specific): specificity = medium              → e.g. "mixed effects model"
  P2 (generic):  specificity = low, high-frequency → e.g. "data analysis", "research"

SearchStrategy(K):
  1. Order K by InformationGain descending
  2. For each P0 term: search → IF hit THEN stop (no need for P1/P2)
  3. For P1 terms (if P0 no-hit): search → deduplicate
  4. Skip P2 terms (redundant, low signal)

Cross-KB dedup:
  ∀ result r₁ ∈ KBₐ, r₂ ∈ KB_b: IF sim(r₁, r₂) > τ THEN keep_higher_quality(r)
```

#### WHEN → THEN

```
WHEN search_query(Q)
THEN
  keywords = extract_keywords(Q)
  classify by information_gain:
    P0: ["glmmTMB", "δ¹³C", "SIBER"]         → search first, stop on hit
    P1: ["model selection", "niche overlap"]  → search if P0 no-hit
    P2: ["analysis methods", "ecology"]       → SKIP (redundant)
  FOR EACH KB:
    search in parallel
    cross-KB deduplicate (keep higher quality)
  log("info_gain_routing", {P0_hits, P1_hits, P2_skipped, dedup_count})
```

#### Code Mapping

| Level | Path | Runtime |
|-------|------|---------|
| Skill | `ima-smart-search` | Information-gain keyword ordering + cross-KB dedup |
| Config | (implicit in skill) | P0/P1/P2 classification rules |
| Knowledge Base | `knowledge_bases.ima` (13 KBs) | Target KB set for dedup |

---

### DeepSeek Principles — Rule Index (addendum)

| ID | Name | Trigger | Action | Config Path / Skill |
|----|------|---------|--------|---------------------|
| DS-1 | Entropy Budget | question received | allocate compute by importance | `pipeline.stages[].activation` + `research-orchestrator` |
| DS-2 | Sparse Activation | stage routing | fire only if condition met | `pipeline.stages[].activation` + `karpathy-guard` |
| DS-3 | Differential Verify | handbook chapter referenced | P(stale) check, not full verify | `verify-stats-handbook` skill |
| DS-4 | Info-Gain Routing | search query | P0 first → stop on hit, skip P2 | `ima-smart-search` skill |

---

## 9. Metarules (元规则)

```
M1: Specificity wins — more specific rule overrides general.
M2: Evidence non-negotiable — ∀ claim: |sources| ≥ 1; ∀ core_claim: |sources| ≥ 2.
M3: Human gate — ∀ action ∈ {field_survey, conservation, publication, data_delete, external_api}: require(human_approval).
M4: Audit everything — ∀ state_change: log(before, after, trigger, timestamp).
M5: Fail loudly, recover gracefully — log(ERROR), retreat if recoverable, else alert.
M6: Sparse activation — each Skill fires only when its activation condition is met (karpathy-guard routing).
M7: Efficiency is intelligence — entropy budget over uniform allocation, differential over full verification, information-gain over exhaustive search.
```

---

## 📋 Rule Index

| ID | Engineering Name | Trigger | Action | Config Path / Skill |
|----|-----------------|---------|--------|---------------------|
| FB-1 | Feedback Loop | writer produces output | reviewer tags verification | `verification_loop.verification_status` |
| FB-2 | Source Gate | `|sources| < 1` | block output | `verification_loop.investigation_first` |
| CP-1 | Critical Path | planner activated | identify principal | `contradiction_analysis.contradiction_levels` + `research-planner` |
| CP-2 | Budget Alloc | pipeline routing | weighted allocate | `contradiction_analysis.contradiction_budget_multiplier` + `karpathy-guard` |
| SM-1 | State Advance | stage complete | advance FSM | `phased_strategy.phase_gating` + `research-orchestrator` |
| SM-2 | Strategic Retreat | dead end | retreat state | `phased_strategy.phase_gating.allow_retreat` |
| WF-1 | Weighted Schedule | stage activation | by weight class | `contradiction_analysis.contradiction_levels.*.budget_share` |
| WF-2 | Independent Path | method selected | evaluate independently | `research_balance.independent_path` |
| PT-1 | Proactive Suggest | monitor idle | push suggestions | `frontier-tracker` skill |
| PT-2 | Reverse Question | question too broad | ask clarification | `research-planner` skill |
| EH-1 | Blocker | ANTAGONISTIC | force-resolve + block | `contradiction_analysis.contradiction_types.antagonistic` |
| EH-2 | Warning | NON_ANTAGONISTIC | annotate + continue | `contradiction_analysis.contradiction_types.non_antagonistic` |
| MO-1 | Pareto Check | reviewer evaluates | check balance | `research_balance.priorities` + `research-reviewer` |
| MO-2 | Lexicographic | objective conflict | higher-priority wins | `research_balance.priorities[].rule` |
| DS-1 | Entropy Budget | question received | allocate compute by importance | `pipeline.stages[].activation` + `research-orchestrator` |
| DS-2 | Sparse Activation | stage routing | fire only if condition met | `pipeline.stages[].activation` + `karpathy-guard` |
| DS-3 | Differential Verify | handbook referenced | P(stale) check, not full verify | `verify-stats-handbook` skill |
| DS-4 | Info-Gain Routing | search query | P0 first → stop on hit, skip P2 | `ima-smart-search` skill |

---

> **`assert(evidence.exists())`. No evidence → no claim. No investigation → no output.**

**Last updated: 2026-06-09**
**Architecture: Reasonix Skills (Markdown) + Python orchestrators (porpoise-agent, coilia-agent) — unified by eon-core。验证脚本: `scripts/verify_philosophy_rules.py` (18/18 通过)**

### Cross-Project Python Code Mappings (2026-06-09 新增)

| Rule ID | Python Implementation | Project |
|---------|----------------------|---------|
| FB-1 | `validator.py: enforce_independence()` | cognitive-search-engine |
| FB-2 | `orchestrator.py: _tag_verification()` | porpoise-agent |
| CP-1 | `meso_agent.py: _analyze_contradiction()` | cognitive-search-engine |
| CP-2 | `orchestrator.py: budget_multiplier` | porpoise-agent |
| SM-1 | `orchestrator.py: _should_continue()` | porpoise-agent |
| SM-2 | `orchestrator.py: _detect_dead_end()` | porpoise-agent |
| WF-1 | `orchestrator.py: budget_multiplier` | porpoise-agent |
| WF-2 | `validator.py: enforce_independence()` | cognitive-search-engine |
| DS-1 | `search_optimizer.py: CognitiveBudget` | eon-core |
| DS-2 | `karpathy-guard` Skill (MoE routing) | fish-ecology-assistant |
| DS-4 | `search_optimizer.py: EntropyGuide` | eon-core |
