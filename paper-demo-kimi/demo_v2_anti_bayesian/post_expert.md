# A Bayesian observer model constrained by efficient coding can explain anti-Bayesian percepts (Wei & Stocker, 2015)

> DOI: 10.1038/nn.4105

## 1) Background — 무엇이 문제였고 왜 이 연구를 했나?

Perception 연구의 두 축은 오래 분리되어 있었다.
- **Efficient coding**: 신경계는 제한된 자원을 자연 통계에 맞춰 효율적으로 배분한다.
- **Bayesian decoding**: 뇌는 noisy sensory evidence와 prior를 결합해 추정한다.

문제는, 기존 Bayesian 설명만 보면 보통 prior 쪽으로 **attractive bias**가 나와야 하는데, 실제 psychophysics에는 prior peak에서 멀어지는 **repulsive/anti-Bayesian** 패턴이 반복적으로 관찰된다는 점이다. 이 논문은 이 모순을 “Bayes가 틀렸다”가 아니라, **encoding 제약을 빼먹었기 때문**으로 본다. (Intro p1; Fig.1 p2)

---

## 2) Aim & Hypothesis — 어떤 가설로 돌파했나?

### 핵심 가설 (H1)
효율코딩 제약 하에서 likelihood가 stimulus space에서 비대칭이 되면, Bayesian decoding 자체가 repulsive bias를 낼 수 있다. 즉 anti-Bayesian처럼 보이는 현상은 사실 **encoding-aware Bayesian**의 자연스러운 결과다. (Fig.1 p2; Results p3)

### 대안 가설 (H0)
표준 대칭 likelihood 기반 Bayesian 모델로도 충분하며, repulsive bias/노이즈 소스별 상반 효과를 별도 제약 없이 설명할 수 있다. (Fig.3d 대비 p4)

### 예측
- H1이 참이면:
  1) prior peak 근방에서도 repulsive bias가 가능
  2) **sensory/internal noise**와 **stimulus/external noise**가 bias에 서로 다른 방향으로 작용
- H0가 참이면:
  - 위의 분화 효과를 일관되게 설명하기 어렵고, ad-hoc 가정이 필요해진다.

---

## 3) 가설 검증을 위한 실험/조작적 정의/모델

### 모델 골격
1. **Encoding 단계**: Fisher information 기반 자원배분으로 sensory representation을 규정
2. **Decoding 단계**: 해당 representation에 대해 Bayesian posterior 추정
3. **Loss function**: posterior mean/median/mode(L2/L1/L0) 선택에 따라 정량치 변화 검토 (Methods p2; Online Methods p10)

### 조작적 정의
- Perceptual bias: 추정값 − 실제값
- Noise source 분리:
  - stimulus noise(외부 노이즈)
  - sensory noise(내부 표현 노이즈)

### 원리 포인트
핵심은 **likelihood shape의 비대칭성**이다. sensory space에서는 대칭 noise라도, stimulus space로 되돌아오면 mapping 때문에 비대칭이 되고, 이때 posterior center가 prior peak 반대 방향으로 밀릴 수 있다. (Fig.1/3 p2,p4)

> 인용 확장 논문은 본문 링크로 대체 가능: Jazayeri & Shadlen 2010 (temporal context) 등.

---

## 4) 결과 — figure에서 무엇이 보이고 무엇을 함의하나?

## Fig.3 (p4) — 이 논문의 결정적 메커니즘 그림
- 패널 a,b: noise source가 likelihood geometry에 다르게 작용
- 패널 c: prior(검정) + likelihood(색) 관계에서 attraction/repulsion 조건 시각화
- 패널 d:
  - y축: perceptual bias (위=repulsive, 아래=attractive)
  - 빨강(내부 noise 증가): repulsive 증가 경향
  - 파랑(외부 noise 증가): repulsive 감소, 조건에 따라 attractive로 전환

**함의**: “노이즈가 커지면 bias가 커진다/작아진다” 같은 단일 문장으로는 설명 불가. 어떤 노이즈냐가 본질이다. (Fig.3 p4)

## Fig.4 (p5) — orientation 데이터 정합
- x축: orientation θ(도)
- y축: bias(도)
- 색상/조건별 곡선과 실측치가 전반적으로 동일한 형태를 보임

**함의**: 모델은 단순 정성 설명이 아니라 조건별 곡선 형태까지 맞춘다. (Fig.4 p5)

## Fig.6/7 (p6)
orientation만이 아니라 spatial frequency에서도 동일 프레임이 작동한다.

**함의**: 특정 과제 특이 모델이 아니라 representation-level 원리를 제시. (Fig.6/7 p6)

---

## 5) Discussion — 한계와 다음 질문

### 저자가 실제로 세운 한계/주의점
- Loss function 가정에 따라 정량적 예측은 달라질 수 있음 (질적 패턴의 견고성은 유지).
- 신경생리 구현은 유일하지 않음: 여러 tuning family가 유사 Fisher profile을 만들 수 있음. (Fig.8 p8)

### 다음 질문 (follow-up)
1. 동일 피험자에서 noise source를 정교하게 분리 조작할 때, Fig.3형 상호작용이 얼마나 재현되는가?
2. 시간/수량/가치 판단처럼 다른 modality-domain으로 일반화되는가?
3. 개체별 priors + loss + encoding efficiency를 동시에 식별 가능한가?

---

## 한 줄 요약
이 논문은 “anti-Bayesian”을 Bayesian의 반례로 보지 않고, **효율코딩 제약을 포함한 Bayesian의 필연적 결과**로 재정의한다.

---

## 라벨링
- **Paper states**: 위 Fig/Methods 기반 진술
- **Interpretation**: “representation-level 원리” 일반화 문장
- **Speculation**: cross-domain/개체별 식별 확장 제안
