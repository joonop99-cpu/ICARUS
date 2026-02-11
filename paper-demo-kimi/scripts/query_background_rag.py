#!/usr/bin/env python3
"""Query lightweight background RAG index.

Usage:
  python scripts/query_background_rag.py --index rag/background_index.json --query "anti-bayesian bias efficient coding" --topk 3
"""
import argparse, json, math, re
from collections import Counter

def tok(s: str):
    return re.findall(r"[a-zA-Z0-9_\-]+", s.lower())

def cosine(qvec, qnorm, dvec, dnorm):
    if qnorm == 0 or dnorm == 0:
        return 0.0
    dot = 0.0
    for t, w in qvec.items():
        dot += w * dvec.get(t, 0.0)
    return dot / (qnorm * dnorm)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--index", required=True)
    ap.add_argument("--query", required=True)
    ap.add_argument("--topk", type=int, default=3)
    args = ap.parse_args()

    idx = json.load(open(args.index))
    qtf = Counter(tok(args.query))
    qvec = {t: float(c) for t, c in qtf.items()}
    qnorm = math.sqrt(sum(w*w for w in qvec.values()))

    scored = []
    for d in idx["docs"]:
        s = cosine(qvec, qnorm, d["vec"], d["norm"])
        scored.append((s, d["meta"]))
    scored.sort(reverse=True, key=lambda x: x[0])

    for rank, (s, m) in enumerate(scored[:args.topk], 1):
        print(f"[{rank}] score={s:.4f} paper_id={m['paper_id']}")
        print(f"  title: {m['title']}")
        print(f"  background: {m['background']}")
        print(f"  gap: {m['problem_gap']}")
        print(f"  why: {m['why_this_study']}")

if __name__ == "__main__":
    main()
