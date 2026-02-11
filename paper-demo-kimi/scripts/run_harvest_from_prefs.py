#!/usr/bin/env python3
import argparse, json, subprocess
from pathlib import Path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prefs", default="config/harvest_prefs.json")
    ap.add_argument("--output-root", default="/Users/joonoh/Desktop/OpenClaw_Library")
    args = ap.parse_args()

    p = Path(args.prefs)
    if not p.exists():
        raise SystemExit(f"prefs missing: {p} (copy from config/harvest_prefs.example.json)")
    cfg = json.loads(p.read_text())

    cmd = [
        "python3", "scripts/journal_harvest_async.py",
        "--output-root", args.output_root,
        "--year-min", str(cfg.get("year_min", 2022)),
        "--year-max", str(cfg.get("year_max", 2026)),
        "--keywords", ",".join(cfg.get("keywords", [])),
        "--preferred-authors", ",".join(cfg.get("preferred_authors", [])),
    ]
    print(" ".join(cmd))
    subprocess.check_call(cmd)


if __name__ == "__main__":
    main()
