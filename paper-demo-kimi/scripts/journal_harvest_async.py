#!/usr/bin/env python3
"""Async journal harvester (2022-2026) with randomized polite delay.

Targets default journals:
- Nature Neuroscience
- Neuron
- Journal of Neuroscience

Filters by keyword and preferred author (optional).
Writes metadata + PDF (when direct legal link available), else download-needed list.
"""
import argparse, asyncio, json, os, random, re
from pathlib import Path
import aiohttp

CROSSREF = "https://api.crossref.org/works"
DEFAULT_JOURNALS = {
    "nature_neuroscience": "1097-6256",
    "neuron": "0896-6273",
    "journal_of_neuroscience": "0270-6474",
}


def contains_any(text, words):
    t = (text or "").lower()
    return any(w.lower() in t for w in words)


async def fetch_json(session, url):
    async with session.get(url, timeout=50) as r:
        r.raise_for_status()
        return await r.json()


async def fetch_bytes(session, url):
    async with session.get(url, timeout=90) as r:
        if r.status != 200:
            return None
        ctype = (r.headers.get("content-type") or "").lower()
        if "pdf" not in ctype and not url.lower().endswith(".pdf"):
            return None
        return await r.read()


def safe_name(s):
    s = re.sub(r"[^a-zA-Z0-9._-]+", "_", s.strip())
    return s[:120] if s else "untitled"


async def harvest_journal(session, jname, issn, args, out_meta, out_missing):
    url = (
        f"{CROSSREF}?filter=from-pub-date:{args.year_min}-01-01,until-pub-date:{args.year_max}-12-31,issn:{issn},type:journal-article"
        f"&rows={args.rows_per_journal}&select=DOI,title,author,issued,URL,container-title,link"
    )
    data = await fetch_json(session, url)
    items = (((data or {}).get("message") or {}).get("items") or [])

    papers_dir = Path(args.output_root) / "papers" / "journal_harvest" / jname
    papers_dir.mkdir(parents=True, exist_ok=True)

    for it in items:
        title = ((it.get("title") or [""])[0] or "").strip()
        doi = (it.get("DOI") or "").strip()
        year = ((((it.get("issued") or {}).get("date-parts") or [[None]])[0] or [None])[0])
        authors = [" ".join(filter(None, [a.get("given", ""), a.get("family", "")])).strip() for a in (it.get("author") or [])]
        abstract_probe = " ".join([title, " ".join(authors)])

        if args.keywords and not contains_any(abstract_probe, args.keywords):
            continue
        if args.preferred_authors and not any(contains_any(a, args.preferred_authors) for a in authors):
            continue

        meta = {
            "journal": jname,
            "title": title,
            "doi": doi,
            "year": year,
            "authors": authors,
            "url": it.get("URL", ""),
        }
        out_meta.write(json.dumps(meta, ensure_ascii=False) + "\n")
        await out_meta.drain()

        # randomized polite delay per journal item before PDF attempt
        await asyncio.sleep(random.uniform(args.min_delay_sec, args.max_delay_sec))

        pdf_url = None
        for lk in (it.get("link") or []):
            ctype = (lk.get("content-type") or "").lower()
            if "pdf" in ctype:
                pdf_url = lk.get("URL")
                break

        fname = safe_name(f"{year}_{title}") + ".pdf"
        fpath = papers_dir / fname
        if pdf_url:
            blob = await fetch_bytes(session, pdf_url)
            if blob:
                fpath.write_bytes(blob)
                continue

        out_missing.write(f"- [{jname}] {title} ({year}) doi:{doi} :: no direct PDF link/download blocked\n")
        await out_missing.drain()


async def main_async(args):
    out_root = Path(args.output_root)
    wf = out_root / "workflow" / "harvest"
    wf.mkdir(parents=True, exist_ok=True)
    meta_path = wf / "harvest-metadata.jsonl"
    missing_path = out_root / "workflow" / "missing" / "missing-pdf-list.md"
    missing_path.parent.mkdir(parents=True, exist_ok=True)

    headers = {"User-Agent": "OpenClaw journal-harvest"}
    async with aiohttp.ClientSession(headers=headers) as session:
        with meta_path.open("a", encoding="utf-8") as out_meta, missing_path.open("a", encoding="utf-8") as out_missing:
            tasks = [
                harvest_journal(session, name, issn, args, out_meta, out_missing)
                for name, issn in DEFAULT_JOURNALS.items()
            ]
            # run journals concurrently; delays are inside each stream
            await asyncio.gather(*tasks)

    print(f"wrote metadata={meta_path}")
    print(f"updated missing={missing_path}")


def parse_csv_list(s):
    return [x.strip() for x in (s or "").split(",") if x.strip()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output-root", default="/Users/joonoh/Desktop/OpenClaw_Library")
    ap.add_argument("--year-min", type=int, default=2022)
    ap.add_argument("--year-max", type=int, default=2026)
    ap.add_argument("--rows-per-journal", type=int, default=80)
    ap.add_argument("--keywords", type=parse_csv_list, default=[])
    ap.add_argument("--preferred-authors", type=parse_csv_list, default=[])
    ap.add_argument("--min-delay-sec", type=int, default=60)
    ap.add_argument("--max-delay-sec", type=int, default=180)
    args = ap.parse_args()
    asyncio.run(main_async(args))


if __name__ == "__main__":
    main()
