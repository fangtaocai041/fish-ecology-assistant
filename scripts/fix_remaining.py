"""Fix remaining legacy path references"""
import os

base = "D:/Reasonix/fangtao_fishlab"

for root, dirs, files in os.walk(base):
    dirs[:] = [d for d in dirs if d not in ("__pycache__", ".git", ".reasonix")]
    for f in files:
        if not f.endswith(".py"):
            continue
        path = os.path.join(root, f)
        with open(path, "r", encoding="utf-8", errors="ignore") as fh:
            c = fh.read()

        changed = False
        # Fix path strings
        if "D:/Reasonix/fangtao_fishlab" in c:
            c = c.replace("D:/Reasonix/fangtao_fishlab", "D:/Reasonix/fangtao_fishlab")
            changed = True
        
        # Fix "legacy" as a string literal (used in _paths.py)
        if 'REASONIX_ROOT / "fangtao_fishlab"' in c:
            c = c.replace('REASONIX_ROOT / "fangtao_fishlab"', 'REASONIX_ROOT / "fangtao_fishlab"')
            changed = True

        if changed:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(c)
            print("Fixed:", os.path.relpath(path, base))

print("Done")
