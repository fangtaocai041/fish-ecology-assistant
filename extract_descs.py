#!/usr/bin/env python3
"""从.md知识库生成自包含index.html"""
import os, re, json

BASE = r'D:\Reasonix\fish-ecology-assistant\config\knowledge_base\ecological_theories'

nodes = [
    ('EVO','进化论','cross','1859','Darwin','grand','01_fish_ecology'),
    ('NICHE','生态位理论','terr','1957','Hutchinson','grand','04_terrestrial_ecology/niche_theory.md'),
    ('ISLAND','岛屿生物地理','terr','1967','MacArthur & Wilson','grand','04_terrestrial_ecology/island_biogeography.md'),
    ('SUCC','演替理论','terr','1985','Pickett','grand','04_terrestrial_ecology/succession_theory.md'),
    ('RK','r/K选择','fish','1970','Pianka','grand','01_fish_ecology/rK_selection.md'),
    ('IDH','中度干扰假说','fish','1978','Connell','middle','01_fish_ecology/intermediate_disturbance.md'),
    ('ALT','替代稳态','fresh','2001','Scheffer','middle','02_freshwater_ecology/alternative_stable_states.md'),
    ('RCC','河流连续体','fresh','1980','Vannote','middle','02_freshwater_ecology/river_continuum.md'),
    ('FPC','洪水脉冲','fresh','1989','Junk','middle','02_freshwater_ecology/flood_pulse.md'),
    ('ENV','环境流','fresh','1997','Poff','middle','02_freshwater_ecology/environmental_flows.md'),
    ('HOMOG','生物同质化','fish','2006','Olden','middle','01_fish_ecology/biotic_homogenization.md'),
    ('INV','入侵生物学','fish','1958','Elton','middle','01_fish_ecology/invasion_biology.md'),
    ('META','集合群落','fresh','2004','Leibold','middle','02_freshwater_ecology/metacommunity_theory.md'),
    ('MPOP','集合种群','cons','1999','Hanski','middle','05_conservation_biology/metapopulation.md'),
    ('FISHEVO','捕捞诱导进化','fish','2009','Conover','middle','01_fish_ecology/fishing_induced_evolution.md'),
    ('LEGACY','遗留效应','fish','2011','Cuddington','middle','01_fish_ecology/legacy_effects.md'),
    ('PRIOR','优先效应','cross','2015','Fukami','middle','06_cross_domain_emergence/community_assembly.md'),
    ('FUNCDIV','功能多样性','fish','2021','Su','middle','01_fish_ecology/functional_diversity_fish.md'),
    ('BEF','BEF理论','cross','1997','Tilman','middle','06_cross_domain_emergence/BEF_theory.md'),
    ('KEY','关键种','cross','1966','Paine','middle','06_cross_domain_emergence/keystone_and_engineers.md'),
    ('MIG','洄游理论','fish','1987','Gross','middle','01_fish_ecology/migration_theory.md'),
    ('TROPH','营养级联','cross','1993','Carpenter','middle','06_cross_domain_emergence/topdown_bottomup.md'),
    ('NEUTRAL','中性理论','cross','2001','Hubbell','grand','11_macroecology/neutral_theory.md'),
    ('CONSGEN','保护遗传学','cons','1995','Frankham','middle','05_conservation_biology/conservation_genetics.md'),
    ('PVA','PVA/MVP','cons','1981','Shaffer','middle','05_conservation_biology/population_viability.md'),
    ('REWILD','再野化','cons','2016','Soule','middle','05_conservation_biology/rewilding_theory.md'),
    ('EWS','早期预警','cross','2009','Scheffer','middle','_topology/theory_supplement.md'),
    ('CAS','复杂适应系统','soc','1998','Levin','meta','12_social_ecological/complex_adaptive_systems.md'),
    ('SES','社会生态系统','soc','2009','Ostrom','meta','12_social_ecological/SES_framework.md'),
    ('RESIL','韧性理论','soc','1973','Holling','meta','12_social_ecological/resilience_theory.md'),
    ('ADAPT','适应性管理','soc','1978','Holling','meta','12_social_ecological/adaptive_management.md'),
    ('STORE','保险效应','cross','2010','Schindler','middle','06_cross_domain_emergence/storage_portfolio_effect.md'),
    ('FORAGE','最优觅食','fish','1976','Charnov','middle','01_fish_ecology/optimal_foraging.md'),
    ('ALLEE','Allee效应','cross','1931','Allee','middle','13_behavioural_disease/allee_density.md'),
    ('DILUTE','稀释效应','cross','2010','Ostfeld','middle','13_behavioural_disease/disease_ecology.md'),
    ('WET','湿地洪泛','fresh','1979','Welcomme','middle','10_wetland_ecology/wetland_theory.md'),
    ('MPA','MPA设计','marine','2010','Gaines','middle','03_marine_ecology/marine_protected_areas.md'),
    ('MEGA','淡水巨兽','fresh','2024','He F','middle','_topology/theory_supplement.md'),
    ('DAM','拆坝生态','fresh','2026','Olden','middle','_topology/theory_supplement.md'),
    ('CSR','CSR三角','fish','1977','Grime','middle','01_fish_ecology/csr_life_strategies.md'),
    ('JANZEN','Janzen-Connell','terr','1970','Janzen','middle','04_terrestrial_ecology/janzen_connell.md'),
    ('COMMONS','公地悲剧','soc','1968','Hardin','grand','12_social_ecological/tragedy_of_commons.md'),
    ('TROPH2','营养动力学','fresh','1942','Lindeman','grand','02_freshwater_ecology/trophic_dynamics.md'),
    ('ASSEMBLY','群落构建','cross','1975','Diamond','middle','06_cross_domain_emergence/community_assembly.md'),
    ('BACI','BACI设计','math','1994','Underwood','math','14_mathematical_foundations/BACI_design.md'),
    ('PARADIGM','保护范式','cons','1994','Caughley','middle','05_conservation_biology/caughley_paradigms.md'),
    ('EICA','EICA假说','fish','1995','Blossey','middle','01_fish_ecology/EICA_hypothesis.md'),
    ('FACIL','竞争促进','cross','2003','Bruno','middle','06_cross_domain_emergence/competition_facilitation.md'),
    ('SCALE','空间尺度','cross','1992','Levin','grand','11_macroecology/spatial_scaling.md'),
    ('LV','Lotka-Volterra','math','1925','Lotka','math','14_mathematical_foundations/lotka_volterra.md'),
    ('INFO','信息论','math','1948','Shannon','math','14_mathematical_foundations/information_theory.md'),
    ('GAME','博弈论ESS','math','1973','Maynard Smith','math','14_mathematical_foundations/game_theory_ESS.md'),
    ('NET','网络理论','math','1972','May','math','14_mathematical_foundations/network_theory.md'),
    ('DATA','课题组数据','data','2026','FFRC','data',''),
]

# Read .md summaries
rich_nodes = []
for n in nodes:
    nid,name,dom,year,founder,layer,path = n
    desc = ''
    if path and os.path.isfile(os.path.join(BASE, path)):
        with open(os.path.join(BASE, path), 'r', encoding='utf-8') as f:
            md = f.read()
        # Extract first meaningful paragraphs (skip headers and metadata)
        paragraphs = []
        for line in md.split('\n'):
            line = line.strip()
            if not line or line.startswith('#') or line.startswith('>') or line.startswith('|') or line.startswith('-') or line.startswith('`'):
                continue
            # Clean markdown
            clean = re.sub(r'[#*>`\[\]\(\)]', '', line).strip()
            if len(clean) > 30:
                paragraphs.append(clean)
        desc = ' '.join(paragraphs[:6])[:600]
    if not desc:
        defaults = {
            'EVO': 'Darwin 1859。自然选择。Wallace共同发现。所有生物学理论根基。',
            'CONSGEN': 'Frankham 1995。50/500法则。N_e>=50短期避近交，N_e>=500长期保进化潜力。江豚N_e~250。',
            'MTE': 'Brown 2004。B=B0 M^3/4 e^(-E/kT)。体型+体温→代谢率→宏观生态。',
            'LV': 'Lotka 1925 Volterra 1926。dN/dt=rN-alpha NP。捕食者-猎物振荡。',
            'INFO': 'Shannon 1948。H=-Sigma p_i ln p_i。群落熵。',
            'GAME': 'Maynard Smith 1973。ESS进化稳定策略。鹰鸽博弈。',
            'NET': 'May 1972。稳定性-复杂性悖论。Dunne证明真实食物网更稳健。',
            'DATA': '课题组FFRC淡水中心。22年连续监测·5断面·禁渔BACI·4个T2T基因组·57+SCI·172中文。全球唯一大河完全禁渔前后对比数据。刀鲚·江豚·鳊·鲢·鳙·50+种。',
            'MEGA': 'He F 2024 Biol Rev。>30kg淡水动物=生态系统工程师。江豚恢复→加速生态恢复。',
            'DAM': 'Dolan 2026 Glob Change Biol (Olden参与)。土著/非土著对拆坝响应不同。',
            'EWS': 'Scheffer 2009 Nature。临界减速:临界点前方差增大·自相关增强。',
            'ECOEVO': 'Schoener 2011 Science。生态×进化在相同时间尺度耦合。',
            'STORE': 'Schindler 2010 Nature。Portfolio Effect。异步波动→整体稳定。',
            'TURING': 'Turing 1952。扩散不对称→自发空间斑图。',
            'POWER': 'Bak 1987。自组织临界性SOC。沙堆模型。幂律。',
            'MAXENT': 'Harte 2011。只须总个体+总代谢→精确预测SAD·SAR。',
            'STOICH': 'Sterner & Elser 2002。C:N:P比率驱动食物网。生长率假说。',
        }
        desc = defaults.get(nid, '生态学经典理论。详见知识库对应md文件。')
        desc = defaults.get(nid, '生态学经典理论。详见知识库对应md文件。')
    rich_nodes.append((nid, name, dom, year, founder, layer, desc))

with open(os.path.join(BASE, '_node_data.json'), 'w', encoding='utf-8') as f:
    json.dump(rich_nodes, f, ensure_ascii=False)
print(f'Generated _node_data.json with {len(rich_nodes)} nodes')
print(f'Sample IDH: {rich_nodes[5][6][:100]}...')
