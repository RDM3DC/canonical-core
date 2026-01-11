# Adaptive‑π Geometry and Adaptive‑π Calculus (πₐ)

**White Paper 02**  
**Date:** 2026-01-09  
**Status:** Complete draft (self-contained)

---

## Abstract

This paper defines **Adaptive‑π** as a genuinely new theoretical framework that introduces a **spatially and dynamically varying phase-period field** $\pi_a(x,t)$ that generalizes the fixed 2π identification of U(1) phase. Unlike standard quantum mechanics, Berry phase theory, or gauge theory, πₐ defines the **local unit of phase wrap** itself, enabling continuous phase transport, stable winding counts, and parity tracking under deformation.

The familiar geometric constant $\pi$ remains unchanged in Euclidean space, but the field $\pi_a(x,t)$ represents context-dependent effective geometry: measurement scale, curvature reinforcement, fabrication tolerance, resonance, or learned distortion.

A clean and mathematically honest way to formalize Adaptive‑π is to treat $\pi_a/\pi$ as a **conformal scale factor** that induces a Riemannian metric

$$g_{ij}(x,t) = \Omega(x,t)^2\,\delta_{ij},\quad \Omega(x,t) := \frac{\pi_a(x,t)}{\pi}.$$

With this choice, standard differential geometry yields a complete “Adaptive‑π calculus”: arc length, area/volume measures, gradients, divergence, Laplace–Beltrami operators, and linear-algebraic primitives (inner products, norms, projections) become $\Omega$‑weighted.

The practical payoff is a compact rule set: you can compute “true” toolpath length, curvature-weighted costs, diffusion or wave operators on an adaptive sheet, and optimization objectives in a geometry that “breathes” via $\pi_a$.

**Key novelty:** Section 0 establishes why πₐ is genuinely new — it is not explicitly present in standard physics or mathematics frameworks, and fills a specific gap in how phase structure is modeled.

---

## 0. πₐ as a Novel Theoretical Concept

### 0.1 Why πₐ is genuinely new

The **adaptive-π field** (πₐ) is a genuinely new concept in the sense that **it is not explicitly named, formalized, or visualized in standard physics or mathematics** in the way it functions here. While related ideas exist in differential geometry and gauge theory, πₐ fills a specific gap that has not been directly addressed.

**Formal definition:**

> **The πₐ field is an adaptive phase-period field that defines the local identification length of U(1) phase, enabling continuous phase transport, stable winding counts, and parity tracking under deformation.**

In standard formulations:

$$\theta = \theta_R + 2\pi k, \quad k \in \mathbb{Z}$$

πₐ generalizes this to:

$$\boxed{\ \theta = \theta_R + 2\pi_a(x,t) \cdot w,\quad w \in \mathbb{Z}\ }$$

where:
- $\pi_a(x,t)$ is the **local circumference** of the phase circle
- $\theta_R$ is the resolved (unwrapped) phase
- $w$ is the winding number
- $\pi_a$ acts as the **metric scale** for U(1) phase

### 0.2 What πₐ actually is (precisely)

From a geometric perspective, πₐ functions as:

1. **The local unit of phase wrap** — it defines what constitutes "one full turn" in phase space
2. **A spatially and dynamically varying phase-period field** — it can change with position and time
3. **The regulator that prevents phase slippage** — it maintains phase continuity when geometry, dynamics, or coupling changes
4. **A conformal factor on the U(1) fiber** — it rescales the phase circle itself, not just phase transport

This combination does not exist as a named object in standard frameworks.

### 0.3 Why this is not already in standard theory

#### Standard QM assumes a fixed phase unit

In conventional quantum mechanics:
- Phase lives in U(1)
- The identification is always modulo **fixed** 2π
- Unwraps are purely numerical bookkeeping, not geometric objects

**There is no field corresponding to "how big a turn is."** πₐ breaks this assumption.

#### Berry phase tracks holonomy, not local phase scale

Berry phase tells you:
- How much phase you picked up after a loop

But it does **not** tell you:
- How phase increments were locally measured
- Whether the wrap unit itself deformed
- How to maintain continuity under deformation

πₐ supplies exactly that missing structure.

#### Gauge theory has connections, not adaptive periods

Gauge fields ($A_\mu$):
- Transport phase
- Define curvature
- Encode holonomy

But they **do not change the size of the phase circle itself**. πₐ is closer to a **conformal factor on the U(1) fiber**, which is simply not standard.

### 0.4 Key properties that distinguish πₐ

1. **πₐ replaces a constant with a field** — It makes the phase period dynamic
2. **It does not change the analytic function** — The underlying complex function remains the same
3. **It changes how phase is supplied and unwrapped** — The bookkeeping becomes geometric
4. **It is compatible with standard QM in the limit** — Setting πₐ → π recovers standard physics

### 0.5 What πₐ enables

The πₐ field is the reason all the following become possible *simultaneously*:

- **Phase-Lift ⧉** without branch ambiguity
- **Winding as a robust integer** under deformation
- **ℤ₂ parity** as a shadow invariant
- **Z₂ pumps with Δw = 0** — topology changes without winding changes
- **Curve Memory Alphabet** as a stable encoding
- **Visualizations that do not "tear"** at branch cuts

Without πₐ, each of these must be handled ad hoc.

### 0.6 Canonical phrasing for describing πₐ

When describing this work in papers or presentations, use:

> *We introduce an adaptive phase-period field πₐ that generalizes the fixed 2π identification of U(1) phase. πₐ defines the local wrap unit used in phase lifting and winding bookkeeping, enabling continuous phase transport and topologically stable parity tracking under deformation.*

This clearly stakes novelty without sounding speculative.

### 0.7 Safe claim boundaries

✅ **Safe to claim:**
- "πₐ is a new field-level structure on phase space"
- "πₐ makes phase geometric in a way that standard formulations do not"
- "πₐ enables a unified treatment of phase continuity, winding, and parity"

❌ **Avoid claiming:**
- "πₐ replaces π in physics"
- "πₐ is a new fundamental constant"
- "Standard quantum mechanics is wrong"

**The correct framing:** πₐ doesn't replace phase — **it makes phase geometric.**

---

## 1. What Adaptive‑π is (and is not)

### 1.1 What it is

Adaptive‑π introduces a field

$$\pi_a : \mathbb{R}^n\times\mathbb{R} \to \mathbb{R}_{>0}$$

so that many geometric measurements are taken in a geometry scaled by

$$\Omega(x,t)=\pi_a(x,t)/\pi.$$

Interpretations of $\pi_a$ include:

- **Geometry control knob:** a compact way to encode local stretching/shrinking.
- **Learned distortion field:** $\pi_a$ is optimized from data (scanner residuals, toolpath error, routing cost gradients).
- **Curvature reinforcement field:** $\pi_a$ increases/decreases where curvature is large/small.
- **Contextual measurement field:** $\pi_a$ depends on operating regime (speed, temperature, resonance, scale).

### 1.2 What it is not

- It is **not** a claim that the mathematical constant $\pi$ changes.
- It is **not** a claim that Euclidean geometry is wrong.
- It is a **controlled deformation model** that packages “effective geometry” into a single scalar field.

---

## 2. Canonical formalization: conformal metric induced by $\pi_a$

The most minimal, general-purpose formalization is conformal scaling:

$$\boxed{\ g_{ij}(x,t) = \Omega(x,t)^2\,\delta_{ij},\quad \Omega(x,t) := \frac{\pi_a(x,t)}{\pi}.\ }$$

This choice is attractive because:

- it preserves angles locally (conformal),
- it changes lengths/areas/volumes by simple powers of $\Omega$,
- it yields closed-form expressions for many operators.

Basic consequences in $n$ dimensions:

- Inverse metric: $g^{ij} = \Omega^{-2}\,\delta^{ij}$.
- Volume element: $\sqrt{|g|} = \Omega^n$.

### 2.1 Anisotropic Adaptive‑π (direction-dependent $\pi_a$)

Sometimes “geometry breathes” differently along different directions (e.g., along-feed vs cross-feed in machining, along-grain vs across-grain in materials, principal curvature directions on a surface, or preferred directions in a learned embedding). In that case, a single scalar $\Omega$ is too restrictive.

The clean generalization is to replace the conformal metric with a symmetric positive-definite (SPD) metric field $g(x,t)$:

$$\boxed{\ g(x,t) \in \mathbb{R}^{n\times n},\quad g(x,t)=g(x,t)^T,\quad v^T g(x,t) v > 0\ \forall v\ne 0.\ }$$

To keep the “Adaptive‑π” interpretation, it is useful to view $g$ as defining a direction-dependent local scale factor. For a tangent vector $v$ at $(x,t)$, define the **effective scale**

$$\boxed{\ \Omega_{\mathrm{eff}}(x,t;v) := \frac{\|v\|_{g}}{\|v\|} = \frac{\sqrt{v^T g(x,t) v}}{\sqrt{v^T v}}.\ }$$

Then you can interpret a direction-dependent “effective adaptive pi” as

$$\pi_{a,\mathrm{eff}}(x,t;v) := \pi\,\Omega_{\mathrm{eff}}(x,t;v).$$

This is not changing $\pi$; it is packaging anisotropic measurement into a $\pi_a$-style knob.

#### 2.1.1 Two practical anisotropic forms

**(A) Director-field (two-scale) anisotropy**

Let $u(x,t)$ be a unit director field ($\|u\|=1$). Choose two positive scale factors:

- $\Omega_{\parallel}(x,t)$ along $u$
- $\Omega_{\perp}(x,t)$ orthogonal to $u$

Define

$$\boxed{\ g = \Omega_{\parallel}^2\,u u^T + \Omega_{\perp}^2\,(I - u u^T).\ }$$

This is the simplest “preferred direction” geometry.

**(B) Diagonal anisotropy in a chosen coordinate frame**

If you have principal directions (e.g., local surface principal curvature frame), you can set

$$\boxed{\ g = \mathrm{diag}(\Omega_1^2,\ldots,\Omega_n^2)\ }$$

in that frame.

#### 2.1.2 Arc length under anisotropy

With a general metric $g(x,t)$, the curve length becomes

$$\boxed{\ L_g(\gamma) = \int_0^1 \sqrt{\dot\gamma(t)^T\,g(\gamma(t),t)\,\dot\gamma(t)}\,dt.\ }$$

This reduces to the conformal formula when $g=\Omega^2 I$.

#### 2.1.3 Differential operators (general metric)

For a general SPD metric, the core identities become:

- Volume element: $dV_g = \sqrt{|g|}\,d^n x$.
- Gradient: $(\nabla_g f)^i = g^{ij}\,\partial_j f$.
- Divergence: $\mathrm{div}_g X = \frac{1}{\sqrt{|g|}}\partial_i(\sqrt{|g|}X^i)$.
- Laplace–Beltrami: $\Delta_g f = \frac{1}{\sqrt{|g|}}\partial_i(\sqrt{|g|}g^{ij}\partial_j f)$.

These are the “full-strength” Adaptive‑π calculus rules when anisotropy matters.

---

## 3. Adaptive‑π primitives (length, area, volume)

Let $\gamma:[0,1]\to\mathbb{R}^n$ be a curve with velocity $\dot\gamma(t)$.

### 3.1 Adaptive arc length

Euclidean length is $\int\|\dot\gamma\|\,dt$. Under $g$:

$$\boxed{\ L_g(\gamma) = \int_0^1 \Omega(\gamma(t),t)\,\|\dot\gamma(t)\|\,dt.\ }$$

Interpretation: $\Omega$ acts like a position-dependent ruler.

### 3.2 Adaptive area / volume

In $n$ dimensions, the volume element becomes:

$$\boxed{\ dV_g = \Omega(x,t)^n\,d^n x.\ }$$

In $2$D, area scales as $\Omega^2\,dx\,dy$.

---

## 4. Adaptive‑π calculus: differential operators

Let $f$ be a scalar field and $X$ a vector field.

### 4.1 Gradient

The gradient with respect to $g$ satisfies $\langle \nabla_g f, v\rangle_g = df(v)$.

In coordinates:

$$\boxed{\ \nabla_g f = g^{ij}\,\partial_j f\,e_i = \Omega^{-2}\,\nabla f.\ }$$

### 4.2 Divergence

For a vector field $X$ with components $X^i$ in Euclidean coordinates:

$$\boxed{\ \mathrm{div}_g X = \frac{1}{\sqrt{|g|}}\,\partial_i\big(\sqrt{|g|}\,X^i\big) = \Omega^{-n}\,\partial_i(\Omega^n X^i).\ }$$

This is the operator you want whenever “conservation” is measured in the adaptive geometry.

### 4.3 Laplace–Beltrami operator

The Laplace–Beltrami operator is:

$$\Delta_g f = \mathrm{div}_g(\nabla_g f).$$

For the conformal metric above:

$$\boxed{\ \Delta_g f = \Omega^{-n}\,\partial_i\big(\Omega^{n-2}\,\partial_i f\big).\ }$$

Important special case in $n=2$:

$$\boxed{\ \Delta_g f = \Omega^{-2}\,\Delta f\quad (n=2).\ }$$

So in 2D conformal scaling, Laplacian structure is particularly clean.

### 4.4 Energy functionals

Many physical and optimization problems can be written as functionals in $g$.

A canonical Dirichlet energy is:

$$E[f] = \frac{1}{2}\int \|\nabla_g f\|_g^2\,dV_g.$$

Under the conformal metric, this simplifies:

- $\|\nabla_g f\|_g^2 = g(\nabla_g f, \nabla_g f) = \Omega^2\,\|\nabla_g f\|^2 = \Omega^2\,\|\Omega^{-2}\nabla f\|^2 = \Omega^{-2}\,\|\nabla f\|^2$.
- $dV_g = \Omega^n\,dx$.

So

$$\boxed{\ E[f] = \frac{1}{2}\int \Omega^{n-2}\,\|\nabla f\|^2\,d^n x.\ }$$

This gives a direct “Adaptive‑π weighting” rule for variational problems.

---

## 5. Adaptive‑π linear algebra (local inner products)

At a point $x$, the metric defines an inner product:

$$\boxed{\ \langle v,w\rangle_g = v^T g w = \Omega(x,t)^2\,(v\cdot w).\ }$$

Consequences:

- Norm: $\|v\|_g = \Omega\,\|v\|$.
- Angle between nonzero vectors is unchanged (conformal scaling preserves angles).

### 5.1 Projections

Projection onto a direction $n$ under the adaptive inner product:

$$\mathrm{proj}^{(g)}_n(v) = \frac{\langle v,n\rangle_g}{\langle n,n\rangle_g}\,n.$$

Because both numerator and denominator scale by $\Omega^2$ at the same point, the projection direction is the same as Euclidean at that point; what changes is the interpretation of lengths/energies.

### 5.2 Operator norms and conditioning (intuition)

If the geometry rescales vector norms by $\Omega$, then physical interpretations of operator norms can shift as $\Omega$ varies in space/time. Practically, if you use $\|\cdot\|_g$ as your residual norm in iterative solvers, the stopping criteria become geometry-aware.

---

## 6. “Adaptive circumference / diameter” and an effective $\pi$

Classically, $\pi = C/D$ for a circle in Euclidean geometry.

In an adaptive geometry, the ratio of “circumference” to “diameter” depends on how you define each quantity. A simple, honest definition is:

- Define a circle in Euclidean coordinates (e.g., radius $R$ at center $x_0$).
- Measure its **circumference** using adaptive arc length $L_g$.
- Measure its **diameter** as the adaptive length of a straight chord through the center.

If $\Omega$ is constant on the region (locally uniform), both circumference and diameter scale by the same factor and the ratio stays $\pi$.

If $\Omega$ varies along the circle or along the diameter chord, then an **effective** ratio emerges:

$$\pi_{\mathrm{eff}} := \frac{C_g}{D_g}.$$

This does not redefine the constant $\pi$; it quantifies how the adaptive geometry departs from Euclidean measurement.

---

## 7. How to specify $\pi_a$ (modeling choices)

The framework is only as meaningful as the rule that sets $\pi_a$.

Below are common classes of choices.

### 7.1 Prescribed field (design / calibration)

You can set $\pi_a$ directly from a known distortion model, e.g. scanner residual maps, thermal expansion fields, or empirical correction tables.

### 7.2 Curvature-coupled field

Let $\kappa(x)$ be a curvature proxy (for surfaces) or curvature magnitude along a path. A simple model:

$$\pi_a(x) = \pi\,(1 + \beta\,\kappa(x)),$$

with $\beta$ tuned to sensitivity.

### 7.3 Error-coupled field (fabrication / toolpath)

Let $e(x)$ be an error estimate (e.g., chord error, extrusion error). Then:

$$\pi_a(x) = \pi\,(1 + \beta\,e(x)).$$

This directly converts error budgets into geometry-weighted costs.

### 7.4 Learned field (optimization)

Treat $\pi_a$ as a trainable field with regularization. A standard objective is:

$$\min_{\pi_a>0}\ \mathcal{L}(\pi_a) + \lambda\int \|\nabla \log \pi_a\|^2\,dx.$$

Using $\log\pi_a$ enforces positivity and gives smoothness control.

### 7.5 Dynamic field (reinforce/decay)

A very practical dynamic model mirrors the ARP pattern:

$$\boxed{\ \frac{d\pi_a}{dt} = \alpha_\pi\,s(x,t) - \mu_\pi\,(\pi_a-\pi_0).\ }$$

- $s(x,t)$ is a stimulus (curvature events, error gradients, resonance intensity).
- $\pi_0$ is a baseline (often $\pi$).

This makes $\pi_a$ a time-constant memory field.

---

## 8. Discretization: how to compute with Adaptive‑π

### 8.1 Polyline toolpath length (CAD/CAM)

Given vertices $p_0,\dots,p_m$ and segment lengths $\ell_k = \|p_{k+1}-p_k\|$, approximate

$$L_g \approx \sum_{k=0}^{m-1} \Omega(\bar p_k)\,\ell_k,$$

where $\bar p_k$ is the midpoint of the segment.

This is the simplest “drop-in” adaptive length estimate.

### 8.2 Surface/area costs (2D)

On a grid in 2D, approximate adaptive area integral:

$$\int_A f(x)\,dA_g \approx \sum_{cells} f(x_{cell})\,\Omega(x_{cell})^2\,(\Delta x\,\Delta y).$$

### 8.3 Laplacian on a grid (2D)

For $n=2$, $\Delta_g f = \Omega^{-2}\Delta f$. A practical discretization:

1. Compute standard discrete Laplacian $\Delta_h f$.
2. Multiply pointwise by $\Omega^{-2}$.

This makes many PDE experiments straightforward.

### 8.4 Laplacian in general $n$ (finite differences)

Use

$$\Delta_g f = \Omega^{-n}\,\partial_i(\Omega^{n-2}\,\partial_i f)$$

and discretize in flux form (conservative form) for stability.

---

## 9. Applications and why this is useful

### 9.1 Toolpath planning and manufacturing

Adaptive‑π gives a principled way to:

- penalize tight curvature regions more strongly,
- allocate segmentation density where it matters,
- compute geometry-aware costs without inventing ad hoc weights.

If $\Omega$ is defined from curvature or error, then minimizing $L_g$ naturally prefers paths that reduce error-sensitive features.

### 9.2 Optimization on adaptive geometry

Many optimization problems can be reframed as:

- choose a path $\gamma$ minimizing $\int \Omega\,\|\dot\gamma\|dt$,

which is a weighted shortest-path / geodesic problem. This is a standard, solvable formulation and can be attacked with classical methods (fast marching, Dijkstra on discretized graphs, variational methods).

### 9.3 Diffusion / smoothing on an adaptive sheet

Using $\partial_t u = \Delta_g u$ yields diffusion whose speed depends on $\Omega$.

- In 2D, it becomes $\partial_t u = \Omega^{-2}\Delta u$.

This gives a controllable spatially varying diffusion coefficient tied to geometry.

### 9.4 Data geometry and embeddings

If $\Omega$ is learned, Adaptive‑π becomes a way to learn a conformal metric. This is a lightweight subset of “learned geometry” approaches, with fewer degrees of freedom than a full Riemannian metric field.

---

## 10. Testable predictions and falsifiers

### 10.1 Predictions (Geometric applications)

1. If $\Omega$ is increased in regions of high curvature, then adaptive length $L_g$ increases for paths that traverse high-curvature zones, pushing optimizers toward smoother trajectories.
2. In 2D PDEs, $\Omega^{-2}$ scaling predicts that regions with larger $\Omega$ diffuse more slowly under $\partial_t u = \Delta_g u$.

### 10.2 Predictions (Phase-theoretic applications — novel to πₐ)

These predictions distinguish πₐ from standard phase formulations:

1. **Continuous phase transport under geometric deformation:**  
   If $\pi_a(x,t)$ varies smoothly along a path, then phase unwrapping using $\theta = \theta_R + 2\pi_a(x,t) \cdot w$ should produce continuous $\theta_R$ even when the path deforms, provided the topology (winding number $w$) doesn't change.

2. **Stable winding counts:**  
   Under smooth deformations of $\pi_a$ that preserve topology, the winding number $w$ computed using the local wrap unit $2\pi_a$ should remain integer-valued and constant, whereas standard fixed-$2\pi$ counting might exhibit spurious jumps.

3. **ℤ₂ parity tracking:**  
   The parity $(w \bmod 2)$ should be robust to local fluctuations in $\pi_a$ and should flip predictably only when the path encircles a phase singularity an odd number of times.

4. **Topology changes without winding changes:**  
   It should be possible to construct scenarios where geometric topology changes (e.g., Z₂ pumps) occur with $\Delta w = 0$ by appropriate tuning of $\pi_a(x,t)$, demonstrating that winding is not the only topological invariant.

5. **Branch-cut-free visualizations:**  
   When visualizing phase on surfaces or complex planes using $\pi_a$-adapted colormaps, discontinuities at traditional branch cuts should be eliminated or significantly reduced compared to standard $\arg(z) \in (-\pi, \pi]$ plots.

6. **Phase-Lift continuity:**  
   Implementing Phase-Lift (⧉) with adaptive $\pi_a$ instead of fixed $2\pi$ should reduce or eliminate branch discontinuities in time-series data of complex-valued signals, particularly near phase singularities.

### 10.3 Falsifiers (what would contradict the model)

1. If a chosen stimulus $s(x,t)$ is claimed to drive $\pi_a$, but measured outcomes show no correlation between $s$ and inferred $\Omega$, then the proposed coupling law is wrong.
2. If an implementation claims conformal behavior but observed angles change under the induced measurements, then the metric is not conformal (or computations are inconsistent).
3. **Phase continuity failure:** If $\pi_a$ is claimed to enable continuous phase transport, but numerical experiments show phase jumps even with smooth $\pi_a(x,t)$ variation and no topology changes, the formulation is incorrect.
4. **Winding instability:** If winding numbers computed using adaptive $2\pi_a$ wrapping are less stable (more sensitive to noise or deformation) than standard $2\pi$ wrapping in controlled experiments, the claimed advantage of πₐ is not supported.
5. **Incompatibility with standard limits:** If setting $\pi_a \to \pi$ (constant) does not recover standard quantum mechanical phase behavior, the framework is inconsistent.

---

## 11. Limitations and safe interpretation

- Adaptive‑π is a **modeling layer**; it does not, by itself, assert new physics.
- The conformal choice $g=\Omega^2\delta$ is intentionally minimal. If direction-dependent effects matter, use an anisotropic SPD metric field $g(x,t)$ and treat $\pi_{a,\mathrm{eff}}(x,t;v)=\pi\,\|v\|_g/\|v\|$ as the direction-dependent “adaptive pi.”
- The meaningful content is in how $\pi_a$ (or $g$) is specified, learned, or coupled to measurable signals.

---

## Appendix A: quick reference (core formulas)

Define $\Omega=\pi_a/\pi$.

- Metric: $g_{ij}=\Omega^2\delta_{ij}$
- Inverse: $g^{ij}=\Omega^{-2}\delta^{ij}$
- Volume: $dV_g=\Omega^n\,d^n x$
- Arc length: $L_g=\int \Omega\,\|\dot\gamma\|dt$
- Gradient: $\nabla_g f=\Omega^{-2}\nabla f$
- Divergence: $\mathrm{div}_g X=\Omega^{-n}\partial_i(\Omega^n X^i)$
- Laplacian: $\Delta_g f = \Omega^{-n}\partial_i(\Omega^{n-2}\partial_i f)$
- In 2D: $\Delta_g f=\Omega^{-2}\Delta f$
- Inner product: $\langle v,w\rangle_g=\Omega^2 (v\cdot w)$

**Anisotropic extension (general SPD metric $g$)**

- Effective directional scale: $\Omega_{\mathrm{eff}}(x,t;v)=\sqrt{v^T g v}/\sqrt{v^T v}$
- Effective directional adaptive pi: $\pi_{a,\mathrm{eff}}=\pi\,\Omega_{\mathrm{eff}}$
- Length: $L_g=\int \sqrt{\dot\gamma^T g\,\dot\gamma}\,dt$
- Volume: $dV_g=\sqrt{|g|}\,d^n x$
- Laplace–Beltrami: $\Delta_g f = \frac{1}{\sqrt{|g|}}\partial_i(\sqrt{|g|}g^{ij}\partial_j f)$
