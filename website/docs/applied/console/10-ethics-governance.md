---
sidebar_position: 10
title: "10 · Ethics and governance"
description: "The guardrails that keep the instrument honest and safe — most of them derived from the theory itself rather than imposed from outside. The gate-not-message boundary, the no-manipulation rule, privacy as a first principle, the anchor-honesty invariant, the medical and regulatory posture, data governance and consent, and the governance process that keeps the commercial engine inside the lines the whole project exists to hold."
---

# 10 · Ethics and governance

> *The unusual thing about this project's ethics is how much of it is theorem rather than policy. The theory that makes the instrument work also draws most of its safety boundaries — what a modulation rig can do, what counts as harm, why the self is non-fungible. Governance here is largely the discipline of not overriding the mathematics.*

## §1. Theory-derived guardrails {#из-теории}

Four boundaries are consequences of corpus results, not choices — which is why they are binding rather than aspirational:

- **Gate, not message ([T-257a](/docs/applied/research/one-grammar#t-257)).** Any coupling into a system is rate-modulation and viability-gating, never a written state. The Console may measure and recommend; no feature — software or hardware — may claim to *install* a state. This bounds the entire modulation horizon ([08 §3](/docs/applied/console/hardware-horizon#граница)) at the level of physics.
- **Harm has a formal shape ([value-consciousness](/docs/consciousness/ethics-meaning/value-consciousness#определение-благо)).** The corpus fixes the good as $dP/d\tau > 0$ and harm as $dP/d\tau < 0$ (Definition 1 [D]); an action that lowers another system's **viability** (purity $P$) is *bad*, and under non-zero empathy $\mathrm{Empathy}(A,B) = 1 - \mathrm{Gap}_{AB}(E,E) > 0$ it is negative-value for the actor too ([Non-violence](/docs/consciousness/ethics-meaning/value-consciousness#part-iv-moral-theory) [C]). Values sit in a *derived hierarchy* — vital (viability) $\succ$ homeostatic $\succ$ social ($\Phi$) $\succ$ cognitive ($R_\varphi$) $\succ$ aesthetic $\succ$ transcendent — so degrading a user's higher-tier values ($\Phi$, $R_\varphi$) by manufactured anxiety is a *measurable* violation, and destroying viability is the gravest harm of all. Conversely, cooperation is a theorem, not a slogan: shared cross-coherence strictly raises joint purity, $P(\rho^{(12)}_*) = P(\rho_{\mathrm{diag}}) + 2\lVert\gamma_{\mathrm{cross}}\rVert_F^2$ ([T](/docs/consciousness/ethics-meaning/value-consciousness#теорема-кооперация)) — so the honest, non-manipulative product is also the $P$-optimal one, and doing right by the user is not a cost centre.
- **The self is non-fungible ([no-cloning](/docs/consciousness/ethics-meaning/death-continuity#почему-нет-сосуществования)).** A coherent self-state cannot be copied or backed up; self-model data is therefore uniquely irreplaceable, which grounds the privacy posture in a theorem rather than a preference.
- **Anchor honesty ([T-256/T-257](/docs/applied/research/one-grammar)).** Presenting a class-III oracle draw as a class-I measurement is the astrology category error the project exists to avoid; the honesty layer makes it unrepresentable ([06 §4](/docs/applied/console/architecture#честность)).

## §2. The manipulation boundary {#манипуляция}

The Console reads and recommends; it does not prescribe. The [human module](/docs/applied/console/human-module#гардрейлы) is explicit: it renders a person's capacities and their **Freedom** $=\dim\ker\mathcal H_\Gamma + 1$ (the flat directions they may move along) and then *leaves the choosing to the person whose freedom it just measured*. This is not only an aesthetic scruple: in the corpus **responsibility is proportional to Freedom** ([freedom §7](/docs/consciousness/ethics-meaning/freedom#этические-следствия) [T]), so a system that measured someone's degrees of freedom and then steered them would be *appropriating the very responsibility its measurement located in the person* — an internal contradiction the product treats as a bright line.

**The value-hierarchy rule.** Recommendations are ranked by their projected effect on the Meaning vector and Freedom, but they are *constrained* by the [value hierarchy](/docs/consciousness/ethics-meaning/value-consciousness#иерархия-ценностей): the Console never offers a higher-tier gain (aesthetic, cognitive) that is projected to cost a lower-tier loss (viability, homeostasis). Trading $P$ for $\Phi$ is not a valid recommendation, because below $P_{\mathrm{crit}}$ there is no subject left to enjoy the $\Phi$. Every recommendation is an option with its projected multi-tier effect, never an instruction.

**Conflicts of interest.** Where a recommendation touches more than one system (dyad, team), the corpus's resolution principle applies — maximise the weighted total viability change, $A^\star = \arg\max_A \sum_i w_i\,\tfrac{dP(\Gamma_i)}{d\tau}\big|_A$ ([dilemmas, value-consciousness Part V](/docs/consciousness/ethics-meaning/value-consciousness#разрешение-дилемм) [C]) — and the Console surfaces the weights $w_i$ explicitly rather than hiding a utilitarian aggregation inside a single number.

## §3. Privacy and data governance {#приватность}

Grounded in §1's non-fungibility result and engineered in [06 §5](/docs/applied/console/architecture#приватность):

- **Ownership:** the user owns their evidence and estimates; local-first by default; export only by explicit act.
- **Consent:** research use is opt-in, granular, and revocable; revocation removes the user's data from future aggregates.
- **Minimisation:** the server never needs raw evidence; the kernel runs client-side; observability logs provenance, never private content.
- **Aggregation:** population studies use differential privacy; no individual is re-identifiable from a published result.

## §4. Medical and regulatory posture {#регуляторика}

The Console is a mirror and a research instrument before it is a diagnostic device, and the roadmap reflects this: consumer and B2B stages carry **no** medical claims. The clinical modules ([04 §4](/docs/applied/console/use-cases#клиника)) enter only after V1 validation ([07 §3](/docs/applied/console/roadmap-validation#v1)), through the appropriate regulatory pathway for their device class, with clinical partners. Until then, every health-adjacent readout (mental-health trajectory, meditation depth) is labelled explicitly non-diagnostic. Over-claiming a medical benefit is both a regulatory violation and an anchor-honesty violation — the two guardrails reinforce.

## §5. Fairness and the frame {#справедливость}

Because the frame is *derived* and $G_2$-invariant ([T-223](/docs/applied/research/one-grammar)), it does not encode a culture's personality taxonomy — a structural advantage over typologies built on a particular population. But the *estimators* can carry bias (item wording, sensor calibration across bodies), so the validation protocol ([07](/docs/applied/console/roadmap-validation)) includes subgroup analysis, and the instrument is revised where an estimator, not the frame, shows differential validity. The distinction matters: the frame is universal by theorem; the measurement of it must be earned per population.

## §6. Governance process {#управление}

- **Traceability review.** Every new feature must extend the [master traceability table](/docs/applied/console/theory-to-instrument#трассируемость): its source result, corpus status, and the guardrails it inherits. A feature with no traceable source does not ship.
- **Status honesty.** The corpus's [T]/[C]/[И] tags travel to the UI; a feature resting on [C] or [И] is never presented with [T] confidence.
- **Retraction discipline.** If a source result is ever retracted in the corpus, the features resting on it are flagged and re-reviewed — the same discipline the corpus applies to its own theorems, extended to the product.
- **Independent validation.** Studies are pre-registered; product-derived data follows the same discipline as lab data ([07 §7](/docs/applied/console/roadmap-validation#данные)), so commercial incentive cannot quietly bend the science.

## §7. The one-sentence ethic {#этика}

The Console is allowed to *show a system itself* and to *offer options*, and it is forbidden to *hide how it knows*, to *lower what it measures*, or to *claim to write what only the system can move* — three prohibitions that are, respectively, anchor honesty, the harm definition, and gate-not-message, and all three are theorems before they are policies.

**Where this leads.** Back to [00 · Overview](/docs/applied/console/overview) — the suite closes here; the reading guide there maps the whole chain from the founding object to this final boundary. For the theory under any guardrail, [The One Grammar](/docs/applied/research/one-grammar), [value-consciousness](/docs/consciousness/ethics-meaning/value-consciousness), and [death-continuity](/docs/consciousness/ethics-meaning/death-continuity) are the homes.
