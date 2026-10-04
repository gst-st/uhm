---
title: "Minimality: Exact Bounds and Their Assumptions"
sidebar_position: 1
description: Diagnosability and faithful-representation bounds; functional-role claims corrected
---

# Minimality: exact bounds and their assumptions

$N=7$ is the selected UHM dimension [P]. This page gives two rigorous lower bounds with distinct premises. The former claim that seven functional roles alone prove seven independent Hilbert coordinates is withdrawn [✗] (2026-10-03). The octonionic route supplies structure for a selected seven-dimensional frame; it does not remove the premises below.

## Functional roles and linear dimension

Articulation, structure, dynamics, logic, interiority, ground and unity are the seven semantic roles of the chosen model [D]/[I]. A role is not a vector, and the existence of different operators does not force different basis coordinates.

**Counterexample [T].** On $\mathbb C^2$ set $P=(I+Z)/2$, $H=X$ using Pauli matrices. Then $P^2=P$, $H=H^\dagger$, $U_t=e^{-itH}$ is nontrivial, $[P,H]=iY\ne0$, and the trace provides normalization. Thus the algebraic functions assigned to A,S,D,L,U coexist in dimension two. This does not establish autopoiesis or experience in a qubit; it refutes the proposed deduction from operator roles to Hilbert dimension.

The former pairwise independence table used $[P_A,P_S]\ne0$ for orthogonal basis projectors; in fact both products vanish. Pairwise distinctions of functions would still not prove joint linear independence. Removing the *label* U does not remove the trace on $M_6(\mathbb C)$, and removing a label L does not remove matrix commutators.

## Track Σ: perfect single-fault diagnosis {#теорема-строгая-необходимость-7}

Fix an $N$-axis status grammar $\mathcal C\subseteq\mathbb F_2^N$ satisfying:

1. $d_{\min}(\mathcal C)\ge3$;
2. the Hamming balls of radius one around its words partition $\mathbb F_2^N$;
3. $|\mathcal C|>2$.

These are exact coding assumptions [D]. Their application to **every** alternative physical decomposition is the premise $(\Sigma_6)$ [H], not a consequence of the labels A–U.

**T-349(a), coding theorem [T].** $N\in\{7,15,31,\ldots\}$, in particular $N\ge7$.

**Proof.** Every radius-one ball contains $N+1$ words. The partition gives $(N+1)|\mathcal C|=2^N$. Therefore $N+1=2^r$ for an integer $r\ge1$. At $N=1$ and $N=3$, the cardinalities are respectively one and two, contradicting assumption 3. Hence $r\ge3$ and $N\ge7$. $\square$

**Attainment [T].** For $N=7$, take the $3\times7$ parity-check matrix whose columns are all nonzero vectors of $\mathbb F_2^3$. Its kernel has 16 words. No weight-one or weight-two word is in the kernel, and every nonzero syndrome labels exactly one column. Therefore it corrects every single fault uniquely and its radius-one balls partition the cube.

**Physical lower bound [C at (Σ₆)].** If every admissible decomposition satisfies these assumptions, every admissible decomposition has at least seven axes. If an admissible physical seven-axis realization is also supplied, its minimum is seven. The code establishes attainment of the *coding* bound; it does not prove biological realization or phenomenal content.

<a id="t-349"></a>

**T-349(c), strictness of the premise [T].** The length-15 Hamming code has dimension 11, distance three and $(1+15)2^{11}=2^{15}$, so it meets assumptions 1–3 while no real normed division algebra has dimension 16. Perfect diagnosis does not imply a normed division algebra for every allowed $N$. The former hosting argument likewise starts from Hurwitz's list and cannot replace its division-algebra premise.

## Track A_int: faithful finite-dimensional representation {#representation-bound}

Fix the algebra

$$
A_{\mathrm{int}}=\mathbb C\oplus M_3(\mathbb C)\oplus M_3(\mathbb C).
$$

**Representation theorem [T].** A unital faithful $*$-representation $A_{\mathrm{int}}\to M_N(\mathbb C)$ exists iff $N\ge7$. At $N=7$ it is multiplicity-free and unique up to unitary equivalence.

**Proof.** The three central units give an orthogonal decomposition of the representation space. On the scalar sector the representation has multiplicity $m_0$; matrix units in either $M_3$ sector identify three equal-dimensional ranges, giving dimensions $3m_1$ and $3m_2$. Faithfulness requires $m_i\ge1$. Hence $N=m_0+3m_1+3m_2\ge7$. Conversely choose $(m_0,m_1,m_2)=(N-6,1,1)$. At equality all multiplicities are one, and orthonormal identifications of the three sectors differ by a unitary. $\square$

This strengthens the mathematical dimension statement without identifying operator *names* with coordinates. Selecting $A_{\mathrm{int}}$ as the internal observable algebra remains a structural input; the theorem does not derive that algebra from autopoiesis. Moreover $A_{\mathrm{int}}$ is not $M_7(\mathbb C)$, and restricting a state by sector pinching loses inter-sector coherences. See [T-174](/docs/intro).

## Seven-dimensional realizations {#часть-iv-доказательство-достаточности-конструктивное}

The matrix space $D_7$, its semantic frame, the Fano channel and explicit self-models are mathematically realizable. For a fixed anchor, channel, rates and Hamiltonian, a viable stationary solution requires proof of its existence, its gate margins and the relevant stability. The [φ dynamics](/docs/core/operators/phi-operator) supplies examples for stated parameter regimes.

The former proof initiated the system at $I/7$ and asserted autonomous regeneration through a gate that is zero there. That genesis argument is withdrawn [✗]. The canonical unital self-model does not sustain isolated life; a non-unital anchor or environment is additional data. A pure E-state can have nonzero variance for other observables, so rank one does not mean “all observables have zero variance.” Neither a fixed point nor a nonzero E-entry establishes experience.

## Rosen correspondence {#часть-v-связь-с-mr-системами-розена}

An (M,R)-system contains typed maps $f:A\to B$, repair into a mapping object and specified closure. A table pairing its roles with UHM labels is an interpretation [I]. An isomorphism requires actual objects, arrows, a functor, full faithfulness and essential surjectivity (or explicit inverse maps), not a role count. No categorical isomorphism with a unique minimal phenomenal (M,R)-system is asserted here.

## Basis and clock {#часть-vii-теорема-о-единственности-базиса}

A,S,D,L,E,O,U label a chosen orthonormal frame [D]. Its uniqueness is not proved by general properties of projectors, Hamiltonians, traces or commutators. Preserving a specified octonion multiplication restricts *frame transformations*; it does not determine a neural encoder or identify a physical experiential axis.

### E and O {#единственность-e}

<a id="единственность-o"></a>
<a id="ортогональность-eo"></a>

Distinct roles for E and O can be specified in the model. Their orthogonality then follows from the chosen orthonormal basis, not from causal independence. A literal clock factor must be a tensor factor of an extended realization; a one-dimensional O-axis in $\mathbb C^7$ cannot itself be a seven-state clock. No general uniqueness or physical necessity of E/O follows from a chosen formula for $\kappa$.

## Octonionic structure {#часть-ix-октонионный-вывод}

A real unital normed division algebra which is nonassociative is the octonions by Hurwitz [T], with seven imaginary dimensions. Given a Fano design, naturality under its collineations selects the canonical octonionic orientation class [T]; selecting a division algebra or a sharp minimal Fano instrument is an additional premise. The channel coefficient $1/3$, the unordered design and its oriented multiplication are different objects. See [octonionic derivation](/docs/proofs/minimality/theorem-octonionic-derivation#каноническая-ориентация).

## Open problem and sources {#часть-viii-ограничения-и-открытые-вопросы}

Derive a validated physical requirement that forces $(\Sigma_6)$ or $A_{\mathrm{int}}$, or produce comparative evidence that the seven-axis model outperforms alternative dimensions at matched complexity. The functional dictionary alone does neither.

- R. W. Hamming, [Error Detecting and Error Correcting Codes](https://doi.org/10.1002/j.1538-7305.1950.tb00463.x): diagnosis and packing assumptions.
- John C. Baez, [The Octonions](https://arxiv.org/abs/math/0105155): the division-algebra classification and Fano multiplication.
- [Typed mathematical kernel](/docs/reference/mathematical-kernel): distinction between states, processes, logic and physical bridges.

The counterexamples and coding construction are checked in `website/scripts/check_mathematical_kernel.py`. Retired functional necessity/uniqueness claims T-40c–T-40f are not premises of the replacement bounds.

## Historical links

<a id="определение-12-mr-система-розена"></a>
<a id="конструктивные-контрпримеры"></a>
<a id="теорема-31-необходимость-7-измерений"></a>
<a id="случай-n--6-удаление-единства-u"></a>
<a id="случай-n--3-удаление-логики-l"></a>
<a id="случай-n--2-удаление-динамики-d"></a>
<a id="случай-n--1-удаление-структуры-s"></a>
<a id="случай-n--0-удаление-артикуляции-a"></a>
<a id="итог-части-iii"></a>
<a id="проблема-5-мост"></a>
<a id="трек-сигма"></a>

The old role-removal and functional-uniqueness arguments are withdrawn. Their links resolve to the corrected bounds and explicit assumptions above.
