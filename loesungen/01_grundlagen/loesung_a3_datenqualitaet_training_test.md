# Musterloesung A3: Datenqualitaet, Training/Test, labeled/unlabeled

## Beispielcode

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Daten laden
df = pd.read_csv("../../notebooks/daten/haeuser.csv")

# Zwei Datenmengen
df_klein = df.head(20)
df_gross = df.copy()

def train_eval(data):
    X = data[["groesse_m2", "zimmer", "baujahr"]]
    y = data["preis_euro"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    return mean_squared_error(y_test, y_pred), r2_score(y_test, y_pred)

mse_klein, r2_klein = train_eval(df_klein)
mse_gross, r2_gross = train_eval(df_gross)

print("klein:", mse_klein, r2_klein)
print("gross:", mse_gross, r2_gross)
```

## Fachliche Kernaussagen

- labeled Data enthalten Eingaben plus Zielwert (z. B. Preis).
- unlabeled Data enthalten keine Zielspalte.
- Groessere und saubere Datenmengen verbessern oft die Vorhersagequalitaet.
- Testdaten duerfen nicht zum Training verwendet werden.
