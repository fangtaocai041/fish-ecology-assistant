# fangtao_fishlab — 淡水鱼类生态智能体主系统

[![Version](https://img.shields.io/badge/version-v8.0.0-blue)](./__init__.py)

## 概述

fangtao_fishlab 是一个**多 Agent 协作的知识工程平台**，为淡水鱼类生态学研究提供：
- 🔍 多源文献搜索与验证
- 📚 物种知识库查询
- ⚖️ 多源冲突仲裁
- 📈 涌现行为检测
- 🐟 领域专研分析（江豚/刀鲚/鲌类）
- 🧠 贝叶斯工程化信念更新
- 🔗 声明式管线调度

## 快速开始

```python
from fangtao_fishlab import (
    BetaBelief,          # 🧠 贝叶斯信念引擎
    health_check_all,    # 🩺 一键健康检查（含耗时量化）
    get_adapter,         # 🔌 获取任意项目适配器
    query_library,       # 📚 搜索方陶文库
)

# 贝叶斯更新
b = BetaBelief(alpha=2, beta=2)
b.update(successes=8, trials=10)
print(b.mean())  # 0.714

# 全系统健康检查 + 耗时量化
report = health_check_all()

# 获取特定项目的适配器
cse = get_adapter("cognitive-search-engine")
result = cse.search("鳤")

# 搜索方陶文库
docs = query_library("coilia")
```

## 项目结构

```
fangtao_fishlab/
├── __init__.py                # 统一入口
├── _bayesian/                 # 🧠 独立贝叶斯核心
├── _shared/                   # 共享基础设施
│   ├── adapter_protocol.py    # IProjectAdapter + BayesianAdapterMixin
│   ├── types.py               # Pydantic 模型（CheckReport/AdapterState）
│   ├── config_loader.py       # YAML 配置加载
│   ├── pipeline.py            # 管线调度（STANDARD/FAST/DOMAIN）
│   ├── auditor.py             # 结构化步日志（AuditTrail）
│   ├── errors.py              # 5级错误策略（safe_call）
│   └── path_init.py           # ensure_paths() 路径初始化
├── config/                    # YAML 配置文件
│   ├── agents.yaml            # 9个项目角色定义
│   └── bayesian_priors.yaml   # 贝叶斯先验参数
├── scripts/                   # 工具脚本
│   ├── scaffold.py            # 🏗️ 新建 adapter 脚手架
│   ├── health_check_all.py    # 🩺 统一健康检查（含耗时量化）
│   ├── test_pipeline.py       # 管线端到端测试
│   └── benchmark_comparison.py # 新旧对比基准
├── cognitive-search-engine/   # 🔍 V1 搜索验证
├── fish-ecology-assistant/    # 📚 S0 知识供给
├── eon-core/                  # 🔗 协调中枢
├── conflict-arbiter/          # ⚖️ 冲突仲裁
├── infrastructure/            # 📈 涌现检测
├── porpoise-agent/            # 🐬 P1 江豚
├── coilia-agent/              # 🐟 P2 刀鲚
├── culter-agent/              # 🐟 P3 鲌类
└── san-sheng-wanwu-core/      # 🧘 元框架
```

## 共享模块

| 模块 | 功能 | 被使用 |
|:----|:-----|:------|
| `adapter_protocol.py` | IProjectAdapter + BayesianAdapterMixin | 所有 7 个 adapter |
| `types.py` | CheckReport/AdapterState/SearchResult | FEA, 全局导出 |
| `config_loader.py` | YAML 配置加载 | from_config() |
| `pipeline.py` | STANDARD/FAST/DOMAIN 三条管线 | test_pipeline.py |
| `auditor.py` | AuditTrail 结构化步日志 | CSE health() |
| `errors.py` | 5级错误策略 safe_call() | CSE search() |
| `path_init.py` | ensure_paths() 统一路径 | coilia/porpoise adapter |

## 新建项目

```bash
# 🏗️ 一键生成 adapter 模板
python scripts/scaffold.py new-agent <name>

# 📋 列出已有项目
python scripts/scaffold.py list
```

## 双轨制

| 系统 | 用途 | 特点 |
|:----|:-----|:------|
| 🏠 **fangtao_fishlab** | 🖥️ 日常主系统 | 全功能、独立运行、贝叶斯内置 |
| 🌐 **fish_ecology** | 📦 GitHub 简本 | 轻量、一键 pip install |

## 健康检查示例输出

```
[PASS] cognitive-search-engine   t=547.9ms | health=HEALTHY | score=100.0
[PASS] conflict-arbiter          t=0.2ms   | health=HEALTHY | score=100.0
[PASS] porpoise-agent            t=0.3ms   | health=HEALTHY | score=100.0
[PASS] coilia-agent              t=0.3ms   | health=HEALTHY | score=100.0
[PASS] culter-agent              t=0.4ms   | health=HEALTHY | score=100.0
[DEGR] fish-ecology-assistant    t=6.1ms   | health=DEGRADED
[DEGR] eon-core                  t=0.4ms   | health=STANDBY
```

每步附带耗时 t=xxx ms，执行链路可追踪。
