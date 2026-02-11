# Paper Demo Workflow (Expert 3–10 min version)

## Current demo execution (what is happening now)
- **Parsing/OCR stage model**: no LLM model used.
- **Parser used**: local `PyMuPDF` (`fitz`) extraction from PDF pages (cost-saving mode).
- **Reasoning/post generation model**: `moonshotai/kimi-k2.5`.
- **Output root**: `~/Desktop/OpenClaw_Library/briefings/demo3/`.

## End-to-end workflow
1. **Paper selection**
   - pick 3 representative PDFs from `papers/`.
2. **Local parse (free)**
   - extract text from core pages only (default first 10–15 pages for cost control).
   - produce `paper_raw.md`.
3. **Structured parse artifact**
   - build `parsed.md` with: goal, hypothesis, method, metrics, key results.
4. **Figure-text linking**
   - map core figures/tables to claims and section/page evidence.
   - produce `figure_map.md` and `evidence_map.json`.
5. **Expert post drafting**
   - generate `post_expert.md` (3–10 min read target).
6. **Consistency gate**
   - label each key statement as: Paper states / Interpretation / Speculation.
   - remove unsupported claims.

## Preset (expert mode)
- Audience: domain experts
- Read time: 3–10 min
- Style: dense, no fluff, methodological essence preserved
- Mandatory sections:
  1) Goal & Intent
  2) Structure of Argument
  3) Experimental Procedure & Logic
  4) Analysis Metrics (definition + intuition + assumptions + failure modes)
  5) Interpretation & Implications
  6) Discussion Points

## Constraints
- No hallucinations.
- Every key claim should include evidence pointer when possible: `(Fig.X pY; Sec Z pW)`.
- Separate clearly:
  - **Paper states**
  - **My interpretation**
  - **Speculative idea**
- Token control:
  - avoid repeated full-document passes,
  - process only core sections/figures,
  - cache parsed text.

## API / model requirements
- Minimum APIs: **1** (reasoning+draft generation)
- Recommended APIs: **2** (cheap first pass + stronger verifier)
- Current demo model: `moonshotai/kimi-k2.5`

## Current blockers to perfect flow
- Local toolchain lacks `pdftotext` and some science-parsing libs by default.
- Figure extraction currently text-first; richer figure OCR/axis extraction should be added next.

## Suggested next upgrade (still cost-aware)
- Add local parsers:
  - `marker-pdf`
  - `grobid`
- Add a strict evidence-checker pass before final post.
