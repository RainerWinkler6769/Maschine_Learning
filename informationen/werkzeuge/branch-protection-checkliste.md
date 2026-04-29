# Branch-Protection-Checkliste (main)

Diese Checkliste stellt sicher, dass das E-Learning-Repo langfristig sicher und wartbar wachsen kann.

## 1. Branch-Regeln fuer main

- `Require a pull request before merging`: aktiv
- `Require approvals`: mindestens 1 (empfohlen: 2)
- `Dismiss stale approvals when new commits are pushed`: aktiv
- `Require conversation resolution before merging`: aktiv
- `Require linear history`: aktiv
- `Do not allow bypassing the above settings`: aktiv

## 2. Pflicht-Statuschecks

Diese Workflows muessen als required checks eingetragen werden:

- `Live Stack CI / live-stack-test`
- `Security Scans / filesystem-scan`
- `Security Scans / dependency-scan-python`
- `Security Scans / image-scan`

## 3. Merge-Strategie

- Empfohlen: `Squash merge`
- Auto-merge nur bei gruenen required checks
- Direktes Pushen auf `main` verbieten

## 4. Secret- und Credential-Regeln

- Niemals `.env` committen
- Ausschliesslich `CHANGE_ME`-Platzhalter in `.env.example`
- Secrets nur als GitHub Repository/Environment Secrets pflegen
- Rotation von DB/API-Credentials mindestens quartalsweise

## 5. Release- und Betriebsregeln

- Jeder Release-PR enthaelt:
  - Risikoabschaetzung
  - Rollback-Plan
  - Testnachweis (funktional + Security)
- Kritische Security-Fixes priorisiert innerhalb von 24h triagieren

## 6. Monitoring der Sicherheitslage

- Security-Workflow bei jedem PR und Push auf `main` erzwingen
- Dependabot-Alerts regelmaessig pruefen
- High/Critical Findings vor Merge beheben oder dokumentiert akzeptieren

## 7. Rollen und Verantwortlichkeiten

- Mindestens 2 Maintainer mit Admin-Rechten
- CODEOWNERS fuer kritische Bereiche definieren:
  - `.github/workflows/`
  - `docker-compose.yml`
  - `src/`
  - `tests/live/`

## 8. Quartals-Review

Einmal pro Quartal pruefen:

- Sind required checks noch passend?
- Sind Abhaengigkeiten/Images aktuell?
- Sind Branch-Regeln unveraendert aktiv?
- Gibt es wiederkehrende Security-Befunde?

## 9. Freigabe- und Backup-Routine (verbindlich)

- Lokale Hook-Freigabe aktivieren: `scripts/git/install-hooks.sh`
- Vor jedem Commit: `scripts/git/approval.sh grant commit 15`
- Vor jedem Push: `scripts/git/approval.sh grant push 15`
- Automatische Milestone-Backups aktiv ueberwachen: `.github/workflows/milestone-backup.yml`
- Prozessdokumentation: `informationen/werkzeuge/git-freigabe-backupstrategie.md`
