---
sidebar_position: 6
slug: /physics/gauge-symmetry/rg-flow
title: "Scale dependence of a model"
description: "A sign check for a proposed flow and the data needed for physical matching"
---

# Scale dependence of a model

## Defining a flow {#постановка}

A Wilsonian model specifies its fields, kinetic terms, interactions and regulator. Eliminating a momentum shell generates an effective action. Extracting a few running couplings from it requires a declared projection onto operators. The 21 unordered edges and seven lines of a Fano plane count possible indices. A loop coefficient also depends on the propagator, vertex normalization, dimension and contractions of those indices.

## An exact sign check {#rg-подавление}

Consider a scalar truncation whose equation on a scale interval is $d\lambda/d\log\mu=-\Delta\lambda$ with fixed $\Delta>0$. The solution for a nonzero initial coupling is

$$
\frac{\lambda(\mu)}{\lambda(\mu_0)}
=\left(\frac{\mu}{\mu_0}\right)^{-\Delta}.
$$

Taking $\Delta=5/42$ and $\mu/\mu_0=10^{-61}$ gives a factor $10^{305/42}$, about $10^{7.26}$. The magnitude grows towards the infrared under the stated equation. Whether a scalar truncation describes a measured coupling requires matching its running and boundary value to independent observables.

## Comparing two scales {#стандартная-модель}

For a positive constant rescaling $\alpha=c\lambda$, the beta functions obey $\beta_\alpha=c\beta_\lambda$. A positive quadratic beta function in four dimensions cannot reproduce the negative one-loop beta function of asymptotically free QCD by this rescaling. A test must specify gauge and matter dynamics and compare the coupling at a scale withheld from calibration. A different scale comparison is already defined for transport times on networks. Its observables are the measured times of multiple probes. [Network scale tests](../../geometry/network-scales).
