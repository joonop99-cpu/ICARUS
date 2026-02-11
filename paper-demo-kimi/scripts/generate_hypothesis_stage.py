#!/usr/bin/env python3
"""Generate a structured pre-results hypothesis note from intro/background + RAG hits.

This is the stage executed BEFORE reading full Results/Discussion.
"""
import argparse, json, re

def read_head(path, max_chars=5000):
    txt = open(path).read()
    return txt[:max_chars]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--paper-id", required=True)
    ap.add_argument("--intro", required=True, help="intro/background text file")
    ap.add_argument("--rag-index", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    intro = read_head(args.intro)
    idx = json.load(open(args.rag_index))
    hits = [d["meta"] for d in idx["docs"] if d["meta"].get("paper_id") != args.paper_id][:2]

    tpl = []
    tpl.append(f"# Pre-Results Hypothesis Note ({args.paper_id})\n")
    tpl.append("## Background (from intro + shared field metadata)\n")
    tpl.append("- 핵심 배경 요약: [INTRO 기반으로 채우기]\n")
    tpl.append("- 현재 필드의 공통 문제: [RAG 참조 기반]\n")
    for h in hits:
      tpl.append(f"  - ref `{h['paper_id']}`: {h['problem_gap']}\n")

    tpl.append("\n## Why this study now?\n")
    tpl.append("- [저자 동기/필요성]\n")

    tpl.append("\n## Aim & Hypotheses\n")
    tpl.append("- H1 (저자 핵심가설): [ ]\n")
    tpl.append("- H0 (대안가설): [ ]\n")

    tpl.append("\n## Pre-registered predictions (before Results read)\n")
    tpl.append("- If H1 true, must observe: [ ]\n")
    tpl.append("- If H0 true, must observe: [ ]\n")

    tpl.append("\n## Evidence plan\n")
    tpl.append("- 어떤 Figure/Equation/Method를 보면 가설이 갈리는지: [ ]\n")

    tpl.append("\n---\n")
    tpl.append("### Intro snippet used\n")
    tpl.append(intro.replace("\n", " ")[:2000] + "\n")

    with open(args.out, "w") as f:
        f.write("".join(tpl))
    print(f"wrote {args.out}")

if __name__ == "__main__":
    main()
