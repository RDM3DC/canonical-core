# Canonical Notation Rules

This document establishes the **official notation** for Canonical Core. If you reference these papers, please use these symbols as defined.

---

## Core Symbols

| Symbol | Name | Definition | Paper |
|--------|------|------------|-------|
| **⧉** | Phase-Lift | Prefix operator for phase-structured branching | 04 |
| **πₐ** | Adaptive π | Adaptive π as a field (not constant 3.14159...) | 02 |
| **π** | Standard π | Mathematical constant (3.14159...) | — |
| **CM** | Curve Memory | Memory object encoding path + derivative history | 03 |
| **CMA** | Curve Memory Alphabet | Encoding system for CM | 03 |
| **PROs** | Phase-Resistant Objects | Objects that survive phase transitions | 04 |
| **ARP** | Adaptive Resistance Pattern | Resistance that adapts to strain | 01 |
| **AIN** | Adaptive Impedance Network | Network with adaptive impedance | 01 |

---

## QPS-GR Mapping Symbols

| Symbol | Name | Definition | Paper |
|--------|------|------------|-------|
| **τ_coh** | Coherence time | Time scale for phase coherence | 05 |
| **V_floor** | Visibility floor | Minimum observable visibility | 05 |
| **Δν** | Frequency offset | Clock frequency difference | 05 |
| **ε_strain** | Strain parameter | Dimensionless strain | 05 |
| **QPS** | Quantum Phase Space | Phase space with quantum structure | 05 |

---

## Notation Rules

### 1. ⧉ is a prefix operator
✅ Correct: `⧉(state, context)`  
❌ Wrong: `state⧉` or `⧉state`

### 2. π remains constant, πₐ is a field
- Use **π** for the mathematical constant (3.14159...)
- Use **πₐ** when π is adaptive (context-dependent field)
- Never mix them in the same expression
- **πₐ defines the local phase wrap unit** (not just a rescaling)

✅ Correct: `A = π r²` (circle area in Euclidean geometry)  
✅ Correct: `A = πₐ(context) · r²` (adaptive geometry)  
✅ Correct: `θ = θ_R + 2πₐ(x,t) · w` (phase with adaptive wrap)  
❌ Wrong: `A = π · πₐ · r²`  
❌ Wrong: `θ = θ_R + 2π · πₐ · w` (mixing fixed and adaptive)

**Key distinction:** In standard QM, phase wraps at fixed 2π. With πₐ, the wrap unit itself becomes a dynamic field:
- Standard: `θ ≡ θ + 2πk` (fixed period)
- Adaptive: `θ = θ_R + 2πₐ(x,t) · w` (dynamic period)

### 3. CM is a memory object
- **CM** is not a function; it's a data structure
- Access CM contents via: `CM.path`, `CM.derivatives`, `CM.encode()`

✅ Correct: `CM.path[t]`  
❌ Wrong: `CM(t)`

### 4. CMA is an encoding alphabet
- CMA defines the symbols used to encode CM
- Think of CMA as a "language" for memory

### 5. PROs are objects, not functions
- **PROs** carry properties across phase transitions
- They are instantiated, not called

✅ Correct: `object = PRO(properties)`  
❌ Wrong: `PRO(state) → result`

---

## Typography

### Subscripts and Superscripts
- Use subscripts for indices, labels, parameters: `τ_coh`, `V_floor`, `πₐ`
- Use superscripts for exponents, powers: `r²`, `e^{iθ}`

### Greek Letters
- **π** (pi) – Standard mathematical constant
- **πₐ** (pi-adaptive) – Adaptive π field
- **τ** (tau) – Time scales (τ_coh, τ_relax)
- **ε** (epsilon) – Small parameters (ε_strain)
- **Δ** (delta) – Differences (Δν, Δφ)

### Special Operators
- **⧉** (Phase-Lift) – U+29C9 "Two Joined Squares"
- Use Unicode if possible; otherwise use `\PhaseLift` in LaTeX

---

## LaTeX Macros (Recommended)

If you're writing a paper that references Canonical Core, use these macros:

```latex
\newcommand{\PhaseLift}{\ensuremath{\unicode{x29C9}}}
\newcommand{\pia}{\ensuremath{\pi_{\text{a}}}}
\newcommand{\CM}{\ensuremath{\text{CM}}}
\newcommand{\CMA}{\ensuremath{\text{CMA}}}
\newcommand{\PRO}{\ensuremath{\text{PRO}}}
\newcommand{\tcoh}{\ensuremath{\tau_{\text{coh}}}}
\newcommand{\Vfloor}{\ensuremath{V_{\text{floor}}}}
```

Then use:
```latex
\PhaseLift(state, context) generates a phase-structured branch with memory \CM.
```

---

## Special Topic: πₐ in Phase Equations

The adaptive-π field has specific notation conventions when used in phase equations:

### Standard vs Adaptive Phase Wrap

**Standard QM (fixed wrap):**
```
θ ≡ θ + 2πk,  k ∈ ℤ
```
Phase wraps at fixed 2π intervals.

**Adaptive-π (dynamic wrap):**
```
θ = θ_R + 2πₐ(x,t) · w,  w ∈ ℤ
```
Where:
- `θ_R` = resolved (unwrapped) phase
- `πₐ(x,t)` = local phase-period field
- `w` = winding number

### Key Properties

1. **πₐ is a field, not a constant** — It varies with position and time
2. **πₐ defines the local wrap unit** — Not just a rescaling factor
3. **πₐ enables continuous phase transport** — Phase doesn't "jump" at branch cuts
4. **πₐ → π recovers standard QM** — Standard physics is a special case

### When to Use πₐ

Use **πₐ** when:
- Tracking phase continuity along paths
- Computing winding numbers under deformation
- Implementing Phase-Lift (⧉) operations
- Working with parity tracking (ℤ₂)
- Dealing with topology changes that don't change winding

Use **π** when:
- Working in standard Euclidean geometry
- Using fixed reference frames
- Computing with constant phase periods

---

## Citation Format

When referencing a specific symbol, cite the paper where it's defined:

> "The Phase-Lift operator ⧉ (Paper 04) creates phase-structured branches that carry Curve Memory CM (Paper 03) forward."

---

## Future Extensions

As the framework evolves, new symbols may be added. This document is the **canonical source** for notation—check here first before inventing new symbols.

---

**Last Updated:** 2026-01-09  
**Version:** 0.1.0