//! Honest demonstration protocols. Design rules, enforced by construction:
//!   1. blind ground truth  — the damaged axis is chosen by the RNG, the
//!      diagnoser never sees it; EVERY trial is reported (confusion matrix);
//!   2. proper scoring      — the oracle's probabilities are tested against
//!      FRESH realizations (different seeds) and Brier-scored;
//!   3. baselines           — the navigator races against do-nothing and
//!      random policies on the SAME starting states;
//!   4. real input          — the checkup encodes numbers the user supplies;
//!      the encoding protocol and its status are printed with the result.
//! Nothing below curates its cases; whatever the numbers are, they print.

use crate::holon::*;
use crate::interpret::read;
use crate::model::{model, Domain};
use crate::navigate::*;
use rand::rngs::StdRng;
use rand::{RngExt, SeedableRng};

/// Crush the off-diagonal row/column of one axis by factor f, then re-project.
fn damage(g: &CMat, axis: usize, f: f64) -> CMat {
    let mut d = g.clone();
    for j in 0..N {
        if j != axis {
            d[(axis, j)] *= f;
            d[(j, axis)] *= f;
        }
    }
    project_psd(&d)
}

/// The seven line closures c_l = |γ_ij| + |γ_jk| + |γ_ik|.
fn closures(g: &CMat) -> [f64; 7] {
    let mut c = [0.0; 7];
    for (li, &[i, j, k]) in fano_lines().iter().enumerate() {
        c[li] = g[(i, j)].norm() + g[(j, k)].norm() + g[(i, k)].norm();
    }
    c
}

/// Demo 1 — blind diagnosis THROUGH THE LINES ONLY.
/// Protocol: a healthy attractor state is damaged on a secret axis (chosen by
/// the RNG). The diagnoser observes ONLY the 7 line closures (aggregate
/// observables, not individual coherences), marks lines whose closure dropped,
/// and names the axis whose 3 incident lines best match the broken set —
/// «the broken lines spell out the address». Full confusion matrix printed.
pub fn blind_diagnosis(trials: usize, seed: u64) {
    blind_diagnosis_regime(trials, seed, 0.05, 0.45, 0.0, "heavy damage (crush to 5–45%), noiseless lines");
    blind_diagnosis_regime(trials, seed + 1, 0.70, 0.95, 0.03, "mild damage (crush to 70–95%) + 3% observation noise");
}

fn blind_diagnosis_regime(trials: usize, seed: u64, f_lo: f64, f_hi: f64, noise: f64, label: &str) {
    println!("DEMO 1 — blind diagnosis through the seven lines only");
    println!("  regime: {}", label);
    println!("  protocol: RNG secretly damages one axis; the diagnoser sees only the");
    println!("  7 line closures and must name the axis. Every trial counts.\n");
    let rho = make_selfmodel(0.42);
    let mut rng = StdRng::seed_from_u64(seed);
    // one healthy baseline, honestly disclosed to the diagnoser (a prior checkup)
    let mut healthy = rand_state(&mut rng, 0.5);
    for _ in 0..800 {
        healthy = tick_std(&healthy, &rho);
    }
    let base = closures(&healthy);
    let lines = fano_lines();
    let mut confusion = [[0usize; 7]; 7];
    let mut correct = 0usize;
    for _ in 0..trials {
        let secret = rng.random_range(0..N);
        let f = f_lo + (f_hi - f_lo) * rng.random::<f64>();
        let dmg = damage(&healthy, secret, f);
        let mut now = closures(&dmg);
        for v in now.iter_mut() {
            *v *= 1.0 + noise * 2.0 * (rng.random::<f64>() - 0.5);
        }
        // relative drop per line
        let mut drop = [0.0f64; 7];
        for l in 0..7 {
            drop[l] = (base[l] - now[l]) / base[l].max(1e-12);
        }
        // score each candidate axis: mean drop over its 3 incident lines
        // minus mean drop over the 4 non-incident lines (contrast score)
        let mut best_axis = 0usize;
        let mut best_score = f64::MIN;
        for a in 0..N {
            let (mut on, mut non, mut n_on, mut n_non) = (0.0, 0.0, 0, 0);
            for (li, ln) in lines.iter().enumerate() {
                if ln.contains(&a) {
                    on += drop[li];
                    n_on += 1;
                } else {
                    non += drop[li];
                    n_non += 1;
                }
            }
            let score = on / n_on as f64 - non / n_non as f64;
            if score > best_score {
                best_score = score;
                best_axis = a;
            }
        }
        confusion[secret][best_axis] += 1;
        if best_axis == secret {
            correct += 1;
        }
    }
    println!("  accuracy: {}/{} = {:.1}%  (chance = 14.3%)", correct, trials,
             100.0 * correct as f64 / trials as f64);
    println!("  confusion matrix (rows = secret axis, cols = named axis):");
    print!("        ");
    for a in 0..N {
        print!("{:>5}", AXES[a]);
    }
    println!();
    for s in 0..N {
        print!("      {} ", AXES[s]);
        for a in 0..N {
            print!("{:>5}", confusion[s][a]);
        }
        println!();
    }
    println!();
}

/// Demo 2 — the oracle's calibration curve.
/// Protocol: for a sweep of random starting fogs and both deck styles, the
/// oracle PREDICTS p_golden from M deals (seed group A); then the prediction
/// is tested against M FRESH deals (seed group B, disjoint). Proper scoring:
/// mean |p̂ − freq| and the Brier score of p̂ against each fresh outcome.
pub fn oracle_calibration(starts: usize, deals: usize, seed: u64) {
    println!("DEMO 2 — oracle calibration: predictions vs fresh realizations");
    println!("  protocol: p̂ from {} deals (seeds A) tested on {} fresh deals (seeds B);", deals, deals);
    println!("  binomial se ≈ 0.5/√M = {:.3}. Every start printed, none selected.\n", 0.5 / (deals as f64).sqrt());
    let rho = make_selfmodel(0.42);
    let mut rng = StdRng::seed_from_u64(seed);
    let mut sum_abs = 0.0;
    let mut brier = 0.0;
    let mut n_out = 0usize;
    println!("     start P     deck    p̂ (A)   freq (B)   |diff|");
    for s in 0..starts {
        let a = 0.22 + 0.20 * rng.random::<f64>();
        let g0 = rand_state(&mut rng, a);
        for bold in [false, true] {
            let (p_hat, _, _) = solitaire(&g0, &rho, deals, 70, bold, 1000 + s as u64);
            let (freq, _, _) = solitaire(&g0, &rho, deals, 70, bold, 9000 + s as u64);
            sum_abs += (p_hat - freq).abs();
            // Brier of p_hat against the B-group outcomes: p̂² weighting via freq
            brier += p_hat * p_hat - 2.0 * p_hat * freq + freq; // E[(p̂−X)²] with X~Bern(freq)
            n_out += 1;
            println!(
                "     {:.3}     {}   {:5.1}%    {:5.1}%     {:4.1}%",
                purity(&g0),
                if bold { "bold " } else { "timid" },
                100.0 * p_hat,
                100.0 * freq,
                100.0 * (p_hat - freq).abs()
            );
        }
    }
    println!("\n  mean |p̂ − freq| = {:.1}%   mean Brier = {:.3}  (0 = perfect, 0.25 = coin)",
             100.0 * sum_abs / n_out as f64, brier / n_out as f64);
    println!();
}

/// Demo 3 — navigation benchmark against baselines, same starts for all.
/// Policies: (a) drift only; (b) random timid deck; (c) bold start (60 boosted
/// ticks); (d) adaptive (boost while P < 2/7, then drift). Budget 400 ticks.
pub fn navigate_bench(starts: usize, seed: u64) {
    println!("DEMO 3 — navigation benchmark: 4 policies, the SAME {} random fogs", starts);
    println!("  success = reaching the window within 400 ticks; ± is one std.\n");
    let rho = make_selfmodel(0.42);
    let mut rng = StdRng::seed_from_u64(seed);
    let starts_g: Vec<CMat> = (0..starts).map(|_| rand_state(&mut rng, 0.30)).collect();
    let run = |name: &str, policy: usize, starts_g: &[CMat]| {
        let mut times = Vec::new();
        let mut ok = 0usize;
        for (si, g0) in starts_g.iter().enumerate() {
            let t = match policy {
                0 => time_to_window(g0.clone(), &rho, 0, 400).0,
                1 => {
                    // random timid deck, one realization per start
                    let mut g = g0.clone();
                    let mut rr = StdRng::seed_from_u64(777 + si as u64);
                    let pairs = dial_pairs();
                    let mut t = 400usize;
                    for step in 0..400 {
                        if rr.random::<f64>() < 0.5 {
                            g = tick_std(&g, &rho);
                        } else {
                            let (i, j) = pairs[rr.random_range(0..pairs.len())];
                            let th: f64 = (rr.random::<f64>() - 0.5) * 0.4;
                            g = tick_std(&dial(&g, i, j, th), &rho);
                        }
                        let p = purity(&g);
                        if p > P_CRIT && p <= P_UPPER {
                            t = step;
                            break;
                        }
                    }
                    t
                }
                2 => time_to_window(g0.clone(), &rho, 60, 400).0,
                _ => {
                    // adaptive: boost below the wall, drift inside
                    let mut g = g0.clone();
                    let mut t = 400usize;
                    for step in 0..400 {
                        let p = purity(&g);
                        if p > P_CRIT && p <= P_UPPER {
                            t = step;
                            break;
                        }
                        let gain = if p <= P_CRIT { 3.0 } else { 1.0 };
                        g = tick(&g, &rho, 0.01, 0.2, gain);
                    }
                    t
                }
            };
            if t < 400 {
                ok += 1;
                times.push(t as f64);
            }
        }
        let mean = times.iter().sum::<f64>() / times.len().max(1) as f64;
        let sd = (times.iter().map(|x| (x - mean).powi(2)).sum::<f64>()
            / times.len().max(1) as f64)
            .sqrt();
        println!(
            "    {:22} success {:3}/{}   time-to-window {:6.1} ± {:.1} ticks",
            name, ok, starts_g.len(), mean, sd
        );
    };
    run("drift only", 0, &starts_g);
    run("random timid deck", 1, &starts_g);
    run("bold start (60 ticks)", 2, &starts_g);
    run("adaptive (boost<2/7)", 3, &starts_g);
    println!();
}

/// Demo 5 — the maxim, decomposed and measured.
/// «У человека должна быть цель; если у него нет своей цели, он станет
/// частью чужой цели.» The reduction of meanings, printed for honesty:
///   цель        = the regeneration target ρ* (what κ pulls toward);
///   своя цель   = the share φ_own of one's κ-budget aimed at one's OWN ρ*_B;
///   чужая цель  = the social pull toward another holon's pattern Γ_A;
///   стать частью = the chord's deviation aligning with the OTHER's ideal.
/// Fairness: the total κ-budget is IDENTICAL in every condition; only its
/// allocation differs. The whole φ_own curve prints — no selected points.
pub fn maxim(seed: u64) {
    println!("DEMO 5 — the maxim: «no own goal → part of another's goal»");
    println!("  reduction: goal=ρ*, own-goal share=φ_own, other's goal=social pull");
    println!("  toward Γ_A, capture=cosine of B's deviation with ρ*_A vs ρ*_B.");
    println!("  Total κ-budget identical across conditions; full curve printed.\n");
    let mut rng = StdRng::seed_from_u64(seed);
    let rho_a = rand_selfmodel(&mut rng, 0.42);
    let rho_b = rand_selfmodel(&mut rng, 0.42);
    let dev = |g: &CMat| g.sub(&CMat::grey(N));
    let cosine = |x: &CMat, y: &CMat| {
        let num: f64 = x.a.iter().zip(y.a.iter()).map(|(a, b)| (a.conj() * b).re).sum();
        num / (x.frob_norm() * y.frob_norm()).max(1e-15)
    };
    println!("     φ_own   own-overlap   capture-overlap   P_B     verdict");
    for &phi in &[1.0f64, 0.75, 0.5, 0.25, 0.0] {
        let mut ga = rand_state(&mut StdRng::seed_from_u64(seed + 10), 0.35);
        let mut gb = rand_state(&mut StdRng::seed_from_u64(seed + 11), 0.35);
        for _ in 0..1200 {
            ga = tick_std(&ga, &rho_a);
            let rho_eff = rho_b.scale(phi).add(&ga.scale(1.0 - phi));
            let rho_eff = rho_eff.scale(1.0 / rho_eff.trace().re);
            gb = tick_std(&gb, &rho_eff);
        }
        let own = cosine(&dev(&gb), &dev(&rho_b));
        let cap = cosine(&dev(&gb), &dev(&rho_a));
        let pb = purity(&gb);
        let verdict = if own > cap { "своя цель держит аккорд" } else { "захвачен чужой целью" };
        println!("     {:4.2}      {:+.3}          {:+.3}        {:.3}   {}", phi, own, cap, pb, verdict);
    }
    // the no-goal-at-all limit: κ = 0 entirely
    let mut g0 = rand_state(&mut StdRng::seed_from_u64(seed + 11), 0.35);
    let rho_dummy = CMat::grey(N);
    for _ in 0..1200 {
        g0 = tick(&g0, &rho_dummy, 0.01, 0.2, 0.0);
    }
    println!("     none      —               —             {:.3}   без всякой цели — серое растворение (H23)", purity(&g0));
    println!("\n  status of the mapping: [О/И] (a documented reduction); the dynamics");
    println!("  and every number above: measured. Interpretation per the grammar is");
    println!("  printed by the machine, not narrated afterward.\n");
}

/// Demo 4 — the checkup: encode the USER'S OWN numbers, read the state.
/// scores: seven 0..10 self-ratings (A,S,D,L,E,O,U); pairs: optional named
/// coherences as fractions −1..1 of the PSD bound √(γii γjj).
pub fn checkup(scores: [f64; 7], pairs: &[(usize, usize, f64)], domain: Domain) {
    println!("DEMO 4 — checkup on user-supplied numbers");
    println!("  encoding protocol (printed for honesty): populations = scores/Σ;");
    println!("  coherence(i,j) = c·√(γii·γjj), |c| ≤ 0.9; then the PSD projection.");
    println!("  Status: the self-report Enc is a documented protocol [О/И] — the");
    println!("  reading is falsifiable by retest, not an oracle pronouncement.\n");
    let total: f64 = scores.iter().sum();
    let mut g = CMat::zeros(N);
    for i in 0..N {
        g[(i, i)] = num_complex::Complex64::new(scores[i] / total, 0.0);
    }
    for &(i, j, c) in pairs {
        let bound = (g[(i, i)].re * g[(j, j)].re).sqrt();
        let v = c.clamp(-0.9, 0.9) * bound;
        g[(i, j)] = num_complex::Complex64::new(v, 0.0);
        g[(j, i)] = num_complex::Complex64::new(v, 0.0);
    }
    let g = project_psd(&g);
    let mdl = model(domain);
    let r = read(&g, &mdl);
    let ob = observables(&g);
    println!("  model: {}", mdl.name);
    println!("  {}", r.verdict);
    println!("  P={:.3} R={:.3} Φ={:.3} C={:.3} D_diff={:.2}", ob.p, ob.r, ob.phi, ob.c, ob.d_diff);
    println!("\n  populations (who is loud):");
    for p in &r.populations {
        println!("    {}", p);
    }
    println!("\n  carrying coherences:");
    for c in &r.carrying {
        println!("    {}", c);
    }
    println!("\n  {}", r.strongest_line);
    println!("  {}", r.pain);
    println!();
}

/// Parse `--scores 7,5,4,6,3,2,5` and `--coh AE=0.4,OU=-0.2`.
pub fn run_checkup_cli(args: &[String]) -> Result<(), String> {
    let mut scores = [5.0f64; 7];
    let mut pairs: Vec<(usize, usize, f64)> = Vec::new();
    let mut domain = Domain::Mind;
    let idx_of = |c: char| AXES.iter().position(|&a| a == c);
    let mut i = 0;
    while i < args.len() {
        match args[i].as_str() {
            "--scores" => {
                i += 1;
                let parts: Vec<&str> = args.get(i).ok_or("--scores needs a value")?.split(',').collect();
                if parts.len() != 7 {
                    return Err("--scores needs 7 comma-separated numbers (A,S,D,L,E,O,U)".into());
                }
                for (k, p) in parts.iter().enumerate() {
                    scores[k] = p.trim().parse::<f64>().map_err(|e| e.to_string())?;
                    if scores[k] < 0.0 {
                        return Err("scores must be ≥ 0".into());
                    }
                }
            }
            "--coh" => {
                i += 1;
                for item in args.get(i).ok_or("--coh needs a value")?.split(',') {
                    let (name, val) = item.split_once('=').ok_or("coh format: AE=0.4")?;
                    let mut ch = name.trim().chars();
                    let a = idx_of(ch.next().ok_or("bad pair")?).ok_or("unknown axis")?;
                    let b = idx_of(ch.next().ok_or("bad pair")?).ok_or("unknown axis")?;
                    pairs.push((a, b, val.trim().parse::<f64>().map_err(|e| e.to_string())?));
                }
            }
            "--model" => {
                i += 1;
                domain = match args.get(i).map(|s| s.as_str()) {
                    Some("universal") => Domain::Universal,
                    Some("mind") => Domain::Mind,
                    Some("team") => Domain::Team,
                    Some("llm") => Domain::LlmAgent,
                    Some("market") => Domain::Market,
                    other => return Err(format!("unknown model {:?}", other)),
                };
            }
            other => return Err(format!("unknown flag {}", other)),
        }
        i += 1;
    }
    checkup(scores, &pairs, domain);
    Ok(())
}
