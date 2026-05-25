# Phase-Memory Transport Theory (PMT)

**White Paper 07**  
**Date:** 2026-05-25  
**Status:** Canonical extension draft

---

## Abstract

Phase-Lift and Curve Memory define how phase branches and paths carry history. Adaptive Curvature Flow Networks define how geometry can change under flow. **Phase-Memory Transport Theory (PMT)** adds the missing transport layer: phase itself becomes a history-bearing medium that carries memory through adaptive geometry.

PMT studies coupled dynamics among:

- `θ` — phase
- `M` — memory density
- `G` — adaptive conductance or transport capacity
- `κ` — curvature field

The central loop is:

```text
phase → memory → adaptation → geometry → future phase
```

PMT is the seventh arm of Canonical Core.

---

## 1. Motivation

In many systems, phase is not just an instantaneous angle. It carries history:

- oscillators remember synchronization paths
- RF and optical signals accumulate phase delay
- quantum phases accumulate along paths
- waves remember boundary conditions
- adaptive networks remember coherent routes

Phase-Lift gives branch-aware phase bookkeeping.

Curve Memory gives path-history encoding.

PMT turns those ideas into a transport theory.

---

## 2. Core Principle

The PMT principle is:

> Phase evolution leaves memory, and memory changes future phase transport.

This makes phase a medium of adaptive persistence.

The core cycle is:

```text
θ changes
M records the change
G is modified by M
κ is modified by G
θ then propagates through the changed system
```

---

## 3. Foundational Equations

A minimal PMT model is:

```text
∂θ/∂t = ω − γ ∇·(G ∇θ)
```

```text
∂M/∂t = ξ(∂θ/∂t)² − ρM
```

```text
G_eff = G(1 + σM)
```

where:

- `θ` is the phase field
- `ω` is intrinsic angular frequency
- `γ` is phase transport strength
- `G` is adaptive transport conductance
- `M` is memory density
- `ξ` is memory creation rate
- `ρ` is memory decay rate
- `σ` is memory-to-transport feedback strength

Interpretation:

- phase propagates differently through adapted regions
- rapid phase evolution leaves memory traces
- memory increases or decreases future transport capacity

---

## 4. Coupling to Adaptive Curvature Flow Networks

PMT naturally couples to ACFN:

```text
dG/dt = α|I| − μG + λ|∇κ| + σM
```

```text
∂κ/∂t = η ∇·(G ∇κ) − βκ
```

```text
∂θ/∂t = ω − γ ∇·(G ∇θ)
```

```text
∂M/∂t = ξ(∂θ/∂t)² − ρM
```

This is the first compact four-field system in the expanded Canonical Core.

The recurring state variables are:

```text
G  → adaptation
κ  → geometry
θ  → phase
M  → memory
```

---

## 5. Relation to Phase-Lift

Phase-Lift resolves branch structure:

```text
(⧉f)(z; θ_ref) = f(z; θ_R)
```

where `θ_R` is the unwrapped, history-resolved phase.

PMT describes how `θ_R` is transported through an adaptive medium.

So the relation is:

```text
Phase-Lift gives branch semantics.
PMT gives branch transport dynamics.
```

---

## 6. Relation to Adaptive-π

Adaptive-π changes the local phase-period field:

```text
θ = θ_R + 2πₐ(x,t)w
```

PMT allows the transport of `θ_R` to depend on `G`, `M`, and `κ`.

A possible PMT + Adaptive-π condition is:

```text
∂θ_R/∂t = ω − γ ∇·(G ∇θ_R)
```

with local wrap:

```text
θ = θ_R mod 2πₐ(x,t)
```

This separates:

- resolved phase transport
- adaptive phase wrapping

---

## 7. Memory Density

The memory law:

```text
∂M/∂t = ξ(∂θ/∂t)² − ρM
```

is intentionally simple.

It says:

- fast phase changes write memory
- stable regions slowly forget
- persistent oscillation can create memory channels

Other memory write laws are possible:

```text
∂M/∂t = ξ|∇θ|² − ρM
```

or

```text
∂M/∂t = ξ|∇θ · v| − ρM
```

The canonical model keeps the squared phase-rate form as the first draft.

---

## 8. Transport Regimes

PMT predicts several qualitative regimes.

### 8.1 Low-memory transport

When `M ≈ 0`:

```text
G_eff ≈ G
```

Phase moves through the current adaptive geometry without strong historical reinforcement.

### 8.2 Memory-reinforced transport

When `M > 0` and `σ > 0`:

```text
G_eff > G
```

Phase prefers historically coherent channels.

### 8.3 Memory-blocked transport

If `σ < 0`, memory can represent damage, decoherence, congestion, or fatigue:

```text
G_eff < G
```

Phase avoids historically unstable regions.

---

## 9. Applications

### 9.1 RF and Wireless Routing

PMT suggests a way to model coherent signal routing where past phase stability influences future route preference.

### 9.2 Adaptive Optics

Optical systems may be modeled as phase-memory systems where wavefront correction leaves persistent transport structure.

### 9.3 Quantum-Inspired Navigation

PMT is not a claim that the system is automatically quantum mechanical. It is a history-sensitive phase transport model that can support QPS-style engineering metaphors.

### 9.4 Self-Optimizing Networks

Networks can become:

- path-aware
- phase-aware
- memory-aware
- coherence-aware

---

## 10. Canonical Claim

PMT does not claim that all physical phase transport is adaptive.

The canonical claim is:

> PMT defines a general adaptive transport layer in which phase evolution writes memory, and memory modifies future transport.

It is the information-flow arm of Canonical Core.

---

## 11. Minimal Simulation Recipe

A first PMT simulation can use a 2D grid:

1. Initialize `G(x,y)` and `M(x,y)`.
2. Set source phase frequency `ω`.
3. Evolve `θ`.
4. Write memory from phase change.
5. Update effective conductance.
6. Visualize persistent phase channels.

Pseudo-code:

```text
for each time step:
    θ_t = ω - γ*div(G_eff*grad(θ))
    M += dt*(ξ*θ_t**2 - ρ*M)
    G_eff = G*(1 + σ*M)
    θ += dt*θ_t
```

Expected result:

```text
phase channels that persist because memory modifies future transport
```

---

## 12. Summary

PMT is the seventh arm because it adds adaptive information transport.

The first six arms give:

```text
adaptation, geometry, memory, phase structure, spacetime mapping, dynamic curvature
```

PMT adds:

```text
phase-memory transport
```

The result is the central loop:

```text
phase → memory → adaptation → geometry → future phase
```
