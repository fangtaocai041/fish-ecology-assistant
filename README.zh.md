# 🐟 鱼类生态学助手

[![Python](https://img.shields.io/badge/python-3.10+-blue)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Version](https://img.shields.io/badge/version-8.1-8b5cf6)]()
[![Species](https://img.shields.io/badge/species-430-22c55e)]()
[![Traits](https://img.shields.io/badge/traits-289-orange)]()

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

> 道生一，一生二，二生三，三生万物。

这是三角之 **S (V0)** — 知识供给层。不搜索，不验证，只存储、组织和供给知识。作为三生万物之基，承载430种长江鱼类、289项形态性状，数据来源涵盖FISHMORPH、FishBase、FAO、IUCN、刘凯课题组。

---

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
