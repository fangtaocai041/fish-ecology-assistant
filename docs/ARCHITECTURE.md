# 🏗️ Fish Ecology Assistant — 标准智能体分层架构

> **标准智能体架构模型 (Standard Agent Architectural Model)**
> 基于认知科学、控制论与软件工程交叉领域的 5 层抽象，将双核哲学引擎（Panta Rhei + Systems Thinking）映射为可执行的工程结构。

---

## 目录

0. [双核哲学引擎](#0-双核哲学引擎)
1. [标准 5 层 Agent 架构总览](#1-标准-5-层-agent-架构总览)
2. [交互与感知层 (Interaction & Perception Layer)](#2-交互与感知层-interaction--perception-layer)
3. [认知与决策层 (Cognitive & Decision Layer)](#3-认知与决策层-cognitive--decision-layer)
4. [记忆系统层 (Memory System Layer)](#4-记忆系统层-memory-system-layer)
5. [逻辑映射与转换层 (Mapping & Translation Layer)](#5-逻辑映射与转换层-mapping--translation-layer)
6. [工具与执行层 (Tool & Execution Layer)](#6-工具与执行层-tool--execution-layer)
7. [闭环数据流控制论](#7-闭环数据流控制论)
8. [BDI 模型形式化](#8-bdi-模型形式化)
9. [MDP/POMDP 数学抽象](#9-mdppomdp-数学抽象)
10. [核心认知推理范式](#10-核心认知推理范式)
11. [多智能体协作理论 (MAS)](#11-多智能体协作理论-mas)
12. [五阶段研究流水线（现有映射）](#12-五阶段研究流水线现有映射)
13. [稀疏激活架构](#13-稀疏激活架构)
14. [置信度与涌现系统](#14-置信度与涌现系统)
15. [安全与治理](#15-安全与治理)

---

## 0. 双核哲学引擎

| 核 | 哲学 | 来源 | 核心原则 |
|:--:|------|------|---------|
| 🌍 | **Panta Rhei** | Heraclitus → 科学哲学 | 世界动态 · 知识暂态 · 涌现常态 |
| 🧠 | **Systems Thinking** | 毛泽东思想 | 矛盾分析 · 实践验证 · 阶段推进 · 集中兵力 |

**Panta Rhei 四原则：** 动态世界观 · 效率即智能 · 人机协作 · 可审计

**Systems Thinking 七原则：** 认识论循环 · 矛盾分析 · 阶段论 · 集中兵力 · 主动权 · 分类处理 · 系统平衡

> 双核哲学位于**元方法论层**，向下驱动标准 5 层架构的全部设计与运行时决策。

---

## 1. 标准 5 层 Agent 架构总览

```
┌──────────────────────────────────────────────────────────────┐
│                   元方法论层 (Meta-Methodology)                │
│    Panta Rhei (动态世界观) + Systems Thinking (系统论方法)      │
│    顶层约束：资源分配策略 · 矛盾优先级 · 阶段切换规则             │
└──────────────────────────────────────────────────────────────┘
         │ 驱动
         ▼
┌──────────────────────────────────────────────────────────────┐
│  ① 交互与感知层 (Interaction & Perception Layer)              │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐       │
│  │ NLU 解析  │ │ 多模态感知 │ │ 前端显示  │ │ 意图识别  │       │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘       │
├──────────────────────────────────────────────────────────────┤
│  ② 认知与决策层 (Cognitive & Decision Layer) — LLM 大脑      │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐       │
│  │ 任务分解  │ │ 推理规划  │ │ 自我反思  │ │ 策略生成  │       │
│  │ (CoT/ToT)│ │ (ReAct)  │ │(Reflexion)│ │ (Policy) │       │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘       │
├──────────────────────────────────────────────────────────────┤
│  ③ 记忆系统层 (Memory System Layer)                          │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐            │
│  │ 短期记忆     │ │ 长期记忆     │ │ 知识库 RAG  │            │
│  │ (Context Wd)│ │ (Vector DB) │ │ (IMA x13)  │            │
│  └─────────────┘ └─────────────┘ └─────────────┘            │
├──────────────────────────────────────────────────────────────┤
│  ④ 逻辑映射与转换层 (Mapping & Translation Layer)             │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐       │
│  │ 意图路由  │ │ 工程语言化 │ │ JSON 序列 │ │ 工具选择  │       │
│  │ (Routing) │ │(NL→Code) │ │ 化/SQL   │ │ (Tool Sel)│       │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘       │
├──────────────────────────────────────────────────────────────┤
│  ⑤ 工具与执行层 (Tool & Execution Layer)                      │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐       │
│  │ MCP 服务  │ │ R 沙盒    │ │ 外部 API │ │ 文件系统  │       │
│  │ (x21)    │ │ (vegan等) │ │(NCBI/GS)│ │ 读写     │       │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘       │
└──────────────────────────────────────────────────────────────┘
```

### 当前项目组件 → 架构层映射速查

| 架构层 | 对应组件 | 配置位置 |
|--------|---------|----------|
| ① 交互与感知 | Reasonix Chat 前端 / NLU 解析 / 自然语言输入输出 | Reasonix 引擎层 |
| ② 认知与决策 | Planner / Analyst / Reviewer / LLM (DeepSeek V3+R1) | `config/agent.yaml#pipeline` |
| ③ 记忆系统 | Reasonix Memory / Context Window / IMA 知识库 (x13) | `config/agent.yaml#architecture.layers.memory` |
| ④ 逻辑映射与转换 | Karpathy Guard / 工程语言化规则 / Skill Hub 路由 | `.reasonix/handbooks/engineering-grammar.md` |
| ⑤ 工具与执行 | 21 MCP 服务 + R 4.6.0 / 11 搜索引擎 (含4国内学术) / 文件 IO | `config/component_registry.yaml` |

---

## 2. 交互与感知层 (Interaction & Perception Layer)

**定义：** Agent 与外部世界（人类用户或其他系统）进行信息交换的接口。

**核心机制：**

| 机制 | 项目实现 | 说明 |
|------|---------|------|
| 多模态感知 | 文本输入（Reasonix Chat） | 未来可扩展语音/图像（OCR-Fallback） |
| NLU 解析 | Reasonix 内置 Prompt 解析 | 意图识别、实体提取、降噪 |
| 前端显示 | Reasonix Chat 渲染 + 图表工具 | ECharts 集成、Markdown 输出 |
| 输出包装 | Writer skill → 结构化报告 | 置信度标签、中英双语、可视化 |

**哲学映射（Panta Rhei I）：** 感知层捕获的动态观察 $O_t$ 是信念（Belief）更新的唯一入口。世界在变，每一次感知都是对前一次认知的修正。

---

## 3. 认知与决策层 (Cognitive & Decision Layer)

**定义：** 整个 Agent 的"大脑"，由大语言模型（LLM）充当，负责推理、规划和常识判断。这是 Systems Thinking 七原则的主要执行层。

**核心机制：**

| 机制 | 项目实现 | 哲学映射 |
|------|---------|----------|
| 任务分解 (Task Decom.) | Planner skill → 问题拆解 + 关键词生成 | 矛盾分析（抓主要矛盾） |
| 推理规划 (ReAct) | Orchestrator → Act-Observe-Think 循环 | 认识论循环（实践→认识） |
| 自我反思 (Reflexion) | Reviewer skill → 3 轮迭代修正 | 阶段论（防御→相持→反攻） |
| 策略生成 (Policy) | Analyst skill → 发现 + 涌现检测 | 集中兵力（资源聚焦） |
| 评估与决策 | Contradiction Analysis → 矛盾等级判定 | 分类处理（对抗/非对抗） |

**运行时推理流 (ReAct 范式)：**
```
思考 (Thought)    → "需要计算禁渔前后的 CPUE 变化"
行动 (Action)     → [search_literature("CPUE post fishing ban")]
观察 (Observation) → "返回 3 篇相关论文，其中 1 篇含定量数据"
再思考 (Re-Thinking) → "数据充足，进入 Analyst 阶段"
```

**认知层决策策略函数（形式化）：**
```
π(Aₜ | Oₜ, Mₜ) — 基于当前观察 Oₜ 和记忆 Mₜ，选择最优动作 Aₜ
```

---

## 4. 记忆系统层 (Memory System Layer)

**定义：** 为 Agent 提供上下文状态维持和历史经验调用的存储系统。

**核心机制：**

| 机制 | 项目实现 | 说明 |
|------|---------|------|
| 短期记忆 (STM) | LLM Context Window (8K tokens) | 当前对话轮次的即时状态 |
| 长期记忆 (LTM) | Reasonix Memory System | 跨会话的用户偏好、项目事实 |
| 知识库 RAG | IMA 知识库 (x13) + 向量检索 | 领域知识即时召回（余弦相似度） |
| 审计日志 | JSONL 格式持久化 | 每步推理的完整痕迹 |
| 知识暂态 | Panta Rhei 时间戳 | 每个记忆条目含创建/验证/过期时间 |

**记忆演化函数：**
```
Mₜ₊₁ = Φ(Mₜ, Oₜ, Aₜ)
```
当前记忆 $M_t$ 结合观测 $O_t$ 和动作 $A_t$，通过更新函数 $\Phi$ 演化为 $M_{t+1}$。

**哲学映射（Panta Rhei I）：** 知识是暂态的。记忆有时间戳，有版本生命周期。"遗忘"是控制信息熵增的主动策略。

---

## 5. 逻辑映射与转换层 (Mapping & Translation Layer)

**定义：** 跨越"语义空间"与"代码/系统空间"的桥梁 — 工程落地上最关键的一环。

**核心机制：**

| 机制 | 项目实现 | 说明 |
|------|---------|------|
| 意图路由 (Routing) | Skill Hub → 匹配到 subagent skill | Planner→Executor→Analyst→Writer→Reviewer |
| 工程语言化 | `engineering-grammar.md` 规则集 | 自然语言 → 精确函数签名/条件分支 |
| JSON/参数序列化 | MCP 协议格式化 | LLM 决策 → 标准 JSON-RPC 调用 |
| 工具选择 (Tool Sel.) | Orchestrator → 自适应选择工具 | 当前任务需要哪个 MCP/引擎 |
| 冲突分流 | Contradiction Analysis 映射 | 对抗性矛盾→阻塞/非对抗性→标注 |

**工程语言化规则示例（来自 `.reasonix/handbooks/engineering-grammar.md`）：**
```
❌ "搜索前先估算文献量"
→ ✅ estimated_volume = max(scholar_count(), graph_count(), author_productivity())

❌ "信任但验证"  
→ ✅ trust_score = 50 + 20×doi_ok + 15×search_ok + 10×reviews
      IF ≥ 80 THEN include
```

**哲学映射（Systems Thinking ⑦ 系统平衡）：** 逻辑映射层负责在"自然语言的模糊性"和"代码的精确性"之间维持平衡。任何未被工程语言化的语义碎片都会导致执行层失败。

---

## 6. 工具与执行层 (Tool & Execution Layer)

**定义：** Agent 干涉外部环境并获取客观真实数据的物理或虚拟环境。

**核心机制：**

| 机制 | 项目实现 | 数量 |
|------|---------|:----:|
| MCP 协议工具(国际) | scholar / article / scholarly / ncbi / tavily / exa / web_search | 7 个国际搜索 |
| 国内学术源(内置) | baidu_scholar / cnki / wanfang / cas (通过 web_search site: 策略) | 4 个国内学术引擎 |
| R 沙盒执行 | R 4.6.0 + vegan / SIBER / geomorph / glmmTMB | 4 个统计包 |
| 外部 API 调用 | NCBI E-utilities / Crossref / OpenAlex | 3 个学术 API |
| 文件系统 IO | research_output/ 读写 / scripts/ 执行 | 本地持久化 |
| OCR 工具 | OCR-Fallback (Tesseract) | 图像→文本 |
| 浏览器工具 | Playwright / Puppeteer | 网页交互 |
| 代码执行 | coderunner (沙盒) | 多语言代码运行 |

**哲学映射（Systems Thinking ① 认识论循环）：** 执行层是"实践检验"的场所。代码报错、API 返回空、统计检验不显著 — 这些反馈是下一轮认知迭代的起点。

---

## 7. 闭环数据流控制论

5 层架构之间的数据流不是单向瀑布，而是**闭环控制论反馈系统 (Cybernetic Feedback System)**，遵循 ReAct 范式：

```
                    ┌─────────────────────────┐
                    │  ⑤ 工具与执行层           │
                    │  (Search / Run / Fetch)  │
                    └──────────┬──────────────┘
                               │ 执行结果 / 报错
                               ▼
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│ ① 感知层  │───→│ ② 认知层  │───→│ ④ 映射层  │───→│ ⑤ 执行层  │
│ (输入)   │    │ (决策)   │    │ (转换)   │    │ (行动)   │
└──────────┘    └────┬─────┘    └──────────┘    └──────────┘
                     │                              │
                     │ ③ 记忆层                        │
                     │ (存储/召回)                     │
                     └────────────────────────────────┤
                                                      │ 反馈（错误/新观测）
                                                      ▼
                                              ① 感知层（重新输入）
```

### 项目中的实际闭环示例

```
用户："分析鳤的遗传多样性"
→ ① 感知层：NLU 解析 → 实体["鳤", "遗传多样性"]
→ ③ 记忆层：调取鳤的历史上下文、搜索配置
→ ② 认知层：Planner 任务分解 → "搜索文献 + 分析 + 写报告"
→ ④ 映射层：生成 scholar_search_literature_graph(query="Ochetobius elongatus")
→ ⑤ 执行层：调用 Scholar API → 返回 10 篇论文
→ [反馈] ② 认知层（Anlyst）：分类发现 → "遗传多样性偏低，经历瓶颈效应"
→ [反馈] ⑤ 执行层（检索更多）：ncbi_esearch → 交叉验证
→ ④ 映射层：写成 Markdown 报告
→ ① 感知层（输出）：渲染给用户
→ [反馈] ② 认知层（Reviewer）：质量评分 → 通过/回退
```

---

## 8. BDI 模型形式化

BDI (Belief-Desire-Intention) 是经典 AI 的认知架构，在此我们将其映射到 LLM Agent 系统中：

### Belief（信念）— Agent 对当前环境状态的认知

| BDI 概念 | 项目映射 | 数学表示 |
|----------|---------|----------|
| Belief | 上下文窗口 + 记忆召回 | $B_t = f(\text{Context}_t, \text{Memory}_t)$ |
| 信念更新 | 每次感知+执行后的状态刷新 | $B_{t+1} = B_t \cup \{O_t, A_t\}$ |
| 不确定性 | 置信度标签系统 | $P(belief) \in \{\text{✅验证}, \text{⚠️推断}, \text{❓假设}\}$ |

### Desire（愿望）— 系统的目标函数

| BDI 概念 | 项目映射 | 配置位置 |
|----------|---------|----------|
| Desire | System Prompt + 研究方向 | `config/agent.yaml` 全局目标 |
| 目标分解 | Strategic → Operational → Tactical | `phased_strategy.target_layers` |
| 目标优先级 | 主要矛盾 > 次要矛盾 > 边缘问题 | `contradiction_analysis.contradiction_levels` |

### Intention（意图）— 正在执行的计划

| BDI 概念 | 项目映射 | 说明 |
|----------|---------|------|
| Intention | 当前阶段的行动计划 | Planner 输出的子任务列表 |
| 意图切换 | 阶段门控 (phase_gating) | 不可跳跃、允许退却 |
| 意图放弃 | 矛盾转化检测 | ≥5 独立源指向新矛盾时重新规划 |

**BDI 闭环：**
```
Belief (当前状态) ──→ Desire (要达成的目标) ──→ Intention (行动计划)
     ↑                                                    │
     └──────────── 执行反馈更新信念 ────────────────────────┘
```

---

## 9. MDP/POMDP 数学抽象

Agent 与环境交互的每一时刻 $t$，系统状态可按**部分可观测马尔可夫决策过程 (POMDP)** 形式化：

### 形式化定义

| 符号 | 定义 | 项目映射 |
|:----:|------|---------|
| $S_t$ | 环境真实状态（不可完全观测） | 文献库的真实全貌 |
| $O_t$ | 部分观测 | 搜索引擎返回的 N 篇论文 |
| $A_t$ | 执行动作 | search / analyze / write / review |
| $M_t$ | 记忆状态 | 上下文 + 长期记忆 + 审计日志 |
| $\pi(A_t\|O_t, M_t)$ | 策略函数 | LLM 在给定上下文下选择动作的概率 |
| $R_t$ | 即时奖励 | 搜索结果质量 / 发现数量 / 验证通过 |
| $\gamma$ | 折扣因子 | 时间衰减（Panta Rhei — 知识暂态） |

### 策略优化目标

$$
\max_{\pi} \mathbb{E} \left[ \sum_{t=0}^{T} \gamma^t R_t \right]
$$

即：最大化**整个研究流水线**的累计"收益"（搜索命中数、分析质量、验证通过率）。

### 信念状态更新

$$
P(S_t | O_{1:t}, A_{1:t-1}) \propto P(O_t | S_t) \cdot \sum_{S_{t-1}} P(S_t | S_{t-1}, A_{t-1}) \cdot P(S_{t-1} | O_{1:t-1}, A_{1:t-2})
$$

> **实际意义：** Agent 永远无法确认"文献是否搜全了"。每一次搜索 $A_t$ 产生观测 $O_t$，更新对"文献空间"的信念分布。置信度系统（✅/⚠️/❓）就是这种信念概率的工程简化。

---

## 10. 核心认知推理范式

当前项目实现了多种推理范式的组合。以下是对照学术界前沿的分类：

### 10.1 ReAct (Reasoning + Acting) — ✅ 已实现

**核心思想：** 打破单纯的"思考"或"行动"，强制交替螺旋。

```
项目实现：Orchestrator 的 Act-Observe-Think 循环
映射：五阶段流水线中，每阶段内部的工作流
    Think → Act(搜索) → Observe(返回结果) → Think(分析) → ...
```

### 10.2 Tree of Thoughts (ToT) — ⚡ 部分实现

**核心思想：** 将决策树化为树状搜索，每步生成多个候选，允许回溯。

```
项目实现：
- Planner 阶段生成多个搜索策略分支
- 多引擎并行搜索 = 树状探索
- 矛盾转化检测 = 回溯触发条件
```

| ToT 要素 | 项目映射 |
|----------|---------|
| 候选生成 | 多关键词/多引擎并行 |
| 启发式评估 | 置信度系统 + 涌现检测 |
| 回溯 | `phase_gating.allow_retreat: true` |
| 搜索策略 | BFS（穷举模式）/ DFS（深度聚焦） |

### 10.3 Graph of Thoughts (GoT) — 🔜 可扩展

**核心思想：** 将线性树状结构拓展为有向无环图 (DAG)，允许推理分支的合并与协同。

```
扩展路径：
- Analyst 阶段的多个发现分支可合并
- Executor 阶段跨引擎结果可汇聚
- Reviewer 的多维度评分可融合
```

### 10.4 Reflexion（自我反思）— ✅ 已实现

**核心思想：** Agent 通过内部 Critic 模型评估自身轨迹，生成语言反馈作为下次迭代的上下文。

```
项目实现：
- Reviewer skill = Critic 模型
- 3 轮迭代 = 最大反思次数
- 执行层报错 → 反馈到认知层 → 重新生成
- 审计日志 = 完整轨迹记录
```

| Reflexion 要素 | 项目映射 |
|----------------|---------|
| Actor | Writer / Executor / Analyst |
| Critic | Reviewer (4 维度评分) |
| 语言反馈 | Review 评语 → 返回 Writer |
| 轨迹记忆 | JSONL 审计日志 |

### 10.5 推理模式选择策略

```
IF task 需要严格数理逻辑 (统计分析/模型拟合)
  THEN 启用 System 2 深度推理 (R1 model + Reflexion)
ELIF task 是探索性搜索 (文献调研/知识发现)
  THEN 启用 ReAct 螺旋 (V3 model + 多引擎并行)
ELIF task 需要多路径对比 (假设检验/矛盾分析)
  THEN 启用 ToT 风格搜索 (分歧路经生成 + 评估)
ELIF task 涉及多源融合 (综述/元分析)
  THEN 启用 GoT 风格合并 (分支汇聚 + 交叉验证)
```

---

## 11. 多智能体协作理论 (MAS)

当单体 Agent 的能力遇到瓶颈时，MAS 拓扑通过**群体智能**和**组织行为学**提升涌现能力。

### 11.1 项目中的 MAS 拓扑

```
                    ┌──────────────────────────────┐
                    │   Orchestrator (协调者)        │
                    │   任务分发 + 路由 + 冲突仲裁    │
                    └────┬──────┬──────┬───────────┘
                         │      │      │
              ┌──────────┘      │      └──────────┐
              ▼                 ▼                  ▼
        ┌──────────┐     ┌──────────┐     ┌──────────┐
        │ Planner   │     │ Executor  │     │ Analyst   │
        │ 研究规划  │     │ 文献搜索  │     │ 数据分析  │
        └──────────┘     └──────────┘     └──────────┘
              │                 │                  │
              └──────────┬─────┴──────┬───────────┘
                         ▼            ▼
                   ┌──────────┐ ┌──────────┐
                   │ Writer    │ │ Reviewer │
                   │ 报告撰写  │ │ 质量评审  │
                   └──────────┘ └──────────┘
```

### 11.2 静态工作流 (SOP-based MAS) — ✅ 已实现

**定义：** 借鉴软件工程理论，Agent 分配固定角色，信息按有向图流动。

```
项目映射：五阶段流水线
- Planner → Executor → Analyst → Writer → Reviewer
- 每个 Skill 是一个独立 Agent 角色
- 信息严格按照阶段顺序流动 (no_skip)
```

### 11.3 动态对抗与辩论 (Adversarial MAS) — ⚡ 部分实现

**定义：** 引入博弈论，设置目标相悖的 Agent，多轮对抗使输出收敛到更优解。

```
项目映射：
- Writer (生成) vs Reviewer (批判) = 最简辩论形式
- 3 轮最大迭代 = 有限对抗深度
```

### 11.4 跨项目 MAS — ✅ 已实现

```
项目映射：
- fish-ecology-assistant ↔ porpoise-agent 双向委托
- 协议：DELEGATE to {project}: skill={name} context={...}
- 导出技能：stats-assistant / research-analyst / phd-proposal-writer
- 导入技能：detect-clicks / estimate-abundance / assess-threats
```

### 11.5 MAS 拓扑形式化

将 MAS 建模为有向图 $G = (V, E)$：
- $V$ = Agent 节点集合 (Planner, Executor, Analyst, Writer, Reviewer, Orchestrator)
- $E$ = 通信边 (阶段间信息传递)

**信息熵控制目标：** 确保信息在多跳传递中熵增最小

$$
H(M_{t+1}) \leq H(M_t) + \epsilon
$$

> **实际意义：** Reviewer 的批判反馈不应引入比原始决策更多的噪声。Karpathy Guard 的"精准手术"原则即为此服务。

---

## 12. 五阶段研究流水线（现有映射）

> 以下为从 5 层视角重新审视的五阶段流水线

| 阶段 | 技能 | 主导架构层 | 激活条件 | 模型 |
|:----:|------|:----------:|:---------|:----:|
| 1 | `research-planner` | ② 认知层 | 始终 | V3 (廉價) |
| 2 | `research-executor` | ⑤ 执行层 + ④ 映射层 | Planner 输出查询 | V3 |
| 3 | `research-analyst` | ② 认知层 + ③ 记忆层 | ≥1 搜索结果 | R1 |
| 4 | `research-writer` | ① 感知层（输出端） | ≥1 分析发现 | V3 |
| 5 | `research-reviewer` | ② 认知层（反思） | ≥500 字草稿 | R1 |

### 迭代机制（Reflexion）

```
Reviewer (Critic) 判定:
  ✅ Pass → 输出最终报告
  🔄 Needs Revision → 返回 Writer（最多 3 轮）
  ❌ Fail → 呈现问题给用户
```

---

## 13. 稀疏激活架构

借鉴 DeepSeek MoE 路由 + 效率即智能 (Panta Rhei II)：

| 模块 | 主导层 | 激活条件 | 说明 |
|:-----|:------:|:---------|:-----|
| Planner | ② 认知 | 始终 | 轻量，先行 |
| Executor | ⑤ 执行 | ≥1 搜索查询 | 跳过纯理论问题 |
| Analyst | ② 认知 | ≥1 搜索结果 | 跳过无结果场景 |
| Writer | ① 感知 | ≥1 分析发现 | 跳过无发现场景 |
| Reviewer | ② 认知 | ≥500 字输出 | 跳过快速查询 |
| Stats verify | ⑤ 执行 | 涉及代码/方法 | 静默 |
| IMA search | ③ 记忆 | 领域匹配知识库 | 静默 |
| Emergence | ② 认知 | ≥3 独立来源 | 自动触发 |

---

## 14. 置信度与涌现系统

### 置信度系统（信念概率的工程简化）

| 标签 | 含义 | 对应信念概率 | 允许输出 |
|:-----|:-----|:------------:|:--------:|
| ✅ 已验证 | 多源一致可复现 | $P \geq 0.9$ | 是 |
| ⚠️ 待验证 | 逻辑推断未验证 | $0.5 \leq P < 0.9$ | 是（标注） |
| ❓ 假设 | 有理据但无直接证据 | $0.2 \leq P < 0.5$ | 仅讨论部分 |
| 🚫 无来源 | 不可溯源 | $P < 0.2$ | 禁止 |

### 涌现检测（多智能体协同的群体智能表现）

```
Input: Analyst 阶段的分类发现
Process: 聚合独立来源（不互相引用）
Threshold: ≥3 个独立来源指向同一非预期模式
Output: 涌现信号 → 标记置信度 → 写入报告
```

**涌现置信度：** 3 个独立源→低 · 4 个独立源→中 · 5+ 独立源→高

**哲学映射（Panta Rhei I — 涌现是常态）：** 涌现不是 bug，是 feature。当多个独立 Agent/引擎从不同角度指向同一模式时，系统识别到"整体大于部分之和"。

---

## 15. 安全与治理

| 机制 | 对应层 | 说明 |
|------|:------:|------|
| 人工审批关卡 | ②→① | 野外调查/保护建议/发表草稿 |
| Karpathy Guard | ④ 映射 | 反幻觉/反复杂化/精准手术/目标驱动 |
| 审计日志 (JSONL) | ③ 记忆 | 每事件可追踪 |
| 引用验证 | ②→⑤ | 每声明 ≥2 独立源 |
| API Key 保护 | ⚙️ 基础设施 | .gitignore 隔离敏感配置 |

---

## 附录：架构演进路线

### 已实现 (✅)
- [x] 标准 5 层架构（隐式） — 当前系统的自然形态
- [x] ReAct 推理范式 — Orchestrator 的 Act-Observe-Think 循环
- [x] Reflexion 自我反思 — Writer↔Reviewer 迭代
- [x] SOP-based MAS — 五阶段流水线角色分工
- [x] 跨项目 MAS — fish ↔ porpoise 双向委托
- [x] 工程语言化 — `engineering-grammar.md` 映射层

### 部分实现 (⚡)
- [ ] Tree of Thoughts — 多引擎并行（广度），但缺少启发式剪枝（深度）
- [ ] Adversarial MAS — Writer vs Reviewer（最简辩论），缺少多轮对抗博弈

### 可扩展 (🔜)
- [ ] Graph of Thoughts — 多分支汇合与协同
- [ ] 蒙特卡洛树搜索 (MCTS) — 长链条推理的自发探索
- [ ] 多 Agent 动态路由 — 非固定拓扑的自组织 MAS
- [ ] 隐式思维链 (Hidden CoT) — System 2 慢思考的工程实现

---

> 🧠 双核哲学引擎位置：位于 5 层架构之上，作为**元方法论层**，不参与具体计算，但约束所有层的运行时决策 — 什么矛盾优先、什么阶段跳过、什么资源集中。
>
> **标准架构保证通用性，双核哲学保证方向性。**
