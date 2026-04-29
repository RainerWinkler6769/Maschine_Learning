# Musterlösung: Aufgabe 01 – Daten erkunden mit Pandas

```python
import pandas as pd
import matplotlib.pyplot as plt

# a) Daten laden
df = pd.read_csv("../../notebooks/daten/haeuser.csv")
print(df.head())

# b) Struktur verstehen
print("Form:", df.shape)
print("Spalten:", df.columns.tolist())
df.info()

# c) Statistiken berechnen
print("\nDurchschnittlicher Preis:", df["preis_euro"].mean())
print("Teuerster Preis:         ", df["preis_euro"].max())
print("Günstigster Preis:       ", df["preis_euro"].min())
print(df.describe())

# d) Visualisierung

# Histogramm der Preise
plt.figure()
plt.hist(df["preis_euro"], bins=20, color="steelblue", edgecolor="black")
plt.xlabel("Preis (Euro)")
plt.ylabel("Anzahl")
plt.title("Verteilung der Hauspreise")
plt.tight_layout()
plt.show()

# Streudiagramm: Größe vs. Preis
plt.figure()
plt.scatter(df["groesse_m2"], df["preis_euro"], alpha=0.5, color="steelblue")
plt.xlabel("Größe (m²)")
plt.ylabel("Preis (Euro)")
plt.title("Hausgröße vs. Preis")
plt.tight_layout()
plt.show()
```
