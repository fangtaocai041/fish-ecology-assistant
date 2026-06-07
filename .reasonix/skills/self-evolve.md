---
name: self-evolve
version: "1.0.0"
last_updated: "2026-06-07"
description: Post-pipeline self-evolution — evaluate research execution, trigger parameter adaptation, log evolution history, update component health
runAs: subagent
allowed-tools: [read_file, write_file, search_content]
---
# 🧬 Fish Ecology Assistant Self-Evolution Engine

> **借鉴**: cognitive-search-engine/skills/self-evolve.md — post-search feedback loop → auto-adjust
> **传播**: porpoise-agent/src/skills/self-evolve/SKILL.md (同步创建)
> **Execution**: post_pipeline_feedback_loop() → evaluate_pipeline() → trigger_evolution() → log_evolution() → update_health()

## PREFLIGHT

1. READ `config/evolution.yaml` → current adaptive parameters
2. READ `config/component_registry.yaml` → component health status
3. READ `config/agent.yaml` → current pipeline config

## Post-Pipeline Evolution Cycle

### evaluate_pipeline(result: ResearchResult) → Metrics

```
verification_pass_rate = count(verified_claims) / max(total_claims, 1)
pipeline_completion_rate = count(sessions_with_all_5_stages) / total_sessions
contradiction_resolution_rate = count(resolved_principal_contradictions) / max(total_sessions, 1)
emergence_signal_ratio = count(emergence_signals) / max(total_sessions, 1)
token_efficiency = total_output_tokens / max(total_input_tokens / 1000, 1)
reviewer_score_avg = avg(review_scores) FOR last_N_sessions
skill_activation_count = avg(active_skills_per_session)
search_precision = count(relevant_results) / max(total_results, 1)
baseline = avg(last_10_evolution_logs.metrics)

RETURN Metrics(verification_pass_rate, pipeline_completion_rate, contradiction_resolution_rate,
               emergence_signal_ratio, token_efficiency, reviewer_score_avg,
               skill_activation_count, search_precision, baseline)
```

### trigger_evolution(m: Metrics, config: EvolutionConfig) → list[Adaptation]

```
adaptations = []

# Trigger 1: verification_weak — 验证薄弱
IF m.verification_pass_rate < 0.5 FOR 3 CONSECUTIVE sessions:
  config.min_sources_core_claim = min(5, config.min_sources_core_claim + 1)
  config.max_revision_rounds = min(5, config.max_revision_rounds + 1)
  adaptations.append(Adaptation("verification_weak", "min_sources_core_claim", +1,
    reason="提高三角验证门槛 (FB-1, FB-2)"))
  adaptations.append(Adaptation("verification_weak", "max_revision_rounds", +1))

# Trigger 2: quality_decline — 质量下降
IF m.reviewer_score_avg < 60 FOR 3 CONSECUTIVE sessions:
  config.max_revision_rounds = min(5, config.max_revision_rounds + 1)
  adaptations.append(Adaptation("quality_decline", "max_revision_rounds", +1,
    reason="输出质量下降，增加修订轮次"))

# Trigger 3: contradiction_unresolved — 矛盾未解决
IF m.contradiction_resolution_rate < 0.3 FOR 5 CONSECUTIVE sessions:
  config.contradiction_budget_multiplier = min(4.0, config.contradiction_budget_multiplier + 0.5)
  adaptations.append(Adaptation("contradiction_unresolved", "contradiction_budget_multiplier", +0.5,
    reason="增加主要矛盾资源倾斜 (CP-2)"))

# Trigger 4: emergence_noise — 涌现噪声
IF m.emergence_signal_ratio > 0.5 FOR 5 CONSECUTIVE sessions:
  config.emergence_threshold = min(6, config.emergence_threshold + 1)
  adaptations.append(Adaptation("emergence_noise", "emergence_threshold", +1,
    reason="涌现误报过多，提高阈值"))

# Trigger 5: efficiency_gain — 效率提升
IF m.token_efficiency > m.baseline.token_efficiency × 1.2 FOR 5 CONSECUTIVE:
  config.skill_activation_threshold = min(0.5, config.skill_activation_threshold + 0.05)
  adaptations.append(Adaptation("efficiency_gain", "skill_activation_threshold", +0.05,
    reason="DS-2 稀疏激活优化 — 更少 skill 激活"))

# Trigger 6: efficiency_loss — 效率下降
IF m.token_efficiency < m.baseline.token_efficiency × 0.7 FOR 5 CONSECUTIVE:
  config.search_engine_count = max(5, config.search_engine_count - 2)
  adaptations.append(Adaptation("efficiency_loss", "search_engine_count", -2,
    reason="减少并行引擎节约 token"))

# Trigger 7: pipeline_failure — 管线失败
IF m.pipeline_completion_rate < 0.4 FOR 3 CONSECUTIVE sessions:
  adaptations.append(Adaptation("pipeline_failure_spike", "status", "alert",
    reason="管线失败率飙升 — 建议人工审查 pipeline 阶段配置"))

RETURN adaptations
```

### log_evolution(adaptations: list[Adaptation])

```
FOR EACH a IN adaptations:
  append_jsonl(config.evolution.evolution_log.path, {
    timestamp: now_iso(),
    param: a.param_name,
    old_value: a.old_value,
    new_value: a.new_value,
    trigger: a.trigger,
    pre_metric: a.pre_metric,
    effectiveness_delta: null,
    session_id: current_session_id,
  })
```

### update_health(adaptations: list[Adaptation])

```
UPDATE config/component_registry.yaml:
  FOR EACH affected_component IN adaptations.affected_components:
    component.last_verified = now()
    component.effectiveness = recompute_metrics()
  living_system.health_score = recompute_health()
  living_system.last_health_check = now()
```

## Cross-Project Evolution Data Share

```
IF config.evolution.cross_project.enabled:
  FOR EACH peer IN config.evolution.cross_project.peers:
    shared_metrics = filter(m, peer.share)
    IF peer.evolution_path EXISTS:
      append to peer's evolution-log with source="fish-ecology-assistant"
```

## Self-Evolution Report

```markdown
## 🧬 Fish Ecology Assistant Evolution Report — {date}

### Parameters Adapted
| Param | Old | New | Trigger | Expected Effect |
|-------|:---:|:---:|---------|----------------|
| min_sources_core_claim | 3 | 4 | verification_weak | +33% source threshold |
| contradiction_budget_multiplier | 2.5 | 3.0 | contradiction_unresolved | +20% resources to principal |

### Evolution History
- Total adaptations: {N}
- Evolution rate: {rate}/session
- Trend: 📈 improving / 📉 declining / ➡ stable

### System Health
- Components: {total}, {healthy} 🟢, {warning} 🟡, {critical} 🔴
- Health score: {score}/100
- Skills near expiry: {list}
- MCP services near expiry: {list}
- Cross-project peers: porpoise ({status}), cognitive ({status})
```

## Integration Note

This skill is triggered after each research pipeline completes.
It reads from `config/evolution.yaml` (adaptive parameters) and `config/component_registry.yaml` (health tracking).
Evolution data is shared with porpoise-agent and cognitive-search-engine via `coordination.yaml`.
