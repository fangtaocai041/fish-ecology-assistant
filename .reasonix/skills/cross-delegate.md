---
name: cross-delegate
version: "1.0.0"
last_updated: "2026-06-07"
description: Cross-project skill delegation — call skills in porpoise-agent or cognitive-search-engine
runAs: subagent
allowed-tools: [read_file, search_content, run_skill]
---
# 🔗 Cross-Project Delegation Skill

> **Protocol**: `DELEGATE to {project}: skill={name} context={...}`
> **Config**: `coordination.yaml` §cross_delegation + `config/agent.yaml` §cross_delegation
> **Peers**: porpoise-agent (T) · cognitive-search-engine (V)

## PREFLIGHT

1. READ `D:\Reasonix\coordination.yaml` → current delegation rules
2. READ `config/agent.yaml` §cross_delegation → import_skills / export_skills
3. IDENTIFY target project and skill

---

## Delegation Registry

### Export (fish → others)

| Skill | Available To | Use Case |
|-------|:------------:|----------|
| `stats-assistant` | porpoise | R统计分析 — 生态/遗传模型 |
| `research-analyst` | porpoise | 数据分析 — 涌现检测 + 共识演化 |
| `phd-proposal-writer` | porpoise | 博士研究计划撰写 |
| `ima-smart-search` | porpoise | 跨知识库智能搜索 |

### Import (others → fish)

| Skill | From | Use Case |
|-------|:----:|----------|
| `detect-clicks` | porpoise | 声学脉冲检测 — 鱼探仪数据分析 |
| `estimate-abundance` | porpoise | 种群丰度估计 — cue counting/distance sampling |
| `assess-threats` | porpoise | 威胁评估 — IUCN 标准 |
| `search-literature` | porpoise | 豚类文献搜索 |
| `graph-search-engine` | cognitive | 物种文献认知搜索 — Hub-and-Spoke |
| `cognitive-species-search` | cognitive | 认知物种搜索 — 符号学+语言学+OCR变体 |

---

## Execution Protocol

### delegate_to_porpoise(skill: str, context: dict) → result

```
FORMAT:
  DELEGATE to porpoise-agent:
    skill: {skill}
    context: {context}
    expected_output: {format}

VALIDATE skill IN ["detect-clicks", "estimate-abundance", "assess-threats", "search-literature"]:
  IF valid:
    INVOKE porpoise-agent/src/skills/{skill}/SKILL.md
    RETURN result
  ELSE:
    RETURN { error: "skill not available", available: [...] }
```

### delegate_to_cognitive(skill: str, context: dict) → result

```
FORMAT:
  DELEGATE to cognitive-search-engine:
    skill: {skill}
    context: {context}
    expected_output: {format}

VALIDATE skill IN ["graph-search-engine", "cognitive-species-search", "chinese-academic-search"]:
  IF valid:
    INVOKE cognitive-search-engine/skills/{skill}.md
    RETURN result
  ELSE:
    RETURN { error: "skill not available", available: [...] }
```

### auto_route(context: dict) → delegation_plan

```
IF context CONTAINS ["acoustic", "click", "PAM", "echolocation", "声学", "脉冲"]:
  → delegate_to_porpoise("detect-clicks", context)

IF context CONTAINS ["abundance", "population", "density", "丰度", "种群"]:
  → delegate_to_porpoise("estimate-abundance", context)

IF context CONTAINS ["threat", "IUCN", "conservation status", "威胁", "保护等级"]:
  → delegate_to_porpoise("assess-threats", context)

IF context CONTAINS ["species", "literature", "review", "papers", "文献", "综述"]:
  → delegate_to_cognitive("graph-search-engine", context)

IF context CONTAINS ["variant", "OCR", "typo", "变体", "拼写"]:
  → delegate_to_cognitive("cognitive-species-search", context)

DEFAULT:
  → suggest available skills from both peers
```

---

## Examples

### Example 1: Fish needs acoustic analysis

```
Input: "分析这批鱼探仪数据中的脉冲信号特征"
→ auto_route detects "acoustic" + "脉冲"
→ delegate_to_porpoise("detect-clicks", {
    data: "fish_echosounder_sample.wav",
    threshold_db: -120.0,  # 鱼探仪阈值偏低
    bandpass_low: 50000,    # 鱼类声学频段
  })
```

### Example 2: Fish needs species literature

```
Input: "搜索鳤(Ochetobius elongatus)的全部文献"
→ auto_route detects "species" + "文献"
→ delegate_to_cognitive("graph-search-engine", {
    genus: "Ochetobius",
    species: "elongatus",
    mode: "Hub-and-Spoke",
  })
```

### Example 3: Manual delegation

```
Input: "让江豚agent评估长江禁渔对鱼类群落的影响"
→ delegate_to_porpoise("assess-threats", {
    context: "长江十年禁渔 → 鱼类群落恢复 → 江豚饵料资源变化",
    region: "长江中下游",
  })
```

---

## Cross-Validation

After delegation, always cross-validate results:

```
1. RECEIVE result from peer project
2. IF result CONTAINS factual claims:
     cross_validate via cognitive-search-engine credibility scoring
     tag claims: ✅ verified (≥3 sources) / ⚠️ pending / ❓ hypothesis
3. IF contradiction detected between fish result and peer result:
     log as cross-project contradiction → flag for MesoAgent review
```

---

## Integration with MesoAgent

This skill is designed to be called by the Meso-Cosmos Agent (`skills/meso-orchestrator.md`) during Phase 2 (EXECUTE). The MesoAgent routes research questions, and this skill handles the actual delegation to peer projects.
