"""
Kompetenztests fuer BPE-6/7-Abdeckung im Marschplan.

Ausfuehren:
python -m pytest tests/04_fortgeschritten/test_bpe_kompetenz_mapping.py -v
"""

from pathlib import Path

MARSCHPLAN_PFAD = Path(__file__).parent.parent.parent / "informationen" / "lehrplan" / "marschplan-ki-ml.md"


def test_bpe6_und_bpe7_als_grundlage_enthalten():
    text = MARSCHPLAN_PFAD.read_text(encoding="utf-8")
    assert "BPE 6" in text, "BPE 6 muss im Marschplan klar enthalten sein"
    assert "BPE 7" in text, "BPE 7 muss im Marschplan klar enthalten sein"


def test_verpflichtende_verfahren_bpe6_enthalten():
    text = MARSCHPLAN_PFAD.read_text(encoding="utf-8")
    for inhalt in ["Regression", "Entscheidungsbaum", "k-Means", "k-NN"]:
        assert inhalt in text, f"Verpflichtender Inhalt fehlt: {inhalt}"


def test_verpflichtende_dateninhalte_bpe6_enthalten():
    text = MARSCHPLAN_PFAD.read_text(encoding="utf-8")
    for inhalt in ["Trainingsdaten", "Testdaten", "labeled", "unlabeled", "Datenmenge"]:
        assert inhalt in text, f"Dateninhalt fehlt: {inhalt}"


def test_ki_bereiche_und_neuronale_netze_enthalten():
    text = MARSCHPLAN_PFAD.read_text(encoding="utf-8")
    for inhalt in ["Deep Learning", "Language Processing", "neuronaler Netze", "Aktuelle Entwicklungen"]:
        assert inhalt in text, f"KI-Inhalt fehlt: {inhalt}"


def test_bpe7_tools_und_bwl_transfer_enthalten():
    text = MARSCHPLAN_PFAD.read_text(encoding="utf-8")
    for inhalt in [
        "Grafische Auswertungstools",
        "KI-Programmbibliotheken",
        "betriebswirtschaftliche Probleme",
    ]:
        assert inhalt in text, f"BPE-7-Inhalt fehlt: {inhalt}"


def test_lernziel_mapping_alle_bpe_unterpunkte_abgedeckt():
    text = MARSCHPLAN_PFAD.read_text(encoding="utf-8")
    for punkt in ["BPE 6.1", "BPE 6.2", "BPE 6.3", "BPE 7.1", "BPE 7.2"]:
        assert punkt in text, f"Lernziel-Mapping unvollstaendig: {punkt} fehlt"
