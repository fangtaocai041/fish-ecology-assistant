"""Fix _reasonix path calculation in all legacy adapters"""
import os

base = "D:/Reasonix/fangtao_fishlab"
adapters = [
    "cognitive-search-engine/src/adapter.py",
    "fish-ecology-assistant/src/adapter.py",
    "eon-core/src/adapter.py",
    "conflict-arbiter/src/adapter.py",
    "porpoise-agent/src/adapter.py",
    "coilia-agent/src/adapter.py",
    "culter-agent/src/adapter.py",
]

fix_code = """# Add D:/Reasonix to sys.path for shared protocols (scripts/adapter_protocol)
_reasonix = str(Path(__file__).resolve().parent.parent.parent)
if _reasonix not in sys.path:
    sys.path.insert(0, _reasonix)
# Also ensure workspace root is on path
_workspace_root = str(Path(__file__).resolve().parent.parent.parent.parent)
if _workspace_root not in sys.path:
    sys.path.insert(0, _workspace_root)"""

for rel in adapters:
    path = os.path.join(base, rel)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Count existing parent.parent.parent occurrences
    count = content.count("parent.parent.parent")
    if count == 0:
        print(f"SKIP {rel}: no parent.parent.parent found")
        continue
    
    # Find the _reasonix block
    old_lines = content.split("\n")
    new_lines = []
    i = 0
    fixed = False
    while i < len(old_lines):
        line = old_lines[i]
        if "parent.parent.parent" in line and not fixed:
            # Check next lines for sys.path.insert
            if i + 2 < len(old_lines) and "sys.path.insert" in old_lines[i+2]:
                # Skip the original 3 lines and insert our fix
                new_lines.append(fix_code)
                i += 3
                fixed = True
                continue
        new_lines.append(line)
        i += 1
    
    if fixed:
        new_content = "\n".join(new_lines)
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"FIXED {rel}")
    else:
        print(f"NOT FIXED {rel}: pattern not matched")
