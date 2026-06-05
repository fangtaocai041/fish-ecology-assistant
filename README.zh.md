<p align="center">
  🇬🇧 <a href="README.md">English</a>
</p>

<p align="center">
  <em>"人不能两次踏进同一条河流。"</em> — 赫拉克利特
</p>

<div align="center">
  <h1>🌊 万物皆变 · Panta Rhei</h1>
  <p><strong>把你的编码智能体变成拥有动态世界观的博士级研究团队。</strong></p>
  <p>16 MCP 工具 · 12 AI 子智能体 · 5 引擎搜索 · 13 个知识库</p>
</div>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square" alt="License"></a>
  <a href="#"><img src="https://img.shields.io/badge/万物皆变-core-6366f1?style=flat-square" alt="万物皆变"></a>
  <a href="#"><img src="https://img.shields.io/badge/MCP-16-22c55e?style=flat-square" alt="MCP:16"></a>
  <a href="#"><img src="https://img.shields.io/badge/智能体-12-f59e0b?style=flat-square" alt="智能体:12"></a>
</p>

---

## 🏛️ 核心哲学

> **世界是动态的，知识是暂时的，涌现是常态。**

这不是一句口号，而是贯穿整个项目每一行代码、每一次搜索、每一篇分析的**操作系统**。

科研的本质不是掌握知识——是**认识世界，提出问题，改造世界**。知识只是这条路上的脚印，不是终点。

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
| **知识僵化** | 手册写死不再更新 | 验证记录含"下次复查"日期，按活跃度动态计算 |

---

## 🤔 这个项目是什么

**Fish Ecology Assistant** 是一个将 [Reasonix Code](https://github.com/esengine/deepseek-reasonix) 从通用编码助手转变为**专业鱼类生态学研究团队**的完整配置包。

16 个 MCP 工具，12 个领域 AI 子智能体，5 引擎并行搜索，5 阶段研究流水线，R 统计计算环境——所有输出都遵循动态世界观。

| 能力 | 原生 | **加上本配置** |
|:-----|:----:|:--------------:|
| 搜索引擎 | 1 个 | **5 个** |
| MCP 服务 | 0 | **16 个** |
| AI 子智能体 | 4 个通用 | **12 个**（含涌现检测） |
| R 统计 | — | ✅ 20+ 生态学包 |
| 文献管理 | — | ✅ Zotero 直接查询 |
| 研究流水线 | — | ✅ 5 阶段 + 涌现检测 |
| 知识库 | — | ✅ 13 个 ima 知识库 |

<p align="right">(<a href="#readme-top">回到顶部</a>)</p>

---

## ⚡ 快速上手

```bash
git clone https://github.com/fangtaocai041/fish-ecology-assistant.git
cd fish-ecology-assistant
powershell -ExecutionPolicy Bypass -File .reasonix\setup-migrate.ps1
```

### 你说，它做

| 你说 | 它做什么 |
|:-----|:---------|
| `"研究长江禁渔对鱼类群落的影响——跑流水线"` | 5 阶段：规划→搜索→分析→写作→审查（中英双语，涌现检测） |
| `"验证手册 2.2 章"` | 自动查 CRAN 版本，概率陈旧评分，差分验证 |
| `"在 ima 知识库里搜一下同位素生态位"` | 自动路由，多库并行，信息增益关键词排序 |
| `"帮我做混合效应模型"` | R 代码 + 方法选择 + 诊断，标注验证版本 |

<p align="right">(<a href="#readme-top">回到顶部</a>)</p>

---

## 🧠 AI 子智能体

### 研究流水线（5 阶段自动编排 · 按需激活）

| # | 智能体 | 角色 | 动态世界观体现 |
|:-:|:-------|:-----|:--------------|
| ① | `research-planner` | 🧑‍💼 规划 | 中英双语关键词，覆盖国内外文献 |
| ② | `research-executor` | 🔍 搜索 | 5 引擎并行，标注文献发表年份 |
| ③ | `research-analyst` | 📊 分析 | **共识演变时间轴** + **涌现信号检测** |
| ④ | `research-writer` | ✍️ 写作 | **calibrated language**，时间锚定，不确定性标记 |
| ⑤ | `research-reviewer` | ✅ 审查 | 4 维评分，≤3 轮修订 |

### 领域专家

| 智能体 | 功能 | 哲学体现 |
|:-------|:-----|:---------|
| 📖 `paper-analyzer` | 深度论文分析 | 时间轴（发表时→至今→当前）+ 涌现信号 |
| 📊 `stats-assistant` | R 代码+方法选择 | 代码标注版本，方法标注验证日期 |
| 🔍 `stats-method-finder` | 搜索 CRAN/期刊 | 标记方法验证时间 |
| 🧠 `ima-smart-search` | 跨 13 个知识库搜索 | 动态发现 KB，信息增益路由 |
| ✅ `verify-stats-handbook` | 验证手册代码 | 自动查 CRAN，概率陈旧评分 |
| 🔭 `frontier-tracker` | 跟踪 15+ 前沿实验室 | 按时间排序最新发现 |
| 🎓 `phd-proposal-writer` | 博士 proposal | 参考文献动态覆盖 |

<p align="right">(<a href="#readme-top">回到顶部</a>)</p>

---

## 📡 MCP 服务（16 个工具）

| 服务 | 用途 |
|:-----|:------|
| `tavily` · `exa` · `scholar` · `article` · `scholarly` | 5 引擎并行搜索 |
| `ima` | 13 个知识库 + 笔记读写（14 个 ima 工具） |
| `rplay` · `coderunner` | R 统计 + 沙箱执行 |
| `echarts` · `ocr` · `ocr-fallback` · `playwright` | 图表、OCR、抓取 |
| `git` · `github` · `zotero` | 版本控制 + 文献库 |

<p align="right">(<a href="#readme-top">回到顶部</a>)</p>

---

## ⚡ 工程原则

哲学是灵魂，工程是肉身。DeepSeek 教我们：**能量有限，算法胜暴力**。

| 原则 | 做法 |
|:-----|:-----|
| **熵预算** | 博士课题 → 全管线。日常查询 → 单步搜索。不浪费计算 |
| **稀疏激活** | 规划器必跑。搜索器有词才跑。分析器有结果才跑。不空转 |
| **差分更新** | 只验证有变更的包，不做全量检查 |
| **信息增益** | P0 精确术语先搜，命中就停。P2 冗余词跳过 |

<p align="right">(<a href="#readme-top">回到顶部</a>)</p>

---

## 📁 项目结构

```
fish-ecology-assistant/
├── README.md · README.zh.md
├── .reasonix/
│   ├── mcp-servers/    ← 16 个 MCP 包装器
│   ├── skills/         ← 12 个 AI 子智能体
│   ├── handbooks/      ← 统计手册 + 学习手册
│   └── setup-migrate.ps1
└── research_output/
```

<p align="right">(<a href="#readme-top">回到顶部</a>)</p>

---

## 🌱

> 赫拉克利特说：人不能两次踏进同一条河流。
>
> 我们说：你也不能用上个月的代码分析今天的生态数据。
>
> 认识世界。提出问题。改造世界。
>
> 没有一个答案能走到最后——但每一个好问题都可以。

**万物皆流，无物常驻。太阳每天都是新的。**

<p align="right">— Heraclitus, ~500 BCE</p>

---

<sub>Built with Reasonix Code · Powered by DeepSeek · 2026</sub>
