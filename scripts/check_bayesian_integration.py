#!/usr/bin/env python3
"""
旧项目贝叶斯注入 — 全链路验证脚本

验证所有9个旧项目可以正确导入贝叶斯模块。
"""

import sys
import os

sys.path.insert(0, r"D:\Reasonix")

PASS = 0
FAIL = 0
results = []

def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
        results.append(f"  [PASS] {name}")
    else:
        FAIL += 1
        results.append(f"  [FAIL] {name} — {detail}")

# ═══════════════════════════════════════════════════════
# 1. 检查核心贝叶斯框架本身
# ═══════════════════════════════════════════════════════

try:
    from fish_ecology.core.bayesian import (
        BetaBelief, NormalBelief, DirichletBelief,
        SearchCredibility, KnowledgeUpdater, ConflictResolver,
        ChangePointDetector, AgentBelief, MetaBayesian,
    )
    b = BetaBelief(1, 1)
    b.update(successes=5, trials=10)
    check("核心框架导入", True, f"Beta更新后均值={b.mean():.3f}")
except Exception as e:
    check("核心框架导入", False, str(e))

# ═══════════════════════════════════════════════════════
# 2. cognitive-search-engine
# ═══════════════════════════════════════════════════════

try:
    sys.path.insert(0, r"D:\Reasonix\legacy\cognitive-search-engine")
    # 清理缓存后重新导入
    for k in list(sys.modules.keys()):
        if "cognitive" in k or "search_engine" in k:
            del sys.modules[k]
    from adapter import CognitiveSearchAdapter, bayesian_search_credibility

    # 测 Bayesian 函数
    b = bayesian_search_credibility("pubmed")
    check("CSE: bayesian_search_credibility", b is not None, f"类型={type(b).__name__}")

    # 测 adapter 方法
    adapter = CognitiveSearchAdapter()
    br = adapter.bayesian_engine_reliability("pubmed")
    check("CSE: bayesian_engine_reliability", "reliability" in br, f"可信度={br.get('reliability')}")

    bq = adapter.bayesian_search_quality(8, 10)
    check("CSE: bayesian_search_quality", "bayesian_posterior" in bq,
          f"后验={bq.get('bayesian_posterior')}")

    h = adapter.health()
    check("CSE: health含bayesian", "bayesian_health_score" in h,
          f"健康分={h.get('bayesian_health_score')}")
except Exception as e:
    check("cognitive-search-engine 验证", False, str(e))

# ═══════════════════════════════════════════════════════
# 3. fish-ecology-assistant
# ═══════════════════════════════════════════════════════

try:
    sys.path.insert(0, r"D:\Reasonix\legacy\fish-ecology-assistant")
    for k in list(sys.modules.keys()):
        if "fish_ecology_assistant" in k or "fish" in k and "core" not in k:
            del sys.modules[k]
    from fish_ecology_assistant.adapter import FishEcologyAdapter

    adapter = FishEcologyAdapter()

    v = adapter.bayesian_validate_claim("测试声明", supporting=5, contradicting=1)
    check("FEA: bayesian_validate_claim", v.get("verdict") in ("confirmed", "plausible"),
          f"判定={v.get('verdict')}, 后验={v.get('posterior_mean')}")
except Exception as e:
    check("fish-ecology-assistant 验证", False, str(e))

# ═══════════════════════════════════════════════════════
# 4. eon-core
# ═══════════════════════════════════════════════════════

try:
    sys.path.insert(0, r"D:\Reasonix\legacy\eon-core")
    for k in list(sys.modules.keys()):
        if "eon_core" in k:
            del sys.modules[k]
    from src.adapter import EonCoreAdapter

    adapter = EonCoreAdapter()
    h = adapter.health()
    check("EON: health含bayesian", "bayesian_coordination_confidence" in h,
          f"协调置信度={h.get('bayesian_coordination_confidence')}")
except Exception as e:
    check("eon-core 验证", False, str(e))

# ═══════════════════════════════════════════════════════
# 5. conflict-arbiter
# ═══════════════════════════════════════════════════════

try:
    sys.path.insert(0, r"D:\Reasonix\legacy\conflict-arbiter")
    for k in list(sys.modules.keys()):
        if "conflict_arbiter" in k:
            del sys.modules[k]
    from src.adapter import ConflictArbiterAdapter

    adapter = ConflictArbiterAdapter()
    h = adapter.health()
    check("CA: health含bayesian", "bayesian_confidence" in h,
          f"仲裁置信度={h.get('bayesian_confidence')}")
except Exception as e:
    check("conflict-arbiter 验证", False, str(e))

# ═══════════════════════════════════════════════════════
# 6. infrastructure
# ═══════════════════════════════════════════════════════

try:
    sys.path.insert(0, r"D:\Reasonix\legacy\infrastructure")
    for k in list(sys.modules.keys()):
        if "infrastructure" in k and "fish_ecology" not in k:
            del sys.modules[k]
    import infrastructure
    result = infrastructure.bayesian_emergence_score(10, 5, 1)
    check("INFRA: bayesian_emergence_score", isinstance(result, dict),
          f"z={result.get('z_score')}, signal={result.get('signal')}")
except Exception as e:
    check("infrastructure 验证", False, str(e))

# ═══════════════════════════════════════════════════════
# 7-9. Agents (porpoise, coilia, culter)
# ═══════════════════════════════════════════════════════

for agent_name in ["porpoise-agent", "coilia-agent", "culter-agent"]:
    try:
        sys.path.insert(0, rf"D:\Reasonix\legacy\{agent_name}")
        for k in list(sys.modules.keys()):
            if agent_name.replace("-", "_") in k:
                del sys.modules[k]

        # adapter 可能在 src/ 下
        import importlib
        mod = importlib.import_module(f"src.adapter")

        # 找到 adapter 类
        adapter_cls = None
        for attr in dir(mod):
            if attr.endswith("Adapter"):
                adapter_cls = getattr(mod, attr)
                break
        if adapter_cls:
            adapter = adapter_cls()
            h = adapter.health()
            has_bayesian = "bayesian_confidence" in h
            check(f"{agent_name}: health含bayesian", has_bayesian,
                  f"置信度={h.get('bayesian_confidence')}")
        else:
            check(f"{agent_name}: 未找到Adapter类", False)
    except Exception as e:
        check(f"{agent_name} 验证", False, str(e))

# ═══════════════════════════════════════════════════════
# 10. san-sheng-wanwu-core
# ═══════════════════════════════════════════════════════

try:
    sys.path.insert(0, r"D:\Reasonix\legacy\san-sheng-wanwu-core")
    for k in list(sys.modules.keys()):
        if "san_sheng" in k or "ssww" in k:
            del sys.modules[k]
    import src
    meta = src.bayesian_meta_confidence()
    check("SSWW: bayesian_meta_confidence", "meta_confidence" in meta,
          f"元认知置信度={meta.get('meta_confidence')}")

    calib = src.bayesian_calibrate([
        {"success": True, "confidence": 0.85},
        {"success": False, "confidence": 0.20},
    ])
    check("SSWW: bayesian_calibrate", "calibration_score" in calib,
          f"校准分数={calib.get('calibration_score')}")
except Exception as e:
    check("san-sheng-wanwu-core 验证", False, str(e))

# ═══════════════════════════════════════════════════════
# 汇总
# ═══════════════════════════════════════════════════════

print("=" * 60)
print(f"  Legacy Bayesian Integration Check")
print(f"  Pass: {PASS}/{PASS + FAIL}")
print("=" * 60)
for r in results:
    print(r)
print("=" * 60)

sys.exit(0 if FAIL == 0 else 1)
