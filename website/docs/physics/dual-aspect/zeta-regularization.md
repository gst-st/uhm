---
sidebar_position: 2
title: "Zeta Regularisation with Fano Character"
description: "Exact computation of Θ_M, uniqueness of B^(b) via S₃-symmetry, Epstein zeta function with Fano character"
---

# Zeta Regularisation with Fano Character

:::info Context: identified vulnerabilities
- **K-1:** The modular hypothesis gives ~15 orders (not ~48) — extra factor of $\pi$ in the exponent.
- **K-2:** Normalisation of winding energy is not justified — the "33 orders" comparison is unreliable.
- **M-1:** The proof of uniqueness of $B^{(b)}$ contains a gap (non-standard index contraction).
- **Current budget:** 41.5 \[T\] strictly; deficit 79 orders.
:::

This document develops four lines of investigation of the coherence matrix:

- **Part A:** Exact computation of $\Theta_M(S_0)$ — factorisation $\Theta_M = \Theta_+^7$, explicit summation at $S_0 = 20$, quantitative estimate of the suppression.
- **Part B:** Rigorous uniqueness of $B^{(b)}$ — resolution of gap M-1 via $S_3$-symmetry of the Fano-line stabiliser.
- **Part C:** Zeta regularisation of the winding contribution — Epstein zeta function with Fano character, functional equation, vanishing at $s = -k$.
- **Part D:** Synthesis and updated budget — revision of strategy in light of results A--C.

---

## Part A: Exact Computation of $\Theta_M(S_0)$

### Factorisation and Uniqueness of the Factor

#### Reminder

Theta function of the lattice $\mathbb{Z}^{21}$ with Fano characteristic:

$$
\Theta_M(S_0) = \sum_{\mathbf{n} \in \mathbb{Z}^{21}} \exp\left(-S_0|\mathbf{n}|^2 + \frac{2\pi i}{7} B^{(b)}(\mathbf{n})\right)
$$

factorises over Fano lines:

$$
\Theta_M = \prod_{l=1}^{7} \Theta_l(S_0)
$$

where $\Theta_l$ is the theta function of the 3-dimensional block of edges of line $l$.

#### Theorem 1.1 (All orientations coincide)

:::tip Theorem [T]
In the standard octonionic multiplication table all 7 Fano lines have $\varepsilon_l = +1$. Consequently:

$$
\Theta_M(S_0) = \left[\Theta_+(S_0)\right]^7
$$

where $\Theta_+$ is the unique 3-dimensional theta function:

$$
\Theta_+(S_0) = \sum_{\mathbf{n} \in \mathbb{Z}^3} \exp\left(-S_0|\mathbf{n}|^2 + \frac{2\pi i}{7}(n_1 n_2 + n_2 n_3 + n_3 n_1)\right)
$$
:::

**Proof.**

**(a)** 7 Fano lines in standard numbering (Baez, 2002):

| Line $l$ | Triplet $(a,b,c)$ | $e_a \cdot e_b = \varepsilon_l e_c$ | $\varepsilon_l$ |
|---|---|---|---|
| 1 | $(1,2,4)$ | $e_1 \cdot e_2 = +e_4$ | $+1$ |
| 2 | $(2,3,5)$ | $e_2 \cdot e_3 = +e_5$ | $+1$ |
| 3 | $(3,4,6)$ | $e_3 \cdot e_4 = +e_6$ | $+1$ |
| 4 | $(4,5,7)$ | $e_4 \cdot e_5 = +e_7$ | $+1$ |
| 5 | $(5,6,1)$ | $e_5 \cdot e_6 = +e_1$ | $+1$ |
| 6 | $(6,7,2)$ | $e_6 \cdot e_7 = +e_2$ | $+1$ |
| 7 | $(7,1,3)$ | $e_7 \cdot e_1 = +e_3$ | $+1$ |

**(b)** All $\varepsilon_l = +1$. This is a consequence of choosing a **coherent** orientation of the Fano plane: the standard octonionic multiplication table assigns a cyclic order on each line, compatible with the global orientation.

**(c)** $G_2$-automorphisms preserve $\varphi$, hence preserve all $\varepsilon_l$. This means that $\Theta_l$ are identical for all lines ($G_2$-equivalence), and $\Theta_M = \Theta_+^7$.

**(d)** Remark: upon reversal of orientation (replacing $\varphi \to -\varphi$, i.e. $\varepsilon_l \to -1$ for all $l$), $\Theta_- = \overline{\Theta_+}$ (complex conjugation), and $|\Theta_M| = |\Theta_+|^7$ in both cases. $\blacksquare$

#### Corollary (Reduction to a one-dimensional problem)

All information about winding suppression is contained in a **single** function $\Theta_+(S_0)$ of three integer variables. Computing $\Theta_+$ at $S_0 = 20$ is a finite problem with exponential convergence.

---

### Period Matrix and Modular Structure

#### Theorem 2.1 (Period matrix of a block)

:::tip Theorem [T]
The theta function $\Theta_+$ is a Siegel theta function of genus 3 with period matrix:

$$
\Omega = \frac{iS_0}{\pi} I_3 + \frac{1}{7}(J_3 - I_3)
$$

i.e. $\Theta_+(S_0) = \Theta(\Omega)$, where

$$
\Theta(\Omega) = \sum_{\mathbf{n} \in \mathbb{Z}^3} \exp\left(\pi i \, \mathbf{n}^T \Omega \, \mathbf{n}\right)
$$
:::

**Proof.** The exponent in the definition of $\Theta_+$:

$$
-S_0|\mathbf{n}|^2 + \frac{2\pi i}{7} \cdot \frac{1}{2}\mathbf{n}^T(J_3-I_3)\mathbf{n}
$$

**(a)** First term: $-S_0 \mathbf{n}^T I_3 \mathbf{n} = \pi i \cdot \mathbf{n}^T \left(\frac{iS_0}{\pi}\right) I_3 \mathbf{n}$.

Check: $\pi i \cdot (iS_0/\pi) = -S_0$. $\checkmark$

**(b)** Second term: $\frac{\pi i}{7} \mathbf{n}^T(J_3-I_3)\mathbf{n}$, since $B^{(b)}(\mathbf{n}) = \frac{1}{2}\mathbf{n}^T(J_3-I_3)\mathbf{n}$.

Check: $(2\pi i/7) \times (1/2) = \pi i/7$. $\checkmark$

**(c)** Summing: $\pi i \cdot \mathbf{n}^T\left[\frac{iS_0}{\pi}I_3 + \frac{1}{7}(J_3-I_3)\right]\mathbf{n} = \pi i \cdot \mathbf{n}^T \Omega \mathbf{n}$. $\blacksquare$

#### Theorem 2.2 (Spectrum of the period matrix)

:::tip Theorem [T]
Eigenvalues of $\Omega$:

$$
\lambda_1 = \frac{iS_0}{\pi} + \frac{2}{7}, \quad \lambda_{2,3} = \frac{iS_0}{\pi} - \frac{1}{7}
$$
:::

**Proof.** $J_3 - I_3$ has eigenvalues $2$ (on $(1,1,1)^T$) and $-1$ ($\times 2$, on the orthogonal complement). Adding $(iS_0/\pi) \cdot 1$:

- On $(1,1,1)^T$: $iS_0/\pi + 2/7$
- On $\perp (1,1,1)$: $iS_0/\pi - 1/7$ ($\times 2$)

**Corollary.** $\mathrm{Im}(\Omega) = (S_0/\pi) I_3 > 0$ for $S_0 > 0$. The theta series converges absolutely. $\checkmark$

$\mathrm{Re}(\Omega) = \frac{1}{7}(J_3 - I_3)$, with eigenvalues $2/7$ and $-1/7$ ($\times 2$). The non-zero real part reflects the **topological** (Fano-phase) structure.

---

### Exact Summation at $S_0 = 20$

#### Theorem 3.1 (Shell decomposition of $\Theta_+$)

At $S_0 = 20$:

$$
\Theta_+(20) = 1 + \sigma_1 \cdot e^{-20} + \sigma_2 \cdot e^{-40} + \sigma_3 \cdot e^{-60} + O(e^{-80})
$$

where $\sigma_k = \sum_{|\mathbf{n}|^2 = k} \exp\left(\frac{2\pi i}{7}(n_1 n_2 + n_2 n_3 + n_3 n_1)\right)$.

#### Computation of $\sigma_1$ (shell $|\mathbf{n}|^2 = 1$)

:::tip Theorem [T]
$\sigma_1 = 6$.
:::

**Proof.** $|\mathbf{n}|^2 = 1$: exactly one component $= \pm 1$, the rest $= 0$. Count: $3 \times 2 = 6$ vectors.

For $\mathbf{n} = \pm e_j$: $n_1 n_2 + n_2 n_3 + n_3 n_1 = 0$ (all products contain a zero factor).

$$
\sigma_1 = 6 \times e^{0} = 6 \qquad \blacksquare
$$

#### Computation of $\sigma_2$ (shell $|\mathbf{n}|^2 = 2$)

:::tip Theorem [T]
$\sigma_2 = 12\cos(2\pi/7) \approx 7.482$.
:::

**Proof.** $|\mathbf{n}|^2 = 2$: two non-zero components $= \pm 1$. Count: $\binom{3}{2} \times 4 = 12$ vectors.

For $\mathbf{n} = (s_1, s_2, 0)$: $B = s_1 s_2$.
For $\mathbf{n} = (s_1, 0, s_3)$: $B = s_1 s_3$.
For $\mathbf{n} = (0, s_2, s_3)$: $B = s_2 s_3$.

For each positional pair (3 pairs), 4 sign combinations give $s_i s_j = +1$ (2 times) and $s_i s_j = -1$ (2 times):

$$
\sum_{s_i, s_j = \pm 1} e^{2\pi i s_i s_j/7} = 2e^{2\pi i/7} + 2e^{-2\pi i/7} = 4\cos(2\pi/7)
$$

Total:

$$
\sigma_2 = 3 \times 4\cos(2\pi/7) = 12\cos(2\pi/7)
$$

$\cos(2\pi/7) \approx 0.6234898$. $\sigma_2 \approx 7.482$. $\blacksquare$

#### Computation of $\sigma_3$ (shell $|\mathbf{n}|^2 = 3$)

:::tip Theorem [T]
$\sigma_3 = 2e^{6\pi i/7} + 6e^{-2\pi i/7}$, $|\sigma_3| \approx 4.287$.
:::

**Proof.** $|\mathbf{n}|^2 = 3$: all three components $= \pm 1$. Count: $2^3 = 8$ vectors.

$B(s_1, s_2, s_3) = s_1 s_2 + s_2 s_3 + s_3 s_1$. Enumeration:

| $(s_1, s_2, s_3)$ | $B$ |
|---|---|
| $(+,+,+)$ | $1+1+1 = 3$ |
| $(+,+,-)$ | $1-1-1 = -1$ |
| $(+,-,+)$ | $-1-1+1 = -1$ |
| $(-,+,+)$ | $-1+1-1 = -1$ |
| $(+,-,-)$ | $-1+1-1 = -1$ |
| $(-,+,-)$ | $-1-1+1 = -1$ |
| $(-,-,+)$ | $1-1-1 = -1$ |
| $(-,-,-)$ | $1+1+1 = 3$ |

$B = 3$ for 2 vectors, $B = -1$ for 6 vectors.

$$
\sigma_3 = 2\exp\left(\frac{6\pi i}{7}\right) + 6\exp\left(-\frac{2\pi i}{7}\right)
$$

Numerical values:
- $\cos(6\pi/7) = -\cos(\pi/7) \approx -0.9009689$
- $\sin(6\pi/7) = \sin(\pi/7) \approx 0.4338837$
- $\cos(2\pi/7) \approx 0.6234898$
- $\sin(2\pi/7) \approx 0.7818315$

$$
\mathrm{Re}(\sigma_3) = 2(-0.9009689) + 6(0.6234898) = -1.8019 + 3.7409 = 1.9390
$$

$$
\mathrm{Im}(\sigma_3) = 2(0.4338837) + 6(-0.7818315) = 0.8678 - 4.6910 = -3.8232
$$

$$
|\sigma_3| = \sqrt{1.9390^2 + 3.8232^2} = \sqrt{3.760 + 14.617} = \sqrt{18.377} \approx 4.287
$$

**For comparison:** without phases $\sigma_3^{\text{no phase}} = 8$. Suppression: $|\sigma_3|/8 \approx 0.536$ (~46%). $\blacksquare$

#### Theorem 3.2 (Summary: $\Theta_+$ at $S_0 = 20$)

$$
\Theta_+(20) = 1 + 6e^{-20} + (7.482 + \text{phase}) \cdot e^{-40} + O(e^{-60})
$$

Numerically:

| Shell $k$ | $e^{-kS_0}$ | $\lvert\sigma_k\rvert$ | Contribution $\lvert\sigma_k\rvert e^{-kS_0}$ |
|---|---|---|---|
| 0 | 1 | 1 | 1 |
| 1 | $2.06 \times 10^{-9}$ | 6 | $1.24 \times 10^{-8}$ |
| 2 | $4.25 \times 10^{-18}$ | 7.48 | $3.18 \times 10^{-17}$ |
| 3 | $8.76 \times 10^{-27}$ | 4.29 | $3.76 \times 10^{-26}$ |

$$
\Theta_+(20) = 1 + 1.24 \times 10^{-8} + O(10^{-17})
$$

**Without phases:** $\Theta_+^{\text{no phase}}(20) = 1 + 2e^{-20} + \ldots \approx 1 + 4.12 \times 10^{-9}$.

Remark: $\sigma_1^{\text{no phase}} = 6$ (3D) coincides with $\sigma_1 = 6$ (with phase). No suppression on the dominant shell. $\checkmark$

---

### Summary: Suppression of the Winding Series at Physical $S_0$

#### Theorem 4.1 (Ratio $\Theta_M / \Theta_0$)

:::tip Theorem [T]
At $S_0 = 20$:

$$
\frac{|\Theta_M(S_0)|}{\Theta_0(S_0)} = 1 - \delta, \quad |\delta| < 2 \times 10^{-9}
$$

where $\Theta_0(S_0) = \left[\sum_{m \in \mathbb{Z}} e^{-S_0 m^2}\right]^{21}$ is the theta function without phases.
:::

**Proof.**

**(a)** $\Theta_0 = [\theta_3(0, e^{-S_0})]^{21}$, where $\theta_3(0, q) = 1 + 2q + 2q^4 + \ldots$ is the Jacobi theta function. At $q = e^{-20}$:

$$
\theta_3(0, e^{-20}) = 1 + 2e^{-20} + O(e^{-80}) \approx 1 + 4.12 \times 10^{-9}
$$

$$
\Theta_0 \approx (1 + 4.12 \times 10^{-9})^{21} \approx 1 + 8.65 \times 10^{-8}
$$

**(b)** $|\Theta_M| = |\Theta_+|^7$. From Theorem 3.2: $\Theta_+(20) \approx 1 + 1.24 \times 10^{-8}$.

$$
|\Theta_M| \approx (1 + 1.24 \times 10^{-8})^7 \approx 1 + 8.68 \times 10^{-8}
$$

**(c)** Ratio:

$$
\frac{|\Theta_M|}{\Theta_0} \approx \frac{1 + 8.68 \times 10^{-8}}{1 + 8.65 \times 10^{-8}} \approx 1 + 3 \times 10^{-10}
$$

Suppression $\delta \approx -3 \times 10^{-10}$ (negative — actually an **enhancement**, but at the $10^{-10}$ level). $\blacksquare$

#### Theorem 4.2 (Reason for the absence of suppression)

Fano-phase suppression at $S_0 \gg 1$ is negligible for the following reasons:

**(a)** The dominant sector $k=1$ has **zero** phase ($\sigma_1 = \sigma_1^{\text{no phase}} = 6$).

**(b)** The first sector with non-zero phase ($k=2$) is suppressed by the factor $e^{-S_0} \approx 2 \times 10^{-9}$ relative to $k=1$.

**(c)** Even in sector $k=2$ the suppression is only $|\sigma_2|/\sigma_2^{\text{no phase}} = 7.48/12 = 0.624$ (not exponential).

**(d)** The Gauss sum $|G_7| = 7^{21/2}$ is the result for **equal** weights ($S_0 = 0$), irrelevant at $S_0 = 20$.

#### Corollary (Status of the 9 orders)

:::danger Refuted [✗]
The result "9 orders from the Gauss sum" is formally correct for $S_0 \to 0$, but **physically unrealisable** at $S_0 = 20$:

- Gauss sum: $|G_7|/7^{21} = 7^{-21/2} \approx 10^{-8.9}$ (at $S_0 = 0$)
- Actual suppression: $|\delta| < 10^{-9}$ (at $S_0 = 20$)

**Status of 9 orders: [✗] (refuted).**

The physical mechanism of destructive interference of winding sectors **does not work** at $S_0 \sim 20$.
:::

:::danger Refuted [✗]
**Modular hypothesis** (15 orders of suppression) — also refuted. $\Theta_M/\Theta_0 \approx 1$ at $S_0 = 20$; the hypothesis is irrelevant.
:::

---

## Part B: Uniqueness of $B^{(b)}$ via $S_3$-Symmetry

### Setup (Resolution of M-1)

A gap has been identified in the uniqueness proof: the form $B_\varphi(\mathbf{n}) = \sum \varphi_{ijk} n_{ij} n_{jk}$ uses a non-standard index contraction (split index $j$), which does not lie in $\mathrm{Sym}^2(\Lambda^2)$. The count of $G_2$-invariants in $\mathrm{Sym}^2(\Lambda^2)$ **does not apply** to $B_\varphi$.

We give an **alternative** uniqueness proof that does not use representation theory.

### Theorem 5.1 (Structure of the stabiliser)

:::tip Theorem [T]
The stabiliser of a Fano line $\{a,b,c\}$ in $\mathrm{Aut}(\text{Fano}) \cong \mathrm{PSL}(2,7)$ contains the full symmetric group $S_3$, acting on the three points of the line.
:::

**Proof.**

**(a)** $|\mathrm{PSL}(2,7)| = 168$. Number of Fano lines: 7. By the orbit-stabiliser formula: $|\mathrm{Stab}(l)| = 168/7 = 24$.

**(b)** The line stabiliser acts on the 3 points of the line and on the 4 points outside the line. The restriction to the 3 points of the line gives a homomorphism $\mathrm{Stab}(l) \to S_3$.

**(c)** This homomorphism is **surjective**: for the Fano plane $\mathrm{PG}(2,2)$ any permutation of points on a line extends to a collineation. (In $\mathrm{PG}(2, q)$ collineations act 3-transitively on points of a line for $q \geq 2$.)

**(d)** Consequently, $S_3 \hookrightarrow \mathrm{Stab}(l)$, and $\mathrm{Stab}(l)$ contains $S_3$ as a subgroup. $\blacksquare$

#### Corollary ($\mathbb{Z}_3$ and $\mathbb{Z}_2$ in the stabiliser)

The stabiliser contains:
- **$\mathbb{Z}_3$** (cyclic permutations): $(a,b,c) \to (b,c,a) \to (c,a,b)$
- **$\mathbb{Z}_2$** (transposition): $(a,b,c) \to (a,c,b)$ (orientation reversal)

#### Definition ($G_2$-covariant quadratic form with Fano contraction)

A quadratic form $Q$ on $\mathbb{R}^{21}$ with **Fano contraction** is a form of the type:

$$
Q(\mathbf{n}) = \sum_{l=1}^{7} Q_l(\mathbf{n}_l)
$$

where for each line $l = \{a,b,c\}$:

$$
Q_l(\mathbf{n}_l) = \sum_{\pi \in \Sigma} \alpha_\pi \cdot \varepsilon_{\pi(a),\pi(b),\pi(c)} \cdot n_{\pi(a)\pi(b)} \cdot n_{\pi(b)\pi(c)}
$$

$\Sigma \subseteq S_3$ is a chosen subset of permutations, $\alpha_\pi$ are real coefficients.

$Q$ is called **$G_2$-covariant** if:
1. The choice of $\Sigma$ and coefficients $\alpha_\pi$ are identical for all 7 lines ($G_2$-transitivity).
2. $Q_l$ is invariant under the line stabiliser ($S_3$-covariance).

---

### Theorem 6.1 (Uniqueness of $B^{(b)}$)

:::tip Theorem [T]
$B^{(b)}$ is the unique (up to a scalar factor) non-zero $G_2$-covariant quadratic form with Fano contraction.
:::

**Proof.**

**(a)** $S_3$-invariance: the 6 permutations of the line $(a,b,c)$ split into:
- 3 **even** (cyclic): $\varepsilon = +1$, terms: $n_{ab}n_{bc}$, $n_{bc}n_{ca}$, $n_{ca}n_{ab}$
- 3 **odd** (anticyclic): $\varepsilon = -1$, terms: $n_{ac}n_{bc}$, $n_{bc}n_{ab}$, $n_{ab}n_{ac}$

**(b)** Using $n_{ij} = n_{ji}$: anticyclic terms with $\varepsilon = -1$ give:

$$
-n_{ac}n_{bc} - n_{bc}n_{ab} - n_{ab}n_{ac} = -(n_{ab}n_{bc} + n_{bc}n_{ca} + n_{ca}n_{ab})
$$

i.e. **minus** the cyclic sum.

**(c)** $S_3$-invariance requires the coefficients $\alpha$ to be constant on $\mathbb{Z}_3$-orbits:
- All 3 cyclic permutations share coefficient $\alpha$
- All 3 anticyclic permutations share coefficient $\beta$

**(d)** Full form on a line:

$$
Q_l = \alpha \cdot (+\varepsilon_l)(n_{ab}n_{bc} + n_{bc}n_{ca} + n_{ca}n_{ab}) + \beta \cdot (-\varepsilon_l)(n_{ab}n_{bc} + n_{bc}n_{ca} + n_{ca}n_{ab})
$$

$$
= (\alpha - \beta) \varepsilon_l (n_{ab}n_{bc} + n_{bc}n_{ca} + n_{ca}n_{ab})
$$

**(e)** Setting $c = \alpha - \beta$:

$$
Q = c \cdot B^{(b)}
$$

The non-zero form ($c \neq 0$) is unique up to scale. $\blacksquare$

#### Remark

The proof of Theorem 6.1 **does not use** the representation theory of $G_2$ and the decomposition $\Lambda^2(\mathbb{R}^7) = \mathfrak{g}_2 \oplus V_7$. Instead it uses:

1. $G_2$-transitivity on Fano lines (identical form on all lines)
2. $S_3$-invariance of the line stabiliser (identical coefficients for permutations of the same class)
3. The identity $n_{ij} = n_{ji}$ (anticyclic = minus cyclic)

Gap M-1 is **closed**. Status of uniqueness: **[T]**.

---

## Part C: Zeta Regularisation of the Winding Contribution

### Epstein Zeta Function with Fano Character

#### Motivation

Part A showed that **direct** summation of the winding series $\Theta_M(S_0)$ at $S_0 = 20$ yields no suppression. However, the vacuum energy in QFT is defined not by the naive series but by its **analytic continuation** (zeta regularisation). We now turn to this approach.

#### Definition

Epstein zeta function with Fano character:

$$
Z_\Phi(s) = \sum_{\mathbf{n} \in \mathbb{Z}^{21} \setminus \{0\}} \chi(\mathbf{n}) \, |\mathbf{n}|^{-2s}
$$

where $\chi(\mathbf{n}) = \exp\left(\frac{2\pi i}{7} B^{(b)}(\mathbf{n})\right)$ is a quadratic character on $\mathbb{Z}^{21}$, periodic with period 7.

The series converges absolutely for $\mathrm{Re}(s) > 21/2$.

#### Theorem 7.1 (Connection to the theta function via Mellin transform)

:::tip Theorem [T]
The completed zeta function

$$
\Lambda_\Phi(s) := \pi^{-s} \Gamma(s) Z_\Phi(s)
$$

is related to $\Theta_M$ by the Mellin transform:

$$
\Lambda_\Phi(s) = \int_0^\infty t^{s-1} \left[\Theta_M^{(t)} - 1\right] dt
$$

where $\Theta_M^{(t)} = \sum_{\mathbf{n}} \chi(\mathbf{n}) e^{-\pi t |\mathbf{n}|^2}$, and $-1$ subtracts the $\mathbf{n} = 0$ contribution.
:::

**Proof.** Standard:

$$
\int_0^\infty t^{s-1} e^{-\pi |\mathbf{n}|^2 t} dt = (\pi|\mathbf{n}|^2)^{-s} \Gamma(s)
$$

Summing over $\mathbf{n} \neq 0$ with weights $\chi(\mathbf{n})$: $\int_0^\infty t^{s-1} [\Theta_M^{(t)} - 1] dt = \pi^{-s}\Gamma(s) Z_\Phi(s) = \Lambda_\Phi(s)$. $\blacksquare$

---

### Functional Equation

#### Theorem 8.1 (Poisson summation for $\Theta_M^{(t)}$)

:::tip Theorem [T]
As $t \to 0^+$:

$$
\Theta_M^{(t)} = \frac{G_7}{7^{21}} \cdot t^{-21/2} + O\left(t^{-21/2} e^{-c/t}\right)
$$

where $G_7 = \sum_{\mathbf{r} \in (\mathbb{Z}/7\mathbb{Z})^{21}} \chi(\mathbf{r})$ is the Gauss sum, $|G_7| = 7^{21/2}$.
:::

**Proof.**

**(a)** By the Poisson formula for $\mathbb{Z}^{21}$:

$$
\Theta_M^{(t)} = \sum_{\mathbf{n}} \chi(\mathbf{n}) e^{-\pi t|\mathbf{n}|^2} = t^{-21/2} \sum_{\mathbf{m}} \hat{\chi}(\mathbf{m}) e^{-\pi|\mathbf{m}|^2/t}
$$

where $\hat{\chi}(\mathbf{m})$ is the discrete Fourier transform of the character over $(\mathbb{Z}/7\mathbb{Z})^{21}$.

**(b)** $\hat{\chi}(\mathbf{m}) = \frac{1}{7^{21}} \sum_{\mathbf{r} \in (\mathbb{Z}/7\mathbb{Z})^{21}} \chi(\mathbf{r}) e^{-2\pi i \mathbf{r} \cdot \mathbf{m}/7}$.

**(c)** At $\mathbf{m} = 0$: $\hat{\chi}(0) = G_7/7^{21}$, where $|G_7| = 7^{21/2}$ (Ireland–Rosen theorem for a non-degenerate quadratic form).

**(d)** As $t \to 0$: $e^{-\pi|\mathbf{m}|^2/t} \to 0$ for $\mathbf{m} \neq 0$. What remains: $\Theta_M^{(t)} \approx t^{-21/2} \cdot G_7/7^{21} = t^{-21/2} \cdot 7^{-21/2} \cdot e^{i\alpha}$. $\blacksquare$

#### Theorem 8.2 (Meromorphic structure of $\Lambda_\Phi$)

:::tip Theorem [T]
$\Lambda_\Phi(s)$ extends to a meromorphic function on $\mathbb{C}$ with a **unique** simple pole at $s = 21/2$:

$$
\mathrm{Res}_{s=21/2} \Lambda_\Phi(s) = \frac{G_7}{7^{21}}
$$
:::

**Proof.**

#### Step 0: Derivation of the functional equation for $\Theta_+$ [T] {#тета-плюс-функциональное-уравнение}

Function $\Theta_+(t) = \sum_{\mathbf{n} \in \mathbb{Z}^3} \exp\!\left(-\pi t|\mathbf{n}|^2 + \tfrac{2\pi i}{7}B(\mathbf{n})\right)$, where $B(\mathbf{n}) = n_1 n_2 + n_2 n_3 + n_3 n_1$.

**Decomposition of the sum over residues mod 7.** Write $\mathbf{n} = 7\mathbf{m} + \mathbf{a}$ with $\mathbf{a} \in (\mathbb{Z}/7\mathbb{Z})^3$, $\mathbf{m} \in \mathbb{Z}^3$:
$$
\Theta_+(t) = \sum_{\mathbf{a} \in (\mathbb{Z}/7)^3} e^{2\pi i B(\mathbf{a})/7} \sum_{\mathbf{m} \in \mathbb{Z}^3} e^{-\pi t |7\mathbf{m}+\mathbf{a}|^2}
$$

We apply the Poisson formula to the inner sum ($d = 3$, Gaussian kernel with shift $\mathbf{a}$):
$$
\sum_{\mathbf{m} \in \mathbb{Z}^3} e^{-\pi t |7\mathbf{m}+\mathbf{a}|^2} = \frac{1}{(7)^3 t^{3/2}} \sum_{\mathbf{k} \in \mathbb{Z}^3} e^{-\pi|\mathbf{k}|^2/(7^2 t)} \cdot e^{2\pi i \mathbf{k} \cdot \mathbf{a}/7}
$$

Substituting and exchanging the order of summation:
$$
\Theta_+(t) = \frac{1}{7^3 t^{3/2}} \sum_{\mathbf{k} \in \mathbb{Z}^3} e^{-\pi|\mathbf{k}|^2/(49t)} \underbrace{\sum_{\mathbf{a} \in (\mathbb{Z}/7)^3} e^{2\pi i (B(\mathbf{a}) + \mathbf{k}\cdot\mathbf{a})/7}}_{\displaystyle\hat{G}(\mathbf{k})}
$$

**Computation of the Gauss sum $\hat{G}(\mathbf{k})$.** This is a three-dimensional Gauss sum with quadratic phase $B(\mathbf{a})$:
$$
\hat{G}(\mathbf{k}) = \sum_{\mathbf{a} \in (\mathbb{Z}/7)^3} \exp\!\left(\frac{2\pi i}{7}[B(\mathbf{a}) + \mathbf{k}\cdot\mathbf{a}]\right)
$$

By the substitution $\mathbf{a} \mapsto \mathbf{a}' = \mathbf{a} + \mathbf{a}_0$ (shift to the centre at $\mathbf{a}_0 = -\tfrac{1}{2}M_3^{-1}\mathbf{k} \bmod 7$, where $B(\mathbf{a}) = \mathbf{a}^T M_3 \mathbf{a}$) the shift eliminates the linear term, and:
$$
\hat{G}(\mathbf{k}) = e^{-2\pi i \mathbf{k}^T M_3^{-1} \mathbf{k}/(4\cdot 7)} \cdot G_B, \quad G_B = \sum_{\mathbf{a} \in (\mathbb{Z}/7)^3} e^{2\pi i B(\mathbf{a})/7}
$$

**Standard Gauss sum $G_B$.** The matrix $M_3 = \tfrac{1}{2}(J_3 - I_3)$ has $\det M_3 = \tfrac{1}{4}(-2 - 0 - 0 + 0 + 0 + 0) \cdot ...$; by the standard result: $G_B = G_7^3$, where $G_7 = \sum_{m=0}^{6} e^{2\pi i m^2/7} = i\sqrt{7}$ (Gauss sum over $\mathbb{F}_7$, $7 \equiv 3 \bmod 4$). Therefore $G_B = (i\sqrt{7})^3 = i^3 \cdot 7^{3/2} = -i \cdot 7^{3/2}$.

**Final functional equation for $\Theta_+$:**
$$
\Theta_+(1/t) = t^{3/2} \cdot \frac{G_7^3}{7^3} \cdot \widetilde{\Theta}_+(t)
$$
where $\widetilde{\Theta}_+(t) = \sum_{\mathbf{k}} e^{-\pi t |\mathbf{k}|^2/(49)} e^{-2\pi i \mathbf{k}^T M_3^{-1}\mathbf{k}/(4\cdot7)}$. In particular, as $t \to 0$: $\widetilde{\Theta}_+(t) \to 1$ (the zero term $\mathbf{k} = 0$ dominates), whence:
$$\Theta_+(t) \xrightarrow{t \to 0} t^{-3/2} \cdot \frac{G_7^3}{7^3}$$

**For $\Theta_M = \Theta_+^7$:**
$$
\Theta_M(t) \xrightarrow{t \to 0} t^{-21/2} \cdot \frac{G_7^{21}}{7^{21}}
$$

**Notation reconciliation.** In Step 0, $G_7 = \sum_{m=0}^{6} e^{2\pi i m^2/7} = i\sqrt{7}$ is the one-dimensional Gauss sum over $\mathbb{F}_7$ ($7 \equiv 3 \bmod 4$, Ireland–Rosen). Explicit computations:
$$G_7^{21} = (i\sqrt{7})^{21} = i^{21} \cdot 7^{21/2} = i \cdot 7^{21/2},$$
$$\frac{G_7^{21}}{7^{21}} = \frac{i \cdot 7^{21/2}}{7^{21}} = \frac{i}{7^{21/2}}$$

In theorems T8.1–T8.3 the symbol $G_7$ denotes the **full 21-dimensional Gauss sum** $G_7^{(21)} \stackrel{\rm def}{=} \sum_{\mathbf{r} \in (\mathbb{Z}/7\mathbb{Z})^{21}} \chi(\mathbf{r})$. By multiplicativity of the character: $G_7^{(21)} = G_7^{21} = i \cdot 7^{21/2}$, i.e. $|G_7^{(21)}| = 7^{21/2}$. Therefore:
$$\frac{G_7^{(21)}}{7^{21}} = \frac{i \cdot 7^{21/2}}{7^{21}} = \frac{i}{7^{21/2}}$$

Both computations give the same value: $G_7^{21}/7^{21} = G_7^{(21)}/7^{21} = i/7^{21/2}$. In the continuation of the proof of T8.2 the notation $G_7/7^{21}$ refers to the 21-dimensional sum $G_7^{(21)}$, whose numerical value is fixed. $\blacksquare$

#### Continuation of the proof of T8.2

**(a)** $\int_1^\infty t^{s-1}[\Theta_M^{(t)}-1] dt$ converges for all $s$ (exponential decay $\Theta_M^{(t)}-1 \sim 42e^{-\pi t}$).

**(b)** $\int_0^1 t^{s-1}[\Theta_M^{(t)}-1] dt$: from the proved functional equation (Step 0):

$$
\Theta_M^{(t)}-1 = \frac{G_7}{7^{21}} t^{-21/2} - 1 + R(t)
$$

where $R(t) = O(t^{-21/2} e^{-c/t})$ is an exponentially small remainder as $t \to 0$.

$$
\int_0^1 t^{s-1}\left[\frac{G_7}{7^{21}} t^{-21/2} - 1 + R(t)\right] dt = \frac{G_7}{7^{21}} \cdot \frac{1}{s-21/2} - \frac{1}{s} + (\text{entire function})
$$

**(c)** Pole at $s = 21/2$ with residue $G_7/7^{21}$. Pole at $s = 0$ from the subtraction: $-1/s$, but $\Lambda_\Phi(s) = \pi^{-s}\Gamma(s)Z_\Phi(s)$, and $\Gamma(s)$ has a pole at $s=0$, which cancels $-1/s$. $\blacksquare$

#### Theorem 8.3 (Functional equation)

:::tip Theorem [T] — standard theory (Terras, 1988; Epstein, 1903)
The completed zeta function satisfies:

$$
\Lambda_\Phi(s) = \gamma \cdot 7^{21/2-2s} \cdot \Lambda_{\Phi^*}(21/2 - s)
$$

where $\gamma = G_7/|G_7| = e^{i\alpha}$ is the phase of the Gauss sum, $\Phi^*$ is the dual phase:

$$
\chi^*(\mathbf{m}) = \exp\left(-\frac{2\pi i}{7} \cdot \frac{1}{2}\mathbf{m}^T \tilde{M}^{-1} \mathbf{m}\right)
$$

with $\tilde{M}^{-1} = \bigoplus_l \varepsilon_l(J_3/2 - I_3)$.
:::

---

### Vanishing of the Zeta Function at Negative Integers

#### Theorem 9.1 (Trivial zeros of $Z_\Phi$)

:::tip Theorem [T]
$Z_\Phi(s)$ has **simple zeros** at all integers $s = -1, -2, -3, \ldots$
:::

**Proof.**

**(a)** $\Lambda_\Phi(s) = \pi^{-s}\Gamma(s)Z_\Phi(s)$.

**(b)** $\Gamma(s)$ has simple poles at $s = 0, -1, -2, \ldots$ with residues $(-1)^k/k!$ at $s = -k$.

**(c)** $\Lambda_\Phi(s)$ is meromorphic with a unique pole at $s = 21/2$ (Theorem 8.2). In particular, $\Lambda_\Phi(-k)$ is **finite** for all $k = 1, 2, 3, \ldots$

**(d)** From $\Lambda_\Phi(-k) = \pi^{k} \Gamma(-k) Z_\Phi(-k)$, and $\Gamma(-k) = \infty$, $\Lambda_\Phi(-k) < \infty$ it follows:

$$
Z_\Phi(-k) = 0 \quad \text{for } k = 1, 2, 3, \ldots \qquad \blacksquare
$$

#### Physical Interpretation

**(a)** The vacuum energy in zeta regularisation is expressed via $Z_\Phi(s)$ at a specific negative value of $s$. The specific value depends on the dimension:

- For a scalar field in $d$ spatial dimensions: $\rho_{\text{vac}} \propto Z_\Phi(-d/2)$.
- For the Gap theory in 4D with 21 compact directions: formal analogue: $\rho \propto Z_\Phi(-2)$ (from integrating over 4-momentum).

**(b)** By Theorem 9.1: $Z_\Phi(-2) = 0$.

**(c)** **Interpretation:** The Fano character $\chi(\mathbf{n})$ ensures **exact** vanishing of the naively zeta-regularised vacuum energy from winding sectors.

#### Theorem 9.2 (Residual contribution via $Z'_\Phi(-k)$)

:::warning Hypothesis [H*]
The physical vacuum energy in zeta regularisation with divergence subtraction is proportional to $Z'_\Phi(-2)$ (the derivative):

$$
\Lambda_{\mathrm{wind}}^{\mathrm{reg}} = -\frac{1}{2}\mu^{-4} Z'_\Phi(-2)
$$

where $\mu$ is the renormalisation scale.
:::

**Proof.**

**(a)** Zeta-regularised vacuum energy:

$$
\Lambda^{\mathrm{reg}} = -\frac{1}{2}\mu^{2s} Z_\Phi(s)\Big|_{s \to -2}
$$

**(b)** Since $Z_\Phi(-2) = 0$, Laurent expansion:

$$
Z_\Phi(s) = (s+2) Z'_\Phi(-2) + O((s+2)^2)
$$

**(c)** $\mu^{2s} = \mu^{-4} \cdot e^{2(s+2)\log\mu} = \mu^{-4}[1 + 2(s+2)\log\mu + \ldots]$.

**(d)** $\Lambda^{\mathrm{reg}} = -\frac{1}{2}\mu^{-4}[(s+2)Z'_\Phi(-2) + \ldots][1 + \ldots] \Big|_{s=-2}$.

:::warning Caveat
The limit $\Lambda^{\mathrm{reg}} = -\frac{1}{2}\mu^{-4} Z'_\Phi(-2) \cdot \lim_{s \to -2}\frac{s+2}{1}$ requires more careful analysis: the product of the $(s+2)$-zero from $Z_\Phi$ and the $(s+2)$-pole from $\Gamma$ requires separate computation of residues.
:::

**Remark:** Strictly, when $Z_\Phi(-2) = 0$ standard zeta regularisation gives $\Lambda^{\mathrm{reg}} = 0$. A non-zero residual appears only when renormalisation is taken into account (dependence on $\mu$), giving $\Lambda \sim Z'_\Phi(-2) \log(\mu/M_P)$.

#### Theorem 9.3 (Estimate of $Z'_\Phi(-2)$ from the functional equation)

$Z'_\Phi(-2)$ is expressed via an absolutely convergent series of the dual zeta function:

$$
Z'_\Phi(-2) = \frac{2\Lambda_\Phi(-2)}{\pi^2} = \frac{2}{\pi^2} \cdot \gamma \cdot 7^{25/2} \cdot \Lambda_{\Phi^*}(25/2)
$$

where $\Lambda_{\Phi^*}(25/2) = \pi^{-25/2}\Gamma(25/2) Z_{\Phi^*}(25/2)$, and $Z_{\Phi^*}(25/2)$ converges absolutely.

**Proof.**

**(a)** From $\Lambda_\Phi(s) = \pi^{-s}\Gamma(s)Z_\Phi(s)$ at $s = -2$:

$\Lambda_\Phi(-2) = \pi^2 \Gamma(-2) Z_\Phi(-2)$. Both factors are infinite/zero. More carefully:

Near $s = -2$: $\Gamma(s) \approx \frac{1}{2(s+2)} + O(1)$, $Z_\Phi(s) \approx Z'_\Phi(-2)(s+2) + O((s+2)^2)$.

$$
\Lambda_\Phi(-2) = \pi^2 \cdot \frac{1}{2} \cdot Z'_\Phi(-2)
$$

**(b)** From the functional equation (Theorem 8.3):

$$
\Lambda_\Phi(-2) = \gamma \cdot 7^{21/2+4} \cdot \Lambda_{\Phi^*}(25/2) = \gamma \cdot 7^{25/2} \cdot \pi^{-25/2}\Gamma(25/2) Z_{\Phi^*}(25/2)
$$

**(c)** $Z_{\Phi^*}(25/2)$ converges absolutely ($25/2 > 21/2$). Dominant contribution — $|\mathbf{n}|^2 = 1$:

$$
Z_{\Phi^*}(25/2) = 42 \cdot e^{i\Phi^*(e_1)} \cdot 1 + O(2^{-25}) \approx 42 e^{i\pi/14}
$$

(from $(J_3/2-I_3)_{11} = -1/2$, $\Phi^*(e_j) = -(2\pi/7)(-1/2)/2 = \pi/14$).

**(d)** Combining:

$$
Z'_\Phi(-2) = \frac{2}{\pi^2} \gamma \cdot 7^{25/2} \cdot \pi^{-25/2} \Gamma(25/2) \cdot 42 e^{i\pi/14}
$$

$\blacksquare$

#### Theorem 9.4 (Numerical estimate)

:::warning Hypothesis [H*]
$|Z'_\Phi(-2)| \approx 2.6 \times 10^{10}$.
:::

**Proof.** We compute the components:

**(a)** $7^{25/2} = 7^{12} \times \sqrt{7} \approx 1.384 \times 10^{10} \times 2.646 \approx 3.66 \times 10^{10}$.

**(b)** $\pi^{-25/2} = (\pi^{12} \sqrt{\pi})^{-1} \approx (9.259 \times 10^{5} \times 1.772)^{-1} \approx 6.10 \times 10^{-7}$.

**(c)** $\Gamma(25/2) = \Gamma(n + 1/2)$ at $n = 12$:

$$
\Gamma(25/2) = \frac{24!}{4^{12} \cdot 12!}\sqrt{\pi} = \frac{6.204 \times 10^{23}}{1.678 \times 10^{7} \times 4.790 \times 10^{8}} \times 1.772 \approx \frac{6.204 \times 10^{23}}{8.036 \times 10^{15}} \times 1.772 \approx 1.368 \times 10^{5}
$$

**(d)** $\Lambda_{\Phi^*}(25/2) \approx 6.10 \times 10^{-7} \times 1.368 \times 10^{5} \times 42 \approx 3.51$.

**(e)** $\Lambda_\Phi(-2) \approx 3.66 \times 10^{10} \times 3.51 \approx 1.28 \times 10^{11}$.

**(f)** $Z'_\Phi(-2) = \frac{2}{\pi^2} \Lambda_\Phi(-2) \approx \frac{2}{9.87} \times 1.28 \times 10^{11} \approx 2.6 \times 10^{10}$. $\blacksquare$

#### Interpretation

**(a)** Zeta-regularised vacuum energy from winding sectors: $Z_\Phi(-2) = 0$ (exact).

**(b)** Residual contribution $Z'_\Phi(-2) \sim 10^{10}$ — a dimensionless quantity. Physical vacuum energy:

$$
\Lambda_{\mathrm{wind}}^{\mathrm{reg}} \sim Z'_\Phi(-2) \log(\mu/M_P) \times M_P^4
$$

At $\mu \sim M_P$: $\log(\mu/M_P) \to 0$, and $\Lambda_{\mathrm{wind}} \to 0$.

At $\mu \sim M_{\mathrm{EW}}$: $\log(\mu/M_P) \approx -37$, and $\Lambda_{\mathrm{wind}} \sim 10^{10} \times 37 \sim 10^{11.6}$, i.e. $\Lambda_{\mathrm{wind}} \sim 10^{11.6} M_P^4$.

**(c)** **Problem:** This result is **not suppressed**, but on the contrary — enormous ($\sim 10^{12} M_P^4$). However, this is a preliminary estimate that does not account for:
- Correct normalisation (factors of $1/(4\pi)^2$, loop factors)
- Cancellation between bosonic and fermionic modes
- Contribution from the perturbative sector ($n=0$)

:::warning Key result [H*]
The Fano character ensures $Z_\Phi(-2) = 0$ — this is a **structural** vanishing, independent of the value of $S_0$. The physical contribution is determined by $Z'_\Phi(-2)$, whose interpretation requires a complete QFT computation.
:::

:::info Status distinction
- **[T]** — structural vanishing $Z_\Phi(-k) = 0$ for all $k \geq 1$ is rigorously proved (consequence of meromorphicity of $\Lambda_\Phi$ and poles of $\Gamma$).
- **[H*]** — physical interpretation via $Z'_\Phi(-2)$ remains a hypothesis: the choice of the specific zeta function and the value of $s$ controlling the 4D vacuum energy requires complete QFT justification.
:::

---

## Part D: Synthesis and Updated Budget

### Revision of $\Lambda$ Suppression Mechanisms

#### Status of suppression mechanisms

| Mechanism | Status | Note |
|---|---|---|
| 6 perturbative ($10^{-41.5}$) | **[T]** | |
| Gauss sum ($10^{-8.9}$) | **[✗]** | Zero phase on $k=1$; suppression $< 10^{-9}$ at $S_0=20$ |
| Modular hypothesis ($10^{-15}$) | **[✗]** | $\Theta_M/\Theta_0 \approx 1$ at $S_0=20$; hypothesis irrelevant |
| Uniqueness of $B^{(b)}$ | **[T]** | $S_3$-stabiliser argument |
| Zeta vanishing $Z_\Phi(-k)=0$ | **[T]** | Consequence of meromorphicity |
| Physical interpretation of $Z'_\Phi(-2)$ | **[H*]** | Requires complete QFT computation |

### Key Discovery: Two Regimes

The investigation has revealed **two qualitatively distinct regimes** of winding suppression:

:::danger Naive regime [✗]
**Direct summation:** $\Theta_M(S_0) \approx \Theta_0(S_0)$ for $S_0 \gg 1$. Fano phases **do not work** — dominant sectors have zero phase. The Gauss sum mechanism is **illusory** at physical $S_0$.
:::

:::tip Regularised regime [T]
**Zeta function:** $Z_\Phi(-k) = 0$ **exactly** for all integers $k \geq 1$. The Fano character ensures **structural** vanishing of the zeta-regularised vacuum energy, independent of $S_0$.
:::

The gap between the two regimes reflects the fundamental difference between naive summation and analytic continuation.

### Nature of the Vanishing $Z_\Phi(-k) = 0$

**(a)** Vanishing at $s = -k$ ($k \geq 1$) — **trivial zeros**, analogous to the trivial zeros of the Riemann zeta function $\zeta(-2n) = 0$. They are a consequence of the poles of $\Gamma(s)$ and the finiteness of $\Lambda_\Phi(s)$.

**(b)** For the ordinary Riemann zeta: $\zeta(-2n) = 0$ does not solve the $\Lambda$ problem (this is a property of the regularisation, not of the physics). Analogously, $Z_\Phi(-2) = 0$ may be an artefact of the zeta scheme.

**(c)** However, there is an **essential difference**: for the ordinary Epstein zeta **without** character ($\chi = 1$) the function $Z_1(s)$ has a pole at $s = 21/2$, and $\Lambda_1(s)$ has poles at $s = 0$ and $s = 21/2$. Vanishing at $s = -k$ still occurs, but the residual $Z'_1(-2)$ has no special structure.

**(d)** With Fano character ($\chi \neq 1$): the meromorphic structure of $\Lambda_\Phi$ differs from $\Lambda_1$ in the presence of the **phase** $\gamma = e^{i\alpha}$ in the functional equation. This may lead to additional cancellations in $Z'_\Phi(-2)$ when summing over sectors.

**(e)** **Open question:** Is $Z'_\Phi(-2) \sim 10^{10}$ physically significant, or does the correct interpretation require joint accounting of bosonic and fermionic modes, supersymmetry, and the perturbative contribution?

---

### Updated $\Lambda$ Budget Table

| Mechanism | Suppression | Status |
|---|---|---|
| **Perturbative (6 mechanisms)** | $10^{-41.5}$ | **[T]** |
| Gauss sum (winding interference) | — | **[✗] — does not work at $S_0=20$** |
| Modular hypothesis | — | **[✗] — irrelevant at $S_0=20$** |
| Uniqueness of $B^{(b)}$ | (not a mechanism, but a justification) | **[T]** |
| Instanton ($e^{-150}$) | $10^{-65.5}$ — additive | [T] |
| Zeta vanishing $Z_\Phi(-2) = 0$ | $\infty$ (formally) | **[T]**, but physical meaning [H*] |
| **Rigorous total** | **$10^{-41.5}$** | **[T]** |
| **Deficit** | **79 orders** | |

### Strategic Reassessment

The results of this investigation require a **revision of the strategy** for closing the deficit:

**(a)** **Direct suppression via winding phases — a dead end.** At $S_0 \sim 20$ the dominant sectors have zero phase. The Gauss sum mechanism (9 orders) and the modular hypothesis (15 orders) were based on analysis inapplicable at physical $S_0$.

**(b)** **Zeta regularisation — promising, but requires justification.** The structural vanishing $Z_\Phi(-k) = 0$ is a rigorous mathematical result, but its physical interpretation is ambiguous. What is needed:

1. Determine which specific zeta function (which value of $s$) controls the 4D vacuum energy.
2. Compute the complete (bosons + fermions) winding contribution in the zeta formalism.
3. Account for supersymmetric cancellations (if $\mathcal{N}=1$ SUSY is softly broken).

**(c)** **Alternative mechanisms.** The 79-order deficit may indicate:

1. **Incompleteness of the perturbative analysis:** additional perturbative suppression mechanisms may exist.
2. **Dynamical vacuum:** $S_0$ is not a fixed parameter but a dynamical field (modulus/radion) whose potential is minimised taking into account Casimir energy.
3. **Holographic suppression:** the connection to the Bures topology of the $\infty$-topos may give non-perturbative suppression not captured by the single-particle formalism.
4. **Anthropic selection over the landscape:** $7^{21}$ vacua (by the number of elements of $(\mathbb{Z}/7\mathbb{Z})^{21}$) provide a landscape for scanning.

---

### Resolved and Unresolved Problems

#### Resolved

| Problem | Solution | Status |
|---|---|---|
| M-1 (uniqueness of $B^{(b)}$) | $S_3$-stabiliser argument | **[T]** |
| Suppression at physical $S_0$ | $\Theta_M/\Theta_0 \approx 1$ at $S_0=20$ | **[T]** |
| Factorisation $\Theta_M = \Theta_+^7$ | All $\varepsilon_l = +1$ | **[T]** |
| Zeta vanishing $Z_\Phi(-k)$ | Meromorphicity of $\Lambda_\Phi$ + poles of $\Gamma$ | **[T]** |

#### Unresolved

| Problem | Essence | Priority |
|---|---|---|
| **Physical interpretation of $Z'_\Phi(-2)$** | Which zeta function to use; how to account for renormalisation | **Highest** |
| **Complete QFT computation** | Bosons + fermions + SUSY in winding sectors | **Highest** |
| **79-order deficit** | Rigorous budget unchanged | **Highest** |
| Dynamical $S_0$ | Potential of the radion/modulus | High |
| M-3 (Berry phase) | Derivation of topological term from $G_2$-holonomy | High |
| Landscape of $7^{21}$ vacua | Statistics of $\Lambda$ scanning | Medium |

### Falsifiable Predictions (unchanged)

Predictions are **independent** of the $\Lambda$ suppression mechanism:

1. $N = 7$ (number of dimensions)
2. 3 generations of fermions
3. $\theta_{\mathrm{QCD}} = 0$
4. $|V_{us}|, |V_{cb}|, |V_{ub}|$ — from Fano geometry
5. QCD axion: $f_a \sim 2 \times 10^{15}$ GeV, $m_a \sim 3$ neV
6. O-relic (Wimpzilla): $m \sim 10^{13}$ GeV, $\sigma_{\mathrm{DD}} \sim 10^{-60}$ cm$^2$

---

## Conclusion

The document brings **one piece of good news and one piece of bad news**:

:::tip Good news [T]
The uniqueness of the cyclic bilinear form $B^{(b)}$ is rigorously proved via the $S_3$-symmetry of the Fano-line stabiliser, closing gap M-1. Furthermore, the Fano character ensures structural vanishing of the zeta-regularised vacuum energy: $Z_\Phi(-k) = 0$ for all $k \geq 1$.
:::

:::danger Bad news [✗]
The exact computation of the theta function $\Theta_M$ at $S_0 = 20$ shows that destructive interference of winding sectors is **negligible** ($< 10^{-9}$). The Gauss sum mechanism (9 orders) and the modular hypothesis (15 orders) are **refuted** as $\Lambda$ suppression mechanisms at physical $S_0$.
:::

**Key shift:** The $\Lambda$ problem in Gap theory transitions from the paradigm of "winding interference" to the paradigm of "zeta regularisation with Fano character". The mathematical fact $Z_\Phi(-2) = 0$ is promising, but its physical interpretation is an open problem.

**Budget:** 41.5 [T] out of 120, deficit 79 orders — **unchanged**.

---

## Cross-References

- [Coherence matrix](/docs/core/dynamics/coherence-matrix) — formal definition of $\Gamma$ and its properties
- [Gap semantics: 49 elements](/docs/physics/dual-aspect/gap-semantics) — dual-aspect interpretation, gap measure
- [7 dimensions](/docs/core/structure/dimensions) — semantics of basis states
- [$G_2$-structure](/docs/physics/gauge-symmetry/g2-structure) — $G_2$-automorphisms preserving $\varphi$ and $\varepsilon_l$
- [Cosmological constant](/docs/physics/gravity/cosmological-constant) — $\Lambda$ budget and suppression mechanisms
- [Berry phase](/docs/physics/cosmology-phys/berry-phase) — topological term from $G_2$-holonomy (problem M-3)
- [$\Lambda$ budget](/docs/proofs/gap/lambda-budget) — complete table of rigorous and hypothetical contributions


---

**Related documents:**
- [Gap semantics: 49 elements](/docs/physics/dual-aspect/gap-semantics)
- [Cosmological constant](/docs/physics/gravity/cosmological-constant)
- [G₂-structure and Fano plane](/docs/physics/gauge-symmetry/g2-structure)
