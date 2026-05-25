# Adaptive Computation and Complexity Geometry (ACCG)

**White Paper 13**  
**True Arm:** 12  
**Date:** 2026-05-25  
**Status:** Canonical extension draft

---

## Abstract

Adaptive Computation and Complexity Geometry (ACCG) studies computation when the cost landscape itself adapts during the computation.

In ordinary complexity theory, the problem geometry is usually fixed. ACCG asks what happens when repeated computation changes the geometry, conductance, memory, and future cost of solving.

The core question is:

```text
What does computation become when the space of computation learns?
```

ACCG is the computation/complexity arm of Canonical Core.

---

## 1. Core Idea

In adaptive computation, a path can become cheaper because it has been used before.

A minimal adaptive cost law is:

```text
C_adapt(t) = C_0 + a|κ| − bG − cM.
```

where:

- `C_0` is base computational cost,
- `κ` is curvature/stress/complexity penalty,
- `G` is adaptive conductance,
- `M` is memory reinforcement,
- `a,b,c ≥ 0`.

Computation is easier where:

```text
bG + cM > a|κ|.
```

---

## 2. Adaptive Complexity

Define adaptive complexity of a task `T` as:

```text
K_A(T,t) = min_{paths p solving T} ∫_p [C_0 + a|κ| − bG − cM] ds.
```

Unlike classical static cost, `K_A` changes over time because `G`, `κ`, and `M` evolve.

A problem can become easier after experience:

```text
K_A(T,t+Δt) < K_A(T,t).
```

or harder if memory represents damage or congestion.

---

## 3. Learning Geometry

ACCG turns search history into geometry.

A computation trajectory writes memory:

```text
∂M/∂t = ξ U_path − ρM
```

where `U_path` measures path use, success, coherence, or utility.

Conductance adapts:

```text
dG/dt = αU_path − μG + σM.
```

Then future computational cost changes:

```text
C_adapt = C_0 + a|κ| − bG − cM.
```

---

## 4. Relation to RealignR

RealignR can be interpreted as an ACCG optimizer:

```text
search → memory → geometry update → cheaper future search
```

Instead of treating optimization as moving through a fixed loss surface, ACCG treats optimization as reshaping the effective search geometry.

---

## 5. Relation to AdaptiveCAD

AdaptiveCAD can use ACCG to route computation and geometry operations through learned paths:

- adaptive slicing,
- non-triangle toolpaths,
- geometry-aware meshing,
- stress-aware paths,
- learned sketch/surface operations,
- repeated CAD operation acceleration.

ACCG cost can guide toolpath selection:

```text
path* = argmin_p ∫_p [C_0 + a|κ| − bG − cM] ds.
```

---

## 6. First Theorem: Cost Reduction Condition

### Statement

If adaptive cost is

```text
C_adapt = C_0 + a|κ| − bG − cM,
```

then adaptive memory/conductance reduces cost below base cost when

```text
bG + cM > a|κ|.
```

### Proof

Cost below base means:

```text
C_adapt < C_0.
```

Substitute:

```text
C_0 + a|κ| − bG − cM < C_0.
```

Cancel `C_0`:

```text
a|κ| − bG − cM < 0.
```

Rearrange:

```text
bG + cM > a|κ|.
```

QED.

---

## 7. Second Theorem: Monotone Learning Under Reinforcing Memory

Assume a fixed path `p` has fixed curvature and base cost, while `G` and `M` increase over a training interval.

If

```text
dG/dt ≥ 0
```

and

```text
dM/dt ≥ 0,
```

then path cost

```text
C_p(t)=∫_p [C_0+a|κ|−bG−cM]ds
```

is nonincreasing.

### Proof

Differentiate:

```text
dC_p/dt = ∫_p [−b dG/dt − c dM/dt] ds.
```

Since `b,c ≥ 0`, `dG/dt ≥ 0`, and `dM/dt ≥ 0`,

```text
dC_p/dt ≤ 0.
```

QED.

---

## 8. Adaptive Speedup Ratio

Define base cost:

```text
K_0(T)=min_p ∫_p C_0 ds.
```

and adaptive cost:

```text
K_A(T,t)=min_p ∫_p [C_0+a|κ|−bG−cM]ds.
```

Then adaptive speedup is:

```text
S_A(T,t)=K_0(T)/K_A(T,t).
```

When

```text
S_A>1,
```

adaptive geometry improves computation.

When

```text
S_A<1,
```

adaptive memory/curvature harms computation.

---

## 9. Complexity Classes as Dynamic Regions

ACCG does not immediately redefine P, NP, or classical complexity classes.

Instead, it introduces adaptive computational regimes:

### Cold complexity

No useful memory:

```text
M≈0, G≈G_0.
```

### Warm complexity

Some learned paths:

```text
M>0, G>G_0.
```

### Saturated complexity

Memory/conductance reaches equilibrium:

```text
G→G*, M→M*.
```

### Damaged complexity

Memory creates congestion, fatigue, or false paths:

```text
cM behaves as penalty instead of bonus.
```

---

## 10. ACCG Master Loop

```text
attempt computation
→ measure success/coherence
→ write memory
→ adapt conductance
→ reshape cost geometry
→ compute again
```

This is the computational version of the larger Canonical Core loop:

```text
phase → memory → adaptation → geometry → future phase
```

---

## 11. Applications

### 11.1 Optimization

Adaptive optimizers can learn corridors through search space.

### 11.2 Routing

Networks can reduce cost for historically successful routes.

### 11.3 CAD/Slicing

Toolpaths can adapt to curvature, prior passes, stress, and material memory.

### 11.4 Analog Computing

ER fluids, memristive networks, or adaptive impedance networks can physically encode cost changes.

### 11.5 Simulation Acceleration

Repeated phase/geometry computations can cache not just values, but learned geometry.

---

## 12. Canonical Claim

ACCG does not claim that classical complexity theory is wrong.

The canonical claim is:

```text
ACCG defines computational cost on adaptive geometries whose memory and conductance evolve during computation.
```

---

## 13. Summary

ACCG is the true twelfth arm because it gives the framework a computation theory.

The flagship equation is:

```text
K_A(T,t)=min_p ∫_p [C_0+a|κ|−bG−cM]ds.
```

The main idea is:

```text
computation becomes easier where geometry has learned.
```
