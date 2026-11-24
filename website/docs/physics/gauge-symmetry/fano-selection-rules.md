---
sidebar_position: 3
title: "Selection in a Fano basis"
description: "Support of the octonionic three-form and a conditional interaction vertex"
---

# Selection in a Fano basis

## Support of the trilinear form {#теорема-фано-отбор-fijk}

In an orthonormal imaginary-octonion basis define $f_{ijk}=\langle e_i e_j,e_k\rangle$. For distinct units, $f_{ijk}$ is nonzero exactly on an oriented Fano line and equals $+1$ or $-1$ according to the ordering. Mark $E=5$ and $U=6$. The unique third index is $A=1$ because $(5,6,1)$ is a line. Thus $f_{1EU}=1$ and $f_{kEU}=0$ for all $k\ne1$. Choosing another pair selects a different component by the same calculation. [Multiplication table](./g2-structure#октонионное-умножение-и-g2).

## From a component to an interaction {#каппа-по-подавленным}

A model may declare $y_k=c\,f_{kEU}$ for a particular vertex. Given the marked axes this fixes the zero pattern of that vertex and leaves $c$ free. The calculation requires the marked frame. Under a change of frame the tensor, the external states and the measurement of the vertex must transform together.

To infer a physical mass hierarchy, specify which fields carry each index, their gauge quantum numbers, the Higgs vacuum and all other allowed terms in the interaction. An additional invariant coupling can alter the mass matrix without changing the chosen Fano table. A loop estimate also needs propagators, vertex normalizations and a perturbative regime. [Yukawa matrices](../particle-physics/yukawa-hierarchy).

## Constructive isomorphism $\mathrm{PSL}(2,\mathbb{F}_7) \simeq \mathrm{GL}(3,\mathbb{F}_2) = \mathrm{Aut}(\mathrm{PG}(2,2))$ {#psl2-7-fano-bridge}

The automorphism group of the Fano plane $\mathrm{PG}(2,2)$ provides an exact, zero-axiom algebraic-geometric bridge to the modular flavor symmetry of the magnetized $M = 7$ torus orbifold (`verify_deep_frontier_v8.py`–`verify_deep_frontier_v9.py`, `ToEFrontierV8.lean`–`ToEFrontierV9.lean`):

1. **Zero-axiom constructive group isomorphism (`gl3_f2_generators_psl2_7_relations`, `gl3_f2_order_168_generated_by_psl2_7`) [T]:** Explicit binary $3\times 3$ matrices $A_S, A_T \in \mathrm{GL}(3,\mathbb{F}_2)$ satisfy $\det = 1$, all four Hurwitz $\mathrm{PSL}(2,7)$ relations ($A_S^2 = I$, $A_T^7 = I$, $(A_S A_T)^3 = I$, $(A_S A_T^4)^4 = I$), preserve all 7 collinear Fano lines, and decompose all $168$ elements of $\mathrm{GL}(3,\mathbb{F}_2)$ into $8$ disjoint Bruhat cosets over the $21$-element Frobenius Borel subgroup $B_{21}$ ($8 \times 21 = 168$).
2. **Exact character equivalence and Klein quartic (`sym2_three_eq_fano_six_and_singer_trace`) [T]:** Under this bijection, the symmetric Yukawa space $\mathrm{Sym}^2(H_3^-)$ of the 3 odd Landau generations on $(T^2/\mathbb{Z}_2, M=7)$ is character-isomorphic to the nontrivial Fano harmonic space $\mathbb{C}[\mathrm{PG}(2,2)]/\mathbb{C}\cdot 1 \cong \mathbf{6}$ across all 168 group elements ($\max\lvert\Delta\chi\rvert = 7.94\times 10^{-14}$), the Singer 7-cycle $A_T$ fixes $0$ Fano points while the involution $A_S$ fixes $3$ (one Fano line), and the Klein quartic $K(z) = -z_1^3 z_2 + z_2^3 z_3 + z_3^3 z_1$ is strictly invariant (error $1.1\text{–}3.2\times 10^{-15}$).
3. **Joyce $T^7/\mathbb{Z}_2^3$ no-go and gauge-lifted $G_2$-instanton Kähler lock (`joyce_t7_z2_cubed_b2_zero_and_g2_lock`, `g2_ym_bps_minimum_at_ratio_seven_cq`, F-35A,B) [T] / [C]:** On the flat 7-torus with associative Cayley–Dickson 3-form $\varphi$, a single $T^2_{12}$ flux ($M = 7$) violates the $G_2$-instanton equation ($\lVert F \wedge *\varphi\rVert = 7 \neq 0$), and every untwisted basis 2-form on Joyce's $G_2$ orbifold $T^7/\mathbb{Z}_2^3$ is projected out ($b_2^{\mathrm{untw}} = 0/21$) [✗]. However, both planes $(1,2)$ and $(3,4)$ share the exact $\mathbb{Z}_2^3$ parity `(+1,+1,-1)`: lifting the involution $\gamma$ by $\mathrm{Spin}(10)$ Weyl charge conjugation $\hat{\gamma}(H) = -H$ makes $F \otimes H = \bigl((7/A_{12}) e^{12} - (1/A_{34}) e^{34}\bigr) \otimes H$ strictly $\mathbb{Z}_2^3$-invariant, solves all 7 $G_2$-instanton equations **if and only if the Kähler area ratio locks to $A_{12}/A_{34} = 7$** (the unique strict BPS Yang–Mills minimum $E_{\mathrm{YM}}(r) = \frac{1}{2}(49/r + r) \ge 7$), and yields exact $N_g = 3 \times 1 = 3$ generations $H_3^-(7) \otimes \bar{H}_1^+(-1)$ under $\mathrm{PSL}(2,7) \simeq \mathrm{GL}(3,\mathbb{F}_2)$ [C]. Stabilizing the complex structure $\tau = 0.25 + 1.5i$ and Joyce blow-up moduli remains open [P].
