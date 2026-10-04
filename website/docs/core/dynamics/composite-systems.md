---
sidebar_position: 6
title: "Composite Systems, Correlations and Gap"
slug: /core/dynamics/composite-systems
description: "Correct tensor composition, marginal states, correlation certificates, phase observables and explicit geometric bridges"
---

# Composite Systems, Correlations and Gap

Two simultaneously represented holons use a tensor-product state space. This gives exact tools for marginals and correlations. It does not by itself identify correlation with empathy or seven internal axes with spacetime. This revision of 2026-10-03 replaces the former ambiguous 14-dimensional block model and distinguishes proven matrix statements from proposed physical bridges.

## 1. Composite coherence matrix {#составная-матрица}

For $\mathcal H_A=\mathcal H_B=\mathbb C^7$,

$$
\Gamma_{AB}\in\mathcal D(\mathcal H_A\otimes\mathcal H_B)=\mathcal D(\mathbb C^{49}),\qquad
\Gamma_A=\operatorname{Tr}_B\Gamma_{AB},\quad\Gamma_B=\operatorname{Tr}_A\Gamma_{AB}.
$$

The marginals are positive and trace one **[T]**. Matrix entries have **two** subsystem indices on each side:

$$
\gamma_{ij,kl}=\langle i_Aj_B|\Gamma_{AB}|k_Al_B\rangle.
$$

A correct block notation is a $7\times7$ array of $7\times7$ blocks $B_{ik}$ acting on $B$; then $(\Gamma_A)_{ik}=\operatorname{Tr}B_{ik}$ and $\Gamma_B=\sum_iB_{ii}$. There is no canonical single $7\times7$ off-diagonal block containing all inter-system correlations.

### Tensor product versus direct sum

The direct sum $\mathcal H_A\oplus\mathcal H_B$ represents two alternative sectors of one system. A block-diagonal density matrix is $p\Gamma_A\oplus(1-p)\Gamma_B$, not the trace-two matrix $\Gamma_A\oplus\Gamma_B$. Coherences between alternative sectors may be defined, but they are not bipartite entanglement relative to $A\otimes B$. The tensor product represents the two subsystems simultaneously and admits both classical correlations and entanglement.

### A conditional compression is not a marginal map

Choose ground vectors $|0_A\rangle,|0_B\rangle$ **inside** the seven-dimensional factors. The subspaces $\mathcal H_A\otimes|0_B\rangle$ and $|0_A\rangle\otimes\mathcal H_B$ intersect in the vacuum line. Their sum has dimension $7+7-1=13$; removing the vacuum leaves a 12-dimensional single-excitation space. It is not a 14-dimensional direct sum.

For a projector $\Pi$ onto a selected sector, $\Gamma\mapsto\Pi\Gamma\Pi$ is positive but generally trace-decreasing. The normalised postselected state $\Pi\Gamma\Pi/\operatorname{Tr}(\Pi\Gamma)$ is conditional and nonlinear, and changes generic marginals. For example, $|1_A1_B\rangle\langle1_A1_B|$ has nonzero marginals and zero compression to the ground/single-excitation sector. A 14-dimensional single-excitation space requires seven excitations **plus an extra ground state in each factor**, giving $8\otimes8$ before compression. The former claim that a 14-dimensional projection of the 49-dimensional state preserves its marginals is **retracted [✗]**.

### Product, separable and entangled states

| Type | Exact criterion |
|---|---|
| **Uncorrelated** | $\Gamma_{AB}=\Gamma_A\otimes\Gamma_B$ |
| **Separable** | $\Gamma_{AB}=\sum_xp_x\rho_A^x\otimes\rho_B^x$ for a probability distribution |
| **Entangled** | No such separable decomposition exists |

Products are separable; separable states can be correlated. The example

$$
\Gamma_{AB}=\tfrac12|00\rangle\langle00|+\tfrac12|11\rangle\langle11|
$$

is separable but not the product of its marginals. Thus “no entanglement iff product” is **retracted [✗]**.

### Complete correlation certificate [T]

Let $T_0=I/\sqrt7,T_1,\ldots,T_{48}$ be an orthonormal Hermitian operator basis with $T_a$ traceless for $a>0$. The connected coefficients

$$
C_{ab}=\operatorname{Tr}[\Gamma_{AB}(T_a\otimes T_b)]-
\operatorname{Tr}(\Gamma_AT_a)\operatorname{Tr}(\Gamma_BT_b),\quad a,b>0
$$

vanish simultaneously exactly when the state is a product. **Proof:** expand $\Gamma_{AB}-\Gamma_A\otimes\Gamma_B$ in the tensor operator basis. All coefficients with an identity factor vanish by the marginal identities; the remaining coefficients are precisely $C_{ab}$. The full state has $49^2-1=2400$ real parameters: 96 local parameters and 2304 connected coefficients. A selected set of 49 channels cannot encode arbitrary correlations.

## 2. A typed inter-system Gap observable {#межсистемный-gap}

A phase profile needs a specified complex observable. One possible definition **[D]** selects seven bounded operators $F_i^A,F_j^B$ and uses the connected array

$$
K_{ij}=\operatorname{Tr}[\Gamma_{AB}(F_i^A\otimes(F_j^B)^\dagger)]-
\operatorname{Tr}(\Gamma_AF_i^A)\overline{\operatorname{Tr}(\Gamma_BF_j^B)}.
$$

Then $\mathrm{Gap}_{AB}^{F}(i,j)=|\operatorname{Im}K_{ij}|/|K_{ij}|$ for $K_{ij}\ne0$, with a declared zero convention and detection floor. The operator family, frame, amplitudes and support mask are part of the definition. This is a 49-coordinate **selected observable**, not the whole composite matrix. If all $F_i$ are Hermitian, $K$ is real and this phase detector is identically zero; nontrivial phase detection requires an appropriate complex operator family.

For products $K=0$. A nonzero connected coefficient certifies some correlation; it does not certify entanglement. Conversely, a vanishing selected array need not imply a product unless it spans the full connected operator space. A small phase alone does not establish access to another system's experience.

### Rank and representation types

The internal $\operatorname{Im}\Gamma$ is real skew-symmetric and has rank $0,2,4,6$; at most three skew blocks is not rank at most three. $\operatorname{Im}K$ is generally a real $7\times7$ array of rank at most seven. Neither rank is an empathy or isolation theorem.

If the chosen operator family is supplied with a standard-vector transformation rule, $K\mapsto R_AKR_B^T$, then under **independent** $G_2\times G_2$ it carries the external product $(7,7)$ of dimension 49. Under the **diagonal** subgroup the decomposition is

$$
7\otimes7=\underbrace{1\oplus27}_{\operatorname{Sym}^2(7)}\oplus\underbrace{7\oplus14}_{\Lambda^2(7)}.
$$

The 14 is the adjoint representation of $G_2$. This representation statement does not identify a gauge field or spacetime tensor. An invariant trace is available under the diagonal action, not under arbitrary independent rotations. Primary algebraic context: [Baez, The Octonions](https://math.ucr.edu/home/baez/octonions/node14.html).

## 3. Holevo bound: precise information task {#граница-холево}

**Theorem [T].** For a declared ensemble $\{p_x,\rho_x\}$ on a $d$-dimensional register and a measurement outcome $Y$,

$$
I(X:Y)\le\chi:=S(\bar\rho)-\sum_xp_xS(\rho_x)\le S(\bar\rho)\le\log d,\qquad\bar\rho=\sum_xp_x\rho_x.
$$

It bounds information about the encoded classical label in the stated preparation/measurement task. The logarithm convention fixes the units. Source: [Watrous, Theory of Quantum Information, §5.3.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.double.5.pdf).

The bound does not prohibit tomography using many identically prepared systems, establish permanent inaccessibility of an inner aspect, or prove that empathy bypasses measurement limitations. A restriction on reconstructing another system requires the ensemble, number of uses, available observables and operational notion of understanding to be specified. The former “complete understanding only through a shared inner map” corollary is **retracted [✗]** as an inference from Holevo's theorem; it may be proposed philosophically **[I]**.

## 4. Correlation measure and entanglement {#gap-запутанность}

The former quantity $\mathcal E_{\mathrm{Gap}}$ is exactly **quantum mutual information**:

$$
I(A:B)=S(\Gamma_A)+S(\Gamma_B)-S(\Gamma_{AB})
=D(\Gamma_{AB}\|\Gamma_A\otimes\Gamma_B).
$$

Hence $I\ge0$, with equality exactly on products **[T]**. It measures total correlation, including classical correlation. The separable example above has $I=\log2$; the pure Bell state has $I=2\log2$. In general

$$
I(A:B)\le2\min\{S(\Gamma_A),S(\Gamma_B)\},
$$

by the Araki–Lieb inequality. The old normalisation $\min(S_A,S_B)$ is not a general maximum. Zero marginal entropy also makes ratio-based normalisations singular and needs a declared convention.

A phase Gap and mutual information are distinct statistics. Real product states and real entangled states can both have zero pairwise phase. The former “mutual understanding” inequalities relating nonzero lower Gap to small $I$, without a stated operator/encoding bridge, are **retracted [✗]**. A genuine relation needs declared observables, an ensemble/noise model and a proof, not a change of terminology.

## 5. Collective transitions {#коллективный-переход}

A collective state of $N$ holons lives on $(\mathbb C^7)^{\otimes N}$. Correlation and collective viability require a joint model and an aggregation map. Passing individual gates does not by itself produce a new subject; see [Collective consciousness](/docs/consciousness/subjects/collective-consciousness).

The former universal formula

$$
T_c^{\mathrm{coll}}=T_c^{\mathrm{indiv}}\left(1+(N-1)\bar\sigma^2/\mu^2\right)
$$

is **retracted [✗]** as a theorem about arbitrary interacting holons. It needs a specified statistical Hamiltonian, coupling sign, ensemble, order parameter and approximation. Also $\operatorname{Tr}(K^2)$ is not a nonnegative strength for an arbitrary real array; a positive strength is $\|K\|_F^2=\operatorname{Tr}(K^TK)$. Interaction can stabilise or destabilise an ordered phase depending on the model.

## 6. Empathy as an operational proposal {#эмпатия}

An amplitude-supported small phase can be stipulated as a **phase-alignment test [D]**:

$$
|K_{ij}|>\delta,\qquad\mathrm{Gap}_{AB}^F(i,j)<\epsilon.
$$

Calling this empathy requires a separate behavioural/phenomenal bridge **[H]/[I]**. Nonzero mutual information does not mean “the systems cannot be separable”. Classical communication and correlated learning can support prediction of another agent without quantum entanglement.

A stronger measurable proposal tests an agent's predictions of a partner's independently observed responses across held-out interventions, compares to a marginal-only baseline, and controls shared inputs. Tolerances, readouts and the resource model are declared. The former universal four-condition necessity theorem for empathy is **retracted [✗]**; its phase and viability conditions may be tested as hypotheses, not assumed to follow from quantum information.

## 7. Holonomy and the arrow of time {#мост-голономия}

A nonmaximally mixed state does not determine a connection or imply nontrivial holonomy. A nontrivial holonomy need not differ from its inverse (an element of order two is a counterexample), and reversible parallel transport alone does not establish an entropy-production arrow. Cubic terms, associators and PT breaking need a specified action and transformation law. The former unconditional four-step phenomenology → holonomy → time arrow → octonions chain is **retracted [✗]** in this formulation. Its proposed bridges are tracked in [Octonionic derivation](/docs/proofs/minimality/theorem-octonionic-derivation) and [Lindblad operators](/docs/core/operators/lindblad-operators#замыкание-моста).

## 8. RG flow: an action and scheme are required {#рг-поток}

A beta function belongs to a specified field theory: fields, kinetic term, dimension, renormalisation scheme and dimensionless coupling definitions must be supplied. Seven labels or 21 matrix pairs do not specify one-loop combinatorial coefficients.

The former displayed beta functions and Wilson–Fisher conclusion are **retracted [✗]** as established UHM results. They are internally inconsistent: setting $\lambda_3=0$ in the displayed $\beta_{\lambda_4}=63\lambda_4^2/(4\pi^2)$ leaves only $\lambda_4=0$ as a zero, while the proposed $\lambda_4^*=4\pi^2/63$ gives a nonzero beta function. A Wilson–Fisher calculation in an epsilon expansion would require a dimension term and a declared action. No microscopic/macroscopic time-arrow conclusion follows from these unverified coefficients.

## 9. Algebraic decomposition and spacetime {#геометрия-3+1}

Fixing a unit imaginary octonion gives a stabiliser $SU(3)\subset G_2$. As real representations,

$$
\mathbb R^7\cong\mathbb R\oplus\mathbb C^3;
$$

its complexification restricts as $7_\mathbb C=1\oplus3\oplus\bar3$. The complex three-space has **six real dimensions**. The metric $d\tau^2-\sum_{a=1}^3|dz_a|^2$ therefore has signature $(1,6)$, not $(1,3)$; a Kähler structure does not halve the real dimension.

A real spatial three-plane and a Lorentzian metric require extra data and covariance conditions. Current physical bridges, including the tangent-spinor hypothesis (P), are stated in [Physics correspondence](/docs/proofs/physics/physics-correspondence). The former unconditional 3+1 derivation from the $SU(3)$ split is **retracted [✗]**.

A torsion-free $G_2$ structure on an actual seven-dimensional manifold is geometric data, not supplied by a finite density matrix. Holonomy contained in $G_2$ needs the appropriate differential conditions; equality to $G_2$ is stronger. Identifying the internal axes with compact extra dimensions is a proposed physical bridge **[Pr]**. The former entrywise metric ansatz $g_{ij}\propto|\gamma_{ij}|^2+\mathrm{Gap}(i,j)^2$ need not even be positive definite: for a state with diagonal $1/7$ and a small purely imaginary $\gamma_{12}$, that ansatz gives an off-diagonal entry near one with diagonal entries $1/49$, yielding a negative principal determinant.

No measured cosmological constant is derived here from O-channel opacity. A quantitative relation requires an action, units, normalisation and a renormalisation prescription. Current proposals: [Emergent geometry](/docs/physics/gravity/emergent-geometry) and [Cosmological constant](/docs/physics/gravity/cosmological-constant).

## 10. Curvature needs a geometric bridge {#gap-кривизна}

Riemann curvature belongs to a metric connection on a manifold. A scalar phase array is not such a connection. A proposed projection to spacetime must specify the base manifold, bundle, connection, metric, pullback/projection maps, tensor symmetries and dimensional factors. Summing internal labels alone is not a covariant tensor construction.

The former curvature equalities and unconditional Einstein-equation derivation from Gap are **retracted [✗]** in this form. Zero scalar curvature does not imply a flat Riemann tensor. A spectral-action or variational derivation needs the declared geometric/spectral data and its approximations. See [Einstein equations](/docs/physics/gravity/einstein-equations) and [Physical correspondence](/docs/proofs/physics/physics-correspondence).

## 11. Topology and an actual energy barrier {#топологическая-защита-вакуума}

### Correct scope of T-69 {#теорема-тополог-защита}

**Group-theoretic theorem [T].** For the compact simply connected $G_2$ and its maximal torus $T^2$,

$$
\pi_2(G_2/T^2)\cong\mathbb Z^2.
$$

The long exact sequence of $T^2\to G_2\to G_2/T^2$ uses $\pi_2(G_2)=0$ and $\pi_1(G_2)=0$. The former can also be obtained through $SU(2)\to SU(3)\to S^5$ and $SU(3)\to G_2\to S^6$. This classifies homotopy classes of **maps from a sphere** into the orbit, not individual finite-matrix configurations. A soliton interpretation requires a spatial field and boundary conditions. The stabiliser $T^2$ itself is an extra vacuum-model assumption (SV), not a consequence of a frame phase profile.

**Energy-separation theorem [T].** Let $V:K\to\mathbb R$ be continuous on a nonempty compact configuration space $K$, and let a nonempty compact forbidden set $F\subset K$ be disjoint from the set of global minima $M_0$. Then

$$
\Delta=\min_FV-\min_KV>0.
$$

Every path from a minimum to $F$ reaches energy at least $\min_KV+\Delta$. Proof: the minimum on $F$ is attained; if it equalled the global minimum, $F$ would intersect $M_0$. This theorem requires no winding-number claim. It gives no universal numeric value of $\Delta$.

A positive Hessian gives local stability, not a global barrier $6\mu^2$ or $9\mu^2$. A quantitative bound needs a uniform Hessian estimate along the relevant region and a positive separation distance, or direct minimisation of the full potential. Pairwise Gap is discontinuous at zero coherence, so compactness arguments must use a continuous observable or impose an amplitude floor. The former universal T-69 numeric barriers and unavoidable topological transition to any zero-Gap pair are **retracted [✗]** from this proof; they need stronger specified assumptions beyond (SV).

## 12. Connections and local dynamics {#связи}

For every trace-preserving local channel,

$$
\operatorname{Tr}_A[(\mathcal T_A\otimes\mathrm{id}_B)(\Gamma_{AB})]=\Gamma_B.
$$

It follows from the dual identity $\mathcal T_A^*(I_A)=I_A$. For state-selected local channels this remains a pointwise marginal identity if a valid extension is given. Full no-signalling with nonlinear updates additionally requires a specified measurement prescription; see [Physics correspondence §8](/docs/proofs/physics/physics-correspondence#запрет-сигнализации).

- [Evolution and composite extensions](./evolution#расширение-r-на-составные-системы)
- [Coherence matrix](./coherence-matrix)
- [Gap identifiability and amplitude floors](/docs/consciousness/hierarchy/gap-characterization)
- [Collective consciousness](/docs/consciousness/subjects/collective-consciousness)
- [Standard Model and its bridges](/docs/physics/gauge-symmetry/standard-model)
