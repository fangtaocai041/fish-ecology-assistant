"""Audit: check all boundary conditions in public API"""
import sys

sys.path.insert(0, "D:/Reasonix/fangtao_fishlab")
sys.path.insert(0, "D:/Reasonix")

issues = []

# 1. query_library miss
from fangtao_fishlab import query_library
try:
    r = query_library("nonexistent_xyz_999", "species")
    if r == []:
        pass  # correct: no results
    else:
        issues.append("query_library unexpected: " + str(r))
except FileNotFoundError:
    issues.append("query_library raises FileNotFoundError on miss (should return [])")

# 2. get_adapter miss
from fangtao_fishlab import get_adapter
try:
    a = get_adapter("nonexistent_project")
    issues.append("get_adapter should raise on unknown name")
except ValueError:
    pass  # correct

# 3. get_adapter import fail
try:
    a = get_adapter("san-sheng-wanwu-core")
    h = a.health()
    print("  ssww health:", h.get("status", "?"))
except Exception as e:
    issues.append("get_adapter(ssww) failed: " + str(e)[:60])

# 4. BetaBelief bounds
from _bayesian import BetaBelief
b = BetaBelief(alpha=0, beta=0)  # extreme: zero params
m = b.mean()
# mean should be 0.5 since (0)/(0+0) is undefined -> default
if m == 0.5 or abs(m - 0.5) < 0.01:
    pass
else:
    issues.append("BetaBelief(0,0) gave unexpected mean: " + str(m))

b.update(successes=0, trials=0)  # zero evidence
# should not crash

# 5. infrastructure import
import importlib
try:
    mod = importlib.import_module("infrastructure")
except Exception as e:
    issues.append("infrastructure import failed: " + str(e)[:60])

print("Issues found: {}".format(len(issues)))
for i in issues:
    print("  [BOUNDARY] " + i)
if not issues:
    print("  All boundary conditions passed")
