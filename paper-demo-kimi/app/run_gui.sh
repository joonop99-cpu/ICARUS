#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
VENV="$ROOT/.venv"
LOG_DIR="$ROOT/.logs"
LOG_FILE="$LOG_DIR/gui.log"
PID_FILE="$LOG_DIR/gui.pid"

mkdir -p "$LOG_DIR"

if [[ ! -d "$VENV" ]]; then
  python3 -m venv "$VENV"
fi

source "$VENV/bin/activate"
pip install -q --upgrade pip
pip install -q -r "$ROOT/requirements.txt"

if [[ -f "$PID_FILE" ]]; then
  OLD_PID="$(cat "$PID_FILE" || true)"
  if [[ -n "${OLD_PID:-}" ]] && kill -0 "$OLD_PID" 2>/dev/null; then
    kill "$OLD_PID" || true
    sleep 1
  fi
fi

nohup streamlit run "$ROOT/gui/app.py" --server.port 8502 --server.headless true > "$LOG_FILE" 2>&1 &
echo $! > "$PID_FILE"

echo "Paper Orchestrator running"
echo "URL: http://localhost:8502"
echo "LOG: $LOG_FILE"
