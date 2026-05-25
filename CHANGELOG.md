# Changelog

All notable changes to the Canonical Core project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project follows draft semantic versioning while the canon is evolving.

---

## [Unreleased]

### Added
- Expanded Canonical Core from nine arms to a **12-arm framework**.
- Added the APMG umbrella paper:
  - 10: Adaptive Phase-Memory Geometry (APMG)
- Added three new canonical arms:
  - 11: Adaptive Morphism Theory (AMT)
  - 12: Adaptive Observer and Measurement Theory (AOMT)
  - 13: Adaptive Computation and Complexity Geometry (ACCG)
- Added proof and solution packages:
  - ACFN proof and solution package
  - PMT proof and solution package
  - EPM proof and solution package
  - ACST proof and solution package
  - AMT proof and solution package
  - AOMT proof and solution package
  - ACCG proof and solution package
- Added executable examples:
  - `examples/reduced_acfn_solver.py`
  - `examples/reduced_pmt_solver.py`
  - `examples/minimal_epm_sim.py`
  - `examples/zero_dimensional_epm_solver.py`
  - `examples/minimal_acst_accounting.py`
  - `examples/two_reservoir_acst_solver.py`
  - `examples/amt_morphism_score.py`
  - `examples/aomt_observer_accounting.py`
  - `examples/accg_adaptive_complexity_solver.py`

### Changed
- Updated README to describe the **12-arm Canonical Core** and APMG umbrella object.
- Updated `docs/index.md` with the full 12-arm stack, dependencies, master system, proof packages, and example list.
- Updated project status to `0.3.0-draft`.
- Reframed Canonical Core as:
  - flow
  - geometry
  - memory
  - phase
  - spacetime mapping
  - dynamic curvature
  - transport
  - emergence
  - adaptive laws
  - morphisms
  - measurement
  - computation

### Planned
- Update `/docs/glossary.md` for all 12 arms.
- Update `/docs/notation.md` for APMG, AMT, AOMT, and ACCG.
- Add figures and diagrams to `/figures`.
- Add cross-arm simulations joining ACFN + PMT + EPM + ACST.
- Publish v0.3 docs.

---

## [0.2.0-draft] - 2026-05-25

### Added
- Added four expanded canonical extension papers:
  - 06: Adaptive Curvature Flow Networks (ACFN)
  - 07: Phase-Memory Transport Theory (PMT)
  - 08: Emergent Phase Matter (EPM)
  - 09: Adaptive Conservation and Symmetry Theory (ACST)
- Added the expanded nine-arm reading order to the README.
- Added the four-field expanded-state framing: `G`, `κ`, `θ`, and `M`.
- Updated the framework map from five arms to nine arms in `docs/index.md`.

### Changed
- Reframed Canonical Core as an expanded nine-arm framework:
  - flow
  - geometry
  - memory
  - phase
  - spacetime mapping
  - dynamic curvature
  - transport
  - emergence
  - adaptive laws

---

## [0.1.0] - 2026-01-09

### Added
- Initial release of five canonical white papers:
  - 01: ARP/AIN – Adaptive Resistance and Adaptive Impedance Networks
  - 02: Adaptive-π Geometry and Adaptive-π Calculus
  - 03: Curve Memory and Curve Memory Alphabet
  - 04: Phase-Lift, PR-Root, and PROs
  - 05: QPS-GR Strain, Clock Offset, Visibility, and Refresh Mapping
- README with reading order and quick start guide
- CITATION.cff for GitHub citation button
- Repository structure and roadmap

### Changed
- Organized papers into `/papers` directory
- Established canonical notation rules
