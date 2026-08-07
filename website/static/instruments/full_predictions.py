#!/usr/bin/env python3
"""П-ВАНЧУРИН-1: ПОЛНЫЙ расчёт всех величин моста УГМ↔Ванчурин.

ЕДИНСТВЕННЫЙ источник чисел для UHM-VANCHURIN-BRIDGE.md и -RU.md.
Всякое число в документах обязано печататься здесь. Детерминировано
(сиды 20260806 / 20260807 / 20260808).

Первоисточники (номера уравнений ниже — по ним):
  [V1] V. Vanchurin, "Geometric framework for biological evolution",
       arXiv:2603.15198  — ур. (4.7), (6.3), (6.7)-(6.9), (7.1)-(7.6)
  [V2] V. Vanchurin, "Geometric Learning Dynamics", arXiv:2504.14728,
       Biological Cybernetics (2026) — ур. (2.2), (2.8), (2.9), (5.5)
"""
import itertools
import numpy as np
from scipy.stats import chi2, ncx2
from scipy.optimize import brentq

np.set_printoptions(precision=6, suppress=False, linewidth=150)

N = 7
FANO = [(0, 1, 2), (0, 3, 4), (0, 5, 6), (1, 3, 5), (1, 4, 6), (2, 3, 6), (2, 4, 5)]
PI = np.eye(N) - np.ones((N, N)) / N        # проектор на касательное простр. T
LINE = "=" * 78


def ops_canonical(atomic=True, blocks=None, k=3, n=N):
    """Канонический набор Линдблада: атомы классификатора + блоки дизайна."""
    o = []
    if atomic:
        for i in range(n):
            L = np.zeros((n, n)); L[i, i] = 1.0; o.append(L)
    for ln in (blocks or []):
        P = np.zeros((n, n))
        for m in ln:
            P[m, m] = 1.0
        o.append(P / np.sqrt(k))
    return o


def kappa(lam, ops, gamma=1.0):
    """κ^↑↑ = (1/dt) Σ_e p_e Δ_e⊗Δ_e — ковариация временных изменений, ур. (2.1)."""
    n = len(lam); rho = np.diag(lam); K = np.zeros((n, n))
    for L in ops:
        LrL = L @ rho @ L.T; tr = np.trace(LrL)
        if tr < 1e-15:
            continue
        d = np.diag(LrL / tr - rho)
        K += (gamma * tr / n) * np.outer(d, d)
    return K


def drift(lam, ops, gamma=1.0):
    """Σ_e p_e Δ_e — средний снос за шаг (должен быть строго нулевым)."""
    n = len(lam); rho = np.diag(lam); v = np.zeros(n)
    for L in ops:
        LrL = L @ rho @ L.T; tr = np.trace(LrL)
        if tr < 1e-15:
            continue
        v += (gamma * tr / n) * np.diag(LrL / tr - rho)
    return v


def g_metric(lam, c):
    """Монотонная метрика на коммутирующем секторе: g = c·diag(1/λ).
    c=1/4 — Бюрес (Аксиома 2); c=1 — SLD-QFI = Фишер–Рао."""
    return c * np.diag(1.0 / lam)


def spec_T(A):
    """Спектр оператора, суженного на T (6 ненулевых собственных значений)."""
    ev = np.sort(np.linalg.eigvals(PI @ A @ PI).real)
    return ev[np.abs(ev) > 1e-12]


def state_one_dominant(P_target):
    """λ = (l₁, (1−l₁)/6 ×6) с заданной чистотой — ТОЧНОЕ решение квадратного ур."""
    # 6l² + (1−l)² = 6P  ⟹  7l² − 2l + 1 − 6P = 0
    a, b, cc = 7.0, -2.0, 1.0 - 6.0 * P_target
    l1 = (-b + np.sqrt(b * b - 4 * a * cc)) / (2 * a)
    return np.concatenate([[l1], np.full(6, (1 - l1) / 6)])


def state_two_dominant(P_target):
    """λ = (a, a, (1−2a)/5 ×5) с заданной чистотой — точное решение."""
    # 10a² + (1−2a)² = 5P ⟹ 14a² − 4a + 1 − 5P = 0
    A, B, C = 14.0, -4.0, 1.0 - 5.0 * P_target
    a = (-B + np.sqrt(B * B - 4 * A * C)) / (2 * A)
    return np.concatenate([[a, a], np.full(5, (1 - 2 * a) / 5)])


print(LINE)
print("П-ВАНЧУРИН-1 · ПРЕДСКАЗАНИЯ УГМ ДЛЯ g(κ)-ПРОГРАММЫ")
print("Первоисточники: arXiv:2603.15198 [V1] · arXiv:2504.14728 [V2]")
print(LINE)

# ---------------------------------------------------------------------------
print("\n[0] КОНВЕНЦИЯ МЕТРИКИ: чему равна метрика Бюреса на коммутирующем секторе")
print("    (D_B² = 2(1−F), F — точность; сравнение с классической Фишер Σdλ²/λ)")


def bures2(rho, sig):
    w, V = np.linalg.eigh(rho)
    sr = V @ np.diag(np.sqrt(np.clip(w, 0, None))) @ V.conj().T
    ew = np.linalg.eigvalsh(sr @ sig @ sr)
    return 2 * (1 - np.sum(np.sqrt(np.clip(ew, 0, None))))


rng = np.random.default_rng(20260808)
lam0 = rng.dirichlet(np.ones(N) * 2.0)
dl = rng.normal(size=N); dl -= dl.mean()
fisher = float(np.sum(dl ** 2 / lam0))
for eps in (1e-3, 1e-4, 1e-5):
    d2 = bures2(np.diag(lam0), np.diag(lam0 + eps * dl))
    print(f"    eps={eps:.0e}: D_B²/(eps²·Фишер) = {d2 / eps**2 / fisher:.10f}")
print("    ⟹ ТОЧНО 1/4: g_Бюрес = (1/4)·diag(1/λ), т.к. на диагонали")
print("      D_B² = ½Σ|dρ_jk|²/(λ_j+λ_k) = ½Σdλ²/(2λ) = ¼Σdλ²/λ.")
print("      SLD-QFI (= Фишер–Рао, конвенция натурального градиента) = 4×Бюрес.")
CB, CF = 0.25, 1.0

# ---------------------------------------------------------------------------
print("\n[1] ТЕОРЕМА 1: κ_at ТОЧНО мультиномиальна, (γ/N)(diag λ − λλᵀ)")
rng = np.random.default_rng(20260806)
res = 0.0
for _ in range(2000):
    l = rng.dirichlet(np.ones(N) * rng.uniform(0.4, 4.0))
    res = max(res, np.abs(kappa(l, ops_canonical(True)) -
                          (np.diag(l) - np.outer(l, l)) / N).max())
print(f"    2000 случайных ρ: max|κ_at − (γ/N)(diag λ − λλᵀ)| = {res:.2e}")
print("    Замечание: (diag λ − λλᵀ) — ковариация ОДНОГО испытания мультиномиального")
print("    распределения И одновременно обратная метрика Фишера на симплексе.")

# ---------------------------------------------------------------------------
print("\n[2] ТЕОРЕМА 2: тождество натурального градиента ⟹ a = 1")
rng = np.random.default_rng(20260806)
devs = []
for t in range(200):
    l = rng.dirichlet(np.ones(N) * rng.uniform(0.4, 4.0))
    ev = spec_T(g_metric(l, CB) @ kappa(l, ops_canonical(True)))
    devs.append(ev.max() - ev.min())
    if t < 3:
        print(f"    проба {t}: spec(Π g κ_at Π) = {ev[0]:.12f}  "
              f"(γ/4N = {CB / N:.12f}), разброс {ev.max()-ev.min():.2e}")
print(f"    200 случайных ρ: max разброс = {max(devs):.2e} ⟹ Π g κ_at Π = (γ/4N)·Π ТОЧНО")
print("\n    Константа зависит от конвенции метрики, ФОРМА — нет:")
for nm, c in [("Бюрес   g=¼diag(1/λ)", CB), ("SLD-QFI g= diag(1/λ)", CF)]:
    ev = spec_T(g_metric(lam0, c) @ kappa(lam0, ops_canonical(True)))
    print(f"      {nm}: Πgκ_at Π = {ev[0]:.12f}·I_T = γ·{ev[0]*N:.4f}/N "
          f"(разброс {ev.max()-ev.min():.1e})")
print("\n    КРИТЕРИЙ САМОГО ВАНЧУРИНА, ур. (7.5) [V1]: g⁻¹ = (g⁻¹κg⁻¹)^{a/(2a−1)}")
print("      a=1   ⟹ κ^↑↑ = g⁻¹          (натуральный градиент)")
print("      a=1/2 ⟹ κ^↑↑ = I            (эффективное обучение; g из данных НЕ извлекается)")
print("      a=0   ⟹ g⁻¹ = I             (стохастический градиент)")
gi = np.linalg.pinv(PI @ g_metric(lam0, CB) @ PI)
K = PI @ kappa(lam0, ops_canonical(True)) @ PI
print(f"    max|κ^↑↑_at − (γ/4N)·g⁻¹| = {np.abs(K - (CB/N)*gi).max():.2e}  ⟹ ровно ур. (7.5) при a=1")

# ---------------------------------------------------------------------------
print("\n[3] ТЕОРЕМА 3: универсальный Фано-множитель 11/9")
rng = np.random.default_rng(20260807)
rat = []
for _ in range(300):
    l = rng.dirichlet(np.ones(N) * rng.uniform(0.3, 5.0))
    g = g_metric(l, CB)
    rat.append(np.trace(g @ kappa(l, ops_canonical(True, FANO))) /
               np.trace(g @ kappa(l, ops_canonical(True))))
rat = np.array(rat)
print(f"    300 случайных ρ: отношение ∈ [{rat.min():.12f}, {rat.max():.12f}]")
print(f"    max|отношение − 11/9| = {np.abs(rat - 11/9).max():.2e}  (не зависит от конвенции g)")
print(f"    Доля шума, несомая блочным слоем = 2/11 = {2/11:.12f} — тоже независима от λ")
g = g_metric(lam0, CB)
ta = np.trace(g @ kappa(lam0, ops_canonical(True)))
tf = np.trace(g @ kappa(lam0, ops_canonical(True, FANO)))
print(f"    Бюрес:   Tr(gκ_at) = {ta:.12f} = 3γ/14 = {3/14:.12f}; "
      f"Tr(gκ_full) = {tf:.12f} = 11γ/42 = {11/42:.12f}")
gF = g_metric(lam0, CF)
print(f"    SLD-QFI: Tr(gκ_at) = {np.trace(gF@kappa(lam0,ops_canonical(True))):.12f} = 6γ/7; "
      f"Tr(gκ_full) = {np.trace(gF@kappa(lam0,ops_canonical(True,FANO))):.12f} = 22γ/21")
print("\n    АНИЗОТРОПИЯ: спектр Πgκ_full Π изотропен ТОЛЬКО в I/7")
for lam, nm in [(np.ones(N)/N, "I/7"),
                (np.concatenate([[0.5], np.full(6, 1/12)]), "λ=(1/2,1/12×6), P=7/24"),
                (state_one_dominant(5/14), "P=5/14 (центр окна)")]:
    ev = spec_T(g_metric(lam, CB) @ kappa(lam, ops_canonical(True, FANO)))
    print(f"    {nm:26s}: spec/(γ/4N) = {np.round(np.sort(ev)*N/CB, 6)}  "
          f"анизотропия {ev.max()/ev.min():.4f}")
cl = np.array([13/12, 13/12, 11/9, 11/9, 11/9, 3/2])
ev = np.sort(spec_T(g_metric(np.concatenate([[0.5], np.full(6, 1/12)]), CB) @
                    kappa(np.concatenate([[0.5], np.full(6, 1/12)]),
                          ops_canonical(True, FANO)))) * N / CB
print(f"    для λ=(1/2,1/12×6) заявлено {{13/12,13/12,11/9,11/9,11/9,3/2}}: "
      f"max|Δ| = {np.abs(ev - np.sort(cl)).max():.2e}")
print(f"    сумма = {ev.sum():.10f} = 6·11/9 = {6*11/9:.10f} (след универсален, спектр нет)")

print("\n    ОБОБЩЕНИЕ НА BIBD(v,k,1): отношение = (b−r)/(k(v−1))")
designs = {
    "Фано PG(2,2) (7,3,1)": (7, 3, FANO),
    "AG(2,3)      (9,3,1)": (9, 3, [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),
                                    (0,4,8),(1,5,6),(2,3,7),(0,5,7),(1,3,8),(2,4,6)]),
    "PG(2,3)     (13,4,1)": (13, 4, [tuple(sorted((d+i) % 13 for d in (0,1,3,9)))
                                     for i in range(13)]),
}
for nm, (v, k, bl) in designs.items():
    b = len(bl); r = b * k // v
    pr = {}
    for ln in bl:
        for p in itertools.combinations(sorted(ln), 2):
            pr[p] = pr.get(p, 0) + 1
    ok = len(pr) == v*(v-1)//2 and set(pr.values()) == {1}
    rg = np.random.default_rng(20260808)
    got = []
    for _ in range(40):
        l = rg.dirichlet(np.ones(v) * rg.uniform(0.4, 4.0))
        gg = 0.25 * np.diag(1.0 / l)
        got.append(np.trace(gg @ kappa(l, ops_canonical(False, bl, k, v))) /
                   np.trace(gg @ kappa(l, ops_canonical(True, None, k, v))))
    got = np.array(got); pred = (b - r) / (k * (v - 1))
    print(f"    {nm} b={b:2d} r={r} λ=1 проверен={ok}: предсказано {pred:.10f}, "
          f"численно max|Δ| = {np.abs(got-pred).max():.1e}, r/k = {r/k:.4f}"
          f"{'  ← как у Фано, ΣL†L=I' if abs(r/k-1) < 1e-12 else '  ← ΣL†L≠I, нужна перенормировка'}")

# ---------------------------------------------------------------------------
print("\n[4] ТЕОРЕМА 4: шум ↔ чистота (не зависит от конвенции метрики)")
print("    Tr κ_at = (γ/N)(1−P) и Tr κ_at² = (γ/N)²(P + P² − 2Σλ³)")
for nm, lam in [("I/7 (P=1/7)", np.ones(N)/N),
                ("P_crit = 2/7", state_one_dominant(2/7)),
                ("P = 5/14 (центр)", state_one_dominant(5/14)),
                ("P = 3/7 (верх окна)", state_one_dominant(3/7))]:
    Pur = float(np.sum(lam**2)); S3 = float(np.sum(lam**3))
    K = kappa(lam, ops_canonical(True))
    print(f"    {nm:20s}: P={Pur:.10f} · Tr κ={np.trace(K):.10f} vs (1−P)/N={(1-Pur)/N:.10f}"
          f" · Tr κ²={np.trace(K@K):.3e} vs формула={(Pur+Pur**2-2*S3)/N**2:.3e}")
print(f"    окно P∈(2/7,3/7] ⟹ Tr κ ∈ [4γ/49, 5γ/49) = [{4/49:.10f}, {5/49:.10f})")

# ---------------------------------------------------------------------------
print("\n[5] ТЕОРЕМА 5: секторное расщепление κ^coh")


def super_diss(ops, gamma=1.0):
    """L[ρ] = (γ/N)Σ(LρL† − ½{L†L,ρ}) как матрица 49×49."""
    A = sum(L.conj().T @ L for L in ops); I = np.eye(N)
    S = sum(np.kron(L, L.conj()) for L in ops)
    return (gamma / N) * (S - 0.5 * (np.kron(A, I) + np.kron(I, A.conj())))


S_full = super_diss(ops_canonical(True, FANO))
S_at = super_diss(ops_canonical(True))
for nm, S in [("атомарный (7 опер.)", S_at), ("полный at+Фано (14)", S_full)]:
    ev = np.linalg.eigvals(S).real
    u = np.unique(np.round(ev, 10))
    print(f"    {nm}: спектр = {u} кратности {[int(np.sum(np.abs(ev-x)<1e-9)) for x in u]}"
          f" (−γ/7={-1/7:.9f}, −5γ/21={-5/21:.9f})")
print(f"    max|L_full(γ=1) − L_at(γ=5/3)| = {np.abs(S_full - super_diss(ops_canonical(True), 5/3)).max():.2e}")
print("    ⟹ ОДИН генератор: полный канонический диссипатор ≡ полное дефазирование")
print("      со скоростью 5γ/21. Фано-слой НЕ различим в мастер-уравнении — только")
print("      в выборе Краус-разрешения (unravelling). κ определена ОТНОСИТЕЛЬНО")
print("      канонического разрешения (L-унификация, T-41g–i), а не инвариантна.")
lam = np.array([0.4, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1])
g = g_metric(lam, CB)
ka1 = np.trace(g @ kappa(lam, ops_canonical(True), 1.0))
kf1 = np.trace(g @ kappa(lam, ops_canonical(True, FANO), 1.0))
ka53 = np.trace(g @ kappa(lam, ops_canonical(True), 5/3))
print(f"    при равной скорости НА КАНАЛ γ:      Tr(gκ_full)/Tr(gκ_at) = {kf1/ka1:.10f} = 11/9")
print(f"    при равном ГЕНЕРАТОРЕ (γ_at = 5γ/3): Tr(gκ_full)/Tr(gκ_at) = {kf1/ka53:.10f} = 11/15")
print("\n    κ^coh на диагональном и НЕдиагональных состояниях:")
mask = np.array([[i != j for j in range(N)] for i in range(N)]).reshape(-1)
for c in (0.0, 0.02, 0.10):
    rho = np.diag(lam).astype(complex)
    if c:
        rho[0, 1] += c; rho[1, 0] += c; rho[2, 3] += c/2; rho[3, 2] += c/2
    Kf = np.zeros((N*N, N*N), dtype=complex); off = 0.0
    for L in ops_canonical(True, FANO):
        LrL = L @ rho @ L.conj().T; tr = np.trace(LrL).real
        if tr < 1e-15:
            continue
        D = LrL / tr - rho
        off = max(off, np.abs(D - np.diag(np.diag(D))).max())
        Kf += (tr / N) * np.outer(D.reshape(-1), D.reshape(-1).conj())
    print(f"      коэрентность c={c:.2f} (ρ⪰0: {np.linalg.eigvalsh(rho).min() > -1e-12}): "
          f"max|Δ_e внедиаг| = {off:.3e} · max|κ^coh| = {np.abs(Kf[np.ix_(mask,mask)]).max():.3e}")
print("    ⟹ κ^coh ≡ 0 ТОЧНО на декогерированном многообразии (аттракторе);")
print("      вне него κ^coh = O(‖ρ_coh‖²) и гаснет как exp(−10γt/21).")

# ---------------------------------------------------------------------------
print("\n[6] ЭФФЕКТИВНЫЙ РАНГ (ур. 7.3 [V1]): замкнутая форма и её область")
print("    r_eff = (Tr κ)²/Tr κ² = (1−P)²/(P + P² − 2Σλ³) — НЕ функция одной чистоты")


def reff_num(l):
    ev = np.linalg.eigvalsh(PI @ kappa(l, ops_canonical(True)) @ PI)
    ev = ev[ev > 1e-14]
    return ev.sum() ** 2 / np.sum(ev ** 2)


def reff_cf(l):
    P = np.sum(l**2); return (1-P)**2 / (P - 2*np.sum(l**3) + P**2)


rng = np.random.default_rng(20260808)
d = max(abs(reff_num(l) - reff_cf(l))
        for l in (rng.dirichlet(np.ones(N)*rng.uniform(.3, 4)) for _ in range(300)))
print(f"    300 состояний: max|числ. − замкнутая| = {d:.2e}")
for Pt, nm in [(1/7, "P=1/7 (I/7)"), (2/7, "P=2/7"), (5/14, "P=5/14"), (3/7, "P=3/7")]:
    if Pt == 1/7:
        print(f"    {nm:12s}: r_eff = {reff_num(np.ones(N)/N):.4f}  (максимум N−1 = 6)")
    else:
        print(f"    {nm:12s}: «1 доминанта+6» r_eff = {reff_num(state_one_dominant(Pt)):.4f}"
              f"   ·  «2 доминанты+5» r_eff = {reff_num(state_two_dominant(Pt)):.4f}  ← та же P!")
rng = np.random.default_rng(20260808)
lo, hi = np.inf, -np.inf
for _ in range(400_000):
    l = rng.dirichlet(np.ones(N) * rng.uniform(0.05, 6.0))
    if not (2/7 < np.sum(l**2) <= 3/7):
        continue
    r = reff_cf(l); lo = min(lo, r); hi = max(hi, r)
print(f"    поиск по ВСЕМ λ с P∈(2/7,3/7]: r_eff ∈ [{lo:.4f}, {hi:.4f}]")
print(f"    (край P→2/7⁺ на семействе «1 доминанта»: {reff_cf(state_one_dominant(2/7)):.4f})")
print("    ⟹ интервал [3.59, 4.22] верен ТОЛЬКО на семействе «одна доминанта + шесть равных»;")
print("      фальсифицируемое утверждение — сама замкнутая форма (два момента), не интервал.")

# ---------------------------------------------------------------------------
print("\n[7] НУЛЕВОЙ СНОС: κ есть ЦЕНТРИРОВАННАЯ ковариация (как в ур. 7.4 [V1])")
rng = np.random.default_rng(20260808)
md = max(np.abs(drift(rng.dirichlet(np.ones(N)*2.0), ops_canonical(True, FANO))).max()
         for _ in range(200))
mD = max(np.abs(S_full @ np.diag(rng.dirichlet(np.ones(N)*2.0)).reshape(-1)).max()
         for _ in range(200))
print(f"    max|Σ_e p_e Δ_e| по 200 состояниям = {md:.2e}")
print(f"    max|L_full[diag λ]|              = {mD:.2e}")
print("    ⟹ диссипатор обнуляет ЛЮБОЕ диагональное состояние: на популяциях он даёт")
print("      чистый шум без сноса. Второй момент = центрированная ковариация ур. (7.4),")
print("      а весь снос несёт регенерация R — ровно ланжевеновское расщепление [V1].")

# ---------------------------------------------------------------------------
print("\n[8] ФАЛЬСИФИКАЦИЯ: как отличить a=1 от a=1/2 БЕЗ измерения метрики")
print("    a=1/2 ⟹ κ^↑↑ ∝ Π (сферична);  a=1 ⟹ κ^↑↑ ∝ diag λ − λλᵀ (вычислима по λ).")
print("    Статистика сферичности (Мокли), d=6, df = d(d+1)/2 − 1 = 20:")
print("      T = −M·ln[ det_T(A) / (Tr A/6)^6 ],  A = Σ₀^{-1/2} κ̂ Σ₀^{-1/2}")
df = 20
crit = chi2.ppf(0.95, df)
ncp80 = brentq(lambda nc: ncx2.sf(crit, df, nc) - 0.80, 1e-6, 500.0)
print(f"    порог χ²(0.95, 20) = {crit:.4f}; нецентральность для мощности 80 % = {ncp80:.4f}")
print("    Разделяющая способность Δ(λ) := 6·ln(ср. арифм./ср. геом. собств. κ^↑↑):")
for Pt, nm in [(1/7, "I/7 (P=1/7)"), (2/7, "P=2/7"), (5/14, "P=5/14"), (3/7, "P=3/7")]:
    lam = np.ones(N)/N if Pt == 1/7 else state_one_dominant(Pt)
    ev = np.sort(np.linalg.eigvalsh(PI @ kappa(lam, ops_canonical(True)) @ PI))[-6:]
    Delta = 6*np.log(ev.mean()) - np.sum(np.log(ev))
    tail = "различить НЕЛЬЗЯ (Δ=0)" if Delta < 1e-12 else f"асимпт. оценка M ≳ {int(np.ceil(ncp80/Delta))}"
    print(f"      {nm:14s}: Δ = {Delta:.6f}  ⟹ {tail}")
print("    В I/7 разделения нет вовсе; сила растёт с уходом λ от равномерности.")
print("\n    НО асимптотика χ² при M ≈ d НЕВЕРНА. Прямая симуляция (гауссовы окна):")
rgs = np.random.default_rng(20260808)
Qb, _ = np.linalg.qr(np.column_stack([np.ones(N), rgs.normal(size=(N, N-1))]))
Bt = Qb[:, 1:]


def spher(S6, M):
    sgn, ld = np.linalg.slogdet(S6)
    return np.inf if sgn <= 0 else -M*(ld - 6*np.log(np.trace(S6)/6))


Ms = (25, 50, 100, 200)
size = []
for M in Ms:
    T = [spher((X := rgs.normal(size=(M, 6))).T @ X / M, M) for _ in range(2000)]
    size.append(np.mean(np.array(T) > crit)*100)
print("      размер теста (истина СФЕРИЧНА, должно быть 5 %): " +
      " · ".join(f"M={m}: {s:.1f} %" for m, s in zip(Ms, size)))
for Pt, nm in [(2/7, "P=2/7"), (5/14, "P=5/14"), (3/7, "P=3/7")]:
    lam = state_one_dominant(Pt)
    L = np.linalg.cholesky(Bt.T @ (np.diag(lam) - np.outer(lam, lam)) @ Bt)
    pw = []
    for M in Ms:
        T = [spher((X := rgs.normal(size=(M, 6)) @ L.T).T @ X / M, M) for _ in range(1000)]
        pw.append(np.mean(np.array(T) > crit)*100)
    print(f"      мощность при истине a=1, {nm:7s}: " +
          " · ".join(f"M={m}: {p:.1f} %" for m, p in zip(Ms, pw)))
print("    ⟹ ПРАКТИЧЕСКИЙ ВЫВОД: M ≈ 100 независимых окон даёт размер ≈5 % и мощность ≈100 %")
print("      всюду в окне жизнеспособности; при M ≤ 25 тест антиконсервативен и негоден.")
print("      Приращения ОБЯЗАНЫ агрегироваться по окнам с ΛΔt ≫ 1: идеализованный")
print("      одиночный скачок имеет лишь 7 исходов, κ̂ = diag(p̂) − p̂λᵀ − λp̂ᵀ + λλᵀ")
print("      параметризована 6 числами вместо 21, и калибровка df=20 к ней не применима.")
print("\n    ЧТО ИМЕННО ОЦЕНИВАЕТ ОКНО: составной пуассоновский процесс с нулевым")
print("    средним ⟹ ковариация приращения за окно Δt равна ровно κ·Δt (Кэмпбелл).")
lam = state_one_dominant(3/14 + 3/14)     # P = 3/7, верхний край окна
ops14 = ops_canonical(True, FANO)
rho_l = np.diag(lam)
rates = np.array([np.trace(L @ rho_l @ L.T) / N for L in ops14])
jumps = np.array([np.diag((L @ rho_l @ L.T) / np.trace(L @ rho_l @ L.T) - rho_l)
                  for L in ops14])
Lam = rates.sum()
print(f"      полная скорость скачков Λ = Σ_e γTr(L_eρL_e†)/N = {Lam:.10f} = 2γ/N = {2/N:.10f}")
rgw = np.random.default_rng(20260807)
for dt in (5.0, 50.0):
    W = np.array([jumps[rgw.choice(len(ops14), size=n, p=rates/Lam)].sum(axis=0)
                  if (n := rgw.poisson(Lam*dt)) else np.zeros(N)
                  for _ in range(40000)])
    emp = (W - W.mean(0)).T @ (W - W.mean(0)) / len(W)
    K = kappa(lam, ops14)
    print(f"      Δt={dt:5.1f} (ΛΔt={Lam*dt:6.2f}): max|Cov(окно)/Δt − κ| = "
          f"{np.abs(emp/dt - K).max():.2e}  (‖κ‖max = {np.abs(K).max():.4f})")
print("      ⟹ оценщик по окнам состоятелен; но κ зависит от состояния, поэтому окно")
print("        обязано лежать между двумя временами: 1/Λ ≪ Δt ≪ время сноса от R.")
print("        Существует ли такое окно в конкретной системе — эмпирический вопрос")
print("        об отношении скорости регенерации к скорости диссипации.")

# ---------------------------------------------------------------------------
print("\n[9] ЛЕСТНИЦА УРОВНЕЙ (его multi-level ↔ наш c_F = 1/3)")
print(f"    c_F = 1/|QR(7)| = 1/3; P_crit-лестница ⟹ SAD_max = 3;")
print(f"    dim Cog_n = 7^(n+1): {[7**(n+1) for n in range(4)]}")
print(LINE)
