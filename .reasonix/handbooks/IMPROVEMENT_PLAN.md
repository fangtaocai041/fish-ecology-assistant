# 🔧 Improvement Plan — Reasonix-Native

> **Constraint**: All improvements must work within the Reasonix Code platform.
> **Execution model**: Skills (markdown playbooks) + MCP tools + agent.yaml config + Python bridge (porpoise-agent).
> **Principle**: Don't fight the platform — extend it.

---

## 1. P0: Skill→Config Binding — From Instructional to Mandatory

### Current State
Skills have "Config Reference" sections telling the AI to read agent.yaml. But the AI can skip them.

### Reasonix-Native Fix
Add a **PREFLIGHT** section as the FIRST step of every Skill. This is a Reasonix convention — the AI always executes the first instruction.

```
## PREFLIGHT (MANDATORY — execute before all other steps)

1. READ `config/agent.yaml`
2. EXTRACT the following sections relevant to this Skill:
   - [list specific config paths]
3. STORE extracted values as runtime parameters
4. IF any required section is missing → USE hardcoded fallback → LOG warning
5. PROCEED to Steps only after PREFLIGHT completes
```

**Why it works in Reasonix**: The AI follows Skill instructions sequentially. Placing config reading as step 0 with MANDATORY labeling ensures it happens before any domain logic.

### Files to update
- `research-planner.md` — PREFLIGHT: contradiction_analysis.*
- `research-reviewer.md` — PREFLIGHT: verification_loop.* + research_balance.priorities
- `research-orchestrator.md` — PREFLIGHT: phased_strategy.* + pipeline.stages[].activation
- `research-analyst.md` — PREFLIGHT: contradiction_analysis.contradiction_types + emergence.*
- `research-writer.md` — PREFLIGHT: research_balance.* + verification_loop.verification_status
- `karpathy-guard.md` — PREFLIGHT: all config sections (already has fallback, add mandatory label)

---

## 2. P0: Porpoise-Agent Phase Handlers — Wire MCP Tools

### Current State
```python
async def _run_literature_review(self) -> dict:
    return {"status": "not_implemented", ...}
```

### Reasonix-Native Fix
Porpoise-agent runs as a Python bridge within Reasonix. It can invoke Skills and MCP tools through Reasonix's tool interface. Replace stubs with **Skill delegation**:

```python
async def _run_literature_review(self) -> dict:
    """Delegate to search-literature Skill via Reasonix tool interface."""
    # The Skill handles: scholar, article, scholarly, tavily, exa search
    result = await self._invoke_skill("search-literature", {
        "query": self.context.research_question,
        "max_papers": config.agents["literature"]["max_papers_per_search"],
        "sources": config.agents["literature"]["sources"],
    })
    return {"phase": "literature_review", "status": "completed", "result": result}
```

Each phase handler delegates to the corresponding Skill, which already has the domain logic. The orchestrator becomes a **router + state machine**, delegating execution to Skills.

### Mapping
| Phase | Delegates to Skill | MCP Tools (used by Skill) |
|-------|-------------------|--------------------------|
| Literature Review | `search-literature` | scholar, article, scholarly, tavily, exa |
| Data Analysis | `detect-clicks` / `analyze-acoustic` | rplay, coderunner, filesystem |
| Field Survey | `plan-survey` | (planning only, human-gated) |
| Conservation | `assess-threats` | scholar, article |
| Report Generation | `generate-report` | (generation only) |

---

## 3. P1: Dynamic Contradiction Analysis — Use Reasoning Model

### Current State
```python
if "acoustic" in q_lower: primary = "声学检测精度 vs 环境噪声干扰"
```

### Reasonix-Native Fix
Replace keyword matching with a **reasoning model call**. In Reasonix, this means invoking the reasoning model through the Skill system:

**For fish-ecology-assistant** (research-planner Skill):
```
## PREFLIGHT Step 2: Dynamic Contradiction Analysis

USE `thinking` tool (sequential reasoning) to analyze the research question:
  Prompt: "Identify the principal contradiction in this research question: {question}.
           Output format: {primary_contradiction, primary_aspect, secondary_contradictions, contradiction_type}"
  Model: deepseek-reasoner (config: pipeline.stages[0].model = 'reasoning')
```

**For porpoise-agent** (orchestrator.py):
```python
async def _analyze_contradiction(self, question: str) -> ContradictionSignal:
    """Use reasoning model for dynamic contradiction analysis."""
    prompt = (
        f"分析以下研究问题的主要矛盾、矛盾主要方面、次要矛盾和矛盾类型：\n"
        f"问题：{question}\n"
        f"输出JSON: {{primary_contradiction, primary_aspect, secondary_contradictions, contradiction_type}}"
    )
    response = await self._call_reasoning_model(prompt)  # deepseek-reasoner
    return ContradictionSignal(**response)
```

**Fallback**: If reasoning model unavailable, use current keyword heuristic as fallback.

---

## 4. P1: Dead-End Detection — Multi-Signal

### Current State
Only checks for unresolved ANTAGONISTIC contradictions.

### Reasonix-Native Fix
Add multiple dead-end signals, tracked via audit log:

```python
def _detect_dead_end(self, phase) -> bool:
    signals = []
    
    # Signal 1: Unresolved ANTAGONISTIC contradiction
    if any(s.type == ANTAGONISTIC for s in self.contradiction_signals):
        signals.append("unresolved_antagonistic")
    
    # Signal 2: Phase returned empty results
    if phase.last_output and phase.last_output.get("result_count", 0) == 0:
        signals.append("empty_results")
    
    # Signal 3: Repeated cycle (same phase 3+ times)
    if self.phase_iteration_count.get(phase, 0) >= 3:
        signals.append("repeated_cycle")
    
    # Signal 4: Tool failures exceeded threshold
    if self.tool_failure_count >= 3:
        signals.append("tool_failure_threshold")
    
    if signals:
        audit.log("dead_end_detected", {"phase": phase.value, "signals": signals})
        return True
    return False
```

---

## 5. P1: CI/CD — GitHub Actions for Reasonix Projects

### Reasonix-Native Fix
Create validation scripts that run on every push:

```yaml
# .github/workflows/validate.yml
name: Validate
on: [push, pull_request]
jobs:
  config:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Validate agent.yaml
        run: |
          python -c "
          import yaml
          with open('config/agent.yaml') as f:
              c = yaml.safe_load(f)
          # Check required sections exist
          for section in ['contradiction_analysis', 'verification_loop', 'phased_strategy', 'research_balance']:
              assert section in c, f'Missing: {section}'
          # Check consistency
          assert c['verification_loop']['max_iterations'] == c['orchestrator']['max_revision_rounds']
          print('✅ agent.yaml valid')
          "
  skills:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Validate Skills format
        run: |
          for skill in .reasonix/skills/*.md; do
            # Check frontmatter
            grep -q '^---$' "$skill" || echo "❌ $skill: missing frontmatter"
            # Check PREFLIGHT section
            grep -q 'PREFLIGHT\|Config Reference\|config/agent.yaml' "$skill" || echo "⚠️ $skill: no config reference"
          done
```

---

## 6. P2: Rule Compliance Auditor Skill

### Reasonix-Native Fix
Create a new Skill `rule-auditor` that checks all other Skills for rule compliance:

```
# .reasonix/skills/rule-auditor.md

## PREFLIGHT
1. READ config/agent.yaml → extract all 18 rule IDs and their config paths
2. READ all .reasonix/skills/*.md files
3. For each rule ID, verify at least one Skill references its config path

## Steps
1. Build rule→config mapping from engineering-grammar.md
2. Scan each Skill for config path references
3. Output compliance report: {rule_id: {covered_by: [skill_names], status: PASS|MISSING}}
4. Flag MISSING rules for human review
```

---

## 7. P2: Performance Tracking — Skill Activation Count

### Reasonix-Native Fix
Add activation logging to karpathy-guard:

```
## Activation Tracking (every request)

BEFORE executing any Skill:
  1. INCREMENT activation_counter[skill_name]
  2. LOG: {timestamp, skill_name, trigger_condition, contradiction_level}

AFTER pipeline completes:
  3. REPORT: {total_skills_activated, active_set, inactive_set, token_estimate_saved}
```

This produces empirical data for the "2-4 Skills active per request" claim.

---

## 8. Priority Roadmap (Reasonix-Native)

| # | Improvement | Effort | Files | Timeline |
|:--|------------|:------:|-------|:--------:|
| 1 | PREFLIGHT sections in all 6 Skills | 30 min | 6 × Skill.md | Today |
| 2 | Porpoise phase handlers → Skill delegation | 2 hr | orchestrator.py | This week |
| 3 | Dynamic contradiction analysis (reasoning model) | 1 hr | research-planner.md + orchestrator.py | This week |
| 4 | Multi-signal dead-end detection | 30 min | orchestrator.py | This week |
| 5 | GitHub Actions validation | 1 hr | .github/workflows/ | This week |
| 6 | Rule compliance auditor Skill | 1 hr | rule-auditor.md | Next week |
| 7 | Activation tracking in karpathy-guard | 30 min | karpathy-guard.md | Next week |

---

> **Key insight**: Within Reasonix, the improvement path is **Skill-first**.
> Every capability should be a Skill (or a Skill instruction), not external code.
> The Python orchestrator (porpoise-agent) delegates to Skills, not replaces them.

**Last updated: 2026-06-06**
