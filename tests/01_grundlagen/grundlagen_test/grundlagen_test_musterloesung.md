# Musterlösung: Grundlagen-Test (KI/ML und Python)

- Gesamtpunkte: 25
- Theorie: 17,5 Punkte
- Praxis: 7,5 Punkte

## Teil A: Theorie (17,5 Punkte)

### Aufgabe A1: Begriffe sicher unterscheiden (6 Punkte)

<div style="background-color: #f6f8fa; padding: 10px 12px; border-radius: 6px; border: 1px solid #e1e4e8;">
**Aufgabenstellung:**


Ergänze die Tabelle mit einer kurzen Definition und einem passenden Beispiel.

| Begriff | Kurzdefinition | Beispiel aus Alltag oder Wirtschaft |
|---|---|---|
| KI |  |  |
| Machine Learning |  |  |
| Deep Learning |  |  |

Musterlösung:

| Begriff | Kurzdefinition | Beispiel aus Alltag oder Wirtschaft |
|---|---|---|
| KI | Oberbegriff für Systeme, die Aufgaben mit intelligentem Verhalten lösen. | Chatbot im Kundenservice beantwortet Standardanfragen. |
| Machine Learning | Teilgebiet der KI: Modelle lernen Muster aus Daten statt nur fester Regeln. | Spamfilter lernt aus markierten E-Mails. |
| Deep Learning | Teilgebiet von ML mit mehrschichtigen neuronalen Netzen. | Bilderkennung in einer Qualitätskontrolle. |

Punktevergabe:
- Pro Zeile 2 Punkte: 1 Punkt Definition, 1 Punkt passendes Beispiel.

</div>

### Aufgabe A2: Regelbasiert vs. datenbasiert (3 Punkte)

<div style="background-color: #f6f8fa; padding: 10px 12px; border-radius: 6px; border: 1px solid #e1e4e8;">
**Aufgabenstellung:**


1. Erkläre den Unterschied zwischen regelbasierter und datenbasierter Lösung in 2-4 Sätzen. (2 Punkte)
2. Nenne ein konkretes Beispiel für beide Ansätze. (1 Punkt)

Musterlösung:

- Regelbasiert bedeutet: Entscheidungen erfolgen über feste Wenn-Dann-Regeln, die von Menschen vorgegeben werden.
- Datenbasiert bedeutet: Ein Modell lernt Zusammenhänge aus Beispieldaten und trifft darauf basierend Vorhersagen.
- Beispiel regelbasiert: Wenn Rechnungsbetrag > 1000 Euro, dann zweite Freigabe nötig.
- Beispiel datenbasiert: Modell schätzt Hauspreise aus Wohnfläche, Zimmern und Baujahr.

Punktevergabe:
- 2 Punkte für korrekte Erklärung (beide Ansätze klar abgegrenzt).
- 1 Punkt für mindestens ein korrektes Beispiel je Ansatz (oder ein sehr gutes Vergleichsbeispiel).

</div>

### Aufgabe A3: Training, Test, labeled, unlabeled (5,5 Punkte)

<div style="background-color: #f6f8fa; padding: 10px 12px; border-radius: 6px; border: 1px solid #e1e4e8;">
**Aufgabenstellung:**


1. Warum müssen Trainingsdaten und Testdaten getrennt sein? (2 Punkte)
2. Erkläre labeled Data und unlabeled Data jeweils mit einem Beispiel aus dem Hauspreis-Kontext. (2 Punkte)
3. Darf ein Modell Testdaten beim Lernen sehen? Begründe kurz. (1,5 Punkte)

Musterlösung:

1. Training und Test müssen getrennt sein, damit fair geprüft wird, ob das Modell auf unbekannten Daten funktioniert. Sonst wäre das Ergebnis zu optimistisch.
2. labeled Data im Hauskontext: Eingaben (groesse_m2, zimmer, baujahr) plus Zielwert preis_euro. unlabeled Data: gleiche Eingaben, aber ohne preis_euro.
3. Testdaten dürfen nicht beim Lernen verwendet werden, weil sonst Informationsleck (Data Leakage) entsteht und die Bewertung unzuverlässig wird.

Punktevergabe:
- 2 Punkte für gute Begründung der Trennung.
- 2 Punkte für korrekte Definition + Beispiel labeled/unlabeled.
- 1,5 Punkte für klare Antwort auf Testdatenfrage mit Begründung.

</div>

### Aufgabe A4: Datenmenge und Datenqualität bewerten (3 Punkte)

<div style="background-color: #f6f8fa; padding: 10px 12px; border-radius: 6px; border: 1px solid #e1e4e8;">
**Aufgabenstellung:**


Ein Team trainiert dasselbe Regressionsmodell zweimal:
- Lauf 1: 20 Datensätze
- Lauf 2: vollständiger Datensatz

Bewerte in 4-6 Sätzen, wie sich Datenmenge und Datenqualität auf MSE und R2 auswirken können. (3 Punkte)

Musterlösung:

- Bei nur 20 Datensätzen lernt das Modell oft instabil und verallgemeinert schlechter.
- Mit mehr Daten werden Muster besser erfasst, wodurch MSE typischerweise sinkt und R2 steigen kann.
- Schlechte Datenqualität (Ausreisser, fehlende Werte, falsche Einheiten) kann die Güte trotz grosser Datenmenge verschlechtern.
- Gute Datenqualität und ausreichende Datenmenge zusammen liefern meist robustere Vorhersagen.

Punktevergabe:
- 1 Punkt: Effekt der Datenmenge.
- 1 Punkt: Effekt der Datenqualität.
- 1 Punkt: Bezug zu MSE/R2 fachlich korrekt.

</div>

## Teil B: Praxis (7,5 Punkte)

### Aufgabe B1: Python/Pandas-Grundablauf (7,5 Punkte)

<div style="background-color: #f6f8fa; padding: 10px 12px; border-radius: 6px; border: 1px solid #e1e4e8;">
**Aufgabenstellung:**


Schreibe den Code handschriftlich oder in sauberem Pseudocode. Nutze folgende Annahme:
- Dateiname: ../notebooks/daten/haeuser.csv
- wichtige Spalten: groesse_m2, zimmer, baujahr, preis_euro

1. Lade die CSV-Datei mit Pandas und gib die ersten 5 Zeilen aus. (2 Punkte)
2. Berechne den durchschnittlichen, minimalen und maximalen Hauspreis. (2,5 Punkte)
3. Teile die Daten in Training/Test (80/20), trainiere eine lineare Regression und gib MSE und R2 aus. (3 Punkte)

Musterlösung:

</div>

<div style="background-color: #f0f0f0; padding: 10px 14px; border-radius: 6px; font-family: monospace; border-left: 3px solid #cccccc;">

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1) CSV laden und erste Zeilen anzeigen
df = pd.read_csv("../notebooks/daten/haeuser.csv")
print(df.head())

# 2) Grundstatistiken Preis
durchschnitt = df["preis_euro"].mean()
minimum = df["preis_euro"].min()
maximum = df["preis_euro"].max()
print(durchschnitt, minimum, maximum)

# 3) Split, Modell, Kennzahlen
X = df[["groesse_m2", "zimmer", "baujahr"]]
y = df["preis_euro"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

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
- 2 Punkte: CSV korrekt geladen, `head()` ausgegeben.
- 2,5 Punkte: Mittelwert, Minimum, Maximum korrekt aus `preis_euro` berechnet.
- 3 Punkte: korrekter 80/20-Split, lineare Regression trainiert, MSE und R2 ausgegeben.

## Korrekturhinweis für handschriftliche Lösungen

- Fachlogik geht vor perfekter Syntax.
- Leichte Schreibfehler in Variablennamen können toleriert werden, wenn der Ablauf klar und richtig ist.
- Auch strukturierter Pseudocode kann voll bewertet werden, wenn alle geforderten Schritte vorhanden sind.
