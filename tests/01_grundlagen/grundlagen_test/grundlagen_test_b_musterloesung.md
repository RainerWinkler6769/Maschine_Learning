# Musterlösung: Grundlagen-Test – Version B (KI/ML und Python)

- Gesamtpunkte: 25
- Theorie: 17,5 Punkte
- Praxis: 7,5 Punkte

## Teil A: Theorie (17,5 Punkte)

### Aufgabe A1: Begriffe und ihre Anwendung (6 Punkte)

<div style="background-color: #f6f8fa; padding: 10px 12px; border-radius: 6px; border: 1px solid #e1e4e8;">
**Aufgabenstellung:**


Ordne folgende Begriffe den Beschreibungen zu und nenne jeweils ein Beispiel:

| Konzept | Kurze Erklärung | Beispiel aus Alltag oder Industrie |
|---|---|---|
| Künstliche Intelligenz |  |  |
| Machine Learning |  |  |
| Neuronale Netze |  |  |

Musterlösung:

| Konzept | Kurze Erklärung | Beispiel aus Alltag oder Industrie |
|---|---|---|
| Künstliche Intelligenz | Oberbegriff für intelligente Maschinen, die Probleme lösen und Entscheidungen treffen. | Autonome Fahrzeuge navigieren eigenständig im Strassenverkehr. |
| Machine Learning | Teilgebiet der KI: Systeme lernen Muster aus Trainingsdaten statt vorherzuprogrammierter Regeln. | Empfehlungssystem, das Filme basierend auf Zuschaür-Verhalten vorschlägt. |
| Neuronale Netze | Tiefer liegende ML-Methode mit verschachtelten Schichten, inspiriert von Gehirn-Struktur. | Spracherkennung in Smartphones, die gesprochene Befehle in Text konvertiert. |

Punktevergabe:
- Pro Zeile 2 Punkte: 1 Punkt Erklärung, 1 Punkt passendes Beispiel.

</div>

### Aufgabe A2: Fest programmiert vs. lernend (3 Punkte)

<div style="background-color: #f6f8fa; padding: 10px 12px; border-radius: 6px; border: 1px solid #e1e4e8;">
**Aufgabenstellung:**


1. Erkläre in 2-4 Sätzen, worin sich fest programmierte Systeme von lernenden Systemen unterscheiden. (2 Punkte)
2. Gib zwei konkrete Alltagsbeispiele: eines, das fest programmiert ist, eins, das lernt. (1 Punkt)

Musterlösung:

1. Fest programmierte Systeme folgen vorgegebenen Regeln und verändern sich nicht. Lernende Systeme passen sich basierend auf neün Daten an und verbessern ihre Vorhersagen oder Entscheidungen über die Zeit. Programmierte Systeme sind überall gleich, lernende Systeme werdan durch ihre Daten "geformt".
2. Fest programmiert: Taschenrechner berechnet 2+3 immer gleich. Lernend: Spam-Filter passt sich an neü Spam-Muster an.

Punktevergabe:
- 2 Punkte: Unterschied klar erklärt (Regeln vs. Lernen).
- 1 Punkt: Mindestens ein korrektes Beispiel pro Kategorie.

</div>

### Aufgabe A3: Trainings- und Testphase in ML (5,5 Punkte)

<div style="background-color: #f6f8fa; padding: 10px 12px; border-radius: 6px; border: 1px solid #e1e4e8;">
**Aufgabenstellung:**


Arbeite mit dem Kontext: Ein Unternehmen möchte die Restwertpreise von Autos vorhersagen (Alter, KM-Stand, PS).

1. Warum ist eine Aufteilung in Trainings- und Testdaten sinnvoll? (2 Punkte)
2. Erkläre, was labeled Data und unlabeled Data in diesem Kontext bedeuten (mit jeweils einem Beispiel). (2 Punkte)
3. Was wäre die Folge, wenn Testdaten beim Training "mitlernen" dürfen? (1,5 Punkte)

Musterlösung:

1. Die Aufteilung prüft, ob das Modell wirklich generalisieren kann und nicht nur die Trainingsbeispiele "auswendig lernt". Mit separaten Testdaten kann man objektiv bewerten, wie gut das Modell auf neün, unbekannten Auto-Daten funktioniert.

2. labeled Data: Auto-Datensätze mit Eingaben (Alter, KM, PS) UND bekanntem Zielwert (aktüller Preis). unlabeled Data: Auto-Informationen ohne bekannte Preise – das Modell könnte diese später vorhersagen.

3. Wenn Testdaten bei Training "mitgelernt" werden, entsteht ein Informationsleck: Das Modell kennt die richtige Antwort bereits. Die Testergebnisse wären viel zu positiv und unrealistisch, sodass man nicht weiss, wie gut das Modell wirklich ist.

Punktevergabe:
- 2 Punkte: Gute Begründung (Prüfung auf Generaliserung).
- 2 Punkte: Klare Definition labeled/unlabeled mit Auto-Kontext.
- 1,5 Punkte: Korrekte Antwort zu Data Leakage und Konseqünzen.

</div>

### Aufgabe A4: Einfluss von Datenmenge und Datenbestand (3 Punkte)

<div style="background-color: #f6f8fa; padding: 10px 12px; border-radius: 6px; border: 1px solid #e1e4e8;">
**Aufgabenstellung:**


Ein Team testet ein Regressionsmodell zweimal:
- Experiment 1: 25 Auto-Datensätze
- Experiment 2: 500 Auto-Datensätze

Begründe in 4-6 Sätzen, welche Auswirkungen Datenmenge und Datenqualität (z. B. fehlerhafte KM-Angaben) auf die Vorhersagegüte haben können. (3 Punkte)

Musterlösung:

- Mit nur 25 Datensätzen ist das Modell anfällig für Überanpassung und Unstäbilkeit. Mit 500 Datensätzen erfasst das Modell wahrscheinlich mehr Variation in Auto-Preisen und generalisiert besser.
- Fehlerhafte KM-Angaben (z. B. vertauschte Dezimalstellen) verzerren Vorhersagen. Schlechte Datenqualität kann MSE erhöhen und R2 verringern, selbst bei grosser Datenmenge.
- Daher ist es entscheidend, sowohl ausreichend Daten als auch saubere Daten zu haben.

Punktevergabe:
- 1 Punkt: Einfluss der Menge (mehr Daten → bessere Generaliserung).
- 1 Punkt: Einfluss der Qualität (Fehler → schlechtere Vorhersagen).
- 1 Punkt: Bezug zu MSE/R2 oder klare Auswirkung nachvollziehbar.

</div>

## Teil B: Praxis (7,5 Punkte)

### Aufgabe B1: Datenverarbeitung mit Python/Pandas (7,5 Punkte)

<div style="background-color: #f6f8fa; padding: 10px 12px; border-radius: 6px; border: 1px solid #e1e4e8;">
**Aufgabenstellung:**


Schreibe den Code handschriftlich oder in sauberem Pseudocode.

Szenario:
- Dateiname: ../daten/auto_preise.csv
- Spalten: alter_jahre, km_stand, ps, preis_euro

1. Lade die CSV-Datei mit Pandas, gib die ersten 5 Zeilen aus. (2 Punkte)
2. Berechne Durchschnitt, Minimum und Maximum des Preises. (2,5 Punkte)
3. Teile die Daten 80/20 auf, trainiere ein lineares Regressionsmodell und gib MSE sowie R2 aus. (3 Punkte)

Musterlösung:

</div>

<div style="background-color: #f0f0f0; padding: 10px 14px; border-radius: 6px; font-family: monospace; border-left: 3px solid #cccccc;">

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1) Daten laden und erste Zeilen
df = pd.read_csv("../daten/auto_preise.csv")
print(df.head())

# 2) Kennzahlen berechnen
avg_price = df["preis_euro"].mean()
min_price = df["preis_euro"].min()
max_price = df["preis_euro"].max()
print("Durchschnitt:", avg_price)
print("Minimum:", min_price)
print("Maximum:", max_price)

# 3) Split, Modell, Metriken
X = df[["alter_jahre", "km_stand", "ps"]]
y = df["preis_euro"]

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
- 2 Punkte: CSV geladen, head() ausgegeben, richtiger Dateipfad.
- 2,5 Punkte: mean(), min(), max() korrekt auf preis_euro angewandt.
- 3 Punkte: Train/Test Split 80/20, LinearRegression, MSE und R2 berechnet und ausgegeben.

## Korrekturhinweis für handschriftliche Lösungen

- Fachlogik geht vor perfekter Syntax.
- Leichte Abweichungen bei Spaltennamen  (z. B. "Durchschnitt" statt "avg_price") sind akzeptabel, wenn die Logik richtig ist.
- Strukturierter Pseudocode wird vollständig anerkannt, wenn alle Schritte vorhanden sind.
