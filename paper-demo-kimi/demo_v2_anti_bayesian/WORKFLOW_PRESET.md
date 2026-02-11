# Demo preset: paper-specialized parsing + Kimi reasoning

## Parsing stack (paper/PDF specialized)
- **Local structural parsing**: PyMuPDF (page text + page images)
- **Figure linkage**: figure-caption blocks + in-text figure mentions (`Fig. X`) matched by page proximity
- **Math linkage**: equation-containing blocks (Online Methods pages) linked to claims using citation pointers

> Next upgrade (recommended): Marker + GROBID for stronger table/reference/equation structure.

## Reasoning model usage
- Model: `moonshotai/kimi-k2.5`
- Role:
  1) Build hypothesis/prediction map before reading later sections
  2) Validate/adjust map after Results and Methods
  3) Write expert post with strict evidence pointers

## Constraints
1. Separate labels:
   - **Paper states**
   - **Interpretation**
   - **Speculation**
2. Every key claim gets pointer format:
   - `(Fig.3 p4; Fig.4 p5; Online Methods p10)`
3. Figure interpretation must include axis/line/color/condition meaning.
4. Cost control: core pages first; no repeated full-document pass.

## Output contract
- `parsed.md`
- `figure_map.md`
- `evidence_map.json`
- `post_expert.md`
