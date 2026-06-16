"""FishEcologyAdapter — fish-ecology-assistant (三角核心·知识供给).

核心专精: lookup_species(name: str) → SpeciesProfile
    长江 443 种鱼类知识库查询 + 可信度评分
    通路: P1(fish→cognitive) P2(cognitive→fish)

Exposes fish ecology knowledge supply as a Python-callable interface.
Uses FishEcologyOrchestrator when available, falls back to direct
species DB + config loading for minimal viable operation.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

from .shared import JOURNAL_WHITELIST, build_search_queries, generate_ocr_variants

logger = logging.getLogger(__name__)


@dataclass
class SpeciesProfile:
    """物种档案 — 知识供给层的标准输出格式。"""
    scientific_name: str = ""
    chinese_name: str = ""
    family: str = ""
    distribution: str = ""
    status: str = "unknown"
    references: List[Dict[str, str]] = field(default_factory=list)
    credibility_score: int = 0
    source: str = "kb"  # kb / cognitive / mixed


class FishEcologyAdapter:
    """Adapter for fish-ecology-assistant (V0 — 知识供给层).

    Two-tier operation:
      Tier 1: FishEcologyOrchestrator (full pipeline via Reasonix skills)
      Tier 2: Direct species DB lookup (minimal viable fallback)
    """

    project_name = "fish-ecology-assistant"

    def __init__(self) -> None:
        self._orchestrator: Any = None
        self._species_db: Dict[str, Any] = {}
        self._init()

    def _init(self) -> None:
        """Try orchestrator first, fall back to direct config load."""
        try:
            from .orchestrator import FishEcologyOrchestrator
            self._orchestrator = FishEcologyOrchestrator()
            logger.info("Orchestrator loaded — full pipeline available")
        except ImportError:
            self._load_species_db()
            logger.info("Orchestrator unavailable — using direct species DB")

    def _load_species_db(self) -> None:
        """Fallback: load species DB directly from YAML."""
        import yaml
        kb_path = Path(__file__).resolve().parent.parent / "config" / "fish_species_kb.yaml.bak"
        if kb_path.exists():
            with open(kb_path, "r", encoding="utf-8") as f:
                self._species_db = yaml.safe_load(f) or {}

    def lookup_species(self, name: str) -> SpeciesProfile:
        """Look up a species by scientific or Chinese name.

        Two-tier:
          Tier 1: Full orchestrator pipeline (with credibility scoring)
          Tier 2: Direct species DB scan

        Returns:
            SpeciesProfile with best available information.
        """
        if self._orchestrator:
            result = self._orchestrator.kb_first_lookup(query=name)
            if result.found:
                return SpeciesProfile(
                    scientific_name=result.scientific_name,
                    chinese_name=result.chinese_name,
                    family=result.family,
                    distribution=result.distribution,
                    credibility_score=result.score,
                    source="kb",
                )
        return self._direct_lookup(name)

    def _direct_lookup(self, name: str) -> SpeciesProfile:
        """Direct species DB scan (Tier 2 fallback)."""
        query = name.lower().strip()
        for sp in self._species_db.get("species", []):
            s_name = (sp.get("scientific", "") or sp.get("name", "")).lower()
            c_name = (sp.get("chinese", "") or sp.get("c_name", "")).lower()
            if query in s_name or query == c_name:
                return SpeciesProfile(
                    scientific_name=sp.get("scientific", "") or sp.get("name", ""),
                    chinese_name=sp.get("chinese", "") or sp.get("c_name", ""),
                    family=sp.get("family", ""),
                    distribution=sp.get("distribution", sp.get("dist", "")),
                    credibility_score=10,
                    source="kb",
                )
        return SpeciesProfile(source="kb")

    def health(self) -> Dict[str, Any]:
        """健康检查。"""
        return {
            "project": self.project_name,
            "orchestrator_available": self._orchestrator is not None,
            "species_db_loaded": bool(self._species_db) or bool(self._orchestrator),
        }
