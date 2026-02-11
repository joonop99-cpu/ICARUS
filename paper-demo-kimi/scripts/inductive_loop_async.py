#!/usr/bin/env python3
"""Inductive-bias literature loop scaffold (async discovery + question queue).

Input: seed papers jsonl with fields: title, doi(optional), openalex_id(optional)
Output:
- workflow/loops/inductive_queue.jsonl
- workflow/loops/next_questions.md

Discovery rules:
1) referenced works of current paper
2) same author-group works (first/last author)
3) similar works via OpenAlex related_works + keyword overlap proxy
"""
import argparse, asyncio, json, re
from pathlib import Path
from urllib.parse import quote
import aiohttp

OPENALEX = "https://api.openalex.org"


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip().lower())


async def fetch_json(session, url):
    async with session.get(url, timeout=40) as r:
        r.raise_for_status()
        return await r.json()


async def resolve_work(session, seed):
    if seed.get("openalex_id"):
        wid = seed["openalex_id"]
        if wid.startswith("W"):
            wid = f"https://openalex.org/{wid}"
        return await fetch_json(session, f"{OPENALEX}/works/{quote(wid, safe=':/')}" )
    if seed.get("doi"):
        doi = seed["doi"].lower().replace("https://doi.org/", "")
        return await fetch_json(session, f"{OPENALEX}/works/https://doi.org/{quote(doi)}")
    q = quote(seed["title"])
    data = await fetch_json(session, f"{OPENALEX}/works?search={q}&per-page=1")
    return (data.get("results") or [None])[0]


def pick_authors(work):
    authorships = work.get("authorships") or []
    names = []
    if authorships:
        names.append((authorships[0].get("author") or {}).get("display_name", ""))
    if len(authorships) > 1:
        names.append((authorships[-1].get("author") or {}).get("display_name", ""))
    return [n for n in names if n]


async def discover_from_work(session, work, year_min, year_max):
    out = []
    wid = work.get("id", "")
    title = work.get("display_name", "")

    # 1) referenced works
    for ref in (work.get("referenced_works") or [])[:80]:
        out.append({"reason": "cited_by_current", "source_work": wid, "target_openalex": ref})

    # 2) author-group
    for a in pick_authors(work):
        q = quote(a)
        url = f"{OPENALEX}/works?filter=from_publication_date:{year_min}-01-01,to_publication_date:{year_max}-12-31,authorships.author.display_name.search:{q}&per-page=20"
        data = await fetch_json(session, url)
        for r in (data.get("results") or []):
            out.append({"reason": "author_group", "source_work": wid, "target_openalex": r.get("id"), "author": a})

    # 3) similar works proxy
    for rw in (work.get("related_works") or [])[:30]:
        out.append({"reason": "similarity_proxy", "source_work": wid, "target_openalex": rw, "hint": title[:120]})

    return out


async def main_async(args):
    seeds = [json.loads(x) for x in Path(args.seeds).read_text().splitlines() if x.strip()]
    out_q = Path(args.output_queue)
    out_q.parent.mkdir(parents=True, exist_ok=True)
    out_md = Path(args.output_questions)
    out_md.parent.mkdir(parents=True, exist_ok=True)

    rows = []
    async with aiohttp.ClientSession(headers={"User-Agent": "OpenClaw/inductive-loop"}) as session:
        for s in seeds:
            work = await resolve_work(session, s)
            if not work:
                continue
            discovered = await discover_from_work(session, work, args.year_min, args.year_max)
            rows.extend(discovered)

    # de-dup
    seen = set()
    dedup = []
    for r in rows:
        k = (r.get("target_openalex"), r.get("reason"))
        if k in seen:
            continue
        seen.add(k)
        dedup.append(r)

    out_q.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in dedup) + ("\n" if dedup else ""))

    questions = [
        "Q1. 핵심 claim이 반증가능한 예측으로 명시되는가? (A가 참이면 반드시 관측되어야 하는 결과는?)",
        "Q2. 실험 설계가 claim의 필요충분 조건을 분리해서 테스트하는가?",
        "Q3. metric/figure 해석에서 대안설명(confound)을 배제했는가?",
        "Q4. limitation과 research gap은 무엇이며 다음 검증 질문은 무엇인가?",
    ]
    out_md.write_text("# Next questions\n\n" + "\n".join(f"- {q}" for q in questions) + "\n")
    print(f"wrote queue={out_q} n={len(dedup)}")
    print(f"wrote questions={out_md}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seeds", required=True, help="jsonl: title/doi/openalex_id")
    ap.add_argument("--year-min", type=int, default=2022)
    ap.add_argument("--year-max", type=int, default=2026)
    ap.add_argument("--output-queue", default="/Users/joonoh/Desktop/OpenClaw_Library/workflow/loops/inductive_queue.jsonl")
    ap.add_argument("--output-questions", default="/Users/joonoh/Desktop/OpenClaw_Library/workflow/loops/next_questions.md")
    args = ap.parse_args()
    asyncio.run(main_async(args))


if __name__ == "__main__":
    main()
