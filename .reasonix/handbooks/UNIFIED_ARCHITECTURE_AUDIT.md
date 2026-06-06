# 🔗 Unified Architecture Audit — 求同存异优化

> **方针**: 周恩来 "求同存异" → Engineering translation: **Interface Segregation + Shared Contract + Adapter Pattern**
> **求同 (Seek Common Ground)**: Extract shared protocols, unified interfaces, consistent rule IDs
> **存异 (Reserve Differences)**: Allow project-specific implementations via adapters

---

## 1. 审计结果：两个 agent.yaml 对比

### 1.1 求同 (Common Ground — identical or should be identical)

| Config Section | fish | porpoise | Status |
|---------------|------|----------|:------:|
| `contradiction_analysis.*` | ✅ | ✅ | 🟢 完全一致 |
| `verification_loop.*` | ✅ | ✅ | 🟢 完全一致 |
| `phased_strategy.*` | ✅ | ✅ | 🟢 完全一致 |
| `research_balance.*` | ✅ | ✅ | 🟢 完全一致 |
| `orchestrator.max_steps` | 100 | 100 | 🟢 一致 |
| `orchestrator.max_revision_rounds` | 3 | 3 | 🟢 一致 |
| `orchestrator.human_in_loop` | true | true | 🟢 一致 |
| 18 规则 ID (FB-1..DS-4) | ✅ | ✅ | 🟢 一致 |

### 1.2 存异 (Reserved Differences — domain-specific, acceptable)

| Config Section | fish | porpoise | Status |
|---------------|------|----------|:------:|
| `agent.version` | 1.0.0 | 0.1.0 | 🔴 需对齐 |
| `agents.*` structure | ecology/stats/genetics | acoustic/ecology/field | 🟡 领域差异 (存异) |
| `skills.*` structure | pipeline+domain+guard | flat list | 🟡 架构差异 (存异) |
| `skills.skill_dir` | .reasonix/skills | src/skills | 🟡 路径差异 (存异) |
| `memory.type` | reasonix | chromadb | 🟡 平台差异 (存异) |
| `pipeline.stages` | explicit 5-stage | implicit in orchestrator | 🟡 实现差异 (存异) |
| `knowledge_bases` vs `knowledge_graph` | ima KBs | Neo4j | 🟡 领域差异 (存异) |

### 1.3 求同存异边界

```
┌─────────────────────────────────────────────────┐
│              求同 (Common Ground)                 │
│  contradiction_analysis / verification_loop      │
│  phased_strategy / research_balance              │
│  18 规则 ID / PREFLIGHT 协议 / 激活矩阵          │
│  Cross-delegation protocol                      │
├──────────────────────┬──────────────────────────┤
│   存异 (fish)         │   存异 (porpoise)         │
│   Skills: 14 (md)     │   Skills: 16 (md+py)     │
│   Pipeline: explicit  │   Pipeline: orchestrator  │
│   Memory: reasonix    │   Memory: chromadb       │
│   KB: ima (13 bases)  │   KB: Neo4j + file       │
│   Agents: ecology     │   Agents: acoustic        │
└──────────────────────┴──────────────────────────┘
```

---

## 2. 冲突修复

### 2.1 🔴 agent.version 对齐

```
fish:    1.0.0
porpoise: 0.1.0
→ 统一为 1.0.0 (两个项目共同演进)
```

### 2.2 🔴 添加 shared_config 显式标记

在 agent.yaml 顶部新增 `shared` 节，标记求同部分：

```yaml
shared:
  version: "1.0.0"
  rule_framework: "FB-1..DS-4 (18 rules)"
  philosophy: "dual-core (Panta Rhei + Systems Thinking)"
  config_schema_version: "1.0.0"
```

### 2.3 🟡 添加 cross_delegation 配置节

```yaml
cross_delegation:
  enabled: true
  peer_project: "porpoise-agent"  # or "fish-ecology-assistant"
  peer_skills:
    - { skill: "detect-clicks", domain: "acoustic", direction: "import" }
    - { skill: "stats-assistant", domain: "statistics", direction: "export" }
```

### 2.4 🟡 Version 对齐

```
porpoise agent.version: "0.1.0" → "1.0.0"
```

---

## 3. 协调优化: 激活矩阵统一

### 3.1 问题
两个项目有各自的激活矩阵 (ACTIVATION_MATRIX.md)，但协调规则分散。

### 3.2 求同存异方案

**求同**: 统一的激活阶段定义
```
Stage 0: PREFLIGHT (config read)          — both projects
Stage 1: Contradiction Analysis (CP-1)     — both projects
Stage 2: Domain Execution                  — project-specific (存异)
Stage 3: Verification (FB-1, FB-2)         — both projects
Stage 4: Review + Adapt (MO-1, DS-1..4)    — both projects
```

**存异**: Stage 2 的实现
```
fish:     research-planner → executor → analyst → writer
porpoise: _understand_question → _run_literature_review → _run_data_analysis → ...
```

### 3.3 统一激活协议

```
WHEN either project receives a question:
  1. PREFLIGHT: read config (求同 — identical protocol)
  2. CP-1: analyze contradiction (求同 — identical rule)
  3. SM-1: determine phase (存异 — project-specific routing)
  4. Execute domain logic (存异 — project-specific Skills)
  5. FB-1: tag verification (求同 — identical rule)
  6. MO-1: check balance (求同 — identical rule)
  7. DS-1..4: apply efficiency (求同 — identical rules)
```

---

## 4. 并行/串行协调优化

### 4.1 当前问题
- fish 的 executor 阶段 5 引擎并行，但没有明确的并行上限
- porpoise 的 phases 串行，未利用并行机会
- 两个项目之间无协调——各自独立运行

### 4.2 优化

**并行规则 (求同)**:
```
PARALLEL_ALLOWED:
  - search engines (5 engines ‖)
  - KB searches (13 KBs ‖)
  - domain Skills (independent Skills ‖)
  - fish + porpoise (cross-project delegation ‖)

SERIAL_REQUIRED:
  - pipeline stages (sequential gated)
  - PRIMARY tasks (¬parallel, WF-1)
  - human-gated phases (FIELD_SURVEY, CONSERVATION)
```

**串联规则 (求同)**:
```
Stage N → Stage N+1: gate check (SM-1 no_skip)
Stage N → Stage N-1: dead_end detected (SM-2 retreat)
```

---

## 5. 联合检索优化

### 5.1 当前问题
- fish 的 executor 搜索 5 引擎
- porpoise 的 literature review 搜索不同引擎
- 两个项目的搜索结果不共享

### 5.2 优化: 统一搜索接口

```
search(engines: [...], query: str, domain: str) → SourceDatabase

fish:    search(["tavily","exa","scholar","article","scholarly"], Q, "fish_ecology")
porpoise: search(["scholar","article","tavily","exa"], Q, "porpoise_research")
cross:   search(["tavily","scholar","article"], Q, "cross_domain")
```

**求同**: 搜索接口签名一致
**存异**: 引擎选择按领域不同

---

## 6. 最终优化: 统一协调配置

### 新增: `config/coordination.yaml` (两个项目共用)

```yaml
# 求同存异协调配置 — 两个项目共享

coordination:
  version: "1.0.0"
  
  # 求同: 共享协议
  shared_protocols:
    preflight: "read config/agent.yaml before all Skills"
    rule_ids: ["FB-1","FB-2","CP-1","CP-2","SM-1","SM-2","WF-1","WF-2","PT-1","PT-2","EH-1","EH-2","MO-1","MO-2","DS-1","DS-2","DS-3","DS-4"]
    verification: { min_sources: 2, max_iterations: 3 }
    contradiction: { budget_multiplier: 2.5, transformation_threshold: 5 }
  
  # 存异: 项目特定
  project_specific:
    fish:
      skill_dir: ".reasonix/skills"
      pipeline_type: "explicit_stages"
      memory: "reasonix"
    porpoise:
      skill_dir: "src/skills"
      pipeline_type: "orchestrator"
      memory: "chromadb"
  
  # 桥接: 跨项目委托
  cross_delegation:
    enabled: true
    protocol: "DELEGATE to {project}: skill={name} context={...}"
    
  # 并行策略
  parallelism:
    search_engines: { max_concurrent: 5, strategy: "fan_out" }
    kb_search: { max_concurrent: 13, strategy: "fan_out" }
    domain_skills: { max_concurrent: 3, strategy: "independent" }
    cross_project: { max_concurrent: 2, strategy: "fan_out" }
  
  # 串联策略  
  serialism:
    pipeline_stages: { gate: "no_skip", retreat: "allow" }
    primary_tasks: { strategy: "sequential", reason: "WF-1: 各个歼灭" }
    human_gates: { strategy: "blocking", phases: ["field_survey", "conservation"] }
```

---

## 7. 实施清单

| # | 修复 | 文件 | 影响 |
|:--|------|------|:--:|
| 1 | agent.version 对齐 → 1.0.0 | porpoise agent.yaml | 🟢 |
| 2 | 添加 `shared` 节 | 两个 agent.yaml | 🟢 |
| 3 | 添加 `cross_delegation` 节 | 两个 agent.yaml | 🟡 |
| 4 | 创建 `coordination.yaml` | 两个 config/ | 🟡 |
| 5 | 更新 cross-project 引用 | CROSS_PROJECT_PROTOCOL.md | 🟢 |

---

> **求同存异工程化**: 共享协议 = Interface (求同), 项目实现 = Adapter (存异)
> 18 条规则是契约, agent.yaml 是接口规范, Skills/orchestrator 是实现

**Last updated: 2026-06-06**
