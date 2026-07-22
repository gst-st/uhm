//! Categorical calibration in Rust: the hypothesis battery, re-runnable.
//! A subset of the Python table chosen to cross-verify the Rust core against
//! the reference machine (same constants, same laws, same numbers).

use crate::holon::*;
use crate::navigate::*;
use crate::pair::*;
use num_complex::Complex64 as C64;
use rand::SeedableRng;
use rand::rngs::StdRng;

pub struct Hypo {
    pub id: &'static str,
    pub claim: &'static str,
    pub pass: Option<bool>, // None = untestable here
    pub evidence: String,
}

pub fn run_calibration() -> Vec<Hypo> {
    let mut out: Vec<Hypo> = Vec::new();
    let mut add = |id: &'static str, pass: Option<bool>, claim: &'static str, ev: String| {
        out.push(Hypo { id, claim, pass, evidence: ev });
    };
    let rho = make_selfmodel(0.42);

    // ------------- arithmetic floor -------------
    let qr: Vec<usize> = {
        let mut v: Vec<usize> = (1..7).map(|k| (k * k) % 7).collect();
        v.sort();
        v.dedup();
        v
    };
    add("R01", Some(qr == vec![1, 2, 4]), "QR(7) = {1,2,4}", format!("{:?}", qr));
    let lines = fano_lines();
    let corpus_named: [[usize; 3]; 7] = {
        // {A,S,L},{A,D,O},{A,E,U},{S,D,E},{S,U,O},{D,L,U},{L,E,O} in storage idx
        let mut ls = [[0usize; 3]; 7];
        let name = |c: char| AXES.iter().position(|&a| a == c).unwrap();
        for (r, tri) in [
            ['A', 'S', 'L'], ['A', 'D', 'O'], ['A', 'E', 'U'], ['S', 'D', 'E'],
            ['S', 'U', 'O'], ['D', 'L', 'U'], ['L', 'E', 'O'],
        ]
        .iter()
        .enumerate()
        {
            let mut t: Vec<usize> = tri.iter().map(|&c| name(c)).collect();
            t.sort();
            ls[r] = [t[0], t[1], t[2]];
        }
        ls
    };
    let mut a = lines.to_vec();
    let mut b = corpus_named.to_vec();
    a.sort();
    b.sort();
    add("R02", Some(a == b), "QR translates = the seven corpus named lines", "7/7".into());
    let pair_ok = (0..7).all(|x| {
        (x + 1..7).all(|y| lines.iter().filter(|l| l.contains(&x) && l.contains(&y)).count() == 1)
    });
    add("R03", Some(pair_ok), "every pair of axes lies on exactly one line", "21/21".into());
    let dec = (1..=7u8).all(|ax| syndrome_decode(1u8 << (7 - ax)) == ax);
    add("R04", Some(dec), "Hamming syndrome self-addresses every single fault", "7/7".into());
    let thru_o: Vec<Vec<usize>> = lines
        .iter()
        .filter(|l| l.contains(&O_))
        .map(|l| {
            let mut p: Vec<usize> = l.iter().cloned().filter(|&x| x != O_).collect();
            p.sort();
            p
        })
        .collect();
    let mut to = thru_o.clone();
    to.sort();
    add(
        "R05",
        Some(to == vec![vec![0, 2], vec![1, 6], vec![3, 4]]),
        "lines through O pair the rest as (A,D),(S,U),(L,E)",
        format!("{:?}", to),
    );

    // ------------- dynamics floor -------------
    let mut rng = StdRng::seed_from_u64(42);
    let g0 = rand_state(&mut rng, 0.7);
    let (p0, s0) = (purity(&g0), entropy(&g0));
    let g1 = unitary_half(&g0, 0.02);
    add(
        "R06",
        Some((purity(&g1) - p0).abs() < 1e-12 && (entropy(&g1) - s0).abs() < 1e-9),
        "the unitary half preserves P and S exactly",
        format!("dP={:+.1e}", purity(&g1) - p0),
    );
    let g2 = unitary_half(&g1, -0.02);
    add("R07", Some(g2.max_abs_diff(&g0) < 1e-12), "the unitary half is reversible",
        format!("|dG|={:.1e}", g2.max_abs_diff(&g0)));
    let mut gd = rand_state(&mut rng, 0.8);
    for _ in 0..4000 {
        let grey = CMat::grey(N);
        gd = project_psd(&gd.add(&grey.sub(&gd).scale(0.01 * 0.3)));
    }
    add(
        "R08",
        Some((purity(&gd) - 1.0 / 7.0).abs() < 1e-3 && (entropy(&gd) - (7f64).ln()).abs() < 1e-3),
        "the dissipator alone ends at the grey wall I/7, S = ln 7",
        format!("P={:.4}, S={:.4}", purity(&gd), entropy(&gd)),
    );
    let mut ok_attr = true;
    let mut last_p = 0.0;
    for s in 0..3u64 {
        let mut rr = StdRng::seed_from_u64(100 + s);
        let mut g = rand_state(&mut rr, 0.4 + 0.15 * s as f64);
        for _ in 0..1500 {
            g = tick_std(&g, &rho);
        }
        last_p = purity(&g);
        ok_attr &= last_p > P_CRIT && last_p <= P_UPPER;
    }
    add("R09", Some(ok_attr), "random starts relax into the viable window (T-124)",
        format!("3/3 starts, P*={:.3}", last_p));
    let src = source();
    let mut comm = 0.0f64;
    for i in 0..N {
        for j in 0..N {
            comm += ((H_EFF[i] - H_EFF[j]) * src[(i, j)].norm()).powi(2);
        }
    }
    add("R10", Some(comm.sqrt() > 0.1), "the Source is unstable: [H, Γ_src] ≠ 0 (B1)",
        format!("‖[H,Γ]‖={:.3}", comm.sqrt()));
    let mut gk = rand_state(&mut rng, 0.7);
    for _ in 0..1500 {
        gk = tick(&gk, &rho, 0.01, 0.2, 0.0); // starvation
    }
    let halted = purity(&gk) < 0.150;
    for _ in 0..1500 {
        gk = tick_std(&gk, &rho);
    }
    add(
        "R11",
        Some(halted && purity(&gk) > P_CRIT && purity(&gk) <= P_UPPER),
        "κ = 0 halts at grey; restoring κ reignites (no hysteresis)",
        format!("P_back={:.3}", purity(&gk)),
    );
    let mut gt = rand_state(&mut rng, 0.5);
    for _ in 0..800 {
        gt = tick_std(&gt, &rho);
    }
    let rv = 1.0 / (7.0 * purity(&gt));
    add("R12", Some((1.0 / 3.0..0.5).contains(&rv)), "in the window R = 1/(7P) ∈ [1/3, 1/2)",
        format!("R={:.3}", rv));
    let gr = rand_state(&mut rng, 0.6);
    let gr2 = dial(&gr, 0, 4, 0.3);
    add("R13", Some((purity(&gr2) - purity(&gr)).abs() < 1e-12),
        "SO(7) dials preserve the spectrum", format!("dP={:.1e}", purity(&gr2) - purity(&gr)));
    add(
        "R14",
        Some((max_stress(&CMat::grey(N)) - 1.0).abs() < 1e-9),
        "at the grey state the loudest σ = 1 exactly (the wall)",
        format!("maxσ={:.3}", max_stress(&CMat::grey(N))),
    );
    let zero_modes = H_EFF.iter().filter(|&&x| x.abs() < 1e-12).count();
    add("R15", Some(zero_modes == 1), "dim ker(H_eff) = 1 ⇒ freedom kernel ≥ 2 doors",
        format!("{} zero mode(s)", zero_modes));

    // ------------- pair floor -------------
    let mut rp = StdRng::seed_from_u64(29);
    let mut ok_law = true;
    let mut ok_pos = true;
    let mut ok_red = true;
    let mut worst = 0.0f64;
    for _ in 0..25 {
        let ga = rand_state(&mut rp, 0.6);
        let gb = rand_state(&mut rp, 0.6);
        let pg = pair_gain(&ga, &gb, 0, 4, 1, 5, 1e-3);
        worst = worst.max((pg.d_p - pg.linear - pg.quadratic).abs());
        ok_law &= (pg.d_p - pg.linear - pg.quadratic).abs() < 1e-12;
        ok_pos &= pg.d_p >= -1e-15 && pg.psd_min > -1e-12;
        ok_red &= pg.reduced_delta < 1e-14;
    }
    add("R16", Some(ok_law), "pair purity law: ΔP = linear + 2ε²|γ|² exactly (T-77)",
        format!("worst residual {:.1e} / 25 pairs", worst));
    add("R17", Some(ok_pos), "an aligned bridge never subtracts; PSD kept", "25/25".into());
    add("R18", Some(ok_red), "the gain lives in the bond: reduced states unchanged",
        "25/25, |dG| < 1e-14".into());
    add(
        "R19",
        Some(purity_ladder(3) < 1.0 && purity_ladder(4) > 1.0),
        "the composition ceiling: P⁽³⁾=9/14 < 1 < 54/35=P⁽⁴⁾",
        format!("{:.4} < 1 < {:.4}", purity_ladder(3), purity_ladder(4)),
    );

    // ------------- tower floor -------------
    let mut rt = StdRng::seed_from_u64(37);
    let mut aligned: Vec<CMat> = (0..7).map(|_| rand_state(&mut rt, 0.5)).collect();
    for _ in 0..400 {
        aligned = aligned.iter().map(|g| tick_std(g, &rho)).collect();
    }
    let mut disparate: Vec<CMat> = (0..7).map(|_| rand_state(&mut rt, 0.5)).collect();
    let ids: Vec<CMat> = (0..7).map(|_| rand_selfmodel(&mut rt, 0.42)).collect();
    for _ in 0..400 {
        disparate = disparate.iter().zip(ids.iter()).map(|(g, id)| tick_std(g, id)).collect();
    }
    let (p_al, p_di) = (purity(&gram_meta(&aligned)), purity(&gram_meta(&disparate)));
    add(
        "R20",
        Some(p_al > P_CRIT && p_di <= P_CRIT),
        "a shared ideal makes a viable meta-holon; personal ideals do not",
        format!("meta-P {:.3} vs {:.3} (wall 2/7)", p_al, p_di),
    );

    // ------------- geodesic floor -------------
    let mut rg = StdRng::seed_from_u64(41);
    let gg0 = rand_state(&mut rg, 0.35);
    let mut grr = gg0.clone();
    let mut dmax = 0.0f64;
    for _ in 0..300 {
        grr = grr.add(&rho.sub(&grr).scale(0.01 * 1.5));
        dmax = dmax.max(chord_distance(&grr, &gg0, &rho));
    }
    add("R21", Some(dmax < 1e-12), "pure regeneration rides the m-chord exactly (T-263 shadow)",
        format!("max dist {:.1e}", dmax));

    // ------------- atlas floor -------------
    let g_ds = [0.1, 0.25, 0.4, 0.55];
    let kaps = [0.0, 0.5, 1.0, 2.0, 3.0];
    let atlas = phase_atlas(&g_ds, &kaps, 400, &rho);
    let n_w: usize = atlas.iter().map(|r| r.iter().filter(|&&c| c == Cell::Window).count()).sum();
    add(
        "R22",
        Some(n_w > 0 && n_w < g_ds.len() * kaps.len()),
        "the window is a proper band of the (dissipation, supply) plane",
        format!("{}/{} cells", n_w, g_ds.len() * kaps.len()),
    );
    let col0_grey = atlas.iter().all(|r| r[0] == Cell::Grey);
    add("R23", Some(col0_grey), "the κ = 0 column is all grey: no supply, no being",
        format!("{}/{}", g_ds.len(), g_ds.len()));

    // ------------- determinism -------------
    let mut r1 = StdRng::seed_from_u64(23);
    let mut r2 = StdRng::seed_from_u64(23);
    let mut ga = rand_state(&mut r1, 0.6);
    let mut gb = rand_state(&mut r2, 0.6);
    for _ in 0..200 {
        ga = tick_std(&ga, &rho);
        gb = tick_std(&gb, &rho);
    }
    add("R24", Some(ga.max_abs_diff(&gb) < 1e-12), "the machine is deterministic",
        format!("|dG|={:.1e}", ga.max_abs_diff(&gb)));
    // eigensolver self-check: reconstruct
    let gx = rand_state(&mut r1, 0.7);
    let (w, v) = eigh(&gx);
    let mut rec = CMat::zeros(N);
    for k in 0..N {
        for i in 0..N {
            for j in 0..N {
                rec[(i, j)] += v[(i, k)] * v[(j, k)].conj() * C64::new(w[k], 0.0);
            }
        }
    }
    add("R25", Some(rec.max_abs_diff(&gx.herm()) < 1e-10),
        "the Jacobi eigensolver reconstructs Γ = V diag(w) V†",
        format!("|dG|={:.1e}", rec.max_abs_diff(&gx.herm())));

    // ------------- estimator floor (v0.6) -------------
    {
        use crate::estimator::*;
        let r = track_full(9000, 0.02, 0.05, 0.25, 200, 50);
        add("R26", Some(r.filter < r.obs_only && r.filter < r.dead_reckoning),
            "the [K] filter beats both baselines under process noise",
            format!("{:.4} < obs {:.4}, dead {:.4}", r.filter, r.obs_only, r.dead_reckoning));
        let all: Vec<(usize, usize)> = dial_pairs();
        let k0 = tune_gain_partial(&[], 0.01, 0.05);
        let k21 = tune_gain_partial(&all, 0.01, 0.05);
        let r0 = track_partial(9100, &[], 0.01, 0.05, k0, 200, 50);
        let r21 = track_partial(9100, &all, 0.01, 0.05, k21, 200, 50);
        add("R27", Some(r21.2 < r0.2 && r21.3 < r0.3),
            "full magnitude coverage sharpens P and Φ recovery (m=21 vs m=0, tuned gains)",
            format!("|dP| {:.4}->{:.4}, |dΦ| {:.4}->{:.4}", r0.2, r21.2, r0.3, r21.3));
    }

    out
}
