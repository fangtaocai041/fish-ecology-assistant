---
name: rule-auditor
version: "1.0.0"
last_updated: "2026-06-06"
description: Audit all Skills for rule compliance — verify every engineering rule (FB-1..DS-4) has a corresponding config reference in at least one Skill
runAs: subagent
allowed-tools: []
---
# Rule Auditor

Verify that every engineering rule has runtime enforcement — no rule is "declared but not enforced."

## PREFLIGHT (MANDATORY)

1. READ `config/agent.yaml` → extract all 4 system sections
2. READ `.reasonix/handbooks/engineering-grammar.md` → extract all 18 rule IDs
3. READ all `.reasonix/skills/*.md` files

## Steps

### 1. Build Rule→Config Mapping

From engineering-grammar.md, extract:

| Rule ID | Config Path | Expected in Skill |
|---------|------------|-------------------|
| FB-1 | `verification_loop.verification_status` | research-reviewer |
| FB-2 | `verification_loop.investigation_first` | research-reviewer |
| CP-1 | `contradiction_analysis.contradiction_levels` | research-planner |
| CP-2 | `contradiction_analysis.contradiction_budget_multiplier` | research-planner, karpathy-guard |
| SM-1 | `phased_strategy.phase_gating` | research-orchestrator |
| SM-2 | `phased_strategy.phase_gating.allow_retreat` | research-orchestrator |
| WF-1 | `contradiction_analysis.contradiction_levels.*.budget_share` | karpathy-guard |
| WF-2 | `research_balance.independent_path` | research-writer |
| PT-1 | (frontier-tracker skill) | frontier-tracker |
| PT-2 | (reverse-questioning) | research-planner |
| EH-1 | `contradiction_analysis.contradiction_types.antagonistic` | research-analyst |
| EH-2 | `contradiction_analysis.contradiction_types.non_antagonistic` | research-analyst |
| MO-1 | `research_balance.priorities` | research-writer, research-reviewer |
| MO-2 | `research_balance.priorities[].rule` | research-writer, research-reviewer |
| DS-1 | `pipeline.stages[].activation` | karpathy-guard, research-orchestrator |
| DS-2 | `pipeline.stages[].activation` | karpathy-guard |
| DS-3 | (verify-stats-handbook skill) | verify-stats-handbook |
| DS-4 | (ima-smart-search skill) | ima-smart-search |

### 2. Scan Skills for Config References

For each rule ID, check if at least one Skill references its config path:

```
FOR EACH rule IN rule_map:
  covered_by = []
  FOR EACH skill IN .reasonix/skills/*.md:
    IF skill.content contains rule.config_path:
      covered_by.append(skill.name)
  rule.coverage = covered_by
```

### 3. Output Compliance Report

```
## Rule Compliance Report

| Rule | Config Path | Covered By | Status |
|------|------------|------------|--------|
| FB-1 | verification_loop.verification_status | research-reviewer | ✅ PASS |
| FB-2 | verification_loop.investigation_first | research-reviewer | ✅ PASS |
| ... | ... | ... | ... |

Summary:
- ✅ PASS: N rules with ≥1 Skill coverage
- ⚠️ MISSING: M rules with 0 Skill coverage
- 🔴 CONFIG_MISSING: K rules with config path not found in agent.yaml
```

### 4. Flag Issues

For each MISSING rule:
- Output: `⚠️ Rule {ID} ({name}) has NO Skill coverage. Add config reference to appropriate Skill.`

For each CONFIG_MISSING rule:
- Output: `🔴 Rule {ID} config path {path} not found in agent.yaml. Add config section.`

## Decision Points
- All 18 rules PASS → ✅ System compliant
- Any rule MISSING → ⚠️ Gap identified, output fix instructions
- Any config MISSING → 🔴 Critical, output exact YAML to add
