#!/usr/bin/env python3
"""终极版：借鉴 ECharts 模式生成理论生命之树"""
import json

BASE = r'D:\Reasonix\fish-ecology-assistant\config\knowledge_base\ecological_theories'

with open(f'{BASE}/_node_data.json', 'r', encoding='utf-8') as f:
    raw_nodes = json.load(f)

edges = [
    ("EVO","FISHEVO"),("EVO","CONSGEN"),("NICHE","HOMOG"),("NICHE","FUNCDIV"),("NICHE","INV"),("NICHE","NEUTRAL"),
    ("ISLAND","MPOP"),("ISLAND","META"),("ISLAND","MPA"),("RK","MIG"),("RK","FISHEVO"),
    ("SUCC","IDH"),("SUCC","ALT"),("SUCC","LEGACY"),("SUCC","PRIOR"),
    ("IDH","ALT"),("IDH","HOMOG"),("RCC","FPC"),("RCC","ENV"),("FPC","WET"),("ENV","DAM"),
    ("HOMOG","INV"),("HOMOG","DAM"),("FISHEVO","LEGACY"),("LEGACY","PRIOR"),
    ("FUNCDIV","BEF"),("BEF","STORE"),("KEY","TROPH"),("KEY","MEGA"),
    ("MIG","MCONN"),("MCONN","MPA"),("CAS","SES"),("CAS","RESIL"),("RESIL","ADAPT"),("RESIL","REWILD"),("ADAPT","REWILD"),
    ("NEUTRAL","META"),("ALT","EWS"),("CONSGEN","PVA"),("PVA","MPOP"),("ALLEE","PVA"),("ALLEE","CONSGEN"),
    ("LV","TROPH"),("INFO","FUNCDIV"),("GAME","FORAGE"),("NET","TROPH"),("NET","KEY"),
    ("DATA","IDH"),("DATA","HOMOG"),("DATA","FISHEVO"),("DATA","FUNCDIV"),("DATA","MIG"),("DATA","LEGACY"),("DATA","CONSGEN"),("DATA","CAS"),
    ("DATA","COMMONS"),("BACI","DATA"),("PARADIGM","DATA"),
    ("CSR","RK"),("CSR","IDH"),("CSR","SUCC"),("JANZEN","NEUTRAL"),("JANZEN","DILUTE"),("JANZEN","PRIOR"),
    ("COMMONS","SES"),("COMMONS","ADAPT"),("TROPH2","TROPH"),
    ("ASSEMBLY","PRIOR"),("ASSEMBLY","NEUTRAL"),("ASSEMBLY","NICHE"),("ASSEMBLY","ISLAND"),("BACI","EWS"),
    ("PARADIGM","CONSGEN"),("PARADIGM","PVA"),("PARADIGM","REWILD"),
    ("EICA","INV"),("EICA","HOMOG"),("EICA","FISHEVO"),("FACIL","NICHE"),("FACIL","KEY"),("FACIL","SUCC"),
    ("SCALE","META"),("SCALE","RCC"),("SCALE","ISLAND"),("SCALE","NEUTRAL"),("TROPH","TROPH2"),
    ("ECOEVO","FISHEVO"),("ECOEVO","EVO"),
]

DOMAINS = {"fish":"鱼类生态","fresh":"淡水生态","terr":"陆地生态","marine":"海洋生态","cons":"保护生物","cross":"跨域涌现","math":"数学根基","soc":"社会生态","data":"数据层"}
COLORS = {"fish":"#1f77b4","fresh":"#2ca02c","terr":"#ff7f0e","marine":"#17becf","cons":"#d62728","cross":"#e377c2","math":"#9467bd","soc":"#8c564b","data":"#f0f0f0"}

# Build JS data
nodes_js = []
for n in raw_nodes:
    nid,name,dom,year,founder,layer,desc = n
    desc = desc.replace('\\','\\\\').replace('"','\\"').replace('\n','\\n')[:600]
    if not desc: desc = f'{name}。{DOMAINS.get(dom,dom)}理论。{founder}。'
    nodes_js.append(f'{{i:"{nid}",n:"{name}",d:"{dom}",y:"{year}",f:"{founder}",l:"{layer}",t:"{desc}"}}')
nodes_js_str = ',\n'.join(nodes_js)
    nid,name,dom,year,founder,layer,desc = n
    desc = desc.replace('\\','\\\\').replace('"','\\"').replace('\n','\\n')[:600]
    if not desc: desc = f'{name}。{DOMAINS.get(dom,dom)}理论。{founder}。'
    nodes_js.append(f'{{i:"{nid}",n:"{name}",d:"{dom}",y:"{year}",f:"{founder}",l:"{layer}",t:"{desc}"}}')

edges_js = json.dumps(edges)

html = f'''<!DOCTYPE html><html lang="zh"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>理论生命之树</title>
<script src="https://cdn.bootcdn.net/ajax/libs/echarts/5.5.0/echarts.min.js"></script>
<style>
:root{{--bg:#0d1117;--card:#161b22;--bdr:#30363d;--blu:#58a6ff;--txt:#c9d1d9;--dim:#8b949e}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:system-ui,'Microsoft YaHei',sans-serif;background:var(--bg);color:var(--txt);min-height:100vh}}
header{{background:linear-gradient(135deg,#1a3a2a,#2d5a27,#4a7c3f);color:#fff;padding:1.2rem 1rem;text-align:center}}
header h1{{font-size:1.3rem;letter-spacing:.04em}}
header p{{font-size:.8rem;opacity:.8;margin-top:.3rem}}
.view-tabs{{display:flex;justify-content:center;gap:0;margin:.8rem auto 0;max-width:340px;background:var(--card);border-radius:20px;overflow:hidden;border:1px solid var(--bdr)}}
.vt{{flex:1;padding:.5rem;text-align:center;cursor:pointer;font-size:.8rem;border:none;background:transparent;color:var(--dim);transition:all .2s}}
.vt.active{{background:var(--blu);color:#fff}}
.stats{{display:flex;gap:1rem;flex-wrap:wrap;justify-content:center;padding:.6rem;background:var(--card);border-bottom:1px solid var(--bdr);font-size:.75rem}}
.stats b{{color:var(--blu)}}
.controls{{max-width:1100px;margin:.8rem auto;padding:0 1rem;display:flex;gap:.5rem;flex-wrap:wrap}}
#q{{flex:1;min-width:180px;padding:.5rem .8rem;border:1px solid var(--bdr);border-radius:16px;font-size:.8rem;background:var(--bg);color:var(--txt);outline:none}}
#q:focus{{border-color:var(--blu)}}
.dom-filters{{display:flex;gap:.3rem;flex-wrap:wrap}}
.df{{padding:.25rem .6rem;border-radius:12px;cursor:pointer;font-size:.7rem;border:1px solid var(--bdr);color:var(--dim);transition:all .2s}}
.df.on{{background:var(--blu);color:#fff;border-color:var(--blu)}}
.cards{{max-width:1100px;margin:0 auto;padding:0 1rem 2rem;display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:.8rem}}
.card{{background:var(--card);border-radius:10px;padding:1rem;cursor:pointer;transition:all .2s;border-left:3px solid var(--bdr);position:relative}}
.card:hover{{transform:translateY(-2px);border-left-color:var(--blu);box-shadow:0 4px 16px rgba(0,0,0,.3)}}
.card h3{{font-size:.9rem;color:var(--blu);margin-bottom:.15rem}}
.card .meta{{font-size:.7rem;color:var(--dim);margin-bottom:.4rem}}
.card .desc{{font-size:.75rem;color:var(--txt);line-height:1.55;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}}
.card .detail{{display:none;margin-top:.6rem;padding-top:.6rem;border-top:1px solid var(--bdr);font-size:.78rem;line-height:1.6;white-space:pre-line}}
.card.open .detail{{display:block}}
.card.open .desc{{display:none}}
.card .links{{margin-top:.5rem;display:flex;flex-wrap:wrap;gap:.3rem}}
.card .lk{{padding:.2rem .5rem;border-radius:10px;font-size:.65rem;background:var(--bg);border:1px solid var(--bdr);color:var(--blu);cursor:pointer}}
.card .lk:hover{{border-color:var(--blu)}}
#gv{{display:none}}
#gc{{width:100%;height:650px}}
footer{{text-align:center;padding:1rem;color:var(--dim);font-size:.7rem;border-top:1px solid var(--bdr)}}
@media(max-width:600px){{.cards{{grid-template-columns:1fr}}#gc{{height:400px}}}}
</style></head><body>
<header><h1>🌳 生态学理论生命之树</h1><p>63节点·{len(edges)}连线·15领域 | 知识库本体 .md + 交互式阅读器</p></header>
<div class="view-tabs"><span class="vt active" data-v="cards">📋 卡片浏览</span><span class="vt" data-v="graph">🕸️ 知识图谱</span></div>
<div class="stats"><span>节点 <b>{len(raw_nodes)}</b></span><span>连线 <b>{len(edges)}</b></span><span>领域 <b>9</b></span><span>覆盖理论 <b>45+</b></span></div>
<div id="cv">
<div class="controls"><input id="q" placeholder="🔍 搜索理论/人物/关键词..."><div class="dom-filters" id="df"></div></div>
<div class="cards" id="cards"></div>
</div>
<div id="gv"><div id="gc"></div></div>
<footer>知识库本体：69个.md文件 | Python build_final.py 生成 | 交互式阅读器</footer>
<script>
var D=[{nodes_js_str}];
var E={edges_js};
var C={json.dumps(COLORS)};
var DM={json.dumps(DOMAINS)};
var A={{}};E.forEach(function(e){{if(!A[e[0]])A[e[0]]=[];A[e[0]].push(e[1]);if(!A[e[1]])A[e[1]]=[];A[e[1]].push(e[0])}});
var activeDoms=Object.keys(DM);
var view="cards";

// Domain filter buttons
var dfHtml='';
Object.keys(DM).forEach(function(d){{var c=D.filter(function(x){{return x.d==d}}).length;dfHtml+='<span class="df on" data-d="'+d+'" style="border-color:'+(C[d]||"#ccc")+'">'+(DM[d]||d)+'('+c+')</span>'}});
document.getElementById("df").innerHTML=dfHtml;
document.getElementById("df").onclick=function(e){{if(!e.target.classList.contains("df"))return;e.target.classList.toggle("on");activeDoms=[];document.querySelectorAll(".df.on").forEach(function(x){{activeDoms.push(x.dataset.d)}});renderCards()}};

function renderCards(){{
var q=document.getElementById("q").value.toLowerCase();
var f=D.filter(function(x){{return activeDoms.includes(x.d)}});
if(q)f=f.filter(function(x){{return(x.n+x.f+x.t).toLowerCase().indexOf(q)>-1}});
var h="";
f.forEach(function(n){{
var cs=A[n.i]||[];
h+='<div class="card" id="c-'+n.i+'" onclick="toggleCard(\\''+n.i+'\\')"><h3><span style="color:'+(C[n.d]||"#ccc")+'">●</span> '+n.n+'</h3><div class="meta">'+n.y+' · '+n.f+' · '+(DM[n.d]||n.d)+' · '+(cs.length)+'条连接</div><div class="desc">'+n.t+'</div><div class="detail">'+n.t+'</div><div class="links">'+cs.slice(0,6).map(function(cid){{var cn=D.find(function(x){{return x.i==cid}});return cn?'<span class="lk" onclick="event.stopPropagation();toggleCard(\\''+cn.i+'\\');document.getElementById(\\'c-\\'+cn.i+\\').scrollIntoView({{behavior:\\'smooth\\',block:\\'center\\'}})">'+cn.n+'</span>':''}}).join('')+'</div></div>';
}});
document.getElementById("cards").innerHTML=h||'<div style="text-align:center;padding:2rem;color:var(--dim);grid-column:1/-1">无匹配理论</div>';
}}
function toggleCard(id){{
var el=document.getElementById("c-"+id);if(!el)return;
var wasOpen=el.classList.contains("open");
document.querySelectorAll(".card.open").forEach(function(c){{c.classList.remove("open")}});
if(!wasOpen)el.classList.add("open");
}}

document.getElementById("q").oninput=renderCards;

// View switch
document.querySelectorAll(".vt").forEach(function(v){{v.onclick=function(){{
view=this.dataset.v;document.querySelectorAll(".vt").forEach(function(x){{x.classList.remove("active")}});this.classList.add("active");
document.getElementById("cv").style.display=view=="cards"?"block":"none";
document.getElementById("gv").style.display=view=="graph"?"block":"none";
if(view=="graph")buildGraph();
}}}});

// ECharts graph
var gChart=null;
function buildGraph(){{
var nodes=D.map(function(n,i){{return{{id:n.i,name:n.n,symbolSize:4+(A[n.i]||[]).length*2,itemStyle:{{color:C[n.d]||"#ccc"}},category:n.d,label:{{show:(A[n.i]||[]).length>=3||n.i=="DATA"||n.d=="math",fontSize:9,color:"#999"}},data:n}}}});
var links=E.map(function(e){{return{{source:e[0],target:e[1],lineStyle:{{color:"#30363d",width:.5,opacity:.3}}}}}});
var cats=Object.keys(DM).map(function(d){{return{{name:DM[d]||d,itemStyle:{{color:C[d]||"#ccc"}}}}}});
var opt={{tooltip:{{formatter:function(p){{if(p.dataType=="node"){{var n=p.data.data;return"<b>"+n.n+"</b><br>"+n.y+" "+n.f+"<br>"+(DM[n.d]||n.d)+"<br>"+(A[n.i]||[]).length+"条连接"}}return""}}}},legend:{{bottom:5,textStyle:{{color:"#999",fontSize:10}}}},series:[{{type:"graph",layout:"force",force:{{repulsion:300,edgeLength:[80,250],gravity:.1}},roam:true,draggable:true,data:nodes,links:links,categories:cats,lineStyle:{{curveness:.2}},label:{{show:true,position:"right",fontSize:9,color:"#999"}},emphasis:{{focus:"adjacency",lineStyle:{{width:2}}}}}}]}};
var el=document.getElementById("gc");if(gChart){{gChart.dispose()}}
gChart=echarts.init(el,"dark");gChart.setOption(opt);gChart.on("click",function(p){{if(p.dataType=="node"&&p.data&&p.data.data){{view="cards";document.querySelectorAll(".vt").forEach(function(x){{x.classList.remove("active")}});document.querySelector(".vt[data-v=cards]").classList.add("active");document.getElementById("cv").style.display="block";document.getElementById("gv").style.display="none";toggleCard(p.data.data.i);document.getElementById("c-"+p.data.data.i).scrollIntoView({{behavior:"smooth",block:"center"}});}}}});
window.addEventListener("resize",function(){{if(gChart)gChart.resize()}});
}}
renderCards();
</script></body></html>'''

with open(f'{BASE}/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print(f'Generated: {len(html)//1024} KB')
