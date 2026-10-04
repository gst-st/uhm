---
sidebar_position: 2
title: "The Unconscious: Models and Identifiability"
description: "Separate phase, self-model readout error and experimentally inaccessible content; corrected Hamming scope"
slug: /consciousness/states/unconscious
---

# The Unconscious: Models and Identifiability

Nonconscious processing, inaccurate self-prediction and a complex matrix phase are different notions. Their identification needs a measurement and phenomenal bridge **[H/I]**. Following the [typed kernel](/docs/reference/mathematical-kernel), this page defines a possible mathematical detector and states precisely what it does and does not establish.

## 1. Interpretive context {#история}

Psychoanalytic repression, Jungian shadow and cognitive implicit processing concern different theoretical and experimental constructs. UHM may propose mappings of these constructs to selected matrix channels **[I/H]**, but naming seven axes does not validate the mappings. The former numerical examples of patients, therapy timelines and fixed organism-level channel counts were illustrations without independent reconstruction and are withdrawn as measured or necessary claims.

## 2. A typed candidate detector {#определение}

Supply an actual state $\Gamma$, a numerical self-model $M(\Gamma)\in\mathcal D(\mathbb C^7)$, a fixed frame, amplitude threshold $\eta>0$, and calibrated thresholds $g_0,r_0$. On detected channels define

$$
g_{ij}=\frac{|\operatorname{Im}\gamma_{ij}|}{|\gamma_{ij}|},\quad
r_{ij}=1-\frac{|\gamma_{ij}-M(\Gamma)_{ij}|^2}{|\gamma_{ij}|^2},
$$

and optionally

$$
\mathcal U_{\mathrm{score}}:=\{(i,j):i<j,|\gamma_{ij}|\ge\eta,\ g_{ij}\ge g_0,\ r_{ij}<r_0\}.
$$

This is a detector **[D]** of supported high phase and poor channel reproduction. $r_{ij}$ can be negative and is not a posterior probability; zero coherence makes its ratio undefined. Neither $r_0=1/3$ nor specific phase bands follows from a count of three dynamical summands. Canonical $R=1/(7P)$ and this readout score are different statistics.

**Channel readout identity [T].** With $\delta_{ij}=\gamma_{ij}-M(\Gamma)_{ij}$, the measurement on $(|i\rangle+e^{i\phi}|j\rangle)/\sqrt2$ changes its “plus” probability by $\operatorname{Re}(e^{i\phi}\delta_{ij})$ if the compared diagonal terms coincide. Hence the maximal absolute change over $\phi$ is $|\delta_{ij}|=|\gamma_{ij}|\sqrt{1-r_{ij}}$. Without matching diagonals, their half-sum difference must also be included. This is a measurement-error identity, not a Bayesian or consciousness threshold theorem.

**Independence counterexamples [T].** A state $I/7$ with only $\gamma_{12}=i\epsilon$ and its conjugate is positive for $0<\epsilon<1/7$; it has $g_{12}=1$ but an identity self-model gives $r_{12}=1$. Conversely, positive real $\Gamma(t)=(1-t)I/7+tuu^\dagger$, $u=(1,\ldots,1)/\sqrt7$, has all $g=0$ while the replacement model $M=I/7$ gives $r_{ij}=0$ on every off-diagonal pair. High phase does not force model error; zero phase does not prove access.

An **operational nonconscious-content test [Pr]** separately declares a task, independent report/access criterion, evidence of content-dependent processing and controls for guessing, response demands and measurement noise. Connecting this record to $\mathcal U_{\mathrm{score}}$ is an empirical hypothesis, to be tested on held-out data.

## 3. No theorem of compulsory opaque channels {#теорема-неполная-прозрачность}

The former claim “at least three of 21 channels must have nonzero Gap” is **withdrawn [✗]**, including when presented as conditional solely on a Hamming analogy. For a binary length-$n$ code correcting one bit error, disjoint radius-one balls give

$$
|C|(n+1)\le2^n.
$$

For a linear code with $r$ check bits, $2^r\ge n+1$; at $n=7$, $r\ge3$. This counts redundancy of a specified coding task, not imaginary matrix entries or unexperienced content. A valid codeword has zero syndrome while retaining its error-correction capability.

All entries of $\Gamma(t)$ above are real and all 21 pairwise Gaps are zero. At $t=0.45$ it even passes the complete **7D-proxy** capability gate: $P=.316429$, $R=.451467$, $\Phi=1.215$, $D^{7D}=2.327314$. Thus an assertion of forced nonzero phase conflicts with the stated model. This example does not prove phenomenal access to every process or an empirical L-level. Source and proof: [Hamming, Error Detecting and Error Correcting Codes](https://doi.org/10.1002/j.1538-7305.1950.tb00463.x); [correct Gap scope](/docs/consciousness/hierarchy/gap-characterization#граница-хэмминга-подробно).

## 4. Psychoanalytic mappings as hypotheses {#психоанализ}

### Repression {#вытеснение}

A proposal can ask whether independently assessed repression predicts a selected $(L,E)$ phase or readout-error pattern **[H]**. The assignment $g_{LE}\approx1$ is not a definition or diagnosis of clinical repression, and requires a fixed encoder and comparison against amplitude-only and behavioural baselines.

### Shadow {#тень}

Mapping lack of attention to aspects of experience onto $(A,E)$ is an interpretation **[I]**. A matrix phase cannot establish what someone notices, projects onto others, or phenomenally experiences. These need independent outcomes.

### Archetypes {#архетипы}

A recurrent joint-state or response pattern can be specified statistically **[D]**. The old assertion that an archetype raises purity for every L2 observer is not established. Universality is an empirical quantifier over a defined population and protocol, not a consequence of calling a pattern collective.

## 5. Dynamics and possible phase reduction {#динамика}

For a differentiable nonzero coherence $z(t)=a(t)e^{i\theta(t)}$,

$$
\dot\theta=\operatorname{Im}(\overline z\dot z)/|z|^2.
$$

Away from $\sin\theta=0$, the phase detector satisfies

$$
\dot g=\operatorname{sgn}(\sin\theta)\cos\theta\,\dot\theta.
$$

These identities **[T]** require the actual complex-coherence dynamics. Near zero amplitude an error floor is essential. An arbitrary scalar drift-plus-noise equation for $g$ does not automatically lift to positive density-matrix dynamics or stay in $[0,1]$.

The old three conditions “reflection above $1/6$, enough amplitude, and a bridge channel” are not a sufficient or necessary theorem of awareness. A diagonal unitary can rotate a supported phase without any intermediate bridge; it preserves $P$ and moduli. A model can also know an unchanged high phase. Specify the actual intervention and independently test changes in report/access. Memory kernels do not universally give a clinical integration time proportional to initial Gap.

## 6. Manifestations and causal interpretation {#проявления}

Slips, dreams, pain and projections are not derived from a static selected phase. A causal proposal must state the encoder, dynamics, intervention, readout and independent outcome. Correlation alone does not establish a hidden emotional cause of a bodily symptom or transfer of a coherence between persons. Joint states use tensor products and connected observables with the types in [composite systems](/docs/core/dynamics/composite-systems).

## 7. Therapy as an empirical research proposal {#терапия}

Mappings of CBT, psychoanalysis, body-based therapy and mindfulness to selected channels are **[H/I]**. No treatment efficacy, duration, mechanism or numerical phase trajectory is established by these assignments. A research protocol can compare independently assessed outcomes and preregistered channel/readout measures, with controls and uncertainty; it cannot treat a reduced Gap alone as a validated clinical benefit.

## 8. E-sector analysis {#e-сектор}

The six supported E-pair phases form a frame-referenced profile. Canonical

$$
\mathrm{Coh}_E=\frac{\gamma_{EE}^2+2\sum_{i\ne E}|\gamma_{Ei}|^2}{P}
$$

includes diagonal population. Its positivity is equivalent to $\gamma_{EE}>0$ for PSD states; it does not entail off-diagonal E coupling. No universal E-floor follows from nonzero dissipation; a stationary lower bound needs explicit rate/source assumptions. The proxy $D^{7D}=1+6\mathrm{Coh}_E$ is not the entropy of a literal one-dimensional axis. See [conditional purity balance](/docs/applied/coherence-cybernetics/theorems#теорема-81-условная-необходимость-интериорности-no-zombie).

## 9. Levels do not fix unconscious-channel counts {#сводная-таблица}

| Quantity | What must be measured or specified |
|---|---|
| Number of supported high-phase channels | Matrix, semantic frame, amplitude and phase thresholds |
| Number of poorly reproduced channels | Implemented model, independent targets and calibrated readout error |
| Operationally inaccessible contents | Independent processing/access task |
| L2 | Full typed $\mathsf{Cap}_2$ |
| L3/L4 | Higher-order nonconstant prediction certificates and compatibility |

L0 is universal inside the state model and does not mean all phases are opaque. No counts 21, 18–20, 10–15, 5–10 or minimum three are forced by L-labels. The proposed correspondence between phase and inaccessible content remains open.

## 10. Correct conclusions {#итоги}

Phase, model error and access are independently typed quantities. Coding redundancy does not impose opacity. Matrix identities provide reproducible statistics; biological and phenomenal interpretations require independent evidence. A fully real state is mathematically possible, while complete self-knowledge is a different philosophical/operational question.

## Connections

- [Typed kernel](/docs/reference/mathematical-kernel)
- [Gap identifiability](/docs/consciousness/hierarchy/gap-characterization)
- [Canonical hierarchy](/docs/consciousness/hierarchy/interiority-hierarchy)
- [Reconstruction model and tests](/docs/applied/research/reconstruction-identifiability)
