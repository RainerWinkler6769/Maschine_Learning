# Werkzeuge: Jupyter Notebook

## Was ist Jupyter Notebook?

Jupyter Notebook ist eine interaktive Entwicklungsumgebung, in der du **Code schreiben, ausführen und Ergebnisse direkt sehen** kannst – alles in einem Dokument. Ideal für ML-Experimente.

---

## Starten

```bash
jupyter notebook
```
→ Öffnet sich automatisch im Browser unter `http://localhost:8888`

---

## Die wichtigsten Tastenkürzel

### Im Befehlsmodus (blaue Linie links, `Esc` zum Aktivieren)

| Taste | Aktion |
|-------|--------|
| `A` | Neue Zelle **oberhalb** einfügen |
| `B` | Neue Zelle **unterhalb** einfügen |
| `D D` | Zelle **löschen** |
| `M` | Zelle zu **Markdown** (Text) umwandeln |
| `Y` | Zelle zu **Code** umwandeln |
| `Shift + Enter` | Zelle ausführen und zur nächsten springen |

### Im Bearbeitungsmodus (grüne Linie links, `Enter` zum Aktivieren)

| Taste | Aktion |
|-------|--------|
| `Shift + Enter` | Zelle ausführen |
| `Ctrl + Z` | Rückgängig |
| `Tab` | Code-Vervollständigung |

---

## Zellen-Typen

- **Code-Zelle**: Enthält Python-Code, der ausgeführt wird
- **Markdown-Zelle**: Enthält formatierten Text (Erklärungen, Überschriften)

---

## Typischer Aufbau eines ML-Notebooks

```
1. Imports (numpy, pandas, sklearn, ...)
2. Daten laden und anschauen
3. Daten aufbereiten (bereinigen, transformieren)
4. Modell auswählen und trainieren
5. Modell testen und bewerten
6. Ergebnisse visualisieren
```

---

## Pakete installieren (direkt im Notebook)

```python
# Mit ! können Shell-Befehle im Notebook ausgeführt werden
!pip install scikit-learn pandas matplotlib
```
