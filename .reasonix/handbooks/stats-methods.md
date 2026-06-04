# 📐 统计方法手册 — Fish Ecology & Conservation Genetics

> 按研究问题找方法，按方法找 R 代码。**本手册是你积累、验证过的方案库**，优先使用。

> ⚠️ **代码需定期验证**：R 包版本更新可能导致代码失效或输出变化。每个模板最后标注了"最后验证日期"和"来源"。使用前检查验证状态，发现代码有问题→更新并改日期。

---

## 📋 验证总览

| 章节 | 最后验证 | 验证方式 | 来源 |
|:-----|:--------|:---------|:-----|
| 2.1 两组/多组比较 | 未验证 | — | — |
| 2.2 混合效应模型 | 未验证 | — | — |
| 2.3 形态 PCA/CVA | 未验证 | — | — |
| 2.4 SIBER | 未验证 | — | — |
| 2.5 NMDS+PERMANOVA | 未验证 | — | — |
| 2.6 遗传 DAPC+Fst | 未验证 | — | — |
| 2.7 SDM | 未验证 | — | — |
| 2.8 RDA/CCA | 未验证 | — | — |
| 2.9 食性分析 | 未验证 | — | — |
| 3. 样本量 | 未验证 | — | — |

> **更新流程**：用 `验证手册章节` 技能（见下文）→ 或手动运行代码 + 比对 CRAN 官方文档/vignettes → 确认无误后改日期

---

> **📡 ima 知识库验证**：你也可以调 `ima-smart-search` 技能，在 ima 知识库中搜对应方法的 R 代码和教程。已订阅的"生态学数据统计分析(R语言)"（58人验证）、"统计学"（31830篇）等知识库是高质量代码来源，搜到后与手册代码比对，验证通过后更新验证记录。

## 目录

- [1. 方法选择速查（按研究问题）](#1-方法选择速查按研究问题)
- [2. 常用分析模板](#2-常用分析模板)
  - [2.1 两组/多组比较](#21-两组多组比较)
  - [2.2 混合效应模型](#22-混合效应模型)
  - [2.3 形态学 PCA + CVA](#23-形态学-pca--cva)
  - [2.4 稳定同位素 - SIBER](#24-稳定同位素---siber)
  - [2.5 群落分析 NMDS + PERMANOVA](#25-群落分析-nmds--permanova)
  - [2.6 遗传学 DAPC + Fst](#26-遗传学-dapc--fst)
  - [2.7 物种分布模型（SDM）](#27-物种分布模型-sdm)
  - [2.8 环境因子 RDA / CCA](#28-环境因子-rda--cca)
  - [2.9 食性分析](#29-食性分析)
- [3. 样本量 / 检验效力](#3-样本量--检验效力)
- [4. 常见坑](#4-常见坑)
- [5. 推荐参考书 & 文献](#5-推荐参考书--文献)
- [6. 附录：包版本 & 安装备忘](#6-附录包版本--安装备忘)

---

## 1. 方法选择速查（按研究问题）

### 1.1 我该用什么方法？

```
┌─ "两个群体在某个指标上有差异吗？"
├── 正态 + 方差齐 → t.test() / lm()
├── 非正态 → wilcox.test()
└── 配对 → paired t.test() / wilcox.test(paired=TRUE)

┌─ "多个群体（≥3）有差异吗？"
├── 正态 + 方差齐 → aov() + TukeyHSD()
├── 非正态 → kruskal.test() + dunn.test()
└── 有协变量 → ANCOVA: lm(Y ~ group + covariate)

┌─ "有重复测量 / 随机效应？"
└── 混合效应模型 → glmmTMB / lme4 / nlme

┌─ "想区分形态差异？"
├── 线性测量 → PCA + LDA / CVA
└── 地标点 → Procrustes ANOVA (geomorph)

┌─ "想知道群落组成差异？"
├── 二维 → NMDS (vegan::metaMDS)
├── 统计检验 → PERMANOVA (vegan::adonis2)
└── 环境驱动因子 → RDA / dbRDA

┌─ "想知道物种分布受什么环境因子影响？"
└── SDM → MaxEnt (ENMeval) / biomod2

┌─ "同位素生态位有重叠吗？"
└── SIBER 贝叶斯椭圆

┌─ "群体遗传结构？"
├── PCA → adegenet::glPca
├── 聚类 → DAPC
├── 分化 → Fst / Weir & Cockerham
└── 亲缘关系 → kinship matrix
```

### 1.2 数据类型 → 分析方法映射

| 数据类型 | 格式 | 常用方法 | R 包 |
|:---------|:-----|:---------|:-----|
| 线性形态测量 | `species, SL, BD, HL, ...` | ANOVA / MANOVA / PCA / LDA | `stats`, `MASS`, `vegan` |
| 地标点形态 | `.tps` / 坐标矩阵 | Procrustes ANOVA + PCA + CVA | `geomorph`, `Morpho` |
| 稳定同位素 | `species, d13C, d15N, ...` | SIBER 椭圆 / MixSIAR | `SIBER`, `MixSIAR` |
| 胃含物 | `species, prey, count/vol` | NMDS / PERMANOVA / 多样性指数 | `vegan` |
| 群落矩阵 | species × site | NMDS / dbRDA / PERMANOVA / 指示种 | `vegan`, `indicspecies` |
| 遗传数据 | `.vcf` / genind / genlight | PCA / DAPC / Fst / AMOVA | `adegenet`, `hierfstat`, `poppr` |
| 环境因子 | `temp, DO, pH, depth, ...` | RDA / CCA / dbRDA | `vegan` |
| 物种分布 | 经纬度 + 环境栅格 | MaxEnt / BIOMOD2 | `ENMeval`, `biomod2`, `maxnet` |
| eDNA ASV | ASV × sample | phyloseq / 多样性 / 差异丰度 | `phyloseq`, `DESeq2` |

---

## 2. 常用分析模板

### 2.1 两组/多组比较

```r
# ========== 两组比较 ==========
library(tidyverse)

dat <- read_csv("data/morph.csv")
# 列: species (A/B), SL (mm)

# 正态性 + 方差齐性检查
dat %>% group_by(species) %>% 
  summarise(W = shapiro.test(SL)$statistic, p = shapiro.test(SL)$p.value)

car::leveneTest(SL ~ species, data = dat)

# t-test (正态 + 方差齐)
t.test(SL ~ species, data = dat, var.equal = TRUE)
# Wilcoxon (非正态)
wilcox.test(SL ~ species, data = dat)

# ========== 多组比较 (≥3) ==========
# 正态 + 方差齐
m <- aov(SL ~ species, data = dat)
summary(m)
TukeyHSD(m)

# 非正态
kruskal.test(SL ~ species, data = dat)
# 事后检验需 dunn.test 包
dunn.test::dunn.test(dat$SL, dat$species, method = "bh")

# ========== ANCOVA (含协变量) ==========
# 问题：不同物种的 SL-BD 关系有无差异？
m <- lm(BD ~ SL * species, data = dat)
summary(m)
anova(m)
# 交互项显著 → 斜率不同；不显著 → 去掉交互看截距差异
```

### 2.2 混合效应模型

```r
# ========== 混合效应模型首选：glmmTMB ==========
library(glmmTMB)
library(DHARMa)   # 模型诊断
library(performance)  # 模型比较

# 数据：fish, site, year, 重复测量
# 问题：不同处理下体长差异，site 为随机效应
m <- glmmTMB(SL ~ treatment + (1 | site), 
             data = dat, family = gaussian)
summary(m)

# 模型诊断
sim <- simulateResiduals(m)
plot(sim)

# 模型比较（AIC-based）
m_null <- glmmTMB(SL ~ 1 + (1 | site), data = dat, family = gaussian)
m_full <- glmmTMB(SL ~ treatment + (1 | site), data = dat, family = gaussian)
AIC(m_null, m_full)
anova(m_null, m_full)  # LRT

# ========== 零膨胀计数数据（如胃含物计数）==========
m_zip <- glmmTMB(count ~ treatment + (1 | site),
                 ziformula = ~ treatment,  # 零膨胀部分
                 data = dat, family = nbinom2)
```

### 2.3 形态学 PCA + CVA

```r
# ========== 线性测量 PCA ==========
library(tidyverse)

dat <- read_csv("data/morph.csv")
# 列: species, SL, BD, HL, ED, PDL, CPL, ...

# PCA — 仅数值列
pca <- dat %>% 
  select(SL:CPL) %>%               # 所有测量变量
  prcomp(scale. = TRUE)

# 结果
summary(pca)                       # 各轴解释度
pca$rotation[, 1:3]                # 载荷

# Scree plot
tibble(PC = 1:length(pca$sdev), 
       var = pca$sdev^2 / sum(pca$sdev^2)) %>%
  ggplot(aes(PC, var)) + 
  geom_col(fill = "steelblue", alpha = 0.8) +
  geom_line() + geom_point() +
  labs(y = "Proportion of Variance") +
  theme_bw(base_size = 14)

# 可视化
library(ggfortify)
autoplot(pca, data = dat, colour = "species", 
         loadings = TRUE, loadings.label = TRUE)

# ========== 线性判别分析 LDA/CVA ==========
library(MASS)
lda_model <- lda(species ~ SL + BD + HL + ED + PDL + CPL, data = dat)
lda_pred <- predict(lda_model)

# 分类准确率
table(Actual = dat$species, Predicted = lda_pred$class)
mean(lda_pred$class == dat$species)   # 正确率

# 留一交叉验证
lda_cv <- lda(species ~ SL + BD + HL + ED + PDL + CPL, data = dat, CV = TRUE)
table(Actual = dat$species, Predicted = lda_cv$class)

# ========== 地标点形态（geomorph）===========
library(geomorph)
# 读入 TPS 文件
gpa <- gpagen("data/landmarks.tps")
# Procrustes ANOVA
fit <- procD.lm(gpa$coords ~ species, data = dat)
summary(fit)
# 主成分分析
gm.prcomp(gpa$coords)
# CVA
# (需要用分类标签做 CVA — 见 geomorph 文档)
```

### 2.4 稳定同位素 — SIBER

```r
# ========== SIBER — 贝叶斯生态位椭圆 ==========
library(SIBER)

# 数据格式：community, group, d13C, d15N
dat <- read_csv("data/isotopes.csv")
# 列: species = 社区/物种, location = 群体(如季节/地点)
# d13C, d15N

# 准备 SIBER 格式
siber_dat <- createSiberObject(
  list(
    x = dat$d13C,
    y = dat$d15N,
    community = as.numeric(as.factor(dat$location)),  # location 作为 community
    group = as.numeric(as.factor(dat$species))         # species 作为 group
  )
)

# 标准椭圆面积 (SEAc) — 基于协方差
par(mfrow = c(1,1))
plotSiberObject(siber_dat, 
                ax.pad = 2, 
                hulls = FALSE, 
                ellipses = TRUE,
                group.hulls = TRUE, 
                bty = "L")

# 贝叶斯椭圆面积 (SEAb) — MCMC
priors <- list(
  n = 2,
  id = "uninformative",
  mean = rep(0, 2),
  cov = diag(rep(1, 2)),
  k = 2
)

# 运行 MCMC（行数根据数据量调整）
ellipse_mcmc <- siberMVN(siber_dat, 
                          parms = priors, 
                          n.iter = 20000, 
                          n.burnin = 5000)

# 提取各群体椭圆面积
group_areas <- siberEllipseArea(ellipse_mcmc, siber_dat)

# 计算椭圆重叠
# 调用 maxLikOverlap / bayesianOverlap
```

### 2.5 群落分析 NMDS + PERMANOVA

```r
# ========== NMDS + PERMANOVA ==========
library(vegan)
library(tidyverse)

# 数据
com <- read_csv("data/community.csv")    # species × site（宽表）
env <- read_csv("data/environment.csv")  # site 对应环境/分组

# NMDS
nmds <- metaMDS(com, distance = "bray", try = 100)

# 压力值
nmds$stress   # < 0.10 优秀, < 0.15 良好, < 0.20 可用

# 可视化
scores(nmds) %>% 
  as_tibble(rownames = "site") %>%
  left_join(env) %>%
  ggplot(aes(NMDS1, NMDS2, color = group)) +
  geom_point(size = 3) +
  stat_ellipse() +
  theme_bw(base_size = 14)

# 拟合环境因子
ef <- envfit(nmds, env[, c("temp", "DO", "salinity")], permutations = 999)
ef
plot(ef)  # 添加到 NMDS 图

# ========== PERMANOVA ==========
adonis2(com ~ group, data = env, permutations = 999, method = "bray")
# 显著 → 组间群落差异

# 配对 PERMANOVA
pairwise.adonis <- function(x, factors, ...) {
  # 手写辅助函数：对所有组对跑 adonis
  comb <- combn(unique(factors), 2)
  out <- data.frame()
  for(i in 1:ncol(comb)) {
    idx <- factors %in% comb[, i]
    sub <- adonis2(x[idx, ] ~ factors[idx], ...)
    out <- rbind(out, data.frame(
      pair = paste(comb[1,i], "vs", comb[2,i]),
      R2 = sub$R2[1],
      p = sub$`Pr(>F)`[1]
    ))
  }
  out$p_adjusted <- p.adjust(out$p, "fdr")
  out
}
pairwise.adonis(com, env$group, permutations = 999, method = "bray")
```

### 2.6 遗传学 DAPC + Fst

```r
# ========== DAPC ==========
library(adegenet)
library(vcfR)

# 从 VCF 读入
vcf <- read.vcfR("data/snps.vcf")
gl <- vcfR2genlight(vcf)

# PCA 预览
pca <- glPca(gl, nf = 10)
scatter(pca, posi = "bottomright")

# 交叉验证确定最优 PC 数
xval <- xvalDapc(tab(gl), pop(gl), n.pca = 5:30, 
                  n.rep = 10, parallel = "multicore",
                  training.set = 0.9)
dapc_model <- xval$DAPC

# 可视化
scatter(dapc_model, scree.da = FALSE, legend = TRUE)

# ========== Fst (Weir & Cockerham) ==========
library(hierfstat)
# 从 genind 对象计算
gi <- gl2genind(gl)   # genlight → genind
fst <- pairwise.WCfst(gi)
fst

# 热图
library(pheatmap)
pheatmap(fst)

# ========== AMOVA ==========
library(poppr)
# 需要层次分组（群体 / 区域等）
strata(gi) <- data.frame(pop = pop(gi), region = ...)
amova_result <- poppr.amova(gi, ~region/pop, cutoff = 0.5)
amova_result
```

### 2.7 物种分布模型（SDM）

```r
# ========== MaxEnt (ENMeval) ==========
# 注意：maxent.jar 需要单独下载，放入 java/ 目录
library(ENMeval)

# 数据
occ <- read_csv("data/occurrences.csv")  # 列: species, lon, lat
bioclim <- stack(list.files("data/env/", pattern = ".tif$", full = TRUE))

# 调参
enmeval_result <- ENMevaluate(
  occ = occ[, c("lon", "lat")],
  env = bioclim,
  method = "block",          # 空间分块
  fc = c("L", "LQ", "H"),   # 特征组合
  rm = 1:4,                  # 正则化乘子
  n.bg = 10000,
  algorithm = "maxent.jar"
)

# 选最优模型（AICc 最低）
enmeval_result@results %>% arrange(delta.AICc) %>% head(10)

# 预测
best_model <- enmeval_result@models[[1]]
pred <- predict(best_model, bioclim)

# 变量重要性
plot(enmeval_result, type = "variable.importance")

# ========== maxnet（纯 R，不依赖 Java）===========
library(maxnet)
library(dismo)

# 背景点
bg <- randomPoints(bioclim, 10000)
pres_abs <- c(rep(1, nrow(occ)), rep(0, nrow(bg)))
env_data <- rbind(
  raster::extract(bioclim, occ[, c("lon", "lat")]),
  raster::extract(bioclim, bg)
)

m <- maxnet(pres_abs, env_data, maxnet.formula(pres_abs, env_data, classes = "lq"))
plot(m, type = "cloglog")
```

### 2.8 环境因子 RDA / CCA

```r
# ========== RDA（冗余分析）===========
library(vegan)

# 物种矩阵 (Hellinger 转换 — 推荐)
com_hel <- decostand(com, method = "hellinger")

# RDA
rda_model <- rda(com_hel ~ temp + DO + pH + depth, data = env)
summary(rda_model)

# 方差分解
RsquareAdj(rda_model)
anova(rda_model)       # 整体显著性
anova(rda_model, by = "terms")  # 各变量显著性
anova(rda_model, by = "axis")   # 各排序轴显著性

# 可视化
plot(rda_model)
# ggplot 版
library(ggvegan)
autoplot(rda_model)

# ========== CCA（对应分析，适合单峰响应）===========
cca_model <- cca(com ~ temp + DO + pH + depth, data = env, scale = TRUE)
anova(cca_model, by = "terms")

# ========== 方差分解 (VPA) ============
# 例如：环境变量分成两组：理化 (phys) 和 空间 (space)
rda_phys <- rda(com_hel ~ temp + DO, data = env, scale = TRUE)
rda_space <- rda(com_hel ~ lat + lon, data = env, scale = TRUE)
rda_both <- rda(com_hel ~ temp + DO + lat + lon, data = env, scale = TRUE)

# 手动计算各组分 R²
R2_phys_only <- RsquareAdj(rda_phys)$adj.r.squared
R2_space_only <- RsquareAdj(rda_space)$adj.r.squared
R2_both <- RsquareAdj(rda_both)$adj.r.squared
R2_shared <- R2_phys_only + R2_space_only - R2_both

# 或用 varpart()
varpart(com_hel, ~ temp + DO, ~ lat + lon, data = env)
```

### 2.9 食性分析

```r
# ========== 胃含物分析 ==========
library(vegan)
library(tidyverse)

# 数据: species, prey_item, count / volume / frequency
dat <- read_csv("data/diet.csv")

# 转为物种×猎物矩阵
diet_mat <- dat %>%
  pivot_wider(names_from = prey_item, values_from = count, values_fill = 0) %>%
  column_to_rownames("sample_id") %>%
  select(-species)

# 营养生态位宽度
# 标准化 Levins 指数
diet_mat %>% 
  apply(1, function(x) {
    p <- x / sum(x)
    1 / sum(p^2)  # Levins
  })

# NMDS + PERMANOVA（同群落分析模板）
nmds_diet <- metaMDS(diet_mat, distance = "bray")
adonis2(diet_mat ~ dat$species, permutations = 999)

# 指示种（指示猎物）
library(indicspecies)
indval <- multipatt(diet_mat, dat$species, func = "IndVal.g")
summary(indval)

# ========== 食性重叠 ==========
# Pianka 指数
nicheOverlap(diet_mat, method = "pianka")
```

---

## 3. 样本量 / 检验效力

```r
# ========== 功效分析 ==========
library(pwr)

# t-test: 检测 d = 0.8 效应量，α = 0.05，power = 0.8
pwr.t.test(d = 0.8, sig.level = 0.05, power = 0.8, type = "two.sample")

# ANOVA: k = 4 组，f = 0.4（大效应）
pwr.anova.test(k = 4, f = 0.4, sig.level = 0.05, power = 0.8)

# ========== 经验法则 ==========
# t-test: 每组 ≥ 10（参数），≥ 6（非参数）
# ANOVA: 每组 ≥ 10-15
# PERMANOVA: 每组 ≥ 5（总样本 ≥ 20）
# PCA: 样本量 ≥ 变量数 × 5
# DAPC: 每组 ≥ 10（SNP 数据）
# SDM: 物种点 ≥ 30（最好 ≥ 50）
```

---

## 4. 常见坑

| 坑 | 表现 | 正确做法 |
|:---|:-----|:---------|
| 多重比较不做校正 | 大量假阳性 | `p.adjust()` / `TukeyHSD()` / `fdr` |
| Manly 检验用错 | 群落零模型误用 | PERMANOVA 前提是 **多元同质散布** → `betadisper()` 先检查 |
| PCA 不做标准化 | 大尺度变量主导 | `prcomp(scale. = TRUE)` |
| 方差齐性忽略 | t-test/ANOVA 假阳性 | `leveneTest()` / `bartlett.test()` 先检查 |
| glmmTMB 模型不收敛 | 警告 | 缩放变量 `scale()` / 改优化器 `control = glmmTMBControl(optimizer = nlminb)` |
| NMDS 压力值不看 | 结果不可靠 | stress < 0.15 才解读，否则加维度 `k=3` |
| SDM 不做空间分块 | 模型过拟合 | `ENMeval` 的 `method = "block"` / `"checkerboard"` |
| 零膨胀模型用 Poisson | 过离散 | `nbinom2` / `nbinom1` 族，不行再用 ZIP/ZINB |
| 同位素太小样本 | 椭圆不可靠 | SIBER 每组 ≥ 10 个体 |
| 遗传 PCA 不做 LD prune | SNP 连锁干扰 | `snpgdsLDpruning()` |

---

## 5. 推荐参考书 & 文献

### 教科书

| 领域 | 书名 | 作者 | 备注 |
|:-----|:-----|:-----|:-----|
| 生态统计 | *Ecological Models and Data in R* | Bolker | 入门综合，代码翔实 |
| 混合模型 | *Mixed Effects Models and Extensions in Ecology with R* | Zuur et al. | Zuur 系列必修 |
| 多元分析 | *Numerical Ecology* (3rd ed.) | Legendre & Legendre | 多元生态圣经 |
| 群落生态 | *Multivariate Analysis of Ecological Communities* | Digby & Kempton | 入门 |
| 形态测量 | *Morphometrics with R* | Claude | geomorph 实操 |
| 遗传学 | *Population Genetics in R* | Kamvar et al. | adegenet + poppr |
| 同位素 | *Stable Isotope Ecology* | Fry | 基础理论 |
| SDM | *Species Distribution Modeling* | Franklin | MaxEnt 背景 |

### 关键论文

| 方法 | 关键文献 |
|:-----|:---------|
| SIBER | Jackson et al. (2011) *J Anim Ecol* — SIBER 框架 |
| glmmTMB | Brooks et al. (2017) *R Journal* — glmmTMB 包 |
| ENMeval | Muscarella et al. (2014) *Ecography* — SDM 调参 |
| Procrustes ANOVA | Adams & Otárola-Castillo (2013) *MEPS* — geomorph |
| DAPC | Jombart et al. (2010) *BMC Genetics* — 判别分析 |
| PERMANOVA | Anderson (2001) *Austral Ecology* — 多元置换检验 |
| betadisper | Anderson (2006) *Biometrics* — 多元同质散布 |

---

## 6. 附录：包版本 & 安装备忘

```r
# ========== 包版本记录（当前验证过的版本）===========
# 安装后，用这里记录的版本确保可复现
# glmmTMB     → 1.1.10+
# vegan       → 2.6-4+
# geomorph    → 4.0+
# SIBER       → 2.1.6+
# adegenet    → 2.1.10+
# poppr       → 2.9.6+
# ENMeval     → 2.0.5+
# maxnet      → 0.1.4+
# DHARMa      → 0.4.6+
# performance → 0.12+

# ========== 常用安装 ==========
install.packages(c("tidyverse", "vegan", "glmmTMB", "DHARMa",
                   "performance", "geomorph", "SIBER", "pwr"))

# 遗传学包 (BiocManager)
if (!require("BiocManager", quietly = TRUE)) install.packages("BiocManager")
BiocManager::install(c("adegenet", "poppr", "vcfR", "SNPRelate"))

# SDM 包
install.packages(c("maxnet", "dismo", "raster", "ENMeval"))
```

---

## 📝 验证记录（按时间倒序）

| 日期 | 章节 | 包版本 | 验证方式 | 结果 | 验证人 |
|:----|:-----|:-------|:---------|:-----|:-------|
| — | 全部 | — | — | 待验证 | — |

> **验证方式说明**：
> - **CRAN vignette** → 比对 R 包官方 vignette 或 `?function` 文档
> - **CRAN Task View** → 对照 CRAN Task View 推荐写法
> - **期刊论文** → 对照方法学原始论文（如 SIBER → Jackson 2011）
> - **实际运行** → `coderunner` 跑一次确认输出合理
> - **社区验证** → Stack Overflow / RStudio Community 有多个确认帖

### 如何验证一章？

```r
# 通用验证步骤：

# 1. 确认当前包版本
packageVersion("glmmTMB")

# 2. 查看官方文档
??glmmTMB
# 或：browseVignettes("glmmTMB")  # 在线看

# 3. 运行手册代码 + 比对输出
# 4. 检查函数是否 deprecated:
#    package:function  → CRAN NEWS / pkg NEWS
# 5. 更新手册 + 改日期
```

### 谁来做验证？

- **你主动发现** → 用了某章代码发现报错 → 顺手验证 + 修正
- **智能体代劳** → 调用 `验证手册章节` 技能 → 自动搜索 CRAN / vignette / 论文比对
- **定期批量** → 每 3-6 个月跑一遍验证流程<br>（可以用 `research` 或 `explore` 技能批量查各包的当前版本和更新记录）
```
