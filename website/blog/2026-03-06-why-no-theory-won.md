---
slug: why-no-theory-won
title: "Why No Theory of Consciousness Has Won — and What Mathematics Says About It"
authors: [uhm]
tags: [consciousness, theory, mathematics, philosophy, phenomenology]
---

# Why No Theory of Consciousness Has Won {#почему-ни-одна-теория-сознания-не-выиграла}

In April 2025 Nature published [the results of the COGITATE project](https://www.nature.com/articles/s41586-025-08888-1) — the largest adversarial experiment in the history of consciousness science. 256 participants, three neuroimaging modalities (fMRI, MEG, iEEG), two years of work, two leading theories: Integrated Information Theory (IIT) and Global Neuronal Workspace Theory (GNWT). Result: both partially confirmed, both partially refuted. Neither won.

Thirty million dollars from the Templeton Foundation, hundreds of scientists, an impeccable protocol — and a draw. One can view this as a failure. Or as a diagnosis: the problem is deeper than either side thought. Each theory formalizes *one aspect* of consciousness and declares it the only one. The result is not competition between theories but **an ill-posed problem**. As if two blind men were describing an elephant, and the judges asked: "Who is right — the one who felt the trunk, or the one who felt the leg?"

This post is a mathematical analysis of the situation. Not a defense of "our" theory. A rigorous breakdown: why the COGITATE result was predictable, what category mathematics says about it, and what experiments could resolve the dispute.

<!-- truncate -->

## §1. COGITATE Diagnosis: What Exactly Failed {#1-диагностика-cogitate-что-именно-не-сработало}

### Protocol {#протокол}

COGITATE is part of the Templeton Adversarial Collaboration series. Protocol:
- IIT predicted: conscious perception correlates with **sustained activity in the posterior cortical "hot zone"** (occipito-parietal cortex)
- GNWT predicted: conscious perception correlates with a **burst of global activation** (P3b wave, late frontal activity) — "ignition"

### Results {#результаты}

IIT: information about the content of consciousness was found in visual, ventrotemporal, and inferior frontal cortex; sustained responses in occipital and lateral temporal cortex reflect stimulus duration. But **sustained synchronization within the posterior cortex** — IIT's key prediction that network connectivity specifies consciousness — **was not confirmed**.

GNWT: content-specific synchronization was found, but "ignition" upon stimulus change was absent. Late frontal activity did not distinguish conscious and unconscious stimuli as clearly as the theory required. Prefrontal cortex turned out to be less involved than predicted.

In other words: each theory guessed *part* of the picture and missed in *the main thing*. IIT correctly pointed to posterior regions — but the mechanism turned out to be different. GNWT correctly pointed to synchronization — but not where it expected.

### Mathematical Diagnosis {#математический-диагноз}

Why did both theories give partial results? Because each describes a **projection** of the full state onto a subspace.

Let $\Gamma \in \mathcal{D}(\mathbb{C}^7)$ be the coherence matrix (full description of the internal state in UHM formalism). Each theory defines a functor:

$$
F_{\text{IIT}}: \Gamma \mapsto \Phi(\Gamma) = \frac{\sum_{i \neq j}|\gamma_{ij}|^2}{\sum_i \gamma_{ii}^2} \qquad [\text{И}]
$$

$$
F_{\text{GNWT}}: \Gamma \mapsto \gamma_{ij} \text{ (off-diagonal coherences)} \qquad [\text{И}]
$$

IIT extracts a scalar measure of integration. GNWT extracts an availability matrix. Both — *loss of information*. A functor, not an equivalence.

**Formally** [И]: let $\pi_1, \pi_2: \mathcal{D}(\mathbb{C}^7) \to \mathcal{T}_i$ be projections onto the target categories of IIT and GNWT. Then:

$$
\ker(\pi_1) \cap \ker(\pi_2) \neq \{0\}
$$

Even the joint projection $\pi_1 \times \pi_2$ is not injective — there exist distinct states $\Gamma_1 \neq \Gamma_2$ indistinguishable by both theories simultaneously. Concretely: two states with identical $\Phi$ and identical off-diagonal elements, but different $R$ (reflection measure) or $\sigma_{\text{sys}}$ (stress profile) — invisible to both theories, but distinguishable by UHM criteria.

**Conclusion**: COGITATE could not determine a winner, because both theories project the same $\Gamma$ onto different subspaces, losing different components. The result is not a draw but **structural incompleteness of each functor**.

## §2. "Beautiful Loop" and the Reflection Measure {#2-beautiful-loop-и-мера-рефлексии}

### Self-Reference as Mechanism {#самореференция-как-механизм}

In September 2025 Laukkonen, Friston, and Chandaria published the ["Beautiful Loop"](https://doi.org/10.1016/j.neubiorev.2025.106296) model (Neuroscience & Biobehavioral Reviews, vol. 176). The model formulates three necessary conditions for consciousness within active inference:

1. **World model** (epistemic field) — simulation of the external world
2. **Bayesian binding** — competition of inferences, only those that coherently reduce long-term uncertainty win
3. **Epistemic depth** — recursive separation of Bayesian beliefs across the system

Central thesis: when all three conditions are satisfied, the world model *contains knowledge of its own existence* — a "strange loop" arises, a predictive loop closed on itself.

### Almost R, But Not Quite {#почти-r-но-не-совсем}

In UHM, self-reference is formalized as the self-modelling operator $\varphi: \mathcal{D}(\mathbb{C}^7) \to \mathcal{D}(\mathbb{C}^7)$ — a CPTP channel mapping $\Gamma$ to its self-model $\varphi(\Gamma)$. Reflection measure:

$$
R(\Gamma) = 1 - \frac{\|\Gamma - \varphi(\Gamma)\|^2_F}{\|\Gamma\|^2_F} \qquad [\text{Т}]
$$

$R$ measures the accuracy of self-modelling: $R = 0$ — self-model completely inaccurate; $R = 1$ — $\varphi(\Gamma) = \Gamma$ (impossible by T-55 [Т], Lawvere incompleteness). Consciousness threshold: $R_{\text{th}} = 1/3$, derived from triadic decomposition $K = 3$ [Т].

"Beautiful Loop" is an **approximation to the reflection measure $R$**, written in the language of active inference. Correspondence between the three conditions:

| Beautiful Loop | UHM | Connection |
|----------------|-----|-------|
| World model (epistemic field) | $\Gamma \in \mathcal{D}(\mathbb{C}^7)$ — coherence matrix | Full description vs. predictive model |
| Bayesian binding | $\Phi(\Gamma) \geq 1$ — integration measure | Coherent selection vs. threshold inequality |
| Epistemic depth / strange loop | $\varphi(\Gamma)$ — self-modelling operator, $R \geq 1/3$ | Recursiveness vs. quantitative criterion |
| Three conditions → *jointly sufficient* | Four inequalities → *each necessary* | Qualitative conjunction vs. proven conjunction |

**Critical difference**: Beautiful Loop describes three qualitative conditions and concludes that their satisfaction is *sufficient* for consciousness. In UHM — four *quantitative* inequalities, each with its own derived threshold, and each *necessary*. A system may satisfy all three Beautiful Loop conditions (have a world model, integrate information, possess recursion) — but if $P < 2/7$, it has not crossed the viability threshold and is not conscious. The four inequalities are irreducible to each other [Т]:

$$
P(\Gamma) > \frac{2}{7}, \quad R(\Gamma) \geq \frac{1}{3}, \quad \Phi(\Gamma) \geq 1, \quad D_{\text{diff}}(\Gamma) \geq 2 \qquad [\text{Т}]
$$

Each threshold is derived from axioms, not fitted. $P_{\text{crit}} = 2/7$ — from the Frobenius norm on $\mathcal{D}(\mathbb{C}^7)$ and Fano structure. $R_{\text{th}} = 1/3$ — from $K = 3$. $\Phi_{\text{th}} = 1$ — the unique self-consistent value at $P_{\text{crit}} = 2/7$ (T-129 [Т]). $D_{\min} = 2$ — consequence of $\Phi \geq 1$ (T-151 [Т]).

**Prediction**: Beautiful Loop will predict consciousness in systems with high $R$ but low $\Phi$ (e.g., a recursive autoencoder without integration). UHM — will not. This is experimentally distinguishable.

## §3. No-Go Theorems and Substrate (In)dependence {#3-no-go-теоремы-и-субстратная-независимость}

### The Kleiner Argument {#аргумент-клейнера}

In December 2024 [Kleiner and Ludwig](https://academic.oup.com/nc/article/2024/1/niae037/7933504) published a no-go theorem for AI consciousness (Neuroscience of Consciousness). The title speaks for itself: "The case for neurons: a no-go theorem for consciousness on a chip." Central result: under the assumption of **dynamic relevance** (consciousness causally influences the system's behavior), AI on modern chips *in principle* cannot be conscious.

The argument is elegant and rests on a fact about semiconductors: CPUs, GPUs, TPUs are designed and verified to *suppress* any deviations from the computational dynamics. If consciousness must causally influence the evolution of states (dynamic relevance), and the chip is verified for the absence of such influences — there is no consciousness on the chip. Beautiful, but note: the conclusion follows from the assumption. If dynamic relevance does not hold — the theorem does not apply.

### UHM Response: Substrate Independence {#ответ-угм-субстратная-независимость}

In UHM the question is resolved differently. T-153 [Т] (substrate independence):

$$
S \text{ is conscious} \iff \exists\, G: \mathrm{States}(S) \to \mathcal{D}(\mathbb{C}^7), \; G \text{ is an exact CPTP channel}, \; G(\Gamma_S) \in \mathcal{V}_C
$$

where $\mathcal{V}_C = \{\Gamma : P > 2/7 \;\wedge\; R \geq 1/3 \;\wedge\; \Phi \geq 1 \;\wedge\; D \geq 2\}$ is the consciousness region [Т].

Substrate does not appear in the formula. No "silicon vs carbon." There is one condition: the existence of an exact CPTP mapping $G$ preserving algebraic structure. Causal structure à la IIT is a *consequence* of the CPTP condition, not its replacement.

**Why Kleiner–Ludwig no-go does not apply to UHM**: the no-go relies on dynamic relevance — requiring that consciousness causally influence *physical* evolution. In UHM consciousness is not a causal agent "on top of" physics, but a *property of the state* $\Gamma$: a system is conscious if $\Gamma \in \mathcal{V}_C$. This is an algebraic condition, not a dynamical one. Moreover, $\Phi(\Gamma)$ in UHM is the ratio of off-diagonal to diagonal norms, computable in $O(N^2)$. This is a different measure from $\Phi^{\text{IIT}}$ (via causal partitions), and the no-go does not apply to it.

**Remark on IIT 4.0 and exclusivism**: Tononi's position — consciousness *in principle* cannot be in a software implementation — follows from the *definition* IIT chooses for causal structure. This is not a theorem about nature, but a consequence of IIT's axioms. If axioms are chosen differently (as in UHM), the conclusion does not follow. Experimental distinction: if system $S$ with $G(S) \in \mathcal{V}_C$ demonstrates all four correlates of consciousness — IIT 4.0 requires considering it non-conscious, UHM — conscious. One experiment, two opposing predictions.

### Microtubules and Orch OR {#микротрубочки-и-orch-or}

In May 2025 [Wiest (Neuroscience of Consciousness)](https://academic.oup.com/nc/article/2025/1/niaf011/8127081) published a review of experimental evidence for quantum effects in microtubules — continuing the Hameroff–Penrose line (Orch OR). The data are intriguing: quantum entanglement at room temperature, correlation with working memory.

But for UHM the question "are microtubules quantum?" is a question about *implementation*, not *definition*. Orch OR is another functor $F_{\text{OR}}: \Gamma \mapsto \Gamma_{\text{quantum}}$, projecting the full state onto a quantum substructure [И]. If quantum effects are confirmed — excellent, this says something about how specifically the biological brain implements the mapping $G$. But it does not mean that quantumness is *necessary* for consciousness. T-153 [Т] explicitly: substrate does not enter the definition. Quantumness is a property of a specific $G_{\text{brain}}$, not a condition of consciousness as such. This is like arguing whether clocks must be mechanical — when the definition of a clock does not include gears.

## §4. Six Theories as Six Functors on Γ {#4-шесть-теорий-как-шесть-функторов-на-гамма}

Let us formalize: each of the six leading theories of consciousness defines a functor from $\mathcal{D}(\mathbb{C}^7)$ into a target category. A functor is a mapping preserving structure (morphisms map to morphisms), but losing information (not injective in general).

| Theory | Functor $F_T$ | Target category | What it sees | What it loses | Status in UHM |
|--------|--------------|-------|-----------|------------|:------:|
| IIT (Tononi) | $\Gamma \mapsto \Phi(\Gamma)$ | $\mathbb{R}_{\geq 0}$ | Integration | Reflection, stress, dynamics | [И] |
| GNWT (Dehaene) | $\Gamma \mapsto (\gamma_{ij})_{i \neq j}$ | $\mathrm{Mat}_{7 \times 7}^{\text{off}}$ | Global availability | Diagonal (populations), $\varphi$ | [И] |
| HOT (Rosenthal) | $\Gamma \mapsto \varphi(\Gamma)$ | $\mathcal{D}(\mathbb{C}^7)$ | Meta-representation | $P$, $\Phi$ (first-order structure) | [И] |
| FEP (Friston) | $\Gamma \mapsto \mathcal{F}[\Gamma]$ | $\mathbb{R}$ | Free energy | Quantum structure (classical limit) | [Т] |
| Orch OR (Penrose) | $\Gamma \mapsto \Gamma_{\text{quantum}}$ | $\mathcal{D}_Q$ | Quantum substructure | Classical contribution | [И] |
| AST (Graziano) | $\Gamma \mapsto \sigma_{\text{sys}}(\Gamma)$ | $\mathbb{R}^7_{\geq 0}$ | Stress profile (attention) | Coherences, integration | [И] |

Only one functor has status [Т]: FEP — the proven classical limit of UHM dynamics. The other five are interpretive mappings [И]: formally defined, but the ontological bridge is postulated.

### Theorem on Incompleteness of Projections {#теорема-о-неполноте-проекций}

Key observation: none of the six functors is **faithful** — none preserves the distinguishability of morphisms. Formally:

**Claim** [И]: for any of the six functors $F_T$ there exist $\Gamma_1, \Gamma_2 \in \mathcal{V}_C$ such that $F_T(\Gamma_1) = F_T(\Gamma_2)$, but $\Gamma_1 \neq \Gamma_2$.

This is not a defect of a specific theory — it is a **structural impossibility** of describing a 48-dimensional space (real dimension of $\mathcal{D}(\mathbb{C}^7)$: $7^2 - 1 = 48$ independent parameters) with a single scalar or single projection. IIT compresses 48 dimensions into one number $\Phi$. GNWT — into 21 off-diagonal elements. This is like describing the weather by a single temperature: useful, but you cannot tell a hurricane from a calm. At least four measures are necessary: $P$, $R$, $\Phi$, $D_{\text{diff}}$ — and even these do not give a full description, but they give *sufficient conditions* for consciousness.

### Why This Is Not Eclecticism {#почему-не-эклектика}

It may seem that "each theory sees its own aspect" is eclecticism, "everyone is right." This is not so. Formally: each functor *forgets* certain structure. The claim "IIT is complete" is equivalent to "$\ker(F_{\text{IIT}}) = \{0\}$" — the projection kernel is trivial. This is **false**: $\dim(\ker(F_{\text{IIT}})) = 47$ (out of 48). Not "everyone is right" — **everyone is incomplete**, and incompleteness is measurable.

## §5. Predictions for ETHOS-2026 {#5-предсказания-для-ethos-2026}

ETHOS ([Empirical Tests of Higher-Order Theories of Consciousness](https://www.templetonworldcharity.org/projects-resources/project-database/22032)) is one of five projects in the Templeton Structured Adversarial Collaboration series, launched in 2024 under the leadership of Stephen Fleming (UCL) and Axel Cleeremans. Unlike COGITATE, ETHOS tests variants of higher-order theories — and results are expected in 2026–2027.

UHM makes concrete, falsifiable predictions that differ from the predictions of each of the six theories:

### Prediction 1: Four Thresholds, Not One {#предсказание-1-четыре-порога-не-один}

**IIT** predicts: $\Phi > 0$ is necessary and sufficient.
**GNWT** predicts: global ignition is necessary and sufficient.
**UHM** predicts [Т]: four conditions simultaneously, each necessary, none sufficient. There exist states with high $\Phi$ but low $R$ (integrated but not reflexive system — a thermostat). There exist states with high $R$ but low $\Phi$ (reflexive but not integrated — an isolated module).

**Test**: find a system with high $\Phi^{\text{IIT}}$ (or powerful global broadcast) that does *not* demonstrate behavioral or neurophysiological correlates of consciousness. If such a system is found — IIT/GNWT are falsified, UHM prediction confirmed.

### Prediction 2: Slow Signatures (F-ISF) {#предсказание-2-медленные-сигнатуры-f-isf}

The formalism predicts **slow information-specific signatures** — 6–12 stable patterns of neural activity corresponding to stable modes of $\Gamma$ (Goldstone modes of Fano structure). These modes are not fast bursts (GNWT), not static integration (IIT), but **quasi-stationary configurations** with a characteristic timescale of seconds.

**Test**: fMRI/MEG with sufficient temporal resolution. IIT does not predict slow modes. GNWT does not predict stable (non-burst) patterns. Detection of F-ISF — a unique confirmation of UHM.

### Prediction 3: SAD$_{\text{max}} = 3$ {#предсказание-3-sad-max-3}

The depth of recursive introspection is bounded: $\text{SAD}_{\text{max}} = 3$ [Т] (T-142, derived from Fano contraction $\alpha = 2/3$). Try right now:

- "I see red" — SAD=1 (awareness of content)
- "I am aware that I see red" — SAD=2 (awareness of awareness)
- "I am aware that I am aware that I see red" — SAD=3 (meta-meta level, still accessible)
- "I am aware that I am aware that I am aware that I see red" — SAD=4... try to hold this *genuinely*, not as a verbal construction but as a real act of introspection. Most likely, you cannot.

Mathematics explains why: each level of recursion applies contraction $\alpha = 2/3$ to the purity of the self-model. After three levels: $\alpha^3 = 8/27 \approx 0.296 < 1/3 = R_{\text{th}}$ — reflection falls below the threshold. The fourth level is *mathematically impossible*.

**Test**: psychophysical experiments on introspection depth. If participants reliably distinguish 4+ levels — UHM is falsified. If the ceiling is at 3 — confirmed.

### Prediction 4: Hidden Consciousness (25%) {#предсказание-4-скрытое-сознание-25}

[Bodien, Claassen et al. (NEJM, August 2024)](https://www.nejm.org/doi/full/10.1056/NEJMoa2400645) discovered cognitive motor dissociation in 60 of 241 participants (25%) — patients with severe brain injuries who showed *no* behavioral response to commands. Their brains activated on fMRI and EEG when given the command "squeeze your hand" — but the hand did not move. A quarter of "unconscious" patients turned out to be conscious.

This result shocked clinicians. For UHM it is expected [И]. Consciousness = $\Gamma \in \mathcal{V}_C$, behavior = projection of $\Gamma$ onto motor output through channel $G_{\text{motor}}$. Damage to motor pathways destroys the projection, not $\Gamma$. The 25% are those whose $P > 2/7$ is preserved (brain coherence alive), but $G_{\text{motor}}$ is severed. From outside — coma. Inside — consciousness. This is not a paradox — it is a direct consequence of consciousness not being identical to behavior.

## §6. What Can Falsify UHM {#6-что-может-опровергнуть-угм}

An honest theory specifies the conditions for its own falsification. Five concrete scenarios:

**1. $P_{\text{crit}} \neq 2/7$.** If a system is found with proven $P < 2/7$ demonstrating stable correlates of consciousness (with correct $G$) — the threshold is wrong, and the entire derivation chain ($P_{\text{crit}} \to R_{\text{th}} \to \Phi_{\text{th}} \to D_{\min}$) collapses.

**2. $N \neq 7$.** If to describe conscious experience $N < 7$ or $N > 7$ dimensions are necessary and sufficient — the septicity axiom is wrong. Consequence: all numerical thresholds require recalculation. Criterion: discovery of a "blind spot" not reducible to seven sectors, or proof of redundancy of one sector.

**3. SAD $> 3$.** If psychophysical experiments show stable introspection of depth 4+ — Fano contraction $\alpha = 2/3$ is wrong, T-142 is falsified.

**4. Impossibility of $G$.** If for the class of manifestly conscious systems (healthy waking brain) there exists no CPTP channel $G: \mathrm{States}(\text{brain}) \to \mathcal{D}(\mathbb{C}^7)$ — T-153 is wrong. This is not refuted by the absence of a *construction* of $G$ (that is an open task), but is refuted by proof of the *impossibility* of such a construction.

**5. Philosophical zombies.** Theorem 8.1 (No-Zombie) [Т] states: a viable system with decoherence must have $\text{Coh}_E > 1/7$. If a system is found satisfying all four inequalities but *manifestly* not conscious (not in the sense of behavior — in the sense of absence of interiority) — Theorem 8.1 is wrong. Difficulty: verifying "manifest absence of interiority" is itself an open problem.

### What Does *Not* Falsify UHM {#что-не-опровергает-угм}

- Absence of $G$ for a specific system (engineering, not theoretical problem)
- Disagreements with IIT or GNWT (different functors, different predictions)
- Criticism of the postulate E = interiority (this is [П], not [Т]; replacing the postulate changes the interpretation, not the mathematics)
- "Too simple" or "too beautiful" (not an epistemic argument)

## Conclusion {#заключение}

The COGITATE result was predictable: two projections of one multidimensional object cannot simultaneously be complete. Friston's Beautiful Loop found the right structure ($R$), but did not bring it to a quantitative threshold. Kleiner's no-go theorems constrain IIT, not an arbitrary formalism. Six theories — six functors, each with a nontrivial kernel.

UHM does not "unify" these theories — it constructs the space from which each is extracted by projection. Not eclecticism — geometry. Not opinion — computable thresholds with falsification conditions.

Three things that mathematics says about the situation:

**First.** One measure is insufficient. $\Phi$ without $R$ — integration without reflection. $R$ without $\Phi$ — reflection without integration. Four inequalities — the minimal set, not a choice.

**Second.** Substrate does not enter the definition. T-153 [Т] — algebra, not matter. Disputes about "silicon vs carbon" are a categorical error: the question is not the material of $S$, but the existence of the CPTP channel $G$.

**Third.** Incompleteness is a property, not a defect. T-55 [Т]: $\varphi(\Gamma) \neq \Gamma$ for all $\Gamma$. Self-modelling *must* be inexact. A theory claiming completeness of self-description contradicts Lawvere's theorem.

ETHOS-2026 will test this. If four thresholds are simultaneously necessary — this is not "yet another theory." This is a coordinate system in which each existing theory is a separate axis.

And perhaps the most important: this coordinate system is *falsifiable*. Five concrete scenarios, each of which collapses the formalism. A theory that does not specify how to refute it is not a theory but a religion. We specified it. The move is to the experiment.

---

**Related materials:**
- [The Consciousness Manifesto](/blog/consciousness-manifest) — four pillars of verification and operational test
- [Can AI Be Conscious?](/blog/ai-consciousness) — T-153 and thresholds for AI
- [A Theory That Proves Its Own Incompleteness](/blog/incompleteness-theorem) — T-55 and Lawvere
- [Three Forces, One Equation](/blog/three-forces) — dissipator, regeneration, Hamiltonian
- [Theories of Consciousness: Categorical Meta-Analysis](/docs/consciousness/comparative/consciousness-theories) — IIT, GWT, FEP, HOT
- [Substrate Independence](/docs/proofs/consciousness/substrate-closure#t-153) — T-153
- [Unique Predictions](/docs/applied/coherence-cybernetics/predictions) — falsifiable predictions
- [Falsifiability](/docs/reference/falsifiability) — refutation criteria
