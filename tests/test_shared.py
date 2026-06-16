"""Tests for shared utilities — 共享工具函数测试。"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.shared import (
    JOURNAL_WHITELIST,
    build_search_queries,
    generate_ocr_variants,
)


def test_journal_whitelist_not_empty():
    assert len(JOURNAL_WHITELIST) > 0


def test_journal_whitelist_has_chinese_journals():
    chinese = [k for k in JOURNAL_WHITELIST if any("\u4e00" <= c <= "\u9fff" for c in k)]
    assert len(chinese) > 0


def test_journal_whitelist_has_international():
    intl = [k for k in JOURNAL_WHITELIST if all(c.isascii() or c.isspace() for c in k)]
    assert len(intl) > 0


def test_build_search_queries_with_chinese():
    queries = build_search_queries("Ochetobius elongatus", "鳤")
    assert len(queries) >= 1
    assert any("Ochetobius" in q for q in queries)


def test_build_search_queries_scientific_only():
    queries = build_search_queries("Tribolodon brandti")
    assert len(queries) >= 1


def test_generate_ocr_variants():
    variants = generate_ocr_variants("Ochetobius")
    assert isinstance(variants, list)


def test_generate_ocr_variants_with_limit():
    variants = generate_ocr_variants("Ochetobius", limit=5)
    assert isinstance(variants, list)
    assert len(variants) <= 5
