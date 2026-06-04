<p align=center>
  🇬🇧 <a href=README.md>English</a>
</p>

<div align=center>
  <h1>🧠 Reasonix 研究助手</h1>
  <p><strong>把你的编码智能体变成博士级研究团队。</strong></p>
  <p>16 个 MCP 工具 · 12 个 AI 子智能体 · 5 引擎搜索 · 一键迁移</p>
</div>

<p align=center>
  <a href=LICENSE><img src=https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square alt=License></a>
  <a href=#><img src=https://img.shields.io/badge/Reasonix_Code-6366f1?style=flat-square alt=Reasonix></a>
  <a href=#><img src=https://img.shields.io/badge/MCP-16-22c55e?style=flat-square alt=MCP:16></a>
  <a href=#><img src=https://img.shields.io/badge/智能体-12-f59e0b?style=flat-square alt=智能体:12></a>
  <a href=USERGUIDE.md><img src=https://img.shields.io/badge/文档-用户指南-0ea5e9?style=flat-square alt=文档></a>
</p>

<details>
  <summary>📖 目录</summary>
  <ol>
    <li><a href=#-为什么做这个>为什么做这个</a></li>
    <li><a href=#-你能得到什么>你能得到什么</a></li>
    <li><a href=#-架构>架构</a></li>
    <li><a href=#-快速上手>快速上手</a></li>
    <li><a href=#-开始使用>开始使用</a></li>
    <li><a href=#-ai-子智能体-skills>AI 子智能体</a></li>
    <li><a href=#-mcp-服务工具>MCP 服务工具</a></li>
    <li><a href=#-项目结构>项目结构</a></li>
    <li><a href=#-参与贡献>参与贡献</a></li>
    <li><a href=#-许可证>许可证</a></li>
  </ol>
</details>

---

## 🤔 为什么做这个

Reasonix Code 本身能写代码，但科研不只是写代码——它还需要检索学术数据库、拆解问题、交叉验证来源、跑统计模型、OCR 扫描论文、查询文献管理器、迭代修改稿件。

这个仓库把所有这些打包成一个可移植的配置。

| 能力 | 原生 Reasonix | **加上 fish-ecology-assistant** |
|:-----|:-------------:|:----------------------:|
| 搜索引擎 | 1 个 (`web_search`) | **5 个** (tavily, exa, scholar, article, scholarly) |
| MCP 服务 | 0 | **16 个** |
| AI 子智能体 | 4 个（通用） | **12 个**（领域专用） |
| R 统计 | — | ✅ R 4.6.0 + 20+ 生态学包 |
| OCR 文字识别 | — | ✅ PaddleOCR + Tesseract.js |
| 文献管理器 | — | ✅ 直接查询 Zotero |
| 研究流水线 | — | ✅ 5 阶段 + 自动审查 |
| 知识库 | — | ✅ 连接 13 个 ima 知识库 |
| 新机器配置 | 手动 | ✅ 一个脚本，5 分钟 |

<p align=right>(<a href=#readme-top>回到顶部</a>)</p>

---

## 🎁 你能得到什么

| 类别 | 内容 | 用途 |
|:-----|:-----|:-----|
| 🔍 **5 个搜索引擎** | tavily, exa, scholar, article, scholarly | 从学术数据库到全网 |
| 📊 **R 统计** | R 4.6.0 + 20+ 生态学包 | 形态测量、同位素、群落分析 |
| 🧠 **13 个知识库** | ima 知识库 MCP 集成 | 搜索你的私有和订阅知识库 |
| 🖼️ **双引擎 OCR** | PaddleOCR + Tesseract.js | 扫描论文和截图文字提取 |
| 📚 **Zotero 集成** | 直接 SQL 查询 | 不离开对话查文献库 |
| 📝 **Obsidian 集成** | 读写你的 Obsidian 库 | 研究笔记沉淀到知识库 |
| 🌐 **浏览器自动化** | Playwright | 网页数据抓取和截图 |
| 📈 **图表生成** | ECharts | 可发表的图表 |
| 🎓 **博士申请书写器** | 结构化生成+参考文献 | 从研究主题到完整 proposal |
| 🔄 **自审流水线** | 4 维评分 + 3 轮修订 | 质量可控的输出 |
| 🚀 **一键迁移** | `setup-migrate.ps1` | 克隆 → 运行 → 完成 |

<p align=right>(<a href=#readme-top>回到顶部</a>)</p>

---

## 🏗 架构

<pre>
┌──────────────────────────┐
│  研究 X 主题， │
│ 跑完整流水线           │     编排器
│                           │   (主调度器)
└──────────┬───────────────┘   12 skills · 16 tools
           │
    ┌──────▼───────┐    ┌─────────────────┐
    │ ① 规划器     │───▶│ 子方向          │
    │  🧑‍💼 Plan   │    │  关键词          │
    └──────┬───────┘    │  搜索策略        │
           │            └─────────────────┘
    ┌──────▼───────┐
    │ ② 执行器     │    5 引擎并行
    │  🔍 Search  │    tavily · exa · scholar
    └──────┬───────┘    article · scholarly
           │
    ┌──────▼───────┐
    │ ③ 分析师     │    分类、模式识别、
    │  📊 Analyze │    矛盾检测、涌现信号
    └──────┬───────┘
           │
    ┌──────▼───────┐
    │ ④ 写手       │    结构化综述
    │  ✍️ Write   │    含引用
    └──────┬───────┘
           │
    ┌──────▼───────┐    ┌──────────────┐
    │ ⑤ 审查员     │───▶│ ✅通过→保存  │
    │  ✅ Review  │    └──────────────┘
    └──────┬───────┘    ┌──────────────┐
           └────────────│ 🔄 修订(≤3次)│
                        └──────────────┘
</pre>

<p align=right>(<a href=#readme-top>回到顶部</a>)</p>

---

## ⚡ 快速上手

配置好后，直接对 Reasonix 说：

| 你说 | 它做什么 |
|:-----|:---------|
| `研究[主题]——跑完整流水线` | 5 阶段：规划→搜索→分析→写作→审查 |
| `在 ima 知识库里搜一下[关键词]` | 自动路由到正确知识库，搜索所有相关库，合成结果 |
| `帮我做[统计分析]` | R 代码 + 方法选择 + 诊断 |
| `分析这篇论文：[DOI]` | 深度剖析：方法、质量、可复现性 |
| `查一下我的 Zotero 里关于[主题]` | 直接 SQL 查询文献库 |
| `用 paddleocr 提取这个图片的文字` | OCR 识别中英文 |
| `画一个图表显示[数据]` | ECharts 可视化 |

> 💡 **越具体越好。** `找 2022–2025 年关于长江禁渔的 ≥8 篇同行评审论文` 比 `搜禁渔` 好得多。

<p align=right>(<a href=#readme-top>回到顶部</a>)</p>

---

## 🚀 开始使用

```bash
# 1. 克隆仓库
git clone https://github.com/fangtaocai041/fish-ecology-assistant.git
cd fish-ecology-assistant

# 2. 运行一键迁移脚本
powershell -ExecutionPolicy Bypass -File .reasonix\setup-migrate.ps1

# 3. 重启 Reasonix — 16 个工具 + 12 个技能全部就绪
```

脚本自动处理：依赖检查 → 配置生成 → API 密钥验证 → 路径检测。

> ⚠️ API 密钥文件（`tavily.bat` 等）被 git 忽略——从原机器复制。

<p align=right>(<a href=#readme-top>回到顶部</a>)</p>

---

## 🧠 AI 子智能体 (Skills)

### 研究流水线（5 阶段自动编排）

| # | 智能体 | 角色 | 功能 |
|:-:|:-------|:-----|:-----|
| 🎯 | `research-orchestrator` | **调度器** | 调度全部 5 阶段，重试和回退 |
| ① | `research-planner` | 🧑‍💼 规划 | 拆解问题→关键词+策略，**中英双语** |
| ② | `research-executor` | 🔍 搜索 | 5 引擎并行搜索，**中英双语**查询 |
| ③ | `research-analyst` | 📊 分析 | 分类、模式、矛盾、**涌现检测** |
| ④ | `research-writer` | ✍️ 写作 | 结构化综述，时间锚定 |
| ⑤ | `research-reviewer` | ✅ 审查 | 4 维评分，≤3 轮修订 |

### 领域专家

| 智能体 | 功能 |
|:-------|:------|
| 🎓 `phd-proposal-writer` | 结构化博士申请 proposal |
| 📊 `stats-assistant` | R 代码 + 方法选择 + 结果解读 |
| 🔍 `stats-method-finder` | 搜索 CRAN、期刊、教科书 |
| 📖 `paper-analyzer` | 深度分析：质量评分+可复现性+涌现信号 |
| 🔭 `frontier-tracker` | 跟踪 15+ 个顶级鱼类生态实验室 |
| 📚 `zotero-assistant` | 直接 SQL 查 Zotero |
| 📝 `obsidian-assistant` | 读写 Obsidian 库 |
| 🧠 `ima-smart-search` | 跨知识库智能搜索（自动路由到正确库） |
| ✅ `verify-stats-handbook` | 对比 CRAN + ima 验证手册代码 |

> 🌱 **动态世界观**：所有输出标注时间戳，使用不确定性语言，标记涌现模式。科学在演变——知识是暂时的。

<p align=right>(<a href=#readme-top>回到顶部</a>)</p>

---

## 📡 MCP 服务（工具）

| 服务 | 引擎 | 最佳用途 |
|:-----|:-----|:---------|
| `tavily` | AI 深度搜索 | 全网搜索，15 条结果 |
| `exa` | 语义搜索 | 按含义搜索 |
| `scholar` | Google Scholar | 学术论文、引用数 |
| `article` | 文献元数据 | 全文摘要 |
| `scholarly` | 多源聚合 | 跨库学术搜索 |
| `ima` | ima OpenAPI | 13 个知识库 + 笔记（12 个工具） |
| `rplay` | R 4.6.0 | 形态测量、同位素、群落生态 |
| `coderunner` | 沙箱 | R / Python / JS / Bash |
| `echarts` | ECharts | 可发表的图表 |
| `ocr` | PaddleOCR | 中英文文字识别 |
| `ocr-fallback` | Tesseract.js | 离线 OCR |
| `playwright` | Chromium | 网页抓取、截图 |
| `git` | Git CLI | 版本控制 |
| `github` | GitHub API | 仓库管理 |
| `zotero` | SQLite（只读） | Zotero 文献库查询 |

<p align=right>(<a href=#readme-top>回到顶部</a>)</p>

---

## 📁 项目结构

<pre>
fish-ecology-assistant/
├── README.md                 ← English
├── README.zh.md              ← 中文
├── USERGUIDE.md / GUIDE.md / CHEATSHEET.md
│
├── .reasonix/
│   ├── mcp-servers/          ← 16 个 MCP wrapper
│   ├── skills/               ← 12 个 AI 子智能体
│   ├── handbooks/            ← 统计手册 + 学习手册
│   └── setup-migrate.ps1     ← 一键安装脚本
│
└── research_output/          ← 生成的研究报告
</pre>

<p align=right>(<a href=#readme-top>回到顶部</a>)</p>

---

## 🤝 参与贡献

把这个适配到物理、医学或法律领域了？欢迎 PR！

**改进方向：** Linux/macOS 移植 · 其他领域模板 · Docker 部署

见 [issues 页](https://github.com/fangtaocai041/fish-ecology-assistant/issues)。

<p align=right>(<a href=#readme-top>回到顶部</a>)</p>

---

## 📄 许可证

MIT — 见 [LICENSE](LICENSE)。

基于 Reasonix Code 构建 · 由 DeepSeek 驱动

<p align=right>(<a href=#readme-top>回到顶部</a>)</p>
