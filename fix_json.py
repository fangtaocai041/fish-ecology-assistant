import json
with open(r'D:\Reasonix\fish-ecology-assistant\config\knowledge_base\ecological_theories\_node_data.json','r',encoding='utf-8') as f:
    nodes = json.load(f)

def js(s):
    return s.replace('\\','\\\\').replace('"','\\"').replace('\n','\\n')[:500]

for n in nodes:
    nid,name,dom,year,founder,layer,desc = n
    n[6] = js(desc)
    if len(n[6]) < 15:
        d = {'EVO':'Darwin 1859自然选择','CONSGEN':'Frankham 1995 50/500法则','LV':'Lotka-Volterra','INFO':'Shannon信息论','GAME':'ESS博弈论','NET':'食物网网络理论','DATA':'课题组22年监测数据'}
        n[6] = d.get(nid, name)

with open(r'D:\Reasonix\fish-ecology-assistant\config\knowledge_base\ecological_theories\_node_data.json','w',encoding='utf-8') as f:
    json.dump(nodes, f, ensure_ascii=False)
print('Fixed', len(nodes), 'nodes')
