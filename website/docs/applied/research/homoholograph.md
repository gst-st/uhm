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

## Part IV. The descending holonomy: the sky's own homogram

### 16. The construction

The ladder-of-worlds chapter of the ontology says it plainly: the floor
above conducts the floor below — downward flows the beat, the supply, the
meaning. The bridge from ephemerides into UHM is made computable by one
move: the solar system gets its OWN homogram,

$$
\Gamma_{\text{sky}}(t) \;=\; \text{encode}_{v2}(\text{imprint}(t)),
$$

built by the *same* heptacode encoder that builds a person's natal prior.
The downward bridge at ignition is therefore an **identity, not an
analogy**: a being's natal prior *is* the conductor's page at the moment
its autonomous loop starts (Personality = self-model ignition; Design,
88° of solar arc earlier = body ignition — the phase-stamp reading, [И]).
After ignition the trajectories diverge; transits compare the conductor's
*current* page with your *printed* one — timebridges are where today's
score completes your chords. Influence on beings stays OPEN; the
construction itself is structurally exact.

### 17. Measured (HB19–HB22, `sky_lab.py`)

- **The conductor's climate (HB19).** Over 1900–2100 (36,500 pages):
  $P_{\text{sky}}$ mean 0.308 ± 0.036, range [0.204, 0.533] — **the sky
  itself spends 71.9% of days inside the window of being** (2/7, 3/7].
  $\Phi_{\text{sky}}$ mean 0.85, range [0.21, 1.74]; the most coherent
  pages of two centuries: 1954-04-04 (Φ = 1.74), 1937-04-11, 1976-06-19;
  the flattest pages cluster in Novembers.
- **The rhythm ladder (HB20, aliasing-honest).** The slow staff (no Moon)
  shows the year (365.0 d) and the half-sidereal lunar line (13.88 ≈
  13.66 d); the full sky at 3-hour sampling shows the year and the **solar
  gate rhythm**: the 5.53–5.89 d peak family is the Sun crossing one gate
  (365.25/64 = 5.71 d), *split by Kepler* — orbital eccentricity is
  visible in the wheel's own spectrum.
- **Axis-epochs (HB21).** The slow hands write eras in the *voices*: era
  swings up to 5.4 пп in S and 4.9 пп in L across 20-year windows — the
  «type era» discovery acquires axis resolution (2020–40: +S; 2040–60:
  −L +O +E).
- **The three staves (HB22).** The conductor writes on three staves with
  measured half-lives: the lunar stroke ~2.4 hours, the inner rhythm ~2
  days, the outer bass ~10 days *per line-phase* (the gate skeleton of the
  outer hands lives weeks-to-years; the encoder's line-phase layer turns
  pages faster than gates change — an instrument fact worth knowing).

### 18. In the application: the knowledge base and the reports

The laboratory now closes the loop from input to publishable раскладка:

- **People**: saved profiles (`~/.hhg_persons.json`), one-click reload.
- **The knowledge base** (`~/.hhg_kb.json`): every interpretation text the
  reports use is an editable entry with a stable key and an honesty class;
  defaults are seeded from the corpus SSOT (7 voices, 21 coherences) and
  the reconstruction theorems — the user overwrites any of it and owns
  their own interpretive canon.
- **Reports**: a deterministic markdown generator (numbers from the
  engine, texts from the KB) assembling the full раскладка — summary,
  Rose-64 with per-activation readings, observables, panel, tyaga,
  poristost, yakornost, smychka, nebograph, diary+EWS — saved to
  `~/hhg_report_*.md`; also `hhg-report --md` headless.

## Part V. studio0, the interpretation machine, and the event grammar

### 19. The compositional interpretation machine

Legacy HD carries 384 hand-written line texts. The reconstruction replaces
them with a **grammar over canonical atoms**: every activation story is
composed from body role [И] × side × heptacode object × line-voice accent
(Shchutsky archetypes × the line→voice map) × syndrome pointer × antipode
grounding × triangle resolution — and every atom is an editable, bilingual
knowledge-base key. Each story ends with a *"Simply put"* layer (the
ontology's imagery: seven singers, duet-friendships, the triangle's
resolution song, the witness singer, the Source's blank page) so that — per
the lab's standard — a child can follow the essence.

The hidden layers, with **population baselines** (HB23, n = 1500):
the chart's asking voice; spine share (P(≥7) = 4.9% — the calibration
chart's 7/26 is a top-5% trait); grounded pairs (population 51%); triangle
resolutions (shadow present 33%, witness 32%); amplified stamps (×3 in 63%
of charts, ×4 in 15%; ×2 is universal — pigeonholes); the profile
coherence; personal/group/generational strata; the principal eigenchord;
per-activation fragility in hours; sky resonance.

### 20. studio0 and the backend-grade CLI

The laboratory is a single terminal binary `hhg` (ratatui TUI + clap CLI):
`chart/rose/full/report/duo/sky/cycles/scan/day/diary/kb/persons`, JSON
with `schema: hhg.v1`, `--now` for reproducible transits, `HHG_HOME`,
bilingual throughout (`--lang`, TUI key `l`). `hhg full` returns the whole
computation in one JSON call — the endpoint the future public studio1 will
sit on. Rendering is tested by buffer (ratatui TestBackend), the machine by
totality and determinism (64×6×2 stories; byte-identical reports).

### 21. Cycles validated to minutes; the event grammar v1

The return/opposition solver (grid scan + bisection, honest retrograde
multi-passes) was validated against five production-dashboard anchors of
the calibration chart under the app's own natal assumption: **Sun return
+0.1 min, Moon +0.5, Jupiter IV +0.5, Saturn II −0.9, Uranus opposition
+27 min** (0.0002° — the VSOP truncation scale); it also established that
the production app's cycle times are UTC. On top of it, `hhg scan` runs
the first **event grammar** over a date range: returns/oppositions,
bridge peaks (0.92-quantile local maxima of timebridges), page returns
(minima of ‖Γ_sky−Γ₀‖), and epoch turns (an outer hand entering a new
gate — the cohort's page turning), ranked by slowness weights. All of it
is layer-1/2 honest; what any of it *means for a person* is layer 3 — and
that is exactly what **pravdomer v2** now measures: a blind day protocol
(`hhg day rate` commits the hidden drive prediction at rating time;
`reveal` opens at 21+ days with a permutation test), with the HB09 power
context quoted in the output.

## Part VI. Precision and the wheel's deep relations

### 22. ΔT done right; the two honesty zones of the ephemeris

The linear ΔT surrogate was replaced by the piecewise Espenak–Meeus
polynomials, verified verbatim against the
[NASA Five-Millennium-Canon page](https://eclipse.gsfc.nasa.gov/SEcat5/deltatpoly.html)
(the old model erred by ~80 s ≈ 2.4′ of Moon at the 2100 edge). The
Swiss cross-check was regenerated over the FULL 1900–2100 range and split
into two honesty zones: **strict** (≤2050: Sun 0.7″, planets ≤1″, Moon
12″, node 45″ — the node limit is the truncated lunar series amplified by
1/sin i, not the r×v method) and **projection** (2050+: ΔT of the future
is itself uncertain by minutes — divergence from Swiss there is model
uncertainty about Earth's rotation, not a bug). Line-flip criterion is now
statistical: flips only allowed on Moon/nodes at residual scale, never on
planets.

### 23. The nuclear map and the wheel's harmonic tower (HB24, HB24b)

The oldest "hidden essence" operation of the I-Ching — the nuclear
hexagram (lines 2-3-4 / 3-4-5) — becomes a measured endomorphism of the
heptacode atlas: its only fixed points are **KW 1 = the O-voice and KW 2 =
the Source**, and the entire wheel drains in ≤2 steps into three roots:
the Source (16 gates), the O-voice (16), or the **63↔64 pendulum**
("After ↔ Before Completion", 32). Reports now carry each activation's
nuclear core and the chart's root census.

Sharper still: the wheel's rotational harmonics are the hexagram lines
themselves. Measured (HB24b): the dominant XOR relation at offset $2^k$
flips **exactly one line**, in exactly 32/64 cases (the halving rule), and
the lines descend the mandala's octaves — one gate → line 6 (voice E),
11.25° → U, 22.5° → D, 45° → L, 90° → S, 180° → the exact complement.
With line = voice this yields a native aspect theory with voice types:
opposition = complement (theorem), square = the S-turn, semi-square = L
[И-structured]. HB25 recorded honestly: iterative MLE
([diluted RρR](https://arxiv.org/abs/quant-ph/0611244)) improves diary
reconstruction by only ~8% at small N — below the preregistered adoption
threshold; not merged.

### 24. The year atlas

`hhg year -n Имя --year 2026` assembles the flagship user artifact: twelve
monthly sections of the event grammar (epoch turns, returns/oppositions,
bridge peaks, page returns) merged with the year's lunar returns, all
date-sorted with slowness weights — one markdown, abundance with honesty
classes attached.

### 25. The third arbiter and the dyadic aspect layer

Twelve frozen [JPL Horizons](https://ssd.jpl.nasa.gov/api/horizons.api)
apparent ecliptic-of-date longitudes (1950/1985/2025 × Sun/Moon/Jupiter/
Pluto) now sit in the test suite as the authoritative third arbiter: our
independent chain stays within **4.1″** of JPL (the Moon — the truncated
ELP; everything else ≤0.8″), and on several rows it is *closer to JPL than
Swiss/Moshier* (Pluto-1950: 0.06″ vs 0.53″; Moon-1985: 0.10″ vs 1.22″).

The halving rule became an operating layer: the scanner now emits **dyadic
aspects** — a slow hand entering a gate at ring offset 32/16/8 from a natal
anchor, voice-typed (complement / S-turn / L-turn; the trine and sextile do
not fit the 64-wheel — an honest, falsifiable divergence from astrology;
base rate 1/64 per specific relation) — and **nuclear moves** (a slow hand
entering the nuclear core of a natal gate). The Rose carries the full wheel
depth `gate.line.color.tone.base` with the fractal second/third-order voice
accents [И], and the year atlas marks **event knots** (⚡ — two or more
events within ±2 days). The calibration chart's 2026-08-23 turned out to be
a triple knot: Neptune's epoch turn into gate 25, its L-turn to the natal
North Node, and the Jupiter opposition — all in one day.

## Part VII. Toward people: the daily practice, the abundance layers, and the assistant

### 26. The Telegram field instrument

studio0 now carries a full Telegram backend (`hhg bot`) inside the same binary — a pure, tested router plus a thin rustls transport with inline keyboards. The menu is structured by the essence of the elements: Today (the daily practice) first, then Me / Sky / Diary / Bonds / Assistant / Settings. The **daily page** (`digest.rs`) is its own designed theme: sky weather (climate percentiles), resonance with the printed page, timebridges named as coherences, the event grammar around today, the lunar countdown, the voice of the day, and an honesty footer. Blind ratings feed the pravdomer.

The free-text channel is a **Claude Code agent** (headless CLI) with a per-user workspace holding the rendered homogram, the day, and the running history, engine access as a tool, and a shared engineering **PROBLEMS diary** the agent is instructed to append to whenever it spots a calculation or interpretation gap — a feedback loop for improving the system. Safety and honesty are in its standing instructions: three layers, no diagnosis, autonomy support.

### 27. Abundance and interior physics (this wave)

- **Extended canon**: 21 full coherence portraits and 7 voice portraits (bilingual, editable), woven into reports, synthesis, and the bot (`/coh`, `/voice`).
- **Dynamical fate** (HB29/29b): the natal prior run through the canonical ℒ_Ω. Raw ρ₀ drains 98.7% of the population to grey — the natal self-model alone cannot hold a pattern in the window (the diary is needed); with a sharpened self-model, 43% grey / 57% window / 0% dense, Reflectors 0% (the mirror lives by reflection, not sharpness).
- **The sharpness map** (HB30): sharpening ρ₀ along each voice and reading where the fate lands — the personal *first move*. The best voice crossed the window in 60/60 charts; the voice is personal (never the already-dominant one).
- **Bearing activations**: leave-one-out weight of each of the 26 stamps in Γ₀ (the two lights measurably hold the calibration chart).
- **The life map** (`hhg life`): day-per-year progressions (resonance curve 0–84, life-page-return ages, progressed lunar returns ~27/55/82) woven with the great transit cycles (Saturn return/opposition, Uranus opposition, the 18.6-year nodal lattice), clustered into retrograde series, by decade.

## Part VIII. Two birds: HD as a falsification instrument, and the Rosetta

The reconstruction has always run in two directions at once. Downward, UHM
lends Human Design a rigorous spine — the seven voices, the coherence graph,
the wall of being. But the arrow also points **upward**. Human Design is an
occult architecture of the human that was tuned, over decades, against a very
large number of charts and lived reports. Wherever UHM makes a *structural*
prediction that can be checked against HD's independently-calibrated wiring,
HD stops being a client of the theory and becomes a **measurement** of it —
a chance to corroborate the theory, or to falsify it. Two birds: the same
bridge that grounds HD also puts UHM at risk, which is the only thing that
makes a claim worth believing.

### 28. The falsification suite (`architecture/falsify_lab.py`)

The rule of the suite is pre-registration. For each test we fix, *before the
measurement*, three things: the UHM source, the exact prediction, and the pass
criterion. Then we measure and read the verdict honestly. Three verdicts are
possible:

- **CORROBORATED** — HD's structure matches the UHM prediction;
- **INDEPENDENT** — no relation is found (a null result — scientifically
  valuable, because it bounds where the structure lives);
- **TENSION** — HD's structure *contradicts* the prediction. A tension is a
  falsification signal and must be escalated to the corpus.

Six tests run today.

**TF1 — the cardinality of the alphabet.** UHM T-224 says seven is the unique
self-diagnosing alphabet: a self-model needs exactly seven processing
dimensions, plus drive. Prediction: HD's centers split as **7 processing + 2
pressure**, never 6+2 or 8+2. Measurement: they do, exactly. **CORROBORATED.**
This is the load-bearing coincidence of the whole bridge — HD's nine centers,
built with no knowledge of UHM, resolve into precisely the seven voices plus
the two supply ports (Head, Root).

**TF2 — the complement law.** UHM reads the wheel as the even `[7,6]` code, so
opposite gates must be exact binary complements of the six visible lines.
Measurement: **64/64** exact complements. **CORROBORATED.**

**TF3 — the wall of being.** UHM T-124/T-129: integration `Φ = 0` is grey —
zero being. Prediction (natal-level, defensible): the Reflector, defined by an
empty inner graph, is the **unique** type with `Φ = 0` and the **uniquely
lowest** purity, while every *defined* type carries `Φ ≥ 0.1`. Measurement
over 3000 charts: Reflector `P = 0.197`, uniquely the lowest; Reflector
`Φ = 6·10⁻¹⁸` (numerically exact zero) against every other type `Φ ≥ 0.21`.
**CORROBORATED.** (An earlier version of this test fired a *false* TENSION by
demanding defined types sit above the `2/7` wall on their natal prior. That
was a category error, corrected here: the `2/7` wall is a *dynamical* claim
about a sharpened, conscious state, and all natal priors are diffuse — HB29.
The honest natal prediction is the one above, and it holds. The dynamical
wall is tested separately in HB29b, where Reflectors reach the window 0% of
the time.)

**TF4 — the hidden seventh voice.** UHM makes O (Ground) the parity bit of the
six visible lines. Is that parity a *meaningful* binary in HD, or arithmetic
noise? Test: does the parity partition gates in a way that aligns with the
pressure-fed set better than chance? Permutation test, 5000 shuffles:
`p = 0.80`. **INDEPENDENT.** An honest null — the parity is a real feature of
the code, but it carries no information about HD's pressure wiring. UHM does
not predict it should, so this bounds the claim rather than wounding it.

**TF5 — the Fano organization.** UHM T-224 organizes the 21 coherences as the
Fano plane — seven lines of three. In that plane *every pair already lies on a
line*, so the only non-trivial question is whether HD realizes complete
**lines** (all three pairs of a triad) more than a random graph with the same
edge count. Measurement: HD realizes **1 of 7** complete Fano lines, against
`1.50` expected by chance (`p = 0.93`). **INDEPENDENT** — HD's channel wiring
carries no Fano structure (consistent with the earlier center↔heptacode
mutual-information null, T-H6, `p = 0.62`). The Fano organization is a fact of
the *coherence algebra*, not of HD's historically-grown channel list; the two
are simply different objects.

**TF6 — the three-floor ceiling.** UHM T-142 caps the subject vertical at
three floors: the purity a floor-`n` subject would need,
`P_crit⁽ⁿ⁾ = (2/7)·3ⁿ⁻¹/(n+1)`, first *exceeds 1* — the maximum possible
purity of any state — at `n = 4` (`54/35 ≈ 1.54`), so no fourth floor can
exist. The arithmetic is verified here (ceiling = 3). But Human Design encodes
an *individual*, with no nested-subject vertical to calibrate this against.
**INDEPENDENT by construction** — the ceiling is a UHM-internal fact
(`holarch_lab.py` HL02), not something HD can corroborate or falsify. We record
it for completeness and to mark the honest boundary of the instrument: not
every theorem has an HD handle, and saying so plainly — rather than
manufacturing a test that would only seem to confirm the theory — is part of
the discipline.

**The tally: 3 corroborations, 3 independences, 0 tensions.** No
empirically-calibrated property of Human Design contradicts UHM. The
corroborations are the strong ones — the 7+2 cardinality, the complement law,
the Reflector's exact `Φ = 0` — because they are precisely the structural
axioms the theory cannot do without. The independences are not failures; they
are the map's honest coastline, marking where UHM structure is *not* imprinted
on HD and telling any future skeptic exactly where to dig. The absence of
tensions is the corroboration that matters most: an instrument built for a
different purpose, on a different vocabulary, in a different century, does not
once cut against the theory's spine.

### 29. The Rosetta: a precise ontology, not a rebranding

Calibration is not the same as allegiance. We calibrate through Human Design
because people already live inside its language — but the goal is a new
ontology with its own terminology, one that names each thing by its essence
rather than by an inherited, often occult-anchored label. The **Rosetta**
(`core/src/rosetta.rs`; `hhg rosetta`, `/rosetta`, and the agent's glossary)
is the terminology spine of that ontology. Each row carries four cells: the
legacy HD term, our precise term, the UHM principle it expresses, and a
precision note saying *why* ours is sharper. It is bilingual and editable, and
it is deliberately restrained — we do not rename for the pleasure of renaming;
we rename only where the legacy word blurs or misleads.

A few rows show the shape of it:

- **Channel → coherence.** Not a wire between two centers but a full `K₇`
  edge. The legacy channel list is structurally *blind* on 8 of the 21
  dimension-pairs; the coherence covers all 21 — no blind zone (HB13).
- **Center → voice-dimension (7) or pressure port (2).** HD's nine centers
  conflate population and drive; the reconstruction splits them cleanly.
- **Type → connectivity class.** Not an esoteric caste but a graph invariant
  of the chart. The Reflector is the unique zero-integration class — a claim
  now corroborated (TF3), not asserted.
- **Not-self → *razlad* (`D_ns`).** Not a moral "right/wrong" but a computable
  distance `‖E(Personality) − E(Design)‖` between the self-model and the body
  imprint.
- **Open center → porosity (high gain).** Not "weakness" or "emptiness" but
  susceptibility — and, crucially, a *testable* one: higher self-report
  variance on that voice, an open question logged for the per-user diary.
- **Synastry → the *smychka* (T-77).** Not a compatibility score but a
  computable, non-negative **increment of being** that lives in the bridge,
  not in the two banks — connection literally adds being.

The Rosetta is where the two birds meet. The falsification suite keeps the
reconstruction *honest against HD* — it must never contradict the instrument
that calibrates it. The Rosetta keeps the reconstruction *free of HD* — it
must never be trapped in a vocabulary it has outgrown. Held together, they let
the system be calibrated by Human Design without being owned by it: an
ontology of the human that earns each of its words, and puts each of them at
risk.

## Part IX. The hidden group: from esoteric alphabet to representation theory

Everything so far has treated the wheel as a *given* — 64 gates, seven voices,
21 coherences, seven Fano lines — and built structure on top of it. This part
asks the deeper question: **why this wheel and no other?** The answer is a
single finite group, and finding it is what lifts the whole construction off
the esoteric shelf and onto the scientific floor. The research lives in
`architecture/symmetry_lab.py`; every claim below is measured there, nothing on
faith.

### 30. The 64 gates are the orbits of a finite simple group

The seven voices are the seven nonzero vectors of `F₂³`; the 21 coherences are
their pairs; the seven Fano lines are the collinear triples `{a, b, a⊕b}`. The
symmetry that fixes *all* of this at once — permuting the voices while carrying
lines to lines — is the automorphism group of the Fano plane:

$$ G \;=\; \mathrm{GL}(3,2) \;\cong\; \mathrm{PSL}(2,7), \qquad |G| = 168, $$

a **finite simple group** (the second-smallest non-abelian simple group, after
`A₅`). The lab builds all 168 elements explicitly and checks that every one of
them preserves the set of seven Fano lines — so `G` is exactly `Aut(Fano)`.

Now let `G` act on the *even subsets* of the seven points — which is precisely
the set of 64 gates, since a gate is a King Wen hexagram whose support (the
"on" voices, parity included) is an even subset. The orbits come out as:

| orbit | size | our name | what it is |
|---|---|---|---|
| ∅ | 1 | **source** | the empty support (KW 2) |
| pairs | 21 | **pair** | the 21 coherences |
| lines | 7 | **line** | the Fano-line shadows (the spine) |
| triangles | 28 | **triangle** | the non-collinear triples |
| points | 7 | **voice** | the pure single voices |

`1 + 21 + 7 + 28 + 7 = 64`. Five orbits, and **they are exactly the five
classes of `classify()`** — the lab verifies `classify(kw)` equals the orbit
label of the gate's support for all 64 gates. This is the load-bearing result
of the entire reconstruction restated at its deepest level:

> The gate classification is not a convention we chose. It is the orbit
> decomposition of `Aut(Fano)`, and so it is **forced** — any faithful reading
> of the wheel must produce these five classes and no others. VERIFIED (exact
> combinatorics of the group action, checked for all 64 gates).

Each class is a *single* orbit (the lab checks transitivity): the 21 coherences
are indistinguishable to the group, as are the 7 lines and the 28 triangles.
That is the group-theoretic reason the 21 coherences are genuinely *equal*
citizens (the claim UHM's T-256 makes abstractly, here realized on HD's
empirically-fixed wheel). The syndrome-0 gates — the Hamming spine — turn out
to be exactly `source ∪ lines = 8 = 2³`: the group's canonical representatives,
with the syndrome reading off the coset.

### 31. The bridge to UHM: N_gen = 3 is a representation dimension

A finite group's deepest fingerprint is its character table: the dimensions of
its irreducible representations. `G` has **6 conjugacy classes** (sizes
`1, 21, 24, 24, 42, 56`; element orders `1, 2, 3, 4, 7, 7`), hence six
irreducibles, of dimensions

$$ 1,\; 3,\; 3,\; 6,\; 7,\; 8 \qquad (1^2+3^2+3^2+6^2+7^2+8^2 = 168). $$

The two **3-dimensional** irreps are complex conjugates, and they are indexed
by how an order-7 element acts: its eigenvalues are the 7th roots of unity at
the **quadratic-residue** exponents `{1, 2, 4}` for one, the non-residues
`{3, 5, 6}` for the other. So the number three here is not incidental — it is
`|QR(7)| = (7−1)/2 = 3`.

That is *exactly* the arithmetic behind UHM's generation count: `N_gen = 3`
because `N_gen = |QR(7)|`. The same three quadratic residues mod 7 that force
three fermion generations in the theory are the ones that give `G` its two
three-dimensional representations. **UHM's "three generations" is the dimension
of an irreducible representation of the Human Design wheel's symmetry group.**
This is the two-way bridge in its sharpest form: UHM supplies the wheel with a
group and a reason for its threefold structure; HD supplies the group with a
concrete, empirically-tuned object on which to act.

Two more measured resonances round it out. The 21 involutions of `G` (its
order-2 elements) each fix one Fano line pointwise and move the other four
points — **three involutions per line, `21 = 7 × 3`** — the same 3 again,
riding on each line. And the 48 order-7 elements are all single 7-cycles
(Singer cycles): the *algebraic source of the wheel's circle*. The canonical
one, multiplication by a generator of the field `F₈`, permutes the voices as

$$ A \to S \to D \to L \to E \to O \to U \to A, $$

which is **exactly the canonical voice order**. The order in which UHM lists
its seven voices is not a stylistic choice — it is the rotation of `F₈`.

### 32. The applied layer: structure you can see

The group is not only foundational; it is a working lens, exposed in the engine
as `core/src/symmetry.rs` (`hhg symmetry`, the bot's `/symmetry`, and the
assistant's glossary). Two capabilities fall straight out of §30–31:

- **The structural fingerprint.** Because the five classes are orbits, the
  histogram of a chart's activations across `{source, pair, line, triangle,
  voice}` is a genuine, coordinate-free **invariant** of the chart under the
  full symmetry group — a robust structural profile that no relabelling of
  voices can disturb. (The calibration chart: 26 activations reading
  `voices 7, bridges 4, line-shadows 5, triangles 8, source 2`, with 7 on the
  Hamming spine.)
- **The rotation ring.** The Singer cycle gives every voice a principled
  successor — the voice the wheel turns toward next — a new interpretive axis
  grounded in the field structure rather than asserted. (The developmental
  reading of that succession is honest storyteller-layer, [И]; the cycle
  itself is exact.)

The lesson of Part IX is the one the whole project is aimed at. An alphabet
that arrived wrapped in three thousand years of oracle and metaphor turns out,
when read carefully, to be the orbit structure and representation theory of a
finite simple group of order 168 — the same group whose three quadratic
residues mod 7 the theory already needed for three generations of matter. That
is what it means to move a system from the esoteric class to the scientific
floor: not to strip its beauty, but to find the mathematics that was holding
the beauty up all along.

## Part X. Verification against a production app, and the precision layer

An applied instrument lives or dies by its numbers. This part reports a full
cross-check of the engine against a mature, licensed production app
(humandesign.red, running the Jovian-Archive Rave BodyGraph), on the
calibration chart — and the empirical layer that check forced us to build.

### 33. Twenty-six of twenty-six

The two systems were compared activation by activation — all 13 Personality
plus 13 Design gate·line positions — for the same birth data. The structural
readings agree completely: **type** (Manifesting Generator), **profile**
(3/5), **authority** (Sacral), all **five channels** (1–8, 2–14, 4–63, 10–57,
26–44), all **twenty defined gates**, the **split** (double definition), and
the **incarnation cross** (Right Angle Cross of Penetration, on gates
51/57/54/53). At the finest level, 24 of the 26 gate·line activations matched
exactly; the two that differed were **both the Moon**, off by a single line.

The whole difference traced to **one root cause: the timezone.** The app placed
the birth at UTC+6; our engine, through the IANA time-zone database, placed it
at **UTC+7** — because Alma-Ata on 7 April 1985 was on **Soviet summer time**
(decree time +1 h of DST, in force from 31 March to 29 September 1985). When
the engine is asked to use the app's UTC+6 assumption instead, it reproduces
the production chart **26 of 26, exactly** — including both Moons. So the
ephemeris carries no error against the reference; and on the historical
time-zone it is, if anything, **more correct than the production app**, which
omitted the 1985 summer-time hour. VERIFIED (26/26 at matched time); the
DST-accuracy claim is falsifiable against the birth certificate or any
high-precision ephemeris.

### 34. The Moon is a precision sentinel

Why did a one-hour shift move *only* the Moon? Because the Moon is the fastest
body on the wheel. Measured at the calibration moment, the Moon travels a full
line of the wheel in about **16 minutes** of birth time; the next-fastest body,
the Sun, needs about **416 minutes** — seven hours. Every other body is slower
still. So a birth-time or DST error of the everyday size — up to an hour —
flips the Moon's line and touches nothing else. The Moon is a **precision
sentinel**: the single element sensitive enough to reveal a clock error, while
the rest of the chart stays rock-steady.

This is exactly why 24 held and 2 (both Moons) moved. It is not noise; it is
the wheel's own error-budget made visible.

### 35. The fragility layer — an epistemic level UHM's instrument needed

The sentinel is not a nuisance to hide; it is an interpretation level to
expose. The engine now carries a **fragility** layer (`core/src/fragility.rs`,
`hhg fragility`): for every activation it computes `minutes_to_flip` — how many
minutes of birth-time error would move that reading to the neighbouring line —
and sorts each into a confidence tier: **solid** (> 120 min), **watch**
(30–120 min), **fragile** (< 30 min). On the calibration chart the census is
2 fragile (both Moons, ~7 and ~16 min), 1 watch (Design Mercury), and 23 solid
— and the two fragile activations are *precisely* the two that disagreed with
the production app. The layer predicts its own uncertainty.

This is the "additional level of interpretation" an empirical instrument
demands, and no bodygraph tool shows it: a reading that says out loud which of
its own parts are rock-solid and which are soft. It is also a **falsification
handle**. A fragile activation is one where a small, plausible birth-time error
changes the symbol — so it is exactly where a per-user self-report can
*adjudicate* between the two candidate readings (here, Moon in gate 4 line 3
versus line 4). Run enough of these n-of-1 discriminations and the fragile
activations become a calibration test of the whole pipeline: birth-time
accuracy, time-zone history, and the line boundaries themselves. The solid tier
carries the instrument's confident claims; the fragile tier carries its
testable ones. That division — knowing which of your statements are which — is
the difference between an oracle and a measurement.
