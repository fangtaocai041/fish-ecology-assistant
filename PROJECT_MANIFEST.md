# fish-ecology-assistant · 项目架构宣言

> **KB-First, 数据驱动, 三角验证。**

## 核心原则

1. **实事求是** — 知识库先行 (KB-First), 没有调查就没有发言权
2. **三角验证** — ≥3 个独立源指向同一结论 → 可信
3. **辩证综合** — 多源矛盾不是错误, 是认知升级的驱动力
4. **不骗人** — 知道的就说, 不知道的就不说, 不确定的说"不确定"

## 三角核心架构

```
S (Supply 供给) → V (Verify 验证) → Domain (P₁P₂P₃ 专研)
  知识库提供      文献验证           物种专研分析
  fish-ecology    cognitive-search   porpoise/coilia/culter
```

## 标准

- 所有 `search()` 返回统一 dict 格式: `{status, total, papers/items}`
- KB-First: 先查本地知识库, 再走外部搜索
- 测试覆盖: 每新增功能必须加测试
- 版本记录: 每次改 README 前 `python scripts/save_readme_version.py`

## 行为准则

1. **不编造** — 没有证据的结论不输出
2. **可复现** — 每条结论标注来源和可信度
3. **可审计** — 每个决策记录推理链
