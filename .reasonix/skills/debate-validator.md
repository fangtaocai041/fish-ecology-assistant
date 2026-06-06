---
name: debate-validator
version: "1.0.0"
last_updated: "2026-06-06"
description: D₂ Multi-Agent Debate Mesh — statistician + mathematician + code_auditor cross-validate findings before publication
runAs: subagent
allowed-tools:
  - coderunner_run-code
  - thinking_sequentialthinking
---
# 🕸️ Debate Validator (D₂ 面 — 网状交叉验证)

> **Gemini D₂ 进化**: 从线性 Pipeline(D₁) 进化为多 Agent 网状拓扑(D₂)。
> 三个独立 Agent 对同一结论进行三角交叉验证，≥2/3 同意才通过。

## PREFLIGHT (MANDATORY)

1. READ input findings (from analyst/writer)
2. SPAWN 3 sub-agents: statistician, mathematician, code_auditor
3. Each agent independently validates the findings

## S-T-V Structure

```
S (State):  findings from analyst → shared to all 3 agents
T (Transition): each agent applies its validation logic independently
V (Validation): debate synthesis — ≥2/3 agree → pass
```

## Agent 1: Statistician (统计学家)

```
CHECK:
  - p-value < 0.05 for all claimed significant results
  - effect size reported (not just significance)
  - no p-hacking (all tests pre-registered in methods)
  - sample size adequate for claimed power
  - confidence intervals provided

OUTPUT: {pass: bool, issues: [str], confidence: float}
```

## Agent 2: Mathematician (数学家)

```
CHECK:
  - all model assumptions explicitly stated and verified
  - no division by zero, log(0), or other mathematical errors
  - convergence confirmed for iterative methods
  - degrees of freedom correctly calculated
  - formulas match between methods and results

OUTPUT: {pass: bool, issues: [str], confidence: float}
```

## Agent 3: Code Auditor (代码审计)

```
CHECK:
  - R/Python code is reproducible (set.seed / random_state)
  - package versions pinned (sessionInfo / requirements.txt)
  - no unsafe eval() or system() calls
  - input data path is documented
  - output matches claimed results within rounding tolerance

OUTPUT: {pass: bool, issues: [str], confidence: float}
```

## Debate Synthesis

```
QUORUM = 2  # ≥2/3 agents must pass

IF sum([s.pass, m.pass, c.pass]) >= QUORUM:
  verdict = PASS
  confidence = avg([s.confidence, m.confidence, c.confidence])
ELSE:
  verdict = FAIL
  issues = merge_all_issues()

OUTPUT:
  - verdict: PASS | FAIL
  - confidence: 0.0-1.0
  - dissenting_agent: which agent(s) dissented
  - fix_suggestions: concrete steps to address issues
```

## Decision Points
- All 3 pass → ✅ publish with full confidence
- 2/3 pass → ⚠️ publish with caveats from dissenter
- ≤1/3 pass → ❌ return to analyst for revision
