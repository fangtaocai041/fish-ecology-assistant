# Fish Ecology Assistant 🐟

**鱼类生态学知识供给引擎** — 三角核心 S/V0 层。

> 万物皆变 · Panta Rhei
>
> 长江里的每一片鳞片，都藏着一个故事。
> 我们试着把这些故事，讲给算法听。

[English](README.md) · [中文](README.zh.md) · [更新日志](CHANGELOG.md) · [工程记录](RE.md) · [架构](docs/ARCHITECTURE.md)

---

## 为什么有这个项目？

长江曾是世界上水生生物多样性最丰富的河流之一。443 种鱼类，穿梭在从青藏高原到东海的 6300 公里水域。但过去几十年，它们中的许多在悄悄消失——白鲟（*Psephurus gladius*）在 2022 年被宣布灭绝，长江江豚（*Neophocaena asiaeorientalis*）一度只剩约 1000 头。

2021 年，长江开始实施"十年禁渔"。这是人类历史上规模最大的河流生态修复实验。但问题随之而来：

> **禁渔之后，鱼回来了吗？哪些物种在恢复？哪些仍在崩溃？我们怎么知道？**

这个项目就是为了回答这些问题而生的。它不是一个通用的 AI 助手——它是一个出生在长江边的数字生态学家，它的知识库里有长江的每一科、每一属、每一种，它的搜索针脚扎在中文期刊和英文数据库之间，它的心脏是一套叫做"三生万物"的架构。

> 道生一，一生二，二生三，三生万物。
> 鱼生水，水生万物，万物归于江。

---

## 快速开始

```bash
# 安装
pip install -e .

# 查物种（交互式—先问知识库，再决定是否全网搜）
python scripts/search_species.py "鳤"

# 仅查知识库
python scripts/search_species.py "鳤" --kb-only

# 自动全量搜索 + 写回知识库
python scripts/search_species.py "珠星三块鱼" --auto
```

```python
from src import get_orchestrator

orch = get_orchestrator()
result = orch.kb_first_lookup(query="鳤")
print(result.summary_text)
# 📚 f项目知识库已收录: 鳤（Ochetobius elongatus）
# - 科属: 鲤科
# - 保护: CR（极危）
```

---

## 哲学 · 三生万物

项目的灵魂是一句古老的中国智慧。

| 哲学概念 | 代码落地 | 意义 |
|----------|----------|------|
| **道 (Dao)** | 用户的研究问题 | 现实世界的生态学需求，从这里进入系统 |
| **一 (One)** | `ProjectHub` | 太极 · 统一入口，未分阴阳的初始态 |
| **二 (Two)** | S(知识) ↔ V(验证) | 阴与阳的对立统一——知识库是静的，搜索是动的 |
| **三 (Three)** | fish + cognitive + eon | 密闭三角——最小完整结构，缺一不可 |
| **万物 (Myriad)** | porpoise/coilia/conflict/... | 三角赋能，无限衍生 |

**铁律**: 三角密闭 · 万物开放 · 三角不依赖万物

### Panta Rhei — 万物流转

> "人不能两次踏进同一条河流" — 赫拉克利特

知识不是死的档案。分类学会变，种群会波动，文献会更新。这个项目不假装知识是永恒的——每条文献有 `added_at` 时间戳，每次分类变更记入 `taxonomy_log`，搜索策略根据历史表现自动调参，路径通过环境变量而非硬编码。

### 涌现 — 看见模式

当三个以上独立来源指向同一个非预期信号，系统不会忽略它。`EmergenceSignal` 会亮起，告诉你：**这里可能有一条你没看到的路**。

---

## 三角核心架构

```
                   三 生 万 物
               Triangle → the Myriad

    ┌───────────────────────────────────┐
    │        三角核心 (sealed 3)        │
    │          缺一不可                 │
    │                                   │
    │  S/V0  fish-ecology-assistant    │  ← 本项目：知识供给
    │  V/V1  cognitive-search-engine   │  ← 搜索验证
    │  Coord eon-core                  │  ← 协调内核
    └──────────────┬────────────────────┘
                   │ 赋能
          ┌────────┼────────┐
          ▼        ▼        ▼
       P₁        P₂         C
    porpoise   coilia   conflict-arbiter
    (江豚)     (刀鲚)    (冲突仲裁)
       │
       ▼
    P₃, P₄ ... 万物 · 开放集合 · 无限衍生
```

本系统是三角的 **S (知识供给)** 层。它不负责搜索验证（那是 V 的事），不负责任务调度（那是 Coordinator 的事）。它只做一件事：**知道鱼的事情**。

---

## 两阶段搜索：先问自己人，再问全世界

```
用户说 "查一下鳤"
  │
  ├── Stage 1: kb_first_lookup()
  │     查本地 30 物种知识库（零 token 成本）
  │     ├── ✅ 有数据 → 展示摘要 + 问用户：够了吗？
  │     └── ❌ 没找到 → 推荐 Stage 2
  │
  └── Stage 2: cognitive-search-engine
        调用 V/V1 层 → 多源并行搜索 → 可信度评分 → 写回
```

为什么不直接全网搜？因为知识库里的 30 个物种档案，是用户（和课题组）一篇篇读、一条条写进去的。**先问自己的知识，再问全世界的搜索引擎**——这是对时间和 token 的双重尊重。

---

## 物种知识库

当前收录 **30 个物种**，覆盖长江流域、图们江/绥芬河流域。

| 中文名 | 学名 | 科 | 故事 |
|--------|------|----|------|
| 鳤 | *Ochetobius elongatus* | 鲤科 | CR 极危，2024 年才有了第一个染色体级别基因组。鳤可能是禁渔后恢复最快的物种之一——2025 年的研究正在验证这个猜想。 |
| 刀鲚 | *Coilia nasus* | 鳀科 | "长江三鲜"之首。每年春夏之交，它们从海里游回长江产卵。耳石里的 Sr/Ca 比值，记录着每一条鱼的洄游路线。 |
| 长江江豚 | *Neophocaena asiaeorientalis* | 鼠海豚科 | 长江里唯一的哺乳动物。2017 年约 1012 头，2022 年约 1249 头——禁渔后第一次止跌回升。 |
| 三块鱼 | *Tribolodon brandti* | 鲤科 | 溯河洄游鱼类。日语叫ウグイ（ugui），在日本的溪流里随处可见，在中国却只存在于图们江和绥芬河。 |
| 白鲟 | *Psephurus gladius* | 匙吻鲟科 | 2022 年宣布灭绝。我们把它留在知识库里，不是为了研究——是为了记得。 |

完整列表：`config/fish_species_index.yaml`

---

## 入口 API

```python
from src import (
    get_orchestrator,  # 核心编排器（单例）
    get_hub,           # 跨项目协调中枢（单例）
    FishEcologyAdapter,# 跨项目适配器
)

# ── 查知识库 ──
orch = get_orchestrator()
r = orch.kb_first_lookup(query="鳤")
r.found                # True
r.summary_text         # 人类可读摘要
r.search_recommendation  # "stay_in_kb" | "continue_to_c"

# ── 跨项目协调 ──
hub = get_hub()
hub.is_triangle_complete()    # 三角核心完整？
hub.triangle_status()         # 每个角的状态
hub.search_species("鳤")      # 统一物种搜索

# ── 道→一→二→三→万物 ──
from src.dao_engine import DaoEngine, DaoQuery
engine = DaoEngine()
result = engine.execute(DaoQuery(raw="鳤"))
print(engine.render(result))
```

详细 API 参考：[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)

---

## 项目结构

```
fish-ecology-assistant/
├── src/
│   ├── __init__.py         ← 19 个公共导出 (v6.5.3)
│   ├── orchestrator.py     ← 核心编排器 · KB-First 搜索
│   ├── project_hub.py      ← 跨项目协调 · 三生万物
│   ├── adapter.py          ← 跨项目适配器
│   ├── dao_engine.py       ← 道→一→二→三→万物 执行引擎
│   ├── shared.py           ← 期刊白名单 / OCR 变体
│   ├── types.py            ← 8 dataclass + 4 Enum
│   └── audit_logger.py     ← JSONL 审计
├── scripts/                ← CLI 入口
├── config/                 ← 配置 + 知识库
├── tests/                  ← 33 个测试
├── docs/                   ← 架构文档
└── .reasonix/skills/       ← 28 个 Reasonix Skill
```

---

## 测试

```bash
python -m pytest tests/ -v
# 33 passed in 0.77s
# ├── test_orchestrator.py — 18 tests（已知物种/别名/模糊匹配/边界）
# ├── test_project_hub.py  —  8 tests（三角/万物/单例）
# └── test_shared.py       —  7 tests（白名单/查询/OCR）
```

---

## 关于作者

这个项目是**蔡方陶**（水生生物学硕士在读，江汉大学/中国水产科学研究院长江水产研究所，刘凯课题组）的研究工具。它不是课程作业，不是公司产品——它是一个在实验室里、在长江边、在深夜的 R 语言报错中慢慢长出来的东西。

如果你也是长江鱼类生态的研究者，欢迎用这个工具，欢迎提 issue，欢迎 fork。

---

## 许可证

MIT © 2026 fangtaocai041 · 蔡方陶 · 江汉大学 / FFRC 刘凯课题组

> 鱼在水里，你在岸上，代码在中间。
> 愿算法和河流一样有温度。
>
> **最后更新: 2026-06-21 · Reasonix Code · DeepSeek 驱动**
