# Python-API: Schnellstart im Codespace

Diese Anleitung hilft dir, die Skripte in `src/python-api` schnell zu starten und zu testen.

## 1) In den richtigen Ordner wechseln

```bash
cd /workspaces/edu-code-course-ml/src/python-api
```

## 2) Optional: Virtuelle Umgebung erstellen

```bash
python -m venv .venv
source .venv/bin/activate
```

Hinweis: Im Codespace funktioniert es oft auch ohne eigenes venv, aber mit venv ist es sauberer.

## 3) Abhängigkeiten installieren

```bash
pip install -r requirements.txt
```

## 4) Aufgabe 1 testen (Daten + Diagramme)

```bash
python loesung_01grundlagen.py
```

Falls im Terminal kein Plot-Fenster erscheint:
- In der Datei `loesung_01grundlagen.py` `plt.show()` durch `plt.savefig("histogramm_hauspreise.png", dpi=150)` ersetzen.
- Danach erneut ausführen und die PNG-Datei im Explorer öffnen.

## 5) Aufgabe A3 testen (Regression)

```bash
python loesung_a3grundlagen.py
```

Erwartung: Ausgabe mit `klein:` und `gross:` inklusive MSE- und R2-Wert.

## 6) Häufige Probleme

- `ModuleNotFoundError`:
  - Nochmals `pip install -r requirements.txt` ausführen.
- CSV nicht gefunden:
  - Script wirklich aus `src/python-api` starten (wegen relativem Pfad zur CSV).

## 7) Nützliche Kurzbefehle

```bash
# installierte Pakete prüfen
pip list

# Python-Version prüfen
python --version
```
