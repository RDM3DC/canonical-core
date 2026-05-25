"""
Adaptive Morphism Theory (AMT) morphism score example.

This computes a simple same-grid AMT score between two adaptive states:

    A = (G, kappa, theta, pi_a, M, ledger)
    B = (G, kappa, theta, pi_a, M, ledger)

For phase, it uses wrapped phase distance:

    d_phase(theta1, theta2; pi_a) = min_w |theta1 - theta2 + 2*pi_a*w|

Run:
    python examples/amt_morphism_score.py
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Sequence


Field = Sequence[float]


@dataclass(frozen=True)
class AdaptiveState:
    conductance: Field
    curvature: Field
    phase: Field
    adaptive_pi: Field
    memory: Field
    ledger: Field


@dataclass(frozen=True)
class AMTWeights:
    conductance: float = 1.0
    curvature: float = 1.0
    phase: float = 1.0
    adaptive_pi: float = 1.0
    memory: float = 1.0
    ledger: float = 2.0


def squared_l2(a: Field, b: Field) -> float:
    if len(a) != len(b):
        raise ValueError("fields must have the same length")
    return sum((x - y) ** 2 for x, y in zip(a, b))


def wrapped_phase_distance_sq(theta_a: Field, theta_b: Field, pi_a: Field) -> float:
    if not (len(theta_a) == len(theta_b) == len(pi_a)):
        raise ValueError("phase fields must have the same length")

    total = 0.0
    for x, y, local_pi in zip(theta_a, theta_b, pi_a):
        period = 2.0 * local_pi
        if period <= 0.0:
            raise ValueError("adaptive pi values must be positive")
        delta = x - y
        # Nearest wrapped representative.
        wrapped = ((delta + 0.5 * period) % period) - 0.5 * period
        total += wrapped * wrapped
    return total


def amt_score(a: AdaptiveState, b: AdaptiveState, weights: AMTWeights | None = None) -> float:
    w = weights or AMTWeights()
    return (
        w.conductance * squared_l2(a.conductance, b.conductance)
        + w.curvature * squared_l2(a.curvature, b.curvature)
        + w.phase * wrapped_phase_distance_sq(a.phase, b.phase, a.adaptive_pi)
        + w.adaptive_pi * squared_l2(a.adaptive_pi, b.adaptive_pi)
        + w.memory * squared_l2(a.memory, b.memory)
        + w.ledger * squared_l2(a.ledger, b.ledger)
    )


def demo() -> dict[str, float | bool]:
    n = 64
    xs = [i / n for i in range(n)]

    state_a = AdaptiveState(
        conductance=[1.0 + 0.1 * math.sin(2 * math.pi * x) for x in xs],
        curvature=[0.2 * math.cos(2 * math.pi * x) for x in xs],
        phase=[2 * math.pi * x for x in xs],
        adaptive_pi=[math.pi for _ in xs],
        memory=[0.3 * math.exp(-((x - 0.5) ** 2) / 0.01) for x in xs],
        ledger=[0.0 for _ in xs],
    )

    # Same structure but phase is shifted by one full wrap: should not count as phase mismatch.
    state_b = AdaptiveState(
        conductance=list(state_a.conductance),
        curvature=list(state_a.curvature),
        phase=[p + 2.0 * math.pi for p in state_a.phase],
        adaptive_pi=list(state_a.adaptive_pi),
        memory=list(state_a.memory),
        ledger=list(state_a.ledger),
    )

    score = amt_score(state_a, state_b)

    # Add a small memory distortion and recompute.
    state_c = AdaptiveState(
        conductance=list(state_a.conductance),
        curvature=list(state_a.curvature),
        phase=list(state_a.phase),
        adaptive_pi=list(state_a.adaptive_pi),
        memory=[m + 0.01 for m in state_a.memory],
        ledger=list(state_a.ledger),
    )

    distorted_score = amt_score(state_a, state_c)

    return {
        "wrap_equivalent_score": score,
        "wrap_equivalent_is_zero": abs(score) < 1e-12,
        "memory_distorted_score": distorted_score,
    }


if __name__ == "__main__":
    result = demo()
    print("AMT morphism score demo complete")
    for key, value in result.items():
        if isinstance(value, bool):
            print(f"{key}: {value}")
        else:
            print(f"{key}: {value:.12f}")
