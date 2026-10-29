# Machine-checked operational laws

Run `python3 scripts/verify_readout_descent.py` from the repository root. The
checker selects `verification/lean/lean-toolchain` through Elan; it needs the
pinned Lean toolchain installed. No Mathlib dependency is required for these laws.
The normal corpus gate (`python3 scripts/verify_gate.py`) also runs the check.
An optional `--report /absolute/new/path.json` preserves source fingerprints,
compiler diagnostics, theorem axiom inventories and negative-control outcomes.
Existing reports are never overwritten.

`ReadoutDescent.lean` proves that a supplied split readout admits a unique
compatible transition exactly when that transition preserves observation fibres.
It includes identity/composition laws, partial-action availability and compatible
transport across different state/readout spaces. The dimensions and physical
morphology are unrestricted by these laws. The supplied lift is a section, not
an inverse; an explicit projection counterexample shows why a section alone
cannot recover erased action-relevant information.

All 16 theorem declarations have axiom audits. Only `propext` and `Quot.sound`
are permitted; no project axiom or `sorryAx` is accepted. Five false controls must
fail by evaluation of their false propositions; parser, import and tool failures
are not accepted as counterexample evidence.

This establishes conditional mathematical laws. It does not establish their
premises for an empirical encoder, certify a Rust implementation, provide a
native Verum certificate, or prove phenomenal experience or physical safety.
Verum integration and implementation correspondence require their own checked
artifacts. The full state, calibration, uncertainty and action provenance remain
part of the corpus contract.
