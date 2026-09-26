---
sidebar_position: 3
title: "Structure: the Geometry of Quality Space"
description: "The invariants UHM commits to for quality space and for Γ — dimension, relations, prohibitions — each with its registry status, the methods that test it, and what would confirm or refute it"
slug: /consciousness/empirical/structure
---

# Structure: the Geometry of Quality Space

:::info Why structure is the strongest channel
A calibration fixes constants; any theory can be fitted to a single quality. A **structure** — the pattern of relations among many qualities, or among the components of $\Gamma$ — can be fitted only if it has the shape the theory committed to before the data were seen. UHM commits in advance to complex projective geometry for quality, seven axes and seven Fano lines for $\Gamma$, a window and two bands for a living state. Each commitment forbids something measurable. This page lists the commitments with their statuses, the methods that test them, and the results that would count for and against. It reports no data.
:::

## What a structural test can and cannot show {#scope}

- **It tests geometry, not consciousness.** The quality geometry of a state and the verdict $\mathrm{Cons}(S)$ are independent: the Fubini–Study distances between the eigenrays of $\Gamma$ do not depend on its spectrum, and purity does not depend on the eigenrays; the same geometry is carried by a state with $P = 0.152$ (outside the window) and one with $P = 0.312$ (inside) ([measurement protocol](/docs/applied/research/measurement-protocol#substitution-position) [T]). A similarity structure shared by a person and a language model — GPT-4 matched colour-neurotypical humans on 93 colours at a matching rate of 91.4 % (Kawakita et al. 2024) — says nothing, in UHM, about whether the model is conscious.
- **It supports the identity without proving it.** The identity of the internal side of $\Gamma$ with experience stays [I] whatever the data say ([T-214 [T]](/docs/proofs/categorical/fundamental-closures#t-214)). What structure can do is give that identity many chances to fail.
- **It needs calibration for its metric form.** Without the map $f$ from perceived dissimilarity to $d_{\mathrm{FS}}$ ([calibration, K3](./calibration#k3-metric)) every metric test below is ordinal.

## The invariants {#invariants}

Each row gives what UHM asserts, the status of the assertion, and where it is proved or stated. "Math" is the status of the statement about $\Gamma$; "reading" is the status of its reading as a statement about experience.

| # | Invariant | Math | Reading | Source |
|---|---|---|---|---|
| S1 | Quality space is $\mathbb{CP}^{n-1}$ with the Fubini–Study distance; the enriched Yoneda embedding is an isometry, enriched isomorphism is identity | [T] | [I] | [enriched Yoneda](/docs/proofs/categorical/categorical-formalism#enriched-yoneda) |
| S2 | Intensity and quality are separate parameters: 6 spectral numbers against 42 eigenvector numbers | [T] (T-300) | [I] | [qualia structure](/docs/consciousness/phenomenology/qualia-structure#теорема-пространство-качества) |
| S3 | Content has 7 axes and 21 channels, and no more (closure T.1); $48 = 27 \oplus 14 \oplus 7$ under $G_2$ | [T] (T.1, T-146, T-301) | names of channels [I] | [taxonomy](/docs/consciousness/phenomenology/qualia-structure#замкнутость), [decoder](/docs/consciousness/phenomenology/qualia-structure#теорема-декодер) |
| S4 | Irreducible quality is carried by 7 Fano holonomies $H_p$, one per line | [T] (T-301) | [I] | [decoder](/docs/consciousness/phenomenology/qualia-structure#теорема-декодер) |
| S5 | Fano lines organise the coherences: block transparency | [T] (F-Gap-2) | — | [F-Gap-2](/docs/reference/falsifiability#f-gap-2-блоковая-прозрачность-по-фано-триплетам) |
| S6 | Intra-line Gap below inter-line Gap; testable as triple holonomy on 7 lines against 28 non-lines | [H] (F-Gap-1) | — | [F-Gap-1](/docs/reference/falsifiability#f-gap-1-внутри-триплетный-gap-ниже-межтриплетного) |
| S7 | A line is a parity check on its three signs | [C] (T-306) | — | [what a line checks](/docs/consciousness/phenomenology/qualia-structure#что-проверяет-прямая) |
| S8 | The conscious window $2/7 < P \leq 3/7$ is non-empty, and its four conditions are independent | [T] (T-124, T-124b) | criterion of consciousness: [D] core of T-153 | [conscious window](/docs/proofs/consciousness/conscious-window#t-124b) |
| S9 | Anything alive has $s_1 \in [1/7, 3/14]$ and $s_2 \in [1/7, 2/7]$ (F-Band) | [T] (T-321, T-323) | — | [F-Band](/docs/reference/falsifiability#f-band-две-суммы-живого-состояния) |
| S10 | Under the canonical decay the moduli fall as $e^{-5\gamma t/21}$ and each holonomy's value stays fixed: qualities fade, they do not drift | [T] for the dynamics | [H] as a prediction about experience | [how qualia die](/docs/consciousness/phenomenology/qualia-structure#выцветание) |
| S11 | Irreducible phase and integration are opposed; at $\Phi = 1$ the typical line holonomy is $0.6387$ rad for evenly twisted content | [C] (T-307) | [I] | [how much quality fits](/docs/consciousness/phenomenology/qualia-structure#сколько-качества-помещается) |
| S12 | Emotional space is 30-dimensional; valence is $\mathrm{sign}(dP/d\tau)$ | [T] (T-147); valence [C] (C.1) | names of emotions [I] | [emotional taxonomy](/docs/consciousness/phenomenology/emotional-taxonomy#карта-эмоций) |
| S13 | Number of independent slow components in fMRI lies in $[6, 12]$ | [H] (F-ISF) | — | [F-ISF](/docs/reference/falsifiability#f-isf-isf-компоненты-в-фмрт) |

**Dimension of quality space.** The theory fixes the *type* of geometry, not $n = \dim\mathcal{H}_E$. In the minimal 7D formalism the $E$-sector is one-dimensional; in the 42D Page–Wootters realisation $\rho_E$ is a $7 \times 7$ block on the clock register; a genuinely many-dimensional $\mathcal{H}_E$ needs a composite substrate ([the $\rho_E$ box](/docs/core/structure/dimension-e#rho-e-7d-42d)). The dimension $n$ is therefore something to **measure** — and the realisability condition below gives a way to bound it from similarity data.

## What the geometry forbids {#prohibitions}

A commitment is worth as much as what it excludes. From the invariants above, UHM forbids:

1. **Metric violations.** After calibration, perceived dissimilarities must satisfy the triangle inequality within tolerance ($\lvert d(a,b) + d(b,c) - d(a,c)\rvert < 0.15$ for violations, per [prediction 4](/docs/reference/falsifiability#metric-relations)) and stay within the diameter $\pi/2$ of $\mathbb{CP}^{n-1}$.
2. <a id="realisability"></a>**Unrealisable matrices.** A finite dissimilarity matrix $(d_{ij})$ is realised by rays of $\mathbb{CP}^{n-1}$ if and only if, for some phases $\theta_{ij} = -\theta_{ji}$, the Hermitian matrix $G_{ij} = \cos(d_{ij})\,e^{i\theta_{ij}}$, $G_{ii} = 1$, is positive semidefinite of rank at most $n$ (item 7 of the [enriched Yoneda theorem](/docs/proofs/categorical/categorical-formalism#enriched-yoneda) [T]). In particular **at most $n$ qualities can be pairwise at the maximal distance** $\pi/2$.
3. **Resolution below the probe bound.** A probe set with covering radius $\delta$ has at least $\sin^{-2(n-1)}\delta$ elements; 93 probe colours cannot resolve below $\arcsin(1/\sqrt{93}) \approx 0.104$ rad even on $\mathbb{CP}^1$. A claimed resolution finer than the bound allows is an artefact.
4. **A conscious state outside the bands.** A system that independent evidence in $D_{\mathrm{nat}}$ calls conscious, whose reconstructed $\hat\Gamma$ lies outside the window or outside F-Band, falsifies the reconstruction; a state meeting all four criteria with $s_1$ or $s_2$ outside its band falsifies the algebra ([F-Band](/docs/reference/falsifiability#f-band-две-суммы-живого-состояния); zero counterexamples over $20\,000$ states per band so far).
5. **Drift while fading** [H]. As a state decoheres under the canonical dynamics, a quality loses intensity without passing through neighbouring qualities; "there is no half-changed quale".

## Methods {#methods}

### Similarity geometry: MDS and representational similarity analysis {#mds-rsa}

Collect full pairwise dissimilarity matrices within one modality. Multidimensional scaling gives a first picture of dimension and shape; representational similarity analysis compares the behavioural matrix with the matrix of $d_{\mathrm{FS}}$ between eigenrays of $\hat\Gamma$ ([calibration, K3](./calibration#k3-metric)). The falsifiability page fixes the thresholds: Spearman correlation above 0.6, monotonicity violations below 10 %, triangle tolerance 0.15, MDS stress below 0.1 for $\mathbb{R}^k$.

### The Tsuchiya paradigm: enriched categories and unsupervised alignment {#tsuchiya-paradigm}

Tsuchiya, Phillips and Saigo (2022) model a quality space as a category enriched in dissimilarities, and compare two subjects' spaces by unsupervised Gromov–Wasserstein alignment — no labels, only structure (Kawakita et al., *iScience* 2025, across people; Kawakita, Zeleznikow-Johnston, Tsuchiya & Oizumi, *Sci. Rep.* 14: 15917, 2024, between people and language models). UHM adopts the method and adds a commitment: the space should be a Fubini–Study geometry, so that enriched isomorphism is identity and a Gromov–Wasserstein distance of zero is an isometric bijection ([what UHM adds](/docs/proofs/categorical/categorical-formalism#enriched-yoneda)). The precedent and its standing are on the [theories page](/docs/consciousness/comparative/consciousness-theories#category-qualia).

### Realisability and the rank of quality space — proposed here [Pr] {#rank-estimate}

For a calibrated matrix, search over phases for the smallest rank $n^*$ of a positive semidefinite $G$ realising it within measurement error. Two predictions follow [H]: (a) $n^*$ exists — the matrix is realisable at all; (b) within one modality $n^*$ stabilises as stimuli are added, rather than growing with the stimulus count. A competing geometry (real Euclidean, hyperbolic) is compared by cross-validated fit at equal parameter count; a systematically better fit of a non-projective geometry counts against S1.

### Topological analysis {#topology}

Persistent homology of the similarity structure reports the topology of the **sampled** set of qualities — the hue circle, for instance, is one loop. It does not see the ambient space: a circle embeds in $\mathbb{CP}^1$ as well as in the plane. Topology therefore tests S1 only through what the ambient geometry constrains — bounded diameter, the maximal-distance count, realisability — and is used here to choose stimulus sets that cover a manifold without holes in the probe cover (item 3 above).

### Structure of $\Gamma$ itself {#gamma-structure}

- **Seven axes and the Fano blocks** in self-report: confirmatory factor analysis of the 28-item audit, testing whether the 7-triad block structure fits better than random tripartitions ([Console V0-VAL](/docs/applied/console/roadmap-validation#v0), a self-report analogue of F-Gap-2).
- **Seven axes in neural data**: the number of independent slow components in fMRI (F-ISF [H]), and the seven-component stress tensor ([experiment IV.1](/docs/applied/research/experimental-protocol#exp-4-1)).
- **Fano holonomy**: on live $\hat\Gamma$ with phases from EEG phase locking, compare $\lvert H_p\rvert$ on the 7 lines with the 28 non-line triangles. The corpus's own machine check found no difference on 180 constructed natal states ($+0.03 \pm 0.39$ rad): the Fano structure is what the dynamics preserves, so the signature must be sought in states that have passed through the Fano channel, not in constructions ([current empirical status](/docs/reference/falsifiability#summary-table-of-predictions)).
- **Window and bands**: $\hat P$, $\hat\Phi$, $\hat R$, $s_1$, $s_2$ across sleep–wake and anaesthesia with a frozen $\pi_{\mathrm{bio}}$ ([calibration, K1–K2](./calibration#k1-threshold)). On the uniform diagonal the window is exactly $\Phi \in (1, 2]$, $R \in [1/3, 1/2)$, $C \in (1/2, 2/3]$ ([Step 5](/docs/applied/research/measurement-protocol#pci-связь) [T]) — three readouts that must move together.
- **Fading** [Pr]: during anaesthetic induction or sleep onset, collect repeated similarity judgements on a fixed stimulus set at graded depth. S10 predicts that intensity ratings fall while the rank order of dissimilarities stays that of baseline; a systematic drift of qualities (a hue shifting before it vanishes) counts against S10 as a claim about experience.

## Confirmation and refutation {#verdicts}

| Invariant | Would confirm | Would refute |
|---|---|---|
| S1 geometry | Calibrated matrices realisable at a stable $n^*$; projective geometry fits better than Euclidean at equal parameters; cross-subject alignment near-isometric | Metric violations beyond tolerance; more pairwise-maximal qualities than $n^*$; unrealisable matrices after calibration |
| S2 intensity/quality | Isospectral states differ in quality, not intensity; context changes quality at fixed $\rho_E$ | Identical full invariants, distinguishable experience ([refutation criterion](/docs/reference/falsifiability#refutation-criterion)) |
| S3 seven axes | 7-triad structure beats random tripartitions; $N_{\mathrm{ISF}} \in [6, 12]$ | Block structure no better than random; $N_{\mathrm{ISF}}$ systematically outside $[6, 12]$ |
| S4–S6 Fano | Line holonomies and blocks separate from non-lines in live states | No separation in live states that have passed through the Fano channel |
| S8–S9 window and bands | Wake inside, N3 below, both exits as predicted; conscious states inside F-Band | Any of the falsifiers of [calibration](./calibration#falsification); a conscious state outside F-Band |
| S10 fading | Intensity falls, similarity order holds | Qualities drift before they vanish |

A single refutation acts at the status of the claim it hits: against a [T] row it means an error in the proof or in the bridge to data (the experimental protocol's structural level), against an [H] row it removes the hypothesis, against an [I] reading it removes the support that reading had.

**Next:** [Engineering →](./engineering) · **Back:** [Calibration](./calibration)
