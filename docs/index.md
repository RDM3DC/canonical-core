# How Everything Connects

The five papers in Canonical Core form a layered, interlocking framework. Here's the conceptual map:

## The Stack

```
┌─────────────────────────────────────┐
│ 05: QPS-GR Mapping                  │  ← Engineering layer
│     (strain, clocks, visibility)    │
├─────────────────────────────────────┤
│ 04: Phase-Lift (⧉, PROs)            │  ← Phase structure
│     (branch semantics)              │
├─────────────────────────────────────┤
│ 03: Curve Memory (CM/CMA)           │  ← Memory layer
│     (path + derivative encoding)    │
├─────────────────────────────────────┤
│ 02: Adaptive-π Geometry             │  ← Geometric layer
│     (πₐ as field)                   │
├─────────────────────────────────────┤
│ 01: ARP/AIN                          │  ← Engine layer
│     (adaptation, resistance)        │
└─────────────────────────────────────┘
```

## How to Read Them

1. **Start with ARP/AIN (Paper 01)** – This defines the core adaptation mechanism: how systems respond to strain, how resistance and impedance shape behavior.

2. **Add Geometry (Paper 02)** – Adaptive-π shows what happens when π itself is adaptive: geometry bends with context.

3. **Add Memory (Paper 03)** – Curve Memory encodes the path and derivative history, creating a "memory object" that systems can query.

4. **Add Phase Structure (Paper 04)** – Phase-Lift (⧉) adds branching semantics: how phase transitions create new branches, and what objects (PROs) survive across them.

5. **Map to Physics (Paper 05)** – QPS-GR mapping connects the abstract framework to quantum phase space and general relativity, with explicit engineering constraints.

## Key Dependencies

- **CM requires ARP/AIN** – Memory encoding depends on adaptation response
- **Phase-Lift requires CM** – Phase branches carry memory forward
- **QPS mapping requires all four** – The engineering layer assumes adaptation, geometry, memory, and phase structure

## Canonical Notation

See [notation.md](notation.md) for the full list, but key symbols:

- **⧉** = Phase-Lift operator (prefix, phase branch)
- **πₐ** = Adaptive π (field, not constant)
- **CM** = Curve Memory object
- **CMA** = Curve Memory Alphabet (encoding)
- **PROs** = Phase-Resistant Objects
- **τ_coh** = Coherence time
- **V_floor** = Visibility floor

## What This Framework Does

- **Unifies adaptation, geometry, and memory**
- **Defines phase-structured branching** (not just "forking")
- **Provides engineering semantics** for quantum-GR correspondence
- **Establishes canonical notation** for future work

## What It Doesn't Do (Yet)

- Full experimental validation (future work)
- Worked examples with real datasets (coming in v0.2)
- Visualization tools (planned for `/code`)

## Related Repositories

This repository contains the **theoretical framework** and canonical papers. For **code implementations, graphs, and experiments**, see:

- **[RDM3DC organization on GitHub](https://github.com/RDM3DC)** – Contains multiple repositories with:
  - **[ARP](https://github.com/RDM3DC/arp)** – Code implementations for Adaptive Resistance/Impedance Networks
  - Additional repositories with visualizations, graphs, and experimental results

Visit [github.com/RDM3DC](https://github.com/RDM3DC) to explore all related projects.

---

**Next:** Read the [glossary](glossary.md) for detailed definitions.