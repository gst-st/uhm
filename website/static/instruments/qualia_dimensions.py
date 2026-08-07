#!/usr/bin/env python3
"""П-КВАЛИА-1: механизм квалиа как G₂-инвариантное содержание Γ.

Считает: dim g₂ (самопроверка φ), расщепление антисимметричной части
через φ-свёртку, размерность общей орбиты G₂ на D(ℂ⁷), инвариантное
содержание и его качественную часть, стабилизатор в I/7, значения
φ-инвариантов на конкретной карте. Числа — только из этого вывода.
Индексация: канон-номера 1..7 → 0..6 (умножение e_i e_{i+1} = e_{i+3}).
"""
import numpy as np

N = 7
np.set_printoptions(precision=6, suppress=True)

# ── ассоциативная 3-форма φ: оси-тройки (i, i+1, i+3) mod 7 ─────────
phi = np.zeros((N, N, N))
LINES = [(i, (i + 1) % N, (i + 3) % N) for i in range(N)]
PERMS = [((0, 1, 2), 1), ((1, 2, 0), 1), ((2, 0, 1), 1),
         ((0, 2, 1), -1), ((2, 1, 0), -1), ((1, 0, 2), -1)]
for tri in LINES:
    for p, sg in PERMS:
        phi[tri[p[0]], tri[p[1]], tri[p[2]]] = sg

# ── базис so(7) ────────────────────────────────────────────────────
so7 = []
for i in range(N):
    for j in range(i + 1, N):
        E = np.zeros((N, N)); E[i, j] = 1.0; E[j, i] = -1.0
        so7.append(E)
so7 = np.array(so7)                                    # (21,7,7)

# ── g₂ = {X ∈ so(7) : X·φ = 0} ─────────────────────────────────────
def act(X):
    return (np.einsum('il,ljk->ijk', X, phi)
            + np.einsum('jl,ilk->ijk', X, phi)
            + np.einsum('kl,ijl->ijk', X, phi))

M = np.array([act(X).ravel() for X in so7])            # (21, 343)
u, s, vt = np.linalg.svd(M)
tol = 1e-10 * max(M.shape) * (s[0] if s.size else 1.0)
ker = vt.shape[0]  # placeholder
null_dim = int(np.sum(s < tol)) + (21 - len(s))
g2_basis = [sum(c * so7[k] for k, c in enumerate(vec))
            for vec in u.T[len(s) - null_dim:]] if null_dim else []
# устойчивее: ядро строк M
_, sv, Vt_rows = np.linalg.svd(M.T @ M)
eigval, eigvec = np.linalg.eigh(M @ M.T)
g2_basis = [sum(eigvec[k, c] * so7[k] for k in range(21))
            for c in range(21) if eigval[c] < tol]
print(f"(1) dim g₂ = {len(g2_basis)}   [ожидание 14]")
assert len(g2_basis) == 14, "форма φ неверна"

# ── (2) φ-свёртка антисимметричной части: A ↦ v_i = φ_ijk A_jk ─────
C = np.array([np.einsum('ijk,jk->i', phi, A) for A in so7])   # (21,7)
r_phi = int(np.linalg.matrix_rank(C, tol=1e-9))
print(f"(2) ранг φ-свёртки на Λ²(7) = {r_phi} ⟹ 21 = "
      f"{21 - r_phi} ⊕ {r_phi}   [ожидание 14 ⊕ 7]")

# ── (3) размерность общей орбиты G₂ на D(ℂ⁷) ───────────────────────
def orbit_dim(rho):
    V = []
    for X in g2_basis:
        Cm = X @ rho - rho @ X
        V.append(np.concatenate([Cm.real.ravel(), Cm.imag.ravel()]))
    return int(np.linalg.matrix_rank(np.array(V), tol=1e-9))

rng = np.random.default_rng(20260807)
dims = []
for _ in range(200):
    Z = rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N))
    rho = Z @ Z.conj().T
    rho /= np.trace(rho).real
    dims.append(orbit_dim(rho))
print(f"(3) орбита G₂ на 200 случайных Γ: min={min(dims)} max={max(dims)} "
      f"мода={max(set(dims), key=dims.count)}   [ожидание 14]")

# ── (4) инвариантное содержание и качественная часть ───────────────
gen = max(set(dims), key=dims.count)
total = N * N - 1
iso = total - (N - 1)                    # изоспектральное многообразие
print(f"(4) всего dim D(ℂ⁷) = {total} · спектр = {N-1} · "
      f"изоспектральное = {iso}")
print(f"    инвариантное содержание = {total} − {gen} = {total - gen}; "
      f"из них спектр {N-1}, КАЧЕСТВО = {iso - gen}")

# ── (5) стабилизатор в I/7 и на вещественных состояниях ────────────
print(f"(5) орбита в I/7 = {orbit_dim(np.eye(N) / N)}   "
      f"[ожидание 0 — качества нет в равномерном]")
Zr = rng.normal(size=(N, N)); rr = Zr @ Zr.T; rr /= np.trace(rr)
print(f"    орбита на вещественном Γ (нет когерентных фаз) = "
      f"{orbit_dim(rr.astype(complex))}")

# ── (6) φ-инварианты как метки качества ────────────────────────────
def labels(rho):
    A = rho.imag                            # антисимметричная часть
    S = rho.real - np.trace(rho.real) / N * np.eye(N)
    v = np.einsum('ijk,jk->i', phi, A)      # 7-компонента (φ-вектор)
    a14 = A - sum(v[i] * np.einsum('ijk->jk', phi[i:i+1]) for i in range(N)) * 0
    return dict(v_norm=float(np.linalg.norm(v)),
                A_norm=float(np.linalg.norm(A)),
                S_norm=float(np.linalg.norm(S)),
                phi_S=float(np.einsum('ijk,il,jm,kn,lm->n',
                                      phi, S, S, np.eye(N), np.eye(N)).sum()))
print("(6) φ-метки на трёх состояниях (пример шкалы):")
for tag, r in [("I/7", np.eye(N) / N + 0j),
               ("случайное", rho),
               ("вещественное", rr.astype(complex))]:
    L = labels(r)
    print(f"    {tag:12s} |v|={L['v_norm']:.6f} · |A|={L['A_norm']:.6f} "
          f"· |S₀|={L['S_norm']:.6f}")
