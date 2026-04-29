# E-Learning testen – Schritt-für-Schritt-Anleitung

Diese Anleitung richtet sich an **Schüler und Lehrer**, die das E-Learning-Environment vollständig einrichten, starten und testen möchten. Sie deckt alle Bereiche ab: Docker-Services, ML-Notebooks und automatische Kurztests.

---

## Übersicht

| Phase | Was wird getestet | Aufwand |
|-------|-------------------|---------|
| 1. Vorbereitung | System-Voraussetzungen prüfen | ~5 Min. |
| 2. Repository einrichten | Repo klonen, Umgebung konfigurieren | ~5 Min. |
| 3. Docker-Services starten | Alle Services hochfahren | ~5 Min. |
| 4. Services live prüfen | Browser-Checks & API-Tests | ~5 Min. |
| 5. Automatische Tests | Live-Test & Security-Smoke-Test | ~2 Min. |
| 6. ML-Inhalte testen | Jupyter Notebooks öffnen & ausführen | ~10 Min. |
| 7. Aufgaben & Tests prüfen | Schüler-Tests (pytest) ausführen | ~3 Min. |
| 8. Aufräumen | Services stoppen | ~1 Min. |

Lehrkraft-Kurzreferenz (BPE 6/7): [lehrkraft-test-kurzreferenz.md](lehrkraft-test-kurzreferenz.md)

---

## Phase 1 – Voraussetzungen prüfen

Stelle sicher, dass folgende Werkzeuge installiert und verfügbar sind:

```bash
# Alle vier Befehle müssen eine Versionsnummer ausgeben
docker --version        # Docker ≥ 24
docker compose version  # Compose v2 (kein eigenständiges docker-compose nötig)
git --version           # Git ≥ 2
python3 --version       # Python ≥ 3.9 (für Notebooks & Tests)
jupyter --version       # Jupyter Notebook oder JupyterLab
```

Freie Ports, die benötigt werden:

| Port | Service |
|------|---------|
| 3306 | MySQL |
| 8000 | Python-API |
| 8080 | PHP-Web |
| 8081 | JavaScript-Web |
| 8082 | Java-App |
| 8888 | Jupyter Notebook |

> Sind Ports bereits belegt, können sie in der `.env`-Datei (nächste Phase) angepasst werden.

---

## Phase 2 – Repository einrichten

### 2.1 Repo klonen

```bash
git clone --recurse-submodules https://github.com/ChristineJanischek/edu-code-course-ml.git
cd edu-code-course-ml
```

> Ist das Repo bereits vorhanden, reicht:
> ```bash
> cd edu-code-course-ml
> git pull
> git submodule update --init --recursive
> ```

### 2.1.1 Wiedereinstieg nach Unterbrechung (naechster Tag / anderer Rechner)

So vermeidest du eine doppelte Ordnerstruktur wie `edu-code-course-ml/edu-code-course-ml`:

```bash
# 1) Pruefen, wo du gerade bist
pwd

# 2) Pruefen, ob du bereits in einem Git-Repo bist
git rev-parse --show-toplevel
```

Interpretation:
- Wenn `git rev-parse` einen Pfad ausgibt, bist du schon im Repo oder in einem Unterordner davon: **nicht erneut klonen**, sondern nur aktualisieren (`git pull`).
- Wenn eine Fehlermeldung erscheint (kein Git-Repo), erst dann in den Elternordner wechseln und klonen.

Sicherer Wiedereinstieg im bestehenden Repo:

```bash
cd /workspaces/edu-code-course-ml
git pull
git submodule update --init --recursive
```

### 2.2 Umgebungsvariablen setzen

```bash
cp .env.example .env
```

Öffne `.env` und ersetze **alle** `CHANGE_ME`-Werte durch sichere Passwörter (mindestens 16 Zeichen):

```dotenv
MYSQL_ROOT_PASSWORD=MeinSicheresRootPW2024!
MYSQL_DATABASE=edu_demo
MYSQL_USER=edu_user
MYSQL_PASSWORD=MeinSicheresUserPW2024!
```

> **Sicherheitshinweis:** Die Datei `.env` ist über `.gitignore` vom Commit ausgeschlossen. Niemals echte Passwörter ins Repository einchecken!

---

## Phase 3 – Docker-Services starten

```bash
docker compose up -d --build
```

Der erste Start kann **2–5 Minuten** dauern, da alle Container-Images gebaut werden. Warte, bis alle Services als `healthy` angezeigt werden:

```bash
docker compose ps
```

Erwartete Ausgabe (Auszug):

```
NAME                  STATUS
edu_ml_mysql          running (healthy)
edu_ml_python_api     running (healthy)
edu_ml_php_web        running
edu_ml_js_web         running
edu_ml_java_app       running
```

---

## Phase 4 – Services live im Browser prüfen

Öffne folgende URLs im Browser und überprüfe, ob die Seite lädt und **„Hallo Welt"** angezeigt wird:

| Service | URL | Erwartete Antwort |
|---------|-----|-------------------|
| Python-API Health | http://localhost:8000/health | `{"status": "ok"}` |
| Python-API Root | http://localhost:8000/ | Hallo Welt aus Python |
| PHP-Web | http://localhost:8080 | Hallo Welt aus PHP |
| JavaScript-Web | http://localhost:8081 | Hallo Welt aus JavaScript |
| Java-App | http://localhost:8082 | Hallo Welt aus Java |

**MySQL-Datenbank prüfen:**

Wichtig: Lade zuerst die Werte aus `.env` in die aktuelle Shell. Sonst greifen Fallback-Werte (z. B. `edu_pass`), die oft **nicht** zum laufenden Container passen.

```bash
set -a
source .env
set +a
```

```bash
docker compose exec -T mysql \
  mysql -u"${MYSQL_USER}" -p"${MYSQL_PASSWORD}" "${MYSQL_DATABASE}" \
  -e "SELECT * FROM hello_log LIMIT 5;"
```

Es sollte mindestens ein Eintrag mit `Hallo Welt aus MySQL` erscheinen.

Bei `ERROR 1045 (28000): Access denied`:
- Prüfe, ob `.env` wirklich geladen wurde: `echo "$MYSQL_USER / $MYSQL_DATABASE"`
- Falls `.env` nach dem ersten Start geändert wurde: `docker compose down -v && docker compose up -d --build`
- Hinweis: `down -v` löscht lokale Datenbankdaten (im Unterricht meist unkritisch)

---

## Phase 5 – Automatische Tests ausführen

### 5.1 Live-Stack-Test

Prüft alle Services und die Datenbank automatisch per Skript:

```bash
chmod +x tests/live/test_live_stack.sh
./tests/live/test_live_stack.sh
```

**Erwartete Ausgabe:**
```
[live-test] Alle Live-Checks erfolgreich
```

### 5.2 Security-Smoke-Test

Prüft Sicherheits-Basisanforderungen (`.gitignore`, `.env`, Security-Header):

```bash
chmod +x tests/live/security_smoke.sh
./tests/live/security_smoke.sh
```

**Erwartete Ausgabe:**
```
[security] Security-Smoke-Checks erfolgreich
```

> Erscheint eine Fehlermeldung, lies die Ausgabe genau – sie zeigt an, was angepasst werden muss (z. B. noch vorhandene `CHANGE_ME`-Werte in `.env`).

---

## Phase 6 – ML-Inhalte mit Jupyter Notebooks testen

### 6.1 Jupyter starten

```bash
jupyter notebook
```

Der Browser öffnet sich automatisch unter `http://localhost:8888`.  
Falls nicht, klicke auf den Link in der Terminal-Ausgabe (enthält einen Token).

### 6.2 Notebooks ausführen

Navigiere im Browser zum Ordner `notebooks/` und öffne die Notebooks der Reihe nach:

| Datei | Inhalt | Voraussetzung |
|-------|--------|---------------|
| `00_projektstruktur_analyse.ipynb` | Überblick über das Repo | keine |
| `01_einfuehrung.ipynb` | Python-Einstieg und KI/ML-Basis | keine |
| `02_daten_erkunden.ipynb` | Datenanalyse und Visualisierung | Grundlagen gelesen |
| `03_lineare_regression.ipynb` | Lineare Regression | Datenanalyse abgeschlossen |
| `04_ki_tools_bwl.ipynb` | KI-Transfer auf BWL-Anwendungsfall | Regression und Verfahrenvergleich |

**Alle Zellen eines Notebooks ausführen:**
- Menü: `Kernel` → `Restart & Run All`
- Oder Tastenkürzel: `Strg + Shift + F9` (JupyterLab)

**Erwartung:** Alle Zellen werden ohne Fehler durchgeführt, Ausgaben und Diagramme erscheinen.

### 6.3 Daten prüfen

Die Beispiel-CSV-Datei für die Regressionsaufgabe liegt unter:

```
notebooks/daten/haeuser.csv
```

Überprüfe, ob die Datei lesbar ist:

```bash
head -5 notebooks/daten/haeuser.csv
```

---

## Phase 7 – Schüler-Tests mit pytest ausführen

Automatische Tests prüfen, ob die Aufgabenlösungen korrekt sind:

```bash
# Alle Tests ausführen
python3 -m pytest tests/ -v

# Nur Tests fuer Grundlagen
python3 -m pytest tests/01_grundlagen/ -v

# Verfahrenvergleich
python3 -m pytest tests/03_regression/ -v

# Vertiefung, Transfer und BPE-Mapping
python3 -m pytest tests/04_fortgeschritten/ -v
```

**Erwartete Ausgabe (Beispiel):**
```
tests/01_grundlagen/test_aufgabe_01.py::test_daten_geladen PASSED
...
1 passed in 0.42s
```

> Falls Pakete fehlen:
> ```bash
> pip install pytest pandas numpy matplotlib scikit-learn
> ```

---

## Phase 8 – Services stoppen

Nach dem Testen die Docker-Services geordnet stoppen:

```bash
# Services stoppen (Daten bleiben erhalten)
docker compose down

# Services stoppen UND alle Daten löschen (Volumes)
docker compose down -v
```

---

## Schnellreferenz – Alle Befehle auf einen Blick

```bash
# 1. Setup
cp .env.example .env && nano .env   # CHANGE_ME ersetzen

# 2. Starten
docker compose up -d --build

# 3. Status prüfen
docker compose ps

# 4. Automatische Tests
./tests/live/test_live_stack.sh
./tests/live/security_smoke.sh

# 5. ML-Notebooks
jupyter notebook

# 6. Schüler-Tests
python3 -m pytest tests/ -v

# 7. Stoppen
docker compose down
```

---

## Häufige Probleme & Lösungen

| Problem | Ursache | Lösung |
|---------|---------|--------|
| `CHANGE_ME must be set` | `.env` nicht angepasst | Alle `CHANGE_ME` in `.env` durch echte Werte ersetzen |
| `ERROR 1045 (28000): Access denied` bei MySQL-Check | Shell nutzt nicht die `.env`-Werte oder DB wurde mit alten Werten initialisiert | `set -a; source .env; set +a` und ggf. `docker compose down -v && docker compose up -d --build` |
| Port bereits belegt | Anderer Prozess nutzt den Port | Port in `.env` ändern (z. B. `PHP_WEB_PORT=8090`) |
| `health: starting` nach 2 Min. | Container startet langsam | `docker compose logs mysql` prüfen |
| Notebook-Kernel startet nicht | Jupyter nicht installiert | `pip install notebook` |
| `pytest: command not found` | pytest fehlt | `pip install pytest` |
| `curl: Connection refused` | Service nicht gestartet | `docker compose ps` und `docker compose logs` prüfen |

---

## Weiterführende Informationen

- [Live-Test-Anleitung (Docker-Stack)](live-test-anleitung.md)
- [Jupyter-Anleitung](jupyter.md)
- [Lernhorizont & Lehrplan](../lehrplan/lernhorizont.md)
- [Aufgaben](../../aufgaben/README.md)
- [Tests](../../tests/README.md)
- [Hauptdokumentation (README.md)](../../README.md)
