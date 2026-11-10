---
sidebar_position: 1
title: "The Unitary Regime of the Seven-Level Quantum Model"
description: "The unitary regime of a specified quantum model, its seven-level state space, finite clocks and contextuality."
---

# The Unitary Regime of the Seven-Level Quantum Model

The earlier derivation of quantum physics from UHM has been withdrawn. This chapter starts with a complex Hilbert space, density operators, a specified Hamiltonian and a time parameter. The quantum premise (QG) imports CPTP channels and GKSL dynamics under the usual Markovian assumptions. In finite dimension the Bures topology alone does not recover the physical operator algebra or its composition rule. Within that model one can check its unitary regime, the scope of a category comparison and a finite contextuality witness. Constructing quantum preparations, measurements and composition from operational premises remains open. [Operational reconstruction, G1–G4](https://github.com/gst-st/uhm/blob/main/website/research/operational-reconstruction/README.md) · [Operational states and composition](/docs/core/foundations/operational-processes#process)

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

### 4.2 The Equivalence Theorem

:::warning Retracted: Theorem 3.2 (Category equivalence $\mathbf{Hol}_{R=0} \simeq \mathbf{QM}$) [✗]
An earlier version stated as [T] that the restriction $\pi_{\text{QM}}|_{\mathbf{Hol}_{R=0}}$ is an equivalence of categories $\mathbf{Hol}_{R=0} \simeq \mathbf{QM}$. That is false, and each step of its proof fails.

- **Essential surjectivity fails.** An equivalence must reach every object of $\mathbf{QM}$ up to isomorphism, and the isomorphisms of $\mathbf{QM}$ are unitaries, which preserve dimension and purity. $\mathbf{QM}$ contains systems of every dimension — a qubit, $\mathcal{H} = \mathbb{C}^2$ — and states of every purity — $I/7$, with $P = 1/7$. Objects of $\mathbf{Hol}$ are seven-dimensional coherence matrices with $P > 2/7$ ([Definition 12.1 (V)](/docs/proofs/categorical/categorical-formalism#категория-голономов-hol)), so neither the qubit nor $(\mathbb{C}^7, H, I/7)$ is isomorphic to any $\pi_{\text{QM}}(\mathbb{H})$. Under the master definition $R = 1/(7P) \geq 1/7$ of the [reflection measure](/docs/consciousness/foundations/self-observation#мера-рефлексии-r) no holon has $R = 0$ at all, so $\mathbf{Hol}_{R=0}$ is empty.
- **"At $R = 0$ CPTP channels degenerate to unitaries" is not justified.** Morphisms of $\mathbf{Hol}$ are CPTP channels that preserve viability and commute with self-modelling; nothing in that definition makes them unitary. The replacement channel $X \mapsto \mathrm{Tr}(X)\,\rho^*$ onto a fixed point $\rho^*$ of self-modelling meets both conditions and is not unitary; with no rule sending it to a unitary, $\pi_{\text{QM}}$ is not even defined on morphisms.
- **Full faithfulness is not proven.** The proof asserts a bijection of hom-sets without constructing the functor on morphisms.
:::

**What holds instead.** An earlier note here (2026-09-25) called the following an "identification by definition [D]" and stated it as an isomorphism with the full subcategory on seven-dimensional systems of purity above $2/7$. It is not an isomorphism — a holon also needs $\rho_E \neq 0$, which unitary conjugation does not preserve — but it is an equivalence, and that is a theorem.

Let $\mathbf{Hol}^{u}$ be the category whose objects are pairs $(\Gamma, H)$ with $\Gamma$ an object of $\mathbf{Hol}$ ([Definition 12.1](/docs/proofs/categorical/categorical-formalism#категория-голономов-hol)) and $H$ a Hamiltonian, and whose morphisms $(\Gamma_1, H_1) \to (\Gamma_2, H_2)$ are all unitaries $U$ with $U\Gamma_1U^\dagger = \Gamma_2$, as in Definition 3.1. For a single seven-dimensional state the conditions of Definition 12.1 read: (V) $P = \mathrm{Tr}\,\Gamma^2 > 2/7$; (PH) $\rho_E \neq 0$, which in the 7D formalism is $\gamma_{EE} > 0$; (AP) holds for every state (the replacement channel $X \mapsto \mathrm{Tr}(X)\,\Gamma$ fixes $\Gamma$); (QG) is a condition on the generator, carried by $H$. Let $\mathbf{QM}_7^{>2/7}$ be the full subcategory of $\mathbf{QM}$ on the objects $(\mathbb{C}^7, H, \rho)$ with $\mathrm{Tr}\,\rho^2 > 2/7$.

:::tip Theorem 3.2′ (Holons are seven-dimensional quantum mechanics above purity 2/7) [T]
1. The inclusion $\iota : \mathbf{Hol}^{u} \to \mathbf{QM}_7^{>2/7}$, $(\Gamma, H) \mapsto (\mathbb{C}^7, H, \Gamma)$, is an equivalence of categories. It is not an isomorphism: $(\mathbb{C}^7, H, |O\rangle\langle O|)$ has $P = 1$ and $\gamma_{EE} = 0$, so it is not a holon, yet it is isomorphic in $\mathbf{QM}$ to one.
2. Its isomorphism classes are the spectra $\lambda_1 \geq \dots \geq \lambda_7 \geq 0$ with $\sum\lambda_i = 1$ and $\sum\lambda_i^2 > 2/7$; the automorphism group of an object is the centraliser of $\Gamma$ in $U(7)$, $\prod_i U(m_i)$ over the eigenvalue multiplicities $m_i$.
:::

For the specific inclusion in Theorem 3.2′, dimensions and spectra give sharp scope. All arrows between its objects are included by definition. Every seven-level state of purity $P>2/7$ can be permuted so that a positive diagonal entry occupies the designated $E$ slot. This proves essential surjectivity in the stated state category. Its isomorphism classes are the spectra and the stabiliser is $\prod_j U(m_j)$ for eigenvalue multiplicities $m_j$. An isometry $V:\mathbb C^d\to\mathbb C^7$ pads the spectrum with zeros. Unitaries extend by the identity on the complement, giving a faithful embedding for $d\le3$, since $P\ge1/d>2/7$. Already $I_4/4$ fails the threshold. These arguments concern the inclusion and the indicated embeddings. [Categorical definitions](/docs/proofs/categorical/categorical-formalism#категория-голономов-hol)

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

### 7.2 What the reconstructions mean for UHM {#72-что-реконструкции-значат-для-угм}

Chiribella, D’Ariano and Perinotti combine purification with five operational principles, including local distinguishability. Real quantum theory also admits purification. Two rebits can have identical local-product statistics and be perfectly distinguishable jointly. Transposition provides a separate test of admissibility on a composite: partial transposition of a Bell state has eigenvalue $-1/2$. Recovering complex quantum theory from the proposed UHM state–effect pairing would require a composition rule and experiments that resolve these alternatives. [Reconstruction](https://arxiv.org/abs/1011.6451) · [Real quantum theory](https://arxiv.org/abs/1005.4870) · [Exact preparation controls](https://github.com/gst-st/uhm/blob/main/website/research/operational-reconstruction/verify_preparations.py)

The nonlinear feedback law also depends on operational resources. A fixed environment, channel and partial trace produce an affine map. On the specified canonical ray, the exact nonlinear target requires repeated preparations and heralded success. [Resource bound](https://github.com/gst-st/uhm/blob/main/website/research/operational-reconstruction/feedback.md)

## 8. Kochen–Specker Contextuality in the Holon Space {#8-контекстуальность-кш}

The Fano-line projectors $\Pi_\ell = \sum_{i \in \ell}|i\rangle\langle i|$ commute, and the distribution $p_i = \gamma_{ii}$ reproduces every one of their contexts, so they show no contextuality; the former T-201 claimed otherwise and is retracted ([registry](/docs/reference/status-registry), `test_fano_line_projectors_commute_hence_noncontextual`). Contextuality needs non-commuting projectors. The Fano plane supplies a canonical set of them.

**The rays.** In $\mathbb{R}^7 \subset \mathbb{C}^7$ take the seven basis vectors $|i\rangle$ and, for each of the seven complements $q = \{a, b, c, d\}$ of a Fano line (the words of weight four of the Hamming code $H(7,4)$ of Step T8), the eight rays $\tfrac12(|a\rangle \pm |b\rangle \pm |c\rangle \pm |d\rangle)$. These are 63 rays; with both signs they are 126 unit vectors, closed under the reflections $v \mapsto v - 2\langle u, v\rangle u$ — the root system $E_7$. As octonions they are the purely imaginary units of Coxeter's integral octonions. No orientation of the Fano lines enters: only the lines, through their complements, do.

:::tip Theorem T-201′ (Kochen–Specker contextuality of the Fano–Hamming rays) [T]
The 63 rays form 135 orthonormal bases of $\mathbb{C}^7$, each ray lying in 15 of them, and every set of mutually orthogonal rays extends to one of these bases. There is no assignment $v : \{\text{rays}\} \to \{0, 1\}$ with exactly one ray of value 1 in each basis. Hence for every state $\Gamma \in \mathcal{D}(\mathbb{C}^7)$ the rank-one projectors onto these rays admit no non-contextual value assignment: UHM's state space carries state-independent Kochen–Specker contextuality, with projectors from different bases that do not commute (1008 of the 1953 pairs of rays are neither orthogonal nor equal).
:::

**Proof.** The counts are a finite enumeration of the maximal orthogonal subsets (all have seven elements). Non-colourability is a finite 0/1 feasibility problem — 63 variables, 135 equality constraints $\sum_{r \in b} v_r = 1$ — and it is infeasible; this is checked by an exact integer-programming solver (`test_e7_rays_from_the_hamming_quadrangles_are_kochen_specker`) and was confirmed independently by a propagating backtracking search. A basis-critical subfamily of 36 of the 135 bases is already uncolourable. The configuration $63_{15}$–$135_7$ of the $E_7$ rays and its Kochen–Specker property are due to A. Ruuge, "Exceptional and non-crystallographic root systems and the Kochen–Specker theorem", *J. Phys. A: Math. Theor.* **40**, 2849–2859 (2007), arXiv:0906.2696; what is added here is its construction from the Fano plane and the Hamming code of the UHM chain. $\blacksquare$

The $E_7$ result assumes that all the indicated bases are available as quantum measurements. It supplies no method of implementing them on a physical node. In reconstruction G3 the scalar subcontext covers every context in the proposed dense topology. Sheafification there identifies all spectral characters. A physical contextuality claim requires a site that retains the distinctions and an operational implementation of the contexts. [Ruuge’s construction](https://arxiv.org/abs/0906.2696) · [Context checks](https://github.com/gst-st/uhm/blob/main/website/research/operational-reconstruction/verify_context.py)

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
