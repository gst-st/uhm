---
sidebar_position: 3
title: "Attention and Memory"
description: "Attention control, temporal kernels and recall: conditional mathematics and testable cognitive hypotheses"
slug: /consciousness/states/attention-memory
---

# Attention and Memory

[The Unconscious](/docs/consciousness/states/unconscious) separates phase statistics from access to content. This chapter proposes models of attention and memory; the correspondence to cognitive processes is an empirical hypothesis **[H]**.

:::note Typed quantities
$\Gamma\in\mathcal D(\mathbb C^7)$ is a density matrix in a declared native frame, $P=\mathrm{Tr}(\Gamma^2)$ and $\Phi=P/\sum_i\gamma_{ii}^2-1$. Trace normalization constrains populations and bounds coherences, but does not conserve an attention resource or personal identity. For $\gamma_{ij}\ne0$, $\mathrm{Gap}(i,j)=|\sin\arg\gamma_{ij}|$ is a phase statistic; at zero coherence the phase is undefined. A memory kernel describes dependence of an evolution equation on earlier states. It is not a stored memory or a recall score by definition.
:::

:::warning Scope
Matrix inequalities below are **[T]**. Chosen control objectives and kernel families are **[D]**; their identification with attention, recall and phenomenology — including all historical correspondences in §§1 and 3 — are modelling proposals **[H]**/**[I]** that do not follow from the cited psychological findings or from trace normalization, and require an observation model and task validation. Neither $P$, $\Phi$, Gap nor a fixed-point score alone determines physical consciousness, clinical condition or treatment efficacy. See the [mathematical kernel](/docs/reference/mathematical-kernel).
:::

### Chapter roadmap

Historical models; constrained coherence control; operational tests of attention; kernel families; recoverability and forgetting; interaction with memory.

## 1. Historical perspective: attention {#история-внимание}

### 1.1 William James (1890)

> "Everyone knows what attention is. It is the taking possession by the mind, in clear and vivid form, of one out of what seem several simultaneously possible objects or trains of thought."
>
> — William James, *The Principles of Psychology* (1890), ch. 11

James's description motivates a selective-control model **[I]**/**[H]**. Increasing a chosen coherence relative to others is a possible objective; the transfer of a conserved budget requires an additional controller law, not the historical description or trace normalization.

### 1.2 Filter models (1950–1970s)

:::note Typing multi-target attention: native 7D versus extended $\mathcal{H}_E$
In the native $7\times 7$ matrix $\Gamma \in \mathcal{D}(\mathbb{C}^7)$, the basis axis $E$ is one-dimensional, so $\gamma_{AE}$ is a **single** complex entry and cannot carry multiple stimulus indices. Modelling target-versus-distractor selection or shifting attention between distinct experiential contents ($e_1 \to e_2$) requires declaring an **extended experiential register** $\mathcal{H}_E$ (with orthonormal channel/content basis states $|e_{\mathrm{target}}\rangle, |e_{\mathrm{distr}}\rangle$ or $|e_1\rangle, |e_2\rangle \in \mathcal{H}_E$, giving extended couplings $\Gamma^{\mathrm{ext}}_{A,e_{\mathrm{target}}}$, $\Gamma^{\mathrm{ext}}_{A,e_{\mathrm{distr}}}$, $\Gamma^{\mathrm{ext}}_{A,e_1}$, $\Gamma^{\mathrm{ext}}_{A,e_2}$; see [7D/42D typing](/docs/core/structure/dimension-e#rho-e-7d-42d)), whereas native 7D comparisons operate across distinct native axes $X \in \{S, D, L, E, O, U\}$.
:::

**Broadbent (1958): early selection filter.** Information passes through a narrow 'bottleneck' — only one channel is fully processed, the rest are blocked. In an extended-register model: $|\Gamma^{\mathrm{ext}}_{A,e_{\text{target}}}| \gg |\Gamma^{\mathrm{ext}}_{A,e_{\text{distr}}}|$ — hard filtering.

**Treisman (1964): attenuation model.** Non-target channels are not fully blocked but *attenuated*. In an extended-register model: $|\Gamma^{\mathrm{ext}}_{A,e_{\text{distr}}}| > 0$, with $|\Gamma^{\mathrm{ext}}_{A,e_{\text{distr}}}| \ll |\Gamma^{\mathrm{ext}}_{A,e_{\text{target}}}|$ — soft filtering. Its proposed matrix counterpart requires an independently tested access/response readout **[H]**.

**Deutsch and Deutsch (1963): late selection filter.** All information is fully processed; selection occurs at the response stage. In the native 7D representation: all $|\gamma_{AX}|$ are moderate; selection occurs via channel $(A,D)$ — attention modulates *action* ($D$) rather than early *perception* ($E$).

### 1.3 Posner: components of attention (1980–1990s)

Michael Posner identified three neural 'attention networks':
- **Alerting** (vigilance) — maintenance of the tonic native population $\gamma_{AA}$
- **Orienting** (orientation) — redirecting coherence across states of an extended experiential register $\mathcal{H}_E$: $\Gamma^{\mathrm{ext}}_{A,e_1} \to \Gamma^{\mathrm{ext}}_{A,e_2}$
- **Executive** (executive control) — resolving conflict between competing channels

Mapping these networks to A-sector or extended-register features is a candidate hypothesis **[H]**; naming a matrix entry does not establish its neural implementation.

### 1.4 From classical models to UHM

| Classical model | Proposed UHM counterpart (native 7D or extended $\mathcal{H}_E$) |
|---------------------|---------------|
| Broadbent's filter | Extended $\mathcal{H}_E$: $\|\Gamma^{\mathrm{ext}}_{A,e_{\text{target}}}\| \gg 0$, $\|\Gamma^{\mathrm{ext}}_{A,e_{\text{distr}}}\| \approx 0$ |
| Treisman's attenuation | Extended $\mathcal{H}_E$: $\|\Gamma^{\mathrm{ext}}_{A,e_{\text{target}}}\| > \|\Gamma^{\mathrm{ext}}_{A,e_{\text{distr}}}\| > 0$ |
| Late selection | Native 7D: all $\|\gamma_{AX}\|$ moderate; selection via $(A,D)$ |
| Alerting (Posner) | Native 7D: $\gamma_{AA}$ — tonic level |
| Orienting (Posner) | Extended $\mathcal{H}_E$: $\Gamma^{\mathrm{ext}}_{A,e_1} \to \Gamma^{\mathrm{ext}}_{A,e_2}$ — redistribution |
| Executive (Posner) | Native 7D or extended: resolution of $\|\gamma_{AX_1}\| \stackrel{?}{>} \|\gamma_{AX_2}\|$ ($X_1 \neq X_2$) |

---

## 2. Attention as redistribution of coherence {#внимание}

### 2.1 Definition

**Definition [D].** A candidate attention controller changes selected A-sector entries toward a declared task objective. Selectivity can be represented by increasing $|\gamma_{AX}|$ relative to declared distractor entries, sustained control by maintaining a target over an interval, and divided control by several simultaneous targets. These are alternative objectives, not consequences of normalization. An empirical attention measure must specify the task, stimulus, response and independent performance readout **[H/Pr]**. Unitary control is one model choice; general open-system control need not be unitary.

### 2.2 The 'spotlight' mechanism: detailed derivation

**Theorem [T].** Positivity of each $2\times2$ principal minor gives $|\gamma_{AX}|^2\le\gamma_{AA}\gamma_{XX}$. Summing and using trace one yields

$$
\sum_{X\ne A}|\gamma_{AX}|^2\le\gamma_{AA}(1-\gamma_{AA}).
$$

This is an upper bound, not a fixed sum. The former inference “one coherence rises, another must fall” is false when the bound has slack.

**Counterexample in the proof.** Let $u=(1,\ldots,1)/\sqrt7$ and

$$
\Gamma(t)=(1-t)I_7/7+tuu^\dagger,\qquad 0\le t\le1.
$$

These states are positive and trace one. Every diagonal is $1/7$, every off-diagonal modulus is $t/7$, and $P=(1+6t^2)/7$. All six A-sector moduli can increase together while the trace and diagonal populations stay fixed.

A spotlight tradeoff follows **conditionally** if an additional controller enforces the fixed budget $B_A=\sum_{X\ne A}|\gamma_{AX}|^2$. Then $d|\gamma_{AX}|^2/d\tau>0$ implies $\sum_{Y\ne A,X}d|\gamma_{AY}|^2/d\tau<0$. This conservation is an extra dynamical hypothesis **[D/H]**, to be tested rather than derived from $\mathrm{Tr}\Gamma=1$.

### 2.3 Connection to the [21-pair taxonomy of qualia](/docs/consciousness/phenomenology/qualia-structure#таксономия)

The proposed names apperception $(A,E)$, morphogenesis $(A,S)$, actualisation $(A,D)$ and predication $(A,L)$ belong to the linked interpretive taxonomy **[I]**. Matrix indices alone do not establish these cognitive functions. Test a proposed mapping by independently manipulating task demands and estimating the corresponding entries with a fixed observation model; include competing mappings and held-out tasks **[Pr]**.

### 2.4 Types of attention

The three labels selective, sustained and divided attention are a chosen taxonomy **[D/H]**. Sustained control may impose $|\gamma_{AX}(\tau)|\ge\theta$ on a declared interval; selective control may maximize a target-to-distractor ratio. Neither objective establishes energetic cost, fatigue, a neural network identity or a universal performance loss.

The ratio $|\gamma_{AX}|^2/\sum_{Y\ne A,X}|\gamma_{AY}|^2$ is a matrix contrast **[D]** when its denominator is positive. Calling it an SNR requires an observation model in which the denominator actually measures noise power. A zero denominator requires separate handling. Positivity must be checked for the full matrix; specifying a few entries below their individual bounds is not sufficient.

### 2.5 Attention and Gap

**Theorem [T].** In polar coordinates $\gamma_{ij}=r_{ij}e^{i\theta_{ij}}$, $r_{ij}>0$,

$$
\mathrm{Gap}(i,j)=|\sin\theta_{ij}|,\qquad
\left.\frac{\partial\mathrm{Gap}(i,j)}{\partial r_{ij}}\right|_{\theta_{ij}}=0.
$$

**Counterexample to automatic Gap reduction.** Varying $r$ in $re^{i\theta}$ at fixed phase changes amplitude but leaves Gap unchanged. The family in §2.2 changes all amplitudes while every defined pairwise Gap remains zero. Cross-channel derivatives have no sign without a specified coupled evolution. Even along a flow, where the derivative exists, $\dot G_{ij}=\operatorname{sgn}(\sin\theta_{ij})\cos\theta_{ij}\dot\theta_{ij}$ depends on phase velocity.

Attention training could affect phase, access or model prediction through an independently specified controller **[H]**. The proposed test compares task performance, amplitude and oriented phase before and after the intervention; it does not equate a decrease of this phase statistic with awareness or clinical benefit **[Pr]**.

## 3. Historical perspective: memory {#история-память}

### 3.1 Hermann Ebbinghaus (1885)

Ebbinghaus was the first researcher to apply the experimental method to the study of memory. His main discoveries:

- **Forgetting curve**: retention was studied across delays. A particular power-law fit and its exponent require the measured retention data; neither is fixed by the kernel formalism.
- **Learning curve**: repetition improves retention, but with diminishing returns.
- **Spacing effect**: distributed repetition is more effective than massed practice.

In UHM, a power-law retention fit is a candidate hypothesis **[H]**; §4.5 does not derive its exponent from the kernel alone.

### 3.2 Atkinson and Shiffrin (1968): modal model

The 'three-store' model:
- **Sensory register** — instantaneous snapshot (duration ~250 ms)
- **Short-term (working) memory** — 7 ± 2 items, duration ~20 s
- **Long-term memory** — virtually unlimited capacity and duration

A proposed UHM comparison assigns different kernel families to these stores **[H]**; it does not show that their distinct mechanisms reduce to one kernel:

| Atkinson-Shiffrin model | UHM formalism |
|---------------------------|---------------|
| Sensory register | $K(\tau) \sim \delta(\tau)$ — Markovian limit |
| Working memory | $K(\tau) \sim e^{-\tau/\tau_{WM}}$ — exponential kernel |
| Long-term memory | $K(\tau) \sim \tau^{-\alpha}$ — power-law kernel |

### 3.3 Tulving (1972): types of memory

Endel Tulving introduced the distinction:
- **Episodic memory** — memory of specific events ('I was at the café yesterday')
- **Semantic memory** — knowledge of facts ('Paris is the capital of France')
- **Procedural memory** — skills ('how to ride a bicycle')

In UHM:
- Different fitted retention functions could model episodic and semantic tasks **[H]**; no unique kernel exponent is derived.
- Learned generator parameters are a candidate model of skill retention **[H]**, with the limitations in §4.6.

---

## 4. Types of memory from the non-Markovian kernel {#память}

A temporal kernel and cognitive memory have different types. The former belongs to an evolution law; the latter requires encoded information and a recall task. The following families are candidate models **[D/H]**, not a theorem deriving four cognitive stores.

### 4.1 The memory kernel and cognitive memory

A candidate equation is $\dot z(\tau)=\int_0^\tau K(\tau-s)z(s)\,ds+f(\tau)$. The kernel has units of inverse time squared for dimensionless $z$. In a matrix model, a scalar kernel per entry does not by itself ensure positivity, trace preservation or complete positivity of the evolution. Those conditions must be established for the whole map. A nonzero history kernel alone does not show that task-relevant information can be recalled; a Markovian dynamical system may carry records in its state.

### 4.2 Memory typology

| Candidate family [D] | Mathematical property | Cognitive bridge [H] |
|---|---|---|
| Delta kernel | Local evolution law | Short persistence on a sensory task |
| Exponential kernel | Finite kernel timescale | A fitted working-memory task |
| Power-law kernel | Long temporal tail | A fitted long-retention task |
| Learned generator parameters | Persistent change of evolution law | Skill learning |

The temporal form, observed retention curve and psychological category must be estimated separately. None of the families fixes a universal human timescale or a memory capacity.

### 4.3 Sensory memory

Under a one-sided delta convention, $K=-\lambda\delta$, $\lambda>0$, gives $\dot z=-\lambda z$ and $z(\tau)=z(0)e^{-\lambda\tau}$ **[T]**. Its half-life is $\log2/\lambda$, not zero. The delta kernel removes dependence on earlier values from the evolution law; it does not remove stored information instantaneously. Identification with sensory retention requires an independent task readout **[H]**.

### 4.4 Working memory

For the scalar model $K(\tau)=-c e^{-\omega_c\tau}$, $c,\omega_c>0$, with no forcing and $z(0)=z_0$, differentiation of the convolution equation gives

$$
\ddot z+\omega_c\dot z+cz=0,\qquad\dot z(0)=0.
$$

Oscillations occur only if $c>\omega_c^2/4$. Then, with $\Omega=\sqrt{c-\omega_c^2/4}$,

$$
z(\tau)=z_0e^{-\omega_c\tau/2}
\left(\cos\Omega\tau+\frac{\omega_c}{2\Omega}\sin\Omega\tau\right).
$$

**Proof and counterexample to universal refresh oscillations [T].** Introduce $y=\int_0^\tau e^{-\omega_c(\tau-s)}z(s)ds$; $\dot z=-cy$ and $\dot y=z-\omega_c y$ imply the second-order equation. At $c<\omega_c^2/4$ its two characteristic roots are real; an exponential memory kernel therefore need not produce oscillations. $\Omega$ is an angular frequency; the cycle count in duration $T$ is $\Omega T/(2\pi)$, not $\Omega T$. A neural rehearsal frequency or retained item count does not follow from these roots **[H]**.

### 4.5 Long-term memory

A power-law kernel does not determine a retention exponent by itself. For the explicit scalar equation $\dot z=K*z$, $K(\tau)=-c\tau^{-\alpha}/\Gamma_{\!\mathrm{Euler}}(1-\alpha)$, $0<\alpha<1$, with $c$ in units of time$^{\alpha-2}$, its Laplace transform satisfies

$$
(s+c s^{\alpha-1})\widehat z(s)=z_0,\qquad
\widehat z(s)=\frac{z_0s^{1-\alpha}}{s^{2-\alpha}+c}.
$$

**Correction of the former proof.** The initial term $z_0$ cannot be dropped from $s\widehat z-z_0=\widehat K\widehat z$. The displayed resolvent does not justify the claimed universal exponent $\beta=\alpha/2$; no step permits replacing one inverse transform by that power. Generator terms, initial conditions and the recall readout change the retention law.

A candidate empirical retention fit is $b(\tau)=b_0(1+\tau/\tau_0)^{-\beta}$ **[D/H]**. Its exponent and timescale must be fitted and compared with alternatives. A nonzero long tail of a dynamical quantity alone does not establish readable autobiographical content, permanent storage or identity preservation.

### 4.6 Procedural memory

Learned parameters of $H_{\mathrm{eff}}$ or of an open-system generator may encode a persistent change of policy **[D/H]**. This does not give a canonical embedding $K\hookrightarrow H_{\mathrm{eff}}$: kernels and Hamiltonians have different types and units. Persistence requires an evolution law for the parameters and a performance test. Parameters may drift or be overwritten; being stored in a generator does not prove a skill is never forgotten.

## 5. Forgetting as kernel decoherence {#забывание}

Operational forgetting is a decline of performance on a declared recall task **[D]**. It may be modeled through changing dynamics, stored records or access. Decay of a history kernel is one candidate mechanism **[H]**, not an equivalent definition.

### 5.1 Two mechanisms of forgetting

Recoverability depends on the encoding, channel and allowed decoder. A channel can erase a record while preserving trace one; another can preserve a record while a particular decoder fails to access it. Thus loss of a record and loss of access are distinct, but neither is identified by Gap or $K$ alone.

**Counterexamples.** A Markovian identity channel preserves all encoded states without a history kernel. A replacement channel maps every input to the same trace-one state and destroys distinguishability of the records at its output. Conversely, an invertible phase rotation changes Gap yet permits exact recovery by its inverse. These examples invalidate “$K$ decay = irreversible information loss” and “Gap increase = intact recoverable memory”. Recovery from an environment is a separate question requiring access to that environment.

### 5.2 Forgetting rate and viability

**Conditional result [T].** Suppose a positive differentiable scalar kernel amplitude $k=|K|$ is nonincreasing and, as an additional model assumption, satisfies

$$
\dot k\ge-\frac{\kappa}{P-P_{\mathrm{crit}}}k,
\qquad P>P_{\mathrm{crit}},\quad\kappa\ge0.
$$

Dividing by $k$ and changing the sign gives an **upper** bound on the nonnegative forgetting rate:

$$
0\le r:=-\dot k/k\le\frac{\kappa}{P-P_{\mathrm{crit}}}.
$$

**Counterexample in the proof.** The constant kernel amplitude $k(\tau)=k_0>0$ has $r=0$ and satisfies the inequality for every allowed $P$. Letting $P$ approach the cutoff makes the upper bound weaker; it does not force $r$ to diverge. Non-Markovianity does not imply the assumed inequality either.

The equality $r=\kappa/(P-P_{\mathrm{crit}})$ would be an extra constitutive law **[D/H]**, valid only on an explicitly declared domain, with a separate model at its singular boundary. Neither this law nor the bound identifies dementia stages, a person's survival or loss of identity. Those claims and the former clinical numerical table are withdrawn.

## 6. Integration: attention, memory and Gap {#интеграция}

Attention control, stored records, temporal dependence and phase statistics can interact in a specified model. No universal cycle attention → Gap reduction → awareness → permanent memory follows from the definitions.

### 6.1 Interaction of attention and memory

A testable joint model specifies an encoding $x\mapsto\Gamma_x$, an attention controller, the state evolution, a recall decoder and a task score. Compare changes in that score with estimated amplitudes, oriented phases and kernel parameters on held-out data **[Pr]**. Improvements in a surrogate statistic cannot substitute for an improvement in recall or an independently assessed intervention outcome.

### 6.2 State-dependent memory indexing in agent architectures [Pr] {#настроение-как-адрес}

Empirical psychology documents **state-dependent recall**: material learned in one physiological or affective context is often retrieved more reliably in a matching context (e.g., Godden & Baddeley, 1975). In continual-learning and agent architectures, this motivates **context-indexed memory** as a prospective design pattern **[Pr]** for mitigating catastrophic interference across alternating task regimes ($A \to B \to A$): partitioning policy or transition tables by an internal state key trades cross-context transfer for protection against overwriting.

Within a seven-axis Fano-structured state space, two elementary structural facts **[T]** constrain how such a context key can be chosen:

1. **Point versus line indexing.** Because each of the seven Fano points lies on three distinct Fano lines, indexing memory solely by a single dominant axis is structurally ambiguous with respect to the seven triad blocks, whereas any two distinct axes uniquely determine a single Fano line. Comparing single-axis indexing, Fano-line indexing, and explicit change-detection resets on controlled interference benchmarks (separating transition-model storage from action-policy storage) is a testable engineering protocol **[Pr]**.
2. **Real-valued inputs versus oriented-cycle phase.** Each Fano line admits two opposite cyclic orientations (corresponding to the sign of the oriented triple product $e_i e_j = \pm e_k$ in the chosen octonionic convention). However, purely real-valued encodings carry zero relative phase; using triangle holonomy phase as an address bit requires an observation or input channel that encodes complex phase information above the declared carrier-amplitude floor, together with a specified non-equilibrium dynamical readout.

All architectural performance claims (interference reduction, return-switch accuracy, and phase-sensitivity thresholds) require published benchmarks, explicit baselines, and independent empirical testing before any biological analogy is drawn **[H]**/**[Pr]**.

---

### What we learned {#итоги}

1. Positivity and trace one give an upper bound on A-sector coherence; a conserved attention budget requires an extra controller assumption.
2. At fixed phase, increasing coherence amplitude leaves phase Gap unchanged. Access and task performance require independent readouts.
3. Delta, exponential and power-law kernels describe temporal dependence, not a uniquely derived taxonomy of cognitive memory. Exponential kernels oscillate only in their underdamped parameter regime.
4. Forgetting is assessed by recall performance and recoverability of an encoding. Trace one, nonzero coherence and a long kernel tail do not prove preservation of memories or personal identity.
5. The proposed purity-dependent inequality bounds the decay rate from above; its constant-kernel counterexample rules out the claimed mandatory divergence.
6. Context-indexed memory in §6.2 is a prospective architectural protocol **[Pr]** constrained by Fano incidence and phase-encoding prerequisites; biological and clinical interpretations remain research hypotheses.

## Connections

- **Coherence matrix:** [Definition of Γ](/docs/core/dynamics/coherence-matrix) — A-sector coherences
- **Evolution:** [Equations of motion](/docs/core/dynamics/evolution) — full equation for $\gamma_{ij}(\tau)$
- **Non-Markovian dynamics:** [Memory kernel](/docs/applied/coherence-cybernetics/non-markovian) — forms of $K(\tau)$
- **Gap-dynamics:** [Non-Markovian oscillations](/docs/core/dynamics/gap-dynamics#немарковские-эффекты) — Gap oscillations
- **Qualia:** [21-pair taxonomy](/docs/consciousness/phenomenology/qualia-structure) — qualia types associated with the A-dimension
- **Unconscious:** [Gap-structure of the unconscious](/docs/consciousness/states/unconscious) — connection between forgetting and the unconscious
- **ASC:** [Meditation and attention](/docs/consciousness/states/altered-states#медитация) — meditation and attention protocols
- **CC Theorems:** [Coherence Cybernetics](/docs/applied/coherence-cybernetics/theorems) — T-103 (purity flux; hedonic interpretation [I]) and T-104 (Hilbert–Schmidt/Bures stability radii)
