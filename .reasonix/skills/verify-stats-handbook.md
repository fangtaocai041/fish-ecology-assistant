---
name: verify-stats-handbook
description: 验证统计手册中某一章的代码 — 比对CRAN/官方文档/最新论文
runAs: subagent
allowed-tools: read_file, search_content, coderunner_run-code, web_search, web_fetch, scholar_search_literature_graph
---

# 验证统计手册章节

**目标**: 验证 `.reasonix/handbooks/stats-methods.md` 中某一章的 R 代码是否与当前 CRAN 版本和权威来源一致。

## 输入

任务参数中应包含要验证的**章节编号**（如 `2.2` 或 `2.5`）。

## 验证步骤

### 1. 读取手册对应章节

用 `read_file` 读取 `.reasonix/handbooks/stats-methods.md`，定位到目标章节。提取：
- R 代码块
- 用到的包名和函数名
- 当前标注的"最后验证"状态

### 2. 检查各包当前版本

对每个用到的 R 包，在 CRAN 上查最新版本：
- 搜索 `"<package> CRAN"` 或官网
- 记下最新版本号和发布日期

### 3. 比对官方文档

对章节中的每个关键函数：
1. 搜索 CRAN 官方文档 / vignette（如 `"glmmTMB vignette" site:cran.r-project.org`）
2. 确认函数签名、参数名、推荐用法是否匹配
3. 检查是否有 deprecated 的函数

### 4. 检查权威来源

- **方法论文**：通过 `scholar_search_literature_graph` 搜索该方法的原始论文或最新综述
- **CRAN Task View**：如 `"CRAN Task View: Mixed Models"`
- **社区验证**：Stack Overflow / Cross Validated 关键讨论
- **ima 知识库验证**：如果主流程之前调用了 `ima-smart-search` 获取了代码，将其作为比对样本。对比 ima 代码与手册代码的差异，标注哪个更优。

### 5. 生成验证报告

```markdown
## 验证报告：章节 X.X

### 状态
✅ 通过 / ⚠️ 有小问题 / ❌ 需要更新

### 包版本
| 包名 | 手册中用 | CRAN最新版 | 兼容？ |
|:-----|:---------|:-----------|:-------|
| xxx  | x.y.z    | a.b.c      | ✅/⚠️/❌ |

### 代码检查
- 函数签名匹配：✅/⚠️/❌
- 推荐替代写法：...
- 需更新的代码行：...

### 来源
- CRAN: [链接]
- Vignette: [链接]
- 原始论文: DOI

### 建议更新
...
```

### 6. 如果验证通过

输出报告即可。**不要自动修改手册文件** — 让用户决定是否更新验证日期。

### 约束

1. 不要运行需要真实数据的代码（手册里的代码可能依赖本地文件）
2. 如果 coderunner 不可用，仅做文档比对
3. 输出 ≤ 3000 tokens
