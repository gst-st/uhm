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

Четыре — за выводом 3+1 взамен отозванного (теорема 48c, 25.09.2026):
`colour_commuting_spacetime_is_h2_of_the_clock_complex` (неподвижная часть h₂(𝕆) под SU(3)_C —
h₂(ℂ_O), сигнатура (1,3), централизатор 𝔰𝔬(1,3) ⊕ 𝔲(1)), `no_rotation_of_the_seven_axes_commutes_with_colour`
(запрет для осей и ассоциативных плоскостей), `octonionic_spinor_is_lepton_plus_quark_weyl` и
`every_non_o_axis_is_half_triplet_and_colour_moves_any_axis_to_any` (что верно вместо 45b и (SA)).


Шесть — за разбором вакуума того же дня (A-90, A-83): `v_gap_cubic_term_is_not_g2_invariant`
(V₃ страницы не G₂- и не SU(3)-инвариантен), `su3_invariant_vacuum_has_no_spontaneous_gap`
(на инвариантном семействе с верными секторами V₃ ≡ 0 и минимум при 𝒢_total = 0),
`v_gap_vacuum_is_unique_up_to_its_symmetries_not_up_to_g2` (самосогласованный вакуум единствен
с точностью до 896 симметрий V, лежит на двух G₂-орбитах, носитель — две линии Фано),
`mean_coherence_with_the_tables_own_eps_o` (ε̄ ≈ 0,53 по 21 паре при ε_O ~ 1; по не-O парам ε_33/√5),
`fano_roles_are_fixed_by_three_non_collinear_marks` (T-177: 168 → 24 → 4 → 1; O и пара κ₀ — 2) и
`gamma_eu_vev_breaks_colour` (⟨γ_EU⟩ ≠ 0 оставляет от 𝔰𝔲(3)_C не более 𝔲(1)).


Три — за восстановлением T-53b и T-118 (эмерджентное время §11.4, 25.09.2026):
`depth_register_carries_the_dissipative_arrow` (относительно цепи показаний со связью
Фейнмана–Китаева диссипативная полугруппа — условная динамика точно, на кольце стрела
ломается ровно на одном шаге), `regenerative_solution_is_a_conditional_history` и
`depth_register_time_algebra_is_the_line`.


Семь — за исправленной сборкой Стандартной модели (25.09.2026, T-350 … T-353):
система Клиффорда iL_{e_k}, J, iJ на ℂ⊗𝕆 единственна и максимальна (𝔰𝔭𝔦𝔫(9));
централизатор цвета в ней — 𝔲(2), нормализатор цвета — 12-мерная 𝔤_SM = 𝔠(R_{e_O});
ядро — ровно ℤ₆; (ℂ⊗𝕆, L_{e_O}) = (3,2)_{1/6} ⊕ (1,2)_{−1/2} и не самосопряжено;
семейная симметрия внутри одной копии невозможна, тройственность вращает 𝔲(1)²
на 120°; десятый генератор возвращает 𝔲(1)_{B−L}; у ℤ₇ три нетривиальные
вещественные гармоники.

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


def _nullspace(M, tol=1e-9):
    _, s, vt = np.linalg.svd(M)
    return vt[np.sum(s > tol):]


def _oconj(x):
    y = -x.copy()
    y[0] = x[0]
    return y


def _h2_of_o():
    """Спин-фактор h₂(𝕆): X = [[a, x], [x̄, b]], координаты (a, b, x₀…x₇); форма — det X = ab − |x|²."""
    Gm = np.zeros((10, 10))
    Gm[0, 1] = Gm[1, 0] = 0.5
    Gm[2:, 2:] = -np.eye(8)
    to_m = lambda v: [[v[0] * unit(0), v[2:]], [_oconj(v[2:]), v[1] * unit(0)]]
    from_m = lambda P: np.concatenate([[P[0][0][0], P[1][1][0]], P[0][1]])
    su3 = []
    for X in _su3_of_e_o():
        Y = np.zeros((10, 10))
        Y[3:, 3:] = X
        su3.append(Y)
    return Gm, to_m, from_m, su3


def _clock_complex_matrix(Mc):
    """Комплексная 2×2 матрица, записанная в ℂ_O = ℝ1 ⊕ ℝe_O: i ↦ e_O = e₇."""
    z = lambda c: c.real * unit(0) + c.imag * unit(7)
    return [[z(Mc[0, 0]), z(Mc[0, 1])], [z(Mc[1, 0]), z(Mc[1, 1])]]


def _omatmul(P, Q):
    return [[omul(P[i][0], Q[0][j]) + omul(P[i][1], Q[1][j]) for j in range(2)] for i in range(2)]


def test_colour_commuting_spacetime_is_h2_of_the_clock_complex():
    """Теорема 48c: пространство-время, коммутирующее с цветом, — h₂(ℂ_O) сигнатуры (1,3).

    (a) 𝕆^{SU(3)} = ℂ_O = span{1, e_O}; комплексные структуры на ℝ⁶, коммутирующие с 𝔰𝔲(3), — ±L_{e_O}.
    (b) h₂(𝕆) ≅ ℝ^{1,9}; его SU(3)-неподвижная часть — h₂(ℂ_O), размерность 4, сигнатура det — (1,3).
    (c) централизатор 𝔰𝔲(3) в 𝔰𝔬(1,9) — размерность 7 = 6 + 1, производная алгебра шестимерна,
        форма Киллинга (3,3), т. е. 𝔰𝔬(1,3) ⊕ 𝔲(1); компактная часть четырёхмерна (𝔰𝔬(3) ⊕ 𝔲(1))
        и неподвижна у неё ровно одна прямая — единица 1₂ (время).
    (d) SL(2,ℂ_O): X ↦ MXM† корректна (скобки не важны), сохраняет det, на h₂(ℂ_O) — собственная
        ортохронная Лоренца, на цветовом дополнении W ≅ ℂ³ тождественна и коммутирует с SU(3).
    Свидетель вывода 25.09.2026 взамен отозванного «3+1 из 7 = 1 ⊕ 3 ⊕ 3̄» (аудит A-31, A-33).
    """
    su3_8 = []
    for X in _su3_of_e_o():
        Y = np.zeros((8, 8))
        Y[1:, 1:] = X
        su3_8.append(Y)
    fixed = _nullspace(np.vstack(su3_8))
    assert fixed.shape[0] == 2 and np.allclose(fixed[:, 1:7], 0)                                     # (a) ℂ_O
    six = [X[:6, :6] for X in _su3_of_e_o()]
    comm = np.vstack([np.kron(X.T, np.eye(6)) - np.kron(np.eye(6), X) for X in six])
    cm = [v.reshape(6, 6, order="F") for v in _nullspace(comm)]
    Lo = np.array([omul(unit(7), unit(i + 1))[1:] for i in range(7)]).T[:6, :6]
    assert len(cm) == 2 and all(np.linalg.matrix_rank(np.array([np.eye(6).ravel(), Lo.ravel(), c.ravel()]), tol=1e-9) == 2 for c in cm)
    Gm, to_m, from_m, su3 = _h2_of_o()
    ev = np.linalg.eigvalsh(Gm)
    assert (np.sum(ev > 0), np.sum(ev < 0)) == (1, 9)
    Fix = _nullspace(np.vstack(su3))
    ev = np.linalg.eigvalsh(Fix @ Gm @ Fix.T)
    assert Fix.shape[0] == 4 and (np.sum(ev > 0), np.sum(ev < 0)) == (1, 3)                          # (b)
    basis = []
    for i in range(10):
        for j in range(10):
            E = np.zeros((10, 10))
            E[i, j] = 1
            basis.append(E)
    so19 = [v.reshape(10, 10) for v in _nullspace(np.array([(E.T @ Gm + Gm @ E).ravel() for E in basis]).T)]
    assert len(so19) == 45
    A = np.vstack([np.array([(Y @ X - X @ Y).ravel() for Y in so19]).T for X in su3])
    cent = [sum(c[k] * so19[k] for k in range(45)) for c in _nullspace(A)]
    assert len(cent) == 7                                                                            # (c)
    br = np.array([(X @ Y - Y @ X).ravel() for X in cent for Y in cent])
    u, s, _ = np.linalg.svd(br.T)
    der = [u[:, k].reshape(10, 10) for k in range(np.sum(s > 1e-9))]
    assert len(der) == 6
    D = np.array([d.ravel() for d in der]).T
    ads = [np.array([np.linalg.lstsq(D, (X @ Y - Y @ X).ravel(), rcond=None)[0] for Y in der]).T for X in der]
    K = np.linalg.eigvalsh(np.array([[np.trace(a @ b) for b in ads] for a in ads]))
    assert (np.sum(K > 1e-9), np.sum(K < -1e-9)) == (3, 3)                                            # 𝔰𝔬(1,3)
    S = np.eye(10)
    S[:2, :2] = [[1, 1], [1, -1]]                                                                    # (a,b) = (t+z, t−z)
    c2 = [np.linalg.inv(S) @ X @ S for X in cent]
    kc = _nullspace(np.array([((X + X.T) / 2).ravel() for X in c2]).T)
    comp = [sum(c[k] * c2[k] for k in range(7)) for c in kc]
    fx = _nullspace(np.vstack(comp))
    assert len(comp) == 4 and fx.shape[0] == 1 and abs(abs(fx[0, 0]) - 1) < 1e-9                    # время = 1₂
    rng = np.random.default_rng(48)
    for _ in range(4):                                                                               # (d)
        Mc = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
        Mc /= np.sqrt(np.linalg.det(Mc))
        Mo = _clock_complex_matrix(Mc)
        Md = [[_oconj(Mo[j][i]) for j in range(2)] for i in range(2)]
        L = np.zeros((10, 10))
        for k in range(10):
            X = to_m(np.eye(10)[k])
            P1, P2 = _omatmul(_omatmul(Mo, X), Md), _omatmul(Mo, _omatmul(X, Md))
            assert np.allclose(from_m(P1), from_m(P2)) and np.allclose(P1[0][0][1:], 0) and np.allclose(P1[1][1][1:], 0)
            L[:, k] = from_m(P1)
        assert np.allclose(L.T @ Gm @ L, Gm) and np.allclose(L[:, 3:9], np.eye(10)[:, 3:9])
        g = expm(sum(c * X for c, X in zip(rng.normal(size=8), su3)))
        assert np.allclose(L @ g, g @ L)
        L4 = (np.linalg.inv(S) @ L @ S)[np.ix_([0, 1, 2, 9], [0, 1, 2, 9])]
        assert abs(np.linalg.det(L4) - 1) < 1e-9 and L4[0, 0] >= 1 - 1e-12


def test_no_rotation_of_the_seven_axes_commutes_with_colour():
    """Запрет: ни одна SO(3) на семи осях голонома не коммутирует с SU(3)_C.

    Централизатор 𝔰𝔲(3) в 𝔤₂ — 0, в 𝔰𝔬(7) — 1 (𝔲(1) = L_{e_O} на ℝ⁶), в 𝔲(7) — 3 (𝔲(1)³).
    Путь (а) — ассоциативные 3-плоскости: у каждой из семи линий Фано стабилизатор в 𝔤₂ шестимерен
    (𝔰𝔬(4)) и действует на плоскости как 𝔰𝔬(3), но пересекается с 𝔰𝔲(3) по 𝔲(2) (линии через O, 4)
    или по 𝔰𝔬(3) (остальные четыре, 3) — вращения плоскости суть цветовые вращения.
    """
    su3 = _su3_of_e_o()
    cen = lambda gens: _nullspace(np.vstack([np.array([(Y @ X - X @ Y).ravel() for Y in gens]).T for X in su3])).shape[0]
    so7 = []
    for i in range(7):
        for j in range(i + 1, 7):
            E = np.zeros((7, 7))
            E[i, j], E[j, i] = 1, -1
            so7.append(E)
    assert (cen(G2), cen(so7)) == (0, 1)
    u7 = [E.astype(complex) for E in so7] + [1j * (np.outer(np.eye(7)[i], np.eye(7)[j]) + np.outer(np.eye(7)[j], np.eye(7)[i])) / (2 if i == j else 1)
                                             for i in range(7) for j in range(i, 7)]
    rows = np.vstack([np.array([(Y @ X - X @ Y).ravel() for Y in u7]).T for X in su3])
    rows = np.vstack([rows.real, rows.imag])
    assert _nullspace(rows).shape[0] == 3
    caps = []
    for line in LINES:
        idx = [p - 1 for p in line]
        P = np.zeros((7, 7))
        P[idx, idx] = 1
        stab = [sum(c[k] * G2[k] for k in range(14))
                for c in _nullspace(np.array([((np.eye(7) - P) @ X @ P).ravel() for X in G2]).T)]
        assert len(stab) == 6 and np.linalg.matrix_rank(np.array([(P @ X @ P).ravel() for X in stab]), tol=1e-9) == 3
        A = np.hstack([np.array([X.ravel() for X in stab]).T, -np.array([X.ravel() for X in su3]).T])
        caps.append((7 in line, _nullspace(A).shape[0]))
    assert sorted(caps) == [(False, 3)] * 4 + [(True, 4)] * 3


def test_octonionic_spinor_is_lepton_plus_quark_weyl():
    """𝕆² под SL(2,ℂ_O) × SU(3)_C: левое умножение ψ ↦ Mψ — представление, коммутирующее с цветом.

    Как ℂ_O-модуль 𝕆 = ℂ_O ⊕ ℂ³, поэтому 𝕆² = (2,1) ⊕ (2,3): вейлевский спинор-синглет и
    вейлевский спинор-триплет. Спин и цвет — разные множители, как требует Коулмен–Мандула.
    """
    rng = np.random.default_rng(49)
    su3_8 = []
    for X in _su3_of_e_o():
        Y = np.zeros((8, 8))
        Y[1:, 1:] = X
        su3_8.append(Y)
    act = lambda Mo, p: [omul(Mo[i][0], p[0]) + omul(Mo[i][1], p[1]) for i in range(2)]
    for _ in range(4):
        M1, M2 = (rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)) for _ in range(2))
        g = expm(sum(c * X for c, X in zip(rng.normal(size=8), su3_8)))
        p = [rng.normal(size=8), rng.normal(size=8)]
        a1, a2, a12 = _clock_complex_matrix(M1), _clock_complex_matrix(M2), _clock_complex_matrix(M1 @ M2)
        assert np.allclose(act(a1, act(a2, p)), act(a12, p))
        assert np.allclose(act(a1, [g @ p[0], g @ p[1]]), [g @ v for v in act(a1, p)])
    Lo8 = np.array([omul(unit(7), unit(i)) for i in range(8)]).T
    assert all(np.allclose(Lo8 @ X, X @ Lo8) for X in su3_8)                       # цвет ℂ_O-линеен


def test_every_non_o_axis_is_half_triplet_and_colour_moves_any_axis_to_any():
    """Что верно вместо 45b и (SA): ось не принадлежит ни 𝟑, ни 𝟑̄, а делится поровну.

    P_𝟑 = (1 − iJ)/2 на ℂ⊗ℝ⁶, J = L_{e_O}: ⟨e_k, P_𝟑 e_k⟩ = 1/2 для всех шести осей. Орбита SU(3)_C
    каждой оси пятимерна, то есть это вся S⁵ ⊂ ℝ⁶: цвет переводит любую ось в любую, и всякая
    цвет-инвариантная величина одинакова на S и на L; у SU(3)-инвариантной Γ шесть диагональных
    элементов равны. Цвет-инвариантная асимметрия одна — вес 𝟑 против 𝟑̄ (b ≠ c в Γ = a|O⟩⟨O| + bP_𝟑 + cP_𝟑̄).
    """
    J = np.array([omul(unit(7), unit(i + 1))[1:] for i in range(7)]).T[:6, :6]
    P3 = (np.eye(6) - 1j * J) / 2
    assert np.allclose(P3 @ P3, P3) and np.linalg.matrix_rank(P3) == 3 and np.allclose(np.diag(P3), 0.5)
    su3 = _su3_of_e_o()
    for k in range(6):
        assert np.linalg.matrix_rank(np.array([X[:6, k] for X in su3]).T, tol=1e-9) == 5
    G = np.zeros((7, 7), complex)
    G[6, 6], G[:6, :6] = 0.3, 0.5 * P3 / 3 + 0.2 * P3.conj() / 3
    assert all(np.allclose(X @ G, G @ X) for X in su3) and np.allclose(np.diag(G)[:6], np.diag(G)[0])





# --- Отзыв 25.09.2026 (A-90, A-83): вакуум V_Gap, ε̄, T-177, H ∼ γ_EU -------------------------

_NONFANO = [t for t in itertools.combinations(range(7), 3)
            if tuple(sorted(x + 1 for x in t)) not in {tuple(sorted(l)) for l in LINES}]
_NF = np.array(_NONFANO)


def _gap_total(G):
    """𝒢_total = 2 Σ_{i<j} |γ_ij|² sin²θ_ij = ‖Im Γ‖_F² (gap-thermodynamics §11(a))."""
    return float(np.sum(np.imag(G) ** 2))


def _v3(G):
    """V₃/λ₃ = Σ_{i<j<k ∉ Fano} ‖[e_i,e_j,e_k]‖·|γ_ij||γ_jk||γ_ik| sin(θ_ij+θ_jk−θ_ik) = 2 Σ Im(γ_ij γ_jk γ_ki)."""
    i, j, k = _NF.T
    return float(2 * np.sum(np.imag(G[i, j] * G[j, k] * G[k, i])))


def _v_gap(G, mu2, l3, l4):
    g = _gap_total(G)
    return mu2 * g + l3 * _v3(G) + l4 * g * g


def _state(x):
    A = (x[:49] + 1j * x[49:]).reshape(7, 7)
    R = A @ A.conj().T
    return R / np.trace(R).real


def test_v_gap_cubic_term_is_not_g2_invariant():
    """V₂, V₄ G₂-инвариантны (даже O(7)), кубический член V₃ — нет, и даже не SU(3)_C-инвариантен.

    Свидетель отзыва T-64 (25.09.2026): «G₂-инвариантный потенциал на (S¹)²¹/G₂» и
    таблица симметрий (V₃: «G₂ +») ложны. Из 896 знаковых перестановок, сохраняющих V₃,
    в G₂ лежат 56; ассоциатор неколлинеарной тройки имеет норму 2.
    """
    assert len(_NONFANO) == 28
    for i, j, k in _NONFANO[:5]:
        a = omul(omul(unit(i + 1), unit(j + 1)), unit(k + 1)) - omul(unit(i + 1), omul(unit(j + 1), unit(k + 1)))
        assert abs(np.linalg.norm(a) - 2) < 1e-12
    rng = np.random.default_rng(20)
    G = random_state(rng)
    su3 = _su3_of_e_o()
    moved = 0
    for _ in range(5):
        g = expm(sum(c * X for c, X in zip(rng.normal(size=14), G2)))
        H = g @ G @ g.T
        assert abs(_gap_total(H) - _gap_total(G)) < 1e-12
        moved += abs(_v3(H) - _v3(G)) > 1e-6
        h = expm(sum(c * X for c, X in zip(rng.normal(size=8), su3)))
        moved += abs(_v3(h @ G @ h.T) - _v3(G)) > 1e-6
    assert moved == 10
    samples = [random_state(rng) for _ in range(2)]
    base = [_v3(S) for S in samples]
    fano = {frozenset(l) for l in LINES}
    keep, in_g2 = 0, 0
    for p in itertools.permutations(range(7)):
        if {frozenset(p[i - 1] + 1 for i in l) for l in fano} != fano:
            continue
        P = np.zeros((7, 7))
        P[list(p), range(7)] = 1
        for signs in itertools.product((1, -1), repeat=7):
            Q = P * np.array(signs)
            if all(abs(_v3(Q @ S @ Q.T) - b) < 1e-12 for S, b in zip(samples, base)):
                keep += 1
                in_g2 += np.allclose(np.einsum('ia,jb,kc,abc->ijk', Q, Q, Q, PHI3), PHI3)
    assert (keep, in_g2) == (896, 56)


def test_su3_invariant_vacuum_has_no_spontaneous_gap():
    """На SU(3)_C-инвариантных Γ = a|O⟩⟨O| + bP₃ + cP₃̄ кубик V₃ ≡ 0, 𝒢_total = 6δ², δ = |b−c|/2.

    Свидетель отзыва T-64: с верными секторами (триплет span{A−iD, S−iU, L−iE})
    «пять секторных параметров» не существуют — инвариантное семейство имеет одну
    когерентность δ, и V = 6μ²δ² + 36λ₄δ⁴ минимальна при δ = 0, то есть при 𝒢_total = 0.
    """
    Lo = np.array([omul(unit(7), unit(i + 1))[1:] for i in range(7)]).T
    J = Lo[:6, :6]
    su3 = _su3_of_e_o()
    rng = np.random.default_rng(21)
    for _ in range(20):
        w = rng.dirichlet(np.ones(3))
        a, b, c = w[0], w[1] / 3, w[2] / 3
        G = np.zeros((7, 7), complex)
        G[O_AXIS, O_AXIS] = a
        G[:6, :6] = (b + c) / 2 * np.eye(6) + 1j * (b - c) / 2 * J
        assert abs(np.trace(G).real - 1) < 1e-12 and np.linalg.eigvalsh(G).min() > -1e-12
        assert max(np.abs(X @ G - G @ X).max() for X in su3) < 1e-12
        assert abs(_v3(G)) < 1e-15
        assert abs(_gap_total(G) - 6 * ((b - c) / 2) ** 2) < 1e-12


def _sym_v():
    """Знаковые перестановки, сохраняющие V_Gap: 7 циклических сдвигов e_k ↦ e_{k+1} × 128 смен знаков."""
    out = []
    for k in range(7):
        P = np.zeros((7, 7))
        P[[(i + k) % 7 for i in range(7)], range(7)] = 1
        for signs in itertools.product((1, -1), repeat=7):
            out.append(P * np.array(signs))
    return out


def test_v_gap_vacuum_is_unique_up_to_its_symmetries_not_up_to_g2():
    """Самосогласованный вакуум V_Gap единствен с точностью до Sym(V) (896), но не до G₂; секторов нет.

    Свидетель переформулировки T-64 и T-61 (25.09.2026). Константы теоремы 13.5 взяты в
    неподвижной точке итерации «минимизировать → пересчитать |γ̄| и 𝒢⁰»: λ₃/μ² = 2/(3|γ̄|) ≈ 9,25,
    λ₄/μ² = 1/(2𝒢⁰) ≈ 32,2. Из 12 стартов не меньше 8 дают одно V_min < 0, и все эти
    минимизаторы лежат на одной орбите Sym(V); минимизатор — ранга 2, P ≈ 0,709, носитель —
    объединение двух линий Фано через одну точку, стабилизатор в 𝔤₂ нулевой. Образы под
    Sym(V) дают два значения G₂-инварианта ‖w‖², w_k = φ_ijk Im Γ_ij: две G₂-орбиты при одном V.
    """
    from scipy.optimize import minimize
    l3, l4 = 9.25, 32.22
    rng = np.random.default_rng(22)
    runs = []
    for _ in range(12):
        r = minimize(lambda x: _v_gap(_state(x), 1.0, l3, l4), rng.normal(size=98),
                     method='L-BFGS-B', options={'maxiter': 40000, 'ftol': 1e-16, 'gtol': 1e-12})
        runs.append((r.fun, _state(r.x)))
    vmin, G = min(runs, key=lambda t: t[0])
    best = [H for f, H in runs if f - vmin < 1e-7]
    assert vmin < 0 and len(best) >= 8
    iu = np.triu_indices(7, 1)
    assert abs(2 / (3 * np.abs(G[iu]).mean()) / l3 - 1) < 0.01 and abs(1 / (2 * _gap_total(G)) / l4 - 1) < 0.01
    sym = _sym_v()
    assert len(sym) == 896 and all(abs(_v_gap(Q @ G @ Q.T, 1.0, l3, l4) - vmin) < 1e-12 for Q in sym)
    imgs = [Q @ G @ Q.T for Q in sym]
    assert all(min(np.abs(H - I).max() for I in imgs) < 1e-3 for H in best)
    assert np.linalg.matrix_rank(G, tol=1e-5) == 2 and abs(purity(G) - 0.709) < 0.002
    supp = {i + 1 for i in range(7) if G[i, i].real > 1e-4}
    inside = [set(l) for l in LINES if set(l) <= supp]
    assert len(supp) == 5 and len(inside) == 2 and len(inside[0] & inside[1]) == 1
    M = np.array([(X @ G - G @ X).ravel() for X in G2]).T
    assert np.linalg.svd(np.vstack([M.real, M.imag]), compute_uv=False).min() > 1e-4
    ws = set()
    for H in imgs:
        w = np.einsum('ijk,ij->k', PHI3, H.imag)
        ws.add(round(float(w @ w), 4))
    assert len(ws) == 2


def test_mean_coherence_with_the_tables_own_eps_o():
    """Среднее по 21 паре с ε_O ~ 1 из таблицы — 0,53, не 0,023; по 15 не-O парам — ε_33/√5.

    Свидетель A-83 (теорема 14.2): 0,023 получалось лишь при ε_O = 0,04, что противоречит
    строке «O-to-all: ε_O ~ 1» той же таблицы и T-80 (Gap(O,i) ≈ 1). Порядок 10⁻² держит
    среднеквадратичное по 15 не-O парам: 0,027 при ε_33 = 0,06, 0,0089 при ε_33 = 0,02.
    """
    def mean21(eo, e33=0.02, e3b3b=1e-17, e33b=0.0):
        return np.sqrt((6 * eo ** 2 + 9 * e33b ** 2 + 3 * e33 ** 2 + 3 * e3b3b ** 2) / 21)

    def mean_non_o(e33, e3b3b=1e-17, e33b=0.0):
        return np.sqrt((9 * e33b ** 2 + 3 * e33 ** 2 + 3 * e3b3b ** 2) / 15)
    assert abs(mean21(1.0) - 0.5346) < 1e-4 and abs(mean21(0.04) - 0.0226) < 1e-4
    assert abs(mean_non_o(0.06) - 0.0268) < 1e-4 and abs(mean_non_o(0.02) - 0.0089) < 1e-4


def test_fano_roles_are_fixed_by_three_non_collinear_marks():
    """Коллинеации PG(2,2) (168) действуют регулярно на 168 упорядоченных неколлинеарных тройках.

    Свидетель переформулировки T-177 и T-183 (25.09.2026). Стабилизаторы: точки O — 24,
    двух точек — 4, O и линии Хиггса {A,E,U} — 6 (орбиты {O}, {A,E,U}, {S,D,L}), O и пары
    κ₀ {E,U} — 2 (орбиты {O}, {A}, {D}, {E,U}, {S,L}), трёх неколлинеарных точек — 1.
    Знаки октонионов не помогают: элементы Γ_oct, закрепляющие +e_O, дают те же 24 перестановки.
    """
    fano = {frozenset(l) for l in LINES}
    coll = [p for p in itertools.permutations(range(1, 8))
            if {frozenset(p[i - 1] for i in l) for l in fano} == fano]
    assert len(coll) == 168
    triples = [t for t in itertools.permutations(range(1, 8), 3) if frozenset(t) not in fano]
    assert len(triples) == 168
    assert len({(p[0], p[1], p[2]) for p in coll}) == 168       # образы упорядоченной неколлинеарной тройки (A,S,D)
    A, S, D, L, E, U, O = range(1, 8)

    def orbits(group):
        return {frozenset(p[x - 1] for p in group) for x in range(1, 8)}
    s_o = [p for p in coll if p[O - 1] == O]
    s_oe = [p for p in s_o if p[E - 1] == E]
    s_h = [p for p in s_o if {p[A - 1], p[E - 1], p[U - 1]} == {A, E, U}]
    s_k = [p for p in s_o if {p[E - 1], p[U - 1]} == {E, U}]
    s_oea = [p for p in s_oe if p[A - 1] == A]
    assert [len(s_o), len(s_oe), len(s_h), len(s_k), len(s_oea)] == [24, 4, 6, 2, 1]
    assert orbits(s_h) == {frozenset({O}), frozenset({A, E, U}), frozenset({S, D, L})}
    assert orbits(s_k) == {frozenset({O}), frozenset({A}), frozenset({D}), frozenset({E, U}), frozenset({S, L})}
    perms = set()
    for p in s_o:
        P = np.zeros((7, 7))
        P[[x - 1 for x in p], range(7)] = 1
        for signs in itertools.product((1, -1), repeat=7):
            if signs[O - 1] != 1:
                continue
            Q = P * np.array(signs)
            if np.allclose(np.einsum('ia,jb,kc,abc->ijk', Q, Q, Q, PHI3), PHI3):
                perms.add(p)
    assert len(perms) == 24


def test_gamma_eu_vev_breaks_colour():
    """Γ = I/7 + ε(e^{iφ}|E⟩⟨U| + h.c.): стабилизатор в 𝔰𝔲(3)_C = Stab(e_O) — размерности ≤ 1 (из 8).

    Свидетель отзыва теоремы 1.0 сектора Хиггса (25.09.2026): ⟨γ_EU⟩ ≠ 0 ломает SU(3)_C
    (до U(1) при φ = π/2, полностью при прочих φ); у γ_EU нет синглетной компоненты.
    Испробованный ремонт: γ_EU инвариантна под Stab(e_A) — но лишь вместе с равными γ_SL,
    γ_DO, и это переносит цвет с O на A; SU(2), коммутирующей с цветом, на ℂ⁷ нет (коммутант ℂ³).
    """
    su3 = _su3_of_e_o()

    def stab(G):
        M = np.array([(X @ G - G @ X).ravel() for X in su3]).T
        s = np.linalg.svd(np.vstack([M.real, M.imag]), compute_uv=False)
        return int(np.sum(s < 1e-9))
    assert stab(np.eye(7, dtype=complex) / 7) == 8
    E, U = 4, 5
    dims = []
    for phi in np.linspace(0, 2 * np.pi, 25):
        G = np.eye(7, dtype=complex) / 7
        G[E, U] = 0.01 * np.exp(1j * phi)
        G[U, E] = np.conj(G[E, U])
        dims.append(stab(G))
    assert max(dims) == 1 and min(dims) == 0
    A_AX = 0                                                        # вариант ремонта: цвет = Stab(e_A)
    M = np.array([X @ np.eye(7)[A_AX] for X in G2]).T
    _, s, Vt = np.linalg.svd(M)
    ns = Vt[np.sum(s > 1e-9):]
    su3_a = [sum(ns[a][b] * G2[b] for b in range(14)) for a in range(ns.shape[0])]
    La = np.array([omul(unit(1), unit(i + 1))[1:] for i in range(7)]).T
    G = np.eye(7, dtype=complex) / 7 + 0.02j * La                   # пары (S,L), (E,U), (D,O) линий через A
    assert len(su3_a) == 8 and max(np.abs(X @ G - G @ X).max() for X in su3_a) < 1e-12
    assert abs(G[E, U]) > 0.019 and abs(abs(G[1, 3]) - abs(G[E, U])) < 1e-12 and abs(abs(G[2, 6]) - abs(G[E, U])) < 1e-12
    basis = []
    for i in range(7):
        for j in range(7):
            Z = np.zeros((7, 7), complex)
            Z[i, j] = 1
            basis.append(Z)
    rows = np.vstack([np.array([(Y @ X - X @ Y).flatten() for Y in basis]).T for X in su3])
    assert 49 - np.linalg.matrix_rank(rows, tol=1e-9) == 3                  # коммутант ℂ³: SU(2) с цветом не коммутирует



def _superop(f, d=7):
    """Матрица супероператора X ↦ f(X) в построчной векторизации."""
    S = np.zeros((d * d, d * d), complex)
    for k in range(d * d):
        E = np.zeros(d * d, complex)
        E[k] = 1
        S[:, k] = f(E.reshape(d, d)).ravel()
    return S


def _choi(Phi, d=7):
    C = np.zeros((d * d, d * d), complex)
    for i in range(d):
        for j in range(d):
            E = np.zeros((d, d))
            E[i, j] = 1
            C[i * d:(i + 1) * d, j * d:(j + 1) * d] = (Phi @ E.ravel()).reshape(d, d)
    return (C + C.conj().T) / 2


def _stinespring_unitary(Phi, rng):
    """Унитарный W на ℂ⁷ ⊗ ℂ⁴⁹ с Tr_E W(ρ ⊗ |0⟩⟨0|)W† = Φ(ρ) (Стайнспринг, дополнение базиса)."""
    w, V = np.linalg.eigh(_choi(Phi))
    iso = np.zeros((343, 7), complex)
    for j, (lam, v) in enumerate(zip(w, V.T)):
        if lam > 1e-14:
            K = np.sqrt(lam) * v.reshape(7, 7).T           # оператор Крауса K[a, i]
            for a in range(7):
                iso[a * 49 + j, :] = K[a, :]
    Q, _ = np.linalg.qr(np.hstack([iso, rng.normal(size=(343, 336)) + 1j * rng.normal(size=(343, 336))]))
    W = np.zeros((343, 343), complex)
    cols0 = [i * 49 for i in range(7)]
    W[:, cols0] = iso
    W[:, [c for c in range(343) if c not in cols0]] = Q[:, 7:]
    return W


def _unital_primitive_l0(rng):
    """ℒ₀ = −i[H,·] + ⅔(diag − id): эрмитовы операторы Линдблада (Фано-диссипатор = ⅔·D_atom)."""
    A = rng.normal(size=(7, 7)) + 1j * rng.normal(size=(7, 7))
    H = (A + A.conj().T) / 2
    H /= np.linalg.norm(H, 2)
    gam = 2 / 3
    return H, gam, (lambda X: -1j * (H @ X - X @ H) + gam * (np.diag(np.diag(X)) - X))


def test_depth_register_carries_the_dissipative_arrow():
    """Регистр глубины — точный конечный носитель T-53b (эмерджентное время §11.4, теоремы 11.1, 11.2, 11.4).

    Цепь из N+1 = 13 показаний, среда ℂ⁴⁹, связь Фейнмана–Китаева: 𝒲†Ĉ𝒲 = Λ ⊗ 1 (лапласиан пути),
    щель 4 sin²(π/26); условные состояния совпадают с e^{nΔtℒ₀}ρ₀ до 10⁻¹⁴ при всех n; чистота строго
    падает, D(·‖I/7) не растёт. На кольце стрела ломается ровно на одном шаге из N+1. Орбита одной
    унитарной (часы-орбита на конечном пространстве) после падения D снова растёт. Ошибка между
    показаниями ≤ Δt(2‖H‖ + 2γ).
    """
    rng = np.random.default_rng(7)
    H, gam, L0 = _unital_primitive_l0(rng)
    Lsup = _superop(L0)
    ev = np.linalg.eigvals(Lsup)
    assert np.sum(abs(ev) < 1e-10) == 1                              # примитивна: одна неподвижная точка
    N, dt = 12, 0.3
    Ws = [np.eye(343, dtype=complex)] + [_stinespring_unitary(expm(n * dt * Lsup), rng) for n in range(1, N + 1)]
    assert max(np.linalg.norm(W.conj().T @ W - np.eye(343)) for W in Ws) < 1e-12
    Us = [None] + [Ws[n] @ Ws[n - 1].conj().T for n in range(1, N + 1)]    # не зависят от состояния

    def C_apply(psi):
        out = np.zeros_like(psi)
        for n in range(N + 1):
            out[n] = ((n > 0) + (n < N)) * psi[n]
            if n > 0:
                out[n] -= Us[n] @ psi[n - 1]
            if n < N:
                out[n] -= Us[n + 1].conj().T @ psi[n + 1]
        return out
    e0 = np.zeros(49)
    e0[0] = 1
    psi0 = rng.normal(size=7) + 1j * rng.normal(size=7)
    psi0 /= np.linalg.norm(psi0)
    hist = np.array([W @ np.kron(psi0, e0) for W in Ws]) / np.sqrt(N + 1)
    assert np.linalg.norm(C_apply(hist)) < 1e-13                      # история лежит в ker Ĉ
    v = rng.normal(size=(N + 1, 343)) + 1j * rng.normal(size=(N + 1, 343))
    lhs = np.array([Ws[n].conj().T @ x for n, x in enumerate(C_apply(np.array([Ws[n] @ v[n] for n in range(N + 1)])))])
    Lam = np.diag([float((n > 0) + (n < N)) for n in range(N + 1)]) - np.eye(N + 1, k=1) - np.eye(N + 1, k=-1)
    assert np.linalg.norm(lhs - Lam @ v) < 1e-11                      # 𝒲†Ĉ𝒲 = Λ ⊗ 1
    lev = np.linalg.eigvalsh(Lam)
    assert abs(lev[0]) < 1e-12 and lev[1] > 1e-3
    assert abs(lev[1] - 4 * np.sin(np.pi / (2 * (N + 1))) ** 2) < 1e-12
    rho0 = 0.5 * random_state(rng) + 0.5 * np.outer(psi0, psi0.conj())
    Ps, Ds = [], []
    for n in range(N + 1):
        big = Ws[n] @ np.kron(rho0, np.outer(e0, e0)) @ Ws[n].conj().T
        cond = np.einsum("aibi->ab", big.reshape(7, 49, 7, 49))
        target = (expm(n * dt * Lsup) @ rho0.ravel()).reshape(7, 7)
        assert np.linalg.norm(cond - target) < 1e-13                  # точно, при каждом показании
        Ps.append(purity(cond))
        Ds.append(np.log(7) - entropy(cond))
    assert np.diff(Ps).max() < -1e-3 and np.diff(Ds).max() < 0        # стрела на всей истории
    ring = Ps + [Ps[0]]
    assert int((np.diff(ring) > 0).sum()) == 1                        # кольцо: ровно один шаг против стрелы
    state = np.kron(rho0, np.outer(e0, e0))
    Dorb = []
    for n in range(400):                                              # часы-орбита: одна унитарная W₁
        Dorb.append(np.log(7) - entropy(np.einsum("aibi->ab", state.reshape(7, 49, 7, 49))))
        state = Ws[1] @ state @ Ws[1].conj().T
    Dorb = np.array(Dorb)
    assert (Dorb - np.minimum.accumulate(Dorb)).max() > 0.02
    bound = dt * (2 * np.linalg.norm(H, 2) + 2 * gam)
    worst = 0.0
    for t in np.linspace(0, N * dt, 241):
        n = int(np.floor(t / dt + 1e-12))
        d = ((expm(t * Lsup) - expm(n * dt * Lsup)) @ rho0.ravel()).reshape(7, 7)
        worst = max(worst, np.abs(np.linalg.eigvalsh((d + d.conj().T) / 2)).sum())
    assert 0 < worst <= bound


def test_regenerative_solution_is_a_conditional_history():
    """Полный поток с ℛ = κ g_V (φ(Γ) − Γ) — условная история связи, подогнанной под решение (теорема 11.3).

    Замороженный генератор ℒ_s = ℒ₀ + c(s)(ρ_*(s)Tr − id) на решении совпадает с полной правой частью;
    его пропагаторы за Δt — CPTP (минимальное собственное значение Чоя ≥ 0, след сохраняется) и
    переводят Γ((n−1)Δt) в Γ(nΔt); прямое интегрирование даёт то же решение.
    """
    rng = np.random.default_rng(7)
    _, _, L0 = _unital_primitive_l0(rng)
    Lsup = _superop(L0)
    kap = 3.0

    def full(G):
        return L0(G) + kap * gate(purity(G)) * (_phi_coh_fixed(G) - G)

    def frozen(G):
        c, rs = kap * gate(purity(G)), _phi_coh_fixed(G)
        return Lsup + _superop(lambda X: c * (rs * np.trace(X) - X))
    psi = np.zeros(7, complex)
    psi[0] = 1
    G = 0.9 * np.outer(psi, psi.conj()) + 0.1 * np.eye(7) / 7
    dt, N, sub = 0.25, 12, 40
    h = dt / sub
    Gs, Phis = [G.copy()], []
    for _ in range(N):
        Phi = np.eye(49, dtype=complex)
        for _ in range(sub):
            def f(G, Phi):
                L = frozen(G)
                return (L @ G.ravel()).reshape(7, 7), L @ Phi
            k1 = f(G, Phi)
            k2 = f(G + h / 2 * k1[0], Phi + h / 2 * k1[1])
            k3 = f(G + h / 2 * k2[0], Phi + h / 2 * k2[1])
            k4 = f(G + h * k3[0], Phi + h * k3[1])
            G = G + h / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
            Phi = Phi + h / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        Phis.append(Phi)
        Gs.append(G.copy())
    assert max(np.linalg.norm((frozen(g) @ g.ravel()).reshape(7, 7) - full(g)) for g in Gs) < 1e-13
    assert max(np.linalg.norm((Phis[n] @ Gs[n].ravel()).reshape(7, 7) - Gs[n + 1]) for n in range(N)) < 1e-13
    assert min(np.linalg.eigvalsh(_choi(P)).min() for P in Phis) > -1e-10          # CPTP
    tr = np.eye(7).ravel()
    assert max(np.linalg.norm(tr @ P - tr) for P in Phis) < 1e-12
    assert purity(Gs[0]) > 2 / 7 > purity(Gs[-1])                    # затвор включён в начале решения
    G2 = Gs[0].copy()
    for _ in range(N * sub):
        k1 = full(G2)
        k2 = full(G2 + h / 2 * k1)
        k3 = full(G2 + h / 2 * k2)
        k4 = full(G2 + h * k3)
        G2 = G2 + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    assert np.linalg.norm(G2 - Gs[-1]) < 1e-12


def test_depth_register_time_algebra_is_the_line():
    """Алгебра времени регистра глубины в скейлинговом пределе — C₀(ℝ) (теорема 11.5, T-118).

    Показания t_k = (k − m)Δt с Δt = 1/√N, m = N/2: норма выборки ‖s_N f‖ приближает ‖f‖∞
    не хуже модуля непрерывности ω_f(Δt/2) ≤ Lip(f)·Δt/2, и ошибка падает с ростом N.
    Позиционный регистр из M = 2 O-регистров: 49 упорядоченных показаний, младший разряд — n mod 7.
    """
    f = lambda x: np.exp(-(x - 0.37) ** 2) * np.cos(3 * x)
    xs = np.linspace(-12, 12, 2_000_001)
    sup = np.abs(f(xs)).max()
    lip = np.abs(np.gradient(f(xs), xs)).max()
    errs = []
    for N in (100, 1_000, 10_000, 100_000):
        dt = 1 / np.sqrt(N)
        t = (np.arange(N + 1) - N // 2) * dt
        err = sup - np.abs(f(t)).max()
        assert -1e-9 <= err <= lip * dt / 2 + 1e-9
        errs.append(err)
    assert errs[-1] < errs[0]
    digits = [(n % 7, n // 7) for n in range(49)]
    assert len(set(digits)) == 49 and all(a + 7 * b == n for n, (a, b) in enumerate(digits))


# ---------------------------------------------------------------------------
# Стандартная модель на комплексных октонионах (25.09.2026, T-350 … T-353).
# Пространство 𝒮 = ℂ⊗𝕆 = ℂη₀ ⊕ ℂ⁷ записано вещественно как пары (x, y) ↔ x + iy.
# ---------------------------------------------------------------------------

def _lmul8(i):
    return np.array([omul(unit(i), unit(j)) for j in range(8)]).T


def _rmul8(i):
    return np.array([omul(unit(j), unit(i)) for j in range(8)]).T


def _null_commutant(ops, space, tol=1e-9):
    rows = np.vstack([np.array([(S @ X - X @ S).flatten() for S in space]).T for X in ops])
    _, s, Vt = np.linalg.svd(rows)
    return Vt[np.sum(s > tol):]


@functools.lru_cache(maxsize=None)
def _sm_on_complex_octonions():
    """Клиффордова система 𝒮, 𝔰𝔭𝔦𝔫(9), 𝔰𝔲(3)_C, её централизатор и полная 𝔤_SM."""
    Z, I8 = np.zeros((8, 8)), np.eye(8)
    imul = np.block([[Z, -I8], [I8, Z]])                     # умножение на i
    conj = np.block([[I8, Z], [Z, -I8]])                     # комплексное сопряжение J
    cl = lambda A: np.block([[A, Z], [Z, A]])                # ℂ-линейное продолжение
    gam = [imul @ cl(_lmul8(k)) for k in range(1, 8)] + [conj, imul @ conj]
    spin9 = [gam[a] @ gam[b] / 2 for a in range(9) for b in range(a + 1, 9)]
    su3 = []
    for X in _su3_of_e_o():
        M = np.zeros((8, 8))
        M[1:, 1:] = X
        su3.append(cl(M))
    cen = _null_commutant(su3, spin9)
    C = [sum(v[i] * spin9[i] for i in range(36)) for v in cen]
    zc = _null_commutant(C, C)
    Y = sum(zc[0][i] * C[i] for i in range(len(C)))
    Lu = cl(_lmul8(7))
    q = -Lu @ Y
    ev = np.linalg.eigvalsh((q + q.T) / 2)
    Y = Y * (1 / 6) / ev.max()                               # нормировка: заряд кварков 1/6
    return dict(imul=imul, conj=conj, cl=cl, gam=gam, spin9=spin9, su3=su3, C=C, Y=Y,
                Lu=Lu, Ru=cl(_rmul8(7)), g=su3 + C)


def _span_residual(X, ops):
    F = np.array([o.flatten() for o in ops]).T
    c = np.linalg.lstsq(F, X.flatten(), rcond=None)[0]
    return np.linalg.norm(F @ c - X.flatten())


def test_complex_octonion_clifford_system_is_maximal_spin9():
    """T-350(а): iL_{e_1..7}, J, iJ на 𝒮 = ℂ⊗𝕆 ≅ ℝ¹⁶ — система Клиффорда Cl(9,0), и она единственна.

    Операторы, антикоммутирующие со всеми семью iL_{e_k}, образуют ровно двумерное
    пространство span{J, iJ}: продолжение семи до девяти не выбирается. Объём семи
    равен i. По Гурвицу–Радону на ℝ¹⁶ нет десяти таких операторов (Cl(10,0) ≅ M₃₂(ℝ)),
    так что 𝔰𝔭𝔦𝔫(9) (размерность 36) — наибольшая спинорная алгебра системы.
    """
    d = _sm_on_complex_octonions()
    gam = d["gam"]
    for a in range(9):
        for b in range(9):
            assert np.allclose(gam[a] @ gam[b] + gam[b] @ gam[a], 2 * (a == b) * np.eye(16))
    basis = [np.outer(np.eye(16)[i], np.eye(16)[j]) for i in range(16) for j in range(16)]
    rows = np.vstack([np.array([(S @ X + X @ S).flatten() for S in basis]).T for X in gam[:7]])
    _, s, Vt = np.linalg.svd(rows)
    anti = [v.reshape(16, 16) for v in Vt[np.sum(s > 1e-9):]]
    assert len(anti) == 2
    assert _span_residual(d["conj"], anti) < 1e-9 and _span_residual(d["imul"] @ d["conj"], anti) < 1e-9
    w7 = functools.reduce(np.matmul, gam[:7])
    assert np.allclose(w7, d["imul"])
    assert np.linalg.matrix_rank(np.array([x.flatten() for x in d["spin9"]])) == 36
    G2c = []
    for X in G2:
        M = np.zeros((8, 8))
        M[1:, 1:] = X
        G2c.append(d["cl"](M))
    assert max(_span_residual(X, d["spin9"]) for X in G2c) < 1e-9                   # 𝔤₂ ⊂ 𝔰𝔭𝔦𝔫(7) ⊂ 𝔰𝔭𝔦𝔫(9)


def test_standard_model_algebra_is_the_centraliser_of_colour_in_spin9():
    """T-350(б): 𝔠_{𝔰𝔭𝔦𝔫(9)}(𝔰𝔲(3)_C) = 𝔲(2); 𝔫(𝔰𝔲(3)_C) = 𝔰𝔲(3)⊕𝔰𝔲(2)⊕𝔲(1) = 𝔠(R_{e_O}).

    Централизатор цвета четырёхмерен, центр одномерен, коммутант трёхмерен; нормализатор
    цвета двенадцатимерен и совпадает с централизатором правого умножения на e_O
    (характеристика Краснова); централизатор всей 𝔤_SM в 𝔰𝔭𝔦𝔫(9) — одна 𝔲(1)_Y.
    """
    d = _sm_on_complex_octonions()
    spin9, su3, C = d["spin9"], d["su3"], d["C"]
    assert max(_span_residual(X, spin9) for X in su3) < 1e-9
    assert len(C) == 4
    assert _null_commutant(C, C).shape[0] == 1
    assert np.linalg.matrix_rank(np.array([(a @ b - b @ a).flatten() for a in C for b in C]), tol=1e-9) == 3
    F3 = np.array([x.flatten() for x in su3]).T

    def out3(X):
        return F3 @ np.linalg.lstsq(F3, X.flatten(), rcond=None)[0] - X.flatten()
    M = np.vstack([np.array([out3(S @ X - X @ S) for S in spin9]).T for X in su3])
    assert 36 - np.linalg.matrix_rank(M, tol=1e-9) == 12
    cr = _null_commutant([d["Ru"]], spin9)
    CR = [sum(v[i] * spin9[i] for i in range(36)) for v in cr]
    assert len(CR) == 12 and max(_span_residual(X, d["g"]) for X in CR) < 1e-9
    assert _null_commutant(d["g"], spin9).shape[0] == 1                            # нет Z′ внутри Spin(9)
    assert _null_commutant([d["Lu"]], spin9).shape[0] == 18                        # 𝔰𝔭𝔦𝔫(6)⊕𝔰𝔭𝔦𝔫(3)


def test_spin9_standard_model_group_has_exactly_z6_kernel():
    """T-350(в): ядро SU(3)×SU(2)×U(1) → Spin(9) на 𝒮 — ровно ℤ₆ = {(ω^a, (−1)^b, ω^{−a}(−1)^b)}.

    U(1) параметризована зарядом 6Y ∈ {1, −3} с периодом 2π; центр SU(3)_C — умножение
    на e^{2πL_u/3} на шести осях ≠ O; центр SU(2) — −1. Шесть и только шесть троек
    действуют тождественно: глобальная форма (SU(3)×SU(2)×U(1))/ℤ₆.
    """
    d = _sm_on_complex_octonions()
    P = np.eye(8)
    P[0, 0] = P[7, 7] = 0
    w = expm((2 * np.pi / 3) * d["Lu"] @ d["cl"](P))
    assert max(np.abs(w @ X - X @ w).max() for X in d["su3"]) < 1e-9
    assert np.allclose(expm(2 * np.pi * 6 * d["Y"]), np.eye(16))
    assert not np.allclose(expm(np.pi * 6 * d["Y"]), np.eye(16))
    kernel = []
    for n in range(12):
        u1 = expm((np.pi * n / 6) * 6 * d["Y"])
        for a, wa in enumerate((np.eye(16), w, w @ w)):
            for s in (1, -1):
                if np.allclose(s * wa @ u1, np.eye(16)):
                    kernel.append((a, s, n))
    assert len(kernel) == 6 and sorted({a for a, _, _ in kernel}) == [0, 1, 2] and {s for _, s, _ in kernel} == {1, -1}


def test_complex_octonion_doublets_are_chiral():
    """T-351: (𝒮, L_{e_O}) = (3,2)_{1/6} ⊕ (1,2)_{−1/2}; сопряжённое не изоморфно — тест Дистлера–Гарибальди.

    Коммутант 𝔤_SM в End_ℝ(ℝ¹⁶) четырёхмерен (ℂ⊕ℂ: блок кварков и блок лептонов);
    L_{e_O} = γ_O γ_J γ_{iJ} — объём трёх клиффордовых направлений, дополнительных к цвету,
    коммутирует с 𝔰𝔭𝔦𝔫(6)⊕𝔰𝔭𝔦𝔫(3) и даёт один знак обоим блокам. Физическое i
    с 𝔤_SM не коммутирует. Заряды Q = T₃ + Y: {2/3, −1/3, 0, −1}; лептонная прямая — ℂ_{e_O} = span{1, e_O}.
    """
    d = _sm_on_complex_octonions()
    g, Lu, Y, gam = d["g"], d["Lu"], d["Y"], d["gam"]
    assert np.allclose(gam[6] @ gam[7] @ gam[8], Lu) and np.allclose(Lu @ Lu, -np.eye(16))
    assert max(np.abs(Lu @ X - X @ Lu).max() for X in g) < 1e-12
    assert max(np.abs(d["imul"] @ X - X @ d["imul"]).max() for X in g) > 0.5
    basis = [np.outer(np.eye(16)[i], np.eye(16)[j]) for i in range(16) for j in range(16)]
    assert _null_commutant(g, basis).shape[0] == 4
    q = -Lu @ Y
    assert np.allclose(q, q.T) and np.allclose(q @ Lu, Lu @ q)
    vals, mult = np.unique(np.round(np.linalg.eigvalsh(q), 9), return_counts=True)
    spec = dict(zip(vals, mult // 2))                                               # комплексные кратности
    assert spec == {round(-1 / 2, 9): 2, round(1 / 6, 9): 6}                        # (1,2)_{−1/2} ⊕ (3,2)_{1/6}
    conj_spec = {round(-k, 9): m for k, m in spec.items()}
    assert conj_spec != spec                                                        # (𝒮,L_u) ≇ его сопряжённому
    T3 = -Lu @ (d["imul"] / 2)
    assert _span_residual(d["imul"] / 2, d["C"]) < 1e-9
    Q = T3 + q
    qv, qm = np.unique(np.round(np.linalg.eigvals(Q).real, 9), return_counts=True)
    assert dict(zip(qv, qm // 2)) == {round(-1.0, 9): 1, round(-1 / 3, 9): 3, 0.0: 1, round(2 / 3, 9): 3}
    one, eO, eA = np.eye(16)[0], np.eye(16)[7], np.eye(16)[1]
    assert abs(one @ q @ one + 0.5) < 1e-9 and abs(eO @ q @ eO + 0.5) < 1e-9 and abs(eA @ q @ eA - 1 / 6) < 1e-9
    D = [a @ b - b @ a for a in d["C"] for b in d["C"]]
    assert _span_residual(d["imul"] / 2, D) < 1e-9                                 # i/2 = T₃ ∈ 𝔰𝔲(2)_L
    w, V = np.linalg.eigh(q)
    Pl = V[:, np.isclose(w, -0.5)] @ V[:, np.isclose(w, -0.5)].T
    Jmix = Lu @ (np.eye(16) - 2 * Pl)                                               # знак лептонного блока обращён
    assert np.allclose(Jmix @ Jmix, -np.eye(16)) and max(np.abs(Jmix @ X - X @ Jmix).max() for X in g) < 1e-12
    qm = -Jmix @ Y
    mv, mm = np.unique(np.round(np.linalg.eigvalsh((qm + qm.T) / 2), 9), return_counts=True)
    mix = dict(zip(mv, mm // 2))
    assert mix == {round(1 / 6, 9): 6, 0.5: 2} and {round(-k, 9): m for k, m in mix.items()} != mix   # тоже кирально


def test_family_symmetry_cannot_live_inside_one_copy():
    """T-352(а,б): на 𝒮 с 𝔤_SM коммутируют лишь фазы U(1)_B×U(1)_L; тройственность вращает 𝔲(1)² на 120°.

    (а) Коммутант 𝔤_SM на 𝒮 — ℂ⊕ℂ, поэтому никакая перестановка трёх объектов внутри 𝒮
    (осей {1,2,4}, трёх линий через O, трёх пар (A,D),(S,U),(L,E)) не коммутирует с 𝔤_SM;
    σ: e_k ↦ e_{2k} с ней не коммутирует. (б) Автоморфизм тройственности τ алгебры 𝔰𝔬(8)
    (из локальной тройственности A(xy) = B(x)y + xC(y), τ(A) = κBκ) имеет порядок 3 и
    неподвижную алгебру 𝔤₂ (размерность 14); он неподвижен на 𝔰𝔲(3)_C, а её централизатор
    в 𝔰𝔬(8) — span{L_{e_O}, R_{e_O}} — поворачивает на 2π/3. Тройственность коммутирует с
    цветом, но переводит 𝔤_SM = 𝔠(R_{e_O}) в другое вложение: семейной симметрией она не является.
    """
    d = _sm_on_complex_octonions()

    def sig(k):
        return (2 * k) % 7 or 7
    S = np.zeros((8, 8))
    S[0, 0] = 1
    for k in range(1, 8):
        S[sig(k), k] = 1
    Sc = d["cl"](S)
    assert max(np.abs(Sc @ X - X @ Sc).max() for X in d["g"]) > 0.1
    so8 = []
    for a in range(8):
        for b in range(a + 1, 8):
            M = np.zeros((8, 8))
            M[a, b], M[b, a] = 1, -1
            so8.append(M)
    F8 = np.array([m.flatten() for m in so8]).T
    E = np.eye(8)
    colB = {(i, j): np.array([omul(so8[k] @ E[i], E[j]) for k in range(28)]).T for i in range(8) for j in range(8)}
    colC = {(i, j): np.array([omul(E[i], so8[k] @ E[j]) for k in range(28)]).T for i in range(8) for j in range(8)}
    Mx = np.vstack([np.hstack([colB[i, j], colC[i, j]]) for i in range(8) for j in range(8)])
    K = np.diag([1.0] + [-1.0] * 7)
    T = np.zeros((28, 28))
    for n, A in enumerate(so8):
        r = np.concatenate([A @ omul(E[i], E[j]) for i in range(8) for j in range(8)])
        sol = np.linalg.lstsq(Mx, r, rcond=None)[0]
        assert np.linalg.norm(Mx @ sol - r) < 1e-9
        B = sum(sol[k] * so8[k] for k in range(28))
        T[:, n] = np.linalg.lstsq(F8, (K @ B @ K).flatten(), rcond=None)[0]
    assert np.allclose(np.linalg.matrix_power(T, 3), np.eye(28))
    assert 28 - np.linalg.matrix_rank(T - np.eye(28), tol=1e-9) == 14
    su3o = []
    for X in _su3_of_e_o():
        M = np.zeros((8, 8))
        M[1:, 1:] = X
        su3o.append(np.linalg.lstsq(F8, M.flatten(), rcond=None)[0])
    assert all(np.allclose(T @ x, x) for x in su3o)
    Cb = np.array([np.linalg.lstsq(F8, _lmul8(7).flatten(), rcond=None)[0],
                   np.linalg.lstsq(F8, _rmul8(7).flatten(), rcond=None)[0]]).T
    coef = np.linalg.lstsq(Cb, T @ Cb, rcond=None)[0]
    assert np.allclose(Cb @ coef, T @ Cb)                                           # τ сохраняет span{L_u, R_u}
    ev = np.linalg.eigvals(coef)
    assert np.allclose(sorted(np.angle(ev)), [-2 * np.pi / 3, 2 * np.pi / 3])


def test_left_right_extension_brings_b_minus_l():
    """T-353: добавив к системе десятый генератор (ℝ³² = 𝒮⊗ℝ²), получаем 𝔠_{𝔰𝔭𝔦𝔫(10)}(𝔰𝔲(3)_C) размерности 7.

    Это 𝔰𝔲(2)_L⊕𝔰𝔲(2)_R⊕𝔲(1)_{B−L}: ранг вместе с цветом 5. Синглеты SU(2)_L
    (правые поля) появляются лишь в расширении, и с ними — лишняя 𝔲(1).
    """
    d = _sm_on_complex_octonions()
    s1, s3 = np.array([[0, 1], [1, 0]]), np.diag([1, -1])
    g10 = [np.kron(g, s3) for g in d["gam"]] + [np.kron(np.eye(16), s1)]
    for a in range(10):
        for b in range(10):
            assert np.allclose(g10[a] @ g10[b] + g10[b] @ g10[a], 2 * (a == b) * np.eye(32))
    spin10 = [g10[a] @ g10[b] / 2 for a in range(10) for b in range(a + 1, 10)]
    c10 = _null_commutant([np.kron(X, np.eye(2)) for X in d["su3"]], spin10)
    assert c10.shape[0] == 7
    C10 = [sum(v[i] * spin10[i] for i in range(45)) for v in c10]
    assert _null_commutant(C10, C10).shape[0] == 1
    assert np.linalg.matrix_rank(np.array([(a @ b - b @ a).flatten() for a in C10 for b in C10]), tol=1e-9) == 6


def test_clock_has_three_nontrivial_real_harmonics():
    """T-352(в): у ℤ₇ три нетривиальных вещественных неприводимых представления; Aut(ℤ₇)/{±1} ≅ ℤ₃ переставляет их просто транзитивно.

    Регулярное вещественное представление ℤ₇ = 1 ⊕ три плоскости вращения на 2πm/7,
    m = 1, 2, 3. Умножение m ↦ 2m переводит классы {±1} → {±2} → {±4 = ∓3} → {±1}.
    Оператор на регистре часов ⊗ 1 коммутирует с любой 1 ⊗ X на 𝒮.
    """
    S = np.roll(np.eye(7), 1, axis=0)
    ang = np.round(np.abs(np.angle(np.linalg.eigvals(S))) * 7 / (2 * np.pi)).astype(int)
    vals, mult = np.unique(ang, return_counts=True)
    assert dict(zip(vals, mult)) == {0: 1, 1: 2, 2: 2, 3: 2}
    cls = lambda m: min(m % 7, (-m) % 7)
    orbit = [cls(pow(2, t, 7)) for t in range(3)]
    assert sorted(orbit) == [1, 2, 3] and cls(pow(2, 3, 7)) == 1
    d = _sm_on_complex_octonions()
    P = np.zeros((7, 7))
    for t in range(7):
        P[(2 * t) % 7, t] = 1
    X = d["g"][0]
    assert np.allclose(np.kron(P, np.eye(16)) @ np.kron(np.eye(7), X), np.kron(np.eye(7), X) @ np.kron(P, np.eye(16)))


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
