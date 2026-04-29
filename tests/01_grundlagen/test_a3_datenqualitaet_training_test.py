"""
Tests fuer Aufgabe A3: Datenqualitaet, Training/Test, labeled/unlabeled.

Ausfuehren:
python -m pytest tests/01_grundlagen/test_a3_datenqualitaet_training_test.py -v
"""

from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

DATEN_PFAD = Path(__file__).parent.parent.parent / "notebooks" / "daten" / "haeuser.csv"


def test_a3_datensatz_vorhanden():
    assert DATEN_PFAD.exists(), f"Datensatz fehlt: {DATEN_PFAD}"


def test_a3_train_test_split_konsistent():
    df = pd.read_csv(DATEN_PFAD)
    X = df[["groesse_m2", "zimmer", "baujahr"]]
    y = df["preis_euro"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    assert len(X_train) > len(X_test), "Trainingsdaten sollten groesser als Testdaten sein"
    assert len(X_train) == len(y_train)
    assert len(X_test) == len(y_test)


def test_a3_modell_guete_berechenbar():
    df = pd.read_csv(DATEN_PFAD)
    X = df[["groesse_m2", "zimmer", "baujahr"]]
    y = df["preis_euro"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    assert np.isfinite(mse), "MSE muss berechenbar sein"
    assert np.isfinite(r2), "R2 muss berechenbar sein"
