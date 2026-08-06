---
sidebar_position: 3
title: "Many-Worlds (Everett–Deutsch) and UHM"
description: "A rigorous comparison: what UHM says about parallel universes — point of maximal kinship (Page–Wootters relative states), the no-branching theorem-level argument, the preferred-basis contribution, and a falsifiable fork"
---

# Many-Worlds (Everett–Deutsch) and UHM

:::info Who this chapter is for
David Deutsch (Oxford) is the strongest living advocate of Everett's
many-worlds interpretation (MWI): *The Fabric of Reality* (1997),
*The Beginning of Infinity* (2011), the decision-theoretic derivation
of the Born rule (1999), and — with Chiara Marletto — constructor
theory. This chapter states **precisely** where UHM agrees with,
where it strictly diverges from, and what it *contributes to* the
many-worlds programme. Every claim carries a status marker and a
link to the corpus theorem it rests on. Nothing here is rhetorical.
:::

## 1. The formal core of MWI (Deutsch's form)

To compare rigorously, fix MWI as Deutsch defends it:

| # | MWI commitment | Formal content |
|---|---|---|
| M1 | Universal state | One pure state $\lvert\Psi\rangle$ of everything; no external observer |
| M2 | Dynamics | **Only** unitary evolution $U(t) = e^{-iHt}$; no collapse, ever |
| M3 | Branching | Decoherence splits $\lvert\Psi\rangle$ into quasi-classical branches ("worlds") |
| M4 | Preferred basis | Supplied by environment-induced einselection (Zurek) |
| M5 | Probability | Born weights recovered from rational-agent decision theory (Deutsch 1999) |
| M6 | Evidence claim | Quantum computation: "where was Shor's factorisation computed, if not across worlds?" |

## 2. Point-by-point rigorous comparison

### 2.1 The ontic carrier: $\lvert\Psi\rangle$ vs $\Gamma$ — strict divergence [Т]

UHM's fundamental object is not a universal pure vector but a
**density operator** $\Gamma \in \mathcal{D}(\mathbb{C}^7)$ on the
∞-topos site ([Axiom 1](/docs/core/foundations/axiom-omega#аксиоматика)).
This is not a notational choice; it carries a theorem-level
consequence for the very *definability* of worlds:

:::tip No-branching argument [Т, linear algebra]
A mixed state admits **no canonical convex decomposition**: for any
non-extremal $\Gamma$ there are uncountably many ensembles
$\{(p_k, \lvert\psi_k\rangle)\}$ with
$\Gamma = \sum_k p_k \lvert\psi_k\rangle\langle\psi_k\rvert$, and no
internal fact of $\Gamma$ selects one (classical theorem; the
Schrödinger–HJW purification freedom). Therefore, **if the
fundamental object is $\Gamma$, "worlds" as components of the state
are not invariantly definable.** Branch-talk in UHM can only ever be
*basis-relative bookkeeping*, never ontology.
:::

Everett's move (M1) is only available if the fundamental state is
pure. UHM's [No-Zombie / viability structure](/docs/core/foundations/axiom-septicity#v-жизнеспособность)
*requires* mixedness ($P < 1$ for every viable holon, with the
conscious window $P \in (2/7, 3/7]$ — [T-124](/docs/proofs/consciousness/conscious-window#t-124)):
a pure-state holon is non-viable. So the divergence at M1 is not
aesthetic — **UHM's living systems are constitutively mixed, and
mixedness kills canonical branching.**

### 2.2 Dynamics: unitarity-only vs the triad — strict divergence [Т]

MWI's M2 says the generator is $-i[H,\cdot]$ and nothing else. UHM
proves ([T-57, LGKS completeness](/docs/core/operators/lindblad-operators#полнота-триадной-декомпозиции))
that the axioms force exactly **three** dynamical contributions:

$$
\mathcal{L}_\Omega = \underbrace{-i[H,\cdot]}_{\text{Aut}}
+ \underbrace{\mathcal{D}_\Omega}_{\text{Fano dissipator}}
+ \underbrace{\mathcal{R}}_{\text{regeneration}}
$$

with $\mathcal{D}_\Omega$'s decoherence rate an exact number,
$\lambda_{\text{deco}} = 5\gamma/21$
([T-59](/docs/core/foundations/axiom-omega#теорема-kappa-bootstrap-bound),
machine-verified 2026-08-05 by the 49×49 superoperator: spectrum
exactly $\{0, -5\gamma/21\}$), and $\mathcal{R}$ the *non-unitary,
non-linear* replacement flow toward $\rho_*$
([39f–h](/docs/core/dynamics/evolution#объединённая-теорема-r)).
In MWI decoherence is **descriptive** (a consequence of $U$ acting
on system⊗environment); in UHM dissipation and regeneration are
**generative** — part of the law itself. A holon does not branch;
it *metabolises* coherence.

### 2.3 Preferred basis: UHM's contribution to the MWI programme [Т]

MWI's weakest joint (M4) is well known: einselection answers "which
basis survives decoherence" by pointing at the interaction
Hamiltonian — and leaves "why *that* interaction" open. UHM closes
this joint structurally:

- the measurement basis is the **atomic structure of the classifier
  $\Omega$** ([Theorem 6.1](/docs/physics/quantum-mechanics/measurement#6-предпочтительный-базис)) —
  logic, not environment;
- the frame itself is rigid up to $G_2 = \mathrm{Aut}(\mathbb{O})$
  ([T-42a, Stone–von-Neumann analogue](/docs/proofs/categorical/uniqueness-theorem#g2-ригидность));
- and the seven atoms are not anonymous: they are the derived
  dimension set $\{A,S,D,L,E,O,U\}$ with
  [7/7 functional uniqueness [Т]](/docs/proofs/minimality/theorem-minimality-7).

**Read against Deutsch**: this is the exact structure MWI would need
to *earn* its quasi-classical domains rather than borrow them from
the environment. It is exportable: even a committed Everettian can
take the $\Omega$-atomic answer to M4 as a standalone result.

### 2.4 The Born rule: two derivations, different premisses [Т]/[С]

Deutsch (1999) recovers Born weights from decision-theoretic axioms
(rational preference over quantum games); critics (Barnum et al.)
press circularity. UHM derives measurement probability from the
**Bures geometry forced by the axioms**: the unique monotone metric
characterisation ([T-187](/docs/proofs/categorical/cohesive-closure#53-closing-the-last-open-question-why-bures-t-187))
plus the classifier-projection reading of measurement
([§3, Born rule from UHM](/docs/physics/quantum-mechanics/measurement#3-правило-борна)).
Statuses differ: Deutsch's route imports rationality axioms **[П]**
in our vocabulary; UHM's route stays inside A1–A2 **[Т]** with the
interpretive bridge confined to what "measurement" names **[И]**.

### 2.5 Page–Wootters: the point of maximal kinship [Т]

Here the two programmes genuinely touch. Everett's original name was
the *relative-state* formulation; Deutsch has always emphasised
this. UHM's Axiom 5 — now a theorem
([T-87: A5 derivable from A1–A4](/docs/core/foundations/axiom-omega#pw-constraint)) —
is precisely a relative-state construction: a global constrained
state $\hat{C}\Gamma_{\text{total}} = 0$ whose **conditional states
relative to the clock sector** are the experienced instants
([T-38b, emergent time](/docs/proofs/dynamics/emergent-time)).

So UHM *does* host a rigorous plurality: the $\mathbb{Z}_7$ family
of clock-conditioned states co-present in one timeless $\Gamma$.
The strict difference from MWI: this plurality is **temporal**
(seven phases of one holon), not **modal** (alternative outcomes),
and its cardinality is fixed by the algebra (7), not exponentiating
with every interaction. Call it what it is [И]: *co-present moments,
not parallel worlds.*

### 2.6 "Where was Shor computed?" — UHM's answer [Т]/[И]

Deutsch's M6 argument takes exponential quantum speed-up as direct
evidence of parallel worlds. UHM answers without multiplying
ontology: the computation lives in the **off-diagonal sector of one
$\Gamma$** — the same coherences whose Frobenius weight defines
$\Phi$ ([integration measure](/docs/core/structure/dimension-u#мера-интеграции-φ))
and whose cooperative surplus is exactly
$P(\rho^{(12)}_*) - P(\rho_{\text{diag}}) = 2\lVert\gamma_{\text{cross}}\rVert_F^2$
([T-77](/docs/consciousness/ethics-meaning/value-consciousness#теорема-кооперация)).
Amplitude paths interfering within one state are *resources*, not
*places*. The quantitative UHM-native measure of "how much parallel
room" a configuration has is
$\mathrm{Freedom}(\Gamma) = \dim\ker(\mathcal{H}_\Gamma) + 1$
([finite-dimensional theorem [Т]](/docs/core/foundations/consequences#freedom-конечномерное)) —
flat directions of one landscape, bounded by 7, never $2^n$ worlds.

### 2.7 The falsifiable fork [П]

The comparison yields one experiment-class divergence, stated
honestly:

:::warning Fork (macro-interference of living matter)
**MWI (pure unitarity)**: no principled ceiling on interference
visibility for arbitrarily complex systems — with sufficient
isolation, a virus, a cell, a holon interferes.

**UHM**: any *viable* system carries the internal Fano dissipator
with rate $\lambda_{\text{deco}} = 5\gamma/21 > 0$ [T-59] **by law,
not by environment**. Perfect isolation does not switch it off
(it is part of $\mathcal{L}_\Omega$, [T-57]). Hence a hard ceiling:
interference visibility of a *living* (viable, $P > 2/7$,
$\mathcal{D}_\Omega \neq 0$) system decays at least at
$\lambda_{\text{deco}}$ regardless of shielding.

**Discriminator**: matter-wave interferometry approaching the living
threshold (large biomolecules → viruses → viable cells). Persistent
full-visibility interference of a demonstrably *viable* system would
falsify the UHM triad; a shielding-independent visibility floor
matching $5\gamma/21$ scaling would falsify unitarity-only MWI.
Status: research programme [П] — the numbers ($\gamma$ per system)
need the $\omega_0$-calibration layer.
:::

### 2.8 The Fabric's four strands — structural concordance [И]

Deutsch's *Fabric of Reality* weaves four strands and claims they
form one explanatory fabric. UHM, built independently, arrives at a
four-strand structure with exact counterparts — evidence that the
fabric intuition tracks something real:

| Deutsch's strand | UHM counterpart | Where |
|---|---|---|
| Quantum theory (Everett) | $\Gamma$, Bures topos, triad dynamics | A1–A2, T-57 |
| Epistemology (Popper) | Reflection $R$, self-model $\varphi$, falsifiability registry | [Self-observation](/docs/consciousness/foundations/self-observation), [Falsifiability](/docs/reference/falsifiability) |
| Computation (Turing) | Classification of computations; $\Phi$-classes | [Consequences §Computation](/docs/core/foundations/consequences#классификация-вычислений) |
| Evolution (Darwin) | Autopoiesis (AP), viability V, regeneration $\mathcal{R}$ | [Septicity](/docs/core/foundations/axiom-septicity) |

And constructor theory's counterfactual primitives ("possible /
impossible transformations") have a working UHM analogue: the
threshold catalogue ($P_{\text{crit}}$, $R_{\text{th}}$,
$\Phi_{\text{th}}$, the conscious window) *is* a catalogue of
possible-versus-impossible configurations, maintained with
registry discipline.

## 2.9 The learning-theoretic bridge: UHM fixes Vanchurin's free function [Т]

Deutsch's multiverse and Vanchurin's *self-learning universe* are the
two live programmes that derive physics from something more primitive
(branching worlds; learning dynamics). UHM engages the second one
quantitatively, and the result is a set of exact theorems (T-293–295,
full derivations in `internal/vanchurin-bridge/`):

Vanchurin parametrises the learning algorithm by the functional
relation $g=\kappa^{a}$ between metric and noise covariance
(*Geometric framework for biological evolution*, arXiv:2603.15198,
Eq. 6.8), with $a=0$ (stochastic gradient), $a=\tfrac12$ (efficient
learning — Adam-like, conjectured to underlie biological complexity)
and $a=1$ (natural gradient, the "quantum regime"), and states that
direct estimates of $\kappa$ remain unavailable. In UHM **neither
factor is free**: $g$ is Bures (unique monotone metric, T-187) and
$\kappa$ is the Kraus-increment covariance of the canonical
dissipator (T-41/T-59). Computing both gives

$$
\kappa^{\uparrow\uparrow}_{\text{at}}=\frac{\gamma}{4N}\,g^{-1}
\qquad\Longleftrightarrow\qquad
\Pi\,g\,\kappa_{\text{at}}\,\Pi=\frac{\gamma}{4N}\,\Pi ,
$$

which is *verbatim* his own criterion for $a=1$: substituting $a=1$
into his Eq. 7.5 yields exactly $g^{-1}=g^{-1}\kappa g^{-1}$. Hence
$a=1$ exactly. (The constant is $\gamma/4N$ because the Bures metric
is one **quarter** of Fisher–Rao on commuting perturbations, not one
half; in the SLD-QFI normalisation used in the natural-gradient
literature the identity reads $\gamma\Pi/N$. The exponent and all
ratios below are independent of that choice.)

Three companions, all state-independent. The universal Fano factor
$\operatorname{Tr}(g\kappa_{\text{full}})/\operatorname{Tr}(g\kappa_{\text{at}})=11/9$
at matched per-channel rate — equivalently, the block layer carries
exactly $2/11$ of the noise. The noise–purity law
$\operatorname{Tr}\kappa=\frac{\gamma}{N}(1-P)$, so the conscious
window becomes a learning-noise band $[4\gamma/49,5\gamma/49)$. And a
sector split: $\kappa^{\text{coh}}=0$ on the decohered manifold,
where coherences instead contract deterministically at $5\gamma/21$ —
stochastic learning noise does not reach them. Three consequences
deserve emphasis:

1. **What is a modelling choice for him is a theorem here.** The
   relation $g^{-1}\propto\kappa^{\uparrow\uparrow}$ is his $a=1$
   condition, one option among three; UHM derives it. It is the
   *dynamical* counterpart of the *static* identity $g^{-1}=c$ that
   his §4 obtains from a maximum-entropy argument, where $c$ is the
   population covariance. Granting that static identity too, the two
   together predict $\kappa^{\uparrow\uparrow}=\frac{\gamma}{4N}c$ —
   the covariance of *temporal changes* has the same shape as the
   *static* covariance, differing by a single scalar that is a pure
   rate. One side is routinely measured; the other, he notes, never
   has been.
2. **A falsifiable disagreement**: UHM predicts that a viable learner
   sits at $a=1$ with Fano-induced anisotropy, *not* at the
   $a=\tfrac12$ regime conjectured for biological complexity.
3. **The test needs no metric.** His Eq. 7.5 degenerates at
   $a=\tfrac12$, where $\kappa^{\uparrow\uparrow}=I$ carries no
   information about $g$ at all. So the two hypotheses make opposite
   *shape* claims about one measured object: $a=\tfrac12$ makes
   $\kappa^{\uparrow\uparrow}$ spherical, while $a=1$ makes it
   proportional to $\operatorname{diag}\lambda-\lambda\lambda^{\top}$,
   computable from the state alone. A sphericity test on about a
   hundred aggregated time windows separates them. Its resolving power
   vanishes at the maximally mixed state and grows away from it — so
   the theory predicts that the systems it calls holons, sitting in
   the window $P\in(2/7,3/7]$, are exactly the systems in which its
   own central claim is measurable.

Read together with §2.6: Deutsch asks *where* the computation
happens and answers "in other worlds"; Vanchurin asks *what algorithm*
the world runs; UHM answers the second question with numbers and, in
doing so, removes the need for the first — the computation happens in
the coherence sector of one state, and the learning happens in its
complement.

## 3. Summary verdict

**What UHM strictly says about parallel universes:**

1. **No ontological branching** [Т-level argument]: the fundamental
   state is mixed (viability forces $P < 1$), mixed states have no
   canonical decomposition, and the law itself is the non-unitary
   triad — three independent blockers, any one of which suffices.
   The topos is one; there is no outside for worlds to sit in
   ([T-55/T-56, No Outside](/docs/core/foundations/consequences#структурная-toe)).
2. **Maximal kinship at Page–Wootters** [Т]: UHM is a
   relative-state theory *of time* — seven co-present
   clock-conditioned states of one $\Gamma$; Everett's machinery,
   capped cardinality, temporal not modal.
3. **A genuine contribution to MWI's own programme** [Т]: the
   $\Omega$-atomic, $G_2$-rigid preferred basis — the missing answer
   to M4 — stands independently of whether one accepts branching.
4. **The quantum-computation argument is answered without worlds**
   [Т]/[И]: coherences of one state are the resource; Freedom counts
   the flat directions and is bounded by 7.
5. **One honest experimental fork** [П]: a law-level decoherence
   floor for living matter versus unitarity's unbounded
   interference — a real, eventually decidable disagreement.

*Related pages:* [Measurement](/docs/physics/quantum-mechanics/measurement) ·
[QM reduction](/docs/physics/quantum-mechanics/qm-reduction) ·
[Emergent time](/docs/proofs/dynamics/emergent-time) ·
[Consciousness theories compared](/docs/consciousness/comparative/consciousness-theories)
