---
sidebar_position: 1
title: "Octonions and the Fano plane"
description: "Multiplication, frame symmetry and the SU(3) stabilizer of a marked unit"
---

# Octonions and the Fano plane

## A multiplication table {#октонионное-умножение-и-g2}

<a id="12-таблица-фано-линий"></a>

In the following convention each cyclic triple $(i,j,k)$ means $e_i e_j=e_k$. Reversing two units changes the sign, and $e_i^2=-1$. Together with the unit element these rules specify multiplication on $\mathbb O$.

$$
(1,2,4),\quad(2,3,5),\quad(3,4,6),\quad(4,5,7),\quad(5,6,1),\quad(6,7,2),\quad(7,1,3).
$$

The seven triples are the lines of the Fano plane. Every two distinct indices occur on one line. The indices on that line together with $1_{\mathbb O}$ span a quaternion subalgebra. The incidence table specifies which component of a product can be nonzero. Its cyclic orientations supply the signs. [Baez, *The Octonions*](https://arxiv.org/abs/math/0105155).

## A marked axis {#прецеденты-g2}

<a id="пространство-не-в-im-o"></a>

The automorphism group of this algebra is the compact group $G_2$. Choosing a unit $u\in\mathrm{Im}\,\mathbb O$ reduces its stabilizer to $SU(3)$. On the real six-plane perpendicular to $u$ in $\mathrm{Im}\,\mathbb O$, left multiplication by $u$ defines a complex structure. After complexification the seven-dimensional representation restricts to $\mathbf1\oplus\mathbf3\oplus\bar{\mathbf3}$. The triplet and antitriplet are complex subspaces. A labelling of three real coordinate axes does not determine either subspace. Interpreting this $SU(3)$ as colour requires an action on matter. [Günaydın and Gürsey](https://doi.org/10.1063/1.1666240).

## What an instrument preserves

An instrument that returns populations of the seven individually labelled axes distinguishes frames that a general $G_2$ rotation mixes. For example, rotating a basis preparation into a superposition changes its population record in the fixed frame. A claim of physical gauge symmetry must specify how preparations, measuring devices and transport between sites transform together. This covariance can be verified for a chosen network and group. [Three-site transport](../../networks/three-node-transport).
