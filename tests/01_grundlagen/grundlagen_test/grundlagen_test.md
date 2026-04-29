# Grundlagen-Test (KI/ML und Python)

- Bereich: Grundlagen
- Gesamtpunkte: 25
- Gewichtung: Theorie 17,5 Punkte (70%), Praxis 7,5 Punkte (30%)
- Bearbeitungszeit (Vorschlag): 45-60 Minuten
- Hilfsmittel: Stift, Papier, optional Syntaxhilfe unten

## Hinweise zur Bearbeitung

- Der Test ist so aufgebaut, dass er komplett handschriftlich bearbeitet werden kann.
- Bei Programmieraufgaben zählt der korrekte Ablauf. Kleine Syntaxfehler sind weniger wichtig als die richtige Logik.
- Antworte klar und in ganzen Sätzen, wenn es gefordert ist.

## Teil A: Theorie (17,5 Punkte)

### Aufgabe A1: Begriffe sicher unterscheiden (6 Punkte)

Ergänze die Tabelle mit einer kurzen Definition und einem passenden Beispiel.

<table style="border-collapse: collapse; width: 100%; font-family: Arial, sans-serif; font-size: 11pt;">
  <thead>
    <tr>
      <th style="border: 1px solid #000000; padding: 6px 10px; background-color: #dde3ea; text-align: left; font-weight: bold;">Begriff</th>
      <th style="border: 1px solid #000000; padding: 6px 10px; background-color: #dde3ea; text-align: left; font-weight: bold;">Kurzdefinition</th>
      <th style="border: 1px solid #000000; padding: 6px 10px; background-color: #dde3ea; text-align: left; font-weight: bold;">Beispiel aus Alltag oder Wirtschaft</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #000000; padding: 6px 10px; text-align: left; min-width: 80px;">KI</td>
      <td style="border: 1px solid #000000; padding: 6px 10px; text-align: left; min-width: 80px;"></td>
      <td style="border: 1px solid #000000; padding: 6px 10px; text-align: left; min-width: 80px;"></td>
    </tr>
    <tr>
      <td style="border: 1px solid #000000; padding: 6px 10px; text-align: left; min-width: 80px;">Machine Learning</td>
      <td style="border: 1px solid #000000; padding: 6px 10px; text-align: left; min-width: 80px;"></td>
      <td style="border: 1px solid #000000; padding: 6px 10px; text-align: left; min-width: 80px;"></td>
    </tr>
    <tr>
      <td style="border: 1px solid #000000; padding: 6px 10px; text-align: left; min-width: 80px;">Deep Learning</td>
      <td style="border: 1px solid #000000; padding: 6px 10px; text-align: left; min-width: 80px;"></td>
      <td style="border: 1px solid #000000; padding: 6px 10px; text-align: left; min-width: 80px;"></td>
    </tr>
  </tbody>
</table>

Bewertung:
- pro Begriff: 1 Punkt Definition + 1 Punkt Beispiel

### Aufgabe A2: Regelbasiert vs. datenbasiert (3 Punkte)

1. Erkläre den Unterschied zwischen regelbasierter und datenbasierter Lösung in 2-4 Sätzen. (2 Punkte)
2. Nenne ein konkretes Beispiel für beide Ansätze. (1 Punkt)

<div style="background-color: #f6f8fa; padding: 10px 12px; border-radius: 6px; border: 1px solid #e1e4e8;">
**Antwort:**




</div>

### Aufgabe A3: Training, Test, labeled, unlabeled (5,5 Punkte)

1. Warum müssen Trainingsdaten und Testdaten getrennt sein? (2 Punkte)
2. Erkläre labeled Data und unlabeled Data jeweils mit einem Beispiel aus dem Hauspreis-Kontext. (2 Punkte)
3. Darf ein Modell Testdaten beim Lernen sehen? Begründe kurz. (1,5 Punkte)

<div style="background-color: #f6f8fa; padding: 10px 12px; border-radius: 6px; border: 1px solid #e1e4e8;">
**Antwort:**




</div>

### Aufgabe A4: Datenmenge und Datenqualität bewerten (3 Punkte)

Ein Team trainiert dasselbe Regressionsmodell zweimal:
- Lauf 1: 20 Datensätze
- Lauf 2: vollständiger Datensatz

Bewerte in 4-6 Sätzen, wie sich Datenmenge und Datenqualität auf MSE und R2 auswirken können. (3 Punkte)

<div style="background-color: #f6f8fa; padding: 10px 12px; border-radius: 6px; border: 1px solid #e1e4e8;">
**Antwort:**




</div>

## Teil B: Praxis (Programmierung, 7,5 Punkte)

### Aufgabe B1: Python/Pandas-Grundablauf (7,5 Punkte)

Schreibe den Code handschriftlich oder in sauberem Pseudocode. Nutze folgende Annahme:
- Dateiname: ../notebooks/daten/haeuser.csv
- wichtige Spalten: groesse_m2, zimmer, baujahr, preis_euro

1. Lade die CSV-Datei mit Pandas und gib die ersten 5 Zeilen aus. (2 Punkte)
2. Berechne den durchschnittlichen, minimalen und maximalen Hauspreis. (2,5 Punkte)
3. Teile die Daten in Training/Test (80/20), trainiere eine lineare Regression und gib MSE und R2 aus. (3 Punkte)

<div style="background-color: #f6f8fa; padding: 10px 12px; border-radius: 6px; border: 1px solid #e1e4e8;">
**Antwort:**


</div>

<div style="background-color: #f0f0f0; padding: 10px 14px; border-radius: 6px; font-family: monospace; border-left: 3px solid #cccccc;">

```python



```

</div>

## Syntaxhilfe (optional)

Diese Hilfe darf bei handschriftlicher Lösung als Orientierung genutzt werden.

<div style="background-color: #f0f0f0; padding: 10px 14px; border-radius: 6px; font-family: monospace; border-left: 3px solid #cccccc;">

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Daten laden
df = pd.read_csv("../notebooks/daten/haeuser.csv")
print(df.head())

# Kennzahlen
mean_preis = df["preis_euro"].mean()
min_preis = df["preis_euro"].min()
max_preis = df["preis_euro"].max()

# Features/Ziel
X = df[["groesse_m2", "zimmer", "baujahr"]]
y = df["preis_euro"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modell
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Bewertung
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
```

</div>
