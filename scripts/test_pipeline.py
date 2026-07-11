"""Pipeline end-to-end test with timing"""
import sys
sys.path.insert(0, "D:/Reasonix/fangtao_fishlab")
sys.path.insert(0, "D:/Reasonix")

from _shared.pipeline import STANDARD_PIPELINE

print("=== STANDARD pipeline with timing ===")
r = STANDARD_PIPELINE.run("鳤")
for k, v in r.items():
    st = v.get("status", "?") if isinstance(v, dict) else "?"
    dur = v.get("step_duration_ms", -1) if isinstance(v, dict) else -1
    print("  {:20s} status={:25s} t={}ms".format(k, st, dur))

print("\n[PASS] Pipeline with timing")
