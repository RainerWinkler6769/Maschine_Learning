"""
Tests für Aufgabe 01: Daten erkunden mit Pandas
Schüler können diese Tests ausführen, um ihre Lösung zu prüfen.

Ausführen: python -m pytest tests/01_grundlagen/test_aufgabe_01.py -v
"""

import pytest
import pandas as pd
from pathlib import Path

DATEN_PFAD = Path(__file__).parent.parent.parent / "notebooks" / "daten" / "haeuser.csv"


@pytest.fixture
def df():
    """Lädt den Testdatensatz."""
    return pd.read_csv(DATEN_PFAD)


def test_datei_vorhanden():
    """Der Datensatz muss vorhanden sein."""
    assert DATEN_PFAD.exists(), f"Datensatz nicht gefunden: {DATEN_PFAD}"


def test_spalten_vorhanden(df):
    """Der Datensatz muss die erwarteten Spalten enthalten."""
    erwartete_spalten = {"groesse_m2", "zimmer", "baujahr", "preis_euro"}
    vorhandene_spalten = set(df.columns)
    assert erwartete_spalten.issubset(vorhandene_spalten), (
        f"Fehlende Spalten: {erwartete_spalten - vorhandene_spalten}"
    )


def test_datensatz_nicht_leer(df):
    """Der Datensatz darf nicht leer sein."""
    assert len(df) > 0, "Der Datensatz ist leer"


def test_keine_negativen_preise(df):
    """Alle Preise müssen positiv sein."""
    assert (df["preis_euro"] > 0).all(), "Es gibt negative oder Null-Preise"


def test_durchschnittspreis_berechnung(df):
    """Der Durchschnittspreis muss korrekt berechnet werden können."""
    durchschnitt = df["preis_euro"].mean()
    assert durchschnitt > 0, "Durchschnittspreis muss positiv sein"
    assert isinstance(durchschnitt, float), "Durchschnitt muss eine Dezimalzahl sein"
