---
sidebar_position: 3
title: "Category Hol"
description: "The category of Holons and DensityMat"
---

# Structured holon processes

A category specifies objects, arrows, identities and associative composition. In UHM this language distinguishes numerical states, processes preserving chosen structure, and sheaves on a state-space site. It does not prove the unique phenomenal interpretation formerly claimed from T-42a [✗]. The [canonical formalism](/docs/proofs/categorical/categorical-formalism#категория-голономов-hol) gives the complete typed construction.

## Category DensityMat

An object is $(\mathcal H,\rho)$ with $\rho=\rho^\dagger\geq0$, $\operatorname{Tr}\rho=1$. An arrow $\Lambda:(\mathcal H,\rho)\to(\mathcal K,\sigma)$ is linear CPTP with $\Lambda(\rho)=\sigma$. Positive **semidefinite** states include pure and other rank-deficient states. CPTP requires positivity after adjoining every ancillary system, not merely positivity on the isolated system.

$$
\Lambda(X)=\sum_aK_aXK_a^\dagger,\qquad\sum_aK_a^\dagger K_a=I.
$$

Kraus operators $B_bK_a$ describe a composite $\Psi\Lambda$; the identity has Kraus operator $I$. This proves the category axioms [T]. Every pair of states has a replacement-channel arrow. On a fixed system of dimension greater than one there is no terminal object, since identity and replacement are distinct endomorphisms. With varying system dimensions the terminal object is $(\mathbb C,1)$, via trace; it selects no seven-dimensional preparation.

## Category Hol

Use structured objects $(\mathcal H,M,V,\rho)$, where $M$ is a declared state self-map, $V$ a declared viable region and $\rho\in V$. Physical autonomy and the phenomenal interpretation are additional validated bridge data, not consequences of $\rho\in V$ or nonzero $E$ occupancy. The [holon requirements](/docs/core/foundations/axiom-septicity) separate these claims.

A structure-preserving arrow satisfies

$$
\Lambda(\rho_A)=\rho_B,\quad\Lambda(V_A)\subseteq V_B,\quad\Lambda M_A=M_B\Lambda.
$$

Identities satisfy these conditions, and their preservation under composition follows by substitution [T]. Thus they define a category with a faithful forgetful functor to $\mathbf{DensityMat}$. Multiple structures on one state mean that this need not be an object-injective subcategory until a structure assignment is fixed. A nonlinear $M$ can enter the intertwining equation as a state map; it is not thereby a CPTP arrow.

## Viability and composition

For the chosen native majority convention $V=\{\rho:P>2/7\}$, $P=\operatorname{Tr}\rho^2$ [D]. It is not a universal consciousness or survival theorem. The viable region is not convex: two distinct coordinate pure states are viable, while averaging all seven gives $I_7/7$, outside it.

For product states $P(\rho_A\otimes\rho_B)=P(\rho_A)P(\rho_B)$ [T]. The composite dimension is $N_AN_B$, so applying a native seven-dimensional cut to it requires a declared aggregation map. Arbitrary CPTP aggregation need not preserve majority; a replacement by $I_7/7$ disproves it. At weak coupling a model-specific preservation theorem needs its stated estimates and aggregation assumptions.

## Interiority assignment and sheaves

If an actual process functor $F$ has been supplied, its restriction along the forgetful functor gives $\mathcal I=F\circ U$ [T at supplied $F$]. Existence and empirical/phenomenal validity of $F$ remain separate bridge problems. Dynamic covariance does not prove uniqueness: see [reversible identification](/docs/proofs/categorical/uniqueness-theorem#теорема-единственности).

The sheaf $\infty$-topos $\operatorname{Sh}_\infty(\operatorname{Open}_B(X_N))$ is constructed from open subsets and covers. It is a different category from $\mathbf{Hol}$ or the process category. Logical support reflection lives in a slice of this topos; numerical self-modelling has the types described in [formalization of φ](/docs/proofs/categorical/formalization-phi).

## Historical section addresses

The corrected scope of statements at these addresses is given above.

<a id="category-axioms"></a>
<a id="category-of-holons"></a>
<a id="chapter-summary"></a>
<a id="concrete-example-objects-and-morphisms-of-hol"></a>
<a id="connection-with-7d-structure"></a>
<a id="connections"></a>
<a id="detailed-explanation"></a>
<a id="diagram-conditions-for-membership-in-hol"></a>
<a id="formal-definition"></a>
<a id="hierarchy-of-categories"></a>
<a id="how-the-categories-are-connected-to-each-other"></a>
<a id="interiority-functor"></a>
<a id="motivation-the-passport-of-a-quantum-system"></a>
<a id="motivation-why-a-subcategory"></a>
<a id="non-monoidality-of-hol_v"></a>
<a id="objects-and-arrows"></a>
<a id="precursor-what-a-category-is"></a>
<a id="subcategory-but-not-full"></a>
<a id="the-substantive-meaning-of-each-condition"></a>
<a id="what-a-cptp-channel-is"></a>
<a id="why-categories-in-uhm"></a>
<a id="why-cptp-is-the-right-choice-of-morphisms"></a>
