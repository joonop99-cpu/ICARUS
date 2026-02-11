# paper-demo-kimi (v2 compact)

논문 분석 파이프라인의 **컴팩트 버전**입니다.

## 포함 범위 (현재)
- `demo_v2_anti_bayesian/`: 1편 완성 데모 (figure/text/math 연결)
- `rag/`: Background 메타데이터 + 경량 RAG 인덱스
- `scripts/`: RAG 빌드/질의 + pre-results hypothesis 생성
- `gui/`: 워크플로우 오케스트레이션용 Streamlit GUI
- `local/`: Ollama 로컬모델 외주 유틸

## 핵심 워크플로우
1. Intro + Background 메타데이터 RAG로 **사전 가설(H1/H0)** 생성
2. Figure/Equation/Methods 근거와 대조
3. `Paper states / Interpretation / Speculation` 라벨로 최종 포스트 생성

## 빠른 실행
```bash
# 1) RAG 인덱스 생성
python3 scripts/build_background_index.py --input rag/background_corpus.jsonl --output rag/background_index.json

# 2) 사전 가설 생성 (Results 읽기 전)
python3 scripts/generate_hypothesis_stage.py \
  --paper-id anti_bayesian_2015 \
  --intro demo_v2_anti_bayesian/parsed.md \
  --rag-index rag/background_index.json \
  --out demo_v2_anti_bayesian/pre_results_hypothesis.md

# 3) GUI 실행
streamlit run gui/app.py
```

## 전처리(파싱)는 OpenRouter, 로컬은 실행/보조
```bash
# OpenRouter로 text/equation/figure 파싱 (캐시 포함)
# task별 기본모델 자동 선택:
# - parse_text -> google/gemini-2.0-flash-exp
# - parse_equation -> anthropic/claude-3.5-sonnet
# - parse_figure -> openai/gpt-4.1-mini
export OPENROUTER_API_KEY=...
python3 scripts/openrouter_preparse.py --task parse_text --input context/context_packet.json --out tmp/parse_text.json

# 모델 강제 override 가능
python3 scripts/openrouter_preparse.py --task parse_equation --input context/context_packet.json --model google/gemini-2.0-flash-exp --out tmp/parse_eq.json

# 만료 캐시 정리 (예: 72시간)
python3 scripts/openrouter_preparse.py --cleanup-only --input README.md --cache-ttl-hours 72

# 로컬(Ollama)은 보조 작업(요약/정규화/체크리스트)
python3 local/delegate_basic.py --task summarize --input demo_v2_anti_bayesian/parsed.md --model qwen2.5:7b-instruct
```

## aggressive context compaction
```bash
python3 scripts/context_compact.py --root . --out context/context_packet.json --per-file 2500
```

## Stage B/C (compact packet 고정)
```bash
# Stage B: evidence reconciliation (Kimi)
python3 scripts/stage_b_reconcile.py \
  --packet context/context_packet.json \
  --model moonshotai/kimi-k2.5 \
  --out demo_v2_anti_bayesian/stage_b_reconcile.md

# Stage C: final expert post (Kimi)
python3 scripts/stage_c_finalize.py \
  --packet context/context_packet.json \
  --stage-b demo_v2_anti_bayesian/stage_b_reconcile.md \
  --model moonshotai/kimi-k2.5 \
  --out demo_v2_anti_bayesian/post_expert_compact.md
```

## Async 수집/탐색 루프
```bash
# 1) 저널 수집 (Nature Neuroscience/Neuron/J Neurosci, 2022-2026)
python3 scripts/journal_harvest_async.py \
  --output-root /Users/joonoh/Desktop/OpenClaw_Library \
  --year-min 2022 --year-max 2026 \
  --keywords "numerosity,magnitude,efficient coding,bayesian" \
  --preferred-authors ""

# 2) 시드 기반 inductive queue 생성
python3 scripts/inductive_loop_async.py \
  --seeds /Users/joonoh/Desktop/OpenClaw_Library/workflow/loops/seeds.jsonl \
  --year-min 2022 --year-max 2026
```
