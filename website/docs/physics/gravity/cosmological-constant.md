---
sidebar_position: 3
title: "Cosmological Constant"
slug: /physics/gravity/cosmological-constant
description: "Vacuum energy as a volume-response coefficient, its units, its observability and conditional spectral estimates."
---

# The cosmological constant

The geometric cosmological constant $\Lambda$ is the coefficient of $g_{\mu\nu}$ in the Einstein equation. It has units $\mathrm{m}^{-2}$. A constant vacuum energy density $\epsilon_{\rm vac}$ has units $\mathrm{J\,m^{-3}}$. In general relativity its contribution to that coefficient is

$$
\Lambda_{\rm vac}=\frac{8\pi G_N}{c^4}\,\epsilon_{\rm vac}.
$$

This conversion assumes a metric, the Einstein–Hilbert coupling and a vacuum stress tensor proportional to the metric. An internal register by itself supplies none of those measurements. [Gravitational action](/docs/physics/gravity/einstein-equations)

## Why differences of energy cannot fix this coefficient {#стратегия-замыкания}

Consider two models whose energies at fixed volume differ by a constant. For every pair of states the energy difference is the same in both models. The minimizing states are the same, and the common factor cancels from every normalized Gibbs probability. No sequence of these measurements distinguishes the models, even though they assign different absolute energies to the vacuum. Vanishing cohomology in positive degrees leaves degree-zero constants available. [Identifiability proof](/docs/proofs/gap/lambda-budget#постановка)

## A measurement that can separate two coefficients {#требования-полного-решения}

Suppose a model assigns the action $S_b[h]=S_0[h]+bV[h]$ to an accessible history $h$, where $V$ is a measured additive volume. To test $b$, specify how the instrument reads an action contrast. Independently calibrate the volume, the instrument response and the other action terms. For two histories define $\Delta S_b=S_b[h_2]-S_b[h_1]$ and use the same ordering for $\Delta S_0$ and $\Delta V$. Then

$$
\Delta S_b-\Delta S_0=b\,\Delta V .
$$

If $\Delta V\ne0$ and the instrument resolves this contrast, the ratio determines $b$ in units of action per volume. At equal volume every candidate $b$ yields the same contrast. With a phase-only measurement the phase ambiguity must also be resolved. A third volume contrast provides a held-out test of the fitted coefficient. Identifying $b$ with a gravitational vacuum contribution additionally requires specifying which physical volume is integrated and fixing the action normalization. No such differential volume measurement is supplied by the network results. [Volume-response criterion](/docs/proofs/gap/lambda-budget#структурное-замыкание-лямбда)

## Positive matrix readouts {#теорема-лямбда-положительна}

For a trace-one Hermitian register $\rho$ of dimension seven, $P=\operatorname{Tr}\rho^2$ satisfies

$$
P-\frac17=\|\rho-I/7\|_F^2 .
$$

**T-71.** Choose a readout $\epsilon_{\rm model}=C(P-1/7)$ with a positive $C$ in density units. This readout vanishes at $I/7$ and is positive elsewhere. The positivity statement follows exactly from the identity. The choice of zero, scale, state and coupling of the readout to gravity are physical hypotheses.

### Clock-sector weights {#теорема-лямбда-o-доминирование}

The weighted phase statistic $\mathcal G_O=\sum_{i\ne O}|\gamma_{Oi}|^2\mathrm{Gap}(O,i)^2$ is nonnegative. Other sectors can carry weight independently of these six entries. A physical assertion of $O$-sector dominance therefore needs both a sector profile and an energy functional whose weights are fixed independently of the cosmological observation.

## What spectral calculations determine {#теорема-спектральная-лямбда}

On a supplied four-dimensional Riemannian product geometry, the heat-kernel expansion has a volume term. In natural units its density can involve $\Lambda_{\rm cut}^4\operatorname{Tr}1$, $\Lambda_{\rm cut}^2\operatorname{Tr}D_{\rm int}^2$ and $\operatorname{Tr}D_{\rm int}^4$. Each has energy dimension four. The cutoff moments, the operator and the finite subtraction prescription enter the result. For instance, imposing $\|D_{\rm int}\|\le c_0\varepsilon^3M_P$ on a Hermitian seven-dimensional matrix gives the bound $\operatorname{Tr}D_{\rm int}^4\le7c_0^4\varepsilon^{12}M_P^4$. Bounding this one trace does not set the renormalized volume coefficient. [Spectral action](/docs/physics/gravity/quantum-gravity#canonical-f)

### A finite winding example {#7-сумма-гаусса-для-фано-фаз}

For seven independent, identically oriented blocks and a positive Gaussian cost, the specified theta sum factorizes as $\Theta_M=\Theta_+^7$. At $S_0=20$ the relative reduction in magnitude from the unweighted sum is about $1.34\times10^{-16}$ including zero winding and $1.55\times10^{-9}$ when zero is excluded from both sums. Thus both ratios remain close to one. These are dimensionless properties of the chosen weights. A zero of an analytically continued sum likewise determines a value of that function. Coupling it to physical volume still requires a field model and normalization. [Lattice sum and zeta zeros](/docs/physics/dual-aspect/zeta-regularization)

## Time dependence of a chosen fluid {#теорема-лямбда-дрейф}

**T-254.** If an effective density is specified as $\epsilon_{\rm DE}(a)=C\mathcal G_O(a)^2>0$ with constant $C$, and the fluid is separately conserved, then $d\ln\epsilon_{\rm DE}/d\ln a=-3(1+w)$. Differentiation gives

$$
1+w=-\frac23\,\frac{d\ln\mathcal G_O}{d\ln a}.
$$

A strictly constant density has $w=-1$ under these hypotheses. Interpreting a changing density as an effective fluid requires a map from the register's time coordinate to $a$. It is distinct from a constant geometric $\Lambda$.

### Observable histories {#теорема-трихотомия-ветвей}

**T-255.** A chosen response model can generate particular shapes for $w(a)$. In general a linear response can contain several real or oscillatory modes. A small list of shapes needs its own dynamical restriction and comparison on independent observations.

### Inferring a cosmological state {#теорема-стадия-вселенной}

**T-266.** A history of expansion does not specify a seven-register state or a relaxation rate without an observation map. To infer either, give distinguishable predictions for competing state histories, calibrate on independent records and test the remaining predictions. The sign and magnitude of the physical vacuum contribution remain open.
