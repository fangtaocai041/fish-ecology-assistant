"""验证旧项目文件注入内容"""
import os

legacy_root = r"D:\Reasonix\legacy"

checks = [
    ("CSE-adapter", "cognitive-search-engine/src/adapter.py", "bayesian_engine_reliability"),
    ("CSE-init", "cognitive-search-engine/src/__init__.py", "bayesian_search_credibility"),
    ("FEA", "fish-ecology-assistant/src/adapter.py", "bayesian_validate_claim"),
    ("EON", "eon-core/src/adapter.py", "bayesian_coordination_confidence"),
    ("CA", "conflict-arbiter/src/adapter.py", "bayesian_confidence"),
    ("INFRA", "infrastructure/__init__.py", "bayesian_emergence_score"),
    ("PORPOISE", "porpoise-agent/src/adapter.py", "bayesian_confidence"),
    ("COILIA", "coilia-agent/src/adapter.py", "bayesian_confidence"),
    ("CULTER", "culter-agent/src/adapter.py", "bayesian_confidence"),
    ("SSWW", "san-sheng-wanwu-core/src/__init__.py", "bayesian_meta_confidence"),
]

all_ok = True
for name, path, keyword in checks:
    full = os.path.join(legacy_root, path)
    if os.path.exists(full):
        with open(full, "r", encoding="utf-8") as f:
            content = f.read()
        ok = keyword in content
        print(f'[{"OK" if ok else "FAIL"}] {name}: {path} -> {keyword}')
        if not ok:
            all_ok = False
    else:
        print(f"[FAIL] {name}: {path} NOT FOUND")
        all_ok = False

print()
if all_ok:
    print("=== All 10 injection points verified ===")
else:
    print("=== Some injection points MISSING ===")
