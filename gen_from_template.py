#!/usr/bin/env python3
"""基于三本生态经典合集 index.html 模板，生成理论生命之树"""
import json

# Read reference HTML
with open(r'D:\Reasonix\fish-ecology-assistant\config\knowledge_base\ecological_theories\三本生态经典合集（NEE、BES、ESA生态经典论文）2021.7.2\index.html', 'r', encoding='utf-8') as f:
    template = f.read()

# Read node data
with open(r'D:\Reasonix\fish-ecology-assistant\config\knowledge_base\ecological_theories\_node_data.json', 'r', encoding='utf-8') as f:
    raw_nodes = json.load(f)

# Build theory papers array (same format as ALL_PAPERS)
papers_js = []
for n in raw_nodes:
    nid, name, dom, year, founder, layer, desc = n
    desc = desc.replace('"', '\\"').replace('\n', '\\n')
    if len(desc) < 20:
        defaults = {
            'EVO': 'Darwin 1859。自然选择。Wallace共同发现。所有生物学理论根基。',
            'CONSGEN': 'Frankham 1995。50/500法则。N_e>=50短期避近交。江豚N_e~250。',
            'LV': 'Lotka 1925 Volterra 1926。dN/dt=rN-alpha NP。捕食者-猎物振荡。',
            'INFO': 'Shannon 1948。H=-Sigma p_i ln p_i=群落熵。',
            'GAME': 'Maynard Smith 1973。ESS进化稳定策略。鹰鸽博弈。',
            'NET': 'May 1972。稳定性-复杂性。Dunne真实食物网更稳健。',
            'REWILD': 'Soule & Noss 1998。被动再野化(禁渔)。长江=全球最大被动再野化实验。',
            'MEGA': 'He F 2024 Biol Rev。>30kg淡水动物是生态系统工程师。',
            'DAM': 'Dolan 2026 Glob Change Biol(Olden参与)。土著/非土著对拆坝响应不同。',
            'EWS': 'Scheffer 2009 Nature。临界减速。OBrien 2023 Nature Comms。',
            'ECOEVO': 'Schoener 2011 Science。生态×进化耦合。',
            'STORE': 'Schindler 2010 Nature。Portfolio Effect。',
            'CSR': 'Grime 1977。C竞争S耐压R机会主义。BES#72。',
            'COMMONS': 'Hardin 1968 Science。公地悲剧。长江过度捕捞=教科书案例。',
            'TROPH2': 'Lindeman 1942 Ecology。10%能量传递效率。ESA#01。',
            'ASSEMBLY': 'Diamond 1975。群落构建规则。Connor & Simberloff辩论。',
            'BACI': 'Underwood 1994 Ecol Appl。Beyond BACI。ESA#86。',
            'PARADIGM': 'Caughley 1994 J Anim Ecol。小种群vs下降种群。BES#99。',
            'EICA': 'Blossey 1995 J Ecol。天敌释放→竞争力增强。BES#89。',
            'FACIL': 'Bruno 2003 TREE。竞争+促进双框架。ESA#41。',
            'SCALE': 'Levin 1992 Ecology。格局取决于尺度。ESA#30。',
        }
        desc = defaults.get(nid, f'{name}。{dom}生态学经典理论。{founder}。')

    papers_js.append(f'''{{
        "num": {len(papers_js)+1},
        "title": "{name}",
        "authors": "{founder}",
        "year": {year if year.isdigit() else 'null'},
        "journal": "",
        "source": "{dom}",
        "domain": "{dom}",
        "layer": "{layer}",
        "nodeId": "{nid}",
        "chinese_title": "{desc[:200]}",
        "scholar_url": ""
    }}''')

new_data = '[\n' + ',\n'.join(papers_js) + '\n]'

# Replace the ALL_PAPERS data in template
import re
# Find ALL_PAPERS array and replace
old_data = re.search(r'const ALL_PAPERS = \[.*?\];', template, re.DOTALL)
if old_data:
    template = template[:old_data.start()] + 'const ALL_PAPERS = ' + new_data + ';\n' + template[old_data.end():]

# Replace header title
template = template.replace('🌿 三本生态经典文献合集', '🌳 生态学理论生命之树')
template = template.replace('整合 NEE · BES · ESA 三份百年生态学经典论文清单，构建可探索的学术知识库', '63节点·102连线·15领域 | 生态学理论网络·前世今生·跨域涌现')

# Replace source badges
template = template.replace('NEE · 生态学家必读 100 篇', '鱼类生态')
template = template.replace('BES · 英国生态百年 100 篇', '淡水生态')
template = template.replace('ESA · 美国生态百年 105 篇', '跨域涌现')

# Replace stats
template = template.replace('id="statTotal">305', f'id="statTotal">{len(raw_nodes)}')
template = template.replace('id="statNEE">100', 'id="statFish">12')
template = template.replace('id="statBES">100', 'id="statFresh">10')
template = template.replace('id="statESA">105', 'id="statCross">10')
template = template.replace('id="statDecades">12', 'id="statDomains">9')
template = template.replace('覆盖年代', '理论领域')
template = template.replace('NEE', '鱼类').replace('BES', '淡水').replace('ESA', '涌现')

# Update filter labels  
template = template.replace('data-source="NEE"', 'data-source="fish"')
template = template.replace('data-source="BES"', 'data-source="fresh"') 
template = template.replace('data-source="ESA"', 'data-source="cross"')

# Update footer
template = template.replace('Nature Ecology & Evolution (2017) · British Ecological Society (1913–2013) · Ecological Society of America (1915–2015)',
    '69个.md知识库文件 · build_final.py生成 · 理论生命之树')
template = template.replace('交互式知识库 · 生态学文献探索工具 · 点击卡片展开详情并获取原文链接',
    '生态学理论网络 · 前世今生 · 跨域涌现 · 点击卡片展开详情')

# Update CSS badge colors
template = template.replace('.badge-nee{background:#e8c547;color:#3e3000}', '.badge-fish{background:#1f77b4;color:#fff}')
template = template.replace('.badge-bes{background:#4a90c4;color:#fff}', '.badge-fresh{background:#2ca02c;color:#fff}')
template = template.replace('.badge-esa{background:#c4653a;color:#fff}', '.badge-cross{background:#e377c2;color:#fff}')

template = template.replace('badge-nee','badge-fish').replace('badge-bes','badge-fresh').replace('badge-esa','badge-cross')
template = template.replace('source-nee','source-fish').replace('source-bes','source-fresh').replace('source-esa','source-cross')
template = template.replace('class="card nee"','class="card fish"').replace('class="card bes"','class="card fresh"').replace('class="card esa"','class="card cross"')
template = template.replace('checked-nee','checked-fish').replace('checked-bes','checked-fresh').replace('checked-esa','checked-cross')

# Update graph legend colors
template = template.replace('background:#e8c547"></span> NEE','background:#1f77b4"></span> 鱼类')
template = template.replace('background:#4a90c4"></span> BES','background:#2ca02c"></span> 淡水')
template = template.replace('background:#c4653a"></span> ESA','background:#e377c2"></span> 涌现')

# Fix JS: simplify the filter/card logic for theory domains
template = template.replace('activeSources = { NEE: true, BES: true, ESA: true }',
    'activeSources = { fish: true, fresh: true, terr: true, marine: true, cons: true, cross: true, math: true, soc: true }')

# Update the Y-axis label for decade chart  
template = template.replace("name: '论文数',", "name: '理论数',")
template = template.replace("'论文发表年代分布（按十年统计）'", "'理论诞生年代分布（按十年统计）'")

output_path = r'D:\Reasonix\fish-ecology-assistant\config\knowledge_base\ecological_theories\_topology\index.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(template)
print(f'Generated: {len(template)//1024} KB -> _topology/index.html')
