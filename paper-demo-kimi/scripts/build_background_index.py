#!/usr/bin/env python3
"""Build a lightweight background RAG index from JSONL metadata.

Usage:
  python scripts/build_background_index.py \
    --input rag/background_corpus.jsonl \
    --output rag/background_index.json
"""
import argparse, json, math, re
from collections import Counter, defaultdict

def tok(s: str):
    return re.findall(r"[a-zA-Z0-9_\-]+", s.lower())

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    docs = []
    with open(args.input) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            j = json.loads(line)
            text = " ".join([
                j.get("title", ""),
                " ".join(j.get("authors", [])),
                " ".join(j.get("field_tags", [])),
                j.get("background", ""),
                j.get("problem_gap", ""),
                j.get("why_this_study", ""),
            ])
            docs.append({"paper_id": j["paper_id"], "meta": j, "tokens": tok(text)})

    N = len(docs)
    df = defaultdict(int)
    for d in docs:
        for t in set(d["tokens"]):
            df[t] += 1

    index_docs = []
    for d in docs:
        tf = Counter(d["tokens"])
        vec = {}
        norm = 0.0
        for t, c in tf.items():
            idf = math.log((N + 1) / (df[t] + 1)) + 1.0
            w = c * idf
            vec[t] = w
            norm += w * w
        index_docs.append({
            "paper_id": d["paper_id"],
            "meta": d["meta"],
            "vec": vec,
            "norm": math.sqrt(norm)
        })

    with open(args.output, "w") as f:
        json.dump({"n_docs": N, "docs": index_docs}, f, ensure_ascii=False, indent=2)
    print(f"wrote {args.output} with {N} docs")

if __name__ == "__main__":
    main()
