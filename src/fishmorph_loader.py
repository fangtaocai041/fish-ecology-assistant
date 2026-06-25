"""
fishmorph_loader.py — FISHMORPH 数据库加载器 (Brosse et al. 2022)

10,230 records, 10 morphological traits for freshwater fishes.
Data source: Figshare https://doi.org/10.6084/m9.figshare.14891412

Trait codes (CSV) → human-readable names:
  MBl=body_length, BEl=body_elongation, VEp=eye_vertical_position,
  REs=relative_eye_size, OGp=mouth_position, RMl=relative_mouth_size,
  BLs=body_lateral_shape, PFv=pectoral_fin_vertical_position,
  PFs=relative_pectoral_fin_size, CPt=caudal_peduncle_throttle
"""

import csv
import io
import json
import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)

# (CSV column code, human-readable name)
TRAIT_MAP = [
    ("MBl", "body_length"),
    ("BEl", "body_elongation"),
    ("VEp", "eye_vertical_position"),
    ("REs", "relative_eye_size"),
    ("OGp", "mouth_position"),
    ("RMl", "relative_mouth_size"),
    ("BLs", "body_lateral_shape"),
    ("PFv", "pectoral_fin_vertical_position"),
    ("PFs", "relative_pectoral_fin_size"),
    ("CPt", "caudal_peduncle_throttle"),
]


@dataclass
class FishmorphRecord:
    species: str
    family: str = ""
    order: str = ""
    traits: Dict[str, Optional[float]] = field(default_factory=dict)
    source: str = "FISHMORPH"


class FishmorphLoader:
    """Parse FISHMORPH CSV and expose trait queries."""

    def __init__(self, csv_path: str):
        self._path = Path(csv_path)
        self._records: List[FishmorphRecord] = []
        self._by_species: Dict[str, List[FishmorphRecord]] = {}

    def load(self) -> int:
        """Load FISHMORPH CSV (semicolon-delimited, latin-1)."""
        if not self._path.exists():
            logger.warning(f"Not found: {self._path}")
            return 0

        raw = self._path.read_bytes()
        for enc in ["utf-8", "latin-1", "cp1252"]:
            try:
                text = raw.decode(enc)
                break
            except UnicodeDecodeError:
                continue

        reader = csv.DictReader(io.StringIO(text), delimiter=";")
        for row in reader:
            sp = (row.get("Genus species") or "").strip()
            if not sp:
                continue
            traits = {}
            for csv_col, name in TRAIT_MAP:
                val = (row.get(csv_col) or "").strip()
                if val:
                    try:
                        traits[name] = float(val)
                    except ValueError:
                        pass

            rec = FishmorphRecord(
                species=sp,
                family=(row.get("Family") or "").strip(),
                order=(row.get("Order") or "").strip(),
                traits=traits,
            )
            self._records.append(rec)
            self._by_species.setdefault(sp.lower(), []).append(rec)

        logger.info(f"Loaded {len(self._records)} records, {len(self._by_species)} species")
        return len(self._records)

    def get_species(self, name: str) -> List[FishmorphRecord]:
        return self._by_species.get(name.lower().strip(), [])

    def get_trait_summary(self, name: str) -> Dict[str, Any]:
        recs = self.get_species(name)
        if not recs:
            return {"species": name, "records": 0}
        summary: Dict[str, Any] = {"species": name, "records": len(recs)}
        for _, trait_name in TRAIT_MAP:
            vals = [r.traits[trait_name] for r in recs if trait_name in r.traits]
            if vals:
                summary[trait_name] = {
                    "mean": round(sum(vals) / len(vals), 3),
                    "min": round(min(vals), 3),
                    "max": round(max(vals), 3),
                    "n": len(vals),
                }
        return summary

    def search_by_trait(self, trait: str, min_val: float = None,
                        max_val: float = None) -> List[str]:
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

    def export_summary(self, path: str = None) -> Path:
        out = Path(path or str(self._path.parent / "fishmorph_summary.json"))
        data = {}
        for sp in list(self._by_species.keys())[:200]:
            data[sp] = self.get_trait_summary(sp)
        out.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
        logger.info(f"Summary → {out}")
        return out


def load_fishmorph(csv_path: str) -> FishmorphLoader:
    loader = FishmorphLoader(csv_path)
    loader.load()
    return loader
