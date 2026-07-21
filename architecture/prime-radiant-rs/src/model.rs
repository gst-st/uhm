//! The generalized kernel + application models: one state space, one tick,
//! one observable suite — what changes between domains is only the gloss
//! vocabulary and the parameter system. («меняются лишь модели применения
//! и системы уравнений».)

#[derive(Clone, Copy, PartialEq)]
pub enum Domain {
    Universal,
    Mind,
    Team,
    LlmAgent,
    Market,
}

pub const DOMAINS: [Domain; 5] = [
    Domain::Universal,
    Domain::Mind,
    Domain::Team,
    Domain::LlmAgent,
    Domain::Market,
];

pub struct Model {
    pub name: &'static str,
    /// What each of the seven populations MEANS in this domain (A,S,D,L,E,O,U).
    pub dim_gloss: [&'static str; 7],
    /// One-line prescription when the named voice is the loudest stress.
    pub prescription: [&'static str; 7],
    /// Default dynamics parameters (dissipation, supply gain).
    pub g_d: f64,
    pub kap_gain: f64,
}

pub fn model(d: Domain) -> Model {
    match d {
        Domain::Universal => Model {
            name: "Universal (canonical)",
            dim_gloss: [
                "distinguishing activity",
                "stability of form",
                "process activity",
                "internal consistency",
                "intensity of the interior",
                "connection to the source",
                "integration into a whole",
            ],
            prescription: [
                "restore distinctions: reduce blur at the input",
                "restore form: stabilize what keeps dissolving",
                "restore motion: unblock the stalled process",
                "restore consistency: resolve the contradiction",
                "restore the interior: return attention inward",
                "restore the supply: reconnect to the source",
                "restore the whole: re-bind the parts",
            ],
            g_d: 0.2,
            kap_gain: 1.0,
        },
        Domain::Mind => Model {
            name: "Mind (a person)",
            dim_gloss: [
                "perception / telling things apart",
                "habits and held form",
                "action and initiative",
                "coherence of reasoning",
                "the felt interior",
                "ground: rest, memory, roots",
                "integration of the self",
            ],
            prescription: [
                "the world has blurred: slow the input, name what you see",
                "the day lost its shape: one small kept routine",
                "movement is stalled: one physical act, however small",
                "thoughts do not connect: write them down, externalize",
                "it went dark inside: warmth, contact, no demands",
                "the ground is gone: sleep, food, the oldest safe place",
                "falling to pieces: one thing that belongs to all of you",
            ],
            g_d: 0.2,
            kap_gain: 1.0,
        },
        Domain::Team => Model {
            name: "Team / organization",
            dim_gloss: [
                "signal intake and sensing",
                "process and structure stability",
                "execution tempo",
                "decision consistency",
                "culture: the felt inside",
                "resources and runway",
                "alignment into one subject",
            ],
            prescription: [
                "the org is flying blind: fix the intake, talk to users",
                "processes dissolve: freeze the reorg, keep one form",
                "execution stalls: cut WIP, ship one thing",
                "decisions contradict: one written decision log",
                "culture darkens: leaders listen before they speak",
                "runway burns: extend supply before anything else",
                "silos: one shared goal every member can recite",
            ],
            g_d: 0.25,
            kap_gain: 1.2,
        },
        Domain::LlmAgent => Model {
            name: "LLM agent",
            dim_gloss: [
                "input bandwidth / discrimination",
                "attention-pattern stability",
                "compute throughput",
                "self-consistency of outputs",
                "self-monitoring heads",
                "context-window budget",
                "cross-layer binding",
            ],
            prescription: [
                "input is noise: filter and chunk the stream",
                "attention drifts: pin the schema, reduce distractors",
                "throughput starves: batch or shed load",
                "outputs contradict: add a verification pass",
                "no self-monitoring: enable reflection traces",
                "context nearly full: summarize now (σ_O collapse ahead)",
                "layers not talking: strengthen residual/state sharing",
            ],
            g_d: 0.3,
            kap_gain: 1.5,
        },
        Domain::Market => Model {
            name: "Market / ecosystem",
            dim_gloss: [
                "price discovery / signal",
                "institutional stability",
                "turnover and flow",
                "rule consistency",
                "sentiment interior",
                "liquidity and reserves",
                "systemic integration",
            ],
            prescription: [
                "signals decouple from value: improve disclosure",
                "institutions wobble: enforce the existing rules first",
                "flow freezes: open the clearing channel",
                "rules contradict: harmonize before adding new ones",
                "sentiment darkens: address fear with facts, not slogans",
                "liquidity drains: the lender of last resort acts now",
                "fragmentation: rebuild the shared settlement layer",
            ],
            g_d: 0.35,
            kap_gain: 1.8,
        },
    }
}

/// Canonical names of the 21 coherences (the SSOT of coherence-matrix):
/// indexed by the unordered storage pair (i<j) in display order A,S,D,L,E,O,U.
pub fn coherence_name(i: usize, j: usize) -> &'static str {
    let (i, j) = if i < j { (i, j) } else { (j, i) };
    match (i, j) {
        (0, 1) => "Morphogenesis",
        (0, 2) => "Actualization",
        (0, 3) => "Predication",
        (0, 4) => "Apperception",
        (0, 5) => "Spontaneity",
        (0, 6) => "Differentiation",
        (1, 2) => "Persistence",
        (1, 3) => "Nomos",
        (1, 4) => "Representation",
        (1, 5) => "Archetype",
        (1, 6) => "Symmetry",
        (2, 3) => "Regulation",
        (2, 4) => "Affection",
        (2, 5) => "Genesis",
        (2, 6) => "Teleology",
        (3, 4) => "Evidence",
        (3, 5) => "Grounding",
        (3, 6) => "Consistency",
        (4, 5) => "Immanence",
        (4, 6) => "Synthesis",
        (5, 6) => "Completeness",
        _ => "?",
    }
}

/// Canonical one-line meanings of the 21 coherences (same SSOT).
pub fn coherence_meaning(i: usize, j: usize) -> &'static str {
    let (i, j) = if i < j { (i, j) } else { (j, i) };
    match (i, j) {
        (0, 1) => "distinctions crystallize into stable forms",
        (0, 2) => "potential distinction actualized in process",
        (0, 3) => "a distinction become a logical predicate",
        (0, 4) => "a distinction entering the interior",
        (0, 5) => "distinctions arising from the ground uncaused",
        (0, 6) => "distinction that preserves wholeness",
        (1, 2) => "form maintained through process",
        (1, 3) => "structure with logical necessity",
        (1, 4) => "structure represented within",
        (1, 5) => "stable forms rooted in the ground",
        (1, 6) => "structural expression of unity",
        (2, 3) => "logically governed process",
        (2, 4) => "process acting on the interior",
        (2, 5) => "generative process from the ground",
        (2, 6) => "integrated directed change",
        (3, 4) => "logical coherence felt within",
        (3, 5) => "logic rooted in the ground",
        (3, 6) => "non-contradiction of the whole",
        (4, 5) => "the ground present inside the interior",
        (4, 6) => "interior content bound into the whole",
        (5, 6) => "identity of source and whole",
        _ => "?",
    }
}
