---
sidebar_position: 2
title: Seven dimensions
description: What the seven coordinates encode, what selects their number, and what experiments could identify them.
---

## Reading the seven coordinates

The numerical holon model describes a state by a positive Hermitian matrix of unit trace on $\mathbb C^7$. It chooses seven labelled directions for discussing different aspects of a system. A column name tells the reader which role the model assigns; it does not establish that a physical system has that many independent degrees of freedom or that a person has a particular experience.

| Dimension | Symbol | Intended role |
|---|---|---|
| [Articulation](./dimension-a) | $A$ | Discriminate |
| [Structure](./dimension-s) | $S$ | Hold |
| [Dynamics](./dimension-d) | $D$ | Change |
| [Logic](./dimension-l) | $L$ | Coordinate |
| [Interiority](./dimension-e) | $E$ | Experience |
| [Ground](./dimension-o) | $O$ | Nourish + Measure time |
| [Unity](./dimension-u) | $U$ | Integrate |

The diagonal is a probability distribution for the chosen pointer measurement. For each pair the off-diagonal entry records two real coordinates, constrained by positivity; in particular $|\gamma_{ij}|^2\le\gamma_{ii}\gamma_{jj}$. The 21 complex coherences give 42 real entries; six independent diagonal probabilities bring the full-dimensional state space to 48 real parameters. Setting a diagonal entry to zero forces the entire corresponding row and column to vanish. Such a matrix remains a valid density state; eligibility as a holon with a designated interiority axis is an additional predicate. [Coherence matrix](../dynamics/coherence-matrix)

## Which hypotheses select seven?

A perfect one-error binary code with more than two codewords has at least seven positions; fifteen also works. Independent interference and shared-decoder requirements supply an upper bound on the address. Under all three requirements the address has exactly seven positions. Identifying it with the whole physical state register requires an additional representation preserving accessible preparations and readouts. [Operational derivation and witnesses](../foundations/operational-processes#address)

## What incidence fixes {#комбинаторная-единственность}

The nonzero vectors of $\mathbb F_2^3$ form the seven points of the Fano plane. An ordered triple off a line is a basis: its images specify one invertible map. There are $7\cdot6\cdot4=168$ choices, giving a regular action on such triples. If the point $O$ and the unordered pair $\{E,U\}$ are supplied with $O,E,U$ noncollinear, incidence fixes $A=E+U$ and $D=O+A$. Two labelings remain, interchanging $E,U$ and the corresponding remaining pair. Choosing between them takes an extra mark. This result constrains labels on an incidence structure; it gives no physical meaning to “interiority” by itself.

## Conditional categorical interpretation {#категориальная-семантика}

A chosen differentially cohesive setting has modal operations. Assigning an operation to each semantic label is a separate interpretation. The topology of density matrices alone does not select that setting or the seven labelled rays. A readout on a proposed physical axis must be defined and calibrated independently of its label. [Premises](../../reference/premises)

## Octonionic realization {#октонионная-интерпретация}

The imaginary octonions have seven real dimensions and multiplication admits the automorphism group $G_2$. Choosing a unit imaginary direction reduces the symmetry to a stabilizer isomorphic to $SU(3)$. This supplies a concrete algebraic realization. Inferring an octonionic product from physical operations would require identifying the product and its multiplicative norm. A positive size alone does not exclude zero divisors. [Algebraic model](../../physics/gauge-symmetry/g2-structure) · [An operational test of joint state descriptions](../../networks/reference-comparison)
