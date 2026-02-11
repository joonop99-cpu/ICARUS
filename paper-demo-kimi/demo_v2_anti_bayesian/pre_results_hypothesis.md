# Pre-Results Hypothesis Note (anti_bayesian_2015)

## Background (intro + shared field metadata)
- 지각 연구는 보통 **efficient coding(표상 제약)** 과 **Bayesian decoding(추론)** 을 분리해 설명해왔다.
- 하지만 표준 Bayesian(대칭 likelihood 가정)는 prior 쪽 **attractive bias**를 예측하는 경향이 강한 반면, 실제 psychophysics에는 prior peak에서 멀어지는 **repulsive bias**가 반복 보고된다.
- 관련 메타데이터 참조:
  - `unifying_theory_2024`: attractive/repulsive 상충 결과를 단일 원리로 설명하려는 흐름

## Why this study now?
- 저자 목표는 “anti-Bayesian처럼 보이는 현상”을 Bayesian의 실패로 보지 않고,
  **encoding 제약을 포함한 Bayesian 프레임**에서 재설명하는 것.
- 즉, 필드의 핵심 갭(표상-추론 분리)을 하나의 observer model로 연결하려는 시도.

## Aim & Hypotheses
- **H1 (핵심가설)**: efficient coding으로 인해 stimulus space likelihood가 비대칭이 되면, Bayes decoding에서도 repulsive bias가 자연스럽게 발생한다.
- **H0 (대안가설)**: 표준 대칭 likelihood Bayesian으로도 repulsive bias와 noise-source 차이를 충분히 설명할 수 있다.

## Pre-registered predictions (before full Results read)
- **If H1 true, must observe:**
  1) prior peak 주변에서도 repulsive bias 가능
  2) sensory/internal noise vs stimulus/external noise가 bias에 **서로 다른 방향**의 효과
  3) orientation뿐 아니라 spatial-frequency에서도 같은 원리 유지
- **If H0 true, must observe:**
  1) noise source 분화효과가 약하거나 일관되지 않음
  2) repulsive 패턴을 설명하려면 ad-hoc 가정이 추가로 필요

## Evidence plan (discriminative checks)
- Figure 분기 포인트: **Fig.3, Fig.4, Fig.6/7**
- 수식/원리 포인트: **Online Methods(Fisher information constraint + decoding loss)**
- 판별 기준:
  - Fig.3에서 noise source별 곡선 방향이 갈리는가?
  - Fig.4에서 orientation bias 곡선이 조건별로 정합되는가?
  - Methods 가정(encoding→likelihood 비대칭→decoding bias)이 결과와 일치하는가?
