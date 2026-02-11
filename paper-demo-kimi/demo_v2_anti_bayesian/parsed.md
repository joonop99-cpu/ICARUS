# Paper Analysis: A Bayesian observer model constrained by efficient coding can explain 'anti-Bayesian' percepts

## Citation
Wei, X.-X., & Stocker, A. A. (2015). A Bayesian observer model constrained by efficient coding can explain 'anti-Bayesian' percepts. *Nature Neuroscience*, 18(10), 1509–1517. https://doi.org/10.1038/nn.4105

## Core Goal
Unify efficient coding (neural representation) with Bayesian inference (decoding) to create a fully constrained observer model that can explain seemingly "anti-Bayesian" perceptual biases—where perception is biased *away* from prior expectations rather than toward them.

## Central Hypothesis
When sensory encoding is efficient (optimized for natural stimulus statistics via Fisher information maximization), the resulting likelihood functions become asymmetric in stimulus space. This asymmetry causes Bayesian inference to produce biases *away* from high-probability stimulus values—even though decoding remains Bayes-optimal given the encoding.

Key insight: "Anti-Bayesian" percepts are actually Bayes-optimal given efficient encoding constraints.

## Method
- **Framework**: Encoding-decoding model with two stages:
  1. **Encoding**: Probabilistic sensory measurement m given stimulus θ, with Fisher information J(θ) ∝ p(θ)^2
  2. **Decoding**: Bayesian posterior inference with p(θ|m) ∝ p(m|θ)p(θ)
- **Efficient coding constraint**: Maximizes mutual information I[θ,m] under internal noise
- **Novel theoretical contribution**: Mapping to "sensory space" F(θ) = cumulative of p(θ), where noise is homogeneous
- **Test domains**: Visual orientation and spatial frequency (with known natural statistics)

## Key Metrics/Measures
- **Fisher information**: J(θ) = coding resources allocated to stimulus θ
- **Bias**: Systematic deviation of percept from true stimulus
- **Uncertainty modulation**: Comparison of external noise (stimulus degradation) vs. internal noise (coding limitations)
- **Natural stimulus distributions**: Measured statistics from natural images

## Main Results
1. **Asymmetric likelihoods**: Efficient encoding predicts likelihood functions with heavy tails *away* from prior peaks (Fig. 1c)
2. **Anti-Bayesian prediction confirmed**: Models predict biases away from cardinal orientations and low spatial frequencies (most common in natural scenes)
3. **Differential uncertainty effects** (unique prediction):
   - External noise → increased bias toward prior (attractive)
   - Internal noise → increased bias away from prior (repulsive)
   - This dissociation distinguishes model from standard Bayesian accounts
4. **Quantitative fit**: Model matches published psychophysical data on orientation and spatial frequency perception across multiple studies

## Cost-Control Note
Full paper processed (11 pages). Complete theoretical framework, all figures, and discussion captured in extraction.
