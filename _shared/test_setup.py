"""Shared test setup for all fangtao_fishlab projects"""
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent  # fangtao_fishlab root
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))
_reasonix = _ROOT.parent  # D:/Reasonix
if str(_reasonix) not in sys.path:
    sys.path.insert(0, str(_reasonix))
# fishkb nested package
_fishkb = _ROOT / "fish-ecology-assistant" / "fishkb"
if _fishkb.is_dir() and str(_fishkb) not in sys.path:
    sys.path.insert(0, str(_fishkb))
# Clear module cache
for k in list(sys.modules):
    if k in ("scripts", "adapter", "src", "shared_types") or k.startswith(
        ("scripts.", "src.", "adapter.", "shared_types.")
    ):
        del sys.modules[k]
