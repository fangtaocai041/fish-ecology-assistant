<p align="center">
  🇬🇧 <a href="README.md">English</a>
</p>

<p align="center">
  <em>"我们踏入又不踏入同一条河流。"</em><br>
  <sub>赫拉克利特，残篇 B49a · 约公元前 500 年</sub>
</p>

<div align="center">
  <h1>🌊 万物皆流</h1>
  <p><strong>你的编码智能体，带上时间感。</strong></p>
  <p>16 个工具 &nbsp;·&nbsp; 12 个子智能体 &nbsp;·&nbsp; 5 个引擎 &nbsp;·&nbsp; 13 个知识库</p>
</div>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue?style=flat-square" alt="License"></a>
  <a href="#"><img src="https://img.shields.io/badge/万物皆流-6366f1?style=flat-square" alt="万物皆流"></a>
  <a href="#"><img src="https://img.shields.io/badge/工具-16-22c55e?style=flat-square" alt="16 tools"></a>
  <a href="#"><img src="https://img.shields.io/badge/智能体-12-f59e0b?style=flat-square" alt="12 agents"></a>
</p>

---

## 哲学

> 世界是动态的。知识是暂时的。涌现是常态。

科研不是收集答案。是**认识世界，提出问题，改造世界。** 知识只是脚印，问题是路。

**世界在动。**
R 包在更新，物种在迁徙，共识在位移。今天的对可能是明天的错。我们把每一条结论锚定在时间上——没有什么是"最终"的。

**知识是暂时的。**
证伪是科学的基石。任何发现都只是"当前最佳解释"。我们用校准过的语言：说"证据表明"不说"证明了"。说"Smith(2022)发现"不说"研究表明"。每句话带时间戳。

**涌现无处不在。**
生命、意识、生态系统——拆开看局部，永远看不懂整体。当三个以上独立来源指向同一个意外的模式，我们标记为**涌现信号**。不是噪声，是消息。

| 没有这个 | 有了这个 |
|:---------|:---------|
| 用 2020 的代码跑 2026 的数据 | 自动查 CRAN，标"已验证于 glmmTMB v1.1.10" |
| "研究表明 X" | "Smith(2022)发现 X；Jones(2024)补充 Y" |
| 把异常当噪声忽略 | ≥3 独立来源 → 主动追踪 |
| 文档写死不再更新 | 动态复查日期，概率陈旧评分 |

---

## 这是什么

**Fish Ecology Assistant** — 一个配置包。把通用编码智能体转变为一个遵循上述哲学的专业鱼类生态学研究团队。

| | 之前 | 之后 |
|:--|:----:|:----:|
| 搜索引擎 | 1 | **5** |
| MCP 服务 | 0 | **16** |
| AI 子智能体 | 4 通用 | **12**（涌现感知） |
| R 统计 | — | 20+ 生态学包 |
| 知识库 | — | 13 个 ima 库，动态发现 |

---

## 快速开始

```bash
git clone https://github.com/fangtaocai041/fish-ecology-assistant.git
cd fish-ecology-assistant
powershell -ExecutionPolicy Bypass -File .reasonix\setup-migrate.ps1
```

| 你说 | 它做 |
|:-----|:-----|
| `研究长江禁渔——跑流水线` | 5 阶段 · 规划→搜索→分析→写作→审查 · 中英双语 · 涌现检测 |
| `验证手册 2.2 章` | 自动查 CRAN · 概率陈旧评分 · 差分验证 |
| `搜 ima 知识库：同位素生态位` | 自动路由 · 多库并行 · 信息增益排序 |
| `帮我做混合效应模型` | R 代码 · 方法选择 · 诊断 · 标注版本 |

---

## 子智能体

| 智能体 | 做什么 | 激活条件 |
|:------|:------|:---------|
| 🎯 研究流水线 (×5) | 规划→搜索→分析→写作→审查 | 按阶段依次触发 |
| 📖 论文分析器 | 时间轴分析 + 涌现信号 | 有论文 DOI |
| 📊 统计助手 | R 代码 + 方法选择 | 涉及代码/方法 |
| 🔍 方法查找器 | 搜 CRAN、期刊、教科书 | 遇到不熟悉的方法 |
| 🧠 ima 智能搜索 | 跨 13 个知识库搜索 | 领域匹配到知识库 |
| ✅ 手册验证 | 自动查 CRAN + 陈旧评分 | 明确请求验证 |
| 🎓 博士 proposal | 结构化研究提案 | 明确请求 |

---

## 工具

| 类别 | 服务 |
|:-----|:------|
| 搜索 | `tavily` · `exa` · `scholar` · `article` · `scholarly` |
| 知识 | `ima`（13 知识库 · 14 工具 · MoE 路由） |
| 计算 | `rplay`（R 4.6.0）· `coderunner` |
| 视觉 | `echarts` · `ocr` · `ocr-fallback` · `playwright` |
| 系统 | `git` · `github` · `zotero` |

---

## 运作方式

哲学是灵魂。工程是肉身。**能量有限——聪明的算法胜过更大的模型。**

**熵预算** — 博士课题：全管线。日常查询：单步搜索。不浪费计算。

**稀疏激活** — 规划器必跑。搜索器有词才跑。分析器有结果才跑。写手有发现才跑。不空转。

**差分验证** — 只检查上次验证以来有变更的包。不做全量检查。

**信息增益** — P0 精确术语先搜。命中就停。P2 冗余词跳过。

---

## 结构

```
fish-ecology-assistant/
├── README.md · README.zh.md
├── .reasonix/
│   ├── mcp-servers/     ← 16 个包装器
│   ├── skills/          ← 12 个子智能体
│   ├── handbooks/       ← 统计手册 + 学习手册
│   ├── readme-versions/ ← 历年 README 存档
│   └── setup-migrate.ps1
└── research_output/
```

---

<p align="center">
  <em>"太阳每天都是新的。"</em> — 赫拉克利特，残篇 B6<br>
  <em>"踏入同一条河流的人，流过他们的是不同的、又是不同的水。"</em> — 残篇 B12<br>
  <br>
  认识世界。提出没有人问过的问题。改变可以改变的。<br>
  没有一个答案能走到最后。但每一个好问题都可以。
</p>

<p align="center">
  <sub>基于 Reasonix Code · DeepSeek 驱动 · 2026</sub>
</p>
