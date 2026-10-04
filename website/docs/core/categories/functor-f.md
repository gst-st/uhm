---
sidebar_position: 1
title: "Functor F: DensityMat → Exp"
description: "Definition of the functor F connecting the physical and experiential spaces"
---

# Readout and the proposed functor F

The proposed physical-to-experiential bridge requires a chosen state readout and an interpretation. It is not uniquely determined by the symmetry group of its codomain. The former universal T-42a/T-123 uniqueness claim is withdrawn [✗]; the [replacement theorem](/docs/proofs/categorical/uniqueness-theorem#теорема-единственности) establishes unitary/$G_2$ comparison only under explicit reversible-identification assumptions (RI).

## What a functor specifies

A functor assigns objects and arrows and preserves identities and composition:

$$
F(\mathrm{id}_A)=\mathrm{id}_{F(A)},\qquad F(\Psi\Lambda)=F(\Psi)F(\Lambda).
$$

Specifying $F$ only on states does not supply its action on processes. Declaring an experiential interpretation does not prove either functoriality or uniqueness.

## Object readout

For $X_N=\mathcal D(\mathbb C^N)$ choose $q:X_N\to Y$, with $Y$ a specified quality/configuration space [D/I]. The spectral data $\rho=\sum_\lambda\lambda P_\lambda$ are basis-independent. Eigenvectors in a degenerate eigenspace are not unique. A ray list requires a gauge choice or a quotient; it is not a continuous global spectral coordinate system.

In native $\mathbb C^7$, the $E$ axis has rank one: $P_E\Gamma P_E=\gamma_{EE}P_E$, whose normalisation is just $P_E$. The notation $\operatorname{Tr}_{-E}\Gamma$ is meaningful only for a declared **tensor factor**, not for deleting six basis directions. An extended experiential register and its readout are additional model input. Identifying its rays or eigenvalues with experienced qualities or intensities remains [I/H].

## Descent of arrows

For a surjective $q$, a channel $\Lambda$ induces an actual map $f_\Lambda:Y\to Y$ iff it preserves the readout's equivalence relation:

$$
q(\rho)=q(\sigma)\Longrightarrow q(\Lambda\rho)=q(\Lambda\sigma).
$$

Then $f_\Lambda(q(\rho))=q(\Lambda\rho)$ is well-defined and unique. These channels are closed under composition, and $f_{\Psi\Lambda}=f_\Psi f_\Lambda$, $f_{\mathrm{id}}=\mathrm{id}$. This defines a functor on the declared restricted category [T]. If $q$ is a quotient map, continuity of $q\Lambda$ also makes $f_\Lambda$ continuous. [Full proof](/docs/proofs/categorical/categorical-formalism#4-функтор-f-на-морфизмах).

Reading only $\gamma_{EE}$ fails descent for general channels: swapping axes $A,E$ reveals different $A$ weights in states with the same $E$ weight. Thus an arbitrary channel has no automatic restricted map on experience. Unspecified natural transformations or higher associators do not repair this obstruction.

## Faithfulness and identification

Faithfulness means injection on every hom-set, not on objects. Bijective $q$ gives a faithful conjugation assignment on represented processes, but does not identify the represented category with experience. Covariance $G\Psi_t=F_tG$ can hold for a constant encoder into a stationary state; forward-flow uniqueness does not prove encoder injectivity.

Under RI, comparison of two complete encoders and its inverse extend to CPTP maps; the comparison is unitary conjugation. Requiring a chosen unitary lift to preserve a specified positive octonionic three-form restricts it to $G_2$. If a fixed frame is retained, its common stabilizer further restricts the comparison. These are conditional statements about declared encodings, not a canonical phenomenal translator.

## Geometry and phenomenal interpretation

For a chosen register $\mathcal H_E$ the Fubini–Study metric on $\mathbb P(\mathcal H_E)$ is

$$
d_{FS}([\psi],[\phi])=\arccos|\langle\psi,\phi\rangle|
$$

for unit representatives. The [enriched Yoneda theorem](/docs/proofs/categorical/categorical-formalism#enriched-yoneda) proves precise relational and finite-probe statements inside that quality model. It does not prove that those rays are conscious experiences or that $F$ exists on every quantum process.

A continuous readout between specified spaces induces a geometric morphism between their open-cover sheaf topoi. This sheaf-level construction is different from the process functor and has no automatic physical/phenomenal interpretation. AI encodings and fitted CPTP process approximations require the [measurement protocol](/docs/applied/research/measurement-protocol); ordinary Jacobian linearization does not imply complete positivity or trace preservation.

## Current status

The descent criterion and restricted functoriality are [T]. The state readout, experimental calibration and phenomenal bridge are [D/H/I]. Universal $G_2$ uniqueness, unconditional faithfulness, automatic higher-category completion and closure of the explanatory gap are withdrawn [✗]. Canonical details: [categorical formalism](/docs/proofs/categorical/categorical-formalism), [representation/tomography](/docs/proofs/categorical/uniqueness-theorem), [mathematical kernel](/docs/reference/mathematical-kernel).

## Historical section addresses

The corrected scope of statements at these addresses is given above.

<a id="analogy-a-translator-between-languages"></a>
<a id="canonicity-of-f-why-this-particular-functor"></a>
<a id="chapter-summary"></a>
<a id="concrete-example"></a>
<a id="connection-with-dual-aspect-monism"></a>
<a id="connections"></a>
<a id="context-the-stage-of-experience"></a>
<a id="definition-on-morphisms"></a>
<a id="definition-on-objects"></a>
<a id="diagram-functor-f-in-the-context-of-uhm"></a>
<a id="faithfulness"></a>
<a id="formal-definition"></a>
<a id="functoriality-t"></a>
<a id="intuitive-explanation-what-f-does"></a>
<a id="key-properties"></a>
<a id="limitations-and-open-questions"></a>
<a id="motivation-why-functor-f-is-needed"></a>
<a id="phenomenal-completeness-t"></a>
<a id="precursor-what-a-functor-is"></a>
<a id="qualities-colors-of-experience"></a>
<a id="spectrum-palette-of-intensities"></a>
