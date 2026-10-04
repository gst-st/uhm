---
sidebar_position: 3
title: Falsifiability
description: Verification criteria and predictions of UHM theory
---

# Falsifiability and Predictions

An empirical claim consists of a specified model, a calibrated observation law, a declared population/intervention domain and an outcome prediction. Matrix identities and simulation checks test mathematical or implementation consistency; they do not independently validate a phenomenal or physical identification. Use the [status registry](/docs/reference/status-registry) and [premise register](/docs/reference/premises) to keep these dependencies explicit.

## Falsification Criteria

Compare models on held-out data after freezing encoders, calibration, frame, outcomes, thresholds, noise law and stopping rules. Report confidence intervals, effect sizes, power and multiplicity control. Calibration data are not confirmatory data. A fit to previously observed physical constants is not a new prediction.

### Experimental Predictions

The following are research hypotheses [H] conditional on identifiable state/readout models. The numerical tolerances are protocol choices [D], not universal constants.

#### 1. Isospectral discrimination {#isospectral-discrimination}

Test whether specified states with equivalent spectra but different **identified** eigenspaces produce a preregistered report difference while the predicted intensity remains equivalent. Spectral projectors, rather than arbitrary eigenvectors, are required at degeneracy. Comparing vectors requires a fixed frame and allowed residual symmetry. Establish the spectral equivalence margin and power before looking at outcomes. Spectrum/frame dependence of phenomenal quality is [H/I]; unitary invariance of the spectrum is [T]. An isospectral numerical pair alone supports only the latter.

#### 2. Contextual modulation {#contextual-modulation}

Choose a context encoding and experiential readout, then test interventions predicted to preserve the readout's intensity and alter reported quality. Holding the stimulus fixed does not establish that $\rho_E$ is fixed. In $\mathbb C^7$ the named $E$ axis is a summand, not a tensor subsystem; “discarding $E$” is not automatically a partial trace. A block restriction or a lift to a tensor product must be defined and calibrated. Declare confounders and equivalence margins; an attention effect alone does not confirm this matrix model.

#### 3. Adaptation dynamics {#adaptation-dynamics}

A candidate response model is

$$
\mathcal Q(t)=b_0+b_1\log\frac{\lambda_{\max}(t)}{\langle\lambda_{\max}\rangle_\tau}+\epsilon(t).
$$

The readout, baseline window $\tau$, response units, coefficients and noise are chosen or calibrated on training data [D/H]. Compare held-out likelihood and error with competing adaptation models, including conventional signal-based predictors. Similarity to a logarithmic psychophysical law does not derive this law from matrix axioms. Preregister an effect/error interval and analyse dependent observations at their appropriate subject/session level.

#### 4. Metric relations {#metric-relations}

A selected quality readout predicts $d_{\mathrm{perceived}}$ from $d_{\mathrm{FS}}([q_1],[q_2])=\arccos|\langle q_1,q_2\rangle|$ [H]. The rays and correspondence with reports must be identified independently. Fit scales and maps on training data, test similarity structure on new observations and compare alternative geometries.

The metric requirement is $d(a,c)\le d(a,b)+d(b,c)$, with a declared measurement-error allowance. The former criterion $|d(a,b)+d(b,c)-d(a,c)|<\varepsilon$ incorrectly demanded near equality for every triangle; ordinary nondegenerate metric triangles need not satisfy it. Metricity itself does not pick a unique phenomenal geometry.

## Refutation Criterion {#refutation-criterion}

The ideal claim “equal complete physical/model state gives equal predicted experience” is supervenience [I/H], distinct from a specified empirical response function. Exact spectrum plus spectral projectors determines $\Gamma$, but a finite dataset does not establish exact equality. If history or context enters the prediction, those inputs cannot be dropped from a test of it.

For a concrete response law $F_\theta$ and observation model $O_\theta$, form calibrated compatible state sets $\mathsf C(y)$. A report contrast can contradict the **joint** model only when its uncertainty interval is disjoint from the range predicted over every admissible pair of states and calibration parameters. A broad observation fiber may leave the predicted contrast undetermined. The [fiber theorem](/docs/applied/research/reconstruction-identifiability#fiber-theorem) gives the exact identification criterion.

Covariance of $\mathcal D(\mathbb C^7)$ does not make an encoder unique. A transformation is an allowed gauge only if the observation law, calibration and functional labels leave it unresolved; a group orbit need not exhaust a fiber. Signed complex phases and triangle holonomies cannot be recovered from diagonal entries and coherence magnitudes or unsigned Gap alone. See [phase counterexamples](/docs/applied/research/reconstruction-identifiability#phase-counterexamples).

For a full-rank linear calibrated observation frame, there are 48 independent real state parameters. Informational completeness identifies the state in the noiseless model; finite-sample uncertainty and conditioning remain. fMRI/EEG features are not automatically quantum tomography, and a two-point correlator is not a complete record of arbitrary history.

## Current Empirical Status

This page specifies a programme and its conditional predictions. It does not certify independent validation of a biological encoder, a phenomenal readout, or a fundamental physical rate law. Evidence must identify the dataset/release, preregistration, calibration and held-out subjects, acquisition coverage, complex phase observability, estimation uncertainty and comparison models. A general resemblance to attention, adaptation or known particle data is preliminary compatibility, not validation of the proposed bridge.

The [measurement protocol](/docs/applied/research/measurement-protocol#substitution-position) retains SUB-1 … SUB-6: wakefulness-only frozen calibration, $\lambda_1=\lambda_2=0$ in confirmatory runs, measured complex phases, outcome-blind verdict rules, a separately benchmarked PCI comparison and predefined low-complexity signatures. ID-A … ID-D add observational identification, conditioning and honest undetermined verdicts. Freezing prevents refitting to test labels; it neither proves physical independence under every substitution nor establishes consciousness in a new domain.

## Falsifiable predictions from Fano integration

Choose the Fano incidence structure, rate family, coordinate frame and physical observation map before testing. Each Fano pair belongs to exactly one line, and lines overlap; there are no disjoint “within-line” versus “between-line” pair classes. Equal-rate Fano dephasing attenuates every off-diagonal entry by the same factor, so it does not alone generate preferred coherence blocks.

### F-Gap-1: Intra-triplet Gap below inter-triplet {#f-gap-1-внутри-триплетный-gap-ниже-межтриплетного}

The old pairwise contrast is ill-defined for the complete Fano plane. A replacement hypothesis [H] can compare signed triangle holonomy $\arg(\gamma_{ab}\gamma_{bc}\gamma_{ca})$ on its seven lines with that on the 28 nonline triples, with amplitude eligibility and circular statistics preregistered. No difference follows from incidence alone; simulation and neural prediction require an explicit dynamics and observation model. Magnitude-only data cannot test the signed version.

### F-Gap-2: Block transparency by Fano triplets {#f-gap-2-блоковая-прозрачность-по-фано-триплетам}

Preferential triplet structure is a dynamics/architecture hypothesis [H], not a consequence of uniform Fano dephasing. Specify unequal rates, selected interactions or a triple observable that could distinguish the hypotheses. Seven overlapping $3\times3$ submatrices are not a partition into blocks. Test an explicitly predicted contrast against matched controls; do not count a simulation implementing that contrast as independent confirmation.

### F-ξ: Fano correlation length {#f-ξ-корреляционная-длина-фано}

The historical $\xi_F\sim160\,\mathrm{pc}$ estimate requires a physical spatial field, gradient stiffness, potential curvature, unit conversion and parameter calibration [H/C]. A matrix potential or incidence diagram alone supplies none of these. A correlation-length test is meaningful only after these inputs yield a fixed interval and a specified observable; absence of a chosen scale without adequate sensitivity is inconclusive. See [dark-matter models](/docs/physics/cosmology-phys/dark-matter).

### F-τ_p: Proton lifetime {#f-τ_p-время-жизни-протона}

The historical $\tau_p\sim6.7\times10^{37}$ year estimate is a particle-model hypothesis [H], requiring actual decay operators, couplings, masses and hadronic matrix elements. Preregister a decay-channel distribution/rate interval from those inputs and compare a documented confidence limit or detection. Non-detection well below the predicted sensitivity does not verify a lifetime. See [proton decay](/docs/physics/particle-physics/proton-decay).

### F-m_t: Exactly one $O(1)$ Yukawa (top) {#f-m_t-масса-top-кварка-из-неподвижной-точки-пендлтона-росса}

A selected generation/action model may have a tree-level selection rule [T within that model]. The mapping of a Fano line to physical fields and the allowed operators are additional [C/H] inputs. “$O(1)$” must be replaced by a fixed energy-dependent interval to become falsifiable. A top mass near $173\,\mathrm{GeV}$ used as a boundary condition is not an independently predicted mass. A new Yukawa coupling tests the specified particle model, not incidence geometry alone; see [Yukawa hierarchy](/docs/physics/particle-physics/yukawa-hierarchy).

### F-ISF: ISF components in fMRI {#f-isf-isf-компоненты-в-фмрт}

A count such as 6–12 is an analysis/bridge hypothesis [H]. Gap-entry count, observable rank, statistical components and physical degrees of freedom are different quantities. Specify extraction method, sampling, noise threshold, population and out-of-sample reproducibility. No chosen seven-axis state model forces a universal fMRI component count.

### F-Neural: Neural correlates of L-levels {#f-neural-нейронные-корреляты}

The matrix implication $\Phi\ge1\Rightarrow P\ge2/7$ is [T], with a one-way direction. The full Cap₂ gate is a definition [D] plus an empirical/ontological bridge [H/I]; a physical transition at its threshold is not automatic. Sharpness, continuity, scaling and connectivity monotonicity depend on the dynamics and measurement model.

Test a frozen estimator on new sessions using the [experimental protocol](/docs/applied/research/experimental-protocol). PCI and $P$ have different scales; no numerical conversion follows from the thresholds. Concordance with an independently defined PCI benchmark tests classification support. REM and ketamine signatures and the two proposed low-complexity exits remain registered hypotheses; every gate conjunct and any declared stress criterion needs an identifiable readout with uncertainty.

### F-Higgs: Higgs self-coupling deviation {#f-higgs-отклонение-самосвязи-хиггса}

The historical $10^{-2}$–$10^{-3}$ fractional deviation is [H], conditional on a specified physical action and calculation. Provide a fixed uncertainty interval and experimental definition of the coupling. A measurement with an uncertainty wider than the proposed deviation cannot verify that deviation merely because its central value lies near it. See [Higgs sector](/docs/physics/particle-physics/higgs-sector).

### F-δ_CP: CKM CP-phase from the Fano phase {#f-δ_cp-cp-фаза-ckm-из-фано-фазы}

The numerical phase derivation is withdrawn [✗] (T-345(e)); the old $64.5^\circ$ figure is retained only as a historical model value. Agreement of a withdrawn or adjusted derivation with known data is not evidence for a prediction. A future replacement requires a specified action, physical complex phases and a computation of the chosen CKM invariant; see [CKM](/docs/physics/particle-physics/ckm-matrix#11-вкус-с-часов).

### F-Cabibbo: Cabibbo angle from RG suppression of the Fano angle {#f-cabibbo-угол-кабиббо-из-rg-подавления-фано-угла}

The old $13^\circ$ derivation is withdrawn [✗] (T-345(e)); its adjusted normalization was not predicted. It is not a live falsifier. See [CKM](/docs/physics/particle-physics/ckm-matrix#11-вкус-с-часов).

### F-nEDM: Neutron EDM {#f-nedm-нейтронный-эдм}

The claim $\bar\theta=0$ from the axioms is withdrawn [✗] (T-99). Strong-CP parameters and other possible CP-odd operators remain physical inputs. Geometry alone predicts no universal neutron EDM, including an exactly zero total EDM. A specified action may yield a conditional prediction; see [QCD](/docs/physics/gauge-symmetry/confinement).

### F-w: Dark-energy drift shape {#f-w-форма-дрейфа-тёмной-энергии}

A source equation of state and universe-as-holon mapping are additional cosmological hypotheses [H] (T-266), not outputs of a local matrix Lyapunov law. No universal exclusion of Big Rip, enforced $w=-1$ crossing, or co-drift sign of $G_N$ follows from those matrix equations alone. Specify the stress-energy source, conservation law, calibration, expansion model and permitted parameter class before deriving $w(z)$ or a linked variation of $G_N$. A fit using one expansion parametrization does not establish a unique physical crossing. See [cosmological constant](/docs/physics/gravity/cosmological-constant).

### F-rank7: Rank-7 decoherence anisotropy {#f-rank7-ранг-7-анизотропия-декогеренции}

For the **specified diagonal Fano-jump family**,

$$
r_{ij}=\frac16\sum_{|\ell_p\cap\{i,j\}|=1}\gamma_p,
\qquad r=A\gamma,\quad \gamma\in\mathbb R_{\ge0}^7.
$$

The incidence map $A\in\mathbb R^{21\times7}$ has rank seven, so this model implies 14 linear relations [T under that family] and the stronger feasibility constraint $r\in A\mathbb R_{\ge0}^7$. They do not constrain every possible GKSL generator. A test must identify **temporal decay rates**, distinguish Hamiltonian oscillations, population motion and feedback, and include covariance and acquisition resolution. State magnitudes at one time do not identify rates.

Fit the constrained rate model and compare residuals with their calibrated sampling distribution and alternative dissipators. A residual outside the subspace/cone rejects this calibrated family; its physical application remains [C/H]. The model has seven fitted rates, so the phrase “no adjustable parameters” was incorrect even though its 14 relations contain no additional free rates.

### F-Band: the two sums of a living state {#f-band-две-суммы-живого-состояния}

Write $d=\sum_i\gamma_{ii}^2$, $q=\sum_{i\ne j}|\gamma_{ij}|^2$. The canonical gate implies $q\ge d\ge1/7$ and $d+q\le3/7$, hence

$$
\frac17\le d\le\frac3{14},\qquad \frac17<q\le\frac27.
$$

The strict lower bound for $q$ also uses $P>2/7$: $q=1/7$ would force $d=1/7$ and equality at the excluded purity boundary. The weaker inclusive bands T-321/T-323 remain valid. These are exact algebraic checks, not empirical confirmations of life. A counterexample state passing the declared gate would reveal a derivation or implementation error. Data outside a band can reject the **joint** encoder/readout/gate hypothesis only after accounting for observational uncertainty; it cannot falsify a proved matrix identity.

### Summary table of predictions {#summary-table-of-predictions}

| Claim | Mathematical content | Empirical/physical status |
|---|---|---|
| Isospectral/context/metric/adaptation | Specified response model and state diagnostics | [H], calibrated readout needed |
| F-Gap-1 / F-Gap-2 | Incidence and selected dissipator; old pair/block implication invalid | [H], defined triple observable needed |
| F-rank7 | Rank-seven incidence map and nonnegative rate cone for chosen jumps | [C/H], rate identification needed |
| F-Band | Exact consequence of the stated gate | [T] algebra; biological bridge [H/I] |
| F-Neural / F-ISF | Selected thresholds/component analysis | [H], frozen calibrated observations needed |
| F-ξ / F-τ_p / F-m_t / F-Higgs / F-w | Conditional field/action/cosmological models | [H/C], explicit physical inputs needed |
| F-δ_CP / F-Cabibbo / F-nEDM | Former universal numerical derivations | [✗] withdrawn |

“Passing” numerical checks, compatibility with known data, held-out predictive agreement and independent physical confirmation are different evidence categories. Count them separately; this page does not assign unsupported counts of confirmed predictions.

## Completeness of Theory

The theory is a specified mathematical framework with conditional model results and open empirical bridges. It is not proved universally complete, contradiction-free across every interpretation, self-sufficient in physical inputs, or uniquely applicable to every self-referential system. Successful simulation establishes implementation of its chosen equations. Experience identification, biological survival, spacetime/action mapping and physical rates require additional premises.

A nonlinear state-valued ODE need not be a linear CPTP channel on joint systems. No-signalling and ensemble-independence require a defined extension/physical reading; they are not consequences of writing a valid local density-matrix equation. No universal BQP upper bound or physically efficient SAT algorithm follows from the regenerative ansatz. See [computational limits](/docs/reference/computational#вычислительное-ограничение).

## Vulnerability analysis {#анализ-уязвимостей}

| Question | Established scope | Outstanding condition |
|---|---|---|
| Why seven? | Exact representation/code bounds under named premises | Functional/physical seven-axis bridge; no universal minimum for learning |
| Differentiation | A declared entropy readout or proxy | Identification of that readout; under $\rho_E=\Gamma$, $R\ge1/3$ already implies $e^S\ge7/3$ |
| Reflection | Algebraic identity $R=1/(7P)$ for the selected HS definition | Physical meaning and threshold choice [D/H/I] |
| Experimental support | Preregistered, identifiable predictions can be tested | Independent data and competing models; simulation is not laboratory validation |
| Quantum realization | T-267 [C]: conditional encoding/protected-sector dynamics can be analyzed | Actual substrate, noise, coupling and sector invariance; no universal decoherence-free subspace |

## Theory Boundaries {#границы-теории}

### Structural Boundaries

Seven labels do not imply seven independent coordinates or a unique partition. Codomain symmetry does not identify an encoder; the observations determine a fiber. Local fixed-metric steepest descent T-263 has no universal learning, cosmological-time or complexity consequence. Values and units of $H$, jumps and regeneration rates require calibration. T-266 remains [H]; no measured cosmological purity or fundamental rate follows from the selected local potential.

### Physical Boundaries

Spectral actions, representation embeddings and group stabilizers yield conditional mathematical statements only with their specified geometry, matter representation, action and normalization. These inputs are needed before identifying physical gravity/gauge fields, particle masses, $G_N$, a cosmological source or an equation of state. A formula for $G_N$ in a selected spectral-action normalization is not a parameter-free derivation of its observed value.

For a full-rank state and specified field, T-271 gives $\dot S=-\operatorname{Tr}(\dot\Gamma\log\Gamma)$. Unital entropy production is nonnegative, but it can vanish; regenerative entropy flux has no universal sign. Physical power T-273 [C] requires thermal erasure assumptions and a **positive measured physical entropy-export rate**: $\dot Q\ge k_BT\dot s_{\mathrm{erase}}$ in nats/second. Purity and numerical tick frequency alone give neither such a rate nor a positive hardware power floor; see [Reeb & Wolf](https://arxiv.org/abs/1306.4352).

### Phenomenal Boundaries {#phenomenal-boundaries}

The identification of structural predicates with experience is an axiom/interpretation plus a tested bridge [I/H]. A report classifier does not prove the ontology. The cuts $P>2/7$, $R\ge1/3$, $\Phi\ge1$, $D\ge2$ retain their [defined scope](/docs/reference/mathematical-kernel#thresholds): $\Phi\ge1\Rightarrow P\ge2/7$ is one-way, and the value one is selected [D]. A three-term generator decomposition is not a Bayesian prior that uniquely derives $R_{\mathrm{th}}=1/3$. A physical quality readout, allowable gauge and calibration must be specified rather than deduced from a purported universal functor uniqueness theorem.

### Categorical Boundaries

Name the source/target categories, objects and arrows before claiming a functor, classifier, reflector, topology or temporal modality. A many-to-one state encoder transports source dynamics only if it preserves observation/state fibers. A set-map idempotent need not be a CPTP idempotent or categorical reflector. A tensor-clock lift needs a retraction/readout; it is not automatically Morita equivalence.

### Octonionic Falsification Criteria

Fano wiring, covariance and associators become physical tests only with an independently calibrated realization. An associative matrix encoding is not made nonassociative by naming its coordinates octonionic; specify the triple observable or product being measured. Covariance is a property of a specified action and dynamics, not a universal empirical prediction. Hamming one-error correction is a coding theorem for its stated alphabet/noise/decoder; it is not a guarantee that an arbitrary regenerative ODE corrects one coherence error or detects two.

### Research programme

First establish the observation law and identification of the target functionals. Then fit physical rates from informative trajectories, freeze competing models and preregister interventions. Test all declared gate conditions with confidence sets, report unresolved fibers and indeterminate verdicts, and retain separate ledgers for mathematical checks, simulation benchmarks, observational compatibility and independent experiments. Primary starting points are [Watrous on measurements/channels](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), [Rothenberg on identifiability](https://doi.org/10.2307/1913267), and [Kleiner & Hoel on consciousness falsification](https://arxiv.org/abs/2004.03541).
