# Promptverlauf und Grundlagenskript KI/ML

Zweck dieses Dokuments:
- Vollstaendige Ablage des bisherigen Promptverlaufs aus der Session
- Dauerhafte Sicherung theoretischer Grundlagen im System
- Automatische Verdichtung zu einem kompakten Grundlagenskript

Stand: 2026-04-15

## Teil A: Vollstaendiger Promptverlauf (Session-Auszug)

1. Prompt: Lade den Datensatz ../notebooks/daten/haeuser.csv mit Pandas und zeige die ersten 5 Zeilen an.
Antwort: Datensatz wurde aus notebooks/daten/haeuser.csv geladen und die ersten 5 Zeilen wurden ausgegeben (Spalten: groesse_m2, zimmer, baujahr, preis_euro).

2. Prompt: Was ist KI?
Antwort: KI = Systeme, die Aufgaben loesen, die sonst menschliche Intelligenz erfordern; Fokus auf Mustererkennung aus Daten.

3. Prompt: Algorithmus
Antwort: Eindeutige Schritt-fuer-Schritt-Anleitung zur Problemloesung; endlich, eindeutig, ausfuehrbar, allgemein.

4. Prompt: Warum ist nicht jedes "smarte" System automatisch KI?
Antwort: Smart kann rein regelbasiert sein; KI lernt datenbasiert Muster und generalisiert auf neue Faelle.

5. Prompt: Machine Learning
Antwort: Teilgebiet der KI; Modelle lernen aus Beispieldaten und treffen Vorhersagen fuer neue Daten.

6. Prompt: Formuliere fuer zwei Probleme, ob klassisches Programmieren oder ML sinnvoller ist.
Antwort:
- Versandkosten mit festen Regeln -> klassisches Programmieren
- Spam-Erkennung mit veraenderlichen Mustern -> ML

7. Prompt: Was ist ein Modell
Antwort: Vereinfachte Abbildung der Realitaet; im ML die gelernte Funktion fuer Vorhersagen.

8. Prompt: Supervised Learning
Antwort: Lernen mit Labels (Eingabe + richtige Zielausgabe), um auf neue Eingaben zu generalisieren.

9. Prompt: Unsupervised Learning
Antwort: Lernen ohne Labels; Finden von Strukturen, Gruppen und Auffaelligkeiten in Daten.

10. Prompt: Reinforcement Learning
Antwort: Agent lernt durch Aktionen, Reward/Strafe und Optimierung langfristiger Belohnung.

11. Prompt: Label
Antwort: Richtige Zielantwort zu einem Datenbeispiel im Supervised Learning.

12. Prompt: Klassifikation
Antwort: Vorhersage diskreter Klassen (z. B. Spam vs. Nicht-Spam).

13. Prompt: Regression
Antwort: Vorhersage kontinuierlicher numerischer Werte (z. B. Preis, Umsatz, Temperatur).

14. Prompt: Clustering
Antwort: Unsupervised-Verfahren zur Gruppierung aehnlicher Datenpunkte.

15. Prompt: Reward
Antwort: Numerisches Feedback-Signal (positiv/negativ) im Reinforcement Learning.

16. Prompt: Schreibe den gesammten promtverlauf in ein skript (.md Datei). Ich moechte damit sicherstellen dass alle Theoretischen Grundlagen im System hinterlegt sind und ggf. auch automatisch oder angeleitet zu einem GRundlagenskript zusammengefasst werden . danke
Antwort: Dieses Dokument wurde erstellt und als dauerhafte Grundlage verlinkt.

## Teil B: Automatisch verdichtetes Grundlagenskript

### 1) KI, ML und klassisches Programmieren

KI beschreibt Systeme, die komplexe Aufgaben bearbeiten, die sonst menschliche Intelligenz erfordern.
ML ist ein Teilgebiet der KI: Das System lernt Muster aus Daten statt nur feste Regeln auszufuehren.
Klassisches Programmieren ist sinnvoll, wenn Regeln stabil, klar und vollstaendig formulierbar sind.

Faustregel:
- Klare, feste, rechtssichere Regeln -> klassisches Programmieren
- Komplexe Muster mit vielen Beispielen -> ML

### 2) Grundbegriffe

- Algorithmus: Eindeutige Schrittfolge zur Problemloesung
- Modell: Gelernte Funktion zur Vorhersage auf neuen Daten
- Label: Richtige Zielantwort bei gelabelten Trainingsdaten
- Reward: Bewertungs-/Belohnungssignal im Reinforcement Learning

### 3) Lernarten im ML

- Supervised Learning: Lernen mit Labels
- Unsupervised Learning: Lernen ohne Labels
- Reinforcement Learning: Lernen durch Interaktion und Reward

### 4) Typische Aufgabenarten

- Klassifikation: Vorhersage von Klassen/Kategorien
- Regression: Vorhersage kontinuierlicher Zahlenwerte
- Clustering: Automatische Gruppierung aehnlicher Datenpunkte

### 5) Mini-Entscheidungshilfe fuer Unterricht und Praxis

1. Ist das Ziel eine Kategorie? -> Klassifikation
2. Ist das Ziel ein Zahlenwert? -> Regression
3. Gibt es keine Labels und ich suche Gruppen? -> Clustering
4. Lernt ein Agent durch Belohnung/Strafe in Sequenzen? -> Reinforcement Learning
5. Sind alle Regeln klar formulierbar? -> eher klassisches Programmieren

### 6) Kurzbeispiele

1. Versandkosten nach festen Tarifen -> klassisches Programmieren
2. Spam-Erkennung in E-Mails -> Klassifikation (Supervised Learning)
3. Hauspreis schaetzen -> Regression (Supervised Learning)
4. Kundensegmente bilden -> Clustering (Unsupervised Learning)
5. Spielstrategie optimieren -> Reinforcement Learning

## Teil C: Nutzung als langlebiges Grundlagenskript

Empfohlene Nutzung:
1. Als Glossar fuer schnellen Begriffsabgleich
2. Als Einstieg vor Aufgaben in aufgaben/
3. Als Wiederholung vor Leistungsnachweisen

Pflegehinweis:
- Neue Theoriebegriffe koennen fortlaufend in Teil A (Promptverlauf) und Teil B (Verdichtung) ergaenzt werden.
- Damit bleibt eine nachvollziehbare Historie plus ein kompaktes Lernskript erhalten.
