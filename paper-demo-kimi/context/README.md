# Context Compression

## Aggressive compaction policy
- Never pass raw full docs by default.
- Build `context/context_packet.json` and only send that packet first.
- Hard cap per source file (default 2500 chars).

## Build
```bash
python3 scripts/context_compact.py --root . --out context/context_packet.json --per-file 2500
```

## Prompt-cache policy
- Deterministic system prompt
- Deterministic task template
- Input hashing (`sha256(model + system + user)`) for cache key
- Reuse cached OpenRouter parse outputs before any new API call
