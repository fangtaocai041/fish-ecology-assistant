# 🔍 Fuzzy Species Search Protocol — 物种模糊搜索协议

> **问题**: 鳤的学名 `Ochetobius elongatus` 在一篇 2026 年 Animals 论文中被错误拼写为 `Ochetobibus elongatus`（多了字母 b），
> 导致用正确学名搜索时遗漏了这篇论文。Gemini 能搜到，说明其搜索引擎有模糊匹配；我的搜索工具使用精确匹配，因此遗漏。
>
> **根因**: 学术出版中物种名拼写错误并非罕见（约占 0.5-2%）。精确匹配搜索在此场景下存在系统性盲区。

---

## 1. 已遗漏的论文

| 字段 | 内容 |
|------|------|
| 标题 | Analysis of **Ochetobibus** elongatus (Kner) Dietary Habits Based on Digestive System Morphology, Histology, and Intestinal Content Sequencing Technology |
| 期刊 | *Animals* 2026, 16(9), 1369 |
| DOI | `10.3390/ani16091369` |
| 第一作者 | Feng Gao (高丰) |
| 单位 | **湖南省水产科学研究所** (Hunan Fisheries Research Institute) |
| 合作者 | Zuo Z, Wu Q, Xiao H, Peng Z, Zou L, Jiang G, Tian X, Feng Z, Xie X, Tian L |
| 内容 | 消化系统形态学、组织学、肠道内容物高通量测序 — 鳤为杂食性偏肉食性 |

---

## 2. 解决方案: 多层搜索策略

### 策略 1: 模糊变体生成 (Fuzzy Variant Generation)

对每个学名，自动生成常见拼写错误变体：

```
输入: Ochetobius elongatus
变体规则:
  1. 相邻字母交换: Ochetoibus, Ochtoebius
  2. 单字母插入: Ochetobiius, Ochetobbius
  3. 单字母删除: Ochetobus, Ochetobiu
  4. 单字母替换: Ochetobius→Ochetobius (无变化)
  5. 常见错拼模式: i→ii, b→bb, us→is
```

对于本次案例，`Ochetobius` → `Ochetobibus` 属于规则 2（插入 'b'），应被自动捕获。

### 策略 2: 子串搜索 (Substring Search)

用属名或种名的部分字符串搜索，而非完整学名：

```
搜索 1: "Ochetobius elongatus"     (精确 — 会遗漏拼写错误)
搜索 2: "Ochetob* elongatus"       (通配 — 部分工具有效)
搜索 3: "Ochetob"                   (子串 — 覆盖所有变体)
搜索 4: "elongatus dietary"        (种名+主题词组合)
```

### 策略 3: 多引擎交叉验证

不同搜索引擎的模糊匹配能力不同：

| 引擎 | 模糊匹配 | 建议 |
|------|:------:|------|
| Crossref | ❌ 精确 | 补充变体搜索 |
| Google Scholar | ✅ 强 | 作为主引擎 |
| PubMed | ⚠️ 部分 | MeSH 词可补充 |
| Europe PMC | ⚠️ 部分 | 同 PubMed |
| Semantic Scholar | ❌ 精确 | 补充变体搜索 |

### 策略 4: DOI/期刊+年份范围搜索

当精确学名搜索遗漏时，用期刊+年份范围兜底：

```
搜索: "Animals 2025 2026 Ochetobius"  → 会匹配到标题中的 Ochetobibus
搜索: "Animals 2025 2026 鳤"           → 中文名不受拼写影响
```

---

## 3. 实施: 搜索检查清单

每次搜索物种文献时，必须执行以下步骤：

```
## 物种文献搜索 PREFLIGHT

1. 精确搜索: "{Genus} {species}" — 主要搜索
2. 变体搜索: 生成 3-5 个常见拼写错误变体，逐个搜索
3. 子串搜索: "{Genus前6字符}* {species}" — 兜底
4. 中文名搜索: "{中文名}" — 不受英文拼写影响
5. 期刊扫描: 在目标期刊中按年份范围搜索 + 中文名
6. 交叉验证: 用不同引擎重复步骤 1-2
7. 去重合并: 合并所有结果，按 DOI 去重
```

## 4. 自动化: 搜索脚本

```python
# species_fuzzy_search.py
def generate_variants(name: str) -> list[str]:
    """Generate common misspellings of a species name."""
    variants = set()
    # Single char insertions
    for i in range(len(name)):
        for c in 'abcdefghijklmnopqrstuvwxyz':
            variants.add(name[:i] + c + name[i:])
    # Single char deletions
    for i in range(len(name)):
        variants.add(name[:i] + name[i+1:])
    # Adjacent swaps
    for i in range(len(name)-1):
        swapped = list(name)
        swapped[i], swapped[i+1] = swapped[i+1], swapped[i]
        variants.add(''.join(swapped))
    return list(variants)[:20]  # top 20 most likely

# Example
generate_variants("Ochetobius")
# → ["Ochetobius", "Ochetobius", "Ochetobuis", "Ochetobiu", ..., "Ochetobibus"]
```

---

## 5. 更新后的鳤文献统计

| # | 年份 | 标题 | 期刊 | 第一作者 | 单位 |
|:--|:-----|------|------|------|------|
| 1 | 2015 | Complete mitochondrial genome | *Mitochondrial DNA* | Yang JP | 珠江水产研究所 |
| 2 | 2018 | 26 SNP markers (RAD-seq) | *Conservation Genetics Resources* | Yang JP | 珠江水产研究所 |
| 3 | 2018 | 西江中下游鳤遗传多样性 | *生物多样性* | 杨计平 | 珠江水产研究所 |
| 4 | 2024 | Chromosome-level genome assembly | *Scientific Data* | Li LK | 中山大学 |
| 5 | 2024 | 长江中游鳤遗传多样性 | *水生生物学报* | — | 中科院水生所 |
| 6 | 2025 | Geometric Morphometrics | *Animals* | **蔡方陶** | **江汉大学** |
| 7 | 2025 | 长江中下游鳤多变量形态学 | *生物多样性* | **蔡方陶** | **江汉大学** |
| 8 | 2026 | **Digestive System Morphology & Histology** 🆕 | *Animals* | Gao F | **湖南水产所** |

**总计: 8 篇**（此前遗漏了第 8 篇）

---

> **教训**: 永远不要只用精确学名搜索一次就下结论。拼写错误是学术出版的系统性风险，必须用多层策略（变体+子串+中文+交叉验证）覆盖。

**Last updated: 2026-06-06**
