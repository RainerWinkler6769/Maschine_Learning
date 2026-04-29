# Musterloesung B2: KI-Programmbibliotheken

## Beispielworkflow

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Daten laden
df = pd.read_csv("../../notebooks/daten/haeuser.csv")
X = df[["groesse_m2", "zimmer", "baujahr"]]
y = df["preis_euro"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modell
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("MSE:", mean_squared_error(y_test, y_pred))
print("R2:", r2_score(y_test, y_pred))
```

## Vergleichsvariante

- Variante A: nur groesse_m2
- Variante B: groesse_m2 + zimmer + baujahr

Fachlich erwartbar: Variante B erzielt meist stabilere Guete, da mehr erklaerende Information vorliegt.
