"""
fangtao_fishlab 路径初始化 — 所有子项目共享，消除重复

使用方式（在每个 adapter.py 顶部）:
    from _shared.path_init import ensure_paths
    ensure_paths(__file__)
"""

import sys
from pathlib import Path


def ensure_paths(source_file: str) -> None:
    """确保 fangtao_fishlab 和 D:/Reasonix 在 sys.path 中

    Args:
        source_file: 调用方的 __file__，用于计算相对路径
    """
    # D:/Reasonix/fangtao_fishlab
    _here = Path(source_file).resolve()
    # 从 adapter.py 位置向上找 fangtao_fishlab 根目录
    # adapter 位于 fangtao_fishlab/<project>/src/adapter.py
    _lab_root = None
    for parent in _here.parents:
        if (parent / "__init__.py").exists() and (parent / "_bayesian").exists():
            _lab_root = parent
            break

    if _lab_root and str(_lab_root) not in sys.path:
        sys.path.insert(0, str(_lab_root))

    # D:/Reasonix (scripts/adapter_protocol 所在)
    _reasonix_root = _here.parents[3] if len(list(_here.parents)) >= 4 else None
    # 更可靠的方式：往上找到有 scripts/ 的目录
    for parent in _here.parents:
        if (parent / "scripts" / "adapter_protocol.py").exists():
            _reasonix_root = parent
            break

    if _reasonix_root and str(_reasonix_root) not in sys.path:
        sys.path.insert(0, str(_reasonix_root))
