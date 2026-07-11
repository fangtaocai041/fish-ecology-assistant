"""Phase 1 verification"""
import sys
sys.path.insert(0, "D:/Reasonix/fangtao_fishlab")
sys.path.insert(0, "D:/Reasonix")
sys.path.insert(0, "D:/Reasonix/fangtao_fishlab/cognitive-search-engine")

from src.adapter import CognitiveSearchAdapter
a = CognitiveSearchAdapter()
sc = a.self_check()
print("Type:", type(sc).__name__)
print("Score:", sc.score)
print("Healthy:", sc.is_healthy)
assert sc.score == 100.0
assert sc.is_healthy
print("[PASS] Phase 1 verified")
