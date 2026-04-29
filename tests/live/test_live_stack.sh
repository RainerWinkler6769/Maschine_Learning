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

require_cmd() {
  if ! command -v "$1" >/dev/null 2>&1; then
    echo "[live-test] Fehler: '$1' fehlt"
    exit 1
  fi
}

require_cmd docker
require_cmd curl

python_port="${PYTHON_API_PORT:-8000}"
php_port="${PHP_WEB_PORT:-8080}"
js_port="${JS_WEB_PORT:-8081}"
java_port="${JAVA_APP_PORT:-8082}"

curl -fsS "http://localhost:${python_port}/health" | grep -q "ok"
curl -fsS "http://localhost:${python_port}/" | grep -q "Hallo Welt aus Python"
curl -fsS "http://localhost:${php_port}" | grep -q "Hallo Welt aus PHP"
curl -fsS "http://localhost:${js_port}/app.js" | grep -q "Hallo Welt aus JavaScript"
curl -fsS "http://localhost:${java_port}/" | grep -q "Hallo Welt aus Java"

docker compose exec -T mysql \
  mysql -u"${MYSQL_USER:-edu_user}" -p"${MYSQL_PASSWORD:-edu_pass}" "${MYSQL_DATABASE:-edu_demo}" \
  -e "SELECT COUNT(*) AS count_hello FROM hello_log;" | grep -Eq "count_hello|[1-9]"

echo "[live-test] Alle Live-Checks erfolgreich"
