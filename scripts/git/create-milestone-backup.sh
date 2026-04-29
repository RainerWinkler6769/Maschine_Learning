#!/usr/bin/env bash
set -euo pipefail

repo_root="$(git rev-parse --show-toplevel)"
cd "$repo_root"

milestone_raw="${1:-auto}"
milestone_slug="$(echo "$milestone_raw" | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9._-]+/-/g; s/^-+//; s/-+$//')"
if [[ -z "$milestone_slug" ]]; then
  milestone_slug="auto"
fi

timestamp="$(date -u +%Y%m%dT%H%M%SZ)"
short_sha="$(git rev-parse --short HEAD)"
backup_dir="backups/milestones/${timestamp}_${milestone_slug}_${short_sha}"
mkdir -p "$backup_dir"

bundle_path="$backup_dir/repository.bundle"
manifest_path="$backup_dir/manifest.txt"

# Full-fidelity git backup that can be cloned/restored independently.
git bundle create "$bundle_path" --all

{
  echo "milestone=$milestone_raw"
  echo "timestamp_utc=$timestamp"
  echo "commit=$(git rev-parse HEAD)"
  echo "branch=$(git rev-parse --abbrev-ref HEAD)"
  echo "repository=$(basename "$repo_root")"
} > "$manifest_path"

git log -1 --stat > "$backup_dir/last_commit.txt"
sha256sum "$bundle_path" > "$backup_dir/repository.bundle.sha256"

tarball="${backup_dir}.tar.gz"
tar -czf "$tarball" -C "$(dirname "$backup_dir")" "$(basename "$backup_dir")"

echo "Backup erstellt: $tarball"
