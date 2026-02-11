#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
APP_DIR="$HOME/Applications"
APP_PATH="$APP_DIR/PaperOrchestrator.app"
LAUNCH_SH="$ROOT/app/run_gui.sh"

mkdir -p "$APP_DIR"

TMP_SCPT="$(mktemp)"
cat > "$TMP_SCPT" <<'APPLESCRIPT'
do shell script "bash \"__LAUNCH_SH__\""
do shell script "open http://localhost:8502"
APPLESCRIPT

ESCAPED_LAUNCH=$(printf '%s' "$LAUNCH_SH" | sed 's/[\\&]/\\&/g')
sed -i '' "s|__LAUNCH_SH__|$ESCAPED_LAUNCH|g" "$TMP_SCPT"

osacompile -o "$APP_PATH" "$TMP_SCPT"
rm -f "$TMP_SCPT"

echo "Installed: $APP_PATH"
echo "Double-click app to start GUI and open browser"
