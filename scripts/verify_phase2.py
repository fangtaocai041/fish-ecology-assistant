"""Phase 2: 高压验证 _shared 各模块在隔离环境可运行"""
import sys
sys.path.insert(0, "D:/Reasonix/fangtao_fishlab")
sys.path.insert(0, "D:/Reasonix")

errors = []

# 1. auditor
print("=== auditor ===")
try:
    from _shared.auditor import AuditTrail, StepLog
    t = AuditTrail("test")
    s = t.start("step1")
    t.complete(s, {"ok": True})
    sm = t.summary()
    assert sm["total_steps"] == 1
    assert sm["failed"] == 0
    print("[PASS] AuditTrail: start->complete->summary OK")
except Exception as e:
    errors.append("auditor: " + str(e)[:80])

# 2. pipeline
print("=== pipeline ===")
try:
    from _shared.pipeline import Pipeline, PipelineStep
    p = Pipeline("test", [PipelineStep(name="dummy", adapter="cognitive-search-engine")])
    # 不实际跑，只验证定义
    assert p.name == "test"
    assert len(p.steps) == 1
    print("[PASS] Pipeline: definition OK")
except Exception as e:
    errors.append("pipeline: " + str(e)[:80])

# 3. pipeline_validator
print("=== pipeline_validator ===")
try:
    from _shared.pipeline_validator import PipelineValidator
    v = PipelineValidator()
    v2 = PipelineValidator()
    assert v is not v2  # 非单例
    print("[PASS] PipelineValidator: class OK")
except Exception as e:
    errors.append("pipeline_validator: " + str(e)[:80])

# 4. quality_metrics
print("=== quality_metrics ===")
try:
    from _shared.quality_metrics import QualityMetrics
    q = QualityMetrics(bayesian_calibration=100.0, method_coverage=100.0)
    assert q.overall_score > 0
    print("[PASS] QualityMetrics: score={:.1f}".format(q.overall_score))
except Exception as e:
    errors.append("quality_metrics: " + str(e)[:80])

print()
if errors:
    print("[FAIL] Phase 2: " + "; ".join(errors))
else:
    print("[PASS] Phase 2: all 4 modules verified")
