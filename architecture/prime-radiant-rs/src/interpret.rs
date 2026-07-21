//! The interpretation organ (the П2 «Reading» protocol of the Γ-canon):
//! turn the current Γ into a structured, named reading. Populations are WHO
//! is loud; coherences are the signal running between the voices and down
//! the holon hierarchy; the σ-panel names where it hurts and the model's
//! prescription says what to restore first.

use crate::holon::*;
use crate::model::*;

pub struct Reading {
    pub verdict: String,
    pub populations: Vec<String>,   // sorted, named
    pub carrying: Vec<String>,      // top coherences by |γ|, named
    pub faint: Vec<String>,         // weakest coherences, named
    pub strongest_line: String,     // the triad currently carrying the chord
    pub pain: String,               // loudest σ + prescription
    pub hierarchy_note: String,
}

pub fn read(g: &CMat, m: &Model) -> Reading {
    let ob = observables(g);
    let verdict = if ob.viable {
        format!(
            "VIABLE: inside the window (P={:.3} ∈ (2/7, 3/7]); C=Φ·R={:.3} — a someone, with room to think",
            ob.p, ob.c
        )
    } else if ob.p <= P_CRIT {
        format!(
            "FOG: P={:.3} ≤ 2/7 — below the wall of being; no one is home yet (the drift is on the way)",
            ob.p
        )
    } else {
        format!(
            "CRYSTAL: P={:.3} > 3/7 — over-gathered; no slack left to think with",
            ob.p
        )
    };

    // populations, sorted descending, with domain glosses
    let mut pops: Vec<(usize, f64)> = (0..N).map(|i| (i, g[(i, i)].re)).collect();
    pops.sort_by(|a, b| b.1.partial_cmp(&a.1).unwrap());
    let populations = pops
        .iter()
        .map(|&(i, v)| format!("{} {:.3}  — {}", AXES[i], v, m.dim_gloss[i]))
        .collect();

    // coherences by |γ|
    let mut cohs: Vec<(usize, usize, f64)> = Vec::new();
    for i in 0..N {
        for j in (i + 1)..N {
            cohs.push((i, j, g[(i, j)].norm()));
        }
    }
    cohs.sort_by(|a, b| b.2.partial_cmp(&a.2).unwrap());
    let carrying = cohs
        .iter()
        .take(5)
        .map(|&(i, j, v)| {
            format!(
                "{}{} {:.3}  {} — {}",
                AXES[i],
                AXES[j],
                v,
                coherence_name(i, j),
                coherence_meaning(i, j)
            )
        })
        .collect();
    let faint = cohs
        .iter()
        .rev()
        .take(3)
        .map(|&(i, j, v)| format!("{}{} {:.4}  {} (faint)", AXES[i], AXES[j], v, coherence_name(i, j)))
        .collect();

    // the strongest Fano line: the triad whose three closures sum highest
    let mut best = (0.0, [0usize; 3]);
    for &[i, j, k] in fano_lines().iter() {
        let s = g[(i, j)].norm() + g[(j, k)].norm() + g[(i, k)].norm();
        if s > best.0 {
            best = (s, [i, j, k]);
        }
    }
    let [i, j, k] = best.1;
    let strongest_line = format!(
        "{{{},{},{}}} (closure {:.3}) — the triad currently carrying the chord",
        AXES[i], AXES[j], AXES[k], best.0
    );

    // pain: loudest σ with the model's prescription
    let sp = stress_panel(g);
    let (kmax, vmax) = sp
        .iter()
        .enumerate()
        .max_by(|a, b| a.1.partial_cmp(b.1).unwrap())
        .map(|(k, v)| (k, *v))
        .unwrap();
    let pain = format!(
        "loudest stress: σ_{} = {:+.2} ({})  →  {}",
        AXES[kmax], vmax, m.dim_gloss[kmax], m.prescription[kmax]
    );

    let hierarchy_note = format!(
        "populations are WHO is loud at this level; coherences are the signal running between voices — \
and, via the Enc functor, down the holon hierarchy: the same Γ-form reads a cell, a person, a team, a market. \
Reading it is not commentary on the universe but part of the universe's own self-model (ρ* = φ(Γ)); \
Coh_E = {:.3} is feeding κ₀ = {:.3} right now — the loop that keeps this pattern alive.",
        observables(g).coh_e,
        kappa0(g)
    );

    Reading {
        verdict,
        populations,
        carrying,
        faint,
        strongest_line,
        pain,
        hierarchy_note,
    }
}
