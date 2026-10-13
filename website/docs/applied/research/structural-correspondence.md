---
sidebar_position: 7.1
title: "Correspondence by structural role"
slug: /applied/research/structural-correspondence
description: "Executable comparison of symbolic systems: roles, transformations, Fano incidence, phase cycles and predictive sufficiency"
---

# Correspondence by structural role

The [21 coherences](/docs/core/dynamics/coherence-matrix) have named roles in UHM. A correspondence with another system should preserve those roles through its relations and operations. Matching the number of symbols is only the first constraint. This chapter supplies a comparison contract and exact finite examples; human interpretation and predictive validation have their own obligations.

## 1. A shared signature {#контракт}

Specify a source structure $S$ and a target $H$, each with typed states, named relations, observations and partial actions. The target may contain several holons. An alignment supplies a type map, relation/action correspondence and a computable state map $E:S\to H$. For each selected relation $R$ and action $a$, require

$$
R_S(s_1,\ldots,s_k)\Longrightarrow R_H(E(s_1),\ldots,E(s_k)),
$$
$$
q_H(E(s))=q_S(s),\qquad
s\in\operatorname{dom}(a_S)\Longleftrightarrow E(s)\in\operatorname{dom}(a_H),
$$
$$
E(a_S(s))=a_H(E(s))\quad(s\in\operatorname{dom}(a_S)).
$$

Reflection of relations, replacing the first implication by equivalence, is a stronger requirement and must be requested explicitly. These equations define a relation-preserving realization with exact action semantics on its image. It induces a functor between the categories of allowed action paths; identifying different paths requires checking the declared path equations as well. An arbitrary table of names is not already such a functor.

**Structural position** is the pattern of incidences, allowed changes and observations selected by this signature. Roles may remain indistinguishable under its automorphisms. If the data leave several alignments, retain the family and its distinguishing experiments instead of silently selecting one. A coarse signature can serve exploration; a stronger one can reject an earlier match. This is the same [executable refinement obligation](/docs/reference/mathematical-kernel#observable-closure) used when transferring an acquired representation into holonic computation.

## 2. Trigrams, hexagrams and Fano incidence {#триграммы}

The *Shuo Gua* describes divided/undivided lines, ordered positions and the doubling of trigrams into six-line figures. Encoding each line by a bit gives eight trigrams $V=\mathbb F_2^3$ and 64 hexagrams $V\times V$. This is a faithful encoding of those line patterns. [Primary text: Shuo Gua](https://ctext.org/book-of-changes/shuo-gua).

After choosing $000$ as zero, the seven nonzero vectors carry the Fano lines

$$
\{u,v,u+v\},\qquad u,v\ne0,\ u\ne v.
$$

This gives an exact incidence bridge to $\mathrm{PG}(2,2)$. Addition is an extra declared operation on the bit encoding: the incidence bridge alone does not show that historical interpretive rules use vector addition, or derive which UHM dimension a trigram represents. An explicit isomorphism is also needed between binary indices and the cyclic Fano numbering used elsewhere in the corpus.

Two different structures on the same eight patterns reveal the next constraint:

| Preserved structure, with zero fixed | Number of automorphisms |
|---|---:|
| Vector addition / Fano incidence | $\lvert\mathrm{GL}(3,2)\rvert=168$ |
| Addition and adjacency by changing one line | $3!=6$ |
| Addition and each individually named line-change action | $1$ |

Proof: a linear map is determined by three independent images, giving $7\cdot6\cdot4=168$. If it preserves one-bit adjacency, it must permute the three weight-one vectors. Conversely every coordinate permutation satisfies both requirements. If each of those three actions has its own fixed name, every basis vector is fixed. Without a distinguished zero the cube graph has 48 automorphisms; these are different comparison problems.

For example, the invertible map with columns $(001,011,100)$ preserves Fano lines but sends the one-line step $000\to010$ to $000\to011$, which changes two lines. Thus an incidence match need not preserve the transition grammar. Likewise $V\times V$ carries both six-bit addition and six individual line changes; neither is automatically the traditional ordering of the 64 figures.

## 3. The zodiac: a positive product construction and its boundary {#зодиак}

Number the 12 equal sign positions by $n\in\mathbb Z_{12}$, with a stated origin and orientation. The usual four triplicity classes and three modality classes are residue classes modulo 4 and 3; Ptolemy distinguishes these groupings in Book I, §§11 and 18. The following algebra is our formalization of this selected structure. [Primary text: Tetrabiblos I](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Ptolemy/Tetrabiblos/1B%2A.html).

$$
n\longmapsto(n\bmod3,n\bmod4)
$$

is a bijection, and cyclic succession becomes $(a,b)\mapsto(a+1,b+1)$. This is an exact structural correspondence, including opposition $n\mapsto n+6$. The cyclic step moves both factors; it is not Cartesian-product graph adjacency. Interpreting the factors as particular UHM functions still requires a role alignment.

A $3+4$ split of seven vertices supplies 12 cross-pairs. This realizes the same product set and admits a 12-cycle when its two parts are independently cycled. Additional Fano incidence changes the result: if the three vertices form a Fano line, its stabilizer has 24 elements and has no element of order 12. Consequently that 12-cycle cannot simultaneously be induced by a Fano automorphism. The stabilizer can nevertheless be transitive on the 12 cross-pairs: transitivity is weaker than possessing one cyclic generator.

This boundary identifies what a combined model needs: an explicit clock action alongside the incidence carrier, or a declared weaker correspondence. It does not rule out a dynamical 12-cycle in a richer holonic system, and it does not constrain a $3+4$ split that was never claimed to be a Fano line.

**A constructive phase clock.** Let $P_L$ project onto the three coordinate directions of a Fano line and let $\zeta=e^{2\pi i/12}$. Then

$$
U=\zeta^4P_L+\zeta^3(I-P_L),\qquad \Gamma_{t+1}=U\Gamma_tU^*.
$$

The operator acts on the two subspaces by phases of orders 3 and 4. An entry directed from the line block to its complement acquires $\zeta$; the reverse entry acquires $\zeta^{-1}$. Thus a state with a nonzero cross-block entry has period exactly 12, while within-block entries remain fixed. All seven coordinate Fano projectors are preserved pointwise because they are diagonal. Positivity and trace are preserved by unitary conjugation. Thus incidence and a 12-phase clock coexist on the same matrix; this clock rotates phases, not the 12 cross-pair addresses. No conventional symbolic meaning or human forecast is assumed.

To read this clock, retain a calibrated complex frame and both quadratures of a cross-block coherence. Diagonal projector expectations and closed cycle products alone remain constant. If every diagonal rephasing is instead quotiented out as gauge, the 12 matrices describe one equivalence class and this clock is unobservable in that quotient. The observation contract therefore determines whether the phase construction is an operational clock.

More generally, the unitary normalizer of the set of seven coordinate line projectors is $U(1)^7\rtimes\mathrm{GL}(3,2)$ in a fixed Fano labelling. Two distinct line projectors multiply to the projector of their unique intersection point; these generate the diagonal algebra. Its unitary normalizers are monomial matrices. Their permutation part must preserve Fano lines, and every diagonal unitary is allowed. This proves the claim; the common scalar phase acts trivially on Gamma. This contract does not assert preservation of the oriented octonionic three-form, octonion multiplication or all UHM operators. Those are different signatures, each requiring its own checks.

## 4. Kabbalistic structures: keep the types {#каббала}

The cited recension of *Sefer Yetzirah* distinguishes ten sefirot and 22 letters grouped as three mothers, seven doubles and twelve simples, with correspondences across world, year and embodied life. These are different types and relations. A specific later Tree diagram needs its own incidence data; its graph should not be inferred merely from these counts. [Primary text, chapters I–III](https://www.themathesontrust.org/papers/judaism/saadia.pdf).

For a proposed diagram, encode vertices, labelled paths, orders, oppositions and transformations separately. Ten distinct vertices cannot inject into seven dimension vertices, and 22 distinct paths cannot inject into 21 unordered coherence pairs. This leaves mathematically useful alternatives: observables on a holon, paths in a composed carrier, or an explicit quotient with a record of lost distinctions. None is ruled out by the count mismatch. The source meaning of mediation, opposition or generation then becomes a test of the chosen map through §1, rather than a reason to assign an arbitrary matrix entry.

## 5. Coherences: pair roles and closed phase relations {#фазовые-циклы}

Write $p_i=\gamma_{ii}$ and $\gamma_{ij}=r_{ij}e^{i\theta_{ij}}$. Positivity gives $r_{ij}^2\le p_ip_j$. The determinant constraint for each triple is

$$
p_ip_jp_k-p_i r_{jk}^2-p_j r_{ik}^2-p_k r_{ij}^2
+2\operatorname{Re}(\gamma_{ij}\gamma_{jk}\gamma_{ki})\ge0.
$$

This is a precise link between pair strengths and a joint phase relation. It applies to all 35 triples of seven indices. Fano incidence singles out seven triples; it does not supply the missing matrix entries or replace positive semidefiniteness. The pair and triple inequalities alone need not establish positivity of the full matrix.

Under a diagonal change of complex frame, $\Gamma\mapsto D\Gamma D^*$, an individual phase changes by $\alpha_i-\alpha_j$, whereas a cycle product is invariant. For a cycle $C$ whose edges all have nonzero coherence,

$$
W_C=\prod_{(i,j)\in C}\frac{\gamma_{ij}}{|\gamma_{ij}|}
$$

records its phase holonomy. This transformation law does not declare all diagonal rephasings to be physically unobservable in UHM: that requires specifying how other operators and measurements transform. It does provide a frame-independent comparison of these cycle products when such frame changes are allowed.

Use the actual support graph $G_\Gamma$ of nonzero coherences. For $n$ vertices, $m$ edges and $c$ connected components it has $m-n+c$ independent cycles. A spanning forest determines a cycle basis; a fixed star is valid only when all its required edges exist. The phase of a zero edge is undefined. Numerical implementations must declare the support criterion and report changes of support. Exact nonzero stored components define the algebraic graph; separating signal from numerical noise requires an additional calibrated criterion. This matters for Homoholograph's phase reconstruction and for SYNARC diagnostics alike.

## 6. When a symbolic state supports prediction {#предсказание}

Let $X$ be an observed history, $Z=\pi(X)$ its symbolic representation and $Y$ a future target. A sufficient representation for this target satisfies

$$
\Pr(Y\mid X)=\Pr(Y\mid Z)\quad\text{almost surely}.
$$

This condition is relative to a joint distribution and target; it is not implied by an isomorphism of symbol graphs. For a finite Markov kernel $P$ and state quotient $\pi$, a transition kernel on the symbols valid for every initial state exists exactly when, for every target block $B$,

$$
\sum_{y:\pi(y)=B}P(x,y)
=\sum_{y:\pi(y)=B}P(x',y)
\quad\text{whenever }\pi(x)=\pi(x').
$$

Necessity follows by starting from either state; sufficiency defines the same block probability from every representative. For example, merging states $a,b$ fails if $a$ transitions surely to $c$ while $b$ stays at $b$, with $c$ in another block. Restoring the distinction repairs this failure. In a learned system, this is a constructive reason to refine its representation or retain more history.

**Executable refinement.** Start from a finite partition that retains the selected observations. Within each current block, separate states whose vectors of transition probabilities into current blocks differ; repeat until stable. Each strict round increases the number of blocks, so there are at most $n-k$ strict rounds from $k$ initial blocks on $n$ states. Every stable refinement of the initial partition refines every iterate: by induction, equality of probabilities into its finer blocks implies equality of their sums into each current block. The terminal partition is therefore the coarsest stable refinement of the starting one.

`architecture/symbolica_predictive_quotient.py` implements this known finite lumpability mechanism with exact rational probabilities, an explicit failure witness and a quotient kernel. Its controls exhaust all 216 three-state kernels with entries in $\{0,1/2,1\}$ and all five seed partitions, then compare against every stable refinement. This is a reusable research prototype, not a currently integrated SYNARC learning algorithm. An estimated transition kernel needs separate uncertainty and validation analysis. The classical theory of exact aggregation is prior work: [Buchholz, 1994](https://www.cambridge.org/core/journals/journal-of-applied-probability/article/abs/exact-and-ordinary-lumpability-in-finite-markov-chains/2DC748F09D80BEEB03CCF18036E149D7).

For human forecasts, specify the observation protocol, target and horizon; fit the alignment only on training data; freeze it before evaluation; compare against history, calendar and base-rate controls. A useful reflective practice and an accurate future-event predictor are different measured functions. Existing Homoholograph null results remain evidence for their tested claims and populations; structural findings cannot erase them.

## 7. Engineering consequence {#реализация}

The proposed shared mechanism is a registry of typed correspondences with witnesses: source structure, target carrier, retained operations, unresolved alignments, failure examples and calibration data. Homoholograph would apply it to human observations and interpretations; SYNARC to acquired concepts, questions and executable programs. Integration of this registry remains an engineering task. Both can use UHM coherences while keeping their own tasks and evidence. A proposed mapping becomes reusable when its role and transition contracts are checkable.

The finite controls in `architecture/symbolica_role_transport.py` enumerate the incidence and transition cases above. They validate the stated finite structures, not empirical prediction or phenomenal experience. Together with the [back-projection protocol](/docs/applied/research/symbolic-correspondence#обратная-проекция), they replace unrestricted correspondences with explicit, refinable constructions.
