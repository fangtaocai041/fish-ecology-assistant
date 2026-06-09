"""FishEcologyAdapter — fish-ecology-assistant (V0 / S-State).

【核心专精】lookup_species(name: str) → SpeciesProfile
    长江 443 种鱼类知识库查询 + 可信度评分
    → 通路 P1(→cognitive) P2(←cognitive)

Exposes fish ecology knowledge supply as a Python-callable interface.
Uses FishEcologyOrchestrator when available, falls back to direct
species DB + config loading for minimal viable operation.
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)

# Import shared adapter protocol (workspace root on sys.path)
try:
    from scripts.adapter_protocol import IProjectAdapter
except ImportError:
    IProjectAdapter = object  # fallback for standalone usage


class FishEcologyAdapter(IProjectAdapter):
    """Adapter for fish-ecology-assistant (V0 — 知识供给层).

    Two-tier operation:
      Tier 1: FishEcologyOrchestrator (full pipeline via Reasonix skills)
      Tier 2: Direct species DB lookup (minimal viable fallback)
    """

    project_name = "fish-ecology-assistant"

    # Credibility scoring journal whitelist
    JOURNAL_WHITELIST: Dict[str, int] = {
        "水生生物学报": 25, "中国水产科学": 25, "水产学报": 25,
        "生物多样性": 25, "湖泊科学": 25, "生态学报": 25,
        "Scientific Reports": 30, "PLOS ONE": 30, "Gene": 30,
    }

    def __init__(self) -> None:
        self._orchestrator: Any = None
        self._species_db: Dict[str, Any] = {}
        self._init()

    def _init(self) -> None:
        """Try orchestrator first, fall back to direct config load."""
        try:
            from .orchestrator import FishEcologyOrchestrator
            self._orchestrator = FishEcologyOrchestrator()
        except ImportError:
            self._load_species_db()

    def _load_species_db(self) -> None:
        """Direct load of species knowledge base."""
        try:
            import yaml
            cfg = Path(__file__).resolve().parent.parent / "config" / "yangtze_fish_species.yaml"
            if cfg.is_file():
                self._species_db = yaml.safe_load(cfg.read_text(encoding="utf-8")) or {}
        except Exception:
            pass

    # ── IProjectAdapter interface ──

    def search(self, query: str, **kwargs) -> Dict[str, Any]:
        """Execute a fish ecology search.

        Tier 1: Full orchestrator pipeline (DELEGATE protocol).
        Tier 2: Species DB lookup + search query generation.
        """
        if self._orchestrator:
            return self._orchestrator.delegate_search(
                kwargs.get("species", query),
                kwargs.get("chinese_name", ""),
                **kwargs,
            )

        # Tier 2: Direct species lookup
        species_name = kwargs.get("species", query)
        species_key = species_name.replace(" ", "_").lower()
        species_data = self._species_db.get(species_key, {})
        chinese_name = kwargs.get("chinese_name", species_data.get("chinese_name", ""))

        return {
            "status": "ok",
            "tier": "direct_db",
            "scientific_name": species_name,
            "chinese_name": chinese_name,
            "known_species": bool(species_data),
            "species_data": species_data,
            "search_queries": self._build_queries(species_name, chinese_name),
            "ocr_variants": self._ocr_variants(species_name),
            "sources": ["pubmed", "crossref", "openalex", "cnki", "cscd", "wanfang"],
        }

    def health(self) -> Dict[str, Any]:
        if self._orchestrator:
            return self._orchestrator.health()
        return {
            "project": self.project_name,
            "status": "HEALTHY" if self._species_db else "DEGRADED",
            "tier": "direct_db" if not self._orchestrator else "orchestrator",
            "species_db_size": len(self._species_db),
        }

    def info(self) -> Dict[str, Any]:
        if self._orchestrator:
            return self._orchestrator.info()
        return {
            "project": self.project_name,
            "role": "V0_SupplyVertex (S-State)",
            "symbol": "☀️ 太阳·老阳",
            "capabilities": ["species_knowledge_base", "credibility_scoring",
                           "ocr_variant_generation", "multi_engine_search"],
        }

    # ── Helpers ──

    def _build_queries(self, scientific: str, chinese: str) -> List[str]:
        queries = [scientific]
        if chinese:
            queries.append(chinese)
        for direction in ["genetic", "morphology", "ecology", "survey"]:
            queries.append(f"{scientific} {direction}")
        return queries

    def _ocr_variants(self, name: str) -> List[str]:
        variants = set()
        confusable = {"u": ["b"], "b": ["u"], "i": ["l", "e"], "l": ["i"]}
        for i, ch in enumerate(name):
            if ch.lower() in confusable:
                for sub in confusable[ch.lower()]:
                    variants.add(name[:i] + sub + name[i + 1:])
        for n in range(1, min(4, len(name))):
            variants.add(name[:-n])
        return list(variants)[:15]


def get_adapter() -> FishEcologyAdapter:
    return FishEcologyAdapter()
