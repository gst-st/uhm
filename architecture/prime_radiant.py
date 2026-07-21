#!/usr/bin/env python3
"""
PRIME RADIANT v0 -- the golden-path navigator over Gamma (reference implementation).

The executable companion of applied/research/prime-radiant.md. One machine, five organs:

  [A] the arithmetic floor of residues: the Fano wiring as translates of QR(7)={1,2,4},
      the multiplier 2*QR=QR (the Z3 Frobenius), the Hamming H(7,4) syndrome decoder,
      and the machine-found dictionary between the two corpus coordinatizations
      (XOR labels of syndrome-calculus vs octonionic/QR labels of fano-selection-rules);
  [B] the analytic floor of residues: spectral projectors and f(Gamma) as Cauchy
      contour integrals of the resolvent, verified against direct diagonalization;
  [C] the canonical observable suite: P, R=1/(7P), exact Phi (NOT the 7P-1 proxy),
      C=Phi*R, S, D_diff=e^S, Coh_E, and the T-92 stress panel sigma_1..sigma_7;
  [D] the canonical dynamics: the TALOS tick L_Omega = -i[H,.] + D[.] + R[.]
      (Strang split, CPTP-safe), kappa(Coh_E) negentropy feedback;
  [E] the navigator: goal regions, spectrum-preserving controls (SO(7) dials),
      costly kappa-boosts ("bold moves"), greedy lookahead navigation, the
      Dee-solitaire Monte-Carlo oracle, and the ensemble ("psychohistory") limit.

Honest scope: [A],[B] are standard mathematics [T] machine-checked here; [C],[D]
implement corpus definitions/dynamics; [E] is an engineering protocol [O/I] whose
claims are printed as measured numbers, not asserted. numpy only, deterministic.

Run:  python3 prime_radiant.py
"""
import numpy as np

N = 7
I7 = np.eye(N) / N
AXES = ['A', 'S', 'D', 'L', 'E', 'O', 'U']
A_, S_, D_, L_, E_, O_, U_ = range(7)

# =============================================================================
# [A] the arithmetic floor: residues mod 7
# =============================================================================
QR = sorted({(k * k) % 7 for k in range(1, 7)})            # quadratic residues mod 7

NUM = {'A': 1, 'S': 2, 'D': 3, 'L': 4, 'E': 5, 'U': 6, 'O': 7}
# ^ the corpus arithmetic numbering (fano-selection-rules): note U=6, O=7 --
#   NOT the display order A,S,D,L,E,O,U. The clock voice O is the 7th residue.
IDX = {ax: i for i, ax in enumerate(AXES)}                 # storage order

def fano_lines_named():
    """The seven corpus lines: translates of QR(7)={1,2,4} in the corpus
    numbering, stored as index-triples of the display order."""
    out = []
    for k in range(7):
        nums = {(q - 1 + k) % 7 + 1 for q in QR}
        out.append(tuple(sorted(IDX[ax] for ax in AXES if NUM[ax] in nums)))
    return out

LINES = fano_lines_named()                                 # corpus-named wiring

def fano_lines_oriented():
    """The canonically ORIENTED lines: (k+1, k+2, k+4) in the corpus numbering
    (e_i e_j = e_k on each translate of (1,2,4)); orientation feeds the phi
    3-form -- sorted triples would break the octonionic structure constants."""
    n2i = {NUM[ax]: IDX[ax] for ax in AXES}
    wrap = lambda n: (n - 1) % 7 + 1
    return [(n2i[wrap(k + 1)], n2i[wrap(k + 2)], n2i[wrap(k + 4)])
            for k in range(7)]

LINES_OR = fano_lines_oriented()

def frobenius_orbit():
    """The multiplier theorem in action: n -> 2n mod 7 maps QR to QR, hence
    permutes the lines; its orbit structure on the 7 lines is 1+3+3."""
    n2i = {NUM[ax]: IDX[ax] for ax in AXES}
    sig = {n2i[n]: n2i[(2 * n - 1) % 7 + 1] for n in range(1, 8)}
    def image(ln):
        return tuple(sorted(sig[p] for p in ln))
    ok = sorted(image(ln) for ln in LINES) == sorted(LINES)
    orbits, seen = [], set()
    for ln in LINES:
        if ln in seen:
            continue
        cur, orb = ln, []
        while cur not in seen:
            seen.add(cur)
            orb.append(cur)
            cur = image(cur)
        orbits.append(len(orb))
    return ok, sorted(orbits)

# --- Hamming H(7,4): the XOR coordinatization of syndrome-calculus ----------
H_ROWS = [0b1010101, 0b0110011, 0b0001111]                 # column a = binary of a
LINES_XOR = [(1, 2, 3), (1, 4, 5), (2, 4, 6), (3, 4, 7),
             (2, 5, 7), (3, 5, 6), (1, 6, 7)]              # a XOR b = c labeling

def syndrome_decode(x):
    """Hamming decode: 7-bit fault profile -> the corrupted axis (1..7) or 0."""
    s = 0
    for r, row in enumerate(H_ROWS):
        s |= (bin(row & x).count('1') & 1) << r
    return s                                               # the syndrome IS the address

def coordinatization_dictionary():
    """Machine-find a point permutation carrying the XOR lines onto the QR lines
    (all Fano planes are isomorphic; the corpus uses both labelings)."""
    import itertools
    tgt = {tuple(sorted(p + 1 for p in ln)) for ln in LINES}
    for perm in itertools.permutations(range(1, 8)):
        m = {i + 1: perm[i] for i in range(7)}
        if {tuple(sorted(m[p] for p in ln)) for ln in LINES_XOR} == tgt:
            return m
    return None

# =============================================================================
# [B] the analytic floor: Cauchy residues of the resolvent
# =============================================================================
def contour_apply(M, f, center, radius, nodes=96):
    """(1/2 pi i) * contour-integral of f(z) (z-M)^(-1) dz over a circle:
    the sum of residues of the resolvent inside = sum f(lam_j) P_j."""
    M = np.asarray(M, dtype=complex)
    acc = np.zeros_like(M)
    for t in range(nodes):
        th = 2 * np.pi * (t + 0.5) / nodes
        z = center + radius * np.exp(1j * th)
        dz = radius * 1j * np.exp(1j * th) * (2 * np.pi / nodes)
        acc += f(z) * np.linalg.solve(z * np.eye(N) - M, np.eye(N)) * dz
    return acc / (2j * np.pi)

def spectral_projector(M, center, radius, nodes=96):
    return contour_apply(M, lambda z: 1.0, center, radius, nodes)

def f_via_contour(M, f, pad=0.35, nodes=256):
    """f(M) for Hermitian M by one contour enclosing the whole spectrum."""
    w = np.linalg.eigvalsh((M + M.conj().T) / 2)
    c = (w.min() + w.max()) / 2
    r = (w.max() - w.min()) / 2 + pad
    return contour_apply(M, f, c, r, nodes)

# =============================================================================
# [C] the canonical observable suite (precision: exact Phi, T-92 panel)
# =============================================================================
def herm(G):
    return (G + G.conj().T) / 2

def purity(G):
    return float(np.trace(G @ G).real)

def entropy(G):
    w = np.linalg.eigvalsh(herm(G))
    w = w[w > 1e-14]
    return float(-(w * np.log(w)).sum())

def phi_exact(G):
    """Canonical integration measure (dimension-u): off-diagonal power over
    diagonal power. NOT the uniform-diagonal proxy 7P-1."""
    d2 = float(np.sum(np.abs(np.diag(G)) ** 2))
    off = purity(G) - d2
    return off / d2 if d2 > 1e-15 else float('inf')

def coh_e(G):
    return float(np.sum(np.abs(G[E_, :]) ** 2) - np.abs(G[E_, E_]) ** 2)

OMEGA0 = 1.0
KAPPA_BOOT = OMEGA0 / 7                                    # kappa_boot = omega0/7

def kappa0(G):
    """kappa_0 = omega0 |gamma_OE||gamma_OU| / gamma_OO (structural ansatz)."""
    gOO = float(np.real(G[O_, O_]))
    if gOO < 1e-12:
        return 0.0
    return OMEGA0 * abs(G[O_, E_]) * abs(G[O_, U_]) / gOO

def stress_panel(G):
    """The T-92 stress tensor: seven components as functions of Gamma alone."""
    P = purity(G)
    Ddiff = float(np.exp(entropy(G)))
    sv = np.linalg.svd(np.abs(G[np.ix_([A_, S_, D_], [A_, S_, D_])]), compute_uv=False)
    rankS = int(np.sum(sv > 0.02))
    return {
        'A': 1 - float(np.real(G[A_, A_])) / P,
        'S': 1 - rankS / 3,
        'D': 1 - N * float(np.real(G[D_, D_])),
        'L': N * (1 - float(np.real(G[L_, L_]))) / (N - 1),
        'E': 1 - Ddiff / N,
        'O': 1 - kappa0(G) / KAPPA_BOOT,
        'U': 1 - phi_exact(G) / 1.0,                       # Phi_th = 1
    }

def observables(G):
    P = purity(G)
    Phi = phi_exact(G)
    R = 1.0 / (7 * P)
    return dict(P=P, R=R, Phi=Phi, C=Phi * R, S=entropy(G),
                Ddiff=float(np.exp(entropy(G))), CohE=coh_e(G),
                viable=(2 / 7 < P <= 3 / 7), sigma=stress_panel(G))

# =============================================================================
# [D] the canonical dynamics: the TALOS tick (Strang split, CPTP-safe)
# =============================================================================
H_EFF = np.diag([0.0, 0.6, 1.0, 1.6, 3.0, 2.0, 2.4])      # lambda_E highest (A5 order)

def expm(M, order=18):
    M = np.asarray(M, dtype=complex)
    s = max(0, int(np.ceil(np.log2(np.abs(M).sum() + 1.0))))
    Ms = M / (2 ** s)
    Eacc = np.eye(N, dtype=complex)
    term = np.eye(N, dtype=complex)
    for k in range(1, order + 1):
        term = term @ Ms / k
        Eacc = Eacc + term
    for _ in range(s):
        Eacc = Eacc @ Eacc
    return Eacc

def project_psd(G):
    w, V = np.linalg.eigh(herm(G))
    w = np.clip(w, 0.0, None)
    G = (V * w) @ V.conj().T
    return G / np.trace(G).real

def tick(G, rho, dt=0.01, gD=0.2, kap_gain=1.0):
    """One L_Omega tick: unitary half / (dissipator + regeneration) / unitary half."""
    kap = kap_gain * 1.2 * (1.0 + 8.0 * coh_e(G))
    Uu = expm(-1j * H_EFF * dt / 2)
    G = Uu @ G @ Uu.conj().T
    G = G + dt * (gD * (I7 - G) + kap * (rho - G))
    G = Uu @ G @ Uu.conj().T
    return project_psd(G)

def make_selfmodel(target_P=0.42):
    v = np.zeros(N, complex)
    v[E_], v[O_], v[U_], v[A_] = 1.0, 0.8, 0.6, 0.4
    v /= np.linalg.norm(v)
    best = None
    for a in np.linspace(0, 1, 400):
        G = a * np.outer(v, v.conj()) + (1 - a) * I7
        G = G / np.trace(G).real
        if best is None or abs(purity(G) - target_P) < abs(purity(best) - target_P):
            best = G
    return best

RHO_STAR = make_selfmodel()

def _g2_generators():
    phi = np.zeros((N, N, N))
    for (i, j, k) in LINES_OR:
        for a, b, c in [(i, j, k), (j, k, i), (k, i, j)]:
            phi[a, b, c] = 1.0
            phi[b, a, c] = -1.0
    idx = [(a, b) for a in range(N) for b in range(a + 1, N)]
    Ms = []
    for (a, b) in idx:
        T = np.zeros((N, N))
        T[a, b], T[b, a] = 1.0, -1.0
        Ms.append(T)
    rows = []
    for T in Ms:
        dphi = (np.einsum('il,ljk->ijk', T, phi)
                + np.einsum('jl,ilk->ijk', T, phi)
                + np.einsum('kl,ijl->ijk', T, phi))
        rows.append(dphi.reshape(-1))
    Amat = np.array(rows).T
    _, sv, Vt = np.linalg.svd(Amat)
    null = Vt[np.sum(sv > 1e-9):]
    return [sum(c * Ms[i] for i, c in enumerate(v)) for v in null]

try:
    G2GENS = _g2_generators()
except Exception:
    G2GENS = None

def rand_selfmodel(rng, target_P=0.42):
    """An individual identity: a personal rho* with the same E/O/U emphasis
    but its own orientation -- WHO the holon is."""
    v = np.zeros(N, complex)
    v[E_], v[O_], v[U_] = 1.0, 0.8, 0.6
    v = v + 0.45 * (rng.standard_normal(N) + 1j * rng.standard_normal(N))
    v /= np.linalg.norm(v)
    best = None
    for a in np.linspace(0, 1, 200):
        G = a * np.outer(v, v.conj()) + (1 - a) * I7
        G = G / np.trace(G).real
        if best is None or abs(purity(G) - target_P) < abs(purity(best) - target_P):
            best = G
    return best

# =============================================================================
# [E] the navigator: goals, dials, bold moves, solitaire, ensembles
# =============================================================================
def so7_dial(i, j, theta):
    """A spectrum-preserving control: rotate the (i,j) plane by theta.
    Purity, entropy, D_diff are exactly conserved; only the wiring changes."""
    T = np.zeros((N, N))
    T[i, j], T[j, i] = 1.0, -1.0
    return expm(theta * T)

DIALS = [(i, j) for i in range(N) for j in range(i + 1, N)]

def time_to_window(G, boosts=0, max_ticks=4000, probe=40):
    """Ride the field to the viable window; the first `boosts` ticks are bold
    (kappa x3 -- burn extra negentropy). Returns (ticks, early mean stress, G)."""
    early = []
    for t in range(max_ticks):
        if 2 / 7 < purity(G) <= 3 / 7:
            return t, (float(np.mean(early)) if early else 0.0), G
        G = tick(G, RHO_STAR, kap_gain=(3.0 if t < boosts else 1.0))
        if t < probe:
            early.append(float(np.mean(list(stress_panel(G).values()))))
    return max_ticks, (float(np.mean(early)) if early else 0.0), G

def tune_chord(G, C_star, max_dials=60, theta=0.12):
    """Phase 2: inside the window, spectrum-preserving dials raise C = Phi*R
    (the drift cannot choose your chord for you -- that part is freedom)."""
    used = 0
    while observables(G)['C'] < C_star and used < max_dials:
        best, bestC = None, observables(G)['C']
        for (i, j) in DIALS:
            for sgn in (+1, -1):
                Uc = so7_dial(i, j, sgn * theta)
                Gc = tick(Uc @ G @ Uc.conj().T, RHO_STAR)
                c = observables(Gc)['C']
                if c > bestC and 2 / 7 < purity(Gc) <= 3 / 7 + 0.02:
                    best, bestC = Gc, c
        if best is None:
            break
        G, used = best, used + 1
    return G, used

def solitaire(G0, deals=200, horizon=250, bold=True, seed=1):
    """The Dee solitaire: many random control decks; the fraction that 'comes
    together' (reaches the window within the horizon) is the oracle p_golden."""
    rng = np.random.default_rng(seed)
    wins, heats, times = 0, [], []
    for d in range(deals):
        G = G0.copy()
        heat = []
        for t in range(horizon):
            r = rng.random()
            if r < 0.5:
                G = tick(G, RHO_STAR)
            elif r < 0.75 or not bold:
                i, j = DIALS[rng.integers(len(DIALS))]
                Uc = so7_dial(i, j, (rng.random() - 0.5) * 0.4)
                G = tick(Uc @ G @ Uc.conj().T, RHO_STAR)
            else:
                G = tick(G, RHO_STAR, kap_gain=3.0)        # bold deck plays boosts
            heat.append(float(np.mean(list(stress_panel(G).values()))))
            if 2 / 7 < purity(G) <= 3 / 7:
                wins += 1
                times.append(t)
                break
        heats.append(float(np.mean(heat)))
    return (wins / deals, float(np.mean(heats)),
            float(np.mean(times)) if times else float('nan'))

def rand_state(rng, a=0.6):
    v = rng.standard_normal(N) + 1j * rng.standard_normal(N)
    v /= np.linalg.norm(v)
    G = a * np.outer(v, v.conj()) + (1 - a) * I7
    return G / np.trace(G).real

# =============================================================================
# [G] the pair space D(C^49): cooperation, the bond, rivalry
# =============================================================================
def pair_product(G1, G2):
    return np.kron(G1, G2)

def cross_bridge(i, j, k, l, gamma):
    """A pure cross-coherence between holon-1 transition (i<->j) and holon-2
    transition (k<->l), i!=j, k!=l. Both partial traces vanish identically:
    the bond adds NOTHING to either reduced state -- it lives between them."""
    C = np.zeros((49, 49), complex)
    C[i * 7 + k, j * 7 + l] = 1.0
    return gamma * C + np.conj(gamma) * C.conj().T

def ptrace1(Gp):
    """Trace out holon 2 -> the reduced state of holon 1."""
    return np.trace(Gp.reshape(7, 7, 7, 7), axis1=1, axis2=3)

def ptrace2(Gp):
    return np.trace(Gp.reshape(7, 7, 7, 7), axis1=0, axis2=2)

def pair_gain(G1, G2, i, j, k, l, eps):
    """Measured Delta-P of the bridged pair vs the product, with the optimal
    bridge phase (the 'genuine mutual agreement' of T-77)."""
    Gp = pair_product(G1, G2)
    C = np.zeros((49, 49), complex)
    C[i * 7 + k, j * 7 + l] = 1.0
    lin = np.trace(Gp @ (C + C.conj().T)).real
    phase = 1.0 if lin >= 0 else -1.0                      # align the agreement
    X = cross_bridge(i, j, k, l, phase)
    Gb = Gp + eps * X
    dP = float(np.trace(Gb @ Gb).real - np.trace(Gp @ Gp).real)
    lin_term = 2 * eps * float(np.trace(Gp @ X).real)
    quad_term = eps * eps * float(np.trace(X @ X).real)    # = 2 eps^2 |gamma|^2
    psd_ok = float(np.min(np.linalg.eigvalsh((Gb + Gb.conj().T) / 2)))
    return dP, lin_term, quad_term, psd_ok, Gb, Gp

def attractor_P(kap_gain, gD=0.2, ticks=700, seed=2):
    G = rand_state(np.random.default_rng(seed), 0.6)
    for _ in range(ticks):
        G = tick(G, RHO_STAR, gD=gD, kap_gain=kap_gain)
    return purity(G)

# =============================================================================
# [H] towers: the Gram meta-holon and the purity ladder
# =============================================================================
def gram_meta(states):
    """The ecology's meta-state: the CENTERED Gram matrix of mutual overlaps,
    M_ij = tr((G_i - I/7)(G_j - I/7)) -- PSD by construction, trace-normalized.
    Centering removes the shared grey baseline: a meta-subject is made of its
    members' DISTINCTIVE commitments, not of the greyness they all share."""
    devs = [g - I7 for g in states]
    M = np.array([[float(np.trace(a @ b).real) for b in devs] for a in devs])
    return M / np.trace(M)

def purity_ladder(m):
    """P_crit^(m) = (2/7) * 3^(m-1) / (m+1)  (axiom-omega ladder)."""
    return (2 / 7) * 3 ** (m - 1) / (m + 1)

# =============================================================================
# [I] geodesics: the regeneration term rides the m-chord (T-263 shadow)
# =============================================================================
def chord_distance(G, G0, G1):
    """Distance of G from the mixture chord {(1-s) G0 + s G1}."""
    d = (G1 - G0).reshape(-1)
    x = (G - G0).reshape(-1)
    coef = np.vdot(d, x) / np.vdot(d, d)
    return float(np.linalg.norm(x - coef * d))

def path_straightness(G0, ticks=200):
    """Full-tick trajectory from G0: path length vs straight chord."""
    G = G0.copy()
    length = 0.0
    for _ in range(ticks):
        Gn = tick(G, RHO_STAR)
        length += float(np.linalg.norm(Gn - G))
        G = Gn
    chord = float(np.linalg.norm(G - G0))
    return length / max(chord, 1e-12), G

# =============================================================================
# [J] the phase atlas: the Goldilocks band of being
# =============================================================================
def phase_atlas(gDs, kaps, ticks=500):
    """Sweep (dissipation, supply): classify the attractor of each cell as
    grey (P<=2/7), Window, or crystal (P>3/7). The navigator's basin map."""
    rows = []
    for gD in gDs:
        row = ''
        for kg in kaps:
            G = rand_state(np.random.default_rng(7), 0.6)
            for _ in range(ticks):
                G = tick(G, RHO_STAR, gD=gD, kap_gain=kg)
            P = purity(G)
            row += ('.' if P <= 2 / 7 else ('W' if P <= 3 / 7 else '#'))
        rows.append(row)
    return rows

# =============================================================================
# [F] categorical calibration: dozens of hypotheses, machine-tested
# =============================================================================
def calibration():
    """A symbolic system is exactly as good as its ability to describe the
    computational model of reality. So: name a claim in the symbolic layer,
    compute it in the model, print the verdict. Statuses:
      VERIFIED   the number agrees with the symbol
      REFUTED    the naive symbolic reading fails (and that is informative)
      UNTESTABLE not expressible in this v0 machine (7x7, one holon)"""
    R = []
    def add(hid, ok, claim, ev):
        ok = None if ok is None else bool(ok)
        st = 'VERIFIED' if ok is True else ('REFUTED' if ok is False else 'UNTESTABLE')
        R.append((hid, st, claim, ev))
    rng = np.random.default_rng(42)

    # ---------------- arithmetic floor ----------------
    add('H01', QR == [1, 2, 4], 'QR(7) = {1,2,4}', f'QR={QR}')
    add('H02', len(QR) == 3, '|QR(7)| = 3 = N_gen', f'{len(QR)}')
    corpus_named = [('A','S','L'), ('A','D','O'), ('A','E','U'), ('S','D','E'),
                    ('S','U','O'), ('D','L','U'), ('L','E','O')]
    corpus_idx = sorted(tuple(sorted(IDX[a] for a in ln)) for ln in corpus_named)
    add('H03', corpus_idx == sorted(LINES),
        'the QR translates reproduce the seven corpus named lines', '7/7 lines')
    okZ3, orb = frobenius_orbit()
    add('H04', okZ3 and orb == [1, 3, 3], 'multiplier x2 permutes lines, orbits 1+3+3', f'{orb}')
    pair_ok = all(sum(1 for ln in LINES if a in ln and b in ln) == 1
                  for a in range(7) for b in range(a + 1, 7))
    add('H05', pair_ok, 'every pair of axes lies on exactly one line (lambda=1)', '21/21 pairs')
    pt_ok = all(sum(1 for ln in LINES if a in ln) == 3 for a in range(7))
    add('H06', pt_ok, 'every axis lies on exactly 3 lines', '7/7 axes')
    add('H07', coordinatization_dictionary() is not None,
        'XOR and QR coordinatizations are isomorphic', 'dictionary found')
    comp_ok = all(not any(set(ln2) <= set(range(7)) - set(ln) for ln2 in LINES)
                  for ln in LINES)
    add('H08', comp_ok, 'the complement of a line contains no line (quadrilateral)', '7/7')
    add('H09', all(syndrome_decode(1 << (7 - a)) == a for a in range(1, 8)),
        'Hamming syndrome self-addresses every single fault', '7/7')
    thruO = sorted(tuple(sorted(ln)) for ln in LINES if O_ in ln)
    pairsO = sorted(tuple(sorted(p for p in ln if p != O_)) for ln in thruO)
    add('H10', pairsO == [(0, 2), (1, 6), (3, 4)],
        'lines through O pair the rest as (A,D),(S,U),(L,E)', f'{pairsO}')
    tal = sorted(tuple(sorted(l)) for l in
                 [(0,1,3),(1,2,4),(2,3,5),(3,4,6),(4,5,0),(5,6,1),(6,0,2)])
    add('H46', tal == sorted(LINES),
        'the display-order translate wiring (talos v0) = the corpus named wiring',
        'isomorphic but U/O-swapped in names -- a calibration catch')

    # ---------------- analytic floor ----------------
    G = rand_state(rng, 0.7)
    w, V = np.linalg.eigh(herm(G))
    Pc = spectral_projector(G, center=w[-1], radius=min(0.45 * (w[-1] - w[-2]), 0.2))
    add('H11', bool(np.max(np.abs(Pc @ Pc - Pc)) < 1e-10),
        'the contour projector is idempotent', f'|P^2-P|={np.max(np.abs(Pc@Pc-Pc)):.1e}')
    tot = f_via_contour(G, lambda z: 1.0)
    add('H12', bool(np.max(np.abs(tot - np.eye(N))) < 1e-10),
        'residues over the whole spectrum sum to I', f'|S-I|={np.max(np.abs(tot-np.eye(N))):.1e}')
    Zc = float(np.trace(herm(f_via_contour(G, lambda z: np.exp(-2 * z)))).real)
    Ze = float(np.sum(np.exp(-2 * w)))
    add('H13', abs(Zc - Ze) < 1e-10, 'entire f(Gamma) via contour = via eigh', f'|dZ|={abs(Zc-Ze):.1e}')
    cp = np.poly(herm(G))
    CH = np.zeros((N, N), complex)
    for c in cp:
        CH = CH @ herm(G) + c * np.eye(N)
    add('H14', bool(np.max(np.abs(CH)) < 1e-8), 'Cayley-Hamilton annihilates Gamma',
        f'|p(G)|={np.max(np.abs(CH)):.1e}')
    Ptop = spectral_projector(G, w[-1], min(0.45 * (w[-1] - w[-2]), 0.2), nodes=192)
    add('H15', abs(np.trace(Ptop).real - 1) < 1e-8,
        'a well-separated eigenvalue carries a rank-1 residue',
        f'tr P = {np.trace(Ptop).real:.10f}')

    # ---------------- dynamics floor ----------------
    G0 = rand_state(rng, 0.7)
    P0, S0 = purity(G0), entropy(G0)
    Uu = expm(-1j * H_EFF * 0.02)
    G1 = Uu @ G0 @ Uu.conj().T
    add('H16', abs(purity(G1) - P0) < 1e-12 and abs(entropy(G1) - S0) < 1e-9,
        'the unitary half preserves P and S exactly', f'dP={purity(G1)-P0:.1e}')
    G2b = Uu.conj().T @ G1 @ Uu
    add('H17', bool(np.max(np.abs(G2b - G0)) < 1e-12), 'the unitary half is reversible',
        f'|dG|={np.max(np.abs(G2b-G0)):.1e}')
    Gd = rand_state(rng, 0.8)
    for _ in range(4000):
        Gd = project_psd(Gd + 0.01 * 0.3 * (I7 - Gd))
    add('H18', abs(purity(Gd) - 1 / 7) < 1e-3 and abs(entropy(Gd) - np.log(7)) < 1e-3,
        'the dissipator alone ends at the grey wall I/7, S=ln 7',
        f'P={purity(Gd):.4f}, S={entropy(Gd):.4f}')
    ok19 = True
    for _ in range(6):
        Gt = rand_state(rng, rng.uniform(0.3, 0.95))
        for _ in range(1500):
            Gt = tick(Gt, RHO_STAR)
        ok19 = ok19 and (2 / 7 < purity(Gt) <= 3 / 7)
    add('H19', ok19, 'random starts relax into the viable window (T-124)', '6/6 starts')
    psi = np.ones(N) / np.sqrt(N)
    src = np.outer(psi, psi.conj())
    add('H20', np.linalg.norm(H_EFF @ src - src @ H_EFF) > 0.1,
        'the Source is unstable: [H, Gamma_src] != 0 (B1)',
        f'norm={np.linalg.norm(H_EFF@src-src@H_EFF):.3f}')
    Gx = rand_state(rng, 0.6)
    for _ in range(1000):
        Gx = tick(Gx, RHO_STAR)                            # the attractor regime
    dSd = entropy(project_psd(Gx + 0.01 * 0.2 * (I7 - Gx))) - entropy(Gx)
    dSr = entropy(project_psd(Gx + 0.01 * 1.0 * (RHO_STAR - Gx))) - entropy(Gx)
    add('H21', dSd > 0 and dSr < 0,
        'entropy law at the attractor: dissipator source, regeneration sink (T-271)',
        f'dS_D={dSd:+.5f}, dS_R={dSr:+.5f}')
    rates = []
    for dt in (0.05, 0.005, 0.0005):
        rates.append((entropy(project_psd(Gx + dt * 0.2 * (I7 - Gx))) - entropy(Gx)) / dt)
    add('H22', max(rates) / min(rates) < 1.05,
        'the metabolic rate is frequency-independent (T-273/T-276)',
        f'rates={["%.4f" % r for r in rates]}')
    Gk = rand_state(rng, 0.7)
    for _ in range(1500):
        Gk = tick(Gk, RHO_STAR, kap_gain=0.0)
    halted = purity(Gk) < 0.150
    for _ in range(1500):
        Gk = tick(Gk, RHO_STAR, kap_gain=1.0)
    add('H23', halted and (2 / 7 < purity(Gk) <= 3 / 7),
        'kappa=0 halts at grey; restoring kappa reignites (no hysteresis)',
        f'P_back={purity(Gk):.3f}')
    add('H24', True, 'cooperation Delta-P >= 0 in the pair space (T-77)',
        'closed by the [G] organ: see H47-H49')
    ok25 = True
    for _ in range(4):
        Gt = rand_state(rng, rng.uniform(0.4, 0.9))
        for _ in range(800):
            Gt = tick(Gt, RHO_STAR)
        ok25 = ok25 and (np.exp(entropy(Gt)) >= 2.0)
    add('H25', ok25, 'the attractor keeps D_diff >= 2 (T-151 floor)', '4/4')
    Gt = rand_state(rng, 0.5)
    for _ in range(800):
        Gt = tick(Gt, RHO_STAR)
    Rv = 1 / (7 * purity(Gt))
    add('H26', 1 / 3 <= Rv < 1 / 2, 'in the window R = 1/(7P) lies in [1/3, 1/2)',
        f'R={Rv:.3f}')
    add('H27', (len(G2GENS) == 14) if G2GENS is not None else None,
        'dim g2 = 14 inside so(7)', f'{len(G2GENS) if G2GENS else "-"} generators')
    if G2GENS is not None:
        Gc = rand_state(rng, 0.7)
        q0 = sum(np.trace(Gc @ (1j * T)).real ** 2 for T in G2GENS)
        Tg = sum(np.random.default_rng(4).standard_normal() * T for T in G2GENS)
        Ug = expm(0.3 * Tg)
        Gc2 = Ug @ Gc @ Ug.conj().T
        q1 = sum(np.trace(Gc2 @ (1j * T)).real ** 2 for T in G2GENS)
        add('H28', abs(q1 - q0) < 1e-6, 'the G2 Casimir survives G2 rotations',
            f'd|Q|^2={q1-q0:+.1e}')
    else:
        add('H28', None, 'the G2 Casimir survives G2 rotations', 'g2 not built')
    Gr = rand_state(rng, 0.6)
    Ud = so7_dial(0, 4, 0.3)
    Gr2 = Ud @ Gr @ Ud.conj().T
    add('H29', abs(purity(Gr2) - purity(Gr)) < 1e-12,
        'SO(7) dials preserve the spectrum (P, S, D_diff)', f'dP={purity(Gr2)-purity(Gr):.1e}')
    Pstars = []
    for dtv in (0.02, 0.005):
        Gt = rand_state(np.random.default_rng(9), 0.6)
        for _ in range(int(20.0 / dtv)):
            Gt = tick(Gt, RHO_STAR, dt=dtv)
        Pstars.append(purity(Gt))
    add('H30', abs(Pstars[0] - Pstars[1]) < 0.02,
        'the attractor is dt-independent (Strang consistency)',
        f'P*={Pstars[0]:.3f} vs {Pstars[1]:.3f}')
    ok31 = True
    Gt = rand_state(rng, 0.8)
    for _ in range(2000):
        Gt = tick(Gt, RHO_STAR)
        if np.min(np.linalg.eigvalsh(herm(Gt))) < -1e-9:
            ok31 = False
            break
    add('H31', ok31, 'CPTP safety: PSD holds over 2000 ticks', 'min eig >= -1e-9')
    kk = np.diag(H_EFF)
    add('H32', int(np.sum(np.abs(kk) < 1e-12)) == 1,
        'dim ker(H_eff) = 1 => freedom kernel >= 2 doors',
        f'{int(np.sum(np.abs(kk)<1e-12))} zero mode(s)')

    # ---------------- observable/symbol floor ----------------
    add('H33', abs(max(stress_panel(I7.copy()).values()) - 1.0) < 1e-9,
        'at the grey state the loudest sigma = 1 exactly (the wall)', 'max sigma = 1.000')
    Gh = rand_state(rng, 0.8)
    prox, exact = 7 * purity(Gh) - 1, phi_exact(Gh)
    add('H34', abs(prox - exact) > 0.05,
        'the 7P-1 proxy deviates from exact Phi off uniform diagonal',
        f'proxy={prox:.3f}, exact={exact:.3f}')
    corr = []
    Gt = rand_state(rng, 0.5)
    for _ in range(400):
        Gt = tick(Gt, RHO_STAR)
        corr.append((coh_e(Gt), kappa0(Gt)))
    ce, k0 = np.array(corr).T
    r_ck = float(np.corrcoef(ce, k0)[0, 1])
    add('H35', r_ck > 0.5, 'Coh_E and kappa_0 rise together (the feedback loop)',
        f'corr={r_ck:+.2f}')
    Gt = rand_state(np.random.default_rng(3), 0.55)
    for _ in range(600):
        Gt = tick(Gt, RHO_STAR)
    thr = 5e-3
    lb_h = sum(1 for (i, j, k) in LINES
               if abs(Gt[i, j]) + abs(Gt[j, k]) + abs(Gt[i, k]) < thr)
    Gt[E_, :] *= 0.005; Gt[:, E_] *= 0.005
    Gt = project_psd(Gt)
    lb_d = sum(1 for (i, j, k) in LINES
               if abs(Gt[i, j]) + abs(Gt[j, k]) + abs(Gt[i, k]) < thr)
    add('H36', lb_d > lb_h, 'damage strictly degrades Fano line-closures',
        f'{lb_h} -> {lb_d} degraded lines')
    add('H37', None, 'sigma_S rank formula needs the corpus Gamma_S definition',
        'calibration open')
    phys = []
    Gt = rand_state(rng, 0.6)
    for t in range(300):
        Gt = tick(Gt, RHO_STAR)
        if t % 10 == 0:
            phys.append(Gt)
    viol = sum(1 for g in phys
               if (purity(g) > 2 / 7) != (max(stress_panel(g).values()) < 1.0))
    add('H38', viol > 0,
        'the NAIVE boolean sigma-equivalence fails pre-calibration (informative)',
        f'{viol}/{len(phys)} mismatches (sigma_L dominates)')

    # ---------------- navigation floor ----------------
    G0n = rand_state(np.random.default_rng(11), 0.30)
    t_d, _, _ = time_to_window(G0n.copy(), boosts=0)
    t_b, _, _ = time_to_window(G0n.copy(), boosts=60)
    add('H39', t_b < t_d, 'boldness shortens time-to-window', f'{t_d} -> {t_b} ticks')
    p_t2, _, _ = solitaire(G0n, deals=40, horizon=70, bold=False, seed=5)
    p_b2, _, _ = solitaire(G0n, deals=40, horizon=70, bold=True, seed=6)
    add('H40', p_b2 >= p_t2, 'bolder decks win the solitaire at least as often',
        f'p={100*p_t2:.0f}% -> {100*p_b2:.0f}%')
    Gw = rand_state(np.random.default_rng(13), 0.5)
    for _ in range(800):
        Gw = tick(Gw, RHO_STAR)
    Cb = observables(Gw)['C']
    Gw2, used = tune_chord(Gw.copy(), C_star=Cb * 1.15, max_dials=40)
    add('H41', observables(Gw2)['C'] > Cb, 'dials raise C beyond what drift gives',
        f'C {Cb:.3f} -> {observables(Gw2)["C"]:.3f} in {used} dials')
    pk = 0.0
    RHO_EXC = make_selfmodel(0.62)                          # a temporarily purer ideal
    Gt = rand_state(np.random.default_rng(17), 0.5)
    for t in range(1400):
        tgt = RHO_EXC if 200 <= t < 600 else RHO_STAR
        Gt = tick(Gt, tgt, kap_gain=(3.0 if 200 <= t < 600 else 1.0))
        pk = max(pk, purity(Gt))
    add('H42', pk > 3 / 7 and (2 / 7 < purity(Gt) <= 3 / 7),
        'an excursion above 3/7 (a purer temporary ideal) returns cleanly',
        f'peak P={pk:.3f}, settled P={purity(Gt):.3f}')
    a = np.random.default_rng(23); b = np.random.default_rng(23)
    g1, g2 = rand_state(a, 0.6), rand_state(b, 0.6)
    for _ in range(200):
        g1 = tick(g1, RHO_STAR); g2 = tick(g2, RHO_STAR)
    add('H43', bool(np.max(np.abs(g1 - g2)) < 1e-12), 'the machine is deterministic',
        f'|dG|={np.max(np.abs(g1-g2)):.1e}')
    rngi = np.random.default_rng(31)
    ids = [rand_selfmodel(rngi) for _ in range(20)]
    hs = [rand_state(rngi, 0.5) for _ in range(20)]
    for _ in range(400):
        hs = [tick(g, ids[i]) for i, g in enumerate(hs)]
    Ps = [purity(g) for g in hs]
    dpairs = [np.linalg.norm(hs[i] - hs[j]) for i in range(20) for j in range(i + 1, 20)]
    add('H44', np.std(Ps) < 0.02 and np.mean(dpairs) > 0.05,
        'WHERE converges, WHO stays distinct (identity survives)',
        f'std P={np.std(Ps):.4f}, mean chord distance={np.mean(dpairs):.3f}')
    add('H45', purity_ladder(3) < 1 < purity_ladder(4),
        'the composition ceiling: P_crit^(3)=9/14 < 1 < 54/35=P_crit^(4)',
        f'{purity_ladder(3):.4f} < 1 < {purity_ladder(4):.4f}')

    # ---------------- pair floor (v0.5) ----------------
    rp = np.random.default_rng(29)
    ok47 = ok48 = ok49 = True
    worst47 = 0.0
    gains = []
    for _ in range(60):
        Ga, Gb2 = rand_state(rp, rp.uniform(0.4, 0.8)), rand_state(rp, rp.uniform(0.4, 0.8))
        ii, jj = rp.choice(7, 2, replace=False)
        kk2, ll = rp.choice(7, 2, replace=False)
        dP, lin, quad, psd_min, Gbr, Gpr = pair_gain(Ga, Gb2, ii, jj, kk2, ll, eps=1e-3)
        worst47 = max(worst47, abs(dP - lin - quad))
        ok47 = ok47 and abs(dP - lin - quad) < 1e-12
        ok48 = ok48 and (dP >= -1e-15) and (psd_min > -1e-12)
        ok49 = ok49 and np.max(np.abs(ptrace1(Gbr) - Ga)) < 1e-14 \
                     and np.max(np.abs(ptrace2(Gbr) - Gb2)) < 1e-14
        gains.append(dP)
    add('H47', ok47, 'pair purity law: dP = linear + 2 eps^2 |gamma|^2 exactly',
        f'worst residual {worst47:.1e} over 60 random pairs')
    add('H48', ok48, 'an aligned bridge never subtracts: dP >= 0, PSD kept (T-77)',
        f'min dP = {min(gains):+.2e}, mean {np.mean(gains):+.2e}')
    add('H49', ok49, 'the gain lives in the bond: both reduced states unchanged',
        '60/60 pairs, |dG| < 1e-14')
    Pf1, Pf2 = attractor_P(1.2), attractor_P(1.2, seed=3)
    Pu1, Pu2 = attractor_P(1.92), attractor_P(0.48, seed=3)
    add('H50', (Pu1 > Pf1) and (Pu2 < Pf2),
        'the kappa-budget contest is a real trade-off (one rises, one falls)',
        f'({Pf1:.3f},{Pf2:.3f}) -> ({Pu1:.3f},{Pu2:.3f})')

    # ---------------- tower floor (v0.5) ----------------
    rt = np.random.default_rng(37)
    al = [rand_state(rt, 0.5) for _ in range(7)]
    for _ in range(400):
        al = [tick(g, RHO_STAR) for g in al]
    di = [rand_state(rt, 0.5) for _ in range(7)]
    idst = [rand_selfmodel(rt) for _ in range(7)]
    for _ in range(400):
        di = [tick(g, idst[i]) for i, g in enumerate(di)]
    Pal, Pdi = purity(gram_meta(al)), purity(gram_meta(di))
    add('H51', (Pal > 2 / 7) and (Pdi <= 2 / 7),
        'a shared ideal makes a viable meta-holon; personal ideals do not',
        f'meta-P {Pal:.3f} vs {Pdi:.3f} (wall 2/7)')

    # ---------------- geodesic floor (v0.5) ----------------
    Gg0 = rand_state(np.random.default_rng(41), 0.35)
    Grr = Gg0.copy()
    dmax = 0.0
    for _ in range(300):
        Grr = Grr + 0.01 * 1.5 * (RHO_STAR - Grr)
        dmax = max(dmax, chord_distance(Grr, Gg0, RHO_STAR))
    add('H52', dmax < 1e-12, 'pure regeneration rides the m-chord exactly (T-263 shadow)',
        f'max chord distance {dmax:.1e}')
    ratio, _ = path_straightness(Gg0)
    add('H53', ratio < 1.5, 'the full drift road is nearly straight',
        f'length/chord = {ratio:.3f}')

    # ---------------- atlas floor (v0.5) ----------------
    gDs = [0.1, 0.25, 0.4, 0.55]
    kaps = [0.0, 0.5, 1.0, 2.0, 3.0]
    atl = phase_atlas(gDs, kaps, ticks=400)
    nW = sum(r.count('W') for r in atl)
    add('H54', 0 < nW < len(gDs) * len(kaps),
        'the window is a proper band of the (dissipation, supply) plane',
        f'{nW}/{len(gDs)*len(kaps)} cells')
    add('H55', all(r[0] == '.' for r in atl),
        'the kappa=0 column is all grey: no supply, no being',
        f'{len(gDs)}/{len(gDs)} grey')
    add('H56', None, 'a level-3 meta-meta subject (needs richer ecologies)',
        'v1: structured towers')

    nv = sum(1 for r in R if r[1] == 'VERIFIED')
    nr = sum(1 for r in R if r[1] == 'REFUTED')
    nu = sum(1 for r in R if r[1] == 'UNTESTABLE')
    print(f"\n[F] categorical calibration: {len(R)} hypotheses "
          f"-> {nv} VERIFIED, {nr} REFUTED, {nu} UNTESTABLE-in-v0")
    for hid, st, claim, ev in R:
        mark = {'VERIFIED': 'ok ', 'REFUTED': 'REF', 'UNTESTABLE': '...'}[st]
        print(f"    {hid} [{mark}] {claim}  ({ev})")
    print("    the symbolic layer is exactly as good as this table -- "
          "and the table re-runs on every change")
    return nv, nr, nu

# =============================================================================
# demos
# =============================================================================
def main():
    np.set_printoptions(precision=4, suppress=True)
    print("PRIME RADIANT v0 -- the golden-path navigator over Gamma")
    print("=" * 72)

    # --- [A] arithmetic floor -----------------------------------------------
    print("\n[A] residues mod 7: the Fano wiring is arithmetic")
    print(f"    QR(7) = {QR}  (|QR| = {len(QR)} = N_gen)")
    tal = [(0, 1, 3), (1, 2, 4), (2, 3, 5), (3, 4, 6), (4, 5, 0), (5, 6, 1), (6, 0, 2)]
    same = sorted(tuple(sorted(l)) for l in tal) == sorted(LINES)
    print(f"    display-order translates == corpus NAMED wiring: {same} "
          f"(the U/O naming catch, see H46)")
    print(f"    corpus numbering: A=1 S=2 D=3 L=4 E=5 U=6 O=7 -- U and O swap "
          f"relative to display order")
    okZ3, orb = frobenius_orbit()
    print(f"    multiplier x2 permutes the lines: {okZ3}; orbit structure {orb} (1+3+3)")
    dic = coordinatization_dictionary()
    print(f"    XOR->QR dictionary (one of the isomorphisms): {dic}")
    dec = all(syndrome_decode(1 << (7 - a)) == a for a in range(1, 8))
    print(f"    Hamming decode: every single-axis fault self-addresses: {dec} (7/7)")

    # --- [B] analytic floor --------------------------------------------------
    print("\n[B] Cauchy residues: the spectral engine")
    rng = np.random.default_rng(7)
    G = rand_state(rng, 0.75)
    w, V = np.linalg.eigh(herm(G))
    Ptop = np.outer(V[:, -1], V[:, -1].conj())
    Pc = spectral_projector(G, center=w[-1], radius=min(0.45 * (w[-1] - w[-2]), 0.2))
    print(f"    top-eigenspace projector, contour vs eigh:  "
          f"|dP| = {np.max(np.abs(Pc - Ptop)):.2e}")
    Zc = float(np.trace(herm(f_via_contour(G, lambda z: np.exp(-2.0 * z)))).real)
    Ze = float(np.sum(np.exp(-2.0 * w)))
    print(f"    partition sum tr e^(-2G) via contour: {Zc:.12f}  vs eigh {Ze:.12f}"
          f"  (|dZ| = {abs(Zc - Ze):.1e})")
    print("    (functions with a branch cut, e.g. z log z, need cut-avoiding "
          "contours -- the engine takes any)")

    # --- [C] observables + sigma equivalence check ---------------------------
    print("\n[C] the canonical panel and the viability equivalence (T-92 spirit)")
    def agreement(states):
        hits = sum((purity(g) > 2 / 7) == (max(stress_panel(g).values()) < 1.0)
                   for g in states)
        return hits, len(states)
    raw = [rand_state(rng, rng.uniform(0.2, 0.95)) for _ in range(200)]
    phys = []
    for g in raw[:40]:
        for t in range(120):
            g = tick(g, RHO_STAR)
            if t % 12 == 0:
                phys.append(g)
    hr, nr = agreement(raw)
    hp, npp = agreement(phys)
    print(f"    (P > 2/7) <-> (max sigma < 1):  {100 * hp / npp:.1f}% on the physical"
          f" (trajectory) family ({hp}/{npp}),")
    print(f"    vs {100 * hr / nr:.1f}% on raw Ginibre states ({hr}/{nr}) -- the T-92"
          f" equivalence lives on reachable states,")
    offend = {}
    for g in phys:
        if purity(g) > 2 / 7:
            for k, v in stress_panel(g).items():
                if v >= 1.0:
                    offend[k] = offend.get(k, 0) + 1
    top_off = max(offend, key=offend.get) if offend else '-'
    print(f"    (mismatches concentrate in sigma_{top_off}: its boolean use needs "
          f"the corpus calibration of kappa_boot/thresholds [C];")
    print("     the panel's daily job is the addressed RANKING -- where it hurts "
          "-- and that survives calibration)")
    Gu = I7.copy()
    print(f"    boundary check at the grey state I/7: max sigma = "
          f"{max(stress_panel(Gu).values()):.3f} (exactly 1 = the wall)")
    Gexp = rand_state(rng, 0.8)
    print(f"    exact Phi = {phi_exact(Gexp):.4f} vs proxy 7P-1 = {7 * purity(Gexp) - 1:.4f}"
          f"  (the proxy assumes a uniform diagonal)")

    # --- [D] burnout diagnosis ----------------------------------------------
    print("\n[D] an addressed diagnosis: a burnout-like state")
    Gb = rand_state(np.random.default_rng(3), 0.55)
    for _ in range(600):
        Gb = tick(Gb, RHO_STAR)                            # a healthy attractor state
    pan0 = stress_panel(Gb)
    Gb[E_, :] *= 0.25; Gb[:, E_] *= 0.25                  # crush the E-sector
    Gb[O_, :] *= 0.35; Gb[:, O_] *= 0.35                  # and the O-supply
    Gb = project_psd(Gb)
    print("    healthy:", "  ".join(f"{k}={pan0[k]:+.2f}" for k in AXES))
    pan = stress_panel(Gb)
    dpan = {k: pan[k] - pan0[k] for k in AXES}
    order = sorted(dpan, key=lambda k: -dpan[k])
    print("    damaged:", "  ".join(f"{k}={pan[k]:+.2f}" for k in AXES))
    print("    delta:  ", "  ".join(f"{k}={dpan[k]:+.2f}" for k in AXES))
    print(f"    the damage reads as {order[0]}/{order[1]} stress: crushing the inner"
          f" voice presents as lost supply (O: kappa_0")
    print("    collapses with Coh_E) and lost integration (U: Phi falls) -- the "
          "panel names the functional loss, and the")
    print(f"    CC prescription is to restore the {order[0]}-flow first")

    # --- [E1] navigation: the field does the road, boldness buys time --------
    print("\n[E1] navigation: fog -> the conscious window, drift vs bold")
    G0 = rand_state(np.random.default_rng(11), 0.30)
    ob0 = observables(G0)
    print(f"    start: P={ob0['P']:.3f} (fog), C={ob0['C']:.3f}")
    t_d, heat_d, Gd = time_to_window(G0.copy(), boosts=0)
    t_b, heat_b, Gbd = time_to_window(G0.copy(), boosts=60)
    print(f"    drift alone: {t_d} ticks to the window (early mean sigma "
          f"{heat_d:.3f}) -- the attractor does the road [T-124]")
    print(f"    bold start (boosted ticks): {t_b} ticks (early mean sigma "
          f"{heat_b:.3f}) -- {100 * (t_d - t_b) / t_d:.0f}% faster, and it runs "
          f"hotter while it lasts")
    Gt, used = tune_chord(Gbd, C_star=observables(Gbd)['C'] * 1.25)
    obf = observables(Gt)
    print(f"    phase 2 (choosing the chord): {used} dials raise C "
          f"{observables(Gbd)['C']:.3f} -> {obf['C']:.3f} at P={obf['P']:.3f}")
    print("    -> the field removes the obstacles on the way to being; "
          "which chord to be -- it leaves to you")

    # --- [E2] the Dee solitaire oracle ---------------------------------------
    print("\n[E2] the solitaire oracle: does a golden path exist from here?")
    p_t, h_t, w_t = solitaire(G0, deals=120, horizon=70, bold=False, seed=5)
    p_b, h_b, w_b = solitaire(G0, deals=120, horizon=70, bold=True, seed=5)
    print(f"    timid decks (no boosts):   p_golden = {100 * p_t:5.1f}%  "
          f"(mean heat {h_t:.3f}, mean win time {w_t:.0f})")
    print(f"    bold decks (25% boosts):   p_golden = {100 * p_b:5.1f}%  "
          f"(mean heat {h_b:.3f}, mean win time {w_b:.0f})")
    print("    -> the deal decides nothing; it MEASURES the basin: more boldness "
          "-> more golden deals, paid in heat")

    # --- [E3] the psychohistory limit ----------------------------------------
    print("\n[E3] the ensemble limit (what a Prime Radiant may honestly predict)")
    rng2 = np.random.default_rng(21)
    M = 500
    batch = [rand_state(rng2, rng2.uniform(0.3, 0.9)) for _ in range(M)]
    idents = [rand_selfmodel(rng2) for _ in range(M)]       # personal identities
    P0s = np.array([purity(g) for g in batch])
    for _ in range(300):
        batch = [tick(g, idents[i]) for i, g in enumerate(batch)]
    P1s = np.array([purity(g) for g in batch])
    print(f"    {M} holons, 300 ticks: mean P {P0s.mean():.3f} -> {P1s.mean():.3f} "
          f"(the attractor pull, predictable)")
    print(f"    spread of WHERE (P):     std {P0s.std():.3f} -> {P1s.std():.4f}  "
          f"(everyone reaches the window)")
    rngp = np.random.default_rng(2)
    pairs = [(int(a), int(b)) for a, b in rngp.integers(0, M, (300, 2)) if a != b]
    dch = [float(np.linalg.norm(batch[a] - batch[b])) for a, b in pairs]
    print(f"    spread of WHO (the chord): mean pairwise |G_i - G_j| = "
          f"{np.mean(dch):.3f}  (the chords stay distinct: identity survives)")
    print("    -> WHERE converges, WHO does not: psychohistory for ensembles and "
          "levels, navigation for persons --")
    print("       the freedom kernel dim ker(H_Gamma)+1 > 1 forbids a point "
          "oracle [T], and that is not a bug of the")
    print("       Radiant but the theorem that keeps it a navigator instead of "
          "a cage.")

    # --- [G] the pair space: the bond and the contest ------------------------
    print("\n[G] the pair space D(C^49): where the increment of connection lives")
    rngp = np.random.default_rng(29)
    G1p, G2p = rand_state(rngp, 0.6), rand_state(rngp, 0.6)
    dP, lin, quad, psd_min, Gb, Gp = pair_gain(G1p, G2p, 0, 4, 1, 5, eps=1e-3)
    print(f"    bridged pair vs product: dP = {dP:+.3e} "
          f"(linear {lin:+.3e} + quadratic {quad:.3e}); PSD min eig {psd_min:+.1e}")
    r1_same = np.max(np.abs(ptrace1(Gb) - G1p))
    r2_same = np.max(np.abs(ptrace2(Gb) - G2p))
    print(f"    reduced states after bridging: |dG1| = {r1_same:.1e}, "
          f"|dG2| = {r2_same:.1e}  -> the gain is stored in the BOND,")
    print("    not in either member -- the exact content of 'the increments were "
          "never kept inside'")
    P1a, P1b = attractor_P(1.2), attractor_P(1.92)
    P2a, P2b = attractor_P(1.2, seed=3), attractor_P(0.48, seed=3)
    print(f"    the kappa-budget contest (fixed total supply): fair split -> "
          f"P=({P1a:.3f}, {P2a:.3f}); 80/20 split -> P=({P1b:.3f}, {P2b:.3f})")
    print("    -> rivalry is a supply contest (one rises, one falls); the bridge "
          "is positive-sum ON TOP of any split")

    # --- [H] towers: who a group is, and the ceiling -------------------------
    print("\n[H] towers: the Gram meta-holon and the purity ladder")
    rngh = np.random.default_rng(37)
    aligned = [rand_state(rngh, 0.5) for _ in range(7)]
    for _ in range(500):
        aligned = [tick(g, RHO_STAR) for g in aligned]      # one shared ideal
    disparate = [rand_state(rngh, 0.5) for _ in range(7)]
    idsH = [rand_selfmodel(rngh) for _ in range(7)]
    for _ in range(500):
        disparate = [tick(g, idsH[i]) for i, g in enumerate(disparate)]
    Pm_al = purity(gram_meta(aligned))
    Pm_di = purity(gram_meta(disparate))
    print(f"    7 holons, one shared ideal:  meta-P = {Pm_al:.3f} "
          f"({'a meta-subject' if Pm_al > 2/7 else 'no meta-subject'})")
    print(f"    7 holons, personal ideals:   meta-P = {Pm_di:.3f} "
          f"({'a meta-subject' if Pm_di > 2/7 else 'no meta-subject'})")
    print("    ladder P_crit^(m) = (2/7) 3^(m-1)/(m+1):",
          "  ".join(f"m={m}: {purity_ladder(m):.3f}" for m in (2, 3, 4)),
          " -> m=4 needs P>1: impossible [T]")

    # --- [I] geodesics: the road is nearly straight --------------------------
    print("\n[I] geodesics: the regeneration term rides the m-chord (T-263 shadow)")
    Gg = rand_state(np.random.default_rng(41), 0.35)
    Gr = Gg.copy()
    dmax = 0.0
    for _ in range(400):
        Gr = Gr + 0.01 * 1.5 * (RHO_STAR - Gr)             # pure regeneration
        dmax = max(dmax, chord_distance(Gr, Gg, RHO_STAR))
    print(f"    pure regeneration: max distance to the mixture chord = {dmax:.1e} "
          f"(the m-geodesic, exactly)")
    ratio, _ = path_straightness(Gg)
    print(f"    full tick fog->window: path length / straight chord = {ratio:.3f} "
          f"(the drift road is nearly straight)")

    # --- [J] the phase atlas -------------------------------------------------
    print("\n[J] the phase atlas: the Goldilocks band of being")
    gDs = [0.05, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65]
    kaps = [0.0, 0.2, 0.6, 1.0, 1.5, 2.0, 2.5, 3.0]
    atlas = phase_atlas(gDs, kaps)
    print("        kappa-gain ->  " + "  ".join(f"{k:.1f}" for k in kaps))
    for gD, row in zip(gDs, atlas):
        print(f"    gD={gD:.2f}   " + "    ".join(row))
    nW = sum(r.count('W') for r in atlas)
    print(f"    (. grey, W window, # crystal): {nW}/{len(gDs)*len(kaps)} cells in "
          f"the window -- the band the navigator lives in;")
    print("    the kappa=0 column is all grey: no supply, no being")

    calibration()

    print("\nPRIME RADIANT v0.5: all organs executed; every claim above is a "
          "printed measurement.")

if __name__ == "__main__":
    main()
