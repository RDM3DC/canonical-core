# Artifacts

This directory is reserved for generated outputs from reproducible scripts.

It is intentionally lightweight in git. The starter ARP/AIN simulation writes:

```text
artifacts/arp_ain_sim.csv
artifacts/arp_ain_sim_summary.md
```

Regenerate them with:

```bash
python code/arp_ain_sim.py
```

Default drive signal and parameters are documented in `code/arp_ain_sim.py` and in the generated summary.

The default drive signal is:

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
