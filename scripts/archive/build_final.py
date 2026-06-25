#!/usr/bin/env python3
"""终极版：从 _node_data.json 生成自包含 index.html"""
import json

BASE = r'D:\Reasonix\fish-ecology-assistant\config\knowledge_base\ecological_theories'

with open(f'{BASE}/_node_data.json', 'r', encoding='utf-8') as f:
    nodes = json.load(f)

edges = [
    ("EVO","FISHEVO"),("EVO","CONSGEN"),
    ("NICHE","HOMOG"),("NICHE","FUNCDIV"),("NICHE","INV"),("NICHE","NEUTRAL"),
    ("ISLAND","MPOP"),("ISLAND","META"),("ISLAND","MPA"),
    ("RK","MIG"),("RK","FISHEVO"),
    ("SUCC","IDH"),("SUCC","ALT"),("SUCC","LEGACY"),("SUCC","PRIOR"),
    ("IDH","ALT"),("IDH","HOMOG"),
    ("RCC","FPC"),("RCC","ENV"),("FPC","WET"),("ENV","DAM"),
    ("HOMOG","INV"),("HOMOG","DAM"),
    ("FISHEVO","LEGACY"),("LEGACY","PRIOR"),
    ("FUNCDIV","BEF"),("BEF","STORE"),
    ("KEY","TROPH"),("KEY","MEGA"),
    ("MIG","MCONN"),("MCONN","MPA"),
    ("CAS","SES"),("CAS","RESIL"),
    ("RESIL","ADAPT"),("RESIL","REWILD"),("ADAPT","REWILD"),
    ("NEUTRAL","META"),
    ("ALT","EWS"),("CONSGEN","PVA"),("PVA","MPOP"),("ALLEE","PVA"),("ALLEE","CONSGEN"),
    ("LV","TROPH"),("INFO","FUNCDIV"),("GAME","FORAGE"),("NET","TROPH"),("NET","KEY"),
    ("DATA","IDH"),("DATA","HOMOG"),("DATA","FISHEVO"),("DATA","FUNCDIV"),
    ("DATA","MIG"),("DATA","LEGACY"),("DATA","CONSGEN"),("DATA","CAS"),
    ("DATA","COMMONS"),("BACI","DATA"),("PARADIGM","DATA"),
    ("CSR","RK"),("CSR","IDH"),("CSR","SUCC"),
    ("JANZEN","NEUTRAL"),("JANZEN","DILUTE"),("JANZEN","PRIOR"),
    ("COMMONS","SES"),("COMMONS","ADAPT"),
    ("TROPH2","TROPH"),
    ("ASSEMBLY","PRIOR"),("ASSEMBLY","NEUTRAL"),("ASSEMBLY","NICHE"),("ASSEMBLY","ISLAND"),
    ("BACI","EWS"),
    ("PARADIGM","CONSGEN"),("PARADIGM","PVA"),("PARADIGM","REWILD"),
    ("EICA","INV"),("EICA","HOMOG"),("EICA","FISHEVO"),
    ("FACIL","NICHE"),("FACIL","KEY"),("FACIL","SUCC"),
    ("SCALE","META"),("SCALE","RCC"),("SCALE","ISLAND"),("SCALE","NEUTRAL"),
    ("TROPH","TROPH2"),
]

COLORS = {"fish":"#1f77b4","fresh":"#2ca02c","terr":"#ff7f0e","marine":"#17becf","cons":"#d62728","cross":"#e377c2","math":"#9467bd","soc":"#8c564b","data":"#f0f0f0"}
DOMAINS = {"fish":"鱼类生态","fresh":"淡水生态","terr":"陆地生态","marine":"海洋生态","cons":"保护生物","cross":"跨域涌现","math":"数学根基","soc":"社会生态","data":"数据层"}

# Build JS arrays
nl = []
for n in nodes:
    nid,name,dom,year,founder,layer,desc = n
    desc = desc.replace('\\\\','\\\\\\\\').replace('"','\\\\"').replace('\n','\\\\n').replace('\r','')
    if len(desc) < 20:
        descs = {
            'CONSGEN': 'Frankham 1995 Annual Review。保护遗传学奠基。50/500法则：N_e>=50短期避免近交，N_e>=500长期保持进化潜力。江豚N_e~250-375:短期够·长期不足。——D1路径P6。',
            'MTE': 'Brown 2004 Ecology。B=B0 M^3/4 e^(-E/kT)。West Brown Enquist 1997 Science分形网络模型。体型+体温→代谢率→宏观生态模式。',
            'LV': 'Lotka 1925·Volterra 1926。dN/dt=rN-alpha NP。捕食者-猎物振荡。禁渔=移除人类捕食者→dN/dt=rN指数增长→密度制约→新平衡态。',
            'INFO': 'Shannon 1948。H=-Sigma p_i ln p_i=群落熵。禁渔后Shannon增加=信息复杂性恢复。Margalef 1958将信息论引入生态学。',
            'GAME': 'Maynard Smith & Price 1973。进化稳定策略ESS。鹰鸽博弈·囚徒困境。禁渔→移除超级博弈者→鱼类间自然博弈恢复。',
            'NET': 'May 1972 Nature稳定性-复杂性悖论。Dunne 2002证明真实食物网更稳健。Bascompte 2003嵌套互惠网络。禁渔后食物网重构。',
            'DATA': '课题组·FFRC淡水中心。22年(2004-2026)连续监测·5断面(安庆镇江靖江常熟长江口)·禁渔前16年+禁渔后6年·4个T2T基因组·57+SCI·172中文论文。全球唯一大河完全禁渔前后对比数据。研究物种:刀鲚·江豚·鳊·鲢·鳙·中华绒螯蟹·50+种鱼类。',
        }
        desc = descs.get(nid, '生态学经典理论。详见知识库对应 .md 文件。')
    nl.append(f'{{i:"{nid}",n:"{name}",d:"{dom}",y:"{year}",f:"{founder}",l:"{layer}",t:"{desc[:500]}"}}')
nodes_js = ",\n".join(nl)
edges_js = ",\n".join(f'["{e[0]}","{e[1]}"]' for e in edges)

html = f'''<!DOCTYPE html><html lang="zh"><head><meta charset="UTF-8"><title>理论生命之树</title>
<style>
:root{{--bg:#0d1117;--card:#161b22;--bdr:#30363d;--blu:#58a6ff;--txt:#c9d1d9;--dim:#8b949e}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:system-ui,sans-serif;background:var(--bg);color:var(--txt);height:100vh;display:flex;font-size:14px}}
#L{{width:300px;min-width:160px;background:var(--card);border-right:1px solid var(--bdr);display:flex;flex-direction:column;height:100vh;position:relative}}
#LH{{padding:8px 10px;border-bottom:1px solid var(--bdr);flex-shrink:0}}
#LH h1{{font-size:13px;color:var(--blu);margin-bottom:3px}}
#q{{width:100%;background:var(--bg);border:1px solid var(--bdr);border-radius:4px;padding:5px 7px;color:var(--txt);font-size:10px;outline:none}}
#q:focus{{border-color:var(--blu)}}
#tabs{{display:flex;padding:2px 4px;gap:1px;border-bottom:1px solid var(--bdr);overflow-x:auto;flex-shrink:0}}
.tb{{padding:1px 5px;border-radius:3px;cursor:pointer;font-size:8px;color:var(--dim);border:1px solid transparent;white-space:nowrap}}
.tb:hover,.tb.on{{color:var(--blu);border-color:var(--blu)44;background:#1f6feb18}}
#nav{{flex:1;overflow-y:auto;padding:2px 3px}}
.ni{{display:flex;align-items:center;padding:3px 5px;border-radius:3px;cursor:pointer;font-size:9px;gap:3px;border-left:2px solid transparent;margin:1px 0}}
.ni:hover{{background:#1f6feb11}}
.ni.sel{{background:#1f6feb18;border-left-color:var(--blu)}}
.dt{{width:4px;height:4px;border-radius:50%;flex-shrink:0}}
.nm{{flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}}
#R{{flex:1;position:relative;overflow:hidden}}
#mode{{position:absolute;top:6px;left:50%;transform:translateX(-50%);display:flex;gap:2px;z-index:10;background:var(--card);border:1px solid var(--bdr);border-radius:5px;padding:2px}}
.mb{{padding:2px 8px;border-radius:3px;font-size:9px;cursor:pointer;color:var(--dim)}}
.mb.on{{background:var(--blu);color:#fff}}
#reader,#graph{{position:absolute;top:0;left:0;width:100%;height:100%;overflow-y:auto;display:none}}
#reader.on,#graph.on{{display:block}}
#reader{{padding:20px 28px;line-height:1.7;font-size:.9em}}
#reader h1{{font-size:1.3em;color:var(--blu);margin-bottom:4px}}
#reader h2{{font-size:1.05em;color:var(--blu);margin:16px 0 6px;padding-bottom:3px;border-bottom:1px solid var(--bdr)}}
.bar{{display:flex;gap:3px;flex-wrap:wrap;margin-bottom:8px}}
.tg{{padding:1px 5px;border-radius:7px;font-size:8px;border:1px solid var(--bdr)}}
.desc{{font-size:.9em;line-height:1.75;margin:8px 0;white-space:pre-line}}
.cn{{display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:2px;margin-top:4px}}
.cc{{background:var(--card);border:1px solid var(--bdr);border-radius:4px;padding:5px 7px;cursor:pointer;font-size:9px}}
.cc:hover{{border-color:var(--blu)}}
.cc b{{color:var(--txt);font-size:10px}}
.cc s{{color:var(--dim);font-size:7px;display:block}}
#graph canvas{{display:block}}
.hint{{position:absolute;bottom:30px;left:50%;transform:translateX(-50%);color:var(--dim);font-size:8px;pointer-events:none}}
.ctrls{{position:absolute;bottom:3px;right:3px;display:flex;gap:2px}}
.cb{{width:22px;height:22px;border-radius:3px;background:var(--card);border:1px solid var(--bdr);color:var(--txt);cursor:pointer;font-size:11px;display:flex;align-items:center;justify-content:center}}
.cb:hover{{border-color:var(--blu)}}
#tt{{position:absolute;background:var(--card);border:1px solid var(--blu);border-radius:5px;padding:5px 8px;font-size:9px;pointer-events:none;opacity:0;transition:opacity .15s;max-width:200px;z-index:20}}
#tt b{{color:var(--blu);font-size:10px}}
#tt i{{color:var(--dim);font-style:normal;font-size:8px;display:block;margin-top:1px}}
#thm{{display:flex;gap:2px;margin-top:3px}}
.thd{{width:10px;height:10px;border-radius:50%;cursor:pointer;border:2px solid transparent}}
.thd:hover{{border-color:var(--txt)}}
.thd.on{{border-color:var(--blu)}}
</style></head><body>
<div id="L">
<div id="LH"><h1>理论生命之树</h1>
<div id="thm"><span class="thd on" data-t="dark" style="background:#0d1117" title="GitHub Dark"></span><span class="thd" data-t="light" style="background:#fff" title="GitHub Light"></span><span class="thd" data-t="dracula" style="background:#bd93f9" title="Dracula"></span><span class="thd" data-t="nord" style="background:#88c0d0" title="Nord"></span><span class="thd" data-t="monokai" style="background:#a6e22e" title="Monokai"></span><span class="thd" data-t="solarized" style="background:#fdf6e3" title="Solarized"></span><span class="thd" data-t="tokyo" style="background:#7aa2f7" title="Tokyo Night"></span><span class="thd" data-t="catppuccin" style="background:#cba6f7" title="Catppuccin"></span></div>
<input id="q" placeholder="搜索..."></div>
<div id="tabs"></div><div id="nav"></div></div>
<div id="R"><div id="mode"><span class="mb on" data-m="read">阅读</span><span class="mb" data-m="graph">图谱</span></div>
<div id="reader" class="on"><p style="text-align:center;color:var(--dim);margin-top:40%">点击左侧理论开始阅读</p></div>
<div id="graph"><canvas id="gc"></canvas><div class="hint">滚轮缩放·拖拽·点击节点</div><div class="ctrls"><span class="cb" onclick="GZ(1.3)">+</span><span class="cb" onclick="GZ(.75)">-</span><span class="cb" onclick="GR()">R</span></div></div>
<div id="tt"><b id="ttn"></b><i id="ttb"></i></div></div>
<script>
var D=[{nodes_js}];
var C={json.dumps(COLORS)};
var DM={json.dumps(DOMAINS)};
var A={{}};
[{edges_js}].forEach(function(e){{if(!A[e[0]])A[e[0]]=[];A[e[0]].push(e[1]);if(!A[e[1]])A[e[1]]=[];A[e[1]].push(e[0])}});
var sel=null,tab="all",gMode="read";
function rn(){{
var f=D;if(tab!="all")f=f.filter(function(x){{return x.d==tab}});
var q=document.getElementById("q").value.toLowerCase();
if(q)f=f.filter(function(x){{return(x.n+x.f+x.t).toLowerCase().indexOf(q)>-1}});
var h="",ld="";f.forEach(function(n){{
if(n.d!=ld){{ld=n.d;h+='<div style="padding:5px 7px 1px;font-size:7px;color:var(--dim)">'+(DM[n.d]||n.d)+'</div>'}}
h+='<div class="ni'+(sel&&sel.i==n.i?" sel":"")+'" onclick="go(\\''+n.i+'\\')"><span class="dt" style="background:'+(C[n.d]||"#ccc")+'"></span><span class="nm">'+n.n+'</span></div>';
}});
document.getElementById("nav").innerHTML=h||'<div style="padding:12px;color:var(--dim);font-size:9px;text-align:center">无匹配</div>';
}}
function go(id){{
sel=D.find(function(x){{return x.i==id}});if(!sel)return;
var h='<h1>'+sel.n+'</h1><div class="bar"><span class="tg" style="color:'+(C[sel.d]||"#ccc")+'">'+(DM[sel.d]||sel.d)+'</span><span class="tg">'+sel.y+'</span><span class="tg">'+sel.f+'</span></div>';
h+='<div class="desc">'+sel.t+'</div>';
var cs=A[sel.i]||[];
if(cs.length){{h+='<h2>连接理论 ('+cs.length+')</h2><div class="cn">';
cs.forEach(function(cid){{var cn=D.find(function(x){{return x.i==cid}});if(cn)h+='<div class="cc" onclick="go(\\''+cn.i+'\\')"><b>'+cn.n+'</b><s>'+cn.y+' '+cn.f+'</s></div>'}});
h+='</div>';}}
document.getElementById("reader").innerHTML=h;document.getElementById("reader").scrollTop=0;
document.querySelectorAll(".mb").forEach(function(x){{x.classList.remove("on")}});
document.querySelector(".mb[data-m=read]").classList.add("on");
document.getElementById("reader").classList.add("on");document.getElementById("graph").classList.remove("on");
gMode="read";rn();
}}
document.getElementById("q").oninput=rn;
var tabs='<span class="tb on" data-d="all">全部</span>';
["fish","fresh","terr","marine","cons","cross","math","soc","data"].forEach(function(d){{var c=D.filter(function(x){{return x.d==d}}).length;if(c)tabs+='<span class="tb" data-d="'+d+'">'+(DM[d]||d)+'('+c+')</span>'}});
document.getElementById("tabs").innerHTML=tabs;
document.getElementById("tabs").onclick=function(e){{if(e.target.classList.contains("tb")){{tab=e.target.dataset.d;document.querySelectorAll(".tb").forEach(function(x){{x.classList.remove("on")}});e.target.classList.add("on");rn()}}}};
document.getElementById("mode").onclick=function(e){{if(!e.target.classList.contains("mb"))return;gMode=e.target.dataset.m;document.querySelectorAll(".mb").forEach(function(x){{x.classList.remove("on")}});e.target.classList.add("on");document.getElementById("reader").classList.toggle("on",gMode=="read");document.getElementById("graph").classList.toggle("on",gMode=="graph");if(gMode=="graph")initG()}};
var themes={{
dark:{{bg:"#0d1117",card:"#161b22",bdr:"#30363d",blu:"#58a6ff",txt:"#c9d1d9",dim:"#8b949e",fs:"14px",hd:"linear-gradient(135deg,#0d1117,#161b22,#1a2332)"}},
light:{{bg:"#ffffff",card:"#f6f8fa",bdr:"#d0d7de",blu:"#0969da",txt:"#1f2328",dim:"#656d76",fs:"15px",hd:"linear-gradient(135deg,#f6f8fa,#eaeef2,#ddf4ff)"}},
dracula:{{bg:"#282a36",card:"#21222c",bdr:"#44475a",blu:"#bd93f9",txt:"#f8f8f2",dim:"#6272a4",fs:"14px",hd:"linear-gradient(135deg,#282a36,#44475a,#bd93f944)"}},
nord:{{bg:"#2e3440",card:"#3b4252",bdr:"#4c566a",blu:"#88c0d0",txt:"#eceff4",dim:"#81a1c1",fs:"14px",hd:"linear-gradient(135deg,#2e3440,#3b4252,#88c0d033)"}},
monokai:{{bg:"#272822",card:"#1e1f1c",bdr:"#3e3d32",blu:"#a6e22e",txt:"#f8f8f2",dim:"#75715e",fs:"14px",hd:"linear-gradient(135deg,#272822,#3e3d32,#a6e22e22)"}},
solarized:{{bg:"#fdf6e3",card:"#eee8d5",bdr:"#d3cbb6",blu:"#268bd2",txt:"#586e75",dim:"#93a1a1",fs:"16px",hd:"linear-gradient(135deg,#fdf6e3,#eee8d5,#268bd215)"}},
tokyo:{{bg:"#1a1b26",card:"#16161e",bdr:"#2f3543",blu:"#7aa2f7",txt:"#c0caf5",dim:"#565f89",fs:"14px",hd:"linear-gradient(135deg,#1a1b26,#24283b,#7aa2f722)"}},
catppuccin:{{bg:"#1e1e2e",card:"#181825",bdr:"#313244",blu:"#cba6f7",txt:"#cdd6f4",dim:"#6c7086",fs:"14px",hd:"linear-gradient(135deg,#1e1e2e,#313244,#cba6f733)"}}
}};
var ct="dark";
function AT(t){{ct=t;var c=themes[t];for(var k in c)document.documentElement.style.setProperty("--"+k,c[k]);document.querySelectorAll(".thd").forEach(function(x){{x.classList.toggle("on",x.dataset.t==t)}});document.body.style.fontSize=c.fs||"14px"}}
document.getElementById("thm").onclick=function(e){{if(e.target.classList.contains("thd"))AT(e.target.dataset.t)}};

// ====== GRAPH ======
var GP=[],GZv=1,tZ=1,GX=0,GY=0,tX=0,tY=0,Gsel=null,Gdr=-1,Gho=-1,Gctx=null,gInited=false;
function initG(){{if(gInited)return;gInited=true;
var gc=document.getElementById("gc"),Rg=document.getElementById("graph"),Gw=Rg.clientWidth,Gh=Rg.clientHeight;gc.width=Gw;gc.height=Gh;Gctx=gc.getContext("2d");
D.forEach(function(n,i){{var dx={{fish:.1,fresh:.25,marine:.4,terr:.55,cons:.7,soc:.8,cross:.6,math:.9,data:.15}}[n.d]||.5;var ly={{math:.72,meta:.55,grand:.38,middle:.2,data:.05}}[n.l]||.35;GP.push({{x:dx*Gw+Math.random()*60-30,y:ly*Gh+Math.random()*40-20,vx:0,vy:0}});}})}}
function sim(){{if(gMode!="graph"||GP.length==0)return;
for(var i=0;i<D.length;i++){{for(var j=i+1;j<D.length;j++){{var dx=GP[j].x-GP[i].x,dy=GP[j].y-GP[i].y,d=Math.max(Math.hypot(dx,dy),3),f=400/(d*d);GP[i].vx-=dx/d*f;GP[i].vy-=dy/d*f;GP[j].vx+=dx/d*f;GP[j].vy+=dy/d*f;}}}}
for(var k in A){{if(!A[k])continue;var si=D.findIndex(function(x){{return x.i==k}});if(si<0)continue;A[k].forEach(function(t){{var ti=D.findIndex(function(x){{return x.i==t}});if(ti<0)return;var dx=GP[ti].x-GP[si].x,dy=GP[ti].y-GP[si].y,d=Math.max(Math.hypot(dx,dy),3);GP[si].vx+=dx/d*d*.00015;GP[si].vy+=dy/d*d*.00015;GP[ti].vx-=dx/d*d*.00015;GP[ti].vy-=dy/d*d*.00015;}});}}
var Rg=document.getElementById("graph"),Gw=Rg.clientWidth,Gh=Rg.clientHeight;
D.forEach(function(n,i){{if(Gdr==i)return;var dx={{fish:.1,fresh:.25,marine:.4,terr:.55,cons:.7,soc:.8,cross:.6,math:.9,data:.15}}[n.d]||.5;var ly={{math:.72,meta:.55,grand:.38,middle:.2,data:.05}}[n.l]||.35;GP[i].vx+=(dx*Gw-GP[i].x)*.0004;GP[i].vy+=(ly*Gh-GP[i].y)*.0004;GP[i].vx*=.8;GP[i].vy*=.8;GP[i].x+=GP[i].vx;GP[i].y+=GP[i].vy;}})}}
function draw(){{var ctx=Gctx,zw=GZv,th=themes[ct],Rg=document.getElementById("graph"),Gw=Rg.clientWidth,Gh=Rg.clientHeight;ctx.clearRect(0,0,Gw,Gh);ctx.save();ctx.translate(GX,GY);ctx.scale(zw,zw);
for(var k in A){{if(!A[k])continue;var si=D.findIndex(function(x){{return x.i==k}});if(si<0)continue;A[k].forEach(function(t){{var ti=D.findIndex(function(x){{return x.i==t}});if(ti<0||ti<=si)return;var hl=Gsel&&(k==Gsel.i||t==Gsel.i)||(Gho>=0&&(si==Gho||ti==Gho));ctx.globalAlpha=hl?.35:.06;ctx.lineWidth=hl?.8/zw:.25/zw;ctx.strokeStyle=hl?th.blu:th.bdr;ctx.beginPath();ctx.moveTo(GP[si].x,GP[si].y);ctx.lineTo(GP[ti].x,GP[ti].y);ctx.stroke();}});}}
D.forEach(function(n,i){{var deg=(A[n.i]||[]).length,r=2+deg*1.3;if(n.i=="DATA")r+=1.5;ctx.globalAlpha=1;if(Gsel&&Gsel.i==n.i||Gho==i){{ctx.shadowColor=C[n.d]||"#ccc";ctx.shadowBlur=6/zw}}ctx.fillStyle=C[n.d]||"#ccc";ctx.beginPath();ctx.arc(GP[i].x,GP[i].y,r,0,Math.PI*2);ctx.fill();ctx.shadowBlur=0;if(n.i=="DATA"){{ctx.strokeStyle="#fff";ctx.lineWidth=1.2/zw;ctx.beginPath();ctx.arc(GP[i].x,GP[i].y,r+1.5,0,Math.PI*2);ctx.stroke()}}if(deg>=3||n.i=="DATA"||zw>1.15){{ctx.fillStyle=th.txt;ctx.font="bold "+(8/zw)+"px system-ui";var lb=n.n.length>8?n.n.substring(0,7)+"..":n.n;ctx.fillText(lb,GP[i].x+r+3,GP[i].y+2/zw)}}}});ctx.restore();}}
var gc2=document.getElementById("gc");gc2.onmousedown=function(e){{var mx=(e.offsetX-GX)/GZv,my=(e.offsetY-GY)/GZv,cl=-1,md=12/GZv;GP.forEach(function(p,i){{var d=Math.hypot(mx-p.x,my-p.y);if(d<md){{md=d;cl=i}}}});if(cl>=0){{Gdr=cl}}else{{Gdr=-2}}}};
gc2.onmousemove=function(e){{if(Gdr>=0){{GP[Gdr].x=(e.offsetX-GX)/GZv;GP[Gdr].y=(e.offsetY-GY)/GZv;GP[Gdr].vx=0;GP[Gdr].vy=0;return}}if(Gdr==-2){{GX+=e.movementX;GY+=e.movementY;tX=GX;tY=GY;return}}var mx=(e.offsetX-GX)/GZv,my=(e.offsetY-GY)/GZv,cl=-1,md=10/GZv,Rg=document.getElementById("graph");GP.forEach(function(p,i){{var d=Math.hypot(mx-p.x,my-p.y);if(d<md){{md=d;cl=i}}}});if(cl!=Gho){{Gho=cl;var tt=document.getElementById("tt");if(cl>=0){{var n=D[cl];document.getElementById("ttn").textContent=n.n;document.getElementById("ttb").innerHTML=n.y+" "+n.f+" | "+(A[n.i]||[]).length+"连接 | "+(DM[n.d]||n.d);tt.style.left=Math.min(e.offsetX+8,Rg.clientWidth-210)+"px";tt.style.top=Math.max(e.offsetY-40,5)+"px";tt.style.opacity=1}}else{{tt.style.opacity=0}}}}}};
gc2.onmouseup=function(){{if(Gdr>=0){{go(D[Gdr].i);Gdr=-1}}Gdr=-1}};
gc2.onmouseleave=function(){{Gdr=-1;Gho=-1;document.getElementById("tt").style.opacity=0}};
gc2.onwheel=function(e){{e.preventDefault();tZ*=e.deltaY<0?1.08:.9;tZ=Math.max(.05,Math.min(5,tZ))}};
function GZ(f){{tZ*=f;tZ=Math.max(.05,Math.min(5,tZ))}}
function GR(){{tZ=1;tX=0;tY=0}}
function anim(){{if(gMode=="graph"){{sim();GZv+=(tZ-GZv)*.07;GX+=(tX-GX)*.07;GY+=(tY-GY)*.07;var gc=document.getElementById("gc"),Rg=document.getElementById("graph");if(Rg.clientWidth!=gc.width||Rg.clientHeight!=gc.height){{gc.width=Rg.clientWidth;gc.height=Rg.clientHeight}}draw()}}requestAnimationFrame(anim)}}
anim();rn();
</script></body></html>'''

with open(f'{BASE}/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print(f'Generated {len(html)//1024} KB')
print(f'DO: {html.startswith("<!DOCTYPE")}')
print(f'/html: {html.rstrip().endswith("</html>")}')
