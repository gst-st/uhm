//! The Estimator organ [K] — the gap the §7 blueprint survey exposed, closed
//! for machine-generated observation models: track a HIDDEN holon from noisy,
//! possibly partial readouts by predict–measure–update over D(ℂ⁷).
//!
//! Honesty by construction:
//!   - the hidden trajectory is ground truth the estimator never sees;
//!   - the filter gain is tuned on seed-A trajectories and EVALUATED on
//!     fresh seed-B trajectories (no same-data tuning);
//!   - two baselines run on the identical observations: dead reckoning
//!     (dynamics only) and observation-only (each snapshot alone);
//!   - stated assumptions, printed with results: the filter knows the tick
//!     parameters and ρ* (the Kalman «known dynamics» assumption), and with
//!     magnitude-only coherence readouts the PHASES come entirely from the
//!     dynamics prior — they are not observed.

use crate::holon::*;
use num_complex::Complex64 as C64;
use rand::rngs::StdRng;
use rand::{RngExt, SeedableRng};

/// The hidden truth's step: LIFE jiggles the pattern with a random dial of
/// scale σ_proc (process noise the filter cannot predict), then the tick.
pub fn truth_step(g: &CMat, rho: &CMat, sigma_proc: f64, rng: &mut StdRng) -> CMat {
    let pairs = dial_pairs();
    let (i, j) = pairs[rng.random_range(0..pairs.len())];
    let th = sigma_proc * gauss(rng);
    tick_std(&dial(g, i, j, th), rho)
}

fn gauss(rng: &mut StdRng) -> f64 {
    let u1: f64 = rng.random_range(1e-12f64..1.0);
    let u2: f64 = rng.random_range(0.0f64..1.0);
    (-2.0 * u1.ln()).sqrt() * (2.0 * std::f64::consts::PI * u2).cos()
}

/// Full-matrix noisy readout: Y = Γ + ε, ε Hermitian Gaussian per entry.
pub fn observe_full(g: &CMat, sigma: f64, rng: &mut StdRng) -> CMat {
    let mut y = g.clone();
    for i in 0..N {
        y[(i, i)] += C64::new(sigma * gauss(rng), 0.0);
        for j in (i + 1)..N {
            let e = C64::new(sigma * gauss(rng), sigma * gauss(rng));
            y[(i, j)] += e;
            y[(j, i)] = y[(i, j)].conj();
        }
    }
    y
}

/// Partial readout: the 7 populations and the MAGNITUDES of the masked
/// coherence pairs, all with additive Gaussian noise.
pub struct PartialObs {
    pub pops: [f64; 7],
    pub cohs: Vec<((usize, usize), f64)>,
}

pub fn observe_partial(g: &CMat, mask: &[(usize, usize)], sigma: f64, rng: &mut StdRng) -> PartialObs {
    let mut pops = [0.0; 7];
    for i in 0..N {
        pops[i] = (g[(i, i)].re + sigma * gauss(rng)).max(0.0);
    }
    let cohs = mask
        .iter()
        .map(|&(i, j)| ((i, j), (g[(i, j)].norm() + sigma * gauss(rng)).max(0.0)))
        .collect();
    PartialObs { pops, cohs }
}

/// One predict–update step of the full-matrix filter with blend gain k.
pub fn filter_full_step(est: &CMat, rho: &CMat, y: &CMat, k: f64) -> CMat {
    let pred = tick_std(est, rho);
    project_psd(&pred.scale(1.0 - k).add(&y.scale(k)))
}

/// One predict–update step of the partial filter: observed populations and
/// coherence magnitudes are blended in; phases and unobserved cells come
/// from the dynamics prediction; then trace-normalize and PSD-project.
pub fn filter_partial_step(est: &CMat, rho: &CMat, obs: &PartialObs, k: f64) -> CMat {
    let pred = tick_std(est, rho);
    let mut m = pred.clone();
    for i in 0..N {
        let blended = (1.0 - k) * pred[(i, i)].re + k * obs.pops[i];
        m[(i, i)] = C64::new(blended.max(0.0), 0.0);
    }
    for &((i, j), mag_obs) in &obs.cohs {
        let p = pred[(i, j)];
        let mag = (1.0 - k) * p.norm() + k * mag_obs;
        let phase = if p.norm() > 1e-12 { p / p.norm() } else { C64::new(1.0, 0.0) };
        m[(i, j)] = phase * mag;
        m[(j, i)] = m[(i, j)].conj();
    }
    let t = m.trace().re;
    project_psd(&m.scale(1.0 / t.max(1e-12)))
}

/// Mean tracking error ‖Γ̂ − Γ‖_F over the evaluation window of a hidden
/// trajectory, for: the filter, dead reckoning, observation-only.
pub struct TrackResult {
    pub filter: f64,
    pub dead_reckoning: f64,
    pub obs_only: f64,
}

pub fn track_full(seed: u64, sigma: f64, sigma_proc: f64, k: f64, steps: usize, burn: usize) -> TrackResult {
    let rho = make_selfmodel(0.42);
    let mut rng = StdRng::seed_from_u64(seed);
    let mut truth = rand_state(&mut rng, 0.35);
    let grey = CMat::grey(N);
    let mut est = grey.clone();
    let mut dead = grey.clone();
    let (mut ef, mut ed, mut eo, mut n) = (0.0, 0.0, 0.0, 0usize);
    for t in 0..steps {
        truth = truth_step(&truth, &rho, sigma_proc, &mut rng);
        let y = observe_full(&truth, sigma, &mut rng);
        est = filter_full_step(&est, &rho, &y, k);
        dead = tick_std(&dead, &rho);
        let obs_alone = project_psd(&y);
        if t >= burn {
            ef += est.sub(&truth).frob_norm();
            ed += dead.sub(&truth).frob_norm();
            eo += obs_alone.sub(&truth).frob_norm();
            n += 1;
        }
    }
    TrackResult {
        filter: ef / n as f64,
        dead_reckoning: ed / n as f64,
        obs_only: eo / n as f64,
    }
}

pub fn track_partial(
    seed: u64,
    mask: &[(usize, usize)],
    sigma: f64,
    sigma_proc: f64,
    k: f64,
    steps: usize,
    burn: usize,
) -> (f64, f64, f64, f64) {
    // returns (filter err, obs-only err, |P̂−P| mean, |Φ̂−Φ| mean)
    let rho = make_selfmodel(0.42);
    let mut rng = StdRng::seed_from_u64(seed);
    let mut truth = rand_state(&mut rng, 0.35);
    let grey = CMat::grey(N);
    let mut est = grey.clone();
    let (mut ef, mut eo, mut ep, mut ephi, mut n) = (0.0, 0.0, 0.0, 0.0, 0usize);
    for t in 0..steps {
        truth = truth_step(&truth, &rho, sigma_proc, &mut rng);
        let obs = observe_partial(&truth, mask, sigma, &mut rng);
        est = filter_partial_step(&est, &rho, &obs, k);
        // observation-only baseline: diag from obs, masked cohs real-positive,
        // unobserved cells at the grey prior (zero coherence)
        let mut raw = CMat::zeros(N);
        for i in 0..N {
            raw[(i, i)] = C64::new(obs.pops[i], 0.0);
        }
        for &((i, j), mag) in &obs.cohs {
            raw[(i, j)] = C64::new(mag, 0.0);
            raw[(j, i)] = C64::new(mag, 0.0);
        }
        let tr = raw.trace().re;
        let raw = project_psd(&raw.scale(1.0 / tr.max(1e-12)));
        if t >= burn {
            ef += est.sub(&truth).frob_norm();
            eo += raw.sub(&truth).frob_norm();
            ep += (purity(&est) - purity(&truth)).abs();
            ephi += (phi_exact(&est) - phi_exact(&truth)).abs();
            n += 1;
        }
    }
    (ef / n as f64, eo / n as f64, ep / n as f64, ephi / n as f64)
}

/// Gain tuning on seed-A trajectories: sweep k, return argmin of filter error.
pub fn tune_gain_full(sigma: f64, sigma_proc: f64) -> f64 {
    let mut best = (f64::MAX, 0.3);
    for kq in 1..=17 {
        let k = kq as f64 * 0.05;
        let mut e = 0.0;
        for s in 0..3u64 {
            e += track_full(100 + s, sigma, sigma_proc, k, 260, 60).filter;
        }
        if e < best.0 {
            best = (e, k);
        }
    }
    best.1
}

pub fn tune_gain_partial(mask: &[(usize, usize)], sigma: f64, sigma_proc: f64) -> f64 {
    let mut best = (f64::MAX, 0.3);
    for kq in 1..=17 {
        let k = kq as f64 * 0.05;
        let mut e = 0.0;
        for s in 0..3u64 {
            e += track_partial(100 + s, mask, sigma, sigma_proc, k, 260, 60).0;
        }
        if e < best.0 {
            best = (e, k);
        }
    }
    best.1
}
