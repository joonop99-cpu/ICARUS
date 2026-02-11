# Local delegation (Ollama)

목적: 클라우드 고가 모델(Kimi) 호출 전, 저비용 전처리를 로컬에서 수행해 토큰 사용량을 줄임.

## 권장 분업
- 로컬(Ollama):
  - 섹션 요약
  - 문장 정규화
  - figure caption 정리
  - 초안 체크리스트 생성
- Kimi:
  - 가설-근거 대조
  - 논리적 일관성 점검
  - 최종 전문가 포스트 작성

## 준비
```bash
ollama pull qwen2.5:7b-instruct
```

## 사용
```bash
python3 local/delegate_basic.py --task summarize --input ../demo_v2_anti_bayesian/parsed.md --model qwen2.5:7b-instruct
python3 local/delegate_basic.py --task normalize --input ../demo_v2_anti_bayesian/figure_map.md --model qwen2.5:7b-instruct
```
