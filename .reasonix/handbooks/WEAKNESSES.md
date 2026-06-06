# 🔍 Weaknesses & Improvement Roadmap

> **Honest self-assessment**: Every strength has a corresponding weakness. This document catalogs the gaps — the necessary precondition for improvement.

---

## 1. Critical Gaps

### 1.1 Skill→Config Link is Instructional, Not Programmatic (fish-ecology-assistant)

**Problem**: The 6 Skills now have "Config Reference" sections instructing the AI to read agent.yaml. But Skills are **markdown playbooks** — the AI follows them as natural language instructions, not as programmatic bindings. There is no guarantee the AI will actually read the config at runtime.

**Impact**: The philosophy→code mapping is documented but not enforced. If the AI skips the config reference step, the rules become decorative.

**Fix**: Implement a **config injection mechanism** in Reasonix that auto-appends relevant config sections to Skill prompts before execution. Or: move to a Python orchestrator (like porpoise-agent) for fish-ecology-assistant.

### 1.2 Porpoise-Agent Phase Handlers Are Stubs

**Problem**: 5 of 5 phase handlers return `"status": "not_implemented"`:
```python
async def _run_literature_review(self) -> dict:
    return {"phase": "literature_review", "status": "not_implemented", ...}
```

**Impact**: The orchestrator framework is complete, but the actual research execution is a skeleton. The 18 rules govern a pipeline that doesn't yet produce real research output.

**Fix**: Integrate actual MCP tool calls (scholar, article, tavily, etc.) into each phase handler. Wire up the search-literature, detect-clicks, and generate-report Skills.

### 1.3 Contradiction Analysis is Keyword-Heuristic, Not Analytical

**Problem**: Both projects use hardcoded keyword matching for contradiction analysis:
```python
if "acoustic" in q_lower: primary = "声学检测精度 vs 环境噪声干扰"
elif "conservation" in q_lower: primary = "保护措施效果 vs 持续增加的威胁因子"
```

**Impact**: The "principal contradiction" is selected from a fixed menu of 5 patterns. Real research questions have nuance that keyword matching cannot capture. The system claims to do contradiction analysis but actually does pattern matching.

**Fix**: Replace keyword heuristic with **LLM-powered contradiction analysis** — pass the question to a reasoning model (deepseek-reasoner) and ask it to identify the principal contradiction dynamically.

---

## 2. Structural Weaknesses

### 2.1 No Automated Rule Enforcement Verification

**Problem**: The 18 rules (FB-1..DS-4) are documented in 5 places (README, systems-thinking, engineering-grammar, activation-matrix, agent.yaml) but there is **no test that verifies** each rule is actually enforced at runtime.

**Impact**: Rule rot — as the codebase evolves, rules may silently stop being enforced.

**Fix**: Create a **rule compliance test suite** that programmatically verifies each rule ID maps to an active code path.

### 2.2 Two Architectures, One Philosophy — Synchronization Cost

**Problem**: fish-ecology-assistant (Reasonix Skills) and porpoise-agent (Python) share the same philosophical framework but implement it differently. Changes to the rule set must be manually synchronized across both projects.

**Impact**: Divergence risk. Over time, the two projects may develop inconsistent interpretations of the same rules.

**Fix**: Extract the shared philosophy/config/rule definitions into a **common submodule** or generate project-specific files from a single source of truth.

### 2.3 No Integration Between the Two Projects

**Problem**: Despite sharing the same philosophy and rule framework, the two projects are completely isolated. porpoise-agent cannot delegate a fish-ecology question to fish-ecology-assistant, and vice versa.

**Impact**: Missed opportunity for cross-domain research (e.g., "analyze the impact of fishing bans on porpoise prey fish communities").

**Fix**: Implement a **cross-agent orchestration protocol** where one project can delegate sub-tasks to the other.

---

## 3. Implementation Gaps

### 3.1 No Actual MCP Tool Integration (porpoise-agent)

**Problem**: The orchestrator imports and routes to phases, but no phase handler actually calls MCP tools (scholar, article, tavily, rplay, etc.). The 15 MCP services defined in config are **unused at runtime**.

**Impact**: The pipeline is a routing framework without payload execution.

**Fix**: Implement MCP client integration in each phase handler. For example, `_run_literature_review()` should call `scholar_mcp.search()` and `article_mcp.fetch()`.

### 3.2 No LLM Call in Orchestrator

**Problem**: The orchestrator routes phases and classifies contradictions but **never calls an LLM**. It's a pure rule-based router.

**Impact**: The contradiction analysis (CP-1), strategic layer annotation (SM-1), and verification tagging (FB-1) all use hardcoded logic. The system claims to be AI-powered but the orchestrator itself is deterministic.

**Fix**: Add LLM call hooks in `_analyze_contradiction()` and `_annotate_strategic_layers()` for dynamic, context-aware analysis.

### 3.3 Dead-End Detection is Overly Simplistic

**Problem**: `_detect_dead_end()` only checks for unresolved ANTAGONISTIC contradictions. It doesn't detect:
- Phase returning empty results after execution
- Repeated cycle without progress
- Config errors preventing phase completion
- MCP tool failures

**Impact**: SM-2 (Strategic Retreat) will rarely trigger in practice, making the retreat mechanism theoretical.

**Fix**: Add multiple dead-end signals: empty results, cycle counter, tool failure count, timeout detection.

---

## 4. Operational Gaps

### 4.1 No CI/CD Pipeline

**Problem**: Neither project has GitHub Actions, automated testing on push, or deployment automation.

**Impact**: Every change is manually tested. Regression risk is high.

**Fix**: Add `.github/workflows/test.yml` that runs `pytest` (porpoise-agent) and a config validation script (fish-ecology-assistant).

### 4.2 No Performance Benchmarks

**Problem**: Claims about "2-4 active Skills per request" and "sparse activation reducing cost" are **unmeasured**. No benchmarking data exists.

**Impact**: Performance claims are aspirational, not empirical.

**Fix**: Create a benchmark suite that measures: token consumption per pipeline depth, Skill activation count, response latency, source verification accuracy.

### 4.3 No Production Deployment Documentation

**Problem**: Neither project has deployment instructions beyond "clone and run setup script." No Docker, no cloud deployment, no scaling guidance.

**Impact**: Cannot be deployed in a production research environment without significant manual configuration.

**Fix**: Add Docker Compose setup, environment variable documentation, and production hardening guide.

---

## 5. Design Limitations

### 5.1 The 18 Rules Are Fixed — No Learning Mechanism

**Problem**: The rule framework is static. It doesn't learn from past executions, doesn't adjust thresholds based on success rates, and doesn't evolve.

**Impact**: The system cannot improve over time. The "Panta Rhei" philosophy says "everything flows" but the rules are frozen.

**Fix**: Add a **rule effectiveness tracker** that logs which rules fire and their outcomes, then adjusts thresholds (e.g., `contradiction_budget_multiplier`) based on historical performance.

### 5.2 English-Dominant with Chinese Supplement

**Problem**: While the system claims bilingual support, the codebase, config keys, rule IDs, and documentation are predominantly English. Chinese is secondary.

**Impact**: Non-English-speaking researchers may struggle with the technical layer even though the README is translated.

**Fix**: Internationalize config keys and rule IDs, or provide a Chinese-first configuration variant.

### 5.3 Tight Coupling to DeepSeek

**Problem**: Both projects are designed exclusively for DeepSeek models (deepseek-chat, deepseek-reasoner). Model switching would require significant refactoring.

**Impact**: Vendor lock-in. If DeepSeek API changes pricing or availability, the projects are affected.

**Fix**: Abstract the model layer behind a provider-agnostic interface (support OpenAI, Anthropic, local models).

---

## 6. Test Coverage

### 6.1 Thin Test Suite (porpoise-agent)

```
36 tests, 0.18s — config, loop, orchestrator, tools
```

**Missing tests**:
- Contradiction analysis edge cases (empty question, non-matching keywords)
- Dead-end detection scenarios
- Contradiction gate logic (all 4 types)
- Config validation edge cases
- Phase transition state machine
- Non-interactive mode
- Audit logging format

### 6.2 No Tests for fish-ecology-assistant

**Problem**: Reasonix Skills have zero automated testing. Correctness depends entirely on manual review.

**Fix**: Create a Skill validation script that checks: frontmatter format, tool references, config path validity, rule ID consistency.

---

## 7. Improvement Priority Matrix

| Priority | Gap | Effort | Impact |
|:--------:|-----|:------:|:------:|
| 🔴 P0 | Phase handlers are stubs (porpoise-agent) | High | Critical |
| 🔴 P0 | No MCP tool integration (porpoise-agent) | High | Critical |
| 🟡 P1 | Contradiction analysis is keyword-based | Medium | High |
| 🟡 P1 | Skill→config link is instructional only | Medium | High |
| 🟡 P1 | No CI/CD | Low | Medium |
| 🟢 P2 | No automated rule enforcement tests | Medium | Medium |
| 🟢 P2 | No performance benchmarks | Medium | Low |
| 🟢 P2 | Two-project synchronization cost | High | Medium |
| ⚪ P3 | No learning mechanism | High | Long-term |
| ⚪ P3 | DeepSeek vendor lock-in | High | Long-term |
| ⚪ P3 | No cross-project integration | High | Long-term |

---

> **Honesty is the precondition for improvement.**
> These projects have a strong philosophical and architectural foundation. The next phase is making every documented capability **actually executable** — closing the gap between specification and implementation.

**Last updated: 2026-06-06**
