# 🧠 Reasonix 科研助手 — 快捷指令卡

## 一句话研究（最常用）

> **"帮我研究一下 [主题]，运行完整流程"**

## 11 个智能体速查

| 你想做什么 | 指令 |
|-----------|------|
| 🔬 完整研究 | `/skill research-orchestrator 我的研究问题是：[主题]` |
| 🧑‍💼 分解问题 | `/skill research-planner 研究问题：[主题]` |
| 🔍 搜索文献 | `/skill research-executor [研究计划全文]` |
| 📊 分析资料 | `/skill research-analyst [资料库全文]` |
| ✍️ 写综述/报告 | `/skill research-writer [分析报告全文]` |
| ✅ 审核草稿 | `/skill research-reviewer [草稿全文]` |
| 🎓 写博士计划 | `/skill phd-proposal-writer 研究方向：[主题]` |
| 📊 R 统计分析 | `/skill stats-assistant 我需要做：[分析需求]` |
| 🔍 学陌生方法 | `/skill stats-method-finder 方法：[方法名]` |
| 📖 拆解论文 | `/skill paper-analyzer 解析这篇：[DOI或摘要]` |
| 🔭 前沿追踪 | `/skill frontier-tracker 看看 [团队名] 最近动态` |

## 常用 MCP 工具

| 场景 | 直接说 |
|------|--------|
| 搜学术论文 | "用 scholar 搜索：[关键词]" |
| AI 深度搜索 | "用 tavily 搜索：[问题]" |
| 爬网页 | "用 playwright 打开：[URL]" |
| 画图表 | "用 echarts 画：[需求]" |
| 跑代码 | "用 coderunner 跑这段 R 代码" |
| 识别图片 | "用 paddleocr 识别：[图片]" |

## 博士专题

| 场景 | 指令 |
|------|------|
| 完善研究计划 | `/skill phd-proposal-writer 禁捕后长江下游鲌类同域共存的驱动机制` |
| 鳤形态数据 PCA | `/skill stats-assistant 鳤5群体地标点 Procrustes PCA CVA 完整代码` |
| 拟鲿同位素 SIBER | `/skill stats-assistant 圆尾拟鲿白边拟鲿 SIBER 标准椭圆面积` |
| 查 Oberdorff 最新 | `/skill frontier-tracker Oberdorff Tedesco 近半年` |
| 查国内动态 | `/skill frontier-tracker 水生所 长江所 鳤 2025` |

## 注意

- 11 个技能首次调用时自动加载，之后越来越快
- 完整研究流程约 3-8 分钟
- MCP 服务首次启动需要 10-30 秒预热
