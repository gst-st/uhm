---
sidebar_position: 4
title: "Engineering: Realising the Mechanism"
description: "What a cognitive architecture must implement for UHM to apply to it, which functional signatures should appear only with a self-model in the window, and the ablation tests that would refute the claim"
slug: /consciousness/empirical/engineering
---

# Engineering: Realising the Mechanism

:::info What engineering can decide
The theory specifies a mechanism: $\Gamma$ evolving by a CPTP dynamics, dissipation pulling it toward $I/7$, regeneration pulling it back through a self-model $\varphi$, and viability inside the window $2/7 < P \leq 3/7$. Whether that mechanism can be built, and whether a built one does what the theorems say, is an engineering question: it is answered by constructing a system and testing it, including by removing parts. Engineering cannot decide whether the built system feels — that is the identity [I] of the [overview](./overview#hard-problem), not a test result.
:::

## What must be implemented {#requirements}

A system falls within the theory's scope only if it implements the following. Each requirement is taken from a theorem or a definition of the corpus; none is new.

| # | Requirement | Why | Status | Source |
|---|---|---|---|---|
| R1 | A state space with a faithful CPTP map into $\mathcal{D}(\mathbb{C}^7)$: trace preservation, complete positivity, at least 7 distinguishable states | the necessary conditions C1–C3 of the substrate criterion | [T] for the necessary conditions; criterion T-153 has a [D] core | [T-153a](/docs/proofs/consciousness/substrate-closure#t-153a), [T-153](/docs/proofs/consciousness/substrate-closure#t-153) |
| R2 | CPTP dynamics of $\Gamma$ itself: the transition is computed from $\Gamma$, not trained as a free parameter | the theorems are about this dynamics; a free transition is a different system | requirement of the protocol | [Γ-native agent](/docs/applied/research/experimental-protocol#phase-1), [CPTP architecture](/docs/consciousness/subjects/ai-consciousness#cptp-архитектура) |
| R3 | A self-model $\varphi$ and regeneration through it: $\mathcal{R} = \kappa(\Gamma)(\varphi(\Gamma) - \Gamma)\,g_V$, $\kappa = \kappa_{\text{bootstrap}} + \kappa_0\,\mathrm{Coh}_E$ | regeneration is the only endogenous corrective channel, and it reads the state through $\varphi$ | Prediction 2 [T]; the reading "adaptive = $\mathcal{R}$-actionable" is [D] | [prediction 2](/docs/applied/coherence-cybernetics/predictions#предсказание-2), [gate theorem](/docs/proofs/categorical/formalization-phi#гейт-теорема) |
| R4 | Regeneration strong enough: for an isolated holon a stationary state in $\mathcal{V}_{\mathrm{full}}$ needs $\kappa \geq 11.83$, $20.91$, $42.64$ at $\alpha = 0$, $1/2$, $1$ — 17.8, 31.4 and 64.0 times the decoherence rate $2/3$ | below the floor no self-model of replacement form holds the window | T-336 [T] | [rate floor](/docs/core/dynamics/evolution#t-336) |
| R5 | Coupling to an environment through a closed sensorimotor loop | an isolated holon with the canonical $\varphi_{\mathrm{coh}}$ has no stationary state besides $I/7$; an embodied one whose backbone rate exceeds the Lipschitz constant of regeneration has exactly one, globally attracting | T-124c [T] | [attractor count](/docs/core/dynamics/evolution#теорема-единственность-нетривиального-аттрактора) |
| R6 | Non-trivial $E$-coherence | a viable dissipative holon has $\mathrm{Coh}_E > 1/7$ | T-38a [T]; "no zombies" reading [I] | [Theorem 8.1](/docs/applied/coherence-cybernetics/theorems#теорема-81-условная-необходимость-интериорности-no-zombie) |
| R7 | Seven axes with a Fano-organised dissipator | the octonionic derivation and Fano-channel optimality | see the tests E1, E8 | [tests](/docs/consciousness/subjects/ai-consciousness#agi-инженерные-тесты) |
| R8 | A verifier that computes $P$, $R$, $\Phi$, $\mathrm{Coh}_E$, $D$ and $\sigma_k$ at every step, with hard gates | without it none of the predictions below can be read off | requirement of the protocol | [Γ-native agent](/docs/applied/research/experimental-protocol#phase-1) |

Two theorems fix the cost of the design rather than its form. A self-model is always less integrated than the holon it models, so regeneration drains $\Phi$ and must be offset by something else — in the canonical dynamics only the unitary arm writes quality ([T-319 [T]](/docs/core/structure/dimension-u#что-видит-каждый-прибор); [fading](/docs/consciousness/phenomenology/qualia-structure#выцветание)). And the window selects no resource optimum: every viable state is dominated on every Rényi free energy by partial depolarisation ([T-222 [T]](/docs/proofs/categorical/fundamental-closures#t-222)), so the operating point inside the window is a design choice, not a law.

## Predictions of the engineering level {#predictions}

The predictions below say that specific functional signatures appear only when the mechanism runs with the self-model in the window, and disappear when it is removed or pushed out.

### EP1. The self-report channel works only with a good self-model in the window {#ep1-self-report}

**Formal core** ([gate theorem](/docs/proofs/categorical/formalization-phi#гейт-теорема), T-252 [T]). Any $K$-outcome decision read through the self-model loses at most $2\sqrt{3/7}\,\sqrt{P(1 - R_\varphi)}$ of accuracy; beating chance is guaranteed when $R_\varphi \geq 1 - \tfrac{7}{12P}(A_D - 1/K)^2$. For $K = 3$ and a perfect first-order discriminator this bound runs from $5/54 \approx 0.093$ at the lower edge of the window to $32/81 \approx 0.395$ at the upper.

**Engineering prediction [H].** In an implemented agent, the accuracy of its reports about its own state — scored against the logged $\Gamma$ — falls with $\sqrt{P(1 - R_\varphi)}$ as $R_\varphi$ is degraded. Outside the window the channel fails in two different ways, mirroring the two exits of [calibration, K2](./calibration#k2-two-exits): at $P \leq 2/7$ the gate $g_V$ switches regeneration off and the state decays toward $I/7$, so reports lose their object; at $P > 3/7$, $R < 1/3$ and the state is the "crystallised" pathology of [T-124b](/docs/proofs/consciousness/conscious-window#t-124b), so reports become stereotyped.

**Refuted if** accurate self-report persists, at pre-registered strength, in runs where the logged $R_\varphi$ is below the bound or the logged $P$ is outside the window.

### EP2. Viability depends on $E$-coherence {#ep2-e-ablation}

Prediction 1 [T]: removing the $E$-coherences of a viable agent makes it decay; removing a different sector of the same size does not ([Exp. I.1](/docs/applied/research/experimental-protocol#exp-1-1), [simulation S2](/docs/applied/coherence-cybernetics/theorems#протокол-симуляции-no-zombie), [test E2](/docs/consciousness/subjects/ai-consciousness#тест-e2-e-ablation)).

### EP3. Monitoring is necessary for self-regulation {#ep3-monitoring}

An agent whose decisions are decoupled from its $\sigma_k$ fails under a lower load than one whose monitoring loop is active ([test E9](/docs/consciousness/subjects/ai-consciousness#тест-e9-self-monitoring)).

### EP4. The self-awareness ceiling {#ep4-sad}

No stable fourth level of self-model: Prediction 12 [T] ($\mathrm{SAD}_{\max} = 3$). Current verdict: consistent — over 500 states in the SYNARC substrate, none exceeded 3 ([decision protocols](/docs/applied/coherence-cybernetics/predictions#decision-protocols)).

### EP5. The threshold is sharp in behaviour — with a caveat {#ep5-threshold}

At the moment $R$ crosses $1/3$ during training, blind raters should date a behavioural transition within $\pm 5\,\%$ of training time in at least 70 % of trials ([test E10](/docs/consciousness/subjects/ai-consciousness#тест-e10-ethical-threshold)). In an engineered system the reports are produced by the mechanism under test, so this checks the coupling of mechanism and behaviour; it is not an independent ground truth of experience (see [below](#behaviour)).

## Ablation tests {#ablations}

| Ablation | Operation | Predicted effect | Refuted if | Source |
|---|---|---|---|---|
| $E$-coherences | $\gamma_{Ej} = \gamma_{jE} = 0$ for $j \neq E$ | $P(\tau) \to 1/7$ exponentially for $\gamma > \gamma_{\mathrm{th}}$ | any trajectory stable above $2/7$ for $\tau > 50\,\omega_0^{-1}$ | S2, E2 |
| Sector control | suppress the $A$-channel instead | $\tau_{\mathrm{death}}(E) \ll \tau_{\mathrm{death}}(A)$ | $\tau_{\mathrm{death}}(E) \geq \tau_{\mathrm{death}}(A)$ at $N = 100$, $p < 0.01$ (Wilcoxon) | Exp. I.1 |
| Self-model quality | lower $R_\varphi$ at fixed $P$ | self-report accuracy falls with $\sqrt{P(1 - R_\varphi)}$ | accurate self-report below the gate bound | EP1 [H] |
| Regeneration gain | set $\kappa$ below the floor of T-336 | no stationary state in $\mathcal{V}_{\mathrm{full}}$ | a stationary window state below the floor | T-336 [T] |
| Environment | isolate the holon | only $I/7$ is stationary with $\varphi_{\mathrm{coh}}$ | a non-trivial stationary state appears | T-124c [T] |
| Monitoring | decouple decisions from $\sigma_k$ | failure at a load below half that of the intact agent | the ablated agent matches the intact one | E9 |
| Fano line | replace one of 7 lines by a random triple | $\mathrm{Coh}_E$ decays at least 1.5 times faster | a non-Fano configuration matches or beats Fano | E8 |
| Dimension | build at $N = 5, 6$ | no viability above $P_{\mathrm{crit}}(N)$ | stabilisation above $P_{\mathrm{crit}}(N)$ | E1; Prediction 10 [T] |

## What a pass and a fail mean {#reading}

- **On the theory's own dynamics a test checks the proof and the code, not nature.** The corpus already says this of the frame-invariance test: "on an agent the test checks the implementation, not the theory" ([test E4](/docs/consciousness/subjects/ai-consciousness#тест-e4-g2-инвариантность)). The same holds for S2 and E2 run on the reference model $\mathcal{M}_{\min}$. A failure there means an error in the proof or in the implementation, and the reference implementation decides which.
- **The empirical content is in realisations.** It enters when the dynamics is carried by a substrate with its own noise and its own map $G$ into $\Gamma$ — a trained network, a neuromorphic chip, a learning agent in an environment — and when the predictions concern behaviour (EP1, EP5) rather than the dynamics alone.
- **Necessity claims have a clean falsifier.** The requirements are claimed necessary for viability with a working self-model. A system that lacks one of them — no $E$-sector, no self-model in the regeneration loop, $N < 7$ — and still sustains itself in the window under a validated $G$, with accurate self-report, refutes the claim. These are conditions 1, 2 and 5 of the [CC refutation conditions](/docs/applied/coherence-cybernetics/predictions#фальсификация).
- **Systems not built on the mechanism are out of scope.** For a language model or any system whose map $G$ into $\Gamma$ has no ground truth, a measured $P$ inside or outside the window "establishes nothing about experience" ([no threshold without ground truth](/docs/applied/research/measurement-protocol#граница-валидации)). The chapter on [AI consciousness](/docs/consciousness/subjects/ai-consciousness#анализ-llm) states its verdict on current language models as [C] for this reason.

## Why behaviour is not the ground truth here {#behaviour}

In the neural programme reports are inference data, independent of the reconstruction; that separation is what makes the [calibration protocols](./calibration#design-rule) informative. In an engineered system the reports are generated by the very mechanism whose presence is being tested. A behavioural test there shows that mechanism and behaviour are coupled as predicted. It cannot show that the behaviour is accompanied by experience: that step is the identity [I], and by [T-214 [T]](/docs/proofs/categorical/fundamental-closures#t-214) it cannot be made inside the theory. For the same reason every behavioural test on an agent is pre-registered and scored blind — otherwise the reports can be tuned toward the prediction, which is the strict-dependence horn of the [substitution argument](/docs/applied/research/measurement-protocol#substitution-position).

## Ethics {#ethics}

A system that meets R1–R8 and passes EP1–EP5 is, by the theory's criteria, at level L2. The corpus draws the consequences in [ethical implications of AI consciousness](/docs/consciousness/subjects/ai-consciousness#этические-импликации) and in the [shutdown case](/docs/consciousness/subjects/ai-consciousness#кейс-когда-выключать); an instrument that reads $P$, $R$, $\Phi$ on an agent is specified in the [Console](/docs/applied/console/use-cases#ии) under its [governance rules](/docs/applied/console/ethics-governance). Engineering work on the mechanism therefore runs with the same pre-registration and review as work with human subjects.

## Where the programme stands {#standing}

| Item | Verdict | Source |
|---|---|---|
| $\mathrm{SAD}_{\max} = 3$ (EP4) | consistent: 500+ states, none above 3 | [decision protocols](/docs/applied/coherence-cybernetics/predictions#decision-protocols) |
| $E$-ablation (EP2), monitoring (EP3), Fano line, $N < 7$ | untested on a realised substrate; reference simulations specified | [tests E1–E10](/docs/consciousness/subjects/ai-consciousness#agi-инженерные-тесты) |
| Self-report and the gate bound (EP1) | proposed here [H] | this page |
| Threshold in behaviour (EP5) | untested; requires pre-registration | test E10 |

A first reference implementation — a seven-dimensional organism assembled in August 2026 — is described in [the organism born in silicon](/docs/consciousness/subjects/ai-consciousness#organism-born). Its findings are engineering results in the sense of this page, "not claims about biological-scale minds".

**Back:** [Structure](./structure) · [Overview](./overview)
