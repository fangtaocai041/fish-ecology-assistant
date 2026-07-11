"""验证双向注入完整性"""
import os

legacy = "D:/Reasonix/fangtao_fishlab"

dirs_to_check = [
    "cognitive-search-engine/src/adapter.py",
    "fish-ecology-assistant/src/adapter.py",
    "eon-core/src/adapter.py",
    "conflict-arbiter/src/adapter.py",
    "porpoise-agent/src/adapter.py",
    "coilia-agent/src/adapter.py",
    "culter-agent/src/adapter.py",
    "infrastructure/__init__.py",
    "san-sheng-wanwu-core/src/__init__.py",
]

checks = {
    "self_check": [],
    "fast_search": [],
    "deep_analyze": [],
    "bayesian": [],
}

for d in dirs_to_check:
    fp = os.path.join(legacy, d)
    if os.path.exists(fp):
        with open(fp, "r", encoding="utf-8") as f:
            c = f.read()
        for kw in ["self_check", "fast_search", "deep_analyze", "bayesian"]:
            if kw in c:
                checks[kw].append(d)
    else:
        print(f"[NOT FOUND] {d}")

print("=== Mutual Update Verification ===")
all_pass = True
for kw, files in checks.items():
    status = len(files)
    ok = status == 9
    if not ok:
        all_pass = False
    symbol = "OK" if ok else "MISSING"
    print(f"  [{symbol}] {kw}: {status}/9 projects")
    if not ok:
        for d in dirs_to_check:
            if d not in files:
                print(f"       missing: {d}")

print()
if all_pass:
    print("=== ALL PASS: 9/9 mutual update complete ===")
else:
    print("=== SOME INJECTIONS INCOMPLETE ===")
