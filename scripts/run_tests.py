"""Run all project tests from their home directories"""
import subprocess
import sys
import os

base = "D:/Reasonix/fangtao_fishlab"
projects = [
    ("cognitive-search-engine", "tests/test_imports.py"),
    ("conflict-arbiter", "tests/test_smoke.py"),
    ("culter-agent", "tests/test_smoke.py"),
    ("fish-ecology-assistant", "tests/test_semantic.py"),
    ("infrastructure", "tests/test_deepseek.py"),
]

results = {}
for proj, testfile in projects:
    proj_dir = os.path.join(base, proj)
    test_path = os.path.join(proj_dir, testfile)
    if not os.path.exists(test_path):
        results[proj] = "TEST FILE NOT FOUND"
        continue
    
    r = subprocess.run(
        [sys.executable, "-m", "pytest", testfile, "-v", "--tb=short", "-x"],
        cwd=proj_dir, capture_output=True, text=True, timeout=30
    )
    passed = "PASSED" if "passed" in r.stdout.lower() or "= 0 failed" in r.stdout else "FAILED"
    # count pass/fail
    out_lines = r.stdout.split("\n")
    summary = [l for l in out_lines if "failed" in l.lower() or "passed" in l.lower()]
    results[proj] = summary[-1].strip() if summary else passed
    print("{}: {}".format(proj, results[proj]))

print()
for k, v in results.items():
    print("[{}] {}: {}".format("OK" if "passed" in v.lower() else "FAIL", k, v[:80]))
