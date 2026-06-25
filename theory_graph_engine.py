#!/usr/bin/env python3
"""
theory_graph_engine — 根级 shim，向后兼容

实际实现在 src/theory_graph_engine.py。
留此文件保持 from theory_graph_engine import TheoryGraph 继续可用。
"""
import sys
from pathlib import Path

# Force project root to front of sys.path to resolve src correctly
_PROJECT_ROOT = str(Path(__file__).resolve().parent)
if _PROJECT_ROOT in sys.path:
    sys.path.remove(_PROJECT_ROOT)
sys.path.insert(0, _PROJECT_ROOT)

# Load via importlib to avoid src namespace conflicts
import importlib.util as _util

_spec = _util.find_spec("src.theory_graph_engine")
if _spec is None:
    raise ImportError(
        "src.theory_graph_engine not found. "
        "Expected at: " + str(Path(_PROJECT_ROOT) / "src" / "theory_graph_engine.py")
    )

_mod = _util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
sys.modules["theory_graph_engine_src"] = _mod  # avoid polluting src.theory_graph_engine

TheoryGraph = _mod.TheoryGraph
__all__ = ["TheoryGraph"]

if __name__ == '__main__':
    tg = TheoryGraph()
    import json
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        arg = sys.argv[2] if len(sys.argv) > 2 else None
        cmds = {
            'route': lambda: tg.route(arg),
            'fitness': lambda: f"{arg}: {tg.fitness_score(arg)}",
            'report': lambda: tg.full_report(arg),
            'matrix': lambda: tg.topology_heatmap(),
            'emergence': lambda: tg.emergence_density(arg),
        }
        if cmd in cmds:
            result = cmds[cmd]()
            print(json.dumps(result, ensure_ascii=False, indent=2)
                  if isinstance(result, (dict, list)) else result)
        else:
            print(f"Usage: python theory_graph_engine.py [route|fitness|report|matrix|emergence] <args>")
    else:
        print(f"TheoryGraph v4.0 (src/) | loaded via importlib")
