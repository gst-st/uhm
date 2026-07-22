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
