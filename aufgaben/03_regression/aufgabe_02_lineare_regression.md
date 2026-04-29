# Aufgabe 02: Lineare Regression – Hauspreise vorhersagen

**Schwierigkeit:** Einsteiger  
**Thema:** Regression  
**Hilfsmittel:** [Python-Grundlagen](../../informationen/python/python-grundlagen.md), [Cheatsheet](../../informationen/cheatsheets/ml-python-cheatsheet.md)

---

## Aufgabenstellung

Kannst du den Preis eines Hauses vorhersagen, wenn du nur die Größe (m²) kennst?  
Trainiere dafür ein einfaches lineares Regressionsmodell.

---

## Teilaufgaben

### a) Daten vorbereiten
- Lade den Datensatz `../notebooks/daten/haeuser.csv`
- Wähle `groesse_m2` als Feature (X) und `preis_euro` als Ziel (y)
- Teile die Daten in 80% Training und 20% Test auf

### b) Modell trainieren
- Erstelle ein `LinearRegression`-Modell
- Trainiere es mit den Trainingsdaten

### c) Vorhersagen machen
- Lasse das Modell Preise für die Testdaten vorhersagen
- Vergleiche die Vorhersagen mit den echten Werten

### d) Modell bewerten
- Berechne den **R²-Score** — wie gut ist dein Modell?
- Berechne den **mittleren Fehler** (MSE)

### e) Visualisierung
- Plotte die echten Datenpunkte (Punkte) und die Regressionsgerade (Linie)

---

## Erwartetes Ergebnis

- Ein trainiertes Regressionsmodell
- R²-Score berechnet und interpretiert
- Regressionsgerade visualisiert

---

## Tipp

```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
modell = LinearRegression()
modell.fit(X_train, y_train)
```
