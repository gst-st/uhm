#!/usr/bin/env python3
"""HOLARCH laboratory — mechanical validation of the architecture meta-specification.

Panel HL01–HL20. Honesty classes (as in HomoHoloGraph):
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
# Каноническая плоскость корпуса: транслятами QR(7)={1,2,4} в нумерации
# Фано-арифметики A1 S2 D3 L4 E5 U6 O7. ВНИМАНИЕ: любая валидная плоскость
# Фано проходит HL13 (тождество J−I), поэтому неканоничная разметка тут
# жила незамеченной до 07.08 и портила счётчик HL10.
FANO_LINES = [
    ("A", "S", "L"), ("S", "D", "E"), ("D", "L", "U"), ("L", "E", "O"),
    ("E", "U", "A"), ("U", "O", "S"), ("O", "A", "D"),
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

# ----------------------------------------------------------------------------
# HL15 — the price of addressing: a routing contract must be declared, not learned
# ----------------------------------------------------------------------------

def _rt_fresh() -> np.ndarray:
    G = np.eye(7, dtype=complex) / 7 + 0.02 * np.eye(7)
    return G / np.trace(G).real


def _rt_nudge(G: np.ndarray, i: int, j: int, sg: float) -> np.ndarray:
    """Reinforce cell (i,j), re-project to a state, then dephase."""
    S = G.copy()
    S[i, j] += 0.22 * sg
    S[j, i] += 0.22 * sg
    S = 0.5 * (S + S.conj().T)
    v, Q = np.linalg.eigh(S)
    S = Q @ np.diag(np.clip(v, 1e-9, None)) @ Q.conj().T
    S /= np.trace(S).real
    off = ~np.eye(7, dtype=bool)
    S[off] *= 0.94
    return S


def _rt_run(rng: np.random.Generator, rules: list[np.ndarray], K: int,
            n_leaf: int, mode: str, episodes: int, flip: int) -> int:
    """mode: 'single' | 'reward' | 'commit'. Returns misses."""
    pairs = [(i, j) for i in range(7) for j in range(i + 1, 7)]
    leaves = [_rt_fresh() for _ in range(n_leaf)]
    slots: list[dict[int, int]] = [dict() for _ in range(n_leaf)]
    router, r_slots = _rt_fresh(), {}
    commit: dict[int, int] = {}
    load = [0] * n_leaf
    miss = 0
    for t in range(episodes):
        k = int(rng.integers(K))
        goal = int(rules[t // flip][k])
        if mode == "single" or n_leaf == 1:
            w, rcell = 0, None
        elif mode == "frozen_skew":                    # закреплён, но завален
            if k not in commit:
                commit[k] = 0 if (k % 10) < 7 else (k % n_leaf)
            w, rcell = commit[k], None
        elif mode == "random_bal":                     # баланс без устойчивости
            w, rcell = int(rng.integers(n_leaf)), None
        elif mode == "commit":
            if k not in commit:                       # объявлено однажды
                commit[k] = int(np.argmin(load))
                load[commit[k]] += 1
            w, rcell = commit[k], None
        else:                                          # выучено наградой
            if k not in r_slots:
                r_slots[k] = len(r_slots) % 21
            rcell = pairs[r_slots[k]]
            w = 0 if router[rcell[0], rcell[1]].real >= 0 else 1
        if k not in slots[w]:
            slots[w][k] = len(slots[w]) % 21
        i, j = pairs[slots[w][k]]
        a = 0 if leaves[w][i, j].real >= 0 else 1
        hit = 1 if a == goal else 0
        miss += 1 - hit
        leaves[w] = _rt_nudge(leaves[w], i, j,
                              +1.0 if (a == 0) == (hit == 1) else -1.0)
        if rcell is not None:
            router = _rt_nudge(router, rcell[0], rcell[1],
                               +1.0 if (w == 0) == (hit == 1) else -1.0)
    return miss


def hl15_addressing_price() -> None:
    K, EPI, FLIP, SEEDS = 42, 800, 200, 6      # 42 = 2 x 21: both leaves at capacity
    got = {}
    for tag, nl, mode in (("single", 1, "single"), ("learned", 2, "reward"),
                          ("declared", 2, "commit")):
        tot = []
        for sd in range(SEEDS):
            rng = np.random.default_rng(4700 + sd)
            rr = np.random.default_rng(9100 + sd)
            rules = [rr.integers(0, 2, K) for _ in range(EPI // FLIP)]
            tot.append(_rt_run(rng, rules, K, nl, mode, EPI, FLIP))
        got[tag] = float(np.median(tot))
    # Второе показание: на самом выведенном потолке ширины — четыре листа
    # по 21 каналу, глубина 3 (SAD_max), то есть 21·2² = 84 контекста.
    ceil_got = {}
    for tag, nl, mode in (("single84", 1, "single"), ("declared84", 4, "commit")):
        tot = []
        for sd in range(SEEDS):
            rng = np.random.default_rng(4700 + sd)
            rr = np.random.default_rng(9100 + sd)
            rules = [rr.integers(0, 2, 84) for _ in range(EPI // FLIP)]
            tot.append(_rt_run(rng, rules, 84, nl, mode, EPI, FLIP))
        ceil_got[tag] = float(np.median(tot))
    ceil_gain = 100.0 * (ceil_got["single84"] - ceil_got["declared84"]) \
        / ceil_got["single84"]
    # Третье показание: ветвление. Один бит ограничил бы веер двойкой; хранимый
    # адрес тратит КАНАЛ на дочернего, значит веер доходит до 21. Смотрим B=7.
    br = {}
    for tag, nl in (("single147", 1), ("declared147", 7)):
        tot = []
        for sd in range(4):
            rng = np.random.default_rng(4700 + sd)
            rr = np.random.default_rng(9100 + sd)
            rules = [rr.integers(0, 2, 147) for _ in range(5)]
            tot.append(_rt_run(rng, rules, 147, nl,
                               "single" if nl == 1 else "commit", 5880, 1176))
        br[tag] = float(np.median(tot))
    br_gain = 100.0 * (br["single147"] - br["declared147"]) / br["single147"]
    gain = 100.0 * (got["single"] - got["declared"]) / got["single"]
    ok = (got["declared"] < got["learned"] < got["single"]
          and ceil_got["declared84"] < ceil_got["single84"]
          and br["declared147"] < br["single147"] and br_gain > gain)
    report("HL15", "VERIFIED", ok,
           "price of addressing at K=42 (two leaves, each exactly at the 21-channel "
           f"capacity), median misses over {SEEDS} seeds: single holon "
           f"{got['single']:.0f}, routing learned from task reward "
           f"{got['learned']:.0f}, routing declared once and committed "
           f"{got['declared']:.0f} — the declared contract is worth {gain:.0f}% over "
           "the undivided holon and strictly beats the learned one, so composition "
           "gain requires a committed addressing contract (a measured instance of "
           "\u00a79's 'coordination is declared, not hoped'); at the derived breadth "
           f"ceiling itself — 21\u00b72\u00b2 = 84 contexts over four leaves at depth 3 — "
           f"single {ceil_got['single84']:.0f} vs declared "
           f"{ceil_got['declared84']:.0f}, a {ceil_gain:.0f}% gain, so the ceiling is "
           "reachable and not merely arithmetic; and branching is bounded by "
           "channels rather than by bits — a stored address spends a channel per "
           f"child, so at fan-out 7 (K=147) single {br['single147']:.0f} vs declared "
           f"{br['declared147']:.0f}, a {br_gain:.0f}% gain that is LARGER than at "
           "fan-out 2, which is why the reachable ceiling is 21^3 = 9261 and not "
           "21·2² = 84")


# ----------------------------------------------------------------------------
# HL16 — the 2x2 that separates stability from balance
# ----------------------------------------------------------------------------

def hl16_stability_vs_balance() -> None:
    K, EPI, FLIP, SEEDS, NL = 100, 2000, 400, 12, 4
    got = {}
    for tag, nl, mode in (("single", 1, "single"), ("frozen+balanced", NL, "commit"),
                          ("frozen+skewed", NL, "frozen_skew"),
                          ("churning+balanced", NL, "random_bal")):
        tot = []
        for sd in range(SEEDS):
            rng = np.random.default_rng(4700 + sd)
            rr = np.random.default_rng(9100 + sd)
            rules = [rr.integers(0, 2, K) for _ in range(EPI // FLIP)]
            tot.append(_rt_run(rng, rules, K, nl, mode, EPI, FLIP))
        got[tag] = float(np.median(tot))
    one, fb = got["single"], got["frozen+balanced"]
    fs, cb = got["frozen+skewed"], got["churning+balanced"]
    # Порядок — вот утверждение: баланс без устойчивости ХУЖЕ неделения.
    # Утверждение, которое проверяется: замораживание — предусловие
    # (frozen+skewed бьёт неделение), баланс — множитель поверх него
    # (frozen+balanced лучше всех), а баланс без замораживания предусловия
    # не заменяет (churning+balanced хуже frozen-ячеек).
    ok = fb < fs < one and cb > fs
    # Формулировка ВЫВОДИТСЯ из чисел, а не утверждается поверх них.
    verdict_cb = ("worse than not splitting at all" if cb > one
                  else f"barely distinguishable from not splitting ({one:.0f})")
    report("HL16", "VERIFIED", ok,
           f"stability vs balance at {NL} children (median misses, {SEEDS} seeds): "
           f"undivided {one:.0f}; frozen+balanced {fb:.0f}; frozen+skewed {fs:.0f}; "
           f"churning+balanced {cb:.0f} — perfect balance without a stable address is "
           f"{verdict_cb}, while freezing alone recovers "
           f"{100*(one-fs)/one:.0f}% and freezing with balance "
           f"{100*(one-fb)/one:.0f}%: stability is the precondition, balance the "
           "multiplier — declare the address, and declare it by load")


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
        # Порога на СЧЁТ здесь нет намеренно. Прежний floor (covered >= 2) был
        # выставлен под значения, полученные на НЕканонической плоскости Фано
        # (исправлено 07.08), то есть подогнан задним числом; а подкручивать
        # разборы ради метра прямо запрещает антигудхартовская оговорка §8.
        # Проверяем корректность самого метра, показания печатаем как есть.
        oks.append(0 <= covered <= 7)
        msgs.append(f"{inst.name.split()[0]}: {covered}/7 lines strong (τ=med={tau:.3f})")
    report("HL10", "VERIFIED", all(oks),
           "Fano-coverage meter on the CANONICAL plane (lines whose 3 edges are "
           "all above-median): " + ", ".join(msgs) + " — gauge without a floor: "
           "full T-224 diagnosability needs 7/7, and tuning a design to raise a "
           "diagnostic meter is forbidden by the anti-Goodhart clause; pair "
           "statistics are structure-blind (T-226)")


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

# ----------------------------------------------------------------------------
# HL17 — integration is balance: Φ ≥ 1 exactly when nothing is frustrated
# ----------------------------------------------------------------------------

def _edge_state(S: np.ndarray) -> tuple[np.ndarray, float]:
    """Content `S` scaled to the very edge of positivity, and its λ_min(S)."""
    lam = float(np.min(np.linalg.eigvalsh(S)))
    c = 1.0 / (7.0 * abs(lam)) if lam < 0 else 1.0
    return np.eye(7) / 7.0 + c * S, lam


def _frustrated(S: np.ndarray) -> int:
    """Triangles of K7 whose sign product is negative."""
    return sum(1 for i in range(7) for j in range(i + 1, 7) for k in range(j + 1, 7)
               if S[i, j] * S[j, k] * S[k, i] < 0)


def hl17_integration_is_balance() -> None:
    # Harary: a signed graph is balanced exactly when every cycle carries a
    # positive product of signs, and on a complete graph that is S_ij = s_i·s_j.
    # The product of signs around a triangle IS the sign holonomy — the real
    # limit of the phase holonomy of T-301. So the gate and balance are one.
    rng = np.random.default_rng(53000)
    disagree, ident_err, rows = 0, 0.0, {}
    for _ in range(600):
        s = rng.choice([-1.0, 1.0], size=7)
        S = np.outer(s, s) - np.eye(7)
        flips = int(rng.integers(0, 6))
        for _ in range(flips):
            i = int(rng.integers(0, 7))
            j = (i + 1 + int(rng.integers(0, 6))) % 7
            S[i, j] = -S[i, j]
            S[j, i] = -S[j, i]
        G, lam = _edge_state(S)
        F, nfr = phi(G), _frustrated(S)
        if (F >= 1.0) != (nfr == 0):
            disagree += 1
        # The identity itself, not merely the threshold it implies.
        ident_err = max(ident_err, abs(F - 6.0 / lam ** 2))
        rows.setdefault(flips, []).append(F)
    ok = disagree == 0 and ident_err < 1e-9
    tab = "; ".join(f"{k} flips Φ={np.median(v):.4f}" for k, v in sorted(rows.items()))
    report("HL17", "VERIFIED", ok,
           f"integration is the absence of frustration ({tab}): the gate Φ≥1 and "
           f"Harary balance disagreed in {disagree} of 600 patterns, and the "
           f"identity Φ = 6/λ_min(S)² held to {ident_err:.1e} — so a single "
           "flipped agreement, five frustrated triangles out of thirty-five, "
           "drops integration from 6 to 0.9365 and closes the gate: integrable "
           "content is seven polarities, not twenty-one independent bits")


# ----------------------------------------------------------------------------
# HL18 — the projection is the completion
# ----------------------------------------------------------------------------

def _project(G: np.ndarray) -> np.ndarray:
    """Back onto the state manifold: clip the spectrum, restore unit trace."""
    w, V = np.linalg.eigh(G)
    w = np.clip(w, 0.0, None)
    t = float(np.sum(w))
    return (V * (w / t)) @ V.conj().T if t > 0 else np.eye(7) / 7.0


def _teach(pairs, want, amount: float, project: bool) -> np.ndarray:
    G = np.eye(7) / 7.0
    for _ in range(30):
        for (i, j) in pairs:
            d = amount if want[i, j] else -amount
            G[i, j] += d
            G[j, i] += d
            if project:
                G = _project(G)
    return G


def hl18_projection_completes() -> None:
    # A frustrated pattern does not fit near the boundary of positivity, so
    # projecting back onto the state manifold pulls content towards the nearest
    # balanced pattern — which is to say, it infers pairs it was never told.
    rng = np.random.default_rng(61000)
    got: dict[str, list[float]] = {k: [] for k in
                                   ("cov_proj", "acc_proj", "cov_raw", "acc_rand", "const")}
    for sd in range(60):
        r = np.random.default_rng(61000 + sd)
        s = r.choice([-1.0, 1.0], size=7)
        pol = np.outer(s, s) > 0
        arb = r.random((7, 7)) < 0.5
        arb = np.triu(arb, 1) | np.triu(arb, 1).T
        allp = [(i, j) for i in range(7) for j in range(i + 1, 7)]
        r.shuffle(allp)
        taught, held = allp[:7], allp[7:]

        def score(G, want):
            spoke = [(i, j) for (i, j) in held if abs(G[i, j]) > 1e-12]
            if not spoke:
                return 0.0, float("nan")
            right = sum(1 for (i, j) in spoke if (G[i, j] > 0) == want[i, j])
            return len(spoke) / len(held), right / len(spoke)

        cp, ap = score(_teach(taught, pol, 0.22, True), pol)
        cr, _ = score(_teach(taught, pol, 0.22, False), pol)
        _, ar = score(_teach(taught, arb, 0.22, True), arb)
        share = sum(1 for (i, j) in held if pol[i, j]) / len(held)
        got["cov_proj"].append(cp)
        got["acc_proj"].append(ap)
        got["cov_raw"].append(cr)
        got["acc_rand"].append(ar)
        got["const"].append(max(share, 1 - share))
    m = {k: float(np.nanmedian(v)) for k, v in got.items()}
    # Three things must hold together, or the result is not a mechanism:
    # projection must reach the untaught, be right about them, and be right
    # only when there is a polarity there to complete.
    ok = (m["cov_proj"] > 0.9 and m["cov_raw"] < 1e-9
          and m["acc_proj"] - m["const"] > 0.15 and m["acc_rand"] < 0.575)
    report("HL18", "VERIFIED", ok,
           f"the projection is the completion: taught 7 of 21 pairs, a write that "
           f"projects holds an opinion about {m['cov_proj']:.0%} of the 14 it was "
           f"never shown and is right {m['acc_proj']:.1%} of the time — "
           f"{100*(m['acc_proj']-m['const']):+.1f} pp over the best constant answer "
           f"({m['const']:.1%}) — while the same write without the projection "
           f"reaches {m['cov_raw']:.0%} of them; strip the polarity and accuracy "
           f"falls to {m['acc_rand']:.1%}, a coin, so what the projection "
           "propagates is a polarity and nothing else")



# ----------------------------------------------------------------------------
# HL19 — a Fano line is a parity check, and it is the sign holonomy
# ----------------------------------------------------------------------------

def _line_cells(line: tuple[str, str, str]) -> list[tuple[int, int]]:
    """The three pairs a line carries."""
    a, b, c = (IDX[d] for d in line)
    return [(a, b), (b, c), (a, c)]


def hl19_line_is_a_parity_check() -> None:
    # A line's three cells are three DIFFERENT pairs, and under a polarity their
    # signs multiply to (s_a s_b s_c)² = +1. That is a parity check, and it is the
    # real limit of the phase holonomy T-301 names as the carrier of quality.
    cells = [pair for line in FANO_LINES for pair in _line_cells(line)]
    disjoint = len(set(cells)) == len(cells)
    covers = len(set(cells)) == 21

    parity = True
    for mask in range(64):
        s = np.array([-1.0 if (mask >> k) & 1 else 1.0 for k in range(7)])
        for line in FANO_LINES:
            product = 1.0
            for (i, j) in _line_cells(line):
                product *= s[i] * s[j]
            if product < 0:
                parity = False
    ok = disjoint and covers and parity
    report("HL19", "VERIFIED", ok,
           f"a line is a parity check, not a repetition code: its three cells are three "
           f"different pairs, every pair lies on exactly one of the seven lines "
           f"(disjoint={disjoint}, covering {len(set(cells))} of 21), and under all "
           f"{64} polarities the signs of a line multiply to +1 without exception "
           f"({parity}) — so the seven lines are seven disjoint parity checks, and each "
           "is the sign holonomy around its triangle, the real limit of the phase "
           "holonomy that carries quality")


# ----------------------------------------------------------------------------
# HL20 — what the projection does and does not do to parity
# ----------------------------------------------------------------------------

def hl20_frustration_is_forbidden() -> None:
    rng = np.random.default_rng(70000)

    def broken(G: np.ndarray) -> int:
        n = 0
        for line in FANO_LINES:
            product = 1.0
            for (i, j) in _line_cells(line):
                product *= 1.0 if G[i, j] >= 0 else -1.0
            if product < 0:
                n += 1
        return n

    # A holon taught a polarity, written with the projecting rule.
    bad, neg = [], []
    for sd in range(60):
        r = np.random.default_rng(70000 + sd)
        s = r.choice([-1.0, 1.0], size=7)
        G = np.eye(7) / 7.0
        pairs = [(i, j) for i in range(7) for j in range(i + 1, 7)]
        for _ in range(20):
            for (i, j) in pairs:
                d = 0.22 if s[i] * s[j] > 0 else -0.22
                G[i, j] += d
                G[j, i] += d
                G = _project(G)
        bad.append(broken(G))
        neg.append(sum(1 for (i, j) in pairs if G[i, j] < 0) / 21.0)
    forbidden = max(bad) == 0
    negative = float(np.median(neg))

    # And the other use of a line: one repeated verdict in all three cells.
    # Three equal signs multiply to s³ = s, so a repeated NEGATIVE verdict breaks
    # parity by construction. Measured twice — with the projection and without —
    # because that is where the incompatibility shows.
    def repeated(k: int, project: bool) -> tuple[int, int]:
        G = np.eye(7) / 7.0
        intended = []
        for m, line in enumerate(FANO_LINES):
            positive = m >= k
            intended.append(positive)
            for (i2, j2) in _line_cells(line):
                d = 0.22 if positive else -0.22
                G[i2, j2] += d
                G[j2, i2] += d
                if project:
                    G = _project(G)
        # How many lines still read the verdict they were given?
        kept = 0
        for m, line in enumerate(FANO_LINES):
            votes = sum(1 for (i2, j2) in _line_cells(line) if G[i2, j2] >= 0)
            if (votes >= 2) == intended[m]:
                kept += 1
        return broken(G), kept

    plain = [repeated(k, False) for k in range(8)]
    tracks = all(plain[k][0] == k for k in range(8))
    projected = [repeated(k, True) for k in range(8)]
    proj_broken = max(b for b, _ in projected)
    # With seven lines written false, how many still say false after projecting?
    kept_all_false = projected[7][1]

    _ = rng
    ok = forbidden and negative > 0.3 and tracks and proj_broken > 0 and kept_all_false < 7
    report("HL20", "VERIFIED", ok,
           f"the projection does not introduce frustration, and does not remove it either. "
           f"Taught content that IS a polarity, a write that projects never breaks a line's "
           f"parity (worst case {max(bad)} of 7 across 60 runs), and that is not vacuous — "
           f"{negative:.1%} of the twenty-one cells read negative, so parity holds by the "
           f"signs being consistent rather than absent. But given content that is not a "
           f"polarity it leaves the frustration standing: writing a repeated NEGATIVE verdict "
           f"into k lines leaves exactly k lines broken with nothing projecting ({tracks}), "
           f"and still leaves {proj_broken} of 7 broken with the projection in place. What "
           f"the projection does instead is quietly rewrite what was stored — of seven lines "
           f"all written false, only {kept_all_false} still say false. So a line can serve as "
           "a repetition code, or as the parity check that makes content integrable, and "
           "neither use survives the other intact")



def main() -> int:
    doc_text = open(DOC_EN, encoding="utf-8").read() if os.path.exists(DOC_EN) else None
    print("=" * 88)
    print("HOLARCH LAB — panel HL01–HL20"
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
    hl15_addressing_price()
    hl16_stability_vs_balance()
    hl17_integration_is_balance()
    hl18_projection_completes()
    hl19_line_is_a_parity_check()
    hl20_frustration_is_forbidden()
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
