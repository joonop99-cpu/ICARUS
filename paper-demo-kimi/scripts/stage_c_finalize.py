#!/usr/bin/env python3
"""Stage C: Final expert post from compact packet + Stage B output.
"""
import argparse, hashlib, json, os
from pathlib import Path
import requests

MODEL_DEFAULT = "moonshotai/kimi-k2.5"


def sha(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--packet", default="context/context_packet.json")
    ap.add_argument("--stage-b", default="demo_v2_anti_bayesian/stage_b_reconcile.md")
    ap.add_argument("--model", default=MODEL_DEFAULT)
    ap.add_argument("--cache-dir", default=".cache/openrouter")
    ap.add_argument("--out", default="demo_v2_anti_bayesian/post_expert_compact.md")
    args = ap.parse_args()

    api_key = os.getenv("OPENROUTER_API_KEY", "")
    if not api_key:
        raise SystemExit("OPENROUTER_API_KEY is required")

    packet = Path(args.packet).read_text()
    sb = Path(args.stage_b).read_text() if Path(args.stage_b).exists() else ""
    sys = (
        "You write concise expert research notes. Use only provided packet and stage-B audit. "
        "No hallucination. Mark unknown where evidence is insufficient."
    )
    usr = (
        "Task: Stage C Final Expert Post (3-10 min read)\n"
        "Required sections:\n"
        "- Background & Why this study\n"
        "- Aim & H1/H0\n"
        "- Methods/metrics principle\n"
        "- Figure-by-figure interpretation\n"
        "- Discussion (limits + next questions)\n"
        "Hard rule: prefix each key claim as [Paper states] / [Interpretation] / [Speculation]\n\n"
        f"STAGE_B:\n{sb}\n\nPACKET:\n{packet}"
    )

    cache = Path(args.cache_dir)
    cache.mkdir(parents=True, exist_ok=True)
    key = sha("stage_c\n" + args.model + "\n" + sys + "\n" + usr)
    cf = cache / f"{key}.md"
    if cf.exists():
        out = cf.read_text()
        Path(args.out).write_text(out)
        print(f"cache_hit wrote {args.out}")
        return

    body = {
        "model": args.model,
        "temperature": 0,
        "messages": [
            {"role": "system", "content": sys},
            {"role": "user", "content": usr},
        ],
    }
    r = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        data=json.dumps(body),
        timeout=120,
    )
    r.raise_for_status()
    content = r.json()["choices"][0]["message"]["content"]

    cf.write_text(content)
    Path(args.out).write_text(content)
    print(f"cache_miss wrote {args.out}")


if __name__ == "__main__":
    main()
