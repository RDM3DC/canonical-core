# Canonical Core

**A unified theoretical framework for adaptive systems, adaptive geometry, phase-memory transport, emergent structure, adaptive invariants, morphisms, measurement, and adaptive computation.**

This repository contains the canonical white papers for the expanded **12-arm Canonical Core framework**, with **APMG — Adaptive Phase-Memory Geometry** as the umbrella mathematical container.

Website: https://rdm3dc.github.io/canonical-core/

---

## The Framework at a Glance

### Umbrella Framework

- **APMG — Adaptive Phase-Memory Geometry**  
  The container object that unifies the full stack:

```text
A = (X, g, G, κ, θ_R, π_a, M, Φ, C_A, E, L)
```

### 12 Canonical Arms

1. **ARP/AIN** — Adaptive Resistance / Adaptive Impedance Networks
2. **Adaptive-π Geometry** — Adaptive phase-period geometry
3. **Curve Memory / CMA** — Path and derivative memory structures
4. **Phase-Lift / PR-Root / PROs** — Branch-aware phase operators
5. **QPS-GR Mapping** — Strain / clock / visibility engineering layer
6. **ACFN** — Adaptive Curvature Flow Networks
7. **PMT** — Phase-Memory Transport Theory
8. **EPM** — Emergent Phase Matter
9. **ACST** — Adaptive Conservation and Symmetry Theory
10. **AMT** — Adaptive Morphism Theory
11. **AOMT** — Adaptive Observer and Measurement Theory
12. **ACCG** — Adaptive Computation and Complexity Geometry

The core progression is:

```text
flow
→ geometry
→ memory
→ phase
→ spacetime mapping
→ dynamic curvature
→ transport
→ emergence
→ adaptive laws
→ morphisms
→ measurement
→ computation
```

---

## Papers — Recommended Reading Order

1. **[ARP/AIN: Adaptive Resistance and Adaptive Impedance Networks](papers/01-arp-ain.md)**  
   *The core adaptation engine: how systems respond to strain, flow, and memory.*

2. **[Adaptive-π Geometry and Adaptive-π Calculus](papers/02-adaptive-pi-geometry.md)**  
   *πₐ as an adaptive phase-period field and geometry layer.*

3. **[Curve Memory and Curve Memory Alphabet](papers/03-curve-memory-cma.md)**  
   *How paths and derivatives encode reusable memory.*

4. **[Phase-Lift, PR-Root, and PROs](papers/04-phase-lift-pros.md)**  
   *The ⧉ operator, phase-resolved evaluation, and branch-aware objects.*

5. **[QPS-GR: Strain, Clock Offset, Visibility, and Refresh Mapping](papers/05-qps-gr-refresh-mapping.md)**  
   *Engineering mapping between phase, strain, clocks, and visibility.*

6. **[Adaptive Curvature Flow Networks (ACFN)](papers/06-adaptive-curvature-flow-networks.md)**  
   *Dynamic geometry: flow reshapes curvature and curvature changes future flow.*

7. **[Phase-Memory Transport Theory (PMT)](papers/07-phase-memory-transport-theory.md)**  
   *Phase writes memory, and memory modifies future phase transport.*

8. **[Emergent Phase Matter (EPM)](papers/08-emergent-phase-matter.md)**  
   *Stable phase-memory structures, knots, vortices, and adaptive soliton-like objects.*

9. **[Adaptive Conservation and Symmetry Theory (ACST)](papers/09-adaptive-conservation-symmetry-theory.md)**  
   *Adaptive invariants, quasi-conservation laws, and symmetry with memory feedback.*

10. **[Adaptive Phase-Memory Geometry (APMG)](papers/10-adaptive-phase-memory-geometry.md)**  
    *Umbrella mathematical framework for the full Canonical Core object.*

11. **[Adaptive Morphism Theory (AMT)](papers/11-adaptive-morphism-theory.md)**  
    *When two adaptive systems are structurally equivalent across media, coordinates, or scale.*

12. **[Adaptive Observer and Measurement Theory (AOMT)](papers/12-adaptive-observer-measurement-theory.md)**  
    *Measurement, probe back-action, observability, and validation of adaptive systems.*

13. **[Adaptive Computation and Complexity Geometry (ACCG)](papers/13-adaptive-computation-complexity-geometry.md)**  
    *Computation where the cost landscape itself learns.*

---

## Starter Script and Reproducible Artifacts

The ARP/AIN starter script is now present at:

```text
code/arp_ain_sim.py
```

Run it from the repository root:

```bash
python code/arp_ain_sim.py
```

It generates:

```text
artifacts/arp_ain_sim.csv
artifacts/arp_ain_sim_summary.md
```

Default drive signal:

```text
I(t) = I_bias + I_amp * sin(2*pi*freq_hz*t + phase_rad)
```

Default parameters:

```text
alpha_G = 1.20
mu_G = 0.35
G0 = 0.20
G_min = 1.0e-9
I_bias = 0.80
I_amp = 0.45
freq_hz = 0.50
phase_rad = 0.00
t0 = 0.00
t_end = 20.00
dt = 0.01
```

These values are included in the script and in the generated summary so sample numbers can be checked exactly.

---

## Proof and Solver Packages

The newer arms now include proof packages and executable toy examples.

### Proof Packages

```text
papers/acfn-proof-and-solution-package.md
papers/pmt-proof-and-solution-package.md
papers/epm-proof-and-solution-package.md
papers/acst-proof-and-solution-package.md
papers/11-amt-proof-and-solution-package.md
papers/12-aomt-proof-and-solution-package.md
papers/13-accg-proof-and-solution-package.md
```

### Examples

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

## Core Symbols

| Symbol | Meaning |
|---|---|
| `G` | Adaptive conductance / transport capacity |
| `κ` | Curvature field or curvature proxy |
| `θ_R` | Resolved phase field |
| `M` | Memory density / memory field |
| `Φ` | Emergent phase-memory structure field |
| `C_A` | Adaptive conserved-like quantity |
| `⧉` | Phase-Lift operator |
| `πₐ` | Adaptive-π / adaptive phase-period field |
| `E` | Adaptive energy / Lyapunov functional |
| `L` | Ledger law / conservation-accounting rule |
| `W` | Winding or topological marker |

---

## Flagship Closure

A compact master system for the expanded framework is:

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

## Status

- **Version:** 0.3.1-draft
- **Status:** Expanded canonical draft with 12 arms plus APMG umbrella
- **Next:** Update glossary/notation fully, add diagrams, add cross-arm simulations, and publish v0.3 docs

---

## Citation

```bibtex
@software{canonical_core_2026,
  author = {{RDM3DC}},
  title = {Canonical Core: Adaptive Phase-Memory Geometry and the 12-Arm Adaptive Framework},
  year = {2026},
  url = {https://github.com/RDM3DC/canonical-core},
  version = {0.3.1-draft}
}
```

---

## Repository Structure

```text
canonical-core/
├── README.md
├── LICENSE
├── CITATION.cff
├── CHANGELOG.md
├── papers/
│   ├── 01-arp-ain.md
│   ├── 02-adaptive-pi-geometry.md
│   ├── 03-curve-memory-cma.md
│   ├── 04-phase-lift-pros.md
│   ├── 05-qps-gr-refresh-mapping.md
│   ├── 06-adaptive-curvature-flow-networks.md
│   ├── 07-phase-memory-transport-theory.md
│   ├── 08-emergent-phase-matter.md
│   ├── 09-adaptive-conservation-symmetry-theory.md
│   ├── 10-adaptive-phase-memory-geometry.md
│   ├── 11-adaptive-morphism-theory.md
│   ├── 12-adaptive-observer-measurement-theory.md
│   └── 13-adaptive-computation-complexity-geometry.md
├── docs/
│   ├── index.md
│   ├── glossary.md
│   ├── notation.md
│   └── roadmap.md
├── examples/
├── artifacts/
│   └── README.md
├── figures/
├── code/
│   └── arp_ain_sim.py
└── experiments/
```

---

## License

**Papers/text:** CC BY 4.0 unless otherwise stated  
**Code/examples:** MIT-style permissive use unless otherwise stated

---

**Built by [RDM3DC](https://github.com/RDM3DC)** • **Version 0.3.1-draft** • **2026-05-25**
