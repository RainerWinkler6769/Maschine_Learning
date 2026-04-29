# Git-Freigabe und Backupstrategie

Dieses Dokument definiert verbindliche Routinen fuer Commit-/Push-Freigaben und automatische Backups an Meilensteinen.

## 1. Ziel

- Jeder Commit und jeder Push muss vorher aktiv freigegeben werden.
- Das Repository erzeugt zu wichtigen Meilensteinen automatisch wiederherstellbare Backups.
- Die Qualitaetsprinzipien Erweiterbarkeit, Wartbarkeit, Sicherheit, Dokumentation, Versionsmanagement, Wiederverwendbarkeit und Redundanzvermeidung werden systematisch geprueft.

## 2. Verbindliche Freigabe vor Commit/Push (lokal)

### Einmalig aktivieren

```bash
chmod +x scripts/git/install-hooks.sh
scripts/git/install-hooks.sh
```

### Commit freigeben

```bash
scripts/git/approval.sh grant commit 15
git commit -m "<nachvollziehbare message>"
```

### Push freigeben

```bash
scripts/git/approval.sh grant push 15
git push
```

Hinweise:
- Die Freigabe ist ein One-Time-Token und wird nach erfolgreichem Commit/Push entfernt.
- Ohne gueltige Freigabe blockieren `pre-commit` und `pre-push` den Vorgang.

## 3. Verbindliche Freigabe auf GitHub

Fuer `main` gelten folgende Regeln:

- Pull Request Pflicht
- Mindestens 1 Approval (empfohlen 2)
- Code-Owner-Review fuer kritische Pfade
- Keine direkten Pushes auf `main`
- Required Status Checks muessen gruen sein

Konfiguration siehe:
- `informationen/werkzeuge/branch-protection-checkliste.md`
- `.github/CODEOWNERS`

## 4. Automatische Backupstrategie

Workflow:
- `.github/workflows/milestone-backup.yml`

Ausloeser:
- Push auf `main`
- Push von Tags `v*` und `milestone-*`
- Woechentlich geplanter Lauf (Montag 03:00 UTC)
- Manuell ueber `workflow_dispatch`

Ergebnis:
- Git-Bundle als vollstaendige Repo-Sicherung
- SHA256-Pruefsumme
- Manifest mit Commit-/Branch-Information
- Artefaktablage in `backups/milestones/*.tar.gz`

Lokaler Testlauf:

```bash
chmod +x scripts/git/create-milestone-backup.sh
scripts/git/create-milestone-backup.sh "milestone-lokal"
```

## 5. Qualitaetsroutinen (Best Practice)

Vor jedem Merge nach `main`:

- Architektur und Verantwortlichkeiten klein und modular halten.
- Sicherheitspruefungen (CI + Secrets hygiene) durchfuehren.
- Dokumentationsaenderungen zusammen mit Code aendern.
- Wiederverwendbare Komponenten vor Duplikaten bevorzugen.
- Versionsmanagement strikt ueber PRs, Reviews und nachvollziehbare Commit-Messages.

Quartalsweise Review:

- Branch-Protection und CODEOWNERS gegen Ist-Zustand pruefen.
- Backup-Wiederherstellung testweise validieren.
- CI-Checks auf neue Risiken und Optimierungspotenziale pruefen.
