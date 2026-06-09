<p align="center">
  🇬🇧 <a href="README.md">English</a>
</p>

<div align="center">
  <h1>🌊 万物皆变 · Panta Rhei</h1>
  <p><strong>把你的编码智能体变成拥有标准 5 层 Agent 架构 + 双核哲学引擎（Panta Rhei + 系统论）的博士级研究团队。</strong></p>
  <p>21 个 MCP 服务 · 28 个 AI Skills · 12 引擎搜索 · 13 个知识库 · 18 工程规则 · BDI + ReAct/ToT + MAS · Docker</p>
</div>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square" alt="License"></a>
  <a href="#"><img src="https://img.shields.io/badge/双核哲学-Panta_Rhei_%2B_系统论-6366f1?style=flat-square" alt="双核哲学"></a>
  <a href="#"><img src="https://img.shields.io/badge/MCP-21-22c55e?style=flat-square" alt="MCP:21"></a>
  <a href="#"><img src="https://img.shields.io/badge/skills-28-f59e0b?style=flat-square" alt="Skills:27"></a>
  <a href="docs/ARCHITECTURE.md"><img src="https://img.shields.io/badge/架构-5_层-8b5cf6?style=flat-square" alt="架构:5层"></a>
  <a href="#"><img src="https://img.shields.io/badge/规则-18-8b5cf6?style=flat-square" alt="规则:18"></a>
  <a href="config/agent.yaml"><img src="https://img.shields.io/badge/agent-v2.0.0-ec4899?style=flat-square" alt="Agent:v2.0.0"></a>
</p>

---

## 🧠 由 eon-core 智能协调

> S 层 (V0) 由 [eon-core](https://github.com/fangtaocai041/eon-core) (10层统一内核) 智能协调：**混沌增强路由** · **学者级统计停止** (Rule of Three) · **DeepSeek 级 MoE 门控** · **六道轮回业力引擎**。
> 多流域鱼类物种知识库 (`config/fish_species_kb.yaml`) — 大陆→国家→流域分层。长江 443种 + 持续扩充图们江/绥芬河/黑龙江流域。

## 🔺 S-T-V-P₁-P₂ 架构角色: **State (S / V0)**

> S-T-V-P₁-P₂ 生态系统，由 [eon-core](https://github.com/fangtaocai041/eon-core) 统一协调。
> 提供知识、长江 443 种鱼类数据、矛盾分析和生态发现。
> **D₂ 面**: 多 Agent 辩论网格。**三角验证**: ≥3 独立源。

### 🔗 关联项目 (S-T-V-P₁-P₂ 生态系统)

| 项目 | 角色 | 技术栈 | 说明 |
|------|:----:|--------|------|
| **eon-core** | **协调器** | Python · 10层内核 | EventBus · 六道轮回 · DAG路由 · 四顶点拓扑 |
| **cognitive-search-engine** | **V / V1** (Validation) | Python · BDI+ReAct | 权威可信度评分 · Hub-and-Spoke 搜索 · 共享知识图谱 |
| **porpoise-agent** | **P₁ / V2** (Porpoise) | Python · orchestrator | 5 阶段管线 · 声学分析 · 野外调查 · 保护评估 |
| **coilia-agent** | **P₂ / V3** (Coilia) | Python · 3 skills | 刀鲚专研 · 耳石微化学 · 洄游生态 |

> **协同进化**: Fish (S/V0) 提供知识 → Cognitive (V/V1) 验证 → Porpoise (P₁/V2) + Coilia (P₂/V3) 执行领域管线。
> 知识图谱进化 → 五项目共享。引擎更新通过 submodule → 自动传播。
> 完整规范: workspace 根目录 `coordination.yaml`。

### 🧠 eon-core 统一内核 (Workspace Level)

> **10层同心架构** — OriginKernel → YinYang → 5 Vertices (V0-V4) → 8 Trigrams → Tetrahedron → Samsara → Sphere → Tendrils → Evolution。
> 由 [eon-core](https://github.com/fangtaocai041/eon-core) 统一协调。替代已删除的 meso-cosmos-agent (v7.1)。
> 详见 `eon-core/config/taiji.yaml`。

```
理解 → 路由 → 执行 → 验证 → 合成 → 进化
(Macro) (Meso) (Micro) (Cross) (Merge) (Feedback)
```

## 🔧 工程架构规范 · 职责边界与运行验证

### 项目职责 (工程语言)

f项目 (fish-ecology-assistant) — 知识库
  lookup_species(name) 精确匹配 (学名/中文名)
  fish_species_kb.yaml: 443种长江鱼类分类/分布/保护等级
  taxonomy_log: 科属变更记录含时间·期刊·作者证据

c项目 (cognitive-search-engine) — 搜索引掣
  search_species(name) → CoordinatedSearchResult
  管线: 分类学检查 → 模式路由 → 多引擎搜索 → 合并 → 学科分类
  OCR变体 + 同义词扩展 + 附带论文判定
  分类检测: detect_taxonomy_discrepancy() 自动比较两 yaml

conflict-arbiter — 冲突仲裁
  中国保护等级为权威 (chinese_red_list=100, provincial=90)
  IUCN/CITES 仅参考, 冲突仍报告但不影响裁决
  声明仲裁先检查时空一致性, 不同时空不构成冲突

porpoise-agent — 保护评估 (长江旗舰种)
coilia-agent — 洄游评估 (刀鲚等洄游鱼类)
用户: "搜鳤的文献"
  │
  ├── Step 1: lookup_species("鳤")        → f项目知识库 (精确匹配)
  ├── Step 2: 输出物种画像 (含taxonomy_log变更记录)
  ├── Step 3: ask_choice 是否继续?
  │     ├── A) 全管线: run_fish_pipeline()
  │     ├── B) 仅文献: search_species()
  │     └── C) 仅知识库
  │
  ├── WHILE 全管线:
  │     Phase 1: f项目 lookup (独立运行)
  │     Phase 2: c项目 search + detect_taxonomy_discrepancy
  │     Phase 3: conflict-arbiter (region="china")
  │     Phase 4: porpoise/coilia (仅旗舰种)
  │     Phase 5: 汇总
  │
  └── 用户选择 C → 直接返回, 不调任何外部搜索
```

### 运行验证

```bash
# 运行验证脚本 (从 fish-ecology-assistant 目录)
python scripts/verify_architecture.py
```

```python
# 或直接导入库验证:
from workspace import lookup_species
from unified_search import detect_taxonomy_discrepancy
from arbiter import ConflictArbiter

# f项目: taxonomy_log 含 subgroup/evidence
sd = lookup_species('鳤')['species_data']
assert sd['family'] == 'Xenocyprididae (鲴科)'
tax = sd['taxonomy_log'][0]
assert tax['field'] == 'family' and tax['subgroup'] and tax['related_genera']

# c项目: 分类学一致性
assert detect_taxonomy_discrepancy('Ochetobius elongatus') is None

# conflict-arbiter: 中国优先
ca = ConflictArbiter()
r = ca.detect_conflicts('鳤', sources=[
    {'source':'iucn','iucn':'CR'},
    {'source':'chinese_red_list','protection_level':'国家二级'},
], region='china')
assert r['consensus']['authority'] == 'chinese_classification'
```

> 完整文档见 [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)
> **5 层架构**：交互感知 → 认知决策 → 记忆系统 → 映射转换 → 工具执行
> **理论根基**：BDI 模型 · MDP/POMDP 形式化 · ReAct/ToT/GoT 推理 · Reflexion 自我修正 · MAS 多智能体拓扑

## 🧠 核心哲学

> 🧠 **双核哲学引擎**：Panta Rhei（动态世界观）+ 系统论（矛盾·实践·阶段·集中）
> 世界观回答"世界是什么样的"，方法论回答"我们怎样行动"。
> **全部哲学语言已映射为可执行代码** — 参见 [工程语法](.reasonix/handbooks/engineering-grammar.md)：每条原则有精确的 `WHEN→THEN` 规则、config 路径和 Skill 触发器。
> `.reasonix/handbooks/systems-thinking.md`（哲学） + `.reasonix/handbooks/engineering-grammar.md`（代码映射）

---

### 🌍 Panta Rhei · 动态世界观

> **世界是动态的，知识是暂时的，涌现是常态。**

这不是一句口号，而是贯穿整个项目每一行代码、每一次搜索、每一篇分析的**操作系统**。

### 三大信条

**🌍 世界是动态的**
R 包在更新，物种分布在变化，科学共识在演变，气候变化在重塑生态系统。今天正确的结论半年后可能过时。我们**不把任何知识当作永恒真理**，而是放在时间轴上动态看待。

**📖 知识是暂时的**
科学精神的基石是证伪主义（Popper）。没有发现是终极真理，只有"当前最佳解释"。我们使用 **calibrated language**（校准语言）——说"证据表明"而不说"证明了"，说"Smith(2022)发现"而不说"研究表明"。每一个输出都标注时间锚点。

**🔬 涌现是常态**
生命、意识、生态系统、AI 推理能力——都是**涌现**的结果。单独分析局部拼凑不出整体。当 ≥3 个独立来源指向同一个非预期模式时，系统自动标记为**涌现信号**，而不是当成异常值忽略。

### 为什么这对科研至关重要

| 风险 | 传统做法 | 动态世界观的做法 |
|:-----|:---------|:----------------|
| **时效性差** | 用 2020 年的代码跑 2026 年的数据 | 包版本自动检查，标记"最后验证于 glmmTMB v1.1.10" |
| **过度自信** | "研究表明 X" | "Smith(2022)发现X，但Jones(2024)补充了Y" |
| **忽略新信号** | 把异常值当噪声 | ≥3个独立来源 → 涌现信号，主动追踪 |
| **知识僵化** | 手册写死不再更新 | 验证记录含"下次复查"日期，按包活跃度动态计算 |

<p align=right>(<a href=#readme-top>回到顶部</a>)</p>


### 🧠 系统论 · 七大工程原则
七大原则工程语法化，已映射成为执行代码层

| # | 原则 | 源著作 | 工程映射 |
|---|------|--------|---------|
| ① | 认识论循环 | 《实践论》 | 实践→认识→再实践→再认识 = 验证闭环 |
| ② | 矛盾分析 | 《矛盾论》 | 抓主要矛盾 → 资源聚焦 2.5x |
| ③ | 阶段论 | 《论持久战》 | 战略防御→相持→反攻 = 五阶段流水线 |
| ④ | 集中兵力 | 军事思想 | 主要矛盾方向 60% 计算资源 |
| ⑤ | 主动权 | 《论持久战》 | 前沿追踪主动建议 + "你打你的，我打我的" |
| ⑥ | 分类处理 | 《正确处理矛盾》 | 对抗性/非对抗性矛盾分流策略 |
| ⑦ | 系统平衡 | 《论十大关系》 | 十大研究平衡 + 多目标优化 |

<p align=right>(<a href=#readme-top>回到顶部</a>)</p>

---

## 🐋 DeepSeek 效率原则（效率即智能）

> **已映射到代码**: [工程语法 §8](.reasonix/handbooks/engineering-grammar.md) — DS-1..DS-4 含形式化定义、WHEN→THEN 规则和 config 路径。

能量是有限的。计算有代价。DeepSeek 不堆参数，堆算法。

| ID | 原则 | 代码映射 |
|:---|------|---------|
| **DS-1** | **熵预算** — 计算资源按问题重要性分配。博士课题→全管线，日常查询→单步搜索。 | `pipeline.stages[].activation` + `research-orchestrator` |
| **DS-2** | **稀疏激活** — MoE 路由：每个 Skill 仅在条件满足时激活。每请求 ~2-4/12 活跃。 | `pipeline.stages[].activation` + `karpathy-guard` |
| **DS-3** | **差分验证** — P(stale) 概率评分仅检查变更包，非全量。复查周期 = f(更新频率, 风险, 依赖)。 | `verify-stats-handbook` skill |
| **DS-4** | **信息增益路由** — P0 精确术语优先 → 命中即停。P2 冗余词跳过。跨库去重。 | `ima-smart-search` skill |

---

## 🤔 这个项目是什么

**Fish Ecology Assistant** 是一个将 [Reasonix Code](https://github.com/esengine/deepseek-reasonix) 从通用编码助手转变为**专业鱼类生态学研究团队**的完整配置包。

它基于**标准 5 层 Agent 架构模型**（交互感知 → 认知决策 → 记忆系统 → 映射转换 → 工具执行），集成了 21 个 MCP 服务、25 个 AI Skills（6 流水线 + 17 领域 + 2 守护）、11 引擎并行搜索、13 个知识库、BDI 推理 + ReAct/ToT/MAS 多智能体拓扑、18 条工程规则，以及 R 统计计算环境——所有输出都遵循上述双核哲学。

| 能力 | 原生 Reasonix | **加上本配置** |
|:-----|:-------------:|:--------------:|
| 搜索引擎 | 1 个 | **12 个** (cognitive_search + scholar, article, scholarly, baidu_scholar, cnki, wanfang, cas, ncbi, tavily, exa, web_search) |
| MCP 服务 | 0 | **21 个**（含 cognitive_search DirectLoader + DeepWiki） |
| AI Skills | 4 个（通用） | **28 个**（6 流水线 + 20 领域 + 2 守护，涌现检测） |
| R 统计 | — | ✅ R 4.6.0 + 20+ 生态学包 |
| OCR 文字识别 | — | ✅ PaddleOCR + Tesseract.js |
| 文献管理器 | — | ✅ 直接查询 Zotero |
| 研究流水线 | — | ✅ 5 阶段 + 自动审查 + 涌现检测 |
| 知识库 | — | ✅ 连接 13 个 ima 知识库 |
| 新机器配置 | 手动 | ✅ 一个脚本 或 `docker compose up` |
| CI/CD | — | ✅ GitHub Actions 自动验证 |
| 工程规则 | — | ✅ 18 条 WHEN→THEN 含代码映射 |
| 跨项目 | — | ✅ fish↔porpoise 互委托协议 |

<p align="right">(<a href="#readme-top">回到顶部</a>)</p>

---

## ⚡ 快速上手

```bash
git clone https://github.com/fangtaocai041/fish-ecology-assistant.git
cd fish-ecology-assistant
powershell -ExecutionPolicy Bypass -File .reasonix\setup-migrate.ps1
```

或使用 Docker：
```bash
docker compose up
```

重启 Reasonix，全部就绪。

### 你说，它做

| 你说 | 它做什么 |
|:-----|:---------|
| `"研究长江禁渔对鱼类群落的影响——跑流水线"` | 5 阶段：规划→搜索→分析→写作→审查（中英双语搜索，自动标记涌现信号） |
| `"验证手册 2.2 章"` | 自动查 CRAN 包版本，比对手册，计算复查日期 |
| `"在 ima 知识库里搜一下同位素生态位"` | 自动路由到正确知识库，多库并行搜索，合成结果 |
| `"帮我做混合效应模型"` | R 代码 + 方法选择 + 诊断，标注"截至 YYYY-MM 的推荐做法" |

<p align="right">(<a href="#readme-top">回到顶部</a>)</p>

---

## 🧠 AI 子智能体

### 研究流水线（5 阶段自动编排）

| # | 智能体 | 角色 | 动态世界观体现 |
|:-:|:-------|:-----|:--------------|
| 🎯 | `research-orchestrator` | **调度器** | 调度全部 5 阶段 |
| ① | `research-planner` | 🧑‍💼 规划 | 中英双语关键词，覆盖国内外文献 |
| ② | `research-executor` | 🔍 搜索 | 11 引擎并行（GS 优先 + 4 国内源），标注文献发表年份 |
| ③ | `research-analyst` | 📊 分析 | **共识演变时间轴** + **涌现信号检测** |
| ④ | `research-writer` | ✍️ 写作 | **calibrated language**，时间锚定，不确定性标记 |
| ⑤ | `research-reviewer` | ✅ 审查 | 4 维评分，≤3 轮修订 |

### 领域专家

| 智能体 | 功能 | 哲学体现 |
|:-------|:-----|:---------|
| 📖 `paper-analyzer` | 深度分析论文 | **时间轴**（发表时→至今→当前）+ **涌现信号** |
| 📊 `stats-assistant` | R 代码+方法选择 | 代码标注版本，方法标注验证日期 |
| 🔍 `stats-method-finder` | 搜索 CRAN/期刊 | 标记方法的"最后验证时间" |
| 🧠 `ima-smart-search` | 跨知识库智能搜索 | 动态发现 KB，不过期不硬编码 |
| ✅ `verify-stats-handbook` | 验证手册代码 | 自动查 CRAN 版本，按活跃度算复查周期 |
| 🔭 `frontier-tracker` | 跟踪前沿实验室 | 按时间排序最新发现 |
| 🎓 `phd-proposal-writer` | 博士 proposal | 参考文献动态覆盖，标注时效性 |
| 📚 `zotero-assistant` | 查 Zotero 文献库 | — |
| 📝 `obsidian-assistant` | 读写 Obsidian | — |
| 🛡️ `karpathy-guard` | 行为准则守护 | 熵预算 + 稀疏激活，MoE 路由 |
| 🔍 `rule-auditor` | 规则合规审计 | 扫描全部 Skills 的 18 规则覆盖 |

<p align="right">(<a href="#readme-top">回到顶部</a>)</p>

---

## 📡 MCP 服务（21 个工具）

| 服务 | 引擎 | 用途 |
|:-----|:-----|:------|
| `scholar` | **Google Scholar** | **优先搜索引擎** · 学术论文 |
| `article` | 文献元数据 | 全文摘要 |
| `scholarly` | 多源聚合 | 跨库学术搜索 |
| `baidu_scholar` | 百度学术 | 中文论文 |
| `cnki` | 知网 CNKI | 中文核心期刊 |
| `wanfang` | 万方数据 | 中文学位论文 |
| `cas` | 中科院 IHBCAS | 水生所/动物所出版物 |
| `ncbi` | PubMed | 生物医学文献 |
| `tavily` | AI 深度搜索 | 全网搜索 |
| `exa` | 语义搜索 | 按含义搜索 |
| `ima` | ima OpenAPI | **13 个知识库 + 笔记（14 个工具）** |
| `rplay` | R 4.6.0 | 形态测量、同位素、群落生态 |
| `coderunner` | 沙箱 | 多语言代码执行 |
| `echarts` | ECharts | 图表可视化 |
| `ocr` | PaddleOCR | 中英文 OCR |
| `ocr-fallback` | Tesseract.js | 离线 OCR |
| `playwright` | Chromium | 网页抓取 |
| `git` | Git CLI | 版本控制 |
| `github` | GitHub API | 仓库管理 |
| `zotero` | SQLite | Zotero 查询 |

<p align="right">(<a href="#readme-top">回到顶部</a>)</p>

---

## 📁 项目结构

```
fish-ecology-assistant/
├── README.md                 ← English
├── README.zh.md              ← 中文
│
├── .reasonix/
│   ├── mcp-servers/             ← 21 个 MCP 服务（含 deepwiki）
│   │   └── ima-server.mjs      ← 14 个工具
│   │
│   ├── skills/                  ← 25 个 AI Skill 剧本
│   │   ├── (6 流水线)   research-orchestrator/planner/executor/analyst/writer/reviewer
│   │   ├── (4 物种搜索)  academic/cognitive/fuzzy/unified-species-search
│   │   ├── (3 研究)     frontier-tracker / paper-analyzer / phd-proposal-writer
│   │   ├── (3 工具)     ima-smart-search / zotero-assistant / obsidian-assistant
│   │   ├── (3 统计)     stats-assistant / stats-method-finder / verify-stats-handbook
│   │   ├── (2 守护)     karpathy-guard / rule-auditor
│   │   ├── (2 系统)     component-health-check / living-system-dashboard
│   │   ├── (1 搜索)     google-scholar-search
│   │   ├── (1 辩论)     debate-validator
│   │   └── (1 架构)     explore (内置)
│   │
│   ├── handbooks/
│   │   ├── systems-thinking.md        ← 7 大系统原则
│   │   ├── engineering-grammar.md     ← 18 条 WHEN→THEN
│   │   ├── activation-matrix.md       ← 组件协调
│   │   ├── ADVANTAGES.md              ← 前沿对比
│   │   ├── WEAKNESSES.md              ← 缺口分析
│   │   ├── IMPROVEMENT_PLAN.md        ← 改进路线图
│   │   ├── CROSS_PROJECT_PROTOCOL.md  ← 跨智能体委托
│   │   ├── DEEPWIKI_INTEGRATION.md    ← DeepWiki 集成
│   │   ├── README_UPDATE_RULE.md      ← README 同步协议
│   │   ├── stats-methods.md           ← 统计方法手册
│   │   └── learning-guide.md          ← 学习路径
│   │
│   ├── .github/workflows/validate.yml ← CI/CD 自动验证
│   ├── Dockerfile                     ← Docker 部署
│   └── setup-migrate.ps1              ← 一键安装
│
└── research_output/          ← 生成的研究报告
```

<p align="right">(<a href="#readme-top">回到顶部</a>)</p>

---

---

## 🤝 人机权责边界

> 执行归我。最终决策归你。

（1）AI执行：搜索、分析、生成、标记涌现、建议修订等。

（2）人执行：判断真伪、选择方法、决定方向、承担发表责任等。

工具可以无限进化。但**学术责任与研究品味，永远无法被算法外包。**
这个系统是一个放大器，不是一个作者。

## 🌱 万物皆变 · Panta Rhei

> 赫拉克利特说：人不能两次踏进同一条河流。
>
> 我们说：
> 知识会老去，但人类对世界的追问永不落幕。
> 昨日之真理为今日之基石，今日之未知为明日之征途。
> 我们的目光，从不囿于已知的疆界；
> 我们的脚步，终将踏上那片星光璀璨的浩瀚征途。

这个项目不是一套固定的工具集——它是一个**活的系统**。每个组件都内置了过期机制、版本追踪和涌现感知。随着你的研究深入、R 包更新、新方法涌现，它会和你一起进化。

**最后更新：2026-06-07**
**运行于 Reasonix Code · 由 DeepSeek 驱动**

---

## 📋 README 变更记录

> 版本副本保存在 `.reasonix/readme-versions/`

| 版本 | 日期 | 主题 | 变更内容 |
|:------|:-----|:------|:-------------|
| **v6.1** | 2026-06-07 | 跨项目协同进化 | + agent.version 徽标 (v2.0.0), + S-T-V 三角角色增强, + 三项目协同进化描述, + coordination.yaml 统一协调 |
| **v6** | 2026-06-07 | 认知搜索引擎 | + DirectLoader 协议 (importlib 零进程加载), 双模式搜索 (ParallelSearch 轻量 / CognitiveAgent 完整 BDI ReAct), 知识图谱进化, 三项目共享引擎 |
| **v5** | 2026-06-06 | 搜索 v3.0 | 11 搜索引擎 (GS优先 + 知网/万方/百度学术/中科院), google-scholar-search 技能, 鳤文献全面检索 |\n| **v4** | 2026-06-06 | 系统论 | + 双核哲学（Panta Rhei + 毛泽东思想系统论），7 大系统原则 + 4 DeepSeek 效率原则，工程语法 (18 条 WHEN→THEN)，全量代码映射 |
| **v3** | 2026-06-05 | 工程化 | 全面重写：Panta Rhei 哲学，能力对比，工程效率原则，稀疏激活 |
| **v2** | 2026-06-05 | Panta Rhei | 动态世界观整合，涌现检测，校准语言 |
| **v1** | 2026-06-05 | 原始版本 | 初始发布 — 鱼类生态学助手，5 引擎 + 12 子智能体 |

---

## 📊 自我评价

| 维度 | 评分 | 说明 |
|------|:--:|------|
| 📚 知识广度 | ⭐⭐⭐⭐⭐ | 12 搜索引擎 + 13 知识库 + 长江 443 种鱼类数据库 + 28 AI Skills |
| 🧘 哲学集成 | ⭐⭐⭐⭐⭐ | Panta Rhei + 系统论 — 18 条 WHEN→THEN 工程规则 |
| 🔬 研究管线 | ⭐⭐⭐⭐⭐ | 5 阶段：规划→搜索→分析→撰写→评审，28 AI Skills |
| 🌏 中文文献 | ⭐⭐⭐⭐⭐ | 知网/万方/百度学术/中科院 — 弥补西方数据库系统性盲区 |
| 🔗 生态角色 | ⭐⭐⭐⭐⭐ | S-T-V-P₁-P₂ 中 S/V0 层，由 eon-core 统一调度 |
| 🧪 测试覆盖 | ⭐⭐⭐⭐☆ | 跨项目验证 + 规则合规检查 |

> **核心优势**: 通用鱼类生态研究平台。双核哲学（Panta Rhei + 系统论）不是装饰性引用，而是运行时约束 — 矛盾分析决定搜索策略，阶段论决定停止条件。

## 📜 许可证

MIT License © 2026 fangtaocai041

<p align=right>(<a href=#readme-top>回到顶部</a>)</p>
