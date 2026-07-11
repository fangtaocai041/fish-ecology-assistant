"""Fix CULTER shared_types path — create at expected location"""
from pathlib import Path

target = Path("D:/Reasonix/eon-core/scripts/shared_types.py")
src = Path("D:/Reasonix/fangtao_fishlab/eon-core/scripts/shared_types.py")

target.parent.mkdir(parents=True, exist_ok=True)

if src.exists():
    with open(src, "r", encoding="utf-8") as f:
        content = f.read()
    with open(target, "w", encoding="utf-8") as f:
        f.write(content)
    print("Created:", target)
else:
    print("Source missing:", src)
