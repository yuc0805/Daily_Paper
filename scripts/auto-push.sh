#!/bin/bash
# Auto-commit and push for the AI Knowledge Graph repo.
# Runs natively on macOS via launchd. Bypasses the Claude sandbox's filesystem quirk.

set -u
REPO="$HOME/Documents/AI-Knowledge-Graph"
LOG="$REPO/scripts/auto-push.log"

cd "$REPO" || { echo "$(date '+%F %T')  repo not found" >> "$LOG"; exit 1; }

# Clean any stale lock files (from sandbox commits that left artifacts).
find .git -name "*.lock" -mmin +1 -delete 2>/dev/null

# Make git ignore the file-mode differences that virtiofs introduces.
git config core.fileMode false 2>/dev/null

# If nothing changed, exit quietly.
if [ -z "$(git status --porcelain)" ]; then
  exit 0
fi

STAMP=$(date '+%Y-%m-%d %H:%M')
git add -A
git commit -m "Auto-commit $STAMP" -q

if git remote get-url origin >/dev/null 2>&1; then
  git push origin HEAD 2>&1 | tail -3 >> "$LOG"
  echo "$(date '+%F %T')  pushed" >> "$LOG"
else
  echo "$(date '+%F %T')  no remote, local commit only" >> "$LOG"
fi
