# Schritt-für-Schritt: Histogramm der Hauspreise live im Codespace testen

Diese Anleitung zeigt dir, wie du das Diagramm aus Aufgabe d in deinem Codespace sichtbar machen kannst.

## Ziel
Du willst das Histogramm der Hauspreise aus der Datei loesung_01grundlagen.py ausführen und ansehen.

## 1) Datei öffnen
1. Öffne im Explorer den Ordner src/python-api.
2. Öffne die Datei loesung_01grundlagen.py.
3. Prüfe, dass der Abschnitt Aufgabe d vorhanden ist (Histogramm der Hauspreise).

## 2) Terminal im richtigen Ordner starten
1. Öffne ein Terminal in VS Code.
2. Wechsle in den Ordner:

   cd /workspaces/edu-code-course-ml/src/python-api

## 3) Script ausführen
Führe das Script aus:

python loesung_01grundlagen.py

Hinweis:
- Wenn die Plot-Ausgabe im Codespace-UI direkt angezeigt wird, ist alles fertig.
- Falls kein Fenster erscheint (häufig im Container), nutze Schritt 4 mit Bilddatei.

## 4) Sichere Variante: Diagramm als PNG speichern
Wenn du das Diagramm nicht direkt siehst, ersetze am Ende von Aufgabe d die Zeile mit plt.show() durch:

plt.savefig("histogramm_hauspreise.png", dpi=150)
print("Diagramm gespeichert als histogramm_hauspreise.png")

Danach erneut ausführen:

python loesung_01grundlagen.py

## 5) Ergebnis anzeigen
1. Öffne im Explorer die Datei histogramm_hauspreise.png im Ordner src/python-api.
2. VS Code zeigt dir das Diagramm direkt an.

## 6) Typische Probleme und schnelle Lösungen
- Problem: ModuleNotFoundError für pandas oder matplotlib
  - Lösung:

    pip install -r requirements.txt

- Problem: Datei haeuser.csv nicht gefunden
  - Lösung: Script wirklich aus src/python-api starten (siehe Schritt 2), da der relative Pfad sonst nicht passt.

## 7) Optional: Direktes Arbeiten im Notebook
Wenn du lieber interaktiv arbeitest:
1. Öffne ein Notebook im Ordner notebooks.
2. Führe die Imports und den Histogramm-Code in einer Zelle aus.
3. Dort wird das Diagramm normalerweise direkt unter der Zelle angezeigt.

Viel Erfolg beim Testen.