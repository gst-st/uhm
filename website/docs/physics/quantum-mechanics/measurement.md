---
sidebar_position: 2
title: "Quantum Measurement"
description: "Quantum instruments, the Born pairing, dephasing and the operational cost of feedback."
---

# Quantum Measurement in UHM

Predicting a recorded outcome requires a preparation, an instrument with labelled outcomes and a probability rule. Here those inputs come from finite-dimensional quantum mechanics. A device that resolves two preparations defines a distinction the observer can actually use. For example, the controlled gate in the two-rebit experiment exposes a distinction invisible to all local record histories. [Two-rebit experiment](/docs/physics/quantum-mechanics/qm-reduction#72-что-реконструкции-значат-для-угм) · [Operational records](/docs/core/foundations/operational-processes#process)

## 1. Statement of the Measurement Problem {#1-постановка-проблемы}

### 1.1 The Standard Problem

In standard quantum mechanics, the **measurement problem** consists of three interrelated questions:

1. **The reduction problem:** Why does the state $|\psi\rangle = \sum_k c_k |a_k\rangle$ "collapse" to a specific $|a_k\rangle$ upon measurement?
2. **The probability problem (Born rule):** Why is the probability of outcome $k$ equal to $p_k = |c_k|^2$?
3. **The preferred basis problem:** What determines the basis $\{|a_k\rangle\}$ in which "reduction" occurs?

## 2. The specified measurement instrument {#2-измерение-из-omega}

A subobject $S\hookrightarrow X$ in a topos has a characteristic arrow $\chi_S:X\to\Omega$. A Hilbert-space instrument is a family of completely positive operations whose sum preserves trace. Identifying an arrow with the operation $\Gamma\mapsto P_k\Gamma P_k$ requires a representation and a choice of instrument. Even a fixed observable allows different state updates.

**Lüders instrument.** Choose mutually orthogonal projectors with $\sum_k P_k=I$. Then the operation, probability and conditional state for the recorded outcome $k$ are

$$
\mathcal I_k(\Gamma)=P_k\Gamma P_k,\qquad
p_k=\operatorname{Tr}(P_k\Gamma),\qquad
\Gamma_k=\frac{\mathcal I_k(\Gamma)}{p_k}\quad(p_k>0).
$$

Cyclicity of the trace and $P_k^2=P_k$ give $\mathrm{Tr}\,\mathcal I_k(\Gamma)=p_k$. Replacing $\mathcal I_k$ by $U_k\mathcal I_k(\,\cdot\,)U_k^\dagger$ leaves these probabilities unchanged and can change the conditional states. Summing the operations describes discarding the outcome record.

## 3. The Born rule {#3-правило-борна}

The trace pairing is the probability postulate used here. Positivity and completeness of the projectors give $p_k\ge0$ and $\sum_kp_k=1$. For a pure state and $P_k=|a_k\rangle\langle a_k|$ this gives $|\langle a_k|\psi\rangle|^2$. Gleason’s theorem starts with a normalized, noncontextual, orthogonally additive probability assignment on the projectors of a complex Hilbert space of finite dimension at least three. Each such assignment has a unique representing density operator. Identifying the projectors with available tests and the representing operator with the preparation are physical premises. The topology of the state space supplies neither measurement frequencies nor the trace pairing.

## 4. Connection to Self-Observation ($\varphi$-Operator) {#4-связь-с-самонаблюдением}

Given Kraus operators with $\sum_m K_m^\dagger K_m=I$, the channel $\varphi(\Gamma)=\sum_m K_m\Gamma K_m^\dagger$ describes evolution averaged over the labels. Monitoring a specified Kraus realization yields an instrument. For example, discarding a fair random choice of $I$ or $Z$ gives the same qubit dephasing channel as measuring $Z$ and discarding its outcome. The fair coin and the measurement have different records. Interpreting a monitored channel as self-observation requires a physically accessible record and a way to test what it reports. [Self-observation](/docs/consciousness/foundations/self-observation)

## 5. Decoherence {#5-декогеренция}

Take a purely dissipative GKSL generator with real diagonal $L_m=\mathrm{diag}(\ell_{m1},\ldots,\ell_{mN})$ and constant rates $\gamma_m\ge0$. Direct substitution gives

$$
\Gamma_{ij}(t)=\Gamma_{ij}(0)e^{-r_{ij}t},\qquad
r_{ij}=\tfrac12\sum_m\gamma_m(\ell_{mi}-\ell_{mj})^2.
$$

The populations stay fixed. A coherence decays exactly when at least one positive-rate operator distinguishes its two indices. If every pair is distinguished, the limiting state is the diagonal mixture. A single outcome requires a recorded instrument. This dephasing semigroup is unital, so $D(\Gamma(t)\|I/N)=\log N-S(\Gamma(t))$ cannot increase. A reset to a pure state shows why the entropy conclusion cannot be extended to all CPTP channels. [Entropy and time](/docs/proofs/dynamics/emergent-time#7-теорема-о-стреле-времени)

## 6. Preferred Basis Problem {#6-предпочтительный-базис}

For the specified dephasing generator the fixed algebra consists of blocks indexed by the joint eigenvalue lists of the positive-rate $L_m$. Rank-one blocks select pointer rays up to phases and permutations. Conjugating every $L_m$ rotates the fixed algebra. A noncommuting Hamiltonian can also move a diagonal state out of it. An experiment must calibrate which rays the actual coupling preserves.

## 7. Measurement and regeneration {#7-живые-системы}

For a selected target $\sigma$ and fixed rate, the replacement channel below gives a controlled example of feedback towards a target. Applying this description to an organism requires an independent measurement of the target, rate and response.

<a id="73-self-consistency-condition"></a>

### 7.3 Self-consistency of a specified map

:::tip Theorem 7.1: fixed replacement channel [T under fixed parameters]
Fix $\sigma\in D_7$ and $0<k\le1$ independently of the input. The linear operator map

$$
T_{k,\sigma}(X)=(1-k)X+k\operatorname{Tr}(X)\sigma
$$

is CPTP and has the unique fixed state $\Gamma^*=\sigma$. On states, the fixed-point equation reduces to $k(\sigma-\Gamma)=0$. Moreover

$$
T_{k,\sigma}^n(\Gamma)=\sigma+(1-k)^n(\Gamma-\sigma),\qquad
\|T_{k,\sigma}(\Gamma)-T_{k,\sigma}(\eta)\|_F=(1-k)\|\Gamma-\eta\|_F.
$$

The fixed target $\sigma$ and weight $k$ are independent of the input. If a controller instead estimates them from measurements on each preparation, its data, update and resource costs become part of the experiment.
:::

## 8. No-Signaling {#8-запрет-сигнализации}

Let a fixed local channel $\Phi_A$ be CPTP and act as $\Phi_A\otimes{\rm id}_B$ on a jointly prepared state. Completeness of its Kraus operators gives the marginal identity

$$
\operatorname{Tr}_A[(\Phi_A\otimes{\rm id}_B)(\Gamma_{AB})]
=\operatorname{Tr}_A\Gamma_{AB}.
$$

Multiplying the difference by a scalar depending on the current marginal leaves its partial trace zero. This tests the unconditioned marginal in the stipulated joint update. For a nonlinear map $F$ the preparations $\sum_k p_kF(\rho_k)$ and $F(\sum_k p_k\rho_k)$ can disagree. A physical extension must specify which records are retained, how mixed preparations compose, and what inputs the apparatus receives. The marginal identity alone does not prove no-signalling for arbitrary adaptive protocols. [Joint update](/docs/proofs/physics/physics-correspondence#88-прочтение-вынуждено) · [Ensemble test](/docs/proofs/physics/physics-correspondence#85-ансамблевая-независимость)

G4 gives a sharper resource statement for the canonical feedback ray with known target direction. For $d\ge3$ and fixed $0\le\mu<1$, the exact output conditioned on success needs three or four independent preparations per attempt, depending on $\mu$. No deterministic exact implementation with a finite input bound exists on the whole ray. A computational-speedup claim would also have to count repreparations, success probability, precision and readout. [Proof and assumptions](https://github.com/gst-st/uhm/blob/main/website/research/operational-reconstruction/feedback.md)

**Related models and definitions**

- [Seven-level quantum model](/docs/physics/quantum-mechanics/qm-reduction)
- [Physics Correspondence](/docs/proofs/physics/physics-correspondence)
- [Axiom Ω⁷](/docs/core/foundations/axiom-omega)
- [Evolution of Γ](/docs/core/dynamics/evolution)
- [Self-Observation](/docs/consciousness/foundations/self-observation)
- [Emergent Time](/docs/proofs/dynamics/emergent-time)
- [Dimension L](/docs/core/structure/dimension-l)
- [Critical Purity](/docs/proofs/dynamics/theorem-purity-critical)
- [Physics — Overview](/docs/physics/overview)
