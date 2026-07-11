"""统一所有 adapter 的 import 为三阶：_shared → scripts → object"""
import os, glob

base = "D:/Reasonix/fangtao_fishlab"
target = """try:
    from _shared.adapter_protocol import IProjectAdapter, BayesianAdapterMixin
except ImportError:
    try:
        from scripts.adapter_protocol import IProjectAdapter, BayesianAdapterMixin
    except ImportError:
        IProjectAdapter = object
        BayesianAdapterMixin = object
"""

fix = """try:
    from _shared.adapter_protocol import IProjectAdapter, BayesianAdapterMixin
except ImportError:
    try:
        from scripts.adapter_protocol import IProjectAdapter, BayesianAdapterMixin
    except ImportError:
        IProjectAdapter = object
        BayesianAdapterMixin = object
"""

count = 0
for root, dirs, files in os.walk(base):
    dirs[:] = [d for d in dirs if d not in ("__pycache__", ".git", ".reasonix")]
    for f in files:
        if f == "adapter.py":
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8", errors="ignore") as fh:
                c = fh.read()
            
            old_2level = 'try:\n    from _shared.adapter_protocol import IProjectAdapter, BayesianAdapterMixin\nexcept ImportError:\n    IProjectAdapter = object\n    BayesianAdapterMixin = object'
            if old_2level in c:
                c = c.replace(old_2level, fix)
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(c)
                count += 1
                print("Fixed 2->3: {}".format(os.path.relpath(path, base)))
                continue
            
            # 也处理还留在 scripts. 的
            old_scripts = 'try:\n    from scripts.adapter_protocol import IProjectAdapter, BayesianAdapterMixin\nexcept ImportError:\n    IProjectAdapter = object\n    BayesianAdapterMixin = object'
            if old_scripts in c:
                c = c.replace(old_scripts, fix)
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(c)
                count += 1
                print("Fixed scripts->3: {}".format(os.path.relpath(path, base)))

print("\nTotal: {} files updated".format(count))
