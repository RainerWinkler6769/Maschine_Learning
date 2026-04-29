# Grundlagen-Test – Version C (KI/ML und Python)

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

### Aufgabe A1: KI-Paradigmen unterscheiden (6 Punkte)

Vergleiche folgende Konzepte in einer Tabelle:

<table style="border-collapse: collapse; width: 100%; font-family: Arial, sans-serif; font-size: 11pt;">
  <thead>
    <tr>
      <th style="border: 1px solid #000000; padding: 6px 10px; background-color: #dde3ea; text-align: left; font-weight: bold;">Konzept</th>
      <th style="border: 1px solid #000000; padding: 6px 10px; background-color: #dde3ea; text-align: left; font-weight: bold;">Definition</th>
      <th style="border: 1px solid #000000; padding: 6px 10px; background-color: #dde3ea; text-align: left; font-weight: bold;">Anwendungsbeispiel</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #000000; padding: 6px 10px; text-align: left; min-width: 80px;">Intelligente Systeme</td>
      <td style="border: 1px solid #000000; padding: 6px 10px; text-align: left; min-width: 80px;"></td>
      <td style="border: 1px solid #000000; padding: 6px 10px; text-align: left; min-width: 80px;"></td>
    </tr>
    <tr>
      <td style="border: 1px solid #000000; padding: 6px 10px; text-align: left; min-width: 80px;">Lernende Modelle</td>
      <td style="border: 1px solid #000000; padding: 6px 10px; text-align: left; min-width: 80px;"></td>
      <td style="border: 1px solid #000000; padding: 6px 10px; text-align: left; min-width: 80px;"></td>
    </tr>
    <tr>
      <td style="border: 1px solid #000000; padding: 6px 10px; text-align: left; min-width: 80px;">Tiefes Lernen</td>
      <td style="border: 1px solid #000000; padding: 6px 10px; text-align: left; min-width: 80px;"></td>
      <td style="border: 1px solid #000000; padding: 6px 10px; text-align: left; min-width: 80px;"></td>
    </tr>
  </tbody>
</table>

Bewertung:
- pro Zeile: 1 Punkt korrekte Definition + 1 Punkt relevantes Beispiel

### Aufgabe A2: Algorithmen und Daten (3 Punkte)

1. Erkläre in 3-5 Sätzen den Unterschied zwischen einem regelgesteürten System und einem datengetriebenen Modell. (2 Punkte)
2. Gib für jede Methode ein Beispiel aus dem Bereich Wetter/Klima. (1 Punkt)

<div style="background-color: #f6f8fa; padding: 10px 12px; border-radius: 6px; border: 1px solid #e1e4e8;">
**Antwort:**




</div>

### Aufgabe A3: Daten teilen und labeln (5,5 Punkte)

Kontext: Ein Wetter-Modell soll Tageshöchsttemperaturen vorhersagen (Min-Temp, Luftfeuchtigkeit, Luftdruck gehören zu den Inputs).

1. Erkläre, warum man Daten in Train- und Testsets teilt. (2 Punkte)
2. Definiere labeled und unlabeled Data mit Beispielen aus dem Wetter-Kontext. (2 Punkte)
3. Welche Probleme entstehen, wenn Testdaten beim Training verwendet werden? (1,5 Punkte)

<div style="background-color: #f6f8fa; padding: 10px 12px; border-radius: 6px; border: 1px solid #e1e4e8;">
**Antwort:**




</div>

### Aufgabe A4: Datenumfang und Qualitätsaspekte (3 Punkte)

Ein Forscherteam trainiert ein Wetter-Vorhersage-Modell in zwei Varianten:
- Version 1: 50 Messwerte über einen Monat
- Version 2: 1000 Messwerte über ein Jahr

Begründe in 5-7 Sätzen, wie Datenmenge (temporal/volumenmässig) und Messfehler (z. B. fehlerhafte Sensoren) die Modellgüte (MSE, R2) beeinflussen. (3 Punkte)

<div style="background-color: #f6f8fa; padding: 10px 12px; border-radius: 6px; border: 1px solid #e1e4e8;">
**Antwort:**




</div>

## Teil B: Praxis (Programmierung, 7,5 Punkte)

### Aufgabe B1: Datenanalyse mit Python und Pandas (7,5 Punkte)

Schreibe den Code handschriftlich oder in sauberem Pseudocode.

Szenario:
- Dateiname: ../daten/wetter_daten.csv
- Spalten: min_temp_celsius, luftfeuchtigkeit_prozent, luftdruck_mbar, max_temp_celsius

1. Lade die CSV-Datei mit Pandas und zeige die ersten 5 Zeilen. (2 Punkte)
2. Berechne Mittelwert, Minimale und Maximale Tageshöchsttemperatur. (2,5 Punkte)
3. Teile Daten im Verhältnis 80/20, trainiere ein Regressionsmodell und gib MSE und R2 aus. (3 Punkte)

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
df = pd.read_csv("../daten/wetter_daten.csv")
print(df.head())

# Kennzahlen Max-Temp
mean_temp = df["max_temp_celsius"].mean()
min_temp = df["max_temp_celsius"].min()
max_temp = df["max_temp_celsius"].max()

# Features und Zielwert
X = df[["min_temp_celsius", "luftfeuchtigkeit_prozent", "luftdruck_mbar"]]
y = df["max_temp_celsius"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modelltraining
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Evaluierung
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
```

</div>
