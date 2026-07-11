"""统计 _shared 各模块被 adapter 引用的次数"""
import os

base = "D:/Reasonix/fangtao_fishlab"
shared_dir = os.path.join(base, "_shared")

modules = sorted([f.replace(".py", "") for f in os.listdir(shared_dir) if f.endswith(".py") and f != "__init__.py"])
modules.remove("config_loader")  # 已接线，不计入
modules.remove("path_init")  # 已接线，不计入

for mod in modules:
    count = 0
    adapter_files = []
    for root, dirs, files in os.walk(base):
        for f in files:
            if f == "adapter.py":
                p = os.path.join(root, f)
                with open(p, "r", encoding="utf-8", errors="ignore") as fh:
                    c = fh.read()
                if "from _shared." + mod in c or "import _shared." + mod in c:
                    count += 1
                    adapter_files.append(os.path.relpath(p, base))
    print("{}: {} adapters\n".format(mod, count))
