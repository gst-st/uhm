//! The pair space D(ℂ⁴⁹): the product state, the cross-bridge, partial
//! traces, and the measured T-77 gain. Mirrors the Python organ [G].

use crate::holon::*;
use num_complex::Complex64 as C64;

/// Kronecker product Γ₁ ⊗ Γ₂ (49×49).
pub fn kron(g1: &CMat, g2: &CMat) -> CMat {
    let n = N * N;
    let mut r = CMat::zeros(n);
    for i in 0..N {
        for j in 0..N {
            let s = g1[(i, j)];
            if s.norm_sqr() == 0.0 {
                continue;
            }
            for k in 0..N {
                for l in 0..N {
                    r[(i * N + k, j * N + l)] = s * g2[(k, l)];
                }
            }
        }
    }
    r
}

/// A pure cross-coherence between holon-1 transition (i↔j) and holon-2
/// transition (k↔l), i≠j, k≠l: both partial traces of the bridge vanish
/// identically — the bond adds nothing to either reduced state.
pub fn cross_bridge(i: usize, j: usize, k: usize, l: usize, gamma: C64) -> CMat {
    let n = N * N;
    let mut x = CMat::zeros(n);
    x[(i * N + k, j * N + l)] = gamma;
    x[(j * N + l, i * N + k)] = gamma.conj();
    x
}

/// Reduced state of holon 1 (trace out holon 2).
pub fn ptrace1(gp: &CMat) -> CMat {
    let mut r = CMat::zeros(N);
    for i in 0..N {
        for j in 0..N {
            let mut s = C64::new(0.0, 0.0);
            for k in 0..N {
                s += gp[(i * N + k, j * N + k)];
            }
            r[(i, j)] = s;
        }
    }
    r
}

/// Reduced state of holon 2 (trace out holon 1).
pub fn ptrace2(gp: &CMat) -> CMat {
    let mut r = CMat::zeros(N);
    for k in 0..N {
        for l in 0..N {
            let mut s = C64::new(0.0, 0.0);
            for i in 0..N {
                s += gp[(i * N + k, i * N + l)];
            }
            r[(k, l)] = s;
        }
    }
    r
}

pub struct PairGain {
    pub d_p: f64,
    pub linear: f64,
    pub quadratic: f64,
    pub psd_min: f64,
    pub reduced_delta: f64,
}

/// The measured ΔP of the bridged pair vs the product, with the aligned
/// bridge phase. The exact law: ΔP = linear + 2ε²|γ|² (see H47).
pub fn pair_gain(g1: &CMat, g2: &CMat, i: usize, j: usize, k: usize, l: usize, eps: f64) -> PairGain {
    let gp = kron(g1, g2);
    // align the agreement: sign of the linear term
    let mut c = CMat::zeros(N * N);
    c[(i * N + k, j * N + l)] = C64::new(1.0, 0.0);
    let cc = c.add(&c.dagger());
    let lin_raw = gp.mul(&cc).trace().re;
    let phase = if lin_raw >= 0.0 { 1.0 } else { -1.0 };
    let x = cross_bridge(i, j, k, l, C64::new(phase, 0.0));
    let gb = gp.add(&x.scale(eps));
    let d_p = purity(&gb) - purity(&gp);
    let linear = 2.0 * eps * gp.mul(&x).trace().re;
    let quadratic = eps * eps * x.mul(&x).trace().re; // = 2 ε² |γ|²
    let (w, _) = eigh(&gb);
    let psd_min = w[0];
    let rd1 = ptrace1(&gb).max_abs_diff(g1);
    let rd2 = ptrace2(&gb).max_abs_diff(g2);
    PairGain {
        d_p,
        linear,
        quadratic,
        psd_min,
        reduced_delta: rd1.max(rd2),
    }
}

/// The centered Gram meta-holon of an ecology: M_ij = tr((Γᵢ−I/7)(Γⱼ−I/7)),
/// trace-normalized. A meta-subject is made of its members' distinctive
/// commitments, not of the greyness they share.
pub fn gram_meta(states: &[CMat]) -> CMat {
    let m = states.len();
    let grey = CMat::grey(N);
    let devs: Vec<CMat> = states.iter().map(|g| g.sub(&grey)).collect();
    let mut r = CMat::zeros(m);
    for i in 0..m {
        for j in 0..m {
            r[(i, j)] = C64::new(devs[i].mul(&devs[j]).trace().re, 0.0);
        }
    }
    let t = r.trace().re;
    r.scale(1.0 / t)
}

/// P_crit^(m) = (2/7)·3^(m−1)/(m+1) — the purity ladder (axiom-omega).
pub fn purity_ladder(m: u32) -> f64 {
    (2.0 / 7.0) * 3f64.powi(m as i32 - 1) / (m as f64 + 1.0)
}
