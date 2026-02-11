# Paper Demo (Kimi k2.5)

이 레포는 내가 실제로 사용한 논문 처리 워크플로우 설명과, 논문 3편 데모 결과를 담고 있습니다.

## 포함 내용
- `WORKFLOW.md`: 파이프라인 동작 방식(파싱/추론/제약/비용절감 규칙)
- `demo/<paper_key>/parsed.md`: 논문 구조화 요약(Goal/Hypothesis/Method/Metrics/Results)
- `demo/<paper_key>/paper_raw.md`: 로컬 파싱 원문(핵심 페이지 추출)

## 데모 논문 3편
1. `unifying_theory`
   - A unifying theory explains seemingly contradictory biases in perceptual estimation (Nature Neuroscience, 2024)
2. `anti_bayesian`
   - A Bayesian observer model constrained by efficient coding can explain anti-Bayesian percepts (Nature Neuroscience, 2015)
3. `structure_in_time`
   - Finding Structure in Time (Cognitive Science, 1990)

## 워크플로우 요약
1. PDF 선택
2. 로컬 무료 파싱(PyMuPDF 기반)
3. 핵심 섹션 구조화 (`parsed.md`)
4. 추론 모델(Kimi k2.5)로 논리/방법/지표 중심 해석
5. 근거 기반 포스트 초안 생성

## 제약/원칙
- 과장 금지, 근거 우선
- 토큰 낭비 방지: 핵심 페이지/핵심 섹션 우선 처리
- 사실/해석/추측 분리

---
필요하면 다음 단계로 `figure_map.md`, `evidence_map.json`, `post_expert.md`를 각 논문별로 추가 확장합니다.
