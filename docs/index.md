# How Everything Connects

The nine papers in Canonical Core form a layered, interlocking framework. The first five define the foundation; Papers 06–09 extend it into dynamic geometry, adaptive transport, emergence, and adaptive invariants.

## The Stack

```text
┌───────────────────────────────────────────────┐
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

## How to Read Them

1. **Start with ARP/AIN (Paper 01)** – This defines the core adaptation mechanism: how systems respond to strain, flow, and memory.

2. **Add Geometry (Paper 02)** – Adaptive-π defines a local adaptive phase-period field and gives geometry a tunable phase-wrap structure.

3. **Add Memory (Paper 03)** – Curve Memory encodes path and derivative history, creating a memory object that systems can query.

4. **Add Phase Structure (Paper 04)** – Phase-Lift (⧉) adds branch-aware phase semantics and defines Phase-Resistant Objects.

5. **Map to Physics/Engineering (Paper 05)** – QPS-GR mapping connects the abstract framework to strain, clock offset, visibility, and refresh cadence.

6. **Make Geometry Dynamic (Paper 06)** – ACFN turns geometry into an adaptive state variable: flow reshapes curvature and curvature changes future flow.

7. **Transport Phase-Memory (Paper 07)** – PMT treats phase as a history-bearing transport medium where phase writes memory and memory modifies future transport.

8. **Let Stable Objects Emerge (Paper 08)** – EPM defines stable phase-memory structures such as knots, vortices, adaptive solitons, and geometry-locked islands.

9. **Ask What Remains Conserved (Paper 09)** – ACST defines adaptive conservation, quasi-invariants, and symmetry laws with memory feedback.

## Key Dependencies

- **CM requires ARP/AIN** – Memory encoding depends on adaptive response.
- **Phase-Lift requires CM** – Phase branches carry history forward.
- **QPS mapping requires the first four** – The engineering layer assumes adaptation, geometry, memory, and phase structure.
- **ACFN extends ARP + Adaptive-π** – Dynamic curvature needs both adaptation and geometry.
- **PMT extends Phase-Lift + CM + ACFN** – Phase-memory transport needs resolved phase, memory, and adaptive geometry.
- **EPM extends PMT** – Stable emergent structures require transport plus topological closure.
- **ACST sits above all arms** – Adaptive laws and quasi-invariants describe what persists across the whole stack.

## The Four-Field Core of the Expanded Stack

Papers 06–09 repeatedly use four state variables:

| Variable | Meaning | Primary arm |
|---|---|---|
| `G` | Adaptive conductance / transport capacity | ARP/AIN, ACFN |
| `κ` | Curvature field | Adaptive-π, ACFN |
| `θ` | Phase field / resolved phase | Phase-Lift, PMT |
| `M` | Memory density / memory field | Curve Memory, PMT |

A compact speculative master system is:

```text
dG/dt = α|I| − μG + λ|∇κ| + σM

∂κ/∂t = η ∇·(G ∇κ) − βκ

∂θ/∂t = ω − γ ∇·(G ∇θ)

∂M/∂t = ξ(∂θ/∂t)² − ρM
```

This is the core loop:

```text
phase → memory → adaptation → geometry → future phase
```

## Canonical Notation

See [notation.md](notation.md) for the full list, but key symbols are:

- **⧉** = Phase-Lift operator
- **πₐ** = Adaptive-π field
- **CM** = Curve Memory object
- **CMA** = Curve Memory Alphabet
- **PROs** = Phase-Resistant Objects
- **G** = adaptive conductance / transport capacity
- **κ** = curvature field
- **θ** = phase field
- **M** = memory density
- **ACFN** = Adaptive Curvature Flow Networks
- **PMT** = Phase-Memory Transport Theory
- **EPM** = Emergent Phase Matter
- **ACST** = Adaptive Conservation and Symmetry Theory
- **τ_coh** = Coherence time
- **V_floor** = Visibility floor

## What This Framework Does

- **Unifies adaptation, geometry, and memory**
- **Defines phase-structured branching** through Phase-Lift
- **Provides engineering semantics** for QPS-GR correspondence
- **Adds dynamic geometry** through ACFN
- **Adds adaptive phase-memory transport** through PMT
- **Defines emergent stable structures** through EPM
- **Defines adaptive invariants and quasi-conservation laws** through ACST
- **Establishes canonical notation** for future work

## What It Doesn't Do (Yet)

- Full experimental validation
- Complete worked examples with real datasets
- Numerical solvers for all nine arms
- Formal proofs of all proposed stability and conservation claims
- Full visualization tools for `/code`

## Related Repositories

This repository contains the **theoretical framework** and canonical papers. For **code implementations, graphs, and experiments**, see:

- **[RDM3DC organization on GitHub](https://github.com/RDM3DC)** – Contains multiple repositories with:
  - **[ARP](https://github.com/RDM3DC/Adaptive-Resistance-Principle-ARP-)** – Code implementations for Adaptive Resistance/Impedance Networks
  - Additional repositories with visualizations, graphs, and experimental results

Visit [github.com/RDM3DC](https://github.com/RDM3DC) to explore all related projects.

---

**Next:** Read the [glossary](glossary.md) for detailed definitions.