# Adaptive Resistance Principle (ARP) and Adaptive Impedance Networks (AIN)

**White Paper 01**  
**Date:** 2026-01-09  
**Status:** Complete draft (self-contained)

---

## Abstract

The **Adaptive Resistance Principle (ARP)** is a dynamical rule for networks in which edge conductances strengthen in proportion to carried activity and decay in time in the absence of activity. In its canonical form, ARP is an ordinary differential equation (ODE) on an edge conductance variable $G_{ij}(t)$ driven by the magnitude of current $|I_{ij}(t)|$.

The **Adaptive Impedance Network (AIN)** generalizes ARP to frequency-aware, passive electrical analogs by allowing not only conductance/resistance but also capacitance and inductance to adapt under local excitation. AIN supplies a unified template for (i) self-organizing routing and graph optimization, (ii) adaptive analog computation, and (iii) control-like “memory depth” via time constants.

This paper provides the mathematical definition, equilibrium behavior, discrete-time integration guidance, stability notes, and practical parameterization. It also describes a minimal simulation recipe and testable predictions.

---

## 1. Motivation and framing

Many systems that “learn paths” or “discover structure” can be modeled as **networks with adaptive edges**. The edges represent conductance, trust, affinity, capacity, or an effective coupling. The key design requirement is:

- **Reinforce what is used** (activity strengthens the edge),
- **Forget what is unused** (edges decay toward baseline),
- **Avoid divergence** (unbounded growth),
- **Remain interpretable** (few parameters with clear meaning).

ARP is the simplest continuous-time rule satisfying these requirements.

AIN adds two additional edge-states (capacitance and inductance) so the network can represent not just static routing but **frequency-dependent behavior** (buffering, inertia, damping).

### 1.1 Positioning (what this is similar to, and what is distinct)

ARP/AIN will remind readers of several known ideas:

- **Hebbian-style learning ("fire together, wire together")**: ARP reinforces edges when they are used, but it is framed as a continuous-time physical/flow-coupled law rather than a discrete weight update on labeled samples.
- **Memristive intuition**: conductance is a state variable that changes with excitation. ARP is a deliberately minimal, explicit rule that can be simulated even without a device-level constitutive model.
- **Ant-colony-style reinforcement**: edges on good paths strengthen. ARP expresses this as a dynamical system driven by flow magnitude, with an explicit decay timescale.

The distinct claim of this paper is not that these inspirations are new, but that **a single, parameter-minimal ODE template** (reinforce on activity, decay otherwise) can serve as a clean foundation across routing, analog computation, and adaptive impedance modeling.

---

## 2. Core definitions

Consider a graph with nodes $i,j$ and an edge state per ordered pair (or per undirected edge). Denote:

- $R_{ij}(t)$: resistance on edge $(i,j)$ (nonnegative),
- $G_{ij}(t)$: conductance on edge $(i,j)$ (nonnegative), related by
  $$G_{ij}(t) = \frac{1}{R_{ij}(t)}.$$

Let $I_{ij}(t)$ be the (possibly signed) current through the edge at time $t$ under a chosen driving condition (in circuit analogs, driven by sources/sinks; in routing analogs, driven by demand).

### 2.1 Canonical ARP ODE

The canonical ARP update is:

$$\boxed{\ \frac{dG_{ij}}{dt} = \alpha_G\,|I_{ij}(t)| - \mu_G\,G_{ij}(t).\ }$$

Parameters:

- $\alpha_G \ge 0$: reinforcement gain (how strongly activity increases conductance),
- $\mu_G > 0$: decay rate (forgetting / leakage term).

Interpretation:

- If an edge carries no current ($|I_{ij}|=0$), conductance decays exponentially.
- If an edge carries sustained current, it converges to a nonzero equilibrium.

#### 2.1.1 Dimensional consistency (units)

If this model is instantiated as a physical circuit analog, then:

- $G$ has units of Siemens (S), $R$ has units of Ohms (Ω), and $I$ has units of Amps (A).
- The ODE term $dG/dt$ has units S/s.

Therefore:

$$[\alpha_G] = \frac{\mathrm{S}}{\mathrm{A}\cdot\mathrm{s}},\quad [\mu_G] = \frac{1}{\mathrm{s}}.$$

For non-physical analogs (e.g., routing weights), these “units” can be interpreted as consistent scaling dimensions.

#### 2.1.2 Canonical constrained ARP (deployable default)

In coupled networks, “every edge wins” unless there is competition. A practical, stable-by-default variant is to combine (i) bounded reinforcement and (ii) an explicit global (or local) resource constraint.

One canonical choice is:

$$\boxed{\ \frac{dG_{ij}}{dt} = \alpha_G\,\sigma(|I_{ij}|) - \mu_G\,G_{ij}\ }$$

subject to a conductance budget, for example:

$$\boxed{\ \sum_{(i,j)\in E} G_{ij}(t) \le G_{\mathrm{total}}\ }$$

Implementation note (discrete time): after the Euler update, if $\sum G_{ij} > G_{\mathrm{total}}$, rescale

$$G_{ij} \leftarrow G_{ij}\,\frac{G_{\mathrm{total}}}{\sum G_{ij}}.$$

This simple normalization forces edges to compete and reliably produces sparse backbones.

### 2.2 Network efficiency metric (one canonical choice)

A compact scalar that summarizes “how conductive the used network is” is:

$$\boxed{\ \mathrm{ANE}(t) = \frac{\sum_{ij} G_{ij}(t)\,|I_{ij}(t)|}{\sum_{ij} |I_{ij}(t)|}.\ }$$

This is a weighted average of conductance over active edges.

**Role clarification:** in this paper, $\mathrm{ANE}(t)$ is a **diagnostic** (an instrument panel), not assumed to be an objective function and not claimed to be a Lyapunov function.

---

## 3. ARP equilibrium and timescales

Fix a single edge $(i,j)$ and assume $|I_{ij}(t)|$ is constant in time at value $|I|$ (a local quasi-static assumption often valid when the network dynamics are slower than instantaneous current solving).

Then the ODE is linear:

$$\frac{dG}{dt} + \mu_G G = \alpha_G |I|.$$

### 3.1 Closed-form solution

With initial condition $G(0)=G_0$:

$$G(t) = G_{\mathrm{eq}} + (G_0 - G_{\mathrm{eq}})e^{-\mu_G t},$$

where

$$\boxed{\ G_{\mathrm{eq}} = \frac{\alpha_G}{\mu_G}\,|I|.\ }$$

### 3.2 Interpretation of $\alpha_G/\mu_G$

- $\mu_G^{-1}$ is a memory time constant: the timescale over which unused edges fade.
- The ratio $\alpha_G/\mu_G$ sets the scale of “how much conductance” a given current magnitude will produce at equilibrium.

If the current itself depends on conductance (as it does in circuits), the equilibrium becomes a fixed point of a coupled system. In practice, this coupling is often what yields emergent path selection.

---

## 4. From ARP to AIN: adaptive impedance as a stateful network

ARP treats an edge as purely resistive (conductive). AIN augments each edge with additional passive degrees of freedom:

- $C_{ij}(t)$: capacitance (nonnegative),
- $L_{ij}(t)$: inductance (nonnegative).

AIN uses the same reinforce/decay structure, but the driving signals differ:

### 4.1 AIN update equations

$$\boxed{\ \frac{dC_{ij}}{dt} = \alpha_C\,|V_{ij}(t)| - \mu_C\,C_{ij}(t)\ }$$

$$\boxed{\ \frac{dL_{ij}}{dt} = \alpha_L\,\left|\frac{dI_{ij}(t)}{dt}\right| - \mu_L\,L_{ij}(t)\ }$$

with $\alpha_C,\mu_C,\alpha_L,\mu_L$ as analogous gains and decay rates.

### 4.2 Frequency-aware impedance

For angular frequency $\omega$ (and assuming linear components at that instant), define:

$$Z_{ij}(t,\omega) = R_{ij}(t) + j\omega L_{ij}(t) + \frac{1}{j\omega C_{ij}(t)}.$$

Using $R_{ij}=1/G_{ij}$,

$$\boxed{\ Z_{ij}(t,\omega) = \frac{1}{G_{ij}(t)} + j\omega L_{ij}(t) - \frac{j}{\omega C_{ij}(t)}.\ }$$

This creates a network whose effective coupling depends on frequency and whose parameters adapt to local excitation.

---

## 5. Discrete-time simulation (practical integration)

In most computational uses, ARP/AIN are integrated in discrete time with step $\Delta t$.

### 5.1 Euler discretization (ARP)

$$G_{ij}^{k+1} = G_{ij}^{k} + \Delta t\,(\alpha_G |I_{ij}^{k}| - \mu_G G_{ij}^{k}).$$

To preserve nonnegativity, clamp:

$$G_{ij}^{k+1} \leftarrow \max(G_{\min},\, G_{ij}^{k+1}).$$

A small $G_{\min}>0$ avoids division-by-zero when converting to resistance.

### 5.2 Euler discretization (AIN)

$$C_{ij}^{k+1} = C_{ij}^{k} + \Delta t\,(\alpha_C |V_{ij}^{k}| - \mu_C C_{ij}^{k})$$

$$L_{ij}^{k+1} = L_{ij}^{k} + \Delta t\,\left(\alpha_L\left|\frac{I_{ij}^{k}-I_{ij}^{k-1}}{\Delta t}\right| - \mu_L L_{ij}^{k}\right)$$

Then clamp to $C_{\min},L_{\min}$ similarly.

### 5.3 Step size guidance

A conservative condition for explicit Euler stability on the decay term is:

$$\Delta t \lesssim \frac{1}{\mu_G},\quad \Delta t \lesssim \frac{1}{\mu_C},\quad \Delta t \lesssim \frac{1}{\mu_L}.$$

In practice, use $\Delta t$ one order of magnitude smaller than the fastest decay constant.

---

## 6. Coupling to flows: how $I$ (and $V$) are obtained

ARP/AIN do not by themselves define the currents and voltages; they define how edge parameters adapt **given** those signals. A typical simulation loop is:

1. **Given** edge states $G_{ij}(t)$ (and possibly $C,L$), compute the instantaneous network response to a driving condition.
2. Extract $I_{ij}(t)$ and (if needed) $V_{ij}(t)$.
3. Update $G,C,L$ using ARP/AIN.
4. Repeat.

### 6.1 Resistive flow model (common baseline)

In a purely resistive analog, with node potentials $\phi_i$, edge current is

$$I_{ij} = G_{ij}(\phi_i-\phi_j).$$

Potentials are determined by boundary conditions (sources/sinks) and Kirchhoff constraints.

### 6.2 Why path selection emerges

In many routing-like setups:

- Edges on “useful” paths carry more current.
- ARP increases their conductance.
- Increased conductance draws even more current.

This is a positive feedback loop that concentrates flow into certain structures, while the decay term prevents all edges from accumulating.

### 6.3 Minimal conceptual diagram (flow–adapt loop)

Below is a schematic of the coupled loop. “Solve flows” can be a circuit solve, a routing demand solve, or any rule that maps edge states to currents/voltages.

```text
   (boundary conditions / demand)
     |
     v
     +-------------------+
     |  Solve flows      |
     |  I_ij, V_ij       |
     +-------------------+
     |
     v
     +-------------------+
     |  Adapt edges      |
     |  dG/dt ~ |I| - G  |
     |  dC/dt ~ |V| - C  |
     |  dL/dt ~ |dI/dt|-L|
     +-------------------+
     |
     v
   updated (G,C,L)
     |
     +----> repeat
```

---

## 7. Stability, boundedness, and invariants (what is guaranteed)

### 7.1 Single-edge stability under bounded input

If $|I(t)|$ is bounded, $|I(t)|\le I_{\max}$, then

$$\frac{dG}{dt} \le \alpha_G I_{\max} - \mu_G G.$$

This comparison implies $G(t)$ remains bounded by a quantity on the order of $(\alpha_G/\mu_G)I_{\max}$ plus transient, assuming the flow solver does not create unbounded currents.

### 7.2 Nonnegativity

Continuous-time ODE preserves nonnegativity if $G(0)\ge 0$ and $|I|\ge 0$.

Discrete time requires clamping or a positivity-preserving integrator to avoid numerical undershoot.

### 7.3 Practical passivity constraints (AIN)

For physical interpretability, maintain:

$$G_{ij}(t) > 0,\quad C_{ij}(t) > 0,\quad L_{ij}(t) > 0.$$

This does not “prove passivity” in the full nonlinear adaptive system, but it prevents trivial nonphysical parameter values.

### 7.4 Coupled-network dynamics (important caveat)

Sections 7.1–7.3 are **local guarantees** (single-edge behavior under bounded driving) and numerical hygiene. The full ARP/AIN system is typically **coupled**:

- $I$ depends on $G$ (and possibly $C,L$),
- and $G,C,L$ depend on $I,V,dI/dt$.

As a result, global behaviors can include rapid concentration, slow drift, and (depending on the flow solver and constraints) oscillations or limit cycles.

Practical takeaway:

- If you want robust convergence and competition, use a bounded nonlinearity $\sigma(\cdot)$ and/or an explicit resource constraint (budget/normalization).
- Treat step size $\Delta t$ and decay rates $\mu$ as control knobs that set timescale separation between “solve flows” and “adapt edges.”

---

## 8. Parameterization: how to choose $(\alpha,\mu)$

ARP parameters are interpretable through equilibrium and timescale.

### 8.1 Choose memory depth first

Pick a decay constant $\mu_G$ such that

- desired half-life $T_{1/2}$ satisfies
  $$T_{1/2} = \frac{\ln 2}{\mu_G}.$$

Example: if you want unused edges to halve in strength every 10 seconds, set $\mu_G = \ln 2 / 10$.

### 8.2 Choose gain to match an equilibrium scale

If typical active edge current magnitude is $I_{\mathrm{typ}}$ and you want typical active edge equilibrium conductance $G_{\mathrm{typ}}$, set

$$\alpha_G = \mu_G\,\frac{G_{\mathrm{typ}}}{I_{\mathrm{typ}}}.$$

AIN parameters follow the same logic:

$$C_{\mathrm{eq}} = \frac{\alpha_C}{\mu_C}|V|,\quad L_{\mathrm{eq}} = \frac{\alpha_L}{\mu_L}\left|\frac{dI}{dt}\right|.$$

### 8.3 A note on saturation

Real implementations often add saturation to prevent runaway reinforcement under extreme signals:

$$\frac{dG}{dt} = \alpha_G \sigma(|I|) - \mu_G G,$$

where $\sigma$ is a bounded function (e.g., $\sigma(x)=\tanh(x/I_0)$ or $\sigma(x)=x/(1+x/I_0)$). This is optional; the canonical ARP form is linear in $|I|$.

---

## 9. Minimal algorithm (reference pseudocode)

Below is a minimal architecture that works across routing-like tasks.

1. Initialize conductances $G_{ij}(0)=G_0$ for all edges.
2. For each step $k$:
   - Solve for node potentials (or flows) under your task’s boundary conditions.
   - Compute edge currents $I_{ij}^{k}$.
   - Update each edge:
     $$G_{ij}^{k+1} = \max\Big(G_{\min},\,G_{ij}^{k} + \Delta t\,(\alpha_G|I_{ij}^{k}| - \mu_G G_{ij}^{k})\Big).$$
   - Optionally compute a global scalar such as $\mathrm{ANE}(t)$.

If AIN is enabled, update $C$ and $L$ similarly using $|V|$ and $|dI/dt|$.

---

## 10. Example: closed-form intuition on a simple two-path network

Consider two parallel paths from source $s$ to sink $t$.

- Path A has total conductance $G_A(t)$ (aggregate of edges).
- Path B has total conductance $G_B(t)$.

Assume a fixed applied potential difference $\Delta\phi$ between $s$ and $t$ and ignore internal node structure so currents satisfy:

$$I_A = G_A\,\Delta\phi,\quad I_B = G_B\,\Delta\phi.$$

ARP updates become:

$$\frac{dG_A}{dt} = \alpha_G |I_A| - \mu_G G_A = \alpha_G \Delta\phi\,G_A - \mu_G G_A = (\alpha_G\Delta\phi-\mu_G)G_A.$$

Similarly for $G_B$.

This toy shows:

- If $\alpha_G\Delta\phi > \mu_G$, both paths grow exponentially (unstable without saturation or resource constraints).
- In realistic networks, currents depend on the entire graph and boundary conditions, and practical implementations add constraints (normalization, saturation, limited total resource, or load-dependent sources).

This motivates either:

- saturation functions, and/or
- conservation constraints such as a fixed total conductance budget.

The full ARP approach is best understood as “reinforce used edges while the system continuously recomputes flows”; the network structure then concentrates activity.

A practical rule of thumb: if a deployment shows runaway amplification, add (i) saturation, (ii) a conductance budget/normalization, or (iii) a source model that limits current supply.

---

## 11. Testable predictions and diagnostics

ARP/AIN is not just a metaphor; it implies measurable behaviors.

### 11.1 Hysteresis / memory

If sources are turned off, conductances decay with time constant $1/\mu_G$. When sources are turned on again, previously reinforced edges re-amplify faster if they retained higher $G$.

### 11.2 Sparse backbone emergence

Under repeated routing tasks, a sparse subgraph should carry most of the current while other edges decay toward $G_{\min}$.

### 11.3 Frequency selectivity (AIN)

If AIN is active, repeated high-frequency excitation tends to increase $L$ (via $|dI/dt|$), while repeated voltage excursions increase $C$. The resulting $Z(t,\omega)$ can develop band-like preferences.

### 11.4 Useful plots

- Histograms of $G_{ij}$ over time.
- Current vs conductance scatter $|I_{ij}|$ vs $G_{ij}$.
- Backbone extraction: keep edges with $G_{ij}$ above a threshold and visualize connectivity.
- $\mathrm{ANE}(t)$ as a global convergence/organization signal.

### 11.5 Falsifiers / negative predictions (what should fail)

These are deliberately sharp statements intended to be testable:

1. **Remove decay ($\mu_G=0$)**: conductance will not forget; backbone sparsity and hysteresis structure should degrade into “accumulate everywhere,” unless a separate hard constraint is present.
2. **Remove competition (no budget/normalization and no saturation)**: on tasks with sustained driving, multiple alternative routes tend to co-amplify; the model should become sensitive to initialization and may fail to produce a stable sparse backbone.

---

## 12. Limitations and what ARP/AIN does NOT claim

- ARP is an adaptive rule, not a proof of optimality. It can produce good routing/selection behavior but depends on the flow solver, constraints, and task formulation.
- ARP does not “beat” NP-hardness by itself; the computational cost still appears in the physics/solver step, the precision required, or the convergence time.
- AIN introduces more degrees of freedom; without careful constraints, it can overfit or become numerically stiff.

---

## 13. Roadmap: from white paper to production model

1. **Formalize the task coupling**: define how sources/sinks or demands are set.
2. **Choose constraints**: saturation, budgets, or normalization to ensure bounded behavior.
3. **Benchmark**: compare to classical baselines (shortest path, flow-based heuristics, gradient-based optimizers).
4. **Ablations**: ARP alone vs ARP+AIN vs saturation variants.
5. **Hardware experiments**: verify time-constant memory and backbone emergence under controlled excitation.

---

## Appendix A: quick reference equations

**ARP**

$$\frac{dG_{ij}}{dt} = \alpha_G |I_{ij}| - \mu_G G_{ij}$$

$$G_{ij,\mathrm{eq}} = \frac{\alpha_G}{\mu_G}|I_{ij,\mathrm{eq}}|$$

**AIN**

$$\frac{dC_{ij}}{dt} = \alpha_C |V_{ij}| - \mu_C C_{ij}$$

$$\frac{dL_{ij}}{dt} = \alpha_L \left|\frac{dI_{ij}}{dt}\right| - \mu_L L_{ij}$$

$$Z_{ij}(t,\omega) = \frac{1}{G_{ij}(t)} + j\omega L_{ij}(t) - \frac{j}{\omega C_{ij}(t)}$$

**ANE (one canonical metric)**

$$\mathrm{ANE}(t) = \frac{\sum_{ij} G_{ij}(t)\,|I_{ij}(t)|}{\sum_{ij}|I_{ij}(t)|}$$
