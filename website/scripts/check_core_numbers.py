#!/usr/bin/env python3
"""ЧИСЛА ЯДРА: регрессионные проверки утверждений, на которых стоит корпус.

Каждая проверка — свидетель одного утверждения корпуса. Три из них родились как
ОШИБКИ, найденные внешним аудитом 10.09.2026, и стоят здесь, чтобы не вернуться:
`kl_at_threshold` (точная D_KL на пороге — 0,344, а не 1/2), `phi_not_g2_invariant`
(Φ не $G_2$-инвариантна) и `z7_irreps_are_one_dimensional` (неприводимые
представления ℤ₇ одномерны, регулярное — семимерно). Ещё три стоят за отзывами
25.09.2026: `phi_of_a_product_factorises` (Φ произведения задана частями — условие
Φ₁₂ > 1 выполняет любая несвязанная пара), `window_predicate_not_constant_on_g2_orbit`
(предикат окна не постоянен на $G_2$-орбите) и `coh_e_is_invariant_only_on_the_e_axis_stabiliser`
(Coh_E сохраняют лишь 192 из 1344 элементов реперной группы Γ_oct — те, что оставляют ось E).
Девять — за отзывами того же дня в основаниях: стрела времени только для унитальных
каналов, `6M+1` показание составных часов вместо `7^M`, стационарность не даёт связи
Пейджа–Вуттерса, селективная регенерация сигналит, поток регенерации не выпукло
квазилинеен, сопряжённый канал замены не сохраняет след, проекторы линий Фано
коммутируют (нет контекстуальности Кохена–Шпекера), ранг $G_2$ равен двум, а
R = 1/(7P) не обращается в нуль.

Четыре — за открытыми вопросами оснований (25.09.2026): селективный запрет
сигнализации требует аффинности, затвор бистабилен, а аффинный и нормированно-линейный
потоки — нет; веса Рембелиньского–Цабана не частоты, записанные A; при чисто точечном
спектре относительная динамика возвращается (соответствие с физикой §8.7, эмерджентное
время §11.3).

Пять добавлены отзывом 25.09.2026 (октонионная линия): `no_axis_triple_is_su3_invariant`
(разложение 1_O ⊕ 3_{A,S,D} ⊕ 3̄_{L,E,U} ложно — 0 инвариантных троек из 20),
`generation_z3_lies_in_colour_su3` (ℤ₃ поколений — элемент SU(3)_C),
`su3_invariant_states_are_coherent_only_on_o_line_pairs`,
`only_16_of_128_fano_orientations_are_normed` (пробел шага T15) и
`gamma5_with_i_has_imaginary_spectrum` (спектр iΓ_OΓ_AΓ_SΓ_D — {±i}, не {±1}).

Одна — за отзывом шагов 2–3 КК-7 (теорема 9.3, аудит A-82):
`coupled_holons_can_have_a_product_stationary_state` (связь, коммутирующая с ρ₁*⊗ρ₂*,
оставляет стационарным произведение, I = 0; локальная связь сдвигает маргиналь без корреляции).

Запуск: `python3 scripts/check_core_numbers.py` или `pytest scripts/check_core_numbers.py`.
"""
import functools
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


@functools.lru_cache(maxsize=None)
def frame_group():
    """Γ_oct полным перебором: знаковые перестановки осей, сохраняющие φ₃, — пары (перестановка, матрица).

    Матрица M переводит e_i в ±e_{perm[i]}. Перебор один на весь прогон: им пользуются две проверки.
    """
    out = []
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
                out.append((perm, M))
    return tuple(out)


def test_frame_group_order_and_singer_subgroups():
    """|Γ_oct| = 1344 = 8·168; элементов порядка 7 — 48, то есть 8 зингеровых подгрупп."""
    group = frame_group()
    perms = {perm for perm, _ in group}
    signs_only = sum(perm == tuple(range(7)) for perm, _ in group)
    assert (len(group), len(perms), signs_only) == (1344, 168, 8)

    def order(p):
        q, n = p, 1
        while q != tuple(range(7)):
            q, n = tuple(p[i] for i in q), n + 1
        return n

    assert sum(order(p) == 7 for p in perms) // 6 == 8


def test_coh_e_is_invariant_only_on_the_e_axis_stabiliser():
    """Φ сохраняют все 1344 элемента Γ_oct, Coh_E — лишь 192 = 1344/7, оставляющие ось E на месте.

    Свидетель исправления решётки групп отождествления и следствия 3 теоремы единственности
    (25.09.2026): строка «Γ_oct: Coh_E инвариантна» была ложной — элемент, уводящий ось E на другую
    ось, переводит Coh_E(|e_E⟩⟨e_E|) из 1 в 0, поэтому ker F лежит в стабилизаторе оси E внутри
    Γ_oct, а не совпадает с Γ_oct. Из 192 элементов 96 оставляют e_E, 96 обращают его в −e_E:
    знака оси Coh_E не видит.
    """
    rng = np.random.default_rng(14)
    states = []
    for _ in range(3):
        A = rng.normal(size=(7, 7)) + 1j * rng.normal(size=(7, 7))
        G = A @ A.conj().T
        states.append(G / np.trace(G).real)
    keeps_phi = keeps_coh = keeps_axis = keeps_vector = 0
    for perm, M in frame_group():
        phi = all(abs(integration(M @ G @ M.T) - integration(G)) < 1e-12 for G in states)
        coh = all(abs(coh_e(M @ G @ M.T) - coh_e(G)) < 1e-12 for G in states)
        axis = perm[E_AXIS] == E_AXIS
        assert coh == axis                        # Coh_E сохраняется ровно тогда, когда ось E на месте
        keeps_phi += phi
        keeps_coh += coh
        keeps_axis += axis
        keeps_vector += axis and M[E_AXIS, E_AXIS] == 1
    assert (keeps_phi, keeps_coh, keeps_axis, keeps_vector) == (1344, 192, 192, 96)
    GE = np.zeros((7, 7))
    GE[E_AXIS, E_AXIS] = 1
    perm, M = next(el for el in frame_group() if el[0][E_AXIS] != E_AXIS)
    assert abs(coh_e(GE) - 1) < 1e-12 and abs(coh_e(M @ GE @ M.T)) < 1e-12      # Coh_E: 1 → 0
    assert abs(integration(M @ GE @ M.T) - integration(GE)) < 1e-12              # Φ = 0 не сдвинулась


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


def entropy(G):
    w = np.linalg.eigvalsh(G)
    w = w[w > 1e-15]
    return float(-(w * np.log(w)).sum())


def random_state(rng, d=7):
    A = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    G = A @ A.conj().T
    return G / np.trace(G).real


def random_pure(rng, d=7):
    v = rng.normal(size=d) + 1j * rng.normal(size=d)
    v /= np.linalg.norm(v)
    return np.outer(v, v.conj())


def gate(P):
    """Шлюз жизнеспособности g_V(P) = clamp(7P − 2, 0, 1)."""
    return float(np.clip(7 * P - 2, 0, 1))


def test_reset_channel_lowers_entropy_unital_does_not():
    """Стрела времени — только для унитальных каналов: сброс X ↦ Tr(X)|0⟩⟨0| снижает S с log 7 до 0.

    Свидетель отзыва 25.09.2026 (T-53c, п. 3; теорема 7.1 эмерджентного времени):
    «всякая CPTP-эволюция не уменьшает энтропию» ложно для неунитальных каналов.
    Для унитальных (здесь — смеси унитарных) энтропия не падает.
    """
    rng = np.random.default_rng(21)
    reset = np.zeros((7, 7))
    reset[0, 0] = 1.0                                   # образ любого состояния при сбросе
    assert abs(entropy(np.eye(7) / 7) - np.log(7)) < 1e-12 and entropy(reset) < 1e-12
    worst = np.inf
    for _ in range(100):
        G = random_state(rng)
        Us = [np.linalg.qr(rng.normal(size=(7, 7)) + 1j * rng.normal(size=(7, 7)))[0] for _ in range(3)]
        p = rng.dirichlet(np.ones(3))
        out = sum(pk * U @ G @ U.conj().T for pk, U in zip(p, Us))
        worst = min(worst, entropy(out) - entropy(G))
    assert worst > -1e-10


def test_composite_clock_has_6m_plus_1_readings():
    """M одинаковых O-часов: 6M+1 различимое показание и период 2π/ω₀, а не 7^M.

    Свидетель отзыва 25.09.2026 (эмерджентное время §3.8, T-118): 7^M — размерность
    пространства часов; число показаний 7^M дают лишь позиционные частоты 1 : 7 : 7², …
    """
    T1 = np.arange(7.0)
    for M in range(1, 5):
        total = np.zeros(1)
        for _ in range(M):
            total = np.add.outer(total, T1).ravel()     # спектр T_comp = Σ T⁽ᵐ⁾
        assert len(np.unique(np.round(total, 9))) == 6 * M + 1
        assert np.allclose(np.exp(-2j * np.pi * total), 1)      # период 2π при ω₀ = 1
    positional = np.add.outer(T1, 7 * T1).ravel()
    assert len(np.unique(positional)) == 49                      # 7² только при частотах 1 : 7


def test_stationarity_is_not_the_pw_constraint():
    """[Ĉ, Γ] = 0 не влечёт ĈΓ = 0: связь PW требует supp Γ ⊆ ker Ĉ.

    Свидетель отзыва 25.09.2026 (T-87, шаг 4): Γ = ½(|a⟩⟨a| + |b⟩⟨b|) на двух
    собственных векторах Ĉ с c_a ≠ c_b стационарна, но не лежит ни в каком
    собственном подпространстве Ĉ, тем более в ядре.
    """
    w0 = 1.0
    HO = np.diag([w0 * k for k in range(7)])
    E = np.array([-w0 * j for j in range(6)])
    C = np.kron(HO, np.eye(6)) + np.kron(np.eye(7), np.diag(E))
    c = np.real(np.diag(C))
    a, b = 1 * 6 + 0, 2 * 6 + 0                        # (k=1, j=0) и (k=2, j=0): c = 1 и 2
    G = np.zeros((42, 42))
    G[a, a] = G[b, b] = 0.5
    assert np.linalg.norm(C @ G - G @ C) < 1e-12
    assert min(np.linalg.norm((C - s * np.eye(42)) @ G) for s in (c[a], c[b], 0.0)) > 0.3
    ker = [i for i in range(42) if abs(c[i]) < 1e-12]  # (k=j, j): ω₀k + E_j = 0
    Gk = np.zeros((42, 42))
    for i in ker:
        Gk[i, i] = 1 / len(ker)
    assert np.linalg.norm(C @ Gk) < 1e-12              # supp Γ ⊆ ker Ĉ ⟺ ĈΓ = 0


def test_selective_regeneration_signals():
    """Шлюз g_V делает регенерацию сигнальной при обновлении Людерса у партнёра.

    Свидетель отзыва 25.09.2026 (соответствие с физикой §8.5): кутрит A и голоном B
    в состоянии (1/√3)Σ|k⟩|e_k⟩. Без измерения у A: P(ρ_B) = 1/3, g_V = 1/3; с
    измерением: ветви чистые, g_V = 1 — начальный дрейф втрое больше. При κ,
    зависящей от Coh_E, различаются уже два базиса измерения A.
    """
    e = np.eye(7)
    rho_star = np.diag([0.6, 0.25, 0.15, 0, 0, 0, 0])
    branches = [np.outer(e[k], e[k]) for k in range(3)]
    rho_b = sum(branches) / 3
    assert abs(purity(rho_b) - 1 / 3) < 1e-12 and abs(gate(purity(rho_b)) - 1 / 3) < 1e-12
    drift = lambda G, kappa: kappa(G) * gate(purity(G)) * (rho_star - G)
    const = lambda G: 1.0
    d_no = drift(rho_b, const)
    d_meas = sum(drift(br, const) for br in branches) / 3
    assert np.allclose(d_meas, 3 * d_no) and np.linalg.norm(d_meas - d_no) > 0.1
    kappa_e = lambda G: 1.0 + coh_e(G)
    z = [np.outer(e[E_AXIS], e[E_AXIS]), np.outer(e[O_AXIS], e[O_AXIS])]
    plus, minus = (e[E_AXIS] + e[O_AXIS]) / np.sqrt(2), (e[E_AXIS] - e[O_AXIS]) / np.sqrt(2)
    x = [np.outer(plus, plus), np.outer(minus, minus)]
    assert np.allclose(sum(z) / 2, sum(x) / 2)         # одно и то же среднее состояние B
    dz = sum(drift(br, kappa_e) for br in z) / 2
    dx = sum(drift(br, kappa_e) for br in x) / 2
    assert np.linalg.norm(dz - dx) > 0.1


def test_regenerative_flow_is_not_convex_quasilinear():
    """Образ смеси под потоком регенерации лежит вне отрезка между образами частей.

    Свидетель к соответствию с физикой §8.5: выпуклая квазилинейность
    (Rembieliński–Caban) исключила бы сигнализацию, но поток с каноническими κ(Γ),
    g_V и дефазирующей линейной частью ею не обладает; линейная часть сама по
    себе аффинна (контроль).
    """
    rng = np.random.default_rng(11)
    rho_star = np.diag([0.6, 0.25, 0.15, 0, 0, 0, 0]).astype(complex)
    H = rng.normal(size=(7, 7))
    H = (H + H.T) / 2

    def flow(G, nonlinear=True, t=0.5, n=200):
        G = G.astype(complex).copy()
        h = t / n

        def rhs(X):
            out = -1j * (H @ X - X @ H) + 0.3 * (np.diag(np.diag(X)) - X)
            if nonlinear:
                out = out + (1.0 + coh_e(X)) * gate(purity(X)) * (rho_star - X)
            return out
        for _ in range(n):
            k1 = rhs(G)
            k2 = rhs(G + h / 2 * k1)
            k3 = rhs(G + h / 2 * k2)
            k4 = rhs(G + h * k3)
            G = G + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        return G

    def off_segment(X, A, B):
        D = B - A
        s = min(1.0, max(0.0, np.real(np.vdot(D, X - A)) / np.real(np.vdot(D, D))))
        return np.linalg.norm(X - (A + s * D)) / np.linalg.norm(D)

    rel = []
    for _ in range(6):
        r1, r2 = random_pure(rng), random_pure(rng)
        lam = rng.uniform(0.2, 0.8)
        mix = lam * r1 + (1 - lam) * r2
        rel.append(off_segment(flow(mix), flow(r1), flow(r2)))
        if len(rel) <= 2:
            assert off_segment(flow(mix, False), flow(r1, False), flow(r2, False)) < 1e-9
    assert min(rel) > 0.01


def test_replacement_channel_adjoint_is_not_trace_preserving():
    """Кинжал Φ† := Φ* не замкнут в CPTP: у канала замены Φ(X) = Tr(X)σ сопряжённый Φ*(Y) = Tr(σY)·I.

    Свидетель отзыва 25.09.2026 (определение 7.3 категорного формализма).
    """
    sigma = np.zeros((7, 7))
    sigma[0, 0] = 1.0
    rho = sigma.copy()
    adj = np.trace(sigma @ rho) * np.eye(7)
    X, Y = random_state(np.random.default_rng(5)), random_state(np.random.default_rng(6))
    assert abs(np.trace(np.trace(X) * sigma @ Y) - np.trace(X @ (np.trace(sigma @ Y) * np.eye(7)))) < 1e-12
    assert abs(np.trace(adj) - 7) < 1e-12              # след 7, а не 1


def test_fano_line_projectors_commute_hence_noncontextual():
    """Проекторы линий Фано диагональны, попарно коммутируют и имеют общее распределение p_i = γ_ii.

    Свидетель отзыва T-201 (25.09.2026): контекстуальности Кохена–Шпекера нет.
    """
    P = [np.diag([1.0 if i + 1 in line else 0.0 for i in range(7)]) for line in LINES]
    for A in P:
        for B in P:
            assert np.linalg.norm(A @ B - B @ A) < 1e-15
    G = random_state(np.random.default_rng(7))
    p = np.real(np.diag(G))
    for A, line in zip(P, LINES):
        assert abs(np.real(np.trace(A @ G)) - sum(p[i - 1] for i in line)) < 1e-12
        for B, other in zip(P, LINES):
            both = set(line) & set(other)
            assert abs(np.real(np.trace(A @ B @ G)) - sum(p[i - 1] for i in both)) < 1e-12


def test_g2_rank_is_two():
    """Ранг G₂ равен 2: централизатор общего элемента 𝔤₂ двумерен; у SU(3)×SU(2)×U(1) ранг 4.

    Свидетель отзыва 25.09.2026 (T-275): вложение калибровочной группы Стандартной
    модели в G₂ невозможно по рангу.
    """
    rng = np.random.default_rng(12)
    X = sum(c * g for c, g in zip(rng.normal(size=14), G2))
    ad = np.array([(X @ g - g @ X).ravel() for g in G2]).T
    assert 14 - np.linalg.matrix_rank(ad, tol=1e-9) == 2 < 2 + 1 + 1


def test_reflection_measure_never_vanishes():
    """R = 1/(7P) ∈ [1/7, 1]: подкатегория Hol с R = 0 пуста.

    Свидетель отзыва 25.09.2026 (теорема 3.3 редукции к КМ).
    """
    rng = np.random.default_rng(13)
    Ps = [purity(random_state(rng)) for _ in range(200)] + [1 / 7, 1.0]
    R = np.array([1 / (7 * P) for P in Ps])
    assert R.min() >= 1 / 7 - 1e-12 and R.max() <= 1 + 1e-12


def _su3_of_e_o():
    """Базис 𝔰𝔲(3) = Stab_{𝔤₂}(e_O): восемь антисимметричных матриц 7×7."""
    A = np.array([X @ np.eye(7)[O_AXIS] for X in G2]).T
    _, s, Vt = np.linalg.svd(A)
    ns = Vt[np.sum(s > 1e-9):]
    return [sum(ns[a][b] * G2[b] for b in range(14)) for a in range(ns.shape[0])]


def test_no_axis_triple_is_su3_invariant():
    """Ни одна тройка из шести осей ≠ O не инвариантна под SU(3) = Stab(e_O): 0 из 20.

    Свидетель отзыва 25.09.2026: разложение «7 = 1_O ⊕ 3_{A,S,D} ⊕ 3̄_{L,E,U}» и его
    вещественная форма ℝ¹⊕ℝ³⊕ℝ³ ложны. Коммутант 𝔰𝔲(3) на ℝ⁶ двумерен (ℝ⁶ неприводимо,
    комплексного типа); L_{e_O} спаривает A↔D, S↔U, L↔E, и триплет есть
    span_ℂ{A−iD, S−iU, L−iE}. Размах {A,S,D} сохраняет лишь одномерная 𝔲(1) ⊂ 𝔰𝔲(3).
    Метки осей: A,S,D,L,E,U,O = e₁…e₇ (таблица g2-structure §2.2).
    """
    su3 = _su3_of_e_o()
    assert len(su3) == 8
    invariant = []
    for T in itertools.combinations(range(6), 3):
        P = np.zeros((7, 7))
        P[list(T), list(T)] = 1
        if max(np.abs((np.eye(7) - P) @ X @ P).max() for X in su3) < 1e-9:
            invariant.append(T)
    assert invariant == []
    comm = np.vstack([np.kron(X[:6, :6].T, np.eye(6)) - np.kron(np.eye(6), X[:6, :6]) for X in su3])
    assert 36 - np.linalg.matrix_rank(comm, tol=1e-9) == 2
    Lo = np.array([omul(unit(7), unit(i + 1))[1:] for i in range(7)]).T
    assert np.allclose((Lo @ Lo)[:6, :6], -np.eye(6))
    assert all(abs(Lo[j, i] - 1) < 1e-12 for i, j in ((0, 2), (1, 5), (3, 4)))   # A→D, S→U, L→E
    for a, d in ((0, 2), (1, 5), (3, 4)):                                         # A−iD, S−iU, L−iE ∈ 𝟑
        v = np.zeros(7, complex)
        v[a], v[d] = 1, -1j
        assert np.allclose(Lo @ v, 1j * v)
    P = np.zeros((7, 7))
    P[[0, 1, 2], [0, 1, 2]] = 1
    M = np.array([((np.eye(7) - P) @ X @ P).flatten() for X in su3]).T
    assert len(su3) - np.linalg.matrix_rank(M, tol=1e-9) == 1                     # только 𝔲(1) сохраняет {A,S,D}


def test_generation_z3_lies_in_colour_su3():
    """σ: e_k ↦ e_{2k mod 7} — автоморфизм 𝕆, закрепляющий e_O = e₇, то есть элемент SU(3)_C.

    Свидетель отзыва 25.09.2026 (Теорема 5.2 поколений): в базисе A−iD, S−iU, L−iE
    триплета σ — циклическая перестановка с det = 1, и log σ ∈ 𝔰𝔲(3). Вакуум,
    ломающий ⟨σ⟩, ломает SU(3)_C; ⟨σ⟩ не сохраняет и пару (E,U): σ(E,U) = (D,E).
    """
    def sig(k):
        return (2 * k) % 7 or 7

    S = np.zeros((8, 8))
    S[0, 0] = 1
    for k in range(1, 8):
        S[sig(k), k] = 1
    rng = np.random.default_rng(10)
    for _ in range(20):
        x, y = rng.normal(size=8), rng.normal(size=8)
        assert np.allclose(S @ omul(x, y), omul(S @ x, S @ y), atol=1e-10)
    assert sig(7) == 7 and sorted({tuple(sorted({k, sig(k), sig(sig(k))})) for k in range(1, 8)}) == [(1, 2, 4), (3, 5, 6), (7,)]
    s7 = S[1:, 1:]
    B = np.zeros((7, 3), complex)
    for c, (a, d) in enumerate(((0, 2), (1, 5), (3, 4))):
        B[a, c], B[d, c] = 1, -1j
    M3 = np.linalg.lstsq(B, s7 @ B, rcond=None)[0]
    assert np.allclose(M3, np.roll(np.eye(3), 1, axis=0)) and abs(np.linalg.det(M3) - 1) < 1e-12
    from scipy.linalg import logm
    X = np.real(logm(s7))
    su3 = _su3_of_e_o()
    F = np.array([Y.flatten() for Y in su3]).T
    coef = np.linalg.lstsq(F, X.flatten(), rcond=None)[0]
    assert np.linalg.norm(F @ coef - X.flatten()) < 1e-9
    assert (sig(5), sig(6)) == (3, 5)                                             # (E,U) ↦ (D,E)


def test_su3_invariant_states_are_coherent_only_on_o_line_pairs():
    """SU(3)_C-инвариантная Γ имеет недиагональные элементы лишь на парах (A,D), (S,U), (L,E).

    Отсюда: профиль «Gap одинаков на девяти парах {A,S,D}×{L,E,U}» — не цветовая
    изотропия, а любая когерентность γ_EU ≠ 0 уже нарушает SU(3)_C.
    """
    su3 = _su3_of_e_o()
    basis = []
    for i in range(7):
        for j in range(7):
            E = np.zeros((7, 7), complex)
            E[i, j] = 1
            basis.append(E)
    rows = np.vstack([np.array([(Y @ X - X @ Y).flatten() for Y in basis]).T for X in su3])
    _, s, Vh = np.linalg.svd(rows)
    null = Vh[np.sum(s > 1e-9):]
    assert null.shape[0] == 3                                                     # коммутант ℂ³ (Шур)
    support = {tuple(sorted((i, j))) for v in null for i in range(7) for j in range(7)
               if i != j and abs(v.reshape(7, 7)[i, j]) > 1e-9}
    assert support == {(0, 2), (1, 5), (3, 4)}


def test_only_16_of_128_fano_orientations_are_normed():
    """Из 2⁷ = 128 ориентаций семи линий Фано нормированную алгебру дают ровно 16.

    Свидетель пробела шага T15 (25.09.2026): T12–T14 дают неориентированный BIBD(7,3,1);
    ориентация — вход (Alt), а не выход. Шестнадцать — одна орбита смен знаков
    e_i ↦ −e_i (стабилизатор порядка 8: тождество и семь дополнений линий).
    """
    rng = np.random.default_rng(11)
    samples = [(rng.normal(size=8), rng.normal(size=8)) for _ in range(4)]

    def normed(signs):
        lines = [(i, j, k) if s > 0 else (j, i, k) for (i, j, k), s in zip(LINES, signs)]

        def mul(a, b):
            c = np.zeros(8)
            c[0] = a[0] * b[0] - np.dot(a[1:], b[1:])
            c[1:] += a[0] * b[1:] + b[0] * a[1:]
            for i, j, k in lines:
                for x, y, z in ((i, j, k), (j, k, i), (k, i, j)):
                    c[z] += a[x] * b[y] - a[y] * b[x]
            return c
        return all(abs(np.linalg.norm(mul(x, y)) - np.linalg.norm(x) * np.linalg.norm(y)) < 1e-9
                   for x, y in samples)

    good = {s for s in itertools.product((1, -1), repeat=7) if normed(s)}
    assert len(good) == 16 and (1,) * 7 in good

    def flip(signs, S):
        return tuple(-s if sum(p in S for p in line) % 2 else s for line, s in zip(LINES, signs))

    subsets = [set(c) for r in range(8) for c in itertools.combinations(range(1, 8), r)]
    assert {flip((1,) * 7, S) for S in subsets} == good


def test_gamma5_with_i_has_imaginary_spectrum():
    """В соглашении Γ_iΓ_j + Γ_jΓ_i = −2δ_ij (левое умножение в 𝕆): (Γ_OΓ_AΓ_SΓ_D)² = +1.

    Свидетель отзыва 25.09.2026 (Стандартная модель §4.3): «γ₅ = iΓ_OΓ_AΓ_SΓ_D с
    собственными значениями ±1» ложно — спектр iΓ_OΓ_AΓ_SΓ_D есть {±i}; так для всех 35 четвёрок.
    """
    def lmul(i):
        return np.array([omul(unit(i), unit(j)) for j in range(8)]).T

    G = [lmul(i) for i in range(1, 8)]
    assert all(np.allclose(G[a] @ G[b] + G[b] @ G[a], -2 * (a == b) * np.eye(8)) for a in range(7) for b in range(7))
    for q in itertools.combinations(range(7), 4):
        P = G[q[0]] @ G[q[1]] @ G[q[2]] @ G[q[3]]
        assert np.allclose(P @ P, np.eye(8))
    P = G[O_AXIS] @ G[0] @ G[1] @ G[2]                                            # O, A, S, D
    ev = np.linalg.eigvals(1j * P)
    assert np.allclose(np.abs(ev.imag), 1) and np.allclose(ev.real, 0)


def _rk4(G, rhs, t, n):
    G = G.astype(complex).copy()
    h = t / n
    for _ in range(n):
        k1 = rhs(G)
        k2 = rhs(G + h / 2 * k1)
        k3 = rhs(G + h / 2 * k2)
        k4 = rhs(G + h * k3)
        G = G + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return G


def _phi_coh_fixed(G, k=0.8, alpha=0.4):
    """φ_coh с фиксированными k и α: CPTP и унитальный канал (вариант C соответствия с физикой §8.7)."""
    Pis = []
    for line in LINES:
        P = np.zeros((7, 7))
        for i in line:
            P[i - 1, i - 1] = 1
        Pis.append(P)
    fano = sum(P @ G @ P for P in Pis) / 3
    return k * (alpha * np.diag(np.diag(G)) + (1 - alpha) * fano) + (1 - k) * np.eye(7) / 7


def test_selective_no_signalling_needs_affinity():
    """Селективный запрет сигнализации держит член с постоянным темпом и рушит член с затвором.

    Свидетель к соответствию с физикой §8.7: A управляет разложением ρ_B (HJW) через
    случайное измерение на очищении; линейный член c̄(φ̄(Γ) − Γ) даёт одинаковый дрейф
    ветвей и безусловного состояния (до 1e-12), член g_V(P)(ρ* − Γ) на ρ_B с P < 2/7 —
    нет: безусловный затвор закрыт, чистые ветви его открывают.
    """
    rng = np.random.default_rng(5)
    rho_b = random_state(rng)
    assert purity(rho_b) < 2 / 7
    rho_star = np.diag([0.6, 0.25, 0.15, 0, 0, 0, 0])
    w, V = np.linalg.eigh(rho_b)
    psi = sum(np.sqrt(max(w[i], 0)) * np.kron(np.eye(7)[i], V[:, i]) for i in range(7))
    lin = lambda G: 1.3 * (_phi_coh_fixed(G) - G)
    gated = lambda G: gate(purity(G)) * (rho_star - G)
    worst_lin, least_gated = 0.0, np.inf
    for _ in range(20):
        n = int(rng.integers(7, 14))
        U = np.linalg.qr(rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)))[0][:, :7]
        M = (np.kron(U, np.eye(7)) @ psi).reshape(n, 7)
        ps = [np.vdot(v, v).real for v in M]
        brs = [np.outer(v, v.conj()) / p for v, p in zip(M, ps) if p > 1e-14]
        ps = [p for p in ps if p > 1e-14]
        assert np.allclose(sum(p * b for p, b in zip(ps, brs)), rho_b)
        worst_lin = max(worst_lin, np.linalg.norm(sum(p * lin(b) for p, b in zip(ps, brs)) - lin(rho_b)))
        least_gated = min(least_gated, np.linalg.norm(sum(p * gated(b) for p, b in zip(ps, brs)) - gated(rho_b)))
    assert worst_lin < 1e-12 and least_gated > 0.5


def test_gate_bistability_excludes_affine_and_quasilinear_flows():
    """Затвор бистабилен, а аффинный и нормированно-линейный потоки бистабильными быть не могут.

    Свидетель к соответствию с физикой §8.7: γ(I/7 − Γ) + κ g_V(P)(ρ* − Γ) при γ = 0,3,
    κ = 10 притягивает и I/7, и живое состояние с P ≈ 0,4275; без затвора аттрактор один.
    Для класса Рембелиньского–Цабана ρ̇ = Lρ − ρ Tr(Lρ) точка отрезка между собственными
    состояниями движется по логистическому закону, и все базисные старты уходят в одно.
    """
    I7 = np.eye(7) / 7
    rho_star = np.diag([0.6, 0.25, 0.15, 0, 0, 0, 0]).astype(complex)
    gam, kap = 0.3, 10.0
    full = lambda G: gam * (I7 - G) + kap * gate(purity(G)) * (rho_star - G)
    dead = _rk4(0.4 * I7 + 0.6 * rho_star, full, 40.0, 2000)
    alive = _rk4(0.2 * I7 + 0.8 * rho_star, full, 40.0, 2000)
    assert np.linalg.norm(dead - I7) < 1e-4 and abs(purity(alive) - 0.4275) < 1e-3
    linear = lambda G: gam * (I7 - G) + kap * (rho_star - G)
    ends = [_rk4(G0, linear, 40.0, 2000) for G0 in (I7, rho_star, (I7 + rho_star) / 2)]
    assert max(np.linalg.norm(e - ends[0]) for e in ends) < 1e-10
    rng = np.random.default_rng(7)
    Gd = np.diag(rng.normal(size=7))
    Ls = [np.diag(rng.normal(size=7)) for _ in range(2)]
    L = lambda X: Gd @ X + X @ Gd + sum(K @ X @ K.conj().T for K in Ls)
    rc = lambda X: L(X) - X * np.trace(L(X)).real
    basis = [np.diag(np.eye(7)[i]).astype(complex) for i in range(7)]
    mu = [np.trace(L(b)).real for b in basis]
    s0, t = 0.3, 0.7
    Xt = _rk4((1 - s0) * basis[0] + s0 * basis[1], rc, t, 700)
    s_pred = s0 * np.exp(t * mu[1]) / ((1 - s0) * np.exp(t * mu[0]) + s0 * np.exp(t * mu[1]))
    assert abs(np.real(Xt[1, 1]) - s_pred) < 1e-10
    top = int(np.argmax(mu))
    for b in basis:
        end = _rk4(0.97 * b + 0.03 * I7, rc, 30.0, 3000)
        assert int(np.argmax(np.real(np.diag(end)))) == top


def test_rembielinski_caban_weights_are_not_recorded_frequencies():
    """Кубит Рембелиньского–Цабана — локальный фильтр; при записанных частотах A сигнал Жизена возвращается.

    Свидетель к соответствию с физикой §8.7: формула (14) PRR 2, 012027 совпадает с
    ρ ↦ AρA†/Tr(AρA†), A = exp(gt σ_z/2); при gt = 1 и весах ½ компонента Блоха B вдоль e
    равна 0,668 при e·ζ = ½ и 0,762 при e·ζ = 0; веса λ(t) (24) восстанавливают tanh(gt).
    """
    sig = [np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.diag([1.0, -1.0])]
    e, gt = np.array([0.0, 0.0, 1.0]), 1.0
    A = expm(gt / 2 * sig[2])

    def rc14(xi):
        c, s = np.cosh(gt), np.sinh(gt)
        return (xi + e * (s + (c - 1) * (e @ xi))) / (c + (e @ xi) * s)
    xi = np.array([0.3, -0.2, 0.5])
    rho = 0.5 * (np.eye(2) + sum(xi[k] * sig[k] for k in range(3)))
    out = A @ rho @ A.conj().T
    out = out / np.trace(out).real
    assert np.allclose(np.real([np.trace(out @ s) for s in sig]), rc14(xi), atol=1e-14)
    z = {}
    for ce in (0.0, 0.5):
        zeta = np.array([np.sqrt(1 - ce ** 2), 0.0, ce])
        b1, b2 = rc14(-zeta), rc14(zeta)
        lam = 0.5 * (1 - ce * np.tanh(gt))
        assert abs((lam * b1 + (1 - lam) * b2)[2] - np.tanh(gt)) < 1e-12
        z[ce] = 0.5 * (b1 + b2)[2]
    assert abs(z[0.0] - 0.7616) < 1e-4 and abs(z[0.5] - 0.6681) < 1e-4


def test_finite_dimensional_relational_dynamics_recurs():
    """При чисто точечном спектре диссипации нет ни относительно каких часов.

    Свидетель к эмерджентному времени §11.3: замкнутая система 7 × 8 со случайным
    гамильтонианом — D(ρ_S‖I/7) падает с log 7 и затем снова растёт более чем на 0,4;
    двое O-часов с частотами 1 и √2 точно не возвращаются, но при t ≈ 2π·70 состояние
    часов перекрывается с начальным более чем на 0,99.
    """
    rng = np.random.default_rng(3)
    X = rng.normal(size=(56, 56)) + 1j * rng.normal(size=(56, 56))
    w, V = np.linalg.eigh((X + X.conj().T) / 2)
    c = V.conj().T @ np.kron(np.eye(7)[0], np.eye(8)[0])

    def D(t):
        M = (V @ (np.exp(-1j * w * t) * c)).reshape(7, 8)
        ev = np.linalg.eigvalsh(M @ M.conj().T)
        ev = ev[ev > 1e-15]
        return np.log(7) + float((ev * np.log(ev)).sum())
    Ds = np.array([D(t) for t in np.linspace(0, 200, 4001)])
    assert abs(Ds[0] - np.log(7)) < 1e-9
    assert (Ds - np.minimum.accumulate(Ds)).max() > 0.4
    k = np.arange(7)
    tau0 = np.ones(7) / np.sqrt(7)
    ov = lambda t: np.prod([abs(np.vdot(tau0, np.exp(-1j * om * k * t) * tau0)) ** 2 for om in (1.0, np.sqrt(2))])
    assert ov(2 * np.pi * 70) > 0.99 and ov(2 * np.pi * 70) < 1 - 1e-6


def _holon_pair_generator(H, sig, mu=1.0, alpha=0.5):
    """Генератор одного воплощённого голонома, продолженный канонически на ℂ⁷ ⊗ ℂ⁷ (фактор 1).

    L[Γ] = −i[H, Γ] + D_Fano[Γ] + κ g_V (φ_coh(Γ) − Γ) + μ (σ_env − Γ): D_Fano = ⅔(diag Γ − Γ),
    φ_coh(Γ) = k[α diag Γ + (1−α) P_Fano(Γ)] + (1−k) I/7 с k = 1 − 1/(7P), P_Fano(Γ)_ij = γ_ij/3
    при i ≠ j; κ = 1/7 + Coh_E, g_V = clamp(7P − 2, 0, 1); последний член — подкачка к якорю
    π(B(x)) = σ_env (T-148). Продолжение — (φ ⊗ id), скаляры κ, g_V, k читаются на маргинали.
    """
    D = np.eye(7)

    def apply(X4, g):
        P = purity(g)
        kap, gv, k = 1 / 7 + coh_e(g), gate(P), 1 - 1 / (7 * P)
        W = (2 / 3) * (D - 1) + kap * gv * (k * (alpha * D + (1 - alpha) * (1 / 3 + 2 / 3 * D)) - 1) - mu
        tr1 = np.einsum("iaib->ab", X4)
        out = -1j * (np.einsum("ij,jakb->iakb", H, X4) - np.einsum("iakb,kj->iajb", X4, H))
        out += W[:, None, :, None] * X4
        out += np.einsum("ij,ab->iajb", kap * gv * (1 - k) * D / 7 + mu * sig, tr1)
        return out
    return apply


def test_coupled_holons_can_have_a_product_stationary_state():
    """Связь двух голономов не обязана коррелировать их стационарное состояние: I(1:2) = 0.

    Свидетель отзыва шагов 2–3 КК-7 (теорема 9.3, 25.09.2026; аудит A-82). Два воплощённых
    голонома с каноническим генератором и стационарными ρ₁*, ρ₂*. (а) Связь
    H_int ∝ (ρ₁* − I/7) ⊗ (ρ₂* − I/7) нелокальна (след по каждому фактору нулевой), но
    коммутирует с ρ₁* ⊗ ρ₂*: произведение стационарно, из случайного состояния на ℂ⁴⁹ поток
    приходит к нему, I ≈ 0. (б) Локальная связь H_A ⊗ I с [H_int, ρ₁*⊗ρ₂*] ≠ 0 сдвигает
    маргиналь, но корреляции не рождает: «L_int(ρ₁*⊗ρ₂*) ≠ 0 ⇒ I > 0» ложно. (в) Общая связь
    X ⊗ Y даёт I > 0 — критерий слабой связи: корреляционная часть [H_int, ρ₁*⊗ρ₂*].
    """
    rng = np.random.default_rng(7)

    def herm(r):
        A = r.normal(size=(7, 7)) + 1j * r.normal(size=(7, 7))
        return (A + A.conj().T) / 2

    def anchor(lam):
        v = rng.normal(size=7) + 1j * rng.normal(size=7)
        v /= np.linalg.norm(v)
        return lam * np.outer(v, v.conj()) + (1 - lam) * np.eye(7) / 7

    gens = [_holon_pair_generator(0.3 * herm(rng), anchor(lam)) for lam in (0.85, 0.8)]

    def rk4(f, X, t, h=0.05):
        for _ in range(int(round(t / h))):
            k1 = f(X)
            k2 = f(X + h / 2 * k1)
            k3 = f(X + h / 2 * k2)
            k4 = f(X + h * k3)
            X = X + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        return X

    marg = lambda X: (np.einsum("ijkj->ik", X.reshape(7, 7, 7, 7)), np.einsum("ijil->jl", X.reshape(7, 7, 7, 7)))
    rho = []
    for a in gens:
        f = lambda G, a=a: np.einsum("iaja->ij", a(np.kron(G, np.eye(7) / 7).reshape(7, 7, 7, 7), G))
        rho.append(rk4(f, np.eye(7, dtype=complex) / 7, 40))
        assert np.linalg.norm(f(rho[-1])) < 1e-12 and purity(rho[-1]) > 2 / 7     # живой аттрактор
    sigma = np.kron(*rho)

    def rhs(X, Hint):
        g1, g2 = marg(X)
        X4 = X.reshape(7, 7, 7, 7)
        out = gens[0](X4, g1)
        out += gens[1](X4.transpose(1, 0, 3, 2), g2).transpose(1, 0, 3, 2)
        return out.reshape(49, 49) - 1j * (Hint @ X - X @ Hint)

    def mutual(X):
        g1, g2 = marg(X)
        return entropy(g1) + entropy(g2) - entropy((X + X.conj().T) / 2)

    I7 = np.eye(7) / 7
    Hc = np.kron(rho[0] - I7, rho[1] - I7)
    Hc *= 0.3 / np.linalg.norm(Hc, 2)
    assert np.linalg.norm(np.einsum("iaib->ab", Hc.reshape(7, 7, 7, 7))) < 1e-12      # нелокальна
    assert np.linalg.norm(Hc @ sigma - sigma @ Hc) < 1e-14 and np.linalg.norm(rhs(sigma, Hc)) < 1e-12
    X = rk4(lambda X: rhs(X, Hc), random_state(np.random.default_rng(100), 49), 24)
    assert np.linalg.norm(X - sigma) < 1e-8 and abs(mutual(X)) < 1e-10              # (а) I = 0
    Hl = np.kron(herm(np.random.default_rng(3)), np.eye(7))
    Hl *= 0.3 / np.linalg.norm(Hl, 2)
    assert np.linalg.norm(Hl @ sigma - sigma @ Hl) > 1e-2
    X = rk4(lambda X: rhs(X, Hl), sigma.astype(complex), 24)
    g1, g2 = marg(X)
    assert np.linalg.norm(X - sigma) > 1e-2 and np.linalg.norm(X - np.kron(g1, g2)) < 1e-8   # (б)
    Hg = np.kron(herm(np.random.default_rng(4)), herm(np.random.default_rng(5)))
    Hg *= 0.3 / np.linalg.norm(Hg, 2)
    X = rk4(lambda X: rhs(X, Hg), sigma.astype(complex), 24)
    assert np.linalg.norm(rhs(X, Hg)) < 1e-8 and mutual(X) > 1e-3                    # (в) I > 0


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
