# Pipeline (minimal, compact-first)

1. `context_packet.json` 생성 (강한 char cap)
2. OpenRouter pre-parse (text/equation/figure)
3. Kimi Stage B (`stage_b_reconcile.py`)
4. Kimi Stage C (`stage_c_finalize.py`)

규칙:
- Stage B/C는 packet 입력만 사용
- raw full-doc 입력 금지
- 캐시 hit 우선
