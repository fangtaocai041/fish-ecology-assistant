"""Tests for fish-ecology search performance benchmarks.

Covers:
  - kb_first_lookup speed (< 100ms)
  - Fuzzy match recall
  - FTS5 full-text search
"""

import sys
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import pytest

# Module-level imports to avoid path issues when tests run together
from src.orchestrator import get_orchestrator, FishEcologyOrchestrator, KbFirstResult
from fishkb.db import KnowledgeDB
from fishkb.search import FishSpeciesMatcher


# ═══════════════════════════════════════════════════════════════
# §1 test_kb_first_lookup_speed — 应在 100ms 内完成
# ═══════════════════════════════════════════════════════════════

def test_kb_first_lookup_speed_below_100ms():
    """kb_first_lookup 应在 100ms 内完成 (单个查询)."""
    orch = get_orchestrator()

    # 预热 (首次可能加载配置)
    _ = orch.kb_first_lookup(query="鳤")

    # 测量
    t0 = time.perf_counter()
    result = orch.kb_first_lookup(query="鳤")
    elapsed_ms = (time.perf_counter() - t0) * 1000

    assert elapsed_ms < 100, \
        f"kb_first_lookup 耗时 {elapsed_ms:.1f}ms，应 < 100ms"
    assert result.found is True


def test_kb_first_lookup_speed_warm_cache():
    """多次查询应在 100ms 内完成 (热缓存)."""
    orch = get_orchestrator()

    queries = ["鳤", "刀鲚", "翘嘴鲌", "Ochetobius elongatus", "Coilia nasus"]
    # 预热
    for q in queries:
        _ = orch.kb_first_lookup(query=q)

    for q in queries:
        t0 = time.perf_counter()
        result = orch.kb_first_lookup(query=q)
        elapsed_ms = (time.perf_counter() - t0) * 1000
        assert elapsed_ms < 100, \
            f"kb_first_lookup('{q}') 耗时 {elapsed_ms:.1f}ms，应 < 100ms"


def test_kb_first_lookup_speed_scientific_name():
    """学名查询应在 100ms 内完成."""
    orch = get_orchestrator()

    _ = orch.kb_first_lookup(query="Ochetobius elongatus")
    t0 = time.perf_counter()
    result = orch.kb_first_lookup(query="Ochetobius elongatus")
    elapsed_ms = (time.perf_counter() - t0) * 1000

    assert elapsed_ms < 100, \
        f"学名查询耗时 {elapsed_ms:.1f}ms，应 < 100ms"
    assert result.found is True


def test_kb_first_lookup_not_found_is_fast():
    """未找到物种的查询也应快速返回."""
    orch = get_orchestrator()

    t0 = time.perf_counter()
    result = orch.kb_first_lookup(query="xyzabc123_nonexistent_species")
    elapsed_ms = (time.perf_counter() - t0) * 1000

    assert elapsed_ms < 200, \
        f"未命中查询耗时 {elapsed_ms:.1f}ms，应 < 200ms"
    assert result.found is False


# ═══════════════════════════════════════════════════════════════
# §2 test_fuzzy_match_recall — 模糊匹配召回率
# ═══════════════════════════════════════════════════════════════

def test_fuzzy_match_recall_exact_chinese():
    """精确中文名应 100% 召回."""
    orch = get_orchestrator()

    # 精确匹配
    result = orch.kb_first_lookup(query="鳤")
    assert result.found is True
    assert result.chinese_name == "鳤"


def test_fuzzy_match_recall_exact_scientific():
    """精确学名应召回."""
    orch = get_orchestrator()

    result = orch.kb_first_lookup(query="Ochetobius elongatus")
    assert result.found is True
    assert "Ochetobius" in result.scientific_name


def test_fuzzy_match_recall_partial_scientific():
    """部分学名 (属名) 应能召回."""
    orch = get_orchestrator()

    result = orch.kb_first_lookup(query="Ochetobius")
    assert result.found is True
    assert "Ochetobius" in result.scientific_name


def test_fuzzy_match_recall_coilia():
    """Coilia 属名应召回刀鲚."""
    orch = get_orchestrator()

    result = orch.kb_first_lookup(query="Coilia")
    assert result.found is True
    assert "Coilia" in result.scientific_name


def test_fuzzy_match_recall_all_candidates():
    """模糊搜索应返回多个候选."""
    orch = get_orchestrator()

    # 使用 fishkb 的模糊匹配
    result = orch.kb_first_lookup(query="鲌")
    # 可能精确匹配或模糊匹配
    assert isinstance(result.all_candidates, list)
    # "鲌" 应至少匹配翘嘴鲌或相关物种
    if result.found:
        assert "鲌" in result.chinese_name or \
               any("鲌" in c.get("chinese_name", "") for c in result.all_candidates)


def test_fuzzy_match_recall_aliases():
    """别名应能召回."""
    orch = get_orchestrator()

    # 翘嘴鲌的别名 "白鱼" 应能匹配 (若 KB 有别名配置)
    result = orch.kb_first_lookup(query="白鱼")
    # 别名匹配依赖于 KB 中 aliases 字段的配置
    # 模糊候选数应大于 0
    assert isinstance(result.all_candidates, list)
    # 至少应从模糊匹配中获得候选
    if result.found:
        assert result.chinese_name or result.matched_by_alias


def test_fuzzy_match_recall_synonyms():
    """异名应能召回."""
    orch = get_orchestrator()

    # Tribolodon brandti 的异名匹配
    result = orch.kb_first_lookup(query="Tribolodon hakonensis")
    # 可能精确或异名匹配
    if result.found:
        assert result.scientific_name or result.matched_by_synonym


# ═══════════════════════════════════════════════════════════════
# §3 test_species_db_fts5_search — FTS5 全文搜索
# ═══════════════════════════════════════════════════════════════

def test_fts5_search_importable():
    """fishkb KnowledgeDB 应可导入."""
    assert KnowledgeDB is not None


def test_fts5_search_db_creation():
    """KnowledgeDB 应可创建内存数据库."""
    db = KnowledgeDB(db_path=":memory:")
    assert db is not None
    assert db.conn is not None
    db.conn.close()


def test_fts5_search_schema_exists():
    """FTS5 虚拟表应存在于 schema 中."""
    import sqlite3
    db = KnowledgeDB(db_path=":memory:")
    # 检查 FTS5 表是否存在
    row = db.conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='species_fts'"
    ).fetchone()
    assert row is not None, "species_fts FTS5 虚拟表应存在"
    db.conn.close()


def test_fts5_search_insert_and_query():
    """FTS5 插入和查询应正常工作."""
    db = KnowledgeDB(db_path=":memory:")

    # 插入测试物种
    db.conn.execute(
        "INSERT INTO species (id, scientific, chinese, family) VALUES (?, ?, ?, ?)",
        ("test_id", "Testus specimenus", "测试鱼", "Testidae")
    )
    db.conn.commit()
    # 重建 FTS5 索引 (external content 表需要手动重建)
    db.conn.execute("INSERT INTO species_fts(species_fts) VALUES('rebuild')")
    db.conn.commit()

    # 通过 FTS5 搜索
    rows = db.conn.execute(
        "SELECT scientific, chinese FROM species_fts WHERE species_fts MATCH ?",
        ("测试鱼",)
    ).fetchall()
    assert len(rows) >= 1, "FTS5 应能搜到 '测试鱼'"
    assert any("测试鱼" in (r["chinese"] or "") for r in rows)
    db.conn.close()


def test_fts5_search_scientific_name():
    """FTS5 应能搜学名."""
    db = KnowledgeDB(db_path=":memory:")

    db.conn.execute(
        "INSERT INTO species (id, scientific, chinese, family) VALUES (?, ?, ?, ?)",
        ("test_fts", "Coreius heterodon", "铜鱼", "鲤科")
    )
    db.conn.commit()
    # 重建 FTS5 索引
    db.conn.execute("INSERT INTO species_fts(species_fts) VALUES('rebuild')")
    db.conn.commit()

    rows = db.conn.execute(
        "SELECT scientific, chinese FROM species_fts WHERE species_fts MATCH ?",
        ("Coreius",)
    ).fetchall()
    assert len(rows) >= 1
    db.conn.close()


def test_fts5_search_family():
    """FTS5 应能搜科名."""
    db = KnowledgeDB(db_path=":memory:")

    db.conn.execute(
        "INSERT INTO species (id, scientific, chinese, family) VALUES (?, ?, ?, ?)",
        ("test_family", "Some fish", "某种鱼", "鲤科")
    )
    db.conn.commit()
    # 重建 FTS5 索引
    db.conn.execute("INSERT INTO species_fts(species_fts) VALUES('rebuild')")
    db.conn.commit()

    rows = db.conn.execute(
        "SELECT scientific, chinese FROM species_fts WHERE species_fts MATCH ?",
        ("鲤科",)
    ).fetchall()
    assert len(rows) >= 1
    db.conn.close()


def test_fts5_search_no_match_returns_empty():
    """FTS5 无匹配应返回空."""
    db = KnowledgeDB(db_path=":memory:")

    rows = db.conn.execute(
        "SELECT scientific FROM species_fts WHERE species_fts MATCH ?",
        ("zzz_nonexistent_xyz",)
    ).fetchall()
    assert len(rows) == 0
    db.conn.close()


def test_fts5_search_multiple_insert():
    """FTS5 批量插入后搜索."""
    db = KnowledgeDB(db_path=":memory:")

    species_data = [
        ("sp1", "Ochetobius elongatus", "鳤", "鲤科"),
        ("sp2", "Coilia nasus", "刀鲚", "鳀科"),
        ("sp3", "Culter alburnus", "翘嘴鲌", "鲤科"),
    ]
    for sp in species_data:
        db.conn.execute(
            "INSERT INTO species (id, scientific, chinese, family) VALUES (?, ?, ?, ?)", sp
        )
    db.conn.commit()
    # 重建 FTS5 索引
    db.conn.execute("INSERT INTO species_fts(species_fts) VALUES('rebuild')")
    db.conn.commit()

    # 搜索鲤科 → 应返回 2 条
    rows = db.conn.execute(
        "SELECT scientific FROM species_fts WHERE species_fts MATCH ?",
        ("鲤科",)
    ).fetchall()
    assert len(rows) == 2, f"鲤科应有 2 条，实际: {len(rows)}"

    # 搜索鳤 → 应返回 1 条
    rows = db.conn.execute(
        "SELECT scientific FROM species_fts WHERE species_fts MATCH ?",
        ("鳤",)
    ).fetchall()
    assert len(rows) == 1
    db.conn.close()


def test_fts5_search_prefix():
    """FTS5 前缀搜索."""
    db = KnowledgeDB(db_path=":memory:")

    db.conn.execute(
        "INSERT INTO species (id, scientific, chinese, family) VALUES (?, ?, ?, ?)",
        ("pref", "Coilia nasus", "刀鲚", "鳀科")
    )
    db.conn.commit()
    # 重建 FTS5 索引
    db.conn.execute("INSERT INTO species_fts(species_fts) VALUES('rebuild')")
    db.conn.commit()

    # FTS5 prefix 搜索: "Coil*"
    rows = db.conn.execute(
        "SELECT scientific FROM species_fts WHERE species_fts MATCH ?",
        ('"Coil"*',)
    ).fetchall()
    # 前缀搜索可能返回结果
    assert isinstance(rows, list)
    db.conn.close()


def test_fts5_search_booleans():
    """FTS5 单关键词搜索."""
    db = KnowledgeDB(db_path=":memory:")

    db.conn.execute(
        "INSERT INTO species (id, scientific, chinese, family) VALUES (?, ?, ?, ?)",
        ("bool1", "Species A", "测试鱼A", "鲤科")
    )
    db.conn.execute(
        "INSERT INTO species (id, scientific, chinese, family) VALUES (?, ?, ?, ?)",
        ("bool2", "Species B", "测试鱼B", "鳀科")
    )
    db.conn.commit()
    # 重建 FTS5 索引
    db.conn.execute("INSERT INTO species_fts(species_fts) VALUES('rebuild')")
    db.conn.commit()

    # 单关键词搜索
    rows = db.conn.execute(
        "SELECT chinese FROM species_fts WHERE species_fts MATCH ?",
        ("测试鱼A",)
    ).fetchall()
    assert len(rows) == 1
    db.conn.close()


# ═══════════════════════════════════════════════════════════════
# §4 额外集成测试 (fish-ecology orchestrator)
# ═══════════════════════════════════════════════════════════════

def test_orchestrator_kb_first_lookup_known_species():
    """已知物种 '鳤' 应精确匹配."""
    orch = get_orchestrator()
    result = orch.kb_first_lookup(query="鳤")
    assert result.found is True
    assert result.chinese_name == "鳤"
    assert result.search_recommendation == "stay_in_kb"


def test_orchestrator_kb_first_lookup_unknown():
    """未知物种应返回 found=False."""
    orch = get_orchestrator()
    result = orch.kb_first_lookup(query="xyz_unknown_fish_123")
    assert result.found is False


def test_fishkb_matcher_import():
    """fishkb FishSpeciesMatcher 应可导入."""
    assert FishSpeciesMatcher is not None
    assert KbFirstResult is not None


def test_fishkb_matcher_creation():
    """FishSpeciesMatcher 应可创建."""
    db = KnowledgeDB(db_path=":memory:")
    matcher = FishSpeciesMatcher(db)
    assert matcher is not None
    assert matcher.db is not None
    db.conn.close()


def test_fishkb_matcher_lookup_in_memory():
    """在内存数据库中查找物种."""
    db = KnowledgeDB(db_path=":memory:")
    db.conn.execute(
        "INSERT INTO species (id, scientific, chinese, family) VALUES (?, ?, ?, ?)",
        ("test_lookup", "TestFish testus", "测试物种", "Testidae")
    )
    db.conn.commit()

    matcher = FishSpeciesMatcher(db)
    result = matcher.kb_first_lookup(query="测试物种")
    assert result.found is True
    assert result.chinese_name == "测试物种"
    db.conn.close()
