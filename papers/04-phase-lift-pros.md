# Phase-Lift (⧉), PR-Root (⧉√), and Phase-Resolved Operators (PROs)

**White Paper 04**  
**Date:** 2026-01-09  
**Status:** Complete draft (self-contained)

---

## Abstract

Multi-valued complex functions (square root, logarithm, fractional powers) are single-valued only after a **branch choice**. In practice, most errors and “mysteries” come from making that choice implicitly, then forgetting it matters.

This paper defines a minimal, deterministic convention called **Phase-Lift** (operator **⧉**) that evaluates multi-valued functions on a **phase-resolved (history-resolved) cover** by explicitly tracking a resolved argument $\theta_R$ via phase unwrapping. The canonical example is **PR-Root**, written **⧉√**, which selects a specific branch of the square root given a phase reference or a continuity rule along a path.

We formalize Phase-Lift, define a family of **Phase-Resolved Operators (PROs)** (⧉√, ⧉log, ⧉(z^a), etc.), provide algorithms and implementation guidance, clarify what claims are and are not being made, and state testable behaviors (including monodromy under loops around the origin).

---

## 1. Motivation and framing

Complex analysis gives perfectly consistent answers about multi-valued functions, but the consistency is conditional:

- A function like $\sqrt{z}$ or $\log z$ is not single-valued on $\mathbb{C}\setminus\{0\}$.
- Any numeric routine must pick a branch cut and a principal branch (often silently).
- When a quantity evolves in time (or along a curve in the complex plane), the “correct” branch is usually the one that preserves continuity, not the principal one.

**Phase-Lift** is a deliberately small layer of bookkeeping that makes this explicit.

### 1.1 What this is

- A notational and computational convention for **explicit branch selection**.
- A tool for keeping derivations honest when sign/branch flips matter.
- A deterministic way to get continuity along a path by using a stored phase state.

### 1.2 What this is not

- Not a new number system.
- Not an attempt to “change” $i$.
- Not a claim that physics is altered by rewriting $i$ as $\sqrt{-1}$.

Phase-Lift is about **declaring the convention** used whenever a multi-valued function appears.

---

## 2. Background: multi-valuedness comes from phase

Write a nonzero complex number as $z = r e^{i\theta}$ with $r>0$ and $\theta = \arg(z)$. The phase is only defined modulo $2\pi$:

$$\theta \equiv \theta + 2\pi k, \quad k\in\mathbb{Z}.$$

This is the root cause of multi-valuedness:

- Square root:
  $$\sqrt{z} = \pm \sqrt{r}\,e^{i\theta/2}$$
  with $\theta\equiv\theta+2\pi k$ producing two values.

- Complex logarithm:
  $$\log z = \ln r + i\theta$$
  with $\theta\equiv\theta+2\pi k$ producing infinitely many values.

A “principal” branch corresponds to restricting $\theta$ to an interval such as $(-\pi,\pi]$.

---

## 3. Phase-Lift (⧉): the umbrella operator

Phase-Lift is the rule:

> Evaluate a multi-valued function by first resolving the phase $\theta$ into a specific real value $\theta_R$ (using a declared rule), then use that $\theta_R$ inside the function.

### 3.1 Minimal formal definition

Let $f$ be a complex function whose multi-valuedness is induced by the ambiguity of $\arg(z)$. Define

$$\boxed{\ (\,\,\,⧉f\,\,\,)(z;\theta_{\mathrm{ref}}) := f\big(z\big)\ \text{computed using}\ \theta_R = \mathrm{unwrap}(\arg z;\theta_{\mathrm{ref}}).\ }$$

- $\theta_{\mathrm{ref}}$ is a real reference phase.
- $\mathrm{unwrap}(\theta;\theta_{\mathrm{ref}})$ selects the representative of $\theta+2\pi\mathbb{Z}$ that is “closest” to $\theta_{\mathrm{ref}}$.

This definition is intentionally minimal: it does not require heavy Riemann surface machinery to be useful.

### 3.2 A practical unwrapping rule

A common deterministic unwrapping convention is:

$$\boxed{\ \mathrm{unwrap}(\theta;\theta_{\mathrm{ref}}) := \theta + 2\pi\,\mathrm{round}\Big(\frac{\theta_{\mathrm{ref}}-\theta}{2\pi}\Big).\ }$$

This chooses the $2\pi$-shift of $\theta$ that minimizes $|\theta_R-\theta_{\mathrm{ref}}|$.

### 3.3 Path continuity (history-resolved evaluation)

For time series or path-parameterized inputs $z(t)$, we often want continuity:

- Keep a state variable $\theta_{\mathrm{prev}}$.
- At each step, unwrap the new $\arg z(t)$ against $\theta_{\mathrm{prev}}$.
- Update $\theta_{\mathrm{prev}} \leftarrow \theta_R$.

This produces a **history-resolved phase** $\theta_R(t)$ which is continuous except when the path crosses through $z=0$ (where phase is undefined).

### 3.4 Connection to adaptive-π field (πₐ)

The unwrapping rule above assumes a **fixed** $2\pi$ identification of phase. This is standard in most contexts, but can be generalized:

In **Paper 02 (Adaptive-π Geometry)**, we introduce a phase-period field $\pi_a(x,t)$ that allows the "size" of one full phase turn to vary with position and time. The phase relation becomes:

$$\theta = \theta_R + 2\pi_a(x,t) \cdot w, \quad w \in \mathbb{Z}$$

where $w$ is the winding number.

**Key distinction:**
- **Standard Phase-Lift (this paper):** Uses fixed $2\pi$ wrapping, focuses on branch continuity
- **Adaptive-π (Paper 02):** Generalizes the wrap unit itself, enabling topology changes without winding changes

When $\pi_a \to \pi$ (constant), the adaptive-π formulation reduces to the standard Phase-Lift presented here. The adaptive-π field is particularly important for:
- Stable winding counts under geometric deformation
- ℤ₂ parity tracking
- Curve Memory Alphabet encoding
- Visualizations that avoid branch-cut artifacts

For most practical Phase-Lift applications, the fixed $2\pi$ unwrapping presented here is sufficient.

---

## 4. PR-Root (⧉√): the phase-resolved square root

### 4.1 Definition

Given $z\neq 0$, write $z=r e^{i\theta}$. Choose a resolved phase $\theta_R$ by unwrapping $\theta$ relative to $\theta_{\mathrm{ref}}$ (or relative to a stored phase-state along a path). Define

$$\boxed{\ \ ⧉\sqrt{z\,;\,\theta_{\mathrm{ref}}} := \sqrt{r}\,e^{i\theta_R/2}.\ }$$

Once the phase-resolution rule is chosen, this returns **one value** (no explicit $\pm$) because the branch selection is encoded by $\theta_R$.

### 4.2 The “⧉√(-1) resolves i” shorthand

For $z=-1$, the argument can be resolved as $\theta_R=\pi$ or $\theta_R=-\pi$ (or shifted by $2\pi k$). Under PR-Root:

- If $\theta_R = \pi$, then $⧉\sqrt{-1} = e^{i\pi/2} = i$.
- If $\theta_R = -\pi$, then $⧉\sqrt{-1} = e^{-i\pi/2} = -i$.

So “resolving $i$” means pinning down the half-angle convention.

### 4.3 Key behavior: continuity vs monodromy

Two facts can both be true:

1) If $z(t)$ varies continuously without hitting $0$, and you unwrap phase continuously, then $⧉\sqrt{z(t)}$ varies continuously.

2) If $z(t)$ winds once around the origin, $\theta_R$ increases by $2\pi$, so the half-angle increases by $\pi$, meaning

$$⧉\sqrt{z(T)} = -\,⧉\sqrt{z(0)}$$

even if $z(T)=z(0)$.

This is not a contradiction; it is the standard **two-sheeted monodromy** of the square root made explicit.

---

## 5. PROs: Phase-Resolved Operators

A **Phase-Resolved Operator (PRO)** is any operator written with the Phase-Lift prefix ⧉ that becomes single-valued once a phase-resolution rule is declared.

### 5.1 Phase-resolved log (⧉log)

For $z\neq 0$:

$$\boxed{\ ⧉\log(z;\theta_{\mathrm{ref}}) := \ln|z| + i\,\theta_R.\ }$$

where $\theta_R = \mathrm{unwrap}(\arg z;\theta_{\mathrm{ref}})$.

### 5.2 Phase-resolved power (⧉(z^a))

Define fractional/complex powers using the resolved log:

$$\boxed{\ ⧉(z^a) := \exp\big(a\,⧉\log z\big).\ }$$

This makes the dependence on phase resolution explicit; changing $\theta_R\mapsto\theta_R+2\pi k$ changes $⧉(z^a)$ by the factor $e^{i2\pi a k}$.

### 5.3 Practical rule of thumb

Use PROs when:

- you are near a branch cut,
- you are tracking a quantity along a path (time evolution, continuation),
- the sign/branch choice affects a downstream decision.

Use principal-branch functions when:

- you only need a conventional single value for a single point,
- continuity across branch cuts is not required.

---

## 6. Algorithmic implementation

### 6.1 Core helper: unwrap to nearest reference

Given $\theta$ and $\theta_{\mathrm{ref}}$, compute:

- $k \leftarrow \mathrm{round}((\theta_{\mathrm{ref}}-\theta)/(2\pi))$
- $\theta_R \leftarrow \theta + 2\pi k$

This is stable, deterministic, and easy to unit test.

### 6.2 State-based continuity along a path

Maintain a structure holding the last resolved phase:

- Initialize $\theta_{\mathrm{prev}}$ to a chosen phase reference, or to the first sample’s phase.
- For each new sample:
  - $\theta \leftarrow \arg(z)$
  - $\theta_R \leftarrow \mathrm{unwrap}(\theta;\theta_{\mathrm{prev}})$
  - set $\theta_{\mathrm{prev}} \leftarrow \theta_R$

Then evaluate PRO formulas using $\theta_R$.

### 6.3 Deterministic PR-Root and PR-Log

With $r=|z|$ and resolved $\theta_R$:

- $⧉\sqrt{z} = \sqrt{r}\,e^{i\theta_R/2}$
- $⧉\log z = \ln r + i\theta_R$

### 6.4 Numerical caveats

- **$z=0$**: $\arg(0)$ is undefined; $⧉\log(0)$ is undefined; $⧉\sqrt{0)$ is well-defined as 0 but any phase tracking will break at exactly 0.
- **Near 0**: phase noise can explode; if $|z|$ is extremely small, unwrapping can jump unpredictably from numerical noise.
- **Sampling rate**: for path continuity, you must sample densely enough that true phase changes per step are $<\pi$ (otherwise the “nearest” rule may choose the wrong $2\pi$ shift).

---

## 7. Relationship to parity/holonomy (optional but useful)

Phase bookkeeping has a clean topological shadow.

### 7.1 Z₂ “sheet parity” as a holonomy

For PR-Root, the only thing that matters for sign flips is the phase winding mod 2.

If a path around the origin has total resolved phase change $\Delta\theta_R$, then the square-root sheet toggles when

$$\frac{\Delta\theta_R}{2\pi} \equiv 1 \pmod 2.$$

Define

$$\nu := \Big(\frac{\Delta\theta_R}{2\pi}\Big) \bmod 2 \in \{0,1\}.$$

Then $\nu$ is the parity of the winding number (a Z₂ invariant), and it predicts whether a full traversal returns you to the same or opposite square-root sheet.

### 7.2 Complexity note (what this does and does not imply)

Tracking Z₂ parity is computationally easy (a single flip-flop / XOR accumulation). The interesting separation is not “polynomial time vs NP”, but **model constraints** such as constant-depth circuits vs log-depth circuits, streaming vs batch, and robustness under noise.

In short: Phase-Lift makes holonomy/parity explicit; it does not, by itself, solve hard search problems.

---

## 8. Canonical equation set (safe usage patterns)

These are standard formulas written in a way that makes branch selection explicit.

1) Quadratic roots:

$$x = \frac{-b \pm ⧉\sqrt{b^2-4ac}}{2a}$$

The $\pm$ is still present (it’s a true algebraic symmetry), but the square-root branch is now separately declared.

2) Euler and imaginary unit reminder:

$$e^{i\pi}+1=0\quad\Rightarrow\quad i\equiv ⧉\sqrt{-1}\ \text{once a phase convention is declared}$$

3) Fourier kernel sign convention:

$$\mathcal{F}\{f\}(\omega)=\int f(t)\,e^{-i\omega t}\,dt$$

The sign choice is a convention; Phase-Lift is a way to keep track of conventions when they interact with branch selection.

---

## 9. Tests, predictions, and falsifiers

Phase-Lift is a bookkeeping convention, but it produces concrete, testable behaviors in numeric code.

### 9.1 Unit tests that should pass

1) Nearest-unwrapping correctness:

For any $\theta$ and reference $\theta_{\mathrm{ref}}$, $\theta_R-\theta$ must be an integer multiple of $2\pi$ and must minimize $|\theta_R-\theta_{\mathrm{ref}}|$ (up to tie-breaking).

2) PR-Log consistency with magnitude:

For any $z\neq 0$,

$$\Re(⧉\log z) = \ln|z|.$$

3) PR-Root squares back to input (with resolved phase):

For $z\neq 0$,

$$\big(⧉\sqrt{z}\big)^2 = z$$

as a complex number (within numerical tolerance), provided $\theta_R$ is used consistently.

### 9.2 A simple monodromy experiment

Let $z(t)=e^{it}$ for $t$ from $0$ to $2\pi$ sampled densely, and compute $⧉\sqrt{z(t)}$ with a running phase state.

Expected behavior:

- The value changes continuously.
- At $t=2\pi$, $z(2\pi)=z(0)=1$ but
  $$⧉\sqrt{z(2\pi)} = -⧉\sqrt{z(0)}.$$

If your implementation returns to the same value after one full winding while also keeping continuity and not hitting $0$, it is almost certainly not tracking the lifted phase correctly.

### 9.3 A branch-reference experiment for $-1$

Evaluate $⧉\sqrt{-1}$ with two different references:

- With $\theta_{\mathrm{ref}}\approx +\pi$, expect $+i$.
- With $\theta_{\mathrm{ref}}\approx -\pi$, expect $-i$.

If both references give the same result, you are likely still using a principal-branch function.

---

## 10. Limitations and scope

- Phase-Lift does not remove genuine multi-valuedness; it lifts it to a space where evaluation is single-valued.
- The output depends on the declared phase-resolution rule. This is a feature (explicitness), but it means results are not invariant under arbitrary branch changes.
- Any “physics reinterpretation” is a separate claim and must be supported by independent modeling and experiments; Phase-Lift itself is bookkeeping.

---

## Appendix A: A minimal implementation sketch (Python-style)

This is the core idea in compact, language-agnostic form:

```python
import cmath, math

TWO_PI = 2.0 * math.pi

def unwrap_angle(theta, reference):
    if reference is None:
        return theta
    k = round((reference - theta) / TWO_PI)
    return theta + TWO_PI * k

class PhaseState:
    def __init__(self):
        self.theta = None

def pr_sqrt(z, phase_ref=None, state=None):
    if state is not None and phase_ref is None:
        phase_ref = state.theta

    r = abs(z)
    theta = cmath.phase(z)
    theta_resolved = unwrap_angle(theta, phase_ref)

    value = math.sqrt(r) * cmath.exp(0.5j * theta_resolved)

    if state is not None:
        state.theta = theta_resolved

    return value
```

The same pattern yields $⧉\log$ and $⧉(z^a)$.
