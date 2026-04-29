# Grundlagen KI und ML - Skript (ca. 30 LPE)

Dieses Skript ist als durchgehender Lernpfad fuer den schulischen Einsatz gedacht.
Es kombiniert Fachinhalte, Impulse, Begriffe, Mini-Aufgaben und Reflexion.

## Zielbild

- Schueler unterscheiden KI, ML und Datenkompetenz sicher.
- Schueler koennen einfache Datensaetze lesen, interpretieren und vorbereiten.
- Schueler koennen ein einfaches Regressionsmodell verstehen, nutzen und kritisch bewerten.

## Empfohlener Umfang

- Gesamtumfang: ca. 30 LPE
- Vorschlag: 10 Lernbloecke zu je 3 LPE

## Struktur fuer jede LPE

1. Einstieg (5-10 Min): Leitfrage oder Beispiel aus dem Alltag
2. Erarbeitung (20-25 Min): Begriff, Methode, Demonstration
3. Sicherung (10-15 Min): Mini-Aufgabe + gemeinsamer Check
4. Transfer (5-10 Min): kurze Anwendung auf neuen Kontext

## Schnellstart: Daten-Grundlagen fuer Aufgaben und Tests

Dieser Abschnitt ist eine kompakte Lernhilfe fuer die Aufgaben in `aufgaben/` und die Selbstkontrolle in `tests/`.

### Machine Learning und Artificial Intelligence (KI)

- Artificial Intelligence (Kuenstliche Intelligenz, KI): Oberbegriff fuer Systeme, die Aufgaben mit intelligent wirkendem Verhalten ausfuehren.
- Machine Learning (Maschinelles Lernen, ML): Teilgebiet der KI, bei dem Modelle Muster aus Daten lernen.

Merksatz:
KI ist das Gesamtfeld, ML ist eine wichtige Methode innerhalb der KI.

### Warum Daten zentral sind

Daten sind der Rohstoff von KI und ML. Ohne Daten kann ein Modell nicht lernen, keine Muster erkennen und keine belastbaren Vorhersagen machen.

### Was sind Daten?

Daten sind Informationen in verarbeitbarer Form.

Beispiele:

- Zahlen (z. B. Temperaturen, Preise)
- Texte (z. B. Kommentare, Bewertungen)
- Bilder (z. B. Produktfotos, Roentgenbilder)
- Audio (z. B. Sprache, Geraeusche)

### Arten von Daten

1. Strukturierte Daten
  - klar organisiert, meist tabellarisch
  - Beispiel: Tabelle mit `groesse_m2`, `zimmer`, `baujahr`, `preis_euro`
2. Unstrukturierte Daten
  - keine feste Tabellenstruktur
  - Beispiel: Freitext, Bilder, Videos

### Trainingsdaten und Labels

Viele ML-Verfahren arbeiten mit gelabelten Trainingsdaten:

- Input (Eingabedaten), z. B. Hausgroesse, Zimmerzahl
- Label (Zielwert), z. B. `preis_euro`

Ohne Label kann ein supervised Modell nicht lernen, welcher Zielwert richtig ist.

### Datenqualitaet: was geprueft werden sollte

Gute Daten sind:

- vollstaendig
- korrekt
- moeglichst aktuell
- moeglichst repraesentativ und verzerrungsarm (Bias vermeiden)

Wichtig:
Schlechte Daten fuehren auch bei guten Algorithmen zu schlechten Ergebnissen.

### Datenmenge richtig verstehen

- Zu wenig Daten: hoehere Unsicherheit, instabile Modelle
- Mehr passende Daten: oft bessere Generalisierung

Praxisregel:
Nicht nur die Menge zaehlt, sondern die Kombination aus Menge, Qualitaet und Passung zur Fragestellung.

### Datenschutz und Ethik

Beim Arbeiten mit Daten gelten immer Grundregeln:

- persoenliche Daten schuetzen
- Daten nur zweckgebunden und verantwortungsvoll verwenden
- Verzerrungen erkennen und Diskriminierung vermeiden

### Merksatz fuer den Kurs

Daten sind der Rohstoff der KI: Qualitaet, Menge und Fairness der Daten bestimmen die Qualitaet des Modells.

## Schnellstart: Algorithmische Verfahren fuer A2 und Tests

Dieser Abschnitt ist eine kompakte Lernhilfe fuer den Verfahrensvergleich in A2 und fuer die Selbstkontrolle in den Tests.

### KI und ML kurz einordnen

- Kuenstliche Intelligenz (KI): Oberbegriff fuer Systeme, die Aufgaben mit intelligent wirkendem Verhalten loesen.
- Machine Learning (ML): Teilgebiet der KI, in dem Modelle aus Daten lernen statt nur feste Regeln auszufuehren.

### Was sind algorithmische Verfahren?

Ein Algorithmus ist eine Schritt-fuer-Schritt-Anleitung zur Problemloesung.
Im ML sind algorithmische Verfahren konkrete Lernmethoden, mit denen Muster erkannt und Vorhersagen oder Entscheidungen getroffen werden.

### Wichtige Lernarten und typische Verfahren

1. Supervised Learning (ueberwachtes Lernen)
  - arbeitet mit Eingaben plus bekannten Zielwerten (Labels)
  - Ziel: Vorhersage von Zahlenwerten oder Klassen
  - typische Verfahren im Kurs:
    - lineare Regression (kontinuierliche Werte)
    - Entscheidungsbaum (Klassifikation/Regression)
    - k-NN (Klassifikation)
    - neuronale Netze (je nach Aufbau fuer mehrere Aufgabentypen)

2. Unsupervised Learning (unueberwachtes Lernen)
  - arbeitet ohne vorgegebene Zielwerte
  - Ziel: Strukturen und Gruppen finden
  - typisches Verfahren im Kurs:
    - k-Means (Clustering)

3. Reinforcement Learning (bestaerkendes Lernen)
  - lernt durch Belohnung und Bestrafung in einer Umgebung
  - Ziel: moeglichst gute Strategie entwickeln
  - Beispiel: Spielstrategie lernen

### ML-Ablauf in 5 Schritten

1. Daten sammeln und verstehen
2. Verfahren passend zur Fragestellung waehlen
3. Modell trainieren
4. Modell testen und bewerten
5. Vorhersagen/Entscheidungen reflektieren

### Entscheidungshilfe fuer A2

- Ziel ist ein Zahlenwert (z. B. Preis, Umsatz) -> Regression
- Ziel ist eine Klasse (z. B. ja/nein, Spam/nicht Spam) -> Entscheidungsbaum oder k-NN
- Es gibt keine Labels und du suchst Gruppen -> k-Means

### Merksatz fuer den Kurs

Machine Learning nutzt algorithmische Verfahren, um aus Daten zu lernen und begruendete Vorhersagen oder Entscheidungen zu treffen.

## Schnellstart: Neuronale Netze fuer A4 und Tests

Dieser Abschnitt ist eine kompakte Lernhilfe fuer A4 und fuer die Selbstkontrolle in den Tests.

### Einordnung

- Kuenstliche Intelligenz (KI): Oberbegriff fuer Systeme mit intelligent wirkendem Verhalten.
- Machine Learning (ML): Teilgebiet der KI, bei dem Modelle aus Daten lernen.
- Neuronale Netze: Teilgebiet des ML; sie sind von der Idee biologischer Nervennetze inspiriert, arbeiten aber als mathematische Modelle.

### Aufbau eines einfachen neuronalen Netzes

Ein einfaches neuronales Netz besteht aus mehreren Schichten:

1. Eingabeschicht (Input Layer)
  - nimmt Daten auf, z. B. Pixel eines Bildes
2. Verdeckte Schichten (Hidden Layers)
  - verarbeiten die Eingaben und erkennen Muster
3. Ausgabeschicht (Output Layer)
  - liefert das Ergebnis, z. B. `Katze` oder `kein Hund`

Jedes kuenstliche Neuron:

- erhaelt Eingaben
- gewichtet diese
- berechnet einen neuen Wert
- gibt ein Signal weiter

### Wie lernt ein neuronales Netz?

Vereinfacht laeuft das Training so ab:

1. Eingabedaten werden durch das Netz geschickt.
2. Das Netz erzeugt eine Vorhersage.
3. Die Vorhersage wird mit der richtigen Loesung verglichen.
4. Ein Fehlerwert wird berechnet.
5. Die Gewichte werden angepasst, damit der Fehler kleiner wird.

Wichtig:
Dieses Lernen erfolgt ueber viele Wiederholungen mit Trainingsdaten.

### Einfaches Beispiel

Ein neuronales Netz soll erkennen, ob ein Bild eine Katze zeigt:

- Eingabe: Pixelwerte eines Bildes
- Hidden Layers: erkennen z. B. Kanten, Formen und Kombinationen von Merkmalen
- Ausgabe: `Katze` oder `keine Katze`

Mit vielen passenden Trainingsdaten verbessert sich die Vorhersage oft deutlich.

### Typische Eigenschaften

- erkennt komplexe Muster
- besonders nuetzlich fuer Bilder, Sprache und Texte
- Grundlage vieler moderner KI-Anwendungen, z. B. Sprachassistenten oder Bildanalyse

### Entscheidungshilfe fuer A4

- Geht es um einfache Grundidee und Aufbau? -> Schichten und Gewichte erklaeren
- Geht es um das Lernen? -> Vorhersage, Fehler, Gewichtsanpassung beschreiben
- Geht es um Einordnung? -> Neuronale Netze als Teil von ML und Deep Learning nennen

### Merksatz fuer den Kurs

Neuronale Netze sind lernende Modelle mit verbundenen kuenstlichen Neuronen, die durch Anpassung ihrer Gewichte Muster in Daten erkennen.

## Lernblock 1 (3 LPE): KI im Alltag, Chancen und Grenzen

### Kerninhalte

- Was ist KI?
- Wo begegnet uns KI im Alltag (Navigation, Empfehlungssysteme, Sprachassistenten)?
- Chancen (Unterstuetzung, Automatisierung) und Risiken (Bias, Intransparenz)

### Begriffe

- KI
- Algorithmus
- Automatisierung
- Datenbasis

### Impulse

- Warum ist nicht jedes "smarte" System automatisch KI?
- Welche Entscheidungen sollten Menschen nicht vollstaendig an KI delegieren?

### Mini-Aufgabe

- Sammle 5 Alltagsbeispiele und ordne: KI oder keine KI? Begruende jeweils in 1 Satz.

## Lernblock 2 (3 LPE): Was ist Machine Learning?

### Kerninhalte

- ML als Teilgebiet der KI
- Unterschied: regelbasiertes Programmieren vs. Lernen aus Daten

```
Klassisches Programmieren: Eingabe + Regeln -> Ausgabe
Machine Learning:          Eingabe + Ausgabe -> Regeln (Modell)
```

### Begriffe

- Machine Learning
- Modell
- Training
- Vorhersage

### Mini-Aufgabe

- Formuliere fuer zwei Probleme, ob klassisches Programmieren oder ML sinnvoller ist.

## Lernblock 3 (3 LPE): Lernarten im ML

### Kerninhalte

- Supervised Learning
- Unsupervised Learning
- Reinforcement Learning

### Begriffe

- Label
- Klassifikation
- Regression
- Clustering
- Reward

### Mini-Aufgabe

- Ordne 6 Beispielprobleme einer Lernart zu und erklaere kurz die Wahl.

## Lernblock 4 (3 LPE): Daten verstehen

### Kerninhalte

- Datensatz aufbauen und lesen
- Feature vs. Label
- Datentypen (numerisch, kategorial)

### Begriffe

- Datensatz
- Feature
- Label
- Zielvariable

### Mini-Aufgabe

- Nutze einen einfachen Datensatz und markiere pro Spalte: Feature oder Label, Datentyp, moegliche Probleme.

## Lernblock 5 (3 LPE): Datenqualitaet und Vorbereitung

### Kerninhalte

- Fehlende Werte
- Ausreisser
- Skalierung und einfache Bereinigung

### Begriffe

- Missing Values
- Outlier
- Vorverarbeitung

### Mini-Aufgabe

- Fuehre drei Bereinigungsschritte durch und begruende jeden Schritt in 1-2 Saetzen.

## Lernblock 6 (3 LPE): Lineare Regression verstehen

### Kerninhalte

- Idee der linearen Regression
- Gerade als Modell
- Zusammenhang zwischen Eingabe und Zielwert

### Begriffe

- Lineare Regression
- Koeffizient (Steigung)
- Intercept (Achsenabschnitt)

### Mini-Aufgabe

- Interpretiere Steigung und Intercept in einem konkreten Beispiel (z. B. Wohnflaeche -> Preis).

## Lernblock 7 (3 LPE): Modell trainieren

### Kerninhalte

- Trainings- und Testdaten
- Einfacher Trainingsablauf in Python/Notebook

### Begriffe

- Train-Test-Split
- Fit
- Predict

### Mini-Aufgabe

- Trainiere ein einfaches Modell und dokumentiere die Schritte als Lernprotokoll.

## Lernblock 8 (3 LPE): Modell bewerten

### Kerninhalte

- Fehlermae (einfach erklaert)
- Aussagekraft einer Vorhersage
- Plausibilitaetscheck

### Begriffe

- MAE
- MSE
- R2
- Residuum

### Mini-Aufgabe

- Vergleiche zwei Modelle mit denselben Daten und entscheide, welches sinnvoller ist.

## Lernblock 9 (3 LPE): Fehleranalyse und Modellgrenzen

### Kerninhalte

- Overfitting und Underfitting
- Generalisierung
- Datenverzerrung (Bias)

### Begriffe

- Overfitting
- Underfitting
- Generalisierung
- Bias

### Mini-Aufgabe

- Erklaere zu drei Fehlerszenarien die wahrscheinliche Ursache und eine Verbesserungsidee.

## Lernblock 10 (3 LPE): Transferprojekt und Reflexion

### Kerninhalte

- Kleine Projektfrage entwickeln
- Daten nutzen, Modell bauen, Ergebnis reflektieren
- Grenzen und Verantwortung benennen

### Begriffe

- Modellkritik
- Transparenz
- Verantwortung

### Mini-Aufgabe

- Teamprojekt mit Kurzpraesentation (Problem, Vorgehen, Ergebnis, Grenzen, naechster Schritt).

## Glossar der wichtigsten Begriffe

| Begriff | Kurzdefinition |
|---|---|
| KI | Systeme, die Aufgaben mit intelligent wirkendem Verhalten ausfuehren |
| ML | Teilgebiet der KI, bei dem Systeme aus Daten lernen |
| Datensatz | Strukturierte Sammlung von Beobachtungen |
| Feature | Eingabemerkmal zur Vorhersage |
| Label | Zielwert, der vorhergesagt werden soll |
| Modell | Mathematische Abbildung von Eingaben auf Ausgaben |
| Training | Lernphase des Modells |
| Test | Pruefung mit unbekannten Daten |
| Vorhersage | Ergebnis des Modells fuer neue Eingaben |
| Regression | Vorhersage kontinuierlicher Werte |
| Klassifikation | Zuordnung zu Klassen |
| Clustering | Gruppierung ohne vorgegebene Labels |
| Overfitting | Modell passt Trainingsdaten zu stark an |
| Underfitting | Modell ist zu einfach und lernt zu wenig |
| Bias | Systematische Verzerrung in Daten oder Modell |

## Didaktische Hinweise fuer Lehrkraefte

- Arbeite mit gestuften Hilfen:
  - Hilfe 1: Impulsfrage
  - Hilfe 2: Strategiehinweis
  - Hilfe 3: Fachhinweis
- Lass Schueler zuerst Hypothesen formulieren, dann rechnen/coden.
- Nutze Fehler als Lernanlass ("Was sagt uns der Fehler?").
- Halte Fachsprache sichtbar (Tafel/Glossarwand).

## Erwartungshorizont (kompakt)

- Basisniveau:
  - KI/ML begrifflich unterscheiden
  - einfache Datensaetze lesen
  - lineare Regression in Grundidee erklaeren
- Mittleres Niveau:
  - Modell auf einfachem Datensatz anwenden
  - Ergebnisse mit Fehlerwerten deuten
  - Grenzen des Modells benennen
- Erweitertes Niveau:
  - Verbesserungsmassnahmen begruenden
  - Datenqualitaet kritisch reflektieren
  - Transfer auf neue Fragestellungen leisten

## Pruef- und Aufgabenideen fuer den Kurs

1. Begriffstest mit Begruendung (KI/ML/Feature/Label)
2. Datensatzanalyse mit 5 Leitfragen
3. Guided Coding zur linearen Regression
4. Ergebnisinterpretation mit Fehleranalyse
5. Mini-Projekt mit Reflexionsbericht

## Verbindung zum Repository

- Lernhorizont: ../../informationen/lehrplan/lernhorizont.md
- Marschplan KI/ML: ../../informationen/lehrplan/marschplan-ki-ml.md
- Aufgaben: ../../aufgaben/
- Notebooks: ../../notebooks/
- Tests: ../../tests/
