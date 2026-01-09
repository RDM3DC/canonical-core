# Curve Memory (CM) and the Curve Memory Alphabet (CMA)

**White Paper 03**  
**Date:** 2026-01-09  
**Status:** Complete draft (self-contained)

---

## Abstract

**Curve Memory (CM)** is a representation and update principle in which information is stored not primarily as discrete symbols or isolated state vectors, but as **the geometry of a trajectory**: tangents, curvature, torsion, and higher derivatives of a path evolving through time or through a latent space. CM is “memory as shape,” enabling robust reconstruction, smoothing, and compression of path-dependent information.

**Curve Memory Alphabet (CMA)** is an application-layer encoding scheme that maps discrete tokens (letters/words/commands) into **base curve primitives** that are then **contextually deformed** by previous/following tokens and by an internal memory state. The result is an expressive, continuous “script” where meaning is carried both by the symbol identity and by the geometry of its deformation chain.

This paper provides a rigorous mathematical formulation for CM and CMA, proposes practical parameterizations for implementation (splines, Fourier series, control points), defines update rules (EMA and reinforce/decay laws), shows how CM naturally produces compression transforms (difference/derivative coding), and gives falsifiable predictions.

---

## 1. Motivation

Many systems fail because they store only **points** while the world is governed by **paths**:

- CAD/CAM and 3D printing toolpaths suffer from discretization error accumulation; the “shape between points” matters.
- Robotics, navigation, and tracking are inherently trajectory problems; continuity constraints encode crucial information.
- Machine learning sequences often behave path-dependently; the route through representation space contains structure.
- Human communication contains more than discrete text; rhythm, emphasis, and context are “continuous deformations.”

Curve Memory addresses this by making **the curve itself** (and its differential geometry) the primary data structure.

---

## 2. Core idea: memory as differential geometry

### 2.1 Curves and features

Let $\gamma:[0,1]\to\mathbb{R}^n$ be a curve (a path in state space).

Define the curve-memory feature bundle up to order $k$:

$$\boxed{\ M_k(s) := \big(\gamma(s),\gamma'(s),\gamma''(s),\ldots,\gamma^{(k)}(s)\big).\ }$$

Interpretations:

- $\gamma$ is the state.
- $\gamma'$ is velocity / tangent.
- $\gamma''$ is acceleration / curvature vector proxy.
- In 3D, torsion emerges from $\gamma',\gamma'',\gamma'''$.

A key point is that **shape information is distributed**: it is not localized to a single coordinate but is encoded by derivatives along the curve.

### 2.2 Curvature and torsion (continuous)

If $\gamma$ is sufficiently smooth and parameterized by arc length $s$, curvature magnitude is

$$\boxed{\ \kappa(s) = \|\gamma''(s)\|.\ }$$

In 3D, torsion can be defined (when $\gamma',\gamma'',\gamma'''$ are well-behaved) by

$$\boxed{\ \tau(s) = \frac{\det(\gamma'(s),\gamma''(s),\gamma'''(s))}{\|\gamma'(s)\times\gamma''(s)\|^2}.\ }$$

CM does not require torsion, but it is a natural extension when 3D shape memory matters.

---

## 3. Curve Memory state: representations you can implement

A practical CM system needs a finite-dimensional state.

### 3.1 Spline control-point representation

Represent each segment of $\gamma$ as a cubic spline with control points $P_0,\ldots,P_m$.

- Memory is stored as the set of control points plus optional derivative constraints.
- Smoothness is enforced by continuity of first and second derivatives at joins.

### 3.2 Fourier / harmonic representation

Represent a periodic or windowed curve by a truncated Fourier series:

$$\gamma(s) \approx a_0 + \sum_{k=1}^K \big(a_k\cos(2\pi k s)+b_k\sin(2\pi k s)\big).$$

CM then stores $(a_k,b_k)$; deformation corresponds to coefficient updates.

### 3.3 Jet (derivative) representation

Store derivatives at anchor points:

$$J_i := \big(\gamma(s_i),\gamma'(s_i),\gamma''(s_i)\big).$$

This representation is convenient for “remember the tangent/curvature at landmarks” behavior.

### 3.4 Discrete path representation

For sampled points $x_0,\ldots,x_N$:

- First difference: $\Delta x_t = x_t-x_{t-1}$ approximates tangent.
- Second difference: $\Delta^2 x_t = x_t-2x_{t-1}+x_{t-2}$ approximates curvature vector.

This is the bridge between CM and compression transforms.

---

## 4. Memory update laws

CM becomes powerful when it is not just a static representation but a dynamical state that updates under stimuli.

### 4.1 EMA (exponential moving average) update

Let $F_t$ be a feature extractor producing a curve feature vector (control points, Fourier coefficients, or jets). Then

$$\boxed{\ M_{t+1} = \lambda M_t + (1-\lambda)F_t,\quad \lambda\in[0,1).\ }$$

This yields smooth tracking with a clear “memory length” controlled by $\lambda$.

### 4.2 Reinforce/decay update (ARP-like)

A continuous-time alternative mirrors reinforce/decay dynamics:

$$\boxed{\ \frac{dM}{dt} = \alpha\,S(t) - \mu\,M(t).\ }$$

- $S(t)$ is a stimulus (novelty, error gradient, curvature event, input magnitude).
- $\alpha$ sets reinforcement strength.
- $\mu$ sets forgetting rate.

This makes CM a general-purpose “geometric memory with time constants.”

### 4.3 Curvature-resisting dynamics (stability intuition)

To encode the idea that “sharp bends resist change,” introduce a stiffness that increases with curvature:

$$\frac{d\gamma}{dt} = -\nabla_\gamma \mathcal{E}(\gamma) + \text{inputs},$$

with energy

$$\boxed{\ \mathcal{E}(\gamma) = \int_0^1 \big( w_1\|\gamma'(s)\|^2 + w_2\|\gamma''(s)\|^2 \big)\,ds.\ }$$

- The $\|\gamma''\|^2$ term penalizes curvature, encouraging smoothness.
- Changing $w_2$ changes how “sticky” shape memory is.

This gives a precise variational backbone for CM: memory is a low-energy deformation path.

---

## 5. Encoding: how CM stores information

### 5.1 History dependence (non-Markovian behavior)

A system is Markovian if the next state depends only on the current state. CM is typically **non-Markovian** because the geometry of the curve reflects accumulated history.

One way to formalize this: define an internal curve state $M_t$ that is updated by EMA or reinforce/decay. The output at time $t$ depends on $M_t$, so the influence of old inputs persists through the geometric state.

### 5.2 Information localization: salience = curvature

A recurring empirical principle is:

- low curvature = redundant / steady regions,
- high curvature = transitions / salient events.

This makes CM naturally compatible with compression: you allocate bits where curvature is high.

---

## 6. CMA: Curve Memory Alphabet as an encoding system

CMA maps discrete symbols into a continuous script.

### 6.1 Base glyphs as curve primitives

Let the alphabet of tokens be $\Sigma$ (letters, words, commands).

Assign each token $a\in\Sigma$ a base curve primitive:

$$\boxed{\ B(a):[0,1]\to\mathbb{R}^n.\ }$$

This base primitive is the “glyph skeleton” (e.g., loops, strokes, peaks).

### 6.2 Contextual deformation

Let the context at position $t$ be $c_t$ (previous tokens, next tokens, and/or a memory state $M_t$). Define a deformation operator

$$\boxed{\ D(\cdot\,;c_t): \{\text{curves}\}\to\{\text{curves}\}.\ }$$

Then the realized glyph for token $a_t$ is

$$\boxed{\ \Gamma_t = D\big(B(a_t); c_t\big).\ }$$

The full CMA message is the concatenation (with smoothing constraints) of $\Gamma_t$.

### 6.3 Composition with smooth joins

Concatenate glyph curves by enforcing continuity constraints at boundaries:

- $C^0$ continuity: endpoints match.
- $C^1$ continuity: tangents match.
- optionally $C^2$: curvature matches.

A practical join rule uses a short transition spline that matches endpoints and tangents.

### 6.4 A minimal deformation model (implementable)

Represent each glyph by control points $P\in\mathbb{R}^{m\times n}$. Let the context vector be $u(c_t)\in\mathbb{R}^d$.

Define

$$P_t = P^{(0)}(a_t) + A\,u(c_t)$$

where $A\in\mathbb{R}^{(m\cdot n)\times d}$ is a learned or designed matrix.

This is the simplest “context bends the glyph” mechanism.

---

## 7. Decoding CMA (recovering text from curves)

CMA can be used purely artistically, but it can also be made decodable.

### 7.1 Template matching decoder

Given an observed curve segment $\hat\Gamma$, decode by:

1. Normalize (translation/scale/rotation) to a canonical frame.
2. Compute distance to each template family (token + deformation range).

A common distance is elastic shape matching (e.g., curvature profile distance):

$$d(\hat\Gamma,\Gamma) = \int_0^1 \|\kappa_{\hat\Gamma}(s)-\kappa_{\Gamma}(s)\|^2\,ds.$$

Pick the token minimizing distance.

### 7.2 Probabilistic decoding (HMM-like)

Because deformation depends on context, a decoder can model token sequences:

- hidden state = token,
- observation = curve segment features,
- transition probabilities encode language/command structure.

This turns CMA into a legitimate communications channel.

---

## 8. Compression: CM as a transform family

The CM lens suggests that many signals become compressible after transforming them into “low-curvature” coordinates.

### 8.1 First-difference (delta) transform

For bytes $b_0,\ldots,b_{N-1}$ (interpreted as points on a 1D curve), define

$$d_0=b_0,\quad d_t=(b_t-b_{t-1})\bmod 256.$$

If the underlying data has local smoothness, the deltas concentrate near zero and compress well under entropy coding.

### 8.2 Higher-order differences

Second difference

$$\Delta^2 b_t = b_t - 2b_{t-1} + b_{t-2}$$

corresponds to a discrete curvature proxy. Many structured sequences have sparse second differences, which can be exploited.

### 8.3 Segment-wise polynomial / spline transforms

For numeric sequences, fit short segments by low-degree polynomials or splines and encode residuals. The “curve memory” state stores segment coefficients; residuals are typically small.

This is a principled version of: “store the curve, not the points.”

---

## 9. Applications

### 9.1 CAD/CAM and 3D printing

CM supports:

- reducing discretization drift by storing tangent/curvature constraints,
- adaptive segmentation (more points where curvature high),
- toolpath smoothing with curvature-aware penalties.

### 9.2 Robotics and navigation

CM provides a natural state for:

- trajectory priors,
- motion smoothing,
- map/route memory beyond waypoints.

### 9.3 Machine learning memory beyond weights

CM can be used to store:

- the trajectory of latent states,
- curvature events that mark regime transitions,
- a differentiable memory object that regularizes sequence models.

### 9.4 Communication / art interface (CMA)

CMA can be used as:

- an expressive script where symbols carry “vibe” via deformation,
- a channel for compact semantic content (token) + prosody-like content (shape),
- an interface for creative visual language.

---

## 10. Predictions and falsifiers

### 10.1 Predictions

1. If CM is used in toolpath reconstruction, enforcing $C^1$ or $C^2$ continuity with curvature penalties should reduce cumulative geometric error compared to point-only interpolation.
2. If CMA is used with context deformation, repeated phrases should generate recognizable families of curve motifs that remain similar under normalization.
3. In compression tasks, first- and second-difference transforms should concentrate mass near small magnitudes on locally smooth data, improving entropy-coding efficiency.

### 10.2 Falsifiers (what would contradict the framework)

1. If a dataset has no local smoothness structure, delta/curvature transforms will not reduce entropy; CM-based compression should not help.
2. If CMA glyph deformation is claimed to carry semantic context, but normalized curve features show no systematic variation with context, then the deformation model is not capturing context.
3. If CM claims improved reconstruction from fewer samples, but curvature-aware reconstructions do not outperform baseline spline fits under comparable constraints, then the CM advantage is not present for that domain.

---

## 11. Implementation checklist (minimum viable CM/CMA)

### 11.1 CM core

- Choose representation: control points, Fourier coefficients, or derivative jets.
- Choose update: EMA ($\lambda$) or reinforce/decay ($\alpha,\mu$).
- Choose smoothing energy: at minimum, penalize $\|\gamma''\|^2$.

### 11.2 CMA core

- Define base glyphs $B(a)$ for tokens.
- Define a context vector $u(c_t)$.
- Define deformation $D$ (start linear in context; upgrade later).
- Define join constraints ($C^1$ recommended).

### 11.3 Decoder (optional)

- Start with template matching on curvature profiles.
- Add sequence modeling if needed.

---

## Appendix A: quick reference formulas

- Curve-memory jet: $M_k(s)=(\gamma,\gamma',\ldots,\gamma^{(k)})$
- Curvature (arc-length): $\kappa=\|\gamma''\|$
- EMA update: $M_{t+1}=\lambda M_t+(1-\lambda)F_t$
- Reinforce/decay: $dM/dt=\alpha S(t)-\mu M$
- Smoothness energy: $\mathcal{E}(\gamma)=\int (w_1\|\gamma'\|^2+w_2\|\gamma''\|^2)ds$
- CMA glyph: $\Gamma_t=D(B(a_t);c_t)$
- Delta transform (bytes): $d_0=b_0$, $d_t=(b_t-b_{t-1})\bmod 256$
