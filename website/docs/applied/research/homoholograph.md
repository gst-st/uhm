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
exactly this). The center→dimension dictionary itself is an [I]-dictionary:
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

## 2. The bridge dictionary (an [I]-dictionary, structured)

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
   the [I]-dictionary becomes an empirical object.
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
[I]-dictionary on corpus names; influence on a person remains OPEN — the
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
mixed states, marked as an experimental [I]-instrument), seven sliders, a
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
88° of solar arc earlier = body ignition — the phase-stamp reading, [I]).
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
composed from body role [I] × side × heptacode object × line-voice accent
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
accents [I], and the year atlas marks **event knots** (⚡ — two or more
events within ±2 days). The calibration chart's 2026-08-23 turned out to be
a triple knot: Neptune's epoch turn into gate 25, its L-turn to the natal
North Node, and the Jupiter opposition — all in one day.

## Part VII. Toward people: the daily practice, the abundance layers, and the assistant

### 26. The Telegram field instrument

studio0 now carries a full Telegram backend (`hhg bot`) inside the same binary — a pure, tested router plus a thin rustls transport with inline keyboards. The menu is structured by the essence of the elements: Today (the daily practice) first, then Me / Sky / Diary / Bonds / Assistant / Settings. The **daily page** (`digest.rs`) is its own designed theme: sky weather (climate percentiles), resonance with the printed page, timebridges named as coherences, the event grammar around today, the lunar countdown, the voice of the day, and an honesty footer. Blind ratings feed the pravdomer.

The free-text channel is a **Claude Code agent** (headless CLI) with a per-user workspace holding the rendered homogram, the day, and the running history, engine access as a tool, and a shared engineering **PROBLEMS diary** the agent is instructed to append to whenever it spots a calculation or interpretation gap — a feedback loop for improving the system. Safety and honesty are in its standing instructions: three layers, no diagnosis, autonomy support.

### 27. Abundance and interior physics (this wave)

- **Extended canon**: 21 full coherence portraits and 7 voice portraits (bilingual, editable), woven into reports, synthesis, and the bot (`/coh`, `/voice`).
- **Dynamical fate** (HB29/29b): the natal prior run through the engine's evolution. Raw ρ₀ drains 98.7% of the population to grey — the natal self-model alone cannot hold a pattern in the window (the diary is needed); with the self-model sharpened to the *forced* window-top `P_upper = 3/7` (T-124, not a fitted constant), the fate is converged at 700 ticks (drift `<3·10⁻⁵`) and lands ≈ 10% grey / 90% window / 0% dense (re-measured 2026-07-28; 12/88 before the defaults were corrected), Reflectors 0% (the mirror lives by reflection, not sharpness). VERIFIED (`core/examples/dynamical_fate_audit.rs`). Honest classification after the canonical audit below: this layer runs on the *phenomenological* tick (ad-hoc κ, no gate) and is a construction-layer heuristic — a sharpness indicator, not the forced fate.
- **The canonical ℒ_Ω, implemented and confronted** (`holon::tick_canon`): regeneration with every Γ-dependent factor in its [T]-forced form — the structural rate `κ̂₀ = |γ_OE||γ_OU|/γ_OO`, the V-preservation gate `g_V(P) = clamp(7P−2, 0, 1)` (with `P_opt = 3/7` from `R ≥ 1/3`), the unique CPTP direction `(ρ*−Γ)`; only the flux scale `ω₀` (the energy supply `E` in `ℛ[Γ,E]`) is environmental. Three verified structural facts. (a) **The wall is absorbing**: a sub-wall state drains grey at *any* flux — the gate is shut — where the phenomenological tick tunnels through the wall, a theory violation the engine now names in its own docs. (b) **No inert class**: every natal chart carries `κ̂₀ > 0` (median ≈ 0.01) — the O-channels (Immanence, Completeness) are universally present, and they are the conduits self-regeneration flows through. (c) **The purity-production law** `dP/dt ∝ Tr[Γρ*] − P` makes the fate protocol's distant sharpened target *unreachable*: the natal prior collapses through the wall at every flux tried (100% grey up to `ω₀ = 10⁴`), and even the self-aligned window-top blend is overlap-diluted below `P` on about half the charts (112/200 positive), with only ≈40% crossing at extreme flux (`ω₀ = 10³`). And (d) **the full iterative scheme closes the question**: running the corpus's own Ψ-iteration (ρ⁽⁰⁾ = I/7; evolve the natal Γ₀ under the gated dynamics with the target held fixed; rebuild the self-model as the replacement form `φ(Γ) = (1−k)Γ + k·ρ_P` anchored at the chart's Personality-side encoding; repeat) converges in ~2 iterations to **grey for every chart** at every tested `(ω₀, k)` — because a diffuse state (P ≈ 0.30) has overlap ≈ 1/7 with *any* distinct target, so every fixed natal-constructed self-model is overlap-negative (measured: 0/150 positive anchors). Together these *derive* HB29's empirical "the natal self-model alone cannot hold the window" from the forced mechanism — gate + structural rate + overlap law — and sharpen it into a statement of scope: **under the forced ℒ_Ω the window is a driven regime, not a natal fixed point.** The natal chart's prognostic content is structural — which voices, which coherences, the person's geometry; dynamics belongs to the living layer (transits, the diary, external flux actually entering the state), which is exactly where the engine's prognostics live. VERIFIED (`core/examples/canonical_tick.rs`, `canon_fate.rs`, `canon_attractor.rs`; `holon::tests`).
- **The driven regime: the self-anchor law and the holding threshold `ω₀*`.** Modelling the drive (a year of real ephemeris under the gated canonical tick, one time-unit per day; the driven-target model is a construction [I] on the forced components): (e) the *only* regeneration target that survives the overlap law is the chart's **own natal print** — the self-coincident anchor holds a growing fraction of chart-days as flux rises (16.7% at `ω₀ = 10³`, 41.7% at `3·10³`) and always **inside** the window, never above it: self-maintenance cannot produce crystal. Mixing the sky into the *target* (the composite natal∪sky encoding) is overlap-negative and drains everything — real sky and scrambled sky alike — so the sky's role in `ℛ[Γ,E]` is not to redefine the self-model. The second natural coupling — the sky as a daily CPTP kick on the *state*, `Γ ← (1−ε)Γ + ε·ρ_comp(day)` — is **also null**: it rescues nothing below the threshold, mildly erodes holding above it (a diffuse admixture is entropy-increasing; real ≈ scrambled), and produces no `P`-weather (`⟨r(P, timebridges)⟩ ≈ −0.03`). Both natural couplings of the astronomical layer into the forced dynamics are null/negative — stated as a bound: the daily-page "weather" remains an interpretive [I] layer, not derived from `ℒ_Ω`; the untried couplings (the sky as a flux schedule `ω₀(t)`, or as a perturbation of `H_eff`) stay open and will not be multiplied without independent motivation (VERIFIED, `core/examples/canon_sky_kick.rs`). (f) Each chart then carries a canonical scalar: the **holding threshold `ω₀*`** — the minimum living flux at which self-regeneration toward one's own form balances dissipation. Across charts it spans `264 → 19231` (~70-fold: individuality is large under the forced dynamics), and it obeys a law: `ρ_Spearman(ω₀*, 1/(κ̂₀·(P₀−2/7))) = 0.92` — the threshold is set by O-channel conductance times the natal margin above the wall, with the compensated product `κ̂₀·g_V(P₀)·ω₀*` clustering at ≈ 7–20. A quarter of charts form the **never-class** (cannot hold at any tested flux), decomposing exactly into {sub-wall natal `P` — Reflector-like} ∪ {near-dead O-channels, `κ̂₀ ≲ 0.005`}: they live by reflection and environment, not self-regeneration. Read plainly: *"be your own form" is dynamically forced, and `ω₀*` is the cost of holding it.* VERIFIED (`core/examples/canon_driven.rs`, `canon_threshold.rs`, `canon_threshold_author.rs`). And the conductance has a *bodygraph address* — **the gates of holding**: the eleven King Wen gates whose canonical object feeds `γ_OE`/`γ_OU` (`5,23,28,34,49,58` / `8,26,30,34,38,50`). KW 34 — HD's "Power of the Great" — is the unique **double** conductor (the `EOU` triangle); the two pure pairs, 23 «Immanence» and 8 «Completeness», both sit on the Throat; and two of the seven Fano-line gates (28, and 30 — the `S–O–U` spine line itself) are holding-gates. The layer ships as a reading: the analytic tier classifier from the threshold law (`ω̂₀* = 12/x`, population-quartile cutoffs; the low tier phrased "costly", never "impossible" — the analytic never-criterion has perfect precision but imperfect recall) behind `/form`, `hhg form`, and the agent's `form` tool. VERIFIED (`core/examples/form_layer.rs`; `core/src/form.rs`). Two relational corollaries close the layer. Of HD's thirty-six channels exactly **one** has both gates in the holding set — **28–38, the Channel of Struggle**: the wire the lore ties to perseverance and fighting for meaning is, in the reconstruction, the bodygraph's only two-ended conductor of self-holding. And the **pair field** (the union encoding of two charts) raises the holding conductance above the *better* individual in 54% of random pairs and above the weaker one in another 32% — "next to another person it is cheaper to be yourself" is the statistical norm (86%), with only 14% of pairs pricing holding up; shipped in `/duo` as «Форма вместе» with the holder asymmetry (who brings more of the eleven gates). VERIFIED (`core/examples/form_duo.rs`). Scaling up completes the picture — and falsified the dilution guess in an instructive way: the union field's purity *rises* with group size (repeated gates add coherently; the gate factor climbs 0.23→0.50), so the field's conductance grows and saturates (~N = 7) with no interior peak — but its advantage over the **best member** decays, 52% at N = 2 down to 33% at N = 10 (the strongest of N grows faster than the saturating field). Small circles most often out-hold even their strongest; in larger groups the strongest holder out-holds the shared field — `/group` now names that holder (⚓) and warns, plainly, that an unreplenished holder buckles first and the circle sags with them. VERIFIED (`core/examples/form_group.rs`). The layer's *temporal* dimension closes it: the composite (natal∪sky) field's conductance `x_comp(t)` swings from **interference zeros** — the sky's phase contributions destructively cancel the natal O-channels, the priciest days — to ~16× the natal baseline when a transit stands on a holding-gate (the author's peak: Moon→23). The honest reading is therefore *windows*, not a smooth curve: `/form` now ends with «Окна формы» — dated cheaper-windows with their named drivers (e.g. `NNode→30`, the Node standing on the `S–O–U` spine-line gate) and pricier ones without (interference has no single driver). VERIFIED (`core/examples/form_windows.rs`). The same interference lives *inside* the natal chart itself, through the **lines**: a gate.line feeds its coherences with phase `θ = π·line/3`, so two holding-gates whose lines stand three apart cancel as vectors — exactly, at equal weights. Population-wide this is a first-order effect: **34% of feeding charts carry a strongly muted O-channel** (alignment `|Σv|/Σ|v| < 0.35`), and the never-class decomposes honestly into thirds — sub-wall mirrors, line-muted (one member holds four holding-gates at OE alignment `0.00`), and simply weak. The reading now says it plainly when it applies — «Приглушённый канал: как два голоса, поющие друг против друга; разводите наполняющие занятия по времени» — and the author's own OE channel turns out muted at `0.33`. VERIFIED (`core/examples/form_lines.rs`). Generalized to all twenty-one coherences, the interference becomes **the tuning map**: muting is *uniform* across pairs (16–22% of feeders — an honest null: the Fano structure privileges none), a typical chart carries three muted strings (p75 = 5), and the reading ships as «🎼 Строй карты» — clear strings versus muted, by their canonical names, with the one practice («приглушённая струна — не слабость: сила есть, звучит тише; тише ≠ слабее»). The author's tuning: nineteen fed, three muted (LU, DO, EO), six perfectly clear. VERIFIED (`core/examples/tuning_map.rs`). And the tuning has a *measured floor*: asking whether the wheel's **color** layer carries any non-astronomical phase structure (real charts vs a uniform-color Monte-Carlo null), the raw deviation (+0.030) turns out to be *entirely* the deterministic mirrors — Earth sits exactly `180°` from the Sun and the South Node from the North, and `180°` is exactly 32 gates, so their line/color/tone are identical; mirror-free, real ≡ null to four decimals (`Δ +0.0004`). **The tuning stops at the lines** — the color layer is astronomy, not structure, and no deeper "string map" may be sold as one; the И-fractal reading keeps its [I] charm with its scope now measured. VERIFIED (`core/examples/color_null.rs`). Relationally the tuning obeys a sharply **asymmetric law**: pooling two charts' phases practically never *re*-tunes a muted string (0% at the strict threshold — the partner's vectors would have to cancel an existing misalignment exactly) but **mutes at least one clear string in 96% of pairs** (mean 3.1). Set beside the conductance result (86% of pairs cheaper overall), the honest relational picture is a trade: the shared field lowers the total cost of being yourself while damping specific personal strings — and those muted-by-pair strings are precisely **the map of the personal**: what to do apart, each your own. Shipped as «🎼 Строй пары» in `/duo` and the circle version in `/group`; the daily page now also carries **form weather** (cheaper/pricier to be yourself today, from the day's composite conductance). VERIFIED (`core/examples/tuning_duo.rs`).
- **The sharpness map** (HB30): sharpening ρ₀ along each voice and reading where the fate lands — the personal *first move*. The best voice crossed the window in 60/60 charts; the voice is personal (never the already-dominant one).
- **Bearing activations**: leave-one-out weight of each of the 26 stamps in Γ₀ (the two lights measurably hold the calibration chart).
- **The life map** (`hhg life`): day-per-year progressions (resonance curve 0–84, life-page-return ages, progressed lunar returns ~27/55/82) woven with the great transit cycles (Saturn return/opposition, Uranus opposition, the 18.6-year nodal lattice), clustered into retrograde series, by decade.
- **The growth-gradient of integration** (the `/grow` reading): strengthen one coherence by a fixed step, re-project to a valid Γ, and read the change in integration `Φ` — the sign flips with the string's *own* strength. Worked (the calibration chart 1985-04-07, `Φ₀ = 1.031`): the two strongest strings AD (`ΔΦ = +0.011`) and OU (`+0.005`) **raise** Φ; the two weakest AU (`−0.043`) and SO (`−0.040`) **lower** it. Integration is load-bearing on the strong strings; strengthening a thin one adds a competing binding that fragments before it gathers — the honest **integration↔differentiation trade-off** (`Φ ≥ 1` and `D ≥ 2` are *both* consciousness gates, T-129/T-151). So the growth reading no longer sells "develop your weakest link" as a free win: each edge now carries its real Φ-effect — «gathers you tighter» (ΔΦ > 0) versus «broadens you — yet loosens the knot, in small doses» (ΔΦ < 0). Corollary for self-work: raising integration and widening differentiation pull opposite ways on the same string, so growth is a *balance* held over seasons, not a monotone climb. VERIFIED (`core/src/growth.rs::phi_lever`, `phi_lever_valid_and_fires_both_ways`; numbers regenerate via `corpus_phi_d_numbers`).

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
  reading of that succession is honest storyteller-layer, [I]; the cycle
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

The same honesty now extends *down the wheel's depth*. Each sublayer (line →
color → tone) is a six-fold finer arc, so the knowability question sharpens
with depth, and the exact per-activation answer (recompute at `±2` minutes and
watch what flips) is stark: **the Moon's tone flips in 100% of charts** —
practically undeterminable at realistic birth-time precision — its color is
fragile in 28%, the Sun/Mercury/Venus tones in 10–18%, while Jupiter and
Saturn are solid at every depth; the fifth layer (the base) completes the
verdict — it flips for the Moon in 100% of charts, Mercury 73%, Sun/Venus
54–58%, Mars 30%, and only Jupiter (7%) and Saturn (2%) hold it. The report's wheel-depth lines
(`gate.line.color.tone.base`) now carry an `≈` on any sublayer that flips
within `±2` minutes, with the footnote naming the bound — the И-fractal
reading keeps its charm and acquires its error bars. VERIFIED
(`core/examples/depth_knowability.rs`).

## Part XI. One mechanism, three vocabularies: UHM, active inference, and HD

The reconstruction has, until now, bridged HD to UHM. This part widens the
bridge to a third pillar — the **free-energy / active-inference** account of
mind (Friston and successors), the leading computational theory of how a
self-organizing system perceives and acts. The claim is not that Human Design
is validated psychology. It is sharper and stranger: **UHM's machinery and
active inference are the same machinery**, and HD's own open/defined centers
land exactly where active inference would place high and low sensory precision.
Three vocabularies, one mechanism — and where they meet, each supplies a level
the others lacked. The research is `architecture/psyche_lab.py`.

### 36. The identification

Active inference says a mind is a **generative model** that predicts its
sensory stream and acts to minimize the mismatch (variational free energy),
weighting each channel by its **precision**. Set that beside UHM's encoder and
the correspondence is not analogy but identity of role:

| UHM | active inference | Human Design |
|---|---|---|
| self-model $\rho_0 = E(\text{Personality})$ | the generative model | Personality (conscious) |
| body imprint $\mathrm{body}_0 = E(\text{Design})$ | the sensory stream / body | Design (unconscious) |
| poristost (filter gain) | precision $\pi$ | open vs defined center |
| open center = high gain | low prior precision ⇒ samples the world | conditioning by environment |
| razlad $D_{ns}=\lVert\rho_0-\mathrm{body}_0\rVert$ | prediction error / free energy $F$ | "the mind is not the authority" |
| the filter layer (belief update) | active inference ($\min F$) | strategy / experiment |

The first five rows are **structural identifications** — true by construction
of the mapping, not empirical claims. The reading they produce: a person's
*open* dimensions are the ones where their prior is loose, so they **sample and
amplify the world** there (and those readings vary most day to day); their
*defined* dimensions are steady **sources**. razlad becomes a computable
free-energy proxy — the felt size of the mind↔body gap.

### 37. The chart agrees with itself (verification)

Here is the sharp part. Active inference, given only UHM's gain map, predicts
which dimensions a person samples the world through. Human Design, by an
entirely separate doctrine (which centers are open), says the same thing. On
the calibration chart they **coincide**: the one high-gain dimension the
active-inference reading flags is **Interiority** (E) — and the one open center
in the bodygraph is the Solar Plexus, the emotional center, which HD reads as
"takes in and amplifies the emotions of the room." Two independent mechanisms,
built for different purposes, point to the *same single dimension*. VERIFIED (a
computed agreement on the chart); the razlad value (0.542) matches the engine's
own to four figures. This is the bridge corroborating itself on real data.

### 38. The trait dictionary, and honest limits

A second science of human nature — trait psychology — gives an *axial*
dictionary, each voice touching a well-validated construct: Articulation ↔
assertive expression (extraversion's agency); Structure ↔ conscientious order
plus threat-vigilance (BIS); Dynamics ↔ behavioural drive (BAS); Logic ↔
openness/need-for-coherence; Interiority ↔ affective sensitivity and empathy
(neuroticism's core); Ground ↔ dependability and care; Unity ↔ attachment and
identity coherence. This is deliberately **not** a 7→5 reduction to the Big
Five. The Big Five is itself neither orthogonal nor fundamental — it is a
factor-analytic summary of adjectives. UHM's seven-voice basis is
theorem-forced (T-224), so the arrow runs the other way: the voices are the
principled basis, and the trait constructs are shadows each casts onto an
established instrument. [I], and explicitly not validated on population data.

### 39. The new level, and what it puts at risk

Each field donates a level. Active inference gives UHM a *name and a dynamics*
for razlad (free energy) and reframes the window of being as **precision
control** — being neither too rigid (over-precise prior) nor too diffuse
(under-precise). UHM gives active inference a *non-arbitrary basis*: not a
grab-bag of traits but seven theorem-forced voices to carry the precision
profile. HD gives both an *empirical marking* — the open/defined centers are a
ready map of where a given person's sensory precision is high or low.

That map is now a reading in the engine (`core/src/psyche.rs`, `hhg psyche`,
the bot's `/psyche`): it names a person's sensing channels and steady sources
and states their mind↔body alignment, all in plain language. And it comes with
falsifiable predictions, each testable by one person through the blind n-of-1
diary:

- **P1 [OPEN]** sampler dimensions show *higher* self-report variance than
  source dimensions (high gain = high process noise);
- **P2 [OPEN]** high-razlad days track a felt "not-quite-myself" (free energy
  as experienced misalignment);
- **P3 [OPEN]** a person with an open emotional center has mood that tracks
  their company more than a person with a defined one.

If the diary contradicts these, the bridge is wrong where it is checkable —
which is exactly what an applied instrument built on empirical ground should
offer. The three vocabularies agree on the mechanism; the predictions are where
that agreement is put at risk.

### 40. A second bridge: the window of being is the window of tolerance

The same move works on UHM's **window of being**, `2/7 < P ≤ 3/7`. In clinical
terms this is the **window of tolerance** (Siegel): the arousal band between
shutdown and overwhelm where a person can *both* feel and think and stay
integrated. The three purity regimes map onto the three autonomic zones exactly:
below the wall (`P ≤ 2/7`) the state is maximally mixed — foggy, distant,
under-aroused (hypoarousal); inside the window it is flexible and coherent (the
window of tolerance); above it (`P > 3/7`) it is over-pure — locked in one mode,
rigid, over-aroused (hyperarousal). The calibration chart's `P = 0.309` sits in
the window. This gives the window of being a clinical name and, more usefully, a
set of **self-regulation cues** the engine now reads back (`psyche.rs
zone_gloss`, in `/psyche`): to lift from the fog, gentle activation (movement,
rhythm, voice, eye contact); to ease down from overwhelm, slowing (a long
out-breath, warmth, feet on the ground). The threshold is computed; the zone is
read; the practice is borrowed from a validated clinical frame. [I]

### 41. A third bridge: attachment into the relational layer

The relational machinery — synastry (T-77), the composite, the centered states
— has been waiting for its science, and attachment theory (Bowlby, Ainsworth;
the adult anxiety/avoidance dimensions) is it. Attachment is about how a person
regulates the two pulls of a bond: toward closeness and toward autonomy. UHM
already carries both poles. The **U (Unity/belonging)** and **E
(Interiority/affect)** axes are exactly where a person is joined to others, and
their filter gain says how much those axes *sample* the other. An **open**
belonging axis means the person's mood or sense of self tracks the bond — the
substrate of attachment **anxiety**; a **defined**, self-sourced one means
autonomy comes easily — the substrate of security-or-avoidance. And the
**smychka** (the electromagnetic channels a pair completes that neither had
alone) is the **secure-base function** made computable: how much new wholeness
the bond *creates*.

On the calibration chart this reads cleanly and specifically. The one open
belonging axis is **E** (the open Solar Plexus) and **U is defined** — so the
reading is *affect-porous but identity-steady*: "a loved one's mood easily
becomes yours, but closeness does not dissolve your «I»." That is neither the
anxious pole (where identity, too, would track the bond) nor the avoidant
(where affect would be walled off) — a secure-leaning texture with high
empathy. VERIFIED as a computed reading of the chart; whether it matches the
lived pattern is the [OPEN] question the diary answers.

Two readings now live in the engine (`core/src/attachment.rs`):

- **Solo** (`/psyche`) — the bonding tendency from the openness of the two
  belonging axes: porous or self-sourced in feeling, leaning-on-the-bond or
  steady in identity, with the honest coda that *healthy closeness is two whole
  people side by side, not one shared between two*.
- **Dyadic** (`/duo`) — from the synastry: how much wholeness the bond
  **completes** (the secure base, "we're more together"), how **balanced** the
  giving is (mutual vs "one pulls, the other leans"), and how **integrated** the
  pair is as a whole.

The discipline is the same as everywhere in this program: this is a **prior, a
tendency, never a diagnosis**. Attachment is a learned working model, and
observation always outranks nativity — the chart says where the pulls might sit,
the life says where they are. But the mapping is precise where it is checkable,
and that is what lets a bridge carry weight: the open belonging axis, the
completion count, the balance of giving are all exact, and each turns into a
question a person can actually answer about their own bonds.

### 42. A fourth bridge: the inner family (Internal Family Systems)

The last three bridges read the chart's dynamics and its bonds; this one reads
its *interior* as a system. Internal Family Systems (Schwartz) sees a person not
as a single will but as a family of **parts**, each with a job and a positive
intent, ideally led by a calm, curious **Self**. The mapping is almost too
natural: the seven voices *are* the parts; a voice's population (the Γ diagonal)
is how much internal airtime it gets; and the window of being is the capacity
for **Self-leadership** — the integrated centre that can hear every part without
one seizing the wheel.

The reading (`core/src/parts.rs`, `/parts`) names three things. The **loudest**
part — the voice with the most population, the "manager" that tends to speak for
you. The **quietest** — the voice heard least, which in IFS is often an "exile"
carrying something tender. And the **Self-leadership state** from the arousal
zone: inside the window, a calm centre can hold all the parts; below it they
blur into fog; above it one has grabbed the wheel.

On the calibration chart this produces a reading of unusual coherence *across*
the bridges. The loudest part is **Expression** (A, population 0.206); the
quietest is **Feeling** (E, 0.096) — which is *also* the one open center. So a
special note fires: the part heard least inside is the most exposed outside. In
plain terms — your Feeling is easily drowned out by the louder Expression that
speaks for you, yet it is the very channel through which you catch the room's
weather; it carries a lot and deserves the mic first. That single sentence is
built from three independent readings agreeing — the population (parts), the
gain map (active inference), and the open center (HD) — which is exactly the
kind of convergence a layered instrument should produce. VERIFIED as a computed
reading; [I] as an interpretation; and, like every reading here, a *prior* the
diary can confirm or overturn.

### 43. The portrait: the layers composed

Each reading so far is a single lens. The **portrait** (`core/src/portrait.rs`,
`/portrait`, and the accessible `/me`) is the composed picture — one flowing,
jargon-free paragraph woven from every layer at once: the type as a life-rhythm,
the inner family of parts (loudest and quietest), how the world comes in (the
sensing channels), the arousal zone, and the bonding tendency, closed by an
honest coda — *this is a map, not a cage; your life has the last word.* It does
not concatenate the five full readings (that would be a wall of text); it pulls
each one's key finding and stitches them with connective prose, so it reads as a
paragraph about a person. On the calibration chart the composition is what makes
the convergence visible in plain language: Feeling arrives as the quietest part
*and* the channel through which the world comes in — the same thread the parts,
the gain map, and the open center each surfaced, now said once, warmly, as a
single sentence. This is the architecture paying off: many rigorous layers,
one human read.

### 44. Closing the loop: the n-of-1 self-test

Every bridge so far ends in a prediction the diary could check; this is the
diary. Prediction **P1** — that a person's *sampler* dimensions (open centers,
high gain) should swing more, day to day, than their *source* dimensions —
is now a live test on the user's own data (`core/src/selftest.rs`,
`/checkin`). Each day the person rates all seven voices 0–10; after about two
weeks the engine compares the average day-to-day variance of the sampler voices
to the source voices and says, plainly, whether P1 **holds so far on their
data**. A null or a reversal is not a bug to hide but a *result*: an honest
signal against the model, which is exactly what the diary is for. This is the
whole program's stance made operational — the readings are priors, the diary is
the judge, and the instrument is built to be told it is wrong. With this, the
"two birds" close: Human Design calibrates the engine, the engine's structure
corroborates UHM (Part VIII), and the engine's own predictions are handed back
to the one person who can falsify them — turning a self-portrait into an
experiment.

### 45. Verifying the interpretations, not just the numbers

Part X verified the *numbers* — 26/26 gate·lines against the production app.
But the readings are only as trustworthy as the interpretations built on them,
so those were audited too, on three layers (`architecture/interp_verify.py`;
the QA gate lives in the engine's tests).

**Structural — the foundation.** Every reading (psyche, attachment, parts, the
portrait) rests on a handful of derived facts: the type, the authority, the
profile, and — most load-bearing — which centers are *defined* vs *open*. All of
these match humandesign.red exactly: Manifesting Generator, Sacral, 3/5, **seven
defined centers**, and the **Solar Plexus open**. That last one is decisive: the
one open processing center maps to the sampler voice **E**, which is the hinge
of the whole layered reading (E is the quiet-yet-porous part, the affect-porous
attachment axis, the sensing channel). Because the site agrees the emotional
center is undefined, the foundation of the readings is correct, not asserted.

**Essence — the meaning.** The app also carries the authoritative HD text (the
Ra-Uru-Hu / Bunnell lineage) for each facet of the chart, opened by clicking it.
We pulled the descriptions for all four load-bearing facets and cross-checked
each against our accessible content — **thirteen of thirteen key claims
reflected**:

- *Open Solar Plexus (voice E)*: it absorbs and amplifies the emotions around
  it; those emotions are not always one's own; one rides others' emotional
  waves — matched by the E voice, the `/psyche` sampler line, the `/duo`
  attachment reading, and the people-pleasing topic.
- *Manifesting Generator*: wait and respond rather than initiate (else
  frustration); a motor-to-throat that jumps from response to action fast; and
  the signature trap — *skips steps and must loop back, so slowing down helps* —
  which our type reading states almost verbatim.
- *Sacral authority*: the gut yes/no in the moment; the head talks you into
  things, the body is reliable.
- *Profile 3/5*: the 3rd line's trial-and-error discovery; the 5th line's being
  projected upon as a practical savior.

None of it is a copy: ours is a warmer, more actionable ontology in its own
words. The point is consistency of *meaning* with the established lineage across
every major facet — the strongest correctness check available short of
longitudinal human data (which the `/checkin` self-test now gathers). A
permanent test (`content_reflects_authoritative_hd_claims`) locks each of these
in, so a rewrite that drops the essence fails the build.

**Completeness — the gate.** A permanent test
(`full_completeness_and_parity_audit`) walks all 500-plus interpretation
fragments and fails the build on any empty fragment, any machinery term leaking
into the accessible register, or any break in ru⟺en bilingual parity. Coverage
today: 0 problems. The instrument's interpretations are now guarded the same way
its astronomy is — verified against an external reference, checked for meaning,
and gated for completeness.

## Part XII. The architecture, categorically: three guarantees

A reconstruction of the human should not merely *work*; it should come with
guarantees about *why* its structure is the structure and not an accident. This
part supplies three, each a standard theorem of category theory or group theory
applied to the reconstruction's own objects, and each verified by direct
computation (`architecture/category_lab.py`). The move throughout is the same:
name the categorical object the architecture already *is*, and let its universal
property do the guaranteeing.

### 46. The classification is canonical (a colimit)

Take the group `G = PSL(2,7)` (Part IX) acting on `X`, the 64 gates (the even
subsets of the seven points). Form the **action groupoid** `G ⋉ X`: its objects
are the gates, and there is an arrow `x → g·x` for every group element. The
*connected components* of this groupoid — its `π₀` — are exactly the orbits, and
`π₀ = 5`, with sizes `1, 7, 7, 21, 28`: source, voices, lines, pairs, triangles.
Equivalently, the quotient `X/G` is the **coequalizer** of the two maps
`G × X ⇉ X` (act, project) — a *colimit* in the category of sets. The
computation confirms every step: orbit–stabilizer holds exactly
(`|orbit| · |Stab| = 168` for all five classes), and Burnside's count gives
`(1/|G|) Σ_g |Fix(g)| = 840/168 = 5.000`, the number of classes.

The guarantee is what a colimit buys: **colimits are unique up to unique
isomorphism.** So the five classes are not a modelling choice that could have
gone another way — they are forced by the group action, canonical. And because a
chart's orbit-fingerprint (how its activations distribute over the five classes)
is a function of `X` that is constant on orbits, it *factors through* `X/G` — it
is a coordinate-free invariant of the architecture, blind to any relabelling of
the voices. VERIFIED (the colimit and its invariants are computed facts;
cf. T-256 for the underlying group).

### 47. The self-model exists (a fixed point)

The load-bearing claim of any self-describing system is that it *has* a self —
a stable internal representation of itself, the "I". UHM writes this as the
fixed point `ρ* = φ(Γ)` of the self-observation map. Here is why it must exist.
The state space `D(ℂ⁷)` — density operators on seven dimensions — is **compact**
(closed and bounded) and **convex**. Any *continuous* self-observation map
`φ: D(ℂ⁷) → D(ℂ⁷)` therefore has a fixed point by **Brouwer's theorem**:
`ρ* = φ(ρ*)`. Its categorical shadow is **Lawvere's fixed-point theorem** — the
same diagonal argument that forces the corpus's SPINE — which says that in a
cartesian-closed setting a point-surjective `A → A^A` makes *every* endomap have
a fixed point. Either way, the conclusion is a guarantee, not a hope: **a
self-referential architecture on a compact convex state space cannot fail to
have a stable self-model.** The lab demonstrates it concretely — iterating a
self-observation channel from four random starting states converges to the same
`ρ*` with residual `‖φ(ρ*) − ρ*‖ ≈ 10⁻¹²`. The "I" is not assumed; it is
theorem. VERIFIED (existence is Brouwer/Lawvere; the demonstration is computed).

### 48. Unions have a universal shared state (a colimit)

When people join — a couple, a family, a team — is there really a "we", or only
a heap of "I"s? The meta-holon (H65) answers categorically. Each member's
*centered* state `D_i = Γ_i − I/7` is their commitment (their deviation from
grey). The group's shared state is grey plus the mean of those commitments,
projected back onto the state cone: the **coproduct** of the members'
directions, coequalized into a single state. Its universal property is exactly
that of a colimit: it is the unique state that receives every member's
commitment through the canonical cocone, and the cocone is symmetric under
relabelling the members (verified), so the colimit is well-defined. The "we" is
therefore guaranteed to exist and to be unique given the members — not a
metaphor but a colimit. VERIFIED (the construction and its symmetry are
computed; cf. H65).

### 49. What the three guarantees amount to

Read together, the three are a spine for the whole reconstruction. The
*classification* of the parts is forced (a colimit); the *self* that integrates
them is guaranteed to exist (a fixed point); and the *unions* those selves form
have a universal shared state (a colimit). An alphabet that arrived as oracle
and metaphor is, examined categorically, a `G`-set whose (co)limit structure and
fixed-point theory *are* the architecture of a self and its bonds. This is the
sense in which the reconstruction carries strict mathematical and categorical
guarantees: not that the readings are true of any given person — that remains
for the diary to test — but that the *form* of the architecture is not
arbitrary. It is the only form the mathematics allows.

## Part XIII. Functorial guarantees: what is canonical, what is chosen

Part XII gave three object-level guarantees. This part gives the morphism-level
ones — the guarantees that concern how the reconstruction *transforms* — and in
doing so draws a sharp line between what in a person's chart is canonical and
what is merely a convention. The digging turned up something more honest than a
blanket "everything is invariant": the reconstruction is coordinate-free in
exactly one layer, and knowing precisely which is itself the result. Research in
`architecture/category_lab2.py`.

### 50. The coordinate-free content is the magnitude/orbit layer

Does a person's reading depend on how we happen to *label* the seven voices? The
classification does not (Part IX, §46): `classify` is exactly `G`-equivariant —
verified on all 1280 gate·group pairs, zero mismatches. But what of the full
encoder `E₂`, which decorates the combinatorics with coherence *phases*? Here
the answer is precise. The **magnitude** `|E₂(g·chart)|` equals `U_g |E₂(chart)|
U_g†` for *every* one of the 168 symmetries, to machine zero (`0.00`). The
**complex** state does not — it differs by up to `0.9`, and the reason is exact:
the phase of a coherence is placed by an arbitrary ordering of its two voices
(which one carries `+θ`), a point-ordering convention with no intrinsic meaning.

So the boundary is sharp. **The coordinate-free content of the reconstruction —
the part that is a genuine invariant of the person and not of our labelling — is
exactly the magnitude/combinatorial layer: the populations, the coherence
strengths, and the orbit fingerprint.** The discrete architecture is canonical;
the coherence phase is chosen. What is invariant is what is real. (HD's own
encoder is not even magnitude-equivariant — its channels carry no Fano symmetry,
HB13/TF5 — so it is the reconstruction that makes any coordinate-free reading
possible at all.) VERIFIED (`|E₂|` equivariance is machine-exact).

### 51. The self is a canonical retraction

The self-model exists (Part XII, §47) — but is it *canonical*? Run the
self-observation map `φ` to its fixed point; call the result `Ψ(ρ)` (the
converged self-model reached from `ρ`). Then `Ψ` is **idempotent**: `Ψ∘Ψ = Ψ`,
verified to `2·10⁻¹⁴`. An idempotent is a **retraction** — it projects the whole
state space onto its image, the self-representable states, and fixes them. So the
"I" is not merely *a* fixed point but a *projection*: every state has a canonical
self-model, and the self-model of a self-model is itself. By the Karoubi
splitting, an idempotent is a genuine subobject, so the self-representable states
form a real object inside the architecture, not a fuzzy region. VERIFIED (`Ψ`
idempotency is computed).

### 52. The individual is a naturality failure

Two functors act on the state space: the wheel's **symmetry** `R_g` (relabelling
the voices by a group element) and the wheel's **dynamics** `T` (evolution under
the effective Hamiltonian `H_EFF`). Do they commute — is there a naturality
square making symmetry and time interchangeable? Only trivially: `H_EFF`
commutes with `U_g` for exactly **one** of the 168 group elements, the identity.
So an individual life — a specific trajectory under the dynamics — is precisely
the place where the wheel's symmetry and its dynamics *fail* to commute. **The
individual is a naturality failure; individuality is symmetry breaking stated
categorically.** The seven distinct voice-energies of `H_EFF` are what break the
`168`-fold symmetry of the bare wheel down to the identity, and that breaking is
the person. VERIFIED (the commutant is computed: `1` of `168`).

### 53. What the functorial layer settles

Object-level, the architecture's classification is a colimit, its self a fixed
point, its unions colimits. Morphism-level, its coordinate-free content is
exactly the magnitude/orbit layer, its self is a canonical retraction, and its
individuality is the exact failure of symmetry and dynamics to commute. Together
they answer the question a reconstruction must answer — *why this structure and
not another* — with a chain of standard theorems, each verified: the form is
forced, the self is guaranteed and canonical, the "we" is universal, the
invariant content is delineated to the entry, and the individual is located
exactly where the mathematics says an individual must live. The esoteric
alphabet, followed to the bottom, is the (co)limit and fixed-point theory of a
`G`-set — and the theory says which of its features are real and which are ours
to choose.

## Part XIV. Composition and time: the operad of gathering, the functor of life

Two structural questions remain. First, *how do selves combine* — a couple into
a partnership, partnerships into a family, families into a community? Second,
*how does a self move through time*, and where in that motion does its
individuality live? Each has a categorical answer with a guarantee, verified in
`architecture/category_lab3.py`.

### 54. Gathering is a symmetric operad

An operad is the exact structure for "coherent `n`-ary composition": a system of
`n`-input operations that compose associatively and don't care about the order
of their inputs. Gathering is one. For any `n` members, the operation `γ_n` takes
their commitments — the centered states `D_i = Γ_i − I/7` — to their weighted
mean, and the physical meta-holon is grey plus that mean, projected onto the
state cone. This `γ` satisfies the operad laws, each verified to machine zero:
it is **unital** (`γ_1 = id`, and the meta-holon of one person is that person);
**symmetric** (invariant under all `120` orderings of five members — a group has
no first member); and **associative with tracked weights** (gathering `{a,b}` and
`{c,d,e}` as two units, each member weighted `1/5`, equals the flat `γ_5` — a
barycenter). So **group formation is coherently composable: nesting couples into
families into communities is well-defined, independent of how you bracket it.**
The physical PSD-projection is the small, measured correction to strictness (it
is exact on the commitments, tiny on the states). And the operad's meaningful
*depth* is finite: `P_crit⁽ⁿ⁾` first exceeds `1` at `n = 4`, so gathering bottoms
out at **three floors** (SAD_MAX) — a categorical finiteness on how deep the
"holon of holons" can go. VERIFIED (the operad laws and the depth bound are
computed; cf. H65, T-142).

### 55. Life is a functor from the time-monoid; individuality is its obstruction

Time is a monoid — durations add — so a dynamics is a **functor** from `(ℝ, +)`
to the transformations of the state space: `T_{s+t} = T_s ∘ T_t`. The wheel's
evolution `T_t = e^{-iH_{EFF}t}` is exactly such a one-parameter group (verified:
the functor law holds to `10⁻¹⁶`). Now recall (§52) that `T` does not commute
with the wheel's symmetry `R_g`. The precise content of that failure is an
**obstruction**: the commutator `[T_t, R_g]` is nonzero for every `g` but the
identity — `167` of `168` — and it is *generated* by the infinitesimal commutator
`[H_{EFF}, U_g]`, whose nonzero count is the same `167`. So the finite-time
symmetry-breaking is exactly the integral of the infinitesimal one. **An
individual life is a cocycle — the obstruction to time and symmetry commuting —
and its source is precisely the seven distinct voice-energies of `H_{EFF}`.**
Flatten those energies and the symmetry returns and the individual dissolves;
keep them and the person is the shape of the obstruction. VERIFIED (the functor
law, the generator, and the obstruction counts are computed).

### 56. Eight guarantees

The reconstruction now rests on eight verified categorical guarantees, and
together they answer *why this architecture and not another* end to end. Its
parts are **classified canonically** (a colimit, §46); its **self exists** (a
fixed point, §47) and is **canonical** (a retraction, §51); its **coordinate-free
content is exactly the magnitude/orbit layer** (§50); its **unions have a
universal shared state** (a colimit, §48) and **compose as a symmetric operad**
of finite depth (§54); its **life is a functor** on time (§55); and its
**individuality is the precise obstruction** to symmetry and dynamics commuting
(§52, §55). An alphabet handed down as oracle is, followed to the bottom, the
(co)limit theory, fixed-point theory, operad, and one-parameter group of a
`G`-set — and the mathematics not only reconstructs the architecture of a self,
its bonds, and its life, but says which of their features are forced, which are
guaranteed, which are bounded, and which are ours to choose. That is what it
means to move a picture of the human from the esoteric shelf to the scientific
floor with strict guarantees.

## Part XV. The structural audit: HD measured against the forced structure

Parts XII–XIV proved the seven-voice architecture is *forced* — the unique
alphabet minimality (T-224) and `PSL(2,7)` allow. That is a statement about the
mathematics. It leaves an empirical question the reconstruction is obliged to
ask of its own calibration source: how do Human Design's *own* structures — the
nine centres, the thirty-six channels, the King Wen wheel — actually relate to
the forced one? Not "is HD useful" (it calibrated us end to end), but "is HD's
organisation the forced organisation, an approximation of it, or a different
structure altogether?" Three probes answer, each computed from the engine's
authoritative data, each able to embarrass the theory. The result is sharper —
and more generous to HD — than the intuition that opened the inquiry.

### 57. The bodygraph is structurally independent of the forced alphabet

Take the sixty-four gates the way HD groups them — into nine centres by the
channel wiring — and set that grouping against the two forced decompositions:
the seven voices (each gate's canonical voice, from its heptacode syndrome) and
the five `PSL(2,7)` orbits (the classify classes). They barely relate. No centre
maps to a voice: the *purity* of a centre's voice-distribution — the share held
by its dominant voice — runs from `0.15` (the Throat, nearly uniform across all
seven voices) to `0.37` (the Spleen), where a clean nine-into-seven refinement
would sit near `1`. No centre is pure in orbit class either — every one mixes
pairs, lines and triangles. And the thirty-six channels, read through each
gate's canonical voice, distribute across the twenty-one coherences in a way
statistically **indistinguishable from random** (eight coherences left unwired,
against `7.2` expected by chance alone). The bodygraph's organisation and the
forced alphabet are, to measurement, two different cuts of the same sixty-four
gates. VERIFIED (`core/examples/hd_audit.rs`). The honest caveat: a gate's voice
is *our* reconstruction, so this measures HD against our encoding, not against
an independent oracle — the decisive comparison is experiential (§60).

### 58. Γ and the bodygraph are two lossy projections, neither a function of the other

Both the continuous seven-voice state `Γ` and the discrete bodygraph (type,
authority, profile) are projections of the same birth moment. Over four thousand
sampled charts, the relationship between them is measured, not assumed. The
bodygraph is *coarse*: its `143` distinct type-authority-profile signatures each
cover about twenty-eight of the four thousand charts. Within one such signature,
`Γ` still varies almost as much as it does globally — the within-signature spread
is `0.97` of the global spread: the twenty-eight people a signature lumps
together hold twenty-eight different seven-voice states. The charts nearest to
one another *in `Γ`-space* share a bodygraph signature `4.4%` of the time. And
`Γ` does not carry the HD type at all: a nearest-centroid read recovers it at
`36.6%` against a `35.8%` base rate — **a zero.**

The first two of those three had no null, and adding one changes how they must
be read. Shuffling the signature labels across charts two hundred times — group
sizes preserved exactly, only the label-to-chart link broken — puts the
within-signature spread at `0.985` and the nearest-neighbour agreement at
`1.9%`. Both observed values sit outside the whole permutation distribution.
So the two are **not** independent, and the earlier phrasing («≈1, therefore
the bodygraph barely constrains `Γ`») was an inference drawn from a number's
nearness to one rather than from a baseline.

What that null can and cannot settle is worth stating, because it is weak in a
specific way: it severs the label from the chart *entirely*, while bodygraph and
`Γ` are both functions of the same moment. Independence is therefore rejected
trivially — any two functions of the same `jd` would reject it. What survives
reading is magnitude and direction. The spread tightens by `1.4%`, which is
nothing. Nearest-neighbour agreement runs `2.3×` above chance, a real relative
effect that is still only `4.4` in a hundred. And the type is not recovered at
all. The conclusion the section was built to reach is unchanged and now rests on
the right ground: the two projections share a cause and are weakly dependent,
but **neither recovers the other** `[Т]`.

*Correction of record (2026-07-28).* This paragraph previously reported `0.89`,
`7.2%` and a partial recovery of the type at `64%` against `36%`. Those figures
were measured on encoder path v1, which was the library default while the
product ran v2; the default has since been corrected (§89). Re-measured on both:
v1 reproduces the old numbers (`0.890`, `6.8%`, `59.7%`), the live path gives the
ones above. The change is not cosmetic — **the partial type-recovery disappears
entirely** — and it cuts in the direction of the section's own conclusion: the
two descriptions are *more* independent than was written, not less. So the two
are two largely independent, lossy compressions of the same activations: `Γ`
finer-grained (it distinguishes what the bodygraph lumps) and forced (the
mathematics of Parts XII–XIV); the bodygraph coarser and non-forced, yet keeping
a topological determination `Γ`'s magnitudes drop. VERIFIED
(`core/examples/falsify_gamma_vs_bodygraph.rs`). Neither *structurally*
dominates — which is precisely why the decider must be experiential (§60).

### 59. The King Wen wheel is I Ching–exact, not arbitrary

The last place HD could be arbitrary is the *order* of the gates around the
wheel — the King Wen sequence, handed down from the I Ching with no known
generating rule. It is not arbitrary. Read as six-bit hexagrams, the gate `180°`
opposite on the wheel is the exact bitwise **complement** — in every one of the
thirty-two pairs, without exception (HD's "programming partners" are yin/yang
inversion, an exact binary law). Consecutive gates differ by `1.81` bits on
average against `3.05` for random pairs, and a third of the steps flip a single
bit: the wheel is strongly Gray-*like*, if not a perfect Gray cycle. What the
wheel *order* does **not** independently carry is the forced seven-fold: the
orbit class shows only a weak `+0.21` lag-one autocorrelation around the wheel,
and because a gate's orbit is a function of its bits, even that weak clumping is
*induced* by the binary structure, not independent evidence of the alphabet in
the ordering. VERIFIED (`core/examples/hd_wheel_audit.rs`). So the wheel order is
governed by the I Ching's own exact binary structure — roughly three millennia
old — which HD inherited faithfully; the forced seven-fold lives elsewhere, in
the gate→voice map, not in the linear sequence.

And the **profiles** complete the arithmetic picture. The design Sun sits `88°`
of solar arc before the natal one, and `88°/0.9375° = 93.867` lines ≡ `+2.133`
(mod 6) — so the design line is an *exact function* of where in its line the
natal Sun stands, offset `+2` below the boundary `x = 0.8667` and `+3` above
it. Measured over four thousand charts: exactly HD's twelve profiles and no
others; offsets `+2` at `86.5%` and `+3` at `13.5%` (predicted `86.7/13.3`);
**zero** determinism mismatches. The profile therefore carries *no second
degree of freedom* — it is one continuous coordinate discretized `6×2` ways,
and the rare profiles (`1/4, 2/5, 3/6, 4/1, 5/2, 6/3`) simply mean birth in a
line's last eighth. A sharp corollary: HD's own Right-Angle / Juxtaposition /
Left-Angle grouping does **not** coincide with the real `+2/+3` split — the
lore's classification mixes the two arithmetic classes. Like the types, the
profile is faithful arithmetic riding on one astronomical number. VERIFIED
(`core/examples/profile_arithmetic.rs`). The **incarnation crosses** close the
account: the quartet {Sun_P, Earth_P, Sun_D, Earth_D} is an exact function of
the natal Sun longitude alone (`0/20000` determinism mismatches), with exactly
**128** distinct quartets (= 64 gates × 2 design options) — where HD names 192
crosses by overlaying its three lore-angles on the same one-coordinate space.
Types, profiles, crosses: three vocabularies, one number. VERIFIED
(`core/examples/cross_arithmetic.rs`).

### 60. What the audit settles, and what it leaves to the diary

The three probes triangulate one honest picture, and it is not "HD is wrong."
HD is a *faithful carrier of two ancient, exact structures*: the astronomy (the
gate.line placements, verified against JPL to the arcsecond) and the I Ching's
binary order (the complement law, exact on the wheel). What HD's nine centres
and King Wen wheel do **not** encode is the **forced seven-fold** — the
organising layer minimality and `PSL(2,7)` prove is the unique one the
mathematics allows. That layer is a *different*, deeper cut of the same
sixty-four gates, and it is where the reconstruction lives: the homograph — the
seven voices drawn as a heptagon with their coherences — draws it, continuous
where the bodygraph is binary and forced where the wheel is inherited, while the
bodygraph and wheel remain the familiar calibration surface. The audit does not ask us to replace HD; it locates,
precisely, the layer HD kept implicit and the reconstruction makes explicit.

One thing the structure cannot settle it hands to experience, and this is the
falsifier of the whole programme. `Γ` is finer and forced; the bodygraph is
coarser and inherited — but *does the forced layer track lived experience better
than the inherited one?* Two pre-registered, independent predictions, wired to
the n-of-1 diary, decide it. The first: since coherence couples voices, a steady
voice tightly bound to an open one should still wobble day to day — variance
*leaks through coherences* — where the bodygraph's binary open/defined predicts
it should not. The second: the coherence magnitudes `|γ_ij|` *are* the claim
that two voices are coupled, so tightly-coupled pairs should co-vary in the
diary, where the bodygraph makes no per-pair prediction. Each reports a number
that can come out against `Γ`; agreement of both is far stronger than either
alone. [OPEN] — the probes are built and verified to respond correctly
(`selftest.rs`), and await the days of self-report that will adjudicate the
forced structure against the inherited one on a real person's own life.

## Part XVI. Two symmetries on one wheel: why the I Ching cannot see the Fano lines

Part XV, §59 found something precise and a little humbling: the *order* of the
gates around the wheel is not the forced seven-fold but the I Ching's own exact
binary law — the `180°` gate is the bitwise complement, in all thirty-two pairs.
The forced layer, it concluded, "lives elsewhere, in the gate→voice map." That
raises the sharpest structural question the whole audit can ask. The I Ching is
not just a *list* of sixty-four figures; it is sixty-four figures **with their
own symmetries**, operations three millennia old that a diviner performs without
thinking: read a hexagram upside down (inversion, 反卦), flip every line
yin↔yang (complement, 旁通), take the inner hexagram from lines 2·3·4·3·4·5
(the nuclear). And Part IX gave the forced structure *its* symmetry — the Fano
group `G = PSL(2,7)`, order 168, whose orbits on the sixty-four even codewords
are the five reconstruction classes. **Are these the same symmetry?** If the I
Ching's ancient operations turned out to be elements of the Fano group, the
oracle and the mathematics would be looking at one object through one lens. They
are not — and the exact way they fail to coincide is the cleanest statement the
audit produces of what the reconstruction adds.

### 61. The coarse layer they share: valence

First, what the two structures *do* agree on. Under the heptacode φ, a gate's
seven-voice support has a **weight** — how many of the seven voices it engages —
and that weight is the coarse skeleton of the orbit classes: weight `0` is the
Source (one gate), weight `2` the pairs (twenty-one), weight `6` the voices
(seven), and weight `4` the remaining thirty-five, which the group splits into
seven "lines" and twenty-eight "triangles." The I Ching's line-permutation
operations — inversion and trigram-swap, which merely rearrange the six lines —
cannot change how many lines are yang, so they **preserve weight**, and hence
send Source→Source, pair→pair, voice→voice cleanly. Against a *random* embedding
of the I Ching into the voice-code, three classes descending this way is rare
(`p < 10⁻⁴`, twenty-thousand shuffles). So the two systems genuinely share the
notion of a gate's **valence** — how much of the person it engages. This is real
agreement, but its mechanism is humble: it is just weight-preservation, and the
complement and nuclear operations, which change weight, do not even manage that.

### 62. The fine layer they do not: the Fano lines are invisible to the oracle

The interesting classes are the weight-4 pair — the seven "lines" and the
twenty-eight "triangles." Their split is not about *how many* voices but *which*
seven four-subsets are the complements of Fano lines: it is the genuinely
group-theoretic content, the place `PSL(2,7)` actually does work beyond counting.
**No I Ching operation respects that split.** Inversion, complement, trigram-swap
and the nuclear map all *mix* lines and triangles — a gate the group calls a
"line" is sent to one it calls a "triangle" and back, with no rule. The oracle's
operations see the valence and are blind to the Fano geometry beneath it.

### 63. Why it is impossible, not just unlucky: the cycle-type census

One could object that this is an artefact of *our* particular ordering of the
six lines onto voices (`A,S,L,D,U,E`, with `O` the parity bit). It is not, and
the reason is the deepest fact in this part. Whatever assignment one picks, the
I Ching's inversion and trigram-swap are **involutions that fix one voice and
pair the other six** — cycle type `2³·1` on the seven voices (inversion is
`(A E)(S U)(L D)`; both, tellingly, fix `O`, the Ground, and both swap `S↔U`,
Structure↔Unity). Now census the Fano group by cycle type on the seven voices:

| order | cycle type on 7 voices | count | what it fixes |
|------:|:-----------------------|------:|:--------------|
| 1 | `1·1·1·1·1·1·1` | 1 | everything (identity) |
| 2 | `1·1·1·2·2` | 21 | **a whole line of three voices**, pairs the other four |
| 3 | `1·3·3` | 56 | one voice |
| 4 | `1·2·4` | 42 | one voice |
| 7 | `7` | 48 | nothing (a Singer cycle) |

Total `1+21+56+42+48 = 168`, as it must. Read the involution row: **every**
reflection in the Fano group fixes a *line* — three collinear voices — and swaps
the remaining four. The type `2³·1` (fix one, pair six) simply **does not occur**
in `PSL(2,7)`. So no relabelling of lines onto voices can turn an I Ching
line-symmetry into a Fano automorphism: the impossibility is a theorem about the
group's conjugacy classes, not a matter of convention. The two systems anchor on
incompatible things — the oracle fixes a single voice (and, in its two natural
reflections, that voice is the Ground) and rotates the other six; the group fixes
a whole line of three and rotates the other four. They are **orthogonal
involutions on the same sixty-four gates.**

And yet the two are not strangers — the recursion finds exactly how thin their
overlap is. Compose the oracle's two reflections and something clicks:
`⟨inversion, trigram-swap⟩` is the Klein four-group `{1, R, T, R·T}`, and while
`R` and `T` each escape the Fano group, their product `R·T = (A L)(D E)` has the
reflection type `2²·1³` and — checked directly — fixes the Fano line `{S, O, U}`
(Structure–Ground–Unity), so it **is** a Fano reflection. The intersection is
therefore precisely a `Z₂`: the I Ching's four-element symmetry group and the
168-element Fano group share exactly one non-trivial element — the reflection
about the integrative `S–O–U` line — and the oracle's two generators are exactly
the part that lies outside. Not disjoint, then, but meeting in a single thin
axis: the very line the reconstruction reads as the structural spine.
VERIFIED (`core/examples/iching_orbits.rs`).

### 64. What the two symmetries settle

Part XV located *where* the forced seven-fold lives — in the gate→voice map, not
the wheel order. Part XVI says *why the wheel order could never have carried it*:
the symmetry that generates the wheel (line-reversal and yin/yang complement) and
the symmetry that generates the forced classes (the Fano reflections) meet in
only a single shared reflection — the `Z₂` about the `S–O–U` line (§63) — and are
otherwise disjoint at the involution level. The I Ching kept a real,
exact structure — valence and the binary complement law — with perfect
faithfulness for three thousand years; it simply had no operation that could feel
the Fano lines, because such an operation is not in its symmetry group. The
reconstruction is not a correction of the oracle but a *second lens* fitted over
the same figures: where the I Ching's reflections fix the Ground and turn the
manifest six, the forced structure's reflections fix a line and turn the other
four, and only the second resolves the coherence geometry the homograph draws.
Recursively, the two even share a horizon: iterated to its attractor, the nuclear
map carries every orbit class into the same three fixed points — the Source, the
lone `O`-voice gate, and the `63↔64` pendulum — so the oracle's own deepest
operation drains the wheel toward the Ground the reconstruction places at the
centre. Two symmetries, one set of sixty-four; the audit does not choose between
them, it shows they are complementary and names, exactly, the geometry each can
and cannot see. And the completed picture confirms the reading: adjoining the
complement (the wheel's exact `180°` law) to inversion and trigram-swap, the
oracle's whole symmetry group is the elementary-abelian `(Z₂)³` of order eight,
and its fourteen orbits on the sixty-four gates are **transverse** to the forced
five classes — twelve of the fourteen cut across them. The wheel's symmetry and
the forced partition are not nested but independent cuts of the same set; the
`Z₂` about the `S–O–U` line is the entire overlap. This is CONSTRUCTION, not a
minted theorem — a computed census of finite groups, handed to the same diary
(§60) that must still decide whether the finer geometry tracks a real life.

## Part XVII. A second tradition, honestly: the chakra spine and the S–O–U line

The I Ching gave a clean test because it came with an exact bijection — the
heptacode — so no interpretation entered. A second ancient system, the Vedic
chakras, does not, and the honest thing is to say where the judgement lives
before reading any number. Mapping a chakra to a voice is semantic: we fix one
correspondence from each chakra's *documented* element and function, decided on
its own merits and never by looking at the test — Root (earth, holding form) →
`S`; Sacral (water, the felt interior) → `E`; Solar Plexus (fire, will, action)
→ `D`; Heart (air, union) → `U`; Throat (ether, expression) → `A`; Third Eye
(light, discernment) → `L`; Crown (the source, the ground of being) → `O`. Two
guards keep this from being a story fitted to a wish. First, of all `5040`
bijections, this is the **unique** one that maximises a plain shared-vocabulary
score between the two sides' standard descriptions — it is not hand-steered.
Second, everything below is decided against the full `7!` null.

**The one structural claim that survives.** UHM already distinguishes a single
triple among its seven voices: the Fano line `{S, O, U}`, the integrative spine
— the axis fixed by the one reflection the I Ching shares with the Fano group
(Part XVI, an independent and *earlier* finding, not chosen here). The chakra
system independently distinguishes a triple of its own: `{Root, Heart, Crown}` —
the two poles and the centre of its seven-link spine. Under the documented
mapping, the first lands exactly on the second. Against the `7!` null the
coincidence has `p ≈ 0.029` (one hundred forty-four of five thousand and forty
bijections would do it), and because both triples were named before the test,
this is a single pre-specified comparison, not a search. So two independent
traditions — the oracle's shared symmetry axis and the chakra spine — point at
the same three voices, `Structure–Ground–Unity`. Suggestive, not established:
`p ≈ 0.03` on an interpretive mapping is a hint, not a law.

**What does not survive — and is reported anyway.** The finer claim, that the
chakra *order* up the spine tracks UHM's coupling, fails. Reading the natal
sensor wiring (thirteen of twenty-one voice-pairs, HB13) as the coupling, the
six adjacencies of the mapped spine put four on wired pairs against a null mean
of `3.71` — `p = 0.60`, indistinguishable from chance. The convergence is on the
*distinguished triple*, not on the sequence. VERIFIED as computation
(`core/examples/vedic_synthesis.rs`); [OPEN] as meaning — a mild convergence and
an honest null, offered as an invitation to the diary and to sharper encodings
of the tradition, not as a result the programme leans on.

## Part XVIII. The interpretation crystal: how the engine speaks

Everything before this part is about what the engine *computes*. This part is
about the second half of the instrument — how a computation becomes a sentence
a person can act on — because that half turned out to demand the same rigour
as the first, and repaid it with an architecture.

**The language machine.** Every surface of the product (the day letter, the
week, the year atlas, the life map, the date search) once translated computed
events into words locally, and each surface drifted: one printed «bridge peak —
6 timebridges», another named wheel positions outright. The repair was to make
interpretation a *language* with a grammar. Computed events are typed FACTS —
a machine key plus slots («epoch.turn», the new door, the hand that turned).
A LEXICON assigns each fact key one living phrase; slot values are filled by
exactly one resolver per concept (a door speaks its human theme; a hand its
plain name; a voice-pair its string name). A single WEAVER renders every fact
for every surface under fixed weaving rules: a name never appears without its
consequence; joints are «: » with a lowered continuation; numbers, wheel
indices and canon terms exist only in the advanced register. No surface parses
another surface's strings; all speak through the weaver. VERIFIED as
computation: the weaving rules are enforced by tests that fail the build when
a surface leaks a gate number, a Greek letter, or a bare unexplained name.

**The accessibility contract.** The plain register carries a standing
invariant: no metaphor may reach a reader without a glossary article — the
term store *is* the contract, and a test enumerates the metaphors (sky, page,
string, door, bridge, form, resonance, season, window, …) and fails when one
is missing or incomplete in either language. The advanced register keeps the
machinery read-outs unchanged, one toggle away, so depth is never amputated —
only ordered behind explanation.

**The prognostic catalogue.** The computable day-facts of one person close
under a small set of questions, and the catalogue turned out to be finite:
*tailwind searches* (best days for a launch, a talk, the body, the heart,
foundation, study, rest, a showing — or any life-domain, or any voice-set),
*tempering warnings* (dense stretches where several tests meet; sustained
costly-form runs; the seven-year steps), *orientation* (day, week, ninety
days, year, life), *personal rhythms* (the emotional month calendar, the
personal year), and *shared time* (a day to meet for two, the circle's day,
the week for two). All of these are one engine — a scored walk over the
horizon whose every returned date carries its reasons, woven by the same
weaver — so a new question is a new weighting, not a new subsystem.

**The mirror.** The honesty layers demand that layer-3 readings be tested
only by the person's life, and the instrument now closes that loop itself:
every evening rating is preceded by a hidden, committed prediction of the
day, and once enough pairs accumulate the mirror opens with one of three
verdicts — a match unlike chance (the person's own evidence *for* the tool),
an inverted link (reported as such, not hidden), or an honest null («we keep
counting and never dress hope as fact»). The permutation test behind the
verdict is deterministic and inspectable; the plain register speaks only the
verdict, the advanced register shows r, p and n. [OPEN] by construction: the
mirror's content is each person's own stream, and the programme claims
nothing on their behalf.

*Status: engineering crystallization of Parts I–XVII; no new mathematical
claims. The grammar, catalogue and mirror are implemented, tested and
deployed in the reference engine (`core/src/speak.rs`, `core/src/stalk.rs`,
`core/src/me.rs`, the bot surfaces); the design record lives in the engine
repository's ARCHITECTURE.md.*

## Part XIX. The Enneagram, arithmetically: two laws from one seven

The I Ching (Part XVI) shared the wheel's *order* but not its lines; the chakra
spine (Part XVII) converged on one distinguished triple and no more. The
Enneagram is the sharpest comparison of the three, because it is not a list of
figures or a ladder of centres — it is, explicitly, an **arithmetic diagram**.
Gurdjieff built it on two laws he held to be independent: the **Law of Three**,
the triangle `3–6–9`, three irreducible forces; and the **Law of Seven**, the
octave, drawn as the six-pointed figure whose flow is `1→4→2→8→5→7→1`. Two laws,
two axioms. The question this part settles is whether they are two — and the
answer is that the forced seven already contains its own three, so that what the
Enneagram posits twice, the reconstruction derives once.

### 65. The octave is the multiplicative group mod 7

The Enneagram's process figure is not decorative: its vertices are the digits of
`1/7 = 0.142857…` and its arrows follow their order. That decimal is a fact about
the number seven, and naming it exactly is the whole key.

**Lemma XIX-A.** *The remainders that generate the period of `1/7` trace the
cyclic group `(ℤ/7)*` under multiplication by a primitive root; the visible
digit-cycle `1,4,2,8,5,7` is its faithful shadow — one digit per remainder, the
same period six.*

*Proof.* Long division of `1` by `7` produces at step `k` the remainder
`r_k = 10^k mod 7`. In `ℤ/7`, `10 ≡ 3`, and `3` is a primitive root (`3^1..3^6 =
3,2,6,4,5,1`, all six nonzero residues), so `r_k = 3^k` runs once through
`(ℤ/7)* = {1,3,2,6,4,5}` before repeating. Each digit is `d_k = ⌊10·r_{k-1}/7⌋`,
and the six digits `1,4,2,8,5,7` are in bijection with the six remainders — the
period has length `6 = |(ℤ/7)*|`, the group's order. `∎`

So the Law of Seven, stripped of its musical dress, is the statement that
`(ℤ/7)*` is cyclic of order six. The octave *is* the multiplicative group of the
field with seven elements.

### 66. The three is already inside the seven

Where the Enneagram then adds a *second* law for its triangle, the reconstruction
needs no second anything: the "three" is forced by the same seven that carries
the octave. Part IX fixed the generation count `N_gen = 3`, and its value is not
an input but the order of a canonical subgroup.

**Lemma XIX-B.** *The quadratic residues `QR(7) = {1,2,4}` are the unique
index-two subgroup of `(ℤ/7)*`; they are exactly the even powers of any
primitive root, and `|QR(7)| = (7−1)/2 = 3`.*

*Proof.* Squaring in `ℤ/7` gives `1,4,2,2,4,1` for `1..6`, so the squares are
`{1,2,4}`. In a cyclic group of order six the squares are the even powers of a
generator — `3^0,3^2,3^4 = 1,2,4` — which form the unique subgroup of order
`three`, index two. `∎`

Hence `N_gen = |QR(7)| = 3` is the three of the "Law of Three," read off the
seven directly: it is the residue half of the octave's own cycle, not a separate
principle laid beside it. The Enneagram draws a triangle; the reconstruction
finds it already inscribed as the squares.

### 67. The arrows are half the collineations

The comparison sharpens when both structures are given their symmetries — the
move that decided the I Ching in Part XVI. The reconstruction's seven-fold layer
carries the Fano group `G = PSL(2,7)` (Part IX); the Enneagram carries its
process arrow, one step of the flow `1→4→2→8→5→7`. Model the Fano plane in its
cyclic form: points `ℤ/7`, lines the seven translates `D+i` of the perfect
difference set `D = {1,2,4}` (its six nonzero differences hit each residue once).
A multiplier map `x ↦ m·x` is a collineation exactly when it permutes those
lines.

**Lemma XIX-C.** *The multiplier `x ↦ m·x` is a collineation of the cyclic Fano
plane iff `m ∈ QR(7)`. The Enneagram's process arrow `x ↦ 3x` is therefore not a
collineation, but its square `x ↦ 2x` is; the collineation multipliers form the
index-two subgroup of the process cycle.*

*Proof.* `m·D = {m,2m,4m}`. For `m = 2`: `{2,4,1} = D`, fixed; likewise `m = 4`
fixes `D`, and `m = 1` trivially — so every `m ∈ QR(7)` sends lines to lines.
For `m = 3` (a non-residue and primitive root): `3·D = {3,6,5}`, and checking the
seven translates `D+i = {1,2,4},{2,3,5},{3,4,6},{4,5,0},{5,6,1},{6,0,2},{0,1,3}`
shows `{3,5,6}` is none of them — a line has gone to a non-line, so `x↦3x` breaks
the incidence. The residues `{1,2,4}` are collineation multipliers, the
non-residues `{3,5,6}` are not; and since the process arrow is `x↦3x` with `3` a
generator, its square is `x↦9x = x↦2x ∈ QR(7)`, a collineation. The arrow's cycle
`⟨3⟩` (order six) contains the collineation subgroup `⟨2⟩ = QR(7)` (order three)
at index two. `∎`

Read plainly: **one step of the Enneagram's flow moves a Fano line off itself;
two steps land back on the geometry.** The reconstruction's symmetry is not the
Enneagram's arrow but its square — the residue half of the flow. Every other
step of the octave is a collineation; the steps between are the non-residue coset
the geometry cannot hold.

### 68. The triangle is a second modulus

There remains the triangle itself. Its three vertices `3,6,9` are the multiples
of three among the nine positions — an object in `ℤ/9`, not `ℤ/7`. The hexad
points `1,2,4,5,7,8` are the units mod nine, `(ℤ/9)*`, also of order six but
generated by *doubling* (`1,2,4,8,7,5`), a different cycle from the octave's
`1,4,2,8,5,7`. So the nine-point diagram is a **hybrid of two moduli**: a
`mod 7` sequence (the `142857` flow, Lemma XIX-A) laid over `mod 9` positions
(triangle and units). This is not a flaw in the Enneagram — it is why it *needs*
two laws: the triangle lives where the octave does not, and no single arithmetic
holds both. The reconstruction keeps one modulus. Its three is the residue
subgroup of the seven (Lemma XIX-B), inscribed, not overlaid; there is no `mod 9`
triangle to import, and none is missing.

### 69. What the Enneagram settles

Four lenses, one statement. **Arithmetically** (§65–66) the octave is `(ℤ/7)*`
and the triangle is its residue subgroup — the seven already carries the three.
**Group-theoretically** (§66) `N_gen = |QR(7)| = 3` is derived where the
Enneagram axiomatises; where the tradition writes two laws, the reconstruction
proves one implies the other's count. **Geometrically** (§67) the process arrow
is not a Fano collineation but its square is, and the collineation subgroup sits
at index two inside the flow. **Modularly** (§68) the Enneagram straddles `mod 7`
and `mod 9`, and needs its second law precisely because of it, while the
reconstruction is `mod 7` throughout.

The honest reading `[И]`: this is not a claim that the Enneagram "reduces to" the
reconstruction, nor that its psychology is anywhere in these residues. It is the
narrower and firmer thing the mathematics does license — that the two laws the
tradition holds apart are, at the level of the arithmetic each is drawn from, one
law seen twice: a cyclic group of order six and the order-three subgroup it
already contains. The Enneagram inscribes the seven and the three on separate
figures; the forced structure shows the three was the seven's own squares all
along. That the oldest of these diagrams should encode, in the period of `1/7`,
the very group whose residues fix `N_gen` is offered as an invitation to the
comparative record — suggestive of a shared arithmetic root beneath the
traditions, not a doctrine the programme leans on. *(Verified as computation:
`core/examples` reproduces Lemmas XIX-A through XIX-C; `[И]` as meaning.)*

## Part XX. The personality projections: the empirical taxonomies inside the seven voices

Parts XV–XIX measured the reconstruction against the symbolic traditions. This
part turns to the empirical science of personality — the Big Five and
Cloninger's temperament model, the two most validated instruments the field
has — and asks the sharper question. Not whether the reconstruction *resembles*
them, but whether it *generates* them; and, once it does, what its own structure
carries that they cannot see.

### 70. The predictive-processing bridge

The Five-Factor Model is usually told as a lexical fact: factor-analyse enough
trait adjectives across enough people and five dimensions fall out. Its deepest
modern reading, though, is mechanistic. DeYoung's Cybernetic Big Five Theory
frames the five factors as parameters of a *predictive, goal-directed* control
system — the same free-energy account of mind the reconstruction already runs in
its active-inference layer (`psyche.rs`). On that reading the bridge is not
analogy but shared mechanism:

- **Plasticity** (Openness + Extraversion) is exploration — a system that raises
  the precision it grants incoming signal and so *samples* the world. In the
  reconstruction this is exactly a high-gain (open) voice.
- **Stability** (Conscientiousness + Agreeableness + emotional stability) is
  maintenance — defending stable goals and interpretations against disruption. It
  is a defined, low-gain voice held as a steady internal source.
- **Neuroticism** is low Stability — the same maintenance system read as its
  failure to hold, its reactivity riding the Feeling voice's gain. (The mind↔body
  prediction error `razlad` was expected, on a free-energy account, to carry it;
  §73 reports that in this substrate it does not — the bridge is kept honest
  there rather than assumed here.)

So the Big Five is not imported into the reconstruction; it is *recovered* from
the very quantities — gain, definedness, prediction error — the reconstruction
already computes for other purposes.

### 71. The construction that forces the covariance

The five factors are not statistically independent. They cluster into two
metatraits — Plasticity binding O and E, Stability binding C, A and low-N — and
that covariance is the fingerprint any honest projection must reproduce:
`corr(O,E) > 0`, `corr(C,A) > 0`, `corr(C,N) < 0`, `corr(A,N) < 0`.

A naive projection fails it. If each factor is a weighted sum of *voice levels*
(the diagonal of `Γ`, normalised to sum one), the levels form a **simplex**, and
factors built on disjoint voices acquire a spurious negative correlation from the
constraint alone. Measured across 2340 charts, that naive map gives
`corr(C,A) = −0.17` and `corr(A,N) = +0.22` — both signs wrong.

The repair is to build the way the trait hierarchy is actually built:
metatrait-first. Compute Plasticity and Stability from *gain and razlad* — signals
that are not simplex-bound — and set each factor to `W·(its metatrait) +
(1−W)·(its specific voices)`. The shared metatrait now carries the between-factor
variance, and the empirical covariance is reproduced by construction. At
`W = 0.45`:

| relation | empirical | reconstruction (n = 2340) |
|---|---|---|
| `O–E` (Plasticity) | `+` | `+0.72` |
| `C–A` (Stability) | `+` | `+0.49` |
| `C–N` | `−` | `−0.74` |
| `A–N` | `−` | `−0.40` |

The model resolves one level finer, into the ten DeYoung aspects — two per
factor, each a metatrait plus a single specific voice, the factor being their
mean. All ten nest in their parent (population correlations `0.64`–`0.95`), so
the finer optic is real, not decorative: a high Openness that is Intellect (the
Meaning voice) reads differently from one that is aesthetic Openness (Expression
and Feeling), and the reconstruction can say which.

This is a consistency result, not yet independent evidence: the construction is
*engineered* to be able to carry the fingerprint, and it can. The evidence proper
is in §72. *(Verified as computation: `core/src/bigfive.rs` and its
`construct_validity_matches_big_five` test fail the build if the four signs
break.)*

### 72. The substrate generates the taxonomies

The strong test is convergence. A projection engineered to carry one instrument's
covariance proves little on its own; the test is whether a projection of the SAME
object onto a DIFFERENT validated instrument, tuned to nothing in the first,
reproduces the cross-instrument structure the literature reports. Three further
instruments answer, of three different kinds.

The first is Cloninger's seven temperament-and-character dimensions. Projected
from `Γ` by their own definitions and correlated with the Big Five projection,
they reproduce the empirical directions (De Fruyt and colleagues):
Self-Directedness runs against Neuroticism, Cooperativeness with Agreeableness,
Novelty-Seeking with Extraversion and with Openness, Harm-Avoidance with
Neuroticism, Persistence with Conscientiousness, Reward-Dependence with
Agreeableness — every major sign as reported, one weak dimension aside. This is
not a measurement left in a notebook: it ships as a guarded feature of the engine
— a module (`core/src/cloninger.rs`) whose build fails if those cross-correlations
break sign.

The second is Schwartz's four higher-order values — a taxonomy of a different
kind, motivational rather than dispositional. Projected the same way it lands the
same: Openness-to-Change with Openness and Extraversion, Conservation with
Conscientiousness and against Openness, Self-Transcendence with Agreeableness —
the value circumplex's known map onto the trait space, six of seven signs, the
one miss being Self-Enhancement's modest antagonism to Agreeableness, which the
substrate has no clean agency-voice to carry.

The third is Holland's six vocational interests — RIASEC, a taxonomy of yet
another kind again: not who a person is or what they hold worth but the KIND OF
ACTIVITY that draws them, the dominant model in career psychology. Projected the
same way, its interest↔trait signs land as the vocational literature reports
(Barrick, Mount and Gupta): Artistic and Investigative with Openness, Social with
Extraversion and Agreeableness, Enterprising with Extraversion, Conventional with
Conscientiousness — all six checked, and, like the others, shipped as a guarded
module (`core/src/riasec.rs`) that will not build if a sign flips.

The honest reading is at the level of *sign*, not magnitude. The shared metatrait
construction that lets any of these reproduce the correct signs also inflates the
magnitudes above what a between-instrument correlation should be, so the numbers
are not to be read as effect sizes; the direction is the claim. And its reach is
the point: a trait taxonomy, a temperament taxonomy, a values taxonomy and a
taxonomy of vocational interests — four coordinate systems laid on one manifold by
hands that never consulted each other — agree, in sign, where the science says
they should. Four points triangulate what two cannot. The agreement is built into
no single projection; it is the substrate showing through all four.

A fifth framework answers from a different direction still. Self-Determination
Theory (Deci and Ryan) names not what a person is but what MOVES them — three
basic psychological needs: autonomy, competence, relatedness. Projected the same
way and guarded the same way (`core/src/sdt.rs`), its need↔trait signs land as
the literature reports: autonomy with Openness, competence with
Conscientiousness and against Neuroticism, relatedness with Agreeableness and
Extraversion. And of the five it sits closest to the substrate — its three needs
are very nearly the quantities the reconstruction's predictive layer already
runs on: acting from an integrated self-model (autonomy), predicting the world
effectively (competence), coupling to an environment of others (relatedness).
Read from beneath, the two poles of the seeker–keeper axis are themselves two
needs: the seeker's is autonomy, the keeper's is competence.

### 73. The shared core

The categorical shape of the result is a *factorisation*. Let the personality
object be the reconstruction's data — `Γ`, the gain vector, `razlad`. A taxonomy
is a projection of that object onto a few coordinates: `π_B` to the Big Five's
five, `π_T` to Cloninger's seven. These projections are not independent maps;
they factor, in large part, through a shared low-dimensional **core** — the two
metatraits and the prediction-error term, `(Plasticity, Stability, razlad)`.
Regressed on that three-dimensional core, the Big Five factors return an average
`R² = 0.65` — but the carriage is worth reading honestly. Neuroticism's
`R² = 0.64` is carried almost entirely by **Stability** (it is anti-stability by
construction), not by `razlad`: the marginal correlation of N with razlad across
the full population is `≈0.01`. The prediction-error term earns its place in the
core through the other factors and the shared metatraits, not through the anxiety
it was theorised to carry — the free-energy → trait-anxiety bridge is, in this
substrate, a motivation and not a measured fact. Roughly two-thirds of each
factor is the core; the remainder is voice-specific detail.

Convergent validity is then exactly the statement that both taxonomy-projections
factor through the same core: `π_B` and `π_T` disagree only in their
factor-specific residuals, and agree wherever the core speaks — which is why
their cross-correlations come out as the literature has them. The diagram
commutes because the two descriptive charts share a generator they did not know
they shared.

And that shared generator is not only statistical. The fifth projection sits its
two agentic needs on exactly these two metatrait axes (§72) — autonomy on
Plasticity, competence on Stability — so the core through which every descriptive
chart factors is, read motivationally, the substrate's own structure of
self-determination: the statistical bottleneck and the seat of the will are one
object `[И]`. It is a reason the core is three-dimensional and not richer — a
predictive organism has exactly these degrees of freedom to spend (explore,
stabilise, and the error between), and a description of it can be no simpler and
needs be no larger.

### 74. What the projections settle

The relation is generation-and-subsumption, not imitation. Two things fix its
direction.

First, the seven voices are **near-orthogonal**. Measured across 2340 charts the
voice gains are almost mutually independent: the supposed exploration triad
`{A,D,L}` has mean internal correlation `+0.06`, the stability triad `{S,O,U}`
`+0.10` — neither is a tight cluster — and Plasticity and Stability themselves
correlate `−0.00`. The one appreciable hidden edge is `gain(A)–gain(L) = +0.33`:
the openness of Expression and of Meaning move together, an articulation-of-sense
link the lexical taxonomies have no coordinate for. A space of seven nearly
independent axes is strictly higher-dimensional than any five- or seven-*factor*
descriptive model whose factors are, by their own covariance, partly redundant.
The taxonomies are lower-dimensional lenses on the richer object, not the object.

Second, because they are lenses, the reconstruction has *surplus* — structure the
projections drop — and surplus is testable. The near-independence of the gains,
the `A–L` edge, the near-zero coupling of `razlad` to trait anxiety (a place the
substrate contradicts a naive free-energy expectation, and says so), the mild
explorer↔calm coupling the gain geometry implies: each is a prediction a purely
descriptive model cannot make, and each is falsifiable — per person through the blind diary
(the pravdomer), and at population scale against a scored instrument (BFI-2,
IPIP, the TCI). The reconstruction earns the comparison not by matching the
instruments but by predicting, from one mechanism, both the structure they share
and the structure they miss.

The honest status is `[Г]` shading to `[И]`: a conjecture with a stated
mechanism (§70) and a stated test (§74), not a theorem. What is already firm is
narrower and worth stating plainly — that the two most validated taxonomies in
personality science are, at the level of the covariance each rests on, two
projections of one seven-voice object, and that the object keeps more than either
projection returns. *(Verified as computation: `core/src/bigfive.rs` reproduces
the Big Five construction and its construct-validity and razlad tests; the
convergent-validity and orthogonality measurements are reproducible from the
per-voice gain, level and razlad the engine exposes on every chart.)*

### 75. The core, reverse-engineered

The projections settle *outward* — how the reconstruction relates to the
instruments. One question runs the other way: not what core we posited, but what
core the interpretations, taken together, *imply*. Read it off them. Take
everything the interpretive layer actually varies over a person — the seven
voice levels, the seven gains, `razlad`, and the twenty-one coherences (the
strings between voices) — thirty-six numbers, and measure the effective
dimensionality of that space across the population. The answer is what the core
must be to carry the readings the crystal already gives.

It is **not** low. Across 2340 charts the interpretation space has a
participation ratio of `17.3` and a dozen components above unit variance (a
thirteenth grazes the line at `1.01`) — its first principal axis holds only
`16.6%` of the variance, and the spectrum decays slowly after it. The object the crystal reads is roughly seventeen-dimensional:
neither the three of the shared metatrait core (§73), nor the five of a taxonomy,
nor even the seven of the voices.

The decomposition names where that dimensionality lives. The diagonal alone —
levels, gains, `razlad`, fifteen numbers — carries an effective `8.9`
dimensions. The twenty-one coherences alone carry `16.6`. And adjoining the
diagonal to the coherences lifts the total only to `17.3` — a gain of `0.7`. Two
things follow, and both are structural, not incidental. The coherences hold about
half the core outright; and they very nearly *subsume* the diagonal — the voice
strengths are, to first order, recoverable from the relationships between voices,
not independent of them. Measured head-on the subsumption is directional and
large: regressed across the population, each voice level is on average `80%`
recoverable (linear `R²`) from the twenty-one coherences, while the coherences
are only `28%` recoverable from the seven levels — the relations fix the
strengths far more than the strengths fix the relations. The relations are the
deeper description; the strengths are mostly their shadow. This is the
reconstruction's relational ontology, measured rather than asserted.

The consequence for interpretation is exact, and it is why a taxonomy reads as
generic while a coherence reading reads as *yours*. A five-factor profile is a
five-dimensional compression of a seventeen-dimensional object; it keeps the
diagonal's low-rank projection and discards the strings entire. The personalised
detail — the small distinguishing facts that carry, per person, more than the
broad ones — does not live in the factors. It lives in the coherences the factors
throw away. The optics that matter for precision are string-level optics.

So the core, reverse-engineered through the crystal, is the full `Γ` with its
coherences foremost — a high-dimensional relational object of which every
validated taxonomy is a thin, externally-anchored shadow. The honest boundary is
the same as before: the shadows are confirmed against the instruments (§72); the
seventeen-dimensional body is the reconstruction's surplus, falsifiable per
person through the blind diary and, in principle, against any sufficiently
fine-grained criterion, but not yet closed against a population one. What the
analysis fixes is the *shape* the core must have to be worth its readings — not a
claim that every one of its dimensions has already been paid for in data.

There is a practical corollary, and it is the operating principle of the detail
optics. If the personal signal lives in the high-dimensional body, magnitude is
the wrong way to read it out. The strongest coherence is, for most people, one of
the same three — `SE`, `DU` and `DL` lead in about two-thirds of charts — so
leading with strength returns the population's headline, not the person's.
Leading instead with *distinctiveness*, each coherence weighted by how far it
departs from the population baseline, recovers the individual. Measured, the lead
string chosen by strength carries `3.31` bits of between-person information;
chosen by distinctiveness it carries `4.37`, against a ceiling of
`log2(21) = 4.39` — near-maximal, with no single string leading more than seven
percent of the time. The general is what you share; the detail is where you
depart, and reading by departure is how a seventeen-dimensional object is made to
speak in a sentence.
*(Verified as computation: the effective dimensionalities are the participation
ratios of the correlation spectra of the level/gain/razlad/coherence features
the engine exposes on every chart; the information figures are the entropies of
the lead-coherence distribution under the two rankings.)*

### 75b. The geometry of the string space — and the confound that reclaimed it

The taxonomies of §70–74 project the seven voices onto outside instruments. A
harder question is what structure the 21-string space carries by itself. We
measured it twice, the second time against ourselves.

**First pass (real people).** Over every third record of the Gauquelin
registry (N = 5291, clock-precise births) we factor-analysed the string
strengths |γ_ij|: the spectrum came out flat (8 %, 7 %, 7 % — no general
factor, no class-betraying step; effective dimensionality by participation ratio 18.8 of 21), the theoretical Plasticity/Stability split
appeared only as a weak sign pattern (+0.16 vs −0.23 on axis 1), and the
leading axes read as voice contrasts — Meaning against Feeling (LO, SL vs
EO, SE, SU, OU), the word against the deed (AS, AO, AE vs SD, DE, DO).

**Second pass (the confound attack, pre-registered).** Slow bodies place
neighbouring gates into the same strings, so those axes could belong to the
WHEEL rather than to humanity. We ran the identical pipeline over N = 5291
random moments, uniform on 1850–2000. The verdict was unambiguous: the
random ensemble reproduces the human axes with |cos| = 0.94 on axes 1 and 2.
[C]

**The residual (g5).** The last question of the hierarchy — does humanity
add anything the wheel does not carry — was asked directly: the top
eigenvalue of the difference matrix C_people − C_random came out at 0.201
against a noise floor of 0.152–0.170 from independent random pairs — and,
decisively, below the human sample's own split-half floor of 0.217: two
random halves of the same people differ more than people differ from random
moments. (The human sample's higher internal floor reflects its epoch and
profession clustering, not hidden structure.) At this order the residual is
noise:
what is visible is the wheel's, and what people add is below this
instrument's floor. [C]

**What this settles.** The flat spectrum and the voice-contrast axes are
properties of the ENCODER's geometry — they hold for any ensemble of
moments, and real births add no detectable structure of their own at this
order. Three consequences stay useful. The individual variation the engine
reads is high-dimensional by construction: a person is genuinely not
compressible into one or two grand scales here (§75) — though this is now a
design fact, not an empirical discovery about people. The population adds
nothing the wheel did not already carry — consistent with the external
validation of §70 (natal→trait ≈ 0 at population level). And the method
paid: a result that survived one night only because we attacked it ourselves
the next morning is worth more than a result never attacked. [C]

*(Verified as computation: `machinery_axes_probe.rs` — the Gauquelin pass,
the deterministic random-moment control, and the axis cosines are printed by
one probe; the pre-registered guesses g1, g2, g4 and their verdicts stand in
its header.)*

### 75c. Where individuality lives: the point, not the population

The day's nulls line up into one positive statement. At the population level
the engine predicts nothing: natal charts do not sort professions (§70,
eta² < 0.5 %), pivotal months of well-documented lives are neither
dasha-marked nor transit-dense (both pre-registered pilots null), and the
string space's visible structure belongs to the wheel, with the human
residual below the sample's own split-half noise (§75b). Anyone selling
population-grade prediction from birth data is selling past these numbers.

What survives every one of those tests is the OTHER claim — the one the
product actually makes. A single chart is a high-dimensional internal
structure (the flat spectrum guarantees it is not compressible into types),
and its reading is checked the only place it can be: against the one life it
describes. That is not a retreat; it is the derived shape of the instrument.
The self-verification loop the product runs — the blind day-protocol, the
accuracy mirror, the P-quality correlation on the person's own diary — is
the falsifiability program AT the only scale where the signal was ever
claimed. [C]

So the honest division of labour stands, now as a data-driven conclusion
rather than a declared principle: the population is where we test and
refuse; the point is where we read and verify. «Проверяется только вашей
жизнью» — the corpus's old sentence — turns out to be not a disclaimer but
the architecture. [C]


### 75d. The genetic aspect, honestly: where 64 = 64 ends

Any system claiming completeness must say something about genes, and the
temptation is arranged for it: our wheel carries 64 gates, the genetic code
64 codons, and 2⁶ = 4³ is exact. Human Design and Gene Keys make the
identification directly. We tested it structurally instead of poetically
(`architecture/genetics_lab.py`), pre-registering three questions.

**Degeneracy signature (G1).** The standard code partitions 64 codons into
21 classes — 20 amino acids and stop — with class sizes {6,6,6, 4×5, 3,3,
2×9, 1,1}. No natural partition of our wheel carries that shape: nuclear
roots split 32/16/16, Hamming weight 20/15/15/6/6/1/1, either trigram 8×8.
The cardinalities agree; the structures do not. [C]

**Where the redundancy hides (G2).** In the code, degeneracy is concentrated
in the third nucleotide: changing it preserves the amino acid 67 % of the
time, against 1–4 % for the first two. In the hexagram the picture is not
milder but sharper and different: the nuclear root is a function of lines 3
and 4 alone — (0,0) source, (1,1) O-voice, unequal pendulum — so flipping
lines 1, 2, 5, 6 preserves the root always, and flipping 3 or 4 never does.
[T] This also explains the pendulum's 32/64 base rate: it is exactly the
XOR = 1 class. Both systems are redundant; the code hides its redundancy in
one position, the wheel in four inert lines.

**Any bijection at all (G3).** Insisting on hexagram ↔ codon, we enumerated
all 24 base-orderings × 3 natural bit-groupings and measured the best
agreement between the induced amino-acid classes and our roots: Jaccard
0.119, inside the 0.10–0.15 chance band. There is no encoding under which
the two partitions align. Gene Keys inherits the same numbering and the same
boundary. [C]

**What this settles for the system.** The gene–health link is real and
massively evidenced — monogenic disease, polygenic risk scores — and it does
not travel through 64-symbol numerology. Claiming otherwise would trade a
verifiable instrument for an unverifiable one. The bridge from our layer to
health runs where our layer actually measures: circadian and infradian
rhythm, load and recovery, the stress signature, the behaviour a person
logs. That is the same n-of-1 discipline of §75c — and it is why «checked
only by your own life» is the honest phrase here too. [C]


## Part XXI. One crystal, many scripts: the octonions under astrology, the sciences, and life

The reconstruction's skeleton is an object, not a metaphor: the octonions, their
imaginary Fano heptad, and their automorphism group `G₂`. This Part follows that one
object as it casts its shadow across the scripts humanity has used to read itself —
astrology first (§76–77), then the I Ching (§78) and the Kabbalah (§79), then the
whole spectrum at once (§80); and beyond divination, into the physics the corpus
already derives from the same crystal (§81), the calibration that makes a life *this*
life (§82), and life itself as a self-maintaining symbolic system (§83). One crystal;
many scripts; a single honest ledger of what is exact `[Т]`, what is structural `[С]`,
what is conjecture `[Г]`, and what is only descriptive `[И]`.

A word on foundations. The octonion apparatus this Part leans on is not assumed here
but *proven* in the corpus. The associator's sign law — `+1` on the seven Fano lines
(the associative quaternion triples), `−1` on the volumes, checked on all `343`
triples — is [T-243](./syndrome-calculus.md#октонионная-реализация); the Fano plane's
automorphism group `PSL(2,7)` of order `168` is
[T-256](./one-grammar.md#теорема-классификация-карт); and the octonionic Jordan ceiling
(`ℋₙ(𝕆)` formally real iff `n ≤ 3`), the third and algebraic derivation of
`SAD_MAX = 3`, is
[T-268](../../consciousness/hierarchy/depth-tower.md#критическая-чистота-sad). This
Part's own labs (`architecture/symbolica_*.py`) reconstruct the same `G₂ = Aut(𝕆)`
from the Fano form independently — an accidental cross-check between the applied
synthesis and the corpus's theorems. So where a tradition is read here as a shadow of
that apparatus, the *apparatus* is `[Т]`; only the reading is `[И]`.

### 76. The seven and the twelve are one object

For two thousand years astrology carried two numbers whose kinship it never
explained: seven moving lights and twelve fixed signs. The reconstruction's own
skeleton — the seven voices as the Fano plane, the octonions behind it — answers
the older puzzle too, and answers it with a single object.

Take `G₂`, the smallest of the five exceptional Lie groups and the automorphism
group of the octonions. Two facts about it are elementary once computed
(`architecture/symbolica_g2.py`). Its root system has exactly **twelve roots**,
and laid in the root plane they fall on exactly the twelve zodiacal
thirty-degree positions, `0°, 30°, … , 330°`. The roots come in two lengths, six
long and six short, and around the wheel they **alternate**, long–short–long: which
is precisely the alternation of sign polarity, the active and the receptive, that
the tradition has assigned Aries–Taurus–Gemini and onward since antiquity. The
twelve signs are the twelve roots of `G₂`.

And the group's smallest faithful representation is **seven-dimensional** — the
seven imaginary octonion units, which is to say the seven Fano points, which is
to say the seven voices. The seven classical planets are the weights of the
seven-representation of the same group whose roots are the signs.

One exceptional group carries both numbers at once. The seven and the twelve were
never two systems glued at the edges; they are one object — `G₂` — seen from its
two natural sides, the representation and the roots. The isomorphism is a
theorem `[Т]`; that the ancients were feeling their way toward an exceptional Lie
group, twenty centuries before Killing and Cartan named it, is the reading `[И]`.

### 77. The aspects are root angles; the wheel is one crystal over two fields

The correspondence does not stop at the counting. The angles the tradition calls
**aspects** are exactly the angles between the roots of `G₂`. Two roots of the same
length stand at `60°, 120°, 180°` — the sextile, the trine, the opposition, the
aspects the tradition calls *soft*, easy, flowing. Two roots of different length
stand at `30°, 90°, 150°` — the semisextile, the square, the quincunx, the aspects
it calls *hard*, tense, demanding. The astrologer's oldest felt distinction,
between an easy aspect and a difficult one, is the root-**length** distinction of
`G₂`: ease is a relation between likes, tension a relation between unlikes.

The **four elements and three modalities** fall out of the same wheel with no
further assumption. The twelve-fold ring is `ℤ/12 = ℤ/4 × ℤ/3`; its order-three
orbits are the trines — four signs of one element a hundred-and-twenty degrees
apart — and its order-four orbits are the squares — three signs of one modality
ninety degrees apart. Fire is a `ℤ/3` orbit; the cardinal cross is a `ℤ/4` orbit;
the zodiac's fourfold-by-threefold classification is the factorization of its own
cyclic group.

And here the two threads of this corpus meet. The octonions have automorphisms
over any field. **Over the real numbers** that automorphism group is `G₂`, and its
shadow is the continuous wheel: seven planets, twelve signs, the aspects between
them — astrology. **Over the field of two elements** the seven imaginary units
become the seven points of the Fano plane, and the collineations of that geometry
are `GL(3,2) = PSL(2,7)`, the group of order `168` that fixes the seven voices and
their twenty-one coherences — the reconstruction (Part IX). Astrology lives on the
real shadow of the octonions; the seven voices live on the binary shadow. They are
not analogous systems that happen to rhyme. They are one algebra — the octonions —
read through two different fields, and this is the seam where the perennial wheel
and the crystal of voices are shown to be the same crystal.

*(Verified as computation: `architecture/symbolica_g2.py` builds the `G₂` root
system explicitly and checks each claim — the twelve roots at thirty-degree
spacing, the long/short alternation, the seven-weight representation, the Weyl
group `D₆` of order twelve, the aspect angles as inter-root angles, and the
`ℤ/4 × ℤ/3` element/modality factorization. The two-field statement is standard:
`Aut(𝕆/ℝ) = G₂`; the Fano plane of the imaginary units mod 2 has collineation
group `PSL(2,7)`.)*

### 78. The I Ching is the binary shadow

Human Design, from which this reconstruction draws its natal sensor, is built
directly on the I Ching: its sixty-four gates are the sixty-four hexagrams. So the
oldest of the divinatory systems is not a distant cousin of the crystal — it is
the crystal's own foundation, and its combinatorics are exactly the octonion
structure seen over the field of two elements.

A trigram is three lines, each broken or whole — three bits — so the eight
trigrams are the eight elements of `F₂³`, the octonion basis. And the I Ching's
own millennia-old classification of them, the *family* — mother, father, three
sons, three daughters — is precisely the Hamming-weight grading of `F₂³`: the
mother `☷` is all-yin, weight zero, the origin; the three sons carry one yang line
each, the three basis vectors; the three daughters carry two, the three pairwise
sums; the father `☰` is all-yang, weight three, the sum of all. The Chinese sages'
family of eight is the graded octonion basis, name for name.

The correspondence is sharper than a labelling. The octonion units do not
merely *sit* on `F₂³` — they *multiply* by it: `e_a·e_b = ±e_{a⊕b}`, the
product of two units always lands on the line-wise sum of their trigrams, and
the whole algebra is the group algebra of the trigram group twisted by a sign
(verified by direct Cayley–Dickson computation in `symbolica_trigrams.py`: all
sixty-four unit products land on the XOR of their indices, and the associator
`(e₁e₂)e₄ ≠ e₁(e₂e₄)` witnesses that the sign twist is exactly what carries the
octonions' nonassociativity). The family is then not a grading only but an
arithmetic: two sons compose to a daughter (`☳⊕☵=☱`), a son with his
complementary daughter composes to the father, and each such identity the
tradition states is a theorem of the sum. Even the *Earlier Heaven* circle of
Fuxi — the pre-Zhou arrangement of the eight around a ring — places exactly the
complement pairs opposite one another: Heaven against Earth, Lake against
Mountain, Fire against Water, Thunder against Wind; four oppositions, each
summing to `☰`. `[Т]` throughout; the single convention is yin = 0.

The seven non-Earth trigrams are then the seven Fano points, and their
exclusive-or triples are the seven Fano lines — the same imaginary-octonion
triples that carry the twenty-one voice-coherences (Part IX). A full hexagram is
an upper trigram over a lower, a point of `F₂³ × F₂³ = F₂⁶`; the sixty-four gates
are the sixty-four such points, and the engine reads the planets into them. Where
astrology is the octonions' real shadow, the I Ching — and Human Design, and the
seven voices — is their binary shadow. `[Т]` for the structure; the
trigram-to-voice reading of *meaning* is `[И]`.

### 79. Kabbalah and Tarot alphabetise the same strata

The Sefer Yetzirah, the foundational text of Kabbalah, does not merely list the
twenty-two Hebrew letters; it **stratifies** them, and the stratification is the
crystal's. Three *mother* letters, seven *double* letters bound to the seven
planets, twelve *simple* letters bound to the twelve signs: three and seven and
twelve, and their sum is twenty-two — the alphabet, the twenty-two Major Arcana of
the Tarot, the twenty-two paths of the Tree of Life.

These are the crystal's own numbers. The seven doubles are the seven voices — the
Fano points, the planets. The twelve simples are the twelve signs — the `G₂` roots
of the last two sections. And the three mothers are the three already inside the
seven: the three quadratic residues modulo seven, `|QR(7)| = 3`, the generation
count `N_gen` (Sec. 66). The Sefer Yetzirah's `3 + 7 + 12 = 22` is the crystal's
stratification, alphabetised; add the ten Sephiroth — the Pythagorean tetractys
`1+2+3+4` — and the tradition's thirty-two "paths of wisdom" are `10 + 22`, ten
nodes and twenty-two edges on the same skeleton.

The counts are forced `[Т]`; the specific letter-to-planet and card-to-path
assignments are the schools' own, and they disagree, so we leave them `[И]` rather
than force one. What is not `[И]` is the architecture: Kabbalah and Tarot are not a
further system to be reconciled with the wheel and the hexagrams — they are the
same fabric written in a third script. Astrology reads it over the reals through
`G₂`; the I Ching reads it over `F₂` through the Fano plane; Kabbalah letters it.
One crystal, several scripts — which is what a superposition of the predictive
systems, done honestly and from the mathematics up, was always going to look like.

### 80. The atlas: one crystal in many scripts

Widen the aperture and the pattern does not thin — it thickens. The numbers that
organise the world's predictive systems are a short, closed list, and every entry
on it is an invariant of the same small structure.

The **heptad** returns everywhere seven closes on itself: seven planets, seven
metals, seven chakras, seven double letters, seven notes of the scale — the Fano
points, the octonion imaginaries, the voices. The **dodecad** returns wherever the
heptad's own group speaks: twelve signs, twelve months, twelve Chinese branches —
the roots of `G₂`. The **octad** is the octonions themselves, `2³`: the eight
trigrams, the three runic families of eight. And `2⁶ = 64` is two octonion shadows
stacked — the sixty-four hexagrams, the sixty-four Human Design gates, and, beyond
all divination, the sixty-four codons of the genetic code, `4³` bases that are `2⁶`
bits, the same lattice the I Ching drew, now found running life.

Even the systems that look least like a wheel are the crystal read differently.
The **Enneagram** is not a diagram to be taken on faith: its inner hexad, the
figure `1-4-2-8-5-7`, is exactly the repeating decimal of one-seventh —
`1/7 = 0.142857…` — and its triangle `3-6-9` is the multiples of three; the
Enneagram is the arithmetic of the heptad, drawn (Sec. 69). **Geomancy** is `2⁴`,
sixteen figures of four binary lines. **Numerology's** casting-out-nines is
arithmetic modulo nine, its master numbers the twenty-two of the alphabet.
**Music** is the clearest of all: seven diatonic degrees inside twelve chromatic,
and the circle of fifths — step seven semitones and you reach all twelve, because
seven and twelve are coprime — is the `7`-and-`12` of `G₂` heard rather than cast.

A few systems carry their own lattice, and we say so rather than force them: the
Maya's `260 = 13 × 20` is a torus of two coprimes that is not the octonion heptad.
That honesty is the whole method. This is not the old game of declaring everything
secretly the same; it is a **ledger**, each correspondence marked `[Т]` where the
structure is exact, `[С]` where it is a real but looser match, `[И]` where it is
only descriptive. What survives the ledger is a genuine core: the octonions and
their shadows — `G₂` over the reals, the Fano plane over `F₂`, the powers of two —
are the body under an astonishing number of the shadows the species has drawn, from
the zodiac to the genetic code to the gauge groups of the Standard Model, through
the same exceptional chain `𝕆 → G₂ → E₈`. The reconstruction does not add a system
to the pile. It names the body, once, in one vocabulary — the seven voices — and
keeps the ledger honest.

*(`architecture/symbolica_atlas.py` tabulates the spectrum with its status marks;
the sharpest checks run on the spot: `142857 × 7 = 999999`, the Enneagram as `1/7`;
`2⁶ = 4³ = 64`, the hexagrams as the codons; `gcd(7, 12) = 1`, the circle of
fifths.)*

### 81. The same body, doing physics

There is one more script, and it is the one a sceptic will least expect: the
visible universe. Everything Part XXI has read in the occult systems — the
octonions, their automorphism group `G₂`, the Fano plane, the group `PSL(2,7)`,
the three that live inside the seven — is the very apparatus from which the corpus
derives fundamental physics. Not an analogy to it. The same objects.

Turn to the corpus's own *G₂-Structure and the Fano Plane* and *Standard Model
from G₂*. There, `G₂ = Aut(𝕆)` acts on the seven coherences `{A,S,D,L,E,U,O}`
exactly as it acts on the octonion imaginaries; the colour group `SU(3)_C` appears
as the **stabiliser of the time direction** inside `G₂` (Cor. 1.1); the
electroweak sector is fixed by the Fano-electroweak construction; and the number of
fermion generations is **three** (Thm 3.3, the *count* being the `[Т]` part) — the
same three that is `|QR(7)|`, the same three the Enneagram's triangle draws and the
Sefer Yetzirah counts as its mother letters. The generation-selection principle is
governed by `PSL(2,7)` (the order-`168` automorphism group of the Fano plane; Thm
8.1) — the same group the two-field shadow (Sec. 77) produced from the Fano plane
over `F₂`.

So the chain closes. Read the octonions over the reals, and their group `G₂` casts
the twelve zodiacal roots and the aspects of astrology. Read them over `F₂`, and
the seven Fano points cast the trigrams of the I Ching, the doubles of the
alphabet, and the seven voices. Read them as the corpus does — as the symmetry of
a physical gap field — and the same `G₂`, the same Fano lines, the same
`PSL(2,7)`, the same generational three cast the gauge group `SU(3) × SU(2) × U(1)`,
the fermion families, and the CKM phase. One crystal; the zodiac, the hexagrams,
the Tree, and the Standard Model are its shadows on four screens.

This is the sense — and the only rigorous sense — in which the subtle fabric and
the visible universe "develop by the same principles." It is not that the stars
push. It is that the *mathematics of completeness* is small, exceptional, and
singular: there is essentially one maximal normed division algebra, one seven-point
projective plane, one simple group of order `168`, and any structure — a physics or
a divination — that reaches for the complete, closed set of qualities is driven onto
the same short list of invariants. The ancients drew the shadows without the
algebra. The corpus supplies the algebra, and finds it already load-bearing under
the physics. The reconstruction's task is finished when the two are spoken in one
vocabulary — which is what this long reconstruction has tried to do.

*(The physics claims cited here are the corpus's own, carrying their own status;
see [G₂-Structure and the Fano Plane](../../physics/gauge-symmetry/g2-structure.md)
and [Standard Model from G₂](../../physics/gauge-symmetry/standard-model.md).
Part XXI adds no physics — it observes only that the crystal it read in the occult
systems is the crystal already there, holding up the world.)*

### 82. The inner side, and what calibrates it

One question has stood open since the corpus's chapter on the hard problem, and it
states it plainly: of everything about experience, one thing is *not* fixed by
structure — the **calibration**. The theory proves (by Yoneda) that a quale's
identity is its relational position, and that the phenomenal functor `F` is
**faithful on `G₂`-orbits**: two systems feel identical exactly when their matrices
differ by a `G₂ = Aut(𝕆)` transformation. So the inner life a system has is its `Γ`
*modulo* `G₂` — the `G₂`-invariant part. What the corpus then honestly declares open
is the one thing `F` is blind to: the choice of representative *inside* the orbit,
the `G₂`-**frame**. "Which position is red" is not relational; it is the frame.

Now recall Sec. 76: the real form of that same `G₂` casts the zodiac — its twelve
roots are the signs, its seven-dimensional representation the planets. So the frame
`F` cannot see is coordinatised by precisely the seven-and-twelve skeleton the
astrologers drew. And this dissolves the last discomfort about what a
birth-configuration could possibly be *for*. It is not a cause. It is a
**calibration**: the external, physical boundary conditions into which a life is
thrown — the type and composition of its planetary system — fix the `G₂`-frame, and
the frame is exactly the freedom the inner structure leaves open. The stars do not
push the psyche; they *coordinatise the gauge* that the psyche's own relational
geometry cannot fix from within.

This is the dual-aspect monism the corpus already holds, carried one step further.
`Γ` has an outer side (physics) and an inner side (experience); they are one object.
What Secs. 76–81 add is the shape of each side and the map between them: the inner
side is the `G₂`-invariant crystal — universal, the same seven voices in every
system that instantiates it (this is what *monism* means — one architecture
underneath); the outer side is that crystal in a particular frame, and the frame is
set locally, by the cosmos the system is embedded in. The invariant is shared; the
calibration is local. That is why the same seven-fold and twelve-fold structure
recurs across every tradition (Sec. 80) — it is the invariant — while each
individual chart is unrepeatable — it is the frame.

There is even a reason the calibration *must* be local, not merely that it happens
to be. A global intrinsic calibration — one consistent rule assigning "which
position is red" across every configuration at once — would be a continuous global
section of the orbit map, and such a section exists only if the group acts with a
single orbit type. It does not. Building `G₂` explicitly as the stabiliser of the
octonion Fano form and computing the orbit dimension directly
(`architecture/symbolica_frame_bundle.py`, which also re-derives `dim G₂ = 14` from
the form), the isotropy *varies*: the maximally mixed centre is fixed by all of
`G₂` (orbit dimension `0`), a pure state by a three-dimensional subgroup (orbit
`11`), a generic state by nothing (orbit `14`). And this is the *whole* picture:
sweeping all fifteen spectral types of `Γ` — the partitions of `7`
(`architecture/symbolica_stratification.py`) — the orbit is the full `14` (a locally
free action, discrete stabiliser) for **every** non-degenerate `Γ`, collapsing only
at those two loci: the centre `[7]` (orbit `0`) and the single-distinguished-direction
type `[6,1]` (orbit `11`). So calibration is generically the *whole* of `G₂` —
fourteen independent parameters, no redundancy — and `𝒟(ℂ⁷)/G₂` is a **stratified**
space of exactly three orbit-dimension strata, not a manifold; the orbit map is no
global bundle, and there is **no global slice**: no global calibration `[С]`. The frame can be fixed only
*locally*, near each configuration. So "the environment sets the calibration" is not
an optional metaphysical extra — it is the natural filler of a hole the geometry
forces to be there: *something* local must choose the frame, because nothing global
can.

Two honest consequences follow, and they strengthen the theory rather than decorate
it. First, it **sharpens the corpus's own open question**. "Which quale is red" was
listed as an unexplained empirical residue, on a par with the electron mass; it can
now be named exactly — it is the `G₂`-frame, the `≤ 14` real parameters `F` is blind
to `[С]` — and a *source* can be proposed for it: the external boundary data `[Г]`.
An open question with a named structure and a candidate mechanism is a stronger
question than a shrug. Second, it yields a genuine **monist prediction** `[Г]`: a
mind arising in another planetary system — a different star, a different composition
— would instantiate the *same* inner crystal under a *different* frame. Its beings
would draw a different zodiac and read a different sky, and underneath they would
have the same seven voices, because the inner architecture is `G₂`-invariant and
only the calibration is local. Everything with an outer side has an inner side; the
inner side is one architecture; and the endless variety of the visible cosmos is the
endless variety of frames upon it.

*(`architecture/symbolica_calibration.py` verifies the accounting: `dim G₂ = 14`
frame parameters against the `48` of `Herm₀(7)`; the twelve roots and rank-two
Cartan; and the identification of the calibration residue with the frame `F` is
faithful modulo. The `G₂`-faithfulness of `F` is the corpus's own theorem — see
[Two-Aspect Monism](../../consciousness/foundations/two-aspect-monism.md).)*

### 83. Life as a symbolic-energo-informational system

You put the widest version of the thesis this way: if a planetary system can give
rise to life, and life is at bottom a *symbolic-energo-informational* system —
calibrated on its outer face by the type and composition of that planetary system,
while its inner face is the universal architecture — then the reconstruction is not
describing a metaphor but the actual seam of the world. Read against the corpus, the
intuition is exact, because each of its three words is a reading the corpus already
carries of the one primitive `Γ`.

**The three faces are already in the primitive.** "Energo-informational-symbolic"
is not three systems glued together; it is `Γ` seen three ways. *Energetic*: the
external, physical aspect — `Γ` as physics, and specifically as a **driven-
dissipative** process, held up against decay by a regeneration term. *Informational*:
the coherences `γ_ij` themselves — the correlations whose integration is measured by
`Φ`. *Symbolic*: the internal aspect — the seven voices, the meaning-frame, the
interiority that two-aspect monism places on the inner side of the very same object.
One `Γ`; an energetic outside, an informational structure, a symbolic inside. `[С]`
(a reading of established structure, not a new claim).

**What makes it alive is already a theorem.** The corpus does not leave
"self-maintaining" as a metaphor. A configuration persists only when its
regeneration `ℛ` overcomes dissipation `ℒ₀`, and the regeneration gain switches on
**exactly above the critical purity** `P_crit = 2/7` `[Т]` — below it a
configuration inevitably disintegrates; above it, it holds itself together, gain
against loss, a flame or a laser above threshold rather than an isolated decay (see
[viability](../../core/dynamics/viability.md) and the [regeneration
form](../../core/dynamics/evolution.md#вывод-формы-регенерации)). *That* is the
physical signature of life: a symbolic-energo-informational knot that regenerates
its own coherences faster than the world erodes them. "Our planetary system gave
rise to life" becomes precise — it supplied the conditions for a patch of `Γ` to
cross `2/7` into self-regeneration. `[Т]` for the threshold and the regeneration;
`[Г]`/`[И]` for identifying this crossing with biological abiogenesis.

**Calibrated by the planetary system — twice.** The planetary environment enters on
two channels, both already in the theory. It supplies the **energy gradient** that
keeps `ℛ` above dissipation — the *driven* in driven-dissipative, the star a living
system feeds on. And it supplies the **boundary data** that fixes the `G₂`-frame —
the calibration of Sec. 82, the sky a chart records. Substrate to stay alive; frame
to be *this* life and no other. `[С]` for the frame (Sec. 82); `[И]` for the
energy-gradient reading (ordinary non-equilibrium thermodynamics, in UHM's own
language).

**The monist reading, made precise.** Two-aspect monism already holds that *every*
`Γ` has an inner side — interiority at `L0`, for all systems. Life is where that
inner side becomes **self-maintaining** (`P > 2/7`) and, higher still, **cognitive**
(`R ≥ 1/3`, `Φ ≥ 1`, `D ≥ 2`, all `[Т]`). So your closing intuition — *everything
has an inner side, and the inner side is architecture and symbolic systems* — is
exactly two-aspect monism sharpened by the crystal: the inner side is not formless
experience but the **structured seven-voice architecture**, universal by
`G₂`-invariance, and life is the universe folding a patch of itself into a
self-maintaining knot that carries that architecture — dimly at first, then, past
the thresholds, consciously. Another planetary system, with another star and another
chemistry, would fold a different knot: the same seven voices, a different
calibration, a different substrate — a different **dialect** of the one inner
architecture.

None of this adds machinery. It names, in a single breath, three results the corpus
proves separately — that `Γ` has an energetic, an informational, and a symbolic
reading (two-aspect monism with `Φ`); that it lives by regenerating above `2/7`
([viability](../../core/dynamics/viability.md)); that its frame is externally set
(Sec. 82) — and observes that your one sentence, *life is a symbolic-energo-
informational system whose inner side is a universal architecture calibrated by its
cosmos*, is those three results read as one.

### 84. The ideal self-description: what a holon can say about itself, and how much it does

A symbolic system that strives toward its ideal self-description sounds like a
programme without an end. It is not: for a holon the target is finite, and it can
be counted.

The state is `Γ ∈ D(ℂ⁷)` — a unit-trace positive Hermitian `7×7` — so it carries
exactly `48 = 7² − 1` real parameters ([definitions](../coherence-cybernetics/definitions.md)).
And because **seven is prime**, the maximal family of mutually unbiased bases
exists and has exactly `d + 1 = 8` members (Wootters and Fields, 1989). Eight
bases give `8 × 6 = 48` independent probabilities, and `Γ` is recovered from them
in closed form,

$$
\Gamma \;=\; \sum_{b=1}^{8}\sum_{i=1}^{7} p_{b,i}\,|b,i\rangle\langle b,i| \;-\; I .
$$

So «an ideal self-description» is not an aspiration but a **constructible finite
object [T]**: forty-eight numbers, optimally arranged in eight bases. Any account
a holon gives of itself can be measured against that ceiling. (The arithmetic is
the one the heptacode's syndrome census already whispered — eight families over a
seven-letter alphabet.)

The ceiling is lower than forty-eight, though, and the corpus already says why.
The phenomenal functor is faithful only on `G₂`-orbits ([T-123](../../proofs/consciousness/conscious-window.md#t-123),
[two-aspect monism](../../consciousness/foundations/two-aspect-monism.md)), and
`dim G₂ = 14`, so fourteen of the forty-eight directions are frame, not content:
**thirty-four parameters are distinguishable in principle.**

**What the natal encoder actually reaches.** Measured across the §75 population
(2340 charts, 1940–2004 × 12 months × 3 times), as the participation ratio
`PR = (Σλ)²/Σλ²` of the feature-correlation spectrum
(`core/examples/self_description.rs`):

| subspace | parameters | effective dimensions | PC1 |
|---|---|---|---|
| diagonal — the voice levels | 7 | **5.1** | 31.5 % |
| off-diagonal real parts | 21 | 18.5 | 9.0 % |
| off-diagonal imaginary parts | 21 | 17.4 | 10.6 % |
| coherence magnitudes (the §75 view) | 21 | 16.6 | 12.3 % |
| **the full state vector** | **48** | **35.4** | 7.0 % |

*Numbers re-measured 2026-07-28.* The table previously read `4.0 / 18.1 / 16.9 /
16.7 / 32.3`. Those were taken before the encoder's diagonal was pinned
(`pin_diag`, default since 2026-07-27); with the pin switched off the probe
reproduces them exactly (`32.5`, magnitudes `16.7`), which identifies the cause
precisely. Both readings below are unchanged in direction and one of them gets
stronger.

Two things follow, one of them a correction of our own earlier reading.

**The phases carry half the state.** §75 measured the interpretation-feature
vector — levels, gains, `razlad` and coherence *magnitudes* — and found an
effective dimension of `17.3`. That measurement replicates here exactly
(magnitudes alone: `16.7`), which is a welcome independent confirmation through a
different code path. But magnitudes are only half of the off-diagonal content:
the `42` real numbers of the off-diagonal split `21` real and `21` imaginary, and
including the phases lifts the effective dimension from `16.6` to `35.4` — it
more than doubles. §75's number was right about the object it measured and
undercounts the *state* by about a factor of two. The personal detail we said
lives in the coherences lives, half of it, in their **phases**.

**The reached dimension does NOT sit on the gauge-free ceiling — the
conjecture is refuted [✗], now doubly.** The measured `35.4` no longer stands
*close to* `34 = 48 − dim G₂` — it **exceeds** it, which alone makes the
frame-fixed reading impossible: an encoder confined to the gauge-free quotient
could not explore more directions than that quotient has. On the earlier figure
of `32.3` the reading was merely tempting, and we first read it forward: perhaps the natal encoder is
frame-fixed and explores about `95 %` of everything a holon could differ in. The
test was stated and then run (`core/examples/g2_gauge_test.rs`). Build `𝔤₂` as
the stabiliser of the associative 3-form inside `𝔰𝔬(7)` — taking `φ` from the
corpus's own canonically oriented Fano wiring, which self-checks by yielding
exactly `dim = 14` — form the orbit tangents `[X, Γ]` at each chart, and ask what
fraction of the population's variance lies along them:

| | share of variance along `G₂`-gauge directions |
|---|---|
| conjecture (encoder frame-fixed) | 0 % |
| **measured** (2340 charts, 117 base points) | **28.8 %** (range 26.1–31.5) |
| isotropic null (scatter indifferent to gauge) | 29.2 % |

The measurement lands on the null. **The natal encoder does not fix a frame**:
its image is not transversal to the gauge orbits, and the population's scatter
fills the gauge directions as readily as any others. The closeness of `32.3` to
`34` was a coincidence, and the `95 %` reading is withdrawn.

What replaces it is sharper and less comfortable. The phenomenal functor is blind
to the frame ([T-123](../../proofs/consciousness/conscious-window.md#t-123)), so a
difference between two charts that lies along a gauge direction is a difference
**no experience can register**. Roughly `28 %` of natal chart-to-chart variation
is of that kind: real in the parametrisation, invisible in the phenomenology.
Individuality as computed from a birth chart is therefore smaller than the raw
`32.3` dimensions suggest — a bound we now have a number for, and one that no
amount of better writing can recover.

**Where the description is actually lost.** Setting the links side by side gives
the honest chain — and it does not fall where one would guess:

| link | dimensions | of the previous |
|---|---|---|
| the state's parameters | 48 | — |
| distinguishable in principle (`48 − dim G₂`) | 34 | 71 % |
| reached by the natal encoding | 32.3 | — |
| …of whose variance is phenomenally visible | ≈ 72 % | (28 % is frame) |
| named as signals by the engine | 22 | — |
| reaching the plain-language reading | 9 | 41 % |

Two losses, then, of different kinds: the capture spends about a quarter of its
variation on the frame — a bound no writing can undo — while **the telling loses
most of what survives.** The engine
computes a thirty-two-dimensional object and speaks nine of its named signals to
an ordinary reader, keeping the rest in a machine register behind a flag. That is
why the interpretation work is not copy-editing: raising what the readings carry
is precisely raising the system's own self-model fidelity, the quantity the
corpus calls `R_φ` ([the three forms of R](../../consciousness/foundations/self-observation.md#формы-r)),
applied to the system rather than to the person it describes. A symbolic system
striving toward its ideal self-description, made operational, is exactly this
number moving toward one.

**And the remaining directions have only one road.** Whatever the natal
encoding cannot reach — and whatever changes after birth — is reachable only by
measurement in time: the diary as state tomography. The protocol is not a
sketch; it is built and checked (`core/examples/tomography.rs`). The eight bases
are verified mutually unbiased to `1.7·10⁻¹⁶`, the closed-form reconstruction
returns real charts to `1.6·10⁻¹⁵`, and the structural fact that makes a partial
diary worth anything is exact: each basis contributes a **six-dimensional block**
of the state space, and the eight blocks are mutually orthogonal to `1.2·10⁻¹⁶`.
So `48 = 8 × 6` with no redundancy — no basis repeats what another has already
said, and measuring `k` of them is not a blurred picture of everything but an
**exact** reading of a `6k`-dimensional slice.

That gives the living layer a price list, and the price list carries a sting:

| bases measured | parameters fixed | residual variance | fair share would be |
|---|---|---|---|
| 1 | 6 | **93.0 %** | 87.5 % |
| 2 | 12 | 81.4 % | 75.0 % |
| 4 | 24 | 47.9 % | 50.0 % |
| 6 | 36 | 22.8 % | 25.0 % |
| 8 | 48 | 0.0 % | 0.0 % |

The first basis is the computational one — the seven voice levels, which is
exactly what the diary already asks for. And it is the **weakest** of the eight:
it fixes `6` parameters but removes only `7.0 %` of the variance where an average
basis removes `12.5 %`. The voice levels are the least informative question the
instrument could ask. This is the same finding as the phases, seen from the other
side: what individuates a person is not how loud each voice is but how the voices
stand in relation, and relation is phase. A diary that asks only «rate your seven
voices» measures the flattest slice of the state; two or three well-chosen
relational questions would learn more per question than the current seven do.
Designing them — turning the non-computational bases into things a person can
actually answer — is the open work of the living layer `[О]`, and it is now a
well-posed problem rather than an aspiration.

### 85. Two walks through the sixty-four: the book and the wheel {#два-хода-по-64}

Terence McKenna's *Time Wave Zero* earns its place in this part not by its famous
failure but by its structural core. The construction took the King Wen sequence —
the canonical *order* of the sixty-four hexagrams — measured how many lines change
from each hexagram to the next, and read the resulting profile as a **dynamic of
novelty**, unfolded onto a 384-node grid (64 hexagrams × 6 lines; McKenna also
prized the near-coincidence 13 × 29.53 ≈ 384 days of the lunar year). The terminal
date the wave pointed at was refuted by the calendar itself `[✗]`. What survives
the refutation is the question the construction actually poses: **is a canonical
ordering of the sixty-four statistically special — and in which direction?** That
question is exact, and our architecture happens to carry *two* canonical orderings
of the same nodes — the book's and the wheel's — so it can be answered twice
(lab: `architecture/symbolica_timewave.py`).

The grid itself is shared: 384 = 64 × 6 is also the lattice of the wheel's
line-divisions, which the Sun crosses in one year (about a line per day) and the
Moon in one sidereal month. But a shared lattice is shared *combinatorics* — `2⁶`
states, six lines each — and nothing more `[Т]`; whatever else the two systems
have in common must be looked for in the walks. Define the novelty step
`h(i)` as the number of lines changed between consecutive nodes of a walk, and
compare each canonical walk with 20 000 random orderings of the same nodes:

| walk | mean step | step spectrum {h: count} | lag-1 autocorrelation | z of mean vs null |
|---|---|---|---|---|
| random orderings | 3.05 ± 0.15 | spread around 3 | −0.03 ± 0.12 | — |
| the book (King Wen) | 3.34 | {1: 2, 2: 20, 3: 14, 4: 19, 6: 9} | −0.26 | +2.0 |
| the wheel (year order) | 1.81 | {1: 34, 2: 16, 3: 8, 4: 4, 5: 2} | −0.57 | −8.4 |

Two findings, in opposite directions. The book is *mildly* special, toward
larger, alternating steps: its well-known pair mechanism — every odd hexagram
followed by its turn-over, or by its inversion when the figure is symmetric —
makes within-pair steps large (mean 3.75) against ordinary between-pair steps
(2.94); no step of size 5 occurs at all, and the nine full inversions (h = 6)
are exactly the symmetric pairs. It is a **narrative** order: it dramatises
opposition. The wheel is special by an order of magnitude more, and the other
way: more than half its steps (34 of 64) change a *single* line, none change all
six, and the spectrum falls by almost exactly a factor of two per added line —
`34·16·8·4·2` against the exact halving `32·16·8·4·2`. The spectra are exact
counts `[Т]`; the z-scores are empirical against a fixed ensemble `[С]`. The
wheel is a near-Gray walk — the year unfolds by minimal mutations — which
sharpens the earlier Gray-code observation on the wheel from the Human Design
audit into a quantitative law of decrease.

The principle, named: **the book and the wheel are two walks on one crystal.**
The nodes are shared — the same sixty-four doors with the same voice-readings
(§80) — but the *order* is a second, independent layer of meaning, and the two
canonical orders encode opposite temporal characters: the book walks like a
story, by confrontations — large, anticorrelated steps, opposition pairs; the
wheel walks like a calendar, by growth — smallest possible steps, smooth
unfolding. McKenna's «novelty» is therefore a property of a *walk*, not of the
nodes; the honest core of his intuition is that different walks through one
symbol-set carry different, measurable temporal signatures — `[С]` for the
numbers above, `[И]` for reading step-size as novelty. In our reconstruction the
labour is split accordingly: the doors' meanings live on the nodes, the year's
dynamic lives on the wheel-walk (themes hand over gradually, each door differing
from its neighbour by about one line), and the book-walk survives *inside* the
nodes as pairing structure — the involutions and nuclear roots of Part XVI.
Neither walk is «the true one»: they are two projections of the crystal into
time, a narrative one and a cyclic one — and the Mawangdui manuscript order
supplies a third with its own signature (block-sorted by trigram families:
steps of mean 1.75 inside a block, 3.25 at the seams; z = −7.6 against the
same null): a *catalogue*. Story, calendar, dictionary — three canonical
modalities of one crystal, each measurably non-random in its own direction.

### 86. The interior ladder: the four gates as a route, and the capture boundary {#интериорная-лестница}

The corpus defines consciousness by four gates — purity inside the window
`P ∈ (2/7, 3/7]` (T-124), reflection `R ≥ 1/3`, integration `Φ ≥ 1` (T-129),
differentiation `D ≥ 2` (T-151) — and treats them as a static conjunction. The
psychedelic corpus, read through the reconstruction, turns the conjunction into
a **route**: the stages of a dissolution are the gates failing in order, and the
return is the same gates recovering in reverse. One identity does the heavy
lifting, and it was already in the canon: with the canonical `R = 1/(7P)`, the
upper edge of the window and the reflection threshold are the *same point*,

    P > 3/7  ⟺  R = 1/(7P) < 1/3   `[Т]`

— so «ego death», the failure of self-observation, is not a separate event but
the exact crossing of the window's upper edge. What the tradition reports as
losing oneself, the algebra states as purity leaving the band where a
self-model can still watch.

The order of the remaining stages is not universal, and that is the finding
(lab: `architecture/interiority_lab.py`, an honest toy of the porosity
dynamics, with its three instrument artifacts caught and documented along the
way — total porosity, a connectivity marker degenerate on disconnected graphs,
and a start state that violated `D ≥ 2`). The route is a **function of the
porosity profile** — how fast the world's entry widens across channels versus
how deep it presses. A wide fast profile (all channels open almost at once)
reaches *unity first*: `D → 1` at mean step 39 of 80, connectivity doubling at
49, the window's edge only at 75 — union arrives while the observer still
stands, which is the DMT-like breakthrough phenomenology (56 of 60
trajectories). A narrow slow profile orders it the other way: connectivity
first (61), the edge second (75), full union last (79) — the long
«everything is connected» phase, then dissolution, then oneness at the peak:
the psilocybin-like route (43 of 60). Same crystal, same gates; the substance
chooses the profile, the profile chooses the order `[С]`.

Two more results anchor the phenomenology. First, the report «more real than
reality» has a carrier in the model `[С]`: inside the unity window the mean
off-diagonal coherence stands at ×8.6 its baseline (60 of 60 trajectories put
the connectivity maximum inside unity) — super-integration with collapsed
differentiation is precisely a state *more coherent than the ordinary one*,
and the mind reports it as excess reality. Second, the entity question is put
as a discriminating test rather than an opinion: if entities are detached
modes of the person's own self-model, their profile should correlate with the
person's *quiet* voices (the unheard returning as Other); if they are external
fragments entering through porosity, with the person's *open* channels. The
toy model cannot decide this — a passive-input dynamics answers «world» by
construction — so the question is preregistered for report corpora with natal
data `[О]`; it is observable and falsifiable.

The same crossing guards the social layer. Model propaganda as an external
rank-one source — «one thought», a maximally pure state — fed through open
channels with repetition (lab: `architecture/holarchy_ladder_lab.py`). Capture
turns out percolative: a pressure threshold below which it does not spread,
and the population's true defence is not its starting distribution (that
version was refuted by its own numbers and stands as an errata in the lab) but
the **living filter**: while `P` stays inside the window, `R ≥ 1/3` damps the
repetition, and the full filter doubles the pressure threshold. The boundary
of vulnerability is the same line as above: captured is possible when
`P > 3/7`, i.e. `R < 1/3` — **capture and trance are one door opened from two
sides** `[С]` for the toy, `[Т]` for the boundary identity. A tradition that
trains presence in the window trains, in the same gesture, immunity to
capture; a system that pushes a population toward one pure thought walks it,
in the same gesture, out of the conscious band. The susceptibility claim also
carries an external anchor `[С]`: across 137 autocratic-regime onsets of the
Geddes–Wright–Frantz registry with World-Bank coverage, per-capita growth in
the three years to the start runs 1.70 points below the country's own norm
(z = −4.3 against a within-country null; the anticipatory window that excludes
the start year still holds z = −2.6), while the same test against *global*
shocks returns zero — capture follows the local depletion of its field, not
the world's waves, which is the social twin of the point-not-population
theorem (§75c).

Grof's perinatal sequence falls out of the same construction. From several
thousand LSD protocols Grof distilled a stable order — serene unity (BPM I),
no-exit compression (BPM II), titanic struggle (BPM III), death-rebirth into
light (BPM IV). The perinatal *causality* — that these are memories of birth —
remains disputed `[И]`; the sequence itself is a reproducible corpus invariant
`[С]`, and in the reconstruction it is the **resistance curve of the gate
route**: define suffering(t) as the entry pressure times the still-living
reflection filter, and the model puts its peak strictly between the
«everything connects» phase and the window's edge — BPM II–III, the filter
holding against the press — in 43 of 43 narrow-profile and 58 of 58
wide-profile trajectories. On the narrow route the tail after unity holds 6 %
of the peak: the catharsis of BPM IV, no one left to suffer. The prediction
that the narrow profile suffers *higher* was refuted by the model's own
numbers — the peaks are nearly equal; what distinguishes the routes is
**resolution**: the wide profile keeps 47 % of its suffering *inside* unity
(the terror-within-breakthrough of DMT reports), the narrow one converts it at
the moment of passage. This matches the Imperial triad of scales — challenging
experience as the area under the resistance curve, emotional breakthrough
(Roseman 2019) as the tail's conversion, mystical experience as the depth of
unity — with a preregistered corollary: breakthrough scores should track the
peak-to-tail *ratio*, not the peak `[О]`.

The route also runs backwards, and not symmetrically. Driving the porosity
through a full cycle (0 → 1 → 0, sixty trajectories) gives the return leg two
measured properties `[С]`: the gates recover at a porosity **smaller by
Δσ ≈ 0.16–0.19** than the one at which they failed — the world once let in
does not leave when the pressure is merely removed, so between the peak and
the re-closing of the gates there is a real **integration window**, which is
where the therapeutic work happens; and the recovery order is
last-fallen-first-restored in 75 % of trajectories — a tendency, not a law,
because on a narrow profile both gates fall almost together at the peak and
the return order is noisy. Integration, in other words, is not the trip
rewound: what opened at the peak closes on its own porosity and mostly in
reverse order.

The Klüver precedent frames the method. Thousands of subjective mescaline
reports condensed into four form constants; half a century later they proved
to be the plane-wave spectrum of a log-polar cortex — the lab reproduces that
derivation by direct computation. Reports → invariants → mechanism → theorem:
the interior ladder above is the same schema applied one level deeper, with
the gates of the reconstruction as the mechanism layer.

### 87. The five-mode chart: the spectrum of a natal Γ̂ and the personal blind plane {#пятимодовая-карта}

Ask the plainest spectral question the reconstruction allows: what are the
eigenvalues of a natal Γ̂? Across three thousand ephemeris charts spread
uniformly over 1940–2010 the answer has a shape no one ordered in advance
(`core/examples/spectral_gaps.rs`): the mean spectrum runs 0.499, 0.288,
0.154, 0.054, 0.004 (re-measured 2026-07-28 on the corrected defaults; it read
0.448, 0.275, 0.168, 0.088, 0.022 before the diagonal was pinned) — and then **nothing**: λ₆ and λ₇ are numerical zeros on
98.7 % of charts (the exceptions carry λ₆ ≤ 0.043). A natal chart is a
**five-mode object in a seven-voice space**: every chart owns a two-dimensional
subspace of voice superpositions it does not carry at all. The head of the
spectrum decays geometrically at ≈ 0.62 ± 0.13 per step — near 1/φ on average,
but with a spread wide enough that we file it as a tendency of means, not a
law. And the positional gap profile matches purity-matched random densities —
no «natural classes of modes» beyond the rank cut: what distinguishes the
population is the cut itself and the steep head.

Is the missing plane shared — two directions the encoder simply never feeds?
No (`kernel_probe.rs`): the mean kernel projector is nearly isotropic (its
seven eigenvalues sit between 0.23 and 0.34, all ≈ 2/7), so the blind planes
of different charts spray the whole space. The deficit is a **local law**:
each chart has its own personal blind plane.

The mechanism turned out to be one honest theorem of the construction
(`rank_origin_probe.rs`). The encoder assembles a raw matrix — the population
diagonal of trace one plus the β-weighted coherence structure of trace zero —
and ends by projecting onto the PSD cone with trace renormalisation. The raw
matrix almost always carries negative inertia: **(5+, 2−) on 72 % of charts,
(4+, 3−) on 27 %, (6+, 1−) on 1.4 %** — and that last figure independently
matches the 38/3000 rank-six charts of the first probe. So Γ̂ is the
renormalised positive part of the raw chart, and the personal blind plane is
precisely its clipped negative subspace — the directions where the coherence
structure outweighed the population. A quarter of the population carries a
*three*-dimensional blind space. Why is (5+, 2−) the typical inertia? The
phase diagram over β answers plainly: the working point β = 0.12 sits at the
**peak of the (5+, 2−) phase** (85 %), with (6, 1) below β ≈ 0.05 and (4, 3)
above β ≈ 0.15 — five-modedness is a property of the encoder's chosen working
point, standing at the maximum of its own phase `[С]`.

Two readings close the section. First, a caution: all of this is a statement
about the sky-plus-encoder structure — dates here are uniform draws, not
people, and no person-level claim is made `[С]`. Second, a refinement of the
window: on **89 %** of charts (62 % before the defaults were corrected) the
dominant mode alone already outweighs the upper
edge, λ₁ > 3/7, while the chart's purity stays inside the window because of
how the tail is distributed — consciousness, in this reconstruction, lives on
the **distribution of modes, not on the dominant one**. The product keeps its
discipline here: the blind plane is computable per person, but its meaning is
not yet earned, so it stays out of the readings until it is `[О]`.

**How the conditional gets settled.** «A property of the encoder's working
point» is a `[С]`, and a `[С]` that names no way of being wrong is a
decoration. Here the way is direct, because there exists a second Γ̂ that never
passes through the encoder at all: the one estimated from a diary, a
normalised covariance of daily marks. If five-modedness is a trace of the
encoder, that second matrix has no reason to show it; if it is a property of
the state, it shows it anyway. So the rank of the diary Γ̂ separates the two
readings, and it costs the observer nothing extra — the same sixty entries
already being collected for the three-way split answer this too.

The rule was fixed before the first entry: a mode counts as live if it carries
more than 1 % of the trace; **five or fewer live modes** reads as a property of
the state, **more than five** as an artefact of the encoder. The threshold is
not a guess. Power was computed first, on synthetic series of known rank: at
sixty days the instrument reads true rank 3 as 3 (99 % of runs), true rank 5 as
5 (87 %), and true rank 7 as 6 (73 %). The boundary was then chosen by
enumeration over the worst of the two error rates — `≤ 5` gives 16.5 %, while
`≤ 4` and `≤ 6` give 87 % and 89 % and were rejected. The instrument's known
bias is written into the rule rather than left implicit: at full rank it more
often finds six than seven, because the seventh mode falls under the 1 %
floor — so an outcome of «6» reads as full rank, not as near-five-modedness.
Verifier: `core/examples/diary_rank_prereg.rs`; the outcome appears on its own
at sixty days and stays silent before that `[С]`.

**The two outcomes are not equally informative, and saying so is part of the
preregistration.** A second probe asked what happens when this test sits
alongside the three-way split test that runs on the same entries
(`core/examples/prereg_independence.rs`). The two are not independent, and the
dependence is one-directional. Sweeping the purity of a three-factor series —
the weight `w` on the shared factor — the split lands on **92–100 % of runs
across the whole range from w = 0.4 to 0.9**, while rank switches abruptly:
five or fewer modes on 100 % of runs at w = 0.9, 87 % at w = 0.8, and **exactly
0 % already at w = 0.7**. So once the three-group structure is present, the
rank is not measuring the structure at all — it is measuring *how much of the
diary is not those three factors*. The reverse direction is clean: low rank
alone does not carry a series into the predicted split, which stays at the
blind 1.4–2.0 %, so the 1/70 declared for the split is unaffected.

Three consequences follow, all fixed before the first entry. First, **«more
than five» is the default outcome** over almost the whole noise range and is
therefore weak evidence on its own; **«five or fewer» is rare and strong**.
Second, when the split lands *and* rank comes out low, the two are **one
finding, not two** — the second follows from the first and must not be added to
it. Third, split-lands-with-high-rank is **not** a contradiction, as a naive
reading of the first probe suggested: it is the ordinary case below w = 0.8 and
reads as «the three factors are there and they are not the whole of it». The
product states each of these in the reading itself rather than leaving the
reader to add what does not add `[О]`.

**And the blind probability the other test rests on is true only by symmetry.**
The split test declares blind odds of 1/70. That holds if the seven voices are
exchangeable — no partition favoured over another. In self-report they are
never exchangeable: there is a **common day-factor**, and today being good
lifts all seven marks at once. A halo with *equal* loadings is harmless, since
it raises every correlation alike and all seventy partitions score the same.
A halo with sharply *unequal* loadings is not. If the wording of the questions
happens to make mood bite harder on Expression, Movement and Meaning than on
Form, Grounding and Unity, the predicted partition wins **from the questions**,
not from the metatraits. Measured on eight nulls that contain no metatraits at
all (`core/examples/halo_confound.rs`): seven independent voices land on the
predicted split 1.35 % of the time, an equal-loading halo 1.10 %, a halo plus
response style 1.55 % — all at the blind rate — while a loading skew of 0.35
gives **4.95 %** and a skew of 0.45 gives **16.6 %**, up to **11.6× the
declared 1/70**.

The discriminator turned out to sit in the spectrum of the same matrix. One
common factor is rank one: λ₁ takes nearly everything. Genuine metatraits are
*two* group factors plus a pivot, so λ₂ is comparable to λ₁. Among halos that
do land on the predicted split, λ₂/λ₁ runs 0.23–0.34; among genuine metatraits
it runs 0.81–0.84 — and, decisively, **it does not fall as the structure
weakens**: at w = 0.25 only 19 % of runs land at all, but those that land still
show 0.84. So the threshold cannot cut away weak-but-real structure. Chosen by
enumeration over the worst of the two errors: **λ₂/λ₁ ≥ 0.45, worst error
0.2 %**. Declared before the first entry: below that threshold a landing does
**not** count, however many days accumulate — what it would measure is how
differently the seven questions catch a mood, not the bridge to the Big Five
`[О]`.

The general lesson outlives this instrument. **A probability derived from
symmetry is true exactly as far as the symmetry holds in the data.** «One in
seventy, because there are seventy equiprobable partitions» is a statement
about the *enumeration*, not about people. It is checked by building nulls in
which the symmetry is broken deliberately and plausibly — and here that check
found a real hole and closed it before any data existed.

That rule has a sibling, and the two together cover most of what goes wrong
with a declared threshold. A significance level counts **one** route to the
right answer — the route the test intends. It is valid exactly when no other
route exists. The check mirrors the one above: enumerate everything a
respondent can see *without* doing the intended work — layout, ordering,
wording, length, any residue of how the material was assembled — and test each
against the key. A threshold survives only what it has been tried against `[О]`.

### 88. The information bound of the natal map: why every external null was forced {#информационная-граница}

Twenty-one parts have built a construction. This one measures what the
construction *can* carry, and the answer bounds everything above it. The
result is not statistical — it is read off the signature of a function.

**One input.** The state is assembled by `Chart::from_jd(jd)`: a single real
number, the moment of birth. Nothing else is passed. So the natal map is a
curve,

$$f : \mathbb{R} \longrightarrow \mathcal{D}(\mathbb{C}^7), \qquad jd \mapsto \Gamma,$$

whose image lives in a space of $d^2 - 1 = 48$ real parameters `[Т]`.

**Place does not enter the state.** Two people born in the same instant in
Reykjavik and in Melbourne receive an *identical* Γ — measured difference
$0.0\mathrm{e}0$, though the measurement is superfluous: the coordinates are
absent from the signature `[Т]`. Place lives only in the horizon layer
(`place::gauquelin_sectors`), never in the state. This is a falsifiable
disclosure, and the product now makes it on the `/place` page rather than
letting silence work as a promise.

**The map is very nearly injective.** Across 4000 random charts there are 3933
distinct gate sets (`natal_dimension.rs`). So `f` neither compresses nor
enriches: it is an exact **re-coding of one real number** into 48 coordinates.

**Hence the bound.** Because Γ is a deterministic function of `jd`, the data
processing inequality gives

$$I(\Gamma\;;\;X) \;\le\; I(jd\;;\;X)$$

for any property $X$ of the person `[Т]`.

No processing creates information about a person that the birth moment did not
hold. And the right-hand side is exactly what every external test measured:
15 931 Gauquelin celebrities with accurate times (η² < 0.5 %); sixteen
memoirists over 2.4 million words under frozen dictionaries (zero, the best
pair signed against); wars, revolutions and pandemics (null under two
statistics); three zodiac markings including thirteen unequal constellations
(all inside estimator bias); and the diurnal layer across 130 body × profession
pairs, whose top is occupied by bodies with no traditional claim at all —
including our own control body, Uranus over the military at +3.03.

So the null on the left needs no separate test: it **transfers** from the
nulls on the right, with no further assumption.

Precision matters here, or the statement over-claims. The inequality
*transfers* a bound; it does not manufacture a zero. Our tests are estimates
of finite power — they cap the effect, they do not prove its absence. The
correct sentence is: *whatever bounds the link from moment to person, bounds
the link from Γ to person at least as tightly.* That is what makes further
external testing of the natal layer pointless — the ceiling is shared and
already measured.

**Portrait of the image — and why it deceives.** Measured on the live path
(`use_v2 = true`), after a first pass had used the default, which then pointed
at a dead branch (§89): the image spans **40 of 48** linear directions at 90 %
of variance and 47 at 99 %, and its embedding dimension is **13.80** against
controls of 2.26 (a known curve) and 17.10 (a full 48-dimensional cloud). The
ruler is biased both ways — the known curve should read 1.0 and the full cloud
48 — so the *order* is what may be read, not the absolute.

The direction count needs the same treatment, and it did not have it. «Forty of
forty-eight» reads as wide coverage, but coverage is measured against
something. Four baselines on the same four thousand points settle it:

| ensemble | directions at 90 % |
|---|---|
| isotropic 48-dimensional cloud | 43 |
| curve from one frequency, random map | 29 |
| ten frequencies, random **linear** map | 8 |
| ten frequencies, random **nonlinear** map | 25 |
| **the natal curve** | **40** |

Two readings, pointing opposite ways, and both belong. **Against pure noise the
figure is a ceiling, not an achievement**: an isotropic cloud needs 43, so
noise spreads *wider* than the natal image does. **Against the matched null the
image does spread**: ten sinusoids through a random nonlinear map cover 25.
The linear null's 8 must not be read at all — a linear mixture of ten sinusoids
has covariance of rank exactly ten, and the encoder is nonlinear by
construction. Nor should the remaining gap of fifteen be read as «this much
structure»: the matched null here is merely quadratic, while the encoder passes
through trigonometry of angles and manufactures higher harmonics that lift the
rank on their own. Fifteen is an *upper* bound on what construction contributes.

And here is the instructive part. Geometrically the image is **rich**: nearly
fourteen-dimensional by that estimator, far closer to a full cloud than to a
curve. **And it carries exactly one number.** The richness is manufactured by
discreteness — gates, channels and centres jump at every boundary, so the image
is not a line but a scatter of almost four thousand pieces, one per chart
(3933 distinct gate sets across 4000). A scatter fills space and fools any
geometric ruler, yet holds no more information than the index of the piece —
and that index is fixed by a single `jd`. Geometric richness and information
content are different things, and the first promises nothing about the second.

**What the bound does not reach.** Formally two channels escape it; in
substance, one. **Place** is absent from Γ and therefore outside the
inequality — which invites calling it open, and that would be a mistake: the
diurnal landscape *was* the measurement of place, since `gauquelin_sectors`
takes latitude and longitude on its inputs, and it closed negatively. The
honest residue is that the outcome tested was *profession*; other outcomes are
formally untouched, and no data for them exists. **The diary** is the real
survivor: its input is the person, not the birth moment, and it is the one
place where the instrument has been checked against known truth (return times
0.83 → 0.85, 1.44 → 1.35, 2.80 → 2.82).

Nothing said in earlier parts becomes false. The natal layer was already
described as a frame, a prior, a language of distinctions, and that was
accurate. What changes is the standing of the description: until this section
it was **caution drawn from measurements**, and now it is a **consequence of
the construction** — which lets it be stated more calmly and more strongly.
Everything the system says from a chart is a function of one number. A frame
may be useful without being a measurement; it may not carry more than its
input `[Т]`.

### 89. Two encoder paths, two answers to the window {#перепись-окна}

The previous section bounded what the natal map can carry. This one asks a
blunter question of the same construction — **what does the encoder say about
real people, by the theory's own criteria?** — and the answer arrived only
after an error worth recording, because the error is the finding.

**The census, on 16 000 Gauquelin records with accurate birth times.** The
first pass used `EncoderCfg::default()` and reported that essentially nobody
passes: integration for 0.1 %, all four gates for 0.0 %. That conclusion was
wrong, because the default is **not** the path the product computes:
`use_v2: false` in the default, `use_v2: true` in the live config. Recomputed
along both:

| gate | v1 (the default) | **v2 (what runs)** |
|---|---|---|
| $P > 2/7$ | 40.0 % | **99.4 %** |
| $R \ge 1/3$ | 98.5 % | **87.6 %** |
| $\Phi \ge 1$ | 0.1 % | **90.8 %** |
| $D \ge 2$ | 100 % | **100 %** |
| **all four** | **0.0 %** | **78.4 %** |

Φ by quantiles: v1 — 0.000 / 0.270 / 0.581, max 1.350; **v2 — 0.932 / 1.289 /
1.730, max 2.621.**

**So the finding is not the one that was sought.** It is that the two paths
give **categorically different answers to the system's central predicate**:
one says nobody passes the window of consciousness, the other says three
quarters do. Not a discrepancy in the third digit — different answers to
«is this a living state by the theory's criteria» `[Т]`. And the path left as
the *default* is the one that is not in service, so any probe written against
the default silently measures a dead branch.

**On the live path the gates barely filter.** $D \ge 2$ passes 100 %,
$P > 2/7$ passes 99.4 %. A gate that admits everyone is ornament rather than
discrimination; only $R \ge 1/3$ (87.6 %) does real work, and it does it
through the *upper* edge of the window. Whether the gates are too easy on v2 is
an open question `[О]`, and it is now a numbered one.

**What holds regardless of the path.** Reachability of the gates by the *diary*
estimator never touches the natal chart at all:

| structure of the series | P | Φ | D | gates |
|---|---|---|---|---|
| voices independent | 0.147 | 0.021 | 6.91 | 2/4 |
| weak common wave | 0.157 | 0.089 | 6.69 | 2/4 |
| **middling common wave** | **0.327** | **1.289** | **4.51** | **4/4** |
| strong common wave | 0.826 | 4.771 | 1.60 | 2/4 |
| almost a single voice | 0.981 | 5.868 | 1.07 | 2/4 |

The gates are reachable and, which matters more, **selective**: only the middle
band passes. Voices apart, and there is no integration; voices fused, and there
is no differentiation — precisely what the theory declares consciousness to be,
reproduced from series shaped like daily marks `[Т]`.

**What the error killed.** A prediction had been drawn — that a diary Γ̂ would
clear gates a natal Γ fails. It rested on a contrast of 0.1 % against ≈1.3, and
on the live path there is no contrast at all: the natal median is 1.289, the
same number the middling series gives. The prediction was withdrawn, and
withdrawn *before the first mark was collected*, so no fitting to data was
possible.

**Why the low Φ on v1, for the record.** It is not a tunable: sweeping β from
0.05 to 0.80 lifts the median only to 0.844 and it plateaus there, while the
four-gate rate peaks at 8.8 % near β = 0.45 and falls again. The plateau is not
the Cauchy–Schwarz ceiling — at β = 0.80 only 14 % of pairs sit at it, average
load 0.183 — but the **cone projection**, which discards up to 31 % of the raw
mass as the negative inertia grows. The first mechanism proposed here was the
wrong one; the measurement said so.

**Do the gates discriminate at all?** The question «are they too easy on v2» is
settled not by the pass rate but by comparison against a **null ensemble** —
random density matrices from the Hilbert–Schmidt distribution, which know
nothing of any sky. The ruler is the one already used on textual claims: how
many bits the answer «passed» carries.

| gate | encoder | random | delta | bits |
|---|---|---|---|---|
| $P > 2/7$ | 98.9 % | 37.8 % | +61.1 | 0.089 |
| $R \ge 1/3$ | 91.6 % | **100 %** | −8.4 | 0.414 |
| $\Phi \ge 1$ | 86.3 % | 7.0 % | +79.3 | 0.576 |
| **$D \ge 2$** | **100 %** | **100 %** | **−0.0** | **0.003** |
| all four | 78.0 % | 7.0 % | +71.0 | 0.760 |

**Which sample each table is on, because the two disagree and neither is
wrong.** The census above runs on 16 000 real births spanning 1600–1963; this
table runs on 4000 dates drawn uniformly over 1930–2009. Hence `R ≥ 1/3` reads
87.6 % there and 91.6 % here. Two hypotheses for the gap were measured rather
than assumed (`core/examples/population_effect.rs`). Real births against
uniform dates over the *same* years: largest gap across all four gates
**1.2 points** — so the population, though genuinely non-uniform over the
calendar, explains about one point. Uniform dates across 1600–1963 against
1930–2009: `R` moves 88.6 → 89.7, another **1.1 points**. What remains is
sampling error, which at n = 4000 and a rate near 0.9 runs about half a point
per standard error. No single cause, and no error — but a section that prints
both figures without saying they are different samples invites the reader to
treat one as a typo. Every pass rate is a property of the construction **and**
of the population it is counted on `[О]`.

Median P: encoder 0.3623, random 0.2775, gate 0.2857.

The answer splits in two, and both halves matter. **Against noise the gates
work, and strongly**: all four admit 78 % of charts against 7 % of random
states, and $P > 2/7$ gives 98.9 % against 37.8 % — the encoder does make
states markedly purer than chance, exactly as the gate's derivation claims
(the distance to the formless must exceed noise's own). That is not ornament.

**Between people they barely discriminate.** $P > 2/7$ carries 0.089 bits,
because everyone passes; only $\Phi \ge 1$ does real work (0.576), and the
quartet together yields 0.760 bits — about one binary distinction, «78 against
22». Which is precisely what §88 demands: if the natal layer carries one
number, gates upon it *cannot* separate people. The low discriminability is
not a flaw in the gates but a consequence of the information bound `[Т]`.

**And $D \ge 2$ is dead.** 100 % for the encoder, 100 % for random, 0.003
bits. It is not vacuous mathematically — a nearly pure state would fail it —
but neither ensemble produces such states. As it stands it is not a gate but a
line in a report `[О]`.

#### What survives a harder null {#ворота-против-спектра}

The Hilbert–Schmidt ensemble differs from a chart in *everything at once*,
spectrum included — and three of the four gates read nothing but the spectrum.
Purity is the sum of squared eigenvalues; $R = 1/(7P)$ is a function of purity,
so $P$ and $R$ together are one condition on the spectrum; $D$ is the
exponential of the entropy, again spectral. Only $\Phi$ is computed over a
partition of the seven *named* axes and can therefore see structure. On top of
that the HS ensemble in seven dimensions has mean purity $2d/(d^2+1) = 0.28$,
which sits flush against the threshold $2/7 \approx 0.2857$ — so the 7 % is
in large part a statement about where that ensemble happens to sit.

The sharper null holds the spectrum **identical**. Take a chart, diagonalise
it, keep the eigenvalues, and replace the eigenvectors with a Haar-random
unitary frame: $U\,\mathrm{diag}(\lambda)\,U^\dagger$. Purity and $R$ then agree
with the chart bit for bit (largest observed discrepancy $1.3\cdot10^{-15}$),
and only $\Phi$ and $D$ can move. On 4000 charts:

| gate | charts | same spectrum, random frame | delta |
|---|---|---|---|
| $P > 2/7$ | 98.9 % | 98.9 % | +0.0 |
| $\Phi \ge 1$ | 86.3 % | 70.4 % | **+15.9** |
| $D \ge 2$ | 100 % | 100 % | +0.0 |
| all four | 78.0 % | 62.4 % | +15.6 |

The result is worth stating gate by gate rather than in aggregate. **Three of
the four discriminate exactly zero** beyond the spectrum: for $P$, $R$ and $D$
the earlier «78 % against 7 %» is a claim about *spectra*, not about how a
chart is built. **One gate does real work.** At identical spectrum, charts
clear $\Phi \ge 1$ sixteen points more often than a random frame — median
$\Phi$ 1.235 against 1.134, and the two samples separate with a pair-ranking
score of 0.612 (0.5 would be nothing). The effect is genuine and modest, and
its source is legible: $\Phi$ is computed over the named axes, and a Haar
rotation scrambles the names. So what is shown beyond the spectrum is exactly
this — **the encoder does not place its axes arbitrarily with respect to
integration** `[С]`. That is the whole of the structural claim, and it is
smaller than the aggregate figure suggests.

**And the $\Phi$ signature turned out to be carried by the construction
itself.** The next null asks *which* non-arbitrariness: keep every gate's
multiplicity, magnitude and line-phase, but wire its member axes at random —
forty independent consistent rewirings, and forty more constrained to preserve
each axis's total degree exactly (double edge-swaps on the gate–axis
incidence). The canonical dictionary passes $\Phi \ge 1$ on **88.8 %** of
charts; free rewirings reach 71.1–82.0 % (median 77.1), degree-balanced ones
74.9–83.1 % (median 78.5) — **zero of forty** reach the canonical figure in
either family, permutation $p = 0.024$ in both. So the signature is neither
multiplicities nor axis load: it is the structure of which pairs are coupled.

The mechanism is exact combinatorics, not a tendency. The 64-word dictionary
is a **2-design**: its 21 pair-gates cover all 21 axis pairs exactly once, its
35 triangle-gates cover all 35 distinct triples exactly once, and every axis
pair therefore receives exactly $5 + 1 = 6$ contributions — perfectly uniform
slot load (a random rewiring loads slots 2…12). Contributions carry line
phases, and colliding slots partially cancel, $e^{i\theta_1} + e^{i\theta_2}$;
the design never collides them. Uniform slot load is what $\Phi$ detects
beyond the spectrum — and the mechanism is established by intervention, not
narration: with phases forced to zero the gap vanishes entirely (both families
saturate at 100 %), and the *raw* off-diagonal mass inverts — 1.603 canonical
against 1.664 rewired — exactly as the $\sqrt{k}$-versus-$k$ arithmetic of
random-walk accumulation demands. Remove the cause and the effect is gone.
This is the first measured structural evidence *for* the
$64 = 1 + 21 + 35 + 7$ construction on the encoder side `[С]`. And the same
null cleanly divides the labour between the encoder's two structural facts:
five-modedness (§87) does **not** move under rewiring — rank ≤ 5 on 99.8 % of
charts canonically and 100 % rewired, $\lambda_6$ a numerical zero in both —
so the spectral cutoff belongs to the assembly's working point, exactly as
§87 hedged, while the $\Phi$ signature belongs to the dictionary. Two facts,
two distinct carriers, separated by one instrument. A third layer sits in the
phases themselves: with the canonical wiring kept but activation *lines*
shuffled, the $\Phi$ pass drops to 77.2–86.2 % (median 83.5) — the canonical
assignment beats all 25 shuffles, $p = 0.038$, which is the granularity floor
of 25 replicates and is said rather than hidden. The carrier was then hunted surgically
(`line_carrier.rs`) and turned out not to be what it looked like. Repeated
gates are refuted twice over: their line differences are uniform (Δ = 0 excess
−0.8 pts) and shuffling only their lines drops nothing. The carrier is the
**lights lock**: Earth is defined as Sun + 180°, and 180° is exactly 32 gates —
so Earth's line always equals the Sun's (1000 of 1000 charts), phase-locking
the four heaviest (μ = 2) contributions pairwise. And the residual turned out to be a second
lock of the same nature: the South Node is the North Node + 180° (also 1000 of
1000). Randomising the lines of the four locked bodies — 8 activations of
26 — lands exactly on the full-shuffle floor (84.2 % against 84.2 %), while
randomising the other 18 leaves the share at the canonical level (87.9 %
against 87.6 %). So the ephemeris-line layer is *entirely* the construction's
own geometry — the two derived-body definitions — and the lines of the nine
free bodies carry no measurable phase structure `[С]`. Read cyclically: each
lock is one celestial **axis** — Sun–Earth and nodal — a single sky cycle
read twice in counter-phase; the construction keeps the phase of the two axes
and is deaf to the phase of every free body (where this sits on the ladder of
cycles — [evolution, celestial ladder](/docs/core/dynamics/evolution#небесная-лестница-циклов)). The exact
design property is held by a machine check; the empirical margin is the
probe's.

Machine: `window_census.rs`, `gate_reachability.rs`, `phi_source.rs`,
`gate_discrimination.rs`, `gate_spectrum_null.rs`, `wiring_null.rs`.
