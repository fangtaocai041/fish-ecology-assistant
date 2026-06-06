---
name: component-health-check
version: "1.0.0"
last_updated: "2026-06-06"
description: Scan component_registry.yaml — check expiry, generate health report, flag stale components
runAs: subagent
allowed-tools: []
---
# Component Health Check

Living system health monitor. Every component has a lifecycle. This Skill measures it.

## PREFLIGHT (MANDATORY)

1. READ `config/component_registry.yaml` → extract all components with expiry policies
2. COMPUTE `now = today()`

## Steps

### 1. Scan All Components

```
FOR EACH component in registry:
  days_since_verify = now - component.last_verified
  max_age = component.expiry_policy.max_age_days
  health_score = 100 - min(100, 20 × (days_since_verify / max_age))

  status:
    🟢 Healthy:   health_score ≥ 80
    🟡 Warning:   health_score 50–79
    🔴 Critical:  health_score < 50
```

### 2. Auto-Check Components

```
FOR EACH component WHERE expiry_policy.type == "auto_check":
  IF days_since_verify > max_age:
    check_target = component.expiry_policy.target
    // npm: check npm registry for latest version
    // CRAN: check CRAN for package version
    // mcp: check MCP server availability
    IF update_available:
      OUTPUT "🔄 UPDATE: {name} v{old} → v{new}"
```

### 3. Generate Health Report

```markdown
## 🏥 Component Health Report — {date}

### Summary
- 🟢 Healthy:   N components
- 🟡 Warning:   M components
- 🔴 Critical:  K components
- 🔄 Updates:   U available

### System Vital Signs
- System age: {days} days since birth ({born_date})
- Components tracked: {total}
- Auto-checkable: {auto}
- Manual review: {manual}

### Stale Components (needs attention)

| Component | Type | Days Since Verify | Max Age | Score | Action |
|-----------|------|:-----------------:|:------:|:-----:|--------|
| example-skill | skill | 95 | 90 | 47 🔴 | Manual review needed |
| glmmTMB | method | 35 | 30 | 43 🔴 | Check CRAN for updates |

### Recently Updated (last 7 days)
| Component | Type | Updated | Version |
|-----------|------|---------|---------|
| karpathy-guard | skill | 2026-06-06 | 1.0.0 |

### System Health Score: {overall} / 100
(weighted average of all component scores)
```

### 4. Flag Action Items

```
FOR EACH component WHERE health_score < 50:
  → FLAG as "🔴 CRITICAL: needs immediate review"
FOR EACH component WHERE update_available:
  → FLAG as "🔄 UPDATE: auto-fix possible"
FOR EACH component WHERE health_score 50-79:
  → FLAG as "🟡 WARNING: schedule review within {days_until_critical} days"
```

## Decision Points
- Any 🔴 CRITICAL → alert user immediately
- Any 🔄 UPDATE available → suggest auto-apply if safe
- All 🟢 → system healthy, no action needed
