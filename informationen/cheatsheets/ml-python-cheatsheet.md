# Cheatsheet: Machine Learning mit Python

## NumPy

```python
import numpy as np

np.array([1, 2, 3])          # Array erstellen
a.shape                       # Form (Zeilen, Spalten)
a.mean() / a.std()            # Durchschnitt / Standardabweichung
a.min() / a.max()             # Minimum / Maximum
np.zeros((3, 3))              # 3×3 Nullen-Matrix
np.ones((3, 3))               # 3×3 Einsen-Matrix
np.linspace(0, 1, 100)        # 100 gleichmäßige Werte von 0 bis 1
```

## Pandas

```python
import pandas as pd

pd.read_csv("datei.csv")      # CSV einlesen
df.head(5)                    # Erste 5 Zeilen
df.tail(5)                    # Letzte 5 Zeilen
df.shape                      # (Zeilen, Spalten)
df.describe()                 # Statistik-Übersicht
df.info()                     # Datentypen & fehlende Werte
df["Spalte"]                  # Spalte auswählen
df[df["A"] > 10]              # Zeilen filtern
df.dropna()                   # Zeilen mit NaN entfernen
df.fillna(0)                  # NaN durch 0 ersetzen
df["Spalte"].value_counts()   # Häufigkeiten zählen
```

## Matplotlib

```python
import matplotlib.pyplot as plt

plt.plot(x, y)                # Liniendiagramm
plt.scatter(x, y)             # Streudiagramm
plt.bar(kategorien, werte)    # Balkendiagramm
plt.hist(daten, bins=10)      # Histogramm
plt.xlabel("X") / plt.ylabel("Y")
plt.title("Titel")
plt.legend()
plt.show()
```

## scikit-learn: Modelle

```python
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

modell = LinearRegression()
modell.fit(X_train, y_train)       # Trainieren
modell.predict(X_test)             # Vorhersagen
modell.score(X_test, y_test)       # Bewerten (R² oder Accuracy)
```

## scikit-learn: Vorbereitung

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Aufteilen
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Skalieren (wichtig für viele Modelle)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Textkategorien in Zahlen umwandeln
le = LabelEncoder()
y = le.fit_transform(y)
```

## Labeled vs unlabeled Data (Praxis)

- Labeled Data: Eingaben plus bekannter Zielwert.
- Unlabeled Data: Eingaben ohne Zielwert.

Beispiel (Hauspreise):

- labeled: `groesse_m2=95, zimmer=3, baujahr=2015, preis_euro=310000`
- unlabeled: `groesse_m2=95, zimmer=3, baujahr=2015, preis_euro=?`

Mini-Checkliste fuer Aufgaben:

- 1) Zielspalte bestimmen (bei Regression oft Preis/Umsatz/Temperatur).
- 2) Hat die Zeile einen Zielwert? Ja -> labeled, Nein -> unlabeled.
- 3) labeled Daten fuer Training verwenden.
- 4) unlabeled Daten erst nach dem Training fuer Vorhersagen nutzen.

## scikit-learn: Bewertung

```python
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score, confusion_matrix

# Klassifikation
accuracy_score(y_test, vorhersagen)     # Genauigkeit (0–1)
confusion_matrix(y_test, vorhersagen)   # Konfusionsmatrix

# Regression
mean_squared_error(y_test, vorhersagen) # Mittlerer quadratischer Fehler
r2_score(y_test, vorhersagen)           # R²-Koeffizient (0–1, höher = besser)
```

## Regression: MSE und R2 richtig lesen

- MSE (Mean Squared Error):
  - Formel: Mittelwert von $(y_i - \hat{y}_i)^2$.
  - Bedeutung: Fehler werden quadriert, grosse Ausreisser fallen stark ins Gewicht.
  - Ziel: kleiner ist besser.
  - Hinweis: Die Einheit ist Zielwert^2 (z. B. Euro^2). Deshalb MSE nicht mit anderen Zielgroessen mischen.

- R2 (Bestimmtheitsmass):
  - Bedeutung: Anteil der Zielwert-Varianz, den das Modell erklaert.
  - Wertebereich in der Praxis: kann negativ sein bis maximal 1.0.
  - Daumenregel: nahe 1.0 sehr gut, nahe 0.0 kaum besser als Mittelwert, kleiner 0.0 schlechter als Mittelwert.

- In Aufgaben wie A3 immer so interpretieren:
  - 1) Modell/Parameter gleich halten.
  - 2) Nur einen Faktor aendern (z. B. Datenmenge).
  - 3) MSE und R2 gemeinsam bewerten, nicht nur eine Kennzahl isoliert.
