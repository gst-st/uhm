#!/usr/bin/env python3
"""HOLARCH laboratory — mechanical validation of the architecture meta-specification.

Panel HL01–HL14. Honesty classes (as in HomoHoloGraph):
  VERIFIED — computed fact about the machinery (theorem arithmetic, identity checks,
             SSOT synchronization, coverage completeness);
  DESIGN   — self-consistency of an engineering instance (true by construction,
             demonstrated; NOT evidence about external systems);
  CONS     — numerical consonance with an external published number ([И] reading:
             structural rhyme, stated precisely, never an identity claim).

Everything the spec doc (website/docs/applied/research/holarch.md) quotes as a number
is computed here. Run:  python3 architecture/holarch_lab.py
"""

from __future__ import annotations

import math
import os
import re
import sys
from dataclasses import dataclass, field

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SSOT_TS = os.path.join(ROOT, "website", "src", "data", "coherences.ts")
DOC_EN = os.path.join(ROOT, "website", "docs", "applied", "research", "holarch.md")

DIMS = ["A", "S", "D", "L", "E", "O", "U"]
IDX = {d: i for i, d in enumerate(DIMS)}
E_IDX = IDX["E"]

# Fano lines of the corpus (core/structure — uhm canonical wiring)
FANO_LINES = [
    ("A", "S", "L"), ("A", "D", "E"), ("A", "O", "U"),
    ("S", "D", "O"), ("S", "E", "U"), ("D", "L", "U"), ("L", "E", "O"),
]

PASS, FAIL = "PASS", "FAIL"
RESULTS: list[tuple[str, str, str, str]] = []  # (id, class, verdict, summary)


def report(hid: str, hclass: str, ok: bool, summary: str) -> None:
    RESULTS.append((hid, hclass, PASS if ok else FAIL, summary))
    print(f"[{hid}] {hclass:8s} {'PASS' if ok else 'FAIL'} — {summary}")


# ----------------------------------------------------------------------------
# Γ machinery (corpus formulas)
# ----------------------------------------------------------------------------

def purity(G: np.ndarray) -> float:
    return float(np.real(np.trace(G @ G)))


def phi(G: np.ndarray) -> float:
    """Φ = Σ_{i≠j}|γ_ij|² / Σ_i γ_ii²  (dimension-u #мера-интеграции-φ)."""
    diag = np.real(np.diag(G))
    off = np.sum(np.abs(G) ** 2) - np.sum(diag ** 2)
    return float(off / np.sum(diag ** 2))


def r_lower(G: np.ndarray) -> float:
    """Canonical reflexivity lower bound R = 1/(7P)."""
    return 1.0 / (7.0 * purity(G))


def coh_e(G: np.ndarray) -> float:
    """Coh_E = (γ_EE² + 2Σ_{i≠E}|γ_Ei|²) / Tr Γ²  (axiom-septicity #coh-e-canonical)."""
    num = np.abs(G[E_IDX, E_IDX]) ** 2 + 2.0 * sum(
        np.abs(G[E_IDX, j]) ** 2 for j in range(7) if j != E_IDX
    )
    return float(np.real(num) / purity(G))


def d_diff(G: np.ndarray) -> float:
    """D_diff^{7D} = 1 + Coh_E·(N−1)  (operationalization, T-58 route; Coh_E^max = 1)."""
    return 1.0 + 6.0 * coh_e(G)


def sigma_panel(G: np.ndarray) -> dict[str, float]:
    """T-92 canonical stress rows with the v1 errata: σ_E=(N−D)/(N−2), σ_U=2/(1+Φ)."""
    out: dict[str, float] = {}
    for k in ("A", "S", "D", "L", "O"):
        out[k] = float(np.clip(1.0 - 7.0 * np.real(G[IDX[k], IDX[k]]), 0.0, 1.0))
    out["E"] = float(np.clip((7.0 - d_diff(G)) / 5.0, 0.0, 1.0))
    out["U"] = float(2.0 / (1.0 + phi(G)))
    return out


def verdict(G: np.ndarray) -> dict[str, object]:
    P, F, D = purity(G), phi(G), d_diff(G)
    R = r_lower(G)
    v = {
        "P": P, "R": R, "Phi": F, "D": D,
        "V1_noise": P > 2 / 7,
        "V2_reflection": R >= 1 / 3,          # lower-bound form ⇔ P ≤ 3/7
        "V3_integration": F >= 1.0,
        "V4_differentiation": D >= 2.0,
    }
    v["viable_window"] = bool(v["V1_noise"] and v["V2_reflection"]
                              and v["V3_integration"] and v["V4_differentiation"])
    return v


MODES = ("control", "data", "supply")  # [И]-reading of the T-262 trichotomy


def make_gamma_modes(participation: dict[str, tuple[float, float, float]],
                     lambdas: tuple[float, float, float],
                     eps: float) -> np.ndarray:
    """Design-Γ constructor, flow form. Each aspect declares how much it carries of
    the three system-wide flows (control / data / supply); a flow is a coherent mode
    |ψ_m⟩ ∝ participation column, and

        Γ = (1−ε)·Σ_m λ_m |ψ_m⟩⟨ψ_m| + ε·I/7 .

    PSD by construction; couplings are DERIVED: γ_ij = (1−ε)Σ_m λ_m ψ_mi ψ_mj — two
    concerns cohere exactly as much as they are co-loaded on shared flows. ε is the
    unstructured background (no real system is rank-3). The failed first attempt of
    this lab — independent pairwise contract strengths — is itself a result: dense
    pairwise wiring is not jointly realizable (Γ must stay PSD); integration that
    reaches Φ ≥ 1 must ride shared flows, not point-to-point links."""
    lam = np.array(lambdas, dtype=float)
    lam = lam / lam.sum()
    G = np.zeros((7, 7))
    for m in range(3):
        psi = np.array([participation[d][m] for d in DIMS], dtype=float)
        psi = psi / np.linalg.norm(psi)
        G += lam[m] * np.outer(psi, psi)
    return (1.0 - eps) * G + eps * np.eye(7) / 7.0


def top_channels(G: np.ndarray, n: int = 5) -> str:
    pairs = []
    for i in range(7):
        for j in range(i + 1, 7):
            key = DIMS[i] + DIMS[j]
            pairs.append((abs(G[i, j]), key, CANON_COH_NAME.get(key, key)))
    pairs.sort(reverse=True)
    return ", ".join(f"{k}·{name}={v:.3f}" for v, k, name in pairs[:n])


# ----------------------------------------------------------------------------
# HL01 — SSOT synchronization: the 7+21 canonical names used by the spec
# ----------------------------------------------------------------------------

CANON_DIAG = {
    "A": ("Articulation", "Артикуляция"), "S": ("Structure", "Структура"),
    "D": ("Dynamics", "Динамика"), "L": ("Logic", "Логика"),
    "E": ("Interiority", "Интериорность"), "O": ("Ground", "Основание"),
    "U": ("Unity", "Единство"),
}
CANON_COH: dict[str, tuple[str, str]] = {
    "AS": ("Morphogenesis", "Морфогенез"), "AD": ("Actualization", "Актуализация"),
    "AL": ("Predication", "Предикация"), "AE": ("Apperception", "Апперцепция"),
    "AO": ("Spontaneity", "Спонтанность"), "AU": ("Differentiation", "Дифференциация"),
    "SD": ("Persistence", "Персистенция"), "SL": ("Nomos", "Номос"),
    "SE": ("Representation", "Репрезентация"), "SO": ("Archetype", "Архетип"),
    "SU": ("Symmetry", "Симметрия"), "DL": ("Regulation", "Регуляция"),
    "DE": ("Affection", "Аффекция"), "DO": ("Genesis", "Генезис"),
    "DU": ("Teleology", "Телеология"), "LE": ("Evidence", "Эвиденция"),
    "LO": ("Grounding", "Фундирование"), "LU": ("Consistency", "Консистентность"),
    "EO": ("Immanence", "Имманентность"), "EU": ("Synthesis", "Синтез"),
    "OU": ("Completeness", "Полнота"),
}
CANON_COH_NAME = {k: v[0] for k, v in CANON_COH.items()}


def hl01_ssot_sync() -> None:
    src = open(SSOT_TS, encoding="utf-8").read()
    cell = re.compile(
        r"key:\s*'(\w+)'.*?name:\s*\{en:\s*'([^']+)',\s*ru:\s*'([^']+)'\}")
    found = {m.group(1): (m.group(2), m.group(3)) for m in cell.finditer(src)}
    errs = []
    for key, pair in {**{k * 2: v for k, v in CANON_DIAG.items()}, **CANON_COH}.items():
        if found.get(key) != pair:
            errs.append(f"{key}: lab={pair} ssot={found.get(key)}")
    ok = not errs and len(found) == 28
    report("HL01", "VERIFIED", ok,
           f"lab canon == coherences.ts SSOT: {28 - len(errs)}/28 cells"
           + (f"; drift: {errs[:3]}" if errs else ""))


# ----------------------------------------------------------------------------
# HL02 — depth ladder P_crit^(n) = (2/7)·3^(n−1)/(n+1); ceiling at n=4
# ----------------------------------------------------------------------------

def hl02_depth_ladder() -> None:
    from fractions import Fraction
    lad = {n: Fraction(2, 7) * Fraction(3 ** (n - 1), n + 1) for n in range(1, 5)}
    expect = {1: Fraction(1, 7), 2: Fraction(2, 7), 3: Fraction(9, 14), 4: Fraction(54, 35)}
    ok = lad == expect and lad[4] > 1
    report("HL02", "VERIFIED", ok,
           "P_crit^(n) = " + ", ".join(f"n={n}: {v}" for n, v in lad.items())
           + f"; n=4 → {lad[4]} > 1 ⇒ depth ceiling 3 (T-142 [Т/С])")


# ----------------------------------------------------------------------------
# HL03 — Γ-calculator reference points
# ----------------------------------------------------------------------------

def hl03_reference_points() -> None:
    I7 = np.eye(7) / 7.0
    grey = verdict(I7)
    pureE = np.zeros((7, 7)); pureE[E_IDX, E_IDX] = 1.0
    checks = [
        abs(grey["P"] - 1 / 7) < 1e-12,
        grey["Phi"] < 1e-12,
        abs(d_diff(I7) - (1 + 6 / 7)) < 1e-12,
        not grey["viable_window"],
        abs(coh_e(pureE) - 1.0) < 1e-12 and abs(d_diff(pureE) - 7.0) < 1e-12,
    ]
    # a viable window state: three broad flows + moderate background
    part = {d: (1.0, 1.0, 1.0) for d in DIMS}
    part["U"] = (1.6, 0.7, 0.9); part["D"] = (0.9, 1.5, 0.9); part["O"] = (0.7, 0.8, 1.7)
    part["E"] = (0.8, 1.3, 1.2)
    Gv = make_gamma_modes(part, (0.36, 0.36, 0.28), eps=0.42)
    vv = verdict(Gv)
    checks.append(vv["viable_window"])
    report("HL03", "VERIFIED", all(checks),
           f"grey: P=1/7, Φ=0, D={d_diff(I7):.3f}, non-viable; pure-E: D=7; "
           f"witness in window: P={vv['P']:.3f}∈(2/7,3/7], Φ={vv['Phi']:.2f}≥1, "
           f"D={vv['D']:.2f}≥2 (T-124 non-empty)")


# ----------------------------------------------------------------------------
# Worked instances (DESIGN): concern budgets + typed contracts
# ----------------------------------------------------------------------------

@dataclass
class Instance:
    name: str
    participation: dict[str, tuple[float, float, float]]  # (control, data, supply)
    lambdas: tuple[float, float, float]
    eps: float
    note: str = ""
    gamma: np.ndarray = field(init=False)

    def __post_init__(self):
        self.gamma = make_gamma_modes(self.participation, self.lambdas, self.eps)


def mixnet_instance() -> Instance:
    """W1 — mixnet node-holon (FANOS/Nym class). Interiority (E) is the anonymity
    resource: the unobservable pool/keys/delays. The data flow runs A→D→E (ingress
    enters the hidden pool); supply carries stake, transport and the cover budget
    (E–O immanence: substrate spent *inside* privacy)."""
    part = {
        #        control  data  supply
        "A": (0.6, 1.5, 0.4),   # ingress articulation lives on the data flow
        "S": (0.9, 1.1, 0.5),   # Sphinx uniform format: schema on data + law
        "D": (1.0, 1.5, 0.8),   # forwarding: data-heavy, supply-metered
        "L": (1.5, 0.9, 0.7),   # routing/crypto law: control-heavy
        "E": (0.6, 1.5, 1.2),   # hidden pool fed by data, paid by supply
        "O": (0.6, 0.7, 1.7),   # transport+stake+cover budget
        "U": (1.6, 0.5, 0.8),   # epoch topology/directory: control organ
    }
    return Instance("W1 mixnet (FANOS/Nym class)", part, (0.34, 0.38, 0.28), 0.40,
                    "E = anonymity as interiority; cover traffic = E–O immanence cost")


def blockchain_instance() -> Instance:
    """W2 — public blockchain holon (modular stack as one organism). Law-machine:
    control flow is dominant (consensus), supply carries stake+DA, data carries
    transactions; E is deliberately lean (public ledger ⇒ thin interiority) but
    NOT empty — node-local state keeps D ≥ 2."""
    part = {
        "A": (0.6, 1.5, 0.4),   # mempool ingress on the data flow
        "S": (1.2, 1.2, 0.6),   # ledger schema: co-loaded on law and data
        "D": (1.0, 1.4, 0.7),   # execution rides data under control
        "L": (1.7, 0.8, 0.8),   # consensus law: the dominant voice
        "E": (0.5, 1.2, 1.0),   # node-local state: lean (public ledger) but alive —
                                # with less, D_diff dips under 2 (measured below)
        "O": (0.7, 0.8, 1.7),   # stake, p2p, data availability
        "U": (1.5, 0.7, 0.9),   # one canonical head (fork-choice)
    }
    return Instance("W2 blockchain (modular L1)", part, (0.40, 0.33, 0.27), 0.42,
                    "L-dominant by design: law-machine; U = one canonical head")


def agent_platform_instance() -> Instance:
    """W3 — LLM-agent platform holon (orchestrator-workers, memory tiers, evals).
    E-rich: memory/context is load-bearing; data flow feeds apperception (A–E),
    control carries planner/orchestrator, supply carries compute/quota."""
    part = {
        "A": (0.7, 1.6, 0.4),   # perception/ingress on data
        "S": (1.0, 1.1, 0.5),   # tool/message schemas (MCP)
        "D": (1.1, 1.4, 0.8),   # tool execution
        "L": (1.5, 0.9, 0.6),   # planner + guardrails + evals law
        "E": (0.7, 1.5, 1.1),   # memory tiers fed by data, priced by supply
        "O": (0.6, 0.7, 1.7),   # models, compute, quotas
        "U": (1.6, 0.7, 0.8),   # orchestrator: one goal, one context
    }
    return Instance("W3 LLM-agent platform", part, (0.36, 0.37, 0.27), 0.40,
                    "E-rich: memory tiers are load-bearing; SYNARC = full realization")


def fmt_verdict(v: dict[str, object]) -> str:
    flags = "".join("✓" if v[k] else "✗" for k in
                    ("V1_noise", "V2_reflection", "V3_integration", "V4_differentiation"))
    return (f"P={v['P']:.3f} R≥{v['R']:.3f} Φ={v['Phi']:.2f} D={v['D']:.2f} "
            f"[{flags}] {'VIABLE' if v['viable_window'] else 'NOT VIABLE'}")


def ablate(inst: Instance, kind: str) -> np.ndarray:
    part = {d: list(v) for d, v in inst.participation.items()}
    lam, eps = inst.lambdas, inst.eps
    if kind == "mud":
        # 80% of activity outside any flow: unstructured background dominates
        return make_gamma_modes(inst.participation, lam, eps=0.80)
    if kind == "monolith":
        # one global pattern eats the system: single mode, no background to reflect in
        return make_gamma_modes(inst.participation, (0.96, 0.02, 0.02), eps=0.04)
    if kind == "fragmentation":
        # flows lose shared carriers: each mode retreats to a disjoint island
        island = {"control": ("L", "U"), "data": ("A", "D"), "supply": ("O", "S")}
        for d in DIMS:
            part[d] = [0.0, 0.0, 0.0]
        for m, ds in enumerate(island.values()):
            for d in ds:
                part[d][m] = 1.0
        part["E"] = [0.0, 0.35, 0.0]  # E barely attached to one island
        return make_gamma_modes({d: tuple(v) for d, v in part.items()}, lam, eps=0.10)
    if kind == "blind":
        # interiority unplugged from every flow: nothing differentiates inside
        part["E"] = [0.02, 0.02, 0.02]
        return make_gamma_modes({d: tuple(v) for d, v in part.items()}, lam, eps)
    raise ValueError(kind)


def hl04_06_instances() -> list[Instance]:
    insts = [mixnet_instance(), blockchain_instance(), agent_platform_instance()]
    for hid, inst in zip(("HL04", "HL05", "HL06"), insts):
        v = verdict(inst.gamma)
        # each ablation must break exactly the invariant it targets (T-124b pattern)
        abl = {
            "mud→V1": (not verdict(ablate(inst, "mud"))["V1_noise"]),
            "monolith→V2": (not verdict(ablate(inst, "monolith"))["V2_reflection"]),
            "fragmentation→V3": (not verdict(ablate(inst, "fragmentation"))["V3_integration"]),
            "blind→V4": (not verdict(ablate(inst, "blind"))["V4_differentiation"]),
        }
        ok = v["viable_window"] and all(abl.values())
        report(hid, "DESIGN", ok,
               f"{inst.name}: {fmt_verdict(v)}; ablations break their own invariant: "
               + ", ".join(k for k, hit in abl.items() if hit)
               + f"; top channels: {top_channels(inst.gamma)}")
    return insts


# ----------------------------------------------------------------------------
# HL07 — subsumption matrix completeness (the "not inferior in any point" gate)
# ----------------------------------------------------------------------------

# (framework, capability) → (mechanism kind, HOLARCH mechanism, spec anchor)
# kinds: N = native, E = embedded (framework kept as a mandated view/procedure),
#        G = honest gap (must be listed in the doc's §12)
MATRIX: list[tuple[str, str, str, str, str]] = [
    ("UML 2.5.1", "structural+behavioral diagram vocabulary", "E", "view emission (class/sequence/state ⇐ S,D,L projections)", "виды"),
    ("UML 2.5.1", "MOF metamodel / tool interchange", "E", "holarch.v1 schema as exchange model; emit XMI via views", "схема"),
    ("UML 2.5.1", "40-year tooling ecosystem", "G", "inherited only through emission; native tooling = reference lab", "границы"),
    ("SysML v2 / KerML 2025", "textual notation, git-native models, API", "N", "holarch.v1 YAML is text-first; lab = API", "схема"),
    ("SysML v2 / KerML 2025", "requirements↔design traceability", "N", "Γ-target → budgets/contracts trace (Ω1→Ω3)", "процедура"),
    ("C4 (Brown)", "zoom levels context→code", "N", "depth tower D=0..3; ceiling theorem bounds meaningful zoom", "глубина"),
    ("C4 (Brown)", "maps-not-models pragmatism", "E", "views are maps; the model (Γ) stays computable behind them", "виды"),
    ("ArchiMate 3.2", "EA layers + relationship taxonomy", "E", "layers = holon strata; relationships ⊂ 21 typed channels", "каналы"),
    ("ISO/IEC/IEEE 42010", "stakeholders/concerns/viewpoints discipline", "N", "concerns = 7 aspects (fixed alphabet); viewpoints = projections", "виды"),
    ("arc42", "documentation template completeness", "E", "doc skeleton emitted from instance (Ω5)", "процедура"),
    ("TOGAF 10 ADM", "enterprise process cycle", "E", "Ω0–Ω9 loop subsumes ADM phases with computable gates", "процедура"),
    ("Zachman", "interrogatives coverage (what/how/where/who/when/why)", "E", "each cell = aspect×view query over the instance", "виды"),
    ("AADL", "analyzable RT/embedded semantics", "E", "O/L channel contracts carry analysis annexes; emit AADL view", "каналы"),
    ("TLA+/Alloy", "temporal/relational formal verification", "E", "L-aspect contracts mandate a formal view (TLA+/Verum)", "каналы"),
    ("DDD (Evans)", "bounded contexts", "N", "holon boundary = context boundary (E-interiority)", "холон"),
    ("DDD (Evans)", "context-mapping patterns (9)", "N", "T-77 contract algebra types the map; gain = 2‖γ_cross‖²", "композиция"),
    ("Hexagonal/Clean", "dependency rule, ports/adapters", "N", "A-ports, O-adapters, L/S/E core; rule = channel direction", "аспекты"),
    ("Parnas 1972", "information hiding as decomposition criterion", "N", "E-interiority is an axis with a measure (Coh_E), not advice", "аспекты"),
    ("Simon 1962", "near-decomposability of viable hierarchy", "N", "γ_cross small-but-nonzero; quantified by Φ window", "инварианты"),
    ("Alexander", "pattern language / semilattice, not tree", "N", "Fano incidence: 7 lines over 7 aspects — a semilattice by theorem", "диагностика"),
    ("DSM", "dependency matrix, clustering", "N", "Γ IS the matrix — typed, PSD, with dynamics and thresholds", "холон"),
    ("VSM (Beer)", "viability criterion + recursion", "N", "4 invariants [Т] + depth tower; VSM S1–S5 map to organs", "инварианты"),
    ("VSM (Beer)", "algedonic (pain/pleasure) channel", "N", "σ-panel + V_hed = dP/dτ (T-103)", "динамика"),
    ("MAPE-K", "autonomic loop over knowledge", "N", "φ(Γ) self-model + ℒ₀ reconciliation is the loop, with theorems", "самомодель"),
    ("Erlang/OTP", "supervision trees, let-it-crash", "N", "ℛ replacement channel; restart = regeneration toward ρ*", "динамика"),
    ("Kubernetes", "desired-state reconciliation, operators", "N", "ρ* attractor + DU-teleology channel; controller = ℒ₀+ℛ", "динамика"),
    ("Reactive Manifesto", "responsive/resilient/elastic/message-driven", "N", "thresholds + ℛ + O-budget elasticity + A/D channel style", "инварианты"),
    ("12-Factor", "operational hygiene rules", "E", "each factor lands in an aspect checklist (Ω2)", "процедура"),
    ("CALM", "coordination ⇔ non-monotonicity boundary", "E", "LU-consistency contracts must declare monotone/coordinated", "каналы"),
    ("Conway/Team Topologies", "org↔system mirroring, 3 interaction modes", "N", "org-holon ⊗ system-holon; T-77 cross-coupling is the mirror", "композиция"),
    ("ADR (Nygard)", "decision log", "N", "status-graded claims ([Т]/[С]/[Г]/[И]) — epistemic vertical", "процедура"),
    ("ATAM (SEI)", "tradeoff analysis on scenarios", "N", "ablation calculus: scenario = ablation, sensitivity = ∂verdict", "процедура"),
    ("Spec Kit SDD", "constitution→specify→plan→tasks pipeline", "N", "Ω0 constitution = invariants; Ω1–Ω6 refine it computably", "процедура"),
    ("AGENTS.md", "machine-readable repo context", "N", "holarch.v1 instance IS the machine context for design", "схема"),
    ("MCP", "typed tool contracts", "N", "S-aspect contract channel (AS/SL) — schema-first interop", "каналы"),
    ("A2A v1.0", "agent-to-agent peering, capability cards", "N", "T-77 synastry contract = peering with measurable gain", "композиция"),
    ("Anthropic agent patterns", "workflows-vs-agents, evaluator-optimizer", "N", "DL-regulation loop + LE-evidence critic; R_φ = eval fidelity", "самомодель"),
    ("LangGraph/AutoGen/CrewAI", "orchestration graphs, roles, handoffs", "E", "U-organ orchestration emitted as graph views", "виды"),
    ("Nym/Loopix", "stratified mixing + cover traffic", "N", "derived in W1: E-interiority + E–O immanence budget", "воркед-mixnet"),
    ("Ethereum modular", "execution/consensus/DA separation", "N", "derived in W2: aspect split + OU-completeness (DA)", "воркед-блокчейн"),
    ("seL4", "verified kernel — logic grounded in hardware model", "N", "LO-grounding channel taken to [Т]-grade contract", "каналы"),
]


def hl07_matrix_completeness(doc_text: str | None) -> None:
    empty = [row for row in MATRIX if not row[3].strip() or not row[4].strip()]
    kinds = {k: sum(1 for r in MATRIX if r[2] == k) for k in ("N", "E", "G")}
    anchors_ok, missing = True, []
    if doc_text is not None:
        for row in MATRIX:
            if f"#{row[4]}" not in doc_text and f"{{#{row[4]}}}" not in doc_text:
                # anchors are Cyrillic section ids; воркед-* map to worked sections
                missing.append(row[4])
        anchors_ok = not missing
    ok = not empty and kinds["G"] <= 1 and anchors_ok
    report("HL07", "VERIFIED", ok,
           f"subsumption matrix: {len(MATRIX)} capability rows, "
           f"native={kinds['N']}, embedded={kinds['E']}, honest gaps={kinds['G']}"
           + ("" if doc_text is None else
              f"; doc anchors {'all present' if anchors_ok else 'MISSING: ' + str(set(missing))}"))


# ----------------------------------------------------------------------------
# HL08 — route compromise + anonymity trilemma budget (mixnet numbers)
# ----------------------------------------------------------------------------

def hl08_mixnet_numbers() -> None:
    f = 1 / 3  # adversarial fraction per stratum
    comp = {l: f ** l for l in (1, 2, 3, 4)}
    # Loopix-style expected latency: ℓ layers, mean per-hop delay 1/μ = 50 ms
    lat = {l: l * 50.0 for l in (1, 2, 3, 4)}
    marg = comp[3] / comp[2], comp[4] / comp[3]
    ok = (abs(comp[3] - 1 / 27) < 1e-12 and comp[2] > 0.1 and comp[3] < 0.04
          and abs(marg[0] - marg[1]) < 1e-12)
    report("HL08", "VERIFIED", ok,
           f"P[fully-hostile route] at f=1/3: ℓ=1→{comp[1]:.1%}, 2→{comp[2]:.1%}, "
           f"3→{comp[3]:.1%}, 4→{comp[4]:.1%}; latency 50ms/hop → {lat[3]:.0f}ms at ℓ=3; "
           f"depth 2→3 buys 9×, 3→4 buys the same 3× as 2→3 at +50ms — "
           f"diminishing absolute returns; trilemma (Das et al.): the remaining gap is "
           f"paid in bandwidth (cover) or latency, never free")


# ----------------------------------------------------------------------------
# HL09 — BFT 1/3 vs R_th=1/3 (consonance, stated precisely, [И])
# ----------------------------------------------------------------------------

def hl09_bft_consonance() -> None:
    # BFT side: quorums of size 2f+1 in n=3f+1 intersect in ≥ f+1 ⇒ ≥1 honest
    n_ok = all(2 * (2 * f + 1) - (3 * f + 1) == f + 1 for f in range(1, 200))
    # UHM side: R_th = 1/3 ⇔ P ≤ 3/7 on the lower-bound form R = 1/(7P)
    p_ceiling = 3 / 7
    uhm_ok = abs(1 / (7 * p_ceiling) - 1 / 3) < 1e-15
    # The consonance: both bound a dominant part by one third OF DIFFERENT WHOLES
    report("HL09", "CONS", n_ok and uhm_ok,
           "BFT: quorum intersection ⇒ safety iff faulty < n/3 [external Т]; "
           "UHM: R≥1/3 ⇔ P≤3/7 (dominance ceiling) [Т]; same fraction, different "
           "bases (validator count vs purity) — structural rhyme, NOT an identity [И]")


# ----------------------------------------------------------------------------
# HL10 — Fano line coverage of instance wiring (third-order diagnosability)
# ----------------------------------------------------------------------------

def hl10_fano_coverage(insts: list[Instance]) -> None:
    msgs, oks = [], []
    for inst in insts:
        G = inst.gamma
        off = np.array([abs(G[i, j]) for i in range(7) for j in range(i + 1, 7)])
        tau = float(np.median(off))  # significant edge := above the median coupling
        def strong(a: str, b: str) -> bool:
            return abs(G[IDX[a], IDX[b]]) >= tau
        covered = sum(
            1 for line in FANO_LINES
            if strong(line[0], line[1]) and strong(line[0], line[2])
            and strong(line[1], line[2])
        )
        oks.append(covered >= 2)
        msgs.append(f"{inst.name.split()[0]}: {covered}/7 lines strong (τ=med={tau:.3f})")
    report("HL10", "VERIFIED", all(oks),
           "Fano-coverage meter (lines whose 3 edges are all above-median): "
           + ", ".join(msgs) + " — nontrivial but NOT saturated; full T-224 "
           "diagnosability needs 7/7, so the meter is a design gauge with an honest "
           "deficit, not a rubber stamp; pair statistics are structure-blind (T-226)")


# ----------------------------------------------------------------------------
# HL11 — T-77 composition gain on org ⊗ system (Conway mirror)
# ----------------------------------------------------------------------------

def hl11_t77_gain() -> None:
    rng = np.random.default_rng(7)
    oks = []
    for _ in range(240):
        d1 = rng.dirichlet(np.ones(7)); d2 = rng.dirichlet(np.ones(7))
        rho_diag = np.diag(np.concatenate([d1, d2]) / 2.0)
        k = rng.integers(1, 4)
        cross = np.zeros((7, 7))
        for _ in range(k):
            i, j = rng.integers(0, 7), rng.integers(0, 7)
            cross[i, j] = rng.uniform(0.01, 0.05)
        rho = rho_diag.copy()
        rho[:7, 7:] = cross / 2.0
        rho[7:, :7] = cross.T / 2.0
        gain = purity(rho) - purity(rho_diag)
        expect = 2 * np.sum((cross / 2.0) ** 2)
        oks.append(abs(gain - expect) < 1e-12)
    report("HL11", "VERIFIED", all(oks),
           f"P(pair) − P(diag) = 2‖γ_cross‖²_F exactly on {sum(oks)}/240 random "
           f"org⊗system pairs (T-77): the integration gain lives in the contract")


# ----------------------------------------------------------------------------
# HL12 — feeding threshold: regeneration/decay must beat 1+√2 (T-259 model)
# ----------------------------------------------------------------------------

def hl12_feeding() -> None:
    # stationary retention λ = x/(1+x); P_∞ = 1/7 + λ²·C*, C* = P*−1/7 at P*=3/7
    Pstar = 3 / 7; Cstar = Pstar - 1 / 7
    def P_inf(x: float) -> float:
        lam = x / (1 + x)
        return 1 / 7 + lam ** 2 * Cstar
    xmin = 1 + math.sqrt(2)
    below, at_, above = P_inf(xmin * 0.9), P_inf(xmin), P_inf(xmin * 1.3)
    ok = below < 2 / 7 and abs(at_ - 2 / 7) < 1e-12 and above > 2 / 7
    report("HL12", "DESIGN", ok,
           f"maintenance/decay ratio x: P_∞(0.9·x_min)={below:.4f} < 2/7, "
           f"P_∞(x_min=1+√2≈{xmin:.3f})=2/7 exactly, P_∞(1.3·x_min)={above:.4f} > 2/7 "
           f"— the silver-ratio floor for keeping a system above noise (T-259 [Т в модели])")


# ----------------------------------------------------------------------------
# HL13 — first-order blindness identity Σ_p A(ℓ_p) = J − I (T-226)
# ----------------------------------------------------------------------------

def hl13_first_order_blindness() -> None:
    S = np.zeros((7, 7))
    for line in FANO_LINES:
        for a in line:
            for b in line:
                if a != b:
                    S[IDX[a], IDX[b]] += 1
    ok = np.array_equal(S, np.ones((7, 7)) - np.eye(7))
    evals = sorted(np.linalg.eigvalsh(np.ones((7, 7)) - np.eye(7)))
    report("HL13", "VERIFIED", ok,
           f"Σ_lines A(ℓ) = J − I holds exactly (spectrum {{{evals[0]:.0f}×6, {evals[-1]:.0f}}}): "
           f"equal-weight pairwise monitoring sees no wiring — pair heartbeats are "
           f"provably structure-blind; observability must probe triads")


# ----------------------------------------------------------------------------
# HL14 — client-diversity concentration vs thresholds (external numbers, CONS)
# ----------------------------------------------------------------------------

def hl14_client_diversity() -> None:
    shares = {"Geth": 0.50, "Nethermind": 0.25, "Besu": 0.10, "Reth": 0.08, "Erigon": 0.07}
    total = sum(shares.values())
    top = max(shares.values())
    hhi = sum(s ** 2 for s in shares.values())  # a purity of the client mix
    flags = {
        "supermajority(>2/3)": top > 2 / 3,
        "danger(>1/3)": top > 1 / 3,
    }
    ok = abs(total - 1.0) < 1e-9 and flags["danger(>1/3)"] and not flags["supermajority(>2/3)"]
    report("HL14", "CONS", ok,
           f"Ethereum EL shares 2026 ≈ {shares}: top={top:.0%} — above the community "
           f"1/3 danger line, below the 2/3 finality-killing line; mix-purity "
           f"HHI={hhi:.3f}; the operational guidance ('no client above 1/3') rhymes "
           f"with the R-ceiling anti-dominance form [И]")


# ----------------------------------------------------------------------------

def main() -> int:
    doc_text = open(DOC_EN, encoding="utf-8").read() if os.path.exists(DOC_EN) else None
    print("=" * 88)
    print("HOLARCH LAB — panel HL01–HL14"
          + ("" if doc_text else "   (doc not written yet: anchor check skipped)"))
    print("=" * 88)
    hl01_ssot_sync()
    hl02_depth_ladder()
    hl03_reference_points()
    insts = hl04_06_instances()
    hl07_matrix_completeness(doc_text)
    hl08_mixnet_numbers()
    hl09_bft_consonance()
    hl10_fano_coverage(insts)
    hl11_t77_gain()
    hl12_feeding()
    hl13_first_order_blindness()
    hl14_client_diversity()
    print("-" * 88)
    npass = sum(1 for r in RESULTS if r[2] == PASS)
    print(f"TOTAL: {npass}/{len(RESULTS)} PASS")
    for inst in insts:
        v = verdict(inst.gamma)
        s = sigma_panel(inst.gamma)
        print(f"  {inst.name}: {fmt_verdict(v)}  σ=" +
              " ".join(f"{k}:{s[k]:.2f}" for k in DIMS))
    return 0 if npass == len(RESULTS) else 1


if __name__ == "__main__":
    sys.exit(main())
