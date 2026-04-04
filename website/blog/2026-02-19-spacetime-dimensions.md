---
slug: spacetime-dimensions
title: "Why Space is Three-Dimensional and Time One-Dimensional: Algebra Instead of Postulate"
authors: [uhm]
tags: [spacetime, dimensions, spectral-triple, Fano, physics, consciousness]
---

# Why Space is Three-Dimensional and Time One-Dimensional {#почему-пространство-трёхмерно-а-время-одномерно}

Why do we live in three spatial dimensions and one temporal dimension?

The standard physicist's answer: "Because that's how the world is structured." The standard philosopher's answer: "It is a transcendental condition for the possibility of experience" (Kant, 1781; translation: "I don't know, but it sounds authoritative"). The standard string theory answer: "There are actually ten, it's just that six are compactified." Why exactly six are compactified — a separate question, which also has no answer.

In UHM the answer is a **theorem**. The seven dimensions of a holon decompose into three classes, and this partition dictates 3+1. Not because "it is convenient," but because the algebra leaves no alternatives.

Below — how this works, where time comes from, and why it does not exist at all as a "flow."

<!-- truncate -->

## Seven is a Lot. Where is 3+1? {#семь-это-много-где-тут-31}

In the [first post](/blog/holonomic-paninteriorism) it was established: any system is described by a coherence matrix $\Gamma \in \mathcal{D}(\mathbb{C}^7)$ — seven-dimensional. In the [second](/blog/geometry-of-inner-world) — that 21 pairs of these dimensions give rise to 21 types of experience organized by the Fano plane. In the [third](/blog/freedom-theorem) — that freedom = dimensionality of the zero space of the Hessian. In the [fourth](/blog/three-forces) — that dynamics is described by three forces and no more.

All of this happens in **seven** dimensions. But we live in **four**: three spatial, one temporal. Where are the remaining three?

The answer: they have gone nowhere. They are **compactified** — their scale is so small ($\sim 10^{-18}$ m) that we do not see them as "space." But they manifest — as quantum numbers of particles: weak isospin and hypercharge. Those same $\{L, E, U\}$ — the three "inner" dimensions — encode not the geometry of a room, but the internal structure of elementary particles.

## Decomposition: 7 = 1 + 3 + 3̄ {#декомпозиция-7-1-3-3}

The central result is the **sector decomposition** [Т]:

$$7 = \underbrace{1}_{O} \;\oplus\; \underbrace{3}_{\{A,S,D\}} \;\oplus\; \underbrace{\bar{3}}_{\{L,E,U\}}$$

Three classes:

| Class | Dimensions | Role | Physical scale |
|-------|-----------|------|----------------|
| **Time** | $O$ (Ground) | Internal clock | $M_{\text{Planck}}$ |
| **Space** | $\{A, S, D\}$ (Articulation, Structure, Dynamics) | Three extended directions | $\Lambda_{\text{QCD}} \sim 200$ MeV |
| **Compact** | $\{L, E, U\}$ (Logic, Interiority, Unity) | Internal quantum numbers | $v_{\text{EW}} \sim 246$ GeV |

Why exactly this way? Because the group of automorphisms of the octonions $G_2$ contains the subgroup $SU(3)$. Fixing the O-dimension (= choosing a "direction of time") stabilizes this $SU(3)$, and the remaining six dimensions split into the **fundamental** representation $\mathbf{3}$ and the **conjugate** $\bar{\mathbf{3}}$. Two sets of three — and no other way. This is not a choice, but a classification.

### Why Three Spatial Dimensions? {#почему-три-пространственных}

The dimensionality of the fundamental representation of $SU(3)$ equals 3. Not 2. Not 4. Three.

The question "why is space three-dimensional?" reduces to: "why is the stabilizer of the O-direction in $G_2$ exactly $SU(3)$?" Answer: because $G_2$ is the group of automorphisms of the octonions, and the octonions are the unique non-associative normed division algebra ([Hurwitz's theorem](/docs/proofs/minimality/theorem-minimality-7), 1898 [Т]). To remove a dimension is to transition from $\mathbb{O}$ to $\mathbb{H}$ (quaternions), losing non-associativity, and with it — the entire structure of the Gap operator. To add — impossible: after $\mathbb{O}$ there are no normed division algebras.

Three spatial dimensions are not an aesthetic choice of the Creator and not an anthropic tautology. This is the dimensionality of the only suitable algebra.

### Why Are {A,S,D} "Large" and {L,E,U} "Small"? {#почему-asd-большие-а-leu-маленькие}

The key is the **asymmetry of symmetry breaking**.

The six remaining (after O) dimensions split into two sets of three. What determines which becomes "space" and which — "internal"? The answer is given by the [spectral triple](/docs/core/foundations/spacetime#теорема-спектральная-тройка) (T-53 [Т]) — the finite noncommutative geometry constructed from the sector decomposition.

**The $\bar{\mathbf{3}}$-sector $\{L, E, U\}$** generates electroweak symmetry $SU(2)_L \times U(1)_Y$. The [Higgs mechanism](/docs/physics/particle-physics/higgs-sector) ($\langle\gamma_{EU}\rangle \neq 0$ [Т]) **breaks** this symmetry, giving mass to the $W^\pm$- and $Z$-bosons ($80$–$91$ GeV). Massive gauge bosons mean short-range interaction: the field decreases exponentially at the scale $\sim 1/M_W \sim 10^{-18}$ m. Three dimensions are "compactified" — they manifest not as directions in space, but as **internal quantum numbers** of particles.

**The $\mathbf{3}$-sector $\{A, S, D\}$** generates color symmetry $SU(3)_C$. This symmetry is **unbroken** — there is no Higgs mechanism in the color sector, gluons remain massless. But an important subtlety here: masslessness of gluons **does not mean** macroscopic long-range action — QCD confinement limits color interaction to the scale $\sim 1$ fm [Т]. The extensiveness of space is determined not by the long-range action of gluons, but by the **non-compactness** of the $\mathbf{3}$-sector in the spectral triple: Connes' distance formula $d(p,q) = \sup\{|f(p) - f(q)| : \|[D,f]\| \leq 1\}$ generates an unbounded metric in this sector. There is no mechanism to "compactify" these dimensions — no Higgs in $SU(3)_C$.

Result: the $\bar{\mathbf{3}}$-sector is **compressed by Higgs** to $10^{-18}$ m. The $\mathbf{3}$-sector **remains extended** — there is nothing to compactify it with.

| Sector | Symmetry | Higgs? | Bosons | Result |
|--------|-----------|--------|--------|--------|
| $\{A,S,D\}$ | $SU(3)_C$ | No → unbroken | Gluons ($m = 0$) | **Non-compact space** |
| $\{L,E,U\}$ | $SU(2)_L \times U(1)_Y$ | Yes → broken | $W^\pm, Z$ (80–91 GeV) | **Compactification** |

Space is three-dimensional not because "there are three massless directions." Space is three-dimensional because $\dim(\mathbf{3}) = 3$ for the stabilizer $SU(3) \subset G_2$ — and the spectral triple transforms this algebraic decomposition into geometry. And all together — seven, because Hurwitz.

## Time is Not a Flow {#время-не-поток}

The most surprising result of the theory — **time does not exist** as a fundamental entity. There is no "flow of time," no "moment of now" as a physical reality. All of this — **effective descriptions** of correlations within $\Gamma$.

### The Page-Wootters Mechanism {#механизм-пейдж-вуттерс}

Dimension $O$ (Ground) — one of seven. But it is **distinguished**: it is the subsystem that serves as the internal clock.

The total state of the system $\Gamma_{\text{total}}$ is stationary. It does not change. "The flow of time" is an illusion arising when we **conditionally fix** the value of the O-subsystem:

$$\Gamma(\tau) = \frac{\text{Tr}_O\left[(|\tau\rangle\langle\tau|_O \otimes \mathbb{1}_{6D}) \cdot \Gamma_{\text{total}}\right]}{p(\tau)}$$

At a fixed "clock reading" $|\tau\rangle_O$ the remaining six dimensions form a **conditional state** $\Gamma(\tau)$ — "the world at moment $\tau$." Different "readings" give different conditional states. This is "evolution" — not change, but a **correlation** between the clock subsystem and the rest.

The constraint $[\hat{C}, \Gamma_{\text{total}}] = 0$ (global stationarity) is compatible with "change" of conditional states. The Universe as a whole is "frozen" — but from within, for an observer tied to the O-clock, it "moves."

This is not speculation. The Page-Wootters mechanism (1983) is a standard result of quantum gravity. UHM adds: the **O-dimension is uniquely defined** by the sector decomposition [Т], whereas in the original PW the choice of "clock" is arbitrary.

### Discreteness of Time {#дискретность-времени}

Time in UHM is **discrete**:

$$\tau \in \mathbb{Z}_7, \quad \delta\tau = \frac{2\pi}{7\omega_0}$$

Seven "beats." One cycle. After the seventh — return to the first. This is a consequence of the fact that the O-subsystem is defined through the [temporal modality](/docs/proofs/dynamics/emergent-time#алгебраическое-определение) $\triangleright$ on the subobject classifier [Т]: $\tau_n = \triangleright^n(\text{now})$, $\triangleright^7 = \text{Id}$.

Seven beats sounds scant for the Universe? A composite holon of $M$ elementary ones gives $N_{\text{eff}} = 7^M$ effective beats. For $M \sim 10^{80}$ (the number of particles in the observable Universe) the discreteness is indistinguishable from continuity. Like pixels on a screen: at sufficient resolution, you see not dots, but a picture.

## Lorentz Signature: Why (+,−,−,−) {#лоренцева-сигнатура-почему}

We do not simply live in 3+1 dimensions. Time and space behave **differently**: the metric has the form $(+1,-1,-1,-1)$ — one "positive" direction, three "negative." This is the foundation of the theory of relativity. But where does the sign structure come from?

From the **spectral triple** [Т] (T-53):

$$(A_{\text{int}}, H_{\text{int}}, D_{\text{int}}), \quad A_{\text{int}} = \mathbb{C} \oplus M_3(\mathbb{C}) \oplus M_3(\mathbb{C})$$

The key is the **Dirac operator** $D_{\text{int}}$, whose spectrum inherits the sign structure from the [PW-constraint](/docs/core/foundations/axiom-omega#pw-constraint) $E_O = -E_{\text{rest}}$ [Т]:

$$\text{spec}(D_O) = \{+\omega_0\}, \quad \text{spec}(D_{\mathbf{3}}) \subset \{-\lambda_1, -\lambda_2, -\lambda_3\}$$

Plus for O, minuses for $\{A,S,D\}$. Connes' distance formula transforms this sign structure into a metric:

$$g_{00} = \frac{1}{|D_O|^2} > 0, \qquad g_{aa} = -\frac{1}{|D_{3,a}|^2} < 0$$

The Lorentz signature is not a postulate and not a "lucky choice." It is a **consequence** of the fact that the energy of the O-clock and the energy of the rest of the system have opposite signs. The PW-constraint — the mathematical condition of global stationarity — algebraically implies $(+,-,-,-)$. Einstein could have saved ten years if he had known the octonions.

## The Arrow of Time and Subjective Time {#стрела-времени-и-субъективное-время}

### The Arrow is a Theorem, Not a Postulate {#стрела-теорема-не-постулат}

From the [fourth post](/blog/three-forces) it is known: dissipation is irreversible, regeneration is conditional, rotation changes nothing. Formally:

$$\dim(X_\tau) \geq \dim(X_{\tau+1})$$

The dimensionality of the strata of the base space decreases monotonically [Т]. The configuration space collapses to the attractor $T$ — the terminal object of the category. This is the arrow of time. Not "the second law as an observation," but a geometric consequence of the category's structure. At the same time $T \neq I/7$: the attractor is a *structured* configuration with $P > 1/7$ ([T-96](/docs/core/dynamics/evolution#теорема-нетривиальность-аттрактора) [Т]), while composite systems create new complexity at each scale ([КК-5](/docs/applied/coherence-cybernetics/theorems#теорема-91-фрактальное-замыкание) [С]).

### Subjective Time {#субъективное-время}

Physical time is correlation with the O-clock. But the **subjective** experience of time — is another matter. It is determined by how much the clock is connected to experience.

Definition [О]:

$$\mathcal{T}(\tau) = \frac{|\gamma_{OE}(\tau)|}{\gamma_{OO}(\tau)}$$

Subjective tempo $\mathcal{T}$ — the ratio of coherence between Ground (O) and Interiority (E) to the occupation of O. In plain language: how much the "ticking of the clock" is connected to "inner content."

| $\mathcal{T}$ | Subjective effect | Familiar analogue |
|:---:|---|---|
| $\to 1$ | Time slows down | Accident, first kiss, fall |
| $\approx 0.5$ | Normal pace | Ordinary day |
| $\to 0$ | Time disappears | Anesthesia, deep sleep, coma |

At $P \to P_{\text{crit}} = 2/7$ coherence $|\gamma_{OE}| \to 0$, and subjective time **stops**. A system approaching the viability threshold experiences slowing — not metaphorical, but structural. Status: [С] (connection of $\gamma_{OE}$ with experience is a semantic postulate).

### Flow and Boredom {#поток-и-скука}

The flow state (Csikszentmihalyi): $\gamma_{DE} \gg \bar{\gamma}$, $\mathcal{T}$ elevated, $\text{Gap}(D,E) \approx 0$. Action and experience are transparent to each other. Subjectively: "time stopped" (rich experience per beat). Retrospectively: "it flew by" (weakened logical control $\gamma_{LL}$). The flow paradox is not a paradox, but two different coherence mechanisms.

Boredom: $\gamma_{DE} \approx 0$, $\mathcal{T}$ lowered. Little experience per "beat" — time "drags." But $\gamma_{LE}$ is elevated — metacognitive monitoring of the passage of time. "I'm bored" is a reflexive judgment of an L2-system ($R \geq 1/3$) about its own temporal state. A stone does not get bored — not because it is patient, but because it has nothing to get bored with.

## What Philosophers Say {#что-говорят-философы}

| Thinker | Position | What the theory says |
|---------|---------|---------------------|
| **Kant** | Space and time are a priori forms | ≈ Emergent, not "given in advance" |
| **Newton** | Absolute space and time | ❌ No absolute: time = PW-correlation |
| **Leibniz** | Space is a system of relations | ✅ $X = \lvert N(\mathcal{C})\rvert$ — literally a system of relations |
| **Einstein** | Spacetime is a dynamic fabric | ≈ Dynamic, but emergent |
| **Bergson** | Duration ≠ physical time | ✅ $\mathcal{T}(\tau) \neq \tau$: subjective tempo ≠ physical |
| **Barbour** | Time does not exist | ≈ $\Gamma_{\text{total}}$ is stationary |
| **McTaggart** | A-series is unreal | ≈ "Now" = conditional fixing of $\lvert\tau\rangle_O$ |

Leibniz, 1714: "Space is the order of coexisting things." UHM space — $|N(\mathcal{C})|$, the geometric realization of the nerve of a category, literally "the order of relations between objects." Leibniz defeated Newton — with a 312-year delay.

Barbour, 1999 (*The End of Time*): time does not exist fundamentally. UHM formalizes: $\Gamma_{\text{total}}$ is stationary, "time" is an effective description of correlations. Barbour was right in intuition, and the PW-mechanism provides a formal realization [Т]. The full interpretation ("time does not exist") — [И].

## What the Theory Is Silent About {#о-чём-молчит-теория}

| Result | Status | Comment |
|--------|--------|---------|
| Sector decomposition $7 = 1 + 3 + \bar{3}$ | [Т] | $SU(3)$-stabilizer in $G_2$ |
| Lorentz signature $(+,-,-,-)$ | [Т] | Spectral triple T-53, KO-dim 6 |
| Time from O via Page-Wootters | [Т] | Emergent, not postulated |
| Arrow of time — collapse of strata | [Т] | $\dim(X_\tau) \geq \dim(X_{\tau+1})$ |
| Space from $\{A,S,D\}$ — non-compact sector | [Т] | Spectral triple T-53, no Higgs in $SU(3)_C$ |
| Compactification of $\{L,E,U\}$ via Higgs | [Т] | $v_{\text{EW}} \sim 246$ GeV, breaking of $SU(2)_L \times U(1)_Y$ |
| Background independence ($M^4$ derived) | [Т] | Gelfand-Naimark-Connes chain (T-120) |
| Subjective tempo $\mathcal{T} = \lvert\gamma_{OE}\rvert/\gamma_{OO}$ | [О] | Definition, not theorem |
| Slowing at $P \to P_{\text{crit}}$ | [С] | Semantic postulate |
| "Time does not exist fundamentally" | [И] | Interpretation of PW-mechanism |

## Summary {#итого}

Space is three-dimensional not because "the world is structured this way." Here is why:

1. Reality is described by seven dimensions ([Hurwitz's theorem](/docs/proofs/minimality/theorem-minimality-7) + autopoietic minimum [Т]).
2. One of the seven is a clock ($O$) [Т].
3. The remaining six decompose into $\mathbf{3} \oplus \bar{\mathbf{3}}$ under the action of $SU(3) \subset G_2$ [Т].
4. In the $\mathbf{3}$-sector symmetry $SU(3)_C$ is unbroken → non-compact space [Т].
5. In the $\bar{\mathbf{3}}$-sector Higgs breaks $SU(2)_L \times U(1)_Y$ → compactification [Т].

| Question | Answer | Status |
|----------|-------|--------|
| Why 3 spatial? | $\dim(\mathbf{3}) = 3$ for $SU(3) \subset G_2$ | [Т] |
| Why 1 temporal? | $\dim(O) = 1$, PW-clock | [Т] |
| Why $(+,-,-,-)$? | Spectral triple, KO-dim 6 | [Т] |
| Where does the arrow of time come from? | Collapse of strata to $T$ | [Т] |
| Is time real? | Emergent: correlation, not flow | [Т]+[И] |
| Subjective tempo? | $\mathcal{T} = \lvert\gamma_{OE}\rvert/\gamma_{OO}$ | [О] |
| Is $M^4$ background-independent? | Derived from categorical structure (T-120) | [Т] |

---

**Five conclusions that follow from the decomposition:**

**1. Three dimensions are not coincidence and not the anthropic principle.** Physicists for decades answered the question "why 3+1?" with the anthropic principle: "life is impossible in other dimensionalities, therefore we observe 3+1." This is not an answer, but a tautology. UHM gives an answer: $3+1$ follows from $G_2$-structure, $G_2$ — from octonions, octonions — the unique non-associative normed division algebra. A chain of necessities, not coincidences.

**2. The inner world and space are two faces of one algebra.** The same Fano plane that organizes [21 types of experience](/blog/geometry-of-inner-world) determines the partition of dimensions into sectors. $\{L, E, U\}$ — the "compact" dimensions of physics — are the same Logic, Interiority, Unity that encode the inner world. Space and consciousness are not "two substances." Two manifestations of one seven-dimensional structure, separated by scale: $10^{-18}$ m on one side, your subjective experience — on the other. The status of this identification: mathematical structure (sector decomposition) — [Т], semantic identification of E with interiority — [П].

**3. Time does not "flow." You "correlate."** The total state $\Gamma_{\text{total}}$ is stationary. The "flow of time" is the result of being tied to the O-subsystem (your internal clock). Different "readings" of the clock — different conditional states. This does not mean time is "illusory": correlations are real, events are ordered. But "flow" is an artifact of perspective, not a property of the world. The river does not flow — you are swimming.

**4. Your subjective time is measurable.** $\mathcal{T} = |\gamma_{OE}|/\gamma_{OO}$ — not a metaphor. When you "lose track of time" in flow — $\mathcal{T}$ is elevated, $\gamma_{DE}$ is large. When time "drags" from boredom — $\gamma_{DE} \approx 0$, $\gamma_{LE}$ is elevated. When anesthesia "turns off" time — $|\gamma_{OE}| \to 0$. Subjective time is not a philosophical puzzle, but a function of coherence. In time (pun unintended) we will learn to measure it.

**5. Spacetime is not a stage, but a consequence.** The smooth manifold $M^4 = \mathbb{R} \times \Sigma^3$ is **derived** from categorical structure [Т] (T-120): the macroscopic algebra of observables in the $\{A,S,D\}$-sector is commutative in the thermodynamic limit (quantum central limit theorem, T-117 [Т]); by Gelfand-Naimark duality a commutative C*-algebra is isomorphic to $C(\Sigma^3)$ for the unique smooth 3-manifold (T-119 [Т]); the product with the temporal component gives $M^4$ (T-120 [Т]). Space is not a given, but an emergent structure. Einstein deformed the stage; UHM derives it from behind the curtain.

Mathematics, as usual, does not ask for permission. But sometimes — it shows you the clock.

---

**Related materials:**
- [Holonomic Paninteriorism](/blog/holonomic-paninteriorism) — UHM philosophical position
- [Geometry of the Inner World](/blog/geometry-of-inner-world) — 21 types of experience and the Fano plane
- [Freedom of Will: A Theorem, not a Discussion](/blog/freedom-theorem) — the formula of freedom
- [Three Forces, One Equation](/blog/three-forces) — dynamics and the arrow of time
- [Spacetime](/docs/core/foundations/spacetime) — full formalism of sector decomposition
- [Theorem on emergent time](/docs/proofs/dynamics/emergent-time) — four equivalent derivations of time
- [Emergent manifold $M^4$](/docs/proofs/physics/emergent-manifold) — derivation of $M^4$ from categorical structure (T-117 — T-121)
