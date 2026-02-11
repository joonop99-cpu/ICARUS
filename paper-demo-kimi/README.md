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
export OPENROUTER_API_KEY=...
python3 scripts/openrouter_preparse.py --task parse_text --input demo_v2_anti_bayesian/parsed.md --model google/gemini-2.0-flash-exp --out tmp/parse_text.json

# 로컬(Ollama)은 보조 작업(요약/정규화/체크리스트)
python3 local/delegate_basic.py --task summarize --input demo_v2_anti_bayesian/parsed.md --model qwen2.5:7b-instruct
```

## aggressive context compaction
```bash
python3 scripts/context_compact.py --root . --out context/context_packet.json --per-file 2500
```
