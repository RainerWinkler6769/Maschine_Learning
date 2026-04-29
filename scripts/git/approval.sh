#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Nutzung:
  scripts/git/approval.sh grant <commit|push> [gueltigkeit_minuten]
  scripts/git/approval.sh validate <commit|push>

Beispiele:
  scripts/git/approval.sh grant commit 20
  scripts/git/approval.sh grant push 10
EOF
}

if [[ "${1:-}" == "" ]] || [[ "${2:-}" == "" ]]; then
  usage
  exit 1
fi

command="$1"
action="$2"
valid_minutes="${3:-15}"

if [[ "$action" != "commit" && "$action" != "push" ]]; then
  echo "Ungueltige Aktion: $action" >&2
  usage
  exit 1
fi

repo_root="$(git rev-parse --show-toplevel)"
git_dir="$(git rev-parse --git-dir)"
marker_file="$git_dir/.approval_${action}.token"

current_epoch="$(date +%s)"

case "$command" in
  grant)
    if ! [[ "$valid_minutes" =~ ^[0-9]+$ ]]; then
      echo "gueltigkeit_minuten muss eine Zahl sein." >&2
      exit 1
    fi

    expires_at="$((current_epoch + valid_minutes * 60))"
    approver="$(git config user.name || true)"
    approver="${approver:-unknown}"
    approver_b64="$(printf '%s' "$approver" | base64 -w0)"

    {
      echo "approver_b64=$approver_b64"
      echo "action=$action"
      echo "issued_at=$current_epoch"
      echo "expires_at=$expires_at"
      echo "repo_root=$repo_root"
    } > "$marker_file"

    chmod 600 "$marker_file"
    echo "Freigabe fuer '$action' bis $(date -d "@$expires_at" '+%Y-%m-%d %H:%M:%S') gesetzt."
    ;;
  validate)
    if [[ ! -f "$marker_file" ]]; then
      echo "Freigabe fuer '$action' fehlt."
      echo "Bitte zuerst ausfuehren: scripts/git/approval.sh grant $action 15"
      exit 1
    fi

    expires_at="$(grep '^expires_at=' "$marker_file" | head -n1 | cut -d= -f2-)"
    approver_b64="$(grep '^approver_b64=' "$marker_file" | head -n1 | cut -d= -f2-)"
    approver="$(printf '%s' "$approver_b64" | base64 -d 2>/dev/null || printf 'unknown')"

    if [[ -z "${expires_at:-}" ]] || [[ "$expires_at" -lt "$current_epoch" ]]; then
      rm -f "$marker_file"
      echo "Freigabe fuer '$action' ist abgelaufen. Bitte neu freigeben."
      exit 1
    fi

    # One-time approval token: after one successful operation a new approval is required.
    rm -f "$marker_file"
    echo "Freigabe fuer '$action' geprueft (${approver:-unknown})."
    ;;
  *)
    usage
    exit 1
    ;;
esac
