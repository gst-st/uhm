---
sidebar_position: 17
title: HomoHoloGraph
description: "The coherent life navigator: the natal bodygraph as one sensor feeding a Γ-prior; the bridge dictionary, the HB calibration, and the laboratory application"
---

# HomoHoloGraph: the coherent life navigator

**Status frame.** This page documents an engineering research program, not new
theorems. Every claim carries one of three honesty classes: **VERIFIED**
(computed fact about the machinery or astronomy), **DESIGN** (self-consistency
of an engineering choice — true by construction, demonstrated, *not* evidence
about humans), **OPEN** (needs human data; the n-of-1 protocol exists for
exactly this). The center→dimension dictionary itself is an [И]-dictionary:
structured, configurable, and testable — never a fact.

## 1. The idea: from bodygraph to homogram

[Human Design, dissected earlier](./human-design.md), turned out to be three
layers: a real clock, real hidden combinatorics, and a storyteller whose
bridge to human fate is supported by nothing. HomoHoloGraph keeps the first
two layers, **replaces the storyteller with a computational model**, and
gives the user the instruments to test that model on themselves.

The object is no longer the bodygraph. It is the **homogram** — the person's
holonic record in the UHM state space: a prior $\Gamma_0 \in D(\mathbb{C}^7)$
over the seven dimensions $[A,S,D,L,E,O,U]$ with the theorem-forced
21-coherence wiring (T-224: seven is the unique self-diagnosing alphabet),
plus derived profiles. The natal chart is **one sensor** — valuable because
its input (birth date, time, timezone) is universally available and its
computation is exact. It is a prior, not a verdict: the filter layer updates
it from observation, and observation always outranks nativity.

## 2. The bridge dictionary (an [И]-dictionary, structured)

HD's own taxonomy splits the nine centers into **two pressure centers**
(Head, Root) and seven processing centers. That split is the hinge of the
bridge: seven processing centers map to the seven dimensions; the two
pressure centers are not populations but **drive ports** — where the
environment pumps supply into the pattern.

| center (HD function, literal) | dimension | reading |
|---|---|---|
| Throat — manifestation, speech | **A** Articulation | to distinguish, to express |
| Splenic — survival-now, immune system | **S** Structure | to hold form |
| Sacral — life force, work, response | **D** Dynamics | to move, to process |
| Ajna — conceptualization | **L** Logic | to reconcile |
| Solar Plexus — emotion, the wave | **E** Interiority | to experience |
| Heart/Ego — will, promises, resources | **O** Ground | to root, to provision |
| G — identity, direction, love | **U** Unity | to gather into one |
| Head, Root — the two pressure centers | **κ-ports** | the tyaga (drive profile) |

A structural bonus falls out at once: the defined pressure channels feed only
**L** (from Head) and **D, S, E** (from Root). Articulation, Ground and Unity
have no direct pressure line — they are supplied through internal coherences
only. VERIFIED (a property of the channel table).

## 3. The encoder

For an activation set $\mathcal{A}$ (Design, Personality, or their union),
with $\mu = 2$ for the two lights (Sun/Earth) and $1$ otherwise:

**Populations** — activated processing gates, channeled at full weight,
hanging at half:

$$
w_i \;=\; \sum_{a \in \mathcal{A}:\ c(g_a) \to i} \mu_a
\cdot \big(1 - \tfrac{1}{2}[g_a \text{ hanging}]\big),
\qquad
p_i \;=\; \frac{1-\alpha}{7} + \alpha \frac{w_i}{\sum_j w_j},
\quad \alpha = 0.8 .
$$

**Coherences** — each defined channel between processing centers $i,j$
contributes a phase quantized by its two line values:

$$
\gamma_{ij} \;{+}{=}\; \beta\, e^{i\theta},
\qquad
\theta = \frac{\pi(\bar\ell_a + \bar\ell_b)}{6},
\quad \beta = 0.12,
$$

then Hermitize, project to the PSD cone, normalize the trace. Channels
touching a pressure center contribute to the **tyaga** $\kappa_w$ instead.

Three states come out of one chart: $\Gamma_0 = E(\text{union})$ (the
pattern), $\rho_0 = E(\text{Personality})$ (the mind's self-map),
$\mathrm{body}_0 = E(\text{Design})$ (the body imprint). Two derived
quantities have no analogue in any bodygraph tool:

- **razlad** $D_{ns} = \lVert \rho_0 - \mathrm{body}_0 \rVert_F$ — the
  computable size of the mind↔body imprint mismatch. Population median 0.396,
  IQR [0.33, 0.46]; correlates $r=0.35$ with the Personality/Design
  definition mismatch. HD's "the mind is not the authority" becomes a number.
  VERIFIED (as a property of the encoder over 6000 charts).
- **poristost** — the gain map: an open center marks a dimension that samples
  the environment (high filter gain, high process noise); a defined center —
  low. This is the operational reading of "openness = conditioning," and it
  is *testable per user*: open dimensions must show higher variance in
  repeated self-reports. OPEN.

## 4. The HB calibration (6000 charts; architecture/homoholograph.py)

| # | stratum | result | class |
|---|---|---|---|
| HB01 | physicality | 6000/6000 PSD+trace-1; $P \in [0.151, 0.449]$ | VERIFIED |
| HB02 | Reflector limit | no definition ⇒ $\Phi = 0$ exactly; lowest mean $P$ (0.200) — the encoder *rediscovers* the "lunar mirror" | VERIFIED |
| HB03 | type geometry | mean $P$ orders Reflector < Projector < Generator < Manifestor < MG; types are connectivity classes, scalars separate them only partially ($d' \approx 0.3$) | VERIFIED |
| HB04 | islands | split definition in 60.3% of charts ⇔ disconnected γ-graph (0 violations); **bridges (partner/transit) are what merge islands** | VERIFIED |
| HB05 | razlad | median 0.396; $r = 0.35$ with P/D definition mismatch | VERIFIED |
| HB06 | synastry = T-77 | composite ("electromagnetic") channels are exactly cross-bridges; pair $\Delta P \ge 0$ in 240/240 (phase-aligned), $r = 0.38$ with composite count | VERIFIED |
| HB07 | gains | center-informed gains beat uniform beat anti-informed (0.242 / 0.245 / 0.326) under doctrine-shaped noise | DESIGN |
| HB08 | transit dwell | median days per gate: Moon 1, Sun 6, Mars 9, Jupiter 27, Saturn 50, Pluto 68+; the sky completes ≥1 new channel on 98% of days | VERIFIED |
| HB09 | n-of-1 power | blind day-rating vs drive prediction: 0.5σ ≈ 70 d, 0.35σ ≈ 100 d, 0.2σ ≈ 300 d; false positives ≈ 2% | VERIFIED |
| HB10 | authorities | decision policies for the bold-move gate: emotional = wait out the wave (81% vs 73% on AR(1) E-noise), sacral = respond now, splenic = first read | DESIGN |
| HB11 | cohort base rates | type frequencies are epoch functions (the 116M-birth audit); the app must show the *user's cohort* base rates | VERIFIED |
| HB12 | yakornost | ±2 min changes nothing; ±15 min flips gates in 5% of charts and TYPE in 1%; ±60 min — 19% and 2.3% | VERIFIED |
| HB13 | sensor architecture | the bodygraph audited against the K7/Fano standard — see §4b | VERIFIED |

The one refuted expectation along the way is recorded honestly: razlad does
**not** correlate with union-only "cooperative" channels ($r = 0.00$) — they
enter neither pure prior, so no mechanism exists; the correct driver is the
P/D symmetric difference (HB05).

## 4b. The sensor-architecture audit (HB13): nothing on faith

The lab's standard is the theorem-forced one: seven dimensions, the **complete**
$K_7$ of 21 coherences, Fano-organized, self-diagnosing (T-224). The bodygraph's
own 9-center/36-channel architecture was audited against it — exhaustively,
by table:

- **Coverage 13/21.** The 36 channels realize only 17 of 36 center pairs, and
  after the dictionary — only **13 of the 21 dimension pairs**, with
  redundancy up to ×4 (A–U and D–U have four parallel channels each) where
  the UHM standard needs none.
- **The blind zone (8 pairs): D–L, D–O, E–L, E–S, E–U, L–O, L–S, L–U.** No
  natal chart can couple these. **Logic couples natally only to
  Articulation** (5 of its 6 pairs blind); Interiority never meets Structure
  or Unity; Ground never meets Dynamics (there is no Heart–Sacral channel).
- **Class invariance.** Transits and synastry composites draw from the *same*
  36-channel table — so the blind zone is invariant for the **entire HD
  instrument class**. No amount of partners or planetary weather writes into
  those 8 cells. Repair requires sensors *outside* the class: the diary and
  the filter.
- **Fano realizability 1/7.** Of the seven corpus triads only **S–O–U** is
  fully natal-realizable; D–L–U and L–E–O reach 1 of 3 pairs each.
- **No self-diagnosis.** 29 of 36 single-channel faults are indistinguishable
  by center-connectivity syndrome (multiplicity masks members). The UHM Fano
  alphabet has 0 — it is the unique seven-letter system where every single
  fault names itself.
- **Sensitivity bias.** Gates per axis: A=11, D=9, U=8, S=7, E=7, L=6, O=4 —
  the instrument hears Articulation 2.75× louder than Ground.

All VERIFIED (exhaustive checks in `hb13_architecture_audit()`; the blind
zone is a compile-time constant in the Rust core with a test, and the UI
hatches those cells in the $\Gamma_0$ heatmap: the sensor must *show* where
it is blind).

## 5. The application (Rust, `homoholograph/` workspace)

A native laboratory app (egui/eframe GUI + headless `hhg-report --json`),
repo `projects/oldman/homoholograph`, symlinked at `internal/homoholograph`.

**The self-contained ephemeris is itself a result.** Meeus series (VSOP87
planets, ELP-2000/82 Moon, analytic Pluto precessed from J2000), nutation,
aberration, light-time — cross-verified against Swiss/Moshier on 40 moments
× 13 bodies: all planets ≤ 2″, Moon 8″, Pluto 1.3″, and the **true lunar
node computed from first principles** as the ascending node of the osculating
orbit ($h = r \times v$, $\Omega = \operatorname{atan2}(h_x, -h_y)$) — 50″
from Swiss with no node series at all. **520/520 gates and 520/520 lines
agree.** The encoder matches the Python reference to $10^{-6}$ on all 49
matrix entries. VERIFIED (`cargo test`).

Screens (each stating its honesty layer):

- **Гомограмма** — bodygraph (the sensor) + $\Gamma_0$ heatmap + stress
  panel (repaired T-92) + tyaga + poristost + razlad + chord connectivity
  (blocks / lone voices vs HD split).
- **Смычка** — the duogram: composite channels drawn as dashed bridges on
  both bodygraphs; the pair increment $\Delta P \ge 0$ computed live; "the
  increment lives in the bridge, not in the banks."
- **Небограф** — today's timebridges (channels the sky completes), the
  slowness ladder; influence explicitly marked as layer-3 hypothesis.
- **Правдомер** — the three layers, cohort base rates, n-of-1 power table,
  and the **yakornost of the user's own chart** (birth-time robustness —
  shown by no other bodygraph tool).
- **Лаборатория** — the bridge as knobs: dictionary variants, α/β/μ sliders,
  live recompute, a trace journal. $P, \Phi, S$ are invariant under
  dictionary permutation (an axis permutation is an isometry); the panel,
  tyaga and all axis-readings are sensitive — which is precisely the
  testable content of the dictionary.

## 6. What this transforms

| HD doctrine | HomoHoloGraph reading | class |
|---|---|---|
| type | connectivity class of the chart graph; a prior, not a cage | VERIFIED (as construction) |
| strategy | navigation policy over golden paths (drift vs bold crossing) | DESIGN |
| authority | sensor-choice policy for the decision gate | DESIGN |
| open centers | high-gain, high-noise dimensions of the filter | OPEN (testable) |
| not-self | razlad $D_{ns}$ + the stress panel | VERIFIED (as a quantity) |
| conditioning | environment drive through open ports; estimator prior vs observations | DESIGN |
| transits | drive schedule; timebridges | VERIFIED (astronomy) / OPEN (influence) |
| synastry / composite | cross-bridges; $\Delta P \ge 0$ lives in the bond (T-77) | VERIFIED (model) |
| "purpose" | not a verdict: the basin map — where the drift already carries you | DESIGN |

## 7. Roadmap

1. Diary → estimator [K]: track the *current* $\Gamma$, not only the prior;
   poristost-informed gains.
2. Правдомер v2: blind daily predictions from the nebograph + Brier score —
   the app falsifies its own layer 3 per user.
3. Group floor: the team as a meta-holon — what passes upward is the shared
   direction (H65), computed from member states.
4. Dictionary tournament: score alternative dictionaries against user data —
   the [И]-dictionary becomes an empirical object.
5. Geocoding + historical timezones (chrono-tz already handles DST rules).

## Part II. The heptacode: the wheel refounded

The audit of §4b demands more than patches — it demands a reconstruction.
It exists, it is exact, and it keeps the astronomical layer untouched.

### 8. The counting identity and the hidden seventh voice

$$
2^6 = 64 = \binom{7}{0}+\binom{7}{2}+\binom{7}{4}+\binom{7}{6}
$$

A hexagram (six visible lines) **plus one parity bit** is precisely an
even-weight codeword of the $[7,6]$ parity code over the seven dimensions.
The corpus coordinatization dictionary (the $(3\leftrightarrow4)(5\leftrightarrow6)$
involution) fixes position 7 in both labelings — and position 7 is **O,
Ground**. So the I-Ching shows six lines because *the seventh voice is the
parity the six carry*: the Ground does not appear among the lines; it holds
their evenness. Under this reading every one of the 64 gates **is** a
canonical object of the Γ-structure:

| support | count | object |
|---|---|---|
| ∅ | 1 | the **Source** gate (computed: it is KW 2, the Receptive) |
| pair | 21 | a **coherence, by SSOT name** (e.g. KW 51 = Актуализация A–D, KW 8 = Полнота O–U) |
| 4-set = triple′ | 7 | a **Fano-line shadow** (the Hamming spine) |
| 4-set = triple′ | 28 | a **triangle** (tension triad) |
| 6-set = singleton′ | 7 | a pure **voice** (computed: KW 1, the Creative, is the voice of O) |

### 9. Machine-verified theorems (T-H1–T-H6, HB14)

- **T-H1 (atlas).** The census is exactly 1/21/7/28/7. VERIFIED.
- **T-H2 (antipode law).** On the physical wheel, the antipode of pair
  $\{x,y\}$ is the triple $\{x,y,O\}$ — every coherence sits opposite
  *itself, grounded*; the antipode of $\{x,O\}$ is the pure voice $x$; the
  Source sits opposite the voice of O. All 64 verified. (The three pairs
  whose grounding is a Fano line are exactly the corpus lines through O:
  A–D, S–U, L–E.)
- **T-H3 (triangle resolution).** Every tension triad $T$ casts a collinear
  shadow $\sigma(T)=\{a{\oplus}b, b{\oplus}c, a{\oplus}c\}$ and a lone
  witness $m = a{\oplus}b{\oplus}c$; $T \cup \sigma(T) \cup \{m\}$ is all
  seven. 28/28. Every tension *names its resolution line and its witness*.
- **T-H4 (syndromes).** Every gate's Hamming syndrome reads canonically:
  a pair points at the third voice of its line; a triangle at its witness;
  a voice at itself; the Source and the seven line-shadows are the
  syndrome-0 **spine** (KW 2, 12, 18, 28, 30, 54, 61, 63). The census is
  $7\times8+8$. The wheel becomes a self-referential pointer structure —
  the self-diagnosis the legacy wiring lacked (29/36 ambiguous) is
  inherited from the code.
- **T-H6 (independence).** The legacy center assignment carries *no*
  information about the heptacode structure (MI 0.73 bits vs permutation
  null 0.76, p = 0.62): this is a refoundation, not a relabeling.
- **HB14 (coverage in real charts).** Median chart: legacy channels light
  **2 of 21** coherences (max 8; hard ceiling 13); the heptacode reading
  lights **19 of 21** (max 21), with 7 of 8 formerly blind cells lit.
  The blind zone is not just repairable in principle — it is repaired in
  every real chart.

### 10. Empirical calibration against a production instrument

The user's own chart (07.04.1985, 10:57, Dzhambul) was cross-checked against
a production HD application: with the app's assumed zone, our engine matches
**26/26 activations including the third wheel level (color)**; the PHS
arrows («PLL DRR») are reproduced exactly by our tones (tone ≤ 3 = Left).
One honest discrepancy is the *timezone itself*: the app uses UTC+6 while
the IANA history for 1985 (Soviet decree + summer time) gives UTC+7 — and
the difference touches **only the Moon's lines**; the gate set, channels,
type, profile, authority and both Suns are zone-stable. The node tones sit
at the 1.6-arcminute scale where engines legitimately differ by one step.
In the reconstructed reading the same chart shows: P.Sun = the
Actualization coherence (A–D, syndrome → U); D.Sun = the full Fano line
{L,E,U} (spine); Mars and the North Node of Personality on the **Source
gate**; D.Moon = Репрезентация (S–E) — a coherence the legacy instrument
class *cannot see*; profile 3/5 = voices L/U (hexagram line $k$ = voice:
A S L D U E, hidden O).

### 11. What changes in the application

The Rust core carries the generated atlas (`recon.rs`, tested: census,
spine, names) and **encoder v2** — no blind zone, selectable live in the
Laboratory; the **Роза-64** screen re-reads all 26 activations as canonical
objects with SSOT names, syndromes and spine hits. Honesty classes stay:
the code arithmetic and atlas are VERIFIED; object *readings* are the
[И]-dictionary on corpus names; influence on a person remains OPEN — the
pravdomer exists for exactly that question.

## Part III. The living layer: tomography, warnings, the rose ring

### 12. The diary as rigorous state tomography (HB15–HB16)

$d = 7$ is prime, so exactly $d{+}1 = 8$ mutually unbiased bases exist — and
they are the *optimal* measurement set for determining a density matrix
([Wootters & Fields 1989](https://ui.adsabs.harvard.edu/abs/1989AnPhy.191..363W/abstract)).
Eight lenses × six independent numbers $= 48 = d^2{-}1$: the diary needs
exactly 48 numbers for a complete readout of $\Gamma$, with a closed-form
reconstruction

$$
\Gamma \;=\; \sum_{b,m} p_{b,m}\,\Pi_{b,m} \;-\; \mathbb{1}.
$$

Machine-verified: unbiasedness to $2.5\times10^{-16}$, measurement rank 49
(complete); reconstruction exact to $10^{-15}$; at finite samples the MUB
lenses beat Haar-random bases by 2.7–6× in Frobenius error (N = 50/200/800
per basis: 0.26/0.16/0.08 vs 0.70/0.61/0.51). An all-uniform diary
reconstructs exactly the grey state — the instrument is neutral by
construction. The heptacode's syndrome census ($7\times8+8$) had already
whispered the same arithmetic: eight families over a seven-alphabet.
The app blends observation with the natal prior,
$\Gamma_{\text{post}} = (n_0\Gamma_0 + n\hat\Gamma)/(n_0{+}n)$ —
observation outranks nativity as the diary grows.

### 13. Early warnings, with their honest weakness (HB17)

The mood literature reports rising lag-1 autocorrelation and variance before
depressive transitions — critical slowing down
([van de Leemput et al., PNAS 2014](https://www.pnas.org/doi/10.1073/pnas.1312114110);
[a personalized case, 2016](https://karger.com/pps/article/85/2/114/294376/Critical-Slowing-Down-as-a-Personalized-Early)) —
along with a sober critique
([Bos & de Jonge, PNAS 2014](https://www.pnas.org/doi/10.1073/pnas.1323672111))
and a 2025 estimate of real-world sensitivity around **33%**
([Smit et al., 2025](https://journals.sagepub.com/doi/10.1177/21677026241305136)).
We ran the same detector inside the canonical $\mathcal{L}_\Omega$ dynamics
under slow κ-starvation and report exactly what we measured:

- the trend is **real but weak**: Kendall $\tau$(AC+var) $= 0.18 \pm 0.35$
  on ramp runs vs $-0.06 \pm 0.23$ on stationary controls; at the $\tau>0.5$
  threshold: **sensitivity 25%, specificity 100%** — matching the human
  numbers;
- three method findings surfaced on the way, each now part of the
  instrument: (a) the grey wall is a *moving attractor, not a fold* — the
  slowing is finite, so the detector reads "starvation underway", never
  "collapse imminent"; (b) **observable geometry matters**: purity is
  quadratic at its own floor and *silences* the warning deep under the wall
  — linear lenses (exactly the MUB readouts) keep the signal; (c) an
  *episode* is a sustained regime shift, not a daily dip — the crossing
  itself needs long averaging, the same distinction the EMA literature
  draws.

The app's EWS panel states these limits verbatim: a signal, never a verdict.

### 14. The rose ring (HB18)

The classic 6-bit Gray cycle, parity-extended to seven bits, flips exactly
two bits per step — a minimal-step Hamiltonian cycle on the even-weight
code: the **canonical rose ring** (64/64 minimal steps). Measured against
it, the King Wen wheel achieves the minimal step on **50 of 64** transitions
(12 steps of distance 4, 2 of distance 6): the traditional order is nearly
minimal in the code geometry — a structural compliment the tradition earns,
and a canonical alternative the reconstruction now owns.

### 15. In the application

The **Дневник** tab: lens selector (lens 0 = the seven voices; lenses 1–7 =
mixed states, marked as an experimental [И]-instrument), seven sliders, a
note, persistence to `~/.hhg_diary.json`; the posterior $\Gamma$ heatmap
with the shift-from-prior norm; the EWS panel with the measured sensitivity
limits quoted. Tests: unbiasedness, exact reconstruction on the calibration
chart's prior, the uniform-diary-is-grey identity.
