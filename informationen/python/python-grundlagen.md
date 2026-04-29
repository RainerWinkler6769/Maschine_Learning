# Python-Grundlagen für den ML-Kurs

## Variablen & Datentypen

```python
name = "Alice"          # String (Text)
alter = 16              # Integer (Ganzzahl)
groesse = 1.72          # Float (Dezimalzahl)
aktiv = True            # Boolean (Wahrheitswert)
```

## Listen & Schleifen

```python
werte = [10, 20, 30, 40, 50]

# Einzelner Zugriff (Index startet bei 0)
print(werte[0])   # → 10
print(werte[-1])  # → 50 (letztes Element)

# Schleife
for w in werte:
    print(w)

# Mit Index
for i, w in enumerate(werte):
    print(f"Index {i}: {w}")
```

## Funktionen

```python
def berechne_durchschnitt(werte):
    return sum(werte) / len(werte)

ergebnis = berechne_durchschnitt([10, 20, 30])
print(ergebnis)  # → 20.0
```

---

## NumPy – Rechnen mit Arrays

NumPy ist die Basis für ML in Python.

```python
import numpy as np

# Array erstellen
a = np.array([1, 2, 3, 4, 5])

# Rechenoperationen (gelten für alle Elemente)
print(a * 2)       # → [2 4 6 8 10]
print(a + 10)      # → [11 12 13 14 15]
print(a.mean())    # → 3.0  (Durchschnitt)
print(a.max())     # → 5

# 2D-Array (Matrix)
m = np.array([[1, 2], [3, 4], [5, 6]])
print(m.shape)     # → (3, 2)  → 3 Zeilen, 2 Spalten
```

---

## Pandas – Daten als Tabelle

```python
import pandas as pd

# Tabelle laden
df = pd.read_csv("daten.csv")

# Erste 5 Zeilen anzeigen
print(df.head())

# Spalte auswählen
print(df["Alter"])

# Zeilen filtern
jung = df[df["Alter"] < 18]

# Statistik
print(df.describe())
```

---

## Matplotlib – Daten visualisieren

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.xlabel("X-Achse")
plt.ylabel("Y-Achse")
plt.title("Mein Diagramm")
plt.show()
```

---

## scikit-learn – ML-Modelle

```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Daten aufteilen: 80% Training, 20% Test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Modell erstellen und trainieren
modell = LinearRegression()
modell.fit(X_train, y_train)

# Vorhersagen
vorhersagen = modell.predict(X_test)

# Genauigkeit bewerten
score = modell.score(X_test, y_test)
print(f"R²-Score: {score:.2f}")
```
