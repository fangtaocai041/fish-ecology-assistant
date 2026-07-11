"""
验证 infrastructure — 不做 sys.path 过滤
"""
import sys
import os

base = "D:/Reasonix/fangtao_fishlab"

# 保留原始 sys.path，只添加 legacy 父目录
sys.path.insert(0, base)
sys.path.insert(0, "D:/Reasonix")

# 清理缓存
for k in list(sys.modules):
    if "infrastructure" in k:
        del sys.modules[k]

try:
    import infrastructure
    print("[OK] infrastructure imported")

    r = infrastructure.self_check()
    print("  self_check:", r)

    r = infrastructure.bayesian_emergence_score(10, 5, 1)
    print("  bayesian_emergence_score signal:", r.get("signal"))

    r = infrastructure.fast_search("test")
    print("  fast_search mode:", r.get("mode"))

    r = infrastructure.deep_analyze("test")
    print("  deep_analyze ok:", isinstance(r, dict))

    print("[PASS] infrastructure all checks OK")
except Exception as e:
    print("[FAIL] infrastructure:", e)
    import traceback
    traceback.print_exc()
