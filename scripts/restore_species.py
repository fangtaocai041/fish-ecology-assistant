"""从 fish_species_index.yaml 恢复物种 .md 文件"""
import os, yaml
from pathlib import Path

# 找所有 fish_species_index.yaml
sources = [
    "D:/Reasonix/fangtao_fishlab/fish-ecology-assistant/fishkb/config/fish_species_index.yaml",
    "D:/Reasonix/fangtao_fishlab/fish-ecology-assistant/config/fish_species_index.yaml",
]

index_data = None
for s in sources:
    if os.path.exists(s):
        index_data = yaml.safe_load(Path(s).read_text(encoding="utf-8"))
        print(f"Loaded from: {s}")
        break

if not index_data:
    print("No fish_species_index.yaml found!")
    exit(1)

species_list = index_data.get("species", [])
target = "D:/Reasonix/fangtao_library/species"
os.makedirs(target, exist_ok=True)

count = 0
for entry in species_list:
    sid = entry["id"]
    name = entry.get("name", sid)
    sci = entry.get("scientific", "")
    family = entry.get("family", "")
    conservation = entry.get("conservation", "")
    habitat = entry.get("habitat", "")
    distribution = entry.get("distribution", "")

    path = os.path.join(target, f"{sid}.md")
    content = f"""---
id: {sid}
name: {name}
scientific: {sci}
family: {family}
conservation: {conservation}
habitat: {habitat}
distribution: {distribution}
---

# {name} ({sci})

**科**: {family}
**保护等级**: {conservation}
**栖息地**: {habitat}
**分布**: {distribution}
"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    count += 1

print(f"Restored {count} md files to {target}")
