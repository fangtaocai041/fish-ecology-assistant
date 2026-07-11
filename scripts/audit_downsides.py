"""Honest audit of downsides"""
import os

base = "D:/Reasonix/fangtao_fishlab"

# 1. Duplicate adapter_protocol
ws = "D:/Reasonix/scripts/adapter_protocol.py"
local = os.path.join(base, "_shared", "adapter_protocol.py")
print("1. Two copies of adapter_protocol.py:")
print("   workspace exists:", os.path.exists(ws))
print("   local exists:", os.path.exists(local))

# 2. Unmigrated adapters
for proj in ["cognitive-search-engine", "fish-ecology-assistant"]:
    path = os.path.join(base, proj, "src", "adapter.py")
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        c = f.read()
    using = "BaseAdapter" in c
    lines = len(c.split("\n"))
    print("2. {}: {} lines, BaseAdapter={}".format(proj, lines, using))

# 3. conftest count
count = 0
for root, dirs, files in os.walk(base):
    for f in files:
        if f == "conftest.py":
            count += 1
print("3. conftest.py copies: {}".format(count))

# 4. Import boilerplate
path = os.path.join(base, "coilia-agent", "src", "adapter.py")
with open(path, "r", encoding="utf-8", errors="ignore") as f:
    lines = f.readlines()
import_section = 0
for l in lines:
    if "import" in l and "adapter_protocol" in l:
        import_section += 1
    elif import_section > 0 and ("except" in l or "object" in l):
        import_section += 1
print("4. coilia import fallback section: {} lines".format(import_section))

# 5. Still failing tests
print("5. Pre-existing failures:")
print("   eon-core: 4 (cross-project integration + e2e)")
print("   culter-agent: 2 (orchestrator file not found)")
