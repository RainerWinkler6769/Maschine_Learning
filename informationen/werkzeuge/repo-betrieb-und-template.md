# Repo-Betrieb und Template-Verwaltung

Zielgruppe:
- Lehrkraefte mit Administrationsaufgaben
- Entwicklerinnen und Entwickler
- Personen, die das Repository technisch pflegen

Diese Datei enthaelt technische und organisatorische Hinweise, die bewusst aus der Haupt-README ausgelagert wurden.

## Technische Projektstruktur

```text
edu-code-course-ml/
├── src/                         # Live-Demo-Services (Java, Python, PHP, JS, MySQL-Init)
├── docker-compose.yml           # Startet die Root-Live-Umgebung
├── template/                    # Git-Submodule: edu-code-projecttemplate
├── informationen/               # Hilfen, Grundlagen, Werkzeuge, Lehrplan
├── aufgaben/                    # Aufgaben fuer Lernende
├── loesungen/                   # Musterloesungen
├── notebooks/                   # Jupyter-Notebooks
├── tests/                       # Automatisierte Tests
└── README.md                    # Lernpfad fuer Schueler und Lehrkraefte
```

## Root-Live-Umgebung technisch betreiben

Fuer die komplette technische Inbetriebnahme nutze primaer:
- [E-Learning testen](elearning-testen.md)
- [Live testbare Anwendung mit Docker](live-test-anleitung.md)

Kurzablauf:

```bash
cp .env.example .env
# CHANGE_ME-Werte ersetzen
docker compose up -d --build
chmod +x tests/live/test_live_stack.sh
./tests/live/test_live_stack.sh
chmod +x tests/live/security_smoke.sh
./tests/live/security_smoke.sh
```

Wichtige Standard-URLs:
- PHP: http://localhost:8080
- JavaScript-Web: http://localhost:8081
- Python-API: http://localhost:8000/health
- Java-App: http://localhost:8082

## Template-Submodule verwalten

Das Verzeichnis `template/` bindet das Repository `edu-code-projecttemplate` als Git-Submodule ein.

### Submodule initialisieren

```bash
git clone --recurse-submodules https://github.com/ChristineJanischek/edu-code-course-ml.git
# oder nachtraeglich:
git submodule update --init --recursive
```

### Template-Umgebung verwenden

```bash
cd template
bash scripts/bootstrap.sh
bash scripts/start-services.sh
```

### Template aktualisieren

```bash
git submodule update --remote template
git add template
git commit -m "chore: template aktualisiert"
git push
```

Hinweis:
Das Submodule zeigt immer auf einen konkreten Commit. Vor einem Update auf Breaking Changes achten.

## Wichtige Template-Skripte

| Skript | Zweck |
|---|---|
| `scripts/bootstrap.sh` | `.env` erzeugen und Grundkonfiguration vorbereiten |
| `scripts/start-services.sh` | Docker-Dienste starten |
| `scripts/stop-services.sh` | Docker-Dienste stoppen |
| `scripts/test-services.sh` | technische Service-Checks ausfuehren |
| `scripts/validate-docs.sh` | Dokumentationspflicht pruefen |
| `scripts/validate-architecture.sh` | Java-Architekturregeln pruefen |
| `scripts/validate-security.sh` | Sicherheits-Basischecks ausfuehren |

## Pflege- und Freigabedokumente

- [Branch-Protection-Checkliste](branch-protection-checkliste.md)
- [Git-Freigabe und Backupstrategie](git-freigabe-backupstrategie.md)

## Empfehlung fuer den Alltagsbetrieb

1. Fuer Unterricht und Selbstlernen zuerst immer die Haupt-README verwenden.
2. Fuer technische Einrichtung die Datei [E-Learning testen](elearning-testen.md) verwenden.
3. Fuer Repo-Pflege, Template-Updates und Freigaben diese Datei und die verlinkten Admin-Dokumente nutzen.
