"""
贝叶斯注入逻辑验证 — 只测核心逻辑，不碰导入链
"""
import sys
sys.path.insert(0, "D:/Reasonix")

from fish_ecology.core.bayesian import BetaBelief, SelfCheckReport
from fish_ecology.core.bayesian.applications import (
    SearchCredibility, KnowledgeUpdater, ConflictResolver,
    ChangePointDetector, AgentBelief, MetaBayesian
)

checks = []

# 1. BetaBelief
b = BetaBelief(2, 2)
b.update(successes=8, trials=10)
mean = b.mean()
checks.append(("BetaBelief update", 0.7 < mean < 0.85, "mean={:.3f}".format(mean)))

# 2. SelfCheck
r = BetaBelief(1, 1).self_check()
checks.append(("SelfCheck type", isinstance(r, SelfCheckReport), ""))

# 3. SearchCredibility
e = SearchCredibility.engine_reliability("pubmed")
e.update(successes=10, trials=10)
checks.append(("SearchCredibility", e.mean() > 0.85, "mean={:.3f}".format(e.mean())))

# 4. KnowledgeUpdater
r = KnowledgeUpdater.validate_with_bayes("test", 5, 1, 0.8)
checks.append(("KnowledgeUpdater", r["verdict"] in ("confirmed","plausible"),
               "verdict={}, post={:.3f}".format(r["verdict"], r["posterior_mean"])))

# 5. ConflictResolver
r = ConflictResolver.arbitrate("test", [{"name":"A","value":100,"credibility":0.9}])
checks.append(("ConflictResolver", abs(r["weighted_estimate"]-100) < 0.1,
               "est={}".format(r["weighted_estimate"])))

# 6. ChangePointDetector
r = ChangePointDetector.emergence_score(10, 5, 1, 20)
checks.append(("ChangePointDetector", r["signal"]=="strong",
               "z={}, signal={}".format(r["z_score"], r["signal"])))

# 7. AgentBelief
s = AgentBelief.species_status()
sm = s.status_summary()
checks.append(("AgentBelief", sm["population"]["estimate"] > 0,
               "pop={:.0f}".format(sm["population"]["estimate"])))

# 8. MetaBayesian
cal = MetaBayesian.calibrate_prior([
    {"success": True, "confidence": 0.9},
    {"success": False, "confidence": 0.1},
])
checks.append(("MetaBayesian", 0 < cal["calibration_score"] <= 1,
               "cal={:.3f}".format(cal["calibration_score"])))

# 输出
print("=" * 55)
print("  Bayesian Core Logic — ASSERTIONS")
print("=" * 55)
all_pass = True
for name, passed, detail in checks:
    tag = "PASS" if passed else "FAIL"
    if not passed:
        all_pass = False
    msg = "  [{}] {}".format(tag, name)
    if detail:
        msg += "  ({})".format(detail)
    print(msg)

print()
if all_pass:
    print("  ALL 8 ASSERTIONS PASSED")
else:
    print("  SOME ASSERTIONS FAILED")
