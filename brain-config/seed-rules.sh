#!/bin/bash
# ─── Brain Seed Script — Drawio Master Rules ───────────────────
# Ingest all reference rules into brain DB for FTS5 search.
# Run once after setup, or after rules files update.
#
# Usage: bash brain-config/seed-rules.sh
# Requires: brain binary running (stdio mode) OR python3
# ────────────────────────────────────────────────────────────────

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
POWER_ROOT="$(dirname "$SCRIPT_DIR")"
REFS_DIR="$POWER_ROOT/skills/drawio-master/references"
DB_PATH="${LAMBDA_BRAIN_DB_PATH:-$HOME/.brain/brain.db}"

echo "🧠 Brain Seed — Drawio Master"
echo "   DB: $DB_PATH"
echo "   Rules: $REFS_DIR"
echo ""

# Use python3 to parse rules and insert directly into SQLite
# (No need for brain server running — direct DB access)

python3 "$SCRIPT_DIR/seed-rules.py" "$REFS_DIR" "$DB_PATH"

echo ""
echo "✅ Seed complete. Brain ready for drawio-master queries."
