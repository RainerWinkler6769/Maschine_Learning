import numpy as np
import pandas as pd
from pathlib import Path


BASE_DATA_PATH = Path("../../notebooks/daten/haeuser.csv")
TARGET_DATA_PATH = Path("../../notebooks/daten/haeuser_80.csv")
TARGET_SIZE = 80
RANDOM_SEED = 42


def _clip_int(values, lower, upper):
    return np.clip(np.rint(values), lower, upper).astype(int)


def build_dataset_80(base_df: pd.DataFrame, target_size: int = TARGET_SIZE) -> pd.DataFrame:
    if len(base_df) >= target_size:
        return base_df.head(target_size).copy()

    rng = np.random.default_rng(RANDOM_SEED)
    needed = target_size - len(base_df)

    sampled = base_df.sample(n=needed, replace=True, random_state=RANDOM_SEED).reset_index(drop=True)

    groesse = sampled["groesse_m2"].to_numpy(dtype=float) + rng.normal(0, 8, needed)
    zimmer = sampled["zimmer"].to_numpy(dtype=float) + rng.normal(0, 0.6, needed)
    baujahr = sampled["baujahr"].to_numpy(dtype=float) + rng.normal(0, 6, needed)
    preis = sampled["preis_euro"].to_numpy(dtype=float) + rng.normal(0, 18000, needed)

    synthetic = pd.DataFrame(
        {
            "groesse_m2": _clip_int(groesse, 30, 250),
            "zimmer": _clip_int(zimmer, 1, 8),
            "baujahr": _clip_int(baujahr, 1950, 2025),
            "preis_euro": _clip_int(preis, 80000, 900000),
        }
    )

    combined = pd.concat([base_df, synthetic], ignore_index=True)
    return combined.head(target_size)


def main() -> None:
    base_df = pd.read_csv(BASE_DATA_PATH)

    required_columns = {"groesse_m2", "zimmer", "baujahr", "preis_euro"}
    missing = required_columns.difference(base_df.columns)
    if missing:
        raise ValueError(f"Fehlende Spalten in Quelldatei: {sorted(missing)}")

    dataset_80 = build_dataset_80(base_df, TARGET_SIZE)
    TARGET_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    dataset_80.to_csv(TARGET_DATA_PATH, index=False)

    print(f"Quelle: {BASE_DATA_PATH} ({len(base_df)} Zeilen)")
    print(f"Ziel:   {TARGET_DATA_PATH} ({len(dataset_80)} Zeilen)")
    print("Hinweis: Zusatzdaten sind synthetisch erzeugt.")


if __name__ == "__main__":
    main()