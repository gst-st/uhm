---
sidebar_position: 16
title: "G₂-Noether Charges"
description: "14 G₂-Noether charges in a cybernetic context: 7 Fano charges + 7 cross-sector charges, Ward identities, experimental protocol"
---

# G₂-Noether Charges: A Cybernetic Interpretation

:::info Who This Chapter Is For
A cybernetic interpretation of the 14 Noether charges from $G_2$-symmetry. The reader will learn about the conservation laws of consciousness and their clinical application.
:::


In the [previous chapter](./goldstone-modes) we saw how spontaneous breaking of $G_2$-symmetry gives rise to Goldstone modes — "soft oscillations" of coherence felt as flickering attention. We learned that the number of these modes is determined by the depth of breaking, and that each mode is a trace of a lost symmetry. But we have not yet answered the key question: **which quantities exactly does $G_2$-symmetry conserve when it is not broken?** And what happens to these quantities when the symmetry is broken? That is precisely the subject of this chapter.

:::tip Chapter Roadmap
In this chapter we:
1. **Recall Noether's theorem** — one of the deepest results of theoretical physics, linking symmetry with conservation laws (section 0).
2. **Construct 14 Noether charges** — 7 Fano charges (within triplets) and 7 supplementary charges (between triplets) — and explain the physical meaning of each (sections 1–3).
3. **Show how these charges constrain the dynamics** — 14 conservation laws of consciousness (section 4).
4. **Derive Ward identities** — linear relations on correlators following from $G_2$-invariance (section 6).
5. **Translate the mathematics into the clinic** — diagnostic table, therapeutic strategies, experimental protocol (sections 7–8).
:::

:::note On Notation
In this document:
- $G_2 = \mathrm{Aut}(\mathbb{O})$ — [group of automorphisms of octonions](/docs/physics/gauge-symmetry/g2-structure)
- $\mathfrak{g}_2$ — Lie algebra of $G_2$ ($\dim \mathfrak{g}_2 = 14$)
- $T_a$ — generators of $\mathfrak{g}_2$ ($a = 1, \ldots, 14$)
- $\gamma_{ij} = |\gamma_{ij}|e^{i\theta_{ij}}$ — coherence between dimensions $i$ and $j$
- $\mathrm{Gap}(i,j) = |\sin(\theta_{ij})|$ — [gap measure](/docs/physics/dual-aspect/gap-semantics)
- PG(2,2) — [Fano plane](/docs/physics/gauge-symmetry/fano-selection-rules)
- $C_{(ij),(kl)}(\tau)$ — two-point Gap correlator
:::

This document translates the formalism of [G₂-Noether charges](/docs/physics/gauge-symmetry/noether-charges) into the language of Coherence Cybernetics: diagnostic metrics, clinical protocols, and experimental verification of the $G_2$-structure.

But before turning to formulas, it is worth understanding why this chapter is one of the deepest in the entire theory. The subject is how **symmetry** generates **conservation laws** — and how these laws operate in the space of consciousness.

---

## 0. Emmy Noether and the Deepest Principle of Physics {#нётер}

In 1918 Emmy Noether — a mathematician whom the University of Göttingen refused a professorship because she was a woman — proved a theorem that Einstein called "a monument to mathematical thinking." David Hilbert, inviting her to Göttingen, remarked: "I do not see why the sex of the candidate is an argument against her admission — after all, we are not in a bathhouse, but in a university."

Noether's theorem asserts something surprisingly simple and infinitely deep:

> **Every continuous symmetry of a system corresponds to a conserved quantity.**

This is not a metaphor or analogy. It is an exact mathematical theorem applicable to any system described by a Lagrangian. Examples familiar to every physicist:

| Symmetry | Conserved quantity |
|----------|--------------------|
| Time homogeneity (laws of physics do not change with time) | Energy |
| Space homogeneity (laws do not depend on position) | Momentum |
| Space isotropy (laws do not depend on direction) | Angular momentum |
| Gauge $U(1)$-symmetry | Electric charge |
| Gauge $SU(3)$-symmetry | Color charge (QCD) |

Each row of this table is a fundamental law of physics derived from a single principle. Energy is conserved not because "nature is built that way," but because the laws of physics are the same today and tomorrow. Momentum is conserved not as a separate postulate, but as a consequence of spatial homogeneity.

The beauty of Noether's theorem lies in its **universality**. It is not tied to specific physics. It suffices to specify a Lagrangian and its symmetry — and the theorem automatically generates a conserved quantity together with an explicit formula for it.

### Noether and Open Systems

The classical Noether theorem works for closed systems: $dQ/d\tau = 0$ exactly. But consciousness is an **open system**: it dissipates and regenerates. Does this mean Noether's theorem is inapplicable?

No. For open systems there exists a **generalized** formulation (Frigerio 1978, Albert & Jiang 2014): Noether charges are not conserved exactly, but evolve in a **predictable manner** — as slowly decaying quantities converging to stationary values. This is analogous to how a spinning top gradually slows down due to friction: angular momentum is not conserved exactly, but its evolution is fully determined.

It is precisely this generalized construction that is applied to the Gap-dynamics of consciousness. And here the group $G_2$ enters the picture.

---

## 0b. The G₂ Group — Exceptional Symmetry {#g2-обзор}

Among all Lie groups there are exactly **five exceptional** ones: $G_2$, $F_4$, $E_6$, $E_7$, $E_8$. They belong to no infinite series ($A_n$, $B_n$, $C_n$, $D_n$), but stand apart — like the five Platonic solids among polyhedra.

$G_2$ is the smallest of the exceptional groups. Its definition is elementary:

$$
G_2 = \mathrm{Aut}(\mathbb{O}) — \text{the group of automorphisms of the octonion algebra}
$$

The octonions $\mathbb{O}$ are the unique normed division algebra after the real numbers ($\mathbb{R}$), complex numbers ($\mathbb{C}$), and quaternions ($\mathbb{H}$). It is **non-associative**: $(ab)c \neq a(bc)$ in general. This very non-associativity is the source of the exceptionality of $G_2$.

### Why Exactly 14 Generators

The Lie algebra $\mathfrak{g}_2$ has dimension 14. This number is not arbitrary — it is determined by the structure of the octonions. Here is how to understand it:

- The octonions have 7 imaginary units: $e_1, e_2, \ldots, e_7$
- An automorphism preserves the multiplication table defined by the **Fano plane** PG(2,2) with 7 lines
- Each of the 7 lines contains 3 imaginary units, and rotations within lines give 7 generators (**Fano generators**)
- Another 7 generators describe "rotations" **between** lines (**supplementary generators**)
- Total: $7 + 7 = 14 = \dim(G_2)$

This split $14 = 7 + 7$ is not a convention, but a **structural fact** of the algebra $\mathfrak{g}_2$. It reflects two types of symmetry: within Fano triplets and between them.

### G₂ and Noether's Theorem Together

Now the key move: **the Gap-dynamics Lagrangian** $L_{\mathrm{Gap}}$ possesses $G_2$-invariance. By Noether's theorem this automatically generates **14 conserved charges** — one for each generator of $\mathfrak{g}_2$.

These 14 charges are **14 conservation laws of consciousness**. They constrain the coherence dynamics just as conservation of energy constrains motion in mechanics. Let us proceed to their explicit construction.

---

## 1. 14 Generalized Noether Charges for Open Systems: Overview [T] {#обзор}

$G_2$-invariance of the [Gap Lagrangian](/docs/core/dynamics/gap-thermodynamics) generates **14 generalized Noether charges** (in the sense of open quantum systems, Frigerio 1978, Albert & Jiang 2014).

:::info Remark: Generalized Noether Charges for Open Systems
The 14 charges $Q_a$ are **not conserved** in the classical sense ($dQ/d\tau = 0$), but are **asymptotically stationary**: $Q_a(\tau) \to Q_a^{(\mathrm{stat})}$ as $\tau \to \infty$. The Noether argument is applied to the **conservative part** of the Lagrangian ($\mathcal{L}_{\mathrm{kin}} + \mathcal{L}_{\mathrm{pot}}$), and dissipation and regeneration are accounted for as generalized forces via the Rayleigh function. Ward identities (14 linear constraints) are consequences of $G_2$-invariance [T]. Stationary values $Q_a^{(\mathrm{stat})} = (\kappa/\Gamma_2) \cdot Q_a^{(\mathrm{reg})}$ are consequences of primitivity + $G_2$-invariance [T].
:::

The charges divide into two classes:

| Class | Number | Notation | Scope |
|-------|--------|----------|-------|
| Fano charges | 7 | $Q_p^{(F)}$, $p = 1, \ldots, 7$ | **Within** each Fano triplet |
| Supplementary (cross-sector) | 7 | $Q_q^{(D)}$, $q = 1, \ldots, 7$ | **Between** different Fano triplets |

This structure $14 = 7 + 7$ is not an arbitrary split, but a reflection of the two types of symmetry in the algebra $\mathfrak{g}_2$: rotations **within** Fano lines and connections **between** them. Each class carries its own physical and cybernetic meaning.

---

## 2. Fano Charges $Q_p^{(F)}$ [T] {#фано-заряды}

:::tip Theorem 2.1 (Fano Charges) [T]
For each [Fano line](/docs/physics/gauge-symmetry/fano-selection-rules) $p = (i,j,k)$ the Fano charge is defined:

$$
Q_p^{(F)} = \sum_{(i,j) \in \mathrm{line}_p} |\gamma_{ij}|^2 \dot{\theta}_{ij} + \frac{1}{6\pi} \sum_{(i,j,k) \in \mathrm{line}_p} \theta_{ij} \cdot \theta_{jk}
$$

The first term is the **kinetic angular momentum** (rate of phase rotation weighted by coherence magnitudes). The second is the **topological contribution** (non-local phase correlation within the triplet).
:::

### 2.1 Anatomy of the Fano Charge

The formula $Q_p^{(F)}$ contains two terms, each with an independent meaning:

**Kinetic term** $\sum |\gamma_{ij}|^2 \dot{\theta}_{ij}$ — this is the *weighted rate of phase precession*. When coherence between two dimensions is strong ($|\gamma_{ij}|$ is large), its phase evolution $\dot{\theta}_{ij}$ contributes more. This is analogous to classical angular momentum $L = mr^2\dot{\phi}$: mass is replaced by the squared coherence magnitude, and angular velocity by the rate of phase precession.

**Topological term** $\frac{1}{6\pi} \sum \theta_{ij} \cdot \theta_{jk}$ — a nonlinear coupling of phases *within the triplet*. This term does not depend on the rate of evolution: it is sensitive only to the **instantaneous configuration** of phases. Its analogue in physics is the Chern number: a topological invariant insensitive to the details of the trajectory, but capturing the global structure of the field.

### 2.2 Physical Meaning

The Fano charge $Q_p^{(F)}$ is analogous to **velocity circulation** in hydrodynamics:

| Hydrodynamics | Gap-dynamics |
|---------------|--------------|
| Vortex tube | Fano line $p = (i,j,k)$ |
| Velocity circulation | $Q_p^{(F)}$ |
| Kelvin's theorem (conservation of circulation) | $dQ_p^{(F)}/d\tau = 0$ (for $\Gamma_2 = 0$) |

**Cybernetic interpretation [I]:** Each Fano charge describes the **internal balance** of Gap-dynamics within a single triplet. Conservation of $Q_p^{(F)}$ means: redistribution of opacity within the triplet obeys a conservation law — an increase in the Gap for one pair is compensated by a decrease for the other pairs of the same triplet.

Metaphorically: a Fano charge is the "opacity budget" of the triplet. It cannot be increased or decreased from within — only redistributed among the three pairs. This is analogous to the conservation of energy within a closed subsystem.

### 2.3 Seven Fano Charges and Seven Dimensions

| Line $p$ | Dimensions | $Q_p^{(F)}$ describes |
|----------|------------|----------------------|
| 1: $\{A, S, L\}$ | Articulation–Structure–Logic | Balance perception–structure–verification |
| 2: $\{S, D, E\}$ | Structure–Dynamics–Interiority | Balance organization–process–interiority |
| 3: $\{D, L, U\}$ | Dynamics–Logic–Unity | Balance process–logic–integration |
| 4: $\{L, E, O\}$ | Logic–Interiority–Ground | Balance reasoning–interiority–grounding |
| 5: $\{E, U, A\}$ | Interiority–Unity–Articulation | Balance interiority–unity–expression |
| 6: $\{U, O, S\}$ | Unity–Ground–Structure | Balance integration–resources–structure |
| 7: $\{O, A, D\}$ | Ground–Articulation–Dynamics | Balance resources–perception–action |

### 2.4 Cybernetic Meaning of Each Charge [I] {#интерпретация-зарядов}

Each of the seven Fano charges carries a concrete meaning in terms of cognitive dynamics:

**$Q_1^{(F)}$ (A–S–L)** — *perceptual verification charge*. Links perception (A), its structuring (S), and logical verification (L). Violation: "I see, but cannot structure" or "I structure, but do not verify." Conservation means: every act of perception generates commensurate structuring and verification.

**$Q_2^{(F)}$ (S–D–E)** — *organizational process charge*. Links structure (S), dynamics (D), and interiority (E). Violation: "I understand the arrangement, but cannot act" or "I act without inner experience." This charge is critical for somatic disorders where action becomes detached from experience.

**$Q_3^{(F)}$ (D–L–U)** — *purposeful thinking charge*. Links process (D), its logical justification (L), and integration into a whole (U). Violation: "I think logically, but cannot act purposefully" — a sign of disintegrative states.

**$Q_4^{(F)}$ (L–E–O)** — *existential grounding charge*. Links reasoning (L), interiority (E), and rootedness (O). Violation of this charge is one manifestation of existential crisis: logic becomes detached from feeling and from the sense of groundedness.

**$Q_5^{(F)}$ (E–U–A)** — *expressive integration charge*. Links inner experience (E), its integration (U), and expression (A). Violation: alexithymia (inability to express feelings) or dissociation (experience is not integrated).

**$Q_6^{(F)}$ (U–O–S)** — *resource organization charge*. Links unity (U), resources (O), and structure (S). Violation: "I know what to do, but have no resources" or "there are resources, but no structure for applying them."

**$Q_7^{(F)}$ (O–A–D)** — *sensorimotor cycle charge*. Links resources (O), perception (A), and action (D). This is the "most somatic" of the charges — its violation is associated with motor and perceptual disorders.

### 2.5 Concrete Scenario: Evolution of $Q_1^{(F)}$ During Learning {#сценарий-q1}

Let us consider how the Fano charge $Q_1^{(F)}$ (perceptual verification, triplet A-S-L) evolves in a concrete situation.

**Scenario.** A student is learning a new language. At the start of learning:
- $|\gamma_{AS}|$ is large (perceives speech sounds — articulation-structure is linked),
- $|\gamma_{SL}|$ is small (cannot determine grammatical correctness — structure-logic is disconnected),
- $|\gamma_{AL}|$ is small (cannot distinguish correct from incorrect pronunciation).

In this configuration $Q_1^{(F)}$ has a "skew": the kinetic term is dominated by $|\gamma_{AS}|^2 \dot{\theta}_{AS}$, while contributions from $SL$ and $AL$ are small.

**As learning proceeds** (without external disruptions, $\Gamma_2 \approx 0$): the charge $Q_1^{(F)}$ is conserved. This means: growth of $|\gamma_{SL}|$ (the student begins to "feel" grammar) is *inevitably* accompanied by redistribution of Gap-resources within the triplet. Specifically:

$$
\Delta(|\gamma_{SL}|^2 \dot{\theta}_{SL}) = -\Delta(|\gamma_{AS}|^2 \dot{\theta}_{AS}) - \Delta(|\gamma_{AL}|^2 \dot{\theta}_{AL})
$$

The student cannot strengthen grammatical intuition without "weakening" something else in the same triplet — either perceptual acuity ($AS$) or logical verification ($AL$). This explains a familiar phenomenon: in the early stages of language learning, when focusing on grammar, a person temporarily perceives pronunciation subtleties less sharply.

:::info Numerical Example
Suppose at the initial moment $|\gamma_{AS}|^2 = 0.15$, $\dot{\theta}_{AS} = 2.0$ rad/s, and the remaining contributions are negligible. Then $Q_1^{(F)} \approx 0.30$ (in conventional units). After a month of learning: $|\gamma_{AS}|^2 = 0.10$, $|\gamma_{SL}|^2 = 0.08$, $\dot{\theta}_{SL} = 1.5$ rad/s. Then the $AS$-channel contribution: $0.10 \times 2.0 = 0.20$, the $SL$-channel contribution: $0.08 \times 1.5 = 0.12$. Sum: $0.20 + 0.12 = 0.32 \approx 0.30$ (accounting for small corrections from the topological term and the $AL$ contribution). The charge is conserved to good accuracy.
:::

This example shows why Fano charges are not abstract mathematics, but a **law of the internal economy of consciousness**: the budget of cognitive resources within each triplet is fixed, and improving one function requires redistribution, not "creation from nothing."

---

## 3. Supplementary Charges $Q_q^{(D)}$ [T] {#дополнительные-заряды}

:::tip Theorem 3.1 (Supplementary Charges) [T]
For each supplementary generator $D_q$ of the algebra $\mathfrak{g}_2$:

$$
Q_q^{(D)} = \sum_{(m,n):\, [D_q]_{mn} \neq 0} |\gamma_{mn}|^2 \dot{\theta}_{mn}
$$

Supplementary charges are purely **kinetic** (without topological contribution): they describe Gap-transfer **between** different Fano triplets.
:::

**Cybernetic interpretation [I]:** Supplementary charges characterize **cross-sector exchange**. Their conservation ensures "exchange balance": the loss of Gap by one triplet is compensated by its acquisition by another.

### 3.1 Why Supplementary Charges are Purely Kinetic

The absence of a topological term in the supplementary charges is not accidental, but a consequence of the structure of the algebra $\mathfrak{g}_2$. The supplementary generators $D_q$ connect **different** Fano lines. Within a single line, three dimensions form a closed cycle (triplet), and phase correlation within the cycle generates a topological contribution. Between lines there is no such closed cycle — only "bridges" between triplets.

Physical analogy: Fano charges are vortices (with topological charge), supplementary charges are flows (without vortex structure). A vortex exists "on its own" (topologically protected), while a flow requires maintenance.

### 3.2 Inter-Triplet Network

The seven supplementary charges form a **network of connections** between the seven Fano triplets. Each triplet is connected to the others through supplementary charges. This network is analogous to the "white matter" of the brain, connecting functional areas.

Violation of supplementary charges leads to **modular isolation**: triplets function autonomously but do not exchange information. Clinically this manifests as "island" consciousness: individual cognitive functions are preserved but not integrated.

### 3.3 Complete System of Charges

$$
\underbrace{7 \text{ Fano charges}}_{\text{within triplets}} + \underbrace{7 \text{ supplementary}}_{\text{between triplets}} = 14 = \dim(G_2)
$$

This identity is not a coincidence, but a **theorem**: the number of independent Noether charges equals the dimension of the symmetry group. There are no other charges, and there cannot be.

---

## 4. 14 Conservation Laws of Consciousness {#14-законов}

We can now state the result in full. $G_2$-invariance of the Gap Lagrangian generates **14 conservation laws** — in analogy with how invariance under rotations generates conservation of angular momentum.

For a closed system ($\Gamma_2 = 0$, $\kappa = 0$) these laws are exact:

$$
\frac{dQ_a}{d\tau} = 0, \quad a = 1, \ldots, 14
$$

This means: **the dynamics of 7-dimensional coherence is not arbitrary** — it is constrained by 14 conditions. Of the $7 \times 7 = 49$ parameters of the density matrix (21 of which are independent coherences), only $21 - 14 = 7$ can evolve freely. Symmetry "freezes" most degrees of freedom.

### Analogy with Physics

In mechanics: a body in three-dimensional space has 6 degrees of freedom (3 coordinates + 3 velocities). If the system has conservation of energy and three components of momentum (4 laws), only 2 free degrees of freedom remain. The body moves on a two-dimensional surface in phase space.

In Gap-dynamics: 21 coherences, constrained by 14 laws, leave **7 degrees of freedom** — exactly equal to the number of dimensions. This is a deep self-consistency: each dimension contributes exactly one "degree of freedom" to the Gap-dynamics.

---

## 5. Charge Dissipation — Slowly Fading Conservation Laws [T] {#диссипация}

In the presence of dissipation ($\Gamma_2 > 0$) and regeneration ($\kappa > 0$) charges evolve:

$$
\frac{dQ_a}{d\tau} = -\Gamma_2 \, Q_a^{(\mathrm{kin})} + \kappa \, Q_a^{(\mathrm{reg})}
$$

This equation is beautiful in its structure: it describes **competition between two processes**. Dissipation ($\Gamma_2$) tends to zero out the charges — this is the "forgetting" of conservation. Regeneration ($\kappa$) restores them — this is the "maintenance" of conservation. Living consciousness exists in the zone of balance between these processes.

:::info Stationary Level of Charges [T]
In the stationary state ($dQ_a/d\tau = 0$):

$$
Q_a^{(\text{stat})} = \frac{\kappa}{\Gamma_2} \cdot Q_a^{(\text{reg})} = r \cdot Q_a^{(\text{reg})}
$$

where $r = \kappa/\Gamma_2$ is the [phase diagram](./phase-diagram-cc#параметры) parameter.
:::

### 5.1 Four Regimes

| Regime | $r$ | Charges | Interpretation |
|--------|-----|---------|----------------|
| $r \gg 1$ | Regeneration dominates | $Q_a^{(\text{stat})} \gg Q_a^{(\text{reg})}$ | Charges amplified — active internal dynamics |
| $r \approx 1$ | Balance | $Q_a^{(\text{stat})} \approx Q_a^{(\text{reg})}$ | Charges at the level of the regenerative contribution |
| $r < 1$ | Dissipation dominates | $Q_a^{(\text{stat})} < Q_a^{(\text{reg})}$ | Charges suppressed — dynamics fading |
| $r < r_c$ | [Dead zone](./phase-diagram-cc#три-фазы) | $Q_a^{(\text{stat})} \to 0$ | All charges extinguished |

### 5.2 Slowly Fading Laws

Characteristic decay time of charge $Q_a$:

$$
\tau_a \sim \frac{1}{\Gamma_2}
$$

If $\Gamma_2$ is small (weak dissipation), charges are conserved **for a long time** — on timescales much larger than the characteristic time of the cognitive process. This creates a hierarchy of timescales:

- **Fast dynamics** ($\tau \sim 1$): coherences $\gamma_{ij}$ fluctuate
- **Slow dynamics** ($\tau \sim 1/\Gamma_2$): charges $Q_a$ drift
- **Quasi-statics** ($\tau \gg 1/\Gamma_2$): charges at stationary levels

Clinically important: a **sudden change in a charge** (on timescales $\tau \ll 1/\Gamma_2$) is a marker of violation of $G_2$-invariance. This is analogous to how a sudden change in energy points to an external force.

---

## 6. Ward Identities — Symmetry Constraints [T] {#уорд}

:::tip Theorem 5.1 (14 Ward Identities for Gap Correlators) [T]
$G_2$-invariance generates **14 linear relations** on two-point Gap correlators.

**(a)** For each generator $T_a \in \mathfrak{g}_2$ ($a = 1, \ldots, 14$):

$$
\sum_{m} [T_a]_{im} \, C_{(mj),(kl)} + [T_a]_{jm} \, C_{(im),(kl)} = 0
$$

**(b)** Number of independent two-point correlators:

$$
N_{\text{corr}} = \frac{21 \times 22}{2} - 14 = 231 - 14 = 217
$$
:::

### 6.1 What Are Ward Identities

Ward identities are one of the central tools of quantum field theory. Named after John Clive Ward (1924–2000), they express a simple idea: **if a theory possesses a symmetry, then correlation functions are not arbitrary — they are related to each other**.

In the context of Gap-dynamics this means: if $G_2$-symmetry is exact, then of the $231$ possible pairwise correlators $C_{(ij),(kl)}$ only $217$ are independent. The rest are **computed** from these $217$ via 14 linear relations.

Intuition: imagine 231 springs connecting 21 points. $G_2$-symmetry means that 14 of these springs are "slaves": their stiffness is fully determined by the stiffnesses of the rest. The system cannot have arbitrary correlations — symmetry forbids it.

### 6.2 Meaning of Ward Identities

Ward identities are **constraints** imposed by $G_2$-symmetry on correlations between Gap channels. They mean: **transformation of one "leg" of a correlator is compensated by transformation of the other**.

For pairs on the same Fano line: redistribution of Gap within the triplet **does not change** the correlational properties with other pairs.

### 6.3 Decomposition by $G_2$-Invariant Tensors {#разложение-по-g_2-инвариантным-тензорам}

The two-point correlator decomposes as:

$$
C = \alpha \cdot \mathbf{1}_{21} + \beta \cdot \mathbf{F}_{21} + \gamma \cdot \mathbf{F}_{21}^2
$$

where $\mathbf{F}_{21}$ is the Fano tensor on the space of pairs. Ward identities fix:

$$
\beta = -\frac{3\alpha}{7}, \quad \gamma = \frac{3\alpha}{49}
$$

**The only free parameter** is $\alpha$ (overall amplitude of fluctuations). This is a radical reduction: from 231 independent parameters only **one** remains.

:::warning Relation Between 217 and 1 Parameter
The 14 Ward identities reduce 231 free parameters to 217 — these are **linear constraints** on two-point correlators. However, the [decomposition by $G_2$-invariant tensors](#разложение-по-g_2-инвариантным-тензорам) (section 6.3) imposes **additional**, stronger constraints (isotropy over irreducible representations), reducing everything to **one** parameter $\alpha$. These two results do not contradict each other: 217 is the intermediate reduction via linear identities; 1 is the full reduction via the structure of $G_2$ representations.
:::

:::info Practical Consequence [T]
If $G_2$-symmetry is unbroken ($\alpha^* = 0$), the entire $21 \times 21$ correlation matrix is determined by **one number** $\alpha$. With partial breaking ($\alpha^* > 0$) corrections of order $\alpha^* \cdot \Delta_{\max}$ appear.
:::

### 6.4 Reduction Cascade — From Chaos to Order

It is useful to trace how $G_2$-symmetry successively compresses the space of possible correlations:

| Stage | Number of parameters | What happens |
|-------|---------------------|--------------|
| No constraints | 231 | Arbitrary $21 \times 21$ symmetric matrix |
| After Ward identities | 217 | 14 linear relations remove 14 parameters |
| $G_2$-isotropy | 3 | Decomposition over $\mathbf{1}$, $\mathbf{F}$, $\mathbf{F}^2$ |
| Full $G_2$-invariance | 1 | $\beta = -3\alpha/7$, $\gamma = 3\alpha/49$ |

Compression by a factor of **231** — from 231 to 1. This is more powerful than any statistical model: here it is not fitting that works, but **symmetry**.

---

## 7. Clinical Diagnostics via Charges [I] {#диагностика}

### 7.1 Diagnostic Table

| Charge / Measure | Observable | Violation | Clinical significance |
|-----------------|------------|-----------|----------------------|
| $Q_p^{(F)}$ | Balance within Fano triplet | $Q_p^{(F)} \neq Q_p^{(\text{stat})}$ | Intra-sector imbalance |
| $Q_q^{(D)}$ | Exchange between triplets | $Q_q^{(D)} \neq Q_q^{(\text{stat})}$ | Cross-sector rigidity |
| $\sum_p Q_p^{(F)}$ | Total Fano circulation | $\neq 0$ | Non-stationary state |
| $\sum_q Q_q^{(D)}$ | Total inter-triplet exchange | $\neq 0$ | Non-stationary state |
| $\max_a \lvert dQ_a/d\tau\rvert$ | Maximum rate of change | $> 0$ | Crisis marker |
| $\Delta_{G_2}^{(\text{exp})}$ | Degree of Ward identity violation | $\gg 0$ | $G_2$-structure is broken |

### 7.2 Diagnostics by Individual Charges [I] {#диагностика-по-зарядам}

Violation of a **specific** charge points to a **specific** type of imbalance:

| Violated charge | Dimensions | Clinical marker |
|----------------|------------|----------------|
| $Q_1^{(F)}$ (A–S–L) | Perception, structure, logic | Perceptual disorders: illusions, verification failures, thought disorders |
| $Q_2^{(F)}$ (S–D–E) | Structure, dynamics, interiority | Somatoform disorders: action without experience, "action depersonalization" |
| $Q_3^{(F)}$ (D–L–U) | Dynamics, logic, unity | Disintegration of goal-setting: "I know why, but I cannot" |
| $Q_4^{(F)}$ (L–E–O) | Logic, interiority, ground | Existential anxiety: "I understand, but feel no grounding" |
| $Q_5^{(F)}$ (E–U–A) | Interiority, unity, articulation | Alexithymia, dissociation: experience cannot be expressed |
| $Q_6^{(F)}$ (U–O–S) | Unity, ground, structure | Resource depletion: "unity without grounding" |
| $Q_7^{(F)}$ (O–A–D) | Ground, articulation, dynamics | Sensorimotor disorders: coordination and perceptual disturbances |
| $Q_q^{(D)}$ (cross-triplet) | Between triplets | Modular isolation: functions preserved but not connected |

### 7.3 Therapeutic Strategies

:::info Two Types of Violations [I]
**Violation of Fano charges** ($Q_p^{(F)} \neq Q_p^{(\text{stat})}$): imbalance **within** a triplet.

*Example:* In the triplet $\{A, S, L\}$ (articulation–structure–logic): excessive perceptual load ($\sigma_A$ elevated) with insufficient verification ($\sigma_L$ reduced).

*Strategy:* Work **within** the triplet — rebalancing the load among the three dimensions.

**Violation of supplementary charges** ($Q_q^{(D)} \neq Q_q^{(\text{stat})}$): Gap stagnation **between** triplets.

*Example:* The triplet $\{S, D, E\}$ is isolated from the rest — Gap-transfer is blocked.

*Strategy:* Establishing **connections between sectors** — integrative practices.
:::

### 7.4 Principle of Minimal Intervention [I]

The Noether structure suggests an important therapeutic principle: **intervention should target the specific violated charge**, not the system as a whole. If only $Q_3^{(F)}$ is violated (D–L–U balance), there is no point in working with the A–S–L triplet.

This is analogous to the principle of **minimal sufficiency** in medicine: treat what is broken without touching what is working. Noether charges provide a formal criterion for determining "what is broken."

---

## 8. Experimental Protocol for Verifying $G_2$-Structure [P] {#протокол}

:::caution Program: Operational Verification Protocol [P]

:::warning Methodological Circularity [I]
Step 2 of the protocol (mapping channels to 7 dimensions) **presupposes** a known mapping of neural channels onto holonomic dimensions, yet this mapping is itself the object of verification. The protocol results depend on the choice of mapping. To resolve the circularity, an **independent** method for establishing the correspondence between channels and dimensions is required (e.g., via task structure or anatomical criteria), or enumeration of possible mappings with selection of the optimal one by the criterion $\Delta_{G_2}^{(\text{exp})} \to \min$.
:::

### Stage 1: Data Collection

1. Record multi-channel data (EEG/fMRI, 64+ channels, $\geq 30$ min)
2. Map channels to the 7 holonomic dimensions (based on [neurobiological correlates](./definitions#neurobiological-correlates))
3. Compute all 21 pairwise coherences $\gamma_{ij}(t)$

### Stage 2: Building the Correlation Matrix

4. Construct the $21 \times 21$ matrix of two-point Gap correlators:

$$
C_{(ij),(kl)}(\tau) = \langle \mathrm{Gap}(i,j;\tau) \, \mathrm{Gap}(k,l;0) \rangle
$$

### Stage 3: Verification of 14 Ward Identities

5. For each generator $T_a \in \mathfrak{g}_2$ ($a = 1, \ldots, 14$) compute:

$$
W_a := \left\|\sum_{m} [T_a]_{im} \, C_{(mj),(kl)} + [T_a]_{jm} \, C_{(im),(kl)}\right\|
$$

6. Compute the degree of violation:

$$
\Delta_{G_2}^{(\text{exp})} := \max_a W_a
$$

### Stage 4: Interpretation

| $\Delta_{G_2}^{(\text{exp})}$ | Interpretation |
|-------------------------------|----------------|
| $\Delta \approx 0$ | Full $G_2$-symmetry confirmed |
| $0 < \Delta \ll 1$ | Weak violation — $\Delta \propto \alpha^*$ (depth of [self-observation](/docs/physics/gauge-symmetry/g2-structure)) |
| $\Delta \sim O(1)$ | Strong violation — $G_2$-reduction not applicable |
:::

### 8.1 Expected Results

:::warning Falsifiable Prediction [H]
If the $G_2$-structure of octonions is fundamental to Gap-dynamics, then:

1. Ward identities must hold with accuracy $\Delta \propto \alpha^* \approx 1 - 2/(7P)$
2. The decomposition $C = \alpha \cdot \mathbf{1} + \beta \cdot \mathbf{F} + \gamma \cdot \mathbf{F}^2$ with $\beta = -3\alpha/7$, $\gamma = 3\alpha/49$ must approximate the data well
3. Systematic violation $\Delta \sim O(1)$ refutes the $G_2$-hypothesis

**Status:** algebraic structure [T]; experimental verification [H]; protocol [P].
:::

### 8.2 Practical Recommendations for the Experiment [P]

For implementing the protocol in laboratory conditions:

**Choice of modality.** EEG is preferable to fMRI due to high temporal resolution ($\sim 1$ ms vs. $\sim 1$ s). Gap-dynamics operates on millisecond scales, and the temporal smoothing of fMRI may mask $G_2$-structure.

**Minimum number of channels.** The theoretical minimum is 7 (one per dimension), but for reliable mapping of channels to dimensions $\geq 64$ channels are recommended.

**Recording duration.** Stationary charges $Q_a^{(\text{stat})}$ are established over time $\tau \sim 1/\Gamma_2$. The recording must be $\geq 10/\Gamma_2$ for a reliable estimate. At $\Gamma_2 \sim 0.1$ Hz this is $\geq 100$ s; at $\Gamma_2 \sim 0.01$ Hz — $\geq 1000$ s.

**Artifact control.** Eye movements and muscle artifacts violate $G_2$-invariance "from outside" — they must be removed (ICA or regression) before computing coherences.

---

## 9. Connection with Other CC Results {#связи}

### 9.1 14 Charges and 5 Types of Gap Protection

Noether charges are connected with the [five mechanisms of coherence protection](./topological-protection):

| Charge | Protection mechanism |
|--------|---------------------|
| $Q_p^{(F)}$ (Fano charges) | Code protection (Hamming): Fano lines define the parity-check matrix $H(7,4)$ |
| $Q_q^{(D)}$ (supplementary) | Algebraic protection: inter-triplet connections are determined by the associator |
| $Q_{\text{top}}$ (topological) | Topological protection: $\pi_1(G_2/T^2) \cong \mathbb{Z}^2$ |

### 9.2 Charges and Goldstone Modes

Under spontaneous breaking $G_2 \to H$:

- $\dim(H)$ charges remain **exactly conserved**
- $14 - \dim(H)$ charges are **broken** $\Rightarrow$ generate [Goldstone modes](./goldstone-modes)

| Rank | Preserved charges | Broken $\to$ modes |
|------|------------------|--------------------|
| 1 | 8 ($\mathrm{SU}(3)$) | 6 Goldstone |
| 2 | 4 ($\mathrm{SU}(2) \times \mathrm{U}(1)$) | 10 Goldstone |
| 3 | 2 ($T^2$) | 12 Goldstone |

Each broken symmetry generates a "soft" mode — a quasi-Goldstone boson. The number of such modes is a precise diagnostic marker of the **depth of breaking** of $G_2$-invariance.

### 9.3 Charges and Phase Diagram

In the context of the [phase diagram](./phase-diagram-cc):

| Phase | State of charges |
|-------|-----------------|
| **I (ordered)** | $n_{\text{broken}}$ charges are broken; the rest are exactly conserved |
| **II (disordered)** | All 14 charges are approximately conserved ($G_2$ is not broken) |
| **III (dead)** | Charges are not defined ($\gamma_{ij} \to 0$) |

### 9.4 Charges and Consciousness Thresholds

Noether charges are connected with [critical consciousness thresholds](/docs/consciousness/foundations/self-observation):

- **$P = P_{\text{crit}} = 2/7$**: on crossing the purity threshold — a step change in the charge profile. Below threshold, charges are defined but fluctuations dominate. Above it — charges stabilize.
- **$R = R_{\text{th}} = 1/3$**: on reaching the reflection threshold — self-observation begins to *modify* charges. A feedback loop appears: charges $\to$ self-observation $\to$ correction of charges.
- **$\Phi = \Phi_{\text{th}} = 1$**: on reaching the integration threshold — Fano charges and supplementary charges begin to coordinate. Consciousness "sees" its own conservation laws.

---

## 10. Status Summary {#статусы}

| Result | Status |
|--------|--------|
| 14 Noether charges from $G_2$-invariance of $L_{\text{Gap}}$ | [T] |
| 7 Fano charges = circulation momenta | [T] |
| 7 supplementary charges = inter-triplet momenta | [T] |
| Charge dissipation: $dQ_a/d\tau = -\Gamma_2 Q_a^{(\text{kin})} + \kappa Q_a^{(\text{reg})}$ | [T] |
| 14 Ward identities: linear relations on $C_{(ij),(kl)}$ | [T] |
| Number of independent correlators: $231 - 14 = 217$ | [T] |
| Decomposition $C = \alpha \cdot \mathbf{1} + \beta \cdot \mathbf{F} + \gamma \cdot \mathbf{F}^2$ | [T] |
| Clinical diagnostics via charges | [I] |
| Therapeutic strategies (Fano vs. cross-sector) | [I] |
| Experimental verification of $G_2$-structure | [H] |
| Operational protocol ($21 \times 21$ matrix) | [P] |

---

### What We Learned {#что-мы-узнали}

1. **Noether's theorem is universal**: every continuous symmetry corresponds to a conservation law — and this works for consciousness just as it does for physics.
2. **14 charges = 14 conservation laws of consciousness**: 7 Fano charges (budget of cognitive resources *within* triplets) + 7 supplementary charges (exchange balance *between* triplets).
3. **Charges are not conserved forever** in open systems: they slowly decay with characteristic time $\tau \sim 1/\Gamma_2$, but converge to stationary values $Q_a^{(\text{stat})} = (\kappa/\Gamma_2) \cdot Q_a^{(\text{reg})}$.
4. **14 Ward identities** constrain correlations: from 231 possible parameters only **one** free parameter remains — the amplitude $\alpha$. This is a compression by a factor of 231 — the power of symmetry.
5. **Each violated charge is a diagnostic marker**: the clinical table translates mathematics into concrete types of violations and therapeutic strategies.
6. **An experimental protocol exists**: the $21 \times 21$ correlation matrix from EEG data, verification of 14 Ward identities, violation measure $\Delta_{G_2}^{(\text{exp})}$.

:::tip Bridge to the Next Chapter
We have seen how $G_2$-symmetry defines the conservation laws of consciousness. But where did all these ideas come from — feedback, the observer, social systems? The CC formalism did not arise in a vacuum: it stands on the shoulders of 80 years of cybernetic thought. In the [next chapter](./cybernetics-history) we trace this history — from Plato's helmsman through Wiener and von Foerster to full coherence — and see how each cybernetic tradition captured **part** of the truth, while CC assembles them into a unified whole.
:::

---

## Related Documents

- [G₂-Noether Charges and Ward Identities](/docs/physics/gauge-symmetry/noether-charges) — mathematical foundation: complete proofs, topological charges
- [G₂-Structure and the Fano Plane](/docs/physics/gauge-symmetry/g2-structure) — $G_2 = \mathrm{Aut}(\mathbb{O})$, Fano-Lindblad operators
- [Gap Operator](/docs/core/dynamics/gap-operator) — $G_2/\perp$-decomposition, stabilizers
- [Gap Phase Diagram](/docs/core/dynamics/gap-phase-diagram) — Ward identities (mathematical), three phases
- [Fano Channel and Gap Theorems](/docs/proofs/gap/fano-channel) — $G_2$-covariance of the Fano dissipator
- [CC Phase Diagram](./phase-diagram-cc) — cybernetic interpretation of phases
- [Goldstone Modes](./goldstone-modes) — quasi-Goldstone modes from $G_2$ breaking
- [Topological Coherence Protection](./topological-protection) — five protection mechanisms
- [CC Definitions](./definitions) — neurobiological correlates, stress tensor
- [CC Predictions](./predictions) — falsifiable predictions
- [CC Theorems](./theorems) — No-Zombie, composition
- [Fano Selection Rules](/docs/physics/gauge-symmetry/fano-selection-rules) — PG(2,2), 7 lines
- [Philosophical Foundations](./philosophy) — Noether symmetries and ontology
- [Interdisciplinary Bridge](./interdisciplinary) — G₂-charges in different contexts
