# -*- coding: utf-8 -*-
"""symbolica_frame_bundle.py — is a GLOBAL calibration even possible?

§82 identified 'calibration' (which quale is red) with the G2-FRAME — the within-
orbit representative the phenomenal functor F is blind to — and CONJECTURED it is
fixed by external boundary data. This lab strengthens that conjecture toward
necessity by a rigorous, computed obstruction:

  A global intrinsic calibration = a continuous G2-equivariant choice of frame
  across ALL of D(C^7) = a global section (slice) of the orbit map.
  Such a global slice exists only if the G2-action has a SINGLE orbit type.
  We COMPUTE the orbit dimension at several Γ and show it VARIES (0 at the centre,
  maximal at generic Γ). Varying isotropy ⟹ the quotient D(C^7)/G2 is STRATIFIED,
  the orbit map is NOT a fibre bundle, and NO global slice exists.
  ⟹ there is no global intrinsic calibration; calibration is necessarily LOCAL —
  fixed pointwise, by whatever data the configuration is embedded in. This upgrades
  §82's 'external fixes it' from bare conjecture to 'SOMETHING local must, because
  nothing global can'.

Method (all first-principles, verifiable):
  1. Build the octonion Fano 3-form φ from the QR(7) difference set {1,2,4}.
  2. g2 = { X ∈ so(7) : X preserves φ }  — solve the linear system; assert dim=14.
  3. orbit-dim at Γ = rank{ [X,Γ] : X ∈ g2 basis } in Herm(7).
"""
import numpy as np

N = 7
# ---- [1] Fano 3-form from the QR(7) difference set {1,2,4} (0-indexed) ----
# lines: {i, i+1, i+3} mod 7 for i=0..6  (a standard cyclic octonion presentation)
triples = [tuple(sorted(((i) % 7, (i + 1) % 7, (i + 3) % 7))) for i in range(7)]
triples = sorted(set(triples))
assert len(triples) == 7, triples
# oriented structure constant φ_{abc}, fully antisymmetric, +1 on each oriented line
phi = np.zeros((N, N, N))
def sign_perm(p):
    # sign of permutation of a 3-tuple relative to sorted order
    a, b, c = p
    s = 1
    arr = [a, b, c]
    for i in range(3):
        for j in range(i + 1, 3):
            if arr[i] > arr[j]:
                s = -s
    return s
for (a, b, c) in triples:
    for p in [(a, b, c), (b, c, a), (c, a, b), (a, c, b), (c, b, a), (b, a, c)]:
        phi[p] = sign_perm(p)

# ---- [2] g2 = { X ∈ so(7) : X·φ = 0 } ----
# so(7): antisymmetric 7x7, basis E_{mn} = e_m e_n^T - e_n e_m^T for m<n (21 of them)
so7 = []
idx = []
for m in range(N):
    for n in range(m + 1, N):
        X = np.zeros((N, N))
        X[m, n] = 1.0
        X[n, m] = -1.0
        so7.append(X)
        idx.append((m, n))
assert len(so7) == 21
# action on φ: (X·φ)_{ijk} = Σ_p X_{ip}φ_{pjk} + X_{jp}φ_{ipk} + X_{kp}φ_{ijp}
def act(X):
    t = np.einsum('ip,pjk->ijk', X, phi)
    t += np.einsum('jp,ipk->ijk', X, phi)
    t += np.einsum('kp,ijp->ijk', X, phi)
    return t
# build linear map so7(21) -> R^(7^3); nullspace = g2
M = np.stack([act(X).reshape(-1) for X in so7], axis=1)   # (343, 21)
u, s, vt = np.linalg.svd(M)
tol = 1e-9
null_mask = np.array([ (s[i] if i < len(s) else 0.0) < tol for i in range(21) ])
# right singular vectors with ~zero singular value span the nullspace
rank_M = int((s > tol).sum())
dim_g2 = 21 - rank_M
g2_coeffs = vt[rank_M:]                      # (dim_g2, 21) coefficients in so7 basis
g2 = [sum(c * X for c, X in zip(row, so7)) for row in g2_coeffs]

print("=" * 74)
print("[1-2] G2 built as the stabiliser of the octonion Fano 3-form")
print("  Fano lines (QR(7) {1,2,4}+i):", triples)
print("  dim so(7) =", 21, "  rank of φ-constraint =", rank_M, "  ⟹ dim g2 =", dim_g2)
assert dim_g2 == 14, "g2 must be 14-dimensional"
print("  ✓ dim g2 = 14  (matches G2 = Aut(O); the corpus's 14 generators)")

# ---- [3] orbit dimension at several Γ ----
def orbit_dim(Gamma):
    # tangent to the orbit = span{ [X, Gamma] : X in g2 }, inside Herm(7)
    vecs = []
    for X in g2:
        B = X @ Gamma - Gamma @ X          # X real antisym, Gamma Herm ⟹ B Herm
        vecs.append(np.concatenate([B.real.reshape(-1), B.imag.reshape(-1)]))
    Mv = np.stack(vecs, axis=0)            # (14, 98)
    sv = np.linalg.svd(Mv, compute_uv=False)
    return int((sv > 1e-8).sum())

rng = np.random.default_rng(7)
def rand_herm(rank=None):
    A = rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))
    H = A @ A.conj().T                      # PSD Hermitian
    if rank is not None:
        w, V = np.linalg.eigh(H)
        w[:-rank] = 0.0                    # keep top `rank` eigenvalues
        H = (V * w) @ V.conj().T
    return H / np.trace(H).real

center = np.eye(N) / N
# rank-1 pure state (projector); rank-3; generic full-rank
p1 = rand_herm(rank=1)
p3 = rand_herm(rank=3)
gen = rand_herm()

print()
print("[3] G2-orbit dimension at different Γ  (= 14 − dim stabiliser)")
rows = [
    ("centre  I/7  (maximally mixed)", center),
    ("rank-1  pure state |v><v|",       p1),
    ("rank-3  mixed state",             p3),
    ("generic full-rank Γ",             gen),
]
dims = []
for name, G in rows:
    d = orbit_dim(G)
    dims.append(d)
    print("  %-32s orbit dim = %2d   stabiliser dim = %2d" % (name, d, 14 - d))
distinct = sorted(set(dims))
print()
print("  distinct orbit dimensions observed:", distinct)
assert 0 in dims and max(dims) > 0 and len(distinct) >= 2

print()
print("=" * 74)
print("VERDICT [Т for the computation; С/Г for the reading]")
print("  The G2-action on D(C^7) has ≥%d distinct orbit types (isotropy VARIES:" % len(distinct))
print("  the centre is fixed by all of G2, generic Γ by almost none). Therefore")
print("  D(C^7)/G2 is a STRATIFIED quotient, the orbit map is NOT a global fibre")
print("  bundle, and NO continuous global slice — NO global intrinsic calibration —")
print("  exists. The slice theorem gives only LOCAL slices near each orbit.")
print("  ⟹ calibration ('which |q> is red') CANNOT be a global function of the")
print("  invariant content; it must be fixed LOCALLY, pointwise. §82's 'external")
print("  boundary data fixes the frame' is then not an optional add-on but the")
print("  natural filler of a hole the geometry PROVES is there: something local")
print("  must choose the frame, because nothing global can. [strengthens Г→С]")
