# 🧠 Reasonix Code 多智能体科研助手 — 完整指南

> 本文档面向**你（用户）**，解释整个系统的架构、使用方法和背后的设计理念。

---

## ⚡ 与 Cherry Studio 的对比

| 特性 | Cherry Studio | **Reasonix Code** |
|------|:------------:|:-----------------:|
| 子智能体类型 | 伪多智能体（Skills 内联） | ✅ **真隔离 Subagent**（独立进程、独立上下文） |
| 编排方式 | 手动切换 Agent / 单 Agent 调度 | ✅ **自动串行** 5 阶段流水线 |
| 迭代机制 | 手动 | ✅ **自动迭代**（Reviewer → Writer 最多 3 轮） |
| 并发 | 不支持 | ✅ 可**并行调用多个子智能体** |
| MCP 服务 | 逐个手动配置 | ✅ 一键配置，统一管理 |
| 搜索引擎 | 1 个（web_search） | ✅ **5 引擎**（tavily + exa + scholar + article + scholarly） |
| OCR | 无 | ✅ 双手准备（PaddleOCR + Tesseract.js） |
| 图表 | 单独调用 ECharts | ✅ 研究流程内集成 ECharts |
| 上下文爆炸 | Skill 内联 → 主 Agent 上下文挤爆 | ✅ 子智能体隔离运行，只返回结论 |

---

## 📦 系统架构

```
用户提问
    │
    ▼
┌────────────────────────────────────┐
│  🎯 research-orchestrator (主调度)  │  ← 你面对的是这一个
│  "AI 项目经理"                      │
│  可用 MCP 工具: 15 个               │
│  可用子智能体: 5 个                 │
└──┬──────┬──────┬──────┬──────────┘
   │      │      │      │
   ▼      ▼      ▼      ▼
┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐
│🧑‍💼  │→│🔍   │→│📊   │→│✍️   │→ ✍️(迭代)
│Plan │ │Srch │ │Analy│ │Write│
└─────┘ └─────┘ └─────┘ └──┬──┘
                           │ 
                     ┌─────▼─────┐
                     │  ✅ 审核   │
                     │ 通过/修改  │
                     └───────────┘
```

### 5 个专业子智能体

| 角色 | 技能名 | 类型 | 输入 → 输出 |
|------|--------|------|------------|
| 🧑‍💼 Planner | `research-planner` | subagent | 研究问题 → 研究计划（关键词/子课题/搜索策略） |
| 🔍 Researcher | `research-executor` | subagent | 研究计划 → 原始资料库（5 搜索引擎并行） |
| 📊 Analyst | `research-analyst` | subagent | 资料库 → 分析报告（分类/模式/核心发现） |
| ✍️ Writer | `research-writer` | subagent | 分析报告 → 文档草稿（Markdown，学术格式） |
| ✅ Reviewer | `research-reviewer` | subagent | 草稿 → 审核报告（四维评分/修改建议） |

### 15 个 MCP 工具

```
🔍 搜索 (5):  tavily + exa + scholar + article + scholarly
🌐 浏览 (2):  playwright + web_fetch
🖼️ OCR (2):   paddleocr + ocr-fallback (Tesseract.js)
💻 执行 (2):  coderunner + rplay (R 语言)
🧩 推理 (1):  sequential-thinking
📊 图表 (1):  echarts
🐙 Git (2):  github + git
📁 文件 (1):  filesystem
```

---

## 🚀 使用方法

### 方式一：完整流程（推荐）

直接对 Reasonix Code 说：

> 帮我研究一下「长江下游鱼类多样性现状」，运行完整的研究流程。

Reasonix 会自动：
1. 🧑‍💼 Planner 分解问题
2. 🔍 Researcher 5 引擎搜索
3. 📊 Analyst 分析提炼
4. ✍️ Writer 撰写报告
5. ✅ Reviewer 审核把关
6. 如需修改则自动迭代（最多 3 轮）

### 方式二：调用特定子智能体

```
/skill research-planner 我的研究问题是：XXX
/skill research-executor <研究计划全文>
```

### 方式三：使用编排指令

```
/skill research-orchestrator 我的研究问题是：XXX
```

### 方式四：直接调用 MCP 工具

- "用 tavily 搜索：XXX"
- "用 echarts 画一个柱状图展示..."
- "用 paddleocr 识别这张图片的文字"
- "用 scholar 搜索最新的大模型相关论文"

---

## 🎯 最佳实践

### 1. 研究问题越具体越好

```
❌ "帮我研究深度学习"
✅ "对比 CNN、Transformer 和 Mamba 架构在时间序列预测任务上的性能差异"
```

### 2. 大课题拆小

```
❌ "帮我研究整个计算机视觉领域"
✅ 分 3 次：
   1. "图像分割技术的演进"
   2. "目标检测的最新进展"
   3. "多模态大模型在视觉任务中的应用"
```

### 3. 利用 MCP 工具增强

研究过程中，你可以随时要求：
- "用 echarts 把刚才的数据画成图表"
- "用 playwright 爬一下这篇论文的引用数据"
- "用 github 查一下这个开源项目的 star 趋势"

---

## 📁 项目文件结构

```
D:\Reasonix\data\                      ← 工作目录
├── .reasonix/
│   ├── mcp-servers/                   ← 15 个 MCP 服务统一管理
│   │   ├── tavily.bat / exa.bat       ← 搜索类
│   │   ├── github.bat / rplay.bat     ← 工具类
│   │   ├── paddleocr.bat              ← OCR Plan A
│   │   ├── ocr-fallback/              ← OCR Plan B (Tesseract.js)
│   │   └── README.md
│   └── skills/                        ← 6 个智能体技能
│       ├── research-planner.md        ← 🧑‍💼 规划
│       ├── research-executor.md       ← 🔍 检索
│       ├── research-analyst.md        ← 📊 分析
│       ├── research-writer.md         ← ✍️ 写作
│       ├── research-reviewer.md       ← ✅ 审核
│       └── research-orchestrator.md   ← 🎯 编排
├── research_output/                   ← 研究报告输出目录
└── README.md                          ← 本文件
```

### 外部配置

```
C:\Users\小陶\.reasonix\
├── config.json          ← MCP 注册表 + 全局设置
└── memory\              ← 项目记忆（如 MCP 统一目录规则）
```

---

---

## 🐟 个性化定制（蔡方陶 专用）

本系统已根据你的简历和研究方向定制：

| 维度 | 定制内容 |
|------|---------|
| 🧑‍💼 Planner | 内嵌你研究方向：鱼类生态/保护遗传/水生生物多样性 |
| ✍️ Writer | 支持**学术综述**和**博士研究计划**两种写作模板 |
| 🎓 **phd-proposal-writer** | 🆕 专属博士研究计划撰写（宁农/无锡渔业学院） |
| 📊 **stats-assistant** | 🆕 R 代码生成（geomorph/vegan/SIBER/adegenet） |
| 📖 **paper-analyzer** | 🆕 论文深度解析（目标期刊/方法拆解/可复现评估） |

### 专属场景

**写博士研究计划**
```
/skill phd-proposal-writer 研究主题：长江中下游鳤鱼保护遗传学与生态适应性研究
```

**生成 R 分析代码**
```
/skill stats-assistant 帮我生成 NMDS + PERMANOVA + 椭圆面积分析的完整 R 代码
```

**解析论文**
```
/skill paper-analyzer 请分析这篇论文：[标题+摘要或DOI]
```

---

## 💡 核心心法

在 Reasonix Code 中：

- **子智能体是真正的 AI 专家**（隔离运行，独立推理）
- **MCP 工具是专家的手和眼睛**（15 个外设随时调用）
- **你不操作面板，你直接下指令**（所有编排自动完成）
- **迭代自动闭环**（审核→修改→再审核，最多 3 轮）
