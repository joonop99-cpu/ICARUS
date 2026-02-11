#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PID_FILE="$ROOT/.logs/gui.pid"
if [[ -f "$PID_FILE" ]]; then
  PID="$(cat "$PID_FILE" || true)"
  if [[ -n "${PID:-}" ]] && kill -0 "$PID" 2>/dev/null; then
    kill "$PID" || true
    echo "stopped pid=$PID"
  else
    echo "no running process"
  fi
  rm -f "$PID_FILE"
else
  echo "pid file not found"
fi
