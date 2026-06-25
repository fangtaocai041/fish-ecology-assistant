"""
fishmorph_loader.py — FISHMORPH 数据库加载器 (Brosse et al. 2022)

10,230 records, 10 traits. Data must be downloaded manually:
  https://figshare.com/articles/dataset/FISHMORPH_Database/14891412
  or R: install.packages("traitdata"); data("fishmorph")

Once downloaded as CSV, this module parses and indexes it into fish-ecology KB.

Usage:
    from fishkb.fishmorph_loader import load_fishmorph
    loader = load_fishmorph("path/to/fishmorph.csv")
    loader.index_into_kb(kb)
"""

import csv
import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)

TRAIT_COLUMNS = [
    "body_size",
    "head_size",
    "eye_size",
    "mouth_size",
    "pectoral_fin_size",
    "caudal_fin_size",
    "body_shape",
    "mouth_position",
    "eye_position",
    "caudal_peduncle_ratio",
]


@dataclass
class FishmorphRecord:
    species: str
    family: str = ""
    traits: Dict[str, Optional[float]] = field(default_factory=dict)
    source: str = "FISHMORPH"


class FishmorphLoader:
    """Parse FISHMORPH CSV and expose trait queries."""

    def __init__(self, csv_path: str):
        self._path = Path(csv_path)
        self._records: List[FishmorphRecord] = []
        self._by_species: Dict[str, List[FishmorphRecord]] = {}

    def load(self) -> int:
        """Load and parse FISHMORPH CSV. Returns record count."""
        if not self._path.exists():
            logger.warning(f"FISHMORPH file not found: {self._path}")
            return 0

        with open(self._path, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                sp = row.get("species", row.get("scientific_name", ""))
                if not sp:
                    continue
                traits = {}
                for col in TRAIT_COLUMNS:
                    val = row.get(col)
                    if val and val.strip():
                        try:
                            traits[col] = float(val)
                        except ValueError:
                            traits[col] = None

                rec = FishmorphRecord(
                    species=sp,
                    family=row.get("family", ""),
                    traits=traits,
                )
                self._records.append(rec)
                self._by_species.setdefault(sp.lower(), []).append(rec)

        logger.info(f"Loaded {len(self._records)} FISHMORPH records "
                     f"for {len(self._by_species)} species")
        return len(self._records)

    def get_species(self, name: str) -> List[FishmorphRecord]:
        """Get all records for a species."""
        return self._by_species.get(name.lower().strip(), [])

    def get_trait_summary(self, name: str) -> Dict[str, Any]:
        """Get trait averages for a species."""
        recs = self.get_species(name)
        if not recs:
            return {"species": name, "records": 0}

        summary: Dict[str, Any] = {"species": name, "records": len(recs)}
        for col in TRAIT_COLUMNS:
            vals = [r.traits[col] for r in recs
                    if r.traits.get(col) is not None]
            if vals:
                summary[col] = {
                    "mean": round(sum(vals) / len(vals), 3),
                    "min": round(min(vals), 3),
                    "max": round(max(vals), 3),
                    "n": len(vals),
                }
        return summary

    def search_by_trait(self, trait: str, min_val: float = None,
                        max_val: float = None) -> List[str]:
        """Find species within a trait range."""
        results = set()
        for rec in self._records:
            val = rec.traits.get(trait)
            if val is None:
                continue
            if min_val is not None and val < min_val:
                continue
            if max_val is not None and val > max_val:
                continue
            results.add(rec.species)
        return sorted(results)

    def index_into_kb(self, kb) -> int:
        """Index FISHMORPH traits into fish-ecology knowledge base."""
        indexed = 0
        for sp, recs in self._by_species.items():
            summary = self.get_trait_summary(sp)
            if summary.get("records", 0) > 0:
                try:
                    kb.update_species(sp, {"fishmorph_traits": summary})
                    indexed += 1
                except Exception:
                    pass
        logger.info(f"Indexed {indexed} species into KB")
        return indexed


def load_fishmorph(csv_path: str) -> FishmorphLoader:
    """Convenience: create loader and load data."""
    loader = FishmorphLoader(csv_path)
    loader.load()
    return loader
