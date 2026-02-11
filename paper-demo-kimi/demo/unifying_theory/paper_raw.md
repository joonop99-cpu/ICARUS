# A unifying theory explains seemingly contradictory biases in perceptual estimation__CUP2T59Q.pdf
# Source: /Users/joonoh/Desktop/OpenClaw_Library/papers/bayesian-models/A unifying theory explains seemingly contradictory biases in perceptual estimation__CUP2T59Q.pdf
# Pages extracted: 1-15 of 18


--- Page 1 ---
Nature Neuroscience | Volume 27 | April 2024 | 793–804
793
nature neuroscience
https://doi.org/10.1038/s41593-024-01574-x
Article
A unifying theory explains seemingly  
contradictory biases in perceptual  
estimation
Michael Hahn 
  1 
 & Xue-Xin Wei 
  2 
Perceptual biases are widely regarded as offering a window into the 
neural computations underlying perception. To understand these biases, 
previous work has proposed a number of conceptually different, and even 
seemingly contradictory, explanations, including attraction to a Bayesian 
prior, repulsion from the prior due to efficient coding and central tendency 
effects on a bounded range. We present a unifying Bayesian theory of biases 
in perceptual estimation derived from first principles. We demonstrate 
theoretically an additive decomposition of perceptual biases into attraction 
to a prior, repulsion away from regions with high encoding precision 
and regression away from the boundary. The results reveal a simple and 
universal rule for predicting the direction of perceptual biases. Our theory 
accounts for, and yields, new insights regarding biases in the perception of 
a variety of stimulus attributes, including orientation, color and magnitude. 
These results provide important constraints on the neural implementations 
of Bayesian computations.
Human perceptual decisions are often biased1,2. For instance, a slightly 
tilted vertical bar is often reported to be perceived as more tilted 
than it really is1. As key signatures of the underlying computational 
process, these biases are of broad interest to brain scientists, and 
have substantial societal3,4 and clinical implications5,6. Over the past 
decades, Bayesian inference has emerged as a main theoretical frame-
work for understanding perception and, more generally, cognition 
(sometimes referred to as the ‘Bayesian brain’ hypothesis)7,8. The 
key tenet is that human perception and cognition reflect an optimal 
combination of uncertain sensory input with prior expectations 
according to Bayes’ rule.
Previous studies have proposed several ingredients that may influ-
ence the bias of perceptual judgment. The first idea is that perception 
is biased toward prior expectations9,10. In the Bayesian view, this can be 
formalized as a bias toward the peak of a prior distribution, for example, 
the ‘slow speed prior’ in motion10,11, ‘light from above prior’ in shape 
perception12,13 and categorical priors in explaining biases in spatial 
perception14. A second idea is regression toward the mean: when the 
range of the stimulus is limited, the reported stimulus will be biased 
toward the center of the range2,15. Third, recent work16,17 has considered 
Bayesian models based on efficient neural codes, where stimuli that 
are more frequent in the environment are encoded with higher preci-
sion18–20. Counterintuitively, such models predict biases away from the 
more frequent stimuli16,17 (that is, repulsive biases), primarily because 
the likelihood function is asymmetric, with a heavy tail away from the 
prior. This idea explains why orientation perception exhibits biases 
toward oblique directions21,22 even though these are least frequent 
in natural scene statistics23,24. Fourth, the bias predicted by Bayesian 
models may depend on how strongly observers are assumed to weigh 
smaller and larger estimation errors in making a perceptual decision, 
that is, the loss function15,17,25.
We lack a good understanding of how these disparate ingredients 
together determine perceptual biases, for example, when should one 
expect biases toward or away from prior expectations? This makes it 
Received: 13 April 2023
Accepted: 8 January 2024
Published online: 15 February 2024
 Check for updates
1Saarland University, Saarbrücken, Germany. 2Department of Neuroscience, Department of Psychology, Center for Perceptual Systems,  
Center for Learning and Memory, Center for Theoretical and Computational Neuroscience, The University of Texas at Austin, Austin, TX, USA. 
 e-mail: mhahn@lst.uni-saarland.de; weixx@utexas.edu


--- Page 2 ---
Nature Neuroscience | Volume 27 | April 2024 | 793–804
794
Article
https://doi.org/10.1038/s41593-024-01574-x
(a.u.)
c
p = 0
2
4
6
Likelihood repulsion
Bias
Prior attraction
(a.u.)
(a.u.)
0.4
(deg)
(deg)
(deg)
Bias
10
–10
0
10
–10
0
10
–10
0
10
–10
0
10
–10
0
10
–10
0
+
d
Inference
Representation
Likelihood
Prior
Stimulus
Prior
Resources
Resources
Resources
Resources
Resources
Resources
Resources
Model components
Posterior
Percept
Loss function
Exponent
Resources
Examples
Loss
1. Prior
    attraction
4. Loss functions
5. Sensory 
noise
6. Stimulus
noise
High
Low
High
Low
High exponent (p = 8)
Low exponent (p = 2)
Decomposition of the bias
Repulsion
–180
–180
–180
–180
180
180
180
180
90
180
90
90
0
0
0
0
20
40
180
180
180
180
90
180
90
90
0
0
0
2. Likelihood  
3. Scalar
i
h
g
f
e
0
0
0
0.2
0.5
0
0.4
0
0.5
0
0.2
0
20
40
Total bias
Attraction
Loss
function
Prior
Likelihood
Posterior
 p = 0,   2,   4,   6
a
0
Probability
Probability
Probability
Probability
Probability
Probability
Stimulus
Stimulus
Stimulus
Stimulus
Stimulus
Encoding
b
0
0
0
=
repulsion
σ
F (θ)
F’ (θ)
J (θ)
θ
θ
σ
m
θ
θ
θ
θ
θ
θ
θ
θ
Fig. 1 | Overall theoretical framework. a, The Bayesian observer model is 
specified by the prior, the allocation of coding resources and the loss function. 
Observations are encoded by a nonlinear map, an abstraction of the neural 
representation and subject to neural (sensory) noise. Resource allocation is 
described by the slope of the encoding function. Via Bayesian inference, an 
estimate is generated as the minimizer of a loss function under the posterior. 
b,c, The bias of the estimate consists of two components. When the prior 
(orange) is nonuniform around a stimulus, the posterior (green) is shifted 
toward regions of high prior density compared with the likelihood (gray); the 
estimate (blue) is correspondingly drawn toward the peak of the prior (b). 
When the encoding precision is nonuniform around a stimulus, the width of 
the likelihood will vary across stimuli, with broader likelihoods in regions of 
lower encoding precision (c). In this case, the posterior becomes asymmetric, 
with a heavier tail in those regions. On average across trials, the estimate is 
correspondingly drawn toward those regions. A higher exponent in the loss 
function (here, exponent p = 2, 4, 6) leads to higher tolerance of small errors and 
lower tolerance of large errors, and increases this repulsive bias. d–i, Examples 
(p = 2, unless otherwise indicated). d, When the encoding is uniform, biases 
point toward the prior’s peak. Resources are quantified as the square root of the 
Fisher information throughout the paper. e, When the encoding is nonuniform, 
biases point toward regions with low encoding precision. f, A scalar variable 
obeying Weber’s law, with a log-normal prior; attraction and repulsion combine. 
g, In circular stimuli, both the prior and the encoding may be periodic due to 
efficient coding for natural scene statistics (g)17,28. Biases will point toward 
oblique directions when the encoding varies steeply, and toward the cardinals 
when it varies less. The attractive component is independent of the loss function 
exponent p, whereas the repulsive component increases with the exponent 
(g). h,i, Role of noise (p = 8, see Supplementary Fig. 5 for other exponents): 
increasing sensory noise (h) increases both attraction and repulsion. In contrast, 
stimulus noise (i) increases attraction, but decreases repulsion.


--- Page 3 ---
Nature Neuroscience | Volume 27 | April 2024 | 793–804
795
Article
https://doi.org/10.1038/s41593-024-01574-x
challenging to interpret many previous results and understand the 
neural processes that implement perceptual inferences. Here, we 
develop a theory that unifies all the aforementioned phenomena. Our 
analytical results provide an additive decomposition of perceptual 
biases under a large class of loss functions, and arbitrary combinations 
of encoding models and decoding priors. The theory leads to a simple 
yet widely applicable rule for judging the direction of perceptual biases. 
This theory not only correctly accounts for prominent perceptual bias 
patterns reported in experimental data, but also provides a unified 
understanding of seemingly contradictory perceptual biases.
Results
Bias of Bayesian observer with arbitrary prior and encoding
We first describe a general Bayesian observer model (Fig. 1a) that allows 
arbitrary combinations of prior and encoding. Consider the encoding 
of a one-dimensional variable θ in a population of neurons. The neu-
rons’ sensitivity to θ is captured by their tuning curves. The fidelity 
of the population code as a whole can be characterized by the Fisher 
information, which captures how rapidly the population activity pat-
tern changes for a small change around a given value of θ relative to the 
neural noise. To abstract from the many neurons and their potentially 
complicated noise, we can describe the population code at an abstract 
level by assuming an encoding by a single variable m = F(θ) affected by 
Gaussian noise17,19,26,27:
m = F(θ) + δ,
(1)
where δ is Gaussian noise representing sensory noise, and F(θ) is a con-
tinuous one-to-one mapping between the stimulus space and a 
one-dimensional sensory space. There are potentially many ways to 
implement a particular function F(θ) in a set of tuned neurons. F(θ) 
provides a useful abstraction capturing how much of the limited neu-
ral resources are allocated to different portions along the domain of 
θ: when F changes more quickly around a stimulus θ, more resources 
are allocated to stimuli around θ. Formally, this is described by the 
Fisher information, which is proportional to the square of the slope of 
F: J(θ) = F′(θ)
2/σ2 , where σ2 is the sensory noise variance. When F is 
proportional to the cumulative distribution of the prior, the system 
allocates the coding resources according to the principle of informa-
tion maximization in the small noise regime18,20—a special case that 
was addressed in refs. 17,28. This model also subsumes models involv-
ing domain-specific encodings, such as logarithmic encodings of mag-
nitude29 and log-odds encodings of probabilities30.
Given a sensory measurement m, one can combine the prior dis-
tribution pprior(θ) with the likelihood function p(m∣θ) via Bayes’ rule to 
obtain a posterior distribution p(θ∣m). Bayesian decision theory pro-
vides a normative recipe for deriving a point estimate, by selecting the 
stimulus ̂θ that minimizes the posterior expectation of a given loss 
function (equation (5); Methods). We consider the general family of Lp 
loss functions, that is, losses obtained by raising the absolute error to 
some power p. Intuitively, higher exponents lead to loss functions that 
are more tolerant of small errors, and less tolerant of large errors. In 
particular, p = 1 corresponds to the posterior median and p = 2 results 
in the posterior mean. The limit p → 0 leads to the posterior mode 
(maximum a posteriori (MAP) estimator). One quantity we are particu-
larly interested in is the bias of the estimate, which is the average dif-
ference between the derived estimate and the true stimulus.
Additive decomposition of estimation biases. We derive analytically 
the biases that correspond to different combinations of prior, encoding 
and loss function. Our result shows that the biases can be decomposed 
additively into terms arising from the nonuniformity of the prior and 
the heterogeneity of the encoding. More precisely, for the model 
defined in equation (1), the bias of the optimal Bayesian estimate ̂θ 
under Lp loss (p ≥ 1 an integer) can be written as:
1
J(θ) (log pprior(θ))
′
⏟⎵⎵⎵⎵⎵⏟⎵⎵⎵⎵⎵⏟
Prior attraction
+ p + 2
4
( 1
J(θ))
′
⏟⎵⎵⎵⏟⎵⎵⎵⏟
Likelihood repulsion
;
(2)
and, for the MAP estimator
1
J(θ)(log pprior(θ))
′ + 1
4( 1
J(θ))
′
,
(3)
where J(θ) denotes the Fisher information, and the derivatives were 
taken with respect to the stimulus variable θ. This result demonstrates 
that the Bayesian optimal decision is systematically biased, with the 
bias depending on the forms of the prior, likelihood and loss function. 
These analytical results hold when noise is small (an assumption also 
made by, for example, refs. 11,17,31). Numerical simulations show that 
qualitative patterns remain valid for larger noise (Supplementary 
Fig. 4); however, biases grow more slowly as noise increases, because 
high noise smooths out local variability in prior and encoding precision.
Our results provide a general expression for the bias of the Bayes-
ian optimal estimate under arbitrary combinations of prior distri-
bution, resource allocation and loss function. The first term in the 
equations describes attraction to the prior: the bias is proportional 
to the slope of the logarithmic prior and increased in regions with low 
encoding precision. The second term describes a repulsive bias away 
from regions of high encoding precision, scaling with a factor depend-
ing on the loss function. This additive decomposition into attractive 
and repulsive components clarifies how prior and likelihood repulsion 
(induced by encoding heterogeneity) jointly determine perceptual 
biases. Notably, likelihood repulsion scales with the exponent of the 
loss function, so that repulsive biases increase when the loss function 
is tolerant of small errors, whereas prior attraction is largely independ-
ent of the loss function.
The theory is illustrated using representative examples in Fig. 1d–i. 
Traditional Bayesian models assume a nonuniform prior and a uniform 
encoding (Fig. 1d); this gives rise to attraction toward the prior peak. 
When, on the other hand, the prior is uniform but the encoding preci-
sion is not uniform, a repulsive bias away from regions of high precision 
is predicted32 (Fig. 1e). Figure 1f considers the case of a scalar variable 
whose encoding follows Weber’s law, and is subject to a unimodal prior. 
Here, the bias points toward the prior peak, with strength varying with 
the stimulus.
Previous results as special cases. Special cases of equations (2) and (3) 
recover various previous analytical results (Supplementary Information, 
section 3.1.2). In the special cases p = 0 and p = 2, we recover results from 
refs. 11,31. Some previous work has considered coding models where 
the Fisher information matches the square17 or another power31,33 of 
the prior, which can be justified in terms of efficient coding18,19,34. In this 
setting, our results lead to a general description of the bias in terms of 
the power q linking prior and encoding, not previously known beyond 
the special cases q = 2 (ref. 28) or p = 2 (refs. 31,35). Recent work found 
that, in a broad range of experiments, the discrimination threshold 
and perceptual bias follow a lawful relationship such that the bias 
is proportional to the slope of the squared threshold, which can be 
accounted for by Bayesian inference based on efficient coding28. This 
perceptual law can be derived under a more general condition, that is, 
when the Fisher information is proportional to a power function of the 
prior33. Our results further show that such a proportionality is both a 
sufficient and necessary condition for deriving the perceptual law in 
the Bayesian framework (Supplementary Section 3.1.2).
Simple rule for judging the direction of perceptual biases
Our theory leads to a simple rule to predict the direction of the bias (Fig. 2). 
Likelihood repulsion and prior attraction at a particular stimulus reflect 


--- Page 4 ---
Nature Neuroscience | Volume 27 | April 2024 | 793–804
796
Article
https://doi.org/10.1038/s41593-024-01574-x
how quickly encoding precision and prior density, respectively, vary 
around that stimulus. Thus, one should expect that whichever of the 
two varies more rapidly becomes the main determinant of the overall 
bias: repulsion dominates when encoding precision varies rapidly, and 
attraction dominates when the prior density varies rapidly. Indeed, we 
find that, when noise is small, the bias for a given Lp(p > 0) loss function 
is predicted to have the same sign as:
Q(θ) = (
pprior(θ)
J(θ)
p+2
4
)
′
.
(4)
A similar functional form holds at p = 0 (Methods). As the quantity in 
the denominator quantifies the encoding precision for each stimulus, 
we refer to this as the prior/precision ratio rule, or P/P ratio rule for 
simplicity. Consider the case where the Bayesian estimate is taken to 
be the posterior mean (L2 loss). In this case, the ratio rule can be written 
as Q(θ) = (
pprior(θ)
J(θ)
)
′
. Assuming the neural code maximizes mutual 
information, previous work17,19,34,36 found pprior(θ) ∝√J(θ); thus, the bias 
has the same sign as (
1
pprior(θ))
′
, precisely the opposite of the direction 
of the prior belief. Thus, a repulsive bias is predicted in Bayesian 
observers constructed based on neural representations that maximize 
the information17,20. Furthermore, the ratio rule also clarifies the direc-
tion of biases in efficient coding frameworks based on the optimization 
of other objective functions (Supplementary Section 3.1.2).
The ratio rule formalizes precisely the idea that the direction of 
the perceptual bias depends on how fast the prior distribution and the 
encoding precision change relative to each other (Fig. 2). This ratio 
rule provides a new insight that may reconcile a range of previous 
experimental observations: one plausible explanation of seemingly 
contradicting observations of either attractive or repulsive biases is 
that the balance between the prior and precision may differ across 
different experimental scenarios—a hypothesis we will test later with 
experimental data.
Extensions of the theory
Stimulus boundary induces biases toward the interior. The results so 
far apply to stimuli in the interior of the stimulus space, away from any 
boundary. Intuitively, even with a uniform prior and uniform encoding 
on a bounded range, the minimization of errors may lead to a systematic 
bias toward the interior. Effects of the boundary may become important 
in experiments that measure the perceptual biases using a relatively 
small bounded range37 or ratings on a bounded scale27. We consider 
two ways to model the effect of boundaries, and will compare these two 
schemes quantitatively using experimental data. First, boundaries may 
lead to a truncation of the prior15. We analytically derived the impact 
of the boundary on the bias in this case (see Theorem 3 in Methods). 
In the vicinity of the boundary, biases are dominated by a regression 
effect into the interior of the range; this effect disappears as one moves 
into the interior. Alternatively, when stimuli are limited to an interval 
within a larger stimulus space, subjects might also develop a smoothly 
changing prior, such as a Gaussian prior, as an approximation to the 
sharply dropping prior at the edge (Fig. 1f). For this case, the predicted 
bias is readily accounted for by equations (2) and (3).
Stimulus noise modulates estimation biases. Different sources of 
noise may have different impacts on perception17. The model described 
in equation (1) captures the sensory noise in neural processing (for 
example, limited number of spikes), also referred to as internal noise or 
neural noise. Experimentally, this type of noise is often manipulated by 
varying variables such as exposure duration or contrast. Using stimuli 
with higher contrast or longer duration increases the total number 
of spikes, thus effectively reducing the magnitude of sensory noise. 
In contrast, other experiments (for example, refs. 24,38,39) present 
an array of copies of a stimulus (for example, oriented Gabor), where 
each copy has some amount of noise applied to it, and ask subjects to 
estimate the mean value of the copies in the array. This kind of experi-
mental manipulation injects noise to the stimulus variable before 
neural encoding, and is thus referred to as stimulus noise, or external 
noise. This type of noise is formally modeled as affecting θ before apply-
ing the transform F representing the neural encoding17. Experimental 
work has shown that this latter, stimulus (external) noise also influences 
perceptual biases24,38,39. For instance, in perception of orientation, 
adding Gaussian stimulus noise in stimulus arrays biases responses 
toward the cardinal orientation24,38, whereas sensory noise biases 
responses away from them22. To understand these results, we extended 
the theory to address stimulus noise (see Theorem 2 in Methods). Our 
theory generalizes simulation results in Wei and Stocker17, and provides 
a precise analytical characterization of how stimulus noise affects the 
perceptual biases and how its effect differs from that of sensory noise 
(Fig. 1h–i). When adding stimulus noise, the representation becomes 
noisier, and reliance on the prior increases. Thus, prior attraction 
increases with both sensory and stimulus noise. Simultaneously, and 
more subtly, stimulus noise reduces likelihood repulsion when p > 2, 
because it broadens the posterior and reduces its asymmetry. Thus, the 
theory predicts that, in settings where prior and encoding are aligned, 
increasing sensory noise makes biases more repulsive, while stimulus 
noise makes biases more attractive.
–
Fast-changing prior
Fast-changing encoding
Prior
Probability
Resources
Bias
Bias
Bias
Bias
Resources
Probability
Attraction
Repulsion
Bias
P/P ratio
a
b
Q function
50
20
(deg)
Bias
0
Bias
Ratio
Ratio
+
–
+
0
–
Bias
Bias
+
–
+
+
–
+
–
Resources
0
90
180
Orientation (deg)
0
90
180
Orientation (deg)
0
90
180
Orientation (deg)
0
90
180
Orientation (deg)
0
90
180
Orientation (deg)
0
90
180
Orientation (deg)
0
90
180
Orientation (deg)
90
180
0
90
180
0
90
180
0
90
180
0
90
180
0
90
180
0
90
180
Orientation (deg)
Orientation (deg)
Orientation (deg)
Orientation (deg)
Orientation (deg)
Orientation (deg)
Orientation (deg)
0
0
0
0
0
0
0
0
0
Fig. 2 | Illustration of the P/P ratio rule. a,b, The P/P ratio rule determines 
the direction of the overall bias, when the prior (a) or the resource allocation 
(b) changes more quickly over the stimulus space. In addition to the model 
components and the bias components (p = 2), we plot the ratio between prior 
and Fisher information, and its derivative Q(θ) (equation (4)). As predicted by 
our theory, Q(θ) predicts the direction of the bias: attraction dominates when 
the prior changes faster than the encoding (a), repulsion dominates when the 
resource allocation changes faster (b).


--- Page 5 ---
Nature Neuroscience | Volume 27 | April 2024 | 793–804
797
Article
https://doi.org/10.1038/s41593-024-01574-x
Applications to experimental data
We applied our model to a number of datasets collected in previous 
experiments22,37,38,40–42, ranging from color and orientation perception 
to the estimation of numerosity. To fit our general Bayesian model to 
the data, we developed a general numerical fitting procedure determin-
ing the model components, including prior, encoding and noise 
magnitude, by maximizing the likelihood of trial-by-trial response 
data. Hence, the model is fitted to account for the full response distri-
bution conditioned on the stimulus. We parameterized the resource 
allocation √J(θ) and the prior pprior(θ) by representing the stimulus 
space as a discretized grid of points, and specifying values on each 
point on the grid (details are described in Methods).
Eﬀect of sensory noise
Eﬀect of loss function
Eﬀect of stimulus noise
p = 2
p = 4
p = 6
p = 8
Variability (data)
Low stimulus noise
s.d.
s.d.
Uniform 
prior
Naturalistic
prior
Uniform 
prior
180
(deg)
90
Naturalistic
prior
(deg)
40 ms
80 ms
160 ms
1 s
Presentation time:
f
g
h
(deg)
a
b
c
d
e
Orientation (deg)
Orientation (deg)
Orientation (deg)
Orientation (deg)
Orientation (deg)
Orientation (deg)
Orientation (deg)
(deg
–1)
Prior
Orientation (deg)
Orientation (deg)
Orientation (deg)
Resources
Attraction
Repulsion
Bias (model)
High stimulus noise
–40
Bias
Resources
Resources
Bias
Bias
Bias
Bias
Bias
0 +40
–40 0 +40 (deg)
Bias (data)
Bias (model)
Repulsion
Attraction
Resources
Prior
Probability
Probability
0
0
0
0.2
0
0
0.2
0
4
–4
0
4
–4
Probability
Bias
Bias
Bias
Bias
Bias
Bias
Bias
Probability
Resources
Resources
40
0
180
90
Orientation (deg)
Orientation (deg)
Orientation (deg)
Orientation (deg)
Orientation (deg)
Orientation (deg)
Orientation (deg)
Orientation (deg)
Orientation (deg)
Orientation (deg)
Orientation (deg)
Orientation (deg)
Orientation (deg)
Orientation (deg)
Orientation (deg)
Orientation (deg)
0
180
90
0
0
0
0
4
–4
0
0.2
0.4
0
0.2
0.4
0
–20
20
0
–20
20
0
–20
20
Bias (data)
Orientation (deg)
Bias
Fig. 3 | Bias and variability in orientation estimation. a–c, Bias in 
orientation perception (data collected by ref. 22) (a), with naturalistic (b) or 
uniform (c) prior. The naturalistic prior is based on natural image statistics, 
p(θ) ∝ 2 − ∣sin(θ)∣ (ref. 17,24). We show results for the best-fitting exponent, 
p = 8. The bias is dominated by likelihood repulsion. Decreased exposure 
times correspond to increased sensory noise, leading to increased biases. 
The prior plays a small role; a uniform prior achieves approximately optimal 
fit (Supplementary Fig. 14). d,e, While most loss functions can reproduce 
the bias (Supplementary Fig. 18), small values of p exhibit poor fit to the 
observed variability. The data (e) are best accounted for using a loss function 
that is tolerant of small nonzero errors (for example, p = 8). f–h, Effect of 
increasing stimulus noise (data collected by ref. 38). In this experiment, 
Gabor patches were presented in arrays, with the orientation of each patch 
sampled from a narrow or wide Gaussian distribution around a given stimulus 
value θ, resulting in the low (green) or high (red) stimulus noise condition, 
respectively. Schematic sample stimuli are drawn based on38; contrast is 
adapted for visibility. f, The human data exhibit a decreased bias when 
increasing stimulus noise. We fitted the model both with the prior based on 
natural image statistics (g) and a uniform prior (h), again at p = 8. In agreement 
with our theory, in the data (f), higher stimulus noise (red) decreases repulsion 
and increases attraction, leading to an overall decrease in bias magnitude.  
For the human data in a and e, means and bootstrapped 95% confidence bands 
were plotted. In f, means and bootstrapped 95% confidence intervals over 
n = 120 trials at each stimulus value and condition were plotted.


--- Page 6 ---
Nature Neuroscience | Volume 27 | April 2024 | 793–804
798
Article
https://doi.org/10.1038/s41593-024-01574-x
Application 1: orientation estimation. Perception of orientation is 
generally biased, with some studies finding biases toward cardinal 
orientations24, while others reported systematic biases away from 
them21,22,38,43. Bayesian models have been applied to understand these 
observations17,24,38. In particular, Bayesian models based on efficient 
coding can qualitatively reconcile these contradictory findings17. How-
ever, it remains unclear whether this type of model can quantitatively 
explain the data and, if so, how important each model component is.
We start by reanalyzing the data from ref. 22. In this experiment, 
sensory noise was manipulated (via varying the length of stimulus 
presentation time) while observers were asked to reproduce the ori-
entation of individual Gabor stimuli. Presupposing a well-established 
orientation prior based on natural image statistics17,24,38, we fitted our 
model (defined by equation (1)) to these data (Fig. 3a–c). The fitted 
model exhibits decreased coding precision around the oblique orien-
tations, in agreement with the long-standing experimental finding of 
decreased discriminability close to the oblique orientations, that is, 
oblique effects44. As predicted by our theory, the measured biases point 
away from cardinal directions, and increase for shorter presentation 
times; that is, with increased sensory noise. Meanwhile, Tomassini 
et al.38 and Girshick et al.24 measured biases in orientation perception 
at two levels of stimulus noise applied to arrays of Gabor patches. 
Their results are consistent with the interpretation that the repulsion 
away from cardinal orientations is reduced with larger stimulus noise. 
This pattern is as well predicted by our theory (model fits in Fig. 3f–h).
By directly fitting to trial-by-trial data, these results reveal two 
new insights going beyond previous qualitative models of orienta-
tion perception17. First, the inferred loss function exhibits a higher 
exponent (p = 8) than previously assumed. Estimators with lower 
exponents as assumed in previous work17,24 provide poor fit (Fig. 3d); 
an observation recently also made by ref. 45. Our modeling thus indi-
cates that, in these orientation estimation tasks, human observers are 
much less sensitive to small errors than previously thought. Second, 
the encoding heterogeneity plays an important role in accounting for 
both the repulsion away from the cardinal orientations, and the reduc-
tion of this repulsion when adding stimulus noise. When only sensory 
noise is present, inhomogeneity in encoding leads to an asymmetric 
posterior (Fig. 1c), accounting for the repulsive biases. With increas-
ing stimulus noise, our theory predicts both a reduction of likelihood 
repulsion and an increase of prior attraction (Fig. 1i), pulling responses 
toward the cardinals. Strikingly, in both datasets22,38, a model with a 
uniform prior and appropriate encoding and loss functions achieves 
at least as strong a model fit, and freely fitting a prior indeed leads 
to an approximately uniform fit (Supplementary Figs. 15 and 26). 
These results highlight the importance of loss function and encoding 
heterogeneity in orientation perception.
Cardinal
Intermediate
Oblique
Cardinal
Oblique
Intermediate
a
0.2
0
0
90
180
270
360
Summary
Recovered resources across observers
b
c
d
e
(deg)
(deg
–1)
Prior
(deg)
Probability
Resources
Resources
Resources
Resources
Resources
(deg–1)
Probability
Probability
Probability
Bias (deg)
Bias
Bias
Bias
0.2
0
0.2
0
0.2
0
0.2
0
0
0
0
0
90
180
0
90
180
0
90
180
0
90
180
0
90
180
0
90
180
0
90
180
0
0
5
–5
90
180
0
90
180
0
90
180
0
5
–5
0
5
–5
0
5
–5
Resources
Direction
Attraction
Repulsion
Total bias
Fig. 4 | Modeling the effect of perceptual learning on motion perception. 
a–e, Gekas et al.42 exposed 36 subjects to moving point clouds, whose movement 
directions were sampled from a bimodal distribution centered at different angles 
for different subjects. Sample stimuli are schematic; contrast is increased here 
for visibility. We fitted our model with per-subject adjustments to encoding 
and prior. a, Across subjects, a resource allocation peaking at cardinal angles is 
identified. Dots indicate the central directions for each of the subjects, colored 
depending on whether they are close to the cardinal or oblique directions, or 
in between. Here and in b–d, faint gray curves indicate results for individual 
subjects, with per-subject adjustments both for the transfer function F and for 
the magnitude of sensory noise. The solid curve indicates the average across 
subjects. b–d, We separately consider subjects based on the three-way grouping 
from a, with distributions centered close to cardinal directions (b), centered 
at intermediate directions (c) and centered close to oblique directions (d). 
To compare biases across subjects, we transformed the coordinates for each 
subject so that the central direction was in (90°, 135°). We show results fitted for 
each subject (faint) and averaged (solid). The fitted resource allocation reflects 
increased coding precision at cardinal directions; the fitted prior (solid) roughly 
reflects the bimodal stimulus distribution (dashed). Measured biases (dashed, 
mean; error band, s.e.m. over subjects; solid, model) reflect the impact of both 
encoding inhomogeneity and subject-specific priors. The two components 
reinforce each other for subjects in the cardinal group, while biases are reduced 
in the oblique group. e, Idealized pattern across the three groups of subjects. 
Resources and likelihood repulsion are approximately the same across subjects. 
Different priors give rise to different prior attraction biases; the overall bias is 
reinforced for the cardinal group and reduced for the oblique group.


--- Page 7 ---
Nature Neuroscience | Volume 27 | April 2024 | 793–804
799
Article
https://doi.org/10.1038/s41593-024-01574-x
Application 2: perceptual learning of motion direction. In Appli-
cation 1, the experimental stimulus distribution was uniform across 
stimuli and subjects, and the observed biases could be explained 
largely by the likelihood repulsion. Our theory predicts that a nonu-
niform prior would result in a second bias component (prior attrac-
tion) being added to the repulsive bias. To test this, we analyzed data 
from a perceptual learning task in motion perception42,46. Similar to 
orientation, motion perception exhibits decreased discriminability 
around the oblique directions47 and biases toward these, away from 
the cardinal directions48. Studies have used perceptual learning para-
digms to study how motion perception may adapt to the statistics of 
motion stimuli42,46. In these studies, subjects were asked to estimate 
the motion direction of a coherently moving point cloud. On each trial, 
the movement direction was drawn from a bimodal distribution whose 
peaks were separated by 64 degrees around a central direction that 
was chosen randomly for each subject. To determine whether the per-
ceptual learning-induced effects could be explained by our theory, we 
reanalyzed data collected by Gekas et al.42. Assuming, first, the oblique 
effect in encoding precision and, second, that the subjects learned the 
bimodal stimulus distribution, our theory predicts that biases will 
combine repulsion (away from the cardinal directions) and attraction 
(toward the short-term motion prior). We note that the pattern of bias 
and variability reported in ref. 42 was quite complex, and the Bayesian 
models considered in ref. 42, which assumed homogeneous encoding, 
matched the observed pattern only imperfectly. We hypothesize that 
by considering both encoding heterogeneity and short-term prior, a 
clearer explanation would emerge.
Because the experimentally induced stimulus distribution var-
ies between the subjects in this experiment, we fitted a mixed-effects 
version of our model that includes subject-specific adjustments to 
encoding and prior (Methods). Overall, the results provide strong 
support for our prediction. For subjects where the stimulus distri-
bution was centered close to a cardinal direction, prior attraction 
and likelihood repulsion consistently pointed in the same direction, 
leading to a large bias (Fig. 4b). For subjects where the distribution of 
motion direction was centered close to the oblique, the components 
partially pointed in opposite directions and the magnitude of the bias 
was reduced (Fig. 4d). The recovered resource allocation is comparable 
Numerosity perception
Time interval estimation
Exposure duration:
Solid: 100 ms
Dotted: 2,000 ms
Bias (data)
Repulsion
Attraction
Resources
Priors
Number
Number
Number
Number
Number
Number
Number
Length
Length
Length
Length
Length
Length
Length
Length
Length
Length
Length
Length
Number
Number
Number
Number
Number
c
0
0
0
0
0
0
0
5
0
5
25
50
25
50
0
25
50
0
25
50
0
25
50
0
0
10
25
50
Probability
Resources
Resources
Resources
Resources
Bias
Bias
s.d.
Bias
Bias
Bias
Bias
Bias
Bias
s.d.
Probability
Unimodal
prior
Flat
prior
Variability
(data)
Variability
(data)
Variability
(model)
Bias (model)
Bias (data)
Bias (model)
Variability
(model)
Unimodal
prior
Flat
prior
0
10
0
10
0
–10
–10
–10
0
–0.1
0.1
0
0.08
(s)
(s)
Repulsion
Attraction
Resources
Prior
0
Bias
0.1
–0.1
0
0.1
–0.1
Bias
Bias
Bias
Bias
Bias
0
Probability
0
Probability
0
s.d.
s.d.
s.d.
0.1
0
s.d.
0.1
0.5
1.0
0.5
1.0
0.5
1.0
0.5
1.0
0.5
1.0
0.5
1
0
10
(s
–1)
(s)
0
10
d
g
h
e
f
a
b
Fig. 5 | Modeling central tendency effect in numerosity perception and time 
interval estimation. a,b, Xiang et al.41 exposed subjects to point clouds with 
varying numbers of points, within a range that varied between blocks. We plot 
the measured bias (a) and variability (b) for 3 of the 21 ranges considered. c,d, We 
show fits for the same 3 ranges (Supplementary Figs. 36–38 for the other ranges), 
either with a unimodal prior that is Gaussian in sensory space (c), or a flat prior 
reflecting the true stimulus statistics (d), as assumed in some prior models15,37. 
We show fits at p = 0, results at other exponents are similar (Supplementary 
Figs. 36–38). In each range, biases toward the center of the range are observed. 
Increasing exposure duration (dotted) decreases sensory noise and hence 
biases. The central tendency effect is accounted for by prior attraction under 
the unimodal prior, and by boundary effects under the flat prior. A flat prior 
incorrectly predicts the variability to peak in the center. e–h, Remington et al.37 
asked subjects to reproduce the time interval between two flashes on a screen. 
Stimuli were uniformly distributed within the interval indicated by the orange 
bar. We show measured bias (e) and variability (f). We show fits at p = 0 with 
unimodal prior (g) and with flat prior (h); results at other exponents are similar 
(Supplementary Figs. 40–43). As in a–d, a flat prior incorrectly predicts the 
variability to peak in the center. Freely fitting the prior leads to a similar unimodal 
fit (Supplementary Fig. 43). For the human data in a, b, e and f, we plot the mean 
with error bands indicating bootstrapped 95% confidence intervals.


--- Page 8 ---
Nature Neuroscience | Volume 27 | April 2024 | 793–804
800
Article
https://doi.org/10.1038/s41593-024-01574-x
among subjects who were presented with different motion statistics 
during the task, consistently peaking at cardinal directions (Fig. 4a). 
In contrast, the recovered priors differ systematically and reflect the 
experimentally defined motion statistics (Supplementary Fig. 31). 
Quantitative model fit strongly improved over a model assuming a 
uniform encoding (as assumed by refs. 42,46, difference in held-out 
negative log-likelihood: >50). Putting together, these results show 
that (1) both encoding heterogeneity and short-term priors in this 
perceptual learning task are important for understanding the reported 
errors in motion direction; (2) learning short-term statistics leads to a 
substantial change in the subject’s prior, but less so in their encoding.
Application 3: regression toward the mean in perception. In Appli-
cation 2, prior and encoding both played a substantial role in shaping 
biases, as both varied on a comparable scale. Our theory, specifically 
the P/P ratio rule, predicts that the role of the prior should become 
dominant when the prior varies much more quickly than the encod-
ing precision. We test this prediction using experimental data where 
the stimulus range was constrained to a small range within which the 
encoding precision did not vary much. Here, the P/P ratio rule predicts 
a dominant role for the prior supported within the range. Indeed, 
it is well known that such experiments produce a central tendency 
effect: humans exposed to magnitudes from a bounded range pro-
duce estimates biased toward the center of the range2,49. Recent stud-
ies also found that sensory noise39,50 and stimulus noise39 increase 
the regression effect. Bayesian models15,29,41 have been proposed to 
account for these effects. Our unified framework allows us to adjudicate 
between different hypotheses on the prior distribution used by human 
observers: to model a limited stimulus range, some models proposed 
a flat prior supported on the relevant range15, while others assumed a 
smoothly varying prior that peaks in the interval29,51. Which prior better 
accounts for the data remains unclear. In addition, these kinds of tasks 
prominently exhibit a scaling law (variability increases with the mean 
or, equivalently, a constant Weber fraction), raising the question of how 
much the encoding heterogeneity contributes to the reported biases.
To dissect these factors, we first fit the data collected by Xiang 
et al.41 using our framework. In this task, 300 subjects estimated the 
number of dots on a screen; within each block, dots were distributed 
uniformly in a range of width 30. In model fitting, we constrained the 
encoding precision to be consistent with Weber’s Law. Comparing 
models based on two different priors considered in previous studies 
(flat as in ref. 15, normal in sensory space as in ref. 29), the latter gives 
a much better fit (Fig. 5) than a flat prior. As the encoding satisfies 
Weber’s law, the theory also correctly predicts that the central tendency 
effect is larger for blocks with larger mean numerosity, as observed in 
ref. 41. Examining the fitted models (Fig. 5), we find that the encoding 
heterogeneity leads to a systematic bias toward larger magnitudes, yet 
most of the bias is accounted for by prior attraction. This is expected 
from the theory, because the prior on this bounded range varies much 
faster than the encoding precision.
We replicated these analyses using data from a time interval esti-
mation task37, obtaining similar results (Fig. 5e–h and Supplementary 
Figs. 40 and 42). While previous modeling of time interval estimation15 
had considered a flat prior and the squared loss (p = 2), we again found 
that a unimodal prior led to better fit than the flat prior, and that the 
resulting model fit did not vary much with the exponent (Supplemen-
tary Fig. 39). When freely fitting the prior, we recovered a unimodal 
shape across exponents (Supplementary Fig. 43).
Arbitrary prior
and encoding
Uniform prior
Uniform encoding
a
b
c
Dotted: data
Solid: prediction
(deg
–1)
(deg
–1)
Prior
d
Prior
Bounded range
130
140
150
Delay:
Stimulus noise: Low Low High
2 s
4 s
2 s
120
0
140
180
0
0
0
0.1
0.2
360
(deg)
(deg)
Probability
Probability
Resources
Resources
Resources
Resources
Probability
Probability
0
0
–5
Bias (deg)
Bias
Bias
Bias
Bias
Bias
Bias
Bias
Bias
Bias
Bias
Bias
Bias
s.d.
s.d.
s.d.
5
0.1
0.2
0
–10
10
0
–10
10
0
–10
10
0
0.1
0.2
0
0.1
0.2
0
Angle
Angle
Angle
Angle
Angle
Angle
Angle
Angle
Angle
Angle
Angle
Angle
Angle
Angle
Angle
Angle
Angle
Angle
Angle
Angle
Angle
Angle
Angle
Angle
0
Resources
Repulsion
Bias
Variability
Attraction
Resources
Repulsion
Bias (model)
Bias (data)
Attraction
0
10
0
10
0
10
(deg)
Fig. 6 | Bias and variability in color hue estimation. a–c, Bae et al.40 asked 
subjects to reproduce a color hue on a color wheel. The fitting procedure 
identifies a periodic pattern of resource allocation (a), and a prior peaking in the 
yellow range. We show fit at p = 2; results are similar across different exponents 
(Supplementary Fig. 45). The observed bias pattern (dotted) is mostly accounted 
for by likelihood repulsion; prior attraction accounts for relatively negative 
biases in the green–blue range. (b) A model with a uniform prior can qualitatively 
reproduce bias and variability, though fit is slightly inferior (b). A model relying 
entirely on a prior matches neither bias nor variability well (c). For the human 
data in a–c, we plot the mean together with error band indicating bootstrapped 
95% confidence interval. d, Olkkonen et al.39 presented subjects with stimuli 
taken from a small section on a similar color wheel. Human data are replotted 
from Olkkonen et al.39, as means with s.e.m. over subjects (n = 9 in blue and 
green; n = 18 in red). Encoding resources are from the fit in a; a; unimodal prior is 
assumed based on model fits to other datasets with small stimulus ranges (Fig. 5). 
Parameters were chosen to reproduce reported biases and thresholds, with the 
same loss function (p = 2) as in a. The resulting central tendency effect (red) is 
increased when increasing the delay after presentation (increasing sensory noise, 
blue) or adding external noise to stimuli (green).


--- Page 9 ---
Nature Neuroscience | Volume 27 | April 2024 | 793–804
801
Article
https://doi.org/10.1038/s41593-024-01574-x
These results provide new understanding of a classical effect. They 
suggest that the central tendency effect observed in the estimation of 
scalar variables is well accounted for by a prior normally distributed in 
the sensory space, adapting to the stimulus range. The observers did 
not seem to learn a flat prior perfectly reflecting short-term stimulus 
statistics. While the encoding heterogeneity leads to a small bias toward 
larger values, this component is small compared with the prior attrac-
tion. Although an abrupt drop-off of the prior does not provide a good 
model of the central tendency effect, we note that such an effect may 
still be observed when stimuli are close to a strict boundary of the range 
of allowed responses. See Supplementary Section 1.2, for a relevant 
example of subjective value ratings on a bounded scale27.
Application 4: categories in color perception. Experimental work has 
reported systematic biases in the perception of color hue, which have 
been explained in terms of representations involving discrete color 
categories (for example, ref. 40). In the Bayesian framework, categories 
can be conveniently formalized as priors peaking at the most typical 
elements of a category50, and the observed color bias may be explained 
by a bias toward these exemplars. Through re-analysis of previous data, 
a radically different explanation emerged, as described below.
We fitted our model to the trial-by-trial responses collected by 
Bae et al.40 (Fig. 6a). We find that the model explains the color biases 
primarily as likelihood repulsion, modulated by prior attraction: 
resource allocation is periodic across the color wheel with four 
peaks, creating an overall periodic bias pattern. Attraction to the prior 
accounts for a negative bias in the blue range. Qualitative fit was similar 
across exponents p ≥ 0 (Supplementary Fig. 45).
To better understand the relative importance of the prior and 
the encoding, we fitted two additional models. A model ablating the 
nonuniformity in the prior (Fig. 6b) predicts a similar overall bias pat-
tern, although it cannot account for the trend toward negative biases 
in the blue region. A model ablating the nonuniformity in encoding 
(Fig. 6c) provides a poor characterization of bias and variability of the 
response; and correspondingly has inferior cross-validated likelihood 
(Supplementary Fig. 44). Together, these results suggest that while 
both prior and encoding heterogeneity are needed for fully account-
ing for the pattern of the color biases, the latter accounts for a larger 
fraction of the biases.
If our analytical results and the P/P ratio rule hold universally, it 
should be possible to make attractive biases dominant simply by induc-
ing a quickly varying prior. This is supported by data from Olkkonen 
et al.39, who presented subjects with stimuli taken from a small section 
on a similar color wheel (Fig. 6d). Biases point into the interior of the 
range and increase not only with sensory noise, but also with stimulus 
noise39. This result is compatible with an interpretation as an attraction 
to a prior, overriding the repulsive effect on a small range where the 
prior varies rapidly. Thus, while circular stimulus spaces naturally lead 
to situations where repulsive biases dominate, this is not an intrinsic 
property of the stimulus modality. The principles described by the P/P 
ratio rule generally hold.
General insights emerging from the analyses. Figure 7 summarizes 
some of the main results from the analyses of these datasets. Impor-
tantly, in all cases, the results can be well captured by our P/P ratio rule 
(Fig. 7a). Combining the results from different applications reveals 
large differences between circular variables and scalar variables. For 
circular variables, we find that encoding heterogeneity is often key 
in driving the observed biases, and that prior attraction can play a 
surprisingly small role. This stands in marked contrast to traditional 
models emphasizing attraction to prior expectations. We summarize 
the role of attractive and repulsive biases across the datasets con-
sidered in this work in Fig. 7b, confirming that repulsive biases play 
a larger role in accounting for the overall biases in the four circular 
datasets, and a smaller role in the two scalar datasets. According to our 
empirical results, the loss function often plays a more important role in 
a
b
c
Bias
Relative negative
log-likelihood
Positive
Negative
(1) observed
(2) ratio rule
(3) attraction
(4) repulsion
Orientation
Direction
Color
Time
Numerosity
Exponent (p)
Orientation
Orientation
Direction
Angle
Length
Number
Exponent (p)
Exponent (p)
Exponent (p)
Exponent (p)
Exponent (p)
(deg)
(deg)
(deg)
(deg)
(s)
Attraction
100
0
0
5
10
Repulsion
Attraction
Repulsion
Attraction
Repulsion
Attraction
Repulsion
Attraction
Repulsion
Attraction
Repulsion
(deg)
10
0
(deg)
(deg)
(deg)
(s)
4
0
5
0
5
0
0.05
0
20
0
20
–20
0
20
–20
0
20
–20
0
40
0
20
–20
0
0
5
10
0
5
10
0
5
10
0
5
10
0
5
10
55
25
1.0
0.5
180
90
0
90
135
45
90
0
180
90
0
180
Fig. 7 | General insights gained across datasets. A summary of the relative 
role of attractive and repulsive biases, and their relation to the loss function, for 
the six datasets fitted in Figs. 3–6. We plot data from the Cardinal group in the 
Direction dataset, and from one interval in the Numerosity dataset. a, P/P ratio 
rule, for each stimulus, we plot the sign of (1) the observed bias, (2) the prediction 
made by the P/P ratio rule, (3) prior attraction and (4) likelihood repulsion. 
The P/P ratio rule accurately predicts the sign of the observed bias. Repulsive 
biases play a larger role in accounting for the overall biases in the four circular 
datasets, and a smaller role in the two scalar datasets. b, Magnitudes of likelihood 
repulsion (blue) and prior attraction (orange). For each point in the discretized 
stimulus space constructed in the implemented model, we show a dot indicating 
the absolute value bias magnitude (lowest, 0). Repulsion plays a dominant role 
in the four circular datasets, and only a very small role in the two scalar datasets. 
c, Model fit (y axis), measured by cross-validated negative log-likelihood (lower 
is better), relative to the reported model, by loss function exponent (x axis). Data 
are presented as mean values ± s.e.m. across n = 10 folds, except for Direction, 
where only one fold was used. For the orientation, direction and color datasets, 
different loss functions provide substantially different model fit, whereas effect 
on quantitative fit is small in the two datasets with interval stimulus spaces.


--- Page 10 ---
Nature Neuroscience | Volume 27 | April 2024 | 793–804
802
Article
https://doi.org/10.1038/s41593-024-01574-x
accounting for perceptual data based on circular variables compared 
with that of scalar variables (Fig. 7c). This could be explained by (1) for 
scalar variables, prior attraction tends to be more prominent due to 
the larger total variation of the prior; and (2) according to our theory, 
the magnitude of the prior attraction is not sensitive to the exact form 
of the loss function. Taken together, these results clarify a large and 
disparate literature, and reveal new insights into the factors dominat-
ing the perceptual biases under different experimental conditions.
Discussion
Traditional Bayesian perspectives emphasize perceptual biases due 
to prior expectations9,11,24. In contrast, recent work has discovered that 
Bayesian models based on efficient coding predict biases away from the 
prior expectation, which had been thought to be ‘anti-Bayesian’16,17. Our 
unifying theory reconciles these conflicting perspectives, and further-
more explains experimental findings otherwise accounted for by neither 
previous perspective. Through a combination of theory and analysis of 
experimental data across several modalities, our results demonstrate 
that perceptual biases are determined crucially not only by the prior, 
but also by the encoding, stimulus range, loss function and noise char-
acteristics. Attraction to a prior, commonly considered a hallmark of 
Bayesian models of perception and cognition, may be prominent under 
some conditions (for example, refs. 9,52), but plays a surprisingly sub-
ordinate role in the datasets examined here. For perceptual judgments 
within a bounded range, the boundary plays an important role.
Our approach offers a more complete Bayesian modeling frame-
work compared with previous work9,11,17,24,53,54. This increased modeling 
power also raises an important question: can our more flexible mod-
eling approach recover the ground truth from observation data alone? 
For instance, one might be concerned that repulsive and attractive 
biases might trade off, limiting separate identifiability of encoding, 
prior and loss function. However, our fitting procedure takes into 
account not only the bias, but the entire response distribution, whose 
higher-order statistics may distinctly reflect encoding and prior even 
when the bias does not. To determine whether experimentally realistic 
amounts of data are sufficient to recover the contributions of the dif-
ferent model components, we refitted our model on synthetic datasets 
that were generated by matching the structure and sample sizes to the 
real datasets analyzed above. We found that, on these synthetic data-
sets, our method closely recovered the ground truth (Supplementary 
Section 2.4.2). A conceptually related concern is whether the generality 
of our model allows it to fit arbitrary data well. We find that this is not 
the case. For instance, when swapping the stimulus noise and sensory 
noise conditions in the orientation experiments, the model can no 
longer reproduce even qualitative features of these data (Supplemen-
tary Section 2.4.1 and Supplementary Fig. 51).
By considering an Lp family of loss function, our results generalize 
previous models, yet do not fully take into account the detailed shape 
of, possibly even asymmetric, loss functions55,56. Future work on larger 
datasets with more relaxed assumptions about the loss function may 
allow more precise identification of the loss function. As a preliminary 
step toward this direction, we find that asymmetric loss functions 
that assign different weights to underestimation and overestimation 
errors57,58 lead to biases clearly distinct from those of the symmetric Lp 
losses considered here (Supplementary Section 3.1.4.6).
One outstanding question in neuroscience is how prior beliefs and 
encodings adapt to the statistics of the environment. Recent studies 
propose that encoding and prior are both linked to environmental 
statistics, where the adaption of prior and encoding reflect statistical 
learning and efficient coding, respectively. While this seems to be a 
reasonable hypothesis in a stationary environment, and is supported 
by some experimental data17,24,28, the exact rules that govern these 
adaptations remain debated. Some accounts assume maximization 
of information transformation as the objective that sensory systems 
optimize17–20,59, while others propose objective functions specific to 
particular behavioral tasks (for example, refs. 60,61). Our approach, 
in conjunction with adequate measurement of natural scene statistics, 
may help further adjudicate between these theories. Beyond station-
ary environments, it remains an open question how prior and encod-
ing dynamically evolve62 and respond to task demands63. Insight into 
this question will likely lead to a more principled explanation of vari-
ous attractive and repulsive stimulus-history-related biases reported 
experimentally64–66. Our results suggest that the short-term stimulus 
statistics in an experiment substantially influence the prior, and only 
to a lesser extent the encoding precision. For instance, our results sug-
gest that, in the perception of motion direction, the encoding precision 
will show little change when observers are exposed to different motion 
statistics, while the prior will roughly reflect these short-term statistics.
The recovered prior, encoding and loss function from our 
approach impose specific constraints on the neural implementation of 
perceptual inference67–69, which has stood as an open question despite 
decades of research. Previous theoretical studies suggest that, when 
the prior is embedded in the distribution of neural tuning curves, 
biologically plausible population vector decoders can implement 
Bayesian inference59,70,71. Others propose that the likelihood function 
or the posterior distribution may be represented implicitly in the noisy 
neural response67. Our results provide important constraints for these 
proposals: any reasonable neural implementation of Bayesian infer-
ence should produce behavioral response patterns consistent with 
our theory. For instance, if—as suggested by our results—the observ-
ers’ prior adapts at a faster timescale than the neural encoding in such 
psychophysical tasks, this would suggest that the prior is encoded in 
a different neural substrate than the likelihood function, inconsistent 
with previous proposals34,70. More broadly, by providing a compre-
hensive characterization of behavioral biases and variability from 
first principles, our results provide a rigorous framework for testing a 
principal hypothesis (that is, the Bayesian brain hypothesis) about the 
computations in the brain.
The ability to infer the prior, encoding and loss function directly 
from behavior opens up numerous future directions. By combining our 
method with measurements of brain activity, one can seek to identify 
how priors, likelihood and loss functions are implemented in distrib-
uted brain networks68,69. Furthermore, with high-resolution behav-
ioral data, our method should enable the estimation of these crucial 
components of perceptual inference for an individual observer. This 
will provide a powerful approach to studying the neural basis of the 
interindividual variability of perceptual decisions. Similarly, one could 
apply this approach to study the potential differences in perceptual 
inferences in neurotypical and atypical subjects5,53,72. As perceptual 
estimation of stimulus attributes is fundamental to virtually all cog-
nitive functions, our results may have behavioral consequences and 
implications beyond perception.
Online content
Any methods, additional references, Nature Portfolio reporting sum-
maries, source data, extended data, supplementary information, 
acknowledgements, peer review information; details of author contri-
butions and competing interests; and statements of data and code avail-
ability are available at https://doi.org/10.1038/s41593-024-01574-x.
References
1.	
Jastrow, J. Studies from the University of Wisconsin: on the 
judgment of angles and positions of lines. Am. J. Psychol. 5, 
214–248 (1892).
2.	
Hollingworth, H. L. The central tendency of judgment. J. Philos. 
Psych. Sci. Methods 7, 461–469 (1910).
3.	
Sadi, R., Asl, H. G., Rostami, M. R., Gholipour, A. & Gholipour, 
F. Behavioral finance: the explanation of investors’ personality 
and perceptual biases effects on financial decisions. Int. J. Econ 
Finance 3, 234–241 (2011).


--- Page 11 ---
Nature Neuroscience | Volume 27 | April 2024 | 793–804
803
Article
https://doi.org/10.1038/s41593-024-01574-x
4.	
Frydman, C. & Jin, L. J. Efficient coding and risky choice. Q. J. Econ. 
137, 161–213 (2022).
5.	
Lieder, I. et al. Perceptual bias reveals slow-updating in autism 
and fast-forgetting in dyslexia. Nat. Neurosci. 22, 256–264 (2019).
6.	
Horga, G. & Abi-Dargham, A. An integrative framework for 
perceptual disturbances in psychosis. Nat. Rev. Neurosci. 20, 
763–778 (2019).
7.	
Von Helmholtz, H. Treatise on Physiological Optics, Vol. 3 (Optical 
Society of America, 1925).
8.	
Knill, D. C. & Pouget, A. The Bayesian brain: the role of uncertainty 
in neural coding and computation. Trends Neurosci. 27, 712–719 
(2004).
9.	
Körding, K. P. & Wolpert, D. M. Bayesian integration in 
sensorimotor learning. Nature 427, 244–247 (2004).
10.	 Weiss, Y., Simoncelli, E. P. & Adelson, E. H. Motion illusions as 
optimal percepts. Nat. Neurosci. 5, 598–604 (2002).
11.	
Stocker, A. A. & Simoncelli, E. P. Noise characteristics and prior 
expectations in human visual speed perception. Nat. Neurosci. 9, 
578–585 (2006).
12.	 Sun, J. & Perona, P. Where is the sun? Nat. Neurosci. 1, 183–184 (1998).
13.	 Adams, W. J., Graf, E. W. & Ernst, M. O. Experience can change the 
‘light-from-above’ prior. Nat. Neurosci. 7, 1057–1058 (2004).
14.	 Huttenlocher, J., Hedges, L. V. & Duncan, S. Categories and 
particulars: prototype effects in estimating spatial location. 
Psychol. Rev. 98, 352 (1991).
15.	 Jazayeri, M. & Shadlen, M. N. Temporal context calibrates interval 
timing. Nat. Neurosci. 13, 1020–1026 (2010).
16.	 Wei, X.-X. & Stocker, A. A. Efficient coding provides a direct link 
between prior and likelihood in perceptual Bayesian inference. 
In Proc. Advances in Neural Information Processing Systems (NIPS 
2012) (eds Pereira, F. et al.) 1313–1321 (Curran Associates, 2012).
17.	 Wei, X.-X. & Stocker, A. A Bayesian observer model constrained 
by efficient coding can explain ‘anti-Bayesian’ percepts. Nat. 
Neurosci. 18, 1509–1517 (2015).
18.	 Barlow, H. B. et al. Possible principles underlying the transformation 
of sensory messages. Sensory Communication (ed. Rosenblith, W. A.) 
217–233 (MIT Press, 1961).
19.	 Laughlin, S. A simple coding procedure enhances a neuron’s 
information capacity. Z. Naturforsch. C 36, 910–912 (1981).
20.	 Linsker, R. Self-organization in a perceptual network. Computer 
21, 105–117 (1988).
21.	 Lennie, P. Distortions of perceived orientation. Nat. New Biol. 233, 
155–156 (1971).
22.	 de Gardelle, V., Kouider, S. & Sackur, J. An oblique illusion 
modulated by visibility: non-monotonic sensory integration in 
orientation processing. J. Vision 10, 6 (2010).
23.	 Coppola, D. M., Purves, H. R., McCoy, A. N. & Purves, D. The 
distribution of oriented contours in the real world. Proc. Natl 
Acad. Sci. USA 95, 4002–4006 (1998).
24.	 Girshick, A. R., Landy, M. S. & Simoncelli, E. P. Cardinal 
rules: visual orientation perception reflects knowledge of 
environmental statistics. Nat. Neurosci. 14, 926–932 (2011).
25.	 Körding, K. P. & Wolpert, D. M. The loss function of sensorimotor 
learning. Proc. Natl Acad. Sci. USA 101, 9839–9842 (2004).
26.	 Bell, A. J. & Sejnowski, T. J. An information-maximization approach 
to blind separation and blind deconvolution. Neural Comput. 7, 
1129–1159 (1995).
27.	 Polanía, R., Woodford, M. & Ruff, C. C. Efficient coding of 
subjective value. Nat. Neurosci. 22, 134–142 (2018).
28.	 Wei, X.-X. & Stocker, A. Lawful relation between perceptual bias 
and discriminability. Proc. Natl Acad. Sci. USA 114, 10244–10249 
(2017).
29.	 Petzschner, F. H. & Glasauer, S. Iterative Bayesian estimation as an 
explanation for range and regression effects: a study on human 
path integration. J. Neurosci. 31, 17220–17229 (2011).
30.	 Zhang, H., Ren, X. & Maloney, L. T. The bounded rationality of 
probability distortion. Proc. Natl Acad. Sci. USA 117, 22024–22034 
(2020).
31.	 Prat-Carrabin, A. & Woodford, M. Bias and variance of the 
Bayesian-mean decoder. In Proc. Advances in Neural Information 
Processing Systems 34 (NeurIPS 2021) (eds Ranzata, M. et al.) 
23793–23805 (Curran Associates, 2021).
32.	 Stocker, A. A. & Simoncelli, E. Sensory adaptation within 
a Bayesian framework for perception. Advances in Neural 
Information Processing Systems 18. In Proc. Advances in Neural 
Information Processing Systems (NIPS 2005) (eds Weiss, Y. et al.) 
1291–1298 (MIT, 2005).
33.	 Morais, M. J. & Pillow, J. W. Power-law efficient neural codes 
provide general link between perceptual bias and discriminability. 
In Proc. Advances in Neural Information Processing Systems 31 
(NuerIPS 2018) (eds Bengio, S. et al.) (Curran Associates, 2018).
34.	 Ganguli, D. & Simoncelli, E. P. Implicit encoding of prior 
probabilities in optimal neural populations. Adv. Neural Inf. 
Process. Syst. 2010, 658–666 (2010).
35.	 Prat-Carrabin, A. & Woodford, M. Efficient coding of numbers 
explains decision bias and noise. Nat. Hum. Behav. 6, 1142–1152 
(2022).
36.	 Wei, X.-X. & Stocker, A. Mutual information, Fisher information, 
and efficient coding. Neural Comput. 28, 305–326 (2016).
37.	 Remington, E. D., Parks, T. V. & Jazayeri, M. Late Bayesian inference 
in mental transformations. Nature Commun. 9, 4419 (2018).
38.	 Tomassini, A., Morgan, M. J. & Solomon, J. A. Orientation 
uncertainty reduces perceived obliquity. Vision Res. 50,  
541–547 (2010).
39.	 Olkkonen, M., McCarthy, P. & Allred, S. R. The central tendency 
bias in color perception: effects of internal and external noise.  
J. Vision 14, 5 (2014).
40.	 Bae, G.-Y., Olkkonen, M., Allred, S. R. & Flombaum, J. I. Why some 
colors appear more memorable than others: a model combining 
categories and particulars in color working memory. J. Exp. 
Psychol. Gen. 144, 744–763 (2015).
41.	 Xiang, Y., Graeber, T., Enke, B. &Gershman, S. J. Confidence 
and central tendency in perceptual judgment.Atten. Percept. 
Psychophys. 83, 3024–3034 (2021).
42.	 Gekas, N., Chalk, M., Seitz, A. R. & Seriès, P. Complexity and 
specificity of experimentally induced expectations in motion 
perception. J. Vision 14, P355 (2013).
43.	 Van Bergen, R. S., Ji Ma, W., Pratte, M. S. & Jehee, J. F. Sensory 
uncertainty decoded from visual cortex predicts behavior. Nat. 
Neurosci. 18, 1728–1730 (2015).
44.	 Appelle, S. Perception and discrimination as a function of 
stimulus orientation: the ‘oblique effect’ in man and animals. 
Psychol. Bull. 78, 266–278 (1972).
45.	 Mao, J. & Stocker, A. Holistic inference explains human perception 
of stimulus orientation. Preprint at bioRxiv https://doi.org/10.1101/ 
2022.06.24.497534 (2022).
46.	 Chalk, M., Seitz, A. R. & Seriès, P. Rapidly learned stimulus 
expectations alter perception of motion. J. Vision 10, 2 (2010).
47.	 Gros, B. L., Blake, R. & Hiris, E. Anisotropies in visual motion 
perception: a fresh look. J. Opt. Soc. Am. A. Opt. Image Sci. Vis. 15, 
2003–2011 (1998).
48.	 Krukowski, A. E. & Stone, L. S. Expansion of direction space 
around the cardinal axes revealed by smooth pursuit eye 
movements. Neuron 45, 315–323 (2005).
49.	 Stevens, S. S. & Greenbaum, H. B. Regression effect  
in psychophysical judgment. Percept. Psychophys. 1,  
439–446 (1966).
50.	 Huttenlocher, J., Hedges, L. V. & Vevea, J. L. Why do categories 
affect stimulus judgment?. J. Exp. Psychol. Gen. 129, 220–241 
(2000).


--- Page 12 ---
Nature Neuroscience | Volume 27 | April 2024 | 793–804
804
Article
https://doi.org/10.1038/s41593-024-01574-x
51.	 Cicchini, G. M., Anobile, G. & Burr, D. C. Compressive mapping of 
number to space reflects dynamic encoding mechanisms, not static 
logarithmic transform. Proc. Natl Acad. Sci. USA 111, 7867–7872 (2014).
52.	 Mamassian, P. & Goutcher, R. Prior knowledge on the illumination 
position. Cognition 81, B1–B9 (2001).
53.	 Noel, J.-P., Zhang, L.-Q., Stocker, A. A. & Angelaki, D. E. Individuals 
with autism spectrum disorder have altered visual encoding 
capacity. PLoS Biol. 19, e3001215 (2021).
54.	 Manning, T. S. et al. A general framework for inferring Bayesian 
ideal observer models from psychophysical data. eNeuro 10, 
ENEURO.0144-22.2022 (2023).
55.	 Tversky, A. & Fox, C. R. Weighing risk and uncertainty. Psychol. 
Rev. 102, 269 (1995).
56.	 Shenoy, P. & Yu, A. J. Strategic impatience in go/nogo versus 
forced-choice decision-making. In Proc. Advances in Neural 
Information Processing Systems (NIPS 2012) (eds Pereira, F. et al.) 
2132–2140 (Curran Associates, 2012).
57.	 Mamassian, P. Overconfidence in an objective anticipatory motor 
task. Psychol. Sci. 19, 601–606 (2008).
58.	 Hudson, T. E., Maloney, L. T. & Landy, M. S. Optimal compensation 
for temporal uncertainty in movement planning. PLoS Comput. 
Biol. 4, e1000130 (2008).
59.	 Ganguli, D. & Simoncelli, E. P. Efficient sensory encoding and 
Bayesian inference with heterogeneous neural populations. 
Neural Comput. 26, 2103–2134 (2014).
60.	 Burge, J. & Geisler, W. S. Optimal defocus estimation in individual 
natural images. Proc. Natl Acad. Sci. USA 108, 16849–16854 (2011).
61.	 Park, I. M. & Pillow, J. W. Bayesian efficient coding. Preprint at 
bioRxiv https://doi.org/10.1101/178418 (2017).
62.	 Młynarski, W. F. & Hermundstad, A. M. Efficient and adaptive 
sensory codes. Nat. Neurosci. 24, 998–1009 (2021).
63.	 Roach, N. W., McGraw, P. V., Whitaker, D. J. & Heron, J. 
Generalization of prior information for rapid Bayesian time 
estimation. Proc. Natl Acad. Sci. USA 114, 412–417 (2017).
64.	 Fritsche, M., Spaak, E. & de Lange, F. P. A Bayesian and efficient 
observer model explains concurrent attractive and repulsive 
history biases in visual perception. eLife 9, e55389 (2020).
65.	 Gekas, N., McDermott, K. C. & Mamassian, P. Disambiguating 
serial effects of multiple timescales. J. Vision 19, 24–24 (2019).
66.	 Fischer, J. & Whitney, D. Serial dependence in visual perception. 
Nat. Neurosci. 17, 738–743 (2014).
67.	 Ma, W. J., Beck, J. M., Latham, P. E. & Pouget, A. Bayesian inference 
with probabilistic population codes. Nat. Neurosci. 9, 1432–1438 
(2006).
68.	 Vilares, I., Howard, J. D., Fernandes, H. L., Gottfried, J. A. & 
Kording, K. P. Differential representations of prior and likelihood 
uncertainty in the human brain. Curr. Biol. 22, 1641–1648 (2012).
69.	 Funamizu, A., Kuhn, B. & Doya, K. Neural substrate of dynamic 
Bayesian inference in the cerebral cortex. Nat. Neurosci. 19, 
1682–1689 (2016).
70.	 Wei, X.-X. & Stocker, A. A. Bayesian inference with efficient neural 
population codes. In Proc. Artificial Neural Networks and Machine 
Learning—ICANN 2012: 22nd International Conference on Artificial 
Neural Networks, Part I 22, (eds Villa, A. E. P. et al.) 523–530 
(Springer, 2012).
71.	 Fischer, B. J. & Peña, J. L. Owl’s behavior and neural representation 
predicted by Bayesian inference. Nat. Neurosci. 14, 1061–1066 
(2011).
72.	 Notredame, C.-E., Pins, D., Denéve, S. & Jardri, R. What visual 
illusions teach us about schizophrenia. Front. Integr. Neurosci. 8, 
63 (2014).
Publisher’s note Springer Nature remains neutral with  
regard to jurisdictional claims in published maps and  
institutional affiliations.
Springer Nature or its licensor (e.g. a society or other partner) holds 
exclusive rights to this article under a publishing agreement with 
the author(s) or other rightsholder(s); author self-archiving of the 
accepted manuscript version of this article is solely governed by the 
terms of such publishing agreement and applicable law.
© The Author(s), under exclusive licence to Springer Nature America, 
Inc. 2024


--- Page 13 ---
Nature Neuroscience
Article
https://doi.org/10.1038/s41593-024-01574-x
Methods
Model assumptions
We assume that the stimulus space 𝒳𝒳 is a contiguous one-dimensional 
manifold (the real line, an interval or a circle). The sensory space 𝒴 has 
the same topology as the stimulus space. The sensory space conceptu-
ally represents the one-dimensional submanifold of the space of neural 
activations spanned by the mean encoding of the stimuli in 𝒳𝒳. We 
assume that F ∶𝒳𝒳𝒳𝒴𝒴 is bijective and differentiable, such that its slope 
(and thus the Fisher information of the encoding) is nowhere zero. 
Thus, no two stimuli are mapped to the same mean output. We assume 
that the prior is nowhere zero. Further, we make basic regularity 
assumptions: F′(θ), F−1(θ), and log pprior(θ) are twice continuously dif-
ferentiable, and both they and their first and second derivatives cannot 
grow superpolynomially in θ. We relax these assumptions for Theorem 3 
(Boundary Effects) by allowing the prior to discontinuously become 
zero at a boundary θMax. These assumptions are satisfied for wide 
classes of models across the literature (Supplementary Section 3.1.1). 
Under the model (equation (1)), for a given measurement x, the likeli-
hood function is the distribution of F−1(m); it can be computed as 
p(x|θ) =
1
√2π √J(x) exp (−
(F(x)−F(θ))
2
2σ2
).
Given an Lp loss function and an observed sensory encoding m ∈𝒴𝒴, 
the Bayes estimator ̂θ ∈𝒳𝒳 is defined as
̂θ ∶= arg ̂θ∈𝒳𝒳min ∫
𝒳𝒳
| ̂θ −θ|pp(θ|m)dθ
(5)
The limit p → 0 results in the MAP estimator. Given a true stimulus θ, 
the bias of an estimator ̂θ is
𝔼𝔼𝔼̂θ] −θ = 𝔼𝔼𝔼F−1(m)] −θ
⏟⎵⎵⎵⏟⎵⎵⎵⏟
Encoding bias
+ 𝔼𝔼𝔼̂θ −F−1(m)]
⏟⎵⎵⎵⏟⎵⎵⎵⏟
Decoding bias
(6)
where the expectation runs over the noisy sensory encoding m defined 
in equation (1). Encoding bias always reflects likelihood repulsion and 
is independent of the loss function and the prior, whereas decoding 
bias includes both attractive and repulsive components depending 
on prior and loss function (Supplementary Section 3.1.1).
Analytical results
Our analytical results are stated in three theorems and a simple P/P ratio 
rule for judging the direction of the bias. Theorem 1 is the main theo-
rem, addressing the biases under the model assumed in equation (1). 
Theorem 2 extends the theory to cases where both sensory and stimulus 
noise are present. Theorem 3 extends the theory to address biases close 
to a boundary. The proofs of the theorems are given in Supplementary 
Sections 3.1–3.3. The P/P ratio rule is a straightforward consequence 
of Theorem 1 (see below).
Main theory. Theorem 1. Assume that θ is a point in the interior of the 
stimulus space. For the model defined in equation (1), the bias of the 
estimate ̂θ for Lp loss (p ≥ 1 an integer) with arbitrary prior, for observed 
stimulus θ, can be written as
𝔼𝔼𝔼̂θ] −θ =
1
J(θ) (log pprior(θ))
′
⏟⎵⎵⎵⎵⎵⏟⎵⎵⎵⎵⎵⏟
Prior attraction
+ p + 2
4
( 1
J(θ) )
′
⏟⎵⎵⎵⏟⎵⎵⎵⏟
Likelihood repulsion
;
(7)
and, for the MAP estimator (p = 0),
𝔼𝔼𝔼̂θ] −θ =
1
J(θ) (log pprior(θ))
′ + 1
4 ( 1
J(θ) )
′
,
(8)
both up to approximation error O(σ 4 × CF,pprior,p,θ), when σ is sufficiently 
small, where the error contains constants depending on F, pprior, p 
and θ, but not σ. Here J =
(F′(θ))
2
σ2
 is the Fisher information; both J and 
pprior are functions of θ.
The error term O(σ4 × CF,pprior,p,θ) indicates that the error scales, on 
the one hand, with σ4, and on the other hand, with quantities that 
depend on the exponent and on the smoothness of encoding and prior. 
When σ < 1, O(σ4) has a smaller order of magnitude than 1/J; hence, the 
approximation error is small relative to the size of the bias when noise 
is sufficiently small (Supplementary Fig. 4). The theorem is proven in 
Supplementary Section 3.1.
We prove an analogous decomposition for an alternative model 
sometimes assumed in the literature (for example, refs. 11,15,24,33), 
in which sensory noise is Gaussian in the stimulus space with 
stimulus-dependent variance (Supplementary Section 3.5 for details).
To derive the P/P ratio rule, the bias (equation (7)) can be written 
as (p > 0)
1
J(θ) (log pprior(θ))
′ −
1
J(θ)
p+2
4 (log J(θ))
′
=
1
J(θ) (log pprior(θ) −log J(θ)
p+2
4 )
′
=
1
J(θ) (log
pprior(θ)
J(θ)
p+2
4 )
′
(9)
which has the same sign as Q(θ). At p = 0, an analogous derivation using 
equation (8) leads to Q(θ) = (
pprior(θ)
J(θ)
1
4 )
′
.
Extensions of the theory. We extend the theory to address the impact 
of stimulus noise and the stimulus boundary.
Extension 1: stimulus noise modulates the biases. Theorem 2 con-
siders the impact of stimulus (external) noise, assuming that observers 
take both the sensory noise and stimulus noise into consideration. 
Formally, we extend the model (equation (1)) to
m = F(θ + ε) + δ
(10)
where ε is Gaussian stimulus noise with variance τ2.
Theorem 2. Consider the model in equation (10).
Assume that θ is a point in the interior of the stimulus space. Let 
σ2 be the variance of sensory noise and J(θ) ∶=
(F′(θ))
2
σ2
 the Fisher informa-
tion of the sensory encoding. Let τ2 be the variance of stimulus noise. 
Then, for even integers p > 0, the bias of the estimate ̂θ for Lp loss is
( 1
J(θ) + τ2) (log pprior(θ))
′
⏟⎵⎵⎵⎵⎵⎵⎵⏟⎵⎵⎵⎵⎵⎵⎵⏟
Prior attraction
+ [1 + p −2
4
1
1 + τ2J(θ) ] ( 1
J(θ) )
′
⏟⎵⎵⎵⎵⎵⎵⎵⎵⏟⎵⎵⎵⎵⎵⎵⎵⎵⏟
Likelihood repulsion
(11)
up to approximation error of order O ((σ 4 + τ 4 + σ2τ2) × CF,pprior,p,θ) when 
σ, τ are sufficiently small.
The special case τ2 = 0 recovers the corresponding expression 
in Theorem 1. In the prior attraction term, stimulus noise leads to a 
straightforward increase in bias. In the likelihood repulsion term, 
stimulus noise decreases repulsion when p > 2. This formal result, 
proven in Supplementary Section 3.2, covers even exponents p > 0. 
See Supplementary Fig. 5 for other exponents.
Extension 2: boundary-induced biases. To understand boundary 
effects, we consider the case where the prior is truncated at some point 
θMax close to the point θ, formally, pprior(x) ≡ 0 when x > θMax. Let 
D(θ) ∶=
F(θMax)−F(θ)
σ
 the distance of θ from the boundary in sensory space, 
normalized by noise s.d. Then, we have the following result, proven in 
Supplementary Section 3.3:
Theorem 3. Assume the model in equation (1), and assume pprior(x) ≡ 0 if, 
and only if, x > θMax. Assume θ < θMax. For some positive constants C1,p,θ,F,σ, 
C2,p,D, C3,p,D the bias (for even integers p > 0) is given as


--- Page 14 ---
Nature Neuroscience
Article
https://doi.org/10.1038/s41593-024-01574-x
−C1,p,θ,F,σ
√J(θ)
⏟⎵⎵⏟⎵⎵⏟
Regression
+C2,p,D
1
J(θ) (log pprior(θ))
′
⏟⎵⎵⎵⎵⎵⏟⎵⎵⎵⎵⎵⏟
Prior attraction
+C3,p,D
p + 2
4
( 1
J(θ) )
′
⏟⎵⎵⎵⏟⎵⎵⎵⏟
Likelihood repulsion
(12)
up to approximation error of order O(σ3 × CF,pprior,p,θ,D) when σ is suffi-
ciently small, where the following conditions hold: C1,p,θ,F,σ = Θ(1) as 
σ → 0; limD→∞C1,p,θ,F,σ = 0, limD→∞C2/3,p,D = 1.
The coefficient C1,p,θ,F,σ increases with the exponent p (Supplemen-
tary Fig. 7), so that higher exponents lead to a stronger regression 
effect. We note that, while the boundary-induced regression effect 
bears some conceptual similarity to attraction to a prior, there are two 
key differences: First, the boundary effect increases with higher expo-
nents, unlike prior attraction. Second, the boundary effect scales with 
1
√J, whereas prior attraction scales with 
1
J; the former is larger when 
noise is small, so that the boundary effect dominates repulsion and 
attraction effects close to the boundary (Supplementary Fig. 6). This 
correctly accounts for biases in subjective ratings on a bounded scale 
(Supplementary Section 1.2).
Fitting Procedure
We developed a general fitting procedure that can represent encoding 
and prior without restrictive parametric assumptions often made in 
previous work. The stimulus space is discretized as θ1, …, θN; resource 
allocation and prior are parameterized by the values log
d
dθ F(θi) and 
log pprior(θi), for each i = 1, …, N. Stimuli θ are mapped to the closest grid 
point θi and encoded as F(θi). The encoding likelihood is computed on 
the discrete grid by computing the Gaussian density on each F(θj) and 
renormalizing. An analogous approach is used for stimulus noise, when 
it is present. We then numerically compute the posterior by exact 
Bayesian inference in the discretized stimulus and sensory space. 
The estimator ̂θ is computed using Newton’s method in the full continu-
ous stimulus space (not just the grid), representing the integral in 
equation (5) by a sum over the discretized stimulus space.
The observed responses are assumed to result from the estima-
tor by adding zero-mean motor noise with a stimulus-independent 
width. The motor distribution is represented on the full continuous 
stimulus space. All noise types (sensory, stimulus, motor) are Gaussian 
for interval stimuli and von Mises for circular stimuli. We assume that 
responses reflect a mixture of estimator plus motor noise and a uniform 
distribution, weighted with a fitted guessing rate. Motor noise impacts 
the variability of the observed response, but not its bias. Guessing 
decreases the bias by a constant factor because random guessing is 
unbiased; we elide this in stating our theoretical results for simplicity.
For interval datasets, while the theoretical stimulus space is 
semi-infinite, we defined finite cutoffs for implementation (>150 for 
numerosity, >3 for time intervals). Responses below zero or above the 
cutoffs were excluded, affecting 0.03% (numerosity) or 0.01% (time 
intervals) of observations.
The size of the grid is 180 for circular stimuli, 200 for time interval 
perception and equal to the number of discrete numbers involved (151) 
in numerosity perception.
Resource allocations are fitted nonparametrically in Figs. 3b,c,g,h; 
4 and 6. We enforced the resource allocation to be consistent with 
Weber’s law for the models in Fig. 5. Priors are fitted nonparametri-
cally in Figs. 4 and 6, and are parametric as specified in Figs. 3b,c,g,h 
and 5c,d,g,h. See Supplementary Figs. 15, 25 and 43 for results with 
nonparametrically fitted priors. Figure 7 plots results for the models 
in Figs. 3b,g, 4b, 5c,g and 6a.
Parameters are fitted to maximize trial-by-trial log-likelihood using 
gradient descent (see Supplementary Section 2.1 for details). We employ 
standard automated differentiation methods implemented in PyTorch 
(Python package torch v.1.11.0), differentiating through equation (5) 
using the implicit function theorem (Supplementary Section 2.1.3). 
Besides resource allocation and prior, further parameters are magni-
tudes of sensory, stimulus and motor noise (stimulus noise is assumed 
to be zero except where explicitly manipulated), and a guessing rate. In 
experiments with conditions involving different magnitudes of noise, 
parameters other than the relevant noise magnitudes were shared 
across conditions.
The fitting problem is, in general, not convex; we verified that 
restarting from different configurations led to equivalent results (Sup-
plementary Fig. 13).
Overfitting is mitigated by a regularization term penalizing the 
average squared difference between logarithmic values of FI (prior) on 
adjacent points on the grid, with a weight determined for each dataset 
through cross-validation in preliminary simulations (Supplementary 
Section 2.1.3).
We report results where data from all subjects was pooled, except 
for the data in Fig. 4, where we instead fitted subject-specific adjust-
ments for prior and encoding, and freely fitted all noise parameters 
for each subject: analogous to standard parametric mixed-effects 
models, subject-specific adjustments were subjected to a mean-zero 
prior favoring smooth adjustments (Supplementary Section 2.1.4). 
We parameterized the shared components of the prior and encoding 
relative to the central direction (prior) or the quadrant containing the 
central direction (encoding), and fitted the model using a standard vari-
ational approximation to the intractable likelihood (Supplementary 
Section 2.1.4). A parameterization with subject-specific adjustments is, 
in principle, also applicable to other datasets, though fitting by subject 
adjustments is computationally more expensive. See Supplementary 
Fig. 49 for an application to the model in Fig. 6a.
We used the Python packages torch v.1.11.0, matplotlib v.3.5.3, 
colormath v.3.0.0, numpy v.1.19.0 and scipy v.1.4.1.
Implementation of loss function. For circular stimuli (orientation, 
motion direction and color), we considered two versions of the Lp loss 
in implementing equation (5): the first centers the circular coordinates 
[−180°, 180°] at F−1(m), and applies the ordinary absolute distance. 
This makes equation (5) a convex optimization problem. The second 
version, inspired by the density of the von Mises distribution, uses the 
loss function ℓ(x, y) ∶= (1 −cos(x −y))
p/2. In the low-noise regime, both 
are equivalent (ℓ(x, y) ≈ ∣x − y∣p); hence, our theoretical results apply 
equally to these and other similar loss functions. We report the imple-
mentation with the cosine-based loss as it has better quantitative 
model fit in orientation perception (Supplementary Fig. 14). Another 
natural distance, the geodesic (arc-length) distance, is not differenti-
able everywhere, rendering it impractical in the context of 
gradient-based fitting procedures.
Evaluation and visualization. To estimate model fit, we randomly par-
titioned the trials from each subject into ten folds. We then conducted 
cross-validation, fitting the model for maximum likelihood on nine 
folds (pooled across subjects) and recorded the held-out likelihood 
of the remaining fold. We report the averaged log-likelihood across 
the ten folds. For the motion direction dataset (involving by subject 
parameters), we only evaluated on one fold due to computational cost.
When both encoding and prior are nonuniform, we separately esti-
mated the prior attraction as the decoding bias of the MAP estimator, 
and the likelihood repulsion as the difference between the overall bias 
and the MAP estimator’s decoding bias. For the flat prior in Fig. 5d,h, 
attraction and repulsion were computed for a uniform prior without 
the boundary. For circular stimuli, bias and variability are reported 
using circular statistics.
We estimated the perceptual biases using a Gaussian (intervals) or 
von Mises (circular spaces) kernel, except for Fig. 3f, where we estimated 
the bias for each of the presented orientations separately. We estimated 
variability at points on a regularly spaced grid, and then smoothed the 
result using a kernel as described above. Unless indicated otherwise, 
error bars or bands indicate 95% confidence intervals obtained by boot-
strapping the set of trials. Data in Fig. 6d is replotted from ref. 39.


--- Page 15 ---
Nature Neuroscience
Article
https://doi.org/10.1038/s41593-024-01574-x
Datasets
All datasets used in the study were collected and published in prior 
studies. Data collection and analysis were not performed blind to the 
conditions of the experiments.
Orientation22: 49 subjects reproduced the orientation of a Gabor 
patch by adjusting a blue strip. Stimuli were distributed uniformly. 
However, on a fraction of the trials, the stimulus had orientation 0, 45, 
90 and 135 degrees; we excluded these trials. On each trial, exposure 
time was varied among 20, 40, 80, 160 and 1,000 ms; no stimulus was 
shown on 10% of trials. We excluded the latter set of trials. The number 
of included trials was 2,208 at each of 20 ms, 40 ms, 80 ms, 160 ms 
and 1,104 at 1,000 ms. In Fig. 3, we follow ref. 17 in omitting the 20 ms 
condition for visualization purposes as responses are too variable to 
be estimated reliably with kernel smoothing; however, these data were 
included in model fitting.
Orientation38: five subjects aligned two comparison dots with the 
average orientation of an array of Gabor patches. Within each array, the 
orientations were sampled from a Gaussian distribution with an s.d. 
of 2 degrees (low stimulus noise) or 14 degrees (high stimulus noise). 
Exposure duration was varied between trials; results are averaged 
across these in Fig. 3, following refs. 17,38. The number of trials was 
2,160 in each of the two stimulus noise conditions.
Perceptual learning of motion direction42: 36 subjects used a 
response bar to indicate the motion direction of a cloud of points. 
Subjects were exposed to two distributions distinguished by colors; 
one distribution was bimodal, the second was flat or trimodal for 18 
subjects each. We analyzed the trials associated with the bimodal distri-
bution. Following ref. 42, we excluded the initial 200 trials of each ses-
sion. We excluded trials where no stimulus was shown (zero contrast). 
There were two contrast levels, modeled as separate levels of sensory 
noise; plotted results are averaged across these in Fig. 4. The number 
of included trials was 11,233 at low contrast and 2,315 at high contrast.
Numerosity41: 300 subjects estimated the number of dots on a 
screen (minimum, 15; maximum, 65). Within each block, all stimuli were 
distributed uniformly within an interval of width 30. At the beginning of 
each block, the prior was made salient by informing the subject about 
the average number in the block. We assumed a separate prior for each 
interval, shared across subjects. Exposure duration was varied between 
100 ms and 2,000 ms. The number of included trials was 35,654 at 
100 ms and 35,730 at 2,000 ms.
Time intervals37: a total of 15 subjects estimated and reproduced 
time intervals (Ready-Set-Go Task) in Experiments 1 and 2. There were 
several contexts differing in whether subjects were asked to repro-
duce the time interval or its 0.75- or 1.5-fold; we considered data only 
from sessions in the identity condition. The number of included trials 
was 8,999.
Color40: ten subjects reproduced color hues by clicking on a color 
wheel in CIELAB space. Stimuli were spaced equally on the wheel. For 
three subjects, there was a delay of 900 ms before the response; we 
fitted separate levels of sensory noise for subjects with or without this 
delay. Figure 6 averages over the two conditions; see Supplementary 
Fig. 49 for results by subject. The number of trials was 18,360.
Central tendency effect in color hue39. Unlike the other datasets, 
this used a 2AFC design; the model was not fitted to trial-by-trial data. 
We include results reported for Experiments 2 and 3; red corresponds 
to the average of the identical conditions 2s in Experiment 2 and None 
in Experiment 3; blue corresponds to 4s in Experiment 2; green cor-
responds to High in Experiment 3. Human data are replotted based 
on39. Following some previous work (for example, refs. 11,24), we 
assumed that subjects first decode ̂θ and then compare it with the refer-
ence, as the basis for the response in the 2AFC task.
Reporting summary
Further information on research design is available in the Nature 
Portfolio Reporting Summary linked to this article.
Data availability
No new experimental datasets were collected in this study. The datasets 
used in this study were all published previously. Datasets collected by 
ref. 41 and ref. 37 are publicly available. Requests for other datasets 
should be directed to the original authors who collected the data.
Code availability
The code, including instructions for using the fitting procedure for 
the Bayesian modeling developed in the paper, is freely available at 
https://gitlab.com/m-hahn/unifying-theory-biases.
Acknowledgements
This research uses data from a number of previously published 
studies. We would like to thank G.-Y. Bae, V. de Gardelle, N. Gekas,  
J. Solomon, R. Polania and C. Ruff for sharing their data with us,  
as well as the authors of several other studies for making their data 
publicly available. We thank A. Huttenlocher and M. Woodford  
for helpful discussions, along with B. Geisler, R. Goris, M. Hayhoe,  
N. Kriegeskorte, K. Kay, S. Gershman, G. de Hollander and L. Colgin 
for comments on earlier versions of this paper. X.-X.W. is supported by 
the startup funds provided by The University of Texas at Austin. M.H. 
gratefully acknowledges Saarland University for providing computing 
resources.
Author contributions
M.H. and X.-X.W. conceived and designed the research. M.H. and 
X.-X.W. developed the theoretical framework. M.H. performed the 
theoretical, numerical and data analyses, with input from X.X.W. M.H. 
and X.-X.W. interpreted the results and wrote the paper.
Competing interests
The authors declare no competing interests.
Additional information
Supplementary information The online version contains supplementary 
material available at https://doi.org/10.1038/s41593-024-01574-x.
Correspondence and requests for materials should be addressed to 
Michael Hahn or Xue-Xin Wei.
Peer review information Nature Neuroscience thanks Pascal Mamassian, 
John Serences and the other, anonymous, reviewer(s) for their 
contribution to the peer review of this work.
Reprints and permissions information is available at  
www.nature.com/reprints.
