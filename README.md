# 🧠 多智能体科研助手系统

## 架构概览

```
用户提问
    │
    ▼
┌─────────────────┐
│  🧑‍💼 Planner    │  将问题分解为关键词、子课题、搜索策略
│  (research-     │
│   planner)      │
└────────┬────────┘
         │ 研究计划
         ▼
┌─────────────────┐
│  🔍 Researcher  │  执行 Web 搜索、文献收集、信息提取
│  (research-     │  工具：web_search, web_fetch
│   executor)     │
└────────┬────────┘
         │ 原始资料库
         ▼
┌─────────────────┐
│  📊 Analyst     │  分类、归纳、模式识别、提炼核心观点
│  (research-     │
│   analyst)      │
└────────┬────────┘
         │ 分析报告
         ▼
┌─────────────────┐
│  ✍️ Writer      │  撰写综述/技术文档，Markdown 格式化
│  (research-     │
│   writer)       │
└────────┬────────┘
         │ 文档草稿
         ▼
┌─────────────────┐
│  ✅ Reviewer    │  质量检查、事实核查、格式校验
│  (research-     │  → 通过 / 需修改 / 不通过
│   reviewer)     │
└────────┬────────┘
         │
    ┌────┴────┐
    ▼         ▼
  通过      需修改 ──→ 返回 Writer
```

## 安装的技能（5个子智能体 + 1 编排指令）

| 角色 | 技能名称 | 类型 | 输入 → 输出 |
|------|---------|------|------------|
| 🧑‍💼 Planner | `research-planner` | subagent | 研究问题 → 研究计划 |
| 🔍 Researcher | `research-executor` | subagent | 研究计划 → 原始资料库 |
| 📊 Analyst | `research-analyst` | subagent | 资料库 → 分析报告 |
| ✍️ Writer | `research-writer` | subagent | 分析报告 → 文档草稿 |
| ✅ Reviewer | `research-reviewer` | subagent | 文档草稿 → 审核报告 |
| 🎯 Orchestrator | `research-orchestrator` | inline | **以下指令供 Reasonix Code 执行** |

## 使用方法

### 方式一：直接调用特定角色

```bash
# 示例：先做规划，再看结果
> /skill research-planner "我的研究问题是：大语言模型在医疗诊断中的应用现状"
```

### 方式二：完整流程（推荐）

对 Reasonix Code 说：

> 帮我研究一下「你的研究主题」，运行完整的研究流程。

Reasonix Code 会自动：

1. **运行 Planner** → `run_skill("research-planner")` 分解问题
2. **运行 Researcher** → `run_skill("research-executor")` 搜索收集
3. **运行 Analyst** → `run_skill("research-analyst")` 分析提炼
4. **运行 Writer** → `run_skill("research-writer")` 撰写报告
5. **运行 Reviewer** → `run_skill("research-reviewer")` 审核把关
6. 若需修改则迭代，否则输出最终报告

### 方式三：使用编排智能体

```
> /skill research-orchestrator "我的研究问题是：..."
```

这会触发完整的 5 阶段自动流水线。

## 技能文件位置

```
.reasonix/skills/
├── research-planner.md     # 🧑‍💼 规划智能体
├── research-executor.md    # 🔍 检索智能体（含 web_search/web_fetch 权限）
├── research-analyst.md     # 📊 分析智能体
├── research-writer.md      # ✍️ 写作智能体
└── research-reviewer.md    # ✅ 审核智能体
```
