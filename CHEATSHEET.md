# 🧠 Reasonix Quick Reference · 快捷指令卡

**Bilingual | 中英对照**

---

## 🎯 One-shot Research · 一句话研究

> **"帮我研究一下 [主题]，运行完整流程"**
> **"Research [topic], run the full pipeline"**

---

## 🧬 12 Skills Quick Reference · 12 个智能体速查

| # | Skill · 技能 | Command · 指令 |
|:-:|-------------|---------------|
| 🎯 | Full pipeline · 完整研究 | `/skill research-orchestrator 研究问题：[主题]` |
| 🧑‍💼 | Planner · 规划 | `/skill research-planner 研究问题：[主题]` |
| 🔍 | Researcher · 检索 | `/skill research-executor [研究计划全文]` |
| 📊 | Analyst · 分析 | `/skill research-analyst [资料库全文]` |
| ✍️ | Writer · 写作 | `/skill research-writer [分析报告全文]` |
| ✅ | Reviewer · 审核 | `/skill research-reviewer [草稿全文]` |
| 🎓 | PhD proposal · 博士计划 | `/skill phd-proposal-writer 研究方向：[主题]` |
| 📊 | R stats · 生物统计 | `/skill stats-assistant 分析需求：[需求]` |
| 🔍 | Stats method · 方法检索 | `/skill stats-method-finder 方法：[方法名]` |
| 📖 | Paper analysis · 论文解析 | `/skill paper-analyzer 解析：[DOI/摘要]` |
| 🔭 | Frontier tracking · 前沿追踪 | `/skill frontier-tracker [团队名]` |
| 📚 | Zotero query · 文献查询 | `/skill zotero-assistant [查询内容]` |
| 📝 | Obsidian notes · 笔记管理 | `/skill obsidian-assistant [操作]` |

---

## 📡 16 MCP Tools Quick Reference · 16 个 MCP 工具速查

| Tool · 工具 | Say · 说 | Purpose · 用途 |
|------------|---------|---------------|
| `tavily` | "用 tavily 搜索：XXX" | Deep search · 深度搜索 |
| `exa` | "用 exa 搜索：XXX" | Semantic search · 语义搜索 |
| `scholar` | "用 scholar 搜索：XXX" | Academic papers · 学术论文 |
| `article` | "用 article 查：XXX" | Article details · 论文详情 |
| `scholarly` | "用 scholarly 查：XXX" | Multi-source research · 多源学术 |
| `playwright` | "用 playwright 打开：URL" | Browser automation · 浏览器 |
| `ocr` | "用 paddleocr 识别：图片" | Chinese OCR · 中文识别 |
| `ocr-fallback` | "用 ocr-fallback 识别：图片" | Offline OCR · 离线识别 |
| `echarts` | "用 echarts 画：图表需求" | Data viz · 数据可视化 |
| `coderunner` | "用 coderunner 跑：代码" | Sandbox execution · 沙箱执行 |
| `rplay` | "用 rplay 跑 R 代码" | R 4.6.0 environment · R 环境 |
| `thinking` | "用 thinking 分析：问题" | Multi-step reasoning · 多步推理 |
| `git` | "用 git 查提交历史" | Version control · 版本控制 |
| `github` | "用 github 查仓库" | GitHub API |
| `zotero` | "用 zotero 查文献" | Zotero database · 文献库 |
| `fs` | "帮我读一下 Obsidian 笔记" | Filesystem · 文件系统 |

---

## 📊 R Analysis Decision Tree · R 分析决策树

```
Data type · 数据类型 → Method · 方法 → R package · R 包
─────────────────────────────────────────────────────
Linear morph · 线性形态  → PCA/LDA/MANOVA → stats / MASS
Landmark morph · 地标点  → Procrustes+CVA → geomorph
Stable isotopes · 同位素 → SIBER ellipses → SIBER
Stomach contents · 胃含物 → NMDS/PERMANOVA → vegan
Genetics · 遗传         → PCA/DAPC/Fst    → adegenet / hierfstat
Community · 群落        → RDA/dbRDA       → vegan
Distribution · 分布      → MaxEnt          → dismo / ENMeval
```

---

## 🌐 Key Terms · 关键术语

| Chinese · 中文 | English · 英文 |
|---------------|---------------|
| 生态位分化 | Niche partitioning |
| 同域共存 | Sympatric coexistence |
| 稳定同位素 | Stable isotope (δ¹³C, δ¹⁵N) |
| 几何形态测量 | Geometric morphometrics |
| 环境DNA | Environmental DNA (eDNA) |
| 简化基因组 | RAD-seq |
| 物种分布模型 | Species distribution model (SDM) |
| 长江十年禁渔 | Yangtze 10-year fishing ban (2021-2030) |
| 功能多样性 | Functional diversity |
| 保护遗传学 | Conservation genetics |

---

## ⚡ PhD Proposal Template · 博士计划模板速查

```
/skill phd-proposal-writer 研究方向：[你的主题]

Produces · 输出:
├── 一、立项依据 (Background & Significance)
├── 二、研究目标与内容 (Objectives & Content)
├── 三、研究方案与技术路线 (Methodology & Workflow)
├── 四、创新点与预期成果 (Innovation & Expected Results)
├── 五、研究计划与进度安排 (Timeline · 4 years)
└── 参考文献 (References · ≤40, last 5 years)
```

---

## 💡 Tips · 小贴士

- **Be specific** · 问题越具体 → 结果越好
- **Split big topics** · 大课题拆成小课题分次研究
- **Results auto-save** · 报告自动存 `research_output/`
- **Try /pro** · 切换到 Pro 模型处理复杂任务
- **Cache bonus** · 长会话 90%+ token 缓存 → 越聊越便宜
