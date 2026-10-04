---
slug: /proofs/consciousness/interiority-hierarchy
sidebar_position: 1
title: "Interiority Hierarchy: Rigorous Specification"
format: md
---

# Interiority Hierarchy: Rigorous Specification

This specification proves finite-dimensional consequences of the [canonical typed hierarchy](/docs/consciousness/hierarchy/interiority-hierarchy). The identification of an operational capability with phenomenal consciousness is a separate **[I]/[H]** bridge. Definitions are **[D]**; verified implications under stated assumptions are **[T]**. The revision of 2026-10-03 replaces unsupported universal threshold, topology and phase claims with exact propositions and counterexamples.

## 1. State, frame and experiential data

A record is $z=(\Gamma,\mathsf E,\mathsf M,\mathsf Q)$ with $\Gamma\in\mathcal D(\mathbb C^7)$. The semantic frame is fixed when computing diagonal, E and phase quantities. Write

$$
P=\operatorname{Tr}\Gamma^2,\qquad Q=\sum_i\gamma_{ii}^2,\qquad R=1/(7P),\qquad\Phi=(P-Q)/Q.
$$

These are functions of a matrix. A specified empirical reconstruction and implemented model are extra data, not consequences of trace one or positivity.

### L0 and the existence of a reduction {#уровень-0-интериорность-interiority}

**Definition [D].** $A_0(z)$ means that the matrix is a valid state. The universality of this predicate is tautological inside the model. Its “inner aspect” is the ontological interpretation **[I]**.

**Proposition [T].** If an extension $\widetilde\Gamma\in\mathcal D(\mathcal H_E\otimes\mathcal H_{\bar E})$ and its factorisation are supplied, then $\rho_E=\operatorname{Tr}_{\bar E}\widetilde\Gamma$ is a density matrix. Positivity follows by testing vectors against the partial trace; trace one follows from the defining trace identity. This proposition does not infer a preferred extension or an experiential factor from the seven basis axes.

In the 42D Page–Wootters factorisation $\mathbb C^7_{\mathrm{clock}}\otimes\mathbb C^6_{\mathrm{system}}$, the E-axis is a **summand** of the system factor. Its clock block

$$
B_E=(I\otimes\langle E|)\widetilde\Gamma(I\otimes|E\rangle)
$$

is positive with trace $p_E$. If $p_E>0$, use $\rho_E=B_E/p_E$; if $p_E=0$, this conditional state is undefined. It is not a partial trace onto a seven-dimensional E tensor factor. Choice of lift and conditioning is recorded explicitly.

### L1 and the distinction between a proxy and a spectrum {#уровень-1-феноменальная-геометрия-phenomenal-geometry}

In extension mode define $A_1:=\operatorname{rank}(\rho_E)>1$ and $D^{\mathrm{ext}}=\exp S_{vN}(\rho_E)$. In proxy mode define

$$
A_1:=\mathrm{Coh}_E>0,\qquad D^{7D}:=1+6\,\mathrm{Coh}_E
$$

with

$$
\mathrm{Coh}_E=\frac{\gamma_{EE}^2+2\sum_{i\ne E}|\gamma_{Ei}|^2}{P}.
$$

These are distinct definitions **[D]**. Endpoint conventions do not prove equality of the intermediate values or of threshold decisions.

**Proposition [T].** For positive $\Gamma$, $\mathrm{Coh}_E>0\iff\gamma_{EE}>0$. Indeed positivity of each $2\times2$ principal minor gives $|\gamma_{Ei}|^2\le\gamma_{EE}\gamma_{ii}$. If $\gamma_{EE}=0$, the E-row and column vanish; if it is positive, the numerator contains its positive square. Thus the proxy does not detect off-diagonal coupling by itself. $I/7$ has $\mathrm{Coh}_E=1/7$ and $D^{7D}=13/7$; the pure E-state has $\mathrm{Coh}_E=1$ and $D^{7D}=7$. Neither value is a literal entropy calculation of a one-dimensional E-axis.

For a normalised extension of rank $r$,

$$
1\le\exp S_{vN}(\rho_E)\le r,
$$

with the upper equality exactly for a uniform nonzero spectrum. Rank greater than one implies $D>1$, not $D\ge2$: eigenvalues $(0.99,0.01)$ have rank two and $\exp S\approx1.0576$. The differentiation gate is therefore a separate condition.

### Fubini–Study metric {#определение-12-метрика-фубини-штуди}

<a id="32-метрика-фубини-штуди"></a>
For normalised representatives of rays, one conventional normalisation is

$$
d_{FS}([\psi],[\chi])=\arccos|\langle\psi|\chi\rangle|,
$$

with line element $ds^2=\langle d\psi|d\psi\rangle-|\langle\psi|d\psi\rangle|^2$. The finite pair statistic $1-|\langle\psi|\chi\rangle|^2$ equals $\sin^2d_{FS}$, not the line element. In a degenerate eigenspace of $\rho_E$, individual eigenvectors are not canonical. The invariant spectral data are eigenvalues with their spectral projectors $(\lambda,P_\lambda)$; a selected basis of “qualities” needs additional structure.

## 2. L2: exact algebra and explicit bridges {#уровень-2-когнитивные-квалиа-cognitive-qualia}

Define

$$
\mathsf{Cap}_2:=(P>2/7)\land(R\ge1/3)\land(\Phi\ge1)\land(D\ge2),\qquad A_2:=A_1\land\mathsf{Cap}_2.
$$

The differentiation mode must be declared. In either mode $D\ge2$ already implies its corresponding $A_1$, but retaining $A_1$ makes the cumulative typing visible.

### Proposition: scalar bounds [T]

For every seven-dimensional state,

$$
1/7\le Q\le P\le1,\quad1/7\le R\le1,\quad0\le\Phi\le7P-1\le6.
$$

**Proof.** Positivity gives nonnegative diagonal entries summing to one. Cauchy–Schwarz yields $Q\ge1/7$. Hermiticity yields $P=Q+\sum_{i\ne j}|\gamma_{ij}|^2\ge Q$. Its eigenvalues are probabilities, hence $P\le1$. Substitution gives the other inequalities.

For $A_2$, necessarily

$$
2/7<P\le3/7,\quad1/3\le R<1/2,\quad1\le\Phi\le2.
$$

Also $C:=\Phi R$ obeys

$$
C=\frac1{7Q}-R\le1-R,\qquad 1/3\le C\le2/3\quad\text{under }A_2.
$$

The reverse implication $C\ge1/3\Rightarrow A_2$ is false: a uniform real pure state has $C=6/7$ and fails $R\ge1/3$.

### Status of thresholds {#обоснование-порогов}

The HS identity $\|\Gamma-I/7\|_F^2=P-1/7$ is exact. An adopted majority criterion yields $P>2/7$. An adopted $R\ge1/3$ criterion yields $P\le3/7$. Neither algebra proves that these quantities are universal physical viability or reflective competence. In particular $R$ compares to $I/7$, whereas

$$
R_\varphi=1-\|\Gamma-\varphi(\Gamma)\|_F^2/P
$$

compares to a chosen model and may even be negative; they must not be interchanged. Metric-classification theorems do not uniquely select this scalar ratio or supply a Bayesian probability interpretation. Counting dynamical summands does not count independent information channels.

$\Phi\ge1$ is an explicit choice of HS weight balance. The inequality $\Phi\le7P-1$ does not force a universal conscious threshold: at $P=2/7$ it gives $\Phi\le1$, with equality only for uniform diagonal. For extension mode, $D\ge2\iff S_{vN}\ge\log2$ is exact; choosing one bit as a phenomenal threshold remains a bridge. Calibration and biological universality of all gates are **[H]**.

### Proposition: impossible Boolean profiles [T]

The formal product of three purity bins with two integration and two differentiation outcomes has twelve labels. If $P<2/7$, however, $\Phi<1$ necessarily. At $P=2/7$, $\Phi\ge1$ forces $\Phi=1$ and uniform diagonal, while the strict viability gate still fails. Thus the twelve labels are not twelve independent nonempty state regions. The old below-threshold “flooded/white-out” regions are **retracted [✗]**.

### Proposition: conservative gate stability [T] {#устойчивость-ворот}

If $\Gamma,\widehat\Gamma$ are density matrices and $\|\Gamma-\widehat\Gamma\|_F\le\delta$, then

$$
|P-\widehat P|\le2\delta,\quad|Q-\widehat Q|\le2\delta,\quad|R-\widehat R|\le14\delta,\quad|\Phi-\widehat\Phi|\le112\delta.
$$

For the canonical E-projection, $|\mathrm{Coh}_E-\widehat{\mathrm{Coh}}_E|\le28\delta$, and the proxy differentiation error is at most $168\delta$. These bounds are conservative; ranges of the statistics can tighten them.

**Proof.** $|P-\widehat P|=|\langle\Gamma-\widehat\Gamma,\Gamma+\widehat\Gamma\rangle_{HS}|\le2\delta$ since state HS norms are at most one. The diagonal projection is an HS contraction, giving the same bound for $Q$. Use $P,Q\ge1/7$ in the reciprocal and quotient differences. For $\Phi=P/Q-1$, the two terms are bounded by $14\delta$ and $98\delta$. For the E numerator $B=\|\pi_E\Gamma\|_{HS}^2\le P$, $|B-\widehat B|\le2\delta$ and the two terms in $B/P$ sum to at most $28\delta$.

A gate is certified robustly only if its uncertainty interval stays on the required side of every boundary. A partial record reports unknown tests rather than guessing them. Literal extension entropy is not covered by the proxy bound.

## 3. Experience and the scope of No-Zombie claims

### Experiential record {#31-экспериенциальное-уравнение}

A typed content record can be written

$$
\mathsf{Exp}(z,t)=(\{(\lambda,P_\lambda)\},\mathsf{Context},\mathsf{History},\mathsf{Readout}).
$$

It is mathematically defined only after the experiential realisation and its normalised state are supplied. Calling this record experience is **[I]**. A hard gate multiplies or selects this record by $\mathbf1_{A_2}$ **[D]**. A sigmoid supplies a graded surrogate with declared smoothing parameters; it is not evidence that a sharp physical bifurcation exists.

### Base No-Zombie statement {#34-теорема-о-жизнеспособности-no-zombie-theorem}

Every valid state has $A_0$ by definition, so every viable state represented by the model also has $A_0$. This logical implication is **[T]** and has no independent empirical content concerning phenomenal consciousness. A stronger no-zombie implication must state the viability class, dynamics and experiential bridge separately.

The former argument “more than seven contexts forces a self-model and $R\ge1/3$” is **retracted [✗]**. A seven-dimensional density-matrix space has continuous parameters, not seven classical memory slots. Capacity depends on precision, noise, allowed measurements and resources; context-dependent control does not logically force a model of oneself. Task-specific necessity can only follow from an explicit policy class and resource/error bound, followed by a proved relation to the proposed reflection statistic.

## 4. Metamodel certificates and the cumulative hierarchy

### L3 [D]

For a declared finite or modelled probe family $\mathsf Q_2$ and an implemented metamodel, define

$$
e_2=\sup_q d_B(\widehat\rho_2(q),\rho_2(q)),\qquad v_2=\sup_{q,q'}d_B(\rho_2(q),\rho_2(q')).
$$

The certificate is $\mathsf{MetaCert}_2:=(e_2\le\varepsilon_2)\land(v_2\ge a_2>2\varepsilon_2)$ and $A_3:=A_2\land\mathsf{MetaCert}_2$. Targets represent independently observed first-model responses under the declared probes. Training and testing must not define targets by the metamodel's own output. The choice of probes, tolerances and identification with reflective depth is an operational proposal **[D]/[Pr]**, not a universal categorical derivation.

**Proposition (nonvacuity) [T].** A constant prediction cannot satisfy this certificate. If it did, the triangle inequality would give $d_B(\rho_2(q),\rho_2(q'))\le2\varepsilon_2$ for all pairs, contradicting $v_2\ge a_2>2\varepsilon_2$.

The old T-67 quadratic-component proof is **retracted [✗]**. A nonzero derivative can have a kernel; a CPTP channel may be a replacement channel with zero derivative. A choice of three generator terms plus one modification does not imply four statistically independent channels or a universal $1/4$ prediction threshold.

### Metastability requires dynamics {#теорема-32-метастабильность-l3}

The former universal metastability theorem is **retracted [✗]**. **Conditional local stability [C].** For a smooth finite-dimensional flow at an interior equilibrium, if its tangent Jacobian has all eigenvalues with negative real part, the equilibrium is locally asymptotically stable. To infer retention of $A_3$, require the equilibrium's certificate to have a positive margin and the perturbations to remain in its neighbourhood. Escape times with noise require a specified stochastic process. A fidelity score alone supplies neither a Jacobian nor a lifetime.

### L4 [D]

Define certificates $\mathsf{MetaCert}_n$ for every $n\ge2$ on declared output spaces and probe families. Supply forgetting maps $r_n$ between successive outputs and maps $p_n$ between probe families such that

$$
r_n(\widehat\rho_{n+1}(q))=\widehat\rho_n(p_nq)
$$

in the ideal model, with the analogous target compatibility. If approximate compatibility is intended, its error budget is part of the certificate. Then $A_4:=A_3\land\bigwedge_{n\ge3}\mathsf{MetaCert}_n\land\mathsf{Compatible}$. This definition ensures nesting. It does not prove physical realisability or unreachability.

The old condition $P>6/7$ and its “stability proof” are **retracted [✗]**: $A_4$ inherits $P\le3/7$ from $A_2$. Finite-dimensionality does not identify a purity threshold with a homotopy degree.

## 5. What model iteration actually proves

Use **root fidelity**

$$
f(\rho,\sigma)=\operatorname{Tr}\sqrt{\sqrt\rho\,\sigma\sqrt\rho},\qquad F=f^2,\qquad d_B^2=2-2f.
$$

The square convention is recorded to prevent threshold ambiguity. These are standard state metrics, not the canonical $R$.

### Corrected convergence statement [T] {#теорема-4-3}

If a state map $T$ has an orbit $\rho_n=T^n\rho_0$ converging to a state $\rho_*$, then $f(\rho_{n-1},\rho_n)\to1$ by continuity. A sufficient condition is a uniform contraction $d(T\rho,T\sigma)\le qd(\rho,\sigma)$ with $q<1$ on a complete invariant metric state space; Banach's theorem then yields convergence. CPTP gives nonexpansiveness in appropriate metrics, not strict contraction or a unique fixed point.

For the canonical model

$$
\varphi_{\mathrm{coh}}(\rho)=(1-R(\rho))\mathcal D_\alpha(\rho)+R(\rho)I/7,
$$

where $\mathcal D_\alpha$ preserves the diagonal and multiplies off-diagonals by $1-\alpha$, $0\le\alpha\le1$, there is the exact estimate

$$
\|\varphi_{\mathrm{coh}}(\rho)-I/7\|_F\le\frac67\|\rho-I/7\|_F.
$$

**Proof.** $1-R\le6/7$, $\mathcal D_\alpha(I/7)=I/7$, and the diagonal/off-diagonal splitting makes $\mathcal D_\alpha$ an HS contraction. Iterate the estimate. Thus every orbit converges to $I/7$, and successive fidelities tend to one although this attractor fails the L2 gate. This estimate relative to the fixed point does not assert contraction between every pair of states.

For the Fano case $\alpha=2/3$ and nonzero initial off-diagonal part, the actual canonical-model coherence survival is

$$
S^{(n)}_{\varphi_{\mathrm{coh}}}=3^{-n}\prod_{j=0}^{n-1}(1-R(\rho_j))\le(2/7)^n.
$$

The equality $S^{(n)}=3^{-n}$ holds for iteration of the **bare linear Fano channel**, not for the full state-dependent canonical model. Fidelity tending to one and coherence tending to zero are compatible and do not establish deeper cognition.

At $\rho_*=I/7$, every successive fidelity is already one at finite order. For a unitary CPTP channel swapping two orthogonal pure states, consecutive fidelities are zero. Hence neither finite-order nonattainability of fidelity one nor universal positivity follows from the CPTP property.

### Withdrawn purity/topology argument {#теорема-4-2}

The former universal L4 stability and $P>6/7$ proof are **retracted [✗]**. Concentration of eigenvalues can bound matrix distances. It does not make $\pi_6$ of a separately assigned experiential object vanish, stabilise a Postnikov tower, or force the state-valued self-model to avoid fixed points.

## 6. Categorical structure: precise scope

A Postnikov tower applies to an object $X$ of an $\infty$-topos:

$$
\cdots\to\tau_{\le3}X\to\tau_{\le2}X\to\tau_{\le1}X\to\tau_{\le0}X.
$$

There is a comparison $X\to\varprojlim_n\tau_{\le n}X$; its being an equivalence is the relevant objectwise convergence assumption. No canonical forward-colimit reconstruction or Bures norm between categories is supplied by this notation. Standard references: [Kerodon §3.5](https://kerodon.net/tag/0513) and [definition of a Postnikov tower](https://kerodon.net/tag/055L); [Lurie, Higher Topos Theory §§5.5.6, 7.2.1](https://www.math.ias.edu/~lurie/papers/HTT.pdf).

**Counterexamples [T].** A discrete set is zero-truncated, and its tower stabilises immediately. A representable presheaf on an ordinary category is set-valued, hence zero-truncated; truncation does not recover different scalar L-gates. The entire density-matrix space is convex and therefore contractible. Nontrivial topology may appear in a separately chosen ray space or constraint subspace, but that choice and its relation to operational certificates need a bridge. A claim “every level has $\pi_n\ne0$” does not follow from truncation.

### No theorem that five labels exhaust physical depth {#теорема-43-l4--максимальный-уровень}

The present taxonomy has five labels by definition. Between L3 and its ideal all-order L4 limit one can retain finite certified depths $n=2,3,\ldots$ as an auxiliary statistic. There is no theorem that all systems have at most three metamodel orders. A bounded score obtained by repeating a Fano channel and comparing with chosen thresholds is a bound on **that score**, not on every possible implementation of reflective depth.

### Associator hierarchy {#иерархия-ассоциаторов}

Composition laws and coherence axioms must be specified for the chosen higher category. Nonassociativity of octonions, bicategorical associators, and statistical dependence of channels are different structures. Counting their cells does not determine calibrated Bayes priors or a metacognition threshold. An experiential higher-category model may be proposed **[Pr]**; its operational realisation requires a functor and a correspondence theorem.

## 7. Gap: the correct theorem

For $s(z)=\mathbf G(\Gamma)$, a classification descends through $s$ exactly when it is constant on its fibres. **Proof [T]:** $L=\ell\circ s$ implies fibre constancy; conversely define $\ell(s(z))=L(z)$, well-defined precisely under fibre constancy. This is a factorisation criterion, not an injection from levels into profiles.

Let $u=(1,\ldots,1)/\sqrt7$ and $\Gamma(t)=(1-t)I/7+tuu^\dagger$. Every Gap equals zero, but

$$
P=(1+6t^2)/7,\quad R=1/(1+6t^2),\quad\Phi=6t^2.
$$

At $t=0.45$ all three scalar gates pass; at $t=0.65$ the reflection gate fails. With the explicitly declared proxy,

$$
\mathrm{Coh}_E(t)=\frac{1+12t^2}{7(1+6t^2)},\qquad D^{7D}(t)=1+6\mathrm{Coh}_E(t),
$$

and both states pass $A_1$ and $D^{7D}\ge2$. Thus the **defined 7D-proxy L2 predicate itself** differs despite identical phase profiles. This stronger algebraic counterexample does not establish physical consciousness in either state. In literal extension mode, differentiation and lift are additional data.

For a genuine matrix self-model error $\delta$ and a nonzero amplitude floor $m>\delta$, the per-channel phase error is bounded by $2\delta/m$. Without the floor it is discontinuous at zero. Exact proof, even-rank correction and the withdrawn Hamming-opacity bridge: [Gap identifiability](/docs/consciousness/hierarchy/gap-characterization).

## 8. Thresholds are not automatically bifurcations {#бифуркационные-критерии}

A scalar gate crossing need not change an attractor's stability. A one-dimensional gradient reduction $\dot x=-\partial_xV$ has an $A_k$ potential singularity only under the appropriate degeneracy and transverse unfolding. In the potential convention:

| Type | Germ | Essential control parameters |
|---|---|---:|
| Fold $A_2$ | $x^3$ | 1 |
| Cusp $A_3$ | $x^4$ | 2 |
| Swallowtail $A_4$ | $x^5$ | 3 |

For $A_4$, require $V'=V''=V'''=V''''=0$, $V^{(5)}\ne0$ at the critical point, a valid smooth reduction, and transversality of the three unfolding directions. Merely possessing three parameters is insufficient; an approximate symmetry or a quartic potential does not establish these conditions. The relation between the resulting branches and $A_k(z)$ is another explicit step. Reference for the corresponding vector-field normal forms: [Ghrist, Applied Dynamical Systems, bifurcation chapter](https://www2.math.upenn.edu/~ghrist/preprints/ADS-DRAFT.pdf).

## 9. Stratification and marginal locality {#стратификационная-изоляция}

L-labels do not turn a nonlinear term on or off by themselves. Its gate and extension are specified by the evolution equation. In particular L0 is universal and can have any allowed $R$, including $R=1$ at $I/7$.

**Marginal identity [T].** For a fixed trace-preserving local channel $\mathcal T_A$,

$$
\operatorname{Tr}_A[(\mathcal T_A\otimes\mathrm{id}_B)(\Gamma_{AB})]=\Gamma_B.
$$

The identity also holds pointwise if the channel is selected from the unconditioned local state, provided a valid local channel extension is given at each point. It is not a theorem about a generic nonlinear state map acting on tensor factors. For nonlinear dynamics, averaging selectively conditioned branches can differ from evolving the unconditioned state; the measurement prescription matters. Current scope: [Physics correspondence §8](/docs/proofs/physics/physics-correspondence#запрет-сигнализации).

## 10. Classification algorithm {#61-алгоритм-классификации-уровня}

```text
Require a valid density matrix and declared experiential mode.
P = sum_ij |gamma_ij|^2; Q = sum_i gamma_ii^2
R = 1/(7*P); Phi = (P-Q)/Q
Proxy mode: Coh_E = (gamma_EE^2 + 2*sum_i!=E |gamma_Ei|^2)/P
            A1 = Coh_E > 0; D = 1 + 6*Coh_E
Extension mode: require a normalised declared rho_E
                A1 = rank(rho_E) > 1; D = exp(-Tr(rho_E log rho_E))
A2 = A1 and P > 2/7 and R >= 1/3 and Phi >= 1 and D >= 2
A3 = A2 and verified MetaCert_2
A4 = A3 and verified compatible certificates at every higher order
Return the greatest verified A_k and all unknown/margin-dependent tests.
```

Squared norms are used consistently. State validation, extension entropy and metamodel certificates are distinct operations. The scalar computations are $O(N^2)$; positivity checks and spectral operations generally require $O(N^3)$ dense linear algebra. The all-order predicate is not certified merely by numerically iterating a map a finite number of times.

## 11. Dependency and withdrawal ledger

| Former claim | Current scope |
|---|---|
| Different L-levels force different Gap profiles | **[✗]**; replaced by fibre criterion and explicit counterexample |
| Three check bits require three nonzero pairwise Gaps | **[✗]**; code-to-observable bridge open **[Pr]** |
| T-67: categorical count forces $K=4$ and L3 fidelity threshold | **[✗]**; calibrated metamodel certificate **[D]/[Pr]** |
| T-86: universal L4 unreachability from Postnikov + incompleteness | **[✗]**; inverse tower and conditional resource bound |
| $P>6/7$ defines nested L4 | **[✗]**; incompatible with inherited L2 window |
| CPTP alone forces strict contraction and positive consecutive fidelity | **[✗]**; stated contraction/convergence assumptions |
| Twelve Boolean gate labels are twelve nonempty regions | **[✗]**; feasibility bound $\Phi\le7P-1$ **[T]** |
| T-41: three controls force an $A_4$ transition | **[✗]**; normal-form criteria needed |
| Adaptive generalisation universally forces canonical $R\ge1/3$ | **[✗]**; explicit task/resource bridge needed |

The valid inequalities remain available as mathematical tools. Their physical interpretation and measurement bridge are separate obligations; none is supplied by changing a status label.
