---
sidebar_position: 4
title: "Engineering: Realising the Mechanism"
description: "What a cognitive architecture must implement for UHM to apply to it, which functional signatures should appear only with a self-model in the window, and the ablation tests that would refute the claim"
slug: /consciousness/empirical/engineering
---

# Engineering: Realising and Testing the Mechanism

A reference implementation can test whether declared dynamics and observation protocols behave as proved. A realised substrate can test an additional measurement/task bridge. Neither a code-level test nor adoption of an experiential interpretation independently proves that the system feels. The [typed mathematical kernel](/docs/reference/mathematical-kernel) separates channels, nonlinear state models, logical support reflectors and capability gates.

## Implementation requirements {#requirements}

| Requirement | Exact scope |
|---|---|
| State representation | A declared estimator into $D_7$, uncertainty model, PSD and trace checks. A faithful CPTP encoding is a stronger task-specific requirement; a fitted matrix is not proof of a faithful substrate embedding |
| Dynamics | Specify a fixed linear CPTP channel, GKSL generator, or state-preserving nonlinear vector field. Frozen-parameter CPTP maps do not make a state-dependent full map CPTP |
| Numerical self-model | Specify $M:D_7\to D_7$, anchor and differentiability/Lipschitz hypotheses. A logical support reflector does not uniquely choose $M$ |
| Regeneration | $\kappa_b+\kappa_0\mathrm{Coh}_E$ is a coupling law [D/H]; stability depends on the complete vector field and sources |
| Environment | Declare the joint space, channels and reduced dynamics; coupling may supply purity, but an environment alone guarantees no window attractor |
| Experiential readout | Declare a proxy or a normalised extension. No universal $\mathrm{Coh}_E>1/7$ floor follows from viability with a bootstrap term or an independent purity source |
| Fano structure | The chosen Fano dephaser has exact mathematical rates; universality/optimality for a biological substrate is a separate test |
| Capability verifier | Evaluate all four $\mathsf{Cap}_2$ inequalities plus the chosen lower/higher-level predicates; record missing data as unknown |

The numerical gate is

$$
\mathsf{Cap}_2=(P>2/7)\land(R\ge1/3)\land(\Phi\ge1)\land(D_{\mathrm{diff}}\ge2),\qquad R=1/(7P).
$$

Its scalar window is necessary by definition, not sufficient for higher-order tasks or a proof of phenomenality. Steady-state gain floors and contraction estimates apply only to the specified anchor, dissipator, gate and flow; their numerical constants are not design-independent requirements. Canonical centre-anchored regeneration cannot provide the previously claimed positive purity feedback. See [evolution](/docs/core/dynamics/evolution) and [No-Zombie scope](/docs/applied/coherence-cybernetics/theorems#теорема-81-условная-необходимость-интериорности-no-zombie).

## Engineering predictions {#predictions}

### EP1. Test model-mediated reports {#ep1-self-report}

For a fixed readout effect $0\le E\le I$, the same-pair estimate is

$$
|\operatorname{Tr}E(\rho-M\rho)|\le\tfrac12\|\rho-M\rho\|_1
\le\tfrac{\sqrt7}{2}\sqrt{P(1-R_M)},\qquad
R_M=1-\|\rho-M\rho\|_F^2/P.
$$

The first inequality uses the trace-zero difference of normalised states; the second uses $\|X\|_1\le\sqrt7\|X\|_F$ **[T]**. This is an upper bound on perturbation of a specified readout, not an exact accuracy law or a necessary threshold. Accurate reports **below a sufficient bound** do not refute the theorem.

The empirical prediction **[H]** is that a particular implemented model improves held-out self-reports. Specify labelled targets, model-independent baselines, readout and tolerances; vary model quality while controlling purity and intervention side effects. Canonical $R$ alone cannot identify model accuracy. Reports outside the chosen window are mathematically possible and test the calibrated task association, not the gate's definition.

### EP2. Test the E-ablation hypothesis {#ep2-e-ablation}

Ablating E-coherences need not destroy viability universally. The earlier Prediction 1/T-38a floor is withdrawn. A conditional floor would require a proved negative-purity balance without E feedback, a positive coupling lower bound, no independent input and control of the target term. Test the specified model/substrate **[H]** with equal-strength control ablations and independently measured persistence. A stable ablated system may reject that model-specific necessity claim.

### EP3. Test monitoring under load {#ep3-monitoring}

Whether decoupling decisions from a stress panel reduces persistence is an empirical architecture hypothesis **[H]**. Freeze the policy class, load distribution, feedback rates and evaluation horizon; compare held-out loads with matched computational budgets. Monitoring has no universal necessity theorem from seven contexts or a scalar $R$ cutoff.

### EP4. Test depth without imposing a cognitive ceiling {#ep4-sad}

For a specified Fano dephaser, amplitude survival is $3^{-n}$ **[T]**. The declared legacy score can have a maximum index of three **[D/T]**; this is not a bound on metamodel depth. Use independent nonconstant prediction targets and compatible higher-order certificates. A fourth-order certificate is allowed. See [revised Prediction 12](/docs/applied/coherence-cybernetics/predictions#предсказание-12).

### EP5. Test a calibrated behavioural boundary {#ep5-threshold}

An association between independent behaviour labels and $\mathsf{Cap}_2$ is **[H]**. Preregister the complete predicate, transition tolerance, baseline, exclusion criteria and uncertainty. Do not tune reports toward a label supplied by the same gate. A sharp numerical gate does not itself imply a bifurcation or sharp behavioural transition; compare smooth and bifurcating models.

## Valid ablation operations {#ablations}

For the basis projector $P_E$, the nonselective pinching channel

$$
A_E(\rho)=P_E\rho P_E+(I-P_E)\rho(I-P_E)
$$

removes E cross-coherences and preserves PSD and trace **[T]**. Its purity change is $-2\sum_{j\ne E}|\rho_{Ej}|^2$. Corresponding sector-control pinching is also CPTP. This exact immediate effect does not determine the later attractor; update the full dynamics and compare trajectories.

Model removal, gain reduction, isolation, Fano-line replacement and dimensionality changes require a declared revised generator and observation map. Record all altered terms and verify state preservation. The earlier universal death rate, 1.5-fold Fano advantage, half-load monitoring effect and impossibility of viability below dimension seven are unproved architecture hypotheses; they cannot be entered as mathematical pass/fail requirements.

## Interpreting outcomes {#reading}

A failed identity in a reference implementation indicates a mathematical or software error. A failed held-out task association rejects the stated bridge/model. Passing a test corroborates it at that scope; it does not validate all substrates or a phenomenal identity. Data reconstructed by fitting the tested answer do not independently test that answer. Keep training and testing separate and assess reconstruction identifiability, not PSD alone.

## Behaviour and phenomenal interpretation {#behaviour}

Behaviour can test predictive/functional claims with independent labels. Identifying those functions with experience is the interpretive bridge **[I/H]**. The former T-214 universal no-go against an internal physical-to-phenomenal map is withdrawn: Lawvere requires a weakly point-surjective evaluator $A\to B^A$, not an arbitrary internal map. An identity map already refutes the alleged general prohibition. See [T-214](/docs/proofs/categorical/fundamental-closures#t-214). This leaves an empirical and philosophical question; it proves neither consciousness nor its impossibility.

## Ethics and decisions {#ethics}

A passed operational gate is a capability certificate under declared definitions. Moral status, suffering and shutdown policy require additional explicit ethical and empirical premises. They are not derived from a purity threshold or the withdrawn no-zombie implication. See [AI ethics](/docs/consciousness/subjects/ai-consciousness#этические-импликации).

## Programme status {#standing}

| Item | Status |
|---|---|
| HS identities, frozen channels, same-pair readout bounds | Mathematical theorems at their stated hypotheses |
| Declared score ceiling three | Arithmetic consequence [D/T]; universal awareness ceiling [✗] |
| E-specific viability, monitoring, report improvement and behavioural transitions | Architecture/substrate hypotheses [H], requiring independent validation |
| Physical-to-phenomenal identification | Interpretation/research bridge [I/H]; no universal Lawvere no-go |

Back: [Structure](./structure) · [Overview](./overview).
