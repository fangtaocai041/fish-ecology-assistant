"""Replace scripts.adapter_protocol import with _shared.adapter_protocol"""
import os

base = "D:/Reasonix/fangtao_fishlab"
old = 'from scripts.adapter_protocol import IProjectAdapter, BayesianAdapterMixin\n'
new = 'from _shared.adapter_protocol import IProjectAdapter, BayesianAdapterMixin\n'

count = 0
for root, dirs, files in os.walk(base):
    dirs[:] = [d for d in dirs if d not in ("__pycache__", ".git", ".reasonix")]
    for f in files:
        if f == "adapter.py":
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8", errors="ignore") as fh:
                c = fh.read()
            if old in c:
                c = c.replace(old, new)
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(c)
                count += 1
                print("  {}".format(os.path.relpath(path, base)))

print("\nUpdated: {} files".format(count))
