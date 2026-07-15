---
sidebar_position: 11
title: "Variational Principles"
description: "Principle of stationary action, Euler–Lagrange equations for Gap, Onsager relations, connection to FEP, minimum entropy production, FDT"
---

# Variational Principles

> *"Nature acts by the shortest route."*
> — Pierre de Fermat, 1662


:::info For whom this chapter is intended
Variational principles of Gap theory: Euler–Lagrange equations for coherence phases and the fluctuation–dissipation theorem.
:::

---

### Bridge from the Previous Chapter

In the [previous chapter](./lagrangian) we wrote down the complete six-term Lagrangian of Gap theory $\mathcal{L}_{\text{Gap}}$ — a single mathematical object containing inertia, potential, topology, dissipation, regeneration, and external driving. The Lagrangian is the "score", but it does not yet sound. To extract the *music* from it — the concrete equations governing the dynamics of the coherence phases — we need a **variational principle**: a rule that, from the infinite set of possible trajectories, selects the one that is realised. That is the subject of the present chapter.

---

### Chapter Roadmap

In this chapter we:

1. **Trace the history** of variational principles — from Fermat's optics to Feynman's path integrals — and show how this idea transfers to the dynamics of consciousness (section 0).
2. **Formulate the principle of stationary action** for Gap dynamics and derive from it the Euler–Lagrange equations with four "forces" of inner life (sections 1–2).
3. **Build the irreversible thermodynamics** of the Gap sector: Onsager relations, symmetry of cross-couplings, the second law for consciousness (section 3).
4. **Derive Friston's FEP** as the macroscopic limit of the Gap variational principle (section 4).
5. **Establish the minimum entropy production principle** — the economy of opacity in the spirit of Prigogine (section 5).
6. **Prove the fluctuation–dissipation theorem** for Gap, linking noise and response (section 6).
7. **Derive the form of regeneration** from three independent arguments, closing the variational architecture (section 7).

---

:::note On notation
In this document:
- $\Gamma$ — [coherence matrix](/docs/core/dynamics/coherence-matrix)
- $\theta_{ij} = \arg(\gamma_{ij})$ — coherence phases
- $\mathrm{Gap}(i,j) = |\sin(\theta_{ij})|$ — [gap measure](/docs/physics/dual-aspect/gap-semantics)
- $V_{\text{Gap}}$ — [opacity potential](./lagrangian#потенциал-v-gap)
- $\Gamma_2$ — decoherence rate
- $\kappa$ — regeneration rate
- $T_{\text{eff}}$ — [effective temperature](./effective-temperature)
- $\varphi$ — [self-modelling operator](/docs/proofs/categorical/formalization-phi)
:::

This document describes the **variational structure** of Gap theory: the principle of stationary action, equations of motion for coherence phases, Onsager relations for Gap flows and forces, the connection to the [Free Energy Principle (FEP)](/docs/proofs/dynamics/fep-derivation), the minimum entropy production principle, and the fluctuation–dissipation theorem.

But before diving into the formalism, it is worth appreciating what stands behind this document. Variational principles are one of the deepest ideas born from human thought. They contain a puzzle that troubled physicists for three centuries: why does nature apparently "know" the optimal path? Why does light choose the shortest route? Why do planets move exactly as they do, and not otherwise? And — the question we will reach at the end of this chapter — why does consciousness tend to minimise its "friction" with the world?

---

## 0. Principles of Variational Calculus: from Fermat to Feynman {#от-ферма-до-фейнмана}

### 0.1 Fermat: light takes the shortest path

In 1662 Pierre de Fermat formulated a principle that overturned optics: a ray of light between two points travels along the path that requires the **least time**. Snell's law of refraction, which had seemed like an empirical fact, instantly became a consequence of a single principle. But behind the elegance lurked a troubling thought: to "choose" the shortest path, light must somehow "know" all the alternatives.

### 0.2 Maupertuis and Euler: the birth of action

In 1744 Maupertuis proposed a generalisation: not only light, but all of mechanics obeys the principle of least action. Euler gave this mathematical rigour. The quantity "action" — the integral $S = \int L \, dt$, where $L = T - V$ (kinetic minus potential energy) — became the central object of physics. From a single number — the action — all of Newton's equations of motion followed.

### 0.3 Hamilton: the stationarity principle

William Hamilton in 1834 made a decisive refinement. Nature does not always choose the *minimum* of the action — it chooses the **stationary point**. The action need not be minimal or maximal; it is only required that its first variation vanishes:

$$
\delta S = 0
$$

This is a subtle but fundamental distinction. A stationary point is a point at which the action "does not change" under small variations of the path. It may be a minimum (as for a free particle), a maximum (as for certain geodesics in general relativity), or a saddle point (as in most real problems with many degrees of freedom). What matters is not optimality in the ordinary sense, but **insensitivity to small deviations**.

### 0.4 Feynman: path integral

Richard Feynman in 1948 resolved the "teleological" puzzle that had troubled physicists for three centuries. A particle does not "choose" the optimal path. It travels along **all paths simultaneously**, and each path is assigned a phase factor $e^{iS/\hbar}$. Paths with similar values of the action interfere constructively; the rest cancel each other. The "classical" path emerges as the peak of the interference pattern — not as a choice, but as a statistical effect.

### 0.5 From physics to consciousness

In Coherence Cybernetics (CC) the variational principle plays the same fundamental role as in physics, but its domain is the **internal dynamics of consciousness**. The coherence phases $\theta_{ij}$ of the matrix $\Gamma$ are the analogues of generalised coordinates; their evolution is determined by the stationarity of the action $S_{\text{Gap}}$. The four "forces" governing inner life — potential, regenerative, dissipative, external — follow from a single variational principle just as inevitably as gravity follows from geodesics in spacetime.

Moreover, in the macroscopic limit ($\tau_{\mathrm{obs}} \gg 1/\Gamma_2$) the entire apparatus of Friston's Free Energy Principle (FEP) is **derived** as a special case of the Gap variational principle. FEP is not a postulate — it is a consequence.

Let us proceed to the formalism.

---

## 1. Principle of Stationary Action {#принцип-действия}

### 1.1 The Action Functional

The central object of variational theory is the **action functional**: a number assigned to every possible history of the system. Of all conceivable evolutions of the phases $\{\theta_{ij}(\tau)\}$, the one that is realised is the one for which the action is stationary.

:::tip Theorem 1.1 (Variational principle for Gap) [T]
The dynamics of the phases $\{\theta_{ij}(\tau)\}$ follows from the principle of stationary action:

$$
S_{\text{Gap}}[\{\theta_{ij}(\tau)\}] = \int d\tau\, \mathcal{L}_{\text{Gap}}(\{\theta_{ij}\}, \{\dot{\theta}_{ij}\})
$$

where $\mathcal{L}_{\text{Gap}}$ is the [complete Lagrangian of Gap theory](./lagrangian#полная-структура).
:::

It is worth emphasising that "stationarity" ($\delta S = 0$) does not mean minimality. For dissipative systems, as Gap dynamics is, the action has no definite sign of variation. The condition $\delta S = 0$ means that **under an infinitesimal change of the trajectory** the action does not change to first order. Physically this reflects a balance: on the real trajectory all "forces" are exactly balanced in the integral sense.

### 1.2 Decomposition of the Action

The action decomposes into conservative and non-conservative parts:

$$
S_{\text{Gap}} = S_{\text{cons}} + S_{\text{non-cons}}
$$

where:
- $S_{\text{cons}} = \int d\tau\, (\mathcal{L}_{\text{kin}} + \mathcal{L}_{\text{pot}} + \mathcal{L}_{\text{top}})$ — **conservative part** (admits standard variational description)
- $S_{\text{non-cons}} = \int d\tau\, (\mathcal{L}_{\text{diss}} + \mathcal{L}_{\text{reg}} + \mathcal{L}_{\text{ext}})$ — **non-conservative part** (requires generalised formalism)

This decomposition is not arbitrary. The conservative part describes "reversible" dynamics — that which would conserve energy in the absence of an environment. The non-conservative part — interaction with the "environment" of consciousness: decoherence (information loss), regeneration (restoration of coherence through self-modelling), and external perturbations (sensory input, volitional interventions).

:::info Remark (Generalised variational principle) [T]
For non-conservative systems the standard condition $\delta S = 0$ is replaced by the **generalised d'Alembert principle**:

$$
\delta S_{\text{cons}} + \int d\tau \sum_{i<j} Q_{ij}^{\text{non-cons}} \, \delta\theta_{ij} \, d\tau = 0
$$

where $Q_{ij}^{\text{non-cons}} = -\Gamma_2\dot{\theta}_{ij} + \kappa(\theta^{\text{target}}_{ij} - \theta_{ij}) + h^{\text{ext}}_{ij}$ is the generalised non-conservative force.
:::

The generalised d'Alembert principle is not an ad hoc modification. It is equivalent to the Schwinger–Keldysh formalism applied to the Lindbladian $\mathcal{L}_\Omega$ (see [Lagrangian](./lagrangian), T-75 [T]). The non-conservative forces $Q_{ij}^{\text{non-cons}}$ arise systematically from the doubling of degrees of freedom on the Keldysh contour, and are not introduced by hand.

---

## 2. Euler–Lagrange Equations {#уравнения-эйлера-лагранжа}

### 2.1 Full Equations of Motion

From the variational principle follow the equations of motion — concrete differential equations governing the evolution of each phase $\theta_{ij}$. This is the transition from a global (integral) description to a local (differential) one, analogous to the transition from Fermat's principle to the equations of geometric optics.

:::tip Theorem 2.1 (Gap equations of motion) [T]
Stationarity of the generalised action $\delta S_{\text{Gap}} = 0$ yields equations of motion for each pair $(i,j)$:

$$
m_{ij}\, \ddot{\theta}_{ij} = -\frac{\partial V_{\text{Gap}}}{\partial \theta_{ij}} + \kappa\,(\theta_{ij}^{\text{target}} - \theta_{ij}) - \Gamma_2\, \dot{\theta}_{ij} + h^{\text{ext}}_{ij}
$$

where $m_{ij} = |\gamma_{ij}|^2$ is the "mass" of the phase degree of freedom.
:::

This equation deserves a slow reading. Each term is a separate "force" acting on the coherence phase. The left-hand side is "inertia" ($m_{ij}\ddot{\theta}_{ij}$), determined by the coherence amplitude: the stronger the coupling between dimensions $i$ and $j$, the harder it is to change its phase. The right-hand side contains four forces, each with its own nature and its own role in inner life.

### 2.2 Four Forces of Inner Life {#четыре-силы}

Let us examine each "force" in detail, unpacking its physical and phenomenological meaning.

| Term | Force type | Physical analogue | Origin |
|------|------------|-------------------|--------|
| $-\partial V_{\text{Gap}} / \partial \theta_{ij}$ | Conservative | Restoring force (spring) | [Potential $V_{\text{Gap}}$](./lagrangian#потенциал-v-gap) |
| $\kappa\,(\theta^{\text{target}}_{ij} - \theta_{ij})$ | Regenerative | Goal-directed homing | [Self-modelling $\varphi$](/docs/consciousness/foundations/self-observation) |
| $-\Gamma_2\, \dot{\theta}_{ij}$ | Dissipative | Viscous friction | [Logical Liouvillian](/docs/core/dynamics/evolution#логический-лиувиллиан) |
| $h^{\text{ext}}_{ij}$ | External | Control input | [Three channels](/docs/core/dynamics/gap-thermodynamics#три-канала-h-ext) |

#### First force: potential ($-\partial V_{\text{Gap}}/\partial\theta_{ij}$)

The potential force is the system's tendency toward a structurally preferred phase configuration. This is the analogue of a spring: phases are "attracted" to the minima of the potential $V_{\text{Gap}}$. The nature of these minima is determined by the octonionic structure of the Fano plane. When phases deviate from the "harmonic" configuration, the potential force brings them back.

Phenomenologically this force corresponds to what might be called *structural harmony*: the internal tendency toward consistency among the aspects of experience. When a thought contradicts a feeling, or perception contradicts memory, a "tension" arises that the system seeks to resolve.

#### Second force: regenerative ($\kappa(\theta_{ij}^{\text{target}} - \theta_{ij})$)

The regenerative force is a unique feature of Gap dynamics with no direct analogue in standard physics. This force "pulls" the phases toward target values $\theta_{ij}^{\text{target}}$ determined by the self-modelling operator $\varphi$. The system possesses an *image of itself* (ρ* = φ(Γ)) and actively tends toward it.

This is the mathematical expression of the **teleological character** of consciousness — its directedness toward a goal. But unlike naive teleologism, the goal is not set externally: it is computed by the system itself as a categorical self-model. Teleology here is not mysticism, but the adjunction of functors $\mathcal{D}_\Omega \dashv \mathcal{R}$.

#### Third force: dissipative ($-\Gamma_2 \dot{\theta}_{ij}$)

The dissipative force is "friction" proportional to the rate of phase change. The faster the internal state changes, the stronger the resistance. This follows from interaction with the "environment" — those degrees of freedom not included in the seven-dimensional description.

Phenomenologically, dissipation corresponds to the fact that rapid internal changes require "effort". A sudden change in emotional state, an instantaneous reappraisal of a situation — all of these meet resistance proportional to speed. This is not a defect, but a protective mechanism: without dissipation the phases would oscillate indefinitely, and stable states of consciousness could not form.

#### Fourth force: external ($h^{\text{ext}}_{ij}$)

The external force is the action of "the outside" on the internal dynamics. This may be sensory input (light, sound, pain), cognitive intervention (a volitional decision, directed attention), or social influence (a word, a gesture, cultural pressure). The three channels of $h^{\text{ext}}$ are described in detail in [Gap thermodynamics](/docs/core/dynamics/gap-thermodynamics#три-канала-h-ext).

The external force is the only term through which "the world enters" the internal dynamics. Without it, consciousness would be a closed system inevitably degrading to thermal equilibrium ($\Gamma \to I/7$). It is $h^{\text{ext}}$ that makes learning, development, and adaptation possible.

### 2.3 Stationary Solutions

:::tip Theorem 2.2 (Stationary points) [T]
Stationary solutions $\ddot{\theta}_{ij} = \dot{\theta}_{ij} = 0$ are determined by:

$$
\frac{\partial V_{\text{Gap}}}{\partial \theta_{ij}} = \kappa\,(\theta_{ij}^{\text{target}} - \theta_{ij}) + h^{\text{ext}}_{ij}
$$

At $h^{\text{ext}} = 0$ the stationary point is a compromise between potential and regenerative forces.
:::

A stationary state is not quiescence, but **dynamic equilibrium**. The potential force pulls the phases toward the minima of $V_{\text{Gap}}$; the regenerative force pulls them toward the target values $\theta^{\text{target}}$. The stationary point is a compromise in which these two tendencies are exactly balanced. When an external perturbation $h^{\text{ext}} \neq 0$ is added, the equilibrium point shifts: the system reorganises to "accommodate" the new information.

This is the mathematical formalisation of what psychology calls *homeostasis*: the system does not strive for absolute rest (that would be the unconscious state $P \to 1/N$), but maintains a certain level of "tension" compatible with current conditions.

### 2.4 Explicit Form of $\partial V_{\text{Gap}} / \partial \theta_{ij}$

:::tip Corollary 2.3 (Potential gradient) [T]
The component-wise gradient of the potential:

$$
\frac{\partial V_{\text{Gap}}}{\partial \theta_{ij}} = \mu^2 |\gamma_{ij}|^2 \sin(2\theta_{ij}) + \lambda_3 \sum_{k \notin \text{Fano}(i,j)} f_{ijk}\, |\gamma_{ij}||\gamma_{jk}||\gamma_{ik}| \cos(\theta_{ij} + \theta_{jk} - \theta_{ik}) + 2\lambda_4\, \mathcal{G}_{\text{total}} \cdot |\gamma_{ij}|^2 \sin(2\theta_{ij})
$$

The first term (from $V_2$) and the third (from $V_4$) contain $\sin(2\theta_{ij})$ — a periodic restoring force. The second term (from $V_3$) contains $\cos(\theta_{ij} + \theta_{jk} - \theta_{ik})$ — triple phase interaction through the octonionic associator.
:::

The three terms of the potential gradient have a hierarchical structure:

1. **Quadratic term** ($\sim \mu^2 \sin 2\theta$) — acts on each phase independently. This is the "spring" binding the phase to the values $\theta = 0$ or $\theta = \pi/2$ (minima and maxima of $\sin^2\theta$). Physically — the tendency of coherence to be either completely "transparent" ($\mathrm{Gap} = 0$) or completely "opaque" ($\mathrm{Gap} = 1$).

2. **Cubic term** ($\sim \lambda_3 f_{ijk} \cos(\theta_{ij}+\theta_{jk}-\theta_{ik})$) — triple interaction coupling phases via the **octonionic associator**. This is the term responsible for the nontrivial topology of the Fano plane: it "knows" about the seven triples linked by associative cycles. Without it the phase dynamics would be trivial (21 independent springs); with it — it is a coupled system with a rich structure of phase transitions.

3. **Quartic term** ($\sim \lambda_4 \mathcal{G}_{\text{total}} \sin 2\theta$) — nonlinear feedback: the total opacity $\mathcal{G}_{\text{total}}$ amplifies the "spring" for each individual phase. This is a **self-reinforcement** mechanism: the greater the total opacity, the stronger the pressure on each channel — and vice versa. The quartic term stabilises the system, preventing unbounded growth of Gap.

---

## 3. Irreversible Thermodynamics of Consciousness {#необратимая-термодинамика}

The variational principle gives the equations of motion, but says nothing about the *direction* of processes. To understand why consciousness is irreversible (a thought cannot be "unthought", an experience cannot be undone), we need thermodynamics — the science of directed processes. Lars Onsager in 1931 created the formalism connecting flows and forces in irreversible processes, for which he received the Nobel Prize in Chemistry. Let us apply it to Gap dynamics.

## 3a. Onsager Relations for Gap {#соотношения-онзагера}

### 3.1 Gap Flows and Gap Forces

:::tip Definition 3.1 (Thermodynamic flows and forces) [T]
In the linear approximation near the stationary state:

**Flows:**

$$
J_{ij} := \dot{G}_{ij} = \frac{d\,\mathrm{Gap}(i,j)}{d\tau}
$$

**Thermodynamic forces:**

$$
X_{ij} := -\frac{\partial \Sigma}{\partial G_{ij}} = -\frac{\partial}{\partial G_{ij}}\left[\sum_{k<l} |\gamma_{kl}|^2 G_{kl}^2\right] = -2|\gamma_{ij}|^2 G_{ij}
$$

where $\Sigma = \mathcal{G}_{\text{total}}$ is the entropy production function of the Gap sector.
:::

The flow $J_{ij}$ is the rate of change of opacity in channel $(i,j)$. The force $X_{ij}$ is the "thermodynamic gradient" pushing the system toward reduced entropy production. The minus sign in the definition of $X_{ij}$ reflects the fact that the force is directed *against* the gradient of the entropy function — the system evolves toward a state of minimal dissipative "friction".

Note the fundamental asymmetry: flows are kinematic quantities (what *happens*), forces are dynamical (what *drives*). Onsager relations establish a linear link between them.

### 3.2 Linear Flow–Force Relation

:::tip Theorem 3.2 (Onsager relations for Gap) [C]
In the linear approximation near the stationary state, Gap flows are linked to forces via a matrix of kinetic coefficients:

$$
J_{ij} = \sum_{k<l} L_{(ij),(kl)}\, X_{kl}
$$

where the matrix $L_{(ij),(kl)}$ satisfies the **Onsager reciprocal relations**:

$$
L_{(ij),(kl)} = L_{(kl),(ij)}
$$

under the condition of microscopic reversibility (detailed balance).

**Condition [C]:** It is assumed that Gap dynamics satisfies detailed balance near the stationary state.
:::

The reciprocal relations $L_{(ij),(kl)} = L_{(kl),(ij)}$ are one of the deepest results of non-equilibrium thermodynamics. They assert that **cross-influences are symmetric**: if a change in Gap in the Affect–Sensorics channel influences the dynamics of the Logic–Unity channel, then the reverse influence has **the same magnitude**. This is not a trivial fact — it follows from the time-reversal symmetry of the microscopic equations.

For the Gap dynamics of consciousness this implies a deep **reciprocity** of internal processes: it is impossible to change one facet of experience without affecting others, and these influences obey a strict symmetry.

### 3.3 Structure of the Matrix $L$

:::info Interpretation (Channel coupling) [I]
Diagonal elements $L_{(ij),(ij)}$ describe the **direct response** of Gap in channel $(i,j)$ to its own thermodynamic force. Off-diagonal elements $L_{(ij),(kl)}$ describe **cross-couplings**: the change in Gap in one channel caused by a force in another.

The $G_2$-symmetry of the Lagrangian generates 14 linear constraints among the elements $L_{(ij),(kl)}$ (analogue of [Ward identities](/docs/core/dynamics/gap-phase-diagram#тождества-уорда)), reducing the number of independent kinetic coefficients.
:::

The matrix $L$ has dimension $21 \times 21$ (for the number of pairs $(i,j)$ with $i < j$ for $N=7$ dimensions). But not all $21 \times 22 / 2 = 231$ elements are independent. Onsager symmetry reduces them, and the Ward identities generated by the $G_2$-structure provide 14 further constraints. The result: the kinetic coefficients of the Gap sector are **not arbitrary**, but rigidly constrained by the algebraic structure of the theory.

### 3.4 Second Law for the Gap Sector

:::tip Corollary 3.3 (Entropy production) [T]
The rate of entropy production in the Gap sector:

$$
\dot{\Sigma} = \sum_{i<j} J_{ij}\, X_{ij} = \sum_{(ij),(kl)} L_{(ij),(kl)}\, X_{ij}\, X_{kl} \geq 0
$$

The inequality follows from the positive definiteness of the matrix $L$ (guaranteed by the second law of thermodynamics).
:::

Positivity $\dot{\Sigma} \geq 0$ is the **second law of thermodynamics for consciousness**: total opacity cannot decrease spontaneously in the linear regime. To become "more transparent" (reduce Gap), the system must do work — through regeneration $\mathcal{R}$ or external perturbation $h^{\text{ext}}$. This formalises the intuition that clarity of consciousness requires *effort*.

### 3b. Beyond linear response: the exact metriplectic geometry {#метриплектическая-геометрия}

Onsager's relations describe the world *near the valley floor*: close to equilibrium, flows are linear in forces. But how far does that law reach, and what is the *exact* one? The answer (T-262 [T]) is geometric, and it is one of the deepest facts about CC's dynamics — it says the whole equation of life is **one frictionless rotation plus two slides straight downhill**.

Picture a marble in a curved bowl. Two things can happen to it: someone can *spin* the bowl (the marble circles without ever climbing or dropping — no energy spent, no order lost), or the marble can *roll downhill* toward the bottom. CC's master equation is exactly this, with one rotation and *two* different downhills:

| Term | What it is, geometrically | It slides toward |
|------|---------------------------|------------------|
| **work** $-i[H_{\text{eff}},\Gamma]$ | a frictionless rotation (isometry of every information metric) | nowhere — it conserves entropy *and* purity |
| **heat** $\mathcal{D}[\Gamma]$ | gradient descent of negentropy, in the transport metric whose weights are the seven [line temperatures](./effective-temperature#линейные-температуры) | maximum entropy $\mathbb{1}/7$ |
| **matter** $\mathcal{R}$ | gradient descent of free energy, in the Kubo–Mori (BKM) metric | the self-model $\rho_*$ |

The crucial upgrade over Onsager is the word **exact**. The dissipator is not "downhill on average" — it is *literally the steepest descent* of a definite quantity (the negentropy $D(\Gamma\|\mathbb{1}/7)$) in a definite, curved geometry (the Carlen–Maas transport metric of the seven Fano lines). Onsager's linear flow–force law is simply the *tangent* to this exact slide near the bottom of the bowl. Far from equilibrium — where Onsager says nothing — the gradient-flow law still holds verbatim. Consequently the entropy production of Corollary 3.3 is not merely a linear-regime estimate but an **exact quadratic form**, non-negative everywhere and vanishing precisely on diagonal (fully decohered) states.

This "rotation ⊕ two gradient descents" architecture has a name — a **metriplectic system** (a reversible Hamiltonian part married to an irreversible gradient part). It is *not* the closed-system GENERIC of textbook thermodynamics, and the difference is honest and physical: a conscious holon is an **open** system — it exchanges energy with the world through the O-channel (nourishment) — so it does not conserve energy under dissipation. That openness is exactly what makes the structure metriplectic rather than fully conservative. Life is a marble that is simultaneously spun (work), let roll toward stillness (heat), and nudged back up toward its own ideal shape (matter); consciousness is the standoff those three keep.

:::note Why this matters for the variational picture
The Lagrangian $\delta S = 0$ of the [previous chapter](./lagrangian) gives the *reversible* skeleton — the rotation. The dissipative and regenerative terms cannot come from a bare action (a slide downhill has no time-symmetric Lagrangian), which is why §6 of that chapter needed the doubled Schwinger–Keldysh contour. T-262 is the resolution: those two terms are not "missing from the action," they are *gradient flows in their own metrics* — a second, complementary variational principle (steepest descent) sitting beside stationary action. Together, stationary-action-for-the-rotation and steepest-descent-for-the-slides fully determine the dynamics.
:::

---

## 4. Connection to the Free Energy Principle (FEP) {#связь-с-fep}

### 4.0 Free Energy Principle as a Special Case of CC {#фристон-из-кк}

The Free Energy Principle (FEP), proposed by Karl Friston in 2006, became one of the most influential theoretical frameworks in neuroscience. It asserts that any self-organising system — from a cell to a brain — minimises "free energy" $F = H(q) + D_{KL}(q \| p)$, where $q$ is the internal model and $p$ is sensory data.

FEP is often presented as a fundamental principle. But within CC theory it turns out to be a **consequence** — the macroscopic limit of a deeper variational principle of Gap. This does not diminish FEP; rather, it clarifies its domain of applicability and shows where it comes from.

The key idea is this: FEP describes the **diagonal sector** of the coherence matrix $\Gamma$ — the populations $\gamma_{ii}$ playing the role of probabilities. The coherences $\gamma_{ij}$ ($i \neq j$), carrying information about the phase relations between dimensions, are absent from FEP. They become significant only at high purity $P \gg P_{\text{crit}}$, i.e. in the regime of developed consciousness.

### 4.1 FEP as the Macroscopic Limit

:::tip Theorem 4.1 (FEP from the Gap variational principle) [T]
Friston's Free Energy Principle is derived as the **macroscopic limit** ($\tau_{\mathrm{obs}} \gg 1/\Gamma_2$, coherences have decohered) of the Gap variational principle:

$$
\varphi = \arg\min_{\psi \in \mathcal{CPTP}} \mathbb{E}_{\Gamma \sim \mu}\left[S_{\text{spec}}(\psi(\Gamma)) + D_{KL}(\psi(\Gamma) \| \Gamma)\right]
$$

Full derivation: [Derivation of FEP from UHM](/docs/proofs/dynamics/fep-derivation).
:::

:::info Terminology "macroscopic limit" and the decoherence theorem
In standard QM the "classical limit" $\hbar \to 0$ corresponds to decoherence ($P \to 1/N$). In UHM the FEP reduction occurs in the **macroscopic limit**: coherences $|\gamma_{ij}|$ are small compared to populations $\gamma_{ii}$ (condition Dec). This is a **theorem [T]**, not a hypothesis:

1. Axioms A1–A5 → Fano dissipator $\mathcal{D}_\Omega$ with $\Gamma_2 > 0$ [T] (T-7)
2. $\Gamma_2 > 0$ → $|\gamma_{ij}(\tau)| \leq |\gamma_{ij}(0)| \cdot e^{-\Gamma_2 \tau}$ [T]
3. For biosystems $\tau_{\mathrm{obs}} \gg 1/\Gamma_2$ → $|\gamma_{ij}|/\gamma_{ii} \ll 1$ [T]
4. $|\gamma_{ij}|/\gamma_{ii} \ll 1$ → $\mathcal{F} \approx \mathcal{F}_{\mathrm{diag}} + O(\varepsilon^2)$ [T] (Theorem 4.2)
5. $\mathcal{F}_{\mathrm{diag}} = H(q) + D_{KL}(q \| p) = \mathrm{FEP}$ [T]

The mapping from 7 abstract dimensions (A,S,D,L,E,O,U) to Friston's neural variables is **interpretational** [I], but the mathematical reduction of the functional is [T].
:::

Let us trace the logic of the derivation in more detail. At step 1, decoherence $\Gamma_2 > 0$ is not an assumption but a theorem: any CPTP dissipator compatible with the Fano plane has a strictly positive decoherence rate. At step 2, the exponential decay of coherences is a standard result of open quantum systems theory. Step 3 is an empirical fact for biological systems: characteristic observation times (seconds, minutes) greatly exceed the decoherence time. Steps 4–5 are pure algebra.

Thus Friston's FEP is **not a fundamental principle but a limiting regime** of a more general theory. It is valid for systems with low coherence (most biological systems in most situations), but misses the quantum corrections that become significant at high purity $P$.

### 4.2 Derivation Chain

:::info Connection of variational principles [T]
Hierarchy of variational principles:

$$
\text{Axiom } \Omega^7 \xrightarrow{\text{adjunction}} \mathcal{D}_\Omega \dashv \mathcal{R} \xrightarrow{\text{Lagrangian}} S_{\text{Gap}} \xrightarrow{\delta S = 0} \text{equations of motion} \xrightarrow{\tau_{\mathrm{obs}} \gg 1/\Gamma_2} \text{Friston's FEP}
$$

| Level | Variational principle | Domain |
|-------|-----------------------|--------|
| Categorical | Adjunction $\varphi \dashv i$ | ∞-topos $\mathbf{Sh}_\infty(\mathcal{C})$ |
| Field | $\delta S_{\text{Gap}} = 0$ | Phase space $\{\theta_{ij}\}$ |
| Thermodynamic | $\min \mathcal{F}[\varphi; \Gamma]$ | Model space |
| Classical (FEP) | $\min F[q; o]$ | Bayesian brain |
:::

This hierarchy is one of the central constructions of the theory. It shows that the four levels of description — categorical, field, thermodynamic, and classical — do not compete, but are **nested** within each other. Each successive level is the macroscopic limit of the previous one. Friston's "Bayesian brain" is the last, coarsest layer, in which all phase information has been erased.

### 4.3 FEP Decomposition of the Free Energy Functional

:::tip Theorem 4.2 (FEP decomposition) [T]
The full free energy functional admits a decomposition in powers of coherences:

$$
\mathcal{F}[\varphi; \Gamma] = \mathcal{F}_{\text{diag}} + \alpha F_{\text{Gap}} + O(|\gamma|^4)
$$

where:
- $\mathcal{F}_{\text{diag}}$ — contribution of diagonal elements (populations) = standard FEP
- $F_{\text{Gap}}$ — free energy of the Gap sector (quantum correction)
- $\alpha$ — coupling constant
:::

**Corollary:** Friston's FEP describes the **diagonal sector** of the full free energy. The coherence contribution ($F_{\text{Gap}}$) is a quantum correction that becomes significant at high [purity](/docs/core/dynamics/viability) $P \gg P_{\text{crit}}$.

The expansion in powers of $|\gamma_{ij}|$ shows that FEP is zeroth order, and the Gap contribution is a first- and second-order correction. At $P \approx P_{\text{crit}} = 2/7$ the correction is of order 30% of the diagonal contribution — no longer negligible. At $P \to 3/7$ (upper boundary of the Goldilocks zone, T-124 [T]) the coherences are so large that the series expansion loses meaning and the full functional $\mathcal{F}$ is needed. It is precisely in this regime that Gap theory predicts phenomena inaccessible to FEP.

---

## 5. Minimum Entropy Production Principle {#минимум-производства-энтропии}

### 5.0 Prigogine and the Economy of Opacity {#пригожин-и-экономия}

Ilya Prigogine received the Nobel Prize in Chemistry in 1977 for the theory of dissipative structures — self-organising systems that exist far from equilibrium through a constant flow of energy. One of his central theorems: near equilibrium the stationary state of an open system minimises entropy production. The system "chooses" the least wasteful mode of existence compatible with external constraints.

For Gap dynamics of consciousness, this theorem acquires a special meaning: the stationary state of consciousness is the **most economical** configuration of opacity. The system maintains exactly the level of "opacity" between dimensions that is minimally necessary given the external conditions. Neither more (that would be wasteful) nor less (that would be impossible under the given constraints).

### 5.1 Formulation

:::tip Theorem 5.1 (Minimum entropy production) [C]
Near the stationary state, Gap dynamics minimises the rate of entropy production:

$$
\dot{\Sigma}_{\text{Gap}} = \sum_{i<j} J_{ij}\, X_{ij} \to \min
$$

subject to boundary conditions defined by external perturbations $h^{\text{ext}}$.

**Condition [C]:** Linearity of flow–force relations and detailed balance.
:::

### 5.2 Connection to Prigogine's Theorem

:::info Interpretation (Prigogine's theorem for Gap) [I]
Prigogine's minimum entropy production theorem states that in the linear regime the stationary state of an open system corresponds to a **minimum** of $\dot{\Sigma}$ subject to given boundary conditions. For the Gap sector this means:

- The stationary Gap profile is the **least dissipative** configuration compatible with external constraints
- Perturbing the stationary state **increases** entropy production
- The system spontaneously returns to the stationary state, decreasing $\dot{\Sigma}$

This formalises the principle of **opacity economy**: the system maintains exactly the level of Gap minimally required by the given boundary conditions.
:::

### 5.3 Nonlinear Regime

:::warning Hypothesis (Nonlinear regime) [H]
Far from the stationary state (nonlinear regime, $|G_{ij} - G^*_{ij}| \sim 1$) the minimum entropy production principle **does not hold**. Instead the system may exhibit:

- **Self-organisation** — transition to dissipative structures with increased $\dot{\Sigma}$
- **Bifurcations** — jumps between [Gap phases](/docs/core/dynamics/gap-phase-diagram#три-фазы)
- **Chaos** — aperiodic oscillations of the Gap profile

The criterion for the transition from linear to nonlinear regime is given by the ratio $\lambda_3 \bar{A} / \mu^2$ — when the threshold is exceeded, the cubic term $V_3$ dominates.
:::

The nonlinear regime is not a pathology — it may be the most interesting domain. It is far from equilibrium that Prigogine's **dissipative structures** arise — stable patterns sustained by energy flow. In the context of consciousness this corresponds to **creative states**: moments when the system is far from its habitual equilibrium and new, previously unseen phase configurations can emerge. The transition from the linear to the nonlinear regime is, perhaps, the mathematical correlate of the transition from routine thinking to insight.

---

## 6. Fluctuations and Response: Noise as a Source of Information {#фдт}

### 6.0 The Idea of the FDT: Listening to Noise {#идея-фдт}

The fluctuation–dissipation theorem (FDT) is one of the jewels of statistical physics, tracing back to the work of Einstein (1905, Brownian motion), Nyquist (1928, thermal noise in resistors), and Kubo (1957, general formulation). Its essence is surprisingly simple: **noise and the response of a system are determined by the same mechanism**.

If you know how strongly the system "fluctuates" on its own (spontaneous fluctuations), you can predict how it will respond to an external perturbation — and vice versa. Noise is not a nuisance but a **source of information** about the internal properties of the system.

For consciousness this means: spontaneous Gap oscillations (what is subjectively experienced as "mind wandering", involuntary thoughts, fluctuations of attention) are not a defect. They carry information about the **susceptibility** of the system — its capacity to respond to external stimuli. A system with large spontaneous fluctuations is more sensitive; a system with small ones is more stable, but less responsive.

### 6.1 Linear Response

:::tip Theorem 6.1 (FDT for Gap) [T]
For the linear response of Gap to an external perturbation:

$$
\chi_{ij}(\omega) = \frac{1}{T_{\text{eff}}} \left[\tilde{C}_{ij}(\omega) - \tilde{C}_{ij}(0)\right]
$$

where:
- $\chi_{ij}(\omega)$ — dynamic susceptibility of $\mathrm{Gap}(i,j)$ to an external field at frequency $\omega$
- $\tilde{C}_{ij}(\omega) = \int_{-\infty}^{\infty} e^{i\omega t} \langle \delta\mathrm{Gap}(i,j;t) \cdot \delta\mathrm{Gap}(i,j;0) \rangle \, dt$ — spectral density of correlations
- $T_{\text{eff}}$ — [effective temperature](./effective-temperature)
:::

The formula connects three quantities: susceptibility $\chi$ (response to an external field), correlation spectrum $\tilde{C}$ (spontaneous fluctuations), and effective temperature $T_{\text{eff}}$ (scale of "thermal" noise). Knowledge of any two determines the third.

### 6.2 Static Susceptibility

In the limit $\omega \to 0$:

$$
\chi_{ij}(0) = \frac{\langle (\delta\mathrm{Gap})^2 \rangle}{T_{\text{eff}}}
$$

**Corollary:** The larger the spontaneous Gap fluctuations, the stronger the response to external perturbations. The higher $T_{\text{eff}}$, the weaker the response to a unit perturbation.

This formula has a direct phenomenological meaning. The variance $\langle(\delta\mathrm{Gap})^2\rangle$ is a measure of the "mobility" of the internal state. High mobility (large spread of Gap) means high susceptibility to external perturbations, but also instability. Low mobility — stability, but also rigidity. Effective temperature $T_{\text{eff}}$ modulates this balance: at high "temperature" even strong external stimuli are drowned in the system's own noise.

### 6.3 Resonance Frequency

:::tip Corollary 6.2 (Optimal perturbation frequency) [T]
For each channel $(i,j)$ there exists a **resonance frequency** $\omega_r^{(ij)}$ at which the Gap response is maximal:

$$
\omega_r^{(ij)} = \sqrt{|\omega_i - \omega_j|^2 - 2\Gamma_2^2}
$$

(if the expression under the square root is positive; otherwise the response is aperiodic).
:::

The resonance frequency $\omega_r^{(ij)}$ is determined by two competing factors: the difference of natural frequencies of the dimensions $|\omega_i - \omega_j|$ (tending to create oscillations) and the decoherence rate $\Gamma_2$ (tending to suppress them). When dissipation is too strong ($2\Gamma_2^2 > |\omega_i - \omega_j|^2$), the expression under the square root becomes negative and the resonance disappears — the response becomes **aperiodic** (monotonically decaying).

This division of channels into "oscillating" and "aperiodic" has potential significance for neuroscience: it predicts that different pairs of cognitive dimensions may have qualitatively different response dynamics to stimuli — some oscillate (which may correspond to rhythmic brain activity), others do not.

### 6.4 Full Susceptibility Matrix

:::tip Theorem 6.3 (Operational FDT) [T]
In the presence of an external field $h^{\text{ext}}$ the Gap response is determined by the full susceptibility matrix:

$$
\langle \delta\mathrm{Gap}(i,j) \rangle_{h} = \sum_{(k,l)} \chi_{(ij),(kl)}(\omega) \cdot h^{\text{ext}}_{kl}(\omega)
$$

where $\chi_{(ij),(kl)}$ connects the response of $\mathrm{Gap}(i,j)$ to perturbation in channel $(k,l)$.
:::

The full susceptibility matrix $\chi_{(ij),(kl)}$ is a $21 \times 21$ object describing **all possible** linear responses of the system. Diagonal elements are direct responses (perturbation of channel $(i,j)$ changes the same channel). Off-diagonal elements are cross-couplings: perturbation of one channel affects another. By the Onsager theorem (section 3), the susceptibility matrix is also symmetric under appropriate conditions, which radically limits the number of independent parameters.

---

## 7. Derivation of the Form of Regeneration [T] {#вариационный-вывод-регенерации}

:::tip Status: Theorem [T]
The form of the regenerative term $\mathcal{R}[\Gamma, E] = \kappa(\Gamma) \cdot (\rho_* - \Gamma) \cdot g_V(P)$ is **fully derived** from axioms A1–A5, primitivity of the linear part $\mathcal{L}_0$ [T], standard thermodynamics, and V-invariance. All components that were previously postulated [P] have received status [T].
:::

### 7.1 Result

The form of regeneration:

$$
\mathcal{R}[\Gamma, E] = \kappa(\Gamma) \cdot (\rho_* - \Gamma) \cdot g_V(P)
$$

is **derived** by three independent arguments from [Evolution → Derivation of the Form of Regeneration](/docs/core/dynamics/evolution#вывод-формы-регенерации):

| Component | Derivation method | Status |
|-----------|-------------------|:------:|
| $\kappa(\Gamma)$ | Adjunction $\mathcal{D}_\Omega \dashv \mathcal{R}$ | [T] |
| $\rho_*$ (unique target) | Primitivity of $\mathcal{L}_\Omega$ (Evans–Spon criterion) | [T] |
| $(\rho_* - \Gamma)$ (direction) | Uniqueness of CPTP replacement channel + Bures gradient descent | [T] |
| $g_V(P)$ (gate) | Landauer + V-preservation: $g_V = \mathrm{clamp}\!\bigl(\frac{P - P_{\mathrm{crit}}}{P_{\mathrm{opt}} - P_{\mathrm{crit}}}, 0, 1\bigr)$ | [T] |

Each component deserves a comment:

- **$\kappa(\Gamma)$** — regeneration rate, determined by the adjunction of functors "dissipation $\dashv$ restoration". The stronger the decoherence, the more intense the regenerative response — this is the "immune system" of consciousness.

- **$\rho_*$** — the unique stationary point to which the system tends. Uniqueness follows from primitivity of the linear part $\mathcal{L}_0$ — analogous to ergodicity in the theory of Markov chains.

- **$(\rho_* - \Gamma)$** — direction "toward the goal". That the direction of regeneration is exactly this is not a postulate, but a consequence of the uniqueness of the CPTP replacement channel and the fact that Bures gradient descent on the manifold of density matrices yields precisely this form.

- **$g_V(P)$** — the "gate" that activates regeneration only at $P > P_{\text{crit}}$. The Landauer limit forbids regeneration "from nothing": a minimal purity (information) is needed for the system to be able to restore itself.

### 7.2 Connection to the Variational Principle

The form $(\rho_* - \Gamma)$ coincides with **steepest descent** of the functional $V(\Gamma) = \frac{1}{2}d_B^2(\Gamma, \rho_*)$ in the unique monotone metric (Chentsov–Petz). The Onsager–Machlup functional upon linearisation near $\rho_*$ gives the same form — the derived regeneration **is** an extremal.

This is a remarkable result: regeneration derived from categorical arguments (adjunction of functors) coincides with the extremal found from purely metric considerations (Bures geometry). Two completely different paths lead to the same answer — a sign that the answer is likely correct.

### 7.3 Cascading Corollaries

| Corollary | Status |
|-----------|:------:|
| Evolution equation is fully axiomatic (all 3 terms [T]) | [T] |
| $\mathcal{L}_{\text{reg}}$ in [Lagrangian](./lagrangian#регенеративный-член) is justified | [T] |
| Viability dynamics is fully determined by the axioms | [T] |
| Connection to Prigogine: regeneration is a dissipative structure | [I] |

---

## 8. Summary Table of Variational Results {#сводная-таблица}

| Result | Status | Conditions | Reference |
|--------|--------|------------|-----------|
| Principle of stationary action | [T] | Generalised (with Rayleigh function) | Theorem 1.1 |
| Equations of motion for $\theta_{ij}$ | [T] | Full 4-term structure | Theorem 2.1 |
| Onsager relations | [C] | Linear regime, detailed balance | Theorem 3.2 |
| FEP as macroscopic limit | [T] | $\tau_{\mathrm{obs}} \gg 1/\Gamma_2$ (Dec [T]) | Theorem 4.1 |
| Minimum $\dot{\Sigma}$ | [C] | Linear regime | Theorem 5.1 |
| FDT for Gap | [T] | Stationarity | Theorem 6.1 |
| Form of regeneration ℛ | [T] | CPTP-uniqueness + Bures + Landauer | Section 7 |

---

## 9. Conclusion: Variational Architecture of Consciousness {#заключение}

Let us summarise. In this chapter we traced the path from Fermat to Gap dynamics and established the following picture:

1. **Principle of stationary action** (section 1) — the foundation: from the single functional $S_{\text{Gap}}$ all equations of motion for the coherence phases follow. Nature "chooses" not the optimal but the stationary path — the one insensitive to small perturbations.

2. **Four forces** (section 2) — the content: potential (structural harmony), regenerative (teleological directedness), dissipative (irreversibility), and external (openness) forces determine every moment of inner life. Their balance *is* the current state of consciousness.

3. **Irreversible thermodynamics** (section 3) — direction: Onsager relations establish a deep reciprocity of internal processes and guarantee that total opacity does not decrease spontaneously ($\dot{\Sigma} \geq 0$). Clarity of consciousness requires effort.

4. **FEP as a special case** (section 4) — the boundary: Friston's Free Energy Principle, one of the most influential theories in neuroscience, turns out to be the macroscopic limit of the Gap variational principle. This does not diminish FEP, but defines its domain of applicability.

5. **Minimum entropy production** (section 5) — economy: near equilibrium consciousness "chooses" the least wasteful configuration of opacity. Far from equilibrium dissipative structures are possible — the mathematical correlate of creativity.

6. **Fluctuation–dissipation theorem** (section 6) — information: spontaneous Gap oscillations are not noise but a source of information about the susceptibility of the system. Noise and response are determined by the same mechanism.

7. **Regeneration** (section 7) — closure: the form of the regenerative term is fully derived from the axioms, and it coincides with the extremal of the Bures functional. The circle closes: the variational principle generates forces, forces generate dynamics, dynamics generates stationary states, and stationary states *are* consciousness.

---

## What We Learned {#что-мы-узнали}

A summary of the key results of this chapter:

- **Principle of stationary action** ($\delta S_{\text{Gap}} = 0$) — the unified foundation of all phase dynamics. All equations of motion follow from a single functional (Theorem 1.1 [T]).
- **Four forces of inner life** — potential (structural harmony), regenerative (goal-directed homing by $\varphi$), dissipative (friction of forgetting), and external (the voice of the world) — exhaustively describe the right-hand side of the equations of motion (Theorem 2.1 [T]).
- **Onsager relations** establish a deep *reciprocity* among Gap channels: cross-influences are symmetric, $L_{(ij),(kl)} = L_{(kl),(ij)}$ (Theorem 3.2 [C]).
- **Second law for consciousness**: entropy production in the Gap sector is non-negative, $\dot{\Sigma} \geq 0$. Clarity of consciousness requires effort (Corollary 3.3 [T]).
- **Friston's FEP as a special case**: the Free Energy Principle is derived as the macroscopic limit ($\tau_{\text{obs}} \gg 1/\Gamma_2$) of the Gap variational principle (Theorem 4.1 [T]).
- **Opacity economy principle**: near the stationary state the Gap profile minimises entropy production — the system maintains exactly the level of opacity minimally required (Theorem 5.1 [C]).
- **Fluctuation–dissipation theorem**: spontaneous Gap oscillations and response to an external field are determined by the same mechanism — noise is a source of information (Theorem 6.1 [T]).
- **Regeneration fully derived**: the form $\mathcal{R}[\Gamma, E] = \kappa(\Gamma) \cdot (\rho_* - \Gamma) \cdot g_V(P)$ follows from three independent arguments and coincides with the extremal of the Bures functional (section 7 [T]).

---

### Bridge to the Next Chapter

The variational principle gave us the equations of motion and the thermodynamic structure, but one parameter remained mysterious: the **effective temperature** $T_{\text{eff}}$. We saw that it enters the FDT, determines the scale of fluctuations, and differs from the physical temperature of the body. But what does it represent? How can it be measured? And what happens when it reaches the critical value $T_c$?

In the [next chapter](./effective-temperature) we will answer these questions: define $T_{\text{eff}}$ as the "fever of the mind", derive the critical temperature of the phase transition, construct the Fisher metric on the space of Gap profiles, and show that the coordinates $(t, r)$ define the full phase diagram of consciousness.

---

## Related Documents

- [Lagrangian of Gap theory](./lagrangian) — full 6-term Lagrangian, potential $V_{\text{Gap}}$, symmetries
- [Effective temperature](./effective-temperature) — $T_{\text{eff}}$, phase transition, Fisher metric
- [Derivation of FEP from UHM](/docs/proofs/dynamics/fep-derivation) — rigorous proof of equivalence of the two definitions of $\varphi$
- [Gap thermodynamics](/docs/core/dynamics/gap-thermodynamics) — FDT, Landauer bound, $T_{\text{eff}}$, full Lagrangian
- [Evolution](/docs/core/dynamics/evolution) — equation $d\Gamma(\tau)/d\tau$, variational derivation of regeneration
- [Gap phase diagram](/docs/core/dynamics/gap-phase-diagram) — stationary regimes, bifurcations, catastrophes
- [Gap semantics](/docs/physics/dual-aspect/gap-semantics) — definition of $\mathrm{Gap}(i,j)$, dual-aspect interpretation
- [CC axiomatics](./axiomatics) — categorical foundations, L-unification
- [Definitions](./definitions) — key measures ($P$, $\Phi$, $R$, $\mathrm{Coh}_E$)
- [Comparison with alternatives](./comparison) — CC vs. FEP: variational bridge
- [Exercises](./exercises) — problems on variational principles (block 2)
