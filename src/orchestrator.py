"""
FishEcologyOrchestrator — fish-ecology-assistant 主入口 API 层。

Usage:
    from src.orchestrator import get_orchestrator

    orch = get_orchestrator()
    result = orch.kb_first_lookup(query="鳤")
    print(result.summary_text)

KB-First 两阶段搜索:
  1. kb_first_lookup(query) — 先查本地知识库
  2. 根据 result.search_recommendation 判断是否启动全量搜索
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml

from .shared import JOURNAL_WHITELIST, build_search_queries, generate_ocr_variants

logger = logging.getLogger(__name__)

# ── Config paths ──
HERE = Path(__file__).resolve().parent
PROJECT_ROOT = HERE.parent
CONFIG_DIR = PROJECT_ROOT / "config"
SPECIES_KB_PATH = CONFIG_DIR / "fish_species_kb.yaml.bak"


# ── KbFirstResult ──

@dataclass
class KbFirstResult:
    """Result of a KB-first lookup.

    Attributes:
        found: Whether exact match found in KB.
        scientific_name: Matched scientific name (if found).
        chinese_name: Matched Chinese name.
        family: Taxonomic family.
        distribution: Distribution info.
        score: Credibility score from journal whitelist.
        search_recommendation: "stay_in_kb" if confident, "continue_to_c" if uncertain.
        summary_text: Human-readable summary for user display.
        candidates: List of near-match candidates (if not exact).
    """
    found: bool = False
    scientific_name: str = ""
    chinese_name: str = ""
    family: str = ""
    distribution: str = ""
    score: int = 0
    search_recommendation: str = "stay_in_kb"
    summary_text: str = ""
    candidates: List[Dict[str, Any]] = field(default_factory=list)


# ── FishEcologyOrchestrator ──

class FishEcologyOrchestrator:
    """鱼类生态学知识供给引擎 — 主入口 API 层。

    两阶段搜索的核心调度器：
      Tier 1: 本地知识库精确查询 (kb_first_lookup)
      Tier 2: 委托给 cognitive-search-engine 全量搜索
    """

    STAGES = ["Plan", "Search", "Analyze", "Write", "Review"]

    def __init__(self) -> None:
        self._species_db: Dict[str, Any] = {}
        self._load_species_db()

    # ── Public API ──

    def health(self) -> Dict[str, Any]:
        """健康检查。"""
        return {
            "project": "fish-ecology-assistant",
            "status": "HEALTHY" if self._species_db else "DEGRADED",
            "pipeline_stages": self.STAGES,
            "species_db_size": len(self._species_db.get("species", [])),
            "load_success": bool(self._species_db),
        }

    def info(self) -> Dict[str, Any]:
        """版本与能力信息。"""
        return {
            "project": "fish-ecology-assistant",
            "version": "6.5.0",
            "capabilities": {
                "kb_first_two_stage_search": True,
                "species_kb_query": True,
                "credibility_scoring": True,
                "cross_project_delegation": True,
            },
            "species_count": len(self._species_db.get("species", [])),
        }

    def kb_first_lookup(self, query: str, chinese: str = "") -> KbFirstResult:
        """KB-First 两阶段搜索 — 先查知识库。

        Args:
            query: 搜索关键词（学名或中文名）。
            chinese: 可选的中文名提示（跨项目调用时使用）。

        Returns:
            KbFirstResult 包含匹配结果与搜索建议。
        """
        query = query.strip()
        if not query:
            return KbFirstResult(
                found=False,
                search_recommendation="continue_to_c",
                summary_text="查询词为空，建议启动 c项目全量搜索。",
            )

        # 精确匹配
        match = self._find_species(query, chinese)
        if match:
            return self._build_found_result(match, query)

        # 近缘候选匹配
        candidates = self._find_candidates(query)
        if candidates:
            return self._build_candidate_result(candidates, query)

        return KbFirstResult(
            found=False,
            search_recommendation="continue_to_c",
            summary_text=f"知识库中未找到「{query}」的相关信息。建议启动全量搜索。",
            candidates=[],
        )

    # ── Internal matching ──

    def _load_species_db(self) -> None:
        """Load species knowledge base from YAML config."""
        try:
            if SPECIES_KB_PATH.exists():
                with open(SPECIES_KB_PATH, "r", encoding="utf-8") as f:
                    self._species_db = yaml.safe_load(f) or {}
                logger.info(f"Loaded species DB: {len(self._species_db.get('species', []))} species")
            else:
                logger.warning(f"Species KB not found at {SPECIES_KB_PATH}")
                self._species_db = {}
        except Exception as e:
            logger.error(f"Failed to load species DB: {e}")
            self._species_db = {}

    @staticmethod
    def _match_species(query: str, chinese: str, s_name: str, c_name: object) -> bool:
        """Check if query matches a species by scientific or Chinese name.

        Rules:
          1. query == scientific name (case-insensitive) → exact
          2. query == Chinese name → exact
          3. chinese param == Chinese name → cross-project call
          4. query is a substring (>=3 chars) of scientific name → partial

        c_name may be str or dict (some KB entries store synonyms as
        dicts with 'name' key). Both forms are handled.
        """
        q = query.strip().lower()
        s = s_name.lower() if s_name else ""

        # Normalize c_name: could be str or dict with 'name' key
        if isinstance(c_name, str):
            c = c_name.lower().strip() if c_name else ""
        elif isinstance(c_name, dict):
            raw = (c_name.get("name") or c_name.get("ref") or "")
            c = raw.lower().strip() if raw else ""
        else:
            c = ""

        if s and (q == s or (len(q) >= 3 and q in s)):
            return True
        if c and (q == c):
            return True
        if chinese and c and chinese == c:
            return True
        return False

    def _find_species(self, scientific: str, chinese: str = "") -> Optional[Dict[str, Any]]:
        """Search the flat species list in the knowledge base.

        Matches against: scientific name, Chinese name, aliases, AND synonyms.
        """
        species_list = self._species_db.get("species", [])
        for sp in species_list:
            s_name = sp.get("scientific", "") or sp.get("name", "")
            c_name = sp.get("chinese", "") or sp.get("c_name", "")

            if self._match_species(scientific, chinese, s_name, c_name):
                return sp

            # Check aliases
            for alias in sp.get("aliases", []):
                if self._match_species(scientific, chinese, "", alias):
                    return sp

            # Check synonyms
            for syn in sp.get("synonyms", []):
                if self._match_species(scientific, chinese, "", syn):
                    return sp

        return None

    def _find_candidates(self, query: str) -> List[Dict[str, Any]]:
        """Find near-match candidates using OCR variants."""
        ql = query.lower()
        candidates = []
        for sp in self._species_db.get("species", []):
            s_name = (sp.get("scientific", "") or sp.get("name", "")).lower()
            c_name = (sp.get("chinese", "") or sp.get("c_name", "")).lower()
            if ql in s_name or ql in c_name:
                candidates.append(sp)
        return candidates[:5]

    def _build_found_result(self, match: Dict[str, Any], query: str) -> KbFirstResult:
        s_name = match.get("scientific", "") or match.get("name", "")
        c_name = match.get("chinese", "") or match.get("c_name", "")
        family = match.get("family", "")
        dist = match.get("distribution", match.get("dist", ""))

        # Score by journal credibility
        refs = match.get("references", [])
        max_score = 0
        for ref in refs:
            journal = ref.get("journal", "") if isinstance(ref, dict) else ""
            score = JOURNAL_WHITELIST.get(journal, 0)
            if score > max_score:
                max_score = score

        recommendation = "stay_in_kb" if max_score >= 25 else "continue_to_c"

        lines = [f"✅ 知识库匹配: {s_name} ({c_name})"]
        if family:
            lines.append(f"  科: {family}")
        if dist:
            lines.append(f"  分布: {dist}")
        lines.append(f"  可信度评分: {max_score}")
        lines.append(f"  建议: {'知识库信息充足' if recommendation == 'stay_in_kb' else '建议启动全量搜索验证'}")

        return KbFirstResult(
            found=True,
            scientific_name=s_name,
            chinese_name=c_name,
            family=family,
            distribution=dist,
            score=max_score,
            search_recommendation=recommendation,
            summary_text="\n".join(lines),
        )

    def _build_candidate_result(self, candidates: List[Dict[str, Any]], query: str) -> KbFirstResult:
        lines = [f"🔍 未精确匹配「{query}」，但找到以下候选:", ""]
        cand_list = []
        for sp in candidates:
            s = sp.get("scientific", "") or sp.get("name", "")
            c = sp.get("chinese", "") or sp.get("c_name", "")
            lines.append(f"  • {s} ({c})")
            cand_list.append({"scientific": s, "chinese": c})
        lines.append("")
        lines.append("💡 可能是名称变体，建议用 c项目进行全量搜索。")

        return KbFirstResult(
            found=False,
            search_recommendation="continue_to_c",
            summary_text="\n".join(lines),
            candidates=cand_list,
        )


# ── Module-level cache for singleton pattern ──

_orchestrator_instance: Optional[FishEcologyOrchestrator] = None


def get_orchestrator() -> FishEcologyOrchestrator:
    """Factory function — 返回（缓存的）单例。

    同一进程中多次调用返回同一实例。
    """
    global _orchestrator_instance
    if _orchestrator_instance is None:
        _orchestrator_instance = FishEcologyOrchestrator()
    return _orchestrator_instance
