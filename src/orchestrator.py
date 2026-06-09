"""FishEcologyOrchestrator — Python orchestrator for fish-ecology-assistant.

Bridges the gap between the Reasonix skill-based pipeline (28 markdown skills,
5-stage Plan→Search→Analyze→Write→Review) and programmatic cross-project access.

This is NOT a replacement for the Reasonix skill system — it's a lightweight
Python wrapper that:
  1. Loads species knowledge base (fish_species_kb.yaml — multi-basin)
  2. Generates DELEGATE protocol messages for Reasonix skill dispatch
  3. Provides structured data access for other projects via adapter.py
  4. Validates queries against known species/configurations

Usage:
    from src.orchestrator import FishEcologyOrchestrator
    orch = FishEcologyOrchestrator()
    result = orch.delegate_search("Ochetobius elongatus", chinese_name="鳤")
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)


class FishEcologyOrchestrator:
    """Lightweight Python orchestrator for fish-ecology knowledge supply.

    Loads configs at init, provides structured access to species data,
    and generates Reasonix DELEGATE protocol messages for skill dispatch.
    """

    # Pipeline stages (from research-orchestrator.md)
    STAGES = ["Plan", "Search", "Analyze", "Write", "Review"]

    # Credibility scoring journal whitelist (from v5.0 rules)
    JOURNAL_WHITELIST: Dict[str, int] = {
        "水生生物学报": 25, "中国水产科学": 25, "水产学报": 25,
        "生物多样性": 25, "湖泊科学": 25, "南方水产科学": 25,
        "生态科学": 20, "生态学报": 25,
        "Scientific Data": 30, "Scientific Reports": 30, "Animals": 30,
        "Gene": 30, "Mitochondrial DNA": 30, "Conserv Genet Resour": 30,
        "PLOS ONE": 30,
    }

    def __init__(self) -> None:
        self._project_root = Path(__file__).resolve().parent.parent
        self._agent_config: Dict[str, Any] = {}
        self._species_db: Dict[str, Any] = {}
        self._load_configs()

    def _load_configs(self) -> None:
        """Load agent.yaml and fish_species_kb.yaml (multi-basin)."""
        try:
            import yaml
            agent_cfg = self._project_root / "config" / "agent.yaml"
            if agent_cfg.is_file():
                self._agent_config = yaml.safe_load(agent_cfg.read_text(encoding="utf-8")) or {}

            species_cfg = self._project_root / "config" / "fish_species_kb.yaml"
            if not species_cfg.is_file():
                species_cfg = self._project_root / "config" / "yangtze_fish_species.yaml"
            if species_cfg.is_file():
                self._species_db = yaml.safe_load(species_cfg.read_text(encoding="utf-8")) or {}
        except Exception as exc:
            logger.warning(f"Config load failed: {exc}")

    # ── Public API ──

    def delegate_search(
        self, scientific_name: str, chinese_name: str = "", **kwargs
    ) -> Dict[str, Any]:
        """Cross-project entry point. Returns species data + search hints.

        Searches across: dominant_species, protected_species, and
        individual species entries in the knowledge base.
        """
        species_data = self._find_species(scientific_name, chinese_name)
        cn_name = chinese_name or species_data.get("chinese_name", species_data.get("name", ""))

        # Build result with real species data
        result: Dict[str, Any] = {
            "status": "ok",
            "scientific_name": scientific_name,
            "chinese_name": cn_name,
            "known_species": bool(species_data),
            "species_data": species_data,
            "search_queries": self._build_search_queries(scientific_name, cn_name),
            "ocr_variants": self._generate_ocr_variants(scientific_name),
        }

        # IF known species THEN include taxonomy + research hints
        if species_data:
            result.update({
                "family": species_data.get("family", ""),
                "order": species_data.get("order", ""),
                "iucn_status": species_data.get("iucn", ""),
                "habitat": species_data.get("habitat", ""),
                "max_length_cm": species_data.get("max_length_cm", ""),
            })

        # Always include DELEGATE protocol for full pipeline
        result["delegate"] = {
            "protocol": "DELEGATE",
            "target": "fish-ecology-assistant",
            "skill": "research-orchestrator",
            "pipeline": self.STAGES,
            "max_revision_rounds": 3,
        }

        return result

    @staticmethod
    def _match_species(query: str, chinese: str, s_name: str, c_name: str) -> bool:
        """Check if query matches a species by scientific or Chinese name.

        知识库精确匹配规则 (f项目不做模糊):
          1. query == 学名 (大小写不敏感) ← 优先
          2. query == 中文名 ← 精确
          3. chinese 参数 == 中文名 ← 跨项目调用
          4.学名子串匹配 ← 支持部分拉丁名查询如 "Ochetobius"

        ❌ 无中文名字串匹配 — 模糊搜索是 c项目的职责
        """
        q = query.strip().lower()
        s = s_name.lower() if s_name else ""
        c = c_name.lower() if c_name else ""

        if s and (q == s or (len(q) >= 3 and q in s)):
            return True
        if c and (q == c):
            return True
        if chinese and c and chinese == c:
            return True
        return False

    def _find_species(self, scientific: str, chinese: str = "") -> Dict[str, Any]:
        """Search the flat species list in the knowledge base.

        New multi-basin format: self._species_db["species"] is a list of
        species dicts, each with name/scientific/distribution fields.
        Falls back to old section-based format for backward compat.
        """
        # ── NEW: flat species list ──
        species_list = self._species_db.get("species", [])
        if species_list:
            for item in species_list:
                if not isinstance(item, dict):
                    continue
                s_name = item.get("scientific", "")
                c_name = item.get("name", "")
                aliases = item.get("aliases", []) or []
                if self._match_species(scientific, chinese, s_name, c_name):
                    return {
                        "chinese_name": c_name,
                        "scientific_name": s_name,
                        "aliases": aliases,
                        "family": item.get("family", ""),
                        "conservation": item.get("conservation", ""),
                        "category": item.get("category", ""),
                        "distribution": item.get("distribution", {}),
                        **item,
                    }
                # Also match against aliases
                for alias in aliases:
                    if self._match_species(scientific, chinese, "", alias):
                        return {
                            "chinese_name": alias,
                            "scientific_name": s_name,
                            "aliases": aliases,
                            "family": item.get("family", ""),
                            "conservation": item.get("conservation", ""),
                            "category": item.get("category", ""),
                            "distribution": item.get("distribution", {}),
                            "matched_by_alias": True,
                            **item,
                        }
            return {}

        # ── FALLBACK: old section-based format ──
        for section_key in ["dominant_species", "protected_species", "key_endangered_species_in_graph"]:
            section = self._species_db.get(section_key, []) or []
            if not isinstance(section, list):
                continue
            for item in section:
                if not isinstance(item, dict):
                    continue
                s_name = item.get("scientific", "")
                c_name = item.get("name", "")
                if self._match_species(scientific, chinese, s_name, c_name):
                    return {**item, "chinese_name": c_name, "scientific_name": s_name,
                            "section": section_key}

        return {}

    def lookup_species(self, scientific_name: str) -> Dict[str, Any]:
        """Look up a species in the knowledge base."""
        return self._find_species(scientific_name)

    def list_species(self, family: str = "", limit: int = 50,
                     basin: str = "", country: str = "") -> List[Dict[str, Any]]:
        """List species from the knowledge base, filterable by family/basin/country.

        Args:
            family: Filter by family name (e.g. "鲤科")
            limit: Max results (default 50)
            basin: Filter by basin name (e.g. "长江流域", "图们江流域")
            country: Filter by country name (e.g. "中国")
        """
        results = []

        # ── NEW: flat species list ──
        species_list = self._species_db.get("species", [])
        if species_list:
            for item in species_list:
                if not isinstance(item, dict):
                    continue
                if family and item.get("family", "") != family:
                    continue
                dist = item.get("distribution", {})
                if basin:
                    item_basins = dist.get("basins", []) or []
                    if basin not in item_basins:
                        continue
                if country:
                    item_countries = dist.get("countries", []) or []
                    if country not in item_countries:
                        continue
                results.append({
                    "chinese_name": item.get("name", ""),
                    "scientific_name": item.get("scientific", ""),
                    "family": item.get("family", ""),
                    "category": item.get("category", ""),
                    "distribution": dist,
                    "conservation": item.get("conservation", ""),
                })
                if len(results) >= limit:
                    return results
            return results

        # ── FALLBACK: old section-based format ──
        for item in self._species_db.get("dominant_species", []) or []:
            if not isinstance(item, dict):
                continue
            if family and item.get("family", "") != family:
                continue
            results.append({
                "chinese_name": item.get("name", ""),
                "scientific_name": item.get("scientific", ""),
                "family": item.get("family", ""),
                "section": "dominant",
            })
            if len(results) >= limit:
                return results

        return results

    def score_credibility(self, journal: str, has_doi: bool = False,
                          has_pmid: bool = False, is_preprint: bool = False) -> int:
        """Compute credibility score [0-100] for a paper.

        credibility_score = 50 (baseline)
          + journal_whitelist_bonus
          + 10 IF has_doi
          + 10 IF has_pmid
          - 30 IF is_preprint
        """
        score = 50
        for jname, bonus in self.JOURNAL_WHITELIST.items():
            if jname in journal:
                score += bonus
                break
        if has_doi:
            score += 10
        if has_pmid:
            score += 10
        if is_preprint:
            score -= 30
        return max(0, min(100, score))

    def health(self) -> Dict[str, Any]:
        """Health check."""
        return {
            "project": "fish-ecology-assistant",
            "status": "HEALTHY" if self._agent_config else "DEGRADED",
            "config_loaded": bool(self._agent_config),
            "species_db_size": len(self._species_db),
            "pipeline_stages": self.STAGES,
        }

    def info(self) -> Dict[str, Any]:
        """Version + capabilities."""
        return {
            "project": "fish-ecology-assistant",
            "version": self._agent_config.get("agent", {}).get("version", "unknown"),
            "role": "V0_SupplyVertex (S-State)",
            "pipeline": "5-stage: Plan → Search → Analyze → Write → Review",
            "skill_count": 28,
            "sub_agents": 13,
            "capabilities": [
                "species_knowledge_base",
                "credibility_scoring",
                "ocr_variant_generation",
                "delegate_protocol",
                "chinese_academic_sources",
                "multi_engine_search",
            ],
        }

    # ── Internal ──

    def _build_search_queries(self, scientific_name: str, chinese_name: str) -> List[str]:
        """Build search queries for a species across disciplines."""
        queries = [scientific_name]
        if chinese_name:
            queries.append(chinese_name)
        # Per-discipline queries
        for direction in ["genetic", "morphology", "ecology", "survey"]:
            if direction == "genetic":
                queries.append(f"{scientific_name} genetic diversity population mitochondrial microsatellite")
            elif direction == "morphology":
                queries.append(f"{scientific_name} morphology phenotype shape geometric")
            elif direction == "ecology":
                queries.append(f"{scientific_name} diet feeding habitat reproduction growth")
            elif direction == "survey":
                queries.append(f"{scientific_name} survey diversity community resource")
        return queries

    def _generate_ocr_variants(self, name: str) -> List[str]:
        """Generate OCR error variants for a scientific name."""
        variants = set()
        confusable = {"u": ["b"], "b": ["u"], "i": ["l", "e"], "l": ["i"],
                       "n": ["m"], "m": ["n"]}
        for i, ch in enumerate(name):
            if ch.lower() in confusable:
                for sub in confusable[ch.lower()]:
                    variants.add(name[:i] + sub + name[i + 1:])
        for i in range(len(name)):
            variants.add(name[:i] + name[i + 1:])
        for n in range(1, min(4, len(name))):
            variants.add(name[:-n])
        return list(variants)[:20]


def get_orchestrator() -> FishEcologyOrchestrator:
    """Factory function."""
    return FishEcologyOrchestrator()
