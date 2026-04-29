"""
Tests fuer Aufgabe A2: Verfahrensvergleich ML.

Ausfuehren:
python -m pytest tests/03_regression/test_a2_verfahrenvergleich_ml.py -v
"""

import numpy as np
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier


def test_a2_regression_auf_linearen_daten():
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([2, 4, 6, 8, 10])

    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)

    assert r2_score(y, y_pred) > 0.99, "Regression sollte lineare Daten sehr gut abbilden"


def test_a2_entscheidungsbaum_klassifikation():
    X = np.array([[0], [1], [2], [3], [4], [5]])
    y = np.array([0, 0, 0, 1, 1, 1])

    clf = DecisionTreeClassifier(random_state=42)
    clf.fit(X, y)
    pred = clf.predict(X)

    assert (pred == y).all(), "Entscheidungsbaum sollte die Trainingsklassen korrekt trennen"


def test_a2_kmeans_findet_zwei_cluster():
    X = np.array([[0, 0], [0, 1], [1, 0], [10, 10], [10, 11], [11, 10]])

    km = KMeans(n_clusters=2, random_state=42, n_init=10)
    labels = km.fit_predict(X)

    assert len(set(labels)) == 2, "k-Means sollte zwei Cluster bilden"


def test_a2_knn_klassifiziert_einfaches_muster():
    X = np.array([[0], [1], [2], [8], [9], [10]])
    y = np.array([0, 0, 0, 1, 1, 1])

    clf = KNeighborsClassifier(n_neighbors=3)
    clf.fit(X, y)

    assert clf.predict([[1.5]])[0] == 0
    assert clf.predict([[9.5]])[0] == 1
