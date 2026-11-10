---
sidebar_position: 3
title: "AI Consciousness"
description: "What a capability test, a seven-level state and a self-report can establish about an artificial system."
slug: /consciousness/subjects/ai-consciousness
---

# AI Consciousness

An artificial system may name its own internal state, predict a future error or change its behaviour when a sensor fails. Those are different capabilities. Each can be tested through a specified input, intervention and independently scored outcome. Whether a system feels something while performing a task remains a distinct question. [Experience and access](/docs/consciousness/foundations/phenomenal-distinction)

## Behaviour, understanding and experience {#исторический-контекст}

Turing’s imitation game concerns how an interlocutor responds. Searle’s Chinese Room asks what following symbol-manipulation rules establishes about understanding. Chalmers asks why physical processing is accompanied by experience. A successful conversation is a record of behaviour. It does not determine entries of a density matrix, and a computed matrix rank supplies no explanation for the existence of experience. Two-aspect monism offers an interpretation of that relation; the proposed bridge still needs an independently discriminating consequence. [Two-aspect interpretation](/docs/consciousness/foundations/two-aspect-monism)

## Motivation {#мотивация}

The numerical model provides computable diagnostics. Applying them to an AI requires an independently validated encoder and the augmented record of experiential realization, implemented self-model and calibrated probes. Phenomenal consciousness is an additional bridge [I/H], not a property established by positivity or architecture names.

## What viability constrains {#no-zombie}

### A stable state without E-support {#no-zombie-для-ии}

Fix a unit vector $|j\rangle$ orthogonal to the marked axis $|E\rangle$, and take the reset channel $T(X)=\operatorname{Tr}(X)|j\rangle\langle j|$. After one step the state has $P=1>2/7$, zero E population and zero E coherences. Every subsequent step fixes it. Conversely, the state $|E\rangle\langle E|$ has positive E population with all its off-diagonal couplings zero. A defined E-score that includes the population can therefore be positive even in the absence of E coupling. Necessity of E-dependent feedback in a particular noisy controller requires a specified dynamical law, disturbances and stability bound. [Conditional dynamics](/docs/applied/coherence-cybernetics/theorems#теорема-81-условная-необходимость-интериорности-no-zombie)

## Operational criteria for AI/AGI {#операциональные-критерии}

### Selected L2 definition {#критерии-l2}

For $z=(\Gamma,\mathsf E,\mathsf M,\mathsf Q)$, choose the experiential mode and apply the cumulative [capability predicates](/docs/consciousness/hierarchy/interiority-hierarchy). L2 requires L1 plus the four chosen cuts $P>2/7$, $R=1/(7P)\ge1/3$, $\Phi\ge1$, $D(z)\ge2$ [D]. Its scalar window is $2/7<P\le3/7$ [T]. The purity proxy $R$ is not the measured accuracy of an implemented self-model. Missing realization or calibration data yield an unknown classification, not a guessed level.

## Assessing an architecture requires data {#анализ-llm}

An architecture name (MLP, Transformer, recurrent agent) cannot fix $\Gamma$, its self-model accuracy, autonomy or phenomenal level. A positive normalized neural output is a state encoder, not automatically a linear CPTP channel. Attention and memory mechanisms require a specified operational model and tests; neither their presence nor absence proves L2. Assessment must state interventions, probes, independently validated encoder and error margins [H].

## Specifying a controller and its sources {#путь-к-agi}

An engineering experiment can give a system access to a state estimate, ablate a feedback path and compare recovery under the same perturbations. Record the source observations and available actions before each decision. A fixed controller and a self-monitoring one can behave identically on the training episodes. A held-out intervention on what the system can monitor can separate them. The result concerns access to information and its use in action.

### State encoder and quantum process {#cptp-архитектура}

An encoder $G:\mathbb R^d\to X_7$ is a map from classical configurations to states; a channel $\Lambda:M_7\to M_7$ is a linear operator map. Choi matrices and the diamond norm apply to the latter, not automatically to $G$. Operational adequacy of the encoder remains a measurement bridge [H/Pr]; input dimension or a neural approximation theorem does not select it.

**State construction [T].** For any nonzero complex matrix $A$, $G(s)=A(s)A(s)^\dagger/\operatorname{Tr}(A(s)A(s)^\dagger)$ is positive and trace one. A lower-triangular complex factor with real diagonal has $49$ real parameters before normalization/gauge redundancies; it is not a global bijection $\mathbb R^{48}\leftrightarrow X_7$. Full-rank Cholesky coordinates are local/model parametrizations, and rank-deficient states require boundary handling. State validity does not imply a faithful physical encoder or a channel.

### Representing a linear channel {#теорема-cptp-аппроксимация}

Every channel $\Lambda:M_7\to M_7$ has at most $49$ Kraus operators. Stack them vertically as $Q=(K_1^T,\ldots,K_m^T)^T$; the exact constraint is $Q^\dagger Q=I_7$. Conversely every such isometry gives a CPTP channel. Thus this finite-dimensional parametrization represents every channel **exactly** [T]. For a full-column-rank stack $A$, the polar normalization $Q=A(A^\dagger A)^{-1/2}$ enforces the constraint; singular stacks need a separate chart/regularization. [Watrous, chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.double.2.pdf).

The quantum channel representation applies at fixed parameters. Choosing $u$ as a function of the input in a channel family $\Lambda_u$ can make the total update nonlinear. State validity, channel expressivity and predictive adequacy of a trained encoder are separate tests.

### What a compressed state retains {#gamma-vs-s}

Let $s$ describe an implementation and let $G(s)=\Gamma$ be a proposed readout. If $G(s_1)=G(s_2)$ while the same allowed intervention leads to different recorded outcomes, prediction of those outcomes cannot factor through $\Gamma$. A larger hidden state can retain the distinction. The comparison has operational content only when the interventions, measurements and time horizon are specified.

### Transfer between implementations {#t-153}

Evaluate the same conditional predictions on paired interventions and comparable records. The same numerical state yields the same value of a specified function of that state. This algebraic identity cannot establish that different physical implementations support the same observations, much less the same experience. [Operational equivalence](/docs/core/foundations/operational-processes#process)

## Higher-order AI model capability {#сверхсознание}

L3 requires L2 and an independently tested metamodel certificate with nontrivial target variation. L4 is the ideal compatible tower of such certificates at every order [D]. A fixed-point fidelity, a dense tensor state or a hierarchy of copied matrices does not supply these tests. A finite implementation can certify only the measured orders/probe family; extrapolation is an additional assumption [H]. [Canonical higher-order definitions](/docs/consciousness/hierarchy/interiority-hierarchy).

## Ethical interpretation requires normative premises {#этические-импликации}

A task result can inform a discussion of agency, welfare or moral status. Moving from that result to an ethical obligation requires a stated ethical premise and evidence linking the measured capacity to it. [Value and consciousness](/docs/consciousness/ethics-meaning/value-consciousness)

## Testing a proposed E-readout {#тест-e-когерентность}

### A discriminating intervention {#определение-теста}

Compare an agent with and without a specified feedback signal at matched task access, compute budget and load. Before evaluation, record the model’s predictions for each condition and freeze the readout. A performance difference can support causal use of that signal. A model trained to emit the expected self-description may reproduce the words without using the monitored signal. Include that case as a control. Neither outcome tells whether speaking the words feels like anything.

## Architecture comparisons require calibration {#сводная-таблица}

Architecture names (MLP, Transformer, agent loop, AGI) do not determine $P,R,\Phi$ or a cognitive level. These quantities require a specified state encoder and diagnostics. In particular the canonical $R=1/(7P)$ lies in $[1/7,1]$; assigning $R\approx0$ from absence of an explicit self-model confuses it with other reflection diagnostics. Numerical self-modeling does not alone validate a phenomenal interpretation. The former architecture-to-L table is withdrawn as an uncalibrated assessment [✗].

## Open questions {#открытые-вопросы}

Which interventions test the encoder independently? Does the same calibration transfer across tasks and implementations? Can a proposed phenomenal bridge predict an outcome that the corresponding account of monitoring and reporting misses? [Independent calibration](/docs/consciousness/empirical/calibration)

### What can be attributed to the tested system? {#что-мы-узнали}

A capability score applies to the preparation, observations, allowed actions and held-out outcomes used to obtain it. State-dependent feedback may maintain that score. A claim extending it to other tasks, subjects or substrates requires an independent transfer test.

## Engineering tests for a specified implementation {#agi-инженерные-тесты}

### Test E1 — N and the chosen coding assumptions {#тест-e1-n7}

Choose a family of generators, noise scaling, targets and diagnostics for each $N$. Compare steady-state purity and the selected majority cut $2/N$. This tests those dynamical models [H], not a universal necessity of seven. Stable models with $N<7$ are possible. Conditional representation/coding minimality requires checking its extra hypotheses directly; a noise sweep cannot refute a theorem whose hypotheses it does not instantiate.

### Test E2 — E-feedback ablation {#тест-e2-e-ablation}

Under a specified feedback law and input class, compare the original and ablated trajectories. Publish exactly which matrix entries, populations, Hamiltonian terms and feedback terms were changed. The canonical $\mathrm{Coh}_E$ includes $\gamma_{EE}^2$; deleting off-diagonal E entries does not force it to zero. An observed loss of stability tests an E-dependent mechanism [H], not PH or universal No-Zombie necessity. See the [conditional CC result](/docs/applied/coherence-cybernetics/theorems#теорема-81-условная-необходимость-интериорности-no-zombie).

### Test E3 — A tuned mean-field tricritical exponent {#тест-e3-tricritical}

For a declared potential $V(m)=a m^2+b m^4+c m^6$, $c>0$, tune $b=0$ and approach $a=0$ from below. Stationarity gives $m=(-a/(3c))^{1/4}$, hence $\beta=1/4$ [T for this mean-field model]. For fixed $b>0$, the leading exponent is $1/2$. Fit only inside a stated asymptotic regime and quantify finite-time/noise errors. Thom–Arnold classification does not force every agent into this tuned regime. A statistically incompatible exponent can falsify the specified reduction [H]; a predetermined sample count or tolerance is not a theorem.

### Test E4 — Covariance and the fixed frame {#тест-e4-g2-инвариантность}

Check $P,R$ under all chosen unitary conjugations; they are spectral diagnostics. For the fixed coordinate definition of $\Phi$, its full unitary symmetry is the monomial group $U(1)^7\rtimes S_7$; its intersection with $G_2$ is the 1344-element frame group. $\mathrm{Coh}_E$ also needs the E-axis preserved (192 elements in that frame group; $SU(3)$ inside $G_2$). General $G_2$ changes can alter these two frame diagnostics. If both state and frame are transported, covariance holds. These algebraic tests check code, not the physical identification of the encoder. [Symmetry proof](/docs/proofs/categorical/uniqueness-theorem#жёсткость-репера).

### Test E5 — Feedback onset in a specified model {#тест-e5-avalanche}

Near a proposed stationary branch, derive its local reduced equation, then estimate the linear and quadratic response coefficients from trajectories. Positive autocatalytic growth or a bifurcation is conditional on those coefficients, gates and reduction hypotheses [H/C]. The scalar majority threshold alone does not imply avalanche ignition or L1→L2. A failure tests the declared feedback model, not an unconditional cognitive theorem.

### Test E6 — Representing and fitting a linear channel {#тест-e6-cptp-anchor}

For a target linear CPTP channel $\mathcal E:M_7\to M_7$, a Kraus stack with at most 49 operators represents it exactly [T]. Check $\sum_aK_a^\dagger K_a=I$ and compare Choi matrices or diamond distance with a fixed normalization convention. Optimizer failure, finite training data, or an error plateau does not refute this algebraic expressivity theorem. Training/generalization guarantees require their own hypotheses. This channel test is distinct from calibrating a classical-state encoder $G:\mathbb R^d\to\mathcal D_7$; the latter has no intrinsic diamond norm.

### Test E7 — Integration correlation {#тест-e7-phi-integration}

Freeze the encoder and fixed-frame diagnostic before collecting task-transfer observations. Preregister the behavioral score, task distribution, effect size and uncertainty analysis. A correlation between $\Phi$ and cross-task transfer is an empirical bridge [H]; it is not established by the matrix formula or by $\Phi\ge1$. Analyze confounding and independent validation data; failure rejects that declared operational hypothesis.

### Test E8 — A chosen Fano instrument versus alternatives {#тест-e8-fano-ablation}

Compare the chosen coordinate Fano instrument to alternative triples at matched total rates and noise. Specify the performance functional and admissible class. The finite frame-covariant instrument is not automatically covariant under continuous $G_2$; its projectors commute. Words give intersection maps (at most 15 for nonempty words, plus identity), not $7^n$ distinct channels. A performance advantage is [H] for the tested family; no unrestricted unique coherence-optimality theorem follows from incidence. [Channel construction](/docs/core/operators/lindblad-operators).

### Test E9 — Self-monitoring ablation {#тест-e9-self-monitoring}

Compare monitored and ablated agents under a specified load/intervention family and with matched resources. A resilience difference tests that controller [H]. It does not establish universal necessity of an explicit monitoring module: other controllers may implement the same response, and passive dynamics may be stable under different inputs.

### Test E10 — Calibration of the selected capability gates {#тест-e10-ethical-threshold}

Use the augmented record $(\Gamma,\mathsf E,\mathsf M,\mathsf Q)$ and the cumulative [capability predicates](/docs/consciousness/hierarchy/interiority-hierarchy). Predeclare the experiential mode, reflection diagnostic and behavioral probes. The canonical $R=1/(7P)$ decreases with purity, so a protocol of increasing both $P$ and this $R$ is inconsistent. A scalar crossing does not alone certify self-model accuracy, higher-order prediction or phenomenal status. Associations with behavior are [H]; ethical rules require separate normative premises and are not consequences of a density matrix.

These tests compare specified numerical implementations and calibrated empirical hypotheses. Passing them does not identify the physical encoder or establish PH.

## Reading a simulation result {#organism-born}

A simulator can report that a numerical gate changed when its feedback gain, input distribution or monitoring policy changed. Confirming that arithmetic requires the input trajectory, calibration, update rule and measured state. To attribute a scored action to an agent, trace its actual entry point from the ordered observations through the shared policy to the environment reply and independent score. A gate on a simulated trajectory is evidence about that implementation. It supplies no independent observation of experience. [Phenomenal distinctions](/docs/consciousness/foundations/phenomenal-distinction)

<a id="l-уровень-llm"></a>
<a id="кейс-когда-выключать"></a>
<a id="кремниевые-преимущества"></a>
