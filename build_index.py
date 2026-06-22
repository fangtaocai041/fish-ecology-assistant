#!/usr/bin/env python3
"""从 .md 知识库生成 index.html 阅读器"""
import json, os, re
from pathlib import Path

BASE = Path(r'D:\Reasonix\fish-ecology-assistant\config\knowledge_base\ecological_theories')

# ====== 理论索引 (节点+边+文件路径) ======
NODES = [
    # id, 名称, 域, 年份, 创始人, 层级, 关键词
    ("EVO","进化论","cross","1859","Darwin","grand","evolution Darwin natural selection","01_fish_ecology"),
    ("NICHE","生态位理论","terr","1957","Hutchinson","grand","niche Gause competitive exclusion","04_terrestrial_ecology/niche_theory.md"),
    ("ISLAND","岛屿生物地理","terr","1967","MacArthur & Wilson","grand","island biogeography species-area","04_terrestrial_ecology/island_biogeography.md"),
    ("SUCC","演替理论","terr","1985","Clements Gleason Pickett","grand","succession patch dynamics","04_terrestrial_ecology/succession_theory.md"),
    ("RK","r/K选择","fish","1970","Pianka","grand","life history strategy","01_fish_ecology/rK_selection.md"),
    ("IDH","中度干扰假说","fish","1978","Connell","middle","intermediate disturbance Connell","01_fish_ecology/intermediate_disturbance.md"),
    ("ALT","替代稳态","fresh","2001","Scheffer","middle","regime shift tipping point","02_freshwater_ecology/alternative_stable_states.md"),
    ("RCC","河流连续体","fresh","1980","Vannote","middle","river continuum","02_freshwater_ecology/river_continuum.md"),
    ("FPC","洪水脉冲","fresh","1989","Junk","middle","flood pulse floodplain","02_freshwater_ecology/flood_pulse.md"),
    ("ENV","环境流","fresh","1997","Poff","middle","environmental flow","02_freshwater_ecology/environmental_flows.md"),
    ("HOMOG","生物同质化","fish","2006","Olden","middle","biotic homogenization invasion","01_fish_ecology/biotic_homogenization.md"),
    ("INV","入侵生物学","fish","1958","Elton","middle","invasion enemy release","01_fish_ecology/invasion_biology.md"),
    ("META","集合群落","fresh","2004","Leibold","middle","metacommunity dendritic","02_freshwater_ecology/metacommunity_theory.md"),
    ("MPOP","集合种群","cons","1999","Hanski","middle","metapopulation extinction","05_conservation_biology/metapopulation.md"),
    ("FISHEVO","捕捞诱导进化","fish","2009","Conover","middle","fishing-induced evolution harvest","01_fish_ecology/fishing_induced_evolution.md"),
    ("LEGACY","遗留效应","fish","2011","Cuddington","middle","legacy effects ecological memory","01_fish_ecology/legacy_effects.md"),
    ("PRIOR","优先效应","cross","2015","Fukami","middle","priority effects historical","06_cross_domain_emergence/community_assembly.md"),
    ("FUNCDIV","功能多样性","fish","2021","Brosse Su","middle","functional diversity FISHMORPH","01_fish_ecology/functional_diversity_fish.md"),
    ("BEF","BEF理论","cross","1997","Tilman","middle","biodiversity ecosystem function","06_cross_domain_emergence/BEF_theory.md"),
    ("KEY","关键种","cross","1966","Paine","middle","keystone ecosystem engineer","06_cross_domain_emergence/keystone_and_engineers.md"),
    ("MIG","洄游理论","fish","1987","Gross","middle","migration diadromy anadromous","01_fish_ecology/migration_theory.md"),
    ("MCONN","海洋连通性","marine","2000","Cowen","middle","marine connectivity larval","03_marine_ecology/connectivity_theory.md"),
    ("TROPH","营养级联","cross","1993","Carpenter","middle","trophic cascade top-down","06_cross_domain_emergence/topdown_bottomup.md"),
    ("MTE","代谢理论","cross","2004","Brown West Enquist","grand","metabolic theory allometric","11_macroecology/macroecology.md"),
    ("STOICH","化学计量学","cross","2002","Sterner Elser","middle","ecological stoichiometry","11_macroecology/macroecology.md"),
    ("NEUTRAL","中性理论","cross","2001","Hubbell","grand","neutral theory drift dispersal","11_macroecology/neutral_theory.md"),
    ("MAXENT","最大熵METE","cross","2011","Harte","grand","maximum entropy","11_macroecology/maxent_theory.md"),
    ("CONSGEN","保护遗传学","cons","1995","Frankham","middle","conservation genetics bottleneck","05_conservation_biology/conservation_genetics.md"),
    ("PVA","PVA/MVP","cons","1981","Shaffer Lande","middle","population viability MVP","05_conservation_biology/population_viability.md"),
    ("REWILD","再野化","cons","2016","Soule Svenning","middle","rewilding restoration","05_conservation_biology/rewilding_theory.md"),
    ("EWS","早期预警信号","cross","2009","Scheffer","middle","early warning critical slowing","_topology/theory_supplement.md"),
    ("ECOEVO","生态进化动力学","cross","2011","Schoener","middle","eco-evolutionary dynamics","_topology/theory_supplement.md"),
    ("CAS","复杂适应系统","soc","1998","Holland Levin","meta","complex adaptive system emergence","12_social_ecological/complex_adaptive_systems.md"),
    ("SES","社会生态系统","soc","2009","Ostrom","meta","social-ecological commons","12_social_ecological/SES_framework.md"),
    ("PAN","Panarchy","soc","2002","Gunderson Holling","meta","panarchy adaptive cycle","12_social_ecological/resilience_theory.md"),
    ("RESIL","韧性理论","soc","1973","Holling","meta","resilience resistance recovery","12_social_ecological/resilience_theory.md"),
    ("ADAPT","适应性管理","soc","1978","Holling Walters","meta","adaptive management","12_social_ecological/adaptive_management.md"),
    ("STORE","保险效应","cross","2010","Chesson Schindler","middle","portfolio effect insurance","06_cross_domain_emergence/storage_portfolio_effect.md"),
    ("FORAGE","最优觅食","fish","1976","Charnov","middle","optimal foraging marginal","01_fish_ecology/optimal_foraging.md"),
    ("ALLEE","Allee效应","cross","1931","Allee","middle","Allee density dependence","13_behavioural_disease/allee_density.md"),
    ("DILUTE","稀释效应","cross","2010","Ostfeld","middle","dilution effect disease","13_behavioural_disease/disease_ecology.md"),
    ("WET","湿地洪泛","fresh","1979","Welcomme","middle","wetland floodplain nursery","10_wetland_ecology/wetland_theory.md"),
    ("MPA","MPA设计","marine","2010","Gaines Lubchenco","middle","marine protected area","03_marine_ecology/marine_protected_areas.md"),
    ("MEGA","淡水巨型动物","fresh","2024","He F","middle","freshwater megafauna engineer","_topology/theory_supplement.md"),
    ("DAM","拆坝生态","fresh","2026","Olden Dolan","middle","dam removal barrier","_topology/theory_supplement.md"),
    ("CSR","CSR三角","fish","1977","Grime","middle","CSR competitor stress ruderal","01_fish_ecology/csr_life_strategies.md"),
    ("JANZEN","Janzen-Connell","terr","1970","Janzen Connell","middle","density distance dependence","04_terrestrial_ecology/janzen_connell.md"),
    ("COMMONS","公地悲剧","soc","1968","Hardin","grand","tragedy commons overfishing","12_social_ecological/tragedy_of_commons.md"),
    ("TROPH2","营养动力学","fresh","1942","Lindeman","grand","trophic dynamics energy flow","02_freshwater_ecology/trophic_dynamics.md"),
    ("ASSEMBLY","群落构建","cross","1975","Diamond","middle","community assembly rules","06_cross_domain_emergence/community_assembly.md"),
    ("BACI","BACI设计","math","1994","Underwood","math","BACI impact assessment","14_mathematical_foundations/BACI_design.md"),
    ("PARADIGM","保护范式","cons","1994","Caughley","middle","conservation paradigm declining","05_conservation_biology/caughley_paradigms.md"),
    ("EICA","EICA假说","fish","1995","Blossey","middle","evolution increased competitive","01_fish_ecology/EICA_hypothesis.md"),
    ("FACIL","竞争促进","cross","2003","Bruno","middle","competition facilitation","06_cross_domain_emergence/competition_facilitation.md"),
    ("SCALE","空间尺度","cross","1992","Wiens Levin","grand","spatial scaling pattern","11_macroecology/spatial_scaling.md"),
    ("LV","Lotka-Volterra","math","1925","Lotka Volterra","math","Lotka Volterra predator-prey","14_mathematical_foundations/lotka_volterra.md"),
    ("TURING","Turing斑图","math","1952","Turing","math","Turing pattern reaction-diffusion","14_mathematical_foundations/turing_patterns.md"),
    ("INFO","信息论","math","1948","Shannon","math","information theory entropy","14_mathematical_foundations/information_theory.md"),
    ("GAME","博弈论ESS","math","1973","Maynard Smith","math","game theory ESS evolutionarily","14_mathematical_foundations/game_theory_ESS.md"),
    ("POWER","幂律SOC","math","1987","Bak","math","power law self-organized","14_mathematical_foundations/power_laws_SOC.md"),
    ("NET","网络理论","math","1972","May Dunne","math","network food web stability","14_mathematical_foundations/network_theory.md"),
    ("DATA","课题组22年数据","data","2026","FFRC淡水中心","data","课题组 Yangtze fishing ban monitoring",""),
]

EDGES = [
    ("EVO","FISHEVO"),("EVO","CONSGEN"),("EVO","ECOEVO"),
    ("NICHE","HOMOG"),("NICHE","FUNCDIV"),("NICHE","INV"),("NICHE","NEUTRAL"),
    ("ISLAND","MPOP"),("ISLAND","META"),("ISLAND","MPA"),
    ("RK","MIG"),("RK","FISHEVO"),
    ("SUCC","IDH"),("SUCC","ALT"),("SUCC","LEGACY"),("SUCC","PRIOR"),
    ("IDH","ALT"),("IDH","HOMOG"),
    ("RCC","FPC"),("RCC","ENV"),("FPC","WET"),("ENV","DAM"),
    ("HOMOG","INV"),("HOMOG","DAM"),
    ("FISHEVO","LEGACY"),("FISHEVO","ECOEVO"),("LEGACY","PRIOR"),
    ("FUNCDIV","BEF"),("BEF","STORE"),("BEF","STOICH"),
    ("KEY","TROPH"),("KEY","MEGA"),("TROPH","TROPH2"),
    ("MIG","MCONN"),("MCONN","MPA"),
    ("CAS","PAN"),("CAS","SES"),("PAN","RESIL"),
    ("RESIL","ADAPT"),("RESIL","REWILD"),("ADAPT","REWILD"),
    ("MTE","NEUTRAL"),("MTE","MAXENT"),("NEUTRAL","MAXENT"),("NEUTRAL","META"),
    ("ALT","EWS"),("CONSGEN","PVA"),("PVA","MPOP"),("ALLEE","PVA"),("ALLEE","CONSGEN"),
    ("LV","TROPH"),("TURING","META"),("INFO","FUNCDIV"),
    ("GAME","FORAGE"),("NET","TROPH"),("NET","KEY"),("POWER","MTE"),("POWER","NEUTRAL"),
    ("DATA","IDH"),("DATA","HOMOG"),("DATA","FISHEVO"),("DATA","FUNCDIV"),
    ("DATA","MIG"),("DATA","LEGACY"),("DATA","CONSGEN"),("DATA","CAS"),
    ("DATA","COMMONS"),("BACI","DATA"),("PARADIGM","DATA"),
    ("CSR","RK"),("CSR","IDH"),("CSR","SUCC"),
    ("JANZEN","NEUTRAL"),("JANZEN","DILUTE"),("JANZEN","PRIOR"),
    ("COMMONS","SES"),("COMMONS","ADAPT"),
    ("TROPH2","TROPH"),("TROPH2","STOICH"),("TROPH2","BEF"),
    ("ASSEMBLY","PRIOR"),("ASSEMBLY","NEUTRAL"),("ASSEMBLY","NICHE"),("ASSEMBLY","ISLAND"),
    ("BACI","EWS"),
    ("PARADIGM","CONSGEN"),("PARADIGM","PVA"),("PARADIGM","REWILD"),
    ("EICA","INV"),("EICA","HOMOG"),("EICA","FISHEVO"),
    ("FACIL","NICHE"),("FACIL","KEY"),("FACIL","SUCC"),
    ("SCALE","META"),("SCALE","RCC"),("SCALE","ISLAND"),("SCALE","NEUTRAL"),
    ("SCALE","RCC"),("SCALE","ISLAND"),("SCALE","NEUTRAL"),  # duplicate from above removed in JS
]

DOMAINS = {"fish":"鱼类生态","fresh":"淡水生态","terr":"陆地生态","marine":"海洋生态","cons":"保护生物","cross":"跨域涌现","math":"数学根基","soc":"社会生态","data":"数据层"}
COLORS = {"fish":"#1f77b4","fresh":"#2ca02c","terr":"#ff7f0e","marine":"#17becf","cons":"#d62728","cross":"#e377c2","math":"#9467bd","soc":"#8c564b","data":"#f0f0f0"}

# ====== 生成 HTML ======
nodes_js = ",\n".join(f'{{i:"{n[0]}",n:"{n[1]}",d:"{n[2]}",y:"{n[3]}",f:"{n[4]}",l:"{n[5]}",k:"{n[6]}",p:"{n[7]}"}}' for n in NODES)
edges_js = ",\n".join(f'["{e[0]}","{e[1]}"]' for e in EDGES)
domains_js = json.dumps(DOMAINS, ensure_ascii=False)
colors_js = json.dumps(COLORS, ensure_ascii=False)

html = f'''<!DOCTYPE html><html lang="zh"><head><meta charset="UTF-8"><title>理论生命之树</title>
<style>
:root{{--bg:#0d1117;--card:#161b22;--bdr:#30363d;--blu:#58a6ff;--txt:#c9d1d9;--dim:#8b949e}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:system-ui,sans-serif;background:var(--bg);color:var(--txt);height:100vh;display:flex}}
#L{{width:320px;min-width:180px;background:var(--card);border-right:1px solid var(--bdr);display:flex;flex-direction:column;height:100vh;position:relative}}
#LH{{padding:10px 12px;border-bottom:1px solid var(--bdr);flex-shrink:0}}
#LH h1{{font-size:14px;color:var(--blu);margin-bottom:4px}}
#q{{width:100%;background:var(--bg);border:1px solid var(--bdr);border-radius:5px;padding:6px 8px;color:var(--txt);font-size:11px;outline:none}}
#q:focus{{border-color:var(--blu)}}
#tabs{{display:flex;padding:3px 6px;gap:2px;border-bottom:1px solid var(--bdr);overflow-x:auto;flex-shrink:0;font-size:9px}}
.tb{{padding:2px 6px;border-radius:3px;cursor:pointer;color:var(--dim);border:1px solid transparent;white-space:nowrap}}
.tb:hover,.tb.on{{color:var(--blu);border-color:var(--blu)44;background:#1f6feb18}}
#nav{{flex:1;overflow-y:auto;padding:2px 4px}}
.ni{{display:flex;align-items:center;padding:4px 6px;border-radius:3px;cursor:pointer;font-size:10px;gap:4px;border-left:2px solid transparent;margin:1px 0}}
.ni:hover{{background:#1f6feb11}}
.ni.sel{{background:#1f6feb18;border-left-color:var(--blu)}}
.dt{{width:5px;height:5px;border-radius:50%;flex-shrink:0}}
.nm{{flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}}
#resize{{position:absolute;right:-3px;top:0;width:6px;height:100%;cursor:col-resize;z-index:20}}
#resize:hover{{background:var(--blu)}}
#R{{flex:1;position:relative;overflow:hidden}}
#mode{{position:absolute;top:8px;left:50%;transform:translateX(-50%);display:flex;gap:3px;z-index:10;background:var(--card);border:1px solid var(--bdr);border-radius:6px;padding:2px}}
.mb{{padding:3px 10px;border-radius:4px;font-size:10px;cursor:pointer;color:var(--dim)}}
.mb.on{{background:var(--blu);color:#fff}}
#reader,#graph{{position:absolute;top:0;left:0;width:100%;height:100%;overflow-y:auto;display:none}}
#reader.on,#graph.on{{display:block}}
#reader{{padding:24px 32px;line-height:1.75;font-size:.95em}}
#reader h1{{font-size:1.4em;color:var(--blu)}}
#reader h2{{font-size:1.1em;color:var(--blu);margin:20px 0 8px;padding-bottom:4px;border-bottom:1px solid var(--bdr)}}
#reader h3{{font-size:1em;color:var(--txt);margin:14px 0 4px}}
#reader p,#reader li{{margin:4px 0}}
#reader table{{width:100%;border-collapse:collapse;margin:8px 0;font-size:11px}}
#reader td,#reader th{{border:1px solid var(--bdr);padding:4px 8px}}
#reader th{{background:var(--card);color:var(--blu)}}
#reader code{{background:var(--card);padding:1px 4px;border-radius:3px;font-size:11px}}
#reader pre{{background:var(--card);padding:8px;border-radius:5px;font-size:11px;overflow-x:auto}}
#reader blockquote{{border-left:3px solid var(--blu);padding:2px 0 2px 12px;color:var(--dim);margin:8px 0}}
#reader strong{{color:var(--txt);font-weight:700}}
.bar{{display:flex;gap:4px;flex-wrap:wrap;margin-bottom:10px}}
.tg{{padding:1px 6px;border-radius:8px;font-size:9px;border:1px solid var(--bdr)}}
.cn{{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:3px;margin-top:6px}}
.cc{{background:var(--card);border:1px solid var(--bdr);border-radius:5px;padding:6px 8px;cursor:pointer;font-size:10px}}
.cc:hover{{border-color:var(--blu)}}
.cc b{{color:var(--txt);font-size:11px}}
.cc s{{color:var(--dim);font-size:8px;display:block}}
#graph canvas{{display:block}}
.hint{{position:absolute;bottom:36px;left:50%;transform:translateX(-50%);color:var(--dim);font-size:9px;pointer-events:none}}
.ctrls{{position:absolute;bottom:4px;right:4px;display:flex;gap:2px}}
.cb{{width:24px;height:24px;border-radius:4px;background:var(--card);border:1px solid var(--bdr);color:var(--txt);cursor:pointer;font-size:12px;display:flex;align-items:center;justify-content:center}}
.cb:hover{{border-color:var(--blu)}}
#tt{{position:absolute;background:var(--card);border:1px solid var(--blu);border-radius:6px;padding:6px 10px;font-size:10px;pointer-events:none;opacity:0;transition:opacity .15s;max-width:220px;z-index:20}}
#tt b{{color:var(--blu);font-size:11px}}
#tt i{{color:var(--dim);font-style:normal;font-size:9px;display:block;margin-top:2px}}
#thm{{display:flex;gap:3px;margin-top:4px}}
.thd{{width:12px;height:12px;border-radius:50%;cursor:pointer;border:2px solid transparent}}
.thd:hover{{border-color:var(--txt)}}
.thd.on{{border-color:var(--blu)}}
</style></head><body>
<div id="L"><div id="resize"></div>
<div id="LH"><h1>理论生命之树</h1>
<div id="thm"><span class="thd on" data-t="dark" style="background:#0d1117"></span><span class="thd" data-t="light" style="background:#faf8f5"></span><span class="thd" data-t="sepia" style="background:#f4ecd8"></span><span class="thd" data-t="forest" style="background:#0d2818"></span><span class="thd" data-t="ocean" style="background:#0c1929"></span></div>
<input id="q" placeholder="搜索..."></div>
<div id="tabs"></div><div id="nav"></div></div>
<div id="R"><div id="mode"><span class="mb on" data-m="read">阅读</span><span class="mb" data-m="graph">图谱</span></div>
<div id="reader" class="on"><p style="text-align:center;color:var(--dim);margin-top:40%">点击左侧理论开始阅读<br>或切换到图谱模式</p></div>
<div id="graph"><canvas id="gc"></canvas><div class="hint">滚轮缩放·拖拽·点击节点</div><div class="ctrls"><span class="cb" onclick="GZ(1.3)">+</span><span class="cb" onclick="GZ(.75)">-</span><span class="cb" onclick="GR()">R</span></div></div>
<div id="tt"><b id="ttn"></b><i id="ttb"></i></div></div>
<script>
var D=[{nodes_js}];
var DOM={domains_js};
var C={colors_js};
var A={{}};
[{edges_js}].forEach(function(e){{if(!A[e[0]])A[e[0]]=[];A[e[0]].push(e[1]);if(!A[e[1]])A[e[1]]=[];A[e[1]].push(e[0])}});
var sel=null,tab="all",gMode="read";
function rn(){{
var f=D;if(tab!="all")f=f.filter(function(x){{return x.d==tab}});
var q=document.getElementById("q").value.toLowerCase();
if(q)f=f.filter(function(x){{return x.k.toLowerCase().indexOf(q)>-1||x.n.indexOf(q)>-1||x.f.indexOf(q)>-1}});
var h="",ld="";f.forEach(function(n){{
if(n.d!=ld){{ld=n.d;h+='<div style="padding:6px 8px 2px;font-size:8px;color:var(--dim)">'+ (DOM[n.d]||n.d) +'</div>'}}
h+='<div class="ni'+(sel&&sel.i==n.i?" sel":"")+'" onclick="go(\\''+n.i+'\\')"><span class="dt" style="background:'+(C[n.d]||"#ccc")+'"></span><span class="nm">'+n.n+'</span></div>';
}});
document.getElementById("nav").innerHTML=h||'<div style="padding:16px;color:var(--dim);font-size:10px;text-align:center">无匹配</div>';
}}
function go(id){{
sel=D.find(function(x){{return x.i==id}});if(!sel)return;
var h='<h1>'+sel.n+'</h1><div class="bar"><span class="tg" style="color:'+(C[sel.d]||"#ccc")+'">'+(DOM[sel.d]||sel.d)+'</span><span class="tg">'+sel.y+'</span><span class="tg">'+sel.f+'</span></div>';
if(sel.p){{h+='<div id="mdContent" style="margin:12px 0">加载中...</div>';
fetch(sel.p).then(function(r){{return r.text()}}).then(function(md){{document.getElementById("mdContent").innerHTML=renderMD(md)}}).catch(function(){{document.getElementById("mdContent").innerHTML='<p style="color:var(--dim)">(理论文件: '+sel.p+')</p>'}});
}}else{{h+='<p style="color:var(--dim)">课题组·FFRC淡水中心·22年监测·5断面·4个T2T基因组·全球唯一大河禁渔前后对比数据。</p>'}}
var cs=A[sel.i]||[];
if(cs.length){{h+='<h2>连接理论 ('+cs.length+')</h2><div class="cn">';
cs.forEach(function(cid){{var cn=D.find(function(x){{return x.i==cid}});if(cn)h+='<div class="cc" onclick="go(\\''+cn.i+'\\')"><b>'+cn.n+'</b><s>'+cn.y+' '+cn.f+'</s></div>'}});
h+='</div>';}}
document.getElementById("reader").innerHTML=h;document.getElementById("reader").scrollTop=0;
document.querySelectorAll(".mb").forEach(function(x){{x.classList.remove("on")}});
document.querySelector(".mb[data-m='read']").classList.add("on");
document.getElementById("reader").classList.add("on");document.getElementById("graph").classList.remove("on");
gMode="read";rn();
}}
function renderMD(md){{
var h=md.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
h=h.replace(/^### (.+)/gm,'<h3>$1</h3>');h=h.replace(/^## (.+)/gm,'<h2>$1</h2>');h=h.replace(/^# (.+)/gm,'<h1>$1</h1>');
h=h.replace(/\\*\\*(.+?)\\*\\*/g,'<strong>$1</strong>');h=h.replace(/\\*(.+?)\\*/g,'<i>$1</i>');
h=h.replace(/`([^`]+)`/g,'<code>$1</code>');h=h.replace(/^> (.+)/gm,'<blockquote>$1</blockquote>');
h=h.replace(/^---/gm,'<hr>');
var lines=h.split('\\n'),inTable=false,tableHtml='',out='';
for(var i=0;i<lines.length;i++){{
var l=lines[i];
if(l.startsWith('|')&&l.endsWith('|')){{
if(!inTable){{inTable=true;tableHtml='<table>'}}
var cells=l.split('|').filter(function(c){{return c.trim()}});
var isSep=cells.every(function(c){{return /^[-:\\s]+$/.test(c)}});
if(isSep){{tableHtml+='</thead><tbody>';continue}}
var tag=inTable&&!tableHtml.includes('<thead>')?'th':'td';
tableHtml+='<tr>'+cells.map(function(c){{return '<'+tag+'>'+c.trim()+'</'+tag+'>'}}).join('')+'</tr>';
if(!tableHtml.includes('<thead>'))tableHtml=tableHtml.replace('<table>','<table><thead>');
}}else{{if(inTable){{inTable=false;out+=tableHtml+'</tbody></table>\\n';tableHtml=''}}out+=l+'\\n'}}
}}
if(inTable)out+=tableHtml+'</tbody></table>\\n';h=out;
h=h.replace(/```([\\s\\S]*?)```/g,'<pre><code>$1</code></pre>');
h=h.replace(/^- (.+)/gm,'<li>$1</li>');h=h.replace(/((?:<li>.*<\\/li>\\n?)+)/g,'<ul>$1</ul>');
h=h.replace(/\\[([^\\]]+)\\]\\(([^)]+)\\)/g,'<a href="$2" target="_blank">$1</a>');
return h.replace(/\\n\\n/g,'<br><br>').replace(/\\n/g,'<br>');
}}
document.getElementById("q").oninput=rn;
var tabs='<span class="tb on" data-d="all">全部</span>';
["fish","fresh","terr","marine","cons","cross","math","soc","data"].forEach(function(d){{var c=D.filter(function(x){{return x.d==d}}).length;if(c)tabs+='<span class="tb" data-d="'+d+'">'+(DOM[d]||d)+'('+c+')</span>'}});
document.getElementById("tabs").innerHTML=tabs;
document.getElementById("tabs").onclick=function(e){{if(e.target.classList.contains("tb")){{tab=e.target.dataset.d;document.querySelectorAll(".tb").forEach(function(x){{x.classList.remove("on")}});e.target.classList.add("on");rn()}}}};
document.getElementById("mode").onclick=function(e){{if(!e.target.classList.contains("mb"))return;gMode=e.target.dataset.m;document.querySelectorAll(".mb").forEach(function(x){{x.classList.remove("on")}});e.target.classList.add("on");document.getElementById("reader").classList.toggle("on",gMode=="read");document.getElementById("graph").classList.toggle("on",gMode=="graph");if(gMode=="graph")initG()}};
var themes={{dark:{{bg:"#0d1117",card:"#161b22",bdr:"#30363d",blu:"#58a6ff",txt:"#c9d1d9",dim:"#8b949e",fs:"14px"}},light:{{bg:"#faf8f5",card:"#fff",bdr:"#d4d4d4",blu:"#2563eb",txt:"#1a1a2e",dim:"#6b7280",fs:"15px"}},sepia:{{bg:"#f4ecd8",card:"#faf3e0",bdr:"#c4b896",blu:"#8b5e3c",txt:"#3d2b1f",dim:"#8b7355",fs:"16px"}},forest:{{bg:"#0d2818",card:"#123020",bdr:"#1e4a2e",blu:"#4ade80",txt:"#d4e8d4",dim:"#6b9b6b",fs:"14px"}},ocean:{{bg:"#0c1929",card:"#102440",bdr:"#1a3a5c",blu:"#38bdf8",txt:"#c0daf0",dim:"#5b8db0",fs:"14px"}}}};
var ct="dark";
function AT(t){{ct=t;var c=themes[t];for(var k in c)document.documentElement.style.setProperty("--"+k,c[k]);document.querySelectorAll(".thd").forEach(function(x){{x.classList.toggle("on",x.dataset.t==t)}});document.body.style.fontSize=c.fs||"14px"}}}}
document.getElementById("thm").onclick=function(e){{if(e.target.classList.contains("thd"))AT(e.target.dataset.t)}};
var R=document.getElementById("L"),RS=document.getElementById("resize"),rz=false;
RS.onmousedown=function(e){{rz=true;e.preventDefault()}};
document.onmousemove=function(e){{if(!rz)return;var w=e.clientX;w=Math.max(140,Math.min(600,w));R.style.width=w+"px"}};
document.onmouseup=function(){{rz=false}};

// ====== GRAPH ======
var GP=[],GZv=1,tZ=1,GX=0,GY=0,tX=0,tY=0,Gsel=null,Gdr=-1,Gho=-1,Gctx=null,gInited=false;
function initG(){{if(gInited)return;gInited=true;
var gc=document.getElementById("gc"),Rg=document.getElementById("graph"),Gw=Rg.clientWidth,Gh=Rg.clientHeight;gc.width=Gw;gc.height=Gh;Gctx=gc.getContext("2d");
D.forEach(function(n,i){{var dx={{fish:.1,fresh:.25,marine:.4,terr:.55,cons:.7,soc:.8,cross:.6,math:.9,data:.15}}[n.d]||.5;var ly={{math:.72,meta:.55,grand:.38,middle:.2,data:.05}}[n.l]||.35;GP.push({{x:dx*Gw+(-30+Math.random()*60),y:ly*Gh+(-20+Math.random()*40),vx:0,vy:0}});}})}}
function sim(){{if(gMode!="graph"||GP.length==0)return;
for(var i=0;i<D.length;i++){{for(var j=i+1;j<D.length;j++){{var dx=GP[j].x-GP[i].x,dy=GP[j].y-GP[i].y,d=Math.max(Math.sqrt(dx*dx+dy*dy),3),f=500/(d*d);GP[i].vx-=dx/d*f;GP[i].vy-=dy/d*f;GP[j].vx+=dx/d*f;GP[j].vy+=dy/d*f;}}}}
for(var k in A){{if(!A.hasOwnProperty(k))continue;var si=D.findIndex(function(x){{return x.i==k}});if(si<0)continue;A[k].forEach(function(t){{var ti=D.findIndex(function(x){{return x.i==t}});if(ti<0)return;var dx=GP[ti].x-GP[si].x,dy=GP[ti].y-GP[si].y,d=Math.max(Math.sqrt(dx*dx+dy*dy),3);GP[si].vx+=dx/d*d*.0002;GP[si].vy+=dy/d*d*.0002;GP[ti].vx-=dx/d*d*.0002;GP[ti].vy-=dy/d*d*.0002;}});}}
var Rg=document.getElementById("graph"),Gw=Rg.clientWidth,Gh=Rg.clientHeight;
D.forEach(function(n,i){{if(Gdr==i)return;var dx={{fish:.1,fresh:.25,marine:.4,terr:.55,cons:.7,soc:.8,cross:.6,math:.9,data:.15}}[n.d]||.5;var ly={{math:.72,meta:.55,grand:.38,middle:.2,data:.05}}[n.l]||.35;GP[i].vx+=(dx*Gw-GP[i].x)*.0005;GP[i].vy+=(ly*Gh-GP[i].y)*.0005;GP[i].vx*=.82;GP[i].vy*=.82;GP[i].x+=GP[i].vx;GP[i].y+=GP[i].vy;}})}}
function draw(){{var ctx=Gctx,zw=GZv,th=themes[ct],Rg=document.getElementById("graph"),Gw=Rg.clientWidth,Gh=Rg.clientHeight;ctx.clearRect(0,0,Gw,Gh);ctx.save();ctx.translate(GX,GY);ctx.scale(zw,zw);
for(var k in A){{if(!A.hasOwnProperty(k))continue;var si=D.findIndex(function(x){{return x.i==k}});if(si<0)continue;A[k].forEach(function(t){{var ti=D.findIndex(function(x){{return x.i==t}});if(ti<0||ti<=si)return;var hl=Gsel&&(k==Gsel.i||t==Gsel.i)||(Gho>=0&&(si==Gho||ti==Gho));ctx.globalAlpha=hl?.4:.08;ctx.lineWidth=hl?1/zw:.3/zw;ctx.strokeStyle=hl?th.blu:th.bdr;ctx.beginPath();ctx.moveTo(GP[si].x,GP[si].y);ctx.lineTo(GP[ti].x,GP[ti].y);ctx.stroke();}});}}
D.forEach(function(n,i){{var deg=(A[n.i]||[]).length,r=2.5+deg*1.4;if(n.i=="DATA")r+=1.5;ctx.globalAlpha=1;if(Gsel&&Gsel.i==n.i||Gho==i){{ctx.shadowColor=(C[n.d]||"#ccc");ctx.shadowBlur=8/zw}}ctx.fillStyle=C[n.d]||"#ccc";ctx.beginPath();ctx.arc(GP[i].x,GP[i].y,r,0,Math.PI*2);ctx.fill();ctx.shadowBlur=0;if(n.i=="DATA"){{ctx.strokeStyle="#fff";ctx.lineWidth=1.5/zw;ctx.beginPath();ctx.arc(GP[i].x,GP[i].y,r+2,0,Math.PI*2);ctx.stroke()}}if(deg>=3||n.i=="DATA"||zw>1.2){{ctx.fillStyle=th.txt;ctx.font="bold "+(9/zw)+"px system-ui";var lb=n.n.length>10?n.n.substring(0,9)+"..":n.n;ctx.fillText(lb,GP[i].x+r+3,GP[i].y+2/zw)}}}});ctx.restore();}}
var gc2=document.getElementById("gc");gc2.onmousedown=function(e){{var mx=(e.offsetX-GX)/GZv,my=(e.offsetY-GY)/GZv,cl=-1,md=14/GZv;GP.forEach(function(p,i){{var dx=mx-p.x,dy=my-p.y,d=Math.sqrt(dx*dx+dy*dy);if(d<md){{md=d;cl=i}}}});if(cl>=0){{Gdr=cl;return}}Gdr=-2}};
gc2.onmousemove=function(e){{if(Gdr>=0){{GP[Gdr].x=(e.offsetX-GX)/GZv;GP[Gdr].y=(e.offsetY-GY)/GZv;GP[Gdr].vx=0;GP[Gdr].vy=0;return}}if(Gdr==-2){{GX+=e.movementX;GY+=e.movementY;tX=GX;tY=GY;return}}var mx=(e.offsetX-GX)/GZv,my=(e.offsetY-GY)/GZv,cl=-1,md=12/GZv;GP.forEach(function(p,i){{var dx=mx-p.x,dy=my-p.y,d=Math.sqrt(dx*dx+dy*dy);if(d<md){{md=d;cl=i}}}});if(cl!=Gho){{Gho=cl;var tt=document.getElementById("tt");if(cl>=0){{var n=D[cl];document.getElementById("ttn").textContent=n.n;document.getElementById("ttb").innerHTML=n.y+" "+n.f+" | "+(A[n.i]||[]).length+"连接 | "+(DOM[n.d]||n.d);tt.style.left=Math.min(e.offsetX+10,Gw-230)+"px";tt.style.top=Math.max(e.offsetY-45,5)+"px";tt.style.opacity=1}}else{{tt.style.opacity=0}}}}}};
gc2.onmouseup=function(){{if(Gdr>=0){{go(D[Gdr].i);Gdr=-1}}Gdr=-1}};
gc2.onmouseleave=function(){{Gdr=-1;Gho=-1;document.getElementById("tt").style.opacity=0}};
gc2.onwheel=function(e){{e.preventDefault();tZ*=e.deltaY<0?1.1:.88;tZ=Math.max(.06,Math.min(5,tZ))}};
function GZ(f){{tZ*=f;tZ=Math.max(.06,Math.min(5,tZ))}}
function GR(){{tZ=1;tX=0;tY=0}}
function anim(){{if(gMode=="graph"){{sim();GZv+=(tZ-GZv)*.08;GX+=(tX-GX)*.08;GY+=(tY-GY)*.08;var gc=document.getElementById("gc"),Rg=document.getElementById("graph");if(Rg.clientWidth!=gc.width||Rg.clientHeight!=gc.height){{gc.width=Rg.clientWidth;gc.height=Rg.clientHeight}}draw()}}requestAnimationFrame(anim)}}
anim();rn();
</script></body></html>'''

with open(BASE / 'index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'Generated index.html ({len(html)//1024} KB)')
# Verify
h = html
print(f'DOCTYPE: {h.startswith("<!DOCTYPE")}')
print(f'/html: {h.rstrip().endswith("</html>")}')
