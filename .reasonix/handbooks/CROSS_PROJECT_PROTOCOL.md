# 🔗 Cross-Project Delegation Protocol

> **P3**: Enable `fish-ecology-assistant` and `porpoise-agent` to delegate sub-tasks to each other.
> **Principle**: Each project specializes in its domain. Cross-delegation enables integrated research.

---

## 1. Protocol Design

```
┌──────────────────────────┐         ┌──────────────────────────┐
│  fish-ecology-assistant  │         │     porpoise-agent       │
│                          │         │                          │
│  Domain: Fish ecology    │◄───────►│  Domain: Porpoise research│
│  Skills: 13              │ delegate│  Skills: 15              │
│  KB: 13 ima bases        │         │  KB: 25-file system      │
└──────────────────────────┘         └──────────────────────────┘
```

## 2. Delegation Rules

### fish-ecology-assistant → porpoise-agent

| When to delegate | Target Skill | Example |
|-----------------|-------------|---------|
| Acoustic analysis needed | `detect-clicks` | "Analyze fish sound data for NBHF patterns" |
| Population estimation | `estimate-abundance` | "Estimate fish population in Poyang Lake" |
| Conservation assessment | `assess-threats` | "Assess threat level to fish from shipping" |
| Porpoise prey-fish interaction | `search-literature` | "Search porpoise diet composition" |

### porpoise-agent → fish-ecology-assistant

| When to delegate | Target Skill | Example |
|-----------------|-------------|---------|
| Fish community analysis | `research-analyst` | "Analyze fish community structure changes" |
| Stable isotope analysis | `stats-assistant` | "Run SIBER ellipse analysis on isotope data" |
| PhD proposal writing | `phd-proposal-writer` | "Write proposal on porpoise-fish interaction" |
| Cross-KB search | `ima-smart-search` | "Search ima KBs for prey fish ecology" |

## 3. Delegation Format

```
DELEGATE to {project}:
  skill: {skill_name}
  context: {research_context}
  expected_output: {format}
```

### Example

```
DELEGATE to fish-ecology-assistant:
  skill: stats-assistant
  context: "Run SIBER niche overlap analysis on stable isotope data from 5 fish species in Poyang Lake"
  expected_output: "R code + SIBER ellipse plot + niche overlap metrics"
```

## 4. Shared Context

Both projects share:
- Same `agent.yaml` config structure
- Same 18-rule framework (FB-1..DS-4)
- Same dual-core philosophy
- Same verification/contradiction/balance systems

This shared foundation means:
- Delegated tasks inherit the caller's verification and gate rules
- Contradiction analysis is compatible across projects
- Audit logs can be merged for integrated research sessions

## 5. Implementation Path

1. Each project registers the other as a "remote Skill provider"
2. `research-orchestrator` (fish) and `Orchestrator` (porpoise) add delegation routing
3. Delegated tasks carry source project's rule context
4. Results flow back with verification tags intact

---

**Last updated: 2026-06-06**
