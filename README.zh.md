<p align="center">
  🇬🇧 <a href="README.md">English</a>
</p>

<div align="center">
  <h1>🌊 Panta Rhei · 万物皆变</h1>
  <p><strong>把你的编码智能体变成拥有动态世界观和 DeepSeek 级工程效率的博士级研究团队。</strong></p>
  <p>16 MCP 工具 · 12 AI 子智能体 · 5 引擎搜索 · 13 个知识库</p>
</div>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square" alt="License"></a>
  <a href="#"><img src="https://img.shields.io/badge/万物皆变-核心-6366f1?style=flat-square" alt="万物皆变"></a>
  <a href="#"><img src="https://img.shields.io/badge/熵预算-高效-22c55e?style=flat-square" alt="熵预算"></a>
  <a href="#"><img src="https://img.shields.io/badge/MoE路由-稀疏-f59e0b?style=flat-square" alt="MoE路由"></a>
  <a href="USERGUIDE.md"><img src="https://img.shields.io/badge/文档-指南-0ea5e9?style=flat-square" alt="文档"></a>
</p>

---

## 🏛️ 哲学 + 工程

这个项目建立在两根支柱上：**动态世界观**（认知论）和 **稀疏计算**（方法论）。

### 🌊 万物皆变 — 世界是动态的

> 世界是动态的，知识是暂时的，涌现是常态。

每个输出标注时间锚点。每个声明使用校准语言。每次分析检测涌现信号。没有什么是永恒真理。

### ⚡ DeepSeek 工程思维 — 效率即智能

> 能量是有限的。计算有代价。聪明的算法胜过更大的模型。

不同于"堆参数"的暴力路线，本项目遵循 DeepSeek 的工程哲学：**混合专家路由（MoE）、稀疏激活、熵预算计算**。模块只在激活条件满足时才点火——从不计算不需要的东西。

| 风险 | 传统做法 | 我们的做法 |
|:-----|:----------|:----------|
| 知识陈旧 | 用旧代码跑新数据 | **概率陈旧评分** P(stale) = w·频率 + w·破坏性 + w·依赖度 |
| 过度自信 | "研究表明 X" | **校准语言**："Smith(2022)发现X，Jones(2024)补充Y" |
| 忽略信号 | 把异常当噪声 | **涌现检测**：≥3独立来源 → 主动追踪 |
| 浪费计算 | 每次全量跑管线 | **MoE 稀疏激活**：模块只在显式触发条件满足时才运行 |
| 文档僵化 | 手册从不更新 | **差分验证**：只检查有变更的包 |

<p align="right">(<a href="#readme-top">回到顶部</a>)</p>

---

## 🤔 这是什么

**Fish Ecology Assistant** 将 [Reasonix Code](https://github.com/esengine/deepseek-reasonix) 转变为鱼类生态学专业研究团队——16 工具、12 子智能体、5 引擎搜索、R 统计、13 个知识库。

| 能力 | 原生 Reasonix | **加上本配置** |
|:-----|:-------------:|:--------------:|
| 搜索引擎 | 1 个 | **5 个** (tavily, exa, scholar, article, scholarly) |
| MCP 服务 | 0 | **16 个** |
| AI 子智能体 | 4 个（通用） | **12 个**（涌现感知，校准语言） |
| R 统计 | — | ✅ R 4.6.0 + 20+ 生态学包 |
| 知识库 | — | ✅ 13 个 ima KB（动态发现，MoE 路由） |
| 验证 | — | ✅ 概率陈旧评分 + 差分验证 |
| 配置 | 手动 | ✅ 一个脚本，5 分钟 |

<p align="right">(<a href="#readme-top">回到顶部</a>)</p>

---

## ⚡ 快速上手

```bash
git clone https://github.com/fangtaocai041/fish-ecology-assistant.git
cd fish-ecology-assistant
powershell -ExecutionPolicy Bypass -File .reasonix\setup-migrate.ps1
```

### 你说，它做

| 你说 | 它做什么 | 熵预算 |
|:-----|:---------|:-------|
| `"研究长江禁渔——跑流水线"` | 5 阶段 + 涌现检测 + 中英双语搜索 | 全额 |
| `"验证手册 2.2 章"` | 自动查 CRAN，概率陈旧评分，差分验证 | 中等 |
| `"搜 ima 知识库：同位素生态位"` | IG 关键词路由，跨库去重，MoE 激活 | 轻量 |
| `"快速问题：NMDS stress 阈值？"` | 单阶段查询，无冗余计算 | 最小 |

<p align="right">(<a href="#readme-top">回到顶部</a>)</p>

---

## 🧠 AI 子智能体

### 研究管线 — 稀疏激活

| # | 智能体 | 激活条件 |
|:-:|:------|:---------|
| ① | `research-planner` | **始终**（轻量路由） |
| ② | `research-executor` | 规划器返回 ≥1 搜索词 |
| ③ | `research-analyst` | 执行器返回 ≥1 结果 |
| ④ | `research-writer` | 分析师返回 ≥1 发现 |
| ⑤ | `research-reviewer` | 写手输出 ≥500 字 |

### 领域专家

| 智能体 | 触发条件 |
|:------|:---------|
| 📖 `paper-analyzer` | 提供论文 DOI 或摘要 |
| 📊 `stats-assistant` | 涉及代码/方法/包 |
| 🔍 `stats-method-finder` | 请求不熟悉的方法 |
| 🧠 `ima-smart-search` | 领域匹配到 ≥1 个 ima KB |
| ✅ `verify-stats-handbook` | 明确请求验证手册章节 |
| 🔭 `frontier-tracker` | 明确请求跟踪实验室 |
| 🎓 `phd-proposal-writer` | 明确请求写 proposal |
| 📚 `zotero-assistant` | 涉及 Zotero 查询 |
| 📝 `obsidian-assistant` | 涉及 Obsidian 读写 |

<p align="right">(<a href="#readme-top">回到顶部</a>)</p>

---

## 📡 MCP 服务（16 个工具）

| 服务 | 引擎 | 用途 |
|:-----|:-----|:------|
| `tavily` / `exa` / `scholar` / `article` / `scholarly` | 多引擎搜索 | 5 源并行 |
| `ima` | ima OpenAPI | 13 KBs，IG 关键词路由，MoE 动态发现 |
| `rplay` | R 4.6.0 | 形态测量、同位素、群落生态 |
| `coderunner` | 沙箱 | 多语言执行 |
| `echarts` / `ocr` / `ocr-fallback` / `playwright` | 可视化 + 提取 | 图表、OCR、抓取 |
| `git` / `github` | 版本控制 | 仓库管理 |
| `zotero` | SQLite | 文献库查询 |

<p align="right">(<a href="#readme-top">回到顶部</a>)</p>

---

## 📁 项目结构

```
fish-ecology-assistant/
├── README.md · README.zh.md
├── .reasonix/
│   ├── mcp-servers/          ← 16 个 MCP 包装器
│   │   └── ima-server.mjs   ← 14 个工具（KB + MoE 发现 + IG 路由）
│   ├── skills/               ← 12 个 AI 子智能体
│   │   ├── karpathy-guard.md        ← 熵预算 + 万物皆变
│   │   ├── research-orchestrator.md ← 稀疏激活调度器
│   │   ├── verify-stats-handbook.md ← P(stale)评分 + 差分验证
│   │   ├── ima-smart-search.md      ← IG 关键词优化 + 去重
│   │   └── ... (8 more)
│   ├── handbooks/
│   │   ├── stats-methods.md   ← 版本追踪 R 模板
│   │   └── learning-guide.md  ← 学习路径
│   └── setup-migrate.ps1     ← 一键安装
└── research_output/
```

<p align="right">(<a href="#readme-top">回到顶部</a>)</p>

---

## 🌱 万物皆变 · DeepSeek 驱动

> 赫拉克利特：人不能两次踏进同一条河流。
> DeepSeek：聪明的算法胜过更大的模型。

**最后更新：2026-06-05**
**运行环境：Reasonix Code · DeepSeek 驱动**

<p align="right">(<a href="#readme-top">回到顶部</a>)</p>
