# Tests

Dieses Verzeichnis enthält automatisierte Tests, mit denen Schüler ihre Lösungen selbst überprüfen können.

## Struktur

<div style="background-color: #f0f0f0; padding: 10px 14px; border-radius: 6px; font-family: monospace; border-left: 3px solid #cccccc;">

```
tests/
├── 01_grundlagen/
│   ├── test_aufgabe_01.py
│   ├── test_a1_kursstart_python.py
│   └── test_a3_datenqualitaet_training_test.py
├── 03_regression/
│   └── test_a2_verfahrenvergleich_ml.py
├── 04_fortgeschritten/
│   ├── test_b1_b2_visualisierung_und_bibliotheken.py
│   ├── test_b3_b4_toolauswahl_und_projekt.py
│   └── test_bpe_kompetenz_mapping.py
└── live/
	├── security_smoke.sh
	└── test_live_stack.sh
```

</div>

## BPE-6/7-Abdeckung

- A1: Einstieg KI/ML und Python
- A2: Verfahrensvergleich (Regression, Entscheidungsbaum, k-Means, k-NN)
- A3: Datenqualität, Training/Test, labeled/unlabeled
- B1/B2: Visualisierung und Einsatz von KI-Programmbibliotheken
- B3/B4: Toolauswahl und Anwendungsprojekt im BWL-Kontext

## Tests ausführen

<div style="background-color: #f0f0f0; padding: 10px 14px; border-radius: 6px; font-family: monospace; border-left: 3px solid #cccccc;">

```bash
# Alle Tests
python -m pytest tests/ -v

# Tests für eine bestimmte Aufgabe
python -m pytest tests/01_grundlagen/ -v
python -m pytest tests/03_regression/ -v
python -m pytest tests/04_fortgeschritten/ -v

# Live-Test der Docker-Anwendung
chmod +x tests/live/test_live_stack.sh
./tests/live/test_live_stack.sh

# Security-Smoke-Test der Docker-Anwendung
chmod +x tests/live/security_smoke.sh
./tests/live/security_smoke.sh
```

</div>

## Hinweise für Schüler

- Vor dem Testlauf: Nutze das [Daten-Grundlagen Kurzblatt](../informationen/grundlagen/daten-grundlagen-kurz.md) fuer einen schnellen 1-Seiten-Check.
- Vor A2-Tests: Nutze den Abschnitt [Schnellstart: Algorithmische Verfahren fuer A2 und Tests](../informationen/grundlagen/ki-und-ml.md#schnellstart-algorithmische-verfahren-fuer-a2-und-tests).
- Vor A4 und passenden Kompetenztests: Nutze den Abschnitt [Schnellstart: Neuronale Netze fuer A4 und Tests](../informationen/grundlagen/ki-und-ml.md#schnellstart-neuronale-netze-fuer-a4-und-tests).
- Die Tests prüfen, ob deine Lösung das richtige Ergebnis liefert
- Ein ✓ (grün) bedeutet: Test bestanden
- Ein ✗ (rot) bedeutet: Noch nicht korrekt – lies die Fehlermeldung genau
- Die Tests geben dir Hinweise, aber nicht die vollständige Lösung
