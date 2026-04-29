"""
Tests fuer Aufgaben B1 und B2: Visualisierung und KI-Programmbibliotheken.

Ausfuehren:
python -m pytest tests/04_fortgeschritten/test_b1_b2_visualisierung_und_bibliotheken.py -v
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

DATEN_PFAD = Path(__file__).parent.parent.parent / "notebooks" / "daten" / "haeuser.csv"


def test_b1_visualisierungen_erstellbar_ohne_fehler():
    df = pd.read_csv(DATEN_PFAD)

    fig1 = plt.figure()
    plt.hist(df["preis_euro"], bins=10)
    plt.close(fig1)

    fig2 = plt.figure()
    plt.scatter(df["groesse_m2"], df["preis_euro"])
    plt.close(fig2)

    assert True


def test_b2_sklearn_workflow_laeuft_reproduzierbar():
    df = pd.read_csv(DATEN_PFAD)
    X = df[["groesse_m2", "zimmer", "baujahr"]]
    y = df["preis_euro"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred_1 = model.predict(X_test)

    model2 = LinearRegression()
    model2.fit(X_train, y_train)
    y_pred_2 = model2.predict(X_test)

    assert (y_pred_1 == y_pred_2).all(), "Vorhersagen sollten bei gleichem Workflow identisch sein"
    assert r2_score(y_test, y_pred_1) > 0.5, "Das Modell sollte auf dem Beispieldatensatz sinnvoll lernen"
