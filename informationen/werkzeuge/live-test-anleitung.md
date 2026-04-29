# Live testbare Anwendung mit Docker (Hallo Welt)

Diese Anleitung richtet im Haupt-Repository eine vollständig testbare Mehrsprachen-Demo ein (Java, MySQL, Python, PHP, JavaScript).

## 1. Voraussetzungen

- Docker mit Compose-Unterstützung
- Git
- Freie Ports: 3306, 8000, 8080, 8081, 8082

## 2. Projekt vorbereiten

```bash
cd /workspaces/edu-code-course-ml
cp .env.example .env
```

Wichtig: Ersetze in `.env` alle `CHANGE_ME`-Werte durch sichere Passwoerter (mindestens 16 Zeichen).

## 3. Services starten

```bash
docker compose up -d --build
```

## 4. Live-Checks im Browser und per API

- PHP: http://localhost:8080
- JavaScript-Web: http://localhost:8081
- Python: http://localhost:8000/
- Python-Health: http://localhost:8000/health
- Java: http://localhost:8082/

## 5. Automatischen Live-Test ausführen

```bash
chmod +x tests/live/test_live_stack.sh
./tests/live/test_live_stack.sh
```

Erwartung: `Alle Live-Checks erfolgreich`.

## 6. Security-Smoke-Test ausfuehren

```bash
chmod +x tests/live/security_smoke.sh
./tests/live/security_smoke.sh
```

Erwartung: `Security-Smoke-Checks erfolgreich`.

## 7. Datenbank pruefen (MySQL)

```bash
docker compose exec -T mysql \
  mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" "$MYSQL_DATABASE" \
  -e "SELECT * FROM hello_log;"
```

Es sollte mindestens ein Eintrag mit `Hallo Welt aus MySQL` vorhanden sein.

## 8. Services stoppen

```bash
docker compose down
```

Optional inkl. Volumes:

```bash
docker compose down -v
```
