---
slug: /proofs/categorical/uniqueness-theorem
sidebar_position: 3
title: "Representation rigidity and operational identifiability"
description: "Conditional octonionic symmetry rigidity, finite-time flow injectivity, and the separate identification problem"
---

# Representation Rigidity and Operational Identifiability

:::info Revised 2026-10-03
A symmetry theorem classifies transformations that preserve a **specified** structure. It does not establish that two empirical encoders are related by such a transformation. The former unconditional representation-uniqueness theorem (registry rows 42a and T-123), including its Stone–von Neumann analogy, is withdrawn [✗]. This page replaces it with precise conditional rigidity and identification results.
:::

## Three different questions {#проблема}

1. **Forward uniqueness:** does a given initial matrix have one trajectory under a specified vector field?
2. **Structural rigidity:** which changes of coordinates preserve an octonionic form, frame and specified dynamics?
3. **Operational identifiability:** do observed data determine a unique initial matrix and a unique encoder?

The first two are mathematical questions under stated hypotheses. The third needs a calibrated observation law and proof of injectivity on a stated domain. Ontological primacy of $\Gamma$ does not make a data-to-state map injective.

## Representations and comparison maps {#определения}

### Encoder {#определение-представления}

Let $S$ carry a physical semiflow $\Psi_t$ and let $F_t$ be a specified state-space semiflow. A dynamics-compatible encoder is a continuous map

$$
G:\mathrm{States}(S)\to\mathcal D(\mathbb C^7),\qquad
G\Psi_t=F_tG.
$$

This is a semiconjugacy; it need not be injective, surjective, affine, or reconstructible from measurements. If it is a homeomorphism onto the entire state space, it is a topological conjugacy, still not automatically a quantum-channel isomorphism.

### Equivalence as additional data {#определение-эквивалентности}

Two encoders are equivalent **by definition** under a chosen structure group $K$ if $G_2=\operatorname{Ad}_gG_1$ for $g\in K$, with all frame labels transported consistently. To prove this one must establish a comparison map with the required properties. The expression $G_2G_1^{-1}$ is undefined unless $G_1$ is injective; it is defined only on its image unless surjectivity has also been established.

### Structure and gauge {#определение-калибровки}

Specify which tensors, frame labels, Hamiltonian, clock, anchor and readouts are held fixed and which are transported. The stabilizer of those data is the corresponding structure group. A stabilizer theorem alone cannot make every possible encoder equivalent.

## Forward evolution: strengthened lemmas {#леммы}

### Lemma G1: finite-time propagator injectivity {#лемма-g1}

**[T].** For every finite-dimensional linear generator $L$ and finite $t$, $e^{tL}$ is invertible as a linear operator, with inverse $e^{-tL}$. Hence it is injective on the trace-zero tangent space whenever that space is invariant. No primitivity, diagonalization, or spectral-gap assumption is needed.

For a quantum Markov generator, $e^{tL}$ is CPTP for $t\geq0$; $e^{-tL}$ need not be positive or physically executable. Therefore exact recovery of a known trajectory's initial state is different from reversible dynamics. Recovery may be exponentially ill-conditioned: for $L(\rho)=\sigma-\rho$ on trace-one states, differences shrink by $e^{-t}$ and reconstruction amplifies their noise by $e^t$. The infinite-time reset loses injectivity despite injectivity at every finite time.

### Lemma G2: nonlinear flow injectivity {#лемма-g2}

**[T at local Lipschitz regularity and state invariance].** Suppose $\dot\Gamma=f(\Gamma)$ is an autonomous, locally Lipschitz vector field on an open affine neighborhood of the state set, and solutions starting in that set remain there. Compactness then supplies global forward solutions, and every finite-time flow map is injective.

*Proof.* Picard–Lindelöf gives local uniqueness. If two solutions meet at time $t$, solve the reversed local equation from their common endpoint; uniqueness identifies them on a preceding interval. Repeating along the compact portions of the trajectories identifies them back to the initial time. Compactness and invariance prevent finite-time escape. $\square$

Linear terms, rational weights with $P\geq1/7$, a locally Lipschitz anchor, and a clamp gate satisfy local Lipschitz regularity. A top-eigenvector selection at degeneracy may not. A singular coefficient with denominator $\gamma_{OO}$ needs an actual regularity assumption or extension; bounded values alone do not prove Lipschitz continuity.

Neither lemma proves injectivity of a sensor map, an encoder $G$, or a partial-observation trajectory. Equal observations can arise from different nonintersecting state trajectories.

## Octonionic and frame structures {#предпосылки}

The following statements assume a **specified positive octonionic three-form** $\varphi_3$ on $\mathbb R^7$, its complex extension and a chosen orthonormal coordinate frame. Their validity does not prove that arbitrary physical observations uniquely acquire this structure. The dimension and octonionic construction have the separate premises described in [minimality](/docs/proofs/minimality/theorem-minimality-7) and [mathematical kernel](/docs/reference/mathematical-kernel).

### Lemma G3: fixed numerical data {#лемма-g3}

The seven projectors, Fano filters, selected E/O/U labels, clock extension, anchor law and regeneration rate are representation data or additional proved constructions at their stated hypotheses. They are not all consequences of one subobject classifier. No adjunction between arbitrary dissipation and regeneration derives their scalar coefficients. The minimal $\mathbb C^7$ is not a nontrivial clock tensor product; an extension must be supplied explicitly.

### Lemma G4: stabilizer of the three-form {#лемма-g4}

**[T at the specified form].** For the complex extension of a fixed real positive octonionic three-form,

$$
\{U\in U(7):U^*\varphi_3=\varphi_3\}=G_2\times\mu_3,
\qquad \mu_3=\{I,\omega I,\omega^2I\},\quad\omega^3=1.
$$

Scalar phases act trivially on density matrices, so its conjugation action is that of $G_2$. Here $U^*\varphi_3$ means tensor pullback, not conjugate transpose on a matrix. The real stabilizer is the compact octonion automorphism group $G_2\subset SO(7)$; see Baez, [*The Octonions*](https://arxiv.org/abs/math/0105155).

*Proof.* Its Lie algebra consists of $X=A+iS\in\mathfrak u(7)$ with $A$ real skew and $S$ real symmetric. Since the form is real, $X\cdot\varphi_3=0$ implies that both real components stabilize it. Its real stabilizer Lie algebra is $\mathfrak g_2\subset\mathfrak{so}(7)$; thus $S=0$ and the identity component is $G_2$. Every other element normalizes this component. Compact $G_2$ has only inner automorphisms, so after multiplication by an element of $G_2$ the normalizing element commutes with its irreducible complex seven-dimensional representation. Schur's lemma makes it a scalar $\lambda I$. Preservation of the three-form imposes $\lambda^3=1$. Conversely all these elements preserve the form. $\square$

### Frame decision D-0910, with its precise scope {#g2-ригидность}

The form stabilizer above is a kinematic structure group. Preserving the coordinate pinching introduces a frame. Inside $G_2$ its stabilizer is the finite signed-frame group $\Gamma_{\mathrm{oct}}$ of order $1344$. Further fixed Hamiltonian, clock, E/O/U labels and a nonunital anchor can reduce the group again. Their actual common stabilizer must be computed; pinching alone does not prove that the full model has exactly $1344$ physical identifications.

Treating a frame as physical is model data [D]. A finite change of axes with transported labels is a relabelling; a rotation with frame labels held fixed may change observables. This distinction is retained independently of the withdrawn encoder-uniqueness theorem.

### Frame rigidity, real versus complex symmetries {#жёсткость-репера}

**Theorem [T].** For $\Phi(\rho)=\sum_{i\ne j}|\rho_{ij}|^2/\sum_i\rho_{ii}^2$:

- its maximal conjugation symmetry in $O(7)$ is the signed permutation group;
- its maximal conjugation symmetry in $U(7)$ is the monomial unitary group $U(1)^7\rtimes S_7$ (the scalar $U(1)$ acts trivially);
- its real intersection with the three-form stabilizer is $\Gamma_{\mathrm{oct}}\subset G_2$, of order $1344$.

*Proof.* A pure coordinate state has $\Phi=0$. Its image under $U$ also has $\Phi=0$ iff the corresponding column of $U$ has precisely one nonzero entry: $\sum_i|v_i|^4=1$ for a unit vector iff it is a coordinate vector up to phase. Therefore every symmetry is monomial. Conversely monomial conjugation permutes diagonal entries and preserves all off-diagonal moduli. In the real case the phases are signs. Preserving $\varphi_3$ restricts the permutation to a Fano collineation with eight compatible signed lifts. The kernel of the permutation action has the eight simplex-code signings, yielding $8\cdot168=1344$. $\square$

The earlier statement that $\Phi$ has **no continuous symmetry at all** is withdrawn [✗]: diagonal complex rephasings are continuous symmetries. It has no positive-dimensional symmetry **inside $G_2$**. This theorem classifies a specified observable's symmetries, not all encoders.

$\mathrm{Coh}_E$ is preserved by the $192=1344/7$ elements of $\Gamma_{\mathrm{oct}}$ preserving the E-axis, when that label is fixed. If labels are transported, it is read on the transported axis. $\kappa_0$ with fixed O/E/U labels generally has a smaller stabilizer. Equal-weight Fano and atomic pinching are covariant under all monomial unitaries, while neither is covariant under all of $G_2$.

<a id="теорема-единственности"></a>

## Replacement for universal representation uniqueness {#теорема}

### Conditional operational rigidity [T at (RI)]

Assume two encoders $G_1,G_2$ are bijections onto $\mathcal D(\mathbb C^7)$ and that their comparison $T=G_2G_1^{-1}$ is a **quantum-channel isomorphism**: both $T$ and $T^{-1}$ extend to linear CPTP maps. Assume also that its implementing unitary has a lift preserving the specified three-form. Call these joint bridge hypotheses **(RI)**. Then

$$
G_2=\operatorname{Ad}_gG_1\quad\text{for one }g\in G_2.
$$

If the coordinate frame is fixed as a set, $g\in\Gamma_{\mathrm{oct}}$; if additional labelled data are fixed, $g$ belongs to their common stabilizer. This is a theorem about encoders satisfying (RI), not a derivation of (RI) from viability or flow uniqueness.

### Proof {#доказательство}

Both maps preserve fidelity monotonically; applying each followed by its CPTP inverse forces equality of fidelity for every pair. Their affine bijection maps extreme (pure) states bijectively to pure states. Wigner's theorem then gives unitary or antiunitary conjugation on pure states, and affinity extends it to mixed states. In dimension at least two, antiunitary conjugation is not completely positive (its transposition Choi operator has a negative eigenvalue), so $T=\operatorname{Ad}_U$ for a unitary $U$. The specified three-form lift and Lemma G4 give $\operatorname{Ad}_U=\operatorname{Ad}_g$ with $g\in G_2$. Since the image of $G_1$ is all states, two such $g$ differ by a scalar; the center of compact $G_2$ is trivial, proving uniqueness. Frame and label preservation impose the stated stabilizers. $\square$

A primary precise statement of Wigner's required **pairwise transition-probability preservation** is Géher, [*An elementary proof for the non-bijective version of Wigner's theorem*](https://arxiv.org/abs/1407.0527). Merely preserving the spectrum of each individual matrix is insufficient: all pure states have the same spectrum, yet an arbitrary state-dependent rotation need not preserve their mutual transition probabilities.

### Why the former proof fails {#аналогия}

The previous proof assumed $G_1^{-1}$ without injectivity, assumed spectrum preservation without an observational calibration, and then invoked Wigner without pairwise probability preservation or an affine state-space automorphism. Neither visiting a trajectory near an attractor nor primitivity ensures that an encoder image contains a 48-dimensional open set: one orbit is one-dimensional, and a constant equilibrium encoder is dynamics-compatible. Tietze's extension theorem does not give a unique affine, spectrum-preserving extension of an arbitrary map. Continuity also does not exclude an antiunitary component without a specified homotopy through admissible symmetries.

**Concrete compatibility counterexample [T].** At $H=0$ with pinching dissipation and $M_s$, every diagonal flat-on-support density matrix $\rho=P_V/\mathrm{rank}(P_V)$ is an equilibrium. Both $|e_1\rangle\langle e_1|$ and $(|e_1\rangle\langle e_1|+|e_2\rangle\langle e_2|)/2$ have $P>2/7$. The two constant encoders to these matrices satisfy the same dynamical compatibility equation, but have different spectra and cannot be related by any unitary. Thus compatibility and the numerical purity criterion do not imply the former uniqueness claim. Extra faithful representation requirements are indispensable.

## What can actually be identified {#следствия}

### Kinematic orbit dimension {#физические-состояния}

The unconstrained trace-one state space has real dimension $48$. The generic $G_2$ orbit has dimension $14$, so the principal orbit-space stratum has dimension $34$ [T at the specified action]. A diagonal positive matrix with distinct entries has only a finite orthogonal commutant, giving a witness of a zero-dimensional $G_2$ stabilizer; minimal stabilizer dimension occurs generically. Distinct eigenvalues alone do not ensure this for every complex Hermitian state: some states commuting with a Cartan torus have continuous stabilizers.

Quotienting by a finite frame group leaves dimension $48$. These are counts on the specified unconstrained state space, not a theorem that a chosen sensor protocol measures all parameters, or a global coordinate list of 34 independent invariant scalars.

### Observation injectivity and stability {#обратная-задача}

Let a calibrated observation map be $h$, with observation history $\mathcal O_T(\rho)=\{h(F_t\rho):0\leq t\leq T\}$. Initial-state reconstruction requires $\mathcal O_T$ to be injective on the admissible domain, and robust reconstruction additionally requires a quantitative inverse estimate. Flow injectivity from Lemmas G1–G2 does not establish either requirement for $h$.

**Constructive tomography [T].** In a fixed calibrated frame, probabilities for the seven coordinate projectors and the $42$ projectors onto $(e_i+e_j)/\sqrt2$ and $(e_i-i e_j)/\sqrt2$, $i<j$, determine $\rho$ uniquely:

$$
p_i=\rho_{ii},\quad
q_{ij}^{R}=\tfrac12(p_i+p_j)+\operatorname{Re}\rho_{ij},\quad
q_{ij}^{I}=\tfrac12(p_i+p_j)+\operatorname{Im}\rho_{ij}.
$$

These are separately calibrated two-outcome measurements, not one normalized 49-effect POVM. The one trace relation leaves 48 independent real quantities. Their linear observation operator $A$ on $\mathrm{Herm}_0(7)$ has a positive least singular value, hence $\|\delta\rho\|_F\leq\|\delta y\|_2/\sigma_{\min}(A)$. This proves a particular identification protocol. It does not turn EEG features or a learned encoder into these quantum probabilities without a separate empirical bridge. [Watrous, chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.double.2.pdf).

### Functor faithfulness versus object separation {#верность-функтора}

A faithful functor is injective on **each hom-set/mapping space** in the relevant categorical sense. It need not be injective on objects up to isomorphism. Conversely object separation alone does not prove faithfulness. The former inference $F(\Gamma_1)\cong F(\Gamma_2)\Rightarrow\Gamma_2=g\Gamma_1g^\dagger$ was an additional object-identification claim and is withdrawn with universal encoder rigidity [✗]. A readout of an E-sector need not retain the rest of $\Gamma$; a contractive readout can collapse distinct states to one output. A concrete realization must prove its own object separation and morphism action.

### Invariants and predictive scope {#инварианты}

$P$, $R=1/(7P)$ and the spectrum are unitarily invariant. $\Phi$ and $\mathrm{Coh}_E$ reference the chosen frame; their symmetries are stated above. Rigidity restricts coordinate transformations under (RI), but it fixes no empirical encoder, parameter calibration or predictive accuracy. A small structure group does not by itself make a theory maximally predictive.

<a id="предсказательная-мощность"></a>

## Remaining work {#открытые-вопросы}

The operational question of $G$ remains open [Pr]: specify the physical state/feature domain, calibrated observation law, admissible model class, accessible probes, and noise model; prove injectivity or characterize indistinguishable fibers; then assess prediction on independent data. Conditional rigidity and exact tomography provide usable tools for this programme.

## Status ledger {#резюме}

- Rows 42a/T-123: unconditional encoder uniqueness withdrawn [✗]; conditional (RI) theorem retained [T at (RI)].
- Row 42b: generic orbit dimensions retained with the principal-stratum qualification.
- Row 42c: finite-time linear injectivity strengthened; no primitivity needed.
- Row 42d: finite-time nonlinear flow injectivity retained at explicit Lipschitz/invariance hypotheses; sensor inverse well-posedness is separate.
- Row 42e: stabilizer of a specified octonionic three-form retained [T]; no deduction of arbitrary encoder equivalence.
- Object-faithfulness and maximal predictivity corollaries withdrawn [✗].

[Mathematical kernel](/docs/reference/mathematical-kernel) · [Measurement protocol](/docs/applied/research/measurement-protocol) · [Typed self-model formalization](/docs/proofs/categorical/formalization-phi)

<a id="p1-примитивность"></a>

<a id="p2-единственность"></a>

<a id="p3-мост"></a>

<a id="p4-л-унификация"></a>

<a id="p5-ковариантность"></a>
