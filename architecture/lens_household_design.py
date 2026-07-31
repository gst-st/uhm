"""HB18: информационная полнота БЫТОВОГО томографического набора.

Три типа вопросов дневника (все — естественные, без суперпозиций-жаргона):
  T1 «насколько громко» (7): проекторы |i><i|                — диагональ
  T2 «заодно или врозь» (21): P+_ij = |u><u|, u=(e_i+e_j)/√2 — Re Γ_ij
  T3 «кто вёл» (21):        Pi_ij = |v><v|, v=(e_i+i·e_j)/√2 — Im Γ_ij

Вопрос: образуют ли 49 проекторов информационно полный набор для d=7
(ранг 49 в пространстве эрмитовых матриц), и насколько он хуже MUB по
обусловленности (устойчивость к шуму слайдеров).

Запуск: python3 architecture/lens_household_design.py
"""
import numpy as np

d = 7

def herm_to_vec(H):
    """Вещественная векторизация эрмитовой матрицы (d² координат)."""
    out = []
    for i in range(d):
        out.append(H[i, i].real)
    for i in range(d):
        for j in range(i + 1, d):
            out.append(np.sqrt(2) * H[i, j].real)
            out.append(np.sqrt(2) * H[i, j].imag)
    return np.array(out)

def proj(u):
    u = u / np.linalg.norm(u)
    return np.outer(u, u.conj())

# --- бытовой набор ---------------------------------------------------------
house = []
for i in range(d):
    e = np.zeros(d, complex); e[i] = 1
    house.append(proj(e))
for i in range(d):
    for j in range(i + 1, d):
        e = np.zeros(d, complex); e[i] = 1; e[j] = 1
        house.append(proj(e))
for i in range(d):
    for j in range(i + 1, d):
        e = np.zeros(d, complex); e[i] = 1; e[j] = 1j
        house.append(proj(e))

A_house = np.array([herm_to_vec(P) for P in house])

# --- MUB-набор (8 базисов × 7 векторов = 56 проекторов) --------------------
w = np.exp(2j * np.pi / d)
mub = []
eye = np.eye(d, dtype=complex)
for m in range(d):
    mub.append(proj(eye[m]))
for a in range(1, d + 1):
    for m in range(d):
        v = np.array([w ** (((a - 1) * j * j + m * j) % d)
                      for j in range(d)]) / np.sqrt(d)
        mub.append(proj(v))
A_mub = np.array([herm_to_vec(P) for P in mub])

for name, A in (("household(49)", A_house), ("MUB(56)", A_mub)):
    s = np.linalg.svd(A, compute_uv=False)
    rank = int((s > 1e-10).sum())
    cond = s[0] / s[rank - 1]
    print(f"{name}: rank={rank}/49  cond={cond:.2f}  "
          f"s_min={s[rank-1]:.4f} s_max={s[0]:.4f}")

# --- шумовой замер: восстановление случайных состояний ---------------------
rng = np.random.default_rng(20260731)

def rand_state():
    X = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    G = X @ X.conj().T
    return G / np.trace(G).real

def reconstruct_lsq(A, projs, G, sigma, reps):
    errs = []
    for _ in range(reps):
        p = np.array([np.real(np.trace(P @ G)) for P in projs])
        noisy = p * (1 + sigma * rng.normal(size=len(p)))
        x, *_ = np.linalg.lstsq(A, None, rcond=None) if False else (None,)
        # решаем A^T? — A строк=проекторы, столбцов=49; vec(G) координаты:
        # p = A @ g  ⟹ g = lstsq(A, noisy)
        g, *_ = np.linalg.lstsq(A, noisy, rcond=None)
        # соберём эрмитову обратно
        H = np.zeros((d, d), complex)
        k = 0
        for i in range(d):
            H[i, i] = g[k]; k += 1
        for i in range(d):
            for j in range(i + 1, d):
                H[i, j] = (g[k] + 1j * g[k + 1]) / np.sqrt(2)
                H[j, i] = H[i, j].conjugate()
                k += 2
        # PSD-проекция + нормировка
        lam, V = np.linalg.eigh(H)
        lam = np.clip(lam, 0, None)
        R = (V * lam) @ V.conj().T
        tr = np.trace(R).real
        if tr > 1e-12:
            R = R / tr
        td = 0.5 * np.abs(np.linalg.eigvalsh(R - G)).sum()
        errs.append(td)
    return float(np.median(errs))

REPS_STATES = 40
for sigma in (0.05, 0.15, 0.30):
    th, tm = [], []
    for _ in range(REPS_STATES):
        G = rand_state()
        th.append(reconstruct_lsq(A_house, house, G, sigma, 3))
        tm.append(reconstruct_lsq(A_mub, mub, G, sigma, 3))
    print(f"sigma={sigma}: TD(household)={np.median(th):.4f}  "
          f"TD(MUB)={np.median(tm):.4f}  ratio={np.median(th)/np.median(tm):.2f}")
