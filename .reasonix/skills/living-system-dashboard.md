---
name: living-system-dashboard
version: "1.0.0"
last_updated: "2026-06-06"
description: Generate full living system health dashboard — metrics, evolution log, auto-fix suggestions
runAs: subagent
allowed-tools: []
---
# Living System Dashboard

This Skill generates `get_living_system_report() → HealthDashboard` from `component_registry.yaml`.

## PREFLIGHT (MANDATORY)

1. READ `config/component_registry.yaml` → all 28 components
2. READ `config/agent.yaml` → config consistency check
3. SCAN `.reasonix/skills/*.md` → Skill frontmatter versions

## Dashboard Output

```markdown
# 🏥 Living System Dashboard — {date}

## Vital Signs

| Metric | Value |
|--------|-------|
| System Age | {age} days (born {born_date}) |
| Components Tracked | {total} |
| 🟢 Healthy | {healthy} |
| 🟡 Warning | {warning} |
| 🔴 Critical | {critical} |
| Rules Active | {rules_active} |
| Auto-Fixes Applied | {auto_fixes} |
| Health Score | {score}/100 {status} |

## Component Health

### 🔴 Critical (needs immediate action)
| Component | Type | Days Since Verify | Max Age | Health |
|-----------|------|:-----------------:|:------:|:------:|
| (list critical components) |

### 🟡 Warning (schedule review)
| Component | Type | Days Since Verify | Max Age | Health |
|-----------|------|:-----------------:|:------:|:------:|
| (list warning components) |

### 🟢 Healthy
{healthy_count} components within expiry window.

## Evolution Timeline

### Recent Adaptations (last 30 days)
| Date | Rule | Old Value | New Value | Success Rate |
|------|------|:---------:|:---------:|:------------:|
| (list from evolution log) |

### Skills Updated (last 30 days)
| Skill | Version | Updated |
|-------|---------|---------|
| karpathy-guard | 1.0.0 | 2026-06-06 |

## Auto-Fix Suggestions

| Priority | Trigger | Component | Suggestion | Auto-Fixable |
|:--------:|--------|-----------|------------|:------------:|
| critical | T1_expiry | skills/example | 已过期 15 天 | ❌ manual |
| medium | T3_config | agent.yaml | max_iterations 不一致 | ✅ auto |

## System Evolution Rate
- Adaptations applied: {total_adaptations}
- Evolution rate: {rate} / day
- Trend: 📈 improving / 📉 declining / ➡ stable
```

## Decision Points
- Any 🔴 → alert user: "系统存在 {critical} 个过期组件，建议立即审查"
- Auto-fixable suggestions → "可自动修复 {auto_fixable} 个问题，是否执行？"
- All 🟢 → "系统健康，无需操作"
