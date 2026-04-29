#!/usr/bin/env bash
set -euo pipefail

repo_root="$(git rev-parse --show-toplevel)"

chmod +x "$repo_root"/.githooks/pre-commit
chmod +x "$repo_root"/.githooks/pre-push
chmod +x "$repo_root"/scripts/git/approval.sh

# Set repository-local hooks path so every local commit/push is guarded.
git config --local core.hooksPath .githooks

echo "Hooks aktiviert: core.hooksPath=.githooks"
echo "Freigabe erteilen mit:"
echo "  scripts/git/approval.sh grant commit 15"
echo "  scripts/git/approval.sh grant push 15"
