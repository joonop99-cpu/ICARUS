#!/usr/bin/env python3
import argparse
import subprocess
from pathlib import Path

PROMPTS = {
    "summarize": "다음 텍스트를 연구자용으로 12줄 이내 핵심요약해줘. 과장 금지, 근거 없는 추정 금지.\n\n",
    "normalize": "다음 텍스트를 용어/표기 통일된 형태로 정규화해줘. 의미 변경 금지.\n\n",
    "checklist": "다음 텍스트를 바탕으로 evidence 점검 체크리스트를 bullet로 만들어줘.\n\n",
}


def run_ollama(model: str, prompt: str) -> str:
    p = subprocess.run(["ollama", "run", model, prompt], capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError((p.stderr or p.stdout).strip())
    return p.stdout.strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--task", choices=sorted(PROMPTS.keys()), required=True)
    ap.add_argument("--input", required=True)
    ap.add_argument("--model", default="qwen2.5:7b-instruct")
    ap.add_argument("--out", default="")
    args = ap.parse_args()

    src = Path(args.input)
    text = src.read_text()
    prompt = PROMPTS[args.task] + text[:14000]

    out = run_ollama(args.model, prompt)

    if args.out:
        Path(args.out).write_text(out)
        print(f"wrote {args.out}")
    else:
        print(out)


if __name__ == "__main__":
    main()
