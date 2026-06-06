# Changelog

> 📅 格式基于 [Keep a Changelog](https://keepachangelog.com/)
> 🏷️ 语义版本号: `vMAJOR.MINOR.PATCH`

---

## 2026-06-07

### v3.0 — 搜索引擎革命: Google Scholar 优先 + 国内学术源

#### ✨ 新增
- `.reasonix/skills/google-scholar-search.md` — GS 专用搜索 Skill
- `.reasonix/clash-proxy-rule.md` — Clash Verge 全局代理规则（搜索前必读）
- `research_output/session-2026-06-06-07-comprehensive-summary.md` — 完整会话总结
- `CHANGELOG.md` — 本文件

#### 🔧 配置变更
- `config/coordination.yaml` → **v3.0**: 引擎注册表 7→11 (+baidu_scholar/cnki/wanfang/cas), GS priority=1
- `config/agent.yaml` → 引擎列表 GS 排首位 + chinese_priority:true
- `config/component_registry.yaml` → +4 个新引擎 + 4 个 site: 策略

#### 📚 Skills 更新
- `research-executor.md` → v3.0: 重写搜索矩阵，11 引擎，中英文模式
- `unified-species-search.md` → v3.3.2: 11 引擎并行 + 国内源 site: 策略

#### 📖 文档
- `README.md` / `README.zh.md` → v5: 5→11 引擎，GS 优先标注，新增国内源

---

## 2026-06-07 (03:01)

### v2.1 — 7引擎全面激活

#### ✨ 新增
- `coordination.yaml` → **v2.0**: +search_engine_registry (7引擎+fallback优先级)
- `mcp_servers.yaml`: +search_engine_status (当前/下次启动/API key)

#### 📚 Skills 更新
- `unified-species-search.md` → v3.3: allowed-tools +5引擎, 免费/付费自检
- `research-executor.md` → v2.1: allowed-tools +9工具, Step 0区分免费/付费

---

## 2026-06-07 (02:20)

### v3.2 — OCR 变体预生成 + 多 Query 并行 + 新论文检测

#### ✨ 新增
- `species_variants.yaml`: +ocr_error_model (6 策略) + multi_query_parallel + new_paper_detection
- `.reasonix/mcp-servers/ncbi-mcp.mjs` — NCBI E-utilities 直连

#### 📚 Skills
- `unified-species-search` → v3.1: Layer 0 config 强制读取 + 多 query 并行 + Step 6 新论文标记
- `cognitive-species-search` → **已弃用**
- `fuzzy-species-search` → **已弃用**

---

## 2026-06-07 (00:00-00:22)

### D₂ 多Agent辩论验证 + S-T-V 三角

#### ✨ 新增
- `.reasonix/skills/debate-validator.md` — D₂ 3-Agent 网状辩论(统计+数学+代码)
- S-T-V 三角角色: `fish(S) → porpoise(T) → cognitive(V)`

#### 🔧 配置
- `min_sources_core_claim`: 2→3 (三角验证)
- debate-validator → research-reviewer 验证链接入

---

## 2026-06-06 (23:40-23:46)

### 多 Provider 兼容 + YAML 合规

#### ✨ 新增
- `config/models.yaml` +Gemini/OpenAI 章节
- `config/agent.yaml` +DeepSeek 标准 `llm:` 章节

#### 🔧 修复
- 修复重复 `philosophy` key
- YAML 1.2 合规

---

## 2026-06-06 (22:36-22:40)

### v3.1 — 自适应搜索深度 + 子模块网络

#### ✨ 新增
- `external/cognitive-search-engine` — 三项目共享搜索引擎 (git submodule)
- 自适应搜索深度: 穷举(<20篇) / 分类归纳(20-200) / 满意(>200) 三模式
- `config/coordination.yaml` — 三项目协调配置

---

## 2026-06-06 (22:12-22:23)

### v1~v3 — 物种模糊搜索协议

#### ✨ 新增
- `fuzzy-species-search.md` — 7 层模糊搜索协议 (v1)
- `cognitive-species-search.md` — 认知搜索 (v3): 符号学+语言学+语音学+逻辑学
- `species_variants.yaml` — 鳤/鯮/鱤 种拼写变体配置
- `FUZZY_SPECIES_SEARCH.md` — OCR 遗漏根因分析

#### 📚 Skills
- `research-executor` +Fuzzy Fallback Protocol

---

## 2026-06-06 (20:00-22:00)

### Living System 活系统 + 架构审计

#### ✨ 新增
- `config/component_registry.yaml` — 28 组件全注册 + 过期策略
- `.reasonix/skills/component-health-check.md` — 健康检查 P1
- `.reasonix/skills/living-system-dashboard.md` — 仪表盘 + 自动修复 P3
- `.reasonix/skills/rule-auditor.md` — 规则合规审计 P2
- `.reasonix/handbooks/LIVING_SYSTEM.md` — 活系统方案
- `.reasonix/handbooks/UNIFIED_ARCHITECTURE_AUDIT.md` — 跨项目审计

#### 🔧 配置
- `config/agent.yaml` +shared/cross_delegation 章节
- `config/coordination.yaml` +parallelism/serialism/activation_order

---

## 2026-06-06 (17:00-20:00)

### P0-P3 改进 + 工程语法 18 条规则

#### ✨ 新增
- `.reasonix/handbooks/engineering-grammar.md` — 哲学→代码翻译层 (633 行)
- `.reasonix/handbooks/IMPROVEMENT_PLAN.md` — 改进路线图
- `.reasonix/handbooks/WEAKNESSES.md` — 诚实自评
- `.reasonix/handbooks/ADVANTAGES.md` — 前沿创新对比
- `.reasonix/handbooks/activation-matrix.md` — 激活矩阵
- `.reasonix/handbooks/DeepSeek: D1-D4 效率原则`
- `.github/workflows/validate.yml` — CI/CD

#### 📚 Skills
- 6 个核心 Skill +PREFLIGHT 强制 config 读取
- `karpathy-guard` +12 条规则表 + config 路径

---

## 2026-06-06 (12:00-17:00)

### 双核哲学引擎 + README v4

#### ✨ 新增
- `.reasonix/handbooks/systems-thinking.md` — 系统论 7 原则 (319 行)
- 双核哲学: Panta Rhei + Systems Thinking (毛泽东思想)
- `config/agent.yaml` — 矛盾分析/验证循环/阶段论/十大平衡
- `.reasonix/handbooks/engineering-grammar.md` — 工程语法

#### 📖 文档
- `README.md` / `README.zh.md` → v4: 双核哲学, 系统论 7 原则

---

## 2026-06-05

### v1.0 — 初始架构

#### ✨ 创建
- 项目初始结构与配置
- 五阶段研究流水线 (Planner→Executor→Analyst→Writer→Reviewer)
- 13 个子智能体 Skills
- 16 个 MCP 服务
- 中英双语 README, GUIDE, CHEATSHEET, USERGUIDE
- Dockerfile + Docker 部署
- `.gitignore` + API Key 安全策略
- `research_output/yangtze-fishing-ban-ecological-assessment.md` — 首篇研究报告
