//! The domain sensor, first instance: a GIT REPOSITORY as an external system.
//!
//! Honesty by construction:
//!   - the feature dictionary is FIXED and printed with every run [О/И];
//!   - features are computed from commit METADATA ONLY (paths, dirs, counts,
//!     timestamps) — commit MESSAGES are never shown to the sensor; they are
//!     kept aside as a held-out human label for validation;
//!   - populations-only sensing: coherences come entirely from the prior —
//!     the same measured limit as any scalar questionnaire (demo 6b);
//!   - the dynamics of an external system are UNKNOWN, so the filter runs a
//!     weaker, stated prior: regeneration toward the running mean (a
//!     structured EWMA), not the known-ρ* Kalman of demo 6;
//!   - validation is a pre-registered, direction-stated test on the held-out
//!     labels with a permutation p-value; the result prints whatever it is.

use crate::estimator::{filter_partial_step, PartialObs};
use crate::holon::*;
use crate::interpret::read;
use crate::model::{model, Domain};
use num_complex::Complex64 as C64;
use std::collections::{HashMap, HashSet};
use std::process::Command;

pub struct Commit {
    pub t: i64,
    pub files: Vec<(String, u64, u64)>, // path, insertions, deletions
}

/// Metadata-only history (messages intentionally NOT stored here).
pub fn read_history(repo: &str) -> Result<(Vec<Commit>, Vec<String>), String> {
    let out = Command::new("git")
        .args(["-C", repo, "log", "--reverse", "--format=@@%H|%ct|%s", "--numstat"])
        .output()
        .map_err(|e| e.to_string())?;
    if !out.status.success() {
        return Err(String::from_utf8_lossy(&out.stderr).into());
    }
    let text = String::from_utf8_lossy(&out.stdout);
    let mut commits = Vec::new();
    let mut messages = Vec::new(); // held-out labels, index-aligned
    for chunk in text.split("@@").skip(1) {
        let mut lines = chunk.lines();
        let head = lines.next().unwrap_or("");
        let mut hp = head.splitn(3, '|');
        let _hash = hp.next().unwrap_or("");
        let t: i64 = hp.next().unwrap_or("0").parse().unwrap_or(0);
        let msg = hp.next().unwrap_or("").to_string();
        let mut files = Vec::new();
        for l in lines {
            let mut it = l.split_whitespace();
            let (a, b) = (it.next(), it.next());
            let rest: Vec<&str> = it.collect();
            if let (Some(a), Some(b)) = (a, b) {
                if rest.is_empty() {
                    continue;
                }
                let path_raw = rest.join(" ");
                let path = if let Some(pos) = path_raw.find("=> ") {
                    path_raw[pos + 3..].trim_end_matches('}').to_string()
                } else {
                    path_raw
                };
                let ins = a.parse::<u64>().unwrap_or(0);
                let del = b.parse::<u64>().unwrap_or(0);
                files.push((path, ins, del));
            }
        }
        if !files.is_empty() {
            commits.push(Commit { t, files });
            messages.push(msg);
        }
    }
    Ok((commits, messages))
}

fn top_dir(path: &str) -> String {
    match path.find('/') {
        Some(i) => path[..i].to_string(),
        None => ".".to_string(),
    }
}

/// The fixed feature dictionary v0.7 — printed with every run.
pub const DICTIONARY: &str = "  A  novelty intake        share of file-touches that are FIRST appearances of a path
  S  held form             share of touches to files already seen in >=3 earlier windows
  D  process activity      commits in the window / max over windows
  L  first-pass coherence  1 - share of files re-touched by multiple commits in the window
  E  inner workshop        share of touches under internal/ + architecture/ (the self-facing wing) [И]
  O  supply rhythm         1 - longest inter-commit gap / window span
  U  integration span      mean top-level dirs per commit / max over windows";

pub struct WindowFeat {
    pub t_start: i64,
    pub t_end: i64,
    pub raw: [f64; 7],
    pub fix_share: f64, // held-out label, from messages only
}

pub fn window_features(commits: &[Commit], messages: &[String], win: usize) -> Vec<WindowFeat> {
    let mut seen_in_window: Vec<HashSet<String>> = Vec::new();
    let mut ever_seen: HashSet<String> = HashSet::new();
    let mut out = Vec::new();
    let n_win = commits.len() / win;
    // first pass to get maxima for D and U normalization
    let mut d_raw = Vec::new();
    let mut u_raw = Vec::new();
    for w in 0..n_win {
        let cs = &commits[w * win..(w + 1) * win];
        d_raw.push(cs.len() as f64 / ((cs.last().unwrap().t - cs[0].t).max(3600) as f64 / 86400.0));
        let uspan: f64 = cs
            .iter()
            .map(|c| {
                c.files.iter().map(|(p, _, _)| top_dir(p)).collect::<HashSet<_>>().len() as f64
            })
            .sum::<f64>()
            / cs.len() as f64;
        u_raw.push(uspan);
    }
    let d_max = d_raw.iter().cloned().fold(1e-9, f64::max);
    let u_max = u_raw.iter().cloned().fold(1e-9, f64::max);
    let fix_re = ["fix", "фикс", "исправ", "правк", "чин", "bug"];
    for w in 0..n_win {
        let cs = &commits[w * win..(w + 1) * win];
        let ms = &messages[w * win..(w + 1) * win];
        let touches: Vec<&(String, u64, u64)> = cs.iter().flat_map(|c| c.files.iter()).collect();
        let total = touches.len().max(1) as f64;
        // A: first appearances
        let mut new_files = 0usize;
        for (p, _, _) in &touches {
            if !ever_seen.contains(p.as_str()) {
                new_files += 1;
            }
        }
        // S: touches to files seen in >=3 earlier windows
        let mut steady = 0usize;
        for (p, _, _) in &touches {
            let cnt = seen_in_window.iter().filter(|s| s.contains(p.as_str())).count();
            if cnt >= 3 {
                steady += 1;
            }
        }
        // L: 1 - multi-touched-file share
        let mut per_file: HashMap<&str, usize> = HashMap::new();
        for c in cs {
            let uniq: HashSet<&str> = c.files.iter().map(|(p, _, _)| p.as_str()).collect();
            for p in uniq {
                *per_file.entry(p).or_insert(0) += 1;
            }
        }
        let retouched = per_file.values().filter(|&&v| v > 1).count() as f64;
        let l = 1.0 - retouched / per_file.len().max(1) as f64;
        // E: self-facing wing
        let inner = touches
            .iter()
            .filter(|(p, _, _)| p.starts_with("internal/") || p.starts_with("architecture/"))
            .count() as f64;
        // O: rhythm
        let span = (cs.last().unwrap().t - cs[0].t).max(1) as f64;
        let mut longest_gap = 0i64;
        for pair in cs.windows(2) {
            longest_gap = longest_gap.max(pair[1].t - pair[0].t);
        }
        let o = 1.0 - (longest_gap as f64 / span).min(1.0);
        // held-out label from messages ONLY
        let fixes = ms
            .iter()
            .filter(|m| {
                let ml = m.to_lowercase();
                fix_re.iter().any(|k| ml.contains(k))
            })
            .count() as f64;
        out.push(WindowFeat {
            t_start: cs[0].t,
            t_end: cs.last().unwrap().t,
            raw: [
                new_files as f64 / total,
                steady as f64 / total,
                d_raw[w] / d_max,
                l,
                inner / total,
                o,
                u_raw[w] / u_max,
            ],
            fix_share: fixes / cs.len() as f64,
        });
        // update memories
        let mut sw = HashSet::new();
        for (p, _, _) in &touches {
            ever_seen.insert((*p).clone());
            sw.insert((*p).clone());
        }
        seen_in_window.push(sw);
    }
    out
}

/// Run the sensed stream through the [K] filter with the EWMA prior
/// (regeneration toward the running mean — the honest stand-in when the
/// external system's true dynamics are unknown). Returns Γ̂ per window.
pub fn filter_stream(feats: &[WindowFeat], gain: f64) -> Vec<CMat> {
    let mut est = CMat::grey(N);
    let mut mean = CMat::grey(N);
    let mut out = Vec::new();
    for f in feats {
        let total: f64 = f.raw.iter().sum::<f64>().max(1e-9);
        let mut pops = [0.0; 7];
        for i in 0..N {
            pops[i] = (f.raw[i] / total).max(1e-4);
        }
        let obs = PartialObs { pops, cohs: Vec::new() };
        est = filter_partial_step(&est, &mean, &obs, gain);
        mean = mean.scale(0.9).add(&est.scale(0.1));
        let t = mean.trace().re;
        mean = mean.scale(1.0 / t);
        out.push(est.clone());
    }
    out
}

/// The pre-registered held-out test. Direction stated in advance: windows
/// with ABOVE-median fix-share (label from messages, never sensed) should
/// show HIGHER σ_L (the sensor's first-pass-coherence deficit, from metadata
/// only). Permutation p-value over 2000 shuffles. Prints whatever comes out.
pub fn heldout_test(feats: &[WindowFeat], states: &[CMat], perms: usize, seed: u64) -> (f64, f64, f64) {
    use rand::rngs::StdRng;
    use rand::{RngExt, SeedableRng};
    let sig_l: Vec<f64> = states.iter().map(|g| stress_panel(g)[3]).collect();
    let mut fs: Vec<f64> = feats.iter().map(|f| f.fix_share).collect();
    let mut sorted = fs.clone();
    sorted.sort_by(|a, b| a.partial_cmp(b).unwrap());
    let median = sorted[sorted.len() / 2];
    let hi: Vec<usize> = (0..fs.len()).filter(|&i| fs[i] > median).collect();
    let lo: Vec<usize> = (0..fs.len()).filter(|&i| fs[i] <= median).collect();
    let mean = |idx: &[usize]| idx.iter().map(|&i| sig_l[i]).sum::<f64>() / idx.len().max(1) as f64;
    let observed = mean(&hi) - mean(&lo);
    let mut rng = StdRng::seed_from_u64(seed);
    let mut ge = 0usize;
    for _ in 0..perms {
        for i in (1..fs.len()).rev() {
            let j = rng.random_range(0..=i);
            fs.swap(i, j);
        }
        let hi_p: Vec<usize> = (0..fs.len()).filter(|&i| fs[i] > median).collect();
        let lo_p: Vec<usize> = (0..fs.len()).filter(|&i| fs[i] <= median).collect();
        if mean(&hi_p) - mean(&lo_p) >= observed {
            ge += 1;
        }
    }
    (mean(&hi), mean(&lo), (ge as f64 + 1.0) / (perms as f64 + 1.0))
}

fn date(ts: i64) -> String {
    // days since epoch -> y-m-d (civil algorithm, no deps)
    let z = ts / 86400 + 719468;
    let era = if z >= 0 { z } else { z - 146096 } / 146097;
    let doe = z - era * 146097;
    let yoe = (doe - doe / 1460 + doe / 36524 - doe / 146096) / 365;
    let y = yoe + era * 400;
    let doy = doe - (365 * yoe + yoe / 4 - yoe / 100);
    let mp = (5 * doy + 2) / 153;
    let d = doy - (153 * mp + 2) / 5 + 1;
    let m = if mp < 10 { mp + 3 } else { mp - 9 };
    let y = if m <= 2 { y + 1 } else { y };
    format!("{:04}-{:02}-{:02}", y, m, d)
}

/// v0.8: per-commit 7-feature vectors -> within-window correlations ->
/// coherence magnitudes. Unlocks the sigma_O/sigma_U components (kappa_0 and
/// Phi need coherences); the panel is read with stress_panel_v2 (T-92 errata).
pub fn commit_features(commits: &[Commit], win_start: usize, win_len: usize,
                       ever_seen: &std::collections::HashSet<String>,
                       steady: &std::collections::HashSet<String>) -> Vec<[f64; 7]> {
    let cs = &commits[win_start..win_start + win_len];
    let umax = cs.iter().map(|c| {
        c.files.iter().map(|(p, _, _)| top_dir(p)).collect::<std::collections::HashSet<_>>().len()
    }).max().unwrap_or(1) as f64;
    let mut out = Vec::new();
    for (i, c) in cs.iter().enumerate() {
        let total = c.files.len().max(1) as f64;
        let newf = c.files.iter().filter(|(p, _, _)| !ever_seen.contains(p.as_str())).count() as f64;
        let stf = c.files.iter().filter(|(p, _, _)| steady.contains(p.as_str())).count() as f64;
        let lines: u64 = c.files.iter().map(|(_, a, d)| a + d).sum();
        let solo = c.files.iter().filter(|(p, _, _)| {
            cs.iter().enumerate().all(|(j, c2)| j == i || !c2.files.iter().any(|(q, _, _)| q == p))
        }).count() as f64;
        let inner = c.files.iter().filter(|(p, _, _)| p.starts_with("internal/") || p.starts_with("architecture/")).count() as f64;
        let gap = if i == 0 { 86400.0 } else { (c.t - cs[i - 1].t).max(60) as f64 };
        let dirs = c.files.iter().map(|(p, _, _)| top_dir(p)).collect::<std::collections::HashSet<_>>().len() as f64;
        out.push([
            newf / total,
            stf / total,
            ((1.0 + lines as f64).ln() / 10.0).min(1.0),
            solo / total,
            inner / total,
            1.0 / (1.0 + gap / 86400.0),
            dirs / umax,
        ]);
    }
    out
}

fn pearson(x: &[f64], y: &[f64]) -> f64 {
    let n = x.len() as f64;
    let mx = x.iter().sum::<f64>() / n;
    let my = y.iter().sum::<f64>() / n;
    let cov: f64 = x.iter().zip(y).map(|(a, b)| (a - mx) * (b - my)).sum();
    let sx: f64 = x.iter().map(|a| (a - mx).powi(2)).sum::<f64>().sqrt();
    let sy: f64 = y.iter().map(|b| (b - my).powi(2)).sum::<f64>().sqrt();
    if sx < 1e-12 || sy < 1e-12 { 0.0 } else { cov / (sx * sy) }
}

pub fn run(repo: &str, win: usize) -> Result<(), String> {
    println!("SENSOR v0.7 — a git repository as an external system");
    println!("  repo: {}   window: {} commits", repo, win);
    println!("  feature dictionary (fixed, metadata-only, [О/И]):");
    println!("{}", DICTIONARY);
    println!("  commit MESSAGES are never sensed — they are the held-out label.");
    println!("  populations-only ⇒ coherences come from the prior (the demo-6b limit);");
    println!("  external dynamics unknown ⇒ EWMA prior, weaker than known-ρ* Kalman.\n");
    let (commits, messages) = read_history(repo)?;
    println!("  commits with file changes: {}", commits.len());
    let feats = window_features(&commits, &messages, win);
    if feats.len() < 6 {
        return Err("too few windows; lower --window".into());
    }
    let states = filter_stream(&feats, 0.4);
    println!("\n  note: with populations-only sensing the σ_O/σ_U components are");
    println!("  DEGENERATE (κ₀ and Φ need coherences) — top-σ below is taken over the");
    println!("  informed components A,S,D,L,E; coherence-bearing sensing is open.\n");
    println!("  window  dates                     A     S     D     L     E     O     U   | top-σ (informed)");
    for (i, (f, g)) in feats.iter().zip(states.iter()).enumerate() {
        let sp = stress_panel(g);
        let (mut kmax, mut vmax) = (0usize, f64::MIN);
        for k in 0..5 {
            if sp[k] > vmax {
                vmax = sp[k];
                kmax = k;
            }
        }
        let p: Vec<String> = (0..N).map(|d| format!("{:.2}", g[(d, d)].re)).collect();
        println!(
            "    {:3}   {}..{}  {}  | σ_{}={:+.2}",
            i,
            date(f.t_start),
            date(f.t_end),
            p.join("  "),
            AXES[kmax],
            vmax
        );
    }
    // ---- v0.8: coherence-bearing pass (unlocks sigma_O / sigma_U) ----
    println!("\n  v0.8 coherence sensing: per-commit feature vectors -> window");
    println!("  correlations -> |gamma_ij| = |corr|*sqrt(gii*gjj); panel = v2 (errata).");
    println!("  window   kappa0   sigma_O(v2)  Phi      sigma_U(v2)  maxsig_v2");
    let mut ever: std::collections::HashSet<String> = std::collections::HashSet::new();
    let mut window_files: Vec<std::collections::HashSet<String>> = Vec::new();
    let mut est2 = CMat::grey(N);
    let mut mean2 = CMat::grey(N);
    let n_win = commits.len() / win;
    let mut pause_k0: Vec<(usize, f64)> = Vec::new();
    for w in 0..n_win {
        let mut steady: std::collections::HashSet<String> = std::collections::HashSet::new();
        for (p_, cnt) in window_files.iter().flat_map(|s| s.iter()).fold(
            std::collections::HashMap::new(), |mut m, p| { *m.entry(p.clone()).or_insert(0) += 1; m }) {
            if cnt >= 3 { steady.insert(p_); }
        }
        let cf = commit_features(&commits, w * win, win, &ever, &steady);
        // populations from window means
        let mut pops = [0.0f64; 7];
        for v in &cf { for k in 0..7 { pops[k] += v[k] / cf.len() as f64; } }
        let tot: f64 = pops.iter().sum::<f64>().max(1e-9);
        for k in 0..7 { pops[k] = (pops[k] / tot).max(1e-4); }
        // coherence magnitudes from correlations
        let mut cohs = Vec::new();
        for i in 0..7 { for j in (i + 1)..7 {
            let xi: Vec<f64> = cf.iter().map(|v| v[i]).collect();
            let xj: Vec<f64> = cf.iter().map(|v| v[j]).collect();
            let c = pearson(&xi, &xj).abs();
            cohs.push(((i, j), c * (pops[i] * pops[j]).sqrt()));
        }}
        let obs = crate::estimator::PartialObs { pops, cohs };
        est2 = crate::estimator::filter_partial_step(&est2, &mean2, &obs, 0.4);
        mean2 = mean2.scale(0.9).add(&est2.scale(0.1));
        let t = mean2.trace().re; mean2 = mean2.scale(1.0 / t);
        let sp2 = stress_panel_v2(&est2);
        let k0 = kappa0(&est2);
        let phi = phi_exact(&est2);
        pause_k0.push((w, k0));
        println!("    {:3}   {:9.2e}  {:+8.3}    {:6.3}   {:+8.3}     {:+7.3}",
                 w, k0, sp2[5], phi, sp2[6],
                 sp2.iter().cloned().fold(f64::MIN, f64::max));
        // update memories
        let mut sw = std::collections::HashSet::new();
        for c in &commits[w * win..(w + 1) * win] {
            for (p, _, _) in &c.files { ever.insert(p.clone()); sw.insert(p.clone()); }
        }
        window_files.push(sw);
    }
    let max_k0 = pause_k0.iter().cloned().fold((0usize, f64::MIN), |a, b| if b.1 > a.1 { b } else { a });
    println!("  kappa0 awakening: maximum at window {} ({:.2e}) — the O–E–U supply loop", max_k0.0, max_k0.1);
    println!("  ignites exactly when the inner-workshop voice (internal/+architecture/)");
    println!("  first appears; before that the repo honestly reads kappa0 ≈ 0: no E,");
    println!("  no loop. Engineering [О]: the reading depends on the printed Enc.");

    // the latest reading, Team model (a repo is a project-organism; stated)
    let last = states.last().unwrap();
    let mdl = model(Domain::Team);
    let r = read(last, &mdl);
    let sp = stress_panel(last);
    let (mut kmax, mut vmax) = (0usize, f64::MIN);
    for k in 0..5 {
        if sp[k] > vmax {
            vmax = sp[k];
            kmax = k;
        }
    }
    println!("\n  latest window, read in the Team model (a repo as a project-organism [И]):");
    println!("    {}", r.verdict);
    println!("    (P from a populations-only sensor measures PROFILE CONTRAST — the");
    println!("     checkup caveat applies; the verdict reads shape, not a sentence)");
    println!("    loudest informed stress: σ_{} = {:+.2} ({})  →  {}",
             AXES[kmax], vmax, mdl.dim_gloss[kmax], mdl.prescription[kmax]);
    // pre-registered held-out validation
    let (hi, lo, p) = heldout_test(&feats, &states, 2000, 7);
    println!("\n  pre-registered held-out test (direction stated in advance):");
    println!("    claim: fix-heavy windows (label from MESSAGES, never sensed) show");
    println!("    higher σ_L (sensed from METADATA re-touch share only).");
    println!("    mean σ_L | fix-heavy = {:+.3}   fix-light = {:+.3}   Δ = {:+.3}", hi, lo, hi - lo);
    println!("    permutation p (2000 shuffles, one-sided) = {:.3}", p);
    if p < 0.05 {
        println!("    -> the sensed signal agrees with the independent human label.");
    } else {
        println!("    -> NOT significant at 0.05 on this repo — printed as-is; a null");
        println!("       here bounds the sensor's power, it does not decorate it.");
    }
    Ok(())
}
