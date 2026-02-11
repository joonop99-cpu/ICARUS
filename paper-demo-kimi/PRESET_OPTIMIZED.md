# Optimized Preset (v1)

## Goal
논문 1편을 **Background → Aim/Hypothesis(사전예측) → Methods/Metric 원리 → Figure 해석 → Discussion** 순서로, 근거 링크가 있는 전문가 포스트로 생성한다.

## Stage contract

### Stage A: Background + Pre-Results Hypothesis (Kimi)
입력:
- intro/background 텍스트
- RAG background hit 상위 2~3개

출력(필수):
1. 왜 이 연구를 했는가(필드 문제/갭)
2. H1/H0
3. H1 참일 때 반드시 나와야 하는 결과
4. H0 참일 때 반드시 나와야 하는 결과
5. 어떤 Figure/Equation이 판별 포인트인지

### Stage B: Evidence Reconciliation (Kimi)
입력:
- figure_map
- equations/method blocks
- results text

출력(필수):
- 가설별 지지/반증 표
- 축/색/점선/조건 의미 정리
- claim별 evidence pointer

### Stage C: Final Expert Post (Kimi)
라벨 강제:
- Paper states
- Interpretation
- Speculation

## Hard constraints
- 근거 없는 문장 금지
- key claim마다 `(Fig.X pY; Eq/Methods pZ)` 포인터
- 불확실하면 `unknown` 표기
- 분량은 3~10분 읽기

## Cost controls
- 전체 문서 반복파싱 금지
- 핵심 페이지/핵심 도판 우선
- RAG에서 배경 재사용
