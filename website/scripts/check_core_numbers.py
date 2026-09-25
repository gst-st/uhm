#!/usr/bin/env python3
"""ЧИСЛА ЯДРА: регрессионные проверки утверждений, на которых стоит корпус.

Каждая проверка — свидетель одного утверждения корпуса. Три из них родились как
ОШИБКИ, найденные внешним аудитом 10.09.2026, и стоят здесь, чтобы не вернуться:
`kl_at_threshold` (точная D_KL на пороге — 0,344, а не 1/2), `phi_not_g2_invariant`
(Φ не $G_2$-инвариантна) и `z7_irreps_are_one_dimensional` (неприводимые
представления ℤ₇ одномерны, регулярное — семимерно). Ещё две стоят за отзывами
25.09.2026: `phi_of_a_product_factorises` (Φ произведения задана частями — условие
Φ₁₂ > 1 выполняет любая несвязанная пара) и `window_predicate_not_constant_on_g2_orbit`
(предикат окна не постоянен на $G_2$-орбите).

Запуск: `python3 scripts/check_core_numbers.py` или `pytest scripts/check_core_numbers.py`.
"""
import itertools

import numpy as np
from scipy.linalg import expm
from scipy.optimize import least_squares

LINES = [(1, 2, 4), (2, 3, 5), (3, 4, 6), (4, 5, 7), (5, 6, 1), (6, 7, 2), (7, 1, 3)]
E_AXIS, O_AXIS = 4, 6          # E = e_5, O = e_7 в разметке {A,S,D,L,E,O,U}


def omul(a, b):
    c = np.zeros(8)
    c[0] = a[0] * b[0] - np.dot(a[1:], b[1:])
    c[1:] += a[0] * b[1:] + b[0] * a[1:]
    for i, j, k in LINES:
        for x, y, z in ((i, j, k), (j, k, i), (k, i, j)):
            c[z] += a[x] * b[y] - a[y] * b[x]
    return c


def unit(i):
    v = np.zeros(8)
    v[i] = 1
    return v


def derivation(a, b, x):
    comm = lambda u, v: omul(u, v) - omul(v, u)
    assoc = lambda u, v, w: omul(omul(u, v), w) - omul(u, omul(v, w))
    return comm(comm(a, b), x) - 3 * assoc(a, b, x)


def der_matrix(a, b):
    M = np.zeros((7, 7))
    for i in range(7):
        M[:, i] = derivation(a, b, unit(i + 1))[1:]
    return M


def g2_basis():
    gens = [der_matrix(unit(i), unit(j)) for i in range(1, 8) for j in range(i + 1, 8)]
    basis, flat = [], []
    for g in gens:
        if np.linalg.matrix_rank(np.array(flat + [g.flatten()])) > len(flat):
            flat.append(g.flatten())
            basis.append(g)
    return basis


G2 = g2_basis()
PHI3 = np.zeros((7, 7, 7))
for i, j, k in LINES:
    for (x, y, z), s in (((i, j, k), 1), ((j, k, i), 1), ((k, i, j), 1),
                         ((j, i, k), -1), ((i, k, j), -1), ((k, j, i), -1)):
        PHI3[x - 1, y - 1, z - 1] = s


def purity(G):
    return float(np.real(np.trace(G @ G)))


def integration(G):
    d = np.real(np.diag(G))
    return float((np.sum(np.abs(G) ** 2) - np.sum(d ** 2)) / np.sum(d ** 2))


def coh_e(G, e=E_AXIS):
    off = sum(abs(G[e, i]) ** 2 for i in range(7) if i != e)
    return float((np.real(G[e, e]) ** 2 + 2 * off) / purity(G))


def test_g2_is_fourteen_dimensional():
    assert len(G2) == 14


def test_phi_is_an_ell4_functional():
    """Φ на вещественных чистых состояниях = (1 − ‖v‖₄⁴)/‖v‖₄⁴ — ключ к жёсткости репера."""
    rng = np.random.default_rng(0)
    for _ in range(20):
        v = rng.normal(size=7)
        v /= np.linalg.norm(v)
        n4 = np.sum(v ** 4)
        assert abs(integration(np.outer(v, v)) - (1 - n4) / n4) < 1e-12


def test_kl_at_threshold():
    """Точная D_KL(Γ‖I/7) на экстремальном спектре при P = 2/7 равна 0,344, а не 1/2."""
    lam = np.array([(1 + np.sqrt(6)) / 7] + [(6 - np.sqrt(6)) / 42] * 6)
    assert abs(lam.sum() - 1) < 1e-12 and abs((lam ** 2).sum() - 2 / 7) < 1e-12
    exact = np.log(7) + float((lam * np.log(lam)).sum())
    assert abs(exact - 0.3441) < 1e-3
    assert abs(exact - 0.5) > 0.15          # приближение промахивается заметно


def test_consciousness_measure_identity():
    """C = Φ·R = (1/7)(1/Σγᵢᵢ² − 1/P)."""
    rng = np.random.default_rng(1)
    for _ in range(10):
        A = rng.normal(size=(7, 7)) + 1j * rng.normal(size=(7, 7))
        G = A @ A.conj().T
        G /= np.trace(G).real
        P = purity(G)
        d = np.real(np.diag(G))
        assert abs(integration(G) * (1 / (7 * P)) - (1 / 7) * (1 / np.sum(d ** 2) - 1 / P)) < 1e-10


def test_phi_not_g2_invariant():
    """Явный g ∈ G₂ переводит Φ: 0 → 1 и Coh_E: 1 → 3/4 — Φ и Coh_E не G₂-инвариантны."""
    M = der_matrix(unit(1), unit(2))
    g = expm((np.pi / 16) * M)
    assert np.allclose(g @ g.T, np.eye(7), atol=1e-12)
    act = lambda v: np.r_[v[0], g @ v[1:]]          # действие на 𝕆: вещественная часть неподвижна
    rg = np.random.default_rng(2)
    x, y = np.r_[0, rg.normal(size=7)], np.r_[0, rg.normal(size=7)]
    assert np.allclose(act(omul(x, y)), omul(act(x), act(y)), atol=1e-9)        # g — автоморфизм
    G = np.zeros((7, 7))
    G[0, 0] = 1
    assert abs(integration(G) - 0.0) < 1e-12 and abs(integration(g @ G @ g.T) - 1.0) < 1e-9
    assert abs(coh_e(G, 0) - 1.0) < 1e-12 and abs(coh_e(g @ G @ g.T, 0) - 0.75) < 1e-9
    assert abs(purity(G) - purity(g @ G @ g.T)) < 1e-12                        # P инвариантна


def test_phi_of_a_product_factorises():
    """1 + Φ(Γ₁⊗Γ₂) = (1 + Φ₁)(1 + Φ₂): два несвязанных состояния окна дают Φ₁₂ ≥ 3 при I(1:2) = 0.

    Свидетель отзыва «категорной нередуцируемости» (панпсихизм, §2) и критерия Φ_⊗ > Φ_min
    предсказания 5 (25.09.2026): интеграция совместной матрицы произведения задана частями и
    корреляции частей не отмечает — её отмечает взаимная информация (CC-7).
    """
    rng = np.random.default_rng(12)
    for _ in range(20):
        pair = []
        for _ in range(2):
            A = rng.normal(size=(7, 7)) + 1j * rng.normal(size=(7, 7))
            G = A @ A.conj().T
            pair.append(G / np.trace(G).real)
        Ga, Gb = pair
        lhs = 1 + integration(np.kron(Ga, Gb))
        assert abs(lhs - (1 + integration(Ga)) * (1 + integration(Gb))) < 1e-10 * lhs
    u = np.ones(7) / np.sqrt(7)
    Gw = 0.5 * np.outer(u, u) + 0.5 * np.eye(7) / 7            # P = 5/14, R = 2/5, Φ = 3/2
    P = purity(Gw)
    assert abs(P - 5 / 14) < 1e-12 and abs(integration(Gw) - 1.5) < 1e-12
    assert 2 / 7 < P <= 3 / 7 and 1 / (7 * P) >= 1 / 3           # окно пройдено
    G12 = np.kron(Gw, Gw)
    assert abs(integration(G12) - 21 / 4) < 1e-10                # Φ₁₂ = 21/4 без всякой связи
    entropy = lambda M: float(-sum(w * np.log(w) for w in np.linalg.eigvalsh(M) if w > 1e-15))
    G4 = G12.reshape(7, 7, 7, 7)
    mutual = entropy(np.einsum("ijkj->ik", G4)) + entropy(np.einsum("ijil->jl", G4)) - entropy(G12)
    assert abs(mutual) < 1e-10                                   # I(1:2) = 0
    lam = np.sqrt(1 / 6)
    Gt = lam * np.outer(u, u) + (1 - lam) * np.eye(7) / 7        # Φ = 1 ровно, P = 2/7
    assert abs(integration(Gt) - 1) < 1e-12 and abs(integration(np.kron(Gt, Gt)) - 3) < 1e-10


def test_window_predicate_not_constant_on_g2_orbit():
    """g ∈ G₂ переводит состояние окна (P = 5/14, R = 2/5, Φ = 3/2) в диагональное: Φ = 0 при тех же P, R.

    Свидетель отзыва «предикат сознания постоянен на G₂-орбите» (замечание к T-253, доказательство
    T-153a, двухаспектный монизм, «Вселенная как голоном», 25.09.2026). G₂ транзитивна на S⁶:
    элемент, переводящий равномерный вектор u в e₁, снимает все когерентности, не меняя спектра,
    и C = Φ·R падает с 3/5 до 0.
    """
    u, e1 = np.ones(7) / np.sqrt(7), np.eye(7)[0]
    g_of = lambda c: expm(sum(ci * X for ci, X in zip(c, G2)))
    fit = least_squares(lambda c: g_of(c) @ u - e1, np.full(14, 0.1), xtol=1e-15, ftol=1e-15, gtol=1e-15)
    g = g_of(fit.x)
    assert np.allclose(g @ u, e1, atol=1e-9) and np.allclose(g @ g.T, np.eye(7), atol=1e-12)
    act = lambda v: np.r_[v[0], g @ v[1:]]
    rg = np.random.default_rng(13)
    x, y = np.r_[0, rg.normal(size=7)], np.r_[0, rg.normal(size=7)]
    assert np.allclose(act(omul(x, y)), omul(act(x), act(y)), atol=1e-9)      # g ∈ Aut(𝕆) = G₂
    Gw = 0.5 * np.outer(u, u) + 0.5 * np.eye(7) / 7
    P = purity(Gw)
    assert 2 / 7 < P <= 3 / 7 and 1 / (7 * P) >= 1 / 3 and integration(Gw) >= 1   # окно пройдено
    assert abs(integration(Gw) / (7 * P) - 0.6) < 1e-12                           # C = 3/5
    Gg = g @ Gw @ g.T
    assert abs(purity(Gg) - P) < 1e-12 and integration(Gg) < 1e-9                 # Φ: 3/2 → 0, C → 0


def test_frame_rigidity_no_continuous_symmetry_of_phi():
    """dim{X ∈ 𝔤₂ : δ_XΦ = 0} = 0 и то же в 𝔰𝔬(7) — Банах–Ламперти в первом порядке."""
    rng = np.random.default_rng(4)
    so7 = []
    for i in range(7):
        for j in range(i + 1, 7):
            X = np.zeros((7, 7))
            X[i, j], X[j, i] = 1, -1
            so7.append(X)
    for basis in (G2, so7):
        rows = []
        for _ in range(80):
            v = rng.normal(size=7)
            v /= np.linalg.norm(v)
            rows.append([4 * np.sum(v ** 3 * (X @ v)) for X in basis])
        assert len(basis) - np.linalg.matrix_rank(np.array(rows)) == 0


def test_frame_group_order_and_singer_subgroups():
    """|Γ_oct| = 1344 = 8·168; элементов порядка 7 — 48, то есть 8 зингеровых подгрупп."""
    total, perms, signs_only = 0, set(), 0
    lines0 = {tuple(sorted((a - 1, b - 1, c - 1))) for a, b, c in LINES}
    for perm in itertools.permutations(range(7)):
        if not all(tuple(sorted(perm[i] for i in l)) in lines0 for l in lines0):
            continue
        P = np.zeros((7, 7))
        for i, pi in enumerate(perm):
            P[pi, i] = 1
        for sg in itertools.product((1, -1), repeat=7):
            M = P * np.array(sg)[None, :]
            if np.allclose(np.einsum("ia,jb,kc,abc->ijk", M, M, M, PHI3), PHI3, atol=1e-9):
                total += 1
                perms.add(perm)
                signs_only += perm == tuple(range(7))
    assert (total, len(perms), signs_only) == (1344, 168, 8)

    def order(p):
        q, n = p, 1
        while q != tuple(range(7)):
            q, n = tuple(p[i] for i in q), n + 1
        return n

    assert sum(order(p) == 7 for p in perms) // 6 == 8


def test_stabiliser_lattice():
    """dim Stab(e_O) = 8 (su(3)), dim Stab(e_E,e_O) = 3 (su(2)); Coh_E выживает при SU(2), Φ — нет."""
    def stab_null(vecs):
        A = np.array([np.concatenate([X @ v for v in vecs]) for X in G2]).T
        U, s, Vt = np.linalg.svd(A)
        return Vt[np.sum(s > 1e-9):]

    eO, eE = np.eye(7)[O_AXIS], np.eye(7)[E_AXIS]
    assert stab_null([eO]).shape[0] == 8
    ns = stab_null([eE, eO])
    assert ns.shape[0] == 3
    rng = np.random.default_rng(5)
    c = rng.normal(size=ns.shape[0])
    X = sum(c[a] * ns[a][b] * G2[b] for a in range(ns.shape[0]) for b in range(14))
    g = expm(0.6 * X)
    A = rng.normal(size=(7, 7))
    G = A @ A.T
    G /= np.trace(G)
    assert abs(coh_e(G) - coh_e(g @ G @ g.T)) < 1e-9          # Coh_E инвариантна
    assert abs(integration(G) - integration(g @ G @ g.T)) > 1e-3   # Φ — нет


def test_fano_dissipator_breaks_g2():
    """D_Fano = ⅔·D_atom, не G₂-ковариантен; канонический D_G2 из φ_abc — ковариантен."""
    def Pi(p):
        P = np.zeros((7, 7))
        for i in LINES[p]:
            P[i - 1, i - 1] = 1
        return P

    def d_fano(G):
        out = np.zeros((7, 7), complex)
        for p in range(7):
            L = Pi(p) / np.sqrt(3)
            out += L @ G @ L.T - 0.5 * (L.T @ L @ G + G @ L.T @ L)
        return out

    def d_atom(G):
        return np.diag(np.diag(G)) - G

    def d_g2(G):
        out = np.zeros((7, 7), complex)
        for a in range(7):
            A = PHI3[a] / np.sqrt(6)
            out += A @ G @ A.T - 0.5 * (A.T @ A @ G + G @ A.T @ A)
        return out

    rng = np.random.default_rng(6)
    A = rng.normal(size=(7, 7)) + 1j * rng.normal(size=(7, 7))
    G = A @ A.conj().T
    G /= np.trace(G).real
    assert np.allclose(d_fano(G), (2 / 3) * d_atom(G), atol=1e-12)
    g = expm(0.37 * der_matrix(unit(1), unit(2)) + 0.21 * der_matrix(unit(3), unit(5)))
    assert np.linalg.norm(d_fano(g @ G @ g.T) - g @ d_fano(G) @ g.T) > 1e-2      # ломает G₂
    assert np.linalg.norm(d_g2(g @ G @ g.T) - g @ d_g2(G) @ g.T) < 1e-12         # сохраняет


def test_rho_e_is_scalar_in_7d_and_a_clock_block_in_42d():
    """В 7D ρ_E — скаляр (rank > 1 невыразим); в 42D — блок 7×7 на регистре часов."""
    rng = np.random.default_rng(8)
    A = rng.normal(size=(42, 42)) + 1j * rng.normal(size=(42, 42))
    Gt = A @ A.conj().T
    Gt /= np.trace(Gt).real
    e = np.zeros(6)
    e[E_AXIS] = 1
    Pi = np.kron(np.eye(7), e.reshape(6, 1))       # ℂ⁷ = часы, ℂ⁶ = измерения
    rho = Pi.conj().T @ Gt @ Pi
    assert rho.shape == (7, 7) and np.linalg.matrix_rank(rho) == 7


def test_history_lift_divides_purity_by_seven():
    """Подъём состоянием-историей меняет чистоту: P ↦ P/7 — не изометрия состояний."""
    rng = np.random.default_rng(9)
    A = rng.normal(size=(7, 7)) + 1j * rng.normal(size=(7, 7))
    G = A @ A.conj().T
    G /= np.trace(G).real
    S = np.roll(np.eye(7), 1, axis=0)
    tot = np.zeros((49, 49), complex)
    for k in range(7):
        Sk = np.linalg.matrix_power(S, k)
        tot[7 * k:7 * k + 7, 7 * k:7 * k + 7] = Sk @ G @ Sk.T
    tot /= np.trace(tot).real
    assert abs(purity(G) / purity(tot) - 7) < 1e-9


def test_z7_irreps_are_one_dimensional():
    """Неприводимые представления ℤ₇ одномерны; регулярное — семимерно и распадается на все семь."""
    w = np.exp(2j * np.pi / 7)
    chars = [[w ** (k * n) for n in range(7)] for k in range(7)]
    assert len({round(abs(sum(c)), 9) for c in chars} - {0.0}) == 1   # только тривиальный даёт 7
    reg = np.roll(np.eye(7), 1, axis=0)
    ev = np.linalg.eigvals(reg)
    assert len(ev) == 7 and np.allclose(sorted(np.angle(ev)), sorted(np.angle([w ** k for k in range(7)])))


def test_pw_constraint_kernel_is_at_most_six():
    """Связное пространство PW не может быть 𝒟(ℂ⁷): dim ker Ĉ ≤ 6, то есть ≤ 35 < 48 параметров.

    Свидетель опровержения Морита-эквивалентности T-58 (10.09.2026): у каждого из
    шести нечасовых базисных состояний есть не более одного уровня часов k с
    ω₀k + E_j = 0, поэтому ядро не бывает семимерным ни при какой настройке H_6D.
    """
    w0 = 1.0
    HO = np.diag([w0 * k for k in range(7)])
    rng = np.random.default_rng(0)
    best = 0
    for _ in range(2000):
        E = rng.choice([-w0 * k for k in range(7)], size=6, replace=True)
        C = np.kron(HO, np.eye(6)) + np.kron(np.eye(7), np.diag(E))
        best = max(best, int(np.sum(np.abs(np.diag(C)) < 1e-12)))
    E = np.array([-w0 * j for j in range(6)])          # наилучшая аналитическая настройка
    C = np.kron(HO, np.eye(6)) + np.kron(np.eye(7), np.diag(E))
    assert best == 6 and int(np.sum(np.abs(np.diag(C)) < 1e-12)) == 6
    assert 6 ** 2 - 1 < 7 ** 2 - 1                      # 35 < 48


def test_contractible_space_keeps_degree_zero():
    """На стягиваемом комплексе H⁰ = ℤ ≠ 0, а H^{n>0} = 0 — почему Λ не сокращается.

    Свидетель закрытия вопроса Λ (10.09.2026): вакуумная энергия есть величина
    степени 0 и живёт ровно в той группе, которая НЕ обнуляется.
    """
    rng = np.random.default_rng(3)
    n = 7                                              # конус над случайным графом — стягиваем
    edges = {(i, j) for i in range(n) for j in range(i + 1, n) if rng.random() < 0.5}
    apex = n
    verts = list(range(n + 1))
    edges |= {(i, apex) for i in range(n)}
    tris = {(i, j, apex) for (i, j) in edges if j != apex}
    E, T = sorted(edges), sorted(tris)
    d1 = np.zeros((len(verts), len(E)))
    for c, (i, j) in enumerate(E):
        d1[i, c], d1[j, c] = -1, 1
    d2 = np.zeros((len(E), len(T)))
    idx = {e: k for k, e in enumerate(E)}
    for c, (i, j, k) in enumerate(T):
        d2[idx[(i, j)], c] += 1
        d2[idx[(j, k)], c] += 1
        d2[idx[(i, k)], c] -= 1
    r1, r2 = np.linalg.matrix_rank(d1), np.linalg.matrix_rank(d2)
    h0 = len(verts) - r1
    h1 = (len(E) - r1) - r2
    assert h0 == 1 and h1 == 0                          # H⁰ ≠ 0, H¹ = 0


def main():
    tests = [(n, f) for n, f in sorted(globals().items()) if n.startswith("test_")]
    bad = 0
    for name, fn in tests:
        try:
            fn()
            print(f"  PASS  {name}")
        except AssertionError as exc:
            bad += 1
            print(f"  FAIL  {name}: {exc}")
    print(f"числа ядра: {len(tests) - bad}/{len(tests)} проверок прошли")
    print("правило: утверждение, однажды опровергнутое числом, возвращается только вместе с числом")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
