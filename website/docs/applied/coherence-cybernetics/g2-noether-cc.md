---
sidebar_position: 16
title: "Symmetries and Noether Charges in CC"
description: "Scope of G₂-symmetry in Coherence Cybernetics: exact dissipator covariance U(1)⁷ ⋊ Aut(r) (T-260), withdrawal of universal continuous G₂ Noether conservation (T-2, T-3, T-75 [✗], T-85 [✗]), invariant covariances, and pre-registered experimental protocol"
---

# Symmetries and Noether Charges: A Cybernetic Analysis

:::info Scope and Revision
This chapter analyses the exact symmetry structure of open holon dynamics in Coherence Cybernetics (CC). It distinguishes what is **strictly proved** for the Fano dissipator — the exact diagonal kernel and unitary covariance group $U(1)^7 \rtimes \mathrm{Aut}(r)$ (`T-2`, `T-3`, `T-260`) — from the **withdrawn** claim of 14 universally conserved continuous $G_2$ Noether charges (`T-75 [✗]`, `T-85 [✗]`), clarifies the true freedom of $G_2$-invariant covariances, and defines a pre-registered falsification protocol (`[Pr]`).
:::

In the [previous chapter](./goldstone-modes) we examined how symmetry breaking generates soft modes in effective models. Here we address the dual question: **which symmetries are actually respected by the coherence dynamics, which quantities are conserved, and which putative $G_2$ Noether laws fail to hold universally?**

:::tip Chapter Roadmap
In this chapter we:
1. **Recall Noether's theorem and its exact hypotheses** — why conservation requires a specified invariant action, and what changes in open GKSL systems (section 0).
2. **Distinguish $G_2$ algebra from dissipator symmetry** — why $\dim \mathfrak{g}_2 = 14$, yet the bare Fano/atomic dissipator is **not** $G_2$-covariant (`T-2`, `T-3`, section 0b–1).
3. **Establish the exact scope of the 14 model charges** — separating conditional conservative-ansatz charges from withdrawn universal Keldysh/Berry claims (`T-75 [✗]`, `T-85 [✗]`, sections 2–5).
4. **State the exact conservation structure of the bare dissipator** — the 7-dimensional diagonal kernel and the compact rephasing torus $U(1)^7 \rtimes \mathrm{Aut}(r)$ (`T-260`, section 5.3).
5. **Correct the Ward-identity parameter count** — two independent invariant covariance coefficients on $\Lambda^2 \mathbb{R}^7 = \mathbf{7} \oplus \mathbf{14}$, not one (section 6).
6. **Formulate falsifiable hypotheses and a pre-registered protocol** — without circular mapping optimization (sections 7–8).
:::

:::note On Notation
In this document:
- $G_2 = \mathrm{Aut}(\mathbb{O})$ — [group of automorphisms of the octonions](/docs/physics/gauge-symmetry/g2-structure)
- $\mathfrak{g}_2$ — Lie algebra of $G_2$ ($\dim \mathfrak{g}_2 = 14$)
- $T_a$ — generators of $\mathfrak{g}_2$ ($a = 1, \ldots, 14$)
- $\gamma_{ij} = |\gamma_{ij}|e^{i\theta_{ij}}$ — coherence between dimensions $i$ and $j$ in a fixed basis $\{A, S, D, L, E, O, U\}$
- $\mathrm{Gap}(i,j) = |\sin(\theta_{ij})|$ — [gap measure](/docs/physics/dual-aspect/gap-semantics)
- $\mathrm{PG}(2,2)$ — [Fano plane](/docs/physics/gauge-symmetry/fano-selection-rules)
- $C_{(ij),(kl)}(\tau)$ — two-point Gap correlator
:::

This document connects the mathematical results of [Charges of an invariant action](/docs/physics/gauge-symmetry/noether-charges) and [Gap Lagrangian models](./lagrangian) to Coherence Cybernetics: exact dissipator covariance, conditional benchmark models, diagnostic hypotheses, and experimental tests.

---

## 0. Emmy Noether and the Exact Conditions for Conservation {#нётер}

In 1918 Emmy Noether proved a foundational theorem of variational calculus ([Noether](https://arxiv.org/abs/physics/0503066)):

> **For a differentiable Lagrangian $L(q,\dot{q})$, if an infinitesimal continuous transformation $\delta_a q$ changes $L$ by at most a total time derivative $dB_a/dt$, then on solutions of the Euler–Lagrange equations the quantity $Q_a = \sum_i (\partial L/\partial\dot{q}_i)\delta_a q_i - B_a$ is conserved ($dQ_a/dt = 0$).** `[T]`

Classic physical instances arise when a specified microscopic action obeys the corresponding symmetry:

| Symmetry of the specified action | Conserved quantity |
|----------------------------------|--------------------|
| Time-translation invariance | Energy |
| Spatial translation invariance | Momentum |
| Spatial rotational invariance | Angular momentum |
| Global $U(1)$ phase invariance | Charge |
| Gauge $SU(3)$ symmetry (with gauge constraints) | Color current / charges |

Crucially, Noether's theorem is **conditional on having an invariant dynamical action**. It does not generate conservation laws merely because a state space carries a group action: if the Hamiltonian, potential, dissipator, instrument, or external forcing breaks the symmetry, the corresponding charge is **not conserved**.

### Noether and Open Quantum Systems

In open quantum systems governed by a GKSL master equation $\dot{\Gamma} = \mathcal{L}(\Gamma)$, continuous symmetry splits into **weak symmetry** (covariance of the generator $\mathcal{L}$) and **strong symmetry** (commutation with both the Hamiltonian and every Lindblad jump operator; see Frigerio 1978, Buča & Prosen 2012, Albert & Jiang 2014). Only strong symmetries generate conserved observables in the Heisenberg picture ($\mathcal{L}^\dagger(X) = 0$). Weak symmetries restrict transition structure and spectrum, while broken symmetries yield neither exact conservation nor universal asymptotic charge formulas.

---

## 0b. The G₂ Group vs. Actual Dissipator Symmetry {#g2-обзор}

Among simple Lie groups there are five exceptional groups: $G_2, F_4, E_6, E_7, E_8$. The smallest is the automorphism group of the octonion algebra $\mathbb{O}$:

$$
G_2 = \mathrm{Aut}(\mathbb{O}), \qquad \dim \mathfrak{g}_2 = 14.
$$

On the 7 imaginary units $e_1, \ldots, e_7$, octonion multiplication is encoded by the oriented **Fano plane** $\mathrm{PG}(2,2)$ with 7 lines of 3 points each. Inside $\mathfrak{so}(7)$ ($\dim = 21$), the subalgebra $\mathfrak{g}_2$ has codimension 7:

$$
\Lambda^2 \mathbb{R}^7 \cong \mathfrak{so}(7) = \mathbf{7} \oplus \mathbf{14},
$$

where the 14-dimensional summand is the adjoint representation $\mathfrak{g}_2$ and the 7-dimensional summand is the standard representation of $G_2$.

### Why Continuous G₂ Conservation Does Not Follow for UHM Dynamics

Earlier drafts of Coherence Cybernetics assumed that UHM's open-system dynamics derives from a universal $G_2$-invariant six-term Keldysh action, yielding 14 continuous $G_2$ Noether charges as `[T]`. Three rigorous results overturn that claim:

1. **No universal Keldysh action (`T-75 [✗]`):** The derivation of a universal six-term phase Lagrangian $L_{\mathrm{Gap}}$ from GKSL evolution is **withdrawn** (`T-75 [✗]`). A second-order phase Lagrangian $S[\theta] = \int (\frac{1}{2}\dot\theta^T M \dot\theta - V(\theta))\,dt$ is a **chosen model ansatz**, whereas matrix ODE evolution $\dot{\Gamma} = F(\Gamma)$ directly yields only the first-order phase identity $\dot{\theta}_{ij} = \mathrm{Im}(F_{ij}/\gamma_{ij})$ for $\gamma_{ij}\neq 0$ (see [Gap Lagrangian models](./lagrangian)).
2. **No universal Berry/topological term (`T-85 [✗]`):** The derivation of a universal topological term $\mathcal{L}_{\mathrm{top}}$ from Hermitian Keldysh traces is **withdrawn** (`T-85 [✗]`). The trace of a product of Hermitian matrices is real; a Berry term requires a separately specified eigenbundle and microscopic derivation.
3. **The bare dissipator breaks continuous $G_2$ (`T-2 [T]`, `T-3 [T]`, `T-260 [T]`):** In the chosen coordinate frame, uniform Fano dephasing equals $\frac{2}{3}$ of atomic coordinate dephasing (`T-2 [T]`), and the atomic/Fano dissipator is **not** $G_2$-covariant (`T-3 [T]`). Instead, its exact unitary covariance group is the diagonal-preserving group $U(1)^7 \rtimes \mathrm{Aut}(r)$ (`T-260 [T]`), whose intersection with $G_2$ is the **finite** monomial frame group $\Gamma_{\mathrm{oct}}$ (order $1344$), **not** continuous $G_2$.

Consequently, the 14 continuous $G_2$ charges are **withdrawn as universal laws of UHM open-system dynamics**. They survive solely as a **conditional reference construction** for a specifically postulated $G_2$-invariant conservative phase action (`[C]`), useful as an idealized symmetry benchmark against which actual symmetry breaking is measured.

---

## 1. Withdrawn Universal 14-Charge Claim and Conditional Benchmark Scope {#обзор}

:::warning Retraction and Corrected Scope (`T-2`, `T-3`, `T-260`, `T-75 [✗]`, `T-85 [✗]`)
- **Withdrawn (`[✗]`):** The claim that UHM's GKSL dynamics universally generates 14 continuous $G_2$ Noether charges with a topological triplet term and universal stationary values $Q_a^{(\mathrm{stat})} = (\kappa/\Gamma_2)\,Q_a^{(\mathrm{reg})}$.
- **What holds strictly (`[T]`):**
  1. For the bare coordinate/Fano dissipator, the exact kernel is the 7-dimensional diagonal algebra and the exact unitary covariance group is $U(1)^7 \rtimes \mathrm{Aut}(r)$ (`T-260 [T]`), not continuous $G_2$ (`T-2 [T]`, `T-3 [T]`).
  2. For any **separately postulated** smooth conservative action $S[q] = \int L(q,\dot{q})\,dt$ that is invariant under a continuous $G_2$ action, Noether's theorem yields 14 conserved charges along its Euler–Lagrange trajectories (`[C under postulated G₂-invariant action]`).
:::

In such a postulated $G_2$-invariant conservative benchmark model, one may choose a basis of $\mathfrak{g}_2$ adapted to the Fano plane (for example, splitting a chosen 14-element basis into 7 triplet-adapted generators and 7 complementary generators):

| Benchmark class | Count | Notation | Scope |
|-----------------|-------|----------|-------|
| Fano-adapted basis charges | 7 | $Q_p^{(F)}$, $p = 1, \ldots, 7$ | Postulated $G_2$-invariant conservative ansatz `[C]` |
| Complementary basis charges | 7 | $Q_q^{(D)}$, $q = 1, \ldots, 7$ | Postulated $G_2$-invariant conservative ansatz `[C]` |
| **Exact bare-dissipator conserved observables** | **7** | **$\gamma_{kk}$, $k \in \{A,S,D,L,E,O,U\}$** | **Bare Fano/atomic dissipator at $H=0$, $\kappa=0$ (`T-260 [T]`)** |

Note that the $7 + 7 = 14$ split of $\mathfrak{g}_2$ is a choice of basis adapted to a fixed Fano frame, not a canonical $G_2$-invariant decomposition ($\mathfrak{g}_2$ is simple and irreducible under the adjoint action of $G_2$).

---

## 2. Model Triplet Momenta $Q_p^{(F)}$ (Conditional Ansatz) `[C/I]` {#фано-заряды}

:::caution Conditional Ansatz vs. Withdrawn Topological Term (`T-75 [✗]`, `T-85 [✗]`)
For a **chosen** quadratic phase-kinetic ansatz $L_{\mathrm{kin}} = \frac{1}{2}\sum_{i<j} m_{ij}\dot\theta_{ij}^2$ with constant weights $m_{ij} = |\gamma_{ij}|^2$ on a fixed-amplitude chart ($|\gamma_{ij}| > 0$) and a Fano-line generator $\delta_p$, the kinetic Noether momentum takes the form

$$
Q_p^{(F,\mathrm{kin})} = \sum_{(i,j) \in \mathrm{line}_p} |\gamma_{ij}|^2 \dot{\theta}_{ij}
$$

**Correction (`T-85 [✗]`):** The former second term $+\frac{1}{6\pi}\sum_{(i,j,k)\in\mathrm{line}_p} \theta_{ij}\theta_{jk}$ is **withdrawn**: it was derived from a retracted Keldysh-to-Berry term (`T-85 [✗]`), is not invariant under $2\pi$-shifts of individual phase coordinates $\theta_{ij} \mapsto \theta_{ij} + 2\pi$, and does not represent a Chern number of a finite $7 \times 7$ matrix. Moreover, constant-amplitude phase charts do not form a $G_2$-invariant submanifold of $\mathcal{D}(\mathbb{C}^7)$ (see [Gap Lagrangian models §1](./lagrangian)).
:::

### 2.1 Anatomy of the Kinetic Triplet Statistic

In the fixed-frame phase chart where $|\gamma_{ij}| > 0$:

- **Weighted phase-velocity sum** $\sum_{(i,j)\in\mathrm{line}_p} |\gamma_{ij}|^2 \dot{\theta}_{ij}$ is a **defined kinematic summary statistic** `[D]` of phase circulation along the three pairs of Fano line $p$.
- Because matrix evolution $\dot\Gamma = F(\Gamma)$ is first-order, $\dot\theta_{ij} = \mathrm{Im}(F_{ij}/\gamma_{ij})$ is fixed instantaneously by the state $\Gamma$, not an independent canonical velocity (`T-75 [✗]`). Therefore $Q_p^{(F,\mathrm{kin})}$ is **not** automatically conserved by GKSL evolution.

### 2.2 Hydrodynamic Analogy `[I]`

The circulation analogy is strictly heuristic `[I]` and holds only inside a specifically postulated conservative phase model:

| Hydrodynamics | Conservative phase ansatz (`[C]`) | Full open GKSL holon |
|---------------|-----------------------------------|----------------------|
| Vortex tube | Fano line $p = \{i,j,k\}$ | Coordinate triplet in fixed basis |
| Velocity circulation | $Q_p^{(F,\mathrm{kin})}$ | Non-conserved summary statistic |
| Kelvin's theorem | Requires postulated symmetric action | **Does not hold** (`T-2`, `T-3`, `T-75 [✗]`) |

### 2.3 Canonical Seven Fano Triplets and Seven Axes

Using the canonical Singer cyclic Fano plane on the 7 axes $\{A, S, D, L, E, O, U\}$:

| Line $p$ | Canonical triplet | Axes | Heuristic functional domain `[I]` |
|----------|-------------------|------|-----------------------------------|
| 1 | $\{A, S, L\}$ | Articulation–Structure–Logic | Perception–structuring–verification |
| 2 | $\{S, D, E\}$ | Structure–Dynamics–Interiority | Organization–process–interiority |
| 3 | $\{D, L, U\}$ | Dynamics–Logic–Unity | Process–logic–integration |
| 4 | $\{L, E, O\}$ | Logic–Interiority–Ground | Reasoning–interiority–grounding |
| 5 | $\{E, U, A\}$ | Interiority–Unity–Articulation | Interiority–unity–expression |
| 6 | $\{U, O, S\}$ | Unity–Ground–Structure | Integration–resources–structure |
| 7 | $\{O, A, D\}$ | Ground–Articulation–Dynamics | Resources–perception–action |

### 2.4 Heuristic Cognitive Reading of Triplet Imbalances `[I]` {#интерпретация-зарядов}

Reading the seven Fano triplets in cognitive terms is an **interpretive mapping** `[I]`, not a derived clinical diagnostic law:

- **$\{A, S, L\}$** (*perceptual verification*): links Articulation ($A$), Structure ($S$), and Logic ($L$).
- **$\{S, D, E\}$** (*organizational process*): links Structure ($S$), Dynamics ($D$), and Interiority ($E$).
- **$\{D, L, U\}$** (*goal-directed reasoning*): links Dynamics ($D$), Logic ($L$), and Unity ($U$).
- **$\{L, E, O\}$** (*grounded reflection*): links Logic ($L$), Interiority ($E$), and Ground ($O$).
- **$\{E, U, A\}$** (*expressive integration*): links Interiority ($E$), Unity ($U$), and Articulation ($A$).
- **$\{U, O, S\}$** (*resource organization*): links Unity ($U$), Ground ($O$), and Structure ($S$).
- **$\{O, A, D\}$** (*sensorimotor cycle*): links Ground ($O$), Articulation ($A$), and Dynamics ($D$).

### 2.5 Illustrative Scenario: Trade-Offs Within $\{A, S, L\}$ `[I]` {#сценарий-q1}

Consider a learner acquiring a new language, modelled via pairwise coherences within the triplet $\{A, S, L\}$:
- Initially $|\gamma_{AS}|$ is large (speech sounds are parsed into surface structures), while $|\gamma_{SL}|$ and $|\gamma_{AL}|$ are small (grammatical rules and verification are weak).
- Under a **postulated** conservative triplet constraint $Q_1^{(F,\mathrm{kin})} = \mathrm{const}$ (`[C]`), any increase in $|\gamma_{SL}|^2\dot\theta_{SL}$ would have to be offset by decreases in $|\gamma_{AS}|^2\dot\theta_{AS}$ or $|\gamma_{AL}|^2\dot\theta_{AL}$.
- In actual open-system dynamics, however, no such exact budget conservation is enforced by UHM axioms (`T-3`, `T-75 [✗]`): whether attentional trade-offs occur in a specific cognitive task is an empirical hypothesis `[H]` depending on the Hamiltonian, dissipation, and external training drive, not an exact Noether identity.

---

## 3. Complementary Inter-Triplet Momenta $Q_q^{(D)}$ (Conditional Ansatz) `[C/I]` {#дополнительные-заряды}

:::caution Conditional Model Definition `[D/C]`
Given a postulated $G_2$-invariant conservative phase Lagrangian and a basis $\{T_1,\ldots,T_{14}\}$ of $\mathfrak{g}_2$ split into 7 triplet-adapted generators and 7 complementary generators $D_q$, the complementary kinetic momenta are defined by

$$
Q_q^{(D)} = \sum_{(m,n):\, [D_q]_{mn} \neq 0} c_{q,mn}\, |\gamma_{mn}|^2 \dot{\theta}_{mn},
$$

where the weights $c_{q,mn}$ encode the exact matrix elements of $D_q$ on the phase coordinates. Without a $G_2$-invariant action and matching representation intertwiner, $Q_q^{(D)}$ is **not** conserved along GKSL trajectories.
:::

### 3.1 Basis Dependence vs. Structural Claims

Because $\mathfrak{g}_2$ is a **simple** Lie algebra, it admits no invariant ideal splitting into $7 + 7$. The distinction between "within-triplet" and "cross-triplet" generators is tied to a chosen coordinate basis and its Fano incidence structure, and vanishes under generic $G_2$ rotations. With the topological term withdrawn (`T-85 [✗]`), neither class carries a derived topological protection from finite-matrix traces.

### 3.2 Inter-Triplet Connectivity `[I]`

Heuristically `[I]`, coherences bridging different Fano lines reflect cross-domain coordination. Loss of cross-triplet coherence can serve as a descriptive indicator of modular decoupling, provided the axis-to-observable mapping is independently validated (`[H]`).

### 3.3 Dimension Count of $\mathfrak{g}_2$

The identity

$$
\dim \mathfrak{g}_2 = 14 < 21 = \dim \mathfrak{so}(7)
$$

is an exact algebraic fact `[T]`. What does **not** follow from $\dim \mathfrak{g}_2 = 14$ is that UHM's dissipative coherence evolution obeys 14 conservation laws.

---

## 4. Degree-of-Freedom Count and Why 14 Laws Do Not Freeze GKSL Dynamics {#14-законов}

The earlier claim that "14 conservation laws freeze 21 coherences down to $21 - 14 = 7$ free degrees of freedom" fails on two independent grounds:

1. **State-space geometry:** A density matrix $\Gamma \in \mathcal{D}(\mathbb{C}^7)$ has $7^2 - 1 = 48$ real parameters — $6$ independent diagonal populations plus $21$ complex ($42$ real) off-diagonal coherences — subject to positivity $\Gamma \succeq 0$. A generic $G_2$ rotation mixes diagonal and off-diagonal entries and does not leave a fixed-amplitude phase torus invariant ([Gap Lagrangian models §1](./lagrangian)).
2. **Symmetry breaking by the generator (`T-2`, `T-3`, `T-260`):** Even if one restricts attention to the GKSL generator $\dot\Gamma = -i[H,\Gamma] + \mathcal{D}_{\mathrm{Fano}}(\Gamma) + \mathcal{R}(\Gamma)$, the Fano dissipator breaks continuous $G_2$ (`T-3 [T]`), and no universal conservative $G_2$-invariant action is derived (`T-75 [✗]`).

Therefore, UHM does **not** have 14 universal conservation laws of consciousness. The only universal conservation law of every CPTP/trace-preserving evolution is **trace conservation** $\mathrm{Tr}\,\Gamma = 1$ (`[T]`). Additional conserved quantities exist only for restricted generators — most importantly the bare dissipator discussed in §5.3 (`T-260 [T]`).

---

## 5. Non-Conservation Under Dissipation and the Exact Diagonal Kernel {#диссипация}

In a **postulated** damped-driven phase ansatz $M\ddot\theta + \nabla V + B\dot\theta = u$ ([Variational derivation](./variational)), any candidate symmetry charge $Q_a$ of the conservative part obeys a balance equation determined explicitly by the chosen damping matrix $B$ and forcing $u$:

$$
\frac{dQ_a}{dt} = (\delta_a \theta)^T (-B\dot\theta + u).
$$

This balance is **model-dependent** `[C]`. The former universal formula $dQ_a/d\tau = -\Gamma_2 Q_a^{(\mathrm{kin})} + \kappa Q_a^{(\mathrm{reg})}$ and stationary ratio $Q_a^{(\mathrm{stat})} = (\kappa/\Gamma_2) Q_a^{(\mathrm{reg})}$ are **withdrawn as theorems** of the GKSL equation: the matrix dissipator is not $G_2$-covariant (`T-3 [T]`), regeneration $\mathcal{R}(\Gamma)$ is generally nonlinear and state-dependent, and the phase velocity $\dot\theta_{ij}$ is not an independent canonical momentum (`T-75 [✗]`).

### 5.1 Competition of Rates (Qualitative Regime Classification `[I]`)

In the reduced models of the [phase diagram](./phase-diagram-cc), the dimensionless rate ratio $r = \kappa/\Gamma_2$ controls the balance between regenerative drive and dephasing:

| Regime | Rate ratio $r = \kappa/\Gamma_2$ | Qualitative coherence behavior `[I]` |
|--------|----------------------------------|--------------------------------------|
| Strong regeneration | $r \gg 1$ | Coherences maintained near target structure (model-dependent) |
| Balanced | $r \sim 1$ | Competition between off-diagonal decay and regenerative injection |
| Weak regeneration | $r < 1$ | Off-diagonal coherences suppressed toward diagonal steady states |
| Sub-threshold | Below model threshold | Purity falls below the chosen $P_{\mathrm{crit}} = 2/7$ cut |

### 5.2 Timescales of Off-Diagonal Decay

Under uniform Fano dephasing with rate $\gamma$, every off-diagonal element decays exponentially as $\gamma_{ij}(t) = \gamma_{ij}(0)\,e^{-(2\gamma/3)t}$ (`T-2 [T]`), giving a characteristic coherence relaxation time $\tau_{\mathrm{coh}} = 3/(2\gamma)$. For general line-resolved Fano rates $\gamma_p \ge 0$, pair $(i,j)$ decays at rate $r_{ij} = \frac{1}{6}\sum_{|\ell_p \cap \{i,j\}|=1} \gamma_p$ (see [Effective temperature §8](./effective-temperature#линейные-температуры)).

### 5.3 Exact Conservation of the Bare Dissipator: The Gauge Torus $U(1)^7 \rtimes \mathrm{Aut}(r)$ (`T-260 [T]`) {#тор-зарядов}

While continuous $G_2$ is **broken** by the Fano dissipator (`T-2 [T]`, `T-3 [T]`), the bare dissipator $\mathcal{D}_{\mathrm{Fano}}$ (at $H = 0$, $\kappa = 0$) does possess an **exact** symmetry and conservation structure (`T-260 [T]`):

:::tip Theorem (`T-260`) — Exact Kernel and Covariance of the Bare Dissipator `[T]`
1. **Exact 7-dimensional diagonal kernel:** For every choice of nonnegative line rates $\gamma_p \ge 0$ (with at least one line incident to each pair), the kernel of the bare Fano dissipator is the 7-dimensional commutative algebra of diagonal matrices:
   $$
   \ker(\mathcal{D}_{\mathrm{Fano}}) = \mathrm{span}\{\Pi_k = |k\rangle\langle k| : k \in \{A,S,D,L,E,O,U\}\}.
   $$
   Every diagonal population $\gamma_{kk} = \mathrm{Tr}(\Pi_k \Gamma)$ is exactly invariant under $\mathcal{D}_{\mathrm{Fano}}$ alone: $\mathcal{D}_{\mathrm{Fano}}^\dagger(\Pi_k) = 0$.
2. **Compact gauge torus $U(1)^7$ from projector periodicity:** Each coordinate projector $\Pi_k$ is idempotent with spectrum $\{0, 1\}$. Consequently, the one-parameter unitary group $U_k(\alpha_k) = e^{i\alpha_k \Pi_k}$ is $2\pi$-periodic in $\alpha_k$, and the seven commuting projectors generate the compact **7-torus of diagonal rephasings** $U(1)^7$.
3. **Full unitary covariance group:** The full unitary covariance group of $\mathcal{D}_{\mathrm{Fano}}$ is the semidirect product
   $$
   G_{\mathrm{cov}}(\mathcal{D}_{\mathrm{Fano}}) = U(1)^7 \rtimes \mathrm{Aut}(r),
   $$
   where $\mathrm{Aut}(r) \subseteq S_7$ is the permutation group preserving the pairwise decay-rate table $r_{ij}$. For equal line rates ($\gamma_p = \gamma$), $\mathrm{Aut}(r) = S_7$, so $G_{\mathrm{cov}} = U(1)^7 \rtimes S_7$. Its intersection with $G_2$ is the **finite** octonionic frame group $\Gamma_{\mathrm{oct}}$ (signed permutations, order $1344$, acting on $\mathrm{PG}(2,2)$ through $\mathrm{Aut}(\mathrm{PG}(2,2)) \cong \mathrm{PSL}(2,7)$) — **not** continuous $G_2$.
4. **Effect of a connected Hamiltonian $H$:** Turning on a connected Hamiltonian $H$ (with nonvanishing couplings linking all 7 axes) breaks the conservation of individual diagonal projectors $\Pi_k$ and **removes all non-scalar diagonal conserved charges**, leaving only the scalar identity $I$ (trace conservation $\mathrm{Tr}\,\Gamma = 1$).
:::

:::warning Correction on Compactness vs. Integrality (`T-260`)
The compactness of $U(1)^7$ follows strictly from the $\{0,1\}$ eigenvalue spectrum of the chosen coordinate projectors $\Pi_k$ generating diagonal phase rotations $e^{i\alpha_k \Pi_k}$. It does **not** mean that diagonal populations $\gamma_{kk}$ are integer-quantized: $\gamma_{kk} \in [0, 1]$ are continuous real probabilities satisfying $\sum_k \gamma_{kk} = 1$, and compactness of a symmetry group is **not** equivalent to arbitrary charge-generator integrality. Earlier text asserting discrete integer population steps $\Delta N \in \mathbb{Z}$ was erroneous and has been removed.
:::

---

## 6. Ward Identities and $G_2$-Invariant Covariances (Corrected Scope) {#уорд}

In quantum field theory and statistical physics, Ward identities constrain correlation functions **if and only if** the state, measure, and dynamics are invariant under the symmetry group in question. Applying this to $G_2$ on 21-dimensional pair space requires two critical corrections relative to earlier drafts (see [Charges of an invariant action](/docs/physics/gauge-symmetry/noether-charges#тождества-уорда-разложение)).

### 6.1 What $G_2$-Invariance Actually Implies on $\Lambda^2 \mathbb{R}^7$ `[T]`

:::tip Theorem 6.1 ($G_2$-Invariant Symmetric Covariances on $\Lambda^2 \mathbb{R}^7$) `[T]`
Under the fundamental 7-dimensional representation of $G_2$, the 21-dimensional antisymmetric tensor space decomposes into two **inequivalent** irreducible representations:

$$
\Lambda^2 \mathbb{R}^7 = \mathbf{7} \oplus \mathbf{14}.
$$

By Schur's lemma, every symmetric $G_2$-invariant covariance operator $C$ on $\Lambda^2 \mathbb{R}^7$ has **two** independent real parameters, not one:

$$
C = a\,\mathsf{P}_7 + b\,\mathsf{P}_{14}, \qquad a, b \ge 0,
$$

where $\mathsf{P}_7$ and $\mathsf{P}_{14}$ are the orthogonal projectors onto the $\mathbf{7}$ and $\mathbf{14}$ summands. A single trace measurement fixes only $7a + 14b$; determining both $a$ and $b$ requires a **second** independent measurement.
:::

The infinitesimal invariance equations for a $G_2$-invariant tensor $C$ take the form

$$
\sum_{m} \left([T_a]_{im} C_{(mj),(kl)} + [T_a]_{jm} C_{(im),(kl)} + [T_a]_{km} C_{(ij),(ml)} + [T_a]_{lm} C_{(ij),(km)}\right) = 0
$$

for all $T_a \in \mathfrak{g}_2$ ($a = 1, \ldots, 14$), acting on **all four** indices (both legs of the two-point correlator — transforming only one leg would overconstrain $C$).

### 6.2 Meaning of the Correction

Earlier text asserted that Ward identities reduce the 231 entries of a symmetric $21 \times 21$ matrix first to $231 - 14 = 217$ and then via $G_2$-invariance to **one** parameter $\alpha$. Both steps require correction:
- The number of independent $G_2$-invariant symmetric bilinear forms on $\Lambda^2 \mathbb{R}^7 = \mathbf{7} \oplus \mathbf{14}$ is **2** (parameters $a, b$), not 1.
- Moreover, the unsigned Gap observables $\mathrm{Gap}(i,j) = |\sin(\theta_{ij})| \in [0, 1]$ live on the 21 **unordered** coordinate edges, not directly on the antisymmetric tensor representation $\Lambda^2 \mathbb{R}^7$: matching dimensions $(7, 14)$ does **not** supply a canonical $G_2$-intertwiner between unsigned edge coordinates and $\Lambda^2 \mathbb{R}^7$ ([Charges of an invariant action](/docs/physics/gauge-symmetry/noether-charges#оператор-f21-определение)).

### 6.3 The Fano Adjacency Matrix $F$ on 21 Edges `[T]` {#разложение-по-g_2-инвариантным-тензорам}

On the 21 unordered edges of $\mathrm{PG}(2,2)$, define the symmetric adjacency matrix $\mathbf{F}_{21}$ joining distinct edges that lie on the same Fano line. Because every pair of distinct axes determines a unique Fano line of 3 edges, $\mathbf{F}_{21}$ is block-diagonal with seven $3 \times 3$ blocks $J_3 - I_3$:

- Eigenvalue $+2$ with multiplicity $7$ (constant vector on each Fano line, projector $\Pi_7$),
- Eigenvalue $-1$ with multiplicity $14$ (zero-sum vectors on each Fano line, projector $\Pi_{14}$).

Since $\mathbf{F}_{21}$ satisfies the minimal polynomial $(\mathbf{F}_{21} - 2I)(\mathbf{F}_{21} + I) = 0$, we have $\mathbf{F}_{21}^2 = \mathbf{F}_{21} + 2I$, so every polynomial in $\mathbf{F}_{21}$ spans at most the **2-dimensional** algebra $\mathrm{span}\{\Pi_7, \Pi_{14}\}$ (`[T]`):

$$
C = a'\,\Pi_7 + b'\,\Pi_{14}.
$$

The specific former polynomial $C = \alpha(I - \frac{3}{7}\mathbf{F}_{21} + \frac{3}{49}\mathbf{F}_{21}^2)$ simply selects one particular ray $a' = \frac{19}{49}\alpha$, $b' = \frac{73}{49}\alpha$ by **choice of polynomial**, not by Ward identities!

:::info Actual Dissipator Breaking of $G_2$ (`T-2`, `T-3`)
Even in the theoretical model, the coordinate/Fano dissipator is **not** $G_2$-covariant (`T-3 [T]`). Across every Fano weight $\alpha^* \in [0, 1]$, the $G_2$-covariance violation satisfies $\Delta_{G_2} = \frac{2+\alpha^*}{3}\,\Delta_{\max} \ge \frac{2}{3}\Delta_{\max}$ ([Fano channel](/docs/proofs/gap/fano-channel#g2-ковариантность)). Therefore, an experimental observation of exact $G_2$-invariance ($\Delta_{G_2} \approx 0$) would **contradict** the coordinate Fano-pinching dissipator rather than confirm it! What the Fano dissipator predicts is the **rank-7 line-rate structure** ($r_{ij} = \frac{1}{6}\sum_{|\ell_p \cap \{i,j\}|=1}\gamma_p$) and $U(1)^7 \rtimes \mathrm{Aut}(r)$ covariance (`T-260 [T]`).
:::

### 6.4 Summary of Parameter Counts `[T]`

| Model class for a $21 \times 21$ symmetric covariance | Independent parameters | Exact algebraic basis |
|-------------------------------------------------------|------------------------|-----------------------|
| Unrestricted symmetric $21 \times 21$ matrix | 231 | Arbitrary symmetric matrix |
| $G_2$-invariant bilinear form on $\Lambda^2 \mathbb{R}^7$ | 2 | $a\,\mathsf{P}_7 + b\,\mathsf{P}_{14}$ (`[T]`) |
| Block-Fano-symmetric edge covariance ($\Gamma_{\mathrm{oct}}$-adapted) | 2 | $a'\,\Pi_7 + b'\,\Pi_{14}$ (`[T]`) |
| Former single-parameter polynomial ansatz | 1 | Fixed ratio $a'/b' = 19/73$ (special ansatz `[D]`, not forced by $G_2$) |

---

## 7. Exploratory Diagnostic Hypotheses `[H/I]` {#диагностика}

Because continuous $G_2$ Noether conservation does not hold for open holon dynamics (`T-3`, `T-75 [✗]`), charge deviations **cannot** be treated as validated clinical diagnostics. The tables below record **exploratory interpretive hypotheses** `[H/I]` that require independent psychometric, physiological, and longitudinal validation before any clinical use.

### 7.1 Candidate Symmetry-Breaking Observables `[H/I]`

| Observable | Operational definition | Exploratory hypothesis `[H/I]` |
|------------|------------------------|--------------------------------|
| Fano-line rate residuals | Deviation of estimated decay rates $r_{ij}$ from rank-7 Fano incidence span | Tests the calibrated Fano-jump dissipator ([Effective temperature §8](./effective-temperature#линейные-температуры)) |
| Block-covariance ratio $a'/b'$ | Projection of empirical $21 \times 21$ covariance onto $\Pi_7$ vs. $\Pi_{14}$ | Measures within-triplet vs. cross-triplet correlation anisotropy |
| Diagonal population drift $\dot\gamma_{kk}$ | Rate of change of inferred axis weights | Reflects Hamiltonian coupling + regenerative/external forcing (`T-260`) |
| $G_2$-breaking residual $\Delta_{G_2}^{(\mathrm{exp})}$ | Norm of commutator residual on antisymmetrized pair observables | Benchmark distance from idealized $G_2$-isotropy |

### 7.2 Exploratory Triplet-Profile Hypotheses `[I]` {#диагностика-по-зарядам}

The seven canonical Fano triplets suggest domain-grouped hypotheses `[I]` (none of which is an established medical criterion):

| Canonical triplet | Axes | Exploratory functional focus `[I]` |
|-------------------|------|------------------------------------|
| $\{A, S, L\}$ | Articulation, Structure, Logic | Perceptual parsing, structural organization, logical checking |
| $\{S, D, E\}$ | Structure, Dynamics, Interiority | Coupling of structured action with felt experience |
| $\{D, L, U\}$ | Dynamics, Logic, Unity | Coherence of goal-directed action and reasoning |
| $\{L, E, O\}$ | Logic, Interiority, Ground | Alignment between reasoning, affect, and physiological grounding |
| $\{E, U, A\}$ | Interiority, Unity, Articulation | Integration and verbal/behavioral expression of experience |
| $\{U, O, S\}$ | Unity, Ground, Structure | Resource availability supporting structural integration |
| $\{O, A, D\}$ | Ground, Articulation, Dynamics | Sensorimotor regulation and physiological readiness |
| Cross-triplet edges | Between distinct Fano lines | Global coordination across functional subsystems |

### 7.3 Intervention Hypotheses `[H/I]`

Distinguishing within-triplet imbalance from cross-triplet decoupling is an **untested intervention hypothesis** `[H/I]`. Any therapeutic protocol must be grounded in independently validated clinical trials and medical standards, not inferred from matrix algebra alone.

### 7.4 Principle of Targeted Measurement `[I]`

Rather than assuming a universal conservation law, an applied measurement framework should estimate all four capability margins ($P$, $R$, $\Phi$, $D_{\mathrm{diff}}$) together with axis-level uncertainty sets (see [Measurement of Consciousness](./measurement)) before forming targeted hypotheses.

---

## 8. Pre-Registered Experimental Protocol for Symmetry Testing `[Pr]` {#протокол}

::::caution Research Programme: Pre-Registered Symmetry-Testing Protocol `[Pr]`

:::warning Eliminating Circularity and Multiple-Testing Bias
Mapping neural or behavioral channels to the 7 axes $\{A,S,D,L,E,O,U\}$ is itself part of the empirical hypothesis. **Optimizing or enumerating channel-to-axis mappings to minimize the test statistic $\Delta_{G_2}^{(\mathrm{exp})}$ on the same dataset is statistically invalid (p-hacking / circular overfitting)** and MUST NOT be used.

To prevent circularity, any valid test MUST enforce:
1. **Independent pre-registration of the mapping:** Fix the channel-to-axis encoder *a priori* from anatomical, task-factorial, or functional criteria and deposit the mapping, preprocessing pipeline, and statistical test plan in a public pre-registration before data inspection.
2. **Strict train/test separation (if learned):** If an encoder is learned from data, fit it strictly on an independent calibration split (or independent subjects/sessions) using task labels unrelated to the symmetry statistic, freeze the encoder, and evaluate symmetry residuals exclusively on held-out test data.
3. **Permutation null and multiple-testing control:** Compare the held-out test statistic against a null distribution of random Fano-plane relabellings (permutations of the 7 axes not in $\mathrm{Aut}(\mathrm{PG}(2,2))$) and apply explicit family-wise error or FDR correction (e.g., Holm–Bonferroni or Benjamini–Hochberg) across all tested hypotheses, frequency bands, and time lags.
:::

### Stage 1: Pre-Registered Data Acquisition and Frozen Mapping

1. Record multi-channel neural data (e.g., high-density EEG/MEG, $\ge 64$ channels, with preregistered artifact rejection, filter bands, and window lengths).
2. Apply the **pre-registered, frozen** channel-to-axis readout mapping to obtain 7 complex analytic signals (or state estimates under a declared [reconstruction protocol](/docs/applied/research/reconstruction-identifiability)).
3. Estimate the 21 pairwise complex coherences $\gamma_{ij}(t)$, verify density-matrix positivity ($\Gamma \succeq 0$, $\mathrm{Tr}\,\Gamma = 1$), and report estimation uncertainty.

### Stage 2: Empirical Covariance and Decay-Rate Estimation

4. Compute the empirical $21 \times 21$ covariance matrix $C_{(ij),(kl)}(\tau)$ on held-out test epochs, distinguishing unsigned Gap statistics from signed/antisymmetric pair observables.
5. Separately estimate the 21 pairwise off-diagonal relaxation rates $r_{ij}$ from perturbation-recovery or autocorrelation envelopes.

### Stage 3: Pre-Registered Statistical Tests

6. **Primary Fano-dissipator test (rank-7 law, `T-260`):** Fit the nonnegative rank-7 model $r_{ij} = \frac{1}{6}\sum_{|\ell_p \cap \{i,j\}|=1} \gamma_p$ ($\gamma_p \ge 0$) and test the 14 linear Fano-incidence constraints on held-out data against random 7-block permutations (see [falsifiability F-rank7](/docs/reference/falsifiability#f-rank7-ранг-7-анизотропия-декогеренции)).
7. **Block-Fano covariance test ($\Pi_7 \oplus \Pi_{14}$):** Decompose the held-out empirical $21 \times 21$ covariance matrix into the $\Pi_7 \oplus \Pi_{14}$ subspace versus its orthogonal complement (229 residual degrees of freedom) and compute the variance explained relative to the permutation null across non-isomorphic label assignments.
8. **$G_2$-breaking benchmark:** On an explicitly specified antisymmetric representation $\Lambda^2 \mathbb{R}^7$, evaluate the four-index invariance residual
   $$
   W_a := \left\|\sum_{m} \left([T_a]_{im} C_{(mj),(kl)} + [T_a]_{jm} C_{(im),(kl)} + [T_a]_{km} C_{(ij),(ml)} + [T_a]_{lm} C_{(ij),(km)}\right)\right\|_F
   $$
   and $\Delta_{G_2}^{(\mathrm{exp})} := \max_a W_a / \|C\|_F$, reporting confidence intervals via block bootstrap.

### Stage 4: Honest Falsification Criteria

| Outcome on held-out pre-registered data | Interpretation |
|-----------------------------------------|----------------|
| Rank-7 Fano rate relations rejected ($p_{\mathrm{adj}} < \alpha$) | **Falsifies** the calibrated Fano-jump dissipator under the registered mapping |
| Block-Fano subspace ($\Pi_7 \oplus \Pi_{14}$) no better than random axis permutations | **Falsifies** Fano-triplet covariance organization under the registered mapping |
| $\Delta_{G_2}^{(\mathrm{exp})} \approx 0$ (exact continuous $G_2$ invariance) | **Inconsistent** with the coordinate Fano-pinching dissipator (`T-3`, which requires $\Delta_{G_2} \ge \frac{2}{3}\Delta_{\max}$) |
| Significant rank-7 fit and $\Pi_7 \oplus \Pi_{14}$ excess over permutation null, with nonzero $\Delta_{G_2}^{(\mathrm{exp})}$ | Consistent with the finite-covariance Fano-dissipator model (`T-260`), subject to replication |
::::

### 8.1 Falsifiable Predictions `[H]`

:::warning Falsifiable Empirical Hypotheses `[H]`
Under an independently pre-registered mapping to the 7 axes:
1. **Rank-7 relaxation structure (`T-260`):** If decoherence is governed by the Fano-line jump family, the 21 pairwise decay rates obey the 14 linear incidence constraints of $\mathrm{PG}(2,2)$ better than random non-isomorphic triple systems.
2. **Two-parameter Fano-block covariance:** If fluctuations respect the finite octonionic frame symmetry $\Gamma_{\mathrm{oct}}$ on the 21 edges, the covariance concentrates in the 2-parameter subspace $a'\Pi_7 + b'\Pi_{14}$ (with $a', b'$ both estimated, not fixed to a single arbitrary ratio).
3. **Absence of exact continuous $G_2$ invariance (`T-3`):** Because the coordinate dissipator breaks continuous $G_2$, exact $G_2$ Ward invariance is **not** predicted for the coordinate Fano model.

**Status:** Bare-dissipator kernel and $U(1)^7 \rtimes \mathrm{Aut}(r)$ covariance (`T-260`) `[T]`; non-covariance under continuous $G_2$ (`T-2`, `T-3`) `[T]`; empirical neural mapping `[H]`; testing protocol `[Pr]`.
:::

### 8.2 Practical Experimental Requirements `[Pr]`

- **Modality and temporal resolution:** High-temporal-resolution recordings (EEG/MEG, $\sim 1$ ms sampling) are required to resolve coherence relaxation rates; slow hemodynamic modalities (fMRI) impose severe temporal filtering that must be explicitly modelled.
- **Channel density and inverse modelling:** Source-space reconstruction ($\ge 64$ sensors) reduces volume-conduction leakage, which otherwise creates spurious zero-lag coherences and distorts phase estimates.
- **Recording duration and stationarity:** Verify weak stationarity across segments before estimating stationary covariances; use block-bootstrap resampling to account for temporal autocorrelation.
- **Artifact control:** Pre-register ocular, muscular, and line-noise rejection criteria before inspecting symmetry statistics.

---

## 9. Connections with Other CC Results {#связи}

### 9.1 Symmetry Structure and Protection Mechanisms

| Mathematical structure | Exact scope | Link |
|------------------------|-------------|------|
| Diagonal kernel $\ker(\mathcal{D}_{\mathrm{Fano}})$ (`T-260 [T]`) | Bare Fano dissipator preserves $\gamma_{kk}$; broken by connected $H$ | [Lindblad operators](/docs/core/operators/lindblad-operators#теорема-происхождение-тора) |
| Hamming $(7,4,3)$ parity-check structure (`[T]` for specified binary channel) | Requires declared binary noise and syndrome decoder; not automatic for continuous phases | [Topological protection](./topological-protection) |
| Homotopy $\pi_2(G_2/T^2) \cong \mathbb{Z}^2$ (`[T]` in algebraic topology) | Concerns maps from a 2D spatial domain; a single finite $7\times 7$ matrix carries no such topological charge | [Stability §7](./stability) |

### 9.2 Goldstone Modes

Goldstone's theorem applies to spontaneous breaking of a **continuous** symmetry of an action or Hamiltonian in a thermodynamic/spatial limit. Because the coordinate Fano dissipator explicitly breaks continuous $G_2$ (`T-3 [T]`), any soft modes in a finite-dimensional open matrix model are model-dependent damped modes of a chosen effective potential, not exact massless $G_2$ Goldstone bosons (see [Goldstone modes](./goldstone-modes)).

### 9.3 Connection to the Phase Diagram

In the [CC phase diagram](./phase-diagram-cc), regimes are governed by the chosen potential, regeneration rate $\kappa$, and dephasing rate $\Gamma_2$ rather than by continuous $G_2$ conservation. In particular, stationary branches and stability boundaries depend on the explicit reduced flow (`T-259`), not on 14 conserved charges.

### 9.4 Connection to Capability Thresholds

The defined capability thresholds $P_{\mathrm{crit}} = 2/7$, $R_{\mathrm{th}} = 1/3$, $\Phi_{\mathrm{th}} = 1$, and $D_{\mathrm{diff}} \ge 2$ ([Mathematical kernel](/docs/reference/mathematical-kernel#thresholds)) are algebraic predicates on $\Gamma$ (plus extended readout for $D_{\mathrm{diff}}$). Crossing these thresholds does not follow from, nor produce, 14 conserved $G_2$ charges.

---

## 10. Status Summary {#статусы}

| Statement | Status | Reference |
|-----------|--------|-----------|
| Universal 6-term Keldysh Lagrangian derivation | `[✗]` Retracted | `T-75 [✗]` |
| Universal Keldysh-to-Berry topological term in charges | `[✗]` Retracted | `T-85 [✗]` |
| Universal 14 continuous $G_2$ Noether charges of GKSL dynamics | `[✗]` Retracted | `T-2`, `T-3`, `T-260` |
| Integer quantization of diagonal populations ($\Delta N \in \mathbb{Z}$) | `[✗]` Retracted | `T-260` |
| Fano dephasing $= \frac{2}{3}$ atomic dephasing in fixed frame | `[T]` | `T-2` |
| Atomic/Fano dissipator is **not** $G_2$-covariant | `[T]` | `T-3` |
| Bare dissipator diagonal kernel & $U(1)^7 \rtimes \mathrm{Aut}(r)$ covariance (finite $\Gamma_{\mathrm{oct}} \subset G_2$) | `[T]` | `T-260` |
| Connected $H$ removes non-scalar diagonal conserved charges | `[T]` | `T-260` |
| Noether charges for a *postulated* $G_2$-invariant conservative action | `[C]` | [Noether charges](/docs/physics/gauge-symmetry/noether-charges) |
| $G_2$-invariant symmetric covariance on $\Lambda^2 \mathbb{R}^7$ has **2** parameters ($a\mathsf{P}_7 + b\mathsf{P}_{14}$) | `[T]` | [Noether charges](/docs/physics/gauge-symmetry/noether-charges#тождества-уорда-разложение) |
| Fano edge adjacency $\mathbf{F}_{21}$ has eigenvalues $2$ (mult 7) and $-1$ (mult 14) | `[T]` | [Noether charges](/docs/physics/gauge-symmetry/noether-charges#оператор-f21-определение) |
| Cognitive/clinical triplet reading | `[I]` / `[H]` | §7 |
| Pre-registered symmetry-testing protocol | `[Pr]` | §8 |

---

### What We Learned {#что-мы-узнали}

1. **Noether's theorem is conditional on actual symmetry of the dynamics:** Because UHM's universal Keldysh Lagrangian (`T-75 [✗]`) and Berry term (`T-85 [✗]`) are withdrawn and the bare Fano dissipator breaks continuous $G_2$ (`T-2`, `T-3`), there are **no** 14 universally conserved continuous $G_2$ Noether charges in open holon evolution.
2. **Exact bare-dissipator symmetry is $U(1)^7 \rtimes \mathrm{Aut}(r)$ (`T-260 [T]`):** The bare Fano dissipator preserves the 7 continuous diagonal populations $\gamma_{kk}$ and is covariant under the compact rephasing torus $U(1)^7$ (from the $\{0,1\}$ spectrum of coordinate projectors, not integer population quantization) extended by rate-preserving permutations; its overlap with $G_2$ is the finite group $\Gamma_{\mathrm{oct}}$ (order $1344$). A connected Hamiltonian $H$ removes all non-scalar diagonal conserved charges.
3. **Invariant covariances have two parameters, not one:** On $\Lambda^2 \mathbb{R}^7 = \mathbf{7} \oplus \mathbf{14}$, a $G_2$-invariant symmetric covariance has two independent parameters $(a, b)$; on the 21 Fano edges, the block-Fano algebra $\mathrm{span}\{\Pi_7, \Pi_{14}\}$ is likewise two-dimensional.
4. **Honest empirical testing requires pre-registration:** Channel-to-axis mappings must be fixed independently or cross-validated on separate splits with permutation nulls and multiple-testing correction — never selected by minimizing the symmetry residual on the test data.

:::tip Bridge to the Next Chapter
With the exact symmetries and boundaries of the formalism established, the [next chapter](./cybernetics-history) places Coherence Cybernetics within the broader 80-year arc of cybernetic thought — from Wiener and Ashby to von Foerster — comparing conceptual traditions with exact mathematical boundaries.
:::

---

## Related Documents

- [Charges of an Invariant Action](/docs/physics/gauge-symmetry/noether-charges) — exact Noether conditions and two-parameter invariant covariances
- [Gap Lagrangian Models](./lagrangian) — selected phase action ansatz (`T-75 [✗]` universal Keldysh derivation withdrawn)
- [Variational Derivation](./variational) — Euler–Lagrange equations and energy balance
- [Fano Channel and Gap Theorems](/docs/proofs/gap/fano-channel) — `T-2`, `T-3`, `T-260`, and $G_2$-breaking lower bound
- [Lindblad Operators](/docs/core/operators/lindblad-operators) — exact covariance group $U(1)^7 \rtimes \mathrm{Aut}(r)$
- [Effective Temperature](./effective-temperature) — rank-7 line-rate structure (§8)
- [CC Phase Diagram](./phase-diagram-cc) — reduced flows and regimes
- [Goldstone Modes](./goldstone-modes) — symmetry-breaking modes in effective models
- [Measurement of Consciousness](./measurement) — state reconstruction and uncertainty
- [Falsifiability](/docs/reference/falsifiability) — pre-registered falsification tests
