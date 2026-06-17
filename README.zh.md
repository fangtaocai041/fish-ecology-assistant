# 🐟 鱼类生态学助手

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python) ![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge) ![Version](https://img.shields.io/badge/Version-v8.1-blueviolet?style=for-the-badge) ![Species](https://img.shields.io/badge/Species-430-success?style=for-the-badge) ![Traits](https://img.shields.io/badge/Traits-289-orange?style=for-the-badge) ![FISHMORPH](https://img.shields.io/badge/FISHMORPH-integrated-9cf?style=for-the-badge) ![Population](https://img.shields.io/badge/Population-26%20records-yellow?style=for-the-badge) ![Bilingual](https://img.shields.io/badge/Bilingual-CN%2BEN-ff69b4?style=for-the-badge) ![DB](https://img.shields.io/badge/DB-SQLite-lightgrey?style=for-the-badge) ![Frontier](https://img.shields.io/badge/Frontier-Kalman%7CNetwork-red?style=for-the-badge)

> 🌊 知识供给核心 — 430种长江鱼类，289项形态性状，种群级变异。
> 万物皆变 · Panta Rhei。

[English](README.md) · [中文](README.zh.md) · [更新日志](CHANGELOG.md)

---

## 📖 目录

- [哲学](#-哲学)
- [快速开始](#-快速开始)
- [架构](#-架构)
- [功能特性](#-功能特性)
- [项目结构](#-项目结构)
- [生态体系](#-生态体系)

---

## 🏛️ 哲学

> 🌍 世界是动态的。📖 知识是暂时的。🌟 涌现是常态。

### 📜 三大信条

**🌍 世界是动态的** — R包在更新，物种分布变化，科学共识在演进。今天正确的结论，六个月后可能过时。

**📖 知识是暂时的** — 科学的基石是可证伪（波普尔）。没有发现是终极真理——只有当前最佳解释。我们用校准语言：证据表明，而非证明。

**🌟 涌现是常态** — 生命、意识、生态系统、AI推理——都是涌现现象。当≥3个独立来源指向同一意外模式，系统标记为涌现信号。

### ⚖️ 为什么这对研究很重要

| 场景 | 传统做法 | 动态世界观 |
|:-----|:--------|:----------|
| 引用 | 研究证明 | Smith(2022)发现X，Jones(2024)补充Y |
| 异常值 | 当作噪声 | ≥3来源→涌现信号 |
| 知识衰减 | 手册冻结 | 含下次审查日期 |

> 道生一，一生二，二生三，三生万物。

这是三角之核心，承载 430 种长江鱼类。


## 🚀 快速开始

```bash
git clone git@github.com:fangtaocai041/fish-ecology-assistant.git
cd fish-ecology-assistant
pip install -e .
python src/main.py search --species "刀鲚"
```

---

## 🏗️ 架构

```
fish-ecology-assistant/
  src/           核心 Python 引擎
  ├── adapter.py     IProjectAdapter 标准接口
  ├── orchestrator.py    KB-First 物种搜索
  ├── project_hub.py     跨项目协调中枢
  ├── dao_engine.py      哲学链执行引擎
  ├── types.py           8 个 dataclass + 4 个枚举
  └── kalman_emergence.py 卡尔曼滤波涌现检测
  config/
  ├── knowledge_base/   30 种 .md 物种档案
  └── fish_species_kb.yaml  430 种索引
  data/
  ├── species.db         SQLite (物种+性状+文献)
  ├── FISHMORPH.csv      2.3MB 全球形态数据库
  └── reports/           HTML/CSV 导出
  scripts/
  ├── fishbase_pull.py   FishBase API 自动同步
  ├── trait_network.py   网络科学性状分析
  └── gen_report.py      双语 HTML 报告生成器
```

---

## ✨ 功能特性

| 功能 | 说明 |
|------|------|
| 🗃️ 430 物种 | 完整长江鱼类物种数据库 |
| 📏 289 形态性状 | FISHMORPH(251种) + FishBase + FAO + 文献 |
| 🌊 种群级数据 | 26条含水域标注的种内性状变异记录 |
| 🔬 性状目录 | 61项性状分7大类 (形态→生活史→食性→...) |
| 🏛️ 双语保护等级 | IUCN + 中国红色名录 + 国家重点 + CITES |
| 📊 Excel/HTML 报告 | 双击打开，双层表头，中英双语 |
| 🔄 FishBase 自动同步 | 自动拉取性状，完整溯源 |
| 🕸️ 网络科学 | 性状共现网络，关键性状识别 |
| 📡 卡尔曼滤波 | 从噪声种群数据检测涌现信号 |
| 🔗 KB-First 架构 | 30种核心物种零网络查询 |

---

## 📁 项目结构

```
fish-ecology-assistant/
  (见上方架构图)
```

---

## 🔗 生态体系

本项目是「三生万物」生态的 知识供给核心 (V0)。

```
三角核心 (sealed 3):
  📦 fish-ecology-assistant    → 知识供给 (V0)
  🔍 cognitive-search-engine   → 搜索验证 (V1)
  ⚙️ eon-core                  → 协调内核 (Coord)

万物衍生 (open N):
  🐬 porpoise-agent    → P₁ 江豚专研
  🐟 coilia-agent      → P₂ 刀鲚专研
  🐟 culter-agent      → P₃ 鲌类专研
  🔥 conflict-arbiter  → C  冲突仲裁
```

> 🔥 和则无穷力量，分则顶尖专家引擎。

---
*SanShengWanWu Ecosystem · MIT License · fangtaocai041*
