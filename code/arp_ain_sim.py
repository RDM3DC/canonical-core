"""
Reproducible ARP/AIN starter simulation.

This script fixes the earlier documentation gap: the repository now has the
claimed starter file at:

    code/arp_ain_sim.py

Default ARP model:

    dG/dt = alpha_G * |I(t)| - mu_G * G

Default drive signal:

    I(t) = I_bias + I_amp * sin(2*pi*freq_hz*t + phase_rad)

Default parameters:

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

Run from repository root:

    python code/arp_ain_sim.py

Outputs:

    artifacts/arp_ain_sim.csv
    artifacts/arp_ain_sim_summary.md

The CSV records every timestep so sample numbers can be audited exactly.
"""

from __future__ import annotations

import argparse
import csv
import math
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ARPParams:
    alpha_g: float = 1.20
    mu_g: float = 0.35
    g0: float = 0.20
    g_min: float = 1.0e-9
    i_bias: float = 0.80
    i_amp: float = 0.45
    freq_hz: float = 0.50
    phase_rad: float = 0.00
    t0: float = 0.00
    t_end: float = 20.00
    dt: float = 0.01


def drive_current(t: float, p: ARPParams) -> float:
    """Signed drive current I(t). ARP uses abs(I(t)) for reinforcement."""
    return p.i_bias + p.i_amp * math.sin(2.0 * math.pi * p.freq_hz * t + p.phase_rad)


def euler_step(g: float, i_t: float, p: ARPParams) -> float:
    """One explicit Euler step for canonical ARP."""
    dg_dt = p.alpha_g * abs(i_t) - p.mu_g * g
    return max(p.g_min, g + p.dt * dg_dt)


def simulate(p: ARPParams) -> list[dict[str, float]]:
    """Run deterministic ARP simulation and return row dictionaries."""
    if p.dt <= 0.0:
        raise ValueError("dt must be positive")
    if p.t_end <= p.t0:
        raise ValueError("t_end must be greater than t0")
    if p.mu_g <= 0.0:
        raise ValueError("mu_g must be positive")
    if p.alpha_g < 0.0:
        raise ValueError("alpha_g must be nonnegative")
    if p.i_amp < 0.0:
        raise ValueError("i_amp must be nonnegative")

    rows: list[dict[str, float]] = []
    g = max(p.g_min, p.g0)
    t = p.t0
    step = 0

    # Include initial state and every explicit step up to t_end.
    while t <= p.t_end + 1.0e-12:
        i_t = drive_current(t, p)
        rows.append(
            {
                "step": float(step),
                "t": t,
                "I_t": i_t,
                "abs_I_t": abs(i_t),
                "G": g,
                "R": 1.0 / g,
                "dG_dt": p.alpha_g * abs(i_t) - p.mu_g * g,
            }
        )
        g = euler_step(g, i_t, p)
        step += 1
        t = p.t0 + step * p.dt

    return rows


def summarize(rows: list[dict[str, float]], p: ARPParams) -> dict[str, float]:
    if not rows:
        raise ValueError("no rows to summarize")

    g_values = [r["G"] for r in rows]
    i_abs_values = [r["abs_I_t"] for r in rows]
    final = rows[-1]
    avg_abs_i = sum(i_abs_values) / len(i_abs_values)
    avg_g = sum(g_values) / len(g_values)
    equilibrium_from_avg_abs_i = p.alpha_g * avg_abs_i / p.mu_g

    return {
        "n_rows": float(len(rows)),
        "t0": p.t0,
        "t_end": p.t_end,
        "dt": p.dt,
        "alpha_g": p.alpha_g,
        "mu_g": p.mu_g,
        "g0": p.g0,
        "g_min": p.g_min,
        "i_bias": p.i_bias,
        "i_amp": p.i_amp,
        "freq_hz": p.freq_hz,
        "phase_rad": p.phase_rad,
        "avg_abs_i": avg_abs_i,
        "avg_g": avg_g,
        "min_g": min(g_values),
        "max_g": max(g_values),
        "final_t": final["t"],
        "final_i": final["I_t"],
        "final_abs_i": final["abs_I_t"],
        "final_g": final["G"],
        "final_r": final["R"],
        "equilibrium_from_avg_abs_i": equilibrium_from_avg_abs_i,
    }


def write_csv(rows: list[dict[str, float]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["step", "t", "I_t", "abs_I_t", "G", "R", "dG_dt"],
        )
        writer.writeheader()
        writer.writerows(rows)


def write_summary(summary: dict[str, float], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# ARP/AIN Starter Simulation Summary",
        "",
        "## Model",
        "",
        "```text",
        "dG/dt = alpha_G * |I(t)| - mu_G * G",
        "I(t) = I_bias + I_amp * sin(2*pi*freq_hz*t + phase_rad)",
        "```",
        "",
        "## Exact Parameters Used",
        "",
    ]
    for key in [
        "alpha_g",
        "mu_g",
        "g0",
        "g_min",
        "i_bias",
        "i_amp",
        "freq_hz",
        "phase_rad",
        "t0",
        "t_end",
        "dt",
        "n_rows",
    ]:
        lines.append(f"- `{key}` = `{summary[key]:.12g}`")

    lines += [
        "",
        "## Sample Numbers",
        "",
    ]
    for key in [
        "avg_abs_i",
        "avg_g",
        "min_g",
        "max_g",
        "final_t",
        "final_i",
        "final_abs_i",
        "final_g",
        "final_r",
        "equilibrium_from_avg_abs_i",
    ]:
        lines.append(f"- `{key}` = `{summary[key]:.12g}`")

    lines += [
        "",
        "## Reproducibility Note",
        "",
        "The companion CSV contains every timestep and can be regenerated with:",
        "",
        "```bash",
        "python code/arp_ain_sim.py",
        "```",
        "",
    ]

    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a reproducible ARP/AIN starter simulation.")
    parser.add_argument("--alpha-g", type=float, default=ARPParams.alpha_g)
    parser.add_argument("--mu-g", type=float, default=ARPParams.mu_g)
    parser.add_argument("--g0", type=float, default=ARPParams.g0)
    parser.add_argument("--g-min", type=float, default=ARPParams.g_min)
    parser.add_argument("--i-bias", type=float, default=ARPParams.i_bias)
    parser.add_argument("--i-amp", type=float, default=ARPParams.i_amp)
    parser.add_argument("--freq-hz", type=float, default=ARPParams.freq_hz)
    parser.add_argument("--phase-rad", type=float, default=ARPParams.phase_rad)
    parser.add_argument("--t0", type=float, default=ARPParams.t0)
    parser.add_argument("--t-end", type=float, default=ARPParams.t_end)
    parser.add_argument("--dt", type=float, default=ARPParams.dt)
    parser.add_argument("--out-dir", type=Path, default=Path("artifacts"))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    params = ARPParams(
        alpha_g=args.alpha_g,
        mu_g=args.mu_g,
        g0=args.g0,
        g_min=args.g_min,
        i_bias=args.i_bias,
        i_amp=args.i_amp,
        freq_hz=args.freq_hz,
        phase_rad=args.phase_rad,
        t0=args.t0,
        t_end=args.t_end,
        dt=args.dt,
    )

    rows = simulate(params)
    summary = summarize(rows, params)

    csv_path = args.out_dir / "arp_ain_sim.csv"
    summary_path = args.out_dir / "arp_ain_sim_summary.md"

    write_csv(rows, csv_path)
    write_summary(summary, summary_path)

    print("ARP/AIN starter simulation complete")
    print(f"wrote: {csv_path}")
    print(f"wrote: {summary_path}")
    print(f"final_G: {summary['final_g']:.12g}")
    print(f"final_R: {summary['final_r']:.12g}")
    print(f"avg_abs_I: {summary['avg_abs_i']:.12g}")


if __name__ == "__main__":
    main()
