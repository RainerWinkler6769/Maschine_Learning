import pandas as pd
from pathlib import Path
import math
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Daten laden: fuer den Vergleich klein vs gross wird ein Datensatz mit 80 Zeilen erwartet.
data_path = Path("../../notebooks/daten/haeuser_80.csv")
if not data_path.exists():
    raise FileNotFoundError(
        "Datei notebooks/daten/haeuser_80.csv fehlt. "
        "Bitte zuerst 'python generate_haeuser_80.py' ausfuehren."
    )

df = pd.read_csv(data_path)

# Zwei Datenmengen
df_klein = df.head(20)
df_gross = df.copy()

if len(df_gross) < 80:
    raise ValueError(
        f"Fuer diese Aufgabe werden 80 Zeilen erwartet, gefunden: {len(df_gross)}"
    )


def erklaere_metriken(mse: float, r2: float) -> str:
    rmse = math.sqrt(mse)

    if r2 < 0:
        r2_text = "schwach (schlechter als ein Mittelwert-Modell)"
    elif r2 < 0.5:
        r2_text = "verbesserungsfaehig"
    elif r2 < 0.8:
        r2_text = "solide"
    else:
        r2_text = "sehr gut"

    return (
        f"MSE={mse:.2f} (kleiner ist besser), "
        f"RMSE={rmse:.2f} Euro (typischer Fehler in Ziel-Einheit), "
        f"R2={r2:.4f} ({r2_text})."
    )

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
rmse_klein = math.sqrt(mse_klein)
rmse_gross = math.sqrt(mse_gross)

print(f"Anzahl Datensaetze klein: {len(df_klein)}")
print(f"Anzahl Datensaetze gross: {len(df_gross)}")
print("klein:", mse_klein, r2_klein)
print(f"RMSE klein: {rmse_klein:.2f} Euro")
print("Interpretation klein:", erklaere_metriken(mse_klein, r2_klein))
print("gross:", mse_gross, r2_gross)
print(f"RMSE gross: {rmse_gross:.2f} Euro")
print("Interpretation gross:", erklaere_metriken(mse_gross, r2_gross))

print("\nMerksatz:")
print("- MSE misst die durchschnittliche quadratische Abweichung in Preis^2 (niedriger ist besser).")
print("- RMSE ist die Wurzel aus MSE und liegt wieder in Euro (anschaulicher fuer Berichte).")
print("- R2 misst den erklaerten Varianzanteil (hoeher ist besser, 1.0 ist ideal).")