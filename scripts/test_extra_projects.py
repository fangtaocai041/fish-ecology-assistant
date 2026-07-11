"""
验证 infrastructure 和 san-sheng-wanwu-core 的注入可运行
"""
import sys
import os

base = "D:/Reasonix/fangtao_fishlab"
sys.path = [p for p in sys.path if "python" in p or "site-packages" in p]
sys.path.insert(0, "D:/Reasonix")

results = {}

# === infrastructure ===
print("=== infrastructure ===")
sys.path.insert(0, base)  # 父目录，让 import infrastructure 找到包
for k in list(sys.modules):
    if "infrastructure" in k:
        del sys.modules[k]
try:
    import infrastructure
    r1 = infrastructure.self_check()
    print("  self_check:", r1)
    r2 = infrastructure.bayesian_emergence_score(10, 5, 1)
    print("  bayesian_emergence_score signal:", r2.get("signal"))
    r3 = infrastructure.fast_search("test")
    print("  fast_search mode:", r3.get("mode"))
    r4 = infrastructure.deep_analyze("test")
    print("  deep_analyze ok:", isinstance(r4, dict))
    results["infrastructure"] = "PASS"
except Exception as e:
    print("  FAIL:", e)
    results["infrastructure"] = "FAIL"

# === san-sheng-wanwu-core ===
print("\n=== san-sheng-wanwu-core ===")
for k in list(sys.modules):
    if "ssww" in k or "san_sheng" in k or "src" in k:
        del sys.modules[k]
try:
    sys.path.insert(0, os.path.join(base, "san-sheng-wanwu-core"))
    import src as ssww
    r1 = ssww.self_check()
    print("  self_check:", r1)
    r2 = ssww.bayesian_meta_confidence()
    print("  bayesian_meta_confidence:", r2.get("meta_confidence"))
    r3 = ssww.fast_search("test")
    print("  fast_search mode:", r3.get("mode"))
    r4 = ssww.deep_analyze("test")
    m = r4.get("mode", "unknown") if isinstance(r4, dict) else "ok"
    print("  deep_analyze mode:", m)
    results["ssww"] = "PASS"
except Exception as e:
    print("  FAIL:", e)
    import traceback
    traceback.print_exc()
    results["ssww"] = "FAIL"

print("\n=== Results ===")
for k, v in results.items():
    print("  [{}] {}".format(v, k))
