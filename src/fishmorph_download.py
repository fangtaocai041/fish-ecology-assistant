"""
FISHMORPH download & import script.

Downloads FISHMORPH data from the easiest available source and imports
into fish-ecology knowledge base.

Sources (in priority order):
  1. R traitdata package (easiest, no auth)
  2. Figshare direct download
  3. Kaggle (requires login)

Usage:
    python -m fish_ecology_assistant.src.fishmorph_download --kb
"""

import csv
import json
import logging
import os
import subprocess
import sys
import urllib.request
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)

FISHMORPH_URLS = [
    "https://figshare.com/ndownloader/files/28082766",  # direct CSV
    "https://raw.githubusercontent.com/ropensci/traitdata/master/inst/extdata/fishmorph.csv",
]

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "data" / "fishmorph"
OUTPUT_CSV = OUTPUT_DIR / "fishmorph.csv"


def download_fishmorph() -> Optional[Path]:
    """Download FISHMORPH CSV from available sources. Returns path or None."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for url in FISHMORPH_URLS:
        logger.info(f"Trying: {url}")
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": "ReasonixFishEcology/1.0"
            })
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = resp.read()
                if len(data) > 1000 and b"," in data[:200]:
                    OUTPUT_CSV.write_bytes(data)
                    logger.info(f"Downloaded {len(data)} bytes → {OUTPUT_CSV}")
                    return OUTPUT_CSV
        except Exception as e:
            logger.warning(f"  Failed: {e}")
            continue

    # Fallback: try R
    logger.info("HTTP download failed. Trying R traitdata package...")
    try:
        r_script = """
        library(traitdata)
        data("fishmorph")
        write.csv(fishmorph, "%s", row.names=FALSE)
        """ % str(OUTPUT_CSV).replace("\\", "/")
        result = subprocess.run(
            ["Rscript", "-e", r_script],
            capture_output=True, text=True, timeout=60
        )
        if result.returncode == 0 and OUTPUT_CSV.exists():
            logger.info(f"Downloaded via R → {OUTPUT_CSV}")
            return OUTPUT_CSV
        logger.warning(f"R failed: {result.stderr[:200]}")
    except FileNotFoundError:
        logger.warning("R not installed")
    except Exception as e:
        logger.warning(f"R error: {e}")

    logger.error("All download sources failed.")
    return None


def import_to_kb(csv_path: Optional[Path] = None) -> int:
    """Import FISHMORPH data into fish-ecology KB. Returns species count."""
    if csv_path is None:
        csv_path = OUTPUT_CSV

    if not csv_path or not csv_path.exists():
        logger.error(f"FISHMORPH CSV not found at {csv_path}")
        logger.info("Run download_fishmorph() first.")
        return 0

    from fishkb.fishmorph_loader import FishmorphLoader
    loader = FishmorphLoader(str(csv_path))
    count = loader.load()

    if count == 0:
        logger.error("No records loaded. Check CSV format.")
        return 0

    # Save summary for quick lookup
    summary = {}
    for sp in list(loader._by_species.keys())[:100]:
        trait_summary = loader.get_trait_summary(sp)
        summary[sp] = trait_summary

    summary_path = OUTPUT_DIR / "fishmorph_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False),
                            encoding="utf-8")
    logger.info(f"Summary saved to {summary_path}")

    # Index into KB if available
    try:
        from fishkb.db import get_db
        kb = get_db()
        indexed = loader.index_into_kb(kb)
        logger.info(f"Indexed {indexed} species into KnowledgeDB")
    except ImportError:
        logger.info("fishkb not available, skipping KB index")

    return len(loader._by_species)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    csv_file = download_fishmorph()
    if csv_file:
        import_to_kb(csv_file)
