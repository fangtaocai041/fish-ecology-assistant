<p align="center">
  🇬🇧 <a href="README.md">English</a>
</p>

<div align="center">
  <h1>🌊 万物皆变 · Panta Rhei</h1>
  <p><strong>把你的编码智能体变成拥有动态世界观和DeepSeek级工程效率的博士级研究团队。</strong></p>
  <p>16 MCP 工具 · 12 AI 子智能体 · 5 引擎搜索 · 13 个知识库</p>
</div>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square" alt="License"></a>
  <a href="#"><img src="https://img.shields.io/badge/动态世界观-core-6366f1?style=flat-square" alt="动态世界观"></a>
  <a href="#"><img src="https://img.shields.io/badge/MCP-16-22c55e?style=flat-square" alt="MCP:16"></a>
  <a href="#"><img src="https://img.shields.io/badge/智能体-12-f59e0b?style=flat-square" alt="智能体:12"></a>
</p>

---

## 🏛️ 核心哲学

> **世界是动态的，知识是暂时的，涌现是常态。**

这不是一句口号，而是贯穿整个项目每一行代码、每一次搜索、每一篇分析的**操作系统**。

### 三大信条

**🌍 世界是动态的**
R 包在更新，物种分布在变化，科学共识在演变，气候变化在重塑生态系统。今天正确的结论半年后可能过时。我们**不把任何知识当作永恒真理**，而是放在时间轴上动态看待。

**📖 知识是暂时的**
科学精神的基石是证伪主义（Popper）。没有发现是终极真理，只有"当前最佳解释"。我们使用 **calibrated language**（校准语言）——说"证据表明"而不说"证明了"，说"Smith(2022)发现"而不说"研究表明"。每一个输出都标注时间锚点。

**⚡ 效率即智能**
能量是有限的。计算有代价。DeepSeek 教我们：聪明的算法胜过更大的模型。本项目遵循同一原则——熵预算分配计算资源，MoE 稀疏路由只激活需要的模块，差分验证只检查有变更的包。不求全，求准。

**🔬 涌现是常态**
生命、意识、生态系统、AI 推理能力——都是**涌现**的结果。单独分析局部拼凑不出整体。当 ≥3 个独立来源指向同一个非预期模式时，系统自动标记为**涌现信号**，而不是当成异常值忽略。

### 为什么这对科研至关重要

| 风险 | 传统做法 | 动态世界观的做法 |
|:-----|:---------|:----------------|
| **时效性差** | 用 2020 年的代码跑 2026 年的数据 | 包版本自动检查，标记"最后验证于 glmmTMB v1.1.10" |
| **过度自信** | "研究表明 X" | "Smith(2022)发现X，但Jones(2024)补充了Y" |
| **忽略新信号** | 把异常值当噪声 | ≥3个独立来源 → 涌现信号，主动追踪 |
| **知识僵化** | 手册写死不再更新 | 验证记录含"下次复查"日期，按包活跃度动态计算 |

---

## 🤔 这个项目是什么

**Fish Ecology Assistant** 是一个将 [Reasonix Code](https://github.com/esengine/deepseek-reasonix) 从通用编码助手转变为**专业鱼类生态学研究团队**的完整配置包。

它集成了 16 个 MCP 工具、12 个领域 AI 子智能体、5 引擎并行搜索、自动化的 5 阶段研究流水线，以及 R 统计计算环境——所有输出都遵循上述动态世界观。

| 能力 | 原生 Reasonix | **加上本配置** |
|:-----|:-------------:|:--------------:|
| 搜索引擎 | 1 个 | **5 个** (tavily, exa, scholar, article, scholarly) |
| MCP 服务 | 0 | **16 个** |
| AI 子智能体 | 4 个（通用） | **12 个**（领域专用，含涌现检测） |
| R 统计 | — | ✅ R 4.6.0 + 20+ 生态学包 |
| OCR 文字识别 | — | ✅ PaddleOCR + Tesseract.js |
| 文献管理器 | — | ✅ 直接查询 Zotero |
| 研究流水线 | — | ✅ 5 阶段 + 自动审查 + 涌现检测 |
| 知识库 | — | ✅ 连接 13 个 ima 知识库 |
| 新机器配置 | 手动 | ✅ 一个脚本，5 分钟 |

<p align="right">(<a href="#readme-top">回到顶部</a>)</p>

---

## ⚡ 快速上手

```bash
git clone https://github.com/fangtaocai041/fish-ecology-assistant.git
cd fish-ecology-assistant
powershell -ExecutionPolicy Bypass -File .reasonix\setup-migrate.ps1
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
| ② | `research-executor` | 🔍 搜索 | 5 引擎并行，标注文献发表年份 |
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

<p align="right">(<a href="#readme-top">回到顶部</a>)</p>

---

## 📡 MCP 服务（16 个工具）

| 服务 | 引擎 | 用途 |
|:-----|:-----|:------|
| `tavily` | AI 深度搜索 | 全网搜索 |
| `exa` | 语义搜索 | 按含义搜索 |
| `scholar` | Google Scholar | 学术论文 |
| `article` | 文献元数据 | 全文摘要 |
| `scholarly` | 多源聚合 | 跨库学术搜索 |
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
│   ├── mcp-servers/          ← 16 个 MCP 包装器
│   │   └── ima-server.mjs   ← 14 个工具（知识库+笔记+动态发现+多库搜索）
│   │
│   ├── skills/               ← 12 个 AI 子智能体
│   │   ├── ima-smart-search.md       ← 跨库智能搜索
│   │   ├── verify-stats-handbook.md  ← 自动 CRAN 版本检查
│   │   ├── paper-analyzer.md         ← 时间轴+涌现检测
│   │   ├── research-analyst.md       ← 共识演变+涌现信号
│   │   ├── research-writer.md        ← calibrated language
│   │   └── ...（其余 7 个技能）
│   │
│   ├── handbooks/
│   │   ├── stats-methods.md   ← 统计方法手册（含版本追踪+复查日期）
│   │   └── learning-guide.md  ← 学习路径手册
│   │
│   └── setup-migrate.ps1     ← 一键安装脚本
│
└── research_output/          ← 生成的研究报告
```

<p align="right">(<a href="#readme-top">回到顶部</a>)</p>

---

## 🌱 万物皆变 · Panta Rhei

> 赫拉克利特说：人不能两次踏进同一条河流。
>
> 

这个项目不是一套固定的工具集——它是一个**活的系统**。每个组件都内置了过期机制、版本追踪和涌现感知。随着你的研究深入、R 包更新、新方法涌现，它会和你一起进化。

**最后更新：2026-06-04**
**DeepSeek：聪明的算法胜过更大的模型。**

<p align="right">(<a href="#readme-top">回到顶部</a>)</p>
