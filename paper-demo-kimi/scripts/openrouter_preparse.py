#!/usr/bin/env python3
"""OpenRouter pre-parse worker with local prompt/result cache.

Purpose:
- Use OpenRouter for image/text/equation parsing
- Reuse cached responses to reduce token cost and context bloat
"""
import argparse, hashlib, json, os
from pathlib import Path
import requests

DEFAULT_MODEL = "google/gemini-2.0-flash-exp"


def sha(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def load_text(path: str, max_chars: int) -> str:
    t = Path(path).read_text()
    return t[:max_chars]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--task", choices=["parse_text", "parse_equation", "parse_figure"], default="parse_text")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--max-chars", type=int, default=12000)
    ap.add_argument("--cache-dir", default=".cache/openrouter")
    ap.add_argument("--out", default="")
    args = ap.parse_args()

    api_key = os.getenv("OPENROUTER_API_KEY", "")
    if not api_key:
        raise SystemExit("OPENROUTER_API_KEY is required")

    text = load_text(args.input, args.max_chars)
    sys = (
        "You are a scientific parser. Return compact JSON only. "
        "No prose. Include evidence pointers when possible."
    )
    usr = f"task={args.task}\n\n{text}"

    cache_dir = Path(args.cache_dir)
    cache_dir.mkdir(parents=True, exist_ok=True)
    key = sha(args.model + "\n" + sys + "\n" + usr)
    cache_file = cache_dir / f"{key}.json"
    if cache_file.exists():
        out = cache_file.read_text()
        if args.out:
            Path(args.out).write_text(out)
            print(f"cache_hit wrote {args.out}")
        else:
            print(out)
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
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        data=json.dumps(body),
        timeout=90,
    )
    r.raise_for_status()
    data = r.json()
    content = data["choices"][0]["message"]["content"]

    cache_file.write_text(content)
    if args.out:
        Path(args.out).write_text(content)
        print(f"cache_miss wrote {args.out}")
    else:
        print(content)


if __name__ == "__main__":
    main()
