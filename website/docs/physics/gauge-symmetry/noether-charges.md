---
sidebar_position: 5
title: "G₂ Noether Charges and Ward Identities"
slug: /physics/gauge-symmetry/noether-charges
description: "Conditional Noether charges, typed invariant covariances, chosen Fano incidence and the withdrawn AP/PH phase bridge"
---

# G₂ Noether Charges and Ward Identities

A supplied positive three-form has stabilizer $G_2$ [T]. Conservation laws require a **supplied action and dynamics** possessing that continuous symmetry. A fixed Fano-coordinate instrument, Hamiltonian, regeneration target or external forcing can break it. The former universal fourteen-charge claim and closed AP/PH bridge are withdrawn as statements about all UHM models [✗].

## 1. Conditional Noether theorem

For a differentiable action $L(q,\dot q)$, generators $\delta_aq$ of a $G_2$ action, and variations $\delta_aL=dB_a/dt$, define

$$
Q_a=\sum_i\frac{\partial L}{\partial\dot q_i}\delta_aq_i-B_a,\qquad a=1,\ldots,14.
$$

On Euler–Lagrange solutions $\dot Q_a=0$ [T under these hypotheses]. If generalized forces $F_i$ are added and the symmetry variation is $\delta_aL-dB_a/dt=\Delta_a$, then

$$
\dot Q_a=\sum_iF_i\delta_aq_i+\Delta_a.
$$

Neither the count of generators nor covariance of a dissipative channel makes these quantities conserved. [Noether, *Invariant Variation Problems*](https://arxiv.org/abs/physics/0503066).

## 2. Representation and charge typing

The adjoint representation of $G_2$ is irreducible of dimension fourteen. A coordinate choice can list fourteen generators in two groups of seven, but that is not an invariant $\mathbf7\oplus\mathbf7$ decomposition. The old explicit seven “Fano circulation” and seven “complementary” formulas were not derived from a specified action and are withdrawn as universal charges [✗].

For a specified $SU(3)=\operatorname{Stab}_{G_2}(v)$, the complexified branching is $\mathbf{14}=\mathbf8\oplus\mathbf3\oplus\bar{\mathbf3}$ [T]. Spontaneous selection of a vacuum with stabilizer $SU(3)$ does not erase the other six conservation laws of an exactly invariant action. Explicit symmetry breaking and dissipation are separate mechanisms.

If $\Pi_p$ is a diagonal Fano-line projector and $G=\operatorname{Im}\Gamma$ is skew with zero diagonal, $\operatorname{Tr}(G\Pi_p)=0$ exactly. The former identification of this trace with a sum of off-diagonal phases is withdrawn [✗]. A proposed circulation must instead define an oriented weighting or measurement and establish its dynamical meaning [D/H].

## 3. Stabilizers, Goldstone claims and protection

The [correct Gap stabilizer](/docs/core/dynamics/gap-operator#стабилизаторы) depends on its seven/adjoint components, not its real rank alone. For $\iota_v\varphi\ne0$ the stabilizer is $SU(3)_v$ and matrix rank is six. A regular pure adjoint element has stabilizer $T^2$; a general sum can have a smaller or discrete stabilizer.

For a selected invariant potential, tangent directions to an orbit of minima have zero Hessian in the conservative unconstrained model [T/C]. Physical Goldstone spectra additionally require field/limit assumptions and a kinetic operator. In open systems frequencies and relaxation rates come from the actual linearized dynamics. The old universal $m^2=\Gamma_2\kappa_0/|\gamma|^2$, lifetimes, rank-only mode counts and fMRI assignments are withdrawn as theorems [✗]; experimental connections remain hypotheses [H].

For the specific orbit $G_2/T^2$, $\pi_2\simeq\mathbb Z^2$ [T]. To use this as field-texture protection requires a spatial domain and boundary/homotopy constraints. A single density state can follow the positive path $I/7+t(\Gamma-I/7)$ to zero Gap. No additional universal nondecaying mode follows from the orbit identity.

## 4. Correct invariant correlators {#тождества-уорда-разложение}

Let the random variable take values in $W=\Lambda^2\mathbb R^7=\mathbf7\oplus\mathbf{14}$ for the **chosen** three-form. If its probability law is $G_2$-invariant, its covariance $C$ obeys

$$
R_a C+C R_a^{\mathsf T}=0
$$

for the induced skew generators $R_a$ acting on **both** tensor legs. This is a matrix system of constraints, not fourteen scalar equations; the old dimension $231-14=217$ is withdrawn [✗]. By the multiplicity-free decomposition and Schur's lemma,

$$
C=c_7\mathsf P_7+c_{14}\mathsf P_{14},\qquad c_7,c_{14}\ge0.
$$

The real symmetric invariant covariance space has dimension two [T]. Symmetry leaves both amplitudes free. Fixing total trace leaves a free ratio. Ward identities do not determine $c_7/c_{14}$ or the number $19/49$.

A vacuum breaking $G_2$ to $SU(3)$ need only have the smaller group's covariance, with further independent blocks. Driven, dissipative steady states need not satisfy equilibrium Ward/KMS assumptions. A spectral group identity alone does not specify their distribution.

## 5. The chosen incidence matrix $F_{21}$ {#оператор-f21-определение}

Index the 21 **unordered edges** of a chosen Fano plane. Define $F_{ee'}=1$ only when $e\ne e'$ and the two edges lie on the same line, and zero otherwise. Every edge belongs to one line; each line has three edges. Thus

$$
F_{21}\simeq\operatorname{diag}(J_3-I_3,\ldots,J_3-I_3)
$$

with seven blocks. These are incidence calculations [T], not a derived continuous symmetry of arbitrary coherences.

### Spectrum and projectors {#собственные-значения-f21}

$$
\sigma(F_{21})=\{2^{(7)},-1^{(14)}\},\quad F_{21}^2=F_{21}+2I.
$$

The coordinate eigenspace projectors are

$$
P_+=(F_{21}+I)/3,\qquad P_-=(2I-F_{21})/3.
$$

Equal dimensions seven and fourteen do not identify these **unsigned-edge** projectors with $\mathsf P_7,\mathsf P_{14}$ in the signed wedge representation of $G_2$. An explicit intertwining would be required and was not supplied. The old automatic identification is withdrawn [✗].

### Traces {#следы-f21}

$$
\operatorname{Tr}I=21,\quad\operatorname{Tr}F_{21}=0,\quad\operatorname{Tr}F_{21}^2=42,\quad F_{21}\mathbf1=2\mathbf1.
$$

### Conditional numerical factor {#коррелятор-собственные-значения}

Choosing the coordinate model

$$
C=\alpha I-\frac{3\alpha}{7}F_{21}+\frac{3\alpha}{49}F_{21}^2,\qquad\alpha\ge0
$$

gives eigenvalues $19\alpha/49$ and $73\alpha/49$ [T at this choice]. Since $P_+\mathbf1=\mathbf1$, $\mathbf1^{\mathsf T}C\mathbf1=21(19\alpha/49)$. This proves arithmetic for supplied coefficients [D], not their Ward derivation, unique cosmological suppression or physical calibration [✗/H]. Choosing other nonnegative eigenvalues gives equally valid coordinate covariances.

## 6. Fluctuation–dissipation requires a statistical state

At thermal equilibrium, with a specified observable, Hamiltonian and KMS state, the fluctuation–dissipation relation connects the symmetrized fluctuation spectrum to the dissipative response [T under these hypotheses]. A memory kernel or a regeneration law does not supply that equilibrium state. Outside equilibrium, noise and response must be modeled/measured independently; no universal effective temperature or factor follows. [Kubo, 1957](https://doi.org/10.1143/JPSJ.12.570).

## 7. The withdrawn AP/PH closure bridge {#шаг-6-доказательство}

The previous Theorem 13.0 and Theorem 13.1 / T-165 are withdrawn [✗]. The eight-step argument failed at several independent implications:

- Nonzero reflection or reproduction does not imply invertibility of a self-map. Even an invertible linear channel can contract coherence; its inverse need not be positive. The [RI theorem](/docs/proofs/categorical/uniqueness-theorem#теорема-единственности) requires reversible state-space identification and preservation of supplied structure, not just an AP label.
- $\mathrm{Coh}_E>0$ includes E population and does not imply a nonzero off-diagonal entry. E's semantic role does not force Hamiltonian detuning; $H=0$ is admissible.
- Nonzero complex pair phases need not yield a nonzero summed triangle potential. Triangle terms can cancel; rank-one coherences $z_i\bar z_j$ have zero triangle phase for every triple. Octonion associators do not impose scalar frequency nonadditivity.
- A real positive state with real target, zero Hamiltonian and diagonal dissipator is a phase-Gap counterexample. The selected polynomial $V_3$ was itself withdrawn as $G_2$ invariant. Dissipation can be irreversible with no such cubic term.

Normed octonion multiplication, its associative Fano-line subalgebras and off-line associators remain correct algebra [T **given that algebra**]. They do not prove that AP/PH/QG force that algebra or PT violation. A physical realization and microscopic phase coupling remain a research program [Pr/H]. The native E-axis is a one-dimensional summand; an experiential tensor factor also needs separate data.

## 8. Status and related constructions

| Result | Status |
|---|---|
| Noether charges for a supplied invariant action | [T/C] |
| Irreducible adjoint dimension 14 and specified SU(3) branching | [T] |
| Invariant covariance has two free eigenvalues | [T/C] |
| $F_{21}$ block spectrum, CH identity, coordinate projectors | [T at D] |
| Automatic $F_{21}$↔continuous $G_2$ identification and Ward factor $19/49$ | [✗] |
| Universal AP/PH⇒PT closure T-165 | [✗] |
| Calibrated phase dynamics, effective action and physical inference | [H/Pr] |

See [Gap operator](/docs/core/dynamics/gap-operator), [Gap thermodynamics](/docs/core/dynamics/gap-thermodynamics), [Lindblad operators](/docs/core/operators/lindblad-operators), [conditional reconstruction](/docs/proofs/categorical/uniqueness-theorem) and the [mathematical kernel](/docs/reference/mathematical-kernel).

<a id="5-топологические-заряды-и-защита-gap-конфигураций"></a>
<a id="6-тождества-уорда-для-gap-корреляторов"></a>
