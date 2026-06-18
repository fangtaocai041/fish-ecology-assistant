# HEARTBEAT.md — 项目健康监控

## 指标

| 指标 | 正常范围 | 检查方式 |
|:-----|:---------|:---------|
| 测试通过率 | 100% | `python -m pytest tests/` |
| 知识库物种数 | ≥30 | `sqlite3 data/species.db 'SELECT COUNT(*) FROM species'` |
| 代码无未提交变更 | 是 | `git status --short` |
| pyproject.toml 有效 | 是 | `python -m build --check` |

## 警报

- **🔴 红灯**: 测试 < 90% 或 知识库损坏
- **🟡 黄灯**: 未提交变更超过 5 个文件
- **🟢 绿灯**: 一切正常
