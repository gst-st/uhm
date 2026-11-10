---
sidebar_position: 2
title: "Quark mixing and tests of flavour models"
description: "Independent mass inputs, basis misalignment and a texture test"
---

# Quark mixing and tests of flavour models

## Relative flavour bases {#6-ckm-из-несовпадения-юкавских-текстур}

<a id="ckm-non-circularity"></a>
<a id="thm-10-1-t-265"></a>

Let $U_{uL},U_{dL}$ diagonalize $Y_uY_u^\dagger,Y_dY_d^\dagger$ in the same weak basis. With three left-handed quark doublets and the usual charged current, $V=U_{uL}^\dagger U_{dL}$ is unitary. Specifying the six singular values does not determine this product. At fixed masses one may vary a left unitary rotation of $Y_d$ relative to $Y_u$. A spectral model that takes the Yukawa matrices as input can compute $V$, but testing flavour dynamics requires an independent origin for those matrices. [Example of a finite spectral model](https://arxiv.org/abs/hep-th/0610241).

## A texture tested on another observable {#derivation-vus}

A zero in a mass matrix is a basis-dependent statement. A texture hypothesis must fix the form of both matrices in a common basis. In the Hermitian six-zero Fritzsch ansatz, $V_{cb}$ is a sum of three complex terms with two adjustable relative phases. For the running masses in the repository test at $M_Z$, $(m_u,m_c,m_t)=(0.00123,0.620,168.26)$ GeV and $(m_d,m_s,m_b)=(0.00267,0.05316,2.839)$ GeV, diagonalization gives their magnitudes $a_i$ as $0.00002491$, $0.13181608$ and $0.05993983$. Opposing the smaller terms to the largest attains the triangle bound $2\max_i a_i-\sum_i a_i=0.07185$. The reference value in this test is $0.04183$. Agreement of $\sqrt{m_d/m_s}$ with a Cabibbo estimate does not repair that failure. [Reproducible mass and mixing checks](https://github.com/gst-st/uhm/blob/main/website/scripts/check_core_numbers.py).

## The seven-tick clock {#11-вкус-с-часов}

<a id="thm-4-2"></a>

The shift has seven distinct complex eigenvalues. Every operator commuting with it is diagonal in its Fourier basis. If both mass operators preserve the individual family modes and have nondegenerate spectra, their relative basis gives a permutation up to phases. Obtaining a physical mixing angle and CP phase requires an interaction that distinguishes the two bases. Fitting a correction to the measured phase uses that measurement as input. [Clock harmonics](./fermion-generations#поколения-t328).
