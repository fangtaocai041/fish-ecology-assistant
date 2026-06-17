# 🐟 Fish Ecology Assistant

[![Python](https://img.shields.io/badge/python-3.10+-blue)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Version](https://img.shields.io/badge/version-8.1-8b5cf6)]()
[![Species](https://img.shields.io/badge/species-430-22c55e)]()
[![Traits](https://img.shields.io/badge/traits-289-orange)]()

> 🌊 Knowledge Supply Core — 430 Yangtze fish species, 289 morphological traits, population-level variation.
> Panta Rhei — Everything flows.

[English](README.md) · [中文](README.zh.md) · [CHANGELOG](CHANGELOG.md)

---

## 📖 Table of Contents

- [Philosophy](#-philosophy)
- [Quick Start](#-quick-start)
- [Architecture](#-architecture)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Ecosystem](#-ecosystem)

---

## 🏛️ Philosophy

> 道生一，一生二，二生三，三生万物。

This is the **S-state (V0)** of the Triangle — Knowledge Supply. It does not search or verify; it stores, organizes, and supplies knowledge. As the foundation of SanShengWanWu, it holds 430 Yangtze fish species with 289 morphological traits sourced from FISHMORPH, FishBase, FAO, IUCN, and Liu Kai research group publications.

---

## 🚀 Quick Start

```bash
# Clone
git clone git@github.com:fangtaocai041/fish-ecology-assistant.git
cd fish-ecology-assistant

# Install
pip install -e .

# Run
python src/main.py search --species "Coilia nasus"
```

---

## 🏗️ Architecture

```
fish-ecology-assistant/
  src/           Core Python engine
  ├── adapter.py     IProjectAdapter (V0 canonical)
  ├── orchestrator.py    KB-first species search
  ├── project_hub.py     Cross-project coordination
  ├── dao_engine.py      Philosophical chain executor
  ├── types.py           8 dataclasses + 4 enums
  └── kalman_emergence.py  Kalman Filter emergence detection
  config/
  ├── knowledge_base/   30 species .md profiles
  └── fish_species_kb.yaml  430 species index
  data/
  ├── species.db         SQLite (species + traits + literature)
  ├── FISHMORPH.csv      2.3MB global morphology database
  └── reports/           HTML/CSV exports
  scripts/
  ├── fishbase_pull.py   FishBase API auto-sync
  ├── trait_network.py   Network Science trait analysis
  └── gen_report.py      Bilingual HTML report generator
```

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🗃️ 430 Species | Complete Yangtze River fish species database |
| 📏 289 Morphology Traits | Sourced from FISHMORPH (251), FishBase, FAO, literature |
| 🌊 Population-level Data | 26 records with water-body-specific trait variation |
| 🔬 Trait Catalog | 61 traits in 7 categories (morphology→life history→feeding→...) |
| 🏛️ Bilingual Conservation | IUCN + China Red List + National Protection + CITES |
| 📊 Excel/HTML Reports | Double-click reports with 2-level hierarchical headers |
| 🔄 FishBase Auto-sync | Automated trait pulling with source traceability |
| 🕸️ Network Science | Trait co-occurrence networks, keystone trait identification |
| 📡 Kalman Filter | Emergence signal detection from noisy population data |
| 🔗 KB-First Architecture | Zero-network lookup for 30 core species |

---

## 📁 Project Structure

```
fish-ecology-assistant/
  (see Architecture section above)
```

---

## 🔗 Ecosystem

This project is the Knowledge Supply Core (V0) in the SanShengWanWu ecosystem.

```
Triangle Core (sealed 3):
  📦 fish-ecology-assistant    → Knowledge Supply (V0)
  🔍 cognitive-search-engine   → Search Verification (V1)
  ⚙️ eon-core                  → Coordination Hub (Coord)

Derived Projects (open N):
  🐬 porpoise-agent    → P₁ Porpoise Expert
  🐟 coilia-agent      → P₂ Coilia Expert
  🐟 culter-agent      → P₃ Culter Expert
  🔥 conflict-arbiter  → C  Conflict Arbitration
```

> 🔥 Together infinite power, apart top expert engines.

---
*SanShengWanWu Ecosystem · MIT License · fangtaocai041*
