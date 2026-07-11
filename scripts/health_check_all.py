"""
旧项目统一健康检查 — 一键调用所有9个项目的 self_check()
"""
import sys
import os
import json
import time

base = "D:/Reasonix/fangtao_fishlab"
bayesian_path = "D:/Reasonix"

PROJECTS = [
    ("cognitive-search-engine", "src.adapter", "CognitiveSearchAdapter", "adapter"),
    ("fish-ecology-assistant", "src.adapter", "FishEcologyAdapter", "adapter"),
    ("eon-core", "src.adapter", "EonCoreAdapter", "adapter"),
    ("conflict-arbiter", "src.adapter", "ConflictArbiterAdapter", "adapter"),
    ("porpoise-agent", "src.adapter", "PorpoiseAdapter", "adapter"),
    ("coilia-agent", "src.adapter", "CoiliaAdapter", "adapter"),
    ("culter-agent", "src.adapter", "CulterAdapter", "adapter"),
    ("infrastructure", "__init__", None, "package"),
    ("san-sheng-wanwu-core", "src.__init__", None, "package"),
]


def check_all() -> dict:
    """调用所有旧项目的 self_check()，返回汇总"""
    saved_path = list(sys.path)
    saved_modules = set(sys.modules)
    results = {}

    for proj_name, mod_path, cls_name, ptype in PROJECTS:
        proj_root = os.path.join(base, proj_name)
        checks = {"project": proj_name, "status": "UNKNOWN", "details": {}}

        try:
            if ptype == "adapter":
                # 清理 + 设置路径 (add lab root for _bayesian)
                sys.path = saved_path + [bayesian_path, base, proj_root]
                for k in list(sys.modules):
                    if "src" in k or "adapter" in k or "scripts" in k:
                        del sys.modules[k]
                # 预加载 adapter_protocol（本地优先）
                import importlib
                for _mod in ["_shared.adapter_protocol", "scripts.adapter_protocol"]:
                    try:
                        importlib.import_module(_mod)
                        break
                    except ImportError:
                        continue
                mod = importlib.import_module(mod_path)
                cls = getattr(mod, cls_name)
                inst = cls()
                checks["details"]["import"] = "OK"
                checks["details"]["_orchestrator_loaded"] = str(
                    getattr(inst, "_orchestrator", None) is not None
                )

                # timing + self_check
                _t0 = time.time()
                if hasattr(inst, "self_check"):
                    sc = inst.self_check()
                    # 兼容新旧两种返回类型
                    if hasattr(sc, "score"):
                        checks["details"]["self_check"] = sc.summary()
                        all_ok = sc.is_healthy
                    elif isinstance(sc, dict):
                        checks["details"]["self_check"] = sc
                        all_ok = sc.get("all_ok", False)
                    else:
                        checks["details"]["self_check"] = str(sc)[:80]
                        all_ok = False
                else:
                    all_ok = False
                _t0_elapsed = round((time.time() - _t0) * 1000, 1)
                checks["details"]["duration_ms"] = _t0_elapsed

                # bayesian methods count
                bs = [x for x in dir(inst) if x.startswith("bayesian_")]
                checks["details"]["bayesian_methods"] = bs

                # health — 使用 normalize_health 统一格式
                try:
                    h = inst.health()
                    if hasattr(inst, "normalize_health"):
                        h = inst.normalize_health(h)
                    checks["details"]["health_status"] = h.get("status", "?")
                    checks["details"]["has_bayesian_confidence"] = "bayesian_confidence" in h
                except Exception as e:
                    checks["details"]["health_error"] = str(e)[:60]

                checks["status"] = "PASS" if all_ok else "DEGRADED"

            else:  # package
                sys.path = saved_path + [bayesian_path, base]
                if proj_name == "infrastructure":
                    # 还需基础设施自己的目录
                    sys.path.insert(0, os.path.join(base, "infrastructure"))

                for k in list(sys.modules):
                    if proj_name in k or "infrastructure" in k or "san_sheng" in k:
                        del sys.modules[k]

                if proj_name == "infrastructure":
                    import importlib
                    pkg = importlib.import_module("infrastructure")
                else:
                    sys.path.insert(0, os.path.join(base, proj_name))
                    sys.path.insert(0, os.path.join(base, proj_name, "src"))
                    import src as pkg

                checks["details"]["import"] = "OK"

                if hasattr(pkg, "self_check"):
                    sc = pkg.self_check()
                    checks["details"]["self_check"] = sc
                    all_ok = sc.get("all_ok", False) if isinstance(sc, dict) else False
                else:
                    all_ok = False

                checks["status"] = "PASS" if all_ok else "DEGRADED"

        except Exception as e:
            checks["status"] = "FAIL"
            checks["details"]["error"] = str(e)[:120]

        results[proj_name] = checks
        sys.path = saved_path

    return results


def print_report(results: dict):
    """打印格式化报告"""
    print("=" * 65)
    print("  Legacy Projects — Unified Health Check")
    print("=" * 65)

    pass_count = 0
    for name, r in results.items():
        status = r["status"]
        if status == "PASS":
            pass_count += 1
            tag = "PASS"
        elif status == "DEGRADED":
            tag = "DEGR"
        else:
            tag = "FAIL"

        d = r["details"]
        detail_items = []
        if "duration_ms" in d:
            detail_items.append("t=" + str(d["duration_ms"]) + "ms")
        if "health_status" in d:
            detail_items.append("health=" + d["health_status"])
        if "bayesian_in_health" in d:
            detail_items.append("bayesian=" + ("Y" if d["bayesian_in_health"] else "n"))
        if "bayesian_methods" in d and d["bayesian_methods"]:
            detail_items.append("methods=" + str(len(d["bayesian_methods"])))
        if "self_check" in d:
            sc = d["self_check"]
            if isinstance(sc, dict):
                detail_items.append("checks=" + str({k: v for k, v in sc.items() if k != "all_ok"}))
        detail_str = " | ".join(detail_items) if detail_items else ""

        print("  [{}] {}  {}".format(tag, name.ljust(28), detail_str))
        if "error" in d:
            print("       ERROR: " + d["error"][:80])

    total = len(results)
    print()
    print("  Summary: {}/{} PASS".format(pass_count, total))
    print("=" * 65)
    return pass_count == total


if __name__ == "__main__":
    results = check_all()
    ok = print_report(results)
    sys.exit(0 if ok else 1)
