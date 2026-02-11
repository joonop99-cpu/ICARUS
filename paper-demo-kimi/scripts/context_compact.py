#!/usr/bin/env python3
"""Aggressive context compaction for this project.

Builds one small context packet from selected files with hard caps.
"""
import argparse, json
from pathlib import Path


def clip(path: Path, max_chars: int):
    t = path.read_text() if path.exists() else ""
    return t[:max_chars]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--out", default="context/context_packet.json")
    ap.add_argument("--per-file", type=int, default=2500)
    args = ap.parse_args()

    root = Path(args.root)
    files = [
        "demo_v2_anti_bayesian/pre_results_hypothesis.md",
        "demo_v2_anti_bayesian/figure_map.md",
        "demo_v2_anti_bayesian/evidence_map.json",
        "rag/background_corpus.jsonl",
    ]

    packet = {"project": "paper-demo-kimi", "files": []}
    for rel in files:
        p = root / rel
        packet["files"].append({
            "path": rel,
            "content": clip(p, args.per_file),
        })

    out = root / args.out
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(packet, ensure_ascii=False, indent=2))
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
