---
sidebar_position: 7
title: "Premises of UHM"
description: "Every premise the current UHM corpus uses: axioms, named principles and hypotheses, free parameters, where each is used, its status, which premises are independent, which merge, and which results need none of them"
---

# Premises of UHM

:::info What this page is
One list of everything the corpus **assumes** rather than proves, as of 2026-09-26. Each entry names the premise, its status, the results that use it and what is known about deriving it. The [status registry](/docs/reference/status-registry) remains the canonical record of each result; this page is the canonical record of the inputs. A result that uses none of the premises in sections 2–4 is listed in section 6.

Status letters are those of the registry: **[P]** postulate (an axiom), **[H]** hypothesis (formulated, not proven — here a named assumption), **[Pr]** research programme, here a principle kept open (neither assumed as an axiom nor claimed proven), **[D]** definition by convention; **[I]** interpretation and **[C]** conditional theorem appear only where a row names them, as in the registry. A free parameter is not a statement and has no letter.
:::

## 1. How to read the list {#как-читать}

Three kinds of input are kept apart.

- **Axioms** fix the mathematical object: the ∞-topos, its metric, the dimension, the scale and the Page–Wootters constraint. Everything labelled "[T] as mathematics" in the corpus uses only these.
- **Bridge premises** say which part of that object is physical spacetime, matter or a self-model. They are the reason a result reads "[T] as mathematics, [C at (X)] as physics".
- **Identification hypotheses** of the flavour and vacuum sectors attach numbers to particle data. Several have been refuted in their exact form and survive only in a weaker one.

A premise counts as **used** when a live registry row or theorem carries `[C at (X)]` for it, or when its statement is an explicit step of a proof. A premise that has since become a theorem is listed in section 5 and is no longer an input.

## 2. Axioms [P] {#аксиомы}

| Premise | Statement | Used by | Status and what is known |
|---|---|---|---|
| **Metatheory** | ∞-categories / homotopy type theory as the language; intuitionistic internal logic | every page | outside the theory ([honest axiomatics](/docs/core/foundations/axiom-omega#аксиоматика)) |
| **A1** | reality is the ∞-topos $\mathbf{Sh}_\infty(\mathcal C)$ over $\mathcal D(\mathbb C^N)$ | all results | [P]; derivable from the operational basis only through the hypothesis T-186(a) (T-190) |
| **A2** | the Grothendieck topology is induced by the Bures metric | the topology, the stratification, T-173 | [P]; its topology is forced (every continuous distance on the compact $\mathcal D$ induces the standard one), and within the CPTP-monotone metrics Bures is canonical (T-187; the maximum-entropy recasting T-189) — what stays postulated is the monotonicity of the enrichment |
| **A3** | $N = 7$ | all results | [P]; $N \geq 7$ is [T] (Theorem S); strict necessity needs (P1₆), section 3 |
| **A4** | the scale $\omega_0 > 0$ | dynamics, calibration | [P]; its value is a free parameter, section 4 |
| **A5 constraint** | $\hat C\,\Gamma = 0$, the support condition $\mathrm{supp}\,\Gamma \subseteq \ker\hat C$ of Property 2 — the form of the timeless state | the Page–Wootters link of the clock (T-87, step 4), T-190 | [P]; the clock register and the tensor factor of A5 are [T] (T-87, steps 1–3); the constraint is not derived ([A5](/docs/core/foundations/axiom-omega#pw-constraint)) |
| **(QG)'s formalism** | states are density matrices, admissible maps are CPTP (definition O3) | all dynamics | [D]; "why quantum theory" stays external (T-188) |
| **Frame decision D-0910** | the dynamical frame group is $\Gamma_{\mathrm{oct}}$, 48 physical parameters | the dynamical half of the $G_2$-rigidity (42a), T-334 | [D] ([uniqueness theorem](/docs/proofs/categorical/uniqueness-theorem#g2-ригидность)) |

The independent content of the axioms is A1–A4 plus the constraint of A5. **Independence of the constraint** [T]: A1–A4 admit every density matrix on $\mathcal H_O \otimes \mathcal H_{\text{rest}}$, and $\ker\hat C$ is a proper subspace whenever $\hat C \neq 0$, so a state such as $\lvert\tau_0\rangle\langle\tau_0\rvert \otimes \rho$ with $\hat C(\lvert\tau_0\rangle \otimes \cdot) \neq 0$ satisfies A1–A4 and violates the constraint.

## 3. Bridge premises {#мостовые-посылки}

These are the free inputs that remain after four waves of repair (2026-09-25/26). Each has been tested against derivation, and for each the obstruction is stated.

### (P) — spacetime is built from the spinor factor [H] {#посылка-p}

**Statement.** The tangent vectors of spacetime at a point are the Hermitian forms on the spinor factor $W$ of the fermion field $F = W \otimes_{\mathbb C} \mathcal S_{\mathbb C}$; $\dim W \geq 2$; the causal structure, a quadratic form given up to a factor, is preserved by every transformation of $W$ that preserves UHM's internal structure ([Theorem 48e](/docs/core/foundations/spacetime#теорема-48e)).

**Equivalent forms.** (P) ⟺ (L) ∧ (W) [T, 48e(f)–(g)]: (L) says that tangent vectors form the observables of a two-level system with amplitudes in a composition subalgebra of $\mathbb O$ containing $e_O$; (W) says that the fermion field is a two-component Weyl field. (P) can be stated with any of 48e(g)(iii)–(vii) in place of the quadratic form: light rays are the pure states of $W$, space is isotropic in every rest frame, the group of $W$ is a Lorentz group, $W$ is a bit (the premise of Masanes and Müller), a Lorentz-invariant Weyl mass term exists.

**Used by.** The physical reading of [48c](/docs/core/foundations/spacetime#теорема-48c) — 3+1 dimensions, signature $(1,3)$, rotations that commute with colour — and the second route to the signature in the same page. Every result stated [C at (L)] uses it.

**Not derivable** [T, 48e(f)]: the commutant of UHM's internal operators on the generation is $\mathbb C'$, so the transformations preserving the internal structure are $\mathrm{GL}(n, \mathbb C')$ for every $n$, and nothing internal fixes $n$. Routes tried and closed: the clock's complex structure, the history state of the depth register, the two slots of a self-model, chirality and the Distler–Garibaldi test, the Masanes–Müller reconstruction, the spinor bundle of T-119's $S^3$ (reasons in 48e). Minimality does not replace it: the smallest spinor factor compatible with T-329 is $n = 1$, which leaves spacetime without a spatial direction ([T-347](#t-347)(d)).

### (Cl₀) — fermions are vectors of the spinor module [H] {#посылка-кл0}

**Statement.** Fermion fields take values in the spinor module $\mathcal S = \mathbb C \otimes \mathbb O$ of the octonionic Clifford system ([Standard Model, §2.6](/docs/physics/gauge-symmetry/standard-model#поколение-t329)). The second half of the former assumption (Cl) — that the clock breaks the spin group to the largest connected subgroup in which colour is a normal factor — is a theorem (T-329).

**Used by.** The physical reading of T-326, T-327 and T-329 (each [T] as mathematics, [C at (Cl)] in UHM), of T-332 and T-333, of the joint structure $F = (\mathbf 2, \mathbf{16})$ in 48e(e), and every flavour hypothesis of section 3.4, all of which are stated inside the frame of $\mathcal S$.

**Not derivable from axioms about Γ** [T for the obstruction]: $-1 \in \mathrm{SU}(2)_L$ acts as $-1$ on $\mathcal S$ and as $+1$ on $\mathrm{End}\,\mathcal S$, so every object built from coherence matrices, including their tensor products, has integer weak isospin; doublets are vectors of $\mathcal S$, not operators on it.

**Equivalent form without a named module** [T, [T-347](#t-347)(b)]: (Cl₀) ⟺ (Mod) — *the product of the holon's octonions (T15) acts on matter*: a real-linear $\rho:\mathbb O\to\mathrm{End}_{\mathbb R}(F)$ with $\rho(1) = 1$ and $\rho(x)\rho(x) = \rho(x^2)$, commuting with the $i$ of $\mathcal H$. Then $F \cong U \otimes_{\mathbb R} \mathcal S$, and $\mathcal S$, the parallel spinor $\eta_0$, the nine Clifford generators and $\mathrm{Spin}(9)$ are consequences. The model $\mathbb C^7$ of section 7 fails exactly (Mod). Routes closed by T-347: every property of the holon (a), the maximality of $\mathrm{Spin}(9)$ and a faithful representation of the holon's observables (c).

### (W₀) — the spinor factor is complex: not a free premise {#посылка-w0}

T-329 uses only that the spinor factor of the fermion field is a complex space of some dimension, (W₀). It is **implied** by (P), whose $W$ is complex. Given (Cl₀) it is **equivalent** to the requirement that one generation be chiral and anomaly-free [T, 48e(f),(h)]: with a real Lorentz factor every fermion space on $\mathcal S$ is anomalous or vector-like (h), and with a complex one it is chiral and anomaly-free for every $n$ (f). (W₀) is therefore a consistency condition of a chiral gauge theory together with the observed chirality, not an independent input.

### (MaxΦ) — the self-model's anchor is maximally integrated [Pr] {#посылка-максфи}

**Statement.** The anchor $\rho_a$ of the replacement-form self-model $k\,\mathcal P_\alpha(\Gamma) + R\,\rho_a$ is a state of maximal integration, $\Phi(\rho_a) = 6$ ([T-334](/docs/core/operators/phi-operator#t-334)).

**Equivalent forms** [T, T-334(6)]: (Eq-V) — the self-model privileges no axis (its atomic reading is $\Gamma_{\mathrm{oct}}$-covariant) and is the most viable such; $\rho_a = D\,uu^\dagger D^\dagger$ with $D$ diagonal unitary; maximal relative entropy of coherence, $C_{\mathrm{rel}}(\rho_a) = \log 7$; coherent purity $s = 6/7$. It splits into two halves: (Eq), uniform diagonal, and (Pure), a pure anchor.

**Used by.** The choice of $\varphi_J$ among the self-models the axioms allow: the living attractor of an isolated holon in the window ([evolution](/docs/core/dynamics/evolution#t-335)), the isolated-holon half of C27, the collineation-anchored level of the septicity table. The dynamics of each anchor — T-334 (1)–(5), T-335, T-336 — is [T] without it; the premise decides only which anchor a physical holon has.

**Not derivable from the axioms**: the self-modelling adjunction and the terminal object make $\varphi$ a CPTP left adjoint and leave its anchor open (every anchor gives a channel of the same form). Routes closed in T-334: Curie's principle (gives the family $D((1-t)I/7 + t\,uu^\dagger)D^\dagger$, not $t = 1$), the terminal object (gives (Eq) only), Lawvere and Brouwer (fixed points, not anchors), viability alone. Section 7 adds the routes through the corpus's variational principles.

### (P1₆) — P1 for a competing decomposition [H] {#посылка-p16}

**Statement.** P1 holds for any decomposition covering (AP)+(PH)+(QG), not only for the seven-dimensional one ([strict necessity of N = 7](/docs/proofs/minimality/theorem-minimality-7#теорема-строгая-необходимость-7)).

**Used by.** The strict necessity of $N = 7$ (excluding a rival six-function decomposition) and the maximality half of the double extremality through Track B. $N \geq 7$ does not use it.

**Status.** The chain T1–T15 proves P1 for the frame it starts from, whose step T8 consumes $N = 7$ from Track A; the orientation input (Alt) of that chain is discharged (T15-canon, section 5). No model of a competing decomposition is known, so independence is open.

### Flavour, vacuum and identification hypotheses [H] {#гипотезы-отождествления}

| Premise | Statement | Used by | Status |
|---|---|---|---|
| **(SV)** | the sector values of the Gap vacuum ($\varepsilon_{33}$, $\bar\varepsilon = O(10^{-2})$) | T-69, T-70, T-79–T-81, T-99 (conclusion retracted 2026-09-26), T-120b(ii), T-176, T-180, T-185b, T-216, T-219, C35 and the Λ-budget | [H]; as the vacuum of $V_{\text{Gap}}$ it is refuted [✗] by T-64; it survives only as an independent hypothesis, and under (Cl₀)+(GC) it no longer carries a family index (T-332) |
| **(GC)** | a generation is a non-trivial real harmonic of the clock register | $N_{\text{gen}} = 3$ in the harmonic reading (T-328), the mixing discussion | [H]; the exact family $\mathbb Z_3$ is refuted by $\lvert V_{us}\rvert \approx 0.224$ — only the broken form survives |
| **(UP)** | only up-type fields couple to the Higgs doublet at tree level (holomorphy in one complex doublet) | T-332, the Dirac neutrino mass | [H] at leading order; the exact form is refuted [✗] (it leaves $e$, $\mu$, $\tau$ massless to all orders, T-332(i)) |
| **(PQ)** | an added Peccei–Quinn sector | the Gap-axion table of dark matter and confinement | [H]; the Clifford content has no Peccei–Quinn symmetry and no spontaneous CP violation (T-333(e)–(h)); strong CP is open [Pr] |
| **(FE)** | the electroweak group acts on $\mathrm{span}\{L,E,U\}$ of the system factor | the axis-frame electroweak construction (T-175b, T-219, T-265) | [H]; replaced by (Cl₀) in the Clifford frame, still carried by the axis-frame pages |
| **(SA)** | sector asymmetry of the vacuum Gap profile | neutrino generation assignments, T-219 | [H]; T-52 retired as a theorem |
| **Higgs identification** | $H \sim \gamma_{EU}$ (axis frame); the colour-free plane as the Higgs doublet (Clifford frame, T-329(f)) | the Higgs sector | [H] in both frames |
| **T-186(a)** | the cohesive route to A1 | T-190 (axiomatic closure) | [H] |
| **Physical reading of $M^4$** | the reconstructed $M^4 = \mathbb R \times S^3$ (T-118, T-119, T-120) is physical spacetime | T-120 and T-121 as physics | [I], as in the registry rows T-119 and T-120, which are [T] as mathematics; the former reconstruction conditions of T-119 and the aperiodic time parameter are discharged (section 5); T-120b(ii) stays [C at the vacuum symmetry] through T-64 and (SV), and T-87 as a Page–Wootters mechanism uses the A5 constraint of section 2 |
| **(HOL)** | a composite of holons is itself a holon, with its own dynamics on $\mathcal D(\mathbb C^7)$ | the literal reading of CC-5 and of the population rungs | [I]; not derivable (dimension 49, not 7); CC-5 and CC-6 hold at weak coupling without it |

## 4. Free parameters {#свободные-параметры}

| Parameter | Where | What is known |
|---|---|---|
| $\kappa$, weight of the associator cubic in $V_{\text{Gap}}$ | T-64, T-331 | **Free** [T]: no derived source carries it (T-331(e)); its weight is $0$ for every functional of the isolated dynamics (T-331(f)). Both phases occur: for $0 < \kappa \leq \mu^2/48$ the vacuum is $I/7$, for $\kappa > \min(7\mu^2/48, \kappa_1)$ the Gap is spontaneous with orbit $S^6$ (T-64) |
| $\mu^2$, $\lambda_4$ | $V_{\text{Gap}}$ (T-64) | free couplings of the potential |
| regeneration rate $\kappa$, Fano weight $\alpha$ | the evolution equation, T-334–T-336, T-346 | **Free** [T]: the window needs $\kappa \geq 11.83,\ 20.91,\ 42.64$ at $\alpha = 0,\ \tfrac12,\ 1$ for every self-model (T-336); no route fixes the value above it (T-346) — the threshold $\kappa_c$ of $\varphi_J$ has Galois group $S_7$, the attractor has no interior optimum, the fold survives no detuning, every norm balance with $\mathcal{D}_\Omega$ gives $\kappa g_V \le 1$ against the needed $\ge 1.70$, the categorical $\kappa(\Gamma)$ moves the freedom into $\omega_0$, and composition has only trivial fixed points |
| $\omega_0$ | A4 | the scale; its value differs between holons |
| phase reference $D$ of $\varphi_J$ | T-334(4) | a gauge of the $H$-free dynamics; physical only relative to a non-diagonal $H$ |
| $\bar\theta_{\mathrm{QCD}}$ | T-333, T-99 (corrected 2026-09-26) | free in the Clifford content [Pr]; no $G_2$-invariant Gap term fixes it ([Confinement §3.1c](/docs/physics/gauge-symmetry/confinement#тета-не-из-потенциала)) |

## 5. Premises discharged — no longer inputs {#снятые-посылки}

| Former premise | Discharged by | Date |
|---|---|---|
| (Alt): the Fano orientation is the normed one | [T15-canon](/docs/proofs/minimality/theorem-octonionic-derivation#каноническая-ориентация): the unique orientation class invariant under the 168 collineations | 2026-09-25 |
| (MP) | T11–T13 (Choi rank, L-unification, forced BIBD) | earlier |
| (MM): elementary systems can be entangled | 48e(b): a theorem inside UHM | 2026-09-25 |
| (Q) = (Q1) ∧ (Q2) | replaced by the weaker (L), now (P); (Q) still suffices | 2026-09-25/26 |
| second sentence of (Cl) | T-329: the clock's stabiliser | 2026-09-25 |
| (RT), the real twirl inequality | proven (T-64, Lemma 3) | 2026-09-25 |
| (Col), (Pure) | (Col) follows from (Eq-V); (Pure) is equivalent to maximal viability under (Eq) (T-334) | 2026-09-25 |
| (AGG) | Theorem 9.5 at weak coupling (CC-5, CC-6) | 2026-09-25 |
| (ND) | CC-7 for almost every anchor | 2026-09-25 |
| (CG) | T6, uniform contraction from $S_7$-equivariance | earlier |
| the open reconstruction conditions of T-119 | T-119 restated: the spatial algebra is $C(S^3)$, and all seven of Connes' conditions hold for its Dirac triple (T-120 and T-121 raised to [T] as mathematics with it) | 2026-09-25 |
| an aperiodic time parameter | the depth register: $A_{\text{time}} \cong C_0(\mathbb R)$ as its scaling limit (T-118, T-53b) | 2026-09-25 |

## 6. Results that use no premise of sections 3–4 {#безусловные}

These are [T] from the axioms of section 2 alone (the metatheory, A1–A4, the constraint where stated, the definitions O3 and D-0910):

- **Structure of the primitive.** Cohomological monism and local non-triviality; the octonionic structure from (AP)+(PH)+(QG)+(V) through T15 with the canonical orientation (row 41n); $N \geq 7$ (Theorem S); $G_2$-rigidity (42a, T-123); rigidity of the primitive (T-173); the universal property of the kinematic object (T-174); PhysTheory as a Grothendieck construction (T-211); the encodings T-171 and T-172.
- **Time.** The clock register (T-87, steps 1–3); the depth register and its dissipative arrow (T-53b); the time line as its scaling limit (T-118).
- **Dynamics and consciousness.** Non-emptiness of the conscious window (T-124); dead isolation for every unital self-model; the anchor theorems T-334 (1)–(5), T-335, T-336 for every anchor; no-signalling of the full dynamics (Theorem 8.5).
- **Vacuum.** The $G_2$-invariant potentials (T-331) and the vacuum phases of $V_{\text{Gap}}$ as functions of the free $\kappa$ (T-64).
- **As mathematics.** 48c, 48d, 48e; T-119, T-120; T-326–T-329, T-332, T-333. Their physical readings carry the premises named in section 3.

## 7. Independence and mergers {#независимость}

**Method.** A premise X is independent of the others when there is a model in which all the others hold and X fails. Two premises merge when one statement is proven equivalent to their conjunction and is strictly weaker than asserting them separately — that is, when the merged form reduces the number of independent inputs. Numerical witnesses are in `website/scripts/check_core_numbers.py` (`test_spinor_factor_premise_and_fermion_module_premise_are_independent`, `test_anchor_principle_is_independent_and_attractor_integration_does_not_replace_it`, `test_fermion_module_premise_is_the_holons_product_acting_on_matter`, `test_no_holon_property_maximality_or_minimality_gives_the_bridge_premises`).

### Independence [T] {#модели-независимости}

| Fails | Model in which every other premise holds | Why X fails |
|---|---|---|
| (P) | $F_3 = \mathbb C^3 \otimes_{\mathbb C} \mathcal S_{\mathbb C}$, with any anchor and any $\kappa$ | by 48e(f) every statement about the generation holds for $n = 3$ (anomalies $\times 3 = 0$, chirality); by 48e(g) $\mathrm{Herm}(\mathbb C^3)$ carries no $\mathrm{SL}$-invariant quadratic form (count 0), so no causal structure is preserved |
| (Cl₀) | $F = W \otimes_{\mathbb C} M$ with $W = \mathbb C^2$ and $M = \mathbb C^7$, the holon's own vectors with $\mathfrak g_2$ and the $i$ of $\mathcal H$ | the commutant of $\{\mathfrak g_2, i\}$ on $\mathbb R^{14}$ has dimension 2 (it is $\mathbb C$; without $i$ it is $M_2(\mathbb R)$, dimension 4), so the structure-preserving transformations of $W$ are $\mathrm{GL}(W)$ and (P) holds with $\det$; but $\dim_{\mathbb R}\mathbb C^7 = 14$ is not a multiple of 16, so $M$ is not a $\mathrm{Cl}_7$-module |
| (MaxΦ) | anchor $\rho_t = (1-t)I/7 + t\,uu^\dagger$, $t = 0.9$, $\alpha = \tfrac12$, $\kappa = 100$ | (Eq) holds and a living sink exists in the window, but $\Phi(\rho_t) = 6t^2 = 4.86 < 6$; the unital anchor $I/7$ ($\Phi = 0$) satisfies all axioms and gives dead isolation |
| (Eq) half | a pure anchor with non-uniform diagonal (amplitudes $1 \pm 0.3$, a sink at $\kappa = 50$, T-335) | the anchor is pure, its diagonal is not $I/7$ |
| (Pure) half | $\rho_t$ above | the diagonal is uniform, the anchor is mixed |
| $\kappa$ | $V_{\text{Gap}}$ with two values of $\kappa$ | both are consistent with every other premise and give different vacua (T-64) |
| A5 constraint | a state off $\ker\hat C$ | section 2 |

(P1₆) and the flavour hypotheses of section 3.4 are not in the table: no model of a competing decomposition is known, and the flavour hypotheses are stated inside the frame of (Cl₀), so they presuppose it.

### (P) and (Cl₀): one sentence, two independent inputs {#слияние-p-кл0}

**Proposition** [T]. Let (P̂) be the single statement "matter is a Weyl spinor of the clock-commuting Clifford module": the fermion field is $F = W \otimes_{\mathbb C} \mathcal S_{\mathbb C}$ with $\mathcal S$ the spinor module of the octonionic Clifford system, and spacetime's tangent vectors are the Hermitian forms on $W$, $\dim W \geq 2$, with a causal form preserved by every internal-structure-preserving transformation of $W$. Then

1. (P̂) is exactly (P) as the corpus states it, which already names $\mathcal S_{\mathbb C}$; hence (P) as stated contains (Cl₀) and (W₀);
2. (P̂) ⟺ (Cl₀) ∧ (P\*), where (P\*) is (P) for an arbitrary fermion module $M$ in place of $\mathcal S_{\mathbb C}$ whose internal commutant is $\mathbb C$;
3. (Cl₀) and (P\*) are independent: the two models of the table above realise (Cl₀) ∧ ¬(P\*) and (P\*) ∧ ¬(Cl₀).

*Proof.* (1) is the wording of 48e. (2): given (Cl₀), (P\*) with $M = \mathcal S_{\mathbb C}$ is (P); conversely (P̂) names $\mathcal S$. (3) is the table. $\blacksquare$

So the merger exists as a statement and does not reduce the inputs: the conjunction of two logically independent premises stays two premises. The reason is structural. (Cl₀) is about the internal module, and 48e(f) proves that the internal structure is blind to $W$; (P\*) is about $W$, and the $\mathbb C^7$ model shows that it is blind to the internal module. The accounting used on this page is therefore (Cl₀) plus (P) relative to (Cl₀), with (W₀) contained in both readings.

### (MaxΦ) and the variational principles of the corpus: no derivation {#максфи-и-вариационные-принципы}

**Proposition.** None of the variational principles that the corpus states yields (MaxΦ):

1. **The retracted cross-entropy principle** ([FEP derivation](/docs/proofs/dynamics/fep-derivation)): its minimiser is the projector onto the top eigenvector of $\Gamma$, an intrinsic anchor; intrinsic anchors are spectral and phase-covariant, so they hold no hyperbolic attractor in $\mathcal V_{\mathrm{full}}$ near $H = 0$ ([phase-reference obstruction](/docs/core/dynamics/evolution#теорема-фазовое-препятствие)), and they are not constant [T].
2. **(MaxEnt)** of the operational basis selects the Bures metric (T-189). Applied to the anchor itself it gives $I/7$, $\Phi = 0$, the opposite of (MaxΦ); applied to the atomic reading of the anchor it gives only (Eq) [T].
3. **(V), viability**: the anchor $\rho_t$ of the table lives in the window with $\Phi(\rho_t) < 6$ [T, numerical witness]. **Maximal viability** alone picks anchors with non-uniform diagonal (T-334(6)).
4. **Maximal integration of the living attractor** (a new candidate, not stated in the corpus). For a constant anchor the window attractor at $H = 0$ depends only on $d = \sum_i (\rho_a)_{ii}^2$ and $s = P(\rho_a) - d$, and its integration is $\eta^2 s/d$ with $\eta$ the top root of $\eta = B(P)/A(P)$, $P = d + \eta^2 s$ (T-335). At fixed $d$ it grows with $s$ [T: the root moves right as $s$ grows], so the maximiser is pure. But in the band $\kappa_c(\alpha) < \kappa < \kappa_*(\alpha)$, $\kappa_* \approx 1.012\,\kappa_c$, a pure anchor with slightly non-uniform diagonal beats $uu^\dagger$: at $\alpha = 0$, $\kappa = 16.8$, $d = 1/7 + 10^{-4}$ gives $\Phi_{\mathrm{att}} = 1.25155$ against $1.25148$ [T by the witness]. Above the band $uu^\dagger$ wins on every tested grid (40 diagonals × 3 purities at $\alpha = 0$, $\kappa = 20$), [H] as a global statement. So this principle agrees with (MaxΦ) only above $\kappa_*$, and below $\kappa_c$ — where $uu^\dagger$ has no living attractor and non-uniform anchors do — it contradicts it.

(MaxΦ) therefore stays [Pr]. What the analysis adds: it is the conjunction of two independent halves, (Eq) and (Pure); (Eq) is the terminal object read on the axes and (Pure) is maximal viability under (Eq); a principle about the observable attractor rather than the anchor reproduces it except in a band of relative width $1.2\,\%$ above $\kappa_c$.

### Routes from the holon to (Cl₀), (P) and (W): T-347 {#t-347}

The independence table shows that (Cl₀) and (P) do not follow from the present axioms. T-347 takes the next question: which property of the holon, which extremal principle or which minimal strengthening would give them. It answers route by route.

:::tip Theorem T-347 (the bridge premises of physics against the holon) — [T] as mathematics
**(a) No property of the holon decides the bridge premises.** (Cl₀), (P) and (W₀) are statements about the fermion field $F$, which A1–A5 do not mention. Each model of the independence table can be built over one and the same holon: any $\Gamma$, anchor, $\alpha$ and $\kappa$, in particular a living holon in the window $2/7 < P \le 3/7$ with the anchor $uu^\dagger$. Viability, the window, the self-model and its anchor, regeneration, the 168 Fano collineations and the $G_2$-rigidity therefore hold or fail in those models exactly as in the intended one. The holon's symmetry does not see the difference either: as a $\mathfrak g_2$-module, $\mathcal S = \mathbb C\eta_0 \oplus \mathcal H$ is the holon's Hilbert space plus a trivial line. What separates $\mathcal S$ from every space built from $\mathcal H$ is the centre of the spin cover. The rotation by $2\pi$ in the plane of two axes is $\exp(\pi L_{e_1}L_{e_2}) = -1$ on $\mathbb O$ and $+1$ on $\mathbb R^7$ and on every tensor built from it. The genuinely spinorial modules of $\mathrm{Spin}(7)$ have dimensions $8, 48, 112, \dots$; the tensorial ones have $1, 7, 21, 27, 35, \dots$.

**(b) (Cl₀) is equivalent to the holon's product acting on matter.** Let (Mod) be the statement: there is a real-linear map $\rho:\mathbb O\to\mathrm{End}_{\mathbb R}(F)$ with $\rho(1) = 1$ and $\rho(x)\rho(x) = \rho(x^2)$ for every $x$ — the left alternative law of the holon's octonions — that commutes with the imaginary unit $i$ of $\mathcal H$. Then (Mod) ⟺ (Cl₀): $F \cong U \otimes_{\mathbb R} \mathcal S$ for a real multiplicity space $U$, and on every copy the Clifford system of T-326 is forced. The smallest $\rho$- and $i$-stable space containing $\mathcal H$ is $\mathcal S$. The independence model $M = \mathbb C^7$ fails exactly (Mod).

**(c) Maximality and faithfulness presuppose (Mod).** The Hurwitz–Radon number of $\mathbb R^{14}$ is $\mathrm{HR}(14) = 2$. So the holon's $\mathcal H$ carries at most one complex structure of an anticommuting family (its $i$), and $\mathbb C^7$ has no quaternionic structure. Seven anticommuting complex structures need $8 \mid \dim$: $\mathrm{HR}(8) = 8$, $\mathrm{HR}(16) = 9$, $\mathrm{HR}(14) = \mathrm{HR}(98) = 2$. The maximality of $\mathrm{Spin}(9)$ in T-326(a) — nine generators on $\mathbb R^{16}$ — is a statement about Clifford systems inside a module that (Mod) supplies, and it cannot select the module. Faithful representations of the holon's observable algebra $M_7(\mathbb C)$ have real dimension $14k$. $\mathcal H$ itself ($k = 1$) is faithful and is not a module of $\mathbb O$, and a space that carries both has dimension divisible by $112$. So faithfulness forces nothing.

**(d) Minimality gives $n = 1$, not (W).** By 48e(f) every statement of T-329 holds on $\mathbb C^n \otimes_{\mathbb C} \mathcal S_{\mathbb C}$ for every $n \ge 1$. The smallest spinor factor compatible with T-329 is therefore $n = 1$: $F_1 = \mathcal S_{\mathbb C}$, sixteen left-handed Weyl fields with $\sum Y = \sum Y^3 = 0$, chiral. But $\mathrm{Herm}(\mathbb C^1) = \mathbb R$, so spacetime would have no spatial direction. Minimality under the extra clause "a spatial direction exists" gives $n = 2$ ($\dim \mathrm{Herm} = 4$). That clause plus Occam's razor is an input of the same kind as the boost clause of (P), not a derivation. The only source of the "2" with content is the boost invariance of 48e(g).

**(e) The independence model of (Cl₀) is not chiral.** On $M = \mathbb C^7$ the $\mathfrak g_2$-matrices are real, so $M$ is isomorphic to its conjugate and every Weyl field on it is vectorlike. Gauging the $\mathrm U(1)$ of $i$ instead gives $\operatorname{Tr} Q = \operatorname{Tr} Q^3 = 7$ per component of $W$, an anomaly. So (Cl₀) is independent of the axioms and of (P\*), not of the observed chirality. Whether chirality and anomaly freedom select $\mathcal S$ among all fermion modules built from UHM's structures is open [Pr]; on $\mathcal H$ itself the centraliser of colour in $\mathrm U(7)$ is $\mathrm U(1)^3$ and holds no weak $\mathrm{SU}(2)$ ([Standard Model, §2.1](/docs/physics/gauge-symmetry/standard-model)).
:::

**Proof.** (a) The premises are about $F$ and $W$, and the holon is a separate factor of each model, so every property of the holon has the same value in all of them. $\mathfrak g_2$ acts on $\mathbb O$ by derivations, which kill $1$. $L_{e_1}L_{e_2}$ squares to $-1$, and the rotation by the angle $\theta$ in the $(e_1, e_2)$-plane lifts to $\exp(\tfrac\theta2 L_{e_1}L_{e_2})$; at $\theta = 2\pi$ this is $-1$, and conjugation by $-1$ is trivial on every operator. The dimensions come from Weyl's formula for $B_3$ with highest weights in $(\mathbb Z + \tfrac12)^3$ and in $\mathbb Z^3$ (Humphreys, *Introduction to Lie Algebras and Representation Theory*, Springer 1972, §24).
(b) On $\mathrm{Im}\,\mathbb O$ we have $x^2 = -\lvert x\rvert^2$, and polarising $\rho(x)^2 = \rho(x^2)$ gives $\rho(a)\rho(b) + \rho(b)\rho(a) = -2\langle a, b\rangle$. So $F$ is a module of $\mathrm{Cl}_{0,7} \cong M_8(\mathbb R) \oplus M_8(\mathbb R)$ (Lawson and Michelsohn, *Spin Geometry*, ch. I §4). Its two irreducible modules are eight-dimensional and differ in the sign of the volume element: they are $\mathbb O$ with $L$ (volume $-1$) and $\mathbb O$ with $R$ (volume $+1$), and both obey the law because $\mathbb O$ is alternative. With $i$ commuting, each isotypic part of $F$ is $U_\pm \otimes_{\mathbb R} (\mathbb C \otimes \mathbb O)$. Octonionic conjugation $c$ satisfies $cL_{e_k}c = -R_{e_k}$ and commutes with $i$ and with the conjugation $J$. It carries the system $\{iR_{e_k}, J, iJ\}$ to $\{-iL_{e_k}, J, iJ\}$, which generates the $\mathfrak{spin}(9)$ of T-326. So both parts are $\mathcal S$ with the group of T-326, and $F \cong (U_+ \oplus U_-) \otimes_{\mathbb R} \mathcal S$. Conversely, $\mathcal S$ with $\rho = L$ satisfies (Mod). $\mathcal H$ is not $\rho$-stable because $e_k e_k = -1$; its closure is $\mathcal S$ (fact (i) of [Standard Model, §2.6](/docs/physics/gauge-symmetry/standard-model#поколение-t329)).
(c) $\mathbb R^n$ carries $\mathrm{HR}(n) - 1$ anticommuting complex structures and no more, with $\mathrm{HR}(2^{4a+b}\cdot\text{odd}) = 2^b + 8a$, $0 \le b \le 3$ (Hurwitz 1923, Radon 1922). A quaternionic structure on $\mathbb C^7$ would be $K = A\kappa$, with $\kappa$ the complex conjugation, and $K^2 = -1$ means $A\bar A = -1$; but $\det(A\bar A) = \lvert\det A\rvert^2 \ge 0$ and $\det(-1_7) = -1$. The remaining statements are dimension counts.
(d) 48e(f) and the charge table of T-329(d).
(e) The generators of $\mathfrak g_2$ are real antisymmetric matrices, so complex conjugation intertwines $M$ with $\bar M$. The charge of $i$ is $1$ on each of the seven complex dimensions. $\blacksquare$

*Numbers* (`test_fermion_module_premise_is_the_holons_product_acting_on_matter`, `test_no_holon_property_maximality_or_minimality_gives_the_bridge_premises`):
- $L$ and $R$ satisfy $\rho(x)^2 = \rho(x^2)$ for random $x$; the algebra generated by the seven $L_{e_k}$ on $\mathbb R^8$ has dimension $64$ and commutant of dimension $1$; the volume elements are $-1$ for $L$ and $+1$ for $R$; $cL_{e_k}c = -R_{e_k}$ for all seven;
- $\{iR_{e_k}, J, iJ\}$ satisfies the relations of $\mathrm{Cl}(9,0)$ on $\mathbb R^{16}$; the operators anticommuting with the seven $iR_{e_k}$ form a space of dimension $2$; its $\mathfrak{spin}(9)$ lies in $c\,\mathfrak{spin}(9)_L\,c$ to $10^{-9}$; the closure of $\mathcal H$ (rank $14$) under $L_{e_k}$ and $i$ has rank $16$;
- $\mathfrak g_2$ kills $\eta_0$; $\exp(\pi L_{e_1}L_{e_2}) = -1$ on $\mathbb O$, the $2\pi$-rotation is $+1$ on $\mathbb R^7$; spinorial $\mathrm{Spin}(7)$-dimensions $8, 48, 112$, tensorial $1, 7, 21, 27, 35$;
- $\mathrm{HR}(8) = 8$, $\mathrm{HR}(14) = 2$, $\mathrm{HR}(16) = 9$, $\mathrm{HR}(98) = 2$; $\det(A\bar A) > 0$ for five random $A \in M_7(\mathbb C)$; $\operatorname{lcm}(14, 16) = 112$;
- $F_1$: $16$ fields, $\sum Y = \sum Y^3 = 0$; $\dim \mathrm{Herm}(\mathbb C^n) = 1, 4, 9$ for $n = 1, 2, 3$; one $\mathrm{SL}$-invariant quadratic form at $n = 2$; $\operatorname{Tr} Q = \operatorname{Tr} Q^3 = 7$ on $\mathbb C^7$.

**What T-347 changes.** No status changes. (Cl₀) and (P) stay [H]; the physical readings of T-326, T-327, T-329, T-332 and T-333 stay [C at (Cl)], and that of 48c stays [C at (L)]. What changes is the form of (Cl₀). It no longer names a module or a Clifford system: it says that the product the holon already has (T15) acts on matter, and $\mathcal S$, $\eta_0$, the nine generators and $\mathrm{Spin}(9)$ follow. The premise sits exactly at the centre of the spin cover. The holon, its symmetries and everything built from $\Gamma$ are tensorial, while matter is spinorial, and no property of the holon can take that step (a). For (P), the only non-trivial content is the boost clause; minimality alone gives a spacetime without space (d). The routes asked for on 2026-09-26 are closed: a property of the holon that the models violate by (a), the maximality of $\mathrm{Spin}(9)$ and a faithful representation of the observables by (c), the minimality of the spinor factor by (d).

### Other pairs {#другие-пары}

- **(P) and (MaxΦ)** live in different factors (the spinor factor of matter, the anchor on $\mathbb C^7$); the $F_3$ model with anchor $uu^\dagger$ satisfies (MaxΦ) and not (P), the $\rho_t$ model with $n = 2$ satisfies (P) and not (MaxΦ). Independent.
- **(P1₆) and (P)**: (P1₆) concerns the dimension of the state space, (P) the spinor factor of matter; no implication is known either way. Open.
- **$\kappa$ and (MaxΦ)**: $\kappa$ weights a cubic of $V_{\text{Gap}}$, which the isolated dynamics does not see (T-331(f)); the anchor lives in the self-model. Independent.

## 8. Count {#итог}

After the four waves of 2026-09-25/26 the free inputs of UHM are: the axioms A1–A4 and the constraint of A5 [P]; two bridge premises of physics, (Cl₀) and (P) relative to it [H]; one principle of the self-model, (MaxΦ) [Pr]; the strict-necessity premise (P1₆) [H]; the free parameters of section 4, $\kappa$ among them; and the identification hypotheses of section 3.4, three of which, (SV), (GC) and (UP), survive only in weakened form. Every other input used earlier has been discharged (section 5). (Cl₀) has an equivalent form, (Mod), in which the holon's product acts on matter; T-347 closes the routes that would derive it or (P) from a property of the holon, from maximality or from minimality.
