# Paper Analysis: A unifying theory explains seemingly contradictory biases in perceptual estimation

## Citation
Hahn, M., & Wei, X.-X. (2024). A unifying theory explains seemingly contradictory biases in perceptual estimation. *Nature Neuroscience*, 27, 793–804. https://doi.org/10.1038/s41593-024-01574-x

## Core Goal
Develop a mathematically unified framework explaining apparently contradictory perceptual biases (both attractive and repulsive) as arising from a single Bayesian principle, rather than from separate mechanisms.

## Central Hypothesis
Perceptual biases can be decomposed into three additive components:
1. **Prior attraction**: Pull toward stimulus values with high prior probability (traditional Bayesian prediction)
2. **Likelihood repulsion**: Push away from values with high encoding precision (Fisher information), due to asymmetric likelihood functions
3. **Range regression**: Regression toward the center of bounded stimulus range (boundary effects)

The theory yields a "simple and universal rule": The net bias direction depends on the relative strength of these three components.

## Method
- **Theoretical derivation**: Bayesian decision theory + efficient coding constraints
- **Model components**:
  - Prior distribution p(θ): observer's belief about stimulus frequency
  - Likelihood function p(m|θ): encoding uncertainty (constrained by Fisher information)
  - Loss function: determines how estimation errors are weighted
- **Key theoretical result**: Bias(θ) = Prior_Attraction(θ) + Likelihood_Repulsion(θ) + Range_Regression(θ)
- **Simulations**: Model predictions tested against published data on orientation, color, and magnitude perception

## Key Metrics/Measures
- **Perceptual bias**: Difference between true stimulus and reported percept (θ̂ − θ)
- **Fisher information J(θ)**: Encodes precision of neural representation (∝ p(θ)^α with α as resource allocation parameter)
- **Prior-likelihood interplay**: Determined by exponent α governing resource allocation

## Main Results
1. **Unified decomposition**: All three bias components naturally emerge from first principles without ad hoc assumptions
2. **Explains contradictory findings**:
   - Orientation: Repulsive biases away from cardinal (high-frequency) orientations
   - Color: Attractive biases toward prototype colors
   - Both arise from same model with different parameter regimes
3. **Boundary effects**: Regression bias becomes significant near stimulus range edges
4. **Loss function modulation**: Different loss exponents (p) shift relative contributions (p=2: MSE; p→∞: minimax)

## Cost-Control Note
Processed pages 1-15 (of 18). Core theoretical framework in first 10 pages; results section partially captured. Sufficient for understanding the model architecture and key predictions.
