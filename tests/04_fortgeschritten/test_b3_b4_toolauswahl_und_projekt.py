"""
Tests fuer Aufgaben B3 und B4: KI-Toolauswahl und Anwendungsprojekt.

Ausfuehren:
python -m pytest tests/04_fortgeschritten/test_b3_b4_toolauswahl_und_projekt.py -v
"""

import json
from pathlib import Path

B3_AUFGABE = Path(__file__).parent.parent.parent / "aufgaben" / "04_fortgeschritten" / "aufgabe_b3_ki_toolauswahl_bwl.md"
B4_NOTEBOOK = Path(__file__).parent.parent.parent / "notebooks" / "04_ki_tools_bwl.ipynb"


def test_b3_aufgabe_enthaelt_kernkriterien():
    text = B3_AUFGABE.read_text(encoding="utf-8")

    for kriterium in ["Datenbedarf", "Kosten", "Datenschutz", "Erklaerbarkeit"]:
        assert kriterium in text, f"Kriterium fehlt in B3-Aufgabe: {kriterium}"


def test_b4_notebook_vorhanden_und_strukturiert():
    assert B4_NOTEBOOK.exists(), f"Notebook fehlt: {B4_NOTEBOOK}"

    nb = json.loads(B4_NOTEBOOK.read_text(encoding="utf-8"))
    cells = nb.get("cells", [])
    assert len(cells) >= 4, "B4-Notebook sollte mehrere Arbeitszellen enthalten"

    gesamter_text = "\n".join("".join(c.get("source", [])) for c in cells)
    assert "DecisionTreeRegressor" in gesamter_text, "Ein KI-Modell sollte im B4-Notebook eingesetzt werden"
    assert "Reflexion" in gesamter_text, "B4-Notebook sollte einen Reflexionsteil enthalten"
