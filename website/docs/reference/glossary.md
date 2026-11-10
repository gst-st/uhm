---
sidebar_position: 1
title: "Glossary"
description: "Operational, mathematical and physical terms used in UHM"
---

# Glossary

## Experiments

| Term | Meaning |
|---|---|
| Preparation | An allowed operation that supplies the initial system for an experiment. |
| Instrument | An operation with a recorded outcome and a specified output available for subsequent interventions. |
| Record | What the detector actually returns in a closed test. It can include a symbol, a time, an event probability or an entire time-ordered sequence. |
| Operational state | An equivalence class of preparations giving the same records in every allowed test. |
| Observation fibre | The set of candidate states compatible with the same records at the stated calibration. |
| Identifiability | A quantity is identified by those records if it takes the same value everywhere in the fibre. |
| Coarse-graining | Reporting a function of the output. Combining selected outcomes of one pointer adds their probabilities. |
| Gauge transformation | A change of local frame accompanied by the appropriate transformations of links, matter and readout. |
| Holonomy | Transport around a closed path. A change of basepoint frame conjugates the loop transport. |
| Response distance | Minimal attainable cost of an intervention from one site to another under the specified protocol. Reciprocity is an extra condition. |

[Network experiments](./network-results) · [Observation and testing](./falsifiability).

## States, processes and readouts {#таксономия-конфигураций-γ}

| Term | Meaning |
|---|---|
| Holon | The system whose inputs, allowed actions, component structure and responses the model specifies. The meaning of its proposed semantic roles requires a separate identification. |
| Coherence matrix $\Gamma$ | A positive trace-one matrix in the selected quantum realization. Coherences are off-diagonal entries in a declared basis. |
| Purity $P$ | $\operatorname{Tr}\Gamma^2$. Its range for an $N$-dimensional state is $[1/N,1]$. |
| Channel | In a quantum process model, a linear completely positive trace-preserving map. More generally, operational processes are compared by all the contexts that use them. |
| Dephasing | Attenuation of coherences relative to a specified basis. A channel and elapsed time determine the attenuation. |
| Replacement | A channel $X\mapsto\operatorname{Tr}(X)\sigma$ with specified target $\sigma$. Partial replacement mixes it with another channel. |
| Steady state / attractor | A steady state is fixed by the dynamics. An attractor also has a domain of initial conditions whose trajectories approach it. |
| Clock | A register with distinguishable readings and a physical calibration. For Page–Wootters conditioning one specifies a clock factor, joint state, readout and constraint. |
| Incidence / phase Gap | Fano incidence records which basis triples are lines. A phase Gap measures a specified function of a nonzero coherence phase in a chosen frame. A numerical phase does not define a spacetime curvature. |
| Gate / margin | A gate selects states by declared inequalities. A margin measures distance or slack relative to those inequalities in named units. |
| Seven-role frame | The coordinate labels $A,S,D,L,E,O,U$. Assigning those roles to a physical apparatus requires calibration. |
| Reflection, integration, differentiation | $R$, $\Phi$, $D_{\rm diff}$ are model readouts with distinct domains and conventions. Their connection to a report is an empirical hypothesis. |
| L0–L4 | Labels in the proposed hierarchy of interiority. Conditions to compute a label, a capacity bound for a chosen device, and evidence of experience are separate claims. |
| Intensity, quality, context, history | Candidate components of an experiential description. The report, permitted interventions and observation rule give these terms an experimental meaning. |

[Equations and conventions](./specification) · [Notation](./notation).

## Mathematical structures {#категорные-термины}

A **category** specifies objects, composable arrows and identities. A **functor** also specifies how arrows are mapped, preserving identities and composition. A **terminal object** receives exactly one arrow from each object. In the finite quantum process category the trivial output system represents discarding. A **fixed point** of a particular channel is a different type of object.

A **site** specifies admissible coverings. A **sheaf** supplies restrictions and unique gluing of matching local data. The Bures open site uses covers by unions of open sets of density matrices. An **encoder** maps observed systems into a state representation. Symmetries of the target alone do not fix this map. [Mathematical kernel](./mathematical-kernel).

## Physical constructions and comparisons {#связанные-теории}

**Octonions** form an eight-dimensional real normed division algebra. Its seven imaginary basis units can be described by an oriented Fano table. A marked imaginary unit has stabilizer $SU(3)$. A **fermion bimodule** is a space carrying compatible left and right algebra actions. The matter representation, internal Dirac operator, gauge action and Yukawa couplings of a physical spectral model require additional data. [Octonion structure](../physics/gauge-symmetry/g2-structure) · [Gauge representations](../physics/gauge-symmetry/standard-model).

A **Fritzsch texture** specifies positions of zeros in mass matrices in a common flavour basis. It can be tested using independent masses and mixing measurements. **Infrared focusing** describes reduced sensitivity of a running coupling to its initial value for specified dynamics. Neither term supplies a measured mass by definition. [Mixing test](../physics/particle-physics/ckm-matrix#derivation-vus) · [Yukawa couplings](../physics/particle-physics/yukawa-hierarchy).

Claims made about these structures have a mathematical domain and an evidential status. Definitions, chosen inputs, conditional consequences and physical interpretations are listed in the [premises](./premises) and [status registry](./status-registry).
