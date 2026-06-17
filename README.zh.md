<p align="center">
  🇬🇧 <a href="README.md">English</a>
</p>

<div align="center">
  <h1>🌊 万物皆变 · Panta Rhei</h1>
  <p><strong>把你的编码智能体变成拥有标准 5 层 Agent 架构 + 双核哲学引擎（Panta Rhei + 系统论）的博士级研究团队</strong></p>
  <p>21 個 MCP 服务 · 28 個 AI Skills · 12 引擎搜索 · 13 个知识库 · 18 工程规则 · BDI + ReAct/ToT + MAS · Docker</p>
</div>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square" alt="License"></a>
  <a href="https://deepwiki.com/fangtaocai041/fish-ecology-assistant"><img src="https://devin.ai/assets/askdeepwiki.png" alt="DeepWiki" height="20"></a>
  <a href="#"><img src="https://img.shields.io/badge/双核哲学-Panta_Rhei_%2B_系统-6366f1?style=flat-square" alt="双核哲学"></a>
  <a href="#"><img src="https://img.shields.io/badge/MCP-21-22c55e?style=flat-square" alt="MCP:21"></a>
  <a href="#"><img src="https://img.shields.io/badge/skills-28-f59e0b?style=flat-square" alt="Skills:28"></a>
  <a href="docs/ARCHITECTURE.md"><img src="https://img.shields.io/badge/架构-5层-8b5cf6?style=flat-square" alt="架构:5?></a>
  <a href="#"><img src="https://img.shields.io/badge/规则-18-8b5cf6?style=flat-square" alt="规则:18"></a>
  <a href="config/agent.yaml"><img src="https://img.shields.io/badge/agent-v6.5.0-ec4899?style=flat-square" alt="Agent:v6.5.0"></a>
  <a href="#"><img src="https://img.shields.io/badge/R-4.6.0-276DC3?style=flat-square" alt="R"></a>
  <a href="Dockerfile"><img src="https://img.shields.io/badge/Docker-ready-2496ED?style=flat-square" alt="Docker"></a>
  <a href=".github/workflows/validate.yml"><img src="https://img.shields.io/badge/CI-passing-34D058?style=flat-square" alt="CI"></a>
</p>

---


## 🧠 核心哲学

> 🌍 世界是动态的，知识是暂时的，涌现是常态。
这不是一句口号，而是贯穿整个项目每一行代码、每一次搜索、每一篇分析的操作系统。
### 📜 三大信条

**🌍 世界是动态的** R 包在更新，物种分布在变化，科学共识在演变，气候变化在重塑生态系统。今天正确的结论半年后可能过时。我们不把任何知识当作永恒真理，而是放在时间轴上动态看待。
**📖 知识是暂时的** 科学精神的基石是证伪主义（Popper）。没有发现是终极真理，只是“当前最佳解释”。我们使用校准语言——说"证据表明"而不是“证明”，说"Smith(2022) 发现"而不是「研究表明」"。每一个输出都标注时间锚点。
**🌟 涌现是常态** 生命、意识、生态系统、AI 推理能力——都是涌现的结果。单独分析局部拼凑不出整体。当≥3 个独立来源指向同一个非预期模式时，系统自动标记为涌现信号，而不是当成异常值忽略。
### ⚖ 为什么这对科研至关重要
| 场景 | 传统做法 | 动态世界观的做法 |
|:-----|:--------|:---------------|
| 包版本| → 2020 代码 → 2026 数据 | 自动检查，标记"最后验证于 glmmTMB v1.1.10" |
| 引用 | "研究表明确实如此" | "Smith(2022) 发现 X，但 Jones(2024) 补充了 Y" |
| 异常值 | 忽略，当噪声 | ≥3 独立来源 → 涌现信号，主动追蹤 |
| 知识过期 | 手册写死不再更新 | 验证记录"下次复查日期"，按包活跃度动态计算 |
| 方法选择 | 固定方法用到底 | 动态选择，置信度动态计算 |

### 🧠 系统论· 七大工程原则

| # | 原则 | 源自| 工程映射 |
|---|------|--------|---------|
| ① | 认识论循环| 《实践论》1937) | 数据→模型→验证→修正（闭环控制）|
| ① | 矛盾分析 | 《矛盾论》1937) | 识别主要矛盾 → 资源聚焦 2.5x |
| ① | 阶段性| 《论持久战》1938) | 防御→相持→反攻 = 五阶段流水线 |
| ① | 集中兵力 | 军事思想 | 主矛盾方向60% 计算资源 |
| ① | 主动性| 《论持久战》1938) | 前沿追踪主动建议 + 独立路径 |
| ① | 分类处理 | 《关于正确处理人民内部矛盾的问题》1957) | 对抗性vs 非对抗性→ 不同策略 |
| ① | 系统平衡 | 《论十大关系》1956) | 十大研究平衡 + 多目标优化|

---


## 🐋 DeepSeek 效率原则 (效率即智慧

> **代码映射**: [工程语法 §8](.reasonix/handbooks/engineering-grammar.md)

| ID | 原则 | 代码映射 |
|:---|------|---------|
| **DS-1** | **熵预算** → 计算资源按问题重要性分配。博士课题→全管线，日常→单步搜索。 | `pipeline.stages[].activation` + `research-orchestrator` |
| **DS-2** | **稀疏激活** → MoE 路由：每个 Skill 仅在条件满足时激活。每请求 ~2-4/12 活跃。 | `pipeline.stages[].activation` + `karpathy-guard` |
| **DS-3** | **差分验证** → P(stale) 概率评分仅检查变更包，非全量。复查周期= f(更新频率, 风险, 依赖) | `verify-stats-handbook` skill |
| **DS-4** | **信息增益路由** → P0 精确术语优先 → 命中即停。P2 冗余词跳过。跨库去重。 | `ima-smart-search` skill |

---

## 🔺 三角核心 + 衍生角色: **S/V0 (知识供给)**

> 三角核心 (密闭3) + 衍生 (开放N) 架构: `fish(S/V0)` → `cognitive(V/V1)` → `eon-core(Coord)`，`porpoise(P₁` + `coilia(P₂` + `culter(P₃` + `conflict-arbiter(C)` 为衍生领域专家?> 提供知识、多流域鱼类数据（长江430 + 图们江+ 绥芬河+ 黑龙江扩展中）、矛盾分析和生态发现?> **D??*: ?Agent 辩论网格?*三角验证**: ? 独立源?> ?[eon-core](https://github.com/fangtaocai041/eon-core) 统一协调?
## 📊 自我评价

| 维度 | 评分 | 说明 |
|------|:--:|------|
| 📚 知识广度 | ⭐⭐⭐⭐⭐| 12 搜索引擎 + 13 个知识库+ 多流域鱼类数据库（长江430图们江绥芬河） |
| 🧘 哲学集成 | ⭐⭐⭐⭐⭐| Panta Rhei + 系统论·18 WHEN→THEN 工程规则 |
| 🔬 研究管线 | ⭐⭐⭐⭐⭐| 5 阶段：规划→搜索→分析→撰写→评审，28 AI Skills |
| 🌏 中文文献 | ⭐⭐⭐⭐⭐| 知网/万方/百度学术/中科院弥补西方数据库系统性盲区 |
| 🔗 生态角度| ⭐⭐⭐⭐⭐| 三角核心成员 (V0)，由 eon-core 统一调度 |
| 🧪 测试覆盖 | ⭐⭐⭐⭐⭐| 跨项目验证+ 规则合规检查|

---

## 📋 版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| **v6.5.0** | 2026-06-20 | 🧬 KB-First 两阶段搜索+ 🏠 宿主容器架构 → `ProjectHub` 统一加载6个子系统 · `search_species()` 统一入口 · `delegate_to()` 跨项目委托· fishkb 子库独立 pip 安装 |
| **v6.4.0** | 2026-06-12 | 🔧 工程架构 · exact match(_match_species) · taxonomy_log · detect_taxonomy_discrepancy |
| **v6.3.0** | 2026-06-08 | ☯ 十层同心架构 + conflict-arbiter (V4) 集成 |
| **v6.2** | 2026-06-08 | 三角核心 + 衍生生態· 长江 430 种鱼类知识库 · eon-core 智能调度 |
| **v6.1** | 2026-06-07 | 跨项目协同进化· 三角核心角色 · coordination.yaml |
| **v6.0** | 2026-06-07 | 认知搜索引擎 DirectLoader · 双模式搜索|
| **v5.0** | 2026-06-06 | 12 搜索引擎 · GS优先 + 中文庫 |

> **最新**: v6.5.0 · 2026-06-20

## 🔗 生态体系：三角核心 + 万物衍生

| 项目 | ① | 角色 | 说明 |
|------|:--:|------|------|
| **eon-core** | **Coord** | 协调中枢 | EventBus · CAS · DAG 路由 · 6项目拓扑 |
| **cognitive-search-engine** | **三角 V1** | 验证引擎 | BDI+ReAct · 权威评分 · Hub-and-Spoke 搜索 |
| **porpoise-agent** | **衍生 P₁** | 江豚专研 | 5阶段流水线· 声学分析 · 保护评估 |
| **coilia-agent** | **衍生 P₁** | 刀鲚专研| 耳石微化學· 洄游生态 |
| **culter-agent** | **衍生 P₁** | 鲌类专研 | 营养生态· 生长分析 |
| **conflict-arbiter** | **衍生 C** | 冲突仲裁 | 多源保护级冲突检测|

---

## 🤔 这个项目是什么
**Fish Ecology Assistant** 是一个将 Reasonix Code 从通用编码助手转变为专业鱼类生态学研究团队的完整配置包。它是三生万物三角核心+ 衍生六体架构中的**知识供给核心（S/V0）**，由 **eon-core** 统一协调?
集成了**21 個 MCP 工具** *28 个领域技能**、**12 引擎并行搜索**、自动化**5 阶段研究流水线**、**13 个 IMA 知识库**，以及**R 统计计算环境**——所有输出都遵循上述双核哲学习
### 📊 能力清单

| 能力 | 原生 Reasonix | **加上本配置** |
|:-----|:------------:|:-------------:|
| 搜索引擎 | 1 個 | **12 個** (cognitive_search + scholar, article, scholarly, baidu_scholar, cnki, wanfang, cas, ncbi, tavily, exa, web_search) |
| MCP 服务 | 0 | **21 個**（含 cognitive_search DirectLoader + DeepWiki）|
| AI Skills | 4 个（通用）| **28 个**（6 流水线 + 20 领域 + 2 守护，涌现检测） |
| R 统计 | ① | ✅ R 4.6.0 + 20+ 生态学习|
| OCR | ✅ | ✅ PaddleOCR + Tesseract.js |
| 文献管理 | ① | ✅ 直接查询 Zotero |
| 研究流水线 | ① | ✅ 5 阶段 + 自动审查 + 涌现检测|
| 知识库 | ① | ✅ 连接 13 个 IMA 知识库 |
| 装机 | 手动 | ✅ 一个脚本或 `docker compose up` |
| CI/CD | ✅ | ✅ GitHub Actions 自动验证 |

---

## ☯ 道生一 · 一生二 · 二生三· 三生万物

> — 《道德经》第四十二章

```
        道(Dao)
    外部世界 · 用户的研究问题    长江生态系统的真实需求              │              │        一 (One) → 太极
    命令进入系统 · 统一入口
    fish-ecology-assistant
              │    ┌─────────┴─────────┐    │                  │  阴(Yin)           阳(Yang)
  S/V0 · 知识供给     V/V1 · 搜索验证
  fish                cognitive
    │                  │    └────────┬──────────┘             │ 矛盾统一
             │        三(Three) → 三体
    三角最小封闭结构    S + V + Coord
             │    ┌────────┼────────┬────────┐    │       │       │       │  P₁      P₂      P₃      C
porpoise  coilia  culter  conflict
    │       │       │       │    └────────┼────────┼────────┘             │    万物 (Myriad Things)
    一切事物· 无限演化
    Skills · Papers · Analyses
```

**不是"一万种物种"。是"一??*

| ① | 中文 | English | 在系统中的含義 |
|----|------|---------|---------------|
| ** * | 外界, 自然 | Dao — the external world | 用户的研究问题 长江生态的现实需求|
| **一** | 太极, 命令 | One ?the undivided | 命令进入 fish-ecology-assistant, 统一入口 |
| ** * | 阴阳, 两仪 | Two — Yin and Yang | S(知识/阴)  ?V(验证/阳),, 太极生两仪|
| ** * | 三体, 三角 | Three — the Triangle | fish + cognitive + eon-core, 矛盾统一的封闭结构|
| **万物** | 一切事物| Myriad — all things | 衍生项目 + Skills + 论文 + 输出, 无限演化 |

> **铁律**: 三角密闭 (缺一不可) · 万物开始(无限衍生) · 三角不依赖万物· 二生三即矛盾统一

---

## 🚀 快速开始
```bash
git clone https://github.com/fangtaocai041/fish-ecology-assistant.git
cd fish-ecology-assistant
```

或使用 Docker：```bash
docker compose up
```

---

## 📋 快速导航
- 🎯 技能系统： 6 流水线 + 20 领域 + 2 守护 = 28 Skills
- 🔌 MCP 服务: 21 个（?cognitive_search DirectLoader）- 📁 项目结构: [见上方完整树](#)
- 📜 完整文档: [docs/](docs/) + [.reasonix/handbooks/](.reasonix/handbooks/)
- 🧠 工程语法: [engineering-grammar.md](.reasonix/handbooks/engineering-grammar.md)

---

## 📋 README 变更记录

| 版本 | 日期 | 主题 | 变更内容 |
|:------|:-----|:------|:-------------|
| **v8.1** | 2026-06-20 | README 复原 | 从历史会话记录恢复 系统论七大原则、DeepSeek 效率原则、道生万物架构图、README 变更记录、DeepWiki/双核/Docker 徽标、统一六项目生态 |
| **v7.1** | 2026-06-20 | 数据同步 | + MCP 21 修正, Skills 28 修正, 中英 README 同步, cognitive_search 补入中文 MCP 表|
| **v7.0** | 2026-06-10 | lit-search v3.1 | + lit-search v3.1 (同物异名展开→交互确认→12层管线→三角验证), + credibility_scorer.py, + self_evolve.py, + kb_to_graph_sync.py |
| **v6** | 2026-06-07 | 认知引擎 | + DirectLoader 协议, 双模式搜索 知识图谱进化 |
| **v5** | 2026-06-06 | 搜索 v3.0 | 12 引擎 (GS优先 + 知网/万方/百度学术/中科院）, google-scholar-search 技术 |
| **v4** | 2026-06-06 | 系统论 | + 双核哲学（Panta Rhei + 系统论），7  大系统原则 + 4 效率原则，工程语法(18 WHEN→THEN)，全量代码映射|
| **v3** | 2026-06-05 | 工程化| 全面重写：Panta Rhei 哲学，能力对比，工程效率原则，稀疏激活|
| **v2** | 2026-06-05 | Panta Rhei | 动态世界观整合，涌现检测，校准语言 |
| **v1** | 2026-06-05 | 原始版本 | 初始发布 — 鱼类生态学助手? 引擎 + 12 子智能体 |

---

## 📜 许可证
MIT License © 2026 fangtaocai041

---

> **"不要搜索字符串，要重建所指。**
> Don't search for strings → reconstruct the signified.

---

🌱 **万物皆变 · Panta Rhei**

> 赫拉克利特说：人不能两次踏进同一条河流。
>
> 我们说：知识会老去，但人类对世界的追问永不落幕。昨日之真理为今日之基石，今日之未知为明日之征途。我们的目光，从不囿于已知的疆界；我们的脚步，终将踏上那片星光璀璨的浩瀚征途。

这个项目不是一套固定的工具集——它是一个**活的系统**。

*最后更新: 2026-06-17 | 适用环境: Reasonix Code · DeepSeek 驱动*

---

## 🌱 萬物皆變 · Panta Rhei

> 赫拉克利特說：人不能兩次踏進同一條河流。
>
> 我們說：知識會老去，但人類對世界的追問永不落幕。
> 昨日之真理為今日之基石，今日之未知為明日之征途。
> 我們的目光，從不囌於已知的疆界；我們的腳步，終將踏上那片星光璀璨的浩瀊征途。

這個項目不是一套固定的工具集——它是一個**活的系統**。

*Last updated: 2026-06-17 | Environment: Reasonix Code · DeepSeek 驅動*
