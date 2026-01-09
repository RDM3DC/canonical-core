# QPS/GR Strain → Clock Offset → Visibility → Refresh Mapping

**White Paper 05**  
**Date:** 2026-01-09  
**Status:** Complete draft (self-contained)

---

## Abstract

A Quantum Positioning System (QPS) or any entanglement-assisted time-transfer scheme relies on maintaining phase coherence between distributed quantum systems. In curved or time-varying spacetime, different worldlines accumulate different **proper times**, creating an effective timing mismatch $\Delta\tau(t)$. A minimal engineering question follows:

> Given a spacetime disturbance model (gravitational wave strain $h(t)$ and/or static gravitational redshift), what is the induced $\Delta\tau(t)$, how does it degrade entanglement visibility $V(t)$, and what refresh cadence is required to keep $V(t)$ above a floor?

This paper gives a concrete, computable pipeline:

1) map a GR perturbation (strain or metric potential) to a clock-offset signal $\Delta\tau(t)$,
2) map $\Delta\tau(t)$ to visibility $V(t)$ via a coherence-time model,
3) extract a refresh time (first threshold crossing) and an equivalent refresh rate.

We also highlight a key scaling behavior: for oscillatory high-frequency strain, $\Delta\tau \propto \int h\,dt$ can be strongly suppressed by cancellation, making fast gravitational waves comparatively harmless for timing-based decoherence metrics unless there is a DC component or “memory” effect.

---

## 1. Motivation and scope

In distributed quantum protocols (entanglement distribution, teleportation-based links, QPS), a common failure mode is **loss of phase reference** between nodes. In many physical implementations, the relevant mismatch can be modeled as a time/phase offset between two arms or stations.

This paper focuses on an intentionally minimal question: how much *timing mismatch* does a given gravitational disturbance produce, and what does that imply for refresh.

### 1.1 What is included

- A simple strain-to-proper-time mapping suitable for quick “order-of-magnitude” sweeps.
- A weak-field static redshift model (Earth-scale intuition).
- A visibility model based on a coherence time $\tau_{\mathrm{coh}}$.
- Algorithmic steps for discretized data $h(t)$.

### 1.2 What is not included (by design)

- A full GR derivation for a specific detector/worldline geometry.
- Complete quantum noise modeling (photon loss, detector dark counts, phase noise in lasers, etc.).
- Claims that this mapping by itself explains all decoherence.

The goal is a clean mapping layer you can later embed into richer models.

---

## 2. Definitions

We consider two stations (or arms) $A$ and $B$.

- $\tau_A(t)$: proper time accumulated along station $A$’s worldline up to coordinate time $t$.
- $\tau_B(t)$: proper time accumulated along station $B$’s worldline.
- $\Delta\tau(t) := \tau_A(t) - \tau_B(t)$: relative clock offset.

We use:

- $h(t)$: a gravitational-wave strain time series (dimensionless).
- $\tau_{\mathrm{coh}}$: coherence time (seconds) characterizing how tolerant the quantum link is to timing mismatch.
- $V(t)$: visibility (dimensionless, in $[0,1]$).

---

## 3. Strain-to-clock-offset mapping (toy but computable)

### 3.1 Linearized rule used in the mapper

A simple engineering approximation is to treat the strain as producing a fractional time-rate perturbation:

$$\boxed{\ \frac{d\tau}{dt} \approx 1 + \frac{1}{2}h(t).\ }$$

Then the induced timing offset relative to the undisturbed clock is

$$\boxed{\ \Delta\tau(t) \approx \int_0^t \frac{1}{2} h(t')\,dt'.\ }$$

Notes:

- This is not a universal GR identity. It is a **model assumption** that compresses geometry into a 1D effective time-rate signal.
- It is useful for parameter sweeps and for understanding cancellation/scaling.

### 3.2 Cancellation at high frequency

If $h(t)$ is oscillatory with zero mean, then $\int h(t)dt$ can remain small.

Example: $h(t)=h_0\sin(\omega t)$ gives

$$\Delta\tau(t)=\frac{1}{2}\int_0^t h_0\sin(\omega t')dt' = \frac{h_0}{2\omega}\,(1-\cos(\omega t)).$$

So the scale of the mismatch is

$$\boxed{\ \Delta\tau_{\max} \sim \frac{h_0}{\omega}.\ }$$

Higher frequency ($\omega$ larger) yields **smaller** accumulated mismatch.

### 3.3 When strain matters

The integral suppression disappears when $h(t)$ has:

- a DC component (bias),
- a low-frequency drift component,
- a “memory-like” step/offset (net nonzero time integral over the event),
- strong asymmetry in the burst envelope that leaves residual area.

---

## 4. Static gravitational redshift (weak-field baseline)

For slowly varying, weak gravitational potentials, one often uses

$$\boxed{\ \frac{d\tau}{dt} \approx 1 + \frac{\Phi}{c^2}\ }$$

where $\Phi$ is Newtonian potential (units m\u00b2/s\u00b2) and $c$ is the speed of light.

Near Earth, for a small height difference $\Delta z$,

$$\Delta\Phi \approx g\,\Delta z,$$

so the fractional rate difference is

$$\boxed{\ \frac{d}{dt}\Delta\tau \approx \frac{g\,\Delta z}{c^2}.\ }$$

Integrating for duration $T$ gives

$$\boxed{\ \Delta\tau(T) \approx \frac{g\,\Delta z}{c^2}\,T.\ }$$

This grows linearly with $T$, but the coefficient is tiny in terrestrial settings.

---

## 5. Clock-offset to visibility mapping

### 5.1 Gaussian coherence window model

A simple and common model is that visibility decays as a Gaussian in timing mismatch:

$$\boxed{\ V(t) = \exp\!\left(-\Big(\frac{\Delta\tau(t)}{\tau_{\mathrm{coh}}}\Big)^2\right).\ }$$

Interpretation:

- $\tau_{\mathrm{coh}}$ is the characteristic mismatch scale that reduces visibility significantly.
- The Gaussian form corresponds to (or approximates) Gaussian wavepacket overlap degradation.

### 5.2 Refresh time and refresh rate

Pick a minimum allowed visibility $V_{\mathrm{floor}}$.

Define the **refresh time** as the first threshold crossing:

$$\boxed{\ T_{\mathrm{refresh}} := \inf\{t\ge 0 : V(t) \le V_{\mathrm{floor}}\}.\ }$$

If $T_{\mathrm{refresh}}$ exists, a simple equivalent “refresh rate” is

$$\boxed{\ f_{\mathrm{refresh}} \approx \frac{1}{T_{\mathrm{refresh}}}.\ }$$

### 5.3 Closed form for linear drift

If $\Delta\tau(t)$ grows linearly: $\Delta\tau(t)\approx \rho\,t$ with drift rate $\rho$ (dimensionless), then

$$V(t)=\exp\!\left(-\Big(\frac{\rho t}{\tau_{\mathrm{coh}}}\Big)^2\right).$$

Solving $V(t)=V_{\mathrm{floor}}$ gives

$$\boxed{\ T_{\mathrm{refresh}} = \frac{\tau_{\mathrm{coh}}}{\rho}\,\sqrt{\ln\!\left(\frac{1}{V_{\mathrm{floor}}}\right)}.\ }$$

For static redshift, $\rho \approx g\Delta z/c^2$.

---

## 6. Discretized computation pipeline

Assume we have sampled strain $h[n]$ at times $t[n]$.

### 6.1 Compute $\Delta\tau$ from strain

Using trapezoidal integration:

$$\Delta\tau[n] \approx \sum_{k=1}^{n} \frac{1}{2}\,\frac{h[k]+h[k-1]}{2}\,(t[k]-t[k-1]).$$

### 6.2 Compute visibility

$$V[n] = \exp\!\left(-\left(\frac{\Delta\tau[n]}{\tau_{\mathrm{coh}}}\right)^2\right).$$

### 6.3 Compute refresh time

Find the smallest index $n$ such that $V[n]\le V_{\mathrm{floor}}$, then set

$$T_{\mathrm{refresh}}\approx t[n].$$

If no such $n$ exists over the observation window, then no refresh is triggered by this disturbance under the model.

---

## 7. Worked scaling observations (sanity checks)

These are not fundamental constants; they are sanity-check outcomes of the mapping assumptions.

### 7.1 High-frequency strain “immunity”

Because $\Delta\tau \propto \int h\,dt$, a bursty sinusoidal strain can yield very small integrated area even for large peak amplitude. In prior sweeps with a 200 Hz sine-burst and a visibility floor near $10^{-4}$ with $\tau_{\mathrm{coh}}\sim 10^{-3}\,\mathrm{s}$, visibility remained close to 1 for strain scales far above astrophysical values. The suppression is simply the $1/\omega$ scaling of the integral and envelope cancellation.

Practical takeaway:

- **Fast oscillations** are comparatively harmless in this model.
- **Slow drift / memory** dominates accumulated mismatch.

### 7.2 Static redshift is tiny on human timescales

Using $\Delta\tau(T)\approx (g\Delta z/c^2)T$ with $\Delta z=100\,\mathrm{km}$ and $T=1\,\mathrm{year}$ gives a differential offset on the order of $10^{-8}\,\mathrm{s}$, which is far below a millisecond-scale coherence window.

Practical takeaway:

- For many QPS designs, **intrinsic decoherence sources** dominate over static terrestrial gravity.

---

## 8. Extensions and design knobs

### 8.1 Add DC/memory strain mode

To probe regimes where the integral does not cancel, include:

- step strain: $h(t)=h_0\,\mathbf{1}_{t\ge 0}$ (toy), giving $\Delta\tau(t)=\tfrac{1}{2}h_0 t$.
- burst with offset: $h(t)=h_0\sin(\omega t)\,e^{-t^2/2\sigma^2}+h_{\mathrm{dc}}$.

### 8.2 Differential geometry between nodes

In real deployments, $\Delta\tau$ depends on geometry:

- baseline length and orientation relative to GW polarization,
- motion (satellites, rotation),
- local gravitational potential differences,
- propagation delays and how timing is extracted from quantum measurements.

A next-step model can treat $h(t)$ as producing a differential phase between $A$ and $B$ directly.

### 8.3 ARP-style adaptive refresh control

If refresh is a resource, you can treat it like an adaptive control variable. For example:

- define an error signal $e(t)= -\ln V(t) = (\Delta\tau/\tau_{\mathrm{coh}})^2$,
- adapt a refresh intensity $R(t)$ so that $R$ increases when $e$ grows and decays when $e$ is small.

This mirrors the “reinforce on need, decay otherwise” pattern used elsewhere in the archive.

---

## 9. Predictions and falsifiers

### 9.1 Predictions (conditional on the mapping assumptions)

1) **Frequency suppression:** for comparable peak strain amplitudes, higher-frequency components contribute less to $\Delta\tau$ (roughly $\propto 1/\omega$).

2) **DC dominates:** a small DC drift in $h(t)$ or a memory-like step dominates $\Delta\tau$ over a long window.

3) **Static redshift linearity:** $\Delta\tau$ from altitude differences grows linearly with duration $T$ and scales with $\Delta z$.

### 9.2 Falsifiers (what would break this model)

1) If measured decoherence correlates strongly with instantaneous $h(t)$ rather than with a time-integrated or low-frequency component, this mapping is missing the relevant coupling.

2) If high-frequency oscillatory strain (with near-zero integral) produces large timing mismatches in controlled experiments, the model’s integral suppression is incorrect for that geometry.

3) If visibility degradation vs $\Delta\tau$ is not well-fit by a Gaussian overlap model, the $V=\exp(-(\Delta\tau/\tau_{\mathrm{coh}})^2)$ ansatz is not appropriate; another lineshape (Lorentzian/exponential or a more detailed wavepacket model) is required.

---

## 10. Limitations and careful interpretation

- The strain-to-time rule $d\tau/dt\approx 1+\tfrac{1}{2}h(t)$ is a **toy effective model**. It is useful for rapid sweeps and intuition, but not a substitute for a full GR+detector-geometry derivation.
- Visibility loss in real QPS systems is often dominated by **non-GR noise sources** (loss, thermal noise, oscillator phase noise, atmosphere/turbulence in optical links, etc.). This paper isolates only the timing-mismatch channel.

---

## Appendix A: Minimal reference implementation sketch

This matches the computational structure used in the strain-mapper prototype:

```python
import numpy as np


def strain_to_delta_tau(strain, t):
    # delta_tau(t) = ∫ 0.5*h(t) dt
    frac = 0.5 * strain
    dt = np.diff(t)
    # trapezoid cumulative integral
    out = np.zeros_like(t)
    out[1:] = np.cumsum(0.5 * (frac[1:] + frac[:-1]) * dt)
    return out


def visibility(delta_tau, tau_coh):
    return np.exp(- (delta_tau / tau_coh) ** 2)


def refresh_time(delta_tau, t, tau_coh, V_floor=1e-4):
    V = visibility(delta_tau, tau_coh)
    idx = np.where(V <= V_floor)[0]
    return None if idx.size == 0 else float(t[idx[0]])
```

If you add static drift, you can add it directly into $\Delta\tau(t)$ as a linear term.
