# Lehrkraft-Kurzreferenz: Tests im KI/ML-Kurs (BPE 6/7)

Diese Kurzreferenz hilft Lehrkraeften, die neuen Kurs-Tests schnell und sicher im Unterricht einzusetzen.

## Ziel der Tests

- Lernfortschritt transparent machen
- Selbstkontrolle der Lernenden foerdern
- Mindeststandards fuer BPE 6 und BPE 7 absichern
- Einheitliche Qualitaet fuer den landesweiten Einsatz unterstuetzen

## Schnellstart im Unterricht

1. In den Projektordner wechseln.
2. Tests mit Python starten.
3. Ergebnis gemeinsam interpretieren.

```bash
cd edu-code-course-ml
python3 -m pytest tests/ -v
```

## Empfohlene Reihenfolge je Lernphase

```bash
# Einstieg und Datengrundlagen (A1, A3)
python3 -m pytest tests/01_grundlagen/ -v

# Verfahrenvergleich (A2)
python3 -m pytest tests/03_regression/ -v

# Vertiefung und Transfer (B1-B4 + BPE-Mapping)
python3 -m pytest tests/04_fortgeschritten/ -v
```

## Was wird geprueft?

- Verfuegbarkeit und Struktur von Aufgaben/Notebooks
- Datenqualitaet und Train/Test-Logik
- Grundverhalten zentraler ML-Verfahren
- Einsatz von Visualisierung und KI-Bibliotheken
- BPE-konforme Abdeckung von Pflichtinhalten im Marschplan

## Didaktischer Einsatz im Unterricht

- Vor einer Einheit: Kurztest als Diagnose nutzen
- Waehrend der Einheit: Teiltests fuer Zwischenfeedback einsetzen
- Nach einer Einheit: Volltest zur Lernerfolgssicherung durchfuehren
- In Reflexionsphasen: Fehlermeldungen als Lernanlass verwenden

## Umgang mit Fehlermeldungen

1. Fehlermeldung laut vorlesen lassen.
2. Fachbegriff markieren (z. B. Trainingsdaten, k-Means, R2).
3. Zur passenden Aufgabe oder Notebook-Stelle zurueckgehen.
4. Korrektur vornehmen und Test erneut starten.

## Mindestanforderung fuer Kursfreigabe

- Alle Tests in `tests/` laufen lokal fehlerfrei durch.
- CI-Workflow `ML Course Tests` ist in GitHub gruen.
- Marschplan weist die BPE-6/7-Pflichtinhalte explizit nach.

## Hinweise

- Tests ersetzen keine paedagogische Bewertung, sie ergaenzen sie.
- Fuer projektorientierte Leistungen (B4) immer Produkt, Prozess und Reflexion gemeinsam bewerten.

## Bewertungsmatrix

- Verbindliche Modulmatrix A1-B4: `../lehrplan/bewertungsmatrix-a1-b4.md`
- Druckfertiger Bewertungsbogen (1 Seite je Modul): `../lehrplan/bewertungsbogen-a1-b4-druckversion.md`
- Kompaktbogen (2 Seiten, Klassenuebersicht): `../lehrplan/bewertungsbogen-a1-b4-kompakt-2seiten.md`
- Einzelbogen erweitert (pro Lernende Person): `../lehrplan/bewertungsbogen-einzelperson-erweitert.md`
- PDF-Exportversion (seitenoptimiert): `../lehrplan/bewertungsbogen-a1-b4-pdf-export.md`
