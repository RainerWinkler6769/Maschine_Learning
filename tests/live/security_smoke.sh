#!/usr/bin/env bash
set -euo pipefail

root_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$root_dir"

if [[ -f .env ]]; then
  set -a
  # shellcheck disable=SC1091
  . ./.env
  set +a
fi

if [[ ! -f .gitignore ]]; then
  echo "[security] Fehler: .gitignore fehlt"
  exit 1
fi

if ! grep -qx ".env" .gitignore; then
  echo "[security] Fehler: .env ist nicht in .gitignore eingetragen"
  exit 1
fi

if [[ ! -f .env ]]; then
  echo "[security] Fehler: .env fehlt"
  exit 1
fi

if grep -q "CHANGE_ME" .env; then
  echo "[security] Fehler: .env enthaelt noch CHANGE_ME-Werte"
  exit 1
fi

# Security Header Check auf JS-Web (Nginx)
js_port="${JS_WEB_PORT:-8081}"
headers="$(curl -fsSI "http://localhost:${js_port}/")"

echo "$headers" | grep -qi "x-content-type-options: nosniff"
echo "$headers" | grep -qi "x-frame-options: deny"

echo "[security] Security-Smoke-Checks erfolgreich"
