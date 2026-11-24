---
sidebar_position: 1
title: "Counting clock modes and matter families"
description: "A finite orbit calculation, real clock harmonics and the independence of family multiplicity"
---

# Counting clock modes and matter families

## Three real harmonics {#теорема-ровно-три-генерации}

<a id="поколения-t328"></a>

A cyclic shift on seven states has the complex characters $k=0,\ldots,6$. In a real signal the six nonconstant characters form three conjugate pairs $\{1,6\}$, $\{2,5\}$, $\{3,4\}$. Each gives one real two-dimensional harmonic plane. The quadratic residues $\{1,2,4\}$ select one representative per pair. Assigning one fermion family to each plane is the hypothesis (GC). For any matter representation $V$, the same internal group acts on $V^{\oplus m}$ for every positive $m$.

## Pairings at a Fano point {#thm-2-1}

Fix a Fano point $O$. The four lines avoiding it are the vertices of a tetrahedron. Each of the other six points lies on two of these lines and labels the corresponding edge. The three lines through $O$ pair opposite edges. Its stabilizer $S_4$ permutes the tetrahedron vertices.

Among the 15 perfect matchings of the six edges, one contains all three opposite pairs. Six contain exactly one (three choices of opposite pair, two crossings of the rest), and eight contain none. Burnside's count shows each group is one orbit. The identity fixes 15 matchings, the six 4-cycles fix one each and the remaining 17 permutations fix three each. Thus $(15+6+51)/24=3$. The orbit sizes are **1, 6 and 8**.

## A physical family assignment {#прецеденты-три-поколения}

<a id="thm-gen-4-1"></a>
<a id="thm-gen-4-2"></a>
<a id="гипотеза-секторной-асимметрии"></a>

The octonion associator vanishes on each of the seven Fano lines, including all four lines avoiding $O$. It leaves the physical family assignment underdetermined. A candidate must identify matter fields, preserve their gauge transformations and distinguish their responses. Assigning labels by the measured mass ordering spends that information as input. Manogue and Dray studied a different assignment based on quaternionic subalgebras through one chosen unit. [Their construction](https://arxiv.org/abs/hep-th/9807044) · [Mixing as a test](./ckm-matrix#11-вкус-с-часов).

## Unconditional modular uniqueness of $M = 7$ and odd-flux top-quark selection {#modular-uniqueness-m7}

On a magnetized torus orbifold $T^2/\mathbb{Z}_2$ with flux $M$, independent constructive theorems (`ToEFrontierV6.lean`–`ToEFrontierV9.lean`, `verify_deep_frontier_v6.py`–`verify_deep_frontier_v9.py`) single out the Fano flux $M = 7$ and its $N_g = 3$ odd chiral zero modes uniquely:

1. **Unconditional modular uniqueness (`psl2_order_168_unique_fano7`) [T]:** Proving $M \le J_2(M)$ constructively for all $M \ge 2$ shows that $\lvert\mathrm{PSL}(2,\mathbb{Z}_M)\rvert = 168 = \lvert\mathrm{Aut}(\mathrm{PG}(2,2))\rvert$ holds **if and only if $M = 7$** (for every $M \ge 19$, $\lvert\mathrm{PSL}(2,\mathbb{Z}_M)\rvert > 168$). Because $7 \equiv 3 \pmod 4$, the 7D Landau space splits as $H_7 = H_4^+ \oplus H_3^-$ where the 4 even modes carry a **projective** $\mathbb{Z}_2$-obstructed representation ($\lVert S_{\mathrm{even}}^2 + I_4\rVert = 2.4\times 10^{-15}$) while the **$N_g = 3$ odd generations** carry an exact **linear** irreducible 3D Weil representation of $\mathrm{PSL}(2,7)$ ($\lVert S_{\mathrm{odd}}^2 - I_3\rVert = 3.3\times 10^{-15}$, $\lvert\langle S_{\mathrm{odd}}, T_{\mathrm{odd}}\rangle\rvert = 168$, irrep norm $1.0000000000$) [T].
2. **Odd $M = 7$ vs. even $M = 8$ selection law (`fano7_vs_m8_odd_generation_selection`, `fano7_vs_m8_active_fixed_point_counts`) [T]:** Both $M = 7$ and $M = 8$ yield $N_g = 3$ odd chiral generations, yet every even flux ($M = 6, 8$) vanishes at **all four** orbifold fixed points (`[0, 0, 0, 0]`): at $M = 8$, the Yukawa kernel has zero spectral gap ($0.0000$) and non-hierarchical top spectrum $[0.605, 0.658, 1.0]$ (Schur concentration $0.4084$) [✗]. By contrast, odd Fano $M = 7$ concentrates $100\%$ of odd-mode density at the single fixed point $z_{\mathrm{top}} = (\frac{1}{2}, \frac{1}{2})$ ($\sum \lvert\chi_i\rvert^2 = 7.00 = M$), uniquely yielding $\lambda_{\max}(K^{\mathrm{Yuk}}) = 7/2$ and exact rank-1 third-generation dominance $[0, 0, 1]$ (Schur concentration $1.0000$) [T].
3. **$G_2$-instanton compactification on $T^7/\mathbb{Z}_2^3$ and remaining open moduli (`F-35A,B`) [T] / [C] / [P]:** While untwisted Abelian flux on Joyce's $T^7/\mathbb{Z}_2^3$ vanishes identically ($b_2^{\mathrm{untw}} = 0/21$) [✗], lifting $\gamma$ by $\mathrm{Spin}(10)$ charge conjugation $\hat{\gamma}(H) = -H$ makes the paired flux $F \otimes H = ((7/A_{12})e^{12} - (1/A_{34})e^{34})\otimes H$ solve all 7 $G_2$-instanton equations uniquely at the BPS Kähler minimum $A_{12}/A_{34} = 7$ ($E_{\mathrm{YM}}(7) = 7$), yielding exact $N_g = 3\times 1 = 3$ generations $H_3^-(7) \otimes \bar{H}_1^+(-1)$ [C]. Stabilizing the complex structure $\tau = 0.25 + 1.5i$ and Joyce blow-up moduli remains open [P] ([Fano Selection Rules](../gauge-symmetry/fano-selection-rules#psl2-7-fano-bridge)).
