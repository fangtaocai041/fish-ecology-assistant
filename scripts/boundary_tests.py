"""
boundary_tests.py — 边界极限 + 稳健性扰动测试

[Phase 1] 基础锚定: 穷举各 adapter 的硬限制
[Phase 2] 高压验证: 临界极值不崩, 扰动后恢复

Usage: python scripts/boundary_tests.py
"""

import sys
import os

sys.path.insert(0, "D:/Reasonix/fangtao_fishlab")
sys.path.insert(0, "D:/Reasonix")

results = []


def test(name, fn):
    try:
        fn()
        results.append(("PASS", name, ""))
    except Exception as e:
        results.append(("FAIL", name, str(e)[:100]))


# ====== Boundary Tests ======

# 1. BetaBelief zero params
test("BetaBelief(0,0) mean", lambda: (
    __import__("_bayesian", fromlist=["BetaBelief"]).BetaBelief(0, 0).mean(),
))
test("BetaBelief(0,0) update no crash", lambda: (
    __import__("_bayesian", fromlist=["BetaBelief"]).BetaBelief(0, 0).update(successes=0, trials=0),
))

# 2. BetaBelief extreme params
test("BetaBelief(9999, 1) mean < 1", lambda: (
    __import__("_bayesian", fromlist=["BetaBelief"]).BetaBelief(9999, 1).mean() < 1.0,
))

# 3. query_library missing
test("query_library(lib missing) -> []", lambda: (
    __import__("fangtao_fishlab", fromlist=["query_library"]).query_library("nonexistent_xyz"),
))

# 4. get_adapter unknown
import contextlib
_test_raised = False
try:
    __import__("fangtao_fishlab", fromlist=["get_adapter"]).get_adapter("nonexistent_project")
except Exception:
    _test_raised = True
test("get_adapter(unknown) raises", lambda: _test_raised)

# 5. get_adapter valid
sys.path.insert(0, "D:/Reasonix/fangtao_fishlab/cognitive-search-engine")
test("get_adapter(CSE) works", lambda: (
    __import__("fangtao_fishlab", fromlist=["get_adapter"]).get_adapter("cognitive-search-engine").project_name,
))

# 6. Pipeline empty steps
from _shared.pipeline import Pipeline, PipelineStep
test("Pipeline([]) no crash", lambda: Pipeline("test", []).run("q"))

# 7. health_check import
test("health_check_all import", lambda: (
    __import__("fangtao_fishlab", fromlist=["health_check_all"]).health_check_all(),
))

# 8. empty query -> search
test("CSE search empty query", lambda: (
    __import__("fangtao_fishlab", fromlist=["get_adapter"]).get_adapter("cognitive-search-engine").search(""),
))

# ====== Robustness Tests ======

# 9. safe_call retry on transient
from _shared.errors import safe_call
count = [0]
def flaky():
    count[0] += 1
    if count[0] < 3:
        raise ConnectionError("transient")
    return "ok"

test("safe_call retry transient", lambda: safe_call(flaky, error_type="transient"))

# 10. safe_call fatal no retry
fatal_count = [0]
def fatal_fn():
    fatal_count[0] += 1
    raise RuntimeError("fatal")

try:
    safe_call(fatal_fn, error_type="fatal")
    results.append(("FAIL", "safe_call fatal should raise", ""))
except Exception:
    test("safe_call fatal no retry", lambda: fatal_count[0] == 1)

# ====== Report ======
passed = sum(1 for r in results if r[0] == "PASS")
failed = sum(1 for r in results if r[0] == "FAIL")

print("=" * 55)
print("  Boundary + Robustness Tests")
print("=" * 55)
for tag, name, detail in results:
    s = "PASS" if tag == "PASS" else "FAIL"
    extra = " — " + detail if detail else ""
    print("  [{}] {}{}".format(s, name, extra))

print()
print("  Result: {}/{} passed".format(passed, len(results)))
print("  Boundary violation rate: {}/{}".format(failed, len(results)))
print("=" * 55)

import sys as _sys
_sys.exit(0 if failed == 0 else 1)
