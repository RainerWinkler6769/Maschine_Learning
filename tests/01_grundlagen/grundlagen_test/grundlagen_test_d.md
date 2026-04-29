# Grundlagen-Test – Version D (KI/ML und Python)

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

### Aufgabe A1: Konzepte rund um KI (6 Punkte)

Erkläre folgende Begriffe und gib zu jedem ein Beispiel:

<table style="border-collapse: collapse; width: 100%; font-family: Arial, sans-serif; font-size: 11pt;">
  <thead>
    <tr>
      <th style="border: 1px solid #000000; padding: 6px 10px; background-color: #dde3ea; text-align: left; font-weight: bold;">Begriff</th>
      <th style="border: 1px solid #000000; padding: 6px 10px; background-color: #dde3ea; text-align: left; font-weight: bold;">Erklärung</th>
      <th style="border: 1px solid #000000; padding: 6px 10px; background-color: #dde3ea; text-align: left; font-weight: bold;">Beispiel</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #000000; padding: 6px 10px; text-align: left; min-width: 80px;">KI</td>
      <td style="border: 1px solid #000000; padding: 6px 10px; text-align: left; min-width: 80px;"></td>
      <td style="border: 1px solid #000000; padding: 6px 10px; text-align: left; min-width: 80px;"></td>
    </tr>
    <tr>
      <td style="border: 1px solid #000000; padding: 6px 10px; text-align: left; min-width: 80px;">Maschinenelles Lernen</td>
      <td style="border: 1px solid #000000; padding: 6px 10px; text-align: left; min-width: 80px;"></td>
      <td style="border: 1px solid #000000; padding: 6px 10px; text-align: left; min-width: 80px;"></td>
    </tr>
    <tr>
      <td style="border: 1px solid #000000; padding: 6px 10px; text-align: left; min-width: 80px;">Tiefe Netze</td>
      <td style="border: 1px solid #000000; padding: 6px 10px; text-align: left; min-width: 80px;"></td>
      <td style="border: 1px solid #000000; padding: 6px 10px; text-align: left; min-width: 80px;"></td>
    </tr>
  </tbody>
</table>

Bewertung:
- pro Zeile: 1 Punkt Erklärung + 1 Punkt Beispiel

### Aufgabe A2: Hart kodiert vs. adaptiv (3 Punkte)

1. Unterscheide in 2-4 Sätzen: Was ist der Unterschied zwischen starr programmierten Systemen und Systemen, die lernen? (2 Punkte)
2. Nenne zur Unterscheidung jeweils ein Beispiel. (1 Punkt)

<div style="background-color: #f6f8fa; padding: 10px 12px; border-radius: 6px; border: 1px solid #e1e4e8;">
**Antwort:**




</div>

### Aufgabe A3: Daten in Training und Prüfung (5,5 Punkte)

Szenario: Ein Unternehmen möchte Studierenden-Noten basierend auf Lernstunden, Anwesenheit und bearbeiteten Übungen vorhersagen.

1. Begründe, warum eine Aufteilung der Daten in Training und Test notwendig ist. (2 Punkte)
2. Was sind labeled vs. unlabeled Data in diesem Kontext? Gib je ein Beispiel. (2 Punkte)
3. Welche Fehlerqüllen entstehen, wenn Test-Beispiele (Noten) während des Trainings benutzt werden? (1,5 Punkte)

<div style="background-color: #f6f8fa; padding: 10px 12px; border-radius: 6px; border: 1px solid #e1e4e8;">
**Antwort:**




</div>

### Aufgabe A4: Menge und Qualität von Daten (3 Punkte)

Ein Lehrerteam teste ein Noten-Vorhersage-Modell zweimal:
- Szenario A: 30 Studierenden-Datensätze
- Szenario B: 300 Studierenden-Datensätze

Analysiere in 5-7 Sätzen, wie Datenmenge und Datenqualität (z. B. fehlerhafte Anwesenheitsangaben) die Modellgüte bezüglich MSE und R2 verändern. (3 Punkte)

<div style="background-color: #f6f8fa; padding: 10px 12px; border-radius: 6px; border: 1px solid #e1e4e8;">
**Antwort:**




</div>

## Teil B: Praxis (Programmierung, 7,5 Punkte)

### Aufgabe B1: Datenverarbeitung und Modelltraining (7,5 Punkte)

Schreibe den Code handschriftlich oder in sauberem Pseudocode.

Szenario:
- Dateiname: ../daten/studierende_noten.csv
- Spalten: lern_stunden, anwesenheit_prozent, übungen_bearbeitet, note

1. Lade die CSV-Datei mit Pandas und zeige die ersten 5 Zeilen. (2 Punkte)
2. Berechne Durchschnitt, Minimum und Maximum der Noten. (2,5 Punkte)
3. Teile Daten 80/20, trainiere ein lineares Regressionsmodell und gib MSE und R2 aus. (3 Punkte)

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
df = pd.read_csv("../daten/studierende_noten.csv")
print(df.head())

# Kennzahlen Noten
mean_note = df["note"].mean()
min_note = df["note"].min()
max_note = df["note"].max()

# Features und Ziel
X = df[["lern_stunden", "anwesenheit_prozent", "uebungen_bearbeitet"]]
y = df["note"]

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
