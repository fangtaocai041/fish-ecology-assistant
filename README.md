# 🧠 Multi-Agent Research Assistant · 多智能体科研助手系统

**Bilingual | 中英对照**

> A complete scientific research assistant system powered by Reasonix Code + 16 MCP services + 12 specialized subagents (Skills), tailored for **aquatic ecology / conservation genetics / fisheries science**.
>
> 一个完整的科研助手系统，基于 Reasonix Code + 16 个 MCP 服务 + 12 个专业子智能体（Skills），专为**鱼类生态学 / 保护遗传学 / 渔业资源**方向定制。

---

## 📋 Architecture Overview · 架构总览

```
User · 用户提问
    │
    ▼
┌──────────────────────────────┐
│  🎯 Orchestrator · 主调度    │  ← You interact with this one
│  "AI Project Manager"        │    你面对的是这一个
│  12 skills · 16 MCP tools    │
└──┬──────┬──────┬──────┬─────┘
   │      │      │      │
   ▼      ▼      ▼      ▼
┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐
│🧑‍💼  │→│🔍   │→│📊   │→│✍️   │→ 🔄(≤3 rounds)
│Plan │ │Srch │ │Analy│ │Write│    最多3轮迭代
└─────┘ └─────┘ └─────┘ └──┬──┘
                           │
                     ┌─────▼─────┐
                     │  ✅ Review │
                     │ 审核通过/修改 │
                     └───────────┘
```

---

## 🎯 Quick Start · 快速开始

| 场景 · Scenario | 指令 · Command |
|----------------|---------------|
| 🔬 Full research · 完整研究 | `帮我研究一下 [主题]，运行完整流程` |
| 🎓 Write PhD proposal · 写博士计划 | `/skill phd-proposal-writer 研究方向：[主题]` |
| 📊 R statistical analysis · 统计建模 | `/skill stats-assistant 帮我做：[分析需求]` |
| 📖 Analyze a paper · 解析论文 | `/skill paper-analyzer 解析这篇：[DOI/摘要]` |
| 🔭 Frontier tracking · 前沿追踪 | `/skill frontier-tracker 看看 [团队名] 最近动态` |
| ✍️ Write a review · 写综述 | `/skill research-orchestrator 研究主题：[主题]` |

> 💡 **Try it**: Say "帮我研究一下长江十年禁渔对鱼类群落的影响，运行完整流程"

---

## 🧬 Skills · 智能体（12 个）

### Research Pipeline · 研究流水线（5 阶段自动编排）

| Role · 角色 | Name · 名称 | Type · 类型 | Input → Output · 输入→输出 |
|------------|------------|------------|---------------------------|
| 🧑‍💼 Planner · 规划 | `research-planner` | subagent | Question → Research Plan |
| 🔍 Researcher · 检索 | `research-executor` | subagent | Plan → Source Database |
| 📊 Analyst · 分析 | `research-analyst` | subagent | Sources → Analysis Report |
| ✍️ Writer · 写作 | `research-writer` | subagent | Report → Draft Document |
| ✅ Reviewer · 审核 | `research-reviewer` | subagent | Draft → Review Score |
| 🎯 Orchestrator · 编排 | `research-orchestrator` | inline | Schedules all 5 above |

### Domain Specialists · 领域专用

| Name · 名称 | Purpose · 用途 |
|------------|---------------|
| `frontier-tracker` | 🔭 Track top fish ecology labs globally · 追踪国际顶尖鱼类生态团队 |
| `paper-analyzer` | 📖 Deep paper dissection (methods / innovation / reproducibility) · 论文深度解析 |
| `phd-proposal-writer` | 🎓 Write PhD application proposals (Nanjing Agri U) · 博士研究计划书 |
| `stats-assistant` | 📊 R biostatistics (morphometrics / isotopes / genetics / community) · R 统计分析 |
| `stats-method-finder` | 🔍 Expand unfamiliar statistical methods · 不熟悉方法的检索扩充 |
| `zotero-assistant` | 📚 Query Zotero library via SQL · Zotero 文献库查询 |
| `obsidian-assistant` | 📝 Read/write Obsidian notes · Obsidian 知识库管理 |

---

## 📡 MCP Services · MCP 服务器（16 个）

### 🔍 Search & Academia · 搜索与学术

| Service · 服务 | Type · 类型 | Purpose · 用途 |
|---------------|------------|---------------|
| `tavily` | Deep search · 深度搜索 | AI-powered deep web search (15 results, advanced depth) |
| `exa` | Semantic search · 语义搜索 | Meaning-aware, not keyword matching |
| `scholar` | Academic · 学术 | Google Scholar search for papers |
| `article` | Article fetch · 论文抓取 | Full article metadata & abstract |
| `scholarly` | Scholarly research · 学术研究 | Multi-source scholarly search |

### 🖥️ System & Data · 系统与数据

| Service · 服务 | Type · 类型 | Purpose · 用途 |
|---------------|------------|---------------|
| `fs` | Filesystem · 文件系统 | Mounts Obsidian Vault & server files |
| `git` | Version control · 版本控制 | git operations |
| `github` | GitHub API | Repository/issue/PR access |
| `zotero` | Zotero · 文献库 | SQL query against Zotero database |

### 🧮 Compute & Visualization · 计算与可视化

| Service · 服务 | Type · 类型 | Purpose · 用途 |
|---------------|------------|---------------|
| `rplay` | R language · R 语言 | R 4.6.0 environment via uvx |
| `coderunner` | Code sandbox · 代码沙箱 | Isolated code execution (R/Python/JS etc.) |
| `echarts` | Charts · 图表 | ECharts data visualization |
| `thinking` | Chain-of-thought · 链式推理 | Sequential multi-step reasoning |

### 🖼️ Image & Browser · 图像与浏览器

| Service · 服务 | Type · 类型 | Purpose · 用途 |
|---------------|------------|---------------|
| `ocr` | PaddleOCR | Chinese OCR (tables, formulas, handwriting) |
| `ocr-fallback` | Tesseract.js | Offline OCR (no network needed) |
| `playwright` | Browser automation · 浏览器自动化 | Web scraping, screenshots, form fill |

---

## 🗂️ Project Structure · 项目结构

```
D:\Reasonix\data\                       ← Workspace · 工作目录
├── .gitignore                          ← Excludes secret key files · 排除含密钥文件
├── LICENSE                             ← MIT License
├── README.md                           ← This file · 本文档（中英对照）
├── GUIDE.md                            ← Full guide · 完整指南（中英对照）
├── CHEATSHEET.md                       ← Quick reference · 速查（中英对照）
│
├── .reasonix/
│   ├── mcp-servers/                    ← MCP wrapper scripts · 包装脚本
│   │   ├── tavily.bat / exa.bat        ← Search · 搜索（git-ignored）
│   │   ├── github.bat                  ← GitHub API（git-ignored）
│   │   ├── rplay.bat                   ← R 4.6.0
│   │   ├── paddleocr.bat               ← OCR Plan A
│   │   ├── ocr-fallback/               ← OCR Plan B (Tesseract.js)
│   │   ├── zotero.bat                  ← Zotero SQLite
│   │   └── README.md                   ← MCP server details · 服务详情
│   │
│   └── skills/                         ← 12 skill playbooks · 12 个技能
│       ├── research-planner.md
│       ├── research-executor.md
│       ├── research-analyst.md
│       ├── research-writer.md
│       ├── research-reviewer.md
│       ├── research-orchestrator.md
│       ├── frontier-tracker.md
│       ├── paper-analyzer.md
│       ├── phd-proposal-writer.md
│       ├── stats-assistant.md
│       ├── stats-method-finder.md
│       ├── zotero-assistant.md
│       └── obsidian-assistant.md
│
├── research_output/                    ← Research reports output
│
└── [external] C:\Users\小陶\.reasonix\
    └── config.json                     ← MCP registry + settings · MCP 注册表
```

---

## 💡 Design Principles · 设计理念

| Principle · 原则 | Implementation · 实现 |
|-----------------|----------------------|
| **Subagent isolation · 子智能体隔离** | Each subagent runs in its own context — they never share token space | 每个子智能体独立运行，不共享上下文 |
| **Prefix-cache aligned · 对齐缓存** | Stable prompt prefix → 90%+ cache hit on DeepSeek | 稳定前缀 → 长会话 90%+ 缓存命中 |
| **Graceful degradation · 优雅降级** | MCP fails → auto fallback chain | MCP 不可用时自动降级 |
| **Output budget · 输出约束** | Every skill has explicit token limits per stage | 每个 Skill 有明确的 token 上限 |
| **Self-healing · 自修复** | Built-in retry logic for transient failures | 内置重试与故障切换逻辑 |

---

## 📊 Comparison · 对比

| Feature · 特性 | Standard Reasonix | **Yours · 你的** |
|---------------|:-----------------:|:----------------:|
| MCP services · MCP 服务 | 0 (code only) | **16** |
| Subagent Skills · 子智能体 | 4 built-in | **12** |
| Search engines · 搜索引擎 | 1 (web_search) | **5** (tavily/exa/scholar/article/scholarly) |
| R environment · R 环境 | ✗ | ✅ R 4.6.0 via rplay |
| OCR · 图片识别 | ✗ | ✅ PaddleOCR + Tesseract.js |
| Zotero · 文献库 | ✗ | ✅ Direct SQL query |
| PhD proposal writer · 博士计划书 | ✗ | ✅ Customized for 南农/无锡渔业学院 |
| Domain expertise · 领域知识 | Generic | **鱼类生态 / 保护遗传 / 稳定同位素** |

---

## 🔒 Security · 安全

- API keys (TAVILY, EXA, GITHUB) are stored in **git-ignored** `.bat` files
- 3 个 API 密钥存储在 **git 排除** 的 `.bat` 文件中
- SSH key for GitHub push: `~/.ssh/id_ed25519`
- Zotero database: `D:\ZoteroData\zotero.sqlite`

---

## 📝 License · 许可证

MIT © 2026 蔡方陶 (Fangtao Cai)

Built with [Reasonix Code](https://github.com/esengine/deepseek-reasonix) · DeepSeek-native coding agent
