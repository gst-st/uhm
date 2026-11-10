---
sidebar_position: 2
title: "Zeta Regularisation with Fano Character"
description: "A periodic lattice weight, its theta sum at S₀ = 20, and the scope of its zeta zeros."
---

# Zeta Regularisation with Fano Character

The model takes 21 independent integer labels, a Euclidean cost $S_0|n|^2$, a phase of period seven and a common coefficient for seven oriented Fano lines. It gives two calculable quantities: the relative change of a weighted Gaussian sum and the zeros of its analytically continued zeta function. A physical vacuum-energy calculation requires a spectrum and a normalization for a specified field. [Spectral assumptions](/docs/physics/gravity/cosmological-constant)

## The seven three-dimensional blocks

Each unordered pair of Fano points belongs to one line. Assign one integer to each pair. Choose the same cyclic form $B(x,y,z)=xy+yz+zx$ on each of the seven disjoint blocks of three pair labels. With these conventions

$$
\Theta_+(S_0)=\sum_{u\in\mathbb Z^3}e^{-S_0|u|^2}e^{2\pi i B(u)/7},
\qquad \Theta_M(S_0)=\Theta_+(S_0)^7 .
$$

Absolute convergence for $S_0>0$ justifies factorisation. Reversing the sign of one block conjugates its factor. Its period matrix is $\Omega=iS_0 I_3/\pi+(J_3-I_3)/7$, where $J_3$ has all entries one. The real part has eigenvalues $2/7,-1/7,-1/7$ and the imaginary part is positive definite.

### Which symmetry fixes the polynomial?

The Fano plane over $\mathbb F_2$ has collineation group $GL(3,2)$. A line corresponds to a two-dimensional subspace. Its invertible linear maps permute the three nonzero vectors as $S_3$ and extend to the whole space by fixing a complementary vector. Thus the three edge labels of a line can be permuted. In the span of $xy,yz,zx$ the invariant subspace is exactly the multiples of $B$. If squares are allowed, $x^2+y^2+z^2$ is another invariant. Cross-line terms were excluded at the outset. The continuous group $G_2$ preserves octonion multiplication and in general mixes the seven chosen axes. The uniqueness result concerns the specified polynomial space and its finite incidence symmetry. [Octonion structure](/docs/physics/gauge-symmetry/g2-structure)

## Direct summation at the chosen value $S_0=20$

Set $q=e^{-S_0}$, $\zeta_7=e^{2\pi i/7}$. The shells $|u|^2=1,2,3$ contain 6, 12 and 8 vectors respectively. Their weighted sums are $6$, $12\cos(2\pi/7)$ and $2\zeta_7^3+6\zeta_7^{-1}$. In particular the six nearest sites have phase zero. With $\Theta_0$ the unweighted 21-dimensional sum,

$$
\begin{aligned}
\Theta_+ &= 1+6q+12\cos(2\pi/7)q^2+O(q^3),\\
\Theta_0 &= (1+6q+12q^2+O(q^3))^7,\\
1-|\Theta_M|/\Theta_0 &= 84(1-\cos(2\pi/7))q^2+O(q^3).
\end{aligned}
$$

At $S_0=20$ the relative reduction including the zero vector is about $1.34\times10^{-16}$. The triangle inequality bounds the modulus ratio above by one. Excluding the zero vector in both sums gives $1-|\Theta_M-1|/(\Theta_0-1)\simeq1.55\times10^{-9}$. Both ratios are near unity. This refutes the proposed nine- and fifteen-order multiplicative suppressions **at this input value**. A uniform Gauss sum over the residue classes describes a different limit.

## Poisson summation and analytic continuation {#тета-плюс-функциональное-уравнение}

Write $d=21$ and $\chi(n)=e^{2\pi i\sum_\ell B(n_\ell)/7}$. Define $Z_\Phi(s)=\sum_{n\ne0}\chi(n)|n|^{-2s}$ initially for $\Re s>d/2$ and $\Theta(t)=\sum_n\chi(n)e^{-\pi t|n|^2}$. For the normalized finite Fourier transform and the Poisson formula one has

$$
\widehat\chi(m)=7^{-d}\sum_{r\bmod7}\chi(r)e^{2\pi i r\cdot m/7},
\qquad
\Theta(t)=t^{-d/2}\sum_{m\in\mathbb Z^d}
        \widehat\chi(m)e^{-\pi|m|^2/(49t)}.
$$

In one block the form has matrix $(J_3-I_3)/2$ and determinant $1/4$, a nonzero square modulo seven. Diagonalising over $\mathbb F_7$ gives the unnormalized block Gauss sum $(i\sqrt7)^3$. Multiplying the seven blocks gives $\widehat\chi(0)=i\,7^{-21/2}$. Completing the square over $\mathbb F_7$ gives a dual phase $\chi^*(m)=\widehat\chi(m)/\widehat\chi(0)$. The inverse of four in this square completion is a finite-field inverse.

The Mellin integral of $\Theta(t)-1$ equals $\Lambda_\Phi(s)=\pi^{-s}\Gamma(s)Z_\Phi(s)$ in the convergence half-plane. At $t\to\infty$ the integrand before its Mellin weight decays exponentially. At $t\to0$ it equals $\widehat\chi(0)t^{-d/2}-1+O(t^{-d/2}e^{-c/t})$ for some $c>0$. Splitting the integral at one yields

$$
\Lambda_\Phi(s)=\frac{\widehat\chi(0)}{s-d/2}-\frac1s+F(s),
\qquad F\ \text{entire}.
$$

The completed function has **two** simple poles, at $0$ and $21/2$. The gamma factor shows that $Z_\Phi(-k)=0$ for every positive integer $k$. The same reasoning gives zeros for the unweighted lattice. It implies a zero of at least first order. Simplicity at a particular integer would also require $\Lambda_\Phi(-k)\ne0$.

The Poisson identity, with $u=1/(49t)$, gives $\Lambda_\Phi(s)=i\,7^{d/2-2s}\Lambda_{\Phi^*}(d/2-s)$ using the same completion for the dual series. At $s=-2$ the residue of $\Gamma(s)$ is $1/2$, so

$$
Z'_\Phi(-2)=\frac{2}{\pi^2}\Lambda_\Phi(-2)
=\frac{2i}{\pi^2}\,7^{29/2}\Lambda_{\Phi^*}(25/2).
$$

The dual series at $25/2$ converges absolutely. A numerical estimate using its first few shells needs a bound on the remaining tail.

## What would connect this sum to vacuum energy?

A field model has to specify the operator with this spectrum, multiplicities and weights, the dimensional scale and a renormalization condition connecting its finite term to an observable. Evaluating $\mu^{2s}Z_\Phi(s)$ at $s=-2$ gives zero for every fixed positive $\mu$. A derivative can enter through a separately justified determinant or a compensating pole. Which physical field, if any, has the prescribed periodic weight is open. [Vacuum-energy models](/docs/physics/gravity/cosmological-constant) · [Coherence measurements](/docs/physics/dual-aspect/gap-semantics)
