---
sidebar_position: 30
title: "Exercises and Problems"
description: "Practice problems for self-assessment: from elementary to research-level, with solutions"
---

# Exercises and Problems

> *"You cannot teach a person anything; you can only help them discover it within themselves."*
> — Galileo Galilei


:::info Who This Chapter Is For
Problems for self-assessment covering all chapters of the textbook — from elementary to research-level. The reader will be able to test their understanding of the CC formalism on concrete examples.
:::

We have traveled the full path: from axioms — through dynamics, stability, and learning — to philosophy, comparison with competitors, measurement methodology, and the interdisciplinary bridge. Now it is time to **test understanding**.

Theory without practice is a dead letter. This section contains self-assessment problems organized by difficulty level and by textbook chapter. Each problem is accompanied by hints and references to the relevant sections. The solution is provided in collapsed blocks — try to solve it yourself first.

:::note Difficulty Levels
- ★ — elementary (require only substitution into a formula). A schoolchild can handle these.
- ★★ — intermediate (require understanding the connections between concepts)
- ★★★ — advanced (require independent derivation)
- ★★★★ — research-level (open questions)
:::

:::info How to Use This Section
1. Start with problems at your level (see recommendations at the end)
2. Do not look at the solution until you have tried on your own
3. If stuck — read the hint, then the relevant section
4. Problems ★★★★ have no "correct answers" — these are research questions
:::

---

## 0. Warm-Up: 2×2 Matrices (for Beginners) {#блок-0}

Before diving into $7 \times 7$, let us warm up on small matrices.

### Problem 0.1 ★ What is a density matrix?

A density matrix $\rho$ is a matrix that is: (a) Hermitian ($\rho = \rho^\dagger$), (b) positive semi-definite ($\langle v|\rho|v \rangle \geq 0$ for all $v$), (c) with unit trace ($\mathrm{Tr}(\rho) = 1$).

For $2 \times 2$:

$$
\rho = \begin{pmatrix} a & c \\ c^* & 1-a \end{pmatrix}, \quad a \in [0,1], \quad |c|^2 \leq a(1-a)
$$

**(a)** Verify that $\rho_1 = \begin{pmatrix} 0.7 & 0.1 \\ 0.1 & 0.3 \end{pmatrix}$ is a density matrix.

**(b)** Is $\rho_2 = \begin{pmatrix} 0.5 & 0.6 \\ 0.6 & 0.5 \end{pmatrix}$ a density matrix?

**(c)** Compute the purity $P = \mathrm{Tr}(\rho_1^2)$.

<details>
<summary>Solution</summary>

**(a)** Check: $\mathrm{Tr} = 0.7 + 0.3 = 1$ (ok). Hermitian: $c = c^* = 0.1$ (ok). Positivity: $|c|^2 = 0.01 \leq a(1-a) = 0.7 \times 0.3 = 0.21$ (ok). **Yes**, this is a density matrix.

**(b)** $|c|^2 = 0.36$, $a(1-a) = 0.25$. $0.36 > 0.25$ — positive semi-definiteness violated. **No**, this is not a density matrix. (Eigenvalues: $1.1$ and $-0.1$ — one is negative!)

**(c)** $\rho_1^2 = \begin{pmatrix} 0.7 & 0.1 \\ 0.1 & 0.3 \end{pmatrix}^2 = \begin{pmatrix} 0.50 & 0.10 \\ 0.10 & 0.10 \end{pmatrix}$. $P = \mathrm{Tr}(\rho_1^2) = 0.50 + 0.10 = 0.60$.

Alternatively: $P = a^2 + (1-a)^2 + 2|c|^2 = 0.49 + 0.09 + 0.02 = 0.60$.

</details>

---

### Problem 0.2 ★ Minimum and Maximum Purity (2×2)

**(a)** What is the minimum purity for a $2 \times 2$ density matrix? For which $\rho$ is it achieved?

**(b)** What is the maximum? For which $\rho$?

**(c)** If CC were to work for $N=2$ with threshold $P_{\text{crit}} = 2/N$, what would the threshold be?

<details>
<summary>Solution</summary>

**(a)** Minimum at $\rho = I/2 = \begin{pmatrix} 0.5 & 0 \\ 0 & 0.5 \end{pmatrix}$. $P = 0.25 + 0.25 = 0.50 = 1/N = 1/2$.

**(b)** Maximum at a pure state (rank 1), e.g. $\rho = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$. $P = 1$.

**(c)** $P_{\text{crit}} = 2/2 = 1$ — only a pure state is viable! For $N = 2$ there is no "Goldilocks zone" — the system is either perfect or dead. This is one reason why $N = 2$ is insufficient for consciousness.

</details>

---

### Problem 0.3 ★ Stress for 2×2

Define "stress" by analogy with CC: $\sigma_k = 1 - N \cdot \gamma_{kk}$ for $N=2$.

**(a)** Compute $\sigma_1, \sigma_2$ for $\rho_1$ from Problem 0.1.

**(b)** Interpret: which "dimension" is in deficit?

<details>
<summary>Solution</summary>

**(a)** $\sigma_1 = 1 - 2 \times 0.7 = -0.4$ (surplus), $\sigma_2 = 1 - 2 \times 0.3 = 0.4$ (deficit).

**(b)** Dimension 2 is in deficit ($\sigma_2 > 0$): it receives less than the "fair share" of $1/2$. Dimension 1 is in surplus ($\sigma_1 < 0$).

</details>

---

## 1. Coherence Matrix and Purity {#блок-1}

### Problem 1.1 ★ Computing Purity

Given a coherence matrix in the diagonal approximation:

$$
\Gamma = \mathrm{diag}(0.20, 0.18, 0.15, 0.14, 0.13, 0.12, 0.08)
$$

**(a)** Compute the purity $P = \mathrm{Tr}(\Gamma^2)$.

**(b)** Is the system viable? Compare with $P_{\text{crit}} = 2/7$.

**(c)** Compute all 7 components of the stress tensor $\sigma_k = 1 - 7\gamma_{kk}$.

**(d)** Which dimension is in a critical state?

:::tip Hint
For a diagonal matrix $P = \sum_k \gamma_{kk}^2$. **See:** [Purity](/docs/core/dynamics/viability#определение-чистоты), [Stress Tensor](./definitions#тензор-напряжений).
:::

<details>
<summary>Solution</summary>

**(a)** $P = 0.20^2 + 0.18^2 + 0.15^2 + 0.14^2 + 0.13^2 + 0.12^2 + 0.08^2 = 0.04 + 0.0324 + 0.0225 + 0.0196 + 0.0169 + 0.0144 + 0.0064 = 0.1522$

**(b)** $P = 0.1522 < 2/7 \approx 0.286$. The system is **non-viable**.

**(c)** $\sigma_A = 1 - 7 \times 0.20 = -0.40$, $\sigma_S = 1 - 7 \times 0.18 = -0.26$, $\sigma_D = 1 - 7 \times 0.15 = -0.05$, $\sigma_L = 1 - 7 \times 0.14 = 0.02$, $\sigma_E = 1 - 7 \times 0.13 = 0.09$, $\sigma_O = 1 - 7 \times 0.12 = 0.16$, $\sigma_U = 1 - 7 \times 0.08 = 0.44$.

**(d)** $\sigma_U = 0.44$ — maximum stress. The Unity (U) dimension is the weakest. But none exceeds 1, so by $\sigma$ the system is still "inside," although by $P$ it is already non-viable. This is because $P < 2/7$ can arise with moderate but *uniformly distributed* stresses.

</details>

---

### Problem 1.2 ★★ Maximum and Minimum Purity

**(a)** What is the minimum purity of a matrix $\Gamma \in \mathcal{D}(\mathbb{C}^7)$? At which $\Gamma$ is it achieved?

**(b)** What is the maximum purity? At which $\Gamma$?

**(c)** Show that $P_{\text{crit}} = 2/7$ divides the segment $[1/7, 1]$ exactly at the point where the system acquires the ability to **distinguish itself from chaos** (the Frobenius norm $\|\Gamma - I/7\|_F$ exceeds the distinguishability threshold).

:::tip Hint
The minimum purity is achieved at $\Gamma = I/7$ (maximally mixed state). The maximum — at a pure state (rank 1). **See:** [Theorem on Critical Purity](/docs/proofs/dynamics/theorem-purity-critical).
:::

---

### Problem 1.3 ★ Coherence and Phases

Given the off-diagonal coherence $\gamma_{AE} = 0.05 \cdot e^{i\pi/3}$.

**(a)** What is the modulus $|\gamma_{AE}|$?

**(b)** What is the phase $\theta_{AE}$?

**(c)** What does non-zero coherence between Articulation (A) and Interiority (E) physically mean?

:::tip Hint
**See:** [Coherence Matrix](/docs/core/dynamics/coherence-matrix), [Definitions](./definitions).
:::

<details>
<summary>Solution</summary>

**(a)** $|\gamma_{AE}| = 0.05$.

**(b)** $\theta_{AE} = \pi/3 = 60°$.

**(c)** Non-zero A–E coherence means that perception (A) and self-awareness (E) are *aligned*: changes in perception affect self-awareness and vice versa. This corresponds to interoceptive perception — the ability to feel one's body "from the inside." A person with high $|\gamma_{AE}|$ is well-aware of their bodily sensations.

</details>

---

### Problem 1.4 ★ Uniform System

The matrix $\Gamma = I/7$ — the maximally mixed state.

**(a)** Compute $P$, $\sigma_k$ for all $k$, $\|\sigma\|_\infty$.

**(b)** Why is a system with $\Gamma = I/7$ "dead," even though no $\sigma_k$ exceeds 0?

**(c)** Draw the $\sigma$-profile (7 bars) for $\Gamma = I/7$ and for the system from Problem 1.1. How do they differ?

<details>
<summary>Solution</summary>

**(a)** $P = 7 \times (1/7)^2 = 1/7 \approx 0.143$. $\sigma_k = 1 - 7 \times (1/7) = 0$ for all $k$. $\|\sigma\|_\infty = 0$.

**(b)** Paradox: $\sigma = 0$ (no deficit in anything), but $P = 1/7 < 2/7$ (non-viable). Reason: $\Gamma = I/7$ — *complete indistinguishability*. All dimensions are the same, there is no structure, no information. The system does not "suffer" (σ = 0), but it does not "live" either — it *does not exist as an organized unit*. This is like a perfectly mixed solution: no component is in deficit, but the solution has no structure.

**(c)** For $I/7$: all bars at zero. For Problem 1.1: A and S are below zero (surplus), U is significantly above (deficit). The profile is uneven, pointing to a specific problem (unity deficit).

</details>

---

### Problem 1.5 ★★ Threshold through Coherences

The system is diagonal with $\gamma_{kk} = 1/7$ for all $k$, but has off-diagonal coherences $|\gamma_{ij}| = c$ for all $i \neq j$.

**(a)** Express $P$ in terms of $c$.

**(b)** At what $c$ is $P = 2/7$ achieved?

**(c)** Interpret: what does it mean to "reach purity through coherences alone"?

:::tip Hint
$P = \sum_k \gamma_{kk}^2 + \sum_{i \neq j} |\gamma_{ij}|^2 = 7 \times (1/7)^2 + 42 \times c^2 = 1/7 + 42c^2$.
:::

<details>
<summary>Solution</summary>

**(a)** $P = 1/7 + 42c^2$.

**(b)** $2/7 = 1/7 + 42c^2 \Rightarrow c^2 = 1/(7 \times 42) = 1/294 \Rightarrow c = 1/\sqrt{294} \approx 0.058$.

**(c)** A system with a uniform diagonal but with coherences $c \approx 0.058$ — is "viable through connections." Each dimension taken separately is unremarkable ($\gamma_{kk} = 1/7$), but *coordination* between them ($|\gamma_{ij}| > 0$) creates organization. This is the analog of an organization where each department is average, but teamwork is outstanding.

</details>

---

## 2. Dynamics and Evolution {#блок-2}

### Problem 2.1 ★★ Lindblad Dissipation

Consider a one-dimensional (toy) model: $\Gamma = \begin{pmatrix} p & c \\ c^* & 1-p \end{pmatrix}$ with dissipator $\mathcal{D}[\Gamma] = -\gamma(p - 1/2, c, c^*, 1/2 - p)$.

**(a)** To what state does $\Gamma$ tend as $\tau \to \infty$?

**(b)** Compute the purity $P(\tau)$ and show that it decreases monotonically.

**(c)** Connect this with the CC thesis: "without regeneration the system dies."

<details>
<summary>Solution</summary>

**(a)** $\dot{p} = -\gamma(p - 1/2)$, $\dot{c} = -\gamma c$. Solutions: $p(\tau) = 1/2 + (p_0 - 1/2)e^{-\gamma\tau}$, $c(\tau) = c_0 e^{-\gamma\tau}$. As $\tau \to \infty$: $\Gamma \to I/2$ — maximally mixed state.

**(b)** $P = p^2 + (1-p)^2 + 2|c|^2 = 2(p - 1/2)^2 + 1/2 + 2|c|^2$. Substituting: $P(\tau) = 2(p_0 - 1/2)^2 e^{-2\gamma\tau} + 1/2 + 2|c_0|^2 e^{-2\gamma\tau}$. $dP/d\tau = -4\gamma[(p_0 - 1/2)^2 + |c_0|^2]e^{-2\gamma\tau} < 0$. Purity **decreases monotonically**.

**(c)** Without regeneration ($\mathcal{R} = 0$) purity always falls. For $N=2$: $P \to 1/2$. For $N=7$: $P \to 1/7$. The system degrades to maximum chaos. Regeneration $\mathcal{R}$ is the only thing that can oppose this degradation.

</details>

---

### Problem 2.2 ★★★ Regeneration as Rescue

A regenerative term is added to the system from Problem 2.1:

$$
\mathcal{R}[\Gamma] = \kappa \cdot (\rho_* - \Gamma)
$$

where $\rho_* = \begin{pmatrix} 0.7 & 0.2 \\ 0.2 & 0.3 \end{pmatrix}$ is the target state, $\kappa > 0$.

**(a)** Find the stationary state $\Gamma_{\infty}$ of the full dynamics $\dot{\Gamma} = \mathcal{D}[\Gamma] + \mathcal{R}[\Gamma]$.

**(b)** At what $\kappa$ is the purity of the stationary state $P(\Gamma_\infty) > 2/7$?

**(c)** Interpret the result: what happens with "weak" ($\kappa \ll \gamma$) and "strong" ($\kappa \gg \gamma$) regeneration?

<details>
<summary>Solution</summary>

**(a)** $\dot{\Gamma} = 0$: $-\gamma(\Gamma - I/2) + \kappa(\rho_* - \Gamma) = 0$. $(\gamma + \kappa)\Gamma = \gamma \cdot I/2 + \kappa \cdot \rho_*$. $\Gamma_\infty = \frac{\gamma \cdot I/2 + \kappa \cdot \rho_*}{\gamma + \kappa}$.

$p_\infty = \frac{\gamma/2 + 0.7\kappa}{\gamma + \kappa}$, $c_\infty = \frac{0.2\kappa}{\gamma + \kappa}$.

**(b)** $P(\Gamma_\infty) = 2(p_\infty - 1/2)^2 + 1/2 + 2|c_\infty|^2$. For $N=2$, $P_{\text{crit}} = 2/N = 1$ — a pure state is required, which is impossible. But if $P_{\text{crit}} = 2/7$ is used (for generality): $P > 2/7 \approx 0.286$ holds for sufficiently large $\kappa/\gamma$.

Let $r = \kappa/\gamma$: $p_\infty = (0.5 + 0.7r)/(1+r)$, $c_\infty = 0.2r/(1+r)$. At $r = 1$: $p = 0.6$, $c = 0.1$, $P = 0.02 + 0.5 + 0.02 = 0.54$. At $r = 0.1$: $p = 0.518$, $c = 0.018$, $P \approx 0.5007$. Both > 2/7.

**(c)** With $\kappa \ll \gamma$ (weak regeneration): $\Gamma_\infty \approx I/2$ — dissipation wins, the system is "dead." With $\kappa \gg \gamma$ (strong regeneration): $\Gamma_\infty \approx \rho_*$ — regeneration wins, the system is close to "ideal." The optimum is balance, the Goldilocks zone.

</details>

---

### Problem 2.3 ★★ Lifetime

The system starts at $P(0) = 0.35 > P_{\text{crit}}$. Regeneration is disabled ($\kappa = 0$). Dissipation is exponential: $P(\tau) = 1/7 + (P(0) - 1/7) \cdot e^{-\gamma \tau}$.

**(a)** Find the time $\tau_*$ at which $P(\tau_*) = P_{\text{crit}} = 2/7$.

**(b)** For $\gamma = 0.1$ compute $\tau_*$ numerically.

**(c)** How is this result related to the concept of system "lifetime"? **See:** [Stability](./stability#время-жизни).

<details>
<summary>Solution</summary>

**(a)** $2/7 = 1/7 + (0.35 - 1/7)e^{-\gamma\tau_*}$. $1/7 = (0.35 - 0.143)e^{-\gamma\tau_*} = 0.207 \cdot e^{-\gamma\tau_*}$. $e^{-\gamma\tau_*} = (1/7)/0.207 = 0.690$. $\tau_* = -\ln(0.690)/\gamma = 0.371/\gamma$.

**(b)** $\tau_* = 0.371/0.1 = 3.71$ time units.

**(c)** $\tau_*$ is the time in which the system loses viability in the absence of regeneration. The larger the initial purity (health reserve) and the smaller the dissipation, the longer the system lives. Regeneration ($\kappa > 0$) can make $\tau_* = \infty$ — the system lives forever (as long as $\kappa$ is sufficient).

</details>

---

### Problem 2.4 ★ Balance of Dissipation and Regeneration

Stationary purity (at constant $\gamma$ and $\kappa$):

$$
P_\infty = \frac{\kappa \cdot P_{\rho_*} + \gamma \cdot P_{\min}}{\kappa + \gamma}
$$

where $P_{\rho_*}$ is the purity of the target state, $P_{\min} = 1/7$.

**(a)** If $P_{\rho_*} = 0.5$, at what ratio $\kappa/\gamma$ is $P_\infty = 2/7$ achieved?

**(b)** Interpret: which real systems have $\kappa/\gamma \ll 1$? And $\kappa/\gamma \gg 1$?

<details>
<summary>Solution</summary>

**(a)** $2/7 = (\kappa \cdot 0.5 + \gamma \cdot 1/7) / (\kappa + \gamma)$. Let $r = \kappa/\gamma$: $2/7 = (0.5r + 1/7)/(r + 1)$. $2(r+1)/7 = 0.5r + 1/7$. $2r/7 + 2/7 = 0.5r + 1/7$. $2r/7 - 0.5r = 1/7 - 2/7 = -1/7$. $(2/7 - 1/2)r = -1/7$. $(-3/14)r = -1/7$. $r = (1/7) \times (14/3) = 2/3$.

At $\kappa/\gamma = 2/3$ the system is *exactly on the threshold*. Below — it dies, above — it lives.

**(b)** $\kappa/\gamma \ll 1$: dissipation wins — aging without regeneration. Example: a mouse (lives 2 years, high metabolism, rapid aging). $\kappa/\gamma \gg 1$: regeneration wins — the system is essentially immortal. Example: Turritopsis dohrnii (a jellyfish capable of reverse development).

</details>

---

## 3. Stress Tensor and Diagnostics {#блок-3}

### Problem 3.1 ★ Interpreting a Stress Profile

Two organizations have the following stress profiles:

**Organization X:** $\sigma = [0.2, 0.3, 0.1, 0.2, 0.8, 0.3, 0.4]$

**Organization Y:** $\sigma = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]$

**(a)** Which organization is in a more dangerous position? Why?

**(b)** What type of intervention does each need?

**(c)** What failure pattern threatens Organization X? **See:** [Diagnostics](./diagnostics#паттерны-отказов)

<details>
<summary>Solution</summary>

**(a)** Organization X: $\|\sigma\|_\infty = 0.8$ (E: Interiority). Organization Y: $\|\sigma\|_\infty = 0.5$ (all equal). By $\|\sigma\|_\infty$ — X is more dangerous (0.8 > 0.5). But Y has a *total* stress $\sum \sigma_k = 3.5$ > X: $\sum = 2.3$. X — an acute problem in one place (E peak). Y — a chronically weakened system "on all fronts."

**(b)** X: **targeted intervention** — strengthen reflection and feedback ($\sigma_E = 0.8$ — almost critical). Y: **systemic intervention** — general reorganization, because no dimension is normal.

**(c)** X risks entering the **death spiral**: $\sigma_E = 0.8 \to \mathrm{Coh}_E \downarrow \to \kappa \downarrow \to P \downarrow \to$ all $\sigma_k$ rise. A single deficit launches a cascade.

</details>

---

### Problem 3.2 ★★ Death Spiral

Show that the cascade $\sigma_E \uparrow \to \sigma_O \uparrow \to \sigma_U \uparrow$ (death spiral) follows from CC formulas:

1. $\sigma_E \uparrow$ → $\mathrm{Coh}_E \downarrow$
2. $\mathrm{Coh}_E \downarrow$ → $\kappa \downarrow$ (through the formula $\kappa = \kappa_{\text{bootstrap}} + \kappa_0 \cdot \mathrm{Coh}_E$)
3. $\kappa \downarrow$ → $P \downarrow$
4. $P \downarrow$ → $\sigma_O \uparrow$, $\sigma_U \uparrow$

**See:** [Stability](./stability#спираль-смерти), [Connection of Regeneration and E-Coherence](./axiomatics#связь-регенерации-и-e-когерентности)

---

### Problem 3.3 ★★ Reverse Computation: from σ to Γ

Given the σ-profile: $\sigma = [0.3, 0.1, 0.4, 0.2, 0.6, 0.3, 0.5]$.

**(a)** Recover the diagonal elements $\gamma_{kk}$.

**(b)** Compute $P$ in the diagonal approximation.

**(c)** Is the system viable?

<details>
<summary>Solution</summary>

**(a)** $\gamma_{kk} = (1 - \sigma_k)/7$. $\gamma = (0.100, 0.129, 0.086, 0.114, 0.057, 0.100, 0.071)$.

**(b)** $P = \sum \gamma_{kk}^2 = 0.010 + 0.017 + 0.007 + 0.013 + 0.003 + 0.010 + 0.005 = 0.065$. But $\sum \gamma_{kk} = 0.657 \neq 1$! So the diagonal approximation from the σ-profile is *incorrect* — part of the "mass" is in the off-diagonal elements (or the σ-profile needs normalization).

**(c)** $P = 0.065 \ll 2/7 \approx 0.286$ — **non-viable** in the diagonal approximation. Even with coherences it is hard to achieve $P > 2/7$ with such small $\gamma_{kk}$.

</details>

---

### Problem 3.4 ★ Visualization: σ-Diagram

Draw the σ-profile (radar / spider chart) for the following systems:

**(a)** Healthy person: $\sigma = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]$

**(b)** Patient with depression: $\sigma = [0.2, 0.2, 0.7, 0.3, 0.6, 0.5, 0.4]$

**(c)** Startup on the brink of bankruptcy: $\sigma = [0.3, 0.6, 0.2, 0.4, 0.3, 0.9, 0.7]$

```mermaid
%%{init: {'theme': 'default'}}%%
radar
    title σ-profiles of three systems
    axis A, S, D, L, E, O, U
    "Healthy" : [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    "Depression" : [0.2, 0.2, 0.7, 0.3, 0.6, 0.5, 0.4]
    "Startup" : [0.3, 0.6, 0.2, 0.4, 0.3, 0.9, 0.7]
```

**(d)** Which profile is the most "peaked" (one spike)? Which is the most "round" (uniform)?

<details>
<summary>Solution</summary>

**(d)** Startup — most "peaked" (peak O = 0.9: financial deficit). Healthy — most "round" (all at 0.1). Depression — intermediate, with two pronounced peaks (D = 0.7 and E = 0.6).

</details>

---

## 4. Consciousness and Self-Observation {#блок-4}

### Problem 4.1 ★★ The Triple-Lock Threshold

A system has the following parameters: $P = 0.35$, $R = 0.25$, $\Phi = 1.5$.

**(a)** Are all three consciousness conditions satisfied ($P > 2/7$, $R \geq 1/3$, $\Phi \geq 1$)?

**(b)** Which condition is violated?

**(c)** What does this mean interpretively? What kind of system is this — one that is integrated and viable, but not reflective?

**(d)** Give an example of a real system with such a profile.

<details>
<summary>Solution</summary>

**(a)** $P = 0.35 > 2/7 \approx 0.286$ (ok), $R = 0.25 < 1/3 \approx 0.333$ (**not ok**), $\Phi = 1.5 \geq 1$ (ok). **No**, not all conditions are met.

**(b)** $R < 1/3$ — insufficient reflection.

**(c)** The system is viable (sufficiently organized) and integrated (does not break apart), but *does not know itself* — its self-model is inaccurate. It "lives," but does not "become aware."

**(d)** An insect (bee): high organization (P > 2/7), complex social integration (Φ > 1), but limited metacognition (R < 1/3). Or: a well-functioning thermostat with feedback.

</details>

---

### Problem 4.2 ★★★ SAD and the Depth Ceiling

Self-Awareness Depth:

$$
\mathrm{SAD}(n) = P_{\text{crit}}^{(n)} < P \quad \text{where} \quad P_{\text{crit}}^{(n)} = P_{\text{crit}} \cdot \frac{3^{n-1}}{n+1}
$$

**(a)** Compute $P_{\text{crit}}^{(1)}, P_{\text{crit}}^{(2)}, P_{\text{crit}}^{(3)}, P_{\text{crit}}^{(4)}$.

**(b)** Show that $P_{\text{crit}}^{(4)} > 1$ → SAD = 4 is impossible for any system with $P \leq 1$.

**(c)** Therefore, $\mathrm{SAD}_{\max} = 3$. Interpret: what does "I am aware that I am aware that I am aware" mean — and why is the 4th level impossible?

**See:** [Prediction 12](./predictions#предсказание-12), [Depth Tower](/docs/consciousness/hierarchy/depth-tower#критическая-чистота-sad)

<details>
<summary>Solution</summary>

**(a)** $P_{\text{crit}} = 2/7 \approx 0.286$.
- $P_{\text{crit}}^{(1)} = (2/7) \cdot 1/2 = 1/7 \approx 0.143$
- $P_{\text{crit}}^{(2)} = (2/7) \cdot 3/3 = 2/7 \approx 0.286$
- $P_{\text{crit}}^{(3)} = (2/7) \cdot 9/4 = 18/28 = 9/14 \approx 0.643$
- $P_{\text{crit}}^{(4)} = (2/7) \cdot 27/5 = 54/35 \approx 1.543$

**(b)** $P_{\text{crit}}^{(4)} = 54/35 \approx 1.543 > 1$. But $P \leq 1$ for any density matrix (this is a mathematical property: $P = \mathrm{Tr}(\Gamma^2) \leq \mathrm{Tr}(\Gamma) = 1$). Therefore $P < P_{\text{crit}}^{(4)}$ always, and SAD = 4 is **impossible**.

**(c)** SAD = 1: "I am aware of X" (consciousness). SAD = 2: "I am aware that I am aware of X" (meta-consciousness). SAD = 3: "I am aware that I am aware that I am aware of X" (meta-meta-consciousness — accessible to advanced meditators, philosophers). SAD = 4: "I am aware that I am aware that I am aware that I am aware of X" — this requires purity $P > 1.54$, which is physically impossible. The recursion of self-observation *exhausts* coherence resources.

</details>

---

### Problem 4.3 ★★ Consciousness Measure C

Three systems:

| System | $P$ | $R$ | $\Phi$ |
|--------|-----|-----|--------|
| Bacterium | 0.20 | 0.05 | 0.3 |
| Cat | 0.32 | 0.30 | 1.8 |
| Human | 0.35 | 0.40 | 2.1 |

**(a)** For each: which thresholds are met ($P > 2/7$, $R \geq 1/3$, $\Phi \geq 1$)?

**(b)** Compute $C = \Phi \times R$ for each.

**(c)** Which systems are "conscious" (all three thresholds met)?

<details>
<summary>Solution</summary>

**(a)** Bacterium: $P = 0.20 < 2/7$ (no), $R = 0.05 < 1/3$ (no), $\Phi = 0.3 < 1$ (no). 0 of 3.
Cat: $P = 0.32 > 2/7$ (yes), $R = 0.30 < 1/3$ (no!), $\Phi = 1.8 > 1$ (yes). 2 of 3.
Human: $P = 0.35 > 2/7$ (yes), $R = 0.40 > 1/3$ (yes), $\Phi = 2.1 > 1$ (yes). 3 of 3.

**(b)** Bacterium: $C = 0.3 \times 0.05 = 0.015$. Cat: $C = 1.8 \times 0.30 = 0.54$. Human: $C = 2.1 \times 0.40 = 0.84$.

**(c)** Only the **human** satisfies all three thresholds. The cat is "almost" — it lacks reflection ($R = 0.30$ instead of the required $0.33$). This is consistent with cats demonstrating *limited* metacognition.

</details>

---

### Problem 4.4 ★★ The Goldilocks Zone

The Goldilocks zone: $P \in (2/7, 3/7]$ ([T-124](./phase-diagram-cc)).

**(a)** Compute the boundaries: $2/7 \approx ?$, $3/7 \approx ?$.

**(b)** What is the "width" of the zone: $\Delta P = 3/7 - 2/7$?

**(c)** If $P = 0.45 > 3/7 \approx 0.429$ — the system is "too organized." What does this mean? Give an example.

<details>
<summary>Solution</summary>

**(a)** $2/7 \approx 0.286$, $3/7 \approx 0.429$.

**(b)** $\Delta P = 1/7 \approx 0.143$ — quite a narrow window!

**(c)** $P > 3/7$ — rigidity. The system is too ordered: it cannot adapt to changes. Example: an authoritarian organization with a rigid hierarchy. Or: obsessive-compulsive disorder (excessive orderliness of thought). Or: an overfitted neural network (overfitting — the model has "memorized" the training data and does not generalize).

</details>

---

## 5. Philosophy and Theory Comparison {#блок-5}

### Problem 5.1 ★★ The Zombie Argument

A philosophical zombie is a creature identical to a human in all respects, except for subjective experience.

**(a)** Why does the [No-Zombie theorem](./theorems#теорема-81-условная-необходимость-интериорности-no-zombie) make zombies impossible in CC?

**(b)** Compare with IIT's position on this question.

**(c)** Is this an advantage or a limitation of CC?

**See:** [Philosophical Foundations](./philosophy#hard-problem)

---

### Problem 5.2 ★★ AI and Consciousness

**(a)** Can a modern language model (GPT-4, Claude) be conscious by CC criteria?

**(b)** Which of the four conditions ($P > 2/7$, $R \geq 1/3$, $\Phi \geq 1$, $D_{\text{diff}} \geq 2$) might it satisfy? Which — principally cannot?

**(c)** What needs to be changed in the architecture to bring AI closer to the consciousness threshold? **See:** [Applications](./applications).

---

### Problem 5.3 ★★ IIT vs CC

**(a)** Name three key differences between IIT and CC.

**(b)** In what sense does CC "include" IIT as a special case?

**(c)** What does IIT do better than CC?

**See:** [Comparison with Alternative Theories](./comparison#iit)

---

### Problem 5.4 ★★★ Panpsychism vs CC

**(a)** Formulate the key distinction between CC and panpsychism in one sentence.

**(b)** What is the "combination problem" and why does CC avoid it?

**(c)** Under what conditions would CC *become* panpsychism? (What would need to be changed in the axioms?)

**See:** [Philosophical Foundations](./philosophy#онтология)

<details>
<summary>Solution</summary>

**(a)** CC is emergentism with a precise threshold ($P > 2/7$, $R \geq 1/3$, $\Phi \geq 1$), not unlimited panpsychism: a stone does *not* have experience.

**(b)** The combination problem: if every atom has micro-experience, how do micro-experiences add up to macro-experience? CC bypasses this: there are no micro-experiences — experience is emergent (arises only under threshold conditions).

**(c)** If the threshold were $P > 0$ (not $P > 2/7$) and $R > 0$, $\Phi > 0$ — any system with non-zero parameters would be "slightly conscious." That is panpsychism. CC avoids this by setting *finite* thresholds.

</details>

---

## 6. Interdisciplinary Problems {#блок-6}

### Problem 6.1 ★★ A Physicist Reads an Organizational Audit

Using the [translation table](./interdisciplinary#translation-table), reformulate the following organizational diagnosis in the language of physics:

> "The company suffers from poor inter-departmental coordination (employees do not know what neighboring departments are doing), while each department individually operates effectively."

**(a)** Which elements of $\Gamma$ are affected (diagonal or off-diagonal)?

**(b)** How does this affect $P$ and $\Phi$?

**(c)** What physical analogy would you propose?

<details>
<summary>Solution</summary>

**(a)** Off-diagonal: $|\gamma_{ij}| \to 0$ at normal $\gamma_{kk}$. Each "department" (dimension) has sufficient resources, but the *connections* between them are absent.

**(b)** $P$ decreases (fewer coherences → less $\sum|\gamma_{ij}|^2$). $\Phi$ decreases strongly (spectral gap drops when connections are broken).

**(c)** Physical analogy: a set of non-interacting spins. Each spin has a non-zero polarization (analog of $\gamma_{kk}$), but correlations between spins are absent ($\gamma_{ij} = 0$). This is a *separable* state — the analog of "silos" in an organization.

</details>

---

### Problem 6.2 ★★★ A Biologist Models Immunity

The immune system of a cell: antigen enters → recognized (A) → response structured (S) → dynamics launched (D) → response logic verified (L) → experience integrated (E) → resources mobilized (O) → response coordinated (U).

**(a)** Describe this process as a trajectory in the space of $\sigma_k$: which stress components rise and fall?

**(b)** What happens in autoimmune disease (an error in L)?

**(c)** How does CC explain why stress ($\sigma_E \uparrow$) weakens immunity ($\kappa \downarrow$)?

---

### Problem 6.3 ★★ A Psychologist Interprets a σ-Profile

A patient came with complaints of "the feeling that life is falling apart." Psychometrics gives: σ-profile = [0.3, 0.6, 0.4, 0.3, 0.5, 0.4, 0.8].

**(a)** Which two dimensions are most stressed?

**(b)** What do they mean in psychological language?

**(c)** What therapeutic strategy does CC suggest?

**(d)** Check: is "falling apart" an appropriate expression? Which dimension does it relate to?

<details>
<summary>Solution</summary>

**(a)** $\sigma_U = 0.8$ (Unity) and $\sigma_S = 0.6$ (Structure).

**(b)** $\sigma_U = 0.8$: social isolation, loss of sense of belonging, "I am alone in the world." $\sigma_S = 0.6$: cognitive disorganization — thoughts do not form a coherent picture, planning is difficult.

**(c)** CC strategy: priority — $\sigma_U$ (the highest). Restore social connections (group therapy, supportive community). Then — $\sigma_S$ (cognitive structuring: CBT, planning, routines).

**(d)** "Falling apart" — a metaphor for the loss of U (unity) and S (structure). The patient intuitively describes their own σ-profile! The phrase precisely matches the two most stressed dimensions.

</details>

---

### Problem 6.4 ★★ An Engineer Designs an AI Agent

You are designing an AI agent with 7 modules. Current characteristics:

| Module | Function | Current $\gamma_{kk}$ |
|--------|----------|-----------------------|
| Perception (A) | Input processing | 0.18 |
| Memory (S) | State storage | 0.16 |
| Action (D) | Action generation | 0.15 |
| Reasoning (L) | Logical inference | 0.14 |
| Self-Monitor (E) | State monitoring | 0.08 |
| Resource Mgr (O) | Resource management | 0.15 |
| Integration (U) | Cross-module bus | 0.14 |

**(a)** Compute the σ-profile and find the weakest module.

**(b)** Compute $P$ (diagonal approximation).

**(c)** What needs to be strengthened to achieve $P > 2/7$?

<details>
<summary>Solution</summary>

**(a)** $\sigma = [1-7(0.18), \ldots] = [-0.26, -0.12, -0.05, 0.02, 0.44, -0.05, 0.02]$. Weakest: E (Self-Monitor), $\sigma_E = 0.44$.

**(b)** $P = 0.0324 + 0.0256 + 0.0225 + 0.0196 + 0.0064 + 0.0225 + 0.0196 = 0.1486 < 2/7$.

**(c)** Increase $\gamma_{EE}$ (strengthen Self-Monitor) and add coherences ($|\gamma_{ij}|$) — cross-module attention. Even without changing the diagonal, adding coherences $c \approx 0.06$ between all pairs gives $\Delta P = 42 \times 0.0036 = 0.15$, total $P \approx 0.30 > 2/7$.

</details>

---

### Problem 6.5 ★★★★ Open Question: Composition of Consciousnesses

Two holons $\mathbb{H}_1$ and $\mathbb{H}_2$ with $\Gamma_1, \Gamma_2 \in \mathcal{D}(\mathbb{C}^7)$ are combined. The composite matrix $\Gamma_{12} \in \mathcal{D}(\mathbb{C}^{49})$.

**(a)** Can $C(\Gamma_{12}) > C(\Gamma_1) + C(\Gamma_2)$? (Superadditivity of consciousness)

**(b)** If yes — under what conditions? What does this mean for social systems?

**(c)** This is one of the [open problems](./research-programs) of CC. Propose an attack strategy.

---

## 7. Measurement and Calibration {#блок-7}

### Problem 7.1 ★ PCI — P Calibration

Using the linear calibration $P = 0.461 \cdot \text{PCI} + 0.143$ (from [Measurement Methodology](./measurement#калибровка)):

**(a)** Compute $P$ for PCI = 0.35 (REM sleep with vivid dreams).

**(b)** At what PCI does $P$ cross the upper boundary of the Goldilocks zone ($P = 3/7$)?

**(c)** Does PCI > 0.62 occur in reality? What would it mean?

<details>
<summary>Solution</summary>

**(a)** $P = 0.461 \times 0.35 + 0.143 = 0.304 > 2/7$. Consciousness is present (dreaming!).

**(b)** $3/7 = 0.461 \cdot \text{PCI} + 0.143$. $\text{PCI} = (0.429 - 0.143)/0.461 = 0.620$.

**(c)** PCI > 0.62 — extremely rare. In the literature maximum values are ~0.55–0.60 (meditators, flow states). If PCI > 0.62 → $P > 3/7$ → the system *exits the Goldilocks zone* → risk of rigidity. This may correspond to manic states (excessive organization, but loss of flexibility).

</details>

---

### Problem 7.2 ★★ Organizational Audit: Numerical Example

A company of 100 people underwent a seven-dimensional audit. Results (normalized 0–1):

| Parameter | Value |
|-----------|-------|
| Communication clarity (A) | 0.7 |
| Process stability (S) | 0.8 |
| Adaptation speed (D) | 0.4 |
| Policy consistency (L) | 0.6 |
| Reflection culture (E) | 0.3 |
| Resource adequacy (O) | 0.7 |
| Cross-functionality (U) | 0.5 |

**(a)** Convert to a σ-profile using $\sigma_k = 1 - x_k$ (where $x_k$ is the normalized value).

**(b)** Find $\|\sigma\|_\infty$ and determine the intervention priority.

**(c)** The company plans to invest $1M in one project. CC recommends directing it toward... what?

<details>
<summary>Solution</summary>

**(a)** $\sigma = [0.3, 0.2, 0.6, 0.4, 0.7, 0.3, 0.5]$.

**(b)** $\|\sigma\|_\infty = 0.7$ (E: reflection culture — the weakest). Priority: strengthening reflection.

**(c)** CC recommends: $1M on a reflection culture development program (retrospectives, coaching, psychological safety, 360-review). This will reduce $\sigma_E$, which through the chain $\mathrm{Coh}_E \uparrow \to \kappa \uparrow \to P \uparrow$ will improve *all* indicators. Investment in E — an investment with a multiplicative effect.

</details>

---

### Problem 7.3 ★★ From EEG to σ-Profile

Using the protocol from [Measurement Methodology](./measurement#измерение-чистоты), assignment of channels to groups:

| Group | Channels | Mean power (μV²) |
|-------|----------|------------------|
| A | O1, O2, Oz | 45 |
| S | T3, T4, T5, T6 | 38 |
| D | C3, C4, Cz | 42 |
| L | F3, F4 | 35 |
| E | Fz, Pz | 22 |
| O | Fp1, Fp2 | 40 |
| U | P3, P4 | 30 |

**(a)** Normalize powers: $\gamma_{kk}^{\text{raw}} = \text{power}_k / \sum \text{powers}$.

**(b)** Compute the σ-profile.

**(c)** Interpret: which dimension has "sagged"?

<details>
<summary>Solution</summary>

**(a)** Sum = 45+38+42+35+22+40+30 = 252. $\gamma_A = 45/252 = 0.179$, $\gamma_S = 0.151$, $\gamma_D = 0.167$, $\gamma_L = 0.139$, $\gamma_E = 0.087$, $\gamma_O = 0.159$, $\gamma_U = 0.119$.

**(b)** $\sigma_A = 1 - 7(0.179) = -0.25$, $\sigma_S = 1 - 7(0.151) = -0.06$, $\sigma_D = 1 - 7(0.167) = -0.17$, $\sigma_L = 1 - 7(0.139) = 0.03$, $\sigma_E = 1 - 7(0.087) = 0.39$, $\sigma_O = 1 - 7(0.159) = -0.11$, $\sigma_U = 1 - 7(0.119) = 0.17$.

**(c)** $\sigma_E = 0.39$ — the highest. Midline structures (Fz, Pz) show reduced power. This may indicate a deficit in interoceptive processing — consistent, for example, with alexithymia or depersonalization.

</details>

---

## 8. Learning and Bounds {#блок-8}

### Problem 8.1 ★★ Information Bound

Quantum Chernoff bound (T-109): $n \geq \frac{\ln(1/(2\delta))}{\xi_{\text{QCB}}}$, where $n$ is the number of observations, $\delta$ is the error probability, $\xi_{\text{QCB}}$ is the quantum Chernoff divergence.

**(a)** For $\delta = 0.05$, $\xi_{\text{QCB}} = 0.1$: how many observations are needed?

**(b)** For $\delta = 0.01$: how many?

**(c)** Interpret: why does the required number of observations grow as the allowable error decreases?

**See:** [Learning Bounds](./learning-bounds)

<details>
<summary>Solution</summary>

**(a)** $n \geq \ln(1/0.1) / 0.1 = \ln(10)/0.1 = 2.303/0.1 = 23.03$. **24** observations needed.

**(b)** $n \geq \ln(1/0.02)/0.1 = \ln(50)/0.1 = 3.912/0.1 = 39.12$. **40** observations needed.

**(c)** The more precise the result required (smaller $\delta$), the more data is needed — this is a fundamental information limit. Even an ideal system cannot "guess" the correct answer from one observation — because observations are noisy, and one must *statistically* separate signal from noise.

</details>

---

### Problem 8.2 ★★★ Minimality N=7 for Learning

T-113 asserts: $N = 7$ is the minimum dimensionality for full learning through regeneration.

**(a)** Why can a system with $N = 5$ not learn through regeneration?

**(b)** Which of the 7 dimensions cannot be removed without losing learnability?

**(c)** Is this related to Hurwitz's theorem (octonions)?

**See:** [Learning Bounds](./learning-bounds#теорема-t-113), [Minimality](/docs/proofs/minimality/theorem-minimality-7)

---

## 9. Project Assignments {#блок-9}

### Project 9.1 ★★ Build the σ-Profile of Your Organization

**Assignment:** Using the seven-dimensional audit protocol from [Measurement Methodology](./measurement#измерение-напряжений), conduct an express audit of your organization (or study group, or family).

**Steps:**
1. For each of the 7 dimensions, ask 3 questions to employees (or group members)
2. Normalize answers to the scale [0, 1]
3. Compute the σ-profile
4. Visualize (radar chart)
5. Determine the intervention priority

**Output:** A 1-page report with a σ-diagram and recommendations.

---

### Project 9.2 ★★★ Holon Simulation in Python

**Assignment:** Implement a simple holon simulation.

```python
# Skeleton (fill in the blanks)
import numpy as np

N = 7
dt = 0.01
gamma_diss = 0.1  # dissipation rate
kappa = 0.15       # regeneration rate

# Initial state
Gamma = np.eye(N) / N + 0.05 * np.random.randn(N, N)
Gamma = (Gamma + Gamma.T.conj()) / 2  # Hermitian symmetry
Gamma /= np.trace(Gamma)               # normalization

# Target state (attractor)
rho_star = np.diag([0.20, 0.18, 0.16, 0.14, 0.12, 0.10, 0.10])

# Evolution
for step in range(10000):
    # Dissipation: Gamma -> I/N
    D = -gamma_diss * (Gamma - np.eye(N) / N)
    # Regeneration: Gamma -> rho_star
    R = kappa * (rho_star - Gamma)
    # Update
    Gamma = Gamma + dt * (D + R)
    # Compute P every 100 steps
    if step % 100 == 0:
        P = np.trace(Gamma @ Gamma)
        print(f"Step {step}: P = {P:.4f}")
```

**Questions:**
**(a)** Track $P(\tau)$. Does the system reach a stationary $P_\infty$?

**(b)** Vary $\kappa/\gamma$. At what ratio is $P_\infty = 2/7$?

**(c)** Add an external "stress": every 1000 steps, increase $\sigma_E$ by 0.1. How does this affect the dynamics?

---

### Project 9.3 ★★★★ Analysis of PCI Data

**Assignment:** Find published PCI data (e.g., Casali et al., 2013, or Casarotto et al., 2016).

**(a)** Apply the PCI → $P$ calibration from [Measurement Methodology](./measurement#калибровка).

**(b)** For each state (wakefulness, REM, deep sleep, anesthesia, vegetative state) determine: $P > 2/7$ or $P < 2/7$?

**(c)** Does the CC prediction agree with the clinical diagnosis?

**(d)** Publish the results (preprint on arXiv or bioRxiv).

---

### Project 9.4 ★★ σ-Monitoring Diary

**Assignment:** Over 7 days, keep a diary, rating 7 components of $\sigma$ on a scale of 0–10 each evening:

| Day | $\sigma_A$ | $\sigma_S$ | $\sigma_D$ | $\sigma_L$ | $\sigma_E$ | $\sigma_O$ | $\sigma_U$ |
|-----|------------|------------|------------|------------|------------|------------|------------|
| Mon | | | | | | | |
| ... | | | | | | | |
| Sun | | | | | | | |

**Questions:**
**(a)** Which dimension is consistently high (chronic stress)?
**(b)** Which fluctuates the most?
**(c)** Are there correlations ($\sigma_D$ and $\sigma_E$ rise together?)?
**(d)** What can you change to reduce $\|\sigma\|_\infty$?

---

### Project 9.5 ★★★ Compare Two Theories

**Assignment:** Choose one of the theories from [Comparison with Alternatives](./comparison) (IIT, FEP, GWT, HOT, RPT, or AST).

**(a)** Read the original paper (references are given in chapter 27).

**(b)** Compose a 1-page table "What is common / What differs / Bridge."

**(c)** Formulate *one* experiment that would distinguish that theory from CC (i.e., one outcome confirms the theory, the other confirms CC).

---

## 10. Conceptual Questions for Reflection {#блок-10}

### Question 10.1 Why not 6 and not 8?

Read the [justification for the number 7](/docs/core/foundations/axiom-omega#октонионная-структура) and the [minimality proof](/docs/proofs/minimality/theorem-minimality-7). Then answer:

**(a)** What two mathematical paths lead to the number 7?

**(b)** Is it possible to construct CC for $N = 6$? What would be lost?

**(c)** Is it possible for $N = 8$? What would be redundant?

---

### Question 10.2 Ethics of Coherence

**(a)** If $C = 0.5$ — the system is "half-conscious." Does it have moral status?

**(b)** A person under deep anesthesia: $C \approx 0$. Do they have moral status? Why yes/no?

**(c)** An AI system with $C = 1.5$. Do we have the right to restart it?

**See:** [Philosophical Foundations, ethics](./philosophy#этика)

---

### Question 10.3 Limits of the Theory

**(a)** Name three things that CC *cannot* explain.

**(b)** For each: is this a principled limitation or a temporary gap?

**(c)** If you were a reviewer of a CC paper, what *one* counterargument would you raise?

---

### Question 10.4 Free Will

**(a)** CC adopts a compatibilist position (see [Philosophical Foundations](./philosophy#метафизика)). Explain: how can a system be both *deterministic* and *free*?

**(b)** A libertarian about freedom would say: "Real freedom is the ability to have done otherwise." How would CC respond?

**(c)** A hard determinist would say: "There is no freedom, only the illusion." How would CC respond?

---

### Question 10.5 The Future of CC

**(a)** Which *one* experiment would you run first to test CC?

**(b)** What result would confirm CC? What would falsify it?

**(c)** If CC is confirmed — what practical consequences would this have for medicine? For AI?

---

## 11. Recommendations for Self-Study {#рекомендации}

### Level "Beginner" (★)

1. Read [Introduction](./introduction) and [Definitions](./definitions)
2. Solve problems 0.1–0.3, 1.1, 1.4, 3.4
3. Start a [σ-monitoring diary](#блок-9) (Project 9.4)

### Level "Novice" (★—★★)

1. Read [Introduction](./introduction), [Definitions](./definitions), and [Stability](./stability)
2. Solve problems 1.1–1.5, 3.1, 4.1, 4.3–4.4
3. Try the [minimal code](./implementation#быстрый-старт) from the Implementation section

### Level "Advanced" (★★—★★★)

1. Read [Theorems](./theorems) and [Lagrangian](./lagrangian)
2. Solve problems 2.1–2.4, 4.2, 5.3–5.4, 6.1–6.4, 7.1–7.3, 8.1–8.2
3. Implement the [holon simulation](#блок-9) (Project 9.2)

### Level "Researcher" (★★★—★★★★)

1. Study [Gap Algebra](./gap-algebra), [$G_2$ and Noether](./g2-noether-cc), [Topological Protection](./topological-protection)
2. Solve problems 6.5, 8.2 and all questions from section 10
3. Choose one of projects 9.3 or 9.5
4. Choose an [open problem](./research-programs) and begin working on it

---

:::tip Final Words
This textbook is not the final word. CC is a young theory, and much may change. The best thing you can do is not merely *study* CC, but **test** it. Find a prediction that can be verified. Collect data. Run the numbers. If CC turns out to be wrong — that is also a victory: you will have advanced science.

Good luck.
:::

---

**Further Reading:**
- [Implementation](./implementation) — code for experiments
- [Model Systems](./model-systems) — concrete examples
- [Research Programs](./research-programs) — open questions


---

**Related Documents:**
- [Introduction to CC](/docs/applied/coherence-cybernetics/introduction)
- [Definitions](/docs/applied/coherence-cybernetics/definitions)
- [Theorems](/docs/applied/coherence-cybernetics/theorems)
- [Unique Predictions of CC](/docs/applied/coherence-cybernetics/predictions)
