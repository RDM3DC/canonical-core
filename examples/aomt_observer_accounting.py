"""
Adaptive Observer and Measurement Theory (AOMT) accounting example.

This simulates a measurement channel:

    Y = O(A) + noise + probe_bias

and probe-written memory:

    M_next = M + chi_probe * Y^2 * dt - rho * M * dt

It also computes a simple falsifier check:

    S_effect > N_floor + B_probe + ledger_error

Run:
    python examples/aomt_observer_accounting.py
"""

from __future__ import annotations

import math
import random
from dataclasses import dataclass


@dataclass(frozen=True)
class AOMTParameters:
    steps: int = 1000
    dt: float = 0.01
    true_amplitude: float = 1.0
    signal_frequency: float = 1.0
    noise_std: float = 0.05
    probe_bias: float = 0.03
    chi_probe: float = 0.02
    memory_decay: float = 0.05
    seed: int = 7


def true_observable(t: float, p: AOMTParameters) -> float:
    return p.true_amplitude * math.sin(2.0 * math.pi * p.signal_frequency * t)


def run_observer(params: AOMTParameters | None = None) -> dict[str, float | bool]:
    p = params or AOMTParameters()
    rng = random.Random(p.seed)

    memory = 0.0
    total_probe_written = 0.0
    total_memory_decay = 0.0
    squared_noise_sum = 0.0
    squared_bias_corrected_error_sum = 0.0
    max_ledger_error = 0.0

    signal_energy = 0.0

    for step in range(p.steps):
        t = step * p.dt
        observed_true = true_observable(t, p)
        noise = rng.gauss(0.0, p.noise_std)
        y = observed_true + noise + p.probe_bias

        old_memory = memory
        write = p.chi_probe * y * y
        decay = p.memory_decay * memory
        memory = max(0.0, memory + p.dt * (write - decay))

        total_probe_written += p.dt * write
        total_memory_decay += p.dt * decay
        squared_noise_sum += noise * noise

        bias_corrected = y - p.probe_bias
        squared_bias_corrected_error_sum += (bias_corrected - observed_true) ** 2
        signal_energy += observed_true * observed_true

        ledger_prediction = old_memory + p.dt * (write - decay)
        max_ledger_error = max(max_ledger_error, abs(memory - ledger_prediction))

    rms_noise = math.sqrt(squared_noise_sum / p.steps)
    rms_corrected_error = math.sqrt(squared_bias_corrected_error_sum / p.steps)
    effect_strength = math.sqrt(signal_energy / p.steps)
    falsifier_margin = effect_strength - (rms_noise + abs(p.probe_bias) + max_ledger_error)

    return {
        "final_probe_written_memory": memory,
        "total_probe_written": total_probe_written,
        "total_memory_decay": total_memory_decay,
        "rms_noise": rms_noise,
        "rms_bias_corrected_error": rms_corrected_error,
        "effect_strength": effect_strength,
        "max_ledger_error": max_ledger_error,
        "falsifier_margin": falsifier_margin,
        "effect_passes_falsifier": falsifier_margin > 0.0,
    }


if __name__ == "__main__":
    result = run_observer()
    print("AOMT observer accounting demo complete")
    for key, value in result.items():
        if isinstance(value, bool):
            print(f"{key}: {value}")
        else:
            print(f"{key}: {value:.8f}")
