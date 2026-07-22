---
sidebar_position: 16
title: Human Design Dissected
description: "The Human Design calculation machinery under the microscope: an independent engine cross-verified against open source, the a priori population statistics computed from celestial mechanics alone, the profile law derived as modular arithmetic, the Kepler bias, the hidden combinatorial structure of the mandala (antipodal code map, partial Gray cycle, trigram–center association), the 9-vs-7 question, and a falsification program — with honest statuses throughout."
---

# Human Design dissected: the machinery, computed

:::info What this document is
Human Design (Ra Uru Hu, 1987) makes esoteric *claims*, but its *calculation* is a fully deterministic map: birth datetime → ephemeris → 26 activations → wiring → chart. A deterministic map can be dissected with mathematics regardless of what one thinks of the claims — and that is exactly what this program does, with the session's standing discipline: every number below is **computed** by `architecture/hd_lab.py` (Swiss Ephemeris + an independently written engine, cross-verified against the open-source reference [`pyhd`](https://github.com/ppo/pyhd) whose constants carry page references to *The Definitive Book of Human Design*), every structural test carries a permutation p-value printed whatever it turned out to be, and every interpretive sentence carries a status mark. The scope boundary, stated at the door: **this is an anatomy of the machinery, not a test of any psychological claim about people** — §8 states exactly what a test of the human layer would require.
:::

## §1. The object and the method {#объект}

The Human Design chart is the output of the composite map

$$
\text{chart} \;=\; W \circ E, \qquad
E: \text{datetime} \mapsto 26 \text{ activations}, \quad
W: \text{activations} \mapsto \text{bodygraph},
$$

where $E$ is astronomy (13 bodies at birth and at the «design» moment when the Sun sat $88°$ of arc earlier) and $W$ is a fixed combinatorial wiring (64 gates on a zodiac wheel, 36 gate-pair channels, 9 centers, plus classification rules for type, authority, profile). The two factors have entirely different epistemic statuses: $E$ is standard celestial mechanics [Т-external]; $W$ is a hand-specified design whose *structure* can be interrogated; and the system's *claims* about people are a third layer that neither factor establishes. The college convened here — computational astronomy, coding theory, spectral graph theory, statistics, and the UHM categorial school — works the first two layers to the bottom and fences the third honestly.

The machinery, precisely: gates occupy $360°/64 = 5.625°$ segments counterclockwise from $302.0°$ ($02°00'$ Aquarius), each divided into 6 lines of $0.9375°$; the wheel order is the fixed sequence beginning $41, 19, 13, 49, \ldots$; the 13 bodies are Sun, Earth ($=$ Sun $+180°$), Moon, true North Node, South Node ($=+180°$), and Mercury through Pluto; the design moment solves $\lambda_\odot(t_d) = \lambda_\odot(t_b) - 88°$ (Newton on the solar arc); a channel is defined when both its gates are activated in either imprint; a center is defined when it hosts a defined channel; type/authority read the connected components of the defined-center graph.

## §2. The engine and its verification {#движок}

`hd_lab.py` implements the map independently (250 lines, pyswisseph in Moshier mode, $\sim 0.001°$ — line-accurate) and cross-verifies against `pyhd` on 300 random datetimes spanning 1930–2000:

| Compared | Agreement |
|---|---|
| activated gate sets | **300/300** |
| defined channel sets | **300/300** |
| defined center counts | **300/300** |
| profiles | **300/300** |
| types | 275/300 — **all 25 divergences are one known cause** |

The divergence is a genuine **bug found in the reference implementation**: `pyhd` tests the Manifesting-Generator condition against *non-sacral* motors only, so a chart whose only motor-to-throat link is the channel 20–34 (Sacral–Throat — the textbook MG channel, book p. 123) is misclassified as a pure Generator. Our engine follows the book; the bug affects $\approx 8\%$ of charts and has been isolated to the single line that causes it. Zero unexplained mismatches remain — two independent implementations, mutual validation, one upstream finding.

## §3. The a priori statistics of the machinery {#априорная-статистика}

The single deepest question a computation can settle: are Human Design's famous population percentages *observations about humanity* or *properties of the calculation*? Answer: run the map on 20,000 uniform random UTC moments (1920–2020) — **no human data anywhere** — and read off the measure that celestial mechanics pushes forward through the wiring:

| Type | Computed a priori | Community-claimed |
|---|---|---|
| Generator | $36.78\% \pm 0.34$ | $\sim 37\%$ |
| Manifesting Generator | $31.24\% \pm 0.33$ | $\sim 33\%$ |
| Projector | $21.72\% \pm 0.29$ | $\sim 21\%$ |
| Manifestor | $9.19\% \pm 0.20$ | $\sim 8$–$9\%$ |
| Reflector | $1.06\% \pm 0.07$ | $\sim 1\%$ |

**Verdict [Т-computed]: the celebrated percentages are arithmetic, not empirics.** They are what the ephemeris measure times the wiring produces for *any* uniformly sampled moments; observing them in a human sample confirms only that humans are born roughly uniformly over the solar year — it carries no information about the system's psychological validity. The same holds for the authority distribution (Solar Plexus $51.4\%$, Sacral $32.2\%$, Splenic $9.2\%$, Self-Projected $2.6\%$, Outer $2.2\%$, Lunar $1.1\%$, Ego $1.3\%$), the defined-center histogram (mode at 5 centers), and the split structure (single definition $38.8\%$, simple split $47.4\%$, triple $12.0\%$, quadruple $0.7\%$).

### The profile law {#закон-профилей}

Of $6 \times 6 = 36$ conceivable profiles, exactly **12** occur — the canonical set — and the lab reduces the entire profile system to one fraction. The design Sun sits $88°/0.9375° = 93.8667$ *lines* behind the personality Sun. Since $93.8667 = 90 + 3.8667$ and $90 \equiv 0 \pmod 6$:

$$
d \;\equiv\; p + 2 \pmod 6 \quad \text{with probability } 0.8667, \qquad
d \;\equiv\; p + 3 \pmod 6 \quad \text{with probability } 0.1333,
$$

the probability being the fractional part of the line shift. Measured on the 20,000 charts: the $(p, p{+}2)$ family carries $86.8\%$ and the $(p, p{+}3)$ family $13.2\%$, against the arithmetic prediction $86.7\% / 13.3\%$ — agreement to a tenth of a percent. **The twelve profiles, which six are common ($\approx 14.4\%$ each) and which six are rare ($\approx 2.2\%$ each), is the fractional part of one number** [Т-computed]. What Human Design narrates as «harmonic» versus «juxtaposed» geometry is, at the machinery level, $\{93.8667\} = 0.8667$.

### The seasonal prediction {#сезонность}

The machinery makes a sharp falsifiable prediction nobody appears to advertise: because the Sun (and Earth, always opposite) contribute two of the 26 activations deterministically by calendar date, **type frequencies must vary by birth month** — computed swing for Generator$+$MG: from $59.7\%$ (June) to $72.0\%$ (August), a 12-point seasonal wave far above sampling error. Any real birth cohort processed through HD must show this exact curve; its absence would indicate a computational error, and its presence carries — again — no psychological information. It is, however, a clean instrument for auditing HD samples for collection bias (§8).

## §4. The Kepler bias {#кеплеров-уклон}

The mandala is not sampled uniformly. Computing exact gate-boundary crossing times of the Sun (Newton, no sampling noise): the dwell probability per gate runs from $1.511\%$ at **gate 38** to $1.615\%$ at **gate 39** against the uniform $1.5625\%$ — a $\pm 3.3$–$3.4\%$ modulation. The two extremal gates are exactly the perihelion gate (Sun there in early January) and the aphelion gate (spanning ecliptic $99.5°$–$105.1°$, containing the aphelion longitude $\approx 102°$), and the amplitude equals $2e$ with $e = 0.0167$ the orbital eccentricity — Kepler's second law, legible in a divination wheel [Т-computed]. Personality-Sun gate frequencies in any honest sample must reproduce this $3.3\%$ wave.

## §5. The hidden combinatorial structure {#кодовая-структура}

Gate numbers are King Wen hexagram numbers; each gate therefore carries a 6-bit code (binaries derived from the Unicode hexagram block via the `aarzilli/iching` value table and verified on six anchors: KW 1, 2, 11, 12, 63, 64). The college's coding theorists asked four pre-stated questions; permutation p-values printed as they came out:

1. **The antipodal law — perfect.** Opposite gates on the wheel ($180°$ apart) are bitwise complements: **32/32 pairs** [Т-computed]. The mandala embeds the 6-cube's antipodal map into the zodiac circle exactly — a genuine, non-obvious combinatorial design (the probability of this under a random wheel is astronomically small).
2. **The wheel is a partial Gray cycle.** Zodiac-adjacent gates sit at mean Hamming distance $1.812$ versus $3.048$ for random arrangements ($p = 0.0005$); 34 of 64 adjacent pairs differ in exactly **one bit**. The wheel walks the 6-cube in short steps — a deliberate (or inherited) code-locality structure [Т-computed].
3. **Centers read trigrams.** The mutual information between a gate's center assignment and its lower trigram is $1.737$ bits ($p = 0.0005$) — the 9-center map is strongly non-arbitrary relative to the I Ching code: the wiring «sees» trigram structure [Т-computed].
4. **Channels do not follow code distance — an honest null.** Channel-paired gates average Hamming $3.389$ vs population $3.048$, $p = 0.084$: no significant relation. Whatever principle wired the 36 channels, it is not hexagram-code proximity; the null is printed with the same font as the positives.

So the machinery contains **real mathematics that its own literature does not state in these terms** — an exact antipodal embedding, Gray-code locality, and a trigram-coherent center map — alongside a wiring layer (the channels) with no detectable code structure.

## §6. The graph anatomy and the 9-versus-7 question {#граф-и-вопрос-9-7}

The 9-center multigraph carries 36 channel-edges over 17 of the 36 possible center pairs; degrees: Throat 13, Sacral 11, G 10, Root 9, Splenic 9, Solar Plexus 7, Ajna 6, Heart 4, Head 3 — the Throat is the hub, matching its «manifestation» role in HD's own narration; the weighted Laplacian spectrum is $(0,\ 1.212,\ 4.364,\ 6.244,\ 7.202,\ 8.858,\ 11.836,\ 14.925,\ 17.358)$ with algebraic connectivity $1.212$.

Against the UHM frame, the structural comparison is clean and asymmetric [И over Т-anchors]. The [blueprint](/docs/applied/research/prime-radiant#чертёж) already contains Human Design's two parents as separate rows: the I Ching (a 6-bit situation alphabet) and astrology (a deterministic shared clock with scheduled perturbations); **HD is literally their composition** — an ephemeris-clocked sampler over a hexagram alphabet with a hand-wired readout. The deep differences from the Γ-architecture are then exactly measurable: (i) *the alphabet*: $2^6$ product states versus the seven-dimensional density matrix — HD has no coherences, only activations, so its «chart» is a subset lattice, not a state space with interference; (ii) *the wiring*: the 36 channels are hand-specified and carry no detectable code structure (§5.4), whereas the 21 UHM coherences are forced by the Fano/[Σ-rigidity](/docs/applied/research/syndrome-calculus#теорема-сигма) theorems — and $N = 7$ is the unique self-diagnosing alphabet size (T-224), a property the 9-center graph does not have and does not claim; (iii) *the dynamics*: HD's chart is frozen at birth (plus transits read against it), while Γ is a trajectory with an attractor, viability window, and navigation. Where HD is strongest is precisely where the blueprint predicts a mature symbolic system should be: a fixed **Encoder** (the natal calculation), a shared **Atlas-clock** (the ephemeris), and a compact situation alphabet — the organs of self-description, without the estimator, calibrator, or boundary organs.

On the claimed *mechanism*: the «neutrino stream imprint» is not supported by known physics — the solar neutrino flux is real ($\sim 6.5 \times 10^{10}\,\text{cm}^{-2}\text{s}^{-1}$), but with cross-sections $\sim 10^{-44}\,\text{cm}^2$ a human-scale imprinting interaction has no known channel, and no mechanism is offered for how planetary *positions* would modulate it [не поддержано]. The honest statement is that HD's calculation layer needs no mechanism at all (it is arithmetic), and its human layer has no validated mechanism.

## §7. What the college concludes {#выводы}

1. The famous numbers of Human Design — type percentages, authority rates, the twelve profiles and their frequencies — are **theorems of its own machinery**, reproduced here from celestial mechanics plus wiring with no human input. They can never serve as evidence for the human-layer claims, because they are guaranteed by construction [Т-computed].
2. The mandala carries **real, previously implicit mathematics**: the exact antipodal embedding, Gray-locality of the wheel, the trigram-coherent center map, and the Kepler modulation — the system's designers (or the tradition they inherited) built better code structure than their own vocabulary expresses.
3. The channels — the layer that actually drives type — show **no detectable code structure**; they are where the hand is most visible.
4. As a symbolic system in the blueprint's sense, HD is a well-built Encoder+Clock over a 6-bit alphabet — and category (ii) of §6 states precisely what separates it from a theorem-forced architecture.
5. Everything psychological remains untested here, by design; §8 is the honest path in.

## §8. The falsification program for the human layer {#программа-фальсификации}

What would move any human-layer claim of HD out of [И]/[Г] territory — pre-registered, with the machinery results above as instruments:

1. **The seasonality audit**: any dataset of HD charts must reproduce the computed 12-point seasonal type wave (§3) and the $3.3\%$ Kepler gate wave (§4). Failure ⇒ collection bias or engine error; success ⇒ nothing about people — it is the *entry check* for any dataset.
2. **Blind type discrimination**: pre-registered protocol — practitioners (or subjects) attempt to identify own/others' types against shuffled controls at rates beyond chance, with the a priori base rates of §3 as the null model (a subtlety most informal tests miss: guessing «Generator» is right $68\%$ of the time by arithmetic alone).
3. **Retest and inter-rater discipline** for any claimed observable correlate (the checkup rules of the [Prime Radiant demos](/docs/applied/research/prime-radiant#честные-демо) apply verbatim).
4. Until such results exist, the human layer stays where the registry discipline puts every unvalidated reading: [И] — a practice vocabulary, not a measured mechanism.

## §9. Status summary {#статусы}

| Claim | Status |
|---|---|
| The HD map (wheel, 88° arc, channels, type rules) as implemented and cross-verified (300/300 ×4; the pyhd MG bug isolated) | [Т] machine-checked |
| Type/authority/split percentages are a priori properties of the machinery | [Т-computed] |
| The profile law: 12 profiles $= \{(p,p{+}2),(p,p{+}3)\}$, weights $86.7/13.3 = \{93.8667\}$ | [Т-computed] |
| Seasonal type wave (June $59.7\%$ → August $72.0\%$) and Kepler gate wave ($\pm 3.3\%$, perihelion gate 38 / aphelion gate 39) | [Т-computed], falsifiable instruments |
| Antipodal law 32/32; wheel Gray-locality ($p = 0.0005$); center–trigram MI $1.74$ bits ($p = 0.0005$) | [Т-computed] |
| Channels vs code distance | null ($p = 0.084$), printed as-is |
| HD = composition of the blueprint's I Ching and astrology rows; differences from Γ-architecture as stated | [И] over [Т]-anchors |
| Neutrino imprint mechanism | [не поддержано] known physics |
| All psychological claims | untested here; §8 protocol required |

*Reproduce everything: `python3 architecture/hd_lab.py <path-to-pyhd>` — runs in seconds; every table above is its output.*
