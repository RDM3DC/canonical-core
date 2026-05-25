# AMT Proof and Solution Package

**Paper:** 11  
**True Arm:** 10  
**Framework:** Adaptive Morphism Theory (AMT)  
**Date:** 2026-05-25  
**Status:** Mathematical working draft

---

## 0. Purpose

Adaptive Morphism Theory asks:

```text
When are two adaptive systems the same structure in different coordinates, media, scales, or representations?
```

This proof package gives AMT its first rigorous core:

1. identity morphisms,
2. composition of exact morphisms,
3. category structure for exact adaptive morphisms,
4. triangle-style error bound for approximate morphisms,
5. ledger preservation,
6. phase-aware distance,
7. coarse-graining consistency,
8. a computable morphism score.

---

## 1. APMG Objects

Let an Adaptive Phase-Memory Geometry object be

```text
A = (X, g, G, κ, θ_R, π_a, M, Φ, C_A, E, L).
```

For AMT, the most important fields are:

```text
G      adaptive conductance
κ      curvature field
θ_R    resolved phase
π_a    adaptive phase-period field
M      memory field
L      ledger / conservation-accounting law
```

---

## 2. Exact Morphism

An exact AMT morphism

```text
F: A → B
```

is a map with field transport rules such that the selected fields are preserved:

```text
F*G_B = G_A
F*κ_B = κ_A
F*θ_B = θ_A
F*π_{a,B} = π_{a,A}
F*M_B = M_A
F*L_B = L_A.
```

The symbol `F*` denotes pullback from `B` to `A`.

---

## 3. Approximate Morphism

An approximate AMT morphism satisfies tolerance bounds:

```text
||F*G_B − G_A|| ≤ ε_G
||F*κ_B − κ_A|| ≤ ε_κ
||F*θ_B − θ_A|| ≤ ε_θ
||F*π_{a,B} − π_{a,A}|| ≤ ε_π
||F*M_B − M_A|| ≤ ε_M
||F*L_B − L_A|| ≤ ε_L.
```

A compact morphism score is

```text
E_AMT(F) = w_G||F*G_B − G_A||²
         + w_κ||F*κ_B − κ_A||²
         + w_θ d_phase(F*θ_B, θ_A)²
         + w_π||F*π_{a,B} − π_{a,A}||²
         + w_M||F*M_B − M_A||²
         + w_L||F*L_B − L_A||².
```

---

## 4. Theorem: Identity Morphism

### Statement

Every APMG object `A` has an identity morphism

```text
id_A: A → A
```

with

```text
E_AMT(id_A) = 0.
```

### Proof

The identity map sends every field to itself:

```text
id_A*G_A = G_A
id_A*κ_A = κ_A
id_A*θ_A = θ_A
id_A*π_{a,A} = π_{a,A}
id_A*M_A = M_A
id_A*L_A = L_A.
```

Every difference term in `E_AMT` is zero. Therefore

```text
E_AMT(id_A)=0.
```

QED.

---

## 5. Theorem: Composition of Exact Morphisms

### Statement

If

```text
F: A → B
```

and

```text
H: B → C
```

are exact morphisms, then

```text
H∘F: A → C
```

is exact.

### Proof

Exactness of `H` gives:

```text
H*G_C = G_B.
```

Exactness of `F` gives:

```text
F*G_B = G_A.
```

For the composite pullback:

```text
(H∘F)*G_C = F*(H*G_C) = F*G_B = G_A.
```

The same argument applies to `κ`, `θ`, `π_a`, `M`, and `L`.

Therefore the composite preserves all selected fields and ledger laws.

QED.

---

## 6. Theorem: Exact AMT Forms a Category

### Statement

APMG objects with exact AMT morphisms form a category, denoted

```text
APMG_exact.
```

### Proof

A category requires:

1. objects,
2. morphisms between objects,
3. identity morphisms,
4. associative composition.

Objects are APMG objects. Morphisms are exact AMT maps.

Identity morphisms exist by Theorem 4.

Composition of exact morphisms is exact by Theorem 5.

Composition of functions is associative:

```text
K∘(H∘F) = (K∘H)∘F.
```

Therefore `APMG_exact` is a category.

QED.

---

## 7. Phase-Aware Distance

For wrapped phase, ordinary subtraction can falsely report large differences between nearly equal phases.

Define:

```text
d_phase(θ_1, θ_2; π_a) = min_{w∈ℤ} |θ_1 − θ_2 + 2π_a w|.
```

For Phase-Lifted resolved phase `θ_R`, use:

```text
d_phase(θ_{R,1}, θ_{R,2}) = |θ_{R,1} − θ_{R,2}|.
```

### Theorem: Wrapped Phase Distance Vanishes on Equivalent Wraps

If

```text
θ_1 = θ_2 + 2π_a k
```

for some `k∈ℤ`, then

```text
d_phase(θ_1,θ_2;π_a)=0.
```

### Proof

Choose `w = −k` in the minimization:

```text
|θ_1 − θ_2 + 2π_a(-k)| = |2π_a k − 2π_a k| = 0.
```

Since distances are nonnegative, the minimum is zero.

QED.

---

## 8. Approximate Composition Error Bound

Suppose `F:A→B` has error at most `ε_F` and `H:B→C` has error at most `ε_H` under a compatible norm and non-expansive pullbacks.

Then the composite error satisfies:

```text
ε_{H∘F} ≤ ε_F + ε_H.
```

### Proof Sketch

For one field `q`, compare `q_A` to `(H∘F)*q_C`:

```text
||F*H*q_C − q_A||
≤ ||F*H*q_C − F*q_B|| + ||F*q_B − q_A||.
```

If `F*` is non-expansive,

```text
||F*H*q_C − F*q_B|| ≤ ||H*q_C − q_B|| ≤ ε_H.
```

The second term is at most `ε_F`.

Thus:

```text
||F*H*q_C − q_A|| ≤ ε_H + ε_F.
```

Summing weighted field errors gives the approximate composition bound.

QED.

---

## 9. Ledger Preservation Theorem

### Statement

If `F:A→B` is exact and `B` satisfies ledger law `L_B=0`, then `A` satisfies the pulled-back ledger law:

```text
F*L_B = L_A = 0.
```

### Proof

Exact AMT morphisms preserve ledgers by definition:

```text
F*L_B = L_A.
```

If `L_B=0`, then

```text
L_A = F*0 = 0.
```

QED.

### Interpretation

An exact morphism cannot hide conservation failure. If the source and target disagree on ledger accounting, the map is not exact.

---

## 10. Coarse-Graining Preservation

Let `C:X_fine→X_coarse` be a coarse-graining map. A coarse morphism should preserve global quantities:

```text
∫G_fine dx ≈ Σ G_coarse
```

```text
∫M_fine dx ≈ Σ M_coarse
```

```text
W_fine = W_coarse
```

where topology allows.

### Coarse Error

```text
E_coarse = |Q_G^fine − Q_G^coarse|
         + |Q_M^fine − Q_M^coarse|
         + |W_fine − W_coarse|
         + |L_fine − L_coarse|.
```

A good coarse map has small `E_coarse`.

---

## 11. Solved AMT Test Case

For two scalar grids `A` and `B` with same size, use identity field mapping:

```text
F = id.
```

Then

```text
E_AMT(F) = w_G||G_B−G_A||² + w_M||M_B−M_A||² + w_κ||κ_B−κ_A||².
```

If fields are identical, `E_AMT=0`.

If each field differs by uniform offsets `δ_G`, `δ_M`, `δ_κ` over `N` cells, then

```text
E_AMT = N(w_Gδ_G² + w_Mδ_M² + w_κδ_κ²).
```

This gives the first closed-form AMT score.

---

## 12. What Is Solved So Far

### Proven

- identity morphisms exist,
- exact morphisms compose,
- exact APMG objects and morphisms form a category,
- wrapped phase distance vanishes on equivalent wraps,
- approximate morphism composition error obeys an additive bound under non-expansive maps,
- exact morphisms preserve ledger validity,
- simple grid morphism score has a closed form.

### Core equations

```text
E_AMT(F)=Σ_i w_i||F*field_i−field_i||²+w_L||F*L_B−L_A||².
```

```text
d_phase(θ_1,θ_2;π_a)=min_{w∈ℤ}|θ_1−θ_2+2π_aw|.
```

---

## 13. What Is Still Open

1. Rich categorical structure for approximate morphisms.
2. Optimal transport maps between different grids/manifolds.
3. Graph-to-manifold AMT convergence.
4. AMT for stochastic systems.
5. Experimental morphisms from measured data to model states.

---

## 14. Summary

The first rigorous AMT core is:

```text
adaptive systems can be compared by structure-preserving maps that preserve fields, phase, memory, and conservation ledgers.
```

The practical AMT test is:

```text
small E_AMT means same adaptive structure, different representation.
```
