"""
Adaptive Computation and Complexity Geometry (ACCG) solver.

This solves a reduced learning model:

    dM/dt = xi*U0 - rho*M
    dG/dt = alpha*U0 - mu*G + sigma*M

and computes adaptive path cost:

    C_adapt = C0 + a*abs(kappa) - b*G - c*M

It reports the saturated complexity, speedup ratio, and net speedup after
training/memory/measurement overhead.

Run:
    python examples/accg_adaptive_complexity_solver.py
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ACCGParameters:
    utility: float = 1.0
    alpha: float = 0.7
    mu: float = 0.8
    sigma: float = 0.25
    xi: float = 0.6
    rho: float = 0.9
    c0: float = 10.0
    curvature: float = 2.0
    curvature_weight: float = 0.8
    conductance_bonus: float = 1.2
    memory_bonus: float = 1.0
    training_cost: float = 0.6
    memory_maintenance_cost: float = 0.3
    measurement_error_cost: float = 0.1
    dt: float = 0.002
    steps: int = 10000
    initial_g: float = 0.0
    initial_m: float = 0.0


def equilibrium(p: ACCGParameters) -> dict[str, float | bool]:
    exists = p.mu > 0.0 and p.rho > 0.0
    if not exists:
        return {"exists": False, "G_star": 0.0, "M_star": 0.0}
    m_star = p.xi * p.utility / p.rho
    g_star = p.utility * (p.alpha + p.sigma * p.xi / p.rho) / p.mu
    return {"exists": True, "G_star": g_star, "M_star": m_star}


def adaptive_cost(g: float, m: float, p: ACCGParameters) -> float:
    return (
        p.c0
        + p.curvature_weight * abs(p.curvature)
        - p.conductance_bonus * g
        - p.memory_bonus * m
    )


def run_solver(params: ACCGParameters | None = None) -> dict[str, float | bool]:
    p = params or ACCGParameters()
    g = max(0.0, p.initial_g)
    m = max(0.0, p.initial_m)

    cold_cost = adaptive_cost(0.0, 0.0, p)
    min_cost_seen = adaptive_cost(g, m, p)

    for _ in range(p.steps):
        dm = p.xi * p.utility - p.rho * m
        dg = p.alpha * p.utility - p.mu * g + p.sigma * m
        m = max(0.0, m + p.dt * dm)
        g = max(0.0, g + p.dt * dg)
        min_cost_seen = min(min_cost_seen, adaptive_cost(g, m, p))

    eq = equilibrium(p)
    g_star = float(eq["G_star"])
    m_star = float(eq["M_star"])
    saturated_cost = adaptive_cost(g_star, m_star, p)
    final_cost = adaptive_cost(g, m, p)

    speedup_ratio = cold_cost / max(final_cost, 1e-12)
    saved_cost = cold_cost - final_cost
    overhead = p.training_cost + p.memory_maintenance_cost + p.measurement_error_cost
    net_benefit = saved_cost - overhead

    saturated_speedup_condition_margin = (
        p.conductance_bonus * g_star
        + p.memory_bonus * m_star
        - p.curvature_weight * abs(p.curvature)
    )

    return {
        **eq,
        "final_G": g,
        "final_M": m,
        "cold_cost": cold_cost,
        "final_cost": final_cost,
        "saturated_cost": saturated_cost,
        "min_cost_seen": min_cost_seen,
        "speedup_ratio": speedup_ratio,
        "saved_cost": saved_cost,
        "overhead": overhead,
        "net_benefit": net_benefit,
        "net_speedup": net_benefit > 0.0,
        "saturated_speedup_condition_margin": saturated_speedup_condition_margin,
        "saturated_condition_met": saturated_speedup_condition_margin > 0.0,
    }


if __name__ == "__main__":
    result = run_solver()
    print("ACCG adaptive complexity solver complete")
    for key, value in result.items():
        if isinstance(value, bool):
            print(f"{key}: {value}")
        else:
            print(f"{key}: {value:.8f}")
