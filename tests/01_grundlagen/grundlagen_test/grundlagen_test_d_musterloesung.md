# Musterlösung: Grundlagen-Test – Version D (KI/ML und Python)

- Gesamtpunkte: 25
- Theorie: 17,5 Punkte
- Praxis: 7,5 Punkte

## Teil A: Theorie (17,5 Punkte)

### Aufgabe A1: Konzepte rund um KI (6 Punkte)

<div style="background-color: #f6f8fa; padding: 10px 12px; border-radius: 6px; border: 1px solid #e1e4e8;">
**Aufgabenstellung:**


Erkläre folgende Begriffe und gib zu jedem ein Beispiel:

| Begriff | Erklärung | Beispiel |
|---|---|---|
| KI |  |  |
| Maschinenelles Lernen |  |  |
| Tiefe Netze |  |  |

Musterlösung:

| Begriff | Erklärung | Beispiel |
|---|---|---|
| KI | Übergeordnetes Konzept für Maschinen, die Aufgaben intelligent lösen oder sich verhalten. | Automatische Fehlerdiagnose in Fabriken. |
| Maschinenelles Lernen | Teilbereich der KI, bei dem Algorithmen aus Beispieldaten automatisch Regeln ableiten. | Kreditvergabe-Entscheidungen basierend auf historischen Kreditnehmer-Daten. |
| Tiefe Netze | Neuronale Netze mit vielen Schichten, die komplexe, nichtlineare Muster lernen. | Automatische Handschrifterkennung bei Posteingangsblöcken. |

Punktevergabe:
- Pro Zeile 2 Punkte: 1 Punkt Erklärung, 1 Punkt Beispiel.

</div>

### Aufgabe A2: Hart kodiert vs. adaptiv (3 Punkte)

<div style="background-color: #f6f8fa; padding: 10px 12px; border-radius: 6px; border: 1px solid #e1e4e8;">
**Aufgabenstellung:**


1. Unterscheide in 2-4 Sätzen: Was ist der Unterschied zwischen starr programmierten Systemen und Systemen, die lernen? (2 Punkte)
2. Nenne zur Unterscheidung jeweils ein Beispiel. (1 Punkt)

Musterlösung:

1. Starr programmierte Systeme folgen unveränderlichen Regeln, die einmal geschrieben wurden. Lernende Systeme beobachten Daten und stellen Regeln selbst auf – sie passen sich also an neü Situationen an. Der Unterschied: Das eine ist statisch, das andere ist dynamisch.

2. Starr: "Wenn Note > 4.0, dann Durchfall." Lernend: Modell lernt aus hunderten von Notenverlauf-Beispielen, welche Kombination von Lernstunden und Anwesenheit zu guten Noten führt.

Punktevergabe:
- 2 Punkte: Unterschied klar (starr/unverändert vs. adaptiv/lernend).
- 1 Punkt: Je ein passendes Beispiel für Kategorie.

</div>

### Aufgabe A3: Daten in Training und Prüfung (5,5 Punkte)

<div style="background-color: #f6f8fa; padding: 10px 12px; border-radius: 6px; border: 1px solid #e1e4e8;">
**Aufgabenstellung:**


Szenario: Ein Unternehmen möchte Studierenden-Noten basierend auf Lernstunden, Anwesenheit und bearbeiteten Übungen vorhersagen.

1. Begründe, warum eine Aufteilung der Daten in Training und Test notwendig ist. (2 Punkte)
2. Was sind labeled vs. unlabeled Data in diesem Kontext? Gib je ein Beispiel. (2 Punkte)
3. Welche Fehlerqüllen entstehen, wenn Test-Beispiele (Noten) während des Trainings benutzt werden? (1,5 Punkte)

Musterlösung:

1. Die Aufteilung stellt sicher, dass das Modell Noten für neü, unbekannte Studierenden fair vorhersagen kann. Mit getrennten Testdaten prüft man die echte Vorhersagekräft. Sonst könnte das Modell die Antworten nur auswendig lernen.

2. labeled Data: Ein Datensatz mit (5 Lernstunden, 90% Anwesenheit, 25 Übungen) → Note 1,7. unlabeled Data: Ein neür Studierender mit (6 Lernstunden, 85%, 30 Übungen), aber wir kennen die Note noch nicht – das Modell soll vorhersagen.

3. Wenn Test-Noten beim Trainingen verwendet werden, lernt das Modell die Lösung auswendig. MSE wird kiesnstlich niedrig, R2 kiesnstlich hoch. In der Praxis würden Vorhersagen für echte neü Studierenden dann deutlich schlechter.

Punktevergabe:
- 2 Punkte: Begründung verständlich (echte Vorhersagekraft prüfen).
- 2 Punkte: klare Definition + Beispiel labeled/unlabeled im Noten-Kontext.
- 1,5 Punkte: Fehlerqülle klar erkannt (Overfitting, Information Leakage, kiesnstliche Metriken).

</div>

### Aufgabe A4: Menge und Qualität von Daten (3 Punkte)

<div style="background-color: #f6f8fa; padding: 10px 12px; border-radius: 6px; border: 1px solid #e1e4e8;">
**Aufgabenstellung:**


Ein Lehrerteam teste ein Noten-Vorhersage-Modell zweimal:
- Szenario A: 30 Studierenden-Datensätze
- Szenario B: 300 Studierenden-Datensätze

Analysiere in 5-7 Sätzen, wie Datenmenge und Datenqualität (z. B. fehlerhafte Anwesenheitsangaben) die Modellgüte bezüglich MSE und R2 verändern. (3 Punkte)

Musterlösung:

- Mit nur 30 Datensätzen kann das Modell nicht alle Lernstile und -erfolgsaspekte erfassen. Es kann Überanpassung gibt: hohe Genauigkeit beim Training, schlechte Generaliserung.
- 300 Datensätze zeigen mehr Variation in Lernmustern und Noten. Das Modell lernt bessere, allgemeinerbare Regeln. MSE bei Testdaten sinkt, R2 steigt.
- Fehlerhafte Anwesenheitsdaten (z. B. vertauschte Prozente) verfälschen das Verhältnis zwischen Anwesenheit und Note. Das Modell lernt die falsche Korrelation.
- Daher: Viele Daten allein reichen nicht – auch Datenbestandteile/Qualität ist entscheidend.

Punktevergabe:
- 1 Punkt: Menge-Effekt erkannt (grössere Datenmenge → bessere Generaliserung).
- 1 Punkt: Qualitäts-Effekt erkannt (Fehler verstellen Muster).
- 1 Punkt: Bezug zu MSE und R2, oder Verständnis für praktische Auswirkungen.

</div>

## Teil B: Praxis (7,5 Punkte)

### Aufgabe B1: Datenverarbeitung und Modelltraining (7,5 Punkte)

<div style="background-color: #f6f8fa; padding: 10px 12px; border-radius: 6px; border: 1px solid #e1e4e8;">
**Aufgabenstellung:**


Schreibe den Code handschriftlich oder in sauberem Pseudocode.

Szenario:
- Dateiname: ../daten/studierende_noten.csv
- Spalten: lern_stunden, anwesenheit_prozent, übungen_bearbeitet, note

1. Lade die CSV-Datei mit Pandas und zeige die ersten 5 Zeilen. (2 Punkte)
2. Berechne Durchschnitt, Minimum und Maximum der Noten. (2,5 Punkte)
3. Teile Daten 80/20, trainiere ein lineares Regressionsmodell und gib MSE und R2 aus. (3 Punkte)

Musterlösung:

</div>

<div style="background-color: #f0f0f0; padding: 10px 14px; border-radius: 6px; font-family: monospace; border-left: 3px solid #cccccc;">

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1) Daten laden
df = pd.read_csv("../daten/studierende_noten.csv")
print(df.head())

# 2) Kennzahlen
mean_note = df["note"].mean()
min_note = df["note"].min()
max_note = df["note"].max()
print("Durchschnitt:", mean_note)
print("Minimum:", min_note)
print("Maximum:", max_note)

# 3) Train-Test Split, Modell, Metriken
X = df[["lern_stunden", "anwesenheit_prozent", "uebungen_bearbeitet"]]
y = df["note"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("MSE:", mse)
print("R2:", r2)
```

</div>

Punktevergabe:
- 2 Punkte: CSV korrekt geladen, head() ausgegeben.
- 2,5 Punkte: mean(), min(), max() auf "note" angewendet.
- 3 Punkte: 80/20 Split, LinearRegression, MSE und R2 berechnet/ausgegeben.

## Korrekturhinweis für handschriftliche Lösungen

- Fachlogik zählt mehr als syntaktische Perfektion.
- Verständliche Variablennamen, auch wenn sie küssungen kürsungen werden, sind akzeptabel.
- Pseudocode oder stichwortartige Code-Fragmenty will accepted, wenn Logik und Schritte klar erkennbar sind.
