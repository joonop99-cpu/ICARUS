# Background RAG

## Files
- `background_corpus.jsonl`: paper-level background/problem-gap/why-study metadata
- `background_index.json`: lightweight tf-idf index (generated)
- `background_metadata.schema.json`: schema for metadata quality control

## Build
```bash
python scripts/build_background_index.py \
  --input rag/background_corpus.jsonl \
  --output rag/background_index.json
```

## Query
```bash
python scripts/query_background_rag.py \
  --index rag/background_index.json \
  --query "efficient coding anti-bayesian bias" \
  --topk 3
```

## Usage in pipeline
1. Parse intro/background from target paper
2. Retrieve top-k related background metadata
3. Generate pre-results hypothesis note using intro + retrieved context
4. Continue to methods/results reconciliation

## Optimization notes
- Add weighted fields (title/field_tags/background > others)
- Add citation graph boost (same field + shared citations)
- Add bilingual normalization (ko/en query variants)
