---
sidebar_position: 1
title: "The Unitary Regime of the Seven-Level Quantum Model"
description: "The unitary regime of a specified quantum model, its seven-level state space, finite clocks and contextuality."
---

# The Unitary Regime of the Seven-Level Quantum Model

Start with a complex Hilbert space, density operators, a specified Hamiltonian and a time parameter. The quantum premise (QG) supplies CPTP channels and, under the Markovian assumptions, GKSL dynamics. Finite-dimensional Bures topology alone does not recover the physical operator algebra or its composition rule. Which experiments justify those choices? The unitary limit tests the supplied equation. The two-rebit experiment below tests the choice of composition law. [Operational states and composition](/docs/core/foundations/operational-processes#process)

## Contents

1. [Connection to L-Unification](#1-связь-с-l-унификацией)
2. [Switching off dissipation and regeneration](#2-предельный-функтор)
3. [Category of Quantum-Mechanical Systems](#3-категория-qm)
4. [The restricted category equivalence](#4-функтор-редукции)
5. [Proposed classification of physical systems](#5-таксономия)
6. [Finite clock readings and conditional states](#6-дискретность-времени)
7. [Precedents: Reconstructions of Quantum Theory](#7-прецеденты-реконструкции)
8. [Kochen–Specker Contextuality in the Holon Space](#8-контекстуальность-кш)

## 1. Connection to L-Unification {#1-связь-с-l-унификацией}

The model supplies three terms for the generator of $\Gamma$. The name “logical Liouvillian” refers to an interpretation of the dissipator. A subobject classifier supplies characteristic arrows. Representing those arrows by Hilbert-space effects, choosing coupling strengths and providing a physical clock each need additional structure. [Evolution equation](/docs/core/dynamics/evolution) · [Classifier proposal](/docs/core/foundations/axiom-omega)

## 2. Switching off dissipation and regeneration {#2-предельный-функтор}

**Theorem 3.1 (unitary regime).** Set all dissipative rates and the regenerative coupling to zero in the specified equation. With $H=H^\dagger$ in energy units, the remaining equation is

$$
\dot\Gamma=-\frac{i}{\hbar}[H,\Gamma]+\mathcal D[\Gamma]+\mathcal R[\Gamma]
\quad\longrightarrow\quad
\dot\Gamma=-\frac{i}{\hbar}[H,\Gamma].
$$

For constant $H$, $\Gamma(t)=e^{-itH/\hbar}\Gamma(0)e^{itH/\hbar}$. A pure initial state stays pure, and the representative $\psi(t)=e^{-itH/\hbar}\psi(0)$ obeys the Schrödinger equation. The projector leaves the phase of this representative free. Setting the rates to zero is an independent assumption. With the corpus definition $R=1/(7\,\mathrm{Tr}\,\Gamma^2)$ one has $R\ge1/7$ even at purity one. [Reflection measure](/docs/consciousness/foundations/self-observation#мера-рефлексии-r) · [Regenerative coupling](/docs/core/foundations/axiom-septicity#структурный-анзац-kappa0)

## 3. Category of Quantum-Mechanical Systems {#3-категория-qm}

### 3.1 Definition of the Category QM

**Definition 3.1 (Category QM).**

Objects are triples (Hilbert space, Hamiltonian, initial state):

$$
\mathrm{Ob}(\mathbf{QM}) = \{(\mathcal{H}, H, \rho_0) : \mathcal{H} \text{ — Hilbert space, } H = H^\dagger, \rho_0 \text{ — initial state}\}
$$

Here arrows are unitary isomorphisms $U:\mathcal H_1\to\mathcal H_2$ satisfying $U\rho_1U^\dagger=\rho_2$. This definition compares states and imposes no intertwining condition on the Hamiltonians. Adding one changes the category and its stabilisers.

### 3.2 Connection to the Category of Holons

The category $\mathbf{Hol}$ (of Holons) is defined via:
- **Objects:** Holons $\mathbb{H}$ with 7-dimensional coherence matrix $\Gamma^{(7)}$
- **Morphisms:** Structure-preserving CPTP channels

The forgetful functor $\mathcal{U}: \mathbf{Hol} \to \mathbf{DensityMat}$ is defined by:

$$
\mathcal{U}(\mathbb{H}) := \Gamma_{\mathbb{H}}^{(7)}, \quad \mathcal{U}(f: \mathbb{H}_1 \to \mathbb{H}_2) := \Phi_f
$$

where $\Phi_f$ is the CPTP channel induced by morphism $f$.

:::tip [T] Theorem 1.1 (Functoriality of the forgetful functor)
$\mathcal{U}$ is a functor preserving identities and composition.

*Proof:* Direct consequence of the definition of morphisms in $\mathbf{Hol}$ as structure-preserving CPTP channels. $\blacksquare$
:::

---

## 4. The restricted category equivalence {#4-функтор-редукции}

Consider the state category of seven-level density matrices with $P=\operatorname{Tr}\Gamma^2>2/7$ and all unitaries carrying one state to another. Let a full subcategory also require $\Gamma_{EE}>0$ on a marked axis. The inclusion is an equivalence. Every trace-one state has a positive diagonal entry, and a unitary permutation moves such an entry to the marked axis. The inclusion preserves every allowed arrow between its objects. Isomorphism classes are classified by the spectrum.

The restriction matters. The state $I/7$ has purity $1/7$. An isometry preserves the spectrum up to zero padding, so it embeds any qubit or qutrit state above the threshold, while $I/4$ falls below it. Comparing dynamical systems would also require intertwining their Hamiltonians. [Category definitions](/docs/proofs/categorical/categorical-formalism#категория-голономов-hol)

## 5. Proposed classification of physical systems {#5-таксономия}

The proposed association of unitary evolution with elementary particles, dissipation with open systems and regeneration with life is an interpretation. A qubit coupled to a bath can decohere. Neither a measured purity nor a choice of $\Omega$ specifies which bath or feedback apparatus is present. A classification by $R$ needs an independent procedure for identifying the system and measuring its dynamics.

## 6. Finite clock readings and Page–Wootters conditioning {#6-дискретность-времени}

Choose a clock with $N$ pointer labels and cyclic shift $V|k\rangle=|k+1\bmod N\rangle$. Its readout set is $\mathbb Z_N$ by construction (the content of Theorem 3.4). With energy levels $\hbar\omega_0 k$, consecutive Fourier-clock readings are spaced by $2\pi/(N\omega_0)$. Conditioning a joint clock–system state on such a reading requires a specified tensor product, state and clock measurement. The Page–Wootters constraint is a further input. With $N=7$ and a six-level system this model has dimension 42. At fixed $\omega_0$ the readings become dense on a circle as $N$ grows. Finite dimension alone gives neither a universal chronon nor a continuum time law. [Clock algebra](/docs/core/structure/dimension-o#алгебра-часов) · [Page–Wootters construction](/docs/proofs/dynamics/emergent-time)

## 7. Precedents: Reconstructions of Quantum Theory {#7-прецеденты-реконструкции}

This page obtains quantum mechanics from UHM by switching off two terms of an evolution equation that is already written in the Hilbert-space formalism: the objects of the base category are density matrices on $\mathbb{C}^{42}$ ([Property 1](/docs/core/foundations/axiom-omega#свойство-1)), processes are CPTP channels, probabilities are traces. Since 2001 a separate line of research has done what UHM does not: it **derives** that formalism — complex Hilbert spaces, density matrices, unitary dynamics, the trace rule for probabilities — from requirements on how systems can be prepared, transformed and measured. These derivations are the relevant precedent for any claim that UHM "derives" quantum mechanics, and they bear on UHM in two ways, both stated in §7.2.

They work inside **generalized probabilistic theories** (GPTs): a state is simply the list of outcome probabilities for a fixed set of measurements, and a theory is specified by which states, transformations and measurements it allows. Classical probability theory and quantum theory are two such theories; a **reconstruction** is a theorem that picks out quantum theory among all of them from a few physical requirements.

### 7.1 The reconstructions {#71-реконструкции}

- **Hardy (2001).** L. Hardy, "Quantum theory from five reasonable axioms", arXiv:quant-ph/0101012. A system is characterised by two integers: $K$, the number of probabilities needed to fix a state, and $N$, the largest number of states that can be told apart in a single shot. From five axioms — probabilities as limits of relative frequencies; *simplicity* ($K$ is the smallest function of $N$ consistent with the other axioms); *subspaces* (a system confined to $M$ of its $N$ distinguishable states behaves as a system with $N = M$); *composite systems* ($N_{AB} = N_A N_B$, $K_{AB} = K_A K_B$); *continuity* (a continuous reversible transformation connects any two pure states) — Hardy derives $K = N^r$ with $r$ a positive integer and then $r = 2$, which is complex quantum theory. Dropping the single word "continuous" leaves classical probability theory, with $K = N$.
- **Dakić and Brukner (2011).** B. Dakić, Č. Brukner, "Quantum theory and beyond: is entanglement special?", in *Deep Beauty: Understanding the Quantum World through Mathematical Innovation*, ed. H. Halvorson, Cambridge University Press 2011, pp. 365–392, doi:10.1017/CBO9780511976971.011, arXiv:0911.0695. Three axioms — all systems that carry at most one bit are equivalent; the state of a composite system is fixed by measurements on its parts; any two pure states are connected by a reversible transformation — reconstruct classical probability theory and quantum theory, and continuity of the transformation separates quantum theory. A by-product: no other probabilistic theory can have entanglement without breaking one of the axioms.
- **Masanes and Müller (2011).** Ll. Masanes, M. P. Müller, "A derivation of quantum theory from physical requirements", *New J. Phys.* **13**, 063001 (2011), arXiv:1004.1483. Five requirements — *finiteness* (a system with two distinguishable states has a finite-dimensional state space), *local tomography* (the state of a composite is fixed by the statistics of measurements on its parts), *equivalence of subspaces*, *symmetry* (every pure state can be reversibly mapped to every other), *all measurements allowed* — are met by exactly two theories, classical probability theory and quantum theory; requiring the reversible transformations to be continuous leaves quantum theory alone. The three-dimensionality of the qubit's Bloch ball gets a group-theoretic explanation.
- **Chiribella, D'Ariano and Perinotti (2011).** G. Chiribella, G. M. D'Ariano, P. Perinotti, "Informational derivation of quantum theory", *Phys. Rev. A* **84**, 012311 (2011), arXiv:1011.6451. Five informational principles — causality, perfect distinguishability, ideal compression, local distinguishability, pure conditioning — define a class of theories; one further postulate, **purification** (every mixed state is the marginal of a pure state of a larger system, unique up to a reversible transformation of the added system), singles out finite-dimensional quantum theory, derived without assuming the Hilbert-space framework.
- **The seven-dimensional case with $G_2$ (2013–2021).** In these reconstructions the elementary system — the analogue of a bit — has a Euclidean ball as its state space, and the requirement that any pure state be reachable from any other by a reversible transformation makes its symmetry group transitive on the boundary sphere. For odd ball dimension $d \neq 7$ that group must be $SO(d)$; for $d = 7$ it may also be the exceptional group $G_2$, transitive on $S^6$. This is the one place where the octonionic structure used by UHM appears in the reconstruction literature, and it has been examined and set aside. B. Dakić and Č. Brukner ("The classical limit of a physical theory and the dimensionality of space", in *Quantum Theory: Informational Foundations and Foils*, eds. G. Chiribella, R. W. Spekkens, Springer 2016, arXiv:1307.3984, §VI.C) showed that the unique $G_2$-invariant tensor — the octonionic structure constants $\psi_{ijk}$, nonzero exactly on the seven Fano triples — couples the system to a classical field through generators outside $\mathfrak{g}_2$, so the dynamics leaves $G_2$ and would have to be $SO(7)$, a case they had already excluded. Ll. Masanes, M. P. Müller, D. Pérez-García and R. Augusiak ("Entanglement and the three-dimensionality of the Bloch ball", *J. Math. Phys.* **55**, 122203 (2014), arXiv:1111.4060, §IV.I) proved that two such systems with local group $G_2$ admit no interacting dynamics, hence no entanglement. M. P. Müller's review calls the $d = 7$ ball with $G_2$ "a curious special case", ruled out for two systems, and leaves open whether a post-quantum $G_2$-related theory exists for three or more (lecture notes cited under *Standing* below, §4.2).
- **Höhn (2017).** P. A. Höhn, "Toolbox for reconstructing quantum theory from rules on information acquisition", *Quantum* **1**, 38 (2017), arXiv:1412.8323; the many-qubit case is completed in P. A. Höhn, C. S. M. Wever, "Quantum theory from questions", *Phys. Rev. A* **95**, 012102 (2017), arXiv:1511.01130. An observer interrogates a system with yes/no questions; four rules — a limit on the information available, the existence of complementary information, conservation of the total information between interrogations, and continuous evolution of the observer's knowledge — give the Bloch ball of a qubit (and the disc of a rebit, which an extra rule removes), with unitary time evolution.

**Standing.** These are accepted theorems within the GPT framework; what the field discusses is which requirements are physically compelling. Dakić and Brukner, for instance, note that most earlier attempts either fall short of deriving the theory uniquely or rest on abstract assumptions that themselves need physical motivation (2011, abstract), and Masanes and Müller replaced Hardy's simplicity axiom by their fifth requirement (2011, §I). M. P. Müller's lecture notes review the framework and a reconstruction from tomographic locality, continuous reversibility and the subspace axiom ("Probabilistic theories and reconstructions of quantum theory", *SciPost Phys. Lect. Notes* **28** (2021), arXiv:2011.01286).

### 7.2 An experiment with two rebits {#72-что-реконструкции-значат-для-угм}

A rebit is a two-level system with a real Hilbert space and real symmetric density matrices. Assume independent local $X$ and $Z$ eigenstate sources and analysers, a fair coin, the real tensor product, the Born rule and a coherent controlled-NOT gate. Draw a private bit $t$. For label $b$, prepare the first port in the $X$ eigenstate labelled $t$ and the second in the $Z$ eigenstate labelled $t\oplus b$. Forget $t$ and apply the gate. Its action takes $X\otimes Z$ to $J\otimes J$ under conjugation, with $J=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)$. Thus
$$
\rho_b=\frac{I_4+(-1)^bJ\otimes J}{4}.
$$

Every symmetric local product effect has equal expectation on the two states. A single joint measurement distinguishes the labels perfectly. Apply the same gate once more, measure $X$ and $Z$ locally, and take their parity. The probability of the prepared parity is one. Omit the analyser gate and each parity has probability one half. Reading the control in $Z$ before the preparation gate erases the difference completely. This comparison depends on availability of the specified coherent interaction. [Circuit, local tests and exact controls](https://github.com/uhm-theory/holon/blob/main/website/research/operational-reconstruction/network/RebitExperiment.lean) · [Real local tomography](https://arxiv.org/abs/1005.4870)

More generally, a jointly symmetric difference is invisible to all products of real local projectors exactly when partial transposition on one port negates it. For two rebits this kernel has one dimension, spanned by $J\otimes J$. Nine product tests suffice to detect every difference outside it. The result supplies a discriminator between composition laws for given devices. Deriving a physical realization from weaker premises still requires evidence about what can actually be built. [Operational models](/docs/core/foundations/operational-processes#alternative)

The nonlinear feedback law also depends on operational resources. A fixed environment, channel and partial trace produce an affine map. On the specified canonical ray, the exact nonlinear target requires repeated preparations and heralded success. [Resource bound](https://github.com/uhm-theory/holon/blob/main/website/research/operational-reconstruction/feedback.md)

## 8. Kochen–Specker Contextuality in the Holon Space {#8-контекстуальность-кш}

The Fano-line projectors $\Pi_\ell=\sum_{i\in\ell}|i\rangle\langle i|$ commute. The populations $p_i=\Gamma_{ii}$ give one classical distribution reproducing all of their contexts. Additional bases can test contextuality.

**The rays.** In $\mathbb{R}^7 \subset \mathbb{C}^7$ take the seven basis vectors $|i\rangle$ and, for each of the seven complements $q = \{a, b, c, d\}$ of a Fano line (the words of weight four of the Hamming code $H(7,4)$ of Step T8), the eight rays $\tfrac12(|a\rangle \pm |b\rangle \pm |c\rangle \pm |d\rangle)$. These are 63 rays; with both signs they are 126 unit vectors, closed under the reflections $v \mapsto v - 2\langle u, v\rangle u$ — the root system $E_7$. As octonions they are the purely imaginary units of Coxeter's integral octonions. No orientation of the Fano lines enters: only the lines, through their complements, do.

:::tip Theorem T-201′ (Kochen–Specker contextuality of the Fano–Hamming rays) [T]
The 63 rays form 135 orthonormal bases of $\mathbb{C}^7$, each ray lying in 15 of them, and every set of mutually orthogonal rays extends to one of these bases. There is no assignment $v : \{\text{rays}\} \to \{0, 1\}$ with exactly one ray of value 1 in each basis. Hence for every state $\Gamma \in \mathcal{D}(\mathbb{C}^7)$ the rank-one projectors onto these rays admit no non-contextual value assignment: UHM's state space carries state-independent Kochen–Specker contextuality, with projectors from different bases that do not commute (1008 of the 1953 pairs of rays are neither orthogonal nor equal).
:::

**Proof.** The counts are a finite enumeration of the maximal orthogonal subsets (all have seven elements). Non-colourability is a finite 0/1 feasibility problem — 63 variables, 135 equality constraints $\sum_{r \in b} v_r = 1$ — and it is infeasible; this is checked by an exact integer-programming solver (`test_e7_rays_from_the_hamming_quadrangles_are_kochen_specker`) and was confirmed independently by a propagating backtracking search. A basis-critical subfamily of 36 of the 135 bases is already uncolourable. The configuration $63_{15}$–$135_7$ of the $E_7$ rays and its Kochen–Specker property are due to A. Ruuge, "Exceptional and non-crystallographic root systems and the Kochen–Specker theorem", *J. Phys. A: Math. Theor.* **40**, 2849–2859 (2007), arXiv:0906.2696; what is added here is its construction from the Fano plane and the Hamming code of the UHM chain. $\blacksquare$

The $E_7$ result assumes that all the indicated bases are available as quantum measurements. It supplies no method of implementing them on a physical node. In reconstruction G3 the scalar subcontext covers every context in the proposed dense topology. Sheafification there identifies all spectral characters. A physical contextuality claim requires a site that retains the distinctions and an operational implementation of the contexts. [Ruuge’s construction](https://arxiv.org/abs/0906.2696) · [Context checks](https://github.com/uhm-theory/holon/blob/main/website/research/operational-reconstruction/verify_context.py)

**Related models and definitions**

- [Physics Correspondence](/docs/proofs/physics/physics-correspondence)
- [Quantum Measurement](/docs/physics/quantum-mechanics/measurement)
- [Evolution of Γ](/docs/core/dynamics/evolution)
- [Emergent Time](/docs/proofs/dynamics/emergent-time)
- [Axiom Ω⁷](/docs/core/foundations/axiom-omega)
- [Coherence Matrix](/docs/core/dynamics/coherence-matrix)
- [Dimension O](/docs/core/structure/dimension-o)
- [Critical Purity](/docs/proofs/dynamics/theorem-purity-critical)
- [Categorical Formalism](/docs/proofs/categorical/categorical-formalism)
- [Physics — Overview](/docs/physics/overview)
