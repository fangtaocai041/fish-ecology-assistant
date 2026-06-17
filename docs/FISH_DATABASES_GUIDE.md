# 全球鱼类性状数据库大全

> 三生万物生态系统 · 数据溯源文档
> 最后更新：2026-06-17

---

## 一、全球综合数据库

### 1. FishBase
| 项目 | 内容 |
|------|------|
| 全称 | FishBase — A Global Information System on Fishes |
| 网址 | https://fishbase.de / https://fishbase.se |
| 创立 | 1990年，Daniel Pauly & Rainer Froese（德国GEOMAR/WorldFish） |
| 规模 | **35,800+ 物种**，33万+ 俗名，6万+ 图片 |
| 数据类型 | 分类、形态（体长/体重/体形）、食性（营养级/食谱）、生活史（寿命/繁殖力）、生长（VBGF参数）、栖息地、保护（IUCN） |
| 更新 | 持续更新，年度发布 |
| 获取 | 网页浏览、rfishbase R包、HTML爬虫 |
| 前世今生 | 1990年作为ICLARM（现WorldFish）项目启动。最初只覆盖200种经济鱼类。2000年后获欧盟资助大幅扩展。2010年起由全球12个镜像站维护。2023年API改版。**是全球鱼类学界的核心基础设施。** |

### 2. FISHMORPH
| 项目 | 内容 |
|------|------|
| 全称 | FISHMORPH — Global Database on Morphological Traits of Freshwater Fishes |
| 网址 | https://freshwaterfish.sedoo.fr/fishmorph |
| 创立 | 2021年，Sebastien Brosse等（法国Paul Sabatier大学） |
| 规模 | **9,534 物种**（占全球淡水鱼73%） |
| 数据类型 | 10项形态比率：体延长比(BEl)、眼径比(REs)、口位(OGp)、体形(BLs)、胸鳍比(PFs)、尾柄比(CPt) |
| 更新 | 首次发布2021，Figshare/Kaggle可下载 |
| 前世今生 | 2021年发表于Global Ecology and Biogeography。基于鱼类侧面照片测量。首次实现全球淡水鱼形态性状标准化。**我们已集成251种。** |

### 3. FishTraits (USGS)
| 项目 | 内容 |
|------|------|
| 全称 | FishTraits — Ecological and Life-history Traits of Freshwater Fishes of the United States |
| 网址 | https://www.usgs.gov |
| 创立 | 2012年，Frimpong & Angermeier（弗吉尼亚理工） |
| 规模 | **809 种** 美国淡水鱼类 |
| 数据类型 | 生态性状+生活史（营养级/食性/寿命/成熟年龄/繁殖力/产卵类型） |
| 前世今生 | 博士项目→USGS发布。填补美国鱼类性状数据库空白。影响了后续全球数据库设计。 |

### 4. Neotropical Freshwater Fish Ecomatrix
| 项目 | 内容 |
|------|------|
| 全称 | An Ecological Trait Matrix of Neotropical Freshwater Fishes |
| 网址 | https://www.nature.com/articles/s41597-025-04674-w |
| 创立 | 2025年，Nature Scientific Data |
| 规模 | **6,345 物种**（全部新热带淡水鱼） |
| 数据类型 | **42项生态性状**：体长/4项水化学/21项物理栖息地/10项食性/6项行为 |
| 前世今生 | 全球最完整的单一生物地理区鱼类性状矩阵。由新热带鱼类学家社区协作完成。**其性状分类框架是我们的参考标准之一。** |

---

## 二、保护与分类数据库

### 5. IUCN Red List
| 项目 | 内容 |
|------|------|
| 网址 | https://iucnredlist.org |
| 创立 | 1964年（物种生存委员会SSC） |
| 规模 | **16万+ 物种**（含~3万鱼类） |
| 数据类型 | 保护等级(EX/EW/CR/EN/VU/NT/LC/DD)、种群趋势、威胁因子 |
| 更新 | 每年2次 |
| 前世今生 | 始于1964年"红皮书"。2000年确立v3.1定量标准。2017年起支持API。**我们430种全部标注。** |

### 6. Eschmeyer Catalog of Fishes
| 项目 | 内容 |
|------|------|
| 网址 | https://www.calacademy.org/scientists/projects/eschmeyers-catalog-of-fishes |
| 创立 | 1998年，William Eschmeyer（加州科学院CAS） |
| 规模 | **~6万 有效种**，全部属级和种级分类 |
| 数据类型 | 接受名→异名映射、命名人、发表年份、模式产地 |
| 更新 | **每日持续更新** |
| 前世今生 | 前身是Eschmeyer 1990年出版的《鱼类属级名录》。1998年数字化。现由CAS维护。**全球鱼类分类最高权威。** |

---

## 三、中国特有数据库

### 7. 中国生物多样性红色名录
| 项目 | 内容 |
|------|------|
| 网址 | https://www.mee.gov.cn |
| 创立 | 2015年（生态环境部+中国科学院） |
| 规模 | **4,357 种** 中国脊椎动物（含内陆鱼类） |
| 更新 | 不定期（2015→2023） |
| 前世今生 | 2015年首次系统评估。2023年更新。**我们430种全部标注。** |

### 8. CNKI / 中国知网
| 项目 | 内容 |
|------|------|
| 网址 | https://cnki.net |
| 创立 | 1999年（清华大学） |
| 规模 | 数千万篇中文学术论文 |
| 数据类型 | 中文鱼类学论文（形态描述、生态调查、性状测量） |
| 前世今生 | 前身1995年《中国学术期刊》。**西方数据库完全不索引CNKI——这是我们独有的优势。** |

---

## 四、专项数据库

### 9. AFORO (耳石)
| 网址 | https://aforo.cmima.csic.es |
| 创立 | 2006年，巴塞罗那海洋科学研究所 |
| 规模 | 2,000+ 物种耳石图像 |
| 数据 | 耳石形态、长度-宽度比、面积、周长 |

### 10. FishSounds
| 网址 | https://fishsounds.net |
| 创立 | 2020年，佛罗里达大学 |
| 规模 | 1,000+ 物种鱼类声学记录 |
| 数据 | 发声类型、频率范围、声谱 |

---

## 五、我们与国际顶尖团队的对比

| 国际标准 | 我们 | 优势/差距 |
|----------|------|-----------|
| FishBase 35,800种 | 长江430种+251FISHMORPH | 范围小但种群级深度大 |
| FISHMORPH 10项形态 | 已导入251种 | ✅ 对齐 |
| Neotropical 42性状 | 61项性状(7大类) | ✅ 超越 |
| FishTraits 生态+生活史 | 食性100%+栖息地100% | ✅ 补齐 |
| IUCN | IUCN+中国红皮书+国家+CITES | ✅ 独家四轨 |
| 种群级性状 | 26条水域标注 | ✅ 全球少有 |
| 分类变化追踪 | 20条+性状冲突分析 | ✅ 创新点 |

---

> 参考文献：Froese & Pauly 2024 / Brosse et al. 2022 / Frimpong & Angermeier 2009 / IUCN 2012 / Fricke et al. 2024 / 生态环境部 2015/2023
