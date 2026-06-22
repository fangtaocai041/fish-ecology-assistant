h=open(r'D:\Reasonix\fish-ecology-assistant\config\knowledge_base\ecological_theories\index.html','r',encoding='utf-8').read()
import re
items=re.findall(r't:"([^"]*)"',h)
print(f'Size: {len(h)//1024}KB')
print(f'Desc items: {len(items)}')
for i,item in enumerate(items[:5]):
    print(f'  [{i}] len={len(item)}: {item[:100]}')
empty=[i for i,t in enumerate(items) if len(t)<10]
if empty: print(f'Empty: {empty}')
