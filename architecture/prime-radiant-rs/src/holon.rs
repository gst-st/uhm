//! The mathematical heart: Γ ∈ D(ℂ⁷), the canonical UHM tick, observables,
//! the T-92 stress panel, and the Fano wiring in the corpus numbering.
//!
//! Mirrors `architecture/prime_radiant.py` (the Python reference machine);
//! every constant and formula is the calibrated one — see the H46 catch:
//! the corpus arithmetic numbering is A=1 S=2 D=3 L=4 E=5 **U=6 O=7**.

use num_complex::Complex64 as C64;

pub const N: usize = 7;
pub const AXES: [char; 7] = ['A', 'S', 'D', 'L', 'E', 'O', 'U'];
/// Storage indices (display order A,S,D,L,E,O,U).
pub const A_: usize = 0;
pub const D_: usize = 2;
pub const L_: usize = 3;
pub const E_: usize = 4;
pub const O_: usize = 5;
pub const U_: usize = 6;
/// Corpus arithmetic numbering (fano-selection-rules): NUM[axis] with U=6, O=7.
pub const NUM: [usize; 7] = [1, 2, 3, 4, 5, 7, 6]; // A S D L E O U  (O->7, U->6)

pub const P_CRIT: f64 = 2.0 / 7.0;
pub const P_UPPER: f64 = 3.0 / 7.0;
pub const OMEGA0: f64 = 1.0;
pub const KAPPA_BOOT: f64 = OMEGA0 / 7.0;

/// λ_E highest — the A5 spectral order of the effective Hamiltonian (diagonal).
pub const H_EFF: [f64; 7] = [0.0, 0.6, 1.0, 1.6, 3.0, 2.0, 2.4];

// ============================= complex matrices =============================

#[derive(Clone, PartialEq, Debug)]
pub struct CMat {
    pub n: usize,
    pub a: Vec<C64>,
}

impl CMat {
    pub fn zeros(n: usize) -> Self {
        CMat { n, a: vec![C64::new(0.0, 0.0); n * n] }
    }
    pub fn eye(n: usize) -> Self {
        let mut m = Self::zeros(n);
        for i in 0..n {
            m[(i, i)] = C64::new(1.0, 0.0);
        }
        m
    }
    /// I/n — the grey state.
    pub fn grey(n: usize) -> Self {
        let mut m = Self::eye(n);
        for v in m.a.iter_mut() {
            *v /= n as f64;
        }
        m
    }
    pub fn mul(&self, o: &CMat) -> CMat {
        let n = self.n;
        let mut r = CMat::zeros(n);
        for i in 0..n {
            for k in 0..n {
                let s = self[(i, k)];
                if s.norm_sqr() == 0.0 {
                    continue;
                }
                for j in 0..n {
                    r[(i, j)] += s * o[(k, j)];
                }
            }
        }
        r
    }
    pub fn dagger(&self) -> CMat {
        let n = self.n;
        let mut r = CMat::zeros(n);
        for i in 0..n {
            for j in 0..n {
                r[(j, i)] = self[(i, j)].conj();
            }
        }
        r
    }
    pub fn herm(&self) -> CMat {
        let n = self.n;
        let mut r = CMat::zeros(n);
        for i in 0..n {
            for j in 0..n {
                r[(i, j)] = (self[(i, j)] + self[(j, i)].conj()) * 0.5;
            }
        }
        r
    }
    pub fn trace(&self) -> C64 {
        (0..self.n).map(|i| self[(i, i)]).sum()
    }
    pub fn scale(&self, s: f64) -> CMat {
        let mut r = self.clone();
        for v in r.a.iter_mut() {
            *v *= s;
        }
        r
    }
    pub fn add(&self, o: &CMat) -> CMat {
        let mut r = self.clone();
        for (v, w) in r.a.iter_mut().zip(o.a.iter()) {
            *v += *w;
        }
        r
    }
    pub fn sub(&self, o: &CMat) -> CMat {
        let mut r = self.clone();
        for (v, w) in r.a.iter_mut().zip(o.a.iter()) {
            *v -= *w;
        }
        r
    }
    pub fn max_abs_diff(&self, o: &CMat) -> f64 {
        self.a
            .iter()
            .zip(o.a.iter())
            .map(|(v, w)| (*v - *w).norm())
            .fold(0.0, f64::max)
    }
    pub fn frob_norm(&self) -> f64 {
        self.a.iter().map(|v| v.norm_sqr()).sum::<f64>().sqrt()
    }
}

impl std::ops::Index<(usize, usize)> for CMat {
    type Output = C64;
    fn index(&self, (i, j): (usize, usize)) -> &C64 {
        &self.a[i * self.n + j]
    }
}
impl std::ops::IndexMut<(usize, usize)> for CMat {
    fn index_mut(&mut self, (i, j): (usize, usize)) -> &mut C64 {
        &mut self.a[i * self.n + j]
    }
}

// ====================== Hermitian eigensolver (Jacobi) ======================

/// Cyclic Jacobi for a Hermitian matrix: returns (eigenvalues ascending, V)
/// with A = V diag(w) V†. Robust at n=7 and n=49; off-norm driven < 1e-13.
pub fn eigh(m: &CMat) -> (Vec<f64>, CMat) {
    let n = m.n;
    let mut a = m.herm();
    let mut v = CMat::eye(n);
    for _sweep in 0..60 {
        let mut off = 0.0;
        for p in 0..n {
            for q in (p + 1)..n {
                off += a[(p, q)].norm_sqr();
            }
        }
        if off.sqrt() < 1e-14 {
            break;
        }
        for p in 0..n {
            for q in (p + 1)..n {
                let g = a[(p, q)];
                if g.norm() < 1e-300 {
                    continue;
                }
                let alpha = a[(p, p)].re;
                let beta = a[(q, q)].re;
                let absg = g.norm();
                let phase = g / absg; // e^{i φ}
                let theta = 0.5 * (2.0 * absg).atan2(alpha - beta);
                let (c, s) = (theta.cos(), theta.sin());
                // U: identity except U_pp=c, U_pq=-s·phase, U_qp=s·conj(phase), U_qq=c
                // apply A ← U† A U and V ← V U  (column rotation)
                for i in 0..n {
                    let aip = a[(i, p)];
                    let aiq = a[(i, q)];
                    a[(i, p)] = aip * c + aiq * s * phase.conj();
                    a[(i, q)] = -aip * s * phase + aiq * c;
                }
                for j in 0..n {
                    let apj = a[(p, j)];
                    let aqj = a[(q, j)];
                    a[(p, j)] = apj * c + aqj * s * phase;
                    a[(q, j)] = -apj * s * phase.conj() + aqj * c;
                }
                for i in 0..n {
                    let vip = v[(i, p)];
                    let viq = v[(i, q)];
                    v[(i, p)] = vip * c + viq * s * phase.conj();
                    v[(i, q)] = -vip * s * phase + viq * c;
                }
            }
        }
    }
    let mut idx: Vec<usize> = (0..n).collect();
    let w: Vec<f64> = (0..n).map(|i| a[(i, i)].re).collect();
    idx.sort_by(|&i, &j| w[i].partial_cmp(&w[j]).unwrap());
    let ws: Vec<f64> = idx.iter().map(|&i| w[i]).collect();
    let mut vs = CMat::zeros(n);
    for (newc, &oldc) in idx.iter().enumerate() {
        for r in 0..n {
            vs[(r, newc)] = v[(r, oldc)];
        }
    }
    (ws, vs)
}

/// Nearest physical density matrix: Hermitian, PSD, unit trace.
pub fn project_psd(g: &CMat) -> CMat {
    let (w, v) = eigh(g);
    let n = g.n;
    let mut r = CMat::zeros(n);
    for k in 0..n {
        let lam = w[k].max(0.0);
        if lam == 0.0 {
            continue;
        }
        for i in 0..n {
            for j in 0..n {
                r[(i, j)] += v[(i, k)] * v[(j, k)].conj() * lam;
            }
        }
    }
    let t = r.trace().re;
    r.scale(1.0 / t)
}

// ============================= Fano (corpus) ================================

/// The 7 corpus lines as storage-index triples: translates of QR(7)={1,2,4}
/// in the corpus numbering (U=6, O=7).
pub fn fano_lines() -> [[usize; 3]; 7] {
    let n2i = |n: usize| NUM.iter().position(|&x| x == n).unwrap();
    let mut lines = [[0usize; 3]; 7];
    for k in 0..7 {
        let mut tri: Vec<usize> = [1usize, 2, 4]
            .iter()
            .map(|&q| n2i((q - 1 + k) % 7 + 1))
            .collect();
        tri.sort();
        lines[k] = [tri[0], tri[1], tri[2]];
    }
    lines
}

/// Hamming H(7,4) syndrome decode in the XOR labeling: the syndrome of a
/// single-axis fault IS the axis number. Returns 0 for the clean word.
pub fn syndrome_decode(x: u8) -> u8 {
    const H_ROWS: [u8; 3] = [0b1010101, 0b0110011, 0b0001111];
    let mut s = 0u8;
    for (r, row) in H_ROWS.iter().enumerate() {
        s |= (((row & x).count_ones() & 1) as u8) << r;
    }
    s
}

/// Count degraded Fano line-closures of Γ (all three coherences of a line tiny).
pub fn degraded_lines(g: &CMat, thr: f64) -> usize {
    fano_lines()
        .iter()
        .filter(|&&[i, j, k]| {
            g[(i, j)].norm() + g[(j, k)].norm() + g[(i, k)].norm() < thr
        })
        .count()
}

// ============================== observables =================================

pub fn purity(g: &CMat) -> f64 {
    g.mul(g).trace().re
}

pub fn entropy(g: &CMat) -> f64 {
    let (w, _) = eigh(g);
    -w.iter().filter(|&&x| x > 1e-14).map(|&x| x * x.ln()).sum::<f64>()
}

/// Canonical integration measure Φ = Σ_{i≠j}|γ_ij|² / Σ_i γ_ii²  (NOT 7P−1).
pub fn phi_exact(g: &CMat) -> f64 {
    let d2: f64 = (0..g.n).map(|i| g[(i, i)].norm_sqr()).sum();
    let off = purity(g) - d2;
    if d2 > 1e-15 {
        off / d2
    } else {
        f64::INFINITY
    }
}

pub fn coh_e(g: &CMat) -> f64 {
    (0..N).map(|j| g[(E_, j)].norm_sqr()).sum::<f64>() - g[(E_, E_)].norm_sqr()
}

/// κ₀ = ω₀ |γ_OE| |γ_OU| / γ_OO  (the structural ansatz).
pub fn kappa0(g: &CMat) -> f64 {
    let goo = g[(O_, O_)].re;
    if goo < 1e-12 {
        return 0.0;
    }
    OMEGA0 * g[(O_, E_)].norm() * g[(O_, U_)].norm() / goo
}

#[derive(Clone, Copy, Debug, Default)]
pub struct Observables {
    pub p: f64,
    pub r: f64,
    pub phi: f64,
    pub c: f64,
    pub s: f64,
    pub d_diff: f64,
    pub coh_e: f64,
    pub viable: bool,
}

pub fn observables(g: &CMat) -> Observables {
    let p = purity(g);
    let phi = phi_exact(g);
    let r = 1.0 / (7.0 * p);
    let s = entropy(g);
    Observables {
        p,
        r,
        phi,
        c: phi * r,
        s,
        d_diff: s.exp(),
        coh_e: coh_e(g),
        viable: p > P_CRIT && p <= P_UPPER,
    }
}

/// The T-92 stress panel: seven components as functions of Γ alone.
/// σ_S uses the singular values of |Γ_{ASD}| with the 0.02 tolerance
/// (the Γ_S convention of the reference machine; corpus calibration open — H37).
pub fn stress_panel(g: &CMat) -> [f64; 7] {
    let p = purity(g);
    let d_diff = entropy(g).exp();
    // rank of the 3x3 |abs| block on {A,S,D} via eigenvalues of MᵀM
    let idx = [0usize, 1, 2];
    let mut mm = [[0.0f64; 3]; 3];
    for r in 0..3 {
        for c in 0..3 {
            let mut s = 0.0;
            for k in 0..3 {
                s += g[(idx[k], idx[r])].norm() * g[(idx[k], idx[c])].norm();
            }
            mm[r][c] = s;
        }
    }
    let mut m3 = CMat::zeros(3);
    for r in 0..3 {
        for c in 0..3 {
            m3[(r, c)] = C64::new(mm[r][c], 0.0);
        }
    }
    let (w3, _) = eigh(&m3);
    let rank_s = w3.iter().filter(|&&x| x.max(0.0).sqrt() > 0.02).count();
    [
        1.0 - g[(A_, A_)].re / p,
        1.0 - rank_s as f64 / 3.0,
        1.0 - 7.0 * g[(D_, D_)].re,
        7.0 * (1.0 - g[(L_, L_)].re) / 6.0,
        1.0 - d_diff / 7.0,
        1.0 - kappa0(g) / KAPPA_BOOT,
        1.0 - phi_exact(g) / 1.0,
    ]
}

/// The REPAIRED T-92 panel (2026-07-22 errata): sigma_E and sigma_U
/// renormalized so sigma_i < 1 <=> the canonical threshold holds
/// (D_diff > 2, Phi > 1); restores max sigma < 1 => P > 2/7 via
/// sum(gamma_ii^2) >= 1/7.
pub fn stress_panel_v2(g: &CMat) -> [f64; 7] {
    let mut sp = stress_panel(g);
    let d_diff = entropy(g).exp();
    sp[4] = (7.0 - d_diff) / 5.0;
    sp[6] = 2.0 / (1.0 + phi_exact(g));
    sp
}

pub fn max_stress(g: &CMat) -> f64 {
    stress_panel(g).iter().cloned().fold(f64::MIN, f64::max)
}

// ================================ the tick ==================================

/// exp(−i H_eff dt/2) applied as Γ ← U Γ U† — H_eff is diagonal, so this is
/// the exact phase map γ_jk ← e^{−i(λ_j−λ_k)dt/2} γ_jk (spectrum-preserving).
pub fn unitary_half(g: &CMat, dt: f64) -> CMat {
    let mut r = g.clone();
    for j in 0..N {
        for k in 0..N {
            let ph = -(H_EFF[j] - H_EFF[k]) * dt / 2.0;
            r[(j, k)] *= C64::from_polar(1.0, ph);
        }
    }
    r
}

/// One ℒ_Ω tick (Strang split, CPTP-safe):
/// Γ ← 𝒰 [ Γ + dt·( g_D(I/7 − Γ) + κ(ρ* − Γ) ) ] 𝒰,  κ = gain·1.2·(1+8·Coh_E).
pub fn tick(g: &CMat, rho: &CMat, dt: f64, g_d: f64, kap_gain: f64) -> CMat {
    let kap = kap_gain * 1.2 * (1.0 + 8.0 * coh_e(g));
    let mut x = unitary_half(g, dt);
    let grey = CMat::grey(N);
    let diss = grey.sub(&x).scale(g_d * dt);
    let regen = rho.sub(&x).scale(kap * dt);
    x = x.add(&diss).add(&regen);
    x = unitary_half(&x, dt);
    project_psd(&x)
}

pub fn tick_std(g: &CMat, rho: &CMat) -> CMat {
    tick(g, rho, 0.01, 0.2, 1.0)
}

// ============================ states & controls =============================

/// The structured self-model ρ*: weights E=1.0, O=0.8, U=0.6, A=0.4, mixed
/// with grey to purity closest to `target_p` (the reference construction).
pub fn make_selfmodel(target_p: f64) -> CMat {
    let mut v = [C64::new(0.0, 0.0); N];
    v[E_] = C64::new(1.0, 0.0);
    v[O_] = C64::new(0.8, 0.0);
    v[U_] = C64::new(0.6, 0.0);
    v[A_] = C64::new(0.4, 0.0);
    let nrm = v.iter().map(|x| x.norm_sqr()).sum::<f64>().sqrt();
    for x in v.iter_mut() {
        *x /= nrm;
    }
    let mut proj = CMat::zeros(N);
    for i in 0..N {
        for j in 0..N {
            proj[(i, j)] = v[i] * v[j].conj();
        }
    }
    let grey = CMat::grey(N);
    let mut best = grey.clone();
    let mut bestd = f64::MAX;
    for t in 0..400 {
        let a = t as f64 / 399.0;
        let mut g = proj.scale(a).add(&grey.scale(1.0 - a));
        let tr = g.trace().re;
        g = g.scale(1.0 / tr);
        let d = (purity(&g) - target_p).abs();
        if d < bestd {
            bestd = d;
            best = g;
        }
    }
    best
}

/// The Source Γ_⊙: the maximally coherent S₇-symmetric pure state.
pub fn source() -> CMat {
    let mut g = CMat::zeros(N);
    for i in 0..N {
        for j in 0..N {
            g[(i, j)] = C64::new(1.0 / N as f64, 0.0);
        }
    }
    g
}

/// A random mixed state: a·|v⟩⟨v| + (1−a)·I/7 with Gaussian |v⟩ (seeded).
pub fn rand_state(rng: &mut impl rand::RngExt, a: f64) -> CMat {
    use rand_distr_normal::normal_pair;
    let mut v = [C64::new(0.0, 0.0); N];
    for x in v.iter_mut() {
        let (re, im) = normal_pair(rng);
        *x = C64::new(re, im);
    }
    let nrm = v.iter().map(|x| x.norm_sqr()).sum::<f64>().sqrt();
    for x in v.iter_mut() {
        *x /= nrm;
    }
    let mut proj = CMat::zeros(N);
    for i in 0..N {
        for j in 0..N {
            proj[(i, j)] = v[i] * v[j].conj();
        }
    }
    let g = proj.scale(a).add(&CMat::grey(N).scale(1.0 - a));
    let t = g.trace().re;
    g.scale(1.0 / t)
}

/// Box–Muller without extra deps.
mod rand_distr_normal {
    use rand::RngExt;
    pub fn normal_pair(rng: &mut impl RngExt) -> (f64, f64) {
        let u1: f64 = rng.random_range(1e-12f64..1.0);
        let u2: f64 = rng.random_range(0.0f64..1.0);
        let r = (-2.0 * u1.ln()).sqrt();
        let th = 2.0 * std::f64::consts::PI * u2;
        (r * th.cos(), r * th.sin())
    }
}

/// A spectrum-preserving dial: the Givens rotation of the (i,j) plane by θ,
/// applied as Γ ← R Γ Rᵀ. Purity, entropy, D_diff are exactly conserved.
pub fn dial(g: &CMat, i: usize, j: usize, theta: f64) -> CMat {
    let (c, s) = (theta.cos(), theta.sin());
    let mut r = g.clone();
    // rows
    for k in 0..N {
        let gi = r[(i, k)];
        let gj = r[(j, k)];
        r[(i, k)] = gi * c + gj * s;
        r[(j, k)] = -gi * s + gj * c;
    }
    // columns
    for k in 0..N {
        let gi = r[(k, i)];
        let gj = r[(k, j)];
        r[(k, i)] = gi * c + gj * s;
        r[(k, j)] = -gi * s + gj * c;
    }
    r
}

/// All 21 dial planes.
pub fn dial_pairs() -> Vec<(usize, usize)> {
    let mut v = Vec::new();
    for i in 0..N {
        for j in (i + 1)..N {
            v.push((i, j));
        }
    }
    v
}
