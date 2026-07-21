//! The navigator organs: time-to-window, chord tuning, the solitaire oracle,
//! the phase atlas, ensembles. Mirrors the Python reference.

use crate::holon::*;
use num_complex::Complex64 as C64;
use rand::{RngExt, SeedableRng};
use rand::rngs::StdRng;

/// Ride the field to the viable window; the first `boosts` ticks are bold
/// (κ×3). Returns (ticks, early mean stress over the probe, final Γ).
pub fn time_to_window(mut g: CMat, rho: &CMat, boosts: usize, max_ticks: usize) -> (usize, f64, CMat) {
    let mut early = Vec::new();
    for t in 0..max_ticks {
        let p = purity(&g);
        if p > P_CRIT && p <= P_UPPER {
            let h = if early.is_empty() { 0.0 } else { early.iter().sum::<f64>() / early.len() as f64 };
            return (t, h, g);
        }
        let gain = if t < boosts { 3.0 } else { 1.0 };
        g = tick(&g, rho, 0.01, 0.2, gain);
        if t < 40 {
            let sp = stress_panel(&g);
            early.push(sp.iter().sum::<f64>() / 7.0);
        }
    }
    let h = if early.is_empty() { 0.0 } else { early.iter().sum::<f64>() / early.len() as f64 };
    (max_ticks, h, g)
}

/// Phase 2: inside the window, spectrum-preserving dials raise C = Φ·R.
/// Greedy over the 21 planes × ±θ; returns (Γ, dials used).
pub fn tune_chord(mut g: CMat, rho: &CMat, c_star: f64, max_dials: usize, theta: f64) -> (CMat, usize) {
    let pairs = dial_pairs();
    let mut used = 0;
    while observables(&g).c < c_star && used < max_dials {
        let mut best: Option<(f64, CMat)> = None;
        let base_c = observables(&g).c;
        for &(i, j) in &pairs {
            for sgn in [1.0, -1.0] {
                let cand = tick_std(&dial(&g, i, j, sgn * theta), rho);
                let p = purity(&cand);
                let c = observables(&cand).c;
                if c > base_c && p > P_CRIT && p <= P_UPPER + 0.02 {
                    if best.as_ref().map_or(true, |(bc, _)| c > *bc) {
                        best = Some((c, cand));
                    }
                }
            }
        }
        match best {
            Some((_, gb)) => {
                g = gb;
                used += 1;
            }
            None => break,
        }
    }
    (g, used)
}

/// The Dee solitaire: M random control decks over the horizon; the fraction
/// that reaches the window is the oracle p_golden. Returns (p, mean heat,
/// mean win time or NaN).
pub fn solitaire(g0: &CMat, rho: &CMat, deals: usize, horizon: usize, bold: bool, seed: u64) -> (f64, f64, f64) {
    let mut rng = StdRng::seed_from_u64(seed);
    let pairs = dial_pairs();
    let mut wins = 0usize;
    let mut heats = Vec::new();
    let mut times = Vec::new();
    for _ in 0..deals {
        let mut g = g0.clone();
        let mut heat = Vec::new();
        for t in 0..horizon {
            let r: f64 = rng.random();
            if r < 0.5 {
                g = tick_std(&g, rho);
            } else if r < 0.75 || !bold {
                let (i, j) = pairs[rng.random_range(0..pairs.len())];
                let th: f64 = (rng.random::<f64>() - 0.5) * 0.4;
                g = tick_std(&dial(&g, i, j, th), rho);
            } else {
                g = tick(&g, rho, 0.01, 0.2, 3.0); // the bold deck plays boosts
            }
            let sp = stress_panel(&g);
            heat.push(sp.iter().sum::<f64>() / 7.0);
            let p = purity(&g);
            if p > P_CRIT && p <= P_UPPER {
                wins += 1;
                times.push(t as f64);
                break;
            }
        }
        heats.push(heat.iter().sum::<f64>() / heat.len().max(1) as f64);
    }
    let p = wins as f64 / deals as f64;
    let h = heats.iter().sum::<f64>() / heats.len().max(1) as f64;
    let w = if times.is_empty() { f64::NAN } else { times.iter().sum::<f64>() / times.len() as f64 };
    (p, h, w)
}

/// Attractor purity under a given (g_D, κ-gain) after `ticks` steps from a
/// deterministic mixed start (Source relaxed) — rng-free, reproducible.
pub fn attractor_p(g_d: f64, kap_gain: f64, ticks: usize, rho: &CMat) -> f64 {
    let mut g = source();
    // a short scramble off the Source so κ(Coh_E)-feedback engages generically
    g = project_psd(&g.scale(0.6).add(&CMat::grey(N).scale(0.4)));
    for _ in 0..ticks {
        g = tick(&g, rho, 0.01, g_d, kap_gain);
    }
    purity(&g)
}

#[derive(Clone, Copy, PartialEq)]
pub enum Cell {
    Grey,
    Window,
    Crystal,
}

/// The phase atlas over (dissipation g_D, supply κ-gain).
pub fn phase_atlas(g_ds: &[f64], kaps: &[f64], ticks: usize, rho: &CMat) -> Vec<Vec<Cell>> {
    g_ds.iter()
        .map(|&gd| {
            kaps.iter()
                .map(|&kg| {
                    let p = attractor_p(gd, kg, ticks, rho);
                    if p <= P_CRIT {
                        Cell::Grey
                    } else if p <= P_UPPER {
                        Cell::Window
                    } else {
                        Cell::Crystal
                    }
                })
                .collect()
        })
        .collect()
}

/// An individual identity: a personal ρ*_i — the shared E/O/U emphasis plus
/// its own Gaussian orientation (the reference construction), mixed to the
/// target purity. Identities differ in DIRECTION, not only in wiring.
pub fn rand_selfmodel(rng: &mut impl RngExt, target_p: f64) -> CMat {
    let mut v = [C64::new(0.0, 0.0); N];
    v[E_] = C64::new(1.0, 0.0);
    v[O_] = C64::new(0.8, 0.0);
    v[U_] = C64::new(0.6, 0.0);
    for x in v.iter_mut() {
        let u1: f64 = rng.random_range(1e-12f64..1.0);
        let u2: f64 = rng.random_range(0.0f64..1.0);
        let r = (-2.0 * u1.ln()).sqrt();
        let th = 2.0 * std::f64::consts::PI * u2;
        *x += C64::new(0.45 * r * th.cos(), 0.45 * r * th.sin());
    }
    let nrm = v.iter().map(|x| x.norm_sqr()).sum::<f64>().sqrt();
    let mut proj = CMat::zeros(N);
    for i in 0..N {
        for j in 0..N {
            proj[(i, j)] = v[i] * v[j].conj() / (nrm * nrm);
        }
    }
    let grey = CMat::grey(N);
    let mut best = grey.clone();
    let mut bestd = f64::MAX;
    for t in 0..200 {
        let a = t as f64 / 199.0;
        let g = proj.scale(a).add(&grey.scale(1.0 - a));
        let g = g.scale(1.0 / g.trace().re);
        let d = (purity(&g) - target_p).abs();
        if d < bestd {
            bestd = d;
            best = g;
        }
    }
    best
}

/// Distance of Γ from the mixture chord {(1−s)Γ₀ + sΓ₁} (Frobenius).
pub fn chord_distance(g: &CMat, g0: &CMat, g1: &CMat) -> f64 {
    let d = g1.sub(g0);
    let x = g.sub(g0);
    let dd: f64 = d.a.iter().map(|v| v.norm_sqr()).sum();
    let dx: C64 = d.a.iter().zip(x.a.iter()).map(|(a, b)| a.conj() * b).sum();
    let coef = dx / dd;
    let proj = d.a.iter().map(|v| v * coef).collect::<Vec<_>>();
    x.a.iter()
        .zip(proj.iter())
        .map(|(a, b)| (a - b).norm_sqr())
        .sum::<f64>()
        .sqrt()
}
