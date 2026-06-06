# 🌱 Living System Implementation — 活系统贯彻方案

> **README 原文**: "这个项目不是一套固定的工具集——它是一个活的系统。每个组件都内置了过期机制、版本追踪和涌现感知。随着你的研究深入、R 包更新、新方法涌现，它会和你一起进化。"
>
> **目标**: 让这段话从愿景变为每一个组件的运行时行为。

---

## 0. 当前状态 vs 目标状态

| 维度 | 当前 | 目标 |
|------|------|------|
| **过期感知** | 仅 stats handbook (DS-3) | **所有组件**: Skills, MCP, KB, config, methods |
| **版本追踪** | R 包版本 | **全组件**: Skill 版本, MCP 版本, 知识库版本, 规则版本 |
| **涌现检测** | ✅ ≥3 源 (emergence) | ✅ 已有 + 矛盾转化检测 |
| **自适应** | P3 阈值自适应 (CP-2) | **全规则**: 所有 18 条规则根据效果自适应 |
| **进化** | 无 | **自动建议**: 过期组件 → 建议更新, 新方法 → 建议集成 |

---

## 1. 全组件过期感知

### 1.1 组件过期时间表

每个组件注册时标注 `last_verified` 和 `expiry_policy`:

```yaml
# 新增: config/component_registry.yaml
components:
  skills:
    research-planner:
      version: "1.0.0"
      last_verified: "2026-06-06"
      expiry_policy:
        type: "manual_review"       # manual_review | auto_check | static
        max_age_days: 90
    karpathy-guard:
      version: "1.0.0"
      last_verified: "2026-06-06"
      expiry_policy:
        type: "auto_check"
        check_target: ".reasonix/skills/karpathy-guard.md"
        max_age_days: 60

  mcp_tools:
    scholar:
      version: "latest"
      last_verified: "2026-06-06"
      expiry_policy:
        type: "auto_check"
        check_target: "npm registry"  # check for new versions
        max_age_days: 30

  knowledge_bases:
    ima_fish_ecology:
      version: "2026-06-06"
      last_verified: "2026-06-06"
      expiry_policy:
        type: "manual_review"
        max_age_days: 180

  methods:
    glmmTMB:
      version: "1.1.10"
      last_verified: "2026-06-06"
      expiry_policy:
        type: "auto_check"
        check_target: "CRAN"
        max_age_days: 30
```

### 1.2 过期检测 Skill

新增 `component-health-check` Skill:

```
## Component Health Check

PREFLIGHT: READ config/component_registry.yaml

FOR EACH component:
  days_since_verify = now - component.last_verified
  IF days_since_verify > component.expiry_policy.max_age_days:
    IF component.expiry_policy.type == "auto_check":
      check_for_updates(component.check_target)
      IF update_available:
        OUTPUT "🔄 {component.name}: v{old} → v{new} available"
    ELSE:
      OUTPUT "⚠️ {component.name}: {days_since_verify}d since last review (max {max_age_days}d)"

OUTPUT Health Report:
  ✅ Healthy: N components
  ⚠️ Needs review: M components
  🔄 Update available: K components
```

---

## 2. 全组件版本追踪

### 2.1 版本注册

每个 Skill 的 frontmatter 必须有版本号:

```yaml
---
name: research-planner
version: "1.0.0"
last_updated: "2026-06-06"
description: ...
---
```

### 2.2 版本变更日志

新增 `.reasonix/CHANGELOG.md` 追踪所有版本变更:

```markdown
# Component Changelog

## 2026-06-06

### Skills
- research-planner: v1.0.0 — initial version with contradiction analysis
- karpathy-guard: v1.0.0 — initial version with 18-rule enforcement

### Config
- agent.yaml: v1.0.0 — dual-core philosophy + 4 config sections

### Handbooks
- systems-thinking.md: v1.0.0
- engineering-grammar.md: v1.0.0
```

---

## 3. 涌现感知 — 已实现 + 增强

### 3.1 现有实现 ✅

| 机制 | 状态 | 规则 |
|------|:----:|------|
| 涌现信号检测 (≥3 源) | ✅ | emergence.threshold |
| 矛盾转化检测 (≥5 源) | ✅ | transformation_threshold |
| 死胡同检测 (4 信号) | ✅ | _detect_dead_end() |

### 3.2 增强: 新方法涌现检测

```
## New Method Emergence Detection

frontier-tracker periodically scans for:
  - New R packages in CRAN ecology section
  - New acoustic analysis methods in arXiv
  - New conservation frameworks in IUCN

WHEN new_method_detected AND relevance_score > threshold:
  → ALERT user: "新方法 {name} 可能适用于 {research_area}"
  → SUGGEST integration path
  → LOG to evolution log
```

---

## 4. 自适应 — 从 CP-2 扩展到全规则

### 4.1 当前: 仅 CP-2 自适应

```python
# 当前 P3 实现
_adapt_thresholds():  # 仅调整 contradiction_budget_multiplier
```

### 4.2 目标: 全 18 规则自适应

| 规则 | 自适应参数 | 调整逻辑 |
|------|-----------|---------|
| CP-2 | `contradiction_budget_multiplier` | 成功率 >80% → -0.2, <50% → +0.3 |
| FB-1 | `min_sources_core_claim` | 误报率高 → +1, 漏检率高 → -1 |
| FB-2 | `no_source_penalty` | 过于严格 → block→warn, 过于宽松 → warn→block |
| SM-2 | `allow_retreat` threshold | 退却频率高 → 降低触发阈值 |
| DS-1 | pipeline depth for MEDIUM importance | 效果好的问题类型 → 自动升级到 HIGH |
| EH-1 | ANTAGONISTIC detection sensitivity | 误报多 → 提高触发标准 |

```python
def _adapt_all_thresholds(self) -> dict:
    adaptations = {}
    for rule_id in ["CP-2", "FB-1", "FB-2", "SM-2", "DS-1", "EH-1"]:
        stats = self._rule_effectiveness.get(rule_id, {})
        if stats.get("fires", 0) >= 10:  # minimum sample
            adaptation = self._adapt_rule(rule_id, stats)
            if adaptation:
                adaptations[rule_id] = adaptation
    return adaptations
```

---

## 5. 进化机制 — 自动建议

### 5.1 Evolution Log

```
.evolution/
├── evolution-log.jsonl       # 每次自适应的记录
├── suggestions.json           # 待处理的改进建议
└── health-reports/            # 定期健康检查报告
```

### 5.2 自动建议生成

```
## Evolution Suggestion Engine

Triggers (any one fires):
  T1: component expired (expiry_policy max_age exceeded)
  T2: new method detected (frontier-tracker)
  T3: rule underperforming (success_rate < 30% for 20+ fires)
  T4: config inconsistency detected (config.validate() warnings)
  T5: new DeepSeek model available (model registry check)

Output format:
  {
    "trigger": "T1",
    "component": "research-planner",
    "suggestion": "Skill 已 90 天未验证，建议审查 contradiction_analysis 逻辑",
    "priority": "medium",
    "auto_fix_available": false
  }
```

---

## 6. 活系统指标仪表盘

### 6.1 健康评分

每个组件的健康评分:

```
HealthScore(component) :=
  100 - 20×(days_since_verify / max_age_days)  # 过期惩罚
      - 10×(unresolved_issues)                   # 未解决问题
      + 5×(recent_updates_in_last_30d)           # 近期更新奖励

HealthReport:
  🟢 Healthy (≥80):    N components
  🟡 Warning (50-79):  M components
  🔴 Critical (<50):   K components
```

### 6.2 活系统年龄

```
System age: days since first commit
Components born: total unique components created
Components evolved: total adaptations applied
Components retired: total deprecated components
Evolution rate: adaptations / day
```

---

## 7. 实现优先级

| 优先级 | 组件 | 工作量 | 文件 |
|:------:|------|:------:|------|
| P0 | component_registry.yaml | 30min | 新文件 ×2 |
| P0 | Skill frontmatter 版本号 | 15min | 14+16 Skills |
| P1 | component-health-check Skill | 1h | 新 Skill ×2 |
| P1 | Evolution Log 机制 | 30min | orchestrator.py + config |
| P1 | 全规则自适应 | 2h | orchestrator.py |
| P2 | 新方法涌现检测 | 1h | frontier-tracker 增强 |
| P2 | 活系统仪表盘 | 1h | health-report Skill |
| P3 | 自动修复引擎 | 3h | 新模块 |

---

> **"活的系统"不是比喻——它是可度量的。**
> 每个组件有出生日期 (created_at)、最后验证 (last_verified)、过期时间 (expiry_policy)、适应历史 (evolution_log)。
> 系统通过指标告诉你它有多"活"。

**Last updated: 2026-06-06**
