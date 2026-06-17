![Python 3.10+](https://img.shields.io/badge/Python%203.10%2B-3776AB?style=flat-square)
  ![MIT](https://img.shields.io/badge/MIT-34D058?style=flat-square)
  ![v6.5.0](https://img.shields.io/badge/v6.5.0-8A4FCE?style=flat-square)
  ![430 species](https://img.shields.io/badge/430%20物种-007EC6?style=flat-square)
  ![289 traits](https://img.shields.io/badge/289%20性状-FE7D37?style=flat-square)
  ![21 MCP](https://img.shields.io/badge/21%20MCP-0EA5E9?style=flat-square)
  ![28 skills](https://img.shields.io/badge/28%20技能-D73A4A?style=flat-square)
  ![12 engines](https://img.shields.io/badge/12%20引擎-EC4899?style=flat-square)
  ![13 KBs](https://img.shields.io/badge/13%20知识库-F59E0B?style=flat-square)
  ![CN-EN](https://img.shields.io/badge/中英双语-6B7280?style=flat-square)
</p>

[English](README.md) · [中文](README.zh.md)

<div align="center"><h3>🌊 万物皆流。</h3></div>

世界是动态的，知识是暂时的，涌现是常态。

---

## 📖 目录

- [哲学](#-哲学)
- [快速开始](#-快速开始)
- [架构](#-架构)
- [功能特性](#-功能特性)
- [技能系统](#-技能系统)
- [MCP 工具](#-mcp-工具)
- [项目结构](#-项目结构)
- [版本历史](#-版本历史)
- [自我评估](#-自我评估)
- [生态体系](#-生态体系)

---

## 🎯 核心哲学

> 🌍 世界是动态的，📖 知识是暂时的，🌟 涌现是常态。

这不是一句口号，而是贯穿整个项目每一行代码、每一次搜索、每一篇分析的操作系统。

### 📜 三大信条

**🌍 世界是动态的** — R 包在更新，物种分布在变化，科学共识在演变，气候变化在重塑生态系统。今天正确的结论半年后可能过时。我们不把任何知识当作永恒真理，而是放在时间轴上动态看待。

**📖 知识是暂时的** — 科学精神的基石是证伪主义（Popper）。没有发现是终极真理，只有"当前最佳解释"。我们使用校准语言——说"证据表明"而不说"证明了"，说"Smith(2022) 发现"而不说"研究表明"。每一个输出都标注时间锚点。

**🌟 涌现是常态** — 生命、意识、生态系统、AI 推理能力——都是涌现的结果。单独分析局部拼凑不出整体。当 ≥3 个独立来源指向同一个非预期模式时，系统自动标记为涌现信号，而不是当成异常值忽略。

### ⚖️ 为什么这对科研至关重要

| 🎯 场景 | ❌ 传统做法 | ✅ 动态世界观的做法 |
|:---------|:------------|:------------------|
| 📦 包版本 | 跑 2020 年的代码，不管版本差 | 包版本自动检查，标注"最后验证于 glmmTMB v1.1.10" |
| 📝 引用 | "研究表明确实如此" | "Smith(2022) 发现 X，但 Jones(2024) 补充了 Y" |
| 📊 异常值 | 忽略，当噪声 | ≥3 个独立来源 → 涌现信号，主动追踪 |
| ⏰ 知识过期 | 手册写死，不再更新 | 验证记录含"下次复查日期"，按包活跃度动态计算 |
| 🔧 方法选择 | 固定方法用到死 | 方法动态选择，置信度动态计算 |

> 道生一，一生二，二生三，三生万物。

---

## 🧩 这个项目是什么

**Fish Ecology Assistant** 是一个将 Reasonix Code 从通用编码助手转变为专业鱼类生态学研究团队的完整配置包。它是三生万物 S-T-V-P₁-P₂ 五体架构中的**知识供给核心（S/V0）**，由 **eon-core** 统一协调。

它集成了 **21 个 MCP 工具**、**28 个领域技能**、**12 引擎并行搜索**、自动化的 **5 阶段研究流水线**、**13 个 IMA 知识库**，以及 **R 统计计算环境**——所有输出都遵循上述动态世界观。

### 📊 能力清单

| 🚀 能力 | ✨ 加上本配置 | 💭 原生 Reasonix |
|:---------|:-------------|:-----------------|
| 🔍 搜索 | 12 引擎 (tavily, exa, scholar, article, scholarly, baidu_scholar, cnki, wanfang, cas, ncbi, ima, deepwiki) | 1 个 (web_search) |
| 🤖 AI 技能 | 28 个（6 流水线 + 20 领域 + 2 守卫）| 4 个（通用）|
| 📊 R 统计 | R 4.6.0 + 20+ 生态学包 | — |
| 👁️ OCR | PaddleOCR + Tesseract.js 离线备选 | — |
| 📚 文献 | Zotero SQLite 直接查询 | — |
| ✍️ 写作 | 5 阶段 + 自动审查 + 涌现检测 | — |
| 🏛️ 知识库 | 连接 13 个 IMA 知识库 | — |
| ⚡ 装机 | 一个脚本，5 分钟 | — |

---

## 🚀 快速开始

```bash
git clone git@github.com:fangtaocai041/fish-ecology-assistant.git
cd fish-ecology-assistant
pip install -e .
python src/main.py search --species "刀鲚"
```

---

## 🏗️ 架构

### S-T-V-P₁-P₂ 五体架构

```
S-T-V-P₁-P₂ (三生万物)
  │
  ├── S/V0  fish-ecology-assistant    ← 知识供给（本项目）
  │         Panta Rhei + 系统论世界观
  │         430 物种、289 性状、KB-First 搜索
  │
  ├── T     （未来：理论引擎）
  │
  ├── V/V1  cognitive-search-engine   → 搜索验证
  │         12 引擎、validator.py、evolution_executor
  │
  ├── Coord  eon-core                  → 协调内核
  │         EventBus、DAG 路由、CAS 核心
  │
  ├── P₁    porpoise-agent            → 江豚专研（衍生）
  └── P₂    coilia-agent              → 刀鲚专研（衍生）
```

### 五层内部架构

```
fish-ecology-assistant/
  src/           核心 Python 引擎
  ├── adapter.py            IProjectAdapter 标准接口 + score() 方法
  ├── orchestrator.py       KB-First 物种搜索协调器
  ├── project_hub.py        跨项目协调中枢（eon-core 桥接）
  ├── dao_engine.py         哲学链执行引擎（Panta Rhei → 道）
  ├── types.py              8 个 dataclass + 4 个枚举
  └── kalman_emergence.py   卡尔曼滤波涌现检测
  fishkb/         独立可复用鱼类知识库核心（pip install fishkb）
  ├── fishkb/db.py           KnowledgeDB — SQLite FTS5 知识库
  ├── fishkb/search.py       FishSpeciesMatcher — KB-First 物种匹配
  ├── fishkb/credibility.py  论文可信度评分
  └── fishkb/types.py        核心数据类型
  config/
  ├── agent.yaml             智能体编排配置
  ├── mcp_servers.yaml       21 个 MCP 服务器定义
  ├── coordination.yaml      跨项目协调配置
  ├── evolution.yaml         自进化参数
  ├── component_registry.yaml 活系统组件注册表
  ├── knowledge_base/        30 种 .md 物种档案
  └── fish_species_kb.yaml   430 种索引
  data/
  ├── species.db             SQLite（物种+性状+文献）
  ├── FISHMORPH.csv          2.3MB 全球形态数据库
  └── reports/               HTML/CSV 导出
  scripts/
  ├── fishbase_pull.py       FishBase API 自动同步
  ├── trait_network.py       网络科学性状分析
  └── gen_report.py          双语 HTML 报告生成器
```

### 研究流水线（5 阶段）

```
规划 → 执行 → 分析 → 撰写 → 评审
  ↑                          │
  └────── 反馈循环 ──────────┘
```

所有阶段由 **eon-core** 通过 `project_hub.py` 和 `coordination.yaml` 协调。

---

## ✨ 功能特性

| 功能 | 状态 | 说明 |
|------|:--:|------|
| 🗃️ 430 物种库 | ✅ | 长江鱼类 + 双语保护等级 |
| 📏 289 形态性状 | ✅ | FISHMORPH(251) + FishBase + FAO + 手动 |
| 🌊 种群级数据 | ✅ | 26条含水域标注 |
| 🔬 性状目录 | ✅ | 61项性状分7大类 |
| 🏛️ 保护等级 | ✅ | IUCN + 中国红皮书 + 国家重点 + CITES |
| 📊 Excel/HTML | ✅ | 双语报告，双层表头 |
| 🔗 KB-First 搜索 | ✅ | SQLite FTS5，30种核心零网络 |
| 🕸️ 性状网络 | ✅ | Jaccard共现，关键性状识别 |
| 📡 卡尔曼滤波 | ✅ | 噪声数据涌现检测 |
| 🔄 自进化 | ✅ | 7 触发器参数自适应 |
| 📦 fishkb 子库 | ✅ | 独立 pip 可安装核心（KnowledgeDB + Matcher） |
| 🎯 score() 适配器 | ✅ | IProjectAdapter.score() 跨项目质量评分 |
| 🔄 FishBase同步 | 🟡 | 脚本就绪，SSL环境限制 |
| 🧪 活系统 | ✅ | 组件注册表含过期策略 |

---

## 🎯 技能系统

### 流水线技能（6 个）

| 技能 | 说明 |
|------|------|
| `research-orchestrator` | 顶层流水线协调 |
| `research-planner` | 研究问题分解 + 策略制定 |
| `research-executor` | 多引擎并行文献搜索 |
| `research-analyst` | 统计分析 + 数据解读 |
| `research-writer` | 双语报告生成 |
| `research-reviewer` | 质量审查 + 矛盾检测 |

### 领域技能（20 个）

| 技能 | 说明 |
|------|------|
| `academic-species-search` | 多源物种学术搜索 |
| `cognitive-species-search` | 认知图谱物种搜索 |
| `unified-species-search` | 全引擎统一物种搜索 |
| `fuzzy-species-search` | 模糊名称匹配 + OCR 变体 |
| `google-scholar-search` | Google Scholar 定向搜索 |
| `lit-search` | 综合文献搜索 |
| `frontier-tracker` | 研究前沿追踪 |
| `paper-analyzer` | 深度论文分析 |
| `stats-assistant` | R 统计计算助手 |
| `stats-method-finder` | 统计方法推荐 |
| `verify-stats-handbook` | 手册与当前统计方法验证 |
| `phd-proposal-writer` | 博士开题报告撰写 |
| `ima-smart-search` | IMA 知识库智能搜索 |
| `zotero-assistant` | Zotero 文献管理 |
| `obsidian-assistant` | Obsidian 知识库集成 |
| `component-health-check` | 活系统健康监测 |
| `living-system-dashboard` | 实时系统状态面板 |
| `debate-validator` | 多视角辩论验证 |
| `self-evolve` | 自主参数进化 |
| `rule-auditor` | 研究规则合规审计 |

### 守卫技能（2 个）

| 技能 | 说明 |
|------|------|
| `karpathy-guard` | 代码质量 + 安全守卫 |
| `rule-auditor` | 跨项目规则合规检查 |

---

## 🔌 MCP 工具（21 个）

| 类别 | 工具 | 说明 |
|------|------|------|
| **搜索** | `cognitive_search` | 认知图谱搜索引擎（主入口） |
| | `scholar` | Google Scholar 文献搜索 |
| | `article` | PMC 全文 + 期刊质量（EasyScholar/OpenAlex） |
| | `scholarly` | 多源学术跨库搜索 |
| | `baidu_scholar` | 百度学术中文搜索 |
| | `cnki` | 中国知网中文期刊 |
| | `wanfang` | 万方中文学术数据库 |
| | `cas` | 中科院文献服务 |
| | `ncbi` | NCBI PubMed + Europe PMC |
| | `tavily` | AI 深度网络搜索 |
| | `exa` | 语义网络搜索 |
| | `ima` | IMA 知识库搜索 |
| **计算** | `rplay` | R 4.6.0 统计计算 |
| | `coderunner` | 多语言代码沙盒 |
| | `echarts` | 出版级图表生成 |
| **图像** | `ocr` | PaddleOCR（中英文表格+公式） |
| | `ocr_fallback` | Tesseract.js 离线 OCR |
| | `playwright` | 浏览器自动化 + 抓取 |
| **数据** | `git` | Git 版本控制 |
| | `github` | GitHub API（仓库、议题、PR） |
| **知识** | `zotero` | Zotero SQLite 直接查询 |
| | `obsidian` | Obsidian 知识库读写 |

---

## 📁 项目结构

```
fish-ecology-assistant/
  （见上方架构图）
```

---

## 📜 版本历史

| 版本 | 日期 | 重要更新 |
|------|------|----------|
| **v6.5.0** | 2026-06-17 | KB-First 搜索策略，21 MCP 集成，活系统组件注册表 |
| v6.4.0 | 2026-06-12 | ProjectHub 跨项目协调，eon-core 桥接 |
| v6.3.0 | 2026-06-09 | 自进化引擎（7 触发器），evolution.yaml |
| v6.2.0 | 2026-06-07 | 跨项目进化传播，component_registry.yaml |
| v6.1.0 | 2026-06-06 | 28 技能（6 流水线 + 20 领域 + 2 守卫），rule-auditor |
| v6.0.0 | 2026-06-05 | S-T-V-P₁-P₂ 五体架构，coordination.yaml |
| v5.0.0 | 2026-06-01 | 5 阶段流水线，fishkb 子库，430 物种 |

---

## 🪞 自我评估

### 优势
- **物种覆盖**：430 种长江鱼类及双语保护等级——最全面的开源数据集
- **KB-First 架构**：SQLite FTS5 实现 30 种核心物种零网络查询
- **活系统**：每个组件都有出生日期、最后验证和过期策略
- **跨项目协调**：eon-core EventBus + DAG 路由支持 6 项目生态
- **涌现感知**：卡尔曼滤波从噪声数据检测模式；≥3 来源标记涌现

### 当前局限
- FishBase 同步因 SSL 环境限制暂不可用（脚本已就绪）
- 部分小众中文期刊元数据不完整
- R 包版本漂移监控依赖 CRAN 可用性
- 深度物种遗传分析需专家人工审核

### 路线图
- [ ] SSL 问题解决后恢复 FishBase 自动同步
- [ ] 扩展至 500+ 物种，覆盖湄公河流域
- [ ] 实时种群监测仪表板
- [ ] 深度学习图像形态性状提取

---

## 🔗 生态体系

本项目是「三生万物」生态的 **知识供给核心（S/V0）**。

```
S-T-V-P₁-P₂ 架构（由 eon-core 协调）：

  S/V0  📦 fish-ecology-assistant    → 知识供给
  V/V1  🔍 cognitive-search-engine   → 搜索验证
  Coord ⚙️ eon-core                  → 协调内核

  衍生项目：
    P₁  🐬 porpoise-agent    → 江豚领域专家
    P₂  🐟 coilia-agent      → 刀鲚领域专家
    P₃  🐟 culter-agent      → 鲌类领域专家
    C   🔥 conflict-arbiter  → 冲突仲裁
```

> 🔥 和则无穷力量，分则顶尖专家引擎。

---

🌱 **万物皆变 · Panta Rhei**

> 赫拉克利特说：人不能两次踏进同一条河流。
>
> 我们说：你也不能用上个月的代码分析今天的生态数据。

这个项目不是一套固定的工具集——它是一个**活的系统**。每个组件都内置了过期机制、版本追踪和涌现感知。随着你的研究深入、R包更新、新方法涌现，它会和你一起进化。

*最后更新：2026-06-20　|　适用环境：Reasonix Code · DeepSeek 驱动*
