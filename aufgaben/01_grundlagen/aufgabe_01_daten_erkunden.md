# Aufgabe 01: Daten erkunden mit Pandas

**Schwierigkeit:** Einsteiger  
**Thema:** Datenanalyse  
**Hilfsmittel:** [Python-Grundlagen](../../informationen/python/python-grundlagen.md), [Cheatsheet](../../informationen/cheatsheets/ml-python-cheatsheet.md), [Daten-Grundlagen (Schnellstart)](../../informationen/grundlagen/ki-und-ml.md#schnellstart-daten-grundlagen-fuer-aufgaben-und-tests)

---

## Aufgabenstellung

Du hast einen Datensatz mit Informationen über Häuser (Größe, Zimmeranzahl, Preis).  
Deine Aufgabe ist es, diesen Datensatz zu laden, zu erkunden und erste Erkenntnisse zu gewinnen.

---

## Teilaufgaben

### a) Daten laden
Lade den Datensatz `../notebooks/daten/haeuser.csv` mit Pandas und zeige die ersten 5 Zeilen an.

### b) Struktur verstehen
- Wie viele Zeilen und Spalten hat der Datensatz? (`df.shape`)
- Welche Spalten gibt es? (`df.columns`)
- Gibt es fehlende Werte? (`df.info()`)

### c) Statistiken berechnen
- Was ist der durchschnittliche Hauspreis?
- Was ist der teuerste und günstigste Preis?
- Nutze `df.describe()` für eine Übersicht.

### d) Visualisierung
- Erstelle ein Histogramm der Hauspreise
- Erstelle ein Streudiagramm: Größe (m²) vs. Preis

---

## Erwartetes Ergebnis

- Du kannst den Datensatz laden und ausgeben
- Du kennst Grundstatistiken (Mittelwert, Min, Max)
- Du hast zwei Diagramme erstellt

---

## Tipp

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../notebooks/daten/haeuser.csv")
print(df.head())
```
