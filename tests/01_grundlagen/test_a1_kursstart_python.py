"""
Tests fuer Aufgabe A1: Kursstart KI/ML und Python-Einstieg.

Ausfuehren:
python -m pytest tests/01_grundlagen/test_a1_kursstart_python.py -v
"""

import json
from pathlib import Path

NOTEBOOK_PFAD = Path(__file__).parent.parent.parent / "notebooks" / "01_einfuehrung.ipynb"
AUFGABE_PFAD = Path(__file__).parent.parent.parent / "aufgaben" / "01_grundlagen" / "aufgabe_a1_kursstart_python.md"


def _lade_notebook(pfad: Path) -> dict:
    with open(pfad, encoding="utf-8") as f:
        return json.load(f)


def test_a1_dateien_vorhanden():
    assert NOTEBOOK_PFAD.exists(), f"Notebook fehlt: {NOTEBOOK_PFAD}"
    assert AUFGABE_PFAD.exists(), f"Aufgabe fehlt: {AUFGABE_PFAD}"


def test_a1_notebook_hat_codezellen():
    nb = _lade_notebook(NOTEBOOK_PFAD)
    codezellen = [c for c in nb.get("cells", []) if c.get("cell_type") == "code"]
    assert len(codezellen) >= 3, "Das Einfuehrungs-Notebook sollte mindestens 3 Codezellen enthalten"


def test_a1_begriffsteil_enthalten():
    nb = _lade_notebook(NOTEBOOK_PFAD)
    gesamter_text = "\n".join(
        "".join(cell.get("source", [])) for cell in nb.get("cells", [])
    )
    for begriff in ["KI", "Machine Learning", "Deep Learning"]:
        assert begriff in gesamter_text, f"Begriff fehlt im Notebook: {begriff}"
