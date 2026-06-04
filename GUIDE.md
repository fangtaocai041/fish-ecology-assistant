# 🧠 Complete Guide · 完整指南

**Bilingual | 中英对照**

> This document is for **you (the user)** — explaining the full system architecture, how to use every skill, and best practices.
>
> 本文档面向**你（用户）**——解释整个系统架构、所有技能的使用方法和最佳实践。

---

## 📦 System Overview · 系统概述

### What You Have · 你拥有什么

| Component · 组件 | Count · 数量 | Details · 详情 |
|-----------------|:-----------:|---------------|
| MCP Services · MCP 服务 | **16** | Search · Academia · Compute · OCR · Browser · Git |
| Subagent Skills · 子智能体 | **12** | Research pipeline (5) + Domain specialists (7) |
| Search Engines · 搜索引擎 | **5** | tavily, exa, scholar, article, scholarly |
| OCR Systems · 文字识别 | **2** | PaddleOCR (online) + Tesseract.js (offline) |

### Architecture · 架构

```
            User · 用户
               │
               ▼
    ┌──────────────────────────┐
    │   🎯 Orchestrator        │  ← AI Project Manager
    │   research-orchestrator  │    项目经理
    └──────────┬───────────────┘
               │  dispatches · 调度
    ┌──────────┼──────────┐
    ▼          ▼          ▼
┌──────┐  ┌──────┐  ┌──────────┐
│Pipeline│  │Domain │  │  Direct  │
│Research│  │Skills │  │MCP Tools │
└──────┘  └──────┘  └──────────┘
```

---

## 🎯 Using the System · 使用说明

### Mode 1: Full Research Pipeline · 完整研究流程（推荐）

Simply say to Reasonix Code:
直接对 Reasonix 说：

> **"帮我研究一下 [你的主题]，运行完整流程"**

Or explicitly:
或明确调用：

> `/skill research-orchestrator 我的研究问题是：[主题]`

This triggers the 5-stage pipeline + up to 3 review iterations:
这会触发 5 阶段流水线 + 最多 3 轮审核迭代：

```
Stage 1: 🧑‍💼 Planner  → 分解研究问题
Stage 2: 🔍 Researcher → 5 引擎并行搜索
Stage 3: 📊 Analyst    → 分类、模式识别、提炼
Stage 4: ✍️ Writer     → 撰写综述/报告
Stage 5: ✅ Reviewer   → 四维评分审核
         └── 🔄 需修改 → 返回 Writer 重写（≤3轮）
         └── ✅ 通过   → 输出最终报告到 research_output/
```

### Mode 2: Call a Specific Subagent · 调用特定子智能体

| Skill · 技能 | Command · 指令示例 |
|-------------|------------------|
| 🧑‍💼 Planner | `/skill research-planner 研究问题：长江十年禁渔对鱼类群落的影响` |
| 🔍 Researcher | `/skill research-executor <研究计划全文>` |
| 📊 Analyst | `/skill research-analyst <资料库全文>` |
| ✍️ Writer | `/skill research-writer <分析报告全文>` |
| ✅ Reviewer | `/skill research-reviewer <草稿全文>` |

### Mode 3: Domain Skills · 专用技能

| Skill · 技能 | Command · 指令示例 |
|-------------|------------------|
| 🎓 PhD Proposal · 博士计划 | `/skill phd-proposal-writer 研究方向：禁捕后长江下游鲌类同域共存的驱动机制` |
| 📊 R Stats · 生物统计 | `/skill stats-assistant 生成鳤5群体地标点Procrustes PCA完整R代码` |
| 📖 Paper Analysis · 论文解析 | `/skill paper-analyzer 解析这篇论文：[DOI或标题+摘要]` |
| 🔭 Frontier Tracking · 前沿追踪 | `/skill frontier-tracker 看看Oberdorff团队最近动态` |
| 🔍 Stats Method · 方法检索 | `/skill stats-method-finder 介绍MaxEnt模型的R实现和调参方法` |
| 📚 Zotero Query · 文献库查询 | `/skill zotero-assistant 查一下我Zotero里关于稳定同位素的最新文献` |
| 📝 Obsidian Notes · 笔记管理 | `/skill obsidian-assistant 帮我读一下研究笔记中关于鳤的内容` |

### Mode 4: Direct MCP Tools · 直接调用 MCP

| Scenario · 场景 | Say this · 这样说 |
|---------------|-----------------|
| Deep search · 深度搜索 | "用 tavily 搜索：XXX" |
| Academic search · 学术搜索 | "用 scholar 搜索：Culter alburnus genetic diversity" |
| OCR · 文字识别 | "用 paddleocr 识别这张图片里的文字" |
| Charts · 图表 | "用 echarts 画一个柱状图展示..." |
| Web scraping · 网页抓取 | "用 playwright 打开这个网页..." |
| R code · 跑 R 代码 | "用 coderunner 跑这段 R 代码" |
| Sequential thinking · 多步推理 | "用 thinking 分析这个问题..." |

---

## 🎯 Best Practices · 最佳实践

### 1. Be Specific · 问题越具体越好

```
❌ "帮我研究深度学习"
✅ "对比 CNN、Transformer 和 Mamba 架构在鱼类图像识别任务上的性能差异"
```

### 2. Split Large Topics · 大课题拆小

```
❌ "帮我研究整个鱼类生态学"
✅ 分 3 次：
   1. "长江禁捕对鱼类群落结构的影响"
   2. "稳定同位素在生态位研究中的应用进展"
   3. "eDNA 技术在鱼类监测中的方法论综述"
```

### 3. Use Domain Terminology · 使用领域术语

The system understands these terms naturally:
系统自然理解以下术语：

- **生态位分化** (niche partitioning)
- **稳定同位素** (δ¹³C, δ¹⁵N)
- **几何形态测量** (geometric morphometrics)
- **同域共存** (sympatric coexistence)
- **简化基因组** (RAD-seq)
- **物种分布模型** (MaxEnt)

### 4. Results Are Saved · 结果自动保存

All research outputs are saved to `research_output/`:
所有研究报告保存到 `research_output/` 目录：

```
research_output/
├── 2026-06-03-长江禁渔生态成效评估.md
└── ...
```

---

## 🛠️ Skills Architecture · Skills 架构说明

### 每个 Subagent 的提示词优化原则

All 12 skills have been optimized with the following principles (applied in Step 1-3 of this project's optimization):
所有 12 个 Skills 已按以下原则优化：

| Principle · 原则 | What changed · 改了什么 |
|-----------------|----------------------|
| **Output budget · 输出预算** | Every skill has explicit token limits to prevent context overflow |
| **Fallback chain · 降级链** | MCP tool failures don't break the pipeline — auto fallback |
| **Citation validation · 引用验证** | Core findings require ≥2 independent sources |
| **Anti-hallucination · 防幻觉** | Empty results must be reported as "no results", never fabricated |
| **Cache-friendly · 缓存友好** | Stable frontmatter, variable content at bottom |

---

## 🔒 Security Notes · 安全说明

| Item · 项目 | Status · 状态 |
|------------|:------------:|
| API keys (tavily, exa, github) | ✅ In `.gitignore` |
| SSH key for GitHub push | ✅ `C:\Users\小陶\.ssh\id_ed25519` |
| Zotero database path | ✅ `D:\ZoteroData\zotero.sqlite` |
| OCR-Fallback auto install | ✅ Built-in (npm install on first run) |

---

## 📁 File Locations · 文件位置

| File · 文件 | Path · 路径 |
|------------|------------|
| MCP wrapper scripts · 脚本 | `.reasonix/mcp-servers/` |
| Skills playbooks · 技能 | `.reasonix/skills/` |
| Research outputs · 报告 | `research_output/` |
| Reasonix config · 配置 | `C:\Users\小陶\.reasonix\config.json` |
| Project memory · 记忆 | `C:\Users\小陶\.reasonix\memory\` |

---

## 💡 Philosophy · 核心理念

> **You are the captain. I am the engine room, the navigation system, and all the cables.**
> **你是船长，我是引擎舱 + 导航仪 + 所有缆绳。**

The tool can search 50 papers in seconds, write a draft in minutes, and run R code instantly.
工具可以秒搜 50 篇文献、分钟写草稿、秒跑 R 代码。

But only **you** can decide:
但只有**你**能决定：
- What is a good research question? · 什么是一个好问题？
- What is meaningful science? · 什么是有意义的科学？
- Where should we go next? · 下一步去哪里？

*The stronger the tool, the more irreplaceable the person using it.*
*工具越强，使用工具的人越不可替代。*
