"""
新旧项目实际运行对比基准测试
================================
测试原则：实践出真知，不只看代码，实际跑起来比
================================
"""
import sys
import os
import time
import importlib

base = "D:/Reasonix/fangtao_fishlab"
results = []

def measure(label, fn):
    """测量函数执行时间和结果"""
    start = time.time()
    ok = True
    error = None
    try:
        result = fn()
    except Exception as e:
        result = None
        ok = False
        error = str(e)[:100]
    elapsed = round((time.time() - start) * 1000, 1)  # ms
    results.append({
        "label": label,
        "ok": ok,
        "time_ms": elapsed,
        "error": error,
        "result_preview": str(result)[:80] if result else None,
    })
    tag = "OK" if ok else "FAIL"
    print(f"  [{tag}] {label}: {elapsed}ms {'| ' + str(result)[:60] if ok else '| ERROR: ' + str(error)[:60]}")

# 保存原始 sys.path
saved_path = list(sys.path)

# ═══════════════════════════════════════════════════════
# 第一部分：新项目 fish_ecology
# ═══════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("  [新项目] fish_ecology")
print("=" * 60)

sys.path = saved_path + ["D:/Reasonix"]

# 1.1 导入时间
measure("import fish_ecology", lambda: importlib.import_module("fish_ecology"))

# 1.2 健康检查
measure("health_check()", lambda: __import__("fish_ecology").health_check())

# 1.3 贝叶斯核心
measure("BetaBelief update", lambda: (
    lambda: (
        setattr(__import__("fish_ecology.core.bayesian", fromlist=["BetaBelief"]).BetaBelief(2,2).update(successes=8,trials=10), '_', None)
    )()
)())

def test_beta():
    from fish_ecology.core.bayesian import BetaBelief
    b = BetaBelief(2,2)
    b.update(successes=5, trials=10)
    return {"mean": round(b.mean(), 4), "ci": b.credible_interval()}

measure("BetaBelief mean+CI", test_beta)

# 1.4 搜索可信度
def test_search():
    from fish_ecology.core.bayesian.applications import SearchCredibility
    e = SearchCredibility.engine_reliability("pubmed")
    e.update(successes=10, trials=10)
    return e.mean()
measure("SearchCredibility", test_search)

# 1.5 知识更新
def test_knowledge():
    from fish_ecology.core.bayesian.applications import KnowledgeUpdater
    r = KnowledgeUpdater.validate_with_bayes("test", 5, 1, 0.8)
    return r["verdict"]
measure("KnowledgeUpdater", test_knowledge)

# 1.6 冲突仲裁
def test_conflict():
    from fish_ecology.core.bayesian.applications import ConflictResolver
    r = ConflictResolver.arbitrate("t", [{"name":"A","value":100,"credibility":0.9}])
    return r["weighted_estimate"]
measure("ConflictResolver", test_conflict)

# 1.7 变点检测
def test_emergence():
    from fish_ecology.core.bayesian.applications import ChangePointDetector
    r = ChangePointDetector.emergence_score(10, 5, 1, 20)
    return r["signal"]
measure("ChangePointDetector", test_emergence)

# 1.8 自检
def test_selfcheck():
    from fish_ecology.core.bayesian import BetaBelief
    r = BetaBelief(2,2).self_check()
    return r.passed
measure("SelfCheck", test_selfcheck)

# ═══════════════════════════════════════════════════════
# 第二部分：旧项目 legacy (独立子进程，避免模块缓存干扰)
# ═══════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("  [旧项目] fangtao_fishlab/ adapters")
print("=" * 60)

# 需要测试的 adapter
adapters_to_test = [
    ("cognitive-search-engine", "CognitiveSearchAdapter", ["health", "self_check", "bayesian_engine_reliability"]),
    ("conflict-arbiter", "ConflictArbiterAdapter", ["health", "self_check"]),
    ("porpoise-agent", "PorpoiseAdapter", ["health", "self_check"]),
    ("coilia-agent", "CoiliaAdapter", ["health", "self_check"]),
]

import subprocess
import json

for proj_name, cls_name, methods in adapters_to_test:
    proj_root = os.path.join(base, proj_name)
    
    # 构建测试代码（用子进程避免模块污染）
    test_code = """
import sys, time, json
saved = list(sys.path)
sys.path = saved + ['D:/Reasonix', r'%s']
# 清缓存
for k in list(sys.modules):
    if 'scripts' in k or 'src' in k or 'adapter' in k:
        del sys.modules[k]
# 预加载 adapter_protocol
import importlib
_ = importlib.import_module('scripts.adapter_protocol')
# 导入 adapter
from src.adapter import %s
inst = %s()
r = {}
# health
t0 = time.time()
try:
    h = inst.health()
    r['health'] = round((time.time()-t0)*1000, 1)
    r['health_status'] = h.get('status')
    r['bayesian'] = 'Y' if 'bayesian' in str(h) else 'N'
except Exception as e:
    r['health_error'] = str(e)[:60]
# self_check
t0 = time.time()
try:
    sc = inst.self_check()
    r['self_check'] = round((time.time()-t0)*1000, 1)
    r['all_ok'] = sc.get('all_ok')
except Exception as e:
    r['self_check_error'] = str(e)[:60]
# bayesian 方法
bayes_methods = [x for x in dir(inst) if x.startswith('bayesian_')]
r['bayes_methods'] = len(bayes_methods)
print(json.dumps(r))
""" % (proj_root, cls_name, cls_name)
    
    try:
        p = subprocess.run([sys.executable, "-c", test_code],
                          capture_output=True, text=True, timeout=15)
        out = p.stdout.strip()
        r = json.loads(out) if out else {"error": p.stderr[:80]}
        
        for k, v in r.items():
            results.append({
                "label": f"{proj_name}.{k}",
                "ok": "error" not in k and v is not None,
                "time_ms": v if isinstance(v, (int, float)) else 0,
                "error": None if "error" not in k else str(v)[:60],
                "result_preview": str(v)[:40],
            })
            tag = "OK" if "error" not in k else "FAIL"
            print(f"  [{tag}] {proj_name}.{k}: {v}")
    except Exception as e:
        results.append({
            "label": f"{proj_name}.import",
            "ok": False,
            "time_ms": 0,
            "error": str(e)[:80],
            "result_preview": None,
        })
        print(f"  [FAIL] {proj_name}: {str(e)[:80]}")

# ═══════════════════════════════════════════════════════
# 第三部分：对比汇总
# ═══════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("  对比汇总")
print("=" * 60)

new_results = [r for r in results if not r["label"].startswith(("cognitive", "conflict", "porpoise", "coilia"))]
legacy_results = [r for r in results if r["label"].startswith(("cognitive", "conflict", "porpoise", "coilia"))]

new_ok = sum(1 for r in new_results if r["ok"])
new_total = len(new_results)
legacy_ok = sum(1 for r in legacy_results if r["ok"])
legacy_total = len(legacy_results)

new_times = [r["time_ms"] for r in new_results if r["ok"]]
legacy_times = [r["time_ms"] for r in legacy_results if r["ok"]]

new_avg = round(sum(new_times)/len(new_times), 1) if new_times else 0
legacy_avg = round(sum(legacy_times)/len(legacy_times), 1) if legacy_times else 0

print(f"  新项目 (fish_ecology):")
print(f"    ├─ 成功率: {new_ok}/{new_total} ({round(new_ok/new_total*100)}%)")
print(f"    ├─ 平均响应: {new_avg}ms")
print(f"    └─ 测试项: core(5) + bayesian(3)")

print(f"  旧项目 (legacy adapters):")
print(f"    ├─ 成功率: {legacy_ok}/{legacy_total} ({round(legacy_ok/legacy_total*100)}%)")
print(f"    ├─ 平均响应: {legacy_avg}ms")
print(f"    └─ 测试项: 4个adapter × health+self_check")

print(f"\n  结论:")
if legacy_ok/legacy_total > new_ok/new_total:
    print(f"    ├─ 旧项目成功率更高 ({legacy_ok}/{legacy_total} vs {new_ok}/{new_total})")
else:
    print(f"    ├─ 新项目成功率更高 ({new_ok}/{new_total} vs {legacy_ok}/{legacy_total})")
print(f"    ├─ 新项目综合功能更全 (含7个领域应用)")
print(f"    └─ 旧项目更贴近实际运行环境")
