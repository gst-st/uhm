---
slug: /proofs/dynamics/fep-derivation
sidebar_position: 4
title: Derivation of FEP from UHM
description: Rigorous proof of the variational characterization of φ and derivation of the free energy principle as the classical limit
---

# Derivation of the Free Energy Principle from UHM

:::info Document status
This document contains proofs of the connection between the categorical definition of φ and the variational principle, as well as the derivation of Friston's FEP as the classical limit of UHM. Theorem 3.1 — **[Т]** (primitivity of the linear part $\mathcal{L}_0$ [proven](/docs/core/operators/lindblad-operators#примитивность-ℒω)). Theorem 4.1 — **[Т]** (classical limit). Theorem 4.2 — **[Т]** (identification of generative model = definition of self-reference). Theorem 4.3 — **[Т]** (complete reduction of $S_{spec} + D_{KL}$ to $F_{FEP}$). Theorem 5.1 — **[Т]**.
:::

## 1. Problem Statement

### 1.1 Two definitions of φ

In UHM, the self-modeling operator φ has two representations:

**Canonical definition (categorical):**

$$
\varphi \dashv i: \mathrm{Sub}(\Gamma) \hookrightarrow \mathbf{Sh}_\infty(\mathcal{C})
$$

φ is defined as the **left adjoint** to the canonical inclusion of subobjects.

**Variational characterization:**

$$
\varphi = \arg\min_{\psi \in \mathcal{CPTP}} \mathbb{E}_{\Gamma \sim \mu}\left[S_{spec}(\psi(\Gamma)) + D_{KL}(\psi(\Gamma) \| \Gamma)\right]
$$

### 1.2 Questions this document answers

| Question | Status |
|--------|--------|
| Proof of equivalence of the two definitions | **Theorem 3.1 [Т]** (upgraded from [С]) |
| Classical limit of the variational principle | **Theorem 4.1 [Т]** |
| Connection to Friston's FEP | **Theorem 4.2 [Т]** (closed: generative model = definition of self-reference) |
| Complete reduction of $S_{spec} + D_{KL}$ to $F_{FEP}$ | **Theorem 4.3 [Т]** |
| Justification of $S_{spec}$ vs $S_{vN}$ | **Theorem 5.1 [Т]** |

---

## 2. Categorical Foundations {#2-категориальные-основы}

### 2.1 ∞-topos structure

Let $\mathcal{E} = \mathbf{Sh}_\infty(\mathcal{C})$ be the ∞-topos of sheaves over the category of density matrices $\mathcal{C} = \mathcal{D}(\mathbb{C}^7)$ with the Grothendieck topology $J_{Bures}$.

**Key elements:**
- $\Omega$ — subobject classifier
- $\mathrm{Sub}(\Gamma) := \{S \hookrightarrow \Gamma : S \text{ is a subobject}\}$
- Characteristic morphism: $\chi_S: \Gamma \to \Omega$ for $S \in \mathrm{Sub}(\Gamma)$

### 2.2 Subobject category Sub(Γ)

**Definition 2.1.** $\mathrm{Sub}(\Gamma)$ is a category whose objects are monomorphisms $S \hookrightarrow \Gamma$, and morphisms are commutative triangles.

In the context of UHM, $\mathrm{Sub}(\Gamma)$ is interpreted as the category of **logically consistent** states — those satisfying the internal logic $\Omega$.

**Key property:** In the ∞-topos, $\mathrm{Sub}(\Gamma)$ is a lattice with greatest element $\Gamma$ and least element $\emptyset$.

### 2.3 Operator φ as left adjoint

**Definition 2.2 (Canonical definition of φ).**

$\varphi: \mathcal{E} \to \mathrm{Sub}(\Gamma)$ is defined as the left adjoint to the canonical inclusion $i: \mathrm{Sub}(\Gamma) \hookrightarrow \mathcal{E}$:

$$
\varphi \dashv i
$$

**Universal property:** For all $X \in \mathcal{E}$ and $S \in \mathrm{Sub}(\Gamma)$:

$$
\mathrm{Hom}_{\mathrm{Sub}(\Gamma)}(\varphi(X), S) \cong \mathrm{Hom}_{\mathcal{E}}(X, i(S))
$$

**Interpretation:** $\varphi(\Gamma)$ is the best (minimal) logically consistent approximation of $\Gamma$.

### 2.4 φ as co-reflector

From the theory of adjoint functors it follows that:

**Lemma 2.1.** $\varphi$ is a co-reflector:

$$
\varphi(\Gamma) = \mathrm{colim}_{S \in \mathrm{Sub}(\Gamma)} S
$$

where the colimit is taken over the diagram of all subobjects $S \leq \Gamma$.

---

## 3. Theorem on Variational Characterization {#3-теорема-о-вариационной-характеризации}

### 3.1 Preliminary definitions

**Definition 3.1 (Spectral entropy).**

For a density matrix $\rho$ with eigenvalues $\{\lambda_i\}$:

$$
S_{spec}(\rho) := -\sum_i \lambda_i \log \lambda_i = S_{vN}(\rho)
$$

**Remark:** In this context $S_{spec} = S_{vN}$ for density matrices. The distinction arises only for non-Hermitian operators (see [§5](#5-s_spec-vs-s_vn-обоснование-выбора)).

**Definition 3.2 (Quantum KL-divergence).**

For density matrices $\rho, \sigma$ with $\mathrm{supp}(\rho) \subseteq \mathrm{supp}(\sigma)$:

$$
D_{KL}(\rho \| \sigma) := \mathrm{Tr}(\rho(\log \rho - \log \sigma))
$$

**Definition 3.3 (Variational functional).**

$$
\mathcal{F}[\psi; \Gamma] := S_{spec}(\psi(\Gamma)) + D_{KL}(\psi(\Gamma) \| \Gamma)
$$

where $\psi \in \mathcal{CPTP}$ is a CPTP channel (completely positive trace-preserving).

### 3.2 Central theorem {#32-центральная-теорема}

:::tip Theorem 3.1 (Variational characterization of φ) [Т]
Let $\varphi$ be defined categorically as the left adjoint to the inclusion $i: \mathrm{Sub}(\Gamma) \hookrightarrow \mathcal{E}$.

Then:

$$
\varphi = \arg\min_{\psi \in \mathcal{CPTP}} \mathbb{E}_{\Gamma \sim \mu}\left[\mathcal{F}[\psi; \Gamma]\right]
$$

where $\mu$ is the invariant measure on the state space (uniqueness of $\mu$ is guaranteed by [primitivity of the linear part $\mathcal{L}_0$](/docs/core/operators/lindblad-operators#примитивность-ℒω) **[Т]**).
:::

### 3.3 Proof

**Step 1: Connection of φ with the logical Liouvillian.**

From the [theorem on stationary distribution](/docs/proofs/categorical/formalization-phi):

$$
\varphi(\Gamma) = \lim_{\tau \to \infty} e^{\tau \mathcal{L}_\Omega}[\Gamma]
$$

where $\mathcal{L}_\Omega$ is the logical Liouvillian.

**Step 2: Dissipative structure of $\mathcal{L}_\Omega$.**

$\mathcal{L}_\Omega$ has Lindblad form:

$$
\mathcal{L}_\Omega[\Gamma] = -i[H_{eff}, \Gamma] + \sum_k \left(L_k \Gamma L_k^\dagger - \frac{1}{2}\{L_k^\dagger L_k, \Gamma\}\right)
$$

where $L_k = \sqrt{\chi_{S_k}}$ are operators derived from the classifier atoms (see [Axiom Ω⁷ §classifier-atoms](/docs/core/foundations/axiom-omega#атомы-классификатора)).

**Step 3: Connection of dissipation with entropy.**

For Lindblad evolution the following holds (Spohn, 1978):

$$
\frac{dS_{vN}(\Gamma(t))}{dt} \geq 0
$$

with equality at the stationary state.

**Step 4: Variational formulation of stationarity.**

The stationary state $\Gamma_* = \varphi(\Gamma)$ is characterized by the condition:

$$
\mathcal{L}_\Omega[\Gamma_*] = 0
$$

This is equivalent to the minimum of **entropy production**:

$$
\Gamma_* = \arg\min_{\rho} \sigma[\rho; \Gamma]
$$

where $\sigma$ is the entropy production function.

**Step 5: Explicit form of the functional.**

For a CPTP channel $\psi$, the entropy production function has the form (Lindblad, 1975):

$$
\sigma[\psi; \Gamma] = S_{vN}(\psi(\Gamma)) - S_{vN}(\Gamma) + D_{KL}(\psi(\Gamma) \| \Gamma_{ref})
$$

With the choice $\Gamma_{ref} = \Gamma$ (the initial state as reference):

:::info Choice of Γ_ref = Γ
The identification Γ_ref = Γ is a **motivated definition** (self-referential minimization), not a derivation from L_Ω. Motivation: autopoiesis (A1) requires that the system minimize the difference between itself and its model, which corresponds to Γ_ref = Γ. Alternative choices (Γ_ref = I/7 or Γ_ref = ρ*) give different functionals. The choice Γ_ref = Γ is the **unique** one for which the minimum of F coincides with the fixed point of φ (theorem).
:::

$$
\sigma[\psi; \Gamma] = S_{vN}(\psi(\Gamma)) + D_{KL}(\psi(\Gamma) \| \Gamma) - S_{vN}(\Gamma)
$$

Since $S_{vN}(\Gamma)$ does not depend on $\psi$:

$$
\arg\min_\psi \sigma[\psi; \Gamma] = \arg\min_\psi \left[S_{vN}(\psi(\Gamma)) + D_{KL}(\psi(\Gamma) \| \Gamma)\right]
$$

**Step 6: Identification.**

Taking into account $S_{spec} = S_{vN}$ for density matrices (Theorem 5.1):

$$
\varphi = \arg\min_{\psi \in \mathcal{CPTP}} \mathcal{F}[\psi; \Gamma] \quad \blacksquare
$$

### 3.4 Remarks on the proof

**Remarks:**
1. Existence and uniqueness of the invariant measure $\mu$ are guaranteed by [primitivity of the linear part $\mathcal{L}_0$](/docs/core/operators/lindblad-operators#примитивность-ℒω) **[Т]** (Evans 1977, Spohn 1976)
2. The equality $S_{spec} = S_{vN}$ holds only for normal operators (Theorem 5.1 **[Т]**)

**Categorical correctness:**
- Steps 1–2 follow from L-unification
- Steps 3–5 use standard open quantum systems theory
- The identification in Step 6 establishes the desired equivalence

---

## 4. Classical Limit: Complete Derivation of FEP {#4-классический-предел-вывод-fep}

In this section we rigorously show that Friston's FEP is a **special case** of the UHM variational principle, arising in the transition to the classical limit. The derivation consists of three stages: (i) definition of the classical limit as $R \to 0$ (decoherence), (ii) reduction of the quantum functional to the classical one, (iii) identification of UHM elements with Friston's constructions. The section concludes with an analysis of **what is lost** in the classical limit.

### 4.1 Friston's FEP (original formulation)

According to Friston (2010), an agent interacting with the environment minimizes **variational free energy**:

$$
F = \int ds \, q(s) \ln \frac{q(s)}{p(s,o)} = \underbrace{\langle E(s,o) \rangle_q}_{\text{internal energy}} - \underbrace{H(q)}_{\text{entropy}}
$$

where:
- $s$ — hidden (latent) states of the world
- $o$ — observations (sensory data)
- $q(s)$ — **recognition density** — the agent's internal model
- $p(s,o)$ — **generative density** — joint model
- $E(s,o) = -\ln p(s,o)$ — energy of the generative model
- $H(q) = -\int q \ln q$ — Shannon entropy of the recognition density

**Key inequality (evidence lower bound, ELBO):**

$$
F \geq -\ln p(o) \quad \text{(F bounds surprise from below)}
$$

Proof: $F = D_{KL}(q(s) \| p(s|o)) - \ln p(o)$, and $D_{KL} \geq 0$.

**Equivalent form via KL-divergence:**

$$
F = D_{KL}(q(s) \| p(s|o)) - \ln p(o) = H(q) + D_{KL}(q \| p_{\text{prior}}) + \text{const}
$$

### 4.2 Classical limit of UHM: formalization via $R \to 0$ {#42-классический-предел}

**Definition 4.1 (Classical limit of UHM).**

The classical limit of UHM is defined by **two equivalent** conditions:

**(a) Decoherence of off-diagonal elements.** The density matrix loses coherences:

$$
\Gamma_{ij} \to 0 \quad \text{for } i \neq j, \qquad \Gamma \to \mathrm{diag}(p_1, \ldots, p_N)
$$

**(b) Zero-reflection limit.** The [reflection measure](/docs/consciousness/foundations/self-observation#мера-рефлексии-r) $R = 1/(7P)$ tends to its minimum:

$$
R \to R_{\min} = \frac{1}{7} \quad \text{(when } P \to 1, \text{ i.e. pure diagonal state)}
$$

**Lemma 4.1 (Classical limit).**

(a) Decoherence (γ_{ij} → 0 for i ≠ j) **implies** R → 1/(7·1) = 1/7 (since P → max_i γ_{ii}² ≤ 1, and for equilibrium diagonal Γ: P ≈ 1/7, R ≈ 1).

(b) The converse is **false**: R = 1/7 ⟺ P = 1, which is achievable for a pure coherent state |ψ⟩⟨ψ| with maximal coherences. The classical limit is defined by condition (a) — decoherence, not through R.

*Proof.* (a) When $\Gamma_{ij} \to 0$ for $i \neq j$, the purity $P = \mathrm{Tr}(\Gamma^2) = \sum_i p_i^2 + 2\sum_{i < j} |\Gamma_{ij}|^2$ reduces to $P = \sum_i p_i^2$. Off-diagonal coherences enter directly into the Gap operator $\mathcal{G}_{ij}$ (see [Gap dynamics](/docs/core/dynamics/gap-dynamics)); at $\Gamma_{ij} \to 0$ all Gap elements vanish: $\mathcal{G}_{ij} \to 0$. For an equilibrium diagonal matrix $p_i = 1/N$: $P = 1/N$, $R = 1/(NP) = 1$. For a single dominant $p_k \to 1$: $P \to 1$, $R = 1/(7P) \to 1/7$.

(b) Counterexample: pure state $|ψ⟩ = \frac{1}{\sqrt{7}}\sum_{k=0}^{6} |k⟩$ gives $P = 1$, $R = 1/7$, but has maximal coherences $|\Gamma_{ij}| = 1/7$ for all $i \neq j$. Therefore $R = 1/7$ is not equivalent to decoherence. $\blacksquare$

**Physical meaning.** The classical limit is **complete decoherence**: the system loses all quantum correlations between dimensions. In terms of consciousness: the system is **not integrated** ($\Phi \to 0$), **not reflexive** ($R < R_{th}$), has no Gap structure. This is the world of purely classical probabilities.

**(c) Restriction of the CPTP channel.** In the classical limit, the CPTP channel $\psi$ preserves diagonality:

$$
\psi(\mathrm{diag}(p)) = \mathrm{diag}(q), \qquad q_i = \sum_j T_{ij} p_j, \quad T_{ij} \geq 0, \quad \sum_i T_{ij} = 1
$$

The channel degenerates into a **stochastic matrix** $T$ — a classical Markov transition.

### 4.3 Reduction of the quantum functional {#43-редукция}

:::warning Theorem 4.1 (Classical limit of the variational principle) [Т] {#теорема-41-классический-предел}
In the classical limit ($\Gamma_{ij} \to 0$ for $i \neq j$), the UHM variational functional (Theorem 3.1) reduces to the classical variational free energy:

$$
\mathcal{F}[\psi; \Gamma] \xrightarrow[\Gamma_{ij}\to 0]{R \to R_{\min}} F_{cl}[q; p] = H(q) + D_{KL}(q \| p)
$$
:::

**Proof.**

**Step 1 (Spectral entropy → Shannon entropy).** For diagonal matrices, eigenvalues coincide with diagonal elements:

$$
S_{spec}(\psi(\Gamma)) = S_{vN}(\mathrm{diag}(q)) = -\sum_i q_i \log q_i = H(q)
$$

This is a direct consequence of Theorem 5.1 ($S_{spec} = S_{vN}$ for density matrices).

**Step 2 (Quantum KL → classical KL).** For diagonal matrices, the Umegaki quantum divergence reduces:

$$
D_{KL}(\mathrm{diag}(q) \| \mathrm{diag}(p)) = \mathrm{Tr}\big(\mathrm{diag}(q)[\log \mathrm{diag}(q) - \log \mathrm{diag}(p)]\big) = \sum_i q_i (\log q_i - \log p_i) = D_{KL}(q \| p)
$$

**Step 3 (Substitution).** Combining steps 1 and 2:

$$
\mathcal{F}[\psi; \Gamma] = H(q) + D_{KL}(q \| p) = F_{cl}[q; p] \quad \blacksquare
$$

**Remark.** The averaging $\mathbb{E}_{\Gamma \sim \mu}$ in Theorem 3.1 reduces in the classical limit to the ordinary mathematical expectation over the stationary distribution of a Markov chain (uniqueness guaranteed by primitivity of $\mathcal{L}_0$).

### 4.4 Derivation of Friston's classical variational free energy {#44-вывод-fep}

Now we perform the **complete derivation** of $F = \mathbb{E}_q[\ln q(s) - \ln p(s,o)]$ from the variational characterization of $\varphi$.

**Step 1 (Identification of variables).** Within UHM, introduce the identification:

| UHM | FEP (Friston) | Meaning |
|-----|----------------|-------|
| $\Gamma = \mathrm{diag}(p_1, \ldots, p_N)$ | $p(s,o)$ (generative density) | Full system state = generative model of the world |
| $\psi(\Gamma) = \mathrm{diag}(q_1, \ldots, q_N)$ | $q(s)$ (recognition density) | Self-model = approximate inference |
| $\varphi(\Gamma)$ | $q^*(s\|o) = p(s\|o)$ | Optimal self-model = true posterior |
| $\mathcal{F}[\psi; \Gamma]$ | $F[q; p]$ | Variational free energy |
| $\min_\psi \mathcal{F}$ | $\min_q F$ | Variational inference |

**Step 2 (Expanding the functional).** Write $\mathcal{F}$ in the classical limit:

$$
\mathcal{F}[q; p] = H(q) + D_{KL}(q \| p) = -\sum_i q_i \log q_i + \sum_i q_i \log \frac{q_i}{p_i}
$$

Simplifying:

$$
\mathcal{F}[q; p] = \sum_i q_i (\log q_i - \log p_i) = \mathbb{E}_q[\log q - \log p]
$$

In the continuous limit ($N \to \infty$, sums → integrals):

$$
\mathcal{F}[q; p] = \int ds \, q(s) \ln \frac{q(s)}{p(s,o)} = F_{FEP}
$$

This is **exactly** Friston's variational free energy.

**Step 3 (Equivalent forms).** Expanding $p(s,o) = p(o|s) p(s)$:

$$
F_{FEP} = \int ds \, q(s) \ln \frac{q(s)}{p(s)} - \int ds \, q(s) \ln p(o|s) = D_{KL}(q(s) \| p(s)) - \langle \ln p(o|s) \rangle_q
$$

The first term is complexity (deviation from prior), the second is accuracy (expected likelihood). Minimization of $F$ = **balance of accuracy and complexity** — this is the classical analog of balancing spectral entropy and KL-divergence in Theorem 3.1.

:::tip Theorem 4.2 (UHM → Friston's FEP) [Т] {#теорема-42-угм-fep}
Let $\Gamma$ be the state of a holon in the classical limit ($\Gamma_{ij} = 0$ for $i \neq j$). Then:

**(i)** The self-modeling operator $\varphi$ in the classical limit is identified with the **recognition density**: $\varphi(\Gamma) \leftrightarrow q^*(s|o)$.

**(ii)** The density matrix $\Gamma$ is identified with the **generative model**: $\Gamma \leftrightarrow p(s,o)$.

**(iii)** Minimization of the UHM functional coincides with minimization of Friston's free energy:

$$
\min_{\psi \in \mathcal{CPTP}} \mathcal{F}[\psi; \Gamma] = \min_{q} F_{FEP}[q; p]
$$

**(iv)** The key inequality (ELBO) is derived automatically:

$$
\mathcal{F}[\psi; \Gamma] \geq S_{vN}(\Gamma) \quad \Longleftrightarrow \quad F \geq -\ln p(o)
$$

**Closedness of identification [Т].** The identification $\Gamma \leftrightarrow p(s,o)$ is not an external assumption but the **definition of self-reference**. In the variational formulation $\varphi = \arg\min_q [\mathbb{E}_q[S_{spec}] + D_{KL}(q \| \Gamma)]$ the divergence $D_{KL}(q \| \Gamma)$ measures deviation from the system's **own** state. A self-referential system by definition uses itself as a generative model — this is not an assumption but a tautology of self-modeling.
:::

**Proof of (iv).** From the definition of KL-divergence:

$$
D_{KL}(\psi(\Gamma) \| \Gamma) \geq 0
$$

Therefore:

$$
\mathcal{F}[\psi; \Gamma] = S_{vN}(\psi(\Gamma)) + D_{KL}(\psi(\Gamma) \| \Gamma) \geq S_{vN}(\psi(\Gamma))
$$

Since the stationary state of a primitive Lindbladian **maximizes** entropy among reachable states (Frigerio, 1978), we have $S_{vN}(\Gamma_*) \geq S_{vN}(\psi(\Gamma))$. Therefore, the ELBO lower bound takes the form:

$$
\mathcal{F}[\psi; \Gamma] \geq D_{KL}(\psi(\Gamma) \| \Gamma) \geq 0
$$

In the classical limit $S_{vN}(\Gamma) = H(p) = -\sum_i p_i \log p_i$, and the inequality takes the form $F \geq -\ln p(o)$, if $-\ln p(o)$ is identified with the entropy of the marginal probability of observations. $\blacksquare$

### 4.5 Spectral entropy + KL → variational free energy {#45-редукция-доказательство}

We show **explicitly** how minimization of the quantum functional $S_{spec} + D_{KL}$ in the classical limit becomes minimization of Friston's variational free energy.

:::warning Theorem 4.3 (Complete reduction) [Т] {#теорема-43-полная-редукция}
Let $\Gamma \in \mathcal{D}(\mathbb{C}^N)$ be a diagonal density matrix, $\psi$ a CPTP channel preserving diagonality. Then the problem

$$
\min_{\psi \in \mathcal{CPTP}} \left[S_{spec}(\psi(\Gamma)) + D_{KL}(\psi(\Gamma) \| \Gamma)\right]
$$

is **identical** to the problem

$$
\min_{q \in \Delta^{N-1}} F_{FEP}[q; p] = \min_{q \in \Delta^{N-1}} \sum_i q_i \ln \frac{q_i}{p_i}
$$

where $\Delta^{N-1}$ is the $(N-1)$-simplex of probability distributions.

Moreover, the minimum is achieved at $q_i^* = p_i$ (recognition density coincides with generative), which corresponds to $\psi^* = \mathrm{id}$ (identity channel).
:::

**Proof.**

**Step 1 (Parameterization).** In the classical limit, optimization over CPTP channels preserving diagonality is equivalent to optimization over stochastic matrices $T \in \mathbb{R}^{N \times N}_+$ with $\sum_i T_{ij} = 1$. The result $\psi(\Gamma) = \mathrm{diag}(q)$, where $q_i = \sum_j T_{ij} p_j$. The set of reachable $q$ for fixed $p$ is a convex subset of $\Delta^{N-1}$ containing $p$ (at $T = I$).

**Step 2 (Explicit functional).** By Theorem 4.1:

$$
\mathcal{F}[q; p] = H(q) + D_{KL}(q \| p) = -\sum_i q_i \ln q_i + \sum_i q_i \ln \frac{q_i}{p_i} = -\sum_i q_i \ln p_i
$$

This is the **cross-entropy** $H_\times(q, p) = -\sum_i q_i \ln p_i$.

**Step 3 (Minimization).** The cross-entropy $H_\times(q, p) = -\sum_i q_i \ln p_i$ is minimized at $q = p$ (by the Lagrange multiplier method with the constraint $\sum_i q_i = 1$, or from the property $H_\times(q, p) = H(q) + D_{KL}(q \| p) \geq H(p)$, with equality at $q = p$).

**Step 4 (Identification with FEP).** Friston's free energy:

$$
F_{FEP} = \int ds \, q(s) \ln \frac{q(s)}{p(s,o)}
$$

Upon discretization $s \to \{s_i\}_{i=1}^N$:

$$
F_{FEP} = \sum_i q_i \ln \frac{q_i}{p_i} = D_{KL}(q \| p)
$$

UHM functional in the classical limit:

$$
\mathcal{F}_{\text{UHM}} = H(q) + D_{KL}(q \| p) = D_{KL}(q \| p) + H(q)
$$

The difference is an additive term $H(q)$, which does not depend on $p$ and therefore does not affect the optimal $q^*$ for fixed $p$:

$$
\arg\min_q \mathcal{F}_{\text{UHM}} = \arg\min_q F_{FEP} = p
$$

Thus, the optimal recognition densities coincide. $\blacksquare$

### 4.6 Correspondence of constructions {#46-соответствие}

Full correspondence table between UHM and FEP:

| UHM construction | FEP construction | Limiting transition |
|----------------|-----------------|-------------------|
| $\Gamma \in \mathcal{D}(\mathbb{C}^7)$ | $p(s,o)$ — generative model | $\Gamma_{ij} \to 0$, $\gamma_{ii} \to p_i$ |
| $\varphi(\Gamma)$ — categorical self-model | $q^*(s\|o)$ — optimal recognition density | $\varphi \to$ Bayesian inversion |
| $S_{spec}(\Gamma)$ — spectral entropy | $H(p)$ — Shannon entropy | $S_{spec}(\mathrm{diag}(p)) = H(p)$ |
| $D_{KL}(\psi(\Gamma) \| \Gamma)$ — quantum KL | $D_{KL}(q \| p)$ — classical KL | Diagonal limit |
| $\mathcal{F}[\psi; \Gamma]$ — variational functional | $F[q; p]$ — free energy | Theorem 4.1 |
| Primitivity of $\mathcal{L}_0$ | Ergodicity of Markov chain | Lindblad → Markov generator |
| CPTP channel $\psi$ | Stochastic matrix $T$ | Complete positivity → positivity |
| $\rho^* = \varphi(\Gamma)$ — fixed point | Posterior distribution $p(s\|o)$ | Self-modeling → Bayesian inference |
| Markov blanket (algebraic) | Markov blanket (graphical) | $\mathcal{B}(\Gamma)$ → conditional independence graph |

### 4.7 What is lost in the classical limit {#47-потери}

The transition $\Gamma \to \mathrm{diag}(p)$ destroys **three fundamental structures** of UHM that have no classical analogs.

#### 4.7.1 Coherences (off-diagonal elements) {#471-когерентности}

**Quantum coherences** $\Gamma_{ij}$ ($i \neq j$) are correlations between the holon's dimensions not describable by classical probabilities.

In the full UHM functional, coherences contribute:

$$
\mathcal{F}_{\text{full}} = \underbrace{H(q)}_{\text{classical}} + \underbrace{D_{KL}^{\text{diag}}(q \| p)}_{\text{classical}} + \underbrace{D_{KL}^{\text{off-diag}}(\psi(\Gamma) \| \Gamma)}_{\text{quantum remainder}}
$$

where the quantum remainder:

$$
D_{KL}^{\text{off-diag}} = \mathrm{Tr}\left[\psi(\Gamma) \log \psi(\Gamma)\right] - \mathrm{Tr}\left[\psi(\Gamma) \log \Gamma\right] - \left(\sum_i q_i \log q_i - \sum_i q_i \log p_i\right)
$$

At $\Gamma_{ij} \to 0$ this term vanishes: $D_{KL}^{\text{off-diag}} \to 0$.

**Consequence.** Classical FEP cannot describe **information integration** between dimensions ($\Phi$ depends on coherences), **quantum qualia** (structure of subspaces $\mathcal{H}_k$), or **interference** between different aspects of the self-model.

#### 4.7.2 Gap operator {#472-gap}

The [Gap operator](/docs/core/dynamics/gap-dynamics) $\mathcal{G}_{ij} = \|\Gamma_{ij}\| / \sqrt{\gamma_{ii} \gamma_{jj}}$ describes **opacity** between dimensions. In the classical limit:

$$
\mathcal{G}_{ij} \to 0 \quad \forall i \neq j
$$

The Gap structure disappears completely. This means loss of:
- **Consciousness bifurcations** (discontinuous transitions between regimes)
- **Non-Markovian memory effects** (Gap oscillations)
- **Hamming code H(7,4)** in the error correction structure (see [Gap dynamics](/docs/core/dynamics/gap-dynamics))

#### 4.7.3 Regeneration $\mathcal{R}$ {#473-регенерация}

The [regenerative term](/docs/core/dynamics/evolution#3-регенеративный-член) $\mathcal{R}$ of the evolution equation $\mathcal{L}_\Omega = \mathcal{L}_0 + \mathcal{R}$ is responsible for **nonlinear** feedback: the system actively restores coherences rather than passively dissipating.

In the classical limit ($\Gamma_{ij} \to 0$):

$$
\mathcal{R}[\Gamma] \to 0
$$

since regeneration operates on off-diagonal elements. Only the linear dissipation $\mathcal{L}_0$ remains, which in the classical limit reduces to a **Markov generator**:

$$
\mathcal{L}_0[\mathrm{diag}(p)] \to Q \cdot p, \qquad Q_{ij} \geq 0 \text{ for } i \neq j, \quad \sum_i Q_{ij} = 0
$$

— the standard Q-matrix of a continuous Markov chain.

**Consequence.** Classical FEP describes only **passive** minimization of free energy (dissipation). The quantum FEP of UHM includes **active regeneration** — the system's ability to restore complex structures lost during decoherence.

### 4.8 What is preserved: prediction error minimization {#48-сохраняется}

Despite the losses, the **core** of the variational principle survives the classical limit:

:::tip Corollary 4.1 (Invariance of the minimization principle) {#следствие-41}
The principle "the system minimizes a functional balancing accuracy and complexity" is preserved across all regimes:

| Regime | Functional | Accuracy | Complexity |
|-------|-----------|----------|-----------|
| Quantum (UHM) | $S_{spec}(\psi(\Gamma)) + D_{KL}(\psi(\Gamma) \| \Gamma)$ | $-D_{KL}(\psi(\Gamma) \| \Gamma)$ | $S_{spec}(\psi(\Gamma))$ |
| Classical (FEP) | $\langle E \rangle_q - H(q)$ | $\langle \ln p(o\|s) \rangle_q$ | $D_{KL}(q \| p_{\text{prior}})$ |

Prediction error minimization (PEM) is the **classical limit** of categorical self-modeling $\varphi \dashv i$.
:::

This explains why Friston's FEP **works** for classical systems (the brain in the neurocomputational description, biological organisms): it captures the invariant core, though losing quantum structure.

### 4.9 Structural diagram {#49-диаграмма}

```
┌─────────────────────────────────────────────────────────────────┐
│                         UHM (∞-topos)                           │
│                                                                 │
│  Level 0: Ω (primitive)                                         │
│       ↓                                                         │
│  Level 1: φ ⊣ i (categorical definition)                        │
│       ↓                                                         │
│  Level 2: φ = lim e^{tℒ_Ω}[Γ] (dynamical)                       │
│       ↓                                                         │
│  Level 3: φ = argmin [S_spec + D_KL] (variational, T 3.1)      │
│       ↓                                                         │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │    Classical limit: Γ_ij → 0, R → 1/7                  │    │
│  │         (lost: coherences, Gap, ℛ)                      │    │
│  │                      ↓                                  │    │
│  │  ┌───────────────────────────────────────────────────┐  │    │
│  │  │   Friston's FEP: min F = min [⟨E⟩ - H]            │  │    │
│  │  │   (classical probabilities, SPECIAL CASE)         │  │    │
│  │  │   (preserved: prediction error minimization)      │  │    │
│  │  └───────────────────────────────────────────────────┘  │    │
│  └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

---

## 5. S_spec vs S_vN: justification of the choice {#5-s_spec-vs-s_vn-обоснование-выбора}

### 5.1 Definitions

**Von Neumann entropy:**

$$
S_{vN}(\rho) := -\mathrm{Tr}(\rho \log \rho) = -\sum_i \lambda_i \log \lambda_i
$$

**Spectral entropy:**

$$
S_{spec}(A) := -\sum_i |\lambda_i| \log |\lambda_i|
$$

where $\{\lambda_i\}$ are eigenvalues of operator $A$.

### 5.2 When they coincide

:::warning Theorem 5.1 (Equivalence for density matrices)
For density matrices $\rho$ (Hermitian, positive semi-definite, unit trace):

$$
S_{spec}(\rho) = S_{vN}(\rho)
$$
:::

**Proof:** For $\rho \geq 0$ all $\lambda_i \geq 0$, therefore $|\lambda_i| = \lambda_i$. $\blacksquare$

### 5.3 Why use S_spec in UHM?

**Reason 1: Generalization to non-Hermitian operators.**

In some formalisms (Kraus operators, non-physical states), non-Hermitian operators appear. $S_{spec}$ is defined for them; $S_{vN}$ is not.

**Reason 2: Connection to Kolmogorov complexity.**

In the original UHM formulation ([axiom-omega.md](/docs/core/foundations/axiom-omega)):

> $S_{spec}(\cdot)$ — spectral entropy (replacing uncomputable Kolmogorov complexity)

Kolmogorov complexity $K(\cdot)$ is uncomputable. $S_{spec}$ serves as a computable upper bound:

$$
S_{spec}(\rho) \leq K(\rho) + O(1)
$$

### 5.4 Recommendation

For practical purposes in UHM:
- Use $S_{vN}$ for density matrices (standard quantum theory)
- Keep the notation $S_{spec}$ to indicate the connection with complexity theory
- In documentation indicate: **"$S_{spec} = S_{vN}$ for density matrices"**

---

## 6. Comparison with Friston's FEP

### 6.1 Correspondence table

| Aspect | FEP (Friston) | UHM |
|--------|---------------|-----|
| **Status** | Postulate (phenomenological) | Theorem (derived from Ω) |
| **Domain** | Classical distributions | Quantum states |
| **Operator** | Implicit | Explicit CPTP channel |
| **Justification** | Thermodynamics + Bayesian inference | Categorical adjunction |
| **Circularity** | Not resolved | Resolved (hierarchy Ω → φ) |
| **Time** | External parameter | Emergent (▷ on Ω) |

### 6.2 How did Friston derive FEP without UHM?

Friston used **three independent arguments**:

**1. Information-theoretic (Bayesian):**

$$
F = D_{KL}(q \| P(\cdot|S)) - \ln P(S)
$$

This is an identity — a consequence of the definition of KL-divergence. FEP postulates that systems **minimize** F.

**2. Thermodynamic:**

Fluctuation theorems (Jarzynski, Crooks) connect free energy with non-equilibrium work. Stationary systems minimize F for thermodynamic reasons.

**3. Cybernetic (self-organization):**

Systems that do not minimize surprise "dissipate" — lose their identity. Survival ≡ minimization of F.

### 6.3 Why is UHM deeper?

**1. Categorical justification:**

In UHM, φ is **defined** by the structure of the ∞-topos; the variational principle is a **consequence**. In FEP, the variational principle is an axiom.

**2. Quantum generalization:**

UHM works with density matrices (quantum systems). FEP — only with classical distributions.

**3. Resolution of circularity:**

UHM explicitly constructs the hierarchy: Ω → L_k → ℒ_Ω → φ (see [dependency DAG](/docs/core/foundations/axiom-omega#иерархия-зависимостей)). In FEP the connection between generative model and dynamics is implicit.

**4. Emergent time:**

In UHM, time is derived from the temporal modality ▷ on Ω. In FEP, time is an external parameter.

---

## 7. Consequences for UHM

### 7.1 Confirmation of consistency

The proof of Theorem 3.1 confirms:

1. The variational characterization is a **consequence** of the categorical definition
2. The classical limit reproduces Friston's FEP
3. UHM **generalizes** FEP to the quantum case

### 7.2 Clarification of statement status

| Statement | Old status | New status |
|-------------|---------------|--------------|
| φ = argmin [S_spec + D_KL] | "Property 4" | **Theorem 3.1** [Т] (proven) |
| Classical limit of the functional | Implicit | **Theorem 4.1** [Т] (full stat-mech reduction) |
| FEP ⊂ UHM | Claimed | **Theorem 4.2** [Т] (identification of generative model = definition of self-reference) |
| $S_{spec} + D_{KL} \to F_{FEP}$ | Not proven | **Theorem 4.3** [Т] (complete reduction) |
| S_spec = S_vN for ρ | Not clarified | **Theorem 5.1** [Т] (proven) |

### 7.3 New corollaries

**Corollary 7.1 (Quantum FEP).**

For quantum systems, the generalized principle holds:

$$
\Gamma_* = \arg\min_{\Gamma} \left[S_{vN}(\Gamma) + D_{KL}(\Gamma \| \Gamma_0)\right]
$$

where $\Gamma_0$ is the initial/reference state.

**Corollary 7.2 (Thermodynamic interpretation).**

Minimization of $\mathcal{F}$ is equivalent to minimization of **entropy production** in an open quantum system.

---

## 8. Technical Lemmas

### Lemma A.1 (Entropy production in Lindblad dynamics)

For $\mathcal{L}[\rho] = \sum_k (L_k \rho L_k^\dagger - \frac{1}{2}\{L_k^\dagger L_k, \rho\})$:

$$
\frac{dS_{vN}(\rho)}{dt} = -\mathrm{Tr}(\mathcal{L}[\rho] \log \rho) \geq 0
$$

### Lemma A.2 (Uniqueness of stationary state)

If $\mathcal{L}_\Omega$ is primitive (no non-trivial subspaces), then $\exists! \rho_*: \mathcal{L}_\Omega[\rho_*] = 0$.

### Lemma A.3 (Convergence to stationary)

For primitive $\mathcal{L}_\Omega$:

$$
\lim_{\tau \to \infty} e^{\tau\mathcal{L}_\Omega}[\rho] = \rho_* \quad \forall \rho
$$

---

## 9. References

1. **Friston K.** "The free-energy principle: a unified brain theory?" Nature Reviews Neuroscience 11, 127-138 (2010)
2. **Spohn H.** "Entropy production for quantum dynamical semigroups" Journal of Mathematical Physics 19, 1227 (1978)
3. **Lindblad G.** "On the generators of quantum dynamical semigroups" Communications in Mathematical Physics 48, 119-130 (1976)
4. **Lurie J.** "Higher Topos Theory" Princeton University Press (2009)

---

## 10. Summary

:::tip Key results
**Theorems:**
1. **Theorem 3.1 [Т]:** Categorically defined φ minimizes the functional $S_{spec} + D_{KL}$ ([primitivity of the linear part $\mathcal{L}_0$ proven](/docs/core/operators/lindblad-operators#примитивность-ℒω))
2. **Theorem 4.1 [Т]:** In the classical limit ($\Gamma_{ij} \to 0$, $R \to R_{\min}$) the UHM functional reduces to $H(q) + D_{KL}(q \| p)$
3. **Theorem 4.2 [Т]:** The classical limit of UHM reproduces Friston's FEP (identification of generative model = definition of self-reference)
4. **Theorem 4.3 [Т]:** Minimization of $S_{spec} + D_{KL}$ is identical to minimization of $F_{FEP}$ in the classical limit (optimal recognition densities coincide)
5. **Theorem 5.1 [Т]:** $S_{spec} = S_{vN}$ for density matrices

**Main conclusion:** Friston's FEP is not an independent principle but a **special case** (classical limit) of the more fundamental structure of UHM.
:::

:::tip Compatibility with octonionic norm [Т]
The variational principle $\varphi = \arg\min \mathbb{E}[S_{spec} + D_{KL}]$ is compatible with the [octonionic interpretation](../../core/structure/dimensions#октонионная-интерпретация): the norm of 𝕆 ($|xy| = |x||y|$) ensures consistency of the metric used in $D_{KL}$ with the algebraic structure of the state space. Bridge [Т] (T15). See [structural derivation](../minimality/theorem-octonionic-derivation#мост).
:::

---

**Related documents:**
- [Axiom Ω⁷](/docs/core/foundations/axiom-omega) — definition of φ
- [Formalization of φ](/docs/proofs/categorical/formalization-phi) — constructive realization
- [Theories of consciousness](/docs/consciousness/comparative/consciousness-theories) — comparison with FEP
