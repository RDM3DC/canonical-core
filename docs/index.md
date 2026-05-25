# How Everything Connects

Canonical Core is now organized as a **12-arm adaptive framework** with **APMG — Adaptive Phase-Memory Geometry** as the umbrella mathematical container.

The framework moves from adaptive flow, to geometry, to memory, to phase, to dynamic curvature, to transport, to emergence, to laws, to morphisms, to measurement, to computation.

---

## Umbrella Object

The full APMG object is:

```text
A = (X, g, G, κ, θ_R, π_a, M, Φ, C_A, E, L)
```

where:

| Symbol | Meaning |
|---|---|
| `X` | base space: graph, manifold, mesh, grid, CAD object, or point cloud |
| `g` | metric / geometry structure |
| `G` | adaptive conductance / transport capacity |
| `κ` | curvature field or proxy |
| `θ_R` | resolved phase field |
| `π_a` | adaptive phase-period field |
| `M` | memory field |
| `Φ` | emergent structure field |
| `C_A` | adaptive conserved-like quantity |
| `E` | adaptive energy / Lyapunov functional |
| `L` | ledger / conservation-accounting law |

---

## The 12-Arm Stack

```text
┌───────────────────────────────────────────────┐
│ APMG Umbrella                                 │
│ Adaptive Phase-Memory Geometry                │
└───────────────────────────────────────────────┘

┌───────────────────────────────────────────────┐
│ 12: ACCG                                      │  ← Computation / complexity
│     Adaptive computation on learning geometry │
├───────────────────────────────────────────────┤
│ 11: AOMT                                      │  ← Observer / validation
│     Measurement, noise, probe back-action     │
├───────────────────────────────────────────────┤
│ 10: AMT                                       │  ← Morphisms / equivalence
│     Structure-preserving adaptive maps        │
├───────────────────────────────────────────────┤
│ 09: ACST                                      │  ← Laws / invariants
│     Adaptive conservation and symmetry        │
├───────────────────────────────────────────────┤
│ 08: EPM                                       │  ← Emergence layer
│     Stable phase-memory structures            │
├───────────────────────────────────────────────┤
│ 07: PMT                                       │  ← Transport layer
│     Phase-memory transport                    │
├───────────────────────────────────────────────┤
│ 06: ACFN                                      │  ← Dynamic geometry
│     Adaptive curvature flow networks          │
├───────────────────────────────────────────────┤
│ 05: QPS-GR Mapping                            │  ← Engineering layer
│     Strain, clocks, visibility, refresh       │
├───────────────────────────────────────────────┤
│ 04: Phase-Lift (⧉, PROs)                      │  ← Phase structure
│     Branch semantics                          │
├───────────────────────────────────────────────┤
│ 03: Curve Memory (CM/CMA)                     │  ← Memory layer
│     Path + derivative encoding                │
├───────────────────────────────────────────────┤
│ 02: Adaptive-π Geometry                       │  ← Geometric layer
│     πₐ as adaptive phase-period field         │
├───────────────────────────────────────────────┤
│ 01: ARP/AIN                                   │  ← Engine layer
│     Adaptation, resistance, impedance         │
└───────────────────────────────────────────────┘
```

---

## How to Read Them

1. **ARP/AIN** — core adaptation engine.
2. **Adaptive-π Geometry** — adaptive phase-period geometry.
3. **Curve Memory / CMA** — path and derivative memory.
4. **Phase-Lift / PROs** — branch-aware resolved phase.
5. **QPS-GR Mapping** — engineering map for strain, clocks, and visibility.
6. **ACFN** — geometry becomes dynamic through curvature flow.
7. **PMT** — phase writes memory and memory changes future transport.
8. **EPM** — stable phase-memory structures emerge.
9. **ACST** — adaptive conservation and quasi-invariants.
10. **APMG** — umbrella object joining the stack.
11. **AMT** — maps/equivalence between adaptive systems.
12. **AOMT** — observation, validation, probe back-action.
13. **ACCG** — computation where geometry learns.

---

## Key Dependencies

- **ARP/AIN** supplies adaptive state dynamics.
- **Adaptive-π** supplies adaptive phase-period geometry.
- **Curve Memory** supplies historical path structure.
- **Phase-Lift** supplies resolved branch semantics.
- **QPS-GR** supplies engineering visibility/clock/strain mapping.
- **ACFN** requires adaptation plus curvature/geometry.
- **PMT** requires phase, memory, and adaptive transport.
- **EPM** depends on PMT/ACFN memory-curvature structure.
- **ACST** audits conservation, leakage, storage, and return.
- **AMT** compares systems across representation, scale, or substrate.
- **AOMT** validates observations and accounts for probe disturbance.
- **ACCG** turns adaptive geometry into computational complexity.

---

## Core State Variables

| Variable | Meaning | Main Arms |
|---|---|---|
| `G` | Adaptive conductance / transport capacity | ARP/AIN, ACFN, ACCG |
| `κ` | Curvature field | Adaptive-π, ACFN, EPM |
| `θ_R` | Resolved phase | Phase-Lift, PMT, AOMT |
| `π_a` | Adaptive phase-period field | Adaptive-π, Phase-Lift, AMT |
| `M` | Memory density / field | Curve Memory, PMT, EPM, ACST |
| `Φ` | Emergent structure field | EPM, ACCG |
| `C_A` | Adaptive conserved-like quantity | ACST |
| `L` | Ledger law | ACST, AMT, AOMT |

---

## Master System

A compact master system is:

```text
dG/dt = α|I| − μG + λ|∇κ| + σM

∂κ/∂t = η∇·(G∇κ) − βκ

∂θ_R/∂t = ω + γ∇·(G_eff∇θ_R)

∂M/∂t = ξ(∂θ_R/∂t)^2 − ρM

∂Φ/∂t = D∇²Φ − ∂V_eff(Φ,κ,M,θ_R)/∂Φ

dC_A/dt = P_A − μ_A C_A + σ_A M
```

with:

```text
G_eff = G(1 + σM)
```

and:

```text
V_eff = V0 + uκ − vM.
```

---

## Proof Packages and Examples

The repository now contains proof/solution packages and executable examples for the new arms.

```text
papers/acfn-proof-and-solution-package.md
papers/pmt-proof-and-solution-package.md
papers/epm-proof-and-solution-package.md
papers/acst-proof-and-solution-package.md
papers/11-amt-proof-and-solution-package.md
papers/12-aomt-proof-and-solution-package.md
papers/13-accg-proof-and-solution-package.md
```

```text
examples/reduced_acfn_solver.py
examples/reduced_pmt_solver.py
examples/minimal_epm_sim.py
examples/zero_dimensional_epm_solver.py
examples/minimal_acst_accounting.py
examples/two_reservoir_acst_solver.py
examples/amt_morphism_score.py
examples/aomt_observer_accounting.py
examples/accg_adaptive_complexity_solver.py
```

---

## What This Framework Does

- Unifies adaptation, geometry, memory, and phase.
- Defines branch-aware phase evaluation through Phase-Lift.
- Gives geometry dynamic evolution through ACFN.
- Defines phase-memory transport through PMT.
- Defines emergent stable phase-memory objects through EPM.
- Tracks adaptive conservation laws through ACST.
- Defines equivalence maps through AMT.
- Adds measurement and validation through AOMT.
- Defines adaptive computation and complexity through ACCG.

---

## What It Does Not Do Yet

- It does not experimentally prove new physics.
- It does not claim confirmed new particles or anti-gravity.
- It does not fully solve the complete coupled PDE system.
- It does not replace classical conservation laws; ACST extends accounting for adaptive systems.
- It does not replace classical complexity theory; ACCG defines adaptive cost geometry.

---

## Related Repositories

This repository contains the theoretical framework and canonical papers. For code implementations, graphs, and experiments, see:

- [RDM3DC organization on GitHub](https://github.com/RDM3DC)
- [Adaptive Resistance Principle ARP](https://github.com/RDM3DC/Adaptive-Resistance-Principle-ARP-)
- [ACFN](https://github.com/RDM3DC/ACFN)
- [Phase-Memory Transport Theory](https://github.com/RDM3DC/Phase-Memory-Transport-Theory)
- [Emergent Phase Matter](https://github.com/RDM3DC/Emergent-Phase-Matter)
- [Adaptive Conservation and Symmetry Theory](https://github.com/RDM3DC/Adaptive-Conservation-and-Symmetry-Theory)

---

**Next:** Update the glossary and notation files to fully reflect the 12-arm structure.