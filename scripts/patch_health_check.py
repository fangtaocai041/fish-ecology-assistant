"""Update health check with timing + local adapter_protocol first"""
import os

base = "D:/Reasonix/fangtao_fishlab"
path = os.path.join(base, "scripts", "health_check_all.py")

with open(path, "r", encoding="utf-8", errors="ignore") as f:
    c = f.read()

# 替换: 预加载 adapter_protocol 改为先本地
old_preload = """                # 预加载 adapter_protocol（确保 BayesianAdapterMixin 是最新版）
                import importlib
                _ = importlib.import_module("scripts.adapter_protocol")"""
new_preload = """                # 预加载 adapter_protocol（本地优先）
                import importlib
                for _mod in ["_shared.adapter_protocol", "scripts.adapter_protocol"]:
                    try:
                        importlib.import_module(_mod)
                        break
                    except ImportError:
                        continue"""
c = c.replace(old_preload, new_preload)

# 替换: comment 中的中文
c = c.replace("添加 legacy 根到路径，使 _bayesian 可用", "add lab root for _bayesian")

# 添加 timing: 测量每个 adapter 的耗时
import_timing = """                # timing + self_check
                _t0 = time.time()
                if hasattr(inst, "self_check"):"""
old_timing = """                # self_check
                if hasattr(inst, "self_check"):"""

if old_timing in c:
    c = c.replace(old_timing, import_timing)
    # 在返回前加 duration
    dur_insert = '                checks["details"]["duration_ms"] = round((time.time() - _t0) * 1000, 1)'
    health_insert = '                checks["details"]["duration_ms"] = round((time.time() - _t0) * 1000, 1)\n\n                # bayesian'
    c = c.replace("\n\n                # bayesian", health_insert)

# 给 print_report 的表格加 duration 列
old_header = 'detail_items = []'
new_header = 'detail_items = []\n            if "duration_ms" in d:\n                detail_items.append("t=" + str(d["duration_ms"]) + "ms")'
c = c.replace(old_header, new_header)

with open(path, "w", encoding="utf-8") as f:
    f.write(c)

print("Updated:", os.path.relpath(path, base))
