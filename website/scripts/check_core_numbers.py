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

Семь — за G₂-инвариантным потенциалом Gap (T-331, T-64 в исправленной форме, 25.09.2026):
`g2_invariant_cubics_are_pt_even` (до степени 3 PT-нечётных G₂-инвариантов нет, кубика от Im Γ нет;
PT-нечётных квартик три), `frame_group_cubics_and_the_page_v3_average` (при Γ_oct кубиков 25,
PT-нечётных 3; среднее V₃ страницы по Γ_oct — ноль), `associator_cubic_is_invariant_positive_and_factors_through_lambda3_7`
(𝒜 = 96·Tr(Π₇Λ³Γ) ≥ 0, молчит на ассоциативных состояниях), `real_states_obey_the_associator_identity_and_peak_at_i_over_7`
(𝒜(R) ≤ 672/343), `symmetric_vacuum_hessian_and_the_associator_coupling` (−48/7, 48/7, −96/7;
спектр 𝒬 — 48, 0¹², −24⁸), `colour_invariant_sector_is_solved_in_closed_form` и
`g2_invariant_vacuum_is_symmetric_or_colour_invariant_with_gap` (I/7 при малом κ, орбита S⁶ со
стабилизатором SU(3) и 𝒢 > 0 при большом; κ₁ = 0,0787μ²), `real_twirl_inequality_holds_in_its_proven_cases_and_on_samples`;
`real_twirl_inequality_is_a_sum_of_positive_forms` ((ВУ) доказано: дефект = Σ p_m Q_{u_m}(R − 𝒯R), Q_u ≥ 0),
`colour_sector_transitions_and_the_bound_on_mean_coherence` (λ* = 12,93μ², скачок ранг 7 → ранг 4 при κ₂;
ε̄ < √5/40) и `derived_sources_give_no_associator_cubic` (спектральное действие и функции спектра дают κ = 0).


Три — за восстановлением T-53b и T-118 (эмерджентное время §11.4, 25.09.2026):
`depth_register_carries_the_dissipative_arrow` (относительно цепи показаний со связью
Фейнмана–Китаева диссипативная полугруппа — условная динамика точно, на кольце стрела
ломается ровно на одном шаге), `regenerative_solution_is_a_conditional_history` и
`depth_register_time_algebra_is_the_line`.


Семь — за исправленной сборкой Стандартной модели (25.09.2026, T-326 … T-329):
система Клиффорда iL_{e_k}, J, iJ на ℂ⊗𝕆 единственна и максимальна (𝔰𝔭𝔦𝔫(9));
централизатор цвета в ней — 𝔲(2), нормализатор цвета — 12-мерная 𝔤_SM = 𝔠(R_{e_O});
ядро — ровно ℤ₆; (ℂ⊗𝕆, L_{e_O}) = (3,2)_{1/6} ⊕ (1,2)_{−1/2} и не самосопряжено;
семейная симметрия внутри одной копии невозможна, тройственность вращает 𝔲(1)²
на 120°; десятый генератор возвращает 𝔲(1)_{B−L}; у ℤ₇ три нетривиальные
вещественные гармоники.


Пять — за теоремами сильных оснований (25.09.2026), каждая восстанавливает [T] в верной
форме: `rank_strata_are_manifolds_of_dimension_14k_minus_k2_minus_1` (T-185 (ii′): страты
D(ℂ⁷) — многообразия, D_k ≃ Gr_k(ℂ⁷)), `g2_twirl_is_the_normalised_trace_projection`
(T-212′: «формула Rh» — G₂-скручивание), `octonionic_orientation_is_the_unique_collineation_invariant_class`
(T15-канон: единственный инвариантный класс ориентаций — 𝕆; 0 против 96 ассоциирующих троек,
метрика Брайанта (7,0) против (4,3)), `e7_rays_from_the_hamming_quadrangles_are_kochen_specker`
(T-201′: 63 луча, 135 базисов, раскраски нет) и
`hol_u_is_equivalent_to_seven_dimensional_qm_above_two_sevenths` (теорема 3.2′).


Пять — за задачей о живом аттракторе и чтении измерения (25.09.2026):
`unital_self_model_keeps_an_isolated_holon_dead` (унитальная самомодель — только I/7, P не растёт;
неподвижная точка φ_coh — I/7, а не P = 2/7), `self_registration_sustains_seven_living_attractors`
(φ_s с якорем Γ²/TrΓ² — семь живых аттракторов), `a_distant_holon_marginal_ignores_every_local_operation`
(вынужденное неселективное прочтение, запрет сигнализации), `abrams_lloyd_amplification_runs_on_marginals`
(седло усиливает 2⁻ⁿ за время O(n)) и `non_degeneracy_is_generic_and_aggregation_follows_from_weak_coupling`
((ND) у случайных якорей, (AGG b) с δ = O(g)).

Одна — за переформулировкой T-191 (башня φ, 25.09.2026):
`phi_tower_converges_only_under_backbone_dominance` (у изолированного голонома предел при
фиксированной цели зависит от старта — башня не определена; при μ > L_R + κ_max башня
сжимается с q = κ_max/(μ − L_R) и сходится к одной самомодели от любого якоря).

Одна — за хвостом Хиггса при (Кл) (25.09.2026): `no_higgs_doublet_in_the_clifford_frame`
(на 𝒮 = ℂ⊗𝕆 𝔰𝔲(2)_L действует одними дублетами, так что всякий оператор на 𝒮 — и всякая
когерентность Γ, в том числе γ_EU, — несёт целый спин; вектор Spin(9) — (3⊕3̄)_{±1/3} ⊕ (1,3)_0).

Восемь — за полным поколением (T-326 … T-329, вторая волна 25.09.2026):
`the_tenth_generator_is_forced_by_complexifying_the_spinor` (на 𝒮⊗_ℝℂ′ десятая образующая
вынуждена, ω = ±i′), `left_right_split_is_canonical_and_the_t326_su2_is_diagonal` (V_L ⊕ V_R,
ω = ±L_{e_O}; 𝔰𝔲(2) из T-326 — диагональ L ⊕ R, её 𝔲(1) — (B−L)/2),
`the_clock_stabiliser_gives_pati_salam_then_left_right_then_colour` (21 → 15; 18 → 12; 8),
`one_generation_with_a_right_handed_neutrino` (Y = (B−L)/2 + (i/2)|_{V_R}, Q = i/2 + (B−L)/2, ℤ₆),
`the_full_generation_is_anomaly_free`, `the_colour_singlet_clifford_plane_is_one_higgs_doublet`,
`exact_clock_z3_on_generations_forces_trivial_mixing` ((ПЧ) с точной ℤ₃ опровергнута) и
`fermions_are_vectors_of_s_not_operators_and_eta0_is_forced` ((Кл₀) не выводится из аксиом о Γ).


Четыре — за аттрактором в окне сознания (25.09.2026): `collineation_anchor_holds_a_living_attractor_in_the_window`
(якорь uu† коллинеаций Фано: при κ > κ_c один сток в V_full, спектр якобиана точен),
`phase_symmetric_self_models_hold_no_coherent_hyperbolic_state` (фазовое препятствие; Фано-регистрация
держит P = 1/3, но Φ = 0), `attractor_consistency_is_first_order_in_the_hamiltonian` (T-157 в верной
форме; прежняя граница ложна уже при H = 0) и `phi_coh_contracts_toward_i7_but_is_not_a_contraction`
(«φ — сжатие с коэффициентом k» неверно: липшицева константа 54/49 у чистых состояний).


Четыре — за теоремой 48d и переформулировкой T-119 (25.09.2026):
`no_unital_spin_factor_on_any_holon_register` (единичного спин-фактора нет на ℂ^{7^M}; G₂-коммутант
пары абелев, лапласиан регистра глубины с простым спектром), `colour_singlet_part_of_the_exceptional_jordan_algebra_is_hermitian_c3`
(J₃(𝕆)^{SU(3)} = Herm(ℂ³), пирсово пространство E₁ даёт h₂(ℂ_O) сигнатуры (1,3)),
`spatial_triplet_of_48c_is_the_weak_triplet` (в одной Spin(9) у цвета один централизатор 𝔲(2)) и
`emergent_space_is_the_octahedron_and_its_fluctuations_the_three_sphere` (средние — октаэдр ≅ B³,
флуктуации — ℝ³, минимальная унитизация — S³; цвет-синглетные координаты дают лишь 2).

Шесть — за юкавами в рамке Spin(10) и θ (T-332, T-333, 25.09.2026):
`up_and_down_are_where_the_hilbert_unit_meets_the_clock` (верх — i = L_{e_O}, низ — i = −L_{e_O};
параметр Gap вакуума T-64 — компонента T₃L), `clifford_yukawas_split_up_from_down_only_through_tau_r`
(юкав 2 / 4 / 8 при Пати–Салам / лево-правой / 𝔤_SM; |m_u| = |m_d| при всякой SU(2)_R-инвариантной),
`clock_phase_and_gap_vacuum_dressings_do_not_fit_the_masses`, `the_data_ask_for_an_up_projector_at_one_percent`
(t/b ≈ 68 при 2·10¹⁶ ГэВ, β/α = 0,971), `vacuum_antiunitary_lifts_are_gauge_parity_or_cp` и
`an_unbroken_cp_or_lr_symmetry_contradicts_the_quark_data` (CP ⇒ J = 0; L↔R при одном дублете ⇒ m_t = m_b).

Четыре — за теоремой 48e (25.09.2026): `two_level_systems_of_uhm_are_qubits_and_can_be_entangled`
(двухуровневая система УГМ — грань ранга 2, шар Блоха B³; (ММ) выполнено, 𝕂 = ℂ_O),
`colour_fixed_two_level_faces_of_holon_registers` (ℂ⁷ — 0, 𝒮 — лептонная прямая, пара — одна
симметричная грань), `no_rotation_of_the_internal_generation_commutes_with_the_gauge_group`
(коммутант 𝔤_SM в 𝔰𝔬(32) абелев, 6) и `fermion_space_is_weyl_spinor_times_one_generation`
(F = ℂ_O² ⊗_ℂ 𝒮_ℂ: 51 = 6 + 45, коммутант ℂ, 2 × 16 вейлевских компонент).


Четыре — за выводом якоря φ_J и окном параметров (25.09.2026, T-334 … T-336):
`frame_covariance_modulo_gauge_fixes_the_collineation_anchor` (Γ_oct нерасщепимо, коллинеаций-перестановок в нём 21,
орбита uu† — 64 знаковые перефазировки; однородные потоки на K₇ — только (0, 0) и (π, π); κ_c убывает по t),
`constant_anchor_window_attractor_is_explicit` (стационар (1 − η)diag ρ_a + ηρ_a и точный спектр; диагональный H
точно, Ω_c = 1,839 при κ = 40; H из span{I, J} любой нормы не сдвигает сток),
`no_self_model_holds_the_window_below_the_rate_floor` (κ ≥ 11,83 / 20,91 / 42,64 при любом H и любом якоре) и
`self_model_contraction_holds_only_for_constant_weight_and_unital_part` (лемма 2.1 — лишь при постоянных k и якоре и
унитальном P; у φ_J липшицева константа 1,129; неунитальный канал растягивает расстояние ГШ в √2 раз).

Четыре — за (ВП) и сильной CP в клиффордовом составе (26.09.2026, T-332(h)–(k), T-333(e)–(h)):
`up_projection_is_holomorphy_in_one_complex_doublet` (τ_Rγ(h) = ωγ(jh), j = 2ad Y на плоскости; (ВП) —
голоморфность по одному дублету), `an_exact_up_projection_leaves_the_tau_massless_to_all_orders` (при β = α
пять фаз вместо трёх: d^c с КХД-аномалией 1/2, e^c без неабелевой — m_τ = 0 во всех порядках),
`b_tau_and_the_size_of_the_up_projector_breaking` (ε = 0,0357 / 0,0292 / 0,0288; y_b = y_τ при 6,3·10⁶ ГэВ;
q/p = −0,349; ветвь ранга 4 на 94 из 99 точек) и `no_peccei_quinn_symmetry_in_the_clifford_content`
(при det Y_u, det Y_d ≠ 0 КХД-аномалия нулевая на 300 носителях; 𝟏𝟔 кирален; Γ_v коммутирует с (B−L)/2;
m_a = 2,9 нэВ, изокривизна — Ω_a/Ω_c ≲ 3·10⁻⁵).


Четыре — за источником κ, одним условием для якоря и неподвижными точками самомодели (26.09.2026):
`axis_permutations_average_the_associator_to_a_spectral_cubic` (среднее 𝒜 по перестановкам осей — уже по S₆ —
равно (96/5)e₃ при всякой калибровке; не по 168 коллинеациям), `symmetric_sources_carry_no_associator_weight_and_fano_readouts_carry_any`
(вес ассоциатора у S₇-инвариантных источников 0; у Фано-считываний 1/144, 1/72, 1/168, 49/11664 — зависит от функционала),
`fixed_points_of_self_models_and_the_gap_reflection_hierarchy` (Брауэр, а не Банах: у φ_J одна неподвижная точка Γ_η∞,
у φ_s не меньше восьми; Im φ(Γ) = kc Im Γ; итерации φ_J сходятся лишь при α < α* = 0,790) и
`one_clause_principle_for_the_anchor_is_maximal_integration` ((Рав-Ж) ⇔ Φ(ρ_a) = 6 ⇔ C_rel = log 7).

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


# ── G₂-инвариантный потенциал Gap: T-331 и T-64 в исправленной форме (25.09.2026) ──────────

@functools.lru_cache(maxsize=None)
def _assoc4():
    """a_{ijkl}: [e_i, e_j, e_k] = Σ_l a_{ijkl} e_l. Тензор вполне антисимметричен (a = 2ψ)."""
    A = np.zeros((7, 7, 7, 7))
    for i in range(7):
        for j in range(7):
            for k in range(7):
                x, y, z = unit(i + 1), unit(j + 1), unit(k + 1)
                A[i, j, k] = (omul(omul(x, y), z) - omul(x, omul(y, z)))[1:]
    return A


def _cal_a(G):
    """Ассоциаторный кубик 𝒜(Γ) = Σ ⟨[e_i,e_j,e_k],[e_a,e_b,e_c]⟩ Γ_ia Γ_jb Γ_kc = E‖[x,y,z]‖²."""
    A = _assoc4()
    return float(np.real(np.einsum('ijkl,ia,jb,kc,abcl->', A, G, G, G, A, optimize=True)))


def _cal_a_grad(G):
    """D_ia = ∂𝒜/∂Γ_ia (Γ как 49 независимых комплексных переменных)."""
    A = _assoc4()
    T = np.einsum('ijkl,jb,kc->ibcl', A, G, G, optimize=True)
    return 3 * np.einsum('ibcl,abcl->ia', T, A, optimize=True)


def _l_of(u):
    """Матрица L_u: y ↦ u × y (мнимая часть октонионного произведения)."""
    return np.einsum('xyz,x->zy', PHI3, u)


def _vg_value_grad(x, kap, l4, mu2=1.0):
    """V = μ²𝒢 + λ₄𝒢² − κ𝒜 на Γ = AA†/Tr и её градиент по 98 вещественным параметрам A."""
    A = (x[:49] + 1j * x[49:]).reshape(7, 7)
    M = A @ A.conj().T
    t = np.trace(M).real
    G = M / t
    g = float(np.sum(G.imag ** 2))
    V = mu2 * g + l4 * g * g - kap * _cal_a(G)
    H = (mu2 + 2 * l4 * g) * 2j * G.imag - kap * _cal_a_grad(G).T
    H = (H + H.conj().T) / 2
    K = (H - np.trace(H @ G).real * np.eye(7)) / t
    Gm = 2 * (K @ A)
    return V, np.concatenate([Gm.real.ravel(), Gm.imag.ravel()])


def _colour_family(a, b, c, v=O_AXIS):
    """Γ = a|v⟩⟨v| + bP_𝟑(v) + cP_𝟑̄(v) в осевом базисе: Re = a vvᵀ + (b+c)/2 (I − vvᵀ), Im = (b−c)/2 L_v."""
    e = np.eye(7)[v]
    return a * np.outer(e, e) + (b + c) / 2 * (np.eye(7) - np.outer(e, e)) + 0.5j * (b - c) * _l_of(e)


def _family_min(kap, l4, mu2=1.0):
    """Минимум V на SU(3)_v-инвариантных состояниях: s = b+c, d = b−c, 0 ≤ |d| ≤ s ≤ 1/3.

    При фиксированном s V — многочлен от d² со старшим членом (9/4)λ₄d⁴: минимум по d берётся
    при d = 0, при d = s или во внутренней точке d² = (72κ(1−3s) − (3/2)μ²)/((9/2)λ₄). Три ветви
    минимизируются по s на [0, 1/3]; ветвь d = 0 даёт −672κ/343 при s = 2/7 (состояние I/7).
    """
    from scipy.optimize import minimize_scalar

    def vfun(s, d):
        return 1.5 * mu2 * d * d + 2.25 * l4 * d ** 4 - kap * (48 * s ** 3 + 72 * (1 - 3 * s) * (s * s + d * d))

    def inner(s):
        if l4 <= 0:
            return 0.0
        d2 = (72 * kap * (1 - 3 * s) - 1.5 * mu2) / (4.5 * l4)
        return float(np.sqrt(min(max(d2, 0.0), s * s)))
    cands = [(vfun(2 / 7, 0.0), (2 / 7, 0.0)), (vfun(0.0, 0.0), (0.0, 0.0))]
    for branch in (lambda s: 0.0, lambda s: s, inner):
        r = minimize_scalar(lambda s: vfun(s, branch(s)), bounds=(0.0, 1 / 3), method='bounded',
                            options={'xatol': 1e-13})
        for s0 in np.linspace(0, 1 / 3, 61):
            if vfun(s0, branch(s0)) < r.fun:
                r = minimize_scalar(lambda s: vfun(s, branch(s)), bounds=(max(0, s0 - 0.01), min(1 / 3, s0 + 0.01)),
                                    method='bounded', options={'xatol': 1e-13})
        cands.append((r.fun, (r.x, branch(r.x))))
    return min(cands, key=lambda c: c[0])


def _g2_invariant_counts(dmax=4, N=36):
    """Размерности G₂-инвариантов в Sym(27 ⊕ 7 ⊕ 14) по степеням (S, X₇, X₁₄): интегрирование Вейля."""
    t = np.exp(2j * np.pi * np.arange(N) / N)
    T1, T2 = np.meshgrid(t, t, indexing='ij')
    eps = [(1, 0), (0, 1), (-1, -1)]
    w7 = [(0, 0)] + eps + [(-a, -b) for a, b in eps]
    roots = [w for w in w7 if w != (0, 0)] + [(a1 - a2, b1 - b2) for i, (a1, b1) in enumerate(eps)
                                              for j, (a2, b2) in enumerate(eps) if i != j]
    w14 = [(0, 0), (0, 0)] + roots
    w27 = [(a1 + a2, b1 + b2) for i, (a1, b1) in enumerate(w7) for j, (a2, b2) in enumerate(w7) if i <= j]
    w27.remove((0, 0))
    meas = np.ones_like(T1)
    for a, b in roots:
        meas = meas * (1 - T1 ** a * T2 ** b)
    meas = meas.real / 12

    def h(ws):
        p = [None] + [sum(T1 ** (k * a) * T2 ** (k * b) for a, b in ws) for k in range(1, dmax + 1)]
        out = [np.ones_like(T1)]
        for d in range(1, dmax + 1):
            out.append(sum(p[k] * out[d - k] for k in range(1, d + 1)) / d)
        return out
    hS, h7, h14 = h(w27), h(w7), h(w14)
    return {(s, a, b): int(round(np.mean(hS[s] * h7[a] * h14[b] * meas).real))
            for s in range(dmax + 1) for a in range(dmax + 1) for b in range(dmax + 1) if s + a + b <= dmax}


def test_g2_invariant_cubics_are_pt_even():
    """T-331(а): у G₂-инвариантных многочленов на Herm(ℂ⁷) до степени 3 нет PT-нечётных; на Im Γ нет кубика.

    Γ = I/7 + S + iX, S ∈ 27, X = X₇ + X₁₄. PT: X ↦ −X. Интегрирование Вейля по тору G₂ точно
    для тригонометрических многочленов этой степени. Квадратичных инвариантов три (|S|², |X₇|², |X₁₄|²),
    кубических пять — ни одного с нечётной степенью по X; кубика от одной Im Γ нет вовсе
    (у G₂ нет кубического Казимира). PT-нечётные появляются в степени 4, их три.
    Однородных кубиков по Γ (со следом) — девять.
    """
    c = _g2_invariant_counts()
    by_deg = lambda d, odd=None: sum(v for (s, a, b), v in c.items() if s + a + b == d
                                     and (odd is None or (a + b) % 2 == odd))
    assert [by_deg(d) for d in (1, 2, 3)] == [0, 3, 5]
    assert by_deg(1, 1) == by_deg(2, 1) == by_deg(3, 1) == 0
    assert by_deg(4, 1) == 3
    assert sum(v for (s, a, b), v in c.items() if s == 0 and a + b == 3) == 0
    assert 1 + by_deg(1) + by_deg(2) + by_deg(3) == 9


def test_frame_group_cubics_and_the_page_v3_average():
    """T-331(в): при одной рамочной симметрии Γ_oct кубиков 25, PT-нечётных 3; среднее V₃ страницы — ноль.

    Треугольники Im(γ_ij γ_jk γ_ki) не чувствуют смен знака, знакопеременны по (i,j,k), а стабилизатор
    треугольника в коллинеациях переставляет его вершины всеми способами: Γ_oct-инвариантной
    знакопеременной весовой функции нет, и усреднение V₃ по Γ_oct даёт ноль.
    """
    grp = [M for _, M in frame_group()]

    def sym_char(Q, d, pt):
        p = [None]
        for k in range(1, d + 1):
            Qk = np.linalg.matrix_power(Q, k)
            t1, t2 = np.trace(Qk), np.trace(Qk @ Qk)
            p.append((t1 * t1 + t2) / 2 + ((-1) ** k if pt else 1) * (t1 * t1 - t2) / 2)
        h = [1.0]
        for n in range(1, d + 1):
            h.append(sum(p[k] * h[n - k] for k in range(1, n + 1)) / n)
        return h[d]
    inv = np.mean([sym_char(Q, 3, False) for Q in grp])
    even = np.mean([(sym_char(Q, 3, False) + sym_char(Q, 3, True)) / 2 for Q in grp])
    assert (round(inv), round(inv - even)) == (25, 3)
    G = random_state(np.random.default_rng(370))
    assert abs(_v3(G)) > 1e-4 and abs(np.mean([_v3(M @ G @ M.T) for M in grp])) < 1e-15


def test_associator_cubic_is_invariant_positive_and_factors_through_lambda3_7():
    """T-331(г, д): 𝒜 G₂-инвариантен, PT-чётен, ≥ 0, равен 96·Tr(Π₇ Λ³Γ) и молчит на ассоциативных состояниях.

    Π₇ — проектор на Λ³₇ = {ι_v ψ} ⊂ Λ³ℂ⁷. На координатной тройке 𝒜 = 6‖[e_i,e_j,e_k]‖²/27:
    0 на линии Фано, 24/27 вне её — веса V₃ страницы, но в квадрате. На состояниях ранга ≤ 2
    и на состояниях в плоскости линии Фано (и в любой её G₂-копии) 𝒜 = 0.
    """
    rng = np.random.default_rng(371)
    G = random_state(rng)
    g = expm(sum(c * X for c, X in zip(rng.normal(size=14), G2)))
    assert abs(_cal_a(g @ G @ g.T) - _cal_a(G)) < 1e-12 and abs(_cal_a(G.conj()) - _cal_a(G)) < 1e-14
    assert min(_cal_a(random_state(rng)) for _ in range(20)) > 0
    trip = list(itertools.combinations(range(7), 3))
    idx = {t: n for n, t in enumerate(trip)}

    def lam3(M):
        return np.array([[np.linalg.det(M[np.ix_(a, b)]) for b in trip] for a in trip])
    psi = _assoc4() / 2
    vecs = np.array([[psi[a, b, c, l] for (a, b, c) in trip] for l in range(7)]).T
    Q, _ = np.linalg.qr(vecs)
    P7 = Q @ Q.T
    for _ in range(3):
        G = random_state(rng)
        assert abs(96 * np.trace(P7 @ lam3(G)).real - _cal_a(G)) < 1e-12
    for i, j, k in [(0, 1, 3), (0, 1, 2)]:
        D = np.zeros((7, 7))
        D[[i, j, k], [i, j, k]] = 1 / 3
        on_line = tuple(sorted((i + 1, j + 1, k + 1))) in {tuple(sorted(l)) for l in LINES}
        assert abs(_cal_a(D) - (0 if on_line else 24 / 27)) < 1e-12
    for _ in range(3):
        B = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
        H = np.zeros((7, 7), complex)
        H[np.ix_([0, 1, 3], [0, 1, 3])] = B @ B.conj().T
        g = expm(sum(c * X for c, X in zip(rng.normal(size=14), G2)))
        assert abs(_cal_a(g @ H @ g.T)) < 1e-12
        W = rng.normal(size=(7, 2)) + 1j * rng.normal(size=(7, 2))
        assert abs(_cal_a(W @ W.conj().T)) < 1e-12


def test_real_states_obey_the_associator_identity_and_peak_at_i_over_7():
    """T-64(б): для вещественных R = Σ p_m u_m u_mᵀ  𝒜(R) = 4 Σ p_m[(1−p_m)² − 2|R⁺_m|²] ≤ 672/343.

    R⁺_m — часть R на u_m^⊥, коммутирующая с J_m = L_{u_m}; |R⁺_m|² ≥ (1−p_m)²/6, так что
    𝒜(R) ≤ (8/3) Σ p_m(1−p_m)² ≤ 96/49 = 672/343, равенство только при R = I/7.
    """
    rng = np.random.default_rng(372)
    for _ in range(30):
        k = rng.integers(1, 8)
        W = rng.normal(size=(7, k))
        R = W @ W.T / np.trace(W @ W.T)
        p, U = np.linalg.eigh(R)
        rhs = 0.0
        for m in range(7):
            u = U[:, m]
            P, J = np.eye(7) - np.outer(u, u), _l_of(u)
            Rp = (P @ R @ P + J @ R @ J.T) / 2
            rhs += 4 * p[m] * ((1 - p[m]) ** 2 - 2 * np.sum(Rp * Rp))
        assert abs(_cal_a(R) - rhs) < 1e-12
        assert _cal_a(R) <= 8 / 3 * np.sum(p * (1 - p) ** 2) + 1e-12 and _cal_a(R) < 672 / 343
    assert abs(_cal_a(np.eye(7) / 7) - 672 / 343) < 1e-13


def test_symmetric_vacuum_hessian_and_the_associator_coupling():
    """T-64(в): у I/7 вторые коэффициенты 𝒜 — −48/7 на 27, +48/7 на 7, −96/7 на 14; 𝒬(e_O e_Oᵀ) = {48, 0¹², −24⁸}.

    𝒜(R + iX) − 𝒜(R) = Q_R(X) — квадратичная форма по X, линейная по R. При R = e_O e_Oᵀ её спектр:
    48 на L_{e_O}, −24 на 𝔰𝔲(3)_O, 0 на двенадцати остальных. Отсюда Q_R(X) ≤ 48|X|² и
    Q_R(X) ≤ 288 wᵀRw при X₇ = L_w; I/7 — строгий локальный минимум V ровно при κ < 7μ²/48.
    """
    rng = np.random.default_rng(373)
    I7 = np.eye(7) / 7
    S = rng.normal(size=(7, 7))
    S = S + S.T - 2 * np.trace(S) / 7 * np.eye(7)
    X = rng.normal(size=(7, 7))
    X = X - X.T
    x7 = np.einsum('ijk,k->ij', PHI3, np.einsum('ijk,ij->k', PHI3, X)) / 6
    x14 = X - x7
    q = lambda D: (_cal_a(I7 + 1e-2 * D) + _cal_a(I7 - 1e-2 * D) - 2 * _cal_a(I7)) / 2e-4
    assert abs(q(S) / np.sum(S * S) + 48 / 7) < 1e-8
    assert abs(q(1j * x7) / np.sum(x7 * x7) - 48 / 7) < 1e-8
    assert abs(q(1j * x14) / np.sum(x14 * x14) + 96 / 7) < 1e-8
    basis = []
    for i in range(7):
        for j in range(i + 1, 7):
            E = np.zeros((7, 7))
            E[i, j], E[j, i] = 2 ** -0.5, -2 ** -0.5
            basis.append(E)
    Ro = np.zeros((7, 7))
    Ro[O_AXIS, O_AXIS] = 1
    base = _cal_a(Ro.astype(complex))
    Qm = np.zeros((21, 21))
    for a in range(21):
        for b in range(a, 21):
            qa, qb = _cal_a(Ro + 1j * basis[a]) - base, _cal_a(Ro + 1j * basis[b]) - base
            Qm[a, b] = Qm[b, a] = qa if a == b else (_cal_a(Ro + 1j * (basis[a] + basis[b])) - base - qa - qb) / 2
    w, V = np.linalg.eigh(Qm)
    assert np.allclose(w, [-24] * 8 + [0] * 12 + [48], atol=1e-9)
    Lo = _l_of(np.eye(7)[O_AXIS])
    lo = np.array([np.sum(Lo * E) for E in basis])
    assert abs(abs(V[:, -1] @ lo) / np.linalg.norm(lo) - 1) < 1e-9
    su3 = np.array([[np.sum(Y * E) for E in basis] for Y in _su3_of_e_o()]).T
    assert np.linalg.norm(su3 - V[:, :8] @ (V[:, :8].T @ su3)) < 1e-9


def test_colour_invariant_sector_is_solved_in_closed_form():
    """T-64(д): на Γ = a|v⟩⟨v| + bP_𝟑 + cP_𝟑̄  𝒜 = 48(b+c)³ + 144a(b²+c²), 𝒢 = (3/2)(b−c)².

    Максимум 𝒜 на всём D(ℂ⁷) равен 3 и берётся в (1/4)(|v⟩⟨v| + P_𝟑); на вещественных — 672/343.
    Стабилизатор такого состояния в 𝔤₂ — 𝔰𝔲(3)_v (размерность 8): орбита — G₂/SU(3) = S⁶.
    """
    rng = np.random.default_rng(374)
    for _ in range(10):
        a, b, c = rng.normal(size=3)
        G = _colour_family(a, b, c)
        assert abs(_cal_a(G) - 48 * (b + c) ** 3 - 144 * a * (b * b + c * c)) < 1e-10
        assert abs(_gap_total(G) - 1.5 * (b - c) ** 2) < 1e-12
    G = _colour_family(0.25, 0.25, 0.0)
    assert abs(np.trace(G).real - 1) < 1e-12 and np.linalg.eigvalsh(G).min() > -1e-12
    assert abs(_cal_a(G) - 3) < 1e-12 and abs(_gap_total(G) - 3 / 32) < 1e-12
    M = np.array([(X @ G - G @ X).ravel() for X in G2]).T
    assert int(np.sum(np.linalg.svd(np.vstack([M.real, M.imag]), compute_uv=False) < 1e-9)) == 8


def test_g2_invariant_vacuum_is_symmetric_or_colour_invariant_with_gap():
    """T-64(б–е): глобальный минимум V = μ²𝒢 + λ₄𝒢² − κ𝒜 совпадает с минимумом на цветово-инвариантных.

    При κ = 0,05 (λ₄ = 1) вакуум — I/7 (стабилизатор 14, 𝒢 = 0); при κ = 0,2 — состояние
    a|v⟩⟨v| + bP_𝟑 ранга 4 со стабилизатором 𝔰𝔲(3)_v (8) и 𝒢 > 0: спонтанный Gap при сохранённом
    цвете. Порог первого рода при λ₄ = 0: κ₁ = 0,0787μ² (−4A³/27B² = −672κ/343, A = 144κ − 3/2, B = 384κ).
    """
    from scipy.optimize import minimize, brentq
    rng = np.random.default_rng(375)
    for kap, stab, gap_pos in [(0.05, 14, False), (0.2, 8, True)]:
        fv, _ = _family_min(kap, 1.0)
        runs = []
        for _ in range(5):
            r = minimize(_vg_value_grad, rng.normal(size=98), args=(kap, 1.0), jac=True, method='L-BFGS-B',
                         options={'maxiter': 50000, 'ftol': 1e-16, 'gtol': 1e-11})
            runs.append(r)
        best = min(runs, key=lambda r: r.fun)
        assert abs(best.fun - fv) < 1e-8
        A = (best.x[:49] + 1j * best.x[49:]).reshape(7, 7)
        G = A @ A.conj().T
        G /= np.trace(G).real
        M = np.array([(X @ G - G @ X).ravel() for X in G2]).T
        assert int(np.sum(np.linalg.svd(np.vstack([M.real, M.imag]), compute_uv=False) < 1e-4)) == stab
        assert (_gap_total(G) > 1e-3) == gap_pos
    k1 = brentq(lambda k: 4 * (144 * k - 1.5) ** 3 / (27 * (384 * k) ** 2) - 672 * k / 343, 0.03, 0.14)
    assert abs(k1 - 0.0787) < 1e-4 and 1 / 48 < k1 < 7 / 48


def test_real_twirl_inequality_holds_in_its_proven_cases_and_on_samples():
    """(RT): 𝒜(R) ≤ 8rt² + (16/9)t³ при r = ⟨ŵ,Rŵ⟩, t = 1 − r; доказано при β = 0 и при M⁻ = 0.

    R = [[M, β],[βᵀ, r]] в базисе (ŵ^⊥, ŵ), ŵ = e_O. При β = 0: 𝒜 = 12r(t² − 2|M⁺|²) + 𝒜₆(M),
    𝒜₆(M) ≤ (16/9)t³. При M⁻ = 0: дефект D = 24r(|M⁺|² − t²/6) + 24βᵀ(tI − 2M⁺)β + 8TrM⁺³ − (2/9)t³.
    Вне этих случаев неравенство проверено выборкой; равенство — на SU(3)_ŵ-скручивании R.
    """
    rng = np.random.default_rng(376)
    J = _l_of(np.eye(7)[O_AXIS])[:6, :6]

    def block(M, b, r):
        R = np.zeros((7, 7))
        R[:6, :6], R[:6, O_AXIS], R[O_AXIS, :6], R[O_AXIS, O_AXIS] = M, b, b, r
        return R
    for _ in range(20):
        r = rng.uniform(0.01, 0.9)
        t = 1 - r
        W = rng.normal(size=(6, 6))
        M = W @ W.T
        M *= t / np.trace(M)
        Mp = (M + J @ M @ J.T) / 2
        R6 = block(M, np.zeros(6), 0.0)
        assert abs(_cal_a(block(M, np.zeros(6), r)) - 12 * r * (t * t - 2 * np.sum(Mp * Mp)) - _cal_a(R6)) < 1e-12
        assert _cal_a(R6) <= 16 / 9 * t ** 3 + 1e-12
        L = np.linalg.cholesky(Mp)
        xi = rng.normal(size=6)
        b = np.sqrt(r) * L @ (xi / (np.linalg.norm(xi) * rng.uniform(1, 2)))
        D = 8 * r * t * t + 16 / 9 * t ** 3 - _cal_a(block(Mp, b, r))
        pred = (24 * r * (np.sum(Mp * Mp) - t * t / 6) + 24 * b @ (t * np.eye(6) - 2 * Mp) @ b
                + 8 * np.trace(Mp @ Mp @ Mp) - 2 / 9 * t ** 3)
        assert abs(D - pred) < 1e-12 and pred >= -1e-14
    e_w = np.eye(7)[O_AXIS]
    Lw, Pw = _l_of(e_w), np.eye(7) - np.outer(e_w, e_w)
    for _ in range(10):                      # шестимерное тождество: 𝒜(M) = 4Σ p_m[(t−p_m)² − 2|M_W⁺|² − 2|c|² − q_m²]
        W = np.zeros((7, 6))
        W[:6] = rng.normal(size=(6, 6))
        M = W @ W.T / np.trace(W @ W.T)
        p, U = np.linalg.eigh(M[:6, :6])
        rhs, qsum = 0.0, 0.0
        for m in range(6):
            u = np.zeros(7)
            u[:6] = U[:, m]
            Ju = Lw @ u
            PW = Pw - np.outer(u, u) - np.outer(Ju, Ju)
            K = _l_of(u) @ PW
            MW = PW @ M @ PW
            MWp = (MW + K @ MW @ K.T) / 2
            cvec, q = PW @ M @ Ju, Ju @ M @ Ju
            qsum += q
            rhs += 4 * p[m] * ((1 - p[m]) ** 2 - 2 * np.sum(MWp * MWp) - 2 * cvec @ cvec - q * q)
        assert abs(_cal_a(M) - rhs) < 1e-12 and abs(qsum - 1) < 1e-12
    for _ in range(1500):
        k = rng.integers(1, 8)
        W = rng.normal(size=(7, k))
        R = W @ W.T / np.trace(W @ W.T)
        r = R[O_AXIS, O_AXIS]
        assert _cal_a(R) <= 8 * r * (1 - r) ** 2 + 16 / 9 * (1 - r) ** 3 + 1e-12



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
# Стандартная модель на комплексных октонионах (25.09.2026, T-326 … T-329).
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
    """T-326(а): iL_{e_1..7}, J, iJ на 𝒮 = ℂ⊗𝕆 ≅ ℝ¹⁶ — система Клиффорда Cl(9,0), и она единственна.

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
    """T-326(б): 𝔠_{𝔰𝔭𝔦𝔫(9)}(𝔰𝔲(3)_C) = 𝔲(2); 𝔫(𝔰𝔲(3)_C) = 𝔰𝔲(3)⊕𝔰𝔲(2)⊕𝔲(1) = 𝔠(R_{e_O}).

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
    """T-326(в): ядро SU(3)×SU(2)×U(1) → Spin(9) на 𝒮 — ровно ℤ₆ = {(ω^a, (−1)^b, ω^{−a}(−1)^b)}.

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
    """T-327: (𝒮, L_{e_O}) = (3,2)_{1/6} ⊕ (1,2)_{−1/2}; сопряжённое не изоморфно — тест Дистлера–Гарибальди.

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
    """T-328(а,б): на 𝒮 с 𝔤_SM коммутируют лишь фазы U(1)_B×U(1)_L; тройственность вращает 𝔲(1)² на 120°.

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
    """T-329: добавив к системе десятый генератор (ℝ³² = 𝒮⊗ℝ²), получаем 𝔠_{𝔰𝔭𝔦𝔫(10)}(𝔰𝔲(3)_C) размерности 7.

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
    """T-328(в): у ℤ₇ три нетривиальных вещественных неприводимых представления; Aut(ℤ₇)/{±1} ≅ ℤ₃ переставляет их просто транзитивно.

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


# ---------------------------------------------------------------------------
# Сильные основания (25.09.2026): когезия, эквивалентность с КМ, ориентация Фано,
# контекстуальность Кохена–Шпекера. Пять свидетелей новых теорем [T].
# ---------------------------------------------------------------------------

def test_rank_strata_are_manifolds_of_dimension_14k_minus_k2_minus_1():
    """Страт D_k = {rank Γ = k} — гладкое многообразие размерности 14k − k² − 1; D_7 открыт (48).

    Свидетель T-185 (ii′): состояния лежат в Smooth∞Grpd как стратифицированный объект,
    каждый страт — многообразие; прямолинейная ретракция на P_V/k остаётся в страте
    (D_k ≃ Gr_k(ℂ⁷), форма ∫D_k — тип Грассманиана, ∫D = *).
    """
    rng = np.random.default_rng(21)
    for k in range(1, 8):
        A = rng.normal(size=(7, k)) + 1j * rng.normal(size=(7, k))

        def rho(a):
            M = a.reshape(7, k, 2)
            B = M[..., 0] + 1j * M[..., 1]
            R = B @ B.conj().T
            R = R / np.trace(R).real
            return np.concatenate([R.real.ravel(), R.imag.ravel()])
        a0 = np.stack([A.real, A.imag], axis=-1).ravel()
        J = np.zeros((98, a0.size))
        h = 1e-6
        for t in range(a0.size):
            e = np.zeros(a0.size)
            e[t] = h
            J[:, t] = (rho(a0 + e) - rho(a0 - e)) / (2 * h)
        s = np.linalg.svd(J, compute_uv=False)
        dim = int((s > 1e-6 * s[0]).sum())
        assert dim == 14 * k - k * k - 1, (k, dim)
        R = A @ A.conj().T
        R /= np.trace(R).real
        w, V = np.linalg.eigh(R)
        P = V[:, -k:] @ V[:, -k:].conj().T
        for t in np.linspace(0, 1, 11):
            X = (1 - t) * R + t * P / k
            assert np.linalg.matrix_rank(X, tol=1e-10) == k


def test_g2_twirl_is_the_normalised_trace_projection():
    """Коммутант g₂ на ℂ⁷ одномерен: G₂-скручивание X ↦ ∫ gXg† dg равно (1/7)Tr(X)·I.

    Свидетель T-212′ [T]: «формула Rh» — это G₂-скручивание (проекция на инварианты),
    идемпотентное лишь с нормированным следом (с Tr: E∘E = 7E). Модальность Rh твёрдой
    когезии сохраняет глобальные точки (Rh X(ℝ⁰) = X(ℝ⁰)) и формулой не является.
    """
    rows = []
    for D in G2:
        rows.append(np.kron(D, np.eye(7)) - np.kron(np.eye(7), D.T))   # vec([D, X]) (построчно)
    L = np.vstack(rows)
    s = np.linalg.svd(L, compute_uv=False)
    null = int((s < 1e-10).sum()) + (49 - len(s) if len(s) < 49 else 0)
    assert null == 1
    rng = np.random.default_rng(5)
    X = rng.normal(size=(7, 7)) + 1j * rng.normal(size=(7, 7))
    _, _, Vh = np.linalg.svd(L)
    n = Vh[-1].conj()
    n = n / np.linalg.norm(n)
    proj = (n.conj() @ X.ravel()) * n
    assert np.linalg.norm(proj.reshape(7, 7) - np.trace(X) / 7 * np.eye(7)) < 1e-10
    E1 = lambda Y: np.trace(Y) / 7 * np.eye(7)
    Et = lambda Y: np.trace(Y) * np.eye(7)
    assert np.linalg.norm(E1(E1(X)) - E1(X)) < 1e-12
    assert np.linalg.norm(Et(Et(X)) - 7 * Et(X)) < 1e-9


def _fano_orientation_data():
    rng = np.random.default_rng(11)
    samples = [(rng.normal(size=8), rng.normal(size=8)) for _ in range(4)]

    def mul_for(signs):
        lines = [(i, j, k) if s > 0 else (j, i, k) for (i, j, k), s in zip(LINES, signs)]

        def mul(a, b):
            c = np.zeros(8)
            c[0] = a[0] * b[0] - np.dot(a[1:], b[1:])
            c[1:] += a[0] * b[1:] + b[0] * a[1:]
            for i, j, k in lines:
                for x, y, z in ((i, j, k), (j, k, i), (k, i, j)):
                    c[z] += a[x] * b[y] - a[y] * b[x]
            return c
        return mul

    def normed(signs):
        mul = mul_for(signs)
        return all(abs(np.linalg.norm(mul(x, y)) - np.linalg.norm(x) * np.linalg.norm(y)) < 1e-9
                   for x, y in samples)

    def flip(signs, S):
        return tuple(-s if sum(p in S for p in line) % 2 else s for line, s in zip(LINES, signs))

    subsets = [set(c) for r in range(8) for c in itertools.combinations(range(1, 8), r)]
    allsig = list(itertools.product((1, -1), repeat=7))
    cls = {s: frozenset(flip(s, S) for S in subsets) for s in allsig}
    sets = [frozenset(l) for l in LINES]
    coll = [p for p in itertools.permutations(range(1, 8))
            if all(frozenset(p[x - 1] for x in l) in sets for l in LINES)]

    def act(p, signs):
        out = [0] * 7
        for (i, j, k), s in zip(LINES, signs):
            a, b, c = (p[i - 1], p[j - 1], p[k - 1]) if s > 0 else (p[j - 1], p[i - 1], p[k - 1])
            idx = sets.index(frozenset((a, b, c)))
            L0 = LINES[idx]
            rots = {L0, (L0[1], L0[2], L0[0]), (L0[2], L0[0], L0[1])}
            out[idx] = 1 if (a, b, c) in rots else -1
        return tuple(out)
    return mul_for, normed, cls, coll, act


def test_octonionic_orientation_is_the_unique_collineation_invariant_class():
    """Из 8 калибровочных классов ориентаций линий Фано (по 16) инвариантен относительно
    группы коллинеаций GL(3,2) ровно один — нормированный (𝕆); остальные семь — одна
    орбита, каждый выделяет одну линию. Три равносильные характеристики класса 𝕆:
    инвариантность, ни одной ассоциирующей независимой тройки (0 из 168 против 96),
    знакоопределённая метрика Брайанта 3-формы (7,0) против (4,3).

    Свидетель теоремы T15-канон [T] (строка 41n): (Alt) ⟺ каноничность ориентации.
    """
    mul_for, normed, cls, coll, act = _fano_orientation_data()
    classes = set(cls.values())
    assert len(coll) == 168 and len(classes) == 8 and all(len(c) == 16 for c in classes)
    fixed = [c for c in classes if all(cls[act(p, next(iter(c)))] == c for p in coll)]
    good = {s for s in cls if normed(s)}
    assert len(fixed) == 1 and set(fixed[0]) == good
    rest = [c for c in classes if c != fixed[0]]
    orbit = {cls[act(p, next(iter(rest[0])))] for p in coll}
    assert len(orbit) == 7
    signs_o = next(iter(fixed[0]))
    eps = {}
    for p in itertools.permutations(range(7)):
        inv = sum(1 for a in range(7) for b in range(a + 1, 7) if p[a] > p[b])
        eps[p] = -1 if inv % 2 else 1
    for c in [fixed[0]] + rest:
        signs = next(iter(c))
        mul = mul_for(signs)
        assoc = sum(1 for i, j, k in itertools.permutations(range(1, 8), 3)
                    if {i, j, k} not in [set(l) for l in LINES]
                    and np.allclose(mul(mul(unit(i), unit(j)), unit(k)), mul(unit(i), mul(unit(j), unit(k)))))
        phi = np.zeros((7, 7, 7))
        for (i, j, k), s in zip(LINES, signs):
            for (x, y, z), t in (((i, j, k), 1), ((j, k, i), 1), ((k, i, j), 1),
                                 ((j, i, k), -1), ((i, k, j), -1), ((k, j, i), -1)):
                phi[x - 1, y - 1, z - 1] = s * t
        B = np.zeros((7, 7))
        for p, e in eps.items():
            B += e * np.outer(phi[:, p[0], p[1]], phi[:, p[2], p[3]]) * phi[p[4], p[5], p[6]]
        assert np.abs(B - np.diag(np.diag(B))).max() < 1e-9
        pos = int((np.diag(B) > 0).sum())
        if c == fixed[0]:
            assert assoc == 0 and (pos == 7 or pos == 0)
        else:
            assert assoc == 96 and pos in (3, 4)


def _e7_rays():
    quads = [tuple(p for p in range(1, 8) if p not in l) for l in LINES]
    vecs = [unit(i)[1:] for i in range(1, 8)]
    for q in quads:
        for sg in itertools.product((1, -1), repeat=4):
            if sg[0] < 0:
                continue
            v = np.zeros(7)
            for s, p in zip(sg, q):
                v[p - 1] = s / 2
            vecs.append(v)
    return np.array(vecs)


def test_e7_rays_from_the_hamming_quadrangles_are_kochen_specker():
    """63 луча в ℝ⁷ ⊂ ℂ⁷ — семь осей и ½(±e_a±e_b±e_c±e_d) на семи дополнениях линий Фано
    (слова веса 4 кода Хэмминга): корни E₇ (мнимые единицы целых октонионов Кокстера).
    135 ортонормированных базисов, каждый луч — в 15; раскраски 0/1 с ровно одной
    единицей в каждом базисе нет (MILP — недопустимо). Ориентация линий не участвует.

    Свидетель T-201′ [T]: контекстуальность Кохена–Шпекера в ℂ⁷ с некоммутирующими проекторами
    (Ruuge, J. Phys. A 40, 2849 (2007) — конфигурация E₇ 63₁₅–135₇).
    """
    from scipy.optimize import Bounds, LinearConstraint, milp
    R = _e7_rays()
    n = len(R)
    assert n == 63
    V = np.vstack([R, -R])
    S = {tuple(np.round(v, 9)) for v in V}
    assert all(tuple(np.round(v - 2 * (u @ v) * u, 9)) in S for u in V for v in V)   # система корней
    G = np.abs(R @ R.T) < 1e-9
    bases = []

    def ext(cur, cand):
        if len(cur) == 7:
            bases.append(tuple(cur))
            return
        for idx, c in enumerate(cand):
            ext(cur + [c], [d for d in cand[idx + 1:] if G[c, d]])
    ext([], list(range(n)))
    assert len(bases) == 135
    assert all(sum(r in b for b in bases) == 15 for r in range(n))
    A = np.zeros((len(bases), n))
    for k, b in enumerate(bases):
        A[k, list(b)] = 1
    res = milp(c=np.zeros(n), constraints=[LinearConstraint(A, 1, 1)],
               integrality=np.ones(n), bounds=Bounds(0, 1))
    assert res.status == 2                                   # раскраски нет
    sub = A[[k for k, b in enumerate(bases) if 0 in b]]
    res = milp(c=np.zeros(n), constraints=[LinearConstraint(sub, 1, 1)],
               integrality=np.ones(n), bounds=Bounds(0, 1))
    assert res.status == 0                                   # прибор умеет находить раскраску
    assert int(((~G).sum() - n) // 2) == 1008                # некоммутирующих пар лучей (из 1953)


def test_hol_u_is_equivalent_to_seven_dimensional_qm_above_two_sevenths():
    """Hol^u ≃ QM₇^{P>2/7}: включение полно и верно, существенная сюръективность — перестановкой,
    переводящей вектор носителя в ось E. Чистота — инвариант изоморфизма КМ; при d ≤ 3
    любое состояние имеет P ≥ 1/3 > 2/7 и вкладывается изометрией, при d = 4 состояние I/4
    (P = 1/4) не вкладывается никак: граница d ≤ 3 точна.
    """
    rng = np.random.default_rng(31)
    for _ in range(20):
        G = random_state(rng)
        v = rng.normal(size=7) + 1j * rng.normal(size=7)
        U = np.linalg.qr(v.reshape(7, 1) @ np.ones((1, 7)) + rng.normal(size=(7, 7)))[0]
        assert abs(purity(U @ G @ U.conj().T) - purity(G)) < 1e-12
    G = np.zeros((7, 7), complex)
    G[0, 0], G[1, 1] = 0.7, 0.3                               # γ_EE = 0, P = 0,58 > 2/7
    assert G[E_AXIS, E_AXIS] == 0 and purity(G) > 2 / 7
    j = int(np.argmax(np.real(np.diag(G))))
    perm = list(range(7))
    perm[j], perm[E_AXIS] = perm[E_AXIS], perm[j]
    Pm = np.eye(7)[perm]
    G2_ = Pm @ G @ Pm.T
    assert G2_[E_AXIS, E_AXIS].real > 0 and abs(purity(G2_) - purity(G)) < 1e-15
    for d in (2, 3):
        assert 1 / d > 2 / 7
    assert 1 / 4 < 2 / 7
    Ua = np.linalg.qr(rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)))[0]
    Ub = np.linalg.qr(rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)))[0]
    emb = lambda W: np.block([[W, np.zeros((3, 4))], [np.zeros((4, 3)), np.eye(4)]])
    assert np.linalg.norm(emb(Ua @ Ub) - emb(Ua) @ emb(Ub)) < 1e-13   # функтор


def _frozen_self_registering(G, H, kap=1.0, alpha=0.5, anchor="self"):
    """Замороженный на Γ генератор M^(Γ) голонома с регенерацией к φ_s(Γ) = k P_α(Γ) + R·Γ²/TrΓ².

    Возвращает линейную карту X ↦ M^(Γ)(X): −i[H, X] + ⅔(diag X − X) + κ g_V(P) (k P_α(X) + R σ Tr X − X),
    σ = Γ²/TrΓ² (якорь саморегистрации) или I/7 (канонический φ_coh). Скаляры читаются на Γ.
    """
    P = purity(G)
    R = 1 / (7 * P)
    k = 1 - R
    sig = G @ G / P if anchor == "self" else np.eye(7) / 7
    kg = kap * gate(P)

    def M(X):
        D = np.diag(np.diag(X))
        Pa = D + (1 - alpha) / 3 * (X - D)
        return -1j * (H @ X - X @ H) + (2 / 3) * (D - X) + kg * (k * Pa + R * sig * np.trace(X) - X)
    return M


def _jacobian(f, G, h=1e-6):
    B = []
    for i in range(7):
        for j in range(i + 1, 7):
            M = np.zeros((7, 7), complex)
            M[i, j] = M[j, i] = 1 / np.sqrt(2)
            B.append(M)
            M = np.zeros((7, 7), complex)
            M[i, j], M[j, i] = -1j / np.sqrt(2), 1j / np.sqrt(2)
            B.append(M)
    for m in range(6):
        d = np.zeros(7)
        d[:m + 1], d[m + 1] = 1, -(m + 1)
        B.append(np.diag(d / np.linalg.norm(d)).astype(complex))
    J = np.zeros((48, 48))
    for a, Ba in enumerate(B):
        dF = (f(G + h * Ba) - f(G - h * Ba)) / (2 * h)
        J[:, a] = [np.real(np.trace(Bb @ dF)) for Bb in B]
    return J


def test_unital_self_model_keeps_an_isolated_holon_dead():
    """Унитальная самомодель — мёртвый голоном: единственная стационарная точка I/7, P не растёт.

    Свидетель теоремы о мёртвой изоляции (эволюция, T-96): при каноническом φ_coh (якорь I/7) и
    D_Fano чистота монотонно убывает по траектории даже при κ = 10, все старты приходят в I/7;
    итерации φ_coh дают P = 1/7, а не 2/7; φ, ковариантный относительно G₂ или реперной группы
    Γ_oct, унитален (коммутант обоих — скаляры); «якорь = собственный аттрактор» даёт унитальный
    kP_α + R·id. Перестановки Фано без знаков оставляют двумерный коммутант (I и J).
    """
    def commutant(mats, lie):
        A = np.vstack([np.kron(M, np.eye(7)) - np.kron(np.eye(7), M.T) if lie else np.kron(M, M) - np.eye(49)
                       for M in mats])
        return int(np.sum(np.linalg.svd(A, compute_uv=False) < 1e-9))
    group = frame_group()
    assert commutant(G2, True) == 1 and commutant([M for _, M in group], False) == 1
    assert commutant([np.abs(M) for _, M in group], False) == 2
    rng = np.random.default_rng(0)
    H = 0.3 * (lambda A: (A + A.conj().T) / 2)(rng.normal(size=(7, 7)) + 1j * rng.normal(size=(7, 7)))
    pa = lambda G: np.diag(np.diag(G)) + (G - np.diag(np.diag(G))) / 6               # P_α при α = 1/2
    phi = lambda G: (1 - 1 / (7 * purity(G))) * pa(G) + np.eye(7) / (49 * purity(G))   # φ_coh, якорь I/7
    X = random_pure(rng)
    for _ in range(200):
        X = phi(X)
    assert abs(purity(X) - 1 / 7) < 1e-12                                            # не 2/7
    rho = random_state(rng)
    own = lambda G: (1 - 1 / (7 * purity(rho))) * pa(G) + G / (7 * purity(rho))       # якорь = свой ρ
    assert np.allclose(own(np.eye(7)), np.eye(7))                                    # унитален
    rhs = lambda G: _frozen_self_registering(G, H, kap=10.0, anchor="I7")(G)
    worst, far = -1.0, 0.0
    for s in range(6):
        G = random_pure(np.random.default_rng(50 + s)).astype(complex)
        h, Ps = 0.02, [1.0]
        for _ in range(1500):
            G = _rk4(G, rhs, h, 1)
            Ps.append(purity(G))
        worst = max(worst, float(np.max(np.diff(Ps))))
        far = max(far, np.linalg.norm(G - np.eye(7) / 7))
    assert worst < 0 and far < 1e-3


def test_self_registration_sustains_seven_living_attractors():
    """Саморегистрирующая самомодель φ_s держит изолированный голоном живым: семь аттракторов.

    Свидетель теоремы о самоподдерживающемся аттракторе (эволюция, T-96): φ_s(Γ) = k P_α(Γ) + R Γ²/TrΓ²,
    κ = 1, α = 1/2. При H = 0 базисное состояние e_m неподвижно, спектр якобиана — ровно
    {−κ/7, −(2/3 + κ(1 − 6c/7)), −(2/3 + 6κ(1 − c)/7)}, c = (1 − α)/3. При малом H (‖H‖ = 0,21)
    от каждого e_m поток приходит в свой аттрактор с P > 2/7, невязкой < 1e-12 и Re λ < 0;
    баланс чистоты T-98 с κ g_V на месте κ выполняется до 1e-12. Единственности нет: семь разных.
    """
    c = 0.5 / 3
    zero = np.zeros((7, 7))
    f0 = lambda G: _frozen_self_registering(G, zero)(G)
    e = [np.diag(np.eye(7)[m]).astype(complex) for m in range(7)]
    assert max(np.linalg.norm(f0(x)) for x in e) < 1e-15
    spec = np.unique(np.round(np.linalg.eigvals(_jacobian(f0, e[0])).real, 6))
    assert np.allclose(spec, sorted([-1 / 7, -(2 / 3 + 1 - 6 * c / 7), -(2 / 3 + 6 * (1 - c) / 7)]), atol=1e-6)
    rng = np.random.default_rng(1)
    A = rng.normal(size=(7, 7)) + 1j * rng.normal(size=(7, 7))
    H = 0.05 * (A + A.conj().T) / 2
    f = lambda G: _frozen_self_registering(G, H)(G)
    ends = []
    for x in e:
        G = _rk4(x, f, 150.0, 3000)
        P = purity(G)
        R = 1 / (7 * P)
        fstar = np.real(np.trace(G @ ((1 - R) * (np.diag(np.diag(G)) + (G - np.diag(np.diag(G))) / 6) + R * G @ G / P)))
        pd = float(np.sum(np.real(np.diag(G)) ** 2))
        kg = gate(P)
        assert np.linalg.norm(f(G)) < 1e-12 and P > 2 / 7
        assert abs((2 / 3 * pd + kg * fstar) / (2 / 3 + kg) - P) < 1e-12              # T-98, κ → κ g_V
        assert np.max(np.linalg.eigvals(_jacobian(f, G)).real) < -0.1
        ends.append(G)
    assert min(np.linalg.norm(a - b) for a, b in itertools.combinations(ends, 2)) > 0.5


def test_a_distant_holon_marginal_ignores_every_local_operation():
    """При каноническом продолжении маргиналь голонома B не зависит ни от каких действий у A.

    Свидетель теоремы о вынужденном прочтении (соответствие с физикой §8.8): B — голоном с φ_s,
    A — кубит, состояние запутано, P(ρ_B) = 1/2 (затвор открыт). A ничего не делает, измеряет
    в базисе Z, измеряет в базисе X или вращает кубит: маргиналь B при t = 6 одна и та же до 1e-12.
    Покомпонентная (селективная) эволюция условных состояний B дала бы другое (> 1e-2).
    """
    rng = np.random.default_rng(8)
    A = rng.normal(size=(7, 7)) + 1j * rng.normal(size=(7, 7))
    H = 0.05 * (A + A.conj().T) / 2
    b = np.linalg.qr(rng.normal(size=(7, 2)) + 1j * rng.normal(size=(7, 2)))[0]
    psi = (np.kron(b[:, 0], [1, 0]) + np.kron(b[:, 1], [0, 1])) / np.sqrt(2)
    X0 = np.outer(psi, psi.conj())
    hA = np.array([[0.3, 0.2], [0.2, -0.1]])

    def rhs(X):
        X4 = X.reshape(7, 2, 7, 2)
        M = _frozen_self_registering(np.einsum("iaja->ij", X4), H, kap=3.0)
        out = np.zeros_like(X4)
        for a in range(2):
            for a2 in range(2):
                out[:, a, :, a2] = M(X4[:, a, :, a2])
        out = out.reshape(14, 14)
        HA = np.kron(np.eye(7), hA)
        return out - 1j * (HA @ X - X @ HA)
    marg = lambda X: np.einsum("iaja->ij", X.reshape(7, 2, 7, 2))
    Z = [np.diag([1.0, 0]), np.diag([0, 1.0])]
    Xb = [0.5 * np.array([[1, 1], [1, 1.0]]), 0.5 * np.array([[1, -1], [-1, 1.0]])]
    U = expm(-1j * 1.1 * np.array([[0, 1], [1, 0]]))
    ops = [lambda X: X,
           lambda X: sum(np.kron(np.eye(7), p) @ X @ np.kron(np.eye(7), p) for p in Z),
           lambda X: sum(np.kron(np.eye(7), p) @ X @ np.kron(np.eye(7), p) for p in Xb),
           lambda X: np.kron(np.eye(7), U) @ X @ np.kron(np.eye(7), U).conj().T]
    X1 = X0
    outs = [marg(_rk4(op(X1), rhs, 5.0, 250)) for op in ops]
    assert max(np.linalg.norm(o - outs[0]) for o in outs[1:]) < 1e-12
    single = lambda G: _frozen_self_registering(G, H, kap=3.0)(G)
    assert np.linalg.norm(_rk4(marg(X1), single, 5.0, 250) - outs[0]) < 1e-12     # автономна
    rhoB = marg(X1)
    sel = 0
    for p in Z:
        Y = np.kron(np.eye(7), p) @ X1 @ np.kron(np.eye(7), p)
        w = np.trace(Y).real
        sel = sel + w * _rk4(marg(Y) / w, single, 5.0, 250)
    assert np.linalg.norm(sel - outs[0]) > 1e-2 and abs(purity(rhoB) - 0.5) < 1e-12


def test_abrams_lloyd_amplification_runs_on_marginals():
    """Механизм Абрамса–Ллойда работает и в неселективном прочтении: седло усиливает 2⁻ⁿ за время O(n).

    Свидетель к соответствию с физикой §8.6: голоном с φ_s, κ = 1, диагональный H. Плоское
    состояние diag(½, ½, 0, …) стационарно, у якобиана ровно одно положительное собственное
    значение μ = κR = 2/7. Маргиналь diag(½ + s/2, ½ − s/2, …) при s = 2⁻ⁿ уходит к p₁ ≥ 0,9
    за время, растущее на 10·ln2/μ = 24,26 при n → n + 10; при s = 0 состояние не сдвигается.
    """
    H = np.diag(0.3 * np.arange(7.0))
    f = lambda G: _frozen_self_registering(G, H)(G)
    F = np.diag([0.5, 0.5, 0, 0, 0, 0, 0]).astype(complex)
    assert np.linalg.norm(f(F)) < 1e-15
    ev = np.linalg.eigvals(_jacobian(f, F)).real
    assert np.sum(ev > 1e-9) == 1 and abs(ev.max() - 2 / 7) < 1e-6
    times = []
    for n in (10, 20, 30, 40):
        s = 2.0 ** -n
        G, t = np.diag([0.5 + s / 2, 0.5 - s / 2, 0, 0, 0, 0, 0]).astype(complex), 0.0
        while np.real(G[0, 0]) < 0.9:
            G, t = _rk4(G, f, 0.05, 1), t + 0.05
        times.append(t)
    steps = np.diff(times)
    assert np.all(np.abs(steps - 10 * np.log(2) * 3.5) < 0.1)
    G = _rk4(F, f, times[-1], int(round(times[-1] / 0.05)))
    assert np.linalg.norm(G - F) < 1e-12


def test_non_degeneracy_is_generic_and_aggregation_follows_from_weak_coupling():
    """(ND) выполняется у случайных якорей, а (AGG b) следует из слабой связи с δ = O(g).

    Свидетель к теоремам 9.2–9.3 (КК-6, КК-7): у 12 воплощённых голономов со случайными H и якорями
    аттрактор невырожден (min |Re λ| > 0,05) и P далеко от изломов затвора 2/7 и 3/7. Для пары
    одинаковых голономов с общей связью X ⊗ Y стационарное X(g) отстоит от σ ⊗ σ на величину,
    линейную по g: ‖X(g) − σ⊗σ‖₁ / g при g = 0,01 и 0,02 совпадают до 3 %.
    """
    rng = np.random.default_rng(12)

    def herm(r):
        A = r.normal(size=(7, 7)) + 1j * r.normal(size=(7, 7))
        return (A + A.conj().T) / 2
    single = []
    for _ in range(12):
        v = rng.normal(size=7) + 1j * rng.normal(size=7)
        v /= np.linalg.norm(v)
        lam = rng.uniform(0.6, 0.9)
        a = _holon_pair_generator(0.3 * herm(rng), lam * np.outer(v, v.conj()) + (1 - lam) * np.eye(7) / 7)
        f = lambda G, a=a: np.einsum("iaja->ij", a(np.kron(G, np.eye(7) / 7).reshape(7, 7, 7, 7), G))
        rho = _rk4(np.eye(7) / 7, f, 40.0, 800)
        P = purity(rho)
        assert np.linalg.norm(f(rho)) < 1e-10 and min(abs(P - 2 / 7), abs(P - 3 / 7)) > 1e-3
        assert np.min(np.abs(np.linalg.eigvals(_jacobian(f, rho)).real)) > 0.05
        single.append((a, f, rho))
    a, f, rho = single[0]
    sigma = np.kron(rho, rho)
    Hg = np.kron(herm(np.random.default_rng(4)), herm(np.random.default_rng(5)))
    Hg /= np.linalg.norm(Hg, 2)
    marg = lambda X: (np.einsum("ijkj->ik", X.reshape(7, 7, 7, 7)), np.einsum("ijil->jl", X.reshape(7, 7, 7, 7)))

    def rhs(X, g):
        g1, g2 = marg(X)
        X4 = X.reshape(7, 7, 7, 7)
        out = a(X4, g1) + a(X4.transpose(1, 0, 3, 2), g2).transpose(1, 0, 3, 2)
        return out.reshape(49, 49) - 1j * g * (Hg @ X - X @ Hg)
    ratio = []
    for g in (0.01, 0.02):
        X = _rk4(sigma.astype(complex), lambda X: rhs(X, g), 24.0, 480)
        assert np.linalg.norm(rhs(X, g)) < 1e-8
        ratio.append(np.abs(np.linalg.eigvalsh((X - sigma + (X - sigma).conj().T) / 2)).sum() / g)
    assert abs(ratio[1] / ratio[0] - 1) < 1e-3


def test_phi_tower_converges_only_under_backbone_dominance():
    """T-191 в верной форме: башня самомоделей сходится лишь при доминировании хребта.

    (а) Изолированный голоном, фиксированная цель |0⟩⟨0|, κ = 3: из I/7 затвор закрыт и
    поток стоит (P = 1/7), из |0⟩ приходит в живое состояние (P ≈ 0,98) — предел зависит
    от старта, итерация φ⁽ⁿ⁺¹⁾ = lim exp(τℒ⁽ⁿ⁾) не определена (шаг 1 прежнего доказательства).
    (б) Воплощённый голоном с хребтом μ(σ − Γ), P(σ) > 3/7, κ = 0,1, μ = 3,5: следовая
    константа Липшица регенерации L_R ≤ κ(1 + 2·14) = 29κ, так что μ > L_R + κ_max и
    q = κ/(μ − L_R) = 1/6; от трёх якорей (I/7, |0⟩, случайный чистый) башня сходится к одной
    неподвижной точке (разброс < 1e-10, невязка < 1e-10), и каждое сжатие ≤ q.
    """
    rng = np.random.default_rng(7)
    H = 0.2 * (lambda A: (A + A.conj().T) / 2)(rng.normal(size=(7, 7)) + 1j * rng.normal(size=(7, 7)))

    def gen(a, kap, mu, sig):
        def f(G):
            D = np.diag(np.diag(G))
            out = -1j * (H @ G - G @ H) + (2 / 3) * (D - G) + kap * gate(purity(G)) * (a - G)
            return out + mu * (sig - G) if mu else out
        return f

    tn = lambda X: float(np.abs(np.linalg.eigvalsh((X + X.conj().T) / 2)).sum())
    a0 = np.diag(np.eye(7)[0]).astype(complex)
    f = gen(a0, 3.0, 0.0, None)
    dead = _rk4(np.eye(7) / 7, f, 40.0, 2000)
    live = _rk4(a0, f, 40.0, 2000)
    assert abs(purity(dead) - 1 / 7) < 1e-12 and purity(live) > 3 / 7 and tn(dead - live) > 1
    kap, mu = 0.1, 3.5
    q = kap / (mu - 29 * kap)
    sig = np.diag([0.66, 0.1, 0.06, 0.06, 0.04, 0.04, 0.04]).astype(complex)
    assert purity(sig) > 3 / 7
    seqs = []
    for a in (np.eye(7) / 7, a0, random_pure(rng)):
        a = a.astype(complex)
        seq = [a]
        for _ in range(8):
            a = _rk4(a, gen(a, kap, mu, sig), 12.0, 600)
            seq.append(a)
        seqs.append(seq)
    for i, j in itertools.combinations(range(3), 2):
        for n in range(4):
            d0, d1 = tn(seqs[i][n] - seqs[j][n]), tn(seqs[i][n + 1] - seqs[j][n + 1])
            assert d1 <= q * d0 + 1e-12
    star = seqs[0][-1]
    assert max(tn(star - s[-1]) for s in seqs) < 1e-10
    assert np.linalg.norm(gen(star, kap, mu, sig)(star)) < 1e-10 and gate(purity(star)) == 1.0


def test_no_higgs_doublet_in_the_clifford_frame():
    """Под (Кл) хиггсовского дублета нет ни в состоянии голонома, ни в векторе Spin(9).

    𝔰𝔲(2)_L = [𝔲(2), 𝔲(2)] — производная централизатора цвета в 𝔰𝔭𝔦𝔫(9) (размерность 3).
    На 𝒮 = ℂ⊗𝕆 ≅ ℝ¹⁶ случайный её элемент имеет собственные значения ±ic и только их —
    одни дублеты, синглетов SU(2)_L в 𝒮 нет. Поэтому ad на End(𝒮) = 𝒮⊗𝒮* даёт лишь 0 и ±2ic
    (2⊗2 = 1⊕3): у всякого оператора на 𝒮, в том числе у когерентности γ_EU, спин целый.
    Вектор ℝ⁹ системы (iL_{e_k}, J, iJ): 𝔰𝔲(2)_L даёт 0 (семь раз) и ±2ic — триплет на
    span{iL_{e_O}, J, iJ}; гиперзаряд — ±1/3 на шести цветных, 0 на трёх синглетах.
    """
    d = _sm_on_complex_octonions()
    comm = [A @ B - B @ A for i, A in enumerate(d["C"]) for B in d["C"][i + 1:]]
    U, s, _ = np.linalg.svd(np.array([X.flatten() for X in comm]).T, full_matrices=False)
    r = int(np.sum(s > 1e-9))
    assert r == 3
    X = sum(w * U[:, i].reshape(16, 16) for i, w in enumerate(np.random.default_rng(0).normal(size=3)))
    ev = np.linalg.eigvals(X)
    c = np.max(np.abs(ev.imag))
    assert np.max(np.abs(ev.real)) < 1e-12 and np.allclose(np.abs(ev.imag), c)
    ad = np.abs((ev[:, None] - ev[None, :]).imag) / c
    assert np.all((ad < 1e-8) | (np.abs(ad - 2) < 1e-8))
    G = np.array([g.flatten() for g in d["gam"]]).T

    def on_vector(Z):
        M = np.zeros((9, 9))
        for a, g in enumerate(d["gam"]):
            v = (Z @ g - g @ Z).flatten()
            coef = np.linalg.lstsq(G, v, rcond=None)[0]
            assert np.linalg.norm(G @ coef - v) < 1e-9
            M[:, a] = coef
        return np.sort(np.abs(np.linalg.eigvals(M).imag))
    assert np.allclose(on_vector(X) / c, [0] * 7 + [2, 2], atol=1e-8)
    assert np.allclose(on_vector(d["Y"]), [0] * 3 + [1 / 3] * 6, atol=1e-8)


# ---------------------------------------------------------------------------
# Полное поколение (25.09.2026, T-326 … T-329, вторая волна): комплексификация спинора.
# 𝒮_ℂ = 𝒮 ⊗_ℝ ℂ′ записано как ℝ³² = 𝒮 ⊗ ℝ², i′ = 1 ⊗ [[0,1],[−1,0]], K′ = 1 ⊗ σ₃.
# ---------------------------------------------------------------------------

@functools.lru_cache(maxsize=None)
def _spin10_completion():
    """Десятая образующая, 𝔰𝔭𝔦𝔫(10), половины V_L ⊕ V_R, 𝔰𝔲(2)_L ⊕ 𝔰𝔲(2)_R, (B−L)/2 и гиперзаряд."""
    d = _sm_on_complex_octonions()
    s1, s3 = np.array([[0.0, 1.0], [1.0, 0.0]]), np.diag([1.0, -1.0])
    ip = np.kron(np.eye(16), s3 @ s1)                                  # i′: новая мнимая единица
    g10 = [np.kron(g, s3) for g in d["gam"]] + [np.kron(np.eye(16), s1)]
    spin10 = [g10[a] @ g10[b] / 2 for a in range(10) for b in range(a + 1, 10)]
    lift = lambda X: np.kron(X, np.eye(2))
    su3 = [lift(X) for X in d["su3"]]
    om = functools.reduce(np.matmul, g10)                              # объём Cl(10)
    om4 = g10[6] @ g10[7] @ g10[8] @ g10[9]                            # объём бесцветной 4-плоскости
    PL, PR = (np.eye(32) - om4) / 2, (np.eye(32) + om4) / 2           # ω = +L_{e_O} на V_L, −L_{e_O} на V_R
    cen = [sum(v[i] * spin10[i] for i in range(45)) for v in _null_commutant(su3, spin10)]
    comm = [a @ b - b @ a for a in cen for b in cen]
    U, s, _ = np.linalg.svd(np.array([x.flatten() for x in comm]).T, full_matrices=False)
    der = [U[:, i].reshape(32, 32) for i in range(int(np.sum(s > 1e-9)))]

    def acting_only_on(P):
        rows = np.array([(x @ (np.eye(32) - P)).flatten() for x in der]).T
        _, s_, Vt = np.linalg.svd(rows)
        return [sum(v[i] * der[i] for i in range(len(der))) for v in Vt[np.sum(s_ > 1e-9):]]
    BL = lift(d["Y"])                                                  # гиперзаряд T-326 = (B−L)/2
    I1 = lift(d["imul"])
    T3L, T3R = (I1 / 2) @ PL, (I1 / 2) @ PR                            # i/2 = T₃L + T₃R
    Y = BL + T3R
    return dict(d=d, ip=ip, g10=g10, spin10=spin10, su3=su3, om=om, om4=om4, PL=PL, PR=PR,
                cen=cen, suL=acting_only_on(PL), suR=acting_only_on(PR), BL=BL, I1=I1,
                T3L=T3L, T3R=T3R, Y=Y, lift=lift, sm=su3 + acting_only_on(PL) + [Y])


def _charges(e, X, P=None):
    """Заряды X относительно комплексной структуры ω: собственные числа −ωX (комплексные кратности)."""
    q = -e["om"] @ X
    q = (q + q.T) / 2
    if P is not None:
        q = P @ q @ P
    vals, mult = np.unique(np.round(np.linalg.eigvalsh(q), 9), return_counts=True)
    return {float(v) + 0.0: int(m) for v, m in zip(vals, mult)}


def test_the_tenth_generator_is_forced_by_complexifying_the_spinor():
    """T-329(а): поле Вейля со значениями в вещественном 𝒮 живёт в 𝒮_ℂ = 𝒮⊗_ℝℂ′ ≅ ℝ³²; там Клиффорд вынужденно продолжается до десяти.

    Девять образующих 𝒮, сделанные ℂ′-антилинейными, γ_a⊗K′, сохраняют соотношения; с ними
    антикоммутирует ровно двумерное пространство span{i′K′, i′}. Из него квадрат +1 и
    симметричность имеет лишь ±i′K′ — десятая образующая (знак = ориентация, чётность мира).
    Объём десяти ω = γ₁⋯γ₁₀ равен i′ (с точностью до знака): комплексная структура 𝟏𝟔 Spin(10) —
    та самая мнимая единица, что понадобилась полю. На ℝ³² одиннадцатой нет (Cl(11,0) ≅ M₃₂(ℂ),
    неприводимый модуль ℝ⁶⁴). Подалгебра 𝔰𝔭𝔦𝔫(9) действует как ℂ′-линейное продолжение T-326.
    """
    e = _spin10_completion()
    g10, ip = e["g10"], e["ip"]
    for a in range(10):
        for b in range(10):
            assert np.allclose(g10[a] @ g10[b] + g10[b] @ g10[a], 2 * (a == b) * np.eye(32))
    basis = [np.outer(np.eye(32)[i], np.eye(32)[j]) for i in range(32) for j in range(32)]
    rows = np.vstack([np.array([(S @ X + X @ S).flatten() for S in basis]).T for X in g10[:9]])
    _, s, Vt = np.linalg.svd(rows)
    anti = [v.reshape(32, 32) for v in Vt[np.sum(s > 1e-9):]]
    assert len(anti) == 2
    assert _span_residual(g10[9], anti) < 1e-9 and _span_residual(ip, anti) < 1e-9
    for t in np.linspace(0, np.pi, 7)[1:-1]:                          # a·i′K′ + b·i′: квадрат a² − b²
        T = np.cos(t) * g10[9] + np.sin(t) * ip
        assert not (np.allclose(T @ T, np.eye(32)) and np.allclose(T, T.T))
    assert np.allclose(e["om"], ip) or np.allclose(e["om"], -ip)
    assert max(np.abs(e["om"] @ x - x @ e["om"]).max() for x in e["spin10"]) < 1e-12
    assert np.linalg.matrix_rank(np.array([x.flatten() for x in e["spin10"]]), tol=1e-9) == 45
    assert max(_span_residual(e["lift"](x), e["spin10"]) for x in e["d"]["spin9"]) < 1e-9


def test_left_right_split_is_canonical_and_the_t326_su2_is_diagonal():
    """T-329(б): ℝ³² = V_L ⊕ V_R — собственные пространства объёма бесцветной 4-плоскости {iL_{e_O}, J, iJ, γ₁₀}.

    ω = +L_{e_O} на V_L и −L_{e_O} на V_R (однородно на кварках и лептонах): (V_L, ω) = (𝒮, L_{e_O}) —
    левые дублеты T-326/T-327, (V_R, ω) — сопряжённая копия. Централизатор цвета в 𝔰𝔭𝔦𝔫(10)
    (размерность 7) = 𝔰𝔲(2)_L ⊕ 𝔰𝔲(2)_R ⊕ 𝔲(1): каждая 𝔰𝔲(2) действует только на своей половине,
    центр — гиперзаряд T-326, т. е. (B−L)/2. 𝔰𝔲(2) из 𝔰𝔭𝔦𝔫(9) T-326 — диагональ: у каждого её
    элемента L- и R-части равной нормы. Стабилизатор любого бесцветного вектора (любая Spin(9) ⊃ цвет)
    пересекает 𝔰𝔲(2)_L по нулю: 𝔰𝔲(2)_L не лежит ни в одной такой Spin(9).
    """
    e = _spin10_completion()
    om, PL, PR, L1 = e["om"], e["PL"], e["PR"], e["lift"](e["d"]["Lu"])
    assert np.allclose(e["om4"], e["om4"].T) and np.allclose(e["om4"] @ e["om4"], np.eye(32))
    assert np.trace(PL) == 16 and np.trace(PR) == 16
    assert np.allclose(PL @ om @ PL, PL @ L1 @ PL) and np.allclose(PR @ om @ PR, -PR @ L1 @ PR)
    assert len(e["cen"]) == 7 and len(e["suL"]) == 3 and len(e["suR"]) == 3
    assert all(np.allclose(x @ PR, 0) and np.allclose(PR @ x, 0) for x in e["suL"])
    assert all(np.allclose(x @ PL, 0) and np.allclose(PL @ x, 0) for x in e["suR"])
    zc = _null_commutant(e["cen"], e["cen"])
    assert zc.shape[0] == 1
    Z = [sum(v[i] * e["cen"][i] for i in range(7)) for v in zc]
    assert _span_residual(e["BL"], Z) < 1e-9                                      # центр = гиперзаряд T-326
    d = e["d"]
    comm = [a @ b - b @ a for a in d["C"] for b in d["C"]]
    U, s, _ = np.linalg.svd(np.array([x.flatten() for x in comm]).T, full_matrices=False)
    F = np.array([m.flatten() for m in e["suL"] + e["suR"]]).T
    for i in range(3):
        X = e["lift"](U[:, i].reshape(16, 16))
        c = np.linalg.lstsq(F, X.flatten(), rcond=None)[0]
        assert np.linalg.norm(F @ c - X.flatten()) < 1e-9
        nL = np.linalg.norm(sum(c[k] * e["suL"][k] for k in range(3)))
        nR = np.linalg.norm(sum(c[3 + k] * e["suR"][k] for k in range(3)))
        assert nL > 0.1 and abs(nL - nR) < 1e-9                                   # диагональ L ⊕ R
    rng = np.random.default_rng(7)
    plane = e["g10"][6:10]
    for _ in range(5):
        v = rng.normal(size=4)
        v /= np.linalg.norm(v)
        V = sum(v[i] * plane[i] for i in range(4))
        stab = _null_commutant([V], e["cen"])
        S = [sum(w[i] * e["cen"][i] for i in range(7)) for w in stab]
        FS = np.array([x.flatten() for x in S] + [x.flatten() for x in e["suL"]]).T
        assert np.linalg.matrix_rank(FS, tol=1e-9) == len(S) + 3                  # 𝔰𝔱𝔞𝔟 ∩ 𝔰𝔲(2)_L = 0


def test_the_clock_stabiliser_gives_pati_salam_then_left_right_then_colour():
    """(Кл), второе предложение, — теорема: стабилизатор структурных отображений часов L_{e_O}, R_{e_O}.

    В 𝔤₂: 𝔠(L_{e_O}) = 𝔠(R_{e_O}) = 𝔰𝔲(3)_C (размерность 8) — цвет УГМ. В 𝔰𝔭𝔦𝔫(9) на 𝒮:
    𝔠(L_{e_O}) = 𝔰𝔭𝔦𝔫(6)⊕𝔰𝔭𝔦𝔫(3) = 𝔰𝔲(4)⊕𝔰𝔲(2) (18, Пати–Салам на левой половине),
    𝔠(R_{e_O}) = 𝔠(L_{e_O}, R_{e_O}) = нормализатор цвета (12). В 𝔰𝔭𝔦𝔫(10) на 𝒮_ℂ:
    𝔠(L_{e_O}) = 𝔰𝔲(4)⊕𝔰𝔲(2)_L⊕𝔰𝔲(2)_R (21), 𝔠(R_{e_O}) = 𝔠(L,R) = 𝔰𝔲(3)⊕𝔰𝔲(2)_L⊕𝔰𝔲(2)_R⊕𝔲(1)_{B−L} (15).
    """
    e = _spin10_completion()
    d = e["d"]
    G2c = []
    for X in G2:
        M = np.zeros((8, 8))
        M[1:, 1:] = X
        G2c.append(d["cl"](M))
    dims = lambda ops, space: _null_commutant(ops, space).shape[0]
    assert dims([d["Lu"]], G2c) == 8 and dims([d["Ru"]], G2c) == 8
    assert dims([d["Lu"]], d["spin9"]) == 18 and dims([d["Ru"]], d["spin9"]) == 12
    assert dims([d["Lu"], d["Ru"]], d["spin9"]) == 12
    L1, R1 = e["lift"](d["Lu"]), e["lift"](d["Ru"])
    assert dims([L1], e["spin10"]) == 21 and dims([R1], e["spin10"]) == 15 and dims([L1, R1], e["spin10"]) == 15
    CR = [sum(v[i] * e["spin10"][i] for i in range(45)) for v in _null_commutant([R1], e["spin10"])]
    assert max(_span_residual(x, CR) for x in e["su3"] + e["cen"]) < 1e-9          # 𝔠(R) = цвет ⊕ 7
    CL = [sum(v[i] * e["spin10"][i] for i in range(45)) for v in _null_commutant([L1], e["spin10"])]
    assert np.linalg.matrix_rank(np.array([(a @ b - b @ a).flatten() for a in CL for b in CL]), tol=1e-9) == 21


def test_one_generation_with_a_right_handed_neutrino():
    """T-329(в): Y = (B−L)/2 + T₃R, T₃R = (i/2)|_{V_R}; (𝒮_ℂ, ω) — одно поколение СМ с ν_R.

    На V_L: (3,2)_{1/6} ⊕ (1,2)_{−1/2}; на V_R: u^c (3̄)_{−2/3}, d^c (3̄)_{1/3}, e^c 1_{1}, ν^c 1_{0}.
    Q = T₃L + Y = i/2 + (B−L)/2: {±2/3, ±1/3} по три, ±1 по одному, 0 дважды. Стабилизатор
    вектора ν^c в 𝔰𝔲(3)⊕𝔰𝔲(2)_L⊕𝔰𝔲(2)_R⊕𝔲(1)_{B−L} — ровно 𝔤_SM (размерность 12), в 𝔰𝔭𝔦𝔫(10) — 𝔰𝔲(5) (24).
    Ядро SU(3)×SU(2)_L×U(1)_Y на ℝ³² — снова ровно ℤ₆. Знак T₃R не важен (отражение Вейля SU(2)_R).
    """
    e = _spin10_completion()
    PL, PR, Y = e["PL"], e["PR"], e["Y"]
    assert _span_residual(e["T3R"], e["suR"]) < 1e-9 and _span_residual(e["T3L"], e["suL"]) < 1e-9
    cL = _charges(e, Y, PL)
    cR = _charges(e, Y, PR)
    assert cL == {-0.5: 4, 0.0: 16, round(1 / 6, 9): 12}                         # вещественные размерности
    assert cR == {round(-2 / 3, 9): 6, 0.0: 18, round(1 / 3, 9): 6, 1.0: 2}
    for sgn in (1, -1):
        assert _charges(e, e["BL"] + sgn * e["T3R"], PR) == cR
    q = _charges(e, e["T3L"] + Y)
    assert {k: v // 2 for k, v in q.items()} == {-1.0: 1, round(-2 / 3, 9): 3, round(-1 / 3, 9): 3, 0.0: 2,
                                                  round(1 / 3, 9): 3, round(2 / 3, 9): 3, 1.0: 1}
    assert np.allclose(e["T3L"] + Y, e["I1"] / 2 + e["BL"])                      # Q = i/2 + (B−L)/2
    lr = e["su3"] + e["cen"]
    qY = -e["om"] @ Y
    qB = -e["om"] @ e["BL"]
    M = PR @ ((qY + qY.T) @ (qY + qY.T) / 4 + ((qB + qB.T) / 2 - PR / 2) @ ((qB + qB.T) / 2 - PR / 2)) @ PR
    w, V = np.linalg.eigh(M + 10 * PL)
    nu = V[:, np.abs(w) < 1e-9]
    assert nu.shape[1] == 2                                                        # ν^c: одна комплексная прямая
    v = nu[:, 0]
    rows = np.array([x @ v for x in lr]).T
    _, s, Vt = np.linalg.svd(rows)
    S = [sum(c[i] * lr[i] for i in range(len(lr))) for c in Vt[np.sum(s > 1e-9):]]
    assert len(S) == 12 and max(_span_residual(x, S) for x in e["sm"]) < 1e-9
    rows10 = np.array([x @ v for x in e["spin10"]]).T
    assert 45 - np.linalg.matrix_rank(rows10, tol=1e-9) == 24                    # 𝔰𝔲(5)
    P = np.eye(8)
    P[0, 0] = P[7, 7] = 0
    w3 = expm((2 * np.pi / 3) * e["lift"](e["d"]["Lu"] @ e["d"]["cl"](P)))
    assert max(np.abs(w3 @ x - x @ w3).max() for x in e["su3"]) < 1e-9
    assert np.allclose(expm(2 * np.pi * 6 * Y), np.eye(32)) and not np.allclose(expm(np.pi * 6 * Y), np.eye(32))
    minus = expm(2 * np.pi * e["T3L"])                                             # центр SU(2)_L
    assert np.allclose(minus @ PL, -PL) and np.allclose(minus @ PR, PR)
    kernel = []
    for n in range(12):
        u1 = expm((np.pi * n / 6) * 6 * Y)
        for a, wa in enumerate((np.eye(32), w3, w3 @ w3)):
            for sgn, z2 in ((1, np.eye(32)), (-1, minus)):
                if np.allclose(z2 @ wa @ u1, np.eye(32)):
                    kernel.append((a, sgn, n))
    assert len(kernel) == 6 and sorted({a for a, _, _ in kernel}) == [0, 1, 2]


def test_the_full_generation_is_anomaly_free():
    """T-329(г): все калибровочные и гравитационная аномалии поколения 𝒮_ℂ сокращаются — и не случайно.

    Для любого X ∈ 𝔰𝔭𝔦𝔫(10) след куба зарядов по 𝟏𝟔 равен нулю (у 𝔰𝔬(10) нет кубического
    инварианта), и 𝔲(1)_Y ⊂ 𝔰𝔭𝔦𝔫(10) — гиперзаряд не подобран. Явно: SU(3)²Y, SU(2)²Y, Y³, grav·Y,
    SU(3)³ (левых триплетов столько же, сколько антитриплетов) и глобальная аномалия Виттена
    (4 дублета SU(2)_L — чётно). С ν^c сокращаются и (B−L)³, grav·(B−L).
    """
    e = _spin10_completion()
    om = e["om"]
    rng = np.random.default_rng(11)
    for _ in range(6):
        X = sum(c * x for c, x in zip(rng.normal(size=45), e["spin10"]))
        q = -om @ X
        q = (q + q.T) / 2
        assert abs(np.trace(q @ q @ q)) < 1e-9 and abs(np.trace(q)) < 1e-9
    fields = [(6, 1 / 6, 1 / 3), (3, -2 / 3, -1 / 3), (3, 1 / 3, -1 / 3), (2, -1 / 2, -1), (1, 1, 1), (1, 0, 1)]
    Ys = [k for k, m in _charges(e, e["Y"]).items() for _ in range(m // 2)]
    listed = sorted([round(y, 9) for n, y, _ in fields for _ in range(n)])
    assert sorted(round(y, 9) for y in Ys) == listed
    su3_2_y = 2 * (1 / 6) + (-2 / 3) + (1 / 3)
    su2_2_y = 3 * (1 / 6) + (-1 / 2)
    y3 = sum(n * y ** 3 for n, y, _ in fields)
    grav = sum(n * y for n, y, _ in fields)
    bl3 = sum(n * b ** 3 for n, _, b in fields)
    bl1 = sum(n * b for n, _, b in fields)
    assert max(abs(x) for x in (su3_2_y, su2_2_y, y3, grav, bl3, bl1)) < 1e-12
    assert 2 - 1 - 1 == 0 and (3 + 1) % 2 == 0
    bl3_no_nu = bl3 - 1
    assert abs(bl3_no_nu + 1) < 1e-12                                              # без ν^c (B−L)³ = −1


def test_the_colour_singlet_clifford_plane_is_one_higgs_doublet():
    """T-329(д): бесцветная 4-плоскость вектора ℝ¹⁰, {iL_{e_O}, J, iJ, γ₁₀}, — (1,2,2)₀ = один комплексный дублет Y = ±1/2.

    𝔰𝔲(2)_L действует на ней без неподвижных векторов (собственные числа ±ic/2 · 2), Y — поворот
    с |заряд| = 1/2; клиффордово умножение на её векторы переставляет V_L ↔ V_R (дираковская масса).
    Стабилизатор γ₁₀ (и любого вектора плоскости {iL_{e_O}, γ₁₀}) в 𝔤_SM — 𝔰𝔲(3) ⊕ 𝔲(1)_Q
    с Q = i/2 + (B−L)/2. Цветные направления (3⊕3̄)_{±1/3} сохраняют половины.
    """
    e = _spin10_completion()
    G = np.array([g.flatten() for g in e["g10"]]).T

    def on_vector(Z):
        M = np.zeros((10, 10))
        for a, g in enumerate(e["g10"]):
            v = (Z @ g - g @ Z).flatten()
            c = np.linalg.lstsq(G, v, rcond=None)[0]
            assert np.linalg.norm(G @ c - v) < 1e-9
            M[:, a] = c
        return M
    MY = on_vector(e["Y"])
    assert np.allclose(np.sort(np.abs(np.linalg.eigvals(MY[6:, 6:]).imag)), [0.5] * 4)
    assert np.allclose(MY[6:, :6], 0) and np.allclose(MY[:6, 6:], 0)
    assert np.allclose(np.sort(np.abs(np.linalg.eigvals(MY[:6, :6]).imag)), [1 / 3] * 6)
    rng = np.random.default_rng(3)
    X = sum(c * x for c, x in zip(rng.normal(size=3), e["suL"]))
    ev = np.linalg.eigvals(on_vector(X)[6:, 6:])
    assert np.max(np.abs(ev.real)) < 1e-9 and np.min(np.abs(ev.imag)) > 1e-3           # нет инвариантов: дублет
    for a in range(6, 10):
        g = e["g10"][a]
        assert np.allclose(e["PL"] @ g @ e["PL"], 0) and np.allclose(e["PR"] @ g @ e["PR"], 0)
    for a in range(6):
        g = e["g10"][a]
        assert np.allclose(e["PL"] @ g @ e["PR"], 0)
    Q = e["I1"] / 2 + e["BL"]
    for vec in (9, 6):
        rows = np.array([on_vector(x)[:, vec] for x in e["sm"]]).T
        _, s, Vt = np.linalg.svd(rows)
        S = [sum(c[i] * e["sm"][i] for i in range(len(e["sm"]))) for c in Vt[np.sum(s > 1e-9):]]
        assert len(S) == 9 and _span_residual(Q, S) < 1e-9


def test_exact_clock_z3_on_generations_forces_trivial_mixing():
    """(ПЧ) в точной форме опровергнута: горизонтальная ℤ₃, переставляющая поколения, даёт |V_CKM| — перестановку.

    Пусть ℤ₃ действует на индексе поколения циклической перестановкой P с любыми характерами
    у полей и хиггса. Инвариантная юкавская матрица в базисе Фурье F имеет носитель j − i ≡ k:
    Y Y† диагональна в одном базисе для всех секторов, и |V_CKM| — матрица перестановки
    (данные: |V_us| ≈ 0,225, PDG 2024). Майорановская матрица имеет носитель i + j ≡ k: одно
    массовое состояние совпадает с ароматом заряженного лептона — в PMNS есть столбец с |U| = 1
    (данные: max|U| ≈ 0,85, |U_e3| ≈ 0,15), а два других вырождены с углом 45°.
    """
    rng = np.random.default_rng(5)
    w = np.exp(2j * np.pi / 3)
    P = np.roll(np.eye(3), 1, axis=0)

    def invariant(chi, transpose=False):
        Z = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
        if transpose:
            Z = Z + Z.T
        acc = np.zeros((3, 3), complex)
        for t in range(3):
            Pt = np.linalg.matrix_power(P, t)
            acc += (w ** (-chi * t)) * ((Pt.T if transpose else Pt.conj().T) @ Z @ Pt)
        return acc / 3
    for chi_u, chi_d in itertools.product(range(3), repeat=2):
        Yu, Yd = invariant(chi_u), invariant(chi_d)
        for t in range(3):
            Pt = np.linalg.matrix_power(P, t)
            assert np.allclose(Pt.conj().T @ Yu @ Pt, w ** (chi_u * t) * Yu)
        _, Uu = np.linalg.eigh(Yu @ Yu.conj().T)
        _, Ud = np.linalg.eigh(Yd @ Yd.conj().T)
        V = np.abs(Uu.conj().T @ Ud)
        assert np.allclose(np.sort(V.flatten()), [0] * 6 + [1] * 3, atol=1e-8)
    for chi in range(3):
        Ye = invariant(0)
        M = invariant(chi, transpose=True)
        for t in range(3):
            Pt = np.linalg.matrix_power(P, t)
            assert np.allclose(Pt.T @ M @ Pt, w ** (chi * t) * M)
        _, Ue = np.linalg.eigh(Ye @ Ye.conj().T)
        Mf = Ue.T @ M @ Ue                                                       # майорановская в базисе масс e, μ, τ
        H = Mf.conj().T @ Mf
        m2, Un = np.linalg.eigh(H)
        U = np.abs(Un)
        assert np.isclose(U.max(), 1.0, atol=1e-8)                               # столбец PMNS с |U| = 1
        assert np.isclose(m2[0], m2[1]) or np.isclose(m2[1], m2[2]) or np.isclose(m2[0], m2[2])
    s = np.sin(np.pi * np.arange(1, 4) / 7)                                      # закон m ∝ sinⁿ(πm/7) не проходит
    me, mmu, mtau = 0.51099895, 105.6583755, 1776.86
    n1 = np.log(mmu / me) / np.log(s[1] / s[0])
    n2 = np.log(mtau / mmu) / np.log(s[2] / s[1])
    assert abs(n1 - 9.05) < 0.01 and abs(n2 - 12.8) < 0.05


def test_fermions_are_vectors_of_s_not_operators_and_eta0_is_forced():
    """(Кл₀) не выводится из аксиом о Γ: −1 ∈ SU(2)_L действует на 𝒮 как −1, на End(𝒮) — как +1.

    Всё, что строится из матриц когерентности (операторы, их тензорные произведения), имеет целый
    слабый изоспин; дублеты — векторы 𝒮, а не операторы. Замыкание Im 𝕆 под семью левыми
    умножениями — всё 𝕆 (e_k e_k = −1): параллельный спинор η₀ достраивается вынужденно,
    и ни ℂ⁷ (ℝ¹⁴), ни ℂ⁷ ⊗ ℂ⁷ часов Пейджа–Вуттерса (ℝ⁹⁸) модулем Cl(7) быть не могут —
    размерности модулей кратны 16.
    """
    d = _sm_on_complex_octonions()
    comm = [a @ b - b @ a for a in d["C"] for b in d["C"]]
    U, s, _ = np.linalg.svd(np.array([x.flatten() for x in comm]).T, full_matrices=False)
    assert _span_residual(d["imul"] / 2, [U[:, i].reshape(16, 16) for i in range(3)]) < 1e-9
    minus = expm(2 * np.pi * d["imul"] / 2)
    assert np.allclose(minus, -np.eye(16))
    Z = np.random.default_rng(2).normal(size=(16, 16))
    assert np.allclose(minus @ Z @ np.linalg.inv(minus), Z)
    vecs = [unit(i) for i in range(1, 8)]
    for _ in range(2):
        vecs = vecs + [_lmul8(k) @ v for k in range(1, 8) for v in vecs]
        span = np.array(vecs).T
    assert np.linalg.matrix_rank(span, tol=1e-9) == 8
    assert 14 % 16 != 0 and 98 % 16 != 0 and 16 % 16 == 0


def test_canonical_aggregation_is_unique_and_the_octonion_product_is_dead():
    """Каноническая агрегация (теорема 9.5 (a)) и отвергнутый октонионный путь (теорема 9.6 (b)).

    (а) Линейное отображение End(ℂ^d ⊗ ℂ^d) → End(ℂ^d), инвариантное к перестановке факторов и
    согласованное на всех σ ⊗ σ, единственно — среднее маргиналей (d = 3: ранг системы 729 из 729,
    отклонение от среднего маргиналей ~1e-14); без симметрии остаётся 324 свободных параметра.
    (б) Октонионный канал ℂ⁷⊗ℂ⁷ → ℂ⁷ по структурным константам Фано: VV† = 6I, образ W†W лежит в
    антисимметричном подпространстве; ‖a × b‖² ≤ 2 для комплексных единичных a, b (максимум 2
    достигается); выход несвязанной пары: P ≤ 1/7 + (6/7)w², w ≤ 1/3 для сепарабельных входов, т. е.
    P ≤ 5/21 < 2/7, а для одинаковых жизнеспособных частей P ≤ 0,2522.
    """
    d = 3
    rng = np.random.default_rng(0)
    S = np.zeros((d * d, d * d))
    for i in range(d):
        for j in range(d):
            S[i * d + j, j * d + i] = 1
    N = d ** 6

    def rows(X):
        A = np.zeros((d * d, N), complex)
        for ab in range(d * d):
            A[ab, ab * d ** 4:(ab + 1) * d ** 4] = X.reshape(-1)
        return A
    As, ys = [], []
    for _ in range(60):
        s = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
        s = s + s.conj().T
        As.append(rows(np.kron(s, s)))
        ys.append((s * np.trace(s)).reshape(-1))
    cons = np.vstack(As)
    for _ in range(90):
        X = rng.normal(size=(d * d, d * d)) + 1j * rng.normal(size=(d * d, d * d))
        As.append(rows(X - S @ X @ S))
        ys.append(np.zeros(d * d))
    A, y = np.vstack(As), np.concatenate(ys)
    sv = np.linalg.svd(A, compute_uv=False)
    assert np.sum(sv > 1e-8 * sv[0]) == N                                            # единственность
    sol = np.linalg.lstsq(A, y, rcond=None)[0]
    X = rng.normal(size=(d * d, d * d)) + 1j * rng.normal(size=(d * d, d * d))
    X4 = X.reshape(d, d, d, d)
    mean = (np.einsum("iaja->ij", X4) + np.einsum("aiaj->ij", X4)) / 2
    out = np.array([sol[r * d ** 4:(r + 1) * d ** 4] @ X.reshape(-1) for r in range(d * d)]).reshape(d, d)
    assert np.linalg.norm(out - mean) < 1e-10                                        # = среднее маргиналей
    sv = np.linalg.svd(cons, compute_uv=False)
    assert N - np.sum(sv > 1e-8 * sv[0]) == 324                                      # без симметрии — не единственно
    V = np.array([[PHI3[i, j, k] for i in range(7) for j in range(7)] for k in range(7)])
    assert np.allclose(V @ V.T, 6 * np.eye(7))
    W = V / np.sqrt(6)
    Pi = W.T @ W
    Sw = np.zeros((49, 49))
    for i in range(7):
        for j in range(7):
            Sw[i * 7 + j, j * 7 + i] = 1
    assert np.allclose(Sw @ Pi, -Pi) and np.allclose(Pi @ Pi, Pi)                    # внутри антисимметричного
    for g in G2:
        U = expm(0.7 * g)
        assert np.allclose(W @ np.kron(U, U), U @ W)                                 # G₂-ковариантен
    agg = lambda X: W @ X @ W.T + np.real(np.trace((np.eye(49) - Pi) @ X)) * np.eye(7) / 7
    r = np.random.default_rng(1)
    c2 = 0.0
    for _ in range(400):
        a, b = random_pure(r), random_pure(r)
        c2 = max(c2, 6 * np.real(np.trace(Pi @ np.kron(a, b))))
        assert purity(agg(np.kron(a, b))) <= 5 / 21 + 1e-12
    assert c2 <= 2 + 1e-12
    e = np.eye(7)
    x, z = (e[0] + 1j * e[1]) / np.sqrt(2), (e[2] - 1j * e[5]) / np.sqrt(2)
    assert abs(np.linalg.norm(V @ np.kron(x, z)) ** 2 - 2) < 1e-12                   # граница 2 достигается
    for _ in range(300):
        lam = r.uniform(0.3, 1)
        s = lam * random_pure(r) + (1 - lam) * np.eye(7) / 7
        if purity(s) > 2 / 7:
            p = purity(agg(np.kron(s, s)))
            assert p <= 1 / 7 + (6 / 7) * ((1 - purity(s)) / 2) ** 2 + 1e-12 and p < 0.2522


def test_viability_passes_to_the_aggregate_only_at_weak_coupling():
    """Теоремы 9.5 (b)–(f) и 9.6 (a): жизнеспособность и инварианты переходят к агрегату при слабой связи.

    Воплощённый голоном генератора КК-7 (μ = 1, якорь веса 0,8): P(ρ*) = 0,3115, P(ρ_lin) = 0,3223 —
    стационарное состояние линейной части без регенерации, ε_V = μ(P_lin − 2/7)/(2√P_lin) = 0,03225.
    Связь в базисе Белла (максимально запутанные собственные векторы), размах s = 1,8246, порог g* = 0,01768.
    (b) Тождество маргинали L[X₁] = i g Tr₂[H, X] на стационарном состоянии — до 1e-15.
    (d) При g ≤ g* маргинали жизнеспособны; при g = 1 ещё живы (0,297); при g = 10 — мертвы (→ 1/7).
    (e) Доминирование хребта (κ = 0,1, μ = 3,5, L_R ≤ 29κ): ‖X_i(t) − ρ*‖₁ ≤ e^{−(μ−L_R)t}‖X_i(0) − ρ*‖₁
    + g s/(μ − L_R) из максимально запутанного старта.
    (f) Бассейн: из запутанного и произведённого стартов маргинали приходят на расстояние 0,0643·g.
    """
    rng = np.random.default_rng(12)

    def herm(r):
        A = r.normal(size=(7, 7)) + 1j * r.normal(size=(7, 7))
        return (A + A.conj().T) / 2
    tn = lambda X: float(np.abs(np.linalg.eigvalsh((X + X.conj().T) / 2)).sum())
    I7 = np.eye(7) / 7
    v = rng.normal(size=7) + 1j * rng.normal(size=7)
    v /= np.linalg.norm(v)
    H = 0.3 * herm(rng)
    sig = 0.8 * np.outer(v, v.conj()) + 0.2 * I7
    a = _holon_pair_generator(H, sig, mu=1.0)
    f = lambda G: np.einsum("iaja->ij", a(np.kron(G, I7).reshape(7, 7, 7, 7), G))
    rho = _rk4(I7, f, 40.0, 800)
    assert np.linalg.norm(f(rho)) < 1e-12 and abs(purity(rho) - 0.31146) < 1e-4
    flin = lambda G: -1j * (H @ G - G @ H) + (2 / 3) * (np.diag(np.diag(G)) - G) + (sig * np.trace(G) - G)
    L0 = np.array([flin(E.reshape(7, 7)).reshape(-1) for E in np.eye(49).astype(complex)]).T
    rl = np.linalg.lstsq(np.vstack([L0, np.eye(7).reshape(1, -1)]), np.eye(50)[-1], rcond=None)[0].reshape(7, 7)
    Pl = purity(rl)
    epsV = (Pl - 2 / 7) / (2 * np.sqrt(Pl))
    assert abs(Pl - 0.32234) < 1e-4 and abs(epsV - 0.03225) < 1e-4
    assert tn(rl - sig) <= tn(flin(sig)) + 1e-12                                     # ‖ρ_lin − σ‖₁ ≤ ‖L⁰σ‖₁/μ
    for _ in range(200):                                                              # (c): невязка ниже 2/7
        G = random_state(rng)
        if purity(G) <= 2 / 7:
            assert tn(f(G)) >= epsV - 1e-12
    marg = lambda X: (np.einsum("ijkj->ik", X.reshape(7, 7, 7, 7)), np.einsum("ijil->jl", X.reshape(7, 7, 7, 7)))

    def rhs(X, g, Hint):
        g1, g2 = marg(X)
        X4 = X.reshape(7, 7, 7, 7)
        out = a(X4, g1) + a(X4.transpose(1, 0, 3, 2), g2).transpose(1, 0, 3, 2)
        return out.reshape(49, 49) - 1j * g * (Hint @ X - X @ Hint)
    w = np.exp(2j * np.pi / 7)
    B = np.zeros((49, 49), complex)
    for m in range(7):
        for n in range(7):
            for j in range(7):
                B[j * 7 + (j + m) % 7, m * 7 + n] = w ** (j * n) / np.sqrt(7)
    assert np.allclose(B.conj().T @ B, np.eye(49))
    for col in B.T:
        assert np.allclose(np.einsum("ij,kj->ik", col.reshape(7, 7), col.reshape(7, 7).conj()), I7)
    Hb = B @ np.diag(np.random.default_rng(2).uniform(-1, 1, 49)) @ B.conj().T
    s = np.ptp(np.linalg.eigvalsh(Hb))
    gstar = epsV / s
    assert abs(s - 1.8246) < 1e-3 and abs(gstar - 0.01768) < 1e-4
    sigma = np.kron(rho, rho).astype(complex)
    P1 = {}
    for g in (gstar, 1.0, 10.0):
        n = int(max(800, 60 * g * s))
        X = _rk4(sigma, lambda X: rhs(X, g, Hb), 60.0, n)
        assert np.linalg.norm(rhs(X, g, Hb)) < 1e-9
        g1, g2 = marg(X)
        comm = Hb @ X - X @ Hb
        assert np.linalg.norm(f(g1) - 1j * g * np.einsum("ijkj->ik", comm.reshape(7, 7, 7, 7))) < 1e-12   # (b)
        assert tn(f(g1)) <= g * s + 1e-12
        P1[g] = (purity(g1), purity(g2), purity((g1 + g2) / 2))
    assert min(P1[gstar]) > 2 / 7 and min(P1[1.0]) > 2 / 7                           # (d)
    assert max(P1[10.0]) < 0.16                                                        # 9.6 (a): → 1/7
    Hg = np.kron(herm(np.random.default_rng(4)), herm(np.random.default_rng(5)))
    Hg /= np.linalg.norm(Hg, 2)
    for start in (random_pure(np.random.default_rng(80), 49),
                  np.kron(random_pure(np.random.default_rng(81)), random_pure(np.random.default_rng(82)))):
        ratio = []
        for g in (0.01, 0.02):
            X = _rk4(start, lambda X: rhs(X, g, Hg), 40.0, 800)
            ratio.append(max(tn(m - rho) for m in marg(X)) / g)
        assert abs(ratio[0] - 0.0643) < 1e-3 and abs(ratio[1] / ratio[0] - 1) < 3e-3  # (f) O(g) из бассейна
    # (e) доминирование хребта: фиксированная цель регенерации, κ = 0,1, μ = 3,5, L_R ≤ 29κ
    r = np.random.default_rng(7)
    H2 = 0.2 * herm(r)
    kap, mu, LR = 0.1, 3.5, 2.9
    tgt = np.diag(np.eye(7)[0]).astype(complex)
    sg = np.diag([0.66, 0.1, 0.06, 0.06, 0.04, 0.04, 0.04]).astype(complex)

    def frozen(G):
        gv = gate(purity(G))
        return lambda Y: (-1j * (H2 @ Y - Y @ H2) + (2 / 3) * (np.diag(np.diag(Y)) - Y)
                          + kap * gv * (tgt * np.trace(Y) - Y) + mu * (sg * np.trace(Y) - Y))
    f2 = lambda G: frozen(G)(G)
    rho2 = _rk4(I7, f2, 20.0, 1000)
    assert np.linalg.norm(f2(rho2)) < 1e-12

    def on1(M, X4):
        return np.einsum("ijkl,kalb->iajb", M, X4)

    def sup(Mf):
        return np.array([Mf(E.reshape(7, 7)).reshape(-1) for E in np.eye(49).astype(complex)]).T.reshape(7, 7, 7, 7)

    def rhs2(X, g):
        g1, g2 = marg(X)
        X4 = X.reshape(7, 7, 7, 7)
        out = on1(sup(frozen(g1)), X4) + on1(sup(frozen(g2)), X4.transpose(1, 0, 3, 2)).transpose(1, 0, 3, 2)
        return out.reshape(49, 49) - 1j * g * (Hb @ X - X @ Hb)
    X = random_pure(np.random.default_rng(50), 49)
    d0 = [tn(m - rho2) for m in marg(X)]
    g = 0.2
    for T in range(1, 7):
        X = _rk4(X, lambda X: rhs2(X, g), 1.0, 50)
        for dd, m in zip(d0, marg(X)):
            assert tn(m - rho2) <= np.exp(-(mu - LR) * T) * dd + g * s / (mu - LR)   # (e)


def _living_generator(H, anchor, kap, alpha):
    """Генератор изолированного голонома с регенерацией к φ(Γ) = k P_α(Γ) + R·якорь(Γ), затвор g_V."""
    c = (1 - alpha) / 3

    def f(G):
        P = purity(G)
        R = 1 / (7 * P)
        D = np.diag(np.diag(G))
        return (-1j * (H @ G - G @ H) + (2 / 3) * (D - G)
                + kap * gate(P) * ((1 - R) * (D + c * (G - D)) + R * anchor(G) - G))
    return f


def _stationary(f, G):
    """Уточнение стационарной точки методом наименьших квадратов в 48 вещественных координатах."""
    E = _jacobian_basis()
    to = lambda X: np.real(np.einsum("aij,ji->a", E, X))
    fr = lambda v: np.eye(7) / 7 + np.einsum("a,aij->ij", v, E)
    r = least_squares(lambda v: to(f(fr(v))), to(G - np.eye(7) / 7), xtol=1e-15, ftol=1e-15, gtol=1e-15)
    X = fr(r.x)
    return (X + X.conj().T) / 2


def _jacobian_basis():
    B = []
    for i in range(7):
        for j in range(i + 1, 7):
            M = np.zeros((7, 7), complex)
            M[i, j] = M[j, i] = 1 / np.sqrt(2)
            B.append(M)
            M = np.zeros((7, 7), complex)
            M[i, j], M[j, i] = -1j / np.sqrt(2), 1j / np.sqrt(2)
            B.append(M)
    for m in range(6):
        d = np.zeros(7)
        d[:m + 1], d[m + 1] = 1, -(m + 1)
        B.append(np.diag(d / np.linalg.norm(d)).astype(complex))
    return np.array(B)


def _q_window(eta, c, t=1.0):
    """Q(η) = (6η² − 1)[(t − cη)/(η(1 + 6η²)) − (1 − c)]: стационарность семейства Γ_η ⇔ κQ = 2/3."""
    return (6 * eta ** 2 - 1) * ((t - c * eta) / (eta * (1 + 6 * eta ** 2)) - (1 - c))


def test_collineation_anchor_holds_a_living_attractor_in_the_window():
    """Якорь коллинеаций uu† держит изолированный голоном в сознательном окне: аттрактор в V_full.

    Свидетель теоремы о живом аттракторе в окне (эволюция): φ_J(Γ) = k P_α(Γ) + R uu†, u = (1,…,1)/√7 —
    единственное чистое состояние, неподвижное при 168 коллинеациях Фано (коммутант {I, J}).
    При H = 0 стационарные точки с P > 2/7 — ровно Γ_η = (1−η)I/7 + η uu† с κQ(η) = 2/3; Q строго
    вогнута, κ_c(α) = 2/(3 max Q): 16,63 (α = 0), 29,25 (α = ½), 59,34 (α = 1). При α = ½, κ = 40
    два корня: седло P = 0,2962 и сток P = 0,3213, Φ = 6η² = 1,249; спектр якобиана стока —
    {κηQ′(η); −κgR ×6; −(⅔ + κg(1 − kc)) ×41} до 1e-6; баланс T-98 (κg_V) до 1e-12. Со случайным H
    нормы 1 аттрактор сохраняется в V_full; ниже порога (κ = 20) поток из uu† умирает в I/7.
    """
    perms = []
    for p in itertools.permutations(range(7)):
        lines = {frozenset(x - 1 for x in l) for l in LINES}
        if all(frozenset(p[x - 1] for x in l) in lines for l in LINES):
            perms.append(np.eye(7)[list(p)])
    assert len(perms) == 168
    A = np.vstack([np.kron(M, M) - np.eye(49) for M in perms])
    assert int(np.sum(np.linalg.svd(A, compute_uv=False) < 1e-9)) == 2               # коммутант {I, J}
    u = np.ones(7) / np.sqrt(7)
    uu = np.outer(u, u).astype(complex)
    assert all(np.allclose(M @ u, u) for M in perms)
    ph = np.diag(np.exp(1j * np.random.default_rng(2).uniform(0, 2 * np.pi, 7)))
    A = np.vstack([A, np.kron(ph, ph.conj()) - np.eye(49)])                          # + фазы: унитальна
    assert int(np.sum(np.linalg.svd(A, compute_uv=False) < 1e-9)) == 1
    eta = np.linspace(1 / np.sqrt(6), 1 / np.sqrt(3), 4001)
    for cc in np.linspace(0, 1 / 3, 7):                                               # Q″ < 0 на всём окне
        q = _q_window(eta, cc)
        assert np.max(np.diff(q, 2)) < 0
    kc = {a: (2 / 3) / np.max(_q_window(eta, (1 - a) / 3)) for a in (0.0, 0.5, 1.0)}
    assert abs(kc[0.0] - 16.628) < 5e-3 and abs(kc[0.5] - 29.254) < 5e-3 and abs(kc[1.0] - 59.345) < 5e-3
    assert abs(_q_window(0.5, 1 / 3)) < 1e-15                                         # P_∞(α = 0) = 5/14
    alpha, kap, c = 0.5, 40.0, 0.5 / 3
    zero = np.zeros((7, 7))
    f = _living_generator(zero, lambda G: uu, kap, alpha)
    fam = lambda e: np.eye(7) / 7 + e * (uu - np.eye(7) / 7)
    v = kap * _q_window(eta, c) - 2 / 3
    roots = [eta[i] for i in range(len(eta) - 1) if v[i] * v[i + 1] < 0]
    assert len(roots) == 2
    Ps = []
    for e0 in roots:
        G = _stationary(f, fam(e0))
        e = float(np.real(G[0, 1])) * 7
        assert np.linalg.norm(f(G)) < 1e-12 and np.linalg.norm(G - fam(e)) < 1e-12
        Ps.append(purity(G))
        spec = np.sort(np.linalg.eigvals(_jacobian(f, G)).real)
        P, g = purity(G), gate(purity(G))
        R = 1 / (7 * P)
        dq = (_q_window(e + 1e-7, c) - _q_window(e - 1e-7, c)) / 2e-7
        want = sorted([kap * e * dq] + [-kap * g * R] * 6 + [-(2 / 3 + kap * g * (1 - (1 - R) * c))] * 41)
        assert np.allclose(spec, want, atol=1e-5)
        if dq < 0:
            star, estar = G, e
    assert abs(Ps[0] - 0.2962) < 1e-4 and abs(Ps[1] - 0.3213) < 1e-4
    P = purity(star)
    assert 2 / 7 < P < 3 / 7 and 1 < integration(star) < 2 and abs(integration(star) - 6 * estar ** 2) < 1e-12
    assert np.allclose(np.diag(star).real, 1 / 7, atol=1e-13)
    R = 1 / (7 * P)
    fstar = np.real(np.trace(star @ ((1 - R) * (np.diag(np.diag(star)) + c * (star - np.diag(np.diag(star))))
                                     + R * uu)))
    pd, kg = float(np.sum(np.real(np.diag(star)) ** 2)), kap * gate(P)
    assert abs((2 / 3 * pd + kg * fstar) / (2 / 3 + kg) - P) < 1e-12                  # T-98 с κ g_V
    rng = np.random.default_rng(4)
    B = rng.normal(size=(7, 7)) + 1j * rng.normal(size=(7, 7))
    H = (B + B.conj().T) / 2
    H /= np.linalg.norm(H, 2)
    fh = _living_generator(H, lambda G: uu, kap, alpha)
    G = _stationary(fh, star)
    assert np.linalg.norm(fh(G)) < 1e-12 and np.max(np.linalg.eigvals(_jacobian(fh, G)).real) < -1
    assert 2 / 7 < purity(G) < 3 / 7 and integration(G) > 1 and np.min(np.real(np.diag(G))) > 0.1
    assert np.min(np.linalg.eigvalsh(G)) > 0
    low = _living_generator(H, lambda G: uu, 20.0, alpha)
    assert np.max(20.0 * _q_window(eta, c)) < 2 / 3
    assert abs(purity(_rk4(uu, low, 30.0, 3000)) - 1 / 7) < 1e-9


def test_phase_symmetric_self_models_hold_no_coherent_hyperbolic_state():
    """Без фазового репера когерентное состояние не гиперболично; окно по P — да, V_full — нет.

    Свидетель теоремы о фазовом препятствии (эволюция): при H = 0 самомодель, ковариантная
    относительно диагональных унитарных (φ_coh, φ_s, всякий спектральный якорь, фано-регистрация),
    имеет у недиагональной стационарной точки нулевое собственное значение. Спектральный якорь
    Γ⁸/TrΓ⁸ при α = ½, κ = 40 держит Γ_η той же формы, что и якорь uu†, но у неё 6 нулевых и 6
    растущих направлений. Фано-регистрация (якорь Π_p/3 самой вероятной прямой) даёт при H = 0 семь
    стоков Π_p/3 с P = 1/3 и спектром {−κ/7 ×6; −⅔ − (κ/3)(1 − 4c/7) ×42} при любом κ > 0, Φ = 0.
    """
    alpha, kap, c = 0.5, 40.0, 0.5 / 3
    zero = np.zeros((7, 7))
    u = np.ones(7) / np.sqrt(7)
    uu = np.outer(u, u).astype(complex)

    def spec8(G):
        w, V = np.linalg.eigh((G + G.conj().T) / 2)
        w = np.clip(w, 0, None) ** 8
        return (V * (w / w.sum())) @ V.conj().T
    f = _living_generator(zero, spec8, kap, alpha)
    G = _stationary(f, np.eye(7) / 7 + 0.456 * (uu - np.eye(7) / 7))
    assert np.linalg.norm(f(G)) < 1e-12 and 2 / 7 < purity(G) < 3 / 7 and integration(G) > 1
    ev = np.linalg.eigvals(_jacobian(f, G)).real
    assert np.sum(np.abs(ev) < 1e-5) == 6 and np.sum(ev > 1) == 6
    Pi = [np.diag([1.0 if m + 1 in l else 0.0 for m in range(7)]).astype(complex) for l in LINES]

    def line(G):
        p = [np.real(np.trace(X @ G)) for X in Pi]
        return Pi[int(np.argmax(p))] / 3
    for kap in (0.5, 1.0, 3.0):
        f = _living_generator(zero, line, kap, alpha)
        for X in Pi:
            assert np.linalg.norm(f(X / 3)) < 1e-15 and abs(purity(X / 3) - 1 / 3) < 1e-15
        spec = np.sort(np.linalg.eigvals(_jacobian(f, Pi[0] / 3)).real)
        want = sorted([-kap / 7] * 6 + [-2 / 3 - kap / 3 * (1 - 4 * c / 7)] * 42)
        assert np.allclose(spec, want, atol=1e-6)


def test_attractor_consistency_is_first_order_in_the_hamiltonian():
    """T-157 в верной форме: сдвиг аттрактора от точной самомодели — первого порядка по H.

    Свидетель переформулированной T-157 (замкнутость без субстрата §10). Прежнее «‖ρ* − Γ*_coh‖ ≤
    ‖H‖/(α + κ)» при Γ*_coh = I/7 ложно уже при H = 0: живой аттрактор φ_s есть e_m,
    ‖e_m − I/7‖_F = √(6/7). Верно: ρ*(H) = e_m + O(H), и главный член точен —
    ‖ρ*(H) − e_m‖_F = √2‖H e_m − H_mm e_m‖/(⅔ + 6κ(1 − c)/7) + O(‖H‖²) (при ε = 1e-3 отношение 1 ± 1e-3).
    Тождество дефекта самопознания κg(φ(ρ*) − ρ*) = −ℒ₀[ρ*] — до 1e-12. Для φ_J (α = ½, κ = 40)
    единственная неподвижная точка самомодели Γ_η∞, η∞ = 0,4725, отстоит от аттрактора на 0,0150
    при границе √(6/7)(2η₊/3)/|λ_Y| = 0,0217.
    """
    kap, alpha, c = 1.0, 0.5, 0.5 / 3
    e0 = np.diag(np.eye(7)[0]).astype(complex)
    assert abs(np.linalg.norm(e0 - np.eye(7) / 7) - np.sqrt(6 / 7)) < 1e-15
    rng = np.random.default_rng(9)
    B = rng.normal(size=(7, 7)) + 1j * rng.normal(size=(7, 7))
    H1 = (B + B.conj().T) / 2
    for eps in (1e-3, 1e-2):
        H = eps * H1
        f = lambda G: _frozen_self_registering(G, H, kap=kap, alpha=alpha)(G)
        G = _stationary(f, e0)
        col = H[:, 0].copy()
        col[0] = 0
        first = np.sqrt(2) * np.linalg.norm(col) / (2 / 3 + 6 * kap * (1 - c) / 7)
        ratio = np.linalg.norm(G - e0) / first
        assert abs(ratio - 1) < (2e-3 if eps == 1e-3 else 2e-2)
        P = purity(G)
        R = 1 / (7 * P)
        D = np.diag(np.diag(G))
        phi = (1 - R) * (D + c * (G - D)) + R * G @ G / P
        L0 = -1j * (H @ G - G @ H) + (2 / 3) * (D - G)
        assert np.linalg.norm(kap * gate(P) * (phi - G) + L0) < 1e-12
    eta = np.linspace(0.4, 0.55, 150001)                                              # φ_J: сдвиг O(1/κ)
    q = _q_window(eta, c)
    e_inf = eta[np.argmin(np.abs((1 - c * eta) / (eta * (1 + 6 * eta ** 2)) - (1 - c)))]
    v = 40.0 * q - 2 / 3
    e_plus = max(eta[i] for i in range(len(eta) - 1) if v[i] * v[i + 1] < 0)
    dq = (_q_window(e_plus + 1e-7, c) - _q_window(e_plus - 1e-7, c)) / 2e-7
    dist, bound = np.sqrt(6 / 7) * (e_inf - e_plus), np.sqrt(6 / 7) * (2 * e_plus / 3) / abs(40.0 * e_plus * dq)
    assert abs(e_inf - 0.4725) < 1e-4 and abs(dist - 0.0150) < 1e-4 and abs(bound - 0.0217) < 1e-4
    u = np.ones(7) / np.sqrt(7)
    uu = np.outer(u, u)
    fix = np.eye(7) / 7 + e_inf * (uu - np.eye(7) / 7)
    P = purity(fix)
    R = 1 / (7 * P)
    D = np.diag(np.diag(fix))
    assert np.linalg.norm((1 - R) * (D + c * (fix - D)) + R * uu - fix) < 1e-4       # φ_J(Γ_η∞) = Γ_η∞


def test_phi_coh_contracts_toward_i7_but_is_not_a_contraction():
    """φ_coh сжимает к I/7 (множитель k ≤ 6/7), но не является сжатием: у чистых состояний 54/49.

    Свидетель поправки к расщеплению шага (эволюция, итеративная схема): «схема сходится по Банаху,
    так как φ — сжатие с коэффициентом k» неверно дословно — k есть множитель у отклонения от I/7,
    а не константа Липшица; вдоль e₀ радиальная производная в чистом состоянии 54/49 > 1.
    Верно: шаг Ли–Троттера S = [(1−a) id + aφ_coh]∘e^{Δτℒ₀} даёт ‖Γ_n − I/7‖_F ≤ (1 − a/7)ⁿ‖Γ_0 − I/7‖_F.
    С φ_s при H = 0 у шага восемь неподвижных точек (e_m и I/7) — глобального сжатия нет.
    """
    pa = lambda G: np.diag(np.diag(G)) + (G - np.diag(np.diag(G))) / 6
    phi = lambda G: (1 - 1 / (7 * purity(G))) * pa(G) + np.eye(7) / (49 * purity(G))
    e0 = np.diag(np.eye(7)[0]).astype(complex)
    d = e0 - np.eye(7) / 7
    h = 1e-6
    lip = np.linalg.norm(phi(e0) - phi(e0 - h * d)) / np.linalg.norm(h * d)
    assert abs(lip - 54 / 49) < 1e-5
    rng = np.random.default_rng(12)
    B = rng.normal(size=(7, 7)) + 1j * rng.normal(size=(7, 7))
    H = 0.3 * (B + B.conj().T) / 2
    L0 = lambda G: -1j * (H @ G - G @ H) + (2 / 3) * (np.diag(np.diag(G)) - G)
    a, dt = 0.5, 0.1
    step = lambda G: (1 - a) * _rk4(G, L0, dt, 4) + a * phi(_rk4(G, L0, dt, 4))
    G = random_pure(rng)
    dist = [np.linalg.norm(G - np.eye(7) / 7)]
    for _ in range(60):
        G = step(G)
        dist.append(np.linalg.norm(G - np.eye(7) / 7))
    assert all(dist[n + 1] <= (1 - a / 7) * dist[n] + 1e-12 for n in range(60))
    zero = np.zeros((7, 7))
    phis = lambda G: (1 - 1 / (7 * purity(G))) * pa(G) + G @ G / (7 * purity(G) ** 2)
    stepS = lambda G: (1 - a) * G + a * phis(G)
    fixed = [np.eye(7) / 7] + [np.diag(np.eye(7)[m]).astype(complex) for m in range(7)]
    assert all(np.linalg.norm(stepS(X) - X) < 1e-15 for X in fixed)


# --- Consciousness meta-level, 25.09.2026 (T-221 corrected, Cons(S) against Kleiner-Hoel,
# --- enriched Yoneda for qualia, PCI bridge). Each test witnesses one statement of the
# --- corresponding page; see the page anchors in the docstrings.

def test_first_person_facts_of_two_subjects_are_not_compossible():
    """T-221(a): List's lemma in the centred-world form (List 2023a, footnote 1 of the
    quadrilemma). A centred world is (w, s); 'I am in state X' is the set of centred worlds
    whose centre is in X. For two subjects in different complete states no centred world
    satisfies both first-person facts, while the relativised (stage-indexed) facts are
    jointly satisfiable -- the relationalist route keeps one coherent world."""
    import itertools
    worlds = [("w", {"s1": "X", "s2": "Y"})]
    centred = [(w, s) for w, st in worlds for s in st]
    state = {c: worlds[0][1][c[1]] for c in centred}
    i_am_x = {c for c in centred if state[c] == "X"}
    i_am_y = {c for c in centred if state[c] == "Y"}
    assert i_am_x and i_am_y and not (i_am_x & i_am_y)
    # relativised facts: 'relative to s1, I am X' and 'relative to s2, I am Y' are
    # propositions about uncentred worlds and hold together at w
    rel = [lambda w: w[1]["s1"] == "X", lambda w: w[1]["s2"] == "Y"]
    assert all(f(worlds[0]) for f in rel)
    # the same with every assignment of two distinct complete states out of three
    for a, b in itertools.permutations("XYZ", 2):
        st = {"s1": a, "s2": b}
        cx = {s for s in st if st[s] == a}
        cy = {s for s in st if st[s] == b}
        assert not (cx & cy)


def test_viability_penalty_pins_every_subthreshold_reconstruction_at_two_sevenths():
    """Measurement protocol R5 (A-95): with the default lambda_2 = 100 the reconstruction of
    pi_bio returns P = 2/7 exactly for every uniform sub-threshold state, so P8.2
    (P < 2/7 in N3) cannot be observed; with lambda_2 = 0 the true P is returned. For the
    uniform family the pinning threshold is lambda_2 >= 10(1 - m/m_c), m_c = 1/sqrt(294)."""
    import numpy as np
    from scipy.optimize import minimize
    rng = np.random.default_rng(7)
    iu = np.triu_indices(7, 1)
    pos = []
    k = 0
    for i in range(7):
        for j in range(i + 1):
            pos.append((i, j, k))
            k += 1 if i == j else 2
    n = k

    def build(x):
        L = np.zeros((7, 7), complex)
        for i, j, q in pos:
            L[i, j] = max(x[q], 1e-6) if i == j else x[q] + 1j * x[q + 1]
        G = L @ L.conj().T
        return G / np.trace(G).real

    def recon(m, lam2):
        mag = np.full((7, 7), m)

        def f(x):
            G = build(x)
            ll = -np.sum((np.real(np.diag(G)) - 1 / 7) ** 2) / 0.01
            ll -= np.sum((np.abs(G[iu]) - mag[iu]) ** 2) / 0.05
            return -(ll - lam2 * max(0.0, 2 / 7 - np.real(np.trace(G @ G))))
        best = None
        for _ in range(3):
            x0 = 0.05 * rng.normal(size=n)
            for i, j, q in pos:
                if i == j:
                    x0[q] = np.sqrt(1 / 7)
            r = minimize(f, x0, method="L-BFGS-B",
                         options=dict(ftol=1e-14, gtol=1e-10, maxiter=20000))
            best = r if best is None or r.fun < best.fun else best
        G = build(best.x)
        return float(np.real(np.trace(G @ G)))
    for m in (0.02, 0.05):
        p_true = 1 / 7 + 42 * m * m
        assert p_true < 2 / 7
        assert abs(recon(m, 0.0) - p_true) < 2e-3
        assert abs(recon(m, 100.0) - 2 / 7) < 2e-3
    mc = 1 / np.sqrt(294)
    assert abs(1 / 7 + 42 * mc * mc - 2 / 7) < 1e-15


def test_uniform_diagonal_window_is_phi_between_one_and_two():
    """PCI bridge: on the uniform-diagonal stratum P = (1 + Phi)/7, R = 1/(1 + Phi),
    C = Phi R = Phi/(1 + Phi); the window P in (2/7, 3/7] is Phi in (1, 2] and C in (1/2, 2/3]."""
    import numpy as np
    rng = np.random.default_rng(3)
    seen = [0, 0]
    for _ in range(400):
        ph = np.exp(1j * rng.uniform(0, 2 * np.pi, 7))
        H = rng.uniform(0, 1 / 7) * (np.outer(ph, ph.conj()) - np.eye(7))
        N = rng.normal(size=(7, 7)) + 1j * rng.normal(size=(7, 7))
        N = 0.01 * (N + N.conj().T)
        np.fill_diagonal(N, 0)
        H = H + N
        G = np.eye(7) / 7 + H
        if np.min(np.linalg.eigvalsh(G)) < 0:
            continue
        P = np.real(np.trace(G @ G))
        off = np.sum(np.abs(G) ** 2) - np.sum(np.abs(np.diag(G)) ** 2)
        Phi = off / np.sum(np.abs(np.diag(G)) ** 2)
        assert abs(P - (1 + Phi) / 7) < 1e-12
        R = 1 / (7 * P)
        assert abs(R - 1 / (1 + Phi)) < 1e-12
        assert ((2 / 7 < P <= 3 / 7) == (1 < Phi <= 2 + 1e-15))
        seen[int(2 / 7 < P <= 3 / 7)] += 1
    assert min(seen) >= 20


def test_cons_verdict_and_quality_geometry_are_independent():
    """Kawakita et al. 2024 section: the Fubini-Study distances between the eigenrays of Gamma
    do not depend on its spectrum, and P does not depend on the eigenrays; the same quality
    geometry is carried by a state below 2/7 and by one inside the window."""
    import numpy as np
    rng = np.random.default_rng(11)
    Z = rng.normal(size=(7, 7)) + 1j * rng.normal(size=(7, 7))
    Q, _ = np.linalg.qr(Z)

    def geom(G):
        _, V = np.linalg.eigh(G)
        a = np.abs(V.conj().T @ Q)
        return np.sort(np.round(np.arccos(np.clip(a, 0, 1)), 5).ravel())
    lam_low = np.array([0.20, 0.18, 0.16, 0.14, 0.12, 0.11, 0.09])
    lam_in = np.array([0.50, 0.20, 0.10, 0.08, 0.06, 0.04, 0.02])
    G1 = Q @ np.diag(lam_low) @ Q.conj().T
    G2 = Q @ np.diag(lam_in) @ Q.conj().T
    P1, P2 = np.sum(lam_low ** 2), np.sum(lam_in ** 2)
    assert P1 < 2 / 7 < P2 <= 3 / 7
    assert np.allclose(geom(G1), geom(G2))


def test_enriched_yoneda_embedding_of_fubini_study_rays_is_an_isometry():
    """Categorical formalism, enriched Yoneda: for d = d_FS on CP^{n-1},
    sup_x (d(x, b) - d(x, a)) = d(a, b) (the presheaf hom of y a and y b), attained at x = a;
    a finite delta-net S gives d(a,b) - 2 delta <= max_s |d(s,a) - d(s,b)| <= d(a,b); and the
    normalised volume of an FS ball of radius r in CP^1 and CP^2 is sin^{2(n-1)} r."""
    import numpy as np
    rng = np.random.default_rng(5)

    def ray(n, k):
        v = rng.normal(size=(k, n)) + 1j * rng.normal(size=(k, n))
        return v / np.linalg.norm(v, axis=1, keepdims=True)

    def d(u, v):
        return np.arccos(np.clip(np.abs(u.conj() @ v.T), 0, 1))
    tol = 1e-6
    for n in (2, 3, 7):
        X = ray(n, 4000)
        A = ray(n, 20)
        D_AA = d(A, A)
        D_XA = d(X, A)
        for i in range(20):
            for j in range(20):
                sup = np.max(np.concatenate([D_XA[:, j] - D_XA[:, i], [D_AA[i, j] - D_AA[i, i]]]))
                assert sup <= D_AA[i, j] + tol
                assert abs(sup - D_AA[i, j]) < tol
    # finite-probe Yoneda on CP^1: a net of probes of covering radius delta
    X = ray(2, 3000)
    S = ray(2, 400)
    delta = np.max(np.min(d(X, S), axis=1))
    A = ray(2, 30)
    DAS = d(A, S)
    DAA = d(A, A)
    for i in range(30):
        for j in range(30):
            prof = np.max(np.abs(DAS[i] - DAS[j]))
            assert DAA[i, j] - 2 * delta - tol <= prof <= DAA[i, j] + tol
    for n in (2, 3):
        X = ray(n, 200000)
        c = ray(n, 1)[0]
        dist = np.arccos(np.clip(np.abs(X.conj() @ c), 0, 1))
        for r in (0.3, 0.7, 1.1):
            frac = np.mean(dist <= r)
            assert abs(frac - np.sin(r) ** (2 * (n - 1))) < 5e-3


# --- Теорема 48d и перестройка T-119 … T-121 (25.09.2026) ------------------------------------

def _j3_of_o():
    """J₃(𝕆): X = [[a₁, x₃, x̄₂], [x̄₃, a₂, x₁], [x₂, x̄₁, a₃]], координаты (a₁,a₂,a₃, x₁, x₂, x₃) ∈ ℝ²⁷."""
    def to_m(v):
        a, x = v[:3], [v[3:11], v[11:19], v[19:27]]
        r = lambda s: s * unit(0)
        return [[r(a[0]), x[2], _oconj(x[1])], [_oconj(x[2]), r(a[1]), x[0]], [x[1], _oconj(x[0]), r(a[2])]]

    def from_m(P):
        return np.concatenate([[P[0][0][0], P[1][1][0], P[2][2][0]], P[1][2], P[2][0], P[0][1]])

    def mul(P, Q):
        return [[sum(omul(P[i][k], Q[k][j]) for k in range(3)) for j in range(3)] for i in range(3)]

    def jordan(u, v):
        P, Q = to_m(u), to_m(v)
        A, B = mul(P, Q), mul(Q, P)
        return from_m([[(A[i][j] + B[i][j]) / 2 for j in range(3)] for i in range(3)])

    def lift(X7):
        Y = np.zeros((27, 27))
        for s in range(3):
            Y[4 + 8 * s:11 + 8 * s, 4 + 8 * s:11 + 8 * s] = X7
        return Y
    return jordan, lift


def test_no_unital_spin_factor_on_any_holon_register():
    """Теорема 48d(a)–(b): «двойка» (Q1) не живёт ни в голономах, ни в их регистрах.

    (a) Эрмитова инволюция s₁ на ℂ^d с собственными подпространствами размерностей p, q; всякий
    антикоммутирующий с ней эрмитов оператор переставляет их и имеет ранг ≤ 2·min(p, q) < d при
    нечётном d — двух антикоммутирующих обратимых инволюций, т. е. единичного спин-фактора, нет
    ни на ℂ⁷, ни на ℂ⁴⁹, ни на ℂ^{7^M}. (b) G₂-коммутант пары ℂ⁷⊗ℂ⁷ четырёхмерен и абелев
    (7⊗7 = 1+7+14+27 без кратностей: четыре значения Казимира на подпространствах 1, 7, 14, 27);
    цвет-синглетов в паре ровно 3, G₂-синглет один. Лапласиан пути регистра глубины имеет простой спектр — его коммутант абелев.
    """
    rng = np.random.default_rng(481)
    for d in (7, 49):
        for p in range(1, d):
            s = np.diag([1.0] * p + [-1.0] * (d - p))
            X = np.zeros((d, d), complex)
            B = rng.normal(size=(p, d - p)) + 1j * rng.normal(size=(p, d - p))
            X[:p, p:], X[p:, :p] = B, B.conj().T
            assert np.allclose(s @ X + X @ s, 0) and np.linalg.matrix_rank(X) == 2 * min(p, d - p) < d
    su3 = _su3_of_e_o()
    pair = lambda gens: [np.kron(g, np.eye(7)) + np.kron(np.eye(7), g) for g in gens]
    g2p, su3p = pair(G2), pair(su3)
    Q = np.array([[np.trace(a @ b) for b in G2] for a in G2])                   # форма Киллинга (с точностью до знака)
    Qi = np.linalg.inv(Q)
    cas = sum(Qi[a, b] * g2p[a] @ g2p[b] for a in range(14) for b in range(14))
    vals = np.round(np.linalg.eigvalsh((cas + cas.T) / 2), 6)
    u, cnt = np.unique(vals, return_counts=True)
    assert sorted(cnt) == [1, 7, 14, 27]                                          # без кратностей: коммутант ℂ⁴, абелев
    assert _nullspace(np.vstack(su3p)).shape[0] == 3 and _nullspace(np.vstack(g2p)).shape[0] == 1
    for n in (7, 49, 343):
        L = np.diag([1.0] + [2.0] * (n - 2) + [1.0]) - np.eye(n, k=1) - np.eye(n, k=-1)
        assert np.min(np.diff(np.linalg.eigvalsh(L))) > 1e-5


def test_colour_singlet_part_of_the_exceptional_jordan_algebra_is_hermitian_c3():
    """Теорема 48d(c): J₃(𝕆)^{SU(3)_C} = h₃(ℂ_O) ≅ Herm(ℂ³), J₃(𝕆)^{G₂} = h₃(ℝ).

    Неподвижная часть 27-мерной J₃(𝕆) под 𝔰𝔲(3)_C девятимерна и замкнута относительно
    йорданова произведения; под 𝔤₂ — шестимерна. Пирсово 0-пространство идемпотента E₁ —
    h₂(𝕆) (размерность 10), его цвет-неподвижная часть четырёхмерна и несёт форму det
    сигнатуры (1,3): пространство-время 48c.
    """
    jordan, lift = _j3_of_o()
    su3 = [lift(X) for X in _su3_of_e_o()]
    g2 = [lift(X) for X in G2]
    Fc, Fg = _nullspace(np.vstack(su3)), _nullspace(np.vstack(g2))
    assert (Fc.shape[0], Fg.shape[0]) == (9, 6)
    for u in Fc:
        for v in Fc:
            w = jordan(u, v)
            assert np.linalg.norm(w - Fc.T @ (Fc @ w)) < 1e-9
    E1 = np.zeros(27)
    E1[0] = 1
    assert np.allclose(jordan(E1, E1), E1)
    L = np.array([jordan(E1, np.eye(27)[k]) for k in range(27)]).T
    P0 = _nullspace(L)
    assert P0.shape[0] == 10
    both = _nullspace(np.vstack([L, np.vstack(su3)]))
    assert both.shape[0] == 4
    # det на h₂ = a₂a₃ − |x₁|²: координаты 1, 2 и 3…10
    Gm = np.zeros((27, 27))
    Gm[1, 2] = Gm[2, 1] = 0.5
    Gm[3:11, 3:11] = -np.eye(8)
    ev = np.linalg.eigvalsh(both @ Gm @ both.T)
    assert (np.sum(ev > 1e-9), np.sum(ev < -1e-9)) == (1, 3)


def test_spatial_triplet_of_48c_is_the_weak_triplet():
    """Теорема 48d(d): в одной Spin(9) у цвета один централизатор 𝔲(2) — пространство 48c и SU(2)_L T-326 совпадают.

    Цвет-неподвижная часть вектора ℝ⁹ системы Клиффорда на 𝒮 = ℂ⊗𝕆 трёхмерна — span{iL_{e_O}, J, iJ};
    производная централизатора цвета (единственная 𝔰𝔲(2)) действует на ней неприводимо, как 𝔰𝔬(3).
    Та же тройка в h₂(𝕆) — {e_Oσ_y, σ_z, σ_x}, те же вращения — пространственные вращения 48c(e).
    Отождествить 𝕆² из 48c(f) с 𝒮 значит сделать слабый изоспин пространственным вращением.
    """
    d = _sm_on_complex_octonions()
    gam, su3 = d["gam"], d["su3"]
    G = np.array([g.flatten() for g in gam]).T

    def on_vector(Z):
        M = np.zeros((9, 9))
        for a, g in enumerate(gam):
            v = (Z @ g - g @ Z).flatten()
            coef = np.linalg.lstsq(G, v, rcond=None)[0]
            assert np.linalg.norm(G @ coef - v) < 1e-9
            M[:, a] = coef
        return M
    fixed = _nullspace(np.vstack([on_vector(X) for X in su3]))
    assert fixed.shape[0] == 3
    target = np.zeros((3, 9))
    target[0, 6], target[1, 7], target[2, 8] = 1, 1, 1                          # iL_{e_O}, J, iJ
    assert np.linalg.matrix_rank(np.vstack([fixed, target]), tol=1e-9) == 3
    comm = [A @ B - B @ A for i, A in enumerate(d["C"]) for B in d["C"][i + 1:]]
    U, s, _ = np.linalg.svd(np.array([X.flatten() for X in comm]).T, full_matrices=False)
    su2 = [U[:, i].reshape(16, 16) for i in range(int(np.sum(s > 1e-9)))]
    assert len(su2) == 3
    R = [target @ on_vector(X) @ target.T for X in su2]
    assert np.linalg.matrix_rank(np.array([r.flatten() for r in R]), tol=1e-9) == 3
    assert _nullspace(np.vstack(R)).shape[0] == 0                               # неприводимо: общих неподвижных нет


def _clock_torus_weights():
    """Совместные собственные значения максимального тора U(3) = C_{SO(7)}(J)∩Stab(e_O) на ℂ⁷."""
    su3 = _su3_of_e_o()
    rng = np.random.default_rng(119)
    X = sum(c * g for c, g in zip(rng.normal(size=8), su3))
    cart = [sum(v[k] * su3[k] for k in range(8)) for v in _nullspace(np.array([(X @ g - g @ X).ravel() for g in su3]).T)]
    J = np.array([omul(unit(7), unit(i + 1))[1:] for i in range(7)]).T
    J[6, :], J[:, 6] = 0, 0
    H = [1j * c for c in cart] + [1j * J]
    _, V = np.linalg.eigh(sum(r * h for r, h in zip((1, np.pi, np.e), H)))
    return H, np.array([[np.real(V[:, k].conj() @ h @ V[:, k]) for h in H] for k in range(7)])


def test_emergent_space_is_the_octahedron_and_its_fluctuations_the_three_sphere():
    """T-119 в верной форме: пространство — спектр трёх коммутирующих вращательных зарядов.

    Три генератора (два картановских 𝔰𝔲(3)_C и J = L_{e_O}) коммутируют; совместный спектр на ℂ⁷ —
    начало (ось O) и три антиподальные пары линейно независимых точек: октаэдр ≅ B³ (ранг 𝔰𝔬(7) = 3).
    Средние по M голономам имеют спектр (1/M)·{n ∈ ℤ³ : |n|₁ ≤ M} в весовых координатах — он
    сгущается к октаэдру (всякая точка октаэдра не дальше √3/(2M) от спектра). Флуктуации
    (n − Mμ)/√M при μ внутри октаэдра покрывают всякий шар радиуса R с шагом 1/√M: спектр — ℝ³,
    ковариация в состоянии I/7 невырождена. Минимальная унитизация C₀(ℝ³) — C(S³).
    (d) Эрмитовых операторов, коммутирующих с 𝔰𝔲(3)_C, — ровно 3 (P_O, P_𝟑, P_𝟑̄): цвет-синглетные
    координаты дают два измерения, не три.
    """
    H, pts = _clock_torus_weights()
    assert all(np.allclose(a @ b, b @ a) for a in H for b in H)
    nz = pts[np.linalg.norm(pts, axis=1) > 1e-9]
    assert len(nz) == 6 and np.linalg.matrix_rank(nz, tol=1e-9) == 3
    assert all(min(np.linalg.norm(p + q) for q in nz) < 1e-9 for p in nz)
    B = np.array([nz[0], *[p for p in nz[1:] if np.linalg.matrix_rank(np.array([nz[0], p]), tol=1e-9) == 2][:1]])
    B = np.vstack([B, [p for p in nz if np.linalg.matrix_rank(np.vstack([B, p]), tol=1e-9) == 3][0]])
    w = np.linalg.solve(B.T, nz.T).T                                              # весовые координаты
    assert np.allclose(np.sort(np.abs(w).sum(axis=1)), 1) and np.allclose(np.abs(w).max(axis=1), 1)
    for M in (10, 40):
        g = np.array(list(itertools.product(range(-M, M + 1), repeat=3)))
        spec = g[np.abs(g).sum(axis=1) <= M] / M
        probe = np.random.default_rng(M).uniform(-1, 1, size=(300, 3))
        probe = probe[np.abs(probe).sum(axis=1) <= 1]
        dist = np.min(np.linalg.norm(probe[:, None, :] - spec[None, :, :], axis=2), axis=1)
        assert dist.max() <= np.sqrt(3) / (2 * M) + 1e-12
    mu = np.array([0.1, -0.05, 0.2])                                              # внутри октаэдра
    R, M = 3.0, 10 ** 6
    probe = np.random.default_rng(7).uniform(-R, R, size=(200, 3))
    n = np.rint(probe * np.sqrt(M) + M * mu)
    assert np.all(np.abs(n).sum(axis=1) <= M)
    assert np.max(np.linalg.norm((n - M * mu) / np.sqrt(M) - probe, axis=1)) <= np.sqrt(3) / (2 * np.sqrt(M)) + 1e-12
    Cov = np.array([[np.trace(a @ b).real / 7 for b in H] for a in H])
    assert np.all(np.linalg.eigvalsh(Cov) > 0.1)
    herm = []                                                                     # (d): цвет-синглетных зарядов — 3 (с единицей)
    for i in range(7):
        for j in range(i, 7):
            E = np.zeros((7, 7), complex)
            E[i, j] = E[j, i] = 1
            herm.append(E)
            if i != j:
                F = np.zeros((7, 7), complex)
                F[i, j], F[j, i] = 1j, -1j
                herm.append(F)
    rows = np.vstack([np.array([(S @ X - X @ S).ravel() for S in herm]).T for X in _su3_of_e_o()])
    assert _nullspace(np.vstack([rows.real, rows.imag])).shape[0] == 3


# ---------------------------------------------------------------------------
# Юкавы в клиффордовой рамке Spin(10) и антиунитарная симметрия вакуума (25.09.2026, T-332, T-333).
# Юкава — ℝ-линейное отображение h ↦ M(h) бесцветной 4-плоскости {iL_{e_O}, J, iJ, γ₁₀} в
# ω-антилинейные операторы V_L → V_R (форма дираковской массы, T-329(е)), эквивариантное под группой.
# ---------------------------------------------------------------------------

@functools.lru_cache(maxsize=None)
def _yukawa_frame():
    e = _spin10_completion()
    om, PL, PR, g10 = e["om"], e["PL"], e["PR"], e["g10"]

    def half(P):
        w, V = np.linalg.eigh(P)
        return V[:, w > 0.5]
    UL, UR = half(PL), half(PR)
    G = np.array([g.flatten() for g in g10]).T

    def on_vector(X):
        M = np.zeros((10, 10))
        for a, g in enumerate(g10):
            v = (X @ g - g @ X).flatten()
            M[:, a] = np.linalg.lstsq(G, v, rcond=None)[0]
        return M

    def charge(X):
        q = -om @ X
        return (q + q.T) / 2

    def proj(q, val, P):
        w, V = np.linalg.eigh(P @ q @ P + 50 * (np.eye(32) - P))
        Vs = V[:, np.abs(w - val) < 1e-7]
        return Vs @ Vs.T
    t3l, t3r, bl = charge(e["T3L"]), charge(e["T3R"]), 2 * charge(e["BL"])
    secL = {"u": (0.5, 1 / 3), "d": (-0.5, 1 / 3), "nu": (0.5, -1.0), "e": (-0.5, -1.0)}
    secR = {"u": (-0.5, -1 / 3), "d": (0.5, -1 / 3), "nu": (-0.5, 1.0), "e": (0.5, 1.0)}
    secL = {k: proj(t3l, a, PL) @ proj(bl, b, PL) for k, (a, b) in secL.items()}
    secR = {k: proj(t3r, a, PR) @ proj(bl, b, PR) for k, (a, b) in secR.items()}
    span = lambda ops, space: [sum(v[i] * space[i] for i in range(len(space))) for v in _null_commutant(ops, space)]
    L1, R1 = e["lift"](e["d"]["Lu"]), e["lift"](e["d"]["Ru"])
    tau = -e["I1"] @ L1                                                  # τ = −i·L_{e_O}
    return dict(e=e, UL=UL, UR=UR, on_vector=on_vector, secL=secL, secR=secR, L1=L1, tau=tau,
                PS=span([L1], e["spin10"]), LR=span([L1, R1], e["spin10"]))


def _yukawa_masses(M):
    f = _yukawa_frame()
    return {k: float(np.linalg.svd(f["secR"][k] @ M @ f["secL"][k], compute_uv=False)[0]) for k in f["secL"]}


def _yukawa_space(alg, seed=1):
    """Эквивариантные ω-антилинейные M: плоскость → Hom(V_L, V_R). Алгебра задаётся двумя общими элементами."""
    f = _yukawa_frame()
    e, UL, UR = f["e"], f["UL"], f["UR"]
    rng = np.random.default_rng(seed)
    gens = [sum(c * x for c, x in zip(rng.normal(size=len(alg)), alg)) for _ in range(2)]
    omL, omR = UL.T @ e["om"] @ UL, UR.T @ e["om"] @ UR
    n, rows = 256, []
    for X in gens:
        R = f["on_vector"](X)[6:, 6:]
        XL, XR = UL.T @ X @ UL, UR.T @ X @ UR
        for a in range(4):
            blk = np.zeros((n, 4 * n))
            blk[:, a * n:(a + 1) * n] += np.kron(XR, np.eye(16)) - np.kron(np.eye(16), XL.T)
            for b in range(4):
                blk[:, b * n:(b + 1) * n] -= R[b, a] * np.eye(n)
            rows.append(blk)
    for a in range(4):
        blk = np.zeros((n, 4 * n))
        blk[:, a * n:(a + 1) * n] = np.kron(omR, np.eye(16)) + np.kron(np.eye(16), omL.T)
        rows.append(blk)
    _, s, Vt = np.linalg.svd(np.vstack(rows), full_matrices=True)
    N = Vt[np.sum(s > 1e-9):].T
    to_ops = lambda x: [UR @ x[a * n:(a + 1) * n].reshape(16, 16) @ UL.T for a in range(4)]
    return N, to_ops


def test_up_and_down_are_where_the_hilbert_unit_meets_the_clock():
    """T-332(а): верхние поля — там, где мнимая единица ℋ совпадает с часами, i = L_{e_O}; нижние — i = −L_{e_O}.

    τ = −iL_{e_O} на 𝒮_ℂ: +1 на u_L, ν_L, u^c, ν^c и −1 на d_L, e_L, d^c, e^c — одинаково на обеих
    половинах. τ_R = τ|_{V_R} (= 2T₃R со знаком) коммутирует с 𝔤_SM; τ на V_L — это 2T₃L и с 𝔰𝔲(2)_L
    не коммутирует. На ℂ⁷ ⊂ 𝒮 собственные пространства L_{e_O} = ∓i (цветные «триплет» P_𝟑 и
    «антитриплет» P_𝟑̄ страницы термодинамики Gap) — нижняя и верхняя компоненты кваркового дублета.
    Цветово-инвариантный вакуум T-64 равен a|O⟩⟨O| + (b+c)/2·Π₆ − (b−c)/2·τ: его параметр Gap b − c —
    компонента T₃L; продолженный на 𝒮 весом t на η₀, он коммутирует с 𝔰𝔲(2)_L только при b = c и t = a.
    """
    f = _yukawa_frame()
    e, tau = f["e"], f["tau"]
    assert np.allclose(tau, tau.T) and np.allclose(tau @ tau, np.eye(32))
    for k, sgn in (("u", 1), ("nu", 1), ("d", -1), ("e", -1)):
        for P in (f["secL"][k], f["secR"][k]):
            assert np.allclose(tau @ P, sgn * P)
    tauR = e["PR"] @ tau @ e["PR"]
    assert max(np.abs(tauR @ x - x @ tauR).max() for x in e["sm"]) < 1e-12
    assert max(np.abs(tau @ x - x @ tau).max() for x in e["suL"]) > 0.1
    d = e["d"]
    tS = -d["imul"] @ d["Lu"]                                                    # τ на 𝒮 = ℝ¹⁶
    Lc = _l_of(np.eye(7)[O_AXIS])
    w, V = np.linalg.eigh(1j * Lc)                                               # iL: +1 на L = −i (P_𝟑), −1 на P_𝟑̄
    for val, sgn in ((1.0, -1), (-1.0, 1)):
        for x in V[:, np.abs(w - val) < 1e-9].T:
            X = np.zeros(8, complex)
            X[1:] = x
            xr = np.concatenate([X.real, X.imag])
            assert np.allclose(tS @ xr, sgn * xr)                                 # P_𝟑 — нижние, P_𝟑̄ — верхние
    a, b, c = 0.37, 0.15, 0.06
    G = _colour_family(a, b, c)
    Pi6 = np.eye(7) - np.outer(np.eye(7)[O_AXIS], np.eye(7)[O_AXIS])
    assert np.allclose(G, a * (np.eye(7) - Pi6) + (b + c) / 2 * Pi6 + 1j * (b - c) / 2 * Lc)
    assert np.isclose(float(np.sum(G.imag ** 2)), 1.5 * (b - c) ** 2)            # 𝒢 = ‖Im Γ‖² = (3/2)(b−c)²
    comm = [x @ y - y @ x for x in d["C"] for y in d["C"]]                    # 𝔰𝔲(2) T-326 = 𝔰𝔲(2)_L на V_L ≅ 𝒮
    U, sv, _ = np.linalg.svd(np.array([x.flatten() for x in comm]).T, full_matrices=False)
    su2 = [U[:, i].reshape(16, 16) for i in range(int(np.sum(sv > 1e-9)))]
    assert len(su2) == 3

    def gamma_hat(a, b, c, t):
        M = np.zeros((8, 8), complex)
        M[1:, 1:] = _colour_family(a, b, c)
        M[0, 0] = t
        return np.block([[M.real, -M.imag], [M.imag, M.real]])
    for (a, b, c, t), ok in (((0.4, 0.1, 0.1, 0.4), True), ((0.4, 0.1, 0.1, 0.0), False),
                             ((0.4, 0.2, 0.0, 0.4), False), ((1 / 7, 1 / 7, 1 / 7, 0.0), False)):
        Gh = gamma_hat(a, b, c, t)
        assert (max(np.abs(Gh @ x - x @ Gh).max() for x in su2) < 1e-12) == ok


def test_clifford_yukawas_split_up_from_down_only_through_tau_r():
    """T-332(б, в): юкавы по уровням симметрии — 2, 4, 8 вещественных измерений; расщепление верх/низ даёт лишь τ_R.

    Пати–Салам (𝔠(L_{e_O}), 21): 2 = одна комплексная константа, m_u = m_d = m_ν = m_e. Лево-правая
    (𝔠(L,R), 15): 4 — кварки и лептоны порознь, но |m_u| = |m_d|, |m_ν| = |m_e|. 𝔤_SM (12): 8 —
    ровно span{1, ω}⊗{1, B−L}⊗{1, τ_R}·γ(h), четыре независимые массы. Вещественный вакуум в плоскости
    нейтральных направлений {iL_{e_O}, γ₁₀} при любой SU(2)_R-инвариантной юкаве масс не расщепляет;
    изотропные векторы её комплексификации γ₁₀ ± ω·iL_{e_O} дают массы только верхним (соотв. нижним).
    """
    f = _yukawa_frame()
    e = f["e"]
    plane = e["g10"][6:10]
    rng = np.random.default_rng(5)
    dims, gaps = {}, []
    for name, alg in (("PS", f["PS"]), ("LR", f["LR"]), ("SM", e["sm"])):
        N, to_ops = _yukawa_space(alg)
        dims[name] = N.shape[1]
        for _ in range(3):
            Ms = to_ops(N @ rng.normal(size=N.shape[1]))
            h = np.array([rng.normal(), 0.0, 0.0, rng.normal()])                     # нейтральная плоскость
            m = _yukawa_masses(sum(h[i] * Ms[i] for i in range(4)))
            if name in ("PS", "LR"):
                assert abs(m["u"] - m["d"]) < 1e-9 and abs(m["nu"] - m["e"]) < 1e-9
            if name == "PS":
                assert abs(m["u"] - m["e"]) < 1e-9
            if name == "SM":
                gaps.append(min(abs(m["u"] - m["d"]), abs(m["nu"] - m["e"])))
        if name == "SM":
            tauR = e["PR"] @ f["tau"] @ e["PR"]
            ops = [[T @ B @ D @ e["PR"] @ g @ e["PL"] for g in plane]
                   for D in (np.eye(32), e["om"]) for B in (np.eye(32), e["BL"]) for T in (np.eye(32), tauR)]
            vec = np.array([np.concatenate([(f["UR"].T @ M[a] @ f["UL"]).flatten() for a in range(4)]) for M in ops]).T
            assert np.linalg.matrix_rank(vec, tol=1e-9) == 8 and np.linalg.norm(N @ (N.T @ vec) - vec) < 1e-9
    assert dims == {"PS": 2, "LR": 4, "SM": 8} and max(gaps) > 1e-2
    g10, om = e["g10"], e["om"]
    for th in np.linspace(0, np.pi, 5):
        m = _yukawa_masses(np.cos(th) * g10[9] + np.sin(th) * g10[6])
        assert np.allclose(list(m.values()), 1.0)
    mu, md = _yukawa_masses(g10[9] + om @ g10[6]), _yukawa_masses(g10[9] - om @ g10[6])
    assert np.isclose(mu["u"], 2) and np.isclose(mu["nu"], 2) and mu["d"] < 1e-12 and mu["e"] < 1e-12
    assert np.isclose(md["d"], 2) and np.isclose(md["e"], 2) and md["u"] < 1e-12 and md["nu"] < 1e-12


def test_clock_phase_and_gap_vacuum_dressings_do_not_fit_the_masses():
    """T-332(г, д): фазы часов не расщепляют модули; заселённость вакуума даёт m_τ ≥ 0,46·m_кварк.

    Унитарные «одевания» exp(φ i), exp(φ L_{e_O}), exp(φ ω), exp(φ(B−L)) сохраняют |m_u| = |m_d|: фаза
    Пейджа–Вуттерса меняет лишь аргументы масс. Юкава, взвешенная заселённостями левых компонент
    в вакууме T-64 (u: вес P_𝟑̄, d: вес P_𝟑, ν и e: a/2 каждой, так как e_O — половина ν и половина e),
    даёт на 99 точках фазы Gap отношение лептон/тяжёлый кварк от 0,46 до 0,95 (данные: m_τ/m_t = 0,022
    при 2·10¹⁶ ГэВ) и m_ν = m_e; на ветви ранга 4 при λ₄ = 0 оно ≥ 1/2 аналитически.
    """
    f = _yukawa_frame()
    e = f["e"]
    M0 = e["g10"][9]
    for gen in (e["I1"], f["L1"], e["om"], e["BL"]):
        for phi in (0.3, 1.1):
            U = expm(phi * gen)
            m = _yukawa_masses(U @ M0 @ U)
            assert abs(m["u"] - m["d"]) < 1e-9 and abs(m["nu"] - m["e"]) < 1e-9
    ratios, split = [], []
    for l4 in (0.0, 1.0, 30.0):
        for kap in np.geomspace(0.05, 3.0, 40):
            _, (s, dd) = _family_min(kap, l4)
            if abs(dd) < 1e-9:
                continue
            b, c = (s + dd) / 2, (s - dd) / 2
            a = 1 - 3 * s
            ratios.append((a / 2) / max(b, c))
            split.append(min(b, c) / max(b, c))
    assert len(ratios) >= 90
    assert 0.46 < min(ratios) and max(ratios) < 0.96
    for kap in (0.1, 0.5, 2.0):                                                    # ветвь ранга 4, λ₄ = 0
        s = 0.25 - 1 / (384 * kap)
        assert (1 - 3 * s) / 2 / s >= 0.5


def test_the_data_ask_for_an_up_projector_at_one_percent():
    """T-332(е): однопетлевой бег СМ от M_Z; t/b ≈ 55 при M_Z и ≈ 68 при 2·10¹⁶ ГэВ; b/τ ≈ 0,66.

    Входы: m_t(m_t) = 162,5 ГэВ, m_b(m_b) = 4,18 ГэВ (MS-bar, однопетлевая КХД до M_Z), m_τ = 1,777 ГэВ,
    α_s(M_Z) = 0,118. Клиффордовы соотношения m_t = m_b и m_b = m_τ расходятся с данными в 68 раз и
    на 34 %; коэффициент τ_R, нужный данным, β/α = (y_t − y_b)/(y_t + y_b) = 0,971: юкава — проекция на
    i = L_{e_O} с точностью 1,5 %. Тогда y_ν^D = y_t и сизо M_R = m_D²/0,05 эВ ≈ 1,2–1,4·10¹⁴ ГэВ.
    """
    from scipy.integrate import solve_ivp
    MZ, v, a0 = 91.1876, 246.22, 0.1180
    a_s = lambda mu: a0 / (1 + a0 * (23 / 3) / (2 * np.pi) * np.log(mu / MZ))
    mt = 162.5 * (a_s(MZ) / a_s(162.5)) ** (12 / 23)
    mb = 4.18 * (a_s(MZ) / a_s(4.18)) ** (12 / 23)
    assert 54 < mt / mb < 56

    def rhs(t, s):
        g1, g2, g3, yt, yb, yl = s
        k = 1 / (16 * np.pi ** 2)
        return [k * 4.1 * g1 ** 3, -k * 19 / 6 * g2 ** 3, -k * 7 * g3 ** 3,
                k * yt * (4.5 * yt ** 2 + 1.5 * yb ** 2 + yl ** 2 - 8 * g3 ** 2 - 2.25 * g2 ** 2 - 0.85 * g1 ** 2),
                k * yb * (1.5 * yt ** 2 + 4.5 * yb ** 2 + yl ** 2 - 8 * g3 ** 2 - 2.25 * g2 ** 2 - 0.25 * g1 ** 2),
                k * yl * (3 * yt ** 2 + 3 * yb ** 2 + 2.5 * yl ** 2 - 2.25 * g2 ** 2 - 2.25 * g1 ** 2)]
    s0 = [np.sqrt(5 / 3) * 0.3574, 0.6517, np.sqrt(4 * np.pi * a0)] + [np.sqrt(2) * m / v for m in (mt, mb, 1.77693)]
    out = {}
    for mu in (1e14, 2e16):
        yt, yb, yl = solve_ivp(rhs, (0, np.log(mu / MZ)), s0, rtol=1e-10).y[3:, -1]
        out[mu] = (yt, yb, yl)
    yt, yb, yl = out[2e16]
    assert 66 < yt / yb < 71 and 0.63 < yb / yl < 0.68
    assert 0.965 < (yt - yb) / (yt + yb) < 0.975
    for mu in out:
        MR = (out[mu][0] * v / np.sqrt(2)) ** 2 / 0.050e-9
        assert 1.0e14 < MR < 1.5e14


def _vacuum_antiunitary_lifts():
    """PT = J на 𝒮; g_v — автоморфизм 𝕆 порядка 2, тождественный на кватернионной линии без e_O."""
    e = _spin10_completion()
    d = e["d"]
    gv = None
    for i, j in itertools.combinations(range(1, 7), 2):
        k = int(np.argmax(np.abs(omul(unit(i), unit(j)))))
        if k in (0, 7):
            continue
        D = -np.eye(8)
        D[0, 0] = D[i, i] = D[j, j] = D[k, k] = 1
        if all(np.allclose(D @ omul(unit(p), unit(q)), omul(D @ unit(p), D @ unit(q))) for p in range(8) for q in range(8)):
            gv = D
            break
    Th = d["cl"](gv) @ d["conj"]
    Kp = np.kron(np.eye(16), np.diag([1.0, -1.0]))
    lift = e["lift"]
    return e, gv, Th, {"Theta1": lift(Th), "ThetaK": lift(Th) @ Kp, "J1": lift(d["conj"]), "JK": lift(d["conj"]) @ Kp}


def test_vacuum_antiunitary_lifts_are_gauge_parity_or_cp():
    """T-333(а): поднятия PT и Θ_v = g_v∘PT на 𝒮_ℂ — калибровочный элемент, L↔R-обмен, P-тип или CP-тип.

    PT на ℂ⁷ — сопряжение J, то есть образующая γ₈. Θ_v сохраняет вакуум Γ_v, PT — нет. ℂ′-линейные
    поднятия J⊗1 и Θ_v⊗1 лежат в Spin(10) (сопряжение ими — поворот ℝ¹⁰ с det +1) и коммутируют с ω:
    это унитарные внутренние преобразования 𝟏𝟔, θ-член они не меняют. J⊗1 сохраняет половины;
    Θ_v⊗1 их переставляет, переводит 𝔰𝔲(2)_L в 𝔰𝔲(2)_R и оставляет γ₁₀ и iL_{e_O} на месте.
    Антилинейные поднятия: J⊗K′ переставляет половины (P-тип), Θ_v⊗K′ сохраняет их и нормализует
    𝔤_SM (CP-тип), оставляя iL_{e_O} и обращая γ₁₀. Любое из переставляющих вместе с 𝔤_SM порождает
    лево-правую алгебру (размерность 15).
    """
    e, gv, Th, lifts = _vacuum_antiunitary_lifts()
    assert gv is not None and gv[7, 7] == -1
    M = np.zeros((8, 8), complex)
    M[1:, 1:] = _colour_family(0.4, 0.2, 0.0)
    Mr = np.block([[M.real, -M.imag], [M.imag, M.real]])
    J = e["d"]["conj"]
    assert np.allclose(Th @ Mr @ np.linalg.inv(Th), Mr) and not np.allclose(J @ Mr @ J, Mr)
    om, om4 = e["om"], e["om4"]
    G = np.array([g.flatten() for g in e["g10"]]).T

    def rot(T):
        Ti = np.linalg.inv(T)
        R = np.zeros((10, 10))
        for a, g in enumerate(e["g10"]):
            v = (T @ g @ Ti).flatten()
            c = np.linalg.lstsq(G, v, rcond=None)[0]
            assert np.linalg.norm(G @ c - v) < 1e-9
            R[:, a] = c
        return R
    want = {"J1": (1, 1), "Theta1": (1, -1), "JK": (-1, -1), "ThetaK": (-1, 1)}
    for name, T in lifts.items():
        lin = 1 if np.allclose(T @ om, om @ T) else (-1 if np.allclose(T @ om, -om @ T) else 0)
        half = 1 if np.allclose(T @ om4, om4 @ T) else (-1 if np.allclose(T @ om4, -om4 @ T) else 0)
        assert (lin, half) == want[name]
        R = rot(T)
        assert np.allclose(R @ R.T, np.eye(10)) and np.isclose(np.linalg.det(R), lin)
        if name == "Theta1":
            assert np.isclose(R[9, 9], 1) and np.isclose(R[6, 6], 1)
        if name == "ThetaK":
            assert np.isclose(R[6, 6], 1) and np.isclose(R[9, 9], -1)
    Ti = np.linalg.inv(lifts["ThetaK"])
    assert max(_span_residual(lifts["ThetaK"] @ x @ Ti, e["sm"]) for x in e["sm"]) < 1e-9
    for name in ("Theta1", "JK"):
        T = lifts[name]
        Ti = np.linalg.inv(T)
        assert max(_span_residual(T @ x @ Ti, e["suR"]) for x in e["suL"]) < 1e-9
        ops = list(e["sm"]) + [T @ x @ Ti for x in e["sm"]]
        basis = []
        for X in ops:
            if not basis or _span_residual(X, basis) > 1e-8:
                basis.append(X)
        grew = True
        while grew:
            grew = False
            for A in list(basis):
                for B in list(basis):
                    Z = A @ B - B @ A
                    if _span_residual(Z, basis) > 1e-8:
                        basis.append(Z)
                        grew = True
        assert len(basis) == 15


def test_an_unbroken_cp_or_lr_symmetry_contradicts_the_quark_data():
    """T-333(б, в): ненарушенная CP кварковых юкав даёт J = 0; L↔R-симметрия при одном дублете — |m_u| = |m_d|.

    Обобщённая CP, Y = U Y* U^T для обоих секторов (U унитарна и симметрична), обнуляет инвариант
    Ярлскога — при J_данные = 3,12·10⁻⁵ (PDG 2024). Эрмитовы юкавы (чётность при двух дублетах с вещественными
    вакуумами) дают вещественный det M_uM_d, т. е. θ̄ = 0, и J ≠ 0 — этот путь требует второго дублета.
    """
    rng = np.random.default_rng(13)

    def jarlskog(Yu, Yd):
        _, Uu = np.linalg.eigh(Yu @ Yu.conj().T)
        _, Ud = np.linalg.eigh(Yd @ Yd.conj().T)
        V = Uu.conj().T @ Ud
        return float(np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1])))
    cmat = lambda: rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    for _ in range(20):
        W = np.linalg.qr(cmat())[0]
        U = W @ W.T
        Yu, Yd = cmat(), cmat()
        Yu, Yd = (Yu + U @ Yu.conj() @ U.T) / 2, (Yd + U @ Yd.conj() @ U.T) / 2
        assert abs(jarlskog(Yu, Yd)) < 1e-12
        Hu, Hd = cmat(), cmat()
        Hu, Hd = Hu + Hu.conj().T, Hd + Hd.conj().T
        assert abs(np.imag(np.linalg.det(Hu @ Hd))) < 1e-9 * abs(np.linalg.det(Hu @ Hd))
    assert max(abs(jarlskog(*(lambda A, B: (A + A.conj().T, B + B.conj().T))(cmat(), cmat()))) for _ in range(20)) > 1e-3
    J_data = 3.12e-5                                                            # PDG 2024, (3,12 +0,13 −0,12)·10⁻⁵
    assert J_data > 1e-6
    f = _yukawa_frame()
    N, to_ops = _yukawa_space(f["LR"], seed=3)
    Ms = to_ops(N @ rng.normal(size=N.shape[1]))
    m = _yukawa_masses(0.8 * Ms[0] + 0.6 * Ms[3])
    assert abs(m["u"] - m["d"]) < 1e-9

def test_phi_at_least_one_is_not_the_consciousness_verdict():
    """Fundamental closures section 9 (retracted line "Phi >= 1 iff conscious"): on the
    uniform family Gamma = I/7 + m(J - I) the state with Phi = 3 has P = 4/7 > 3/7 and
    R = 1/4 < 1/3, so Phi >= 1 holds while Cons fails (the too-pure exit)."""
    import numpy as np
    m = np.sqrt(3 / 294)
    G = np.eye(7) / 7 + m * (np.ones((7, 7)) - np.eye(7))
    assert np.min(np.linalg.eigvalsh(G)) > 0 and abs(np.trace(G) - 1) < 1e-12
    diag2 = np.sum(np.diag(G) ** 2)
    Phi = (np.sum(np.abs(G) ** 2) - diag2) / diag2
    P = np.real(np.trace(G @ G))
    R = 1 / (7 * P)
    assert abs(Phi - 3) < 1e-12 and abs(P - 4 / 7) < 1e-12 and abs(R - 1 / 4) < 1e-12
    cons = (P > 2 / 7) and (R >= 1 / 3) and (Phi >= 1)
    assert Phi >= 1 and not cons


def test_verdict_concordance_is_judged_by_kappa_not_by_raw_agreement():
    """PCI bridge in the concordance form (P8.4, SUB-5): the same raw agreement 34/40 = 85 %
    gives Cohen's kappa 0.699 (inconclusive, between 0.4 and 0.8) with balanced verdicts and
    0.167 (falsifying, below 0.4) with skewed ones. Illustrative counts, not data."""
    def kappa(a, b, c, d):                                   # a: both Cons, d: both not, b, c: disagreements
        n = a + b + c + d
        po = (a + d) / n
        pe = ((a + b) * (a + c) + (c + d) * (b + d)) / n ** 2
        return (po - pe) / (1 - pe)
    k1, k2 = kappa(18, 3, 3, 16), kappa(33, 3, 3, 1)
    assert abs((18 + 16) / 40 - 0.85) < 1e-12 and abs((33 + 1) / 40 - 0.85) < 1e-12
    assert abs(k1 - 0.34875 / 0.49875) < 1e-12 and 0.4 < k1 < 0.8
    assert abs(k2 - 0.03 / 0.18) < 1e-12 and k2 < 0.4


def test_two_point_pci_calibration_coincides_with_any_anchor():
    """Measurement section 6.3 (withdrawn): the line through (0, 1/7) and (c, 2/7) returns
    P = 2/7 at PCI = c for every anchor c, so "the thresholds coincide" was put in by hand."""
    for c in (0.20, 0.25, 0.31, 0.40, 0.55):
        a, b = (2 / 7 - 1 / 7) / c, 1 / 7
        assert abs(a * c + b - 2 / 7) < 1e-15
    assert abs((2 / 7 - 1 / 7) / 0.31 - 0.461) < 1e-3


def test_phystheory_forgets_to_topoi_unfaithfully_and_composes_associatively():
    """T-211 (corrected): PhysTheory as the Grothendieck construction of E -> Alg(E) over topoi.
    Finite 1-truncated model: base = finite sets and maps (the discrete topoi Set^X), fibre over X
    = families of monoids, a morphism (f, alpha) has alpha_x: M_x -> N_f(x). Composition
    (g, beta) o (f, alpha) = (g f, beta_f(x) alpha_x) is associative and unital, and the forgetful
    functor is not faithful: over the identity of a point there are two endomorphisms of the
    multiplicative monoid {0, 1}; on (C, *) complex conjugation is a second endomorphism."""
    import itertools
    import random
    mult = ((0, 1), (0, 1), lambda x, y: x * y, 1)           # carrier, carrier, product, unit
    add2 = ((0, 1), (0, 1), lambda x, y: (x + y) % 2, 0)
    triv = ((0,), (0,), lambda x, y: 0, 0)
    monoids = [mult, add2, triv]

    def homs(M, N):
        out = []
        for img in itertools.product(N[0], repeat=len(M[0])):
            h = dict(zip(M[0], img))
            if h[M[3]] != N[3]:
                continue
            if all(h[M[2](x, y)] == N[2](h[x], h[y]) for x in M[0] for y in M[0]):
                out.append(h)
        return out
    assert len(homs(mult, mult)) == 2                         # id and x -> 1: not faithful over id
    assert len(homs(add2, add2)) == 2 and len(homs(triv, mult)) == 1

    rng = random.Random(5)

    def obj():
        n = rng.choice([1, 2])
        return tuple(rng.choice(monoids) for _ in range(n))

    def mor(A, B):
        f = tuple(rng.randrange(len(B)) for _ in range(len(A)))
        alpha = []
        for x, M in enumerate(A):
            hs = homs(M, B[f[x]])
            alpha.append(rng.choice(hs))
        return f, alpha

    def comp(second, first):
        (g, beta), (f, alpha) = second, first
        return (tuple(g[f[x]] for x in range(len(f))),
                [{k: beta[f[x]][v] for k, v in alpha[x].items()} for x in range(len(f))])
    for _ in range(300):
        A, B, C, D = obj(), obj(), obj(), obj()
        u, v, w = mor(A, B), mor(B, C), mor(C, D)
        assert comp(w, comp(v, u)) == comp(comp(w, v), u)
        ident = (tuple(range(len(A))), [{k: k for k in M[0]} for M in A])
        assert comp(u, ident) == u
    zs = [complex(rng.uniform(-2, 2), rng.uniform(-2, 2)) for _ in range(50)]
    assert all(abs((z * w).conjugate() - z.conjugate() * w.conjugate()) < 1e-12 for z in zs for w in zs)
    assert (1 + 0j).conjugate() == 1 and any(z.conjugate() != z for z in zs)



def _random_plane(rng, n, k=2):
    """Ортонормированный базис случайного k-мерного подпространства ℂⁿ (столбцы)."""
    Z = rng.normal(size=(n, k)) + 1j * rng.normal(size=(n, k))
    return np.linalg.qr(Z)[0]


def test_two_level_systems_of_uhm_are_qubits_and_can_be_entangled():
    """Теорема 48e(a)–(b): двухуровневая система УГМ — грань D(ℂ^N) ранга 2, шар Блоха трёхмерен, (ММ) выполнено.

    (a) Грань D(V) ⊂ D(ℂ⁷) и ⊂ D(ℂ⁴⁹) для случайной плоскости V (dim V = 2): аффинная оболочка
    трёхмерна, ρ(r) = (P + r·σ_V)/2 ≥ 0 ⟺ |r| ≤ 1 — шар B³; её порядковое пространство Herm(V) несёт
    det сигнатуры (1,3). Грань D(ℂ³) — не шар: у неё есть граничная точка (ранга 2), не крайняя.
    Шары Блоха h₂(𝕂) имеют размерности dim 𝕂 + 1 = 2, 3, 5, 9; среди граней D(ℂ^N) шары — только
    точки и B³, так что h₂(𝕂) с 𝕂 ∋ e_O — грань голономного регистра лишь при 𝕂 = ℂ_O.
    (b) Для двух граней ранга 2 в ℂ⁷⊗ℂ⁷ составная грань D(V₁⊗V₂) — два кубита: локальная томография
    (16 = 4·4), белловское состояние внутри грани имеет отрицательную частичную транспозицию (−1/2),
    обратимая динамика грани exp(−itσ_x⊗σ_x) переводит произведение в запутанное состояние.
    """
    rng = np.random.default_rng(345)
    pauli = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.diag([1.0, -1.0]).astype(complex)]
    for n in (7, 49):
        V = _random_plane(rng, n)
        P = V @ V.conj().T
        sig = [V @ s @ V.conj().T for s in pauli]
        herm = [P] + sig
        assert np.linalg.matrix_rank(np.array([h.flatten() for h in herm]), tol=1e-9) == 4
        for _ in range(40):
            r = rng.normal(size=3)
            r *= rng.uniform(0, 2) / np.linalg.norm(r)
            rho = (P + sum(c * s for c, s in zip(r, sig))) / 2
            lam = np.linalg.eigvalsh(rho).min()
            assert (lam >= -1e-12) == (np.linalg.norm(r) <= 1 + 1e-12)
    for t, x in ((rng.normal(), rng.normal(size=3)) for _ in range(5)):
        assert abs(np.linalg.det(t * np.eye(2) + sum(c * s for c, s in zip(x, pauli))).real - (t * t - x @ x)) < 1e-12
    mid = np.diag([0.5, 0.5, 0.0])                                                 # D(ℂ³) — не шар
    a, b = np.diag([0.7, 0.3, 0.0]), np.diag([0.3, 0.7, 0.0])
    assert np.isclose(np.linalg.eigvalsh(mid).min(), 0) and np.allclose((a + b) / 2, mid) and not np.allclose(a, b)
    assert [k + 1 for k in (1, 2, 4, 8)] == [2, 3, 5, 9] and [k for k in (1, 2, 4, 8) if k + 1 in (0, 3)] == [2]
    V1, V2 = _random_plane(rng, 7), _random_plane(rng, 7)
    B = [np.kron(V1[:, i], V2[:, j]) for i in range(2) for j in range(2)]
    PP = sum(np.outer(v, v.conj()) for v in B)
    loc = [np.kron(x, y) for x in [V1 @ V1.conj().T] + [V1 @ s @ V1.conj().T for s in pauli]
           for y in [V2 @ V2.conj().T] + [V2 @ s @ V2.conj().T for s in pauli]]
    assert np.linalg.matrix_rank(np.array([m.flatten() for m in loc]), tol=1e-9) == 16   # локальная томография

    def pt_min(psi):
        R = np.outer(psi, psi.conj()).reshape(7, 7, 7, 7).transpose(0, 3, 2, 1).reshape(49, 49)
        return np.linalg.eigvalsh(R).min()
    bell = (B[0] + B[3]) / np.sqrt(2)
    assert np.isclose(pt_min(bell), -0.5) and np.allclose(PP @ bell, bell)
    Wb = np.array(B).T
    H = Wb @ np.kron(pauli[0], pauli[0]) @ Wb.conj().T
    U = expm(-1j * (np.pi / 4) * H)
    assert np.allclose(U @ PP, PP @ U) and pt_min(U @ B[0]) < -0.49                 # сплетающая обратимая динамика


def test_colour_fixed_two_level_faces_of_holon_registers():
    """Теорема 48e(c): цвет-неподвижных двухуровневых систем в регистрах голонома ровно две канонические.

    Цвет-неподвижное подпространство: в ℂ⁷ — одна прямая ℂe_O (грани ранга 2 нет); в 𝒮 = ℂ⊗𝕆 —
    плоскость span{η₀, e_O} (лептонная прямая T-326); в паре ℂ⁷⊗ℂ⁷ — трёхмерно: перестановка
    сомножителей даёт +1 дважды (e_O⊗e_O, Σ_{k≠O} e_k⊗e_k) и −1 один раз (Σ φ_{Ojk} e_j⊗e_k).
    Вращения Блоха лептонной грани (унитарные относительно i) не коммутируют с гиперзарядом T-326:
    с ним коммутирует ровно одна их образующая. Симметричную цвет-синглетную грань пары G₂ не сохраняет.
    """
    su3 = _su3_of_e_o()
    assert _nullspace(np.vstack(su3)).shape[0] == 1
    d = _sm_on_complex_octonions()
    cs = [d["cl"](np.pad(X, ((1, 0), (1, 0)))) for X in su3]
    fixed = _nullspace(np.vstack(cs))
    assert fixed.shape[0] == 4                                                     # вещественная 4 = комплексная 2
    face = [0, 7, 8, 15]                                                           # η₀, e_O и их i-кратные
    assert np.allclose(fixed[:, [k for k in range(16) if k not in face]], 0)
    pauli = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.diag([1.0, -1.0]).astype(complex)]

    def realify(A2):
        A = np.zeros((8, 8), complex)
        A[np.ix_([0, 7], [0, 7])] = A2
        return np.block([[A.real, -A.imag], [A.imag, A.real]])
    bloch = [realify(1j * s / 2) for s in pauli]
    assert all(np.allclose(b @ d["imul"], d["imul"] @ b) for b in bloch)
    assert all(np.allclose(b @ x, x @ b) for b in bloch for x in cs)
    Y = d["Y"]
    rows = np.array([(b @ Y - Y @ b).flatten() for b in bloch]).T
    assert np.linalg.matrix_rank(rows, tol=1e-9) == 2                              # с Y коммутирует одна ось из трёх
    pair = [np.kron(g, np.eye(7)) + np.kron(np.eye(7), g) for g in su3]
    F = _nullspace(np.vstack(pair))
    assert F.shape[0] == 3
    swap = np.eye(49)[[7 * (k % 7) + k // 7 for k in range(49)]]
    ev = np.sort(np.linalg.eigvalsh(F.conj() @ swap @ F.T).real)
    assert np.allclose(ev, [-1, 1, 1])
    eO = np.eye(7)[O_AXIS]
    sym = np.array([np.kron(eO, eO), sum(np.kron(np.eye(7)[k], np.eye(7)[k]) for k in range(7) if k != O_AXIS)])
    assert np.linalg.matrix_rank(np.vstack([F, sym]), tol=1e-9) == 3
    Ps = sym.T @ np.linalg.pinv(sym.T)
    g2p = [np.kron(g, np.eye(7)) + np.kron(np.eye(7), g) for g in G2]
    assert max(np.linalg.norm((np.eye(49) - Ps) @ g @ Ps) for g in g2p) > 0.1        # G₂ её не сохраняет


def _weyl_times_generation():
    """F = S ⊗_ℂ 𝒮_ℂ ⊂ S ⊗_ℝ 𝒮_ℂ: подпространство, где мнимая единица вейлевского S равна i′ из T-329."""
    e = _spin10_completion()
    IS = np.kron(np.eye(2), np.array([[0.0, -1.0], [1.0, 0.0]]))                   # мнимая единица S = ℂ_O² ≅ ℝ⁴

    def realify2(M):
        R = np.zeros((4, 4))
        for a in range(2):
            for b in range(2):
                z = M[a, b]
                R[2 * a:2 * a + 2, 2 * b:2 * b + 2] = [[z.real, -z.imag], [z.imag, z.real]]
        return R
    pauli = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.diag([1.0, -1.0]).astype(complex)]
    rot = [realify2(1j * s / 2) for s in pauli]
    boost = [realify2(s / 2) for s in pauli]
    Z = np.kron(IS, np.eye(32)) @ np.kron(np.eye(4), e["ip"])
    w, V = np.linalg.eigh((Z + Z.T) / 2)
    B = V[:, w < 0]                                                                # IS⊗1 = 1⊗i′  ⟺  (IS⊗i′) = −1
    res = lambda X: B.T @ X @ B
    return dict(e=e, IS=IS, B=B, res=res, rot=[res(np.kron(r, np.eye(32))) for r in rot],
                boost=[res(np.kron(b, np.eye(32))) for b in boost], unit=res(np.kron(IS, np.eye(32))),
                internal=lambda X: res(np.kron(np.eye(4), X)))


def test_no_rotation_of_the_internal_generation_commutes_with_the_gauge_group():
    """Теорема 48e(d): вращения, коммутирующие с G_SM, не действуют на 𝒮_ℂ — спинорный индекс отдельный сомножитель.

    Коммутант 𝔤_SM (T-329(в)) в End_ℝ(𝒮_ℂ) четырнадцатимерен (пять полей комплексного типа и ν^c,
    дважды тривиальное: 5·2 + 4); его пересечение с 𝔰𝔬(32) шестимерно и абелево — 𝔰𝔲(2) в нём нет.
    На ψ ∈ 𝒮 центр −1 ∈ SU(2)_L равен −1 на V_L и +1 на V_R: он не может быть поворотом на 2π,
    который у фермиона равен −1 на всех полях.
    """
    e = _spin10_completion()
    sm = e["sm"]
    so = []
    for i in range(32):
        for j in range(i + 1, 32):
            M = np.zeros((32, 32))
            M[i, j], M[j, i] = 1, -1
            so.append(M)
    G = sum((np.kron(X, np.eye(32)) - np.kron(np.eye(32), X.T)).T @ (np.kron(X, np.eye(32)) - np.kron(np.eye(32), X.T))
            for X in sm)
    assert int(np.sum(np.linalg.eigvalsh(G) < 1e-9)) == 14
    cs = [sum(v[k] * so[k] for k in range(len(so))) for v in _null_commutant(sm, so)]
    assert len(cs) == 6 and max(np.abs(a @ b - b @ a).max() for a in cs for b in cs) < 1e-12
    minus = expm(2 * np.pi * e["T3L"])
    assert np.allclose(minus @ e["PL"], -e["PL"]) and np.allclose(minus @ e["PR"], e["PR"])


def test_fermion_space_is_weyl_spinor_times_one_generation():
    """Теорема 48e(e): согласованная совместная структура 48c и T-326/T-329 — F = ℂ_O² ⊗_ℂ 𝒮_ℂ.

    F реализовано в S⊗_ℝ𝒮_ℂ (ℝ¹²⁸) как подпространство, где мнимая единица вейлевского S = ℂ_O² равна
    i′ поля T-329: вещественная размерность 64, комплексная 32. Отображение ψ⊗s ↦ проекция ψ⊗(s⊗1)
    из S⊗_ℝ𝒮 инъективно и сплетает 𝔰𝔭𝔦𝔫(9) и 𝔰𝔩(2,ℂ): S⊗_ℝ𝒮 ≅ S⊗_ℂ𝒮_ℂ. На F 𝔰𝔩(2,ℂ_O) (6) и
    𝔰𝔭𝔦𝔫(10) (45) коммутируют, их сумма точна (51), коммутант совместного действия — ℂ (2):
    F = (𝟐, 𝟏𝟔) неприводимо комплексного типа. Гиперзаряды на F — вдвое против 𝒮_ℂ: 16 вейлевских
    полей по 2 компоненты, у лептонного дублета 2·2 = 4. На F_L = F ∩ V_L мнимая единица вейлевского
    сомножителя действует как ±L_{e_O} (знак — ориентация γ₁₀), на F_R — как ∓L_{e_O}. Вращения
    пространства (𝔰𝔲(2) ⊂ 𝔰𝔩(2,ℂ_O)) коммутируют со всей 𝔰𝔭𝔦𝔫(10) и пересекаются с 𝔰𝔲(2)_L по нулю.
    """
    f = _weyl_times_generation()
    e, B, internal = f["e"], f["B"], f["internal"]
    assert B.shape[1] == 64
    unit = f["unit"]
    assert np.allclose(unit @ unit, -np.eye(64))
    d = e["d"]
    emb = np.array([np.kron(psi, np.kron(s, [1.0, 0.0])) for psi in np.eye(4) for s in np.eye(16)]).T
    Pemb = B.T @ emb
    assert np.linalg.matrix_rank(Pemb, tol=1e-9) == 64
    for X in d["spin9"][:6]:
        assert np.allclose(Pemb @ np.kron(np.eye(4), X), internal(e["lift"](X)) @ Pemb)
    spin10 = [internal(x) for x in e["spin10"]]
    lor = f["rot"] + f["boost"]
    assert max(np.abs(a @ b - b @ a).max() for a in lor for b in spin10) < 1e-12
    assert np.linalg.matrix_rank(np.array([x.flatten() for x in lor + spin10]), tol=1e-9) == 51
    rng = np.random.default_rng(3451)
    G = np.zeros((4096, 4096))
    for _ in range(3):
        X = sum(c * x for c, x in zip(rng.normal(size=51), lor + spin10))
        ad = np.kron(X, np.eye(64)) - np.kron(np.eye(64), X.T)
        G += ad.T @ ad
    assert int(np.sum(np.linalg.eigvalsh(G) < 1e-8)) == 2
    q = -internal(e["om"]) @ internal(e["Y"])
    vals, mult = np.unique(np.round(np.linalg.eigvalsh((q + q.T) / 2), 9), return_counts=True)
    cF = {float(v) + 0.0: int(m) // 2 for v, m in zip(vals, mult)}                  # комплексные кратности
    assert cF == {round(-2 / 3, 9): 6, -0.5: 4, 0.0: 2, round(1 / 6, 9): 12, round(1 / 3, 9): 6, 1.0: 2}
    assert sum(cF.values()) == 32
    PL, PR = internal(e["PL"]), internal(e["PR"])
    L1 = internal(e["lift"](d["Lu"]))
    sgn = 1 if np.allclose(e["om"], e["ip"]) else -1
    assert np.allclose(PL @ unit @ PL, sgn * PL @ L1 @ PL) and np.allclose(PR @ unit @ PR, -sgn * PR @ L1 @ PR)
    suL = [internal(x) for x in e["suL"]]
    assert np.linalg.matrix_rank(np.array([x.flatten() for x in f["rot"] + suL]), tol=1e-9) == 6
    assert max(np.abs(a @ b - b @ a).max() for a in f["rot"] for b in suL) < 1e-12


# ── (ВУ) доказано; κ и фазовая картина сектора (25.09.2026, вторая волна) ──────────────────

def _cal_a3(X, Y, Z):
    """Симметричная трилинейная форма 𝒜(X, Y, Z), 𝒜(R, R, R) = 𝒜(R)."""
    A = _assoc4()
    return float(np.real(np.einsum('ijkl,ia,jb,kc,abcl->', A, X, Y, Z, A, optimize=True)))


def _twirl_real(R, v=O_AXIS):
    """𝒯_ŵ на вещественных симметричных: проекция на span{ŵŵᵀ, P}."""
    e = np.eye(7)[v]
    r = float(e @ R @ e)
    return r * np.outer(e, e) + (np.trace(R) - r) / 6 * (np.eye(7) - np.outer(e, e))


def _q_twirl(u, Y):
    """Q_u(Y) = −2𝒜(𝒯(uuᵀ), Y, Y) − 𝒜(uuᵀ, Y, Y)."""
    uu = np.outer(u, u)
    return -2 * _cal_a3(_twirl_real(uu), Y, Y) - _cal_a3(uu, Y, Y)


def test_real_twirl_inequality_is_a_sum_of_positive_forms():
    """Лемма 3 (ВУ) [Т]: 8rt² + (16/9)t³ − 𝒜(R) = Σ_m p_m Q_{u_m}(R − 𝒯R), и Q_u ≥ 0 на W (26 измерений).

    Спектр Q_u при u = c·ŵ + s·d (метрика Фробениуса): 16s²/3 десять раз и корни
    9λ² − (216c² + 96s²)λ + 768c²s² + 160s⁴ (раз), 9λ² − (216c² + 144s²)λ + 2016c²s² + 368s⁴ (четыре),
    9λ² − (216c² + 144s²)λ + 2304c²s² + 320s⁴ (три). При s = 0: 0 восемнадцать раз и 24 восемь.
    """
    rng = np.random.default_rng(377)
    e = np.eye(7)[O_AXIS]
    for _ in range(40):
        k = rng.integers(1, 8)
        W = rng.normal(size=(7, k))
        R = W @ W.T / np.trace(W @ W.T)
        r = R[O_AXIS, O_AXIS]
        p, U = np.linalg.eigh(R)
        D = R - _twirl_real(R)
        rhs = sum(p[m] * _q_twirl(U[:, m], D) for m in range(7))
        assert abs(8 * r * (1 - r) ** 2 + 16 / 9 * (1 - r) ** 3 - _cal_a(R) - rhs) < 1e-12
    inv = [np.outer(e, e), (np.eye(7) - np.outer(e, e)) / np.sqrt(6)]
    Wb = []
    for i in range(7):
        for j in range(i, 7):
            F = np.zeros((7, 7))
            F[i, j] = F[j, i] = 1
            F = F - sum(np.sum(F * I) * I for I in inv)
            for G in Wb:
                F = F - np.sum(F * G) * G
            if np.linalg.norm(F) > 1e-9:
                Wb.append(F / np.linalg.norm(F))
    assert len(Wb) == 26
    d = np.eye(7)[0]
    for th in (0.0, 0.2, 0.7, 1.2, np.pi / 2):
        c, s = np.cos(th), np.sin(th)
        u = c * e + s * d
        K = np.array([[0.5 * (_q_twirl(u, A + B) - _q_twirl(u, A) - _q_twirl(u, B)) for B in Wb] for A in Wb])
        ev = np.linalg.eigvalsh(K)
        c2, s2 = c * c, s * s
        pred = [16 * s2 / 3] * 10
        for b1, b0, mult in ((216 * c2 + 96 * s2, 768 * c2 * s2 + 160 * s2 * s2, 1),
                             (216 * c2 + 144 * s2, 2016 * c2 * s2 + 368 * s2 * s2, 4),
                             (216 * c2 + 144 * s2, 2304 * c2 * s2 + 320 * s2 * s2, 3)):
            disc = b1 * b1 - 36 * b0
            assert disc >= 0 and b0 >= 0
            pred += [(b1 - np.sqrt(disc)) / 18, (b1 + np.sqrt(disc)) / 18] * mult
        assert np.max(np.abs(np.sort(ev) - np.sort(pred))) < 1e-10 and ev.min() > -1e-12
        assert (ev.min() > 1e-3) == (s > 1e-9)
    assert sum(abs(x) < 1e-9 for x in ev) == 0
    K0 = np.array([[0.5 * (_q_twirl(e, A + B) - _q_twirl(e, A) - _q_twirl(e, B)) for B in Wb] for A in Wb])
    ev0 = np.linalg.eigvalsh(K0)
    assert np.allclose(ev0, [0] * 18 + [24] * 8, atol=1e-10)


def test_colour_sector_transitions_and_the_bound_on_mean_coherence():
    """T-64(d, e, g) и следствие (ii): λ* = 12,93μ², κ₂(20μ²) = 0,1854μ²; ε̄ < (1/4 − μ²/384κ)/(2√5) < √5/40.

    Секторный потенциал f(s, x) = (3/2)x + (9/4)λ₄x² − κ[48s³ + 72(1−3s)(s² + x)], x = d² ∈ [0, s²], s ≤ 1/3.
    Ниже λ* переход один — первого рода в ранг 4; выше — непрерывный в ранг 7 при 7μ²/48 и скачок
    ранг 7 → ранг 4 при κ₂(λ₄).
    """
    from scipy.optimize import brentq, minimize_scalar
    S = np.linspace(0, 1 / 3, 20001)

    def sector_min(kap, lam):
        A = 72 * kap * (1 - 3 * S) - 1.5
        x = np.clip(A / (4.5 * lam), 0, S ** 2) if lam > 0 else np.where(A > 0, S ** 2, 0.0)
        f = 1.5 * x + 2.25 * lam * x * x - kap * (48 * S ** 3 + 72 * (1 - 3 * S) * (S ** 2 + x))
        i = int(np.argmin(f))
        return f[i], S[i], x[i]

    def f4min(kap, lam):
        g = lambda s: (1.5 - 144 * kap) * s * s + 384 * kap * s ** 3 + 2.25 * lam * s ** 4
        return minimize_scalar(g, bounds=(0, 1 / 3), method='bounded', options={'xatol': 1e-13}).fun

    lstar = brentq(lambda l: f4min(7 / 48, l) + 672 * (7 / 48) / 343, 5, 20, xtol=1e-10)
    assert abs(lstar - 12.93) < 5e-3
    for lam, k1 in ((0, 0.0787), (1, 0.0842), (5, 0.1054)):
        assert abs(brentq(lambda k: f4min(k, lam) + 672 * k / 343, 0.03, 0.146) - k1) < 5e-4
    _, s, x = sector_min(0.17, 20.0)                     # ранг 7: 0 < d² < s²
    assert 1e-4 < x < s * s - 1e-4
    _, s, x = sector_min(0.20, 20.0)                     # ранг 4: d² = s²
    assert abs(x - s * s) < 1e-12
    for kap, lam in itertools.product((0.08, 0.12, 0.2, 0.5, 2.0, 10.0), (0.0, 1.0, 13.0, 20.0, 100.0)):
        _, s, x = sector_min(kap, lam)
        eps = np.sqrt(x) / (2 * np.sqrt(5))
        assert eps <= max(0.0, 0.25 - 1 / (384 * kap)) / (2 * np.sqrt(5)) + 1e-4 and eps < np.sqrt(5) / 40


def test_derived_sources_give_no_associator_cubic():
    """T-331(e) [Т]: функции внедиагональных элементов и функции спектра не несут −κ𝒜 — κ = 0.

    Две диагональные координатные тройки (на линии Фано и вне) имеют один спектр и одни
    (нулевые) внедиагональные элементы, а 𝒜 на них — 0 и 24/27. Кубики G₂-ковариантного
    диссипатора не лежат в оболочке {1, TrΓ², TrΓ³, 𝒜}.
    """
    on, off = np.zeros((7, 7)), np.zeros((7, 7))
    on[[0, 1, 3], [0, 1, 3]] = 1 / 3
    off[[0, 1, 2], [0, 1, 2]] = 1 / 3
    assert abs(_cal_a(on)) < 1e-14 and abs(_cal_a(off) - 24 / 27) < 1e-12
    rng = np.random.default_rng(378)
    Aa = [PHI3[a] / np.sqrt(6) for a in range(7)]
    dg2 = lambda G: sum(A @ G @ A.T for A in Aa) - G
    Gs = [random_state(rng) for _ in range(60)]
    base = np.array([[1.0, np.trace(G @ G).real, np.trace(G @ G @ G).real, _cal_a(G)] for G in Gs])
    for f in (lambda G: np.trace(G @ G @ dg2(G)).real, lambda G: np.trace(G @ dg2(G) @ dg2(G)).real,
              lambda G: np.trace(dg2(G) @ dg2(G) @ dg2(G)).real):
        y = np.array([f(G) for G in Gs])
        coef = np.linalg.lstsq(base, y, rcond=None)[0]
        assert np.max(np.abs(base @ coef - y)) > 1e-3



def _anchor_window_parts(P, kap, c):
    """A(P) = ⅔ + κg(1 − kc), B(P) = κgR — коэффициенты уравнения когерентностей γ(A + iω) = B·a."""
    g = np.clip(7 * P - 2, 0, 1)
    R = 1 / (7 * P)
    return 2 / 3 + kap * g * (1 - (1 - R) * c), kap * g * R


def test_frame_covariance_modulo_gauge_fixes_the_collineation_anchor():
    """T-334: якорь φ_J выводится из (Eq) + наибольшей жизнеспособности с точностью до диагональной калибровки.

    Γ_oct = 2³·GL(3,2) — нерасщепимое расширение: из 168 коллинеаций перестановками без знаков в Γ_oct
    лежит 21 (группа 7:3), дополнения к знаковой подгруппе нет; орбита uu† под Γ_oct — 64 знаковые
    перефазировки D uu† D. Динамика без H ковариантна при всех 5040 перестановках и всех диагональных
    унитарных. Калибровочные инварианты (модули и потоки треугольников): на K₇ с однородными потоками по
    прямым и по непрямым треугольникам остаются лишь (0, 0) и (π, π) — семейство D((1−t)I/7 + t uu†)D†.
    При diag ρ_a = I/7 жизнь в окне зависит лишь от s = P(ρ_a) − 1/7 (как у t-семейства с t = √(7s/6)),
    κ_c строго убывает по t, порог t > (2 − c)/√6; чистота семейства (1 + 6t²)/7 — максимум при t = 1.
    """
    group = frame_group()
    mats = [np.rint(M).astype(int) for _, M in group]
    assert sum(bool(np.all(M >= 0)) for M in mats) == 21
    I7 = np.eye(7, dtype=int)
    key = lambda M: M.tobytes()
    signs = {key(np.rint(M).astype(int)) for p, M in group if p == tuple(range(7))}

    # Гашюц: расщепление над абелевой N равносильно расщеплению над прообразом силовской 2-подгруппы —
    # стабилизатора флага (точка 0 ⊂ прямая через неё), порядок 64; дополнение порядка 8 там ищется перебором.
    flag = next(l for l in ({x - 1 for x in l} for l in LINES) if 0 in l)
    syl = [np.rint(M).astype(int) for p, M in group if p[0] == 0 and {p[x] for x in flag} == flag]
    assert len(syl) == 64
    outside = [M for M in syl if key(M) not in signs]

    def closure(gens):
        S, front = {key(I7): I7}, [I7]
        while front:
            new = []
            for A in front:
                for g in gens:
                    B = A @ g
                    if key(B) not in S:
                        S[key(B)] = B
                        new.append(B)
            front = new
        return S

    assert not any(len(S) == 8 and len(signs & set(S)) == 1
                   for a in outside for b in outside for S in [closure([a, b])])        # нерасщепимо
    u = np.ones(7) / np.sqrt(7)
    orbit = set()
    for M in mats:
        v = np.rint(M @ u * np.sqrt(7)).astype(int)
        assert set(np.abs(v)) == {1}                                               # M u = D u, D = diag(±1)
        orbit.add(tuple(v) if v[0] > 0 else tuple(-v))
    assert len(orbit) == 64
    uu = np.outer(u, u).astype(complex)
    rng = np.random.default_rng(31)
    G = random_pure(rng) * 0.5 + np.eye(7) / 14
    Dph = np.diag(np.exp(1j * rng.uniform(0, 2 * np.pi, 7)))
    f = _living_generator(np.zeros((7, 7)), lambda X: uu, 40.0, 0.5)
    fD = _living_generator(np.zeros((7, 7)), lambda X: Dph @ uu @ Dph.conj().T, 40.0, 0.5)
    assert np.allclose(fD(Dph @ G @ Dph.conj().T), Dph @ f(G) @ Dph.conj().T, atol=1e-12)   # калибровка
    for p in itertools.islice(itertools.permutations(range(7)), 0, 5040, 97):
        Pm = np.eye(7)[list(p)]
        assert np.allclose(Pm @ uu @ Pm.T, uu) and np.allclose(f(Pm @ G @ Pm.T), Pm @ f(G) @ Pm.T, atol=1e-12)
    edges = [(i, j) for i in range(7) for j in range(i + 1, 7)]
    col = {e: n for n, e in enumerate(edges)}
    free = [col[e] for e in edges if e[0] != 0]
    S = np.ones((2 ** 15, 21), dtype=np.int8)
    S[:, free] = 1 - 2 * ((np.arange(2 ** 15)[:, None] >> np.arange(15)[None, :]) & 1)
    lines = {frozenset(x - 1 for x in l) for l in LINES}
    tri = list(itertools.combinations(range(7), 3))
    prod = np.stack([S[:, col[(a, b)]] * S[:, col[(b, c)]] * S[:, col[(a, c)]] for a, b, c in tri], axis=1)
    on = np.array([frozenset(t) in lines for t in tri])
    ok = (np.ptp(prod[:, on], axis=1) == 0) & (np.ptp(prod[:, ~on], axis=1) == 0)
    uniform = {(int(r[on][0]), int(r[~on][0])) for r in prod[ok]}
    assert uniform == {(1, 1), (-1, -1)}
    eta = np.linspace(1 / np.sqrt(6), 1 / np.sqrt(3), 4001)
    for alpha in (0.0, 0.5, 1.0):
        c = (1 - alpha) / 3
        ts = np.linspace((2 - c) / np.sqrt(6) + 0.01, 1, 30)
        kcs = [(2 / 3) / np.max(_q_window(eta, c, t)) for t in ts]
        assert all(np.diff(kcs) < 0)                                               # κ_c убывает по t
        assert all(np.max(np.diff(_q_window(eta, c, t), 2)) < 0 for t in np.linspace(0.01, 1, 12))   # Q_t вогнута
        assert np.max(_q_window(eta, c, (2 - c) / np.sqrt(6) - 1e-3)) <= 1e-12     # ниже порога жизни нет
    for t in (-1 / 6, 0.3, 1.0):
        rho = (1 - t) * np.eye(7) / 7 + t * uu
        assert abs(purity(rho) - (1 + 6 * t ** 2) / 7) < 1e-12
    # (Eq)-якорь общего вида с той же когерентной чистотой s живёт так же, как t-семейство
    alpha, kap, c = 0.5, 80.0, 0.5 / 3
    flat = [np.exp(1j * rng.uniform(0, 2 * np.pi, 7)) / np.sqrt(7) for _ in range(2)]
    anchor = 0.93 * np.outer(flat[0], flat[0].conj()) + 0.07 * np.outer(flat[1], flat[1].conj())
    assert np.allclose(np.diag(anchor).real, 1 / 7)
    s = purity(anchor) - 1 / 7
    tt = np.sqrt(7 * s / 6)
    v = kap * _q_window(eta, c, tt) - 2 / 3
    xi = [eta[i] for i in range(len(eta) - 1) if v[i] > 0 >= v[i + 1]][0]
    G = (1 - xi / tt) * np.eye(7) / 7 + (xi / tt) * anchor
    fa = _living_generator(np.zeros((7, 7)), lambda Y: anchor, kap, alpha)
    G = _stationary(fa, G)
    assert np.linalg.norm(fa(G)) < 1e-12 and abs(purity(G) - (1 + 6 * xi ** 2) / 7) < 1e-4


def test_constant_anchor_window_attractor_is_explicit():
    """T-335: при постоянном якоре стационар с P > 2/7 — (1 − η)diag ρ_a + ηρ_a, спектр якобиана точен.

    Скаляр η — корень h(η) = B(P) − ηA(P), P = d + η²s; спектр — {h′(η); −κgR ×6; −A ×41}.
    Три якоря при α = ½: возмущённый uu† (3 % случайного чистого состояния, κ = 50: P = 0,3185, Φ = 1,227),
    перефазированный D uu† D† (κ = 40, аттрактор — D Γ_η D†) и чистый с амплитудами 1 ± 0,3 (κ = 50: P = 0,3299,
    Φ = 1,148, диагональ 0,105–0,204) — все три стока в V_full. При диагональном H когерентности
    γ_ij = B a_ij/(A + iΔω_ij) точно; для φ_J при разбросе энергий ≤ Ω_c окно держится (Ω_c = 1,839 при κ = 40,
    α = ½; 4,201 при α = 0), сток с диагональю 1/7. H из span{I, J} любой нормы аттрактора не сдвигает.
    """
    alpha, kap = 0.5, 40.0
    c = (1 - alpha) / 3
    rng = np.random.default_rng(7)
    u = np.ones(7) / np.sqrt(7)
    uu = np.outer(u, u).astype(complex)
    Dph = np.diag(np.exp(1j * rng.uniform(0, 2 * np.pi, 7)))
    amp = 1 + 0.3 * rng.uniform(-1, 1, 7)
    psi = amp * np.exp(1j * rng.uniform(0, 2 * np.pi, 7))
    psi /= np.linalg.norm(psi)
    anchors = {"perturbed": (0.97 * uu + 0.03 * random_pure(rng), 50.0),
               "rephased": (Dph @ uu @ Dph.conj().T, 40.0),
               "uneven": (np.outer(psi, psi.conj()), 50.0)}
    eta = np.linspace(1e-4, 0.999, 200001)
    for name, (ra, kap) in anchors.items():
        dg = np.diag(np.diag(ra))
        d = float(np.sum(np.real(np.diag(ra)) ** 2))
        s = purity(ra) - d
        P = d + eta ** 2 * s
        A, B = _anchor_window_parts(P, kap, c)
        h = np.where(P > 2 / 7, B - eta * A, -1.0)
        roots = [i for i in range(len(eta) - 1) if h[i] > 0 >= h[i + 1]]
        assert len(roots) == 1
        e = eta[roots[0]]
        f = _living_generator(np.zeros((7, 7)), lambda X, ra=ra: ra, kap, alpha)
        G = _stationary(f, (1 - e) * dg + e * ra)
        e = float(np.real(np.vdot(ra - dg, G - dg)) / np.real(np.vdot(ra - dg, ra - dg)))
        assert np.linalg.norm(f(G)) < 1e-12 and np.linalg.norm(G - ((1 - e) * dg + e * ra)) < 1e-10
        Pst = purity(G)
        A0, B0 = _anchor_window_parts(Pst, kap, c)
        hp = lambda x: (lambda Pp: (lambda AB: AB[1] - x * AB[0])(_anchor_window_parts(Pp, kap, c)))(d + x * x * s)
        dh = (hp(e + 1e-7) - hp(e - 1e-7)) / 2e-7
        g, R = gate(Pst), 1 / (7 * Pst)
        want = sorted([dh] + [-kap * g * R] * 6 + [-A0] * 41)
        assert np.allclose(np.sort(np.linalg.eigvals(_jacobian(f, G)).real), want, atol=1e-5)
        assert dh < 0
        assert 2 / 7 < Pst <= 3 / 7 and integration(G) > 1 and np.all(np.real(np.diag(G)) > 0)
        if name == "rephased":
            Gs = Dph.conj().T @ G @ Dph
            assert np.allclose(np.diag(Gs).real, 1 / 7) and np.allclose(Gs - np.diag(np.diag(Gs)), e * (uu - np.diag(np.diag(uu))), atol=1e-10)
    kap = 40.0
    Pg = np.linspace(2 / 7 + 1e-7, 3 / 7, 100001)
    oc = {}
    for a, kk in ((0.5, 40.0), (0.0, 40.0), (0.5, 30.0), (0.5, 100.0)):
        A, B = _anchor_window_parts(Pg, kk, (1 - a) / 3)
        oc[(a, kk)] = np.sqrt(np.max((6 / 7) * B ** 2 / (Pg - 1 / 7) - A ** 2))
    assert abs(oc[(0.5, 40.0)] - 1.839) < 2e-3 and abs(oc[(0.0, 40.0)] - 4.201) < 2e-3
    assert abs(oc[(0.5, 30.0)] - 0.414) < 2e-3 and abs(oc[(0.5, 100.0)] - 7.614) < 2e-3
    w = rng.uniform(0, 1, 7)
    w = (w - w.min()) / (w.max() - w.min()) * 0.99 * oc[(0.5, 40.0)]
    H = np.diag(w).astype(complex)
    dw2 = (w[:, None] - w[None, :]) ** 2
    A, B = _anchor_window_parts(Pg, kap, c)
    G_P = np.array([np.sum(B[i] ** 2 / (A[i] ** 2 + dw2[~np.eye(7, dtype=bool)])) / 49 for i in range(0, len(Pg), 50)]) \
        - (Pg[::50] - 1 / 7)
    Pr = Pg[::50][[i for i in range(len(G_P) - 1) if G_P[i] > 0 >= G_P[i + 1]][0]]
    A1, B1 = _anchor_window_parts(Pr, kap, c)
    G0 = np.eye(7) / 7 + (B1 / 7) / (A1 + 1j * (w[:, None] - w[None, :])) * (1 - np.eye(7))
    f = _living_generator(H, lambda X: uu, kap, alpha)
    G = _stationary(f, G0)
    A2, B2 = _anchor_window_parts(purity(G), kap, c)
    exact = np.eye(7) / 7 + (B2 / 7) / (A2 + 1j * (w[:, None] - w[None, :])) * (1 - np.eye(7))
    assert np.linalg.norm(f(G)) < 1e-12 and np.linalg.norm(G - exact) < 1e-10
    assert 2 / 7 < purity(G) < 3 / 7 and np.allclose(np.diag(G).real, 1 / 7)
    assert np.max(np.linalg.eigvals(_jacobian(f, G)).real) < -4
    eta = np.linspace(1 / np.sqrt(6), 0.5, 20001)
    v = kap * _q_window(eta, c) - 2 / 3
    e = eta[[i for i in range(len(eta) - 1) if v[i] > 0 >= v[i + 1]][0]]
    Ge = np.eye(7) / 7 + e * (uu - np.eye(7) / 7)
    G0 = _stationary(_living_generator(np.zeros((7, 7)), lambda X: uu, kap, alpha), Ge)
    fJ = _living_generator(3.0 * np.eye(7) + 50.0 * np.ones((7, 7)), lambda X: uu, kap, alpha)
    assert np.linalg.norm(fJ(G0)) < 1e-11                                            # тот же сток при ‖H‖ = 353


def test_no_self_model_holds_the_window_below_the_rate_floor():
    """T-336: κ ≥ κ_floor(α) у всякой самомодели замещающей формы при любом H — 11,83 / 20,91 / 42,64.

    Из баланса чистоты: (⅔)P_coh = κg(f − P), f − P = R Tr(Γσ) − 1/7 − k(1 − c)P_coh, Tr(Γσ) ≤ λ_max(P),
    P_coh ≥ P/2 в V_full. При H = 0 порог 13,11 / 23,21 / 47,35 достигается постоянным чистым якорем с
    d = P/2 (аттрактор на Φ = 1). κ_c(φ_J)/κ_floor = 1,405 / 1,399 / 1,392. Неравенство баланса проверено
    на стоке φ_J со случайным H нормы 1.
    """
    P = np.linspace(2 / 7 + 1e-9, 3 / 7, 400001)
    g, R = 7 * P - 2, 1 / (7 * P)
    lmax = (1 + np.sqrt(6 * (7 * P - 1))) / 7
    floors, h0 = {}, {}
    for alpha in (0.0, 0.5, 1.0):
        c = (1 - alpha) / 3
        den = g * (R * lmax - 1 / 7 - (1 - R) * (1 - c) * P / 2)
        floors[alpha] = np.min(np.where(den > 0, (P / 3) / np.where(den > 0, den, 1), np.inf))
        et = np.sqrt(P / (2 - P))
        den0 = g * (R - et * (1 - c + c * R))
        h0[alpha] = np.min(np.where(den0 > 0, (2 / 3) * et / np.where(den0 > 0, den0, 1), np.inf))
    assert abs(floors[0.0] - 11.834) < 2e-3 and abs(floors[0.5] - 20.913) < 2e-3 and abs(floors[1.0] - 42.638) < 2e-3
    assert abs(h0[0.0] - 13.113) < 2e-3 and abs(h0[0.5] - 23.209) < 2e-3 and abs(h0[1.0] - 47.353) < 2e-3
    eta = np.linspace(1 / np.sqrt(6), 1 / np.sqrt(3), 40001)
    for alpha, want in ((0.0, 1.405), (0.5, 1.399), (1.0, 1.392)):
        kc = (2 / 3) / np.max(_q_window(eta, (1 - alpha) / 3))
        assert kc > h0[alpha] > floors[alpha] and abs(kc / floors[alpha] - want) < 2e-3
    # порог при H = 0 достигается: чистый якорь с |ψ_0|² = p, остальные равны, d = Σ|ψ_k|⁴
    alpha, c = 0.0, 1 / 3
    et = np.sqrt(P / (2 - P))
    den0 = g * (R - et * (1 - c + c * R))
    dstar = P[np.argmin(np.where(den0 > 0, (2 / 3) * et / np.where(den0 > 0, den0, 1), np.inf))] / 2
    from scipy.optimize import brentq
    p = brentq(lambda q: q ** 2 + (1 - q) ** 2 / 6 - dstar, 1 / 7, 0.9)
    psi = np.array([np.sqrt(p)] + [np.sqrt((1 - p) / 6)] * 6)
    ra = np.outer(psi, psi).astype(complex)
    for kap, alive in ((13.2, True), (12.9, False)):
        d, s = dstar, 1 - dstar
        et = np.linspace(1e-4, 0.999, 400001)
        Pe = d + et ** 2 * s
        A, B = _anchor_window_parts(Pe, kap, c)
        h = np.where(Pe > 2 / 7, B - et * A, -1.0)
        ok = (h >= 0) & (et ** 2 * s >= d) & (Pe <= 3 / 7)
        assert bool(ok.any()) == alive
    # баланс на стоке φ_J со случайным H
    alpha, kap, c = 0.5, 40.0, 0.5 / 3
    u = np.ones(7) / np.sqrt(7)
    uu = np.outer(u, u).astype(complex)
    rng = np.random.default_rng(3)
    Hm = rng.normal(size=(7, 7)) + 1j * rng.normal(size=(7, 7))
    Hm = (Hm + Hm.conj().T) / 2
    Hm /= np.linalg.norm(Hm, 2)
    f = _living_generator(Hm, lambda X: uu, kap, alpha)
    e = 0.4563
    G = _stationary(f, np.eye(7) / 7 + e * (uu - np.eye(7) / 7))
    Pg, Rg = purity(G), 1 / (7 * purity(G))
    pd = float(np.sum(np.real(np.diag(G)) ** 2))
    pc = Pg - pd
    fval = np.real(np.trace(G @ ((1 - Rg) * (np.diag(np.diag(G)) + c * (G - np.diag(np.diag(G)))) + Rg * uu)))
    assert abs((2 / 3) * pc - kap * gate(Pg) * (fval - Pg)) < 1e-10
    lm = np.max(np.linalg.eigvalsh(G))
    assert np.real(np.trace(G @ uu)) <= lm + 1e-12 <= (1 + np.sqrt(6 * (7 * Pg - 1))) / 7 + 1e-12
    assert pc >= Pg / 2 and kap >= floors[0.5]


def test_self_model_contraction_holds_only_for_constant_weight_and_unital_part():
    """Лемма 2.1 формализации φ: φ_k = kP + (1 − k)ρ_a сжимает с константой k по Фробениусу, если k и якорь
    постоянны, а P унитален (здесь P_α); у φ_J с k = 1 − 1/(7P) липшицева константа в базисном состоянии
    1,129 > 1. Неунитальный CPTP может растягивать расстояние Гильберта–Шмидта: X ↦ Tr₂X ⊗ |0⟩⟨0| на
    ℂ²⊗ℂ² — в √2 раз; смесь 0,9 этого канала со сбросом в |00⟩ имеет единственное инвариантное состояние
    и спектр в круге радиуса 0,9, но растягивает в 0,9√2 = 1,27 раза (теорема 3.3 в форме «тогда и только
    тогда» неверна).
    """
    u = np.ones(7) / np.sqrt(7)
    uu = np.outer(u, u).astype(complex)
    alpha, c = 0.5, 0.5 / 3

    def phi_j(G):
        P = purity(G)
        R = 1 / (7 * P)
        D = np.diag(np.diag(G))
        return (1 - R) * (D + c * (G - D)) + R * uu

    B = _jacobian_basis()
    e0 = np.zeros((7, 7), complex)
    e0[0, 0] = 1
    J = np.zeros((48, 48))
    for a, Ba in enumerate(B):
        dlt = (phi_j(e0 + 1e-6 * Ba) - phi_j(e0 - 1e-6 * Ba)) / 2e-6
        J[:, a] = np.real(np.einsum("bij,ji->b", B, dlt))
    assert abs(np.linalg.norm(J, 2) - 1.129) < 2e-3
    rng = np.random.default_rng(4)
    k = 0.8
    phik = lambda G: k * (np.diag(np.diag(G)) + c * (G - np.diag(np.diag(G)))) + (1 - k) * uu
    for _ in range(20):
        G1, G2 = random_pure(rng), random_pure(rng)
        assert np.linalg.norm(phik(G1) - phik(G2)) <= k * np.linalg.norm(G1 - G2) + 1e-12
    ket0 = np.diag([1.0, 0.0])
    X = np.kron(np.diag([1.0, -1.0]), np.eye(2) / 2)

    def tr2_reset(Y, p=1.0):
        T = Y.reshape(2, 2, 2, 2).trace(axis1=1, axis2=3)
        return p * np.kron(T, ket0) + (1 - p) * np.trace(Y) * np.kron(ket0, ket0)

    assert abs(np.linalg.norm(tr2_reset(X)) / np.linalg.norm(X) - np.sqrt(2)) < 1e-12
    M = np.array([tr2_reset(E.reshape(4, 4), 0.9).ravel() for E in np.eye(16)]).T
    ev = np.linalg.eigvals(M)
    assert np.sum(np.abs(ev - 1) < 1e-9) == 1 and np.sort(np.abs(ev))[-2] < 0.9 + 1e-9
    assert abs(np.linalg.norm(tr2_reset(X, 0.9)) / np.linalg.norm(X) - 0.9 * np.sqrt(2)) < 1e-12

def _embed_local(op, sites, M, d=7):
    """op on the ordered tuple `sites`, maximally mixed elsewhere, as an operator on (C^d)^M."""
    k = len(sites)
    rest = [s for s in range(M) if s not in sites]
    full = np.kron(op, np.eye(d ** (M - k)) / d ** (M - k))
    inv = list(np.argsort(list(sites) + rest))
    T = full.reshape([d] * (2 * M)).transpose(inv + [M + i for i in inv])
    return T.reshape(d ** M, d ** M)


def _marginal(G, keep, M, d=7):
    rest = [s for s in range(M) if s not in keep]
    order = list(keep) + rest
    k = len(keep)
    T = G.reshape([d] * (2 * M)).transpose(order + [M + s for s in order])
    return np.einsum("aibi->ab", T.reshape(d ** k, d ** (M - k), d ** k, d ** (M - k)))


def _ket(*idx, d=7):
    v = np.zeros(d ** len(idx))
    v[np.ravel_multi_index(idx, (d,) * len(idx))] = 1
    return v


def test_t174_a_int_corepresents_structures_and_the_old_receiving_map_fails():
    """T-174 (restated 2026-09-26). The multiplicity-free faithful representation of
    A_int = C + M3 + M3 on C^7 has commutant C^3 (orbit U(7)/U(1)^3, dim 46); unitary classes of unital
    *-homs A_int -> M_n are (a,b,c) with a+3b+3c = n, faithful classes exist iff n >= 7 and are unique iff
    n in {7,8,9} (n = 10: three). The tau-preserving conditional expectation E onto A_int is UCP, keeps the
    trace and is NOT multiplicative (the old 'Takesaki homomorphism'). A primitive Lindbladian on C^7 has
    Heisenberg fixed points C*1 only, so no faithful A_int-structure is dynamically fixed. The G2-orbit of a
    generic state is 14-dimensional inside the 48-dimensional D(C^7): geometric morphisms from the point to
    Sh(D(C^7)) (= points of D(C^7)) are not unique up to G2. Unital multiplicative maps det^k: M_7 -> A_int
    are pairwise distinct, so the monoid-typed receiving map is not essentially unique."""
    rng = np.random.default_rng(174)

    def iota(a0, A, B):
        M = np.zeros((7, 7), complex)
        M[0, 0], M[1:4, 1:4], M[4:7, 4:7] = a0, A, B
        return M
    Z3 = np.zeros((3, 3))
    gens = [iota(1, Z3, Z3)]
    for i in range(3):
        for j in range(3):
            Eij = np.zeros((3, 3))
            Eij[i, j] = 1
            gens += [iota(0, Eij, Z3), iota(0, Z3, Eij)]
    K = np.array([np.kron(np.eye(7), g) - np.kron(g.T, np.eye(7)) for g in gens]).reshape(-1, 49)
    assert 49 - np.linalg.matrix_rank(K) == 3                              # commutant C^3, orbit dim 46

    def faithful(n):
        return [(a, b, c) for a in range(1, n) for b in range(1, n) for c in range(1, n) if a + 3 * b + 3 * c == n]
    assert [len(faithful(n)) for n in range(1, 13)] == [0, 0, 0, 0, 0, 0, 1, 1, 1, 3, 3, 3]
    assert [n for n in range(1, 30) if (1, 1, 1) in faithful(n)] == [7]

    def E(a):
        return iota(a[0, 0], a[1:4, 1:4], a[4:7, 4:7])
    X = rng.normal(size=(7, 7)) + 1j * rng.normal(size=(7, 7))
    Y = rng.normal(size=(7, 7)) + 1j * rng.normal(size=(7, 7))
    b = iota(2.0, rng.normal(size=(3, 3)), rng.normal(size=(3, 3)))
    assert np.linalg.norm(E(b) - b) < 1e-12                                 # E o iota = id
    assert abs(np.trace(E(X) @ b) - np.trace(X @ b)) < 1e-10                # tau-preserving bimodule map
    assert np.linalg.norm(E(X @ Y) - E(X) @ E(Y)) > 1                       # not a homomorphism
    choi = sum(np.kron(np.outer(np.eye(7)[i], np.eye(7)[j]), E(np.outer(np.eye(7)[i], np.eye(7)[j])))
               for i in range(7) for j in range(7))
    assert np.linalg.eigvalsh(choi).min() > -1e-12                          # completely positive
    sx = np.array([[0, 1], [1, 0]])
    assert np.allclose(np.diag(np.diag(sx @ sx)), np.eye(2)) and np.allclose(np.diag(np.diag(sx)), 0)

    I7 = np.eye(7)
    H = rng.normal(size=(7, 7)) + 1j * rng.normal(size=(7, 7))
    H = H + H.conj().T
    S = -1j * (np.kron(I7, H) - np.kron(H.T, I7))
    for _ in range(2):
        L = rng.normal(size=(7, 7)) + 1j * rng.normal(size=(7, 7))
        LdL = L.conj().T @ L
        S = S + np.kron(L.conj(), L) - 0.5 * np.kron(I7, LdL) - 0.5 * np.kron(LdL.T, I7)
    assert np.sum(np.abs(np.linalg.eigvals(S)) < 1e-9) == 1                 # primitive: one stationary state
    sv = np.linalg.svd(S.conj().T, compute_uv=False)
    assert np.sum(sv < 1e-9) == 1
    assert np.linalg.norm(S.conj().T @ I7.reshape(-1, order="F")) < 1e-9     # Heisenberg fixed points = C*1
    Hs = np.diag(np.arange(7.0))                                            # simple spectrum: commutant diagonal
    offdiag = [g for g in gens if np.linalg.norm(g - np.diag(np.diag(g))) > 0]
    assert len(offdiag) == 12 and all(np.linalg.norm(Hs @ g - g @ Hs) > 0.5 for g in offdiag)
    Hsec = iota(0.3, 1.7 * np.eye(3), -0.4 * np.eye(3))
    assert all(np.linalg.norm(Hsec @ g - g @ Hsec) < 1e-12 for g in gens)

    rho = rng.normal(size=(7, 7)) + 1j * rng.normal(size=(7, 7))
    rho = rho @ rho.conj().T
    rho /= np.trace(rho)
    T = np.array([(g @ rho - rho @ g).ravel() for g in G2])
    assert np.linalg.matrix_rank(np.hstack([T.real, T.imag])) == 14 < 48

    A1, A2 = rng.normal(size=(7, 7)), rng.normal(size=(7, 7))
    for k in range(4):
        assert abs(np.linalg.det(A1 @ A2) ** k - np.linalg.det(A1) ** k * np.linalg.det(A2) ** k) < 1e-6 * (1 + abs(np.linalg.det(A1 @ A2)) ** k)
    z = np.exp(2j * np.pi / 3)
    D = np.diag([z] + [1] * 6)
    assert abs(np.linalg.det(D) ** 3 - 1) < 1e-12 and abs(np.linalg.det(D) ** 1 - 1) > 0.5


def test_t170_gap_phases_carry_no_g2_action_and_the_torus_quotient_is_not_an_orbifold():
    """T-170 (restated 2026-09-26). (i) The stabiliser of the associative 3-form in gl(7) is 14-dimensional
    and equals Der(O) = g2 (the group coincidence that survives). The former Lemma T-170'.1 fails: on
    R^21 = 14 + 7 the G2-orbit of (0, v) is 6-dimensional (stabiliser SU(3)) and of 0 is a point, so the
    quotient is not an orbifold; and the 21 Gap phases arg(Gamma_ij) are not moved by G2 as a function of
    themselves: two states with equal phases and different moduli get different phases under one g in G2."""
    rng = np.random.default_rng(170)
    cols = []
    for p in range(7):
        for q in range(7):
            Xm = np.zeros((7, 7))
            Xm[p, q] = 1
            dphi = (np.einsum("ai,ajk->ijk", Xm, PHI3) + np.einsum("aj,iak->ijk", Xm, PHI3)
                    + np.einsum("ak,ija->ijk", Xm, PHI3))
            cols.append(dphi.ravel())
    Mphi = np.array(cols).T
    stab = 49 - np.linalg.matrix_rank(Mphi)
    G2flat = np.array([g.ravel() for g in G2]).T
    assert stab == 14 and np.linalg.norm(Mphi @ G2flat) < 1e-10

    def orbit_dim(Xv, v):
        rows = [np.concatenate([(Yg @ Xv - Xv @ Yg).ravel(), Yg @ v]) for Yg in G2]
        return np.linalg.matrix_rank(np.array(rows), tol=1e-8)
    Xg = sum(rng.normal() * g for g in G2)
    v = rng.normal(size=7)
    assert orbit_dim(Xg, v) == 14 and orbit_dim(0 * Xg, v) == 6 and orbit_dim(0 * Xg, 0 * v) == 0

    g = expm(sum(rng.normal() * gg for gg in G2))
    assert np.linalg.norm(g @ g.T - np.eye(7)) < 1e-10
    Z = rng.normal(size=(7, 7)) + 1j * rng.normal(size=(7, 7))
    Ga = Z @ Z.conj().T
    mod = np.abs(rng.normal(size=(7, 7))) + 0.1
    mod = (mod + mod.T) / 2
    Gb = mod * np.exp(1j * np.angle(Ga))
    np.fill_diagonal(Gb, np.abs(np.diag(Ga)))
    iu = np.triu_indices(7, 1)
    assert np.allclose(np.angle(Gb)[iu], np.angle(Ga)[iu])
    da = np.angle(np.exp(1j * (np.angle(g @ Ga @ g.T)[iu] - np.angle(g @ Gb @ g.T)[iu])))
    assert np.max(np.abs(da)) > 0.5


def test_t171_spin_networks_with_unbounded_spin_are_decoded_from_ratios_of_coherences():
    """T-171 (restated 2026-09-26). For random directed graphs on M = 2, 3 vertices, spins up to 20 and
    intertwiner labels, Gamma_S = (1-eta|E|-kappa M) 1/7^M + eta sum psi(j_e) + kappa sum chi(k_v) is a
    full-rank state; edges, directions, spins (2j+1 = ratio of two coherences) and labels are decoded
    exactly, and partial trace decodes to the induced subnetwork. The old C29' fails: W_e^spin is not
    Hermitian and has trace != 1, and reading j = floor(7|gamma|^2)/2 off eta*|gamma| returns 0 for j <= 3
    once eta <= 1/4; the cluster spin j/k is not a half-integer for j = 7/2, k = 2."""
    from fractions import Fraction
    rng = np.random.default_rng(171)
    idx = {t: np.ravel_multi_index(t, (7, 7)) for t in ((0, 1), (1, 2), (2, 3))}

    def state(n, edges, spins, labels):
        eta = kap = 1.0 / (len(edges) + n + 1)
        G = (1 - eta * len(edges) - kap * n) * np.eye(7 ** n) / 7 ** n
        for (a, b), j in zip(edges, spins):
            psi = _ket(0, 1) + _ket(1, 2) + float(2 * j + 1) * _ket(2, 3)
            psi /= np.linalg.norm(psi)
            G = G + eta * _embed_local(np.outer(psi, psi), (a, b), n)
        for v, k in enumerate(labels):
            chi = np.eye(7)[3] + np.eye(7)[4] + (k + 1) * np.eye(7)[5]
            chi /= np.linalg.norm(chi)
            G = G + kap * _embed_local(np.outer(chi, chi), (v,), n)
        return G

    def decode(G, n):
        found, labels = [], []
        for a in range(n):
            for b in range(n):
                if a != b:
                    m = _marginal(G, (a, b), n)
                    if abs(m[idx[(0, 1)], idx[(1, 2)]]) > 1e-12:
                        r = (m[idx[(0, 1)], idx[(2, 3)]] / m[idx[(0, 1)], idx[(1, 2)]]).real
                        found.append(((a, b), Fraction(int(round(r - 1)), 2)))
        for v in range(n):
            m = _marginal(G, (v,), n)
            labels.append(int(round((m[3, 5] / m[3, 4]).real)) - 1)
        return sorted(found), labels
    for n in (2, 3, 3, 3):
        edges = [(a, b) for a in range(n) for b in range(a + 1, n) if rng.random() < 0.7]
        edges = [(b, a) if rng.random() < 0.5 else (a, b) for a, b in edges]
        spins = [Fraction(int(rng.integers(0, 41)), 2) for _ in edges]
        labels = [int(rng.integers(0, 6)) for _ in range(n)]
        G = state(n, edges, spins, labels)
        assert np.linalg.eigvalsh(G).min() > 0 and abs(np.trace(G) - 1) < 1e-10   # full-rank state
        assert decode(G, n) == (sorted(zip(edges, spins)), labels)
        sub = _marginal(G, tuple(range(n - 1)), n)
        induced = sorted((e, s) for e, s in zip(edges, spins) if max(e) < n - 1)
        assert decode(sub, n - 1) == (induced, labels[:n - 1])
    U = np.linalg.qr(rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)))[0]
    We = sum(U[i, j] * np.kron(np.outer(np.eye(7)[i], np.eye(7)[j]), np.outer(np.eye(7)[j], np.eye(7)[i]))
             for i in range(3) for j in range(3))
    assert np.linalg.norm(We - We.conj().T) > 0.1 and abs(np.trace(We) - 1) > 0.1
    for eta in (0.25, 0.1):
        assert all(np.floor(2 * j * eta ** 2) / 2 == 0 for j in (0.5, 1, 1.5, 2, 2.5, 3))
    j = Fraction(7, 2)
    k = -((-j) // 3)                                                        # ceil(j/3) = 2
    assert k == 2 and (2 * (j / k)).denominator != 1                        # j/k = 7/4 is not a spin


def test_t172_every_finite_poset_is_encoded_and_realisation_forgets_order():
    """T-172 (restated 2026-09-26). Every finite poset (no M^4 embedding assumed) on 2-4 elements is encoded
    in Gamma_C = (1 - eta N) 1/7^M + eta sum psi_(c,c'), psi = (|01> + |12>)/sqrt2 on the ordered pair; the
    order is read off <01|rho_cc'|12> != 0, and partial trace decodes the induced suborder. The old
    W_cc' with generic phases is not positive. The realisation |N(C)| of any poset with a least element is
    contractible (Euler characteristic of the order complex 1), and C and C^op have the same chains."""
    rng = np.random.default_rng(172)
    i01, i12 = np.ravel_multi_index((0, 1), (7, 7)), np.ravel_multi_index((1, 2), (7, 7))
    psi = (_ket(0, 1) + _ket(1, 2)) / np.sqrt(2)
    P = np.outer(psi, psi)

    def random_poset(n):
        R = np.zeros((n, n), bool)
        perm = rng.permutation(n)
        for i in range(n):
            for j in range(i + 1, n):
                R[perm[i], perm[j]] = rng.random() < 0.5
        for k in range(n):
            R = R | (R[:, [k]] & R[[k], :])
        return R

    def state(R):
        n = len(R)
        pairs = [(a, b) for a in range(n) for b in range(n) if R[a, b]]
        eta = 1.0 / max(1, len(pairs))
        G = (1 - eta * len(pairs)) * np.eye(7 ** n) / 7 ** n
        for a, b in pairs:
            G = G + eta * _embed_local(P, (a, b), n)
        return G

    def decode(G, n):
        return np.array([[a != b and abs(_marginal(G, (a, b), n)[i01, i12]) > 1e-12 for b in range(n)]
                         for a in range(n)])
    for n in (2, 3, 3, 4):
        R = random_poset(n)
        G = state(R)
        assert np.linalg.eigvalsh(G).min() > -1e-12 and abs(np.trace(G) - 1) < 1e-10
        assert (decode(G, n) == R).all()
        assert (decode(_marginal(G, tuple(range(n - 1)), n), n - 1) == R[:n - 1, :n - 1]).all()
    th = rng.normal(size=(7, 7))
    th = th - th.T
    W = sum(np.exp(1j * th[i, j]) * np.kron(np.outer(np.eye(7)[i], np.eye(7)[j]), np.outer(np.eye(7)[i], np.eye(7)[j]))
            for i in range(7) for j in range(7)) / 7
    assert np.linalg.eigvalsh(W).min() < -0.05

    def chains(R):
        n = len(R)
        out = []
        for size in range(1, n + 1):
            for c in itertools.permutations(range(n), size):
                if all(R[c[i], c[i + 1]] for i in range(size - 1)):
                    out.append(frozenset(c))
        return set(out)
    for n in (1, 2, 3, 4):
        chain = np.triu(np.ones((n, n), bool), 1)
        assert sum((-1) ** (len(s) - 1) for s in chains(chain)) == 1       # contractible order complex
    R = random_poset(4)
    assert chains(R) == chains(R.T)                                         # C and C^op: same order complex


# ── (W) сведена к принципу без числа; внутренняя структура УГМ слепа к кратности (26.09.2026) ──

def _herm_basis(n):
    B = []
    for i in range(n):
        E = np.zeros((n, n), complex)
        E[i, i] = 1
        B.append(E)
    for i in range(n):
        for j in range(i + 1, n):
            E = np.zeros((n, n), complex)
            E[i, j] = E[j, i] = 1
            B.append(E)
            E = np.zeros((n, n), complex)
            E[i, j], E[j, i] = -1j, 1j
            B.append(E)
    return B


def _sl_basis(n, compact_only=False):
    """Вещественный базис 𝔰𝔩(n,ℂ) (или 𝔰𝔲(n)): антиэрмитовы (вращения) и эрмитовы бесследовые (бусты)."""
    H = [h for h in _herm_basis(n)]
    H0 = [h - np.trace(h) / n * np.eye(n) for h in H]
    rot = [1j * h for h in H0]
    boo = [] if compact_only else list(H0)
    out = []
    for X in rot + boo:
        if np.linalg.norm(X) < 1e-12:
            continue
        if out and np.linalg.matrix_rank(np.array([np.concatenate([o.real.ravel(), o.imag.ravel()]) for o in out + [X]]), tol=1e-9) == len(out):
            continue
        out.append(X)
    return out


def _congruence_rep(n, alg):
    """Действие A·X = AX + XA† алгебры alg на Herm(n) (вещественные матрицы n²×n²)."""
    B = _herm_basis(n)
    G = np.array([[np.real(np.trace(a.conj().T @ b)) for b in B] for a in B])
    Ginv = np.linalg.inv(G)
    coords = lambda X: Ginv @ np.array([np.real(np.trace(b.conj().T @ X)) for b in B])
    return [np.array([coords(A @ b + b @ A.conj().T) for b in B]).T for A in alg], B, G


def _invariant_quadratic_forms(n, compact_only=False):
    reps, _, _ = _congruence_rep(n, _sl_basis(n, compact_only))
    d = n * n
    sym = []
    for i in range(d):
        for j in range(i, d):
            S = np.zeros((d, d))
            S[i, j] = S[j, i] = 1
            sym.append(S)
    rows = np.vstack([np.array([(R.T @ S + S @ R).ravel() for S in sym]).T for R in reps])
    _, s, Vt = np.linalg.svd(rows)
    null = Vt[np.sum(s > 1e-9):]
    return [sum(v[k] * sym[k] for k in range(len(sym))) for v in null]


def test_only_a_two_component_spinor_factor_carries_a_relativistic_causal_structure():
    """Теорема 48e(g): n = 2 — единственный размер спинорного сомножителя W, при котором он несёт лоренцеву структуру.

    Для W = ℂⁿ (n = 2, 3, 4): квадратичных форм на Herm(W), инвариантных относительно SL(W)
    (X ↦ MXM†), ровно 1, 0, 0 — при n = 2 это det сигнатуры (1,3); относительно одних вращений
    SU(W) их 2 при всяком n (tr X², (tr X)²): число 2 выбирают бусты. Конус форм ранга ≤ 1
    («лучи света = чистые состояния W») имеет размерность 2n − 1 против n² − 1 у квадрики: 3 = 3,
    5 < 8, 7 < 15. Орбиты SU(W) на бесследовых формах — размерности не выше n² − n против сферы
    n² − 2: 2 = 2, 6 < 7, 12 < 14 (изотропия пространства). Форма Киллинга 𝔰𝔩(n,ℂ) как
    вещественной алгебры — сигнатуры (n²−1, n²−1): (3,3) = 𝔰𝔬(1,3), (8,8) ни у какой 𝔰𝔬(1,k).
    SL(W)-инвариантных билинейных форм на самом W (спаривание массового члена): 1, 0 (ε при n = 2).
    """
    for n, want in ((2, 1), (3, 0), (4, 0)):
        Q = _invariant_quadratic_forms(n)
        assert len(Q) == want
        assert len(_invariant_quadratic_forms(n, compact_only=True)) == 2
    Q = _invariant_quadratic_forms(2)[0]
    _, B, G = _congruence_rep(2, [])
    rng = np.random.default_rng(2600)
    # сигнатура det в координатах эрмитова базиса
    M = np.zeros((4, 4))
    for i, bi in enumerate(B):
        for j, bj in enumerate(B):
            M[i, j] = (np.real(np.linalg.det(bi + bj)) - np.real(np.linalg.det(bi)) - np.real(np.linalg.det(bj))) / 2
    lam = Q.ravel() @ M.ravel() / (M.ravel() @ M.ravel())
    assert np.allclose(Q, lam * M)
    ev = np.linalg.eigvalsh(M)
    assert (int(np.sum(ev > 1e-9)), int(np.sum(ev < -1e-9))) == (1, 3)
    for n in (2, 3, 4):
        psi = rng.normal(size=n) + 1j * rng.normal(size=n)
        _, B, G = _congruence_rep(n, [])
        Ginv = np.linalg.inv(G)
        coords = lambda X: Ginv @ np.array([np.real(np.trace(b.conj().T @ X)) for b in B])
        tang = []
        for k in range(n):
            for z in (1, 1j):
                d = np.zeros(n, complex)
                d[k] = z
                tang.append(coords(np.outer(d, psi.conj()) + np.outer(psi, d.conj())))
        tang.append(coords(np.outer(psi, psi.conj())))
        assert np.linalg.matrix_rank(np.array(tang), tol=1e-9) == 2 * n - 1
        H = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
        X = H + H.conj().T
        X -= np.trace(X) / n * np.eye(n)
        orb = [A @ X - X @ A for A in _sl_basis(n, compact_only=True)]
        rk = np.linalg.matrix_rank(np.array([np.concatenate([o.real.ravel(), o.imag.ravel()]) for o in orb]), tol=1e-9)
        assert rk == n * n - n and (rk >= n * n - 2) == (n == 2)
        alg = _sl_basis(n)
        ad = []
        for A in alg:
            cols = []
            for Bm in alg:
                C = A @ Bm - Bm @ A
                cols.append(np.linalg.lstsq(np.array([np.concatenate([a.real.ravel(), a.imag.ravel()]) for a in alg]).T,
                                            np.concatenate([C.real.ravel(), C.imag.ravel()]), rcond=None)[0])
            ad.append(np.array(cols).T)
        K = np.array([[np.trace(a @ b) for b in ad] for a in ad])
        kv = np.linalg.eigvalsh((K + K.T) / 2)
        sig = (int(np.sum(kv > 1e-6)), int(np.sum(kv < -1e-6)))
        assert sig == (n * n - 1, n * n - 1)
        lorentz = [(k, k * (k - 1) // 2) for k in range(1, 20)]
        assert (sig in lorentz) == (n == 2)
    for n, want in ((2, 1), (3, 0)):
        alg = _sl_basis(n)
        basis = [np.outer(np.eye(n)[i], np.eye(n)[j]) for i in range(n) for j in range(n)]
        rows = np.vstack([np.array([(A.T @ E + E @ A).ravel() for E in basis]).T for A in alg])
        assert n * n - np.linalg.matrix_rank(rows, tol=1e-9) == want            # комплексная размерность


def test_uhm_internal_structure_is_blind_to_the_multiplicity_of_the_fermion_field():
    """Теорема 48e(f): коммутант внутренних ℂ′-линейных операторов УГМ на 𝒮_ℂ — ровно ℂ′ = span{1, i′}.

    Алгебра, порождённая 𝔰𝔭𝔦𝔫(10) (цвет, 𝔰𝔲(2)_L,R, B−L, Y), подъёмами L_{e_O}, R_{e_O}, мнимой
    единицы i пространства ℋ и 𝔤₂, имеет в End_ℝ(ℝ³²) коммутант размерности 2, и это span{1, i′}.
    Значит, на Fₙ = ℂⁿ ⊗_ℂ 𝒮_ℂ коммутант — Mₙ(ℂ′) (вещественная размерность 2n²): внутренняя
    структура не видит n. Десять образующих Клиффорда ℂ′-антилинейны (антикоммутируют с i′) — они
    действуют на Fₙ лишь вместе со структурой на первом сомножителе. i′ = ±L_{e_O} на V_L.
    """
    e = _spin10_completion()
    d, lift, ip = e["d"], e["lift"], e["ip"]
    g2 = []
    for X in G2:
        M = np.zeros((8, 8))
        M[1:, 1:] = X
        g2.append(lift(d["cl"](M)))
    ops = list(e["spin10"]) + [lift(d["Lu"]), lift(d["Ru"]), e["I1"]] + g2
    I32 = np.eye(32)
    G = np.zeros((1024, 1024))
    for X in ops:
        ad = np.kron(X, I32) - np.kron(I32, X.T)
        G += ad.T @ ad
    w, V = np.linalg.eigh(G)
    assert int(np.sum(w < 1e-8)) == 2
    C = [V[:, k].reshape(32, 32) for k in range(2)]
    F = np.array([c.ravel() for c in C]).T
    for T in (np.eye(32), ip):
        assert np.linalg.norm(F @ np.linalg.lstsq(F, T.ravel(), rcond=None)[0] - T.ravel()) < 1e-9
    for g in e["g10"]:
        assert np.allclose(g @ ip, -ip @ g)
    PL = e["PL"]
    sgn = 1 if np.allclose(e["om"], ip) else -1
    assert np.allclose(PL @ ip @ PL, sgn * PL @ lift(d["Lu"]) @ PL)
    for n in (1, 2, 3):
        opsn = [np.kron(np.eye(n), X) for X in ops[:12] + [lift(d["Lu"])]]
        # коммутант 1⊗𝔄 = End(ℝⁿ)⊗ℂ′ проверяем по вложению: всё из Mₙ(ℂ′) коммутирует
        rng = np.random.default_rng(n)
        Z = np.kron(rng.normal(size=(n, n)), np.eye(32)) + np.kron(rng.normal(size=(n, n)), ip)
        assert max(np.abs(Z @ X - X @ Z).max() for X in opsn) < 1e-12


def test_a_real_lorentz_factor_gives_an_anomalous_or_vectorlike_generation():
    """Теорема 48e(h): при вещественном лоренцевом сомножителе всякое фермионное пространство на 𝒮 аномально или векторно.

    Коммутант 𝔤_SM (T-326) в End_ℝ(𝒮) — ℂ ⊕ ℂ (размерность 4, коммутативен): кварковый блок
    (ℝ¹², где цвет действует) и лептонная прямая (ℝ⁴). Комплексные структуры, коммутирующие с 𝔤_SM, —
    ±L_{e_O} на каждом блоке. При J = L_{e_O}: Y-заряды {1/6: 6, −1/2: 2}, ΣY³ = −2/9; при смене знака
    на кварковом блоке кубическая цветовая аномалия Σq³ меняет знак и не равна нулю. На p копиях Q_L
    и m − p копиях Q̄_L она пропорциональна 2p − m: ноль только в векторном случае.
    """
    d = _sm_on_complex_octonions()
    basis = [np.outer(np.eye(16)[i], np.eye(16)[j]) for i in range(16) for j in range(16)]
    com = _null_commutant(d["g"], basis)
    assert len(com) == 4
    C = [v.reshape(16, 16) for v in com]
    assert max(np.abs(a @ b - b @ a).max() for a in C for b in C) < 1e-10
    S = sum(s.T @ s for s in d["su3"])
    w, V = np.linalg.eigh(S)
    PQ = V[:, w > 1e-9] @ V[:, w > 1e-9].T
    assert int(round(np.trace(PQ))) == 12
    Lu = d["Lu"]

    def charges(J, X, P):
        q = -J @ X
        q = P @ ((q + q.T) / 2) @ P
        vals = np.linalg.eigvalsh(q)
        return vals

    qY = np.round(np.linalg.eigvalsh((-Lu @ d["Y"] + (-Lu @ d["Y"]).T) / 2), 9)
    vals, mult = np.unique(qY, return_counts=True)
    cm = {float(v) + 0.0: int(m) // 2 for v, m in zip(vals, mult)}
    assert cm == {-0.5: 2, round(1 / 6, 9): 6}
    assert abs(sum(v ** 3 * m for v, m in cm.items()) - (-2 / 9)) < 1e-9
    rng = np.random.default_rng(7)
    X = sum(c * s for c, s in zip(rng.normal(size=8), d["su3"]))
    A = []
    for sq in (1, -1):
        J = sq * PQ @ Lu @ PQ + (np.eye(16) - PQ) @ Lu @ (np.eye(16) - PQ)
        assert np.allclose(J @ J, -np.eye(16)) and max(np.abs(J @ g - g @ J).max() for g in d["g"]) < 1e-10
        A.append(np.sum(charges(J, X, PQ) ** 3) / 2)
    assert abs(A[0]) > 1e-3 and abs(A[0] + A[1]) < 1e-9


def test_depth_register_history_and_the_two_slots_supply_no_spinor_rotation():
    """Теорема 48e(i): ни история регистра глубины, ни два слота «голоном + самомодель» не дают вращения спинорного сомножителя.

    Фейнман–Китаев: для N = 6 шагов со случайными унитарами на ℂ⁷ гамильтониан распространения после
    сопряжения W = Σ|t⟩⟨t|⊗U_t⋯U_1 равен (L_path/2) ⊗ 1; спектр L_path прост, его коммутант в M₇(ℂ)
    имеет размерность 7 и абелев — 𝔰𝔲(2) на часах с ним не коммутирует. Два слота: алгебра M₇ ⊕ M₇
    с центром ℂ² (бит слота классический); для s₁ = diag(1^p, −1^q), p + q = 7, решения s₁s₂ = −s₂s₁
    имеют ранг не выше 2·min(p, q) < 7 — обратимой пары нет, единичного спин-фактора нет ни в блоке, ни в сумме.
    """
    rng = np.random.default_rng(2611)
    N, d = 6, 7
    Us = []
    for _ in range(N):
        Z = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
        Q, R = np.linalg.qr(Z)
        Us.append(Q @ np.diag(np.diag(R) / np.abs(np.diag(R))))
    T = N + 1
    ket = lambda t: np.eye(T)[t]
    H = np.zeros((T * d, T * d), complex)
    for t in range(1, T):
        P1, P0 = np.outer(ket(t), ket(t)), np.outer(ket(t - 1), ket(t - 1))
        hop = np.kron(np.outer(ket(t), ket(t - 1)), Us[t - 1])
        H += (np.kron(P1 + P0, np.eye(d)) - hop - hop.conj().T) / 2
    W = np.zeros((T * d, T * d), complex)
    acc = np.eye(d)
    for t in range(T):
        if t > 0:
            acc = Us[t - 1] @ acc
        W += np.kron(np.outer(ket(t), ket(t)), acc)
    Lp = np.diag([1.0] + [2.0] * (T - 2) + [1.0]) - np.eye(T, k=1) - np.eye(T, k=-1)
    assert np.allclose(W.conj().T @ H @ W, np.kron(Lp / 2, np.eye(d)))
    ev = np.linalg.eigvalsh(Lp)
    assert np.min(np.diff(ev)) > 1e-3
    basis = [np.outer(np.eye(T)[i], np.eye(T)[j]) for i in range(T) for j in range(T)]
    com = _null_commutant([Lp], basis)
    assert len(com) == T
    Cm = [v.reshape(T, T) for v in com]
    assert max(np.abs(a @ b - b @ a).max() for a in Cm for b in Cm) < 1e-10
    for p in range(8):
        q = 7 - p
        s1 = np.diag([1.0] * p + [-1.0] * q)
        b7 = [np.outer(np.eye(7)[i], np.eye(7)[j]) for i in range(7) for j in range(7)]
        rows = np.array([(s1 @ E + E @ s1).ravel() for E in b7]).T
        _, s, Vt = np.linalg.svd(rows)
        null = Vt[np.sum(s > 1e-9):]
        if len(null) == 0:
            continue
        s2 = sum(c * v.reshape(7, 7) for c, v in zip(rng.normal(size=len(null)), null))
        assert np.linalg.matrix_rank(s2, tol=1e-9) == 2 * min(p, q) < 7


def _field_phases():
    """Шесть фаз поколения (Q, L, u^c, d^c, ν^c, e^c) как ω·P на 𝒮_ℂ и их КХД/SU(2) аномалии."""
    f = _yukawa_frame()
    e = f["e"]
    sL, sR = f["secL"], f["secR"]
    proj = {"Q": sL["u"] + sL["d"], "L": sL["nu"] + sL["e"], "u": sR["u"], "d": sR["d"],
            "n": sR["nu"], "e": sR["e"]}
    col = proj["Q"] + proj["u"] + proj["d"]

    def charge(X):
        q = -e["om"] @ X
        return (q + q.T) / 2
    a3 = lambda X: float(np.trace(charge(X) @ col)) / 12               # Σ q·T(𝟑), T = 1/2 на триплет
    a2 = lambda X: float(np.trace(charge(X) @ (proj["Q"] + proj["L"]))) / 8
    return f, proj, a3, a2


def _yukawa_u1s(alpha, beta, bl=0.0):
    """U(1) на полях поколения и на плоскости Хиггса (заряд q_H при j), сохраняющие (α + βτ_R + b(B−L))γ(h)."""
    f, proj, a3, a2 = _field_phases()
    e = f["e"]
    om, PL, PR = e["om"], e["PL"], e["PR"]
    tauR = PR @ f["tau"] @ PR
    plane = e["g10"][6:10]
    j = 2 * f["on_vector"](e["Y"])[6:, 6:]
    Mh = [(alpha * np.eye(32) + beta * tauR + bl * e["BL"]) @ PR @ g @ PL for g in plane]
    cols = [np.concatenate([((om @ P) @ M - M @ (om @ P)).ravel() for M in Mh]) for P in proj.values()]
    cols.append(np.concatenate([-sum(j[b, a] * Mh[b] for b in range(4)).ravel() for a in range(4)]))
    _, s, Vt = np.linalg.svd(np.array(cols).T)
    N = Vt[np.sum(s > 1e-9):]
    return [(v, sum(c * om @ P for c, P in zip(v[:6], proj.values()))) for v in N], a3, a2


def test_up_projection_is_holomorphy_in_one_complex_doublet():
    """T-332(h): (ВП) ⟺ юкава голоморфна по одному комплексному дублету плоскости.

    Гиперзаряд действует на бесцветной плоскости P как j/2 с j² = −1, и на V_L → V_R
    τ_R·γ(h) = ω·γ(jh). Поэтому (1 ± τ_R)γ(h)/2 = γ(π_± h), π_± = (1 ± ωj)/2 — проекторы на P_ℂ,
    каждый ранга 4 (один дублет): верхняя проекция — ω-линейная функция одного комплексного дублета
    π_+h (гиперзаряд −1/2, H̃ СМ), и только его. Вещественный вакуум даёт ей m_u = 1, m_d = 0.
    """
    f = _yukawa_frame()
    e = f["e"]
    om, PL, PR = e["om"], e["PL"], e["PR"]
    tauR = PR @ f["tau"] @ PR
    plane = e["g10"][6:10]
    RY = f["on_vector"](e["Y"])[6:, 6:]
    j = 2 * RY
    assert np.allclose(j @ j, -np.eye(4)) and np.allclose(j, -j.T)
    for a in range(4):
        jh = sum(j[b, a] * plane[b] for b in range(4))
        assert np.allclose(tauR @ PR @ plane[a] @ PL, PR @ om @ jh @ PL)
    Wj = np.kron(j, np.eye(2))                                        # P_ℂ = P ⊗ ℂ_ω, ω = [[0,−1],[1,0]]
    Wom = np.kron(np.eye(4), np.array([[0.0, -1.0], [1.0, 0.0]]))
    for sgn in (1, -1):
        pi = (np.eye(8) + sgn * Wom @ Wj) / 2
        assert np.allclose(pi @ pi, pi) and round(np.trace(pi)) == 4
    m = _yukawa_masses(((np.eye(32) + tauR) / 2) @ PR @ (0.6 * plane[3] + 0.8 * plane[0]) @ PL)
    assert np.isclose(m["u"], 1) and np.isclose(m["nu"], 1) and m["d"] < 1e-12 and m["e"] < 1e-12


def test_an_exact_up_projection_leaves_the_tau_massless_to_all_orders():
    """T-332(i): точная (ВП) несёт лишнюю симметрию, запрещающую m_τ во всех порядках; данные её опровергают.

    U(1) на шести полях поколения и дублете, сохраняющие юкаву (α + βτ_R)γ(h) (при желании с (B−L)):
    при |β| ≠ |α| их ровно 3 (Y, B, L), и КХД-аномалия каждой равна нулю; при β = ±α — 5, среди них
    фаза e^c (аномалий SU(3) и SU(2) нет: запрет m_e, m_μ, m_τ точен и непертурбативно) и
    КХД-аномальная фаза d^c (A₃ = 1/2 на поколение: m_d, m_s, m_b = 0 во всех порядках теории возмущений).
    """
    f, proj, a3, a2 = _field_phases()
    om = f["e"]["om"]
    assert np.isclose(a3(om @ proj["d"]), 0.5) and abs(a2(om @ proj["d"])) < 1e-12
    assert abs(a3(om @ proj["e"])) < 1e-12 and abs(a2(om @ proj["e"])) < 1e-12
    assert np.isclose(a3(om @ proj["Q"]), 1.0) and np.isclose(a2(om @ proj["Q"]), 1.5)
    for ab in ((1.0, 0.971, 0.0), (1.0, 0.5, 0.0), (0.7, -0.2, 0.3)):
        sols, _, _ = _yukawa_u1s(*ab)
        assert len(sols) == 3 and max(abs(a3(X)) for _, X in sols) < 1e-9
    for beta in (1.0, -1.0):
        sols, _, _ = _yukawa_u1s(1.0, beta)
        assert len(sols) == 5 and max(abs(a3(X)) for _, X in sols) > 0.1
        V = np.array([v for v, _ in sols])
        side = "e" if beta == 1.0 else "n"
        unit = np.zeros(7)
        unit[list(proj).index(side)] = 1.0
        assert np.linalg.norm(V.T @ (V @ unit) - unit) < 1e-9       # фаза e^c (или ν^c) — симметрия


def test_b_tau_and_the_size_of_the_up_projector_breaking():
    """T-332(j): нарушение (ВП) ε = 1 − β/α и b–τ по однопетлевому бегу СМ; ветвь ранга 4 вакуума.

    ε(μ) = 2y_b/(y_t + y_b): 0,0357 при M_Z, 0,0292 при 10¹⁴, 0,0288 при 2·10¹⁶ ГэВ. y_b/y_τ падает от
    1,73 при M_Z до 0,655 при 2·10¹⁶ и равна 1 при ≈ 6,3·10⁶ ГэВ: нарушение без (B−L)-одевания
    сшивается с b = τ лишь там; сшивка при 2·10¹⁶ требует одевания p + q(B−L) с q/p = −0,349.
    Вакуум T-64: на 94 из 99 точек фазы Gap ветвь ранга 4 (одна компонента кваркового дублета
    не заселена, точная кварковая проекция), на остальных доля до 0,75.
    """
    from scipy.integrate import solve_ivp
    from scipy.optimize import brentq
    MZ, v, a0 = 91.1876, 246.22, 0.1180
    a_s = lambda mu: a0 / (1 + a0 * (23 / 3) / (2 * np.pi) * np.log(mu / MZ))
    mt = 162.5 * (a_s(MZ) / a_s(162.5)) ** (12 / 23)
    mb = 4.18 * (a_s(MZ) / a_s(4.18)) ** (12 / 23)

    def rhs(t, s):
        g1, g2, g3, yt, yb, yl = s
        k = 1 / (16 * np.pi ** 2)
        return [k * 4.1 * g1 ** 3, -k * 19 / 6 * g2 ** 3, -k * 7 * g3 ** 3,
                k * yt * (4.5 * yt ** 2 + 1.5 * yb ** 2 + yl ** 2 - 8 * g3 ** 2 - 2.25 * g2 ** 2 - 0.85 * g1 ** 2),
                k * yb * (1.5 * yt ** 2 + 4.5 * yb ** 2 + yl ** 2 - 8 * g3 ** 2 - 2.25 * g2 ** 2 - 0.25 * g1 ** 2),
                k * yl * (3 * yt ** 2 + 3 * yb ** 2 + 2.5 * yl ** 2 - 2.25 * g2 ** 2 - 2.25 * g1 ** 2)]
    s0 = [np.sqrt(5 / 3) * 0.3574, 0.6517, np.sqrt(4 * np.pi * a0)] + [np.sqrt(2) * m / v for m in (mt, mb, 1.77693)]
    T = np.log(2e16 / MZ)
    sol = solve_ivp(rhs, (0, T), s0, rtol=1e-10, dense_output=True)
    at = lambda mu: sol.sol(np.log(mu / MZ))[3:]
    eps = {mu: 2 * at(mu)[1] / (at(mu)[0] + at(mu)[1]) for mu in (MZ, 1e14, 2e16)}
    assert abs(eps[MZ] - 0.0357) < 5e-4 and abs(eps[1e14] - 0.0292) < 5e-4 and abs(eps[2e16] - 0.0288) < 5e-4
    r = {mu: at(mu)[1] / at(mu)[2] for mu in (MZ, 2e16)}
    assert abs(r[MZ] - 1.73) < 0.01 and abs(r[2e16] - 0.655) < 0.005
    mu_bt = MZ * np.exp(brentq(lambda t: sol.sol(t)[4] - sol.sol(t)[5], 0.1, T))
    assert 5e6 < mu_bt < 8e6
    qp = (r[2e16] - 1) / (1 / 3 + r[2e16])                               # (p + q/3)/(p − q) = y_b/y_τ
    assert abs(qp + 0.349) < 0.005
    n = rank4 = 0
    split = []
    for l4 in (0.0, 1.0, 30.0):
        for kap in np.geomspace(0.05, 3.0, 40):
            _, (s, dd) = _family_min(kap, l4)
            if abs(dd) < 1e-9:
                continue
            b, c = (s + dd) / 2, (s - dd) / 2
            n += 1
            rank4 += min(b, c) < 1e-9
            split.append(min(b, c) / max(b, c))
    assert (n, rank4) == (99, 94) and 0.74 < max(split) < 0.76


def test_no_peccei_quinn_symmetry_in_the_clifford_content():
    """T-333(e)–(g): при трёх поколениях 𝟏𝟔 и одном дублете нет U(1) с КХД-аномалией; аксион страницы ТМ.

    Заряды (Q_i, u_i, d_i, H), сохраняющие ненулевые входы Y_u (QH̃u^c) и Y_d (QHd^c) при det ≠ 0:
    на 300 случайных масках носителя с невырожденными матрицами КХД-аномалия Σ(2q_Q + q_u + q_d) = 0
    на всём пространстве решений. 𝟏𝟔 кирален: мультимножество гиперзарядов цветных состояний не
    замкнуто относительно смены знака (векторной пары для Нельсона–Барра нет). Страница тёмной
    материи: m_a = 2,9 нэВ при f_a = 2·10¹⁵ ГэВ — арифметика верна; при θ_i = H_I/(2πf_a) плотность
    аксиона — изокривизна порядка единицы, и β_iso < 0,038 требует Ω_a/Ω_c ≲ 3·10⁻⁵ против 10⁻².
    """
    rng = np.random.default_rng(7)
    checked = 0
    while checked < 300:
        Mu, Md = rng.random((3, 3)) < 0.6, rng.random((3, 3)) < 0.6
        Yu, Yd = Mu * rng.normal(size=(3, 3)), Md * rng.normal(size=(3, 3))
        if abs(np.linalg.det(Yu)) < 1e-3 or abs(np.linalg.det(Yd)) < 1e-3:
            continue
        rows = []                                                         # неизвестные: q_Q(3), q_u(3), q_d(3), q_H
        for (Mk, off, sH) in ((Mu, 3, -1.0), (Md, 6, 1.0)):
            for i, jj in zip(*np.nonzero(Mk)):
                row = np.zeros(10)
                row[i] += 1
                row[off + jj] += 1
                row[9] += sH
                rows.append(row)
        _, s, Vt = np.linalg.svd(np.array(rows))
        N = Vt[np.sum(s > 1e-9):]
        anom = np.array([2, 2, 2, 1, 1, 1, 1, 1, 1, 0.0])
        assert np.abs(N @ anom).max() < 1e-9
        checked += 1
    f, proj, _, _ = _field_phases()
    e = f["e"]
    q = -e["om"] @ e["Y"]
    q = (q + q.T) / 2
    col = proj["Q"] + proj["u"] + proj["d"]
    w = np.round(np.linalg.eigvalsh(col @ q @ col + 50 * (np.eye(32) - col)), 9)
    ys = sorted(x for x in w if x < 10)
    assert sorted(-x for x in ys) != ys
    d = e["d"]
    for a, b, c in ((0.37, 0.15, 0.06), (0.4, 0.3, 0.0)):                 # вакуум T-64 на 𝒮 коммутирует с (B−L)/2
        M = np.zeros((8, 8), complex)
        M[1:, 1:] = _colour_family(a, b, c)
        M[0, 0] = a
        Gh = np.block([[M.real, -M.imag], [M.imag, M.real]])
        assert np.abs(Gh @ d["Y"] - d["Y"] @ Gh).max() < 1e-12
    mu_, md_, mpi, fpi, fa = 2.16e-3, 4.67e-3, 0.135, 0.092, 2e15
    ma = np.sqrt(mu_ * md_) / (mu_ + md_) * mpi * fpi / fa * 1e18                 # нэВ
    assert 2.8 < ma < 3.0
    HI = np.pi * 2.435e18 * np.sqrt(2.1e-9 * 0.036 / 2)
    assert abs(HI / (2 * np.pi * fa) - 3.7e-3) < 2e-4
    PS_max = 0.038 / (1 - 0.038) * 2.1e-9
    frac = np.sqrt(PS_max / (4 / 60))                                     # P_δ ≈ 4/N, N = 60
    assert 2e-5 < frac < 5e-5 and 1e-2 / frac > 200


def _pt_odd_quartic(G):
    """PT-нечётный G₂-инвариант степени 4 типа S³X₇: ⟨φ·X, φ·(N S)⟩, N_pq = φ_pab S_ac S_bd φ_qcd.

    S — бесследовая часть Re Γ, X = Im Γ. Линеен по X, поэтому его первая вариация на
    вещественных состояниях в направлениях Im Γ, вообще говоря, не нуль.
    """
    S = G.real - np.trace(G.real) / 7 * np.eye(7)
    v = np.einsum('kij,ij->k', PHI3, G.imag)
    N = np.einsum('pab,ac,bd,qcd->pq', PHI3, S, S, PHI3)
    return float(v @ np.einsum('kab,ab->k', PHI3, N @ S))


def test_theta_route_through_the_gap_potential_fails_for_v3_and_for_pt_odd_quartics():
    """T-99 (исправление 26.09.2026): шаг 4 ложен при всяком λ₃ ≠ 0; PT-нечётная квартика — источник фаз, не страж.

    (1) На вещественных Γ (все θ_ij ∈ {0, π}) V₂ + V₃ + V₄ страницы ≡ 0: 𝒢_total = ‖Im Γ‖² = 0 и V₃ = 0.
    Производная V₃ вдоль i·X на вещественном состоянии не нуль, поэтому для λ₃ = 9,25; 1; 0,1; 0,01
    сдвиг R → R + itX с подходящим знаком t даёт V < 0: вакуум лежит вне вещественных состояний,
    фазы в нём не нуль (свидетель `v_gap_vacuum_is_unique…` даёт 𝒢_total = 1/(2λ₄) > 0).
    «Все фазы обращаются в нуль» шага 4 опровергнуто для самого V₃, при любых секторных модулях.
    (2) Явная PT-нечётная квартика типа S³X₇ (одна из трёх PT-нечётных квартик T-331) G₂-инвариантна,
    меняет знак при PT, так что потенциал с ней не инвариантен ни относительно какого g∘PT, g ∈ G₂;
    её первая вариация по Im Γ на вещественных состояниях не нуль, и μ²𝒢 + λ₄𝒢² + εQ имеет V < 0 —
    PT-нечётный член рождает фазы вакуума, а не запрещает их.
    """
    rng = np.random.default_rng(3399)
    W = rng.normal(size=(7, 7))
    R = W @ W.T / np.trace(W @ W.T)
    assert _gap_total(R) == 0 and abs(_v3(R)) < 1e-15
    X = rng.normal(size=(7, 7))
    X = X - X.T
    h = 1e-6
    dv3 = (_v3(R + 1j * h * X) - _v3(R - 1j * h * X)) / (2 * h)
    assert abs(dv3) > 1e-3
    for l3, l4 in ((9.25, 32.22), (1.0, 0.1), (0.1, 1.0), (0.01, 10.0)):
        t = -np.sign(l3 * dv3) * 0.1 * abs(l3 * dv3) / (np.sum(X * X) + abs(l3) * 50)
        G = R + 1j * t * X
        assert np.linalg.eigvalsh(G).min() > 0
        assert _v_gap(G, 1.0, l3, l4) < 0 < _gap_total(G)
    G = random_state(rng)
    g = expm(sum(c * Y for c, Y in zip(rng.normal(size=14), G2)))
    q = _pt_odd_quartic(G)
    assert abs(q) > 1e-6
    assert abs(_pt_odd_quartic(g @ G @ g.T) - q) < 1e-14 and abs(_pt_odd_quartic(G.conj()) + q) < 1e-15
    assert abs(_pt_odd_quartic(g @ G.conj() @ g.T) + q) < 1e-14
    dq = (_pt_odd_quartic(R + 1j * h * X) - _pt_odd_quartic(R - 1j * h * X)) / (2 * h)
    assert abs(dq) > 1e-4 and abs(_pt_odd_quartic(R)) < 1e-15
    t = -np.sign(dq) * 0.1 * abs(dq) / np.sum(X * X)
    G = R + 1j * t * X
    assert np.linalg.eigvalsh(G).min() > 0
    V = _gap_total(G) + 10 * _gap_total(G) ** 2 + _pt_odd_quartic(G)
    assert V < 0 < _gap_total(G)


def _sym_basis_27():
    """Ортонормированный базис бесследовых вещественных симметричных 7×7 (27 = представление G₂)."""
    B = []
    for i in range(7):
        for j in range(i + 1, 7):
            M = np.zeros((7, 7))
            M[i, j] = M[j, i] = 1 / np.sqrt(2)
            B.append(M)
    Q, _ = np.linalg.qr(np.column_stack([np.ones(7)] + [np.eye(7)[:, k] - np.eye(7)[:, k + 1] for k in range(6)]))
    B += [np.diag(Q[:, k]) for k in range(1, 7)]
    return np.array(B)


def _sym3(T):
    return sum(T.transpose(p) for p in itertools.permutations(range(3))) / 6


def _associator_weight_tools():
    """Вес ассоциатора κ[F] кубика F на вещественном секторе: κ[F] = −⟨F, 𝒜°⟩/⟨𝒜°, 𝒜°⟩ (Фишер),
    𝒜° = 𝒜 − (96/5)e₃ = 𝒜 − (32/5)tr Δ³. Возвращает базис, тензор 𝒜°, функцию веса."""
    B = _sym_basis_27()
    A = _assoc4()
    K = np.einsum('ijkl,abcl->iajbkc', A, A)
    TA = _sym3(np.einsum('iajbkc,pia,qjb,rkc->pqr', K, B, B, B, optimize=True))
    X3 = np.einsum('pab,qbc,rca->pqr', B, B, B)
    T3 = _sym3((X3 + X3.transpose(0, 2, 1)) / 2)
    To = TA - 32 / 5 * T3
    w = lambda T: -float(np.sum(T * To)) / float(np.sum(To * To))
    return B, TA, T3, To, w


def _e3(G):
    ev = np.linalg.eigvalsh(G)
    return float(sum(ev[i] * ev[j] * ev[k] for i, j, k in itertools.combinations(range(7), 3)))


def test_axis_permutations_average_the_associator_to_a_spectral_cubic():
    """T-331(f) [Т]: среднее 𝒜 по перестановкам осей — спектральный кубик (96/5)e₃(Γ), при всякой калибровке.

    Π₇ (проектор Λ³ℂ⁷ на Λ³₇) усредняется по S₇ в I/5: Λ³ℂ⁷ = Λ³V₆ ⊕ Λ²V₆ (20 + 15), а
    Tr(Π₇ dΓ(M)) = 3 Tr M для всякого M (линейный G₂-инвариант на End ℂ⁷ один — след), так что
    Tr(Π₇ E_w) = 3 для всякого единичного w ∈ ℂ⁷, E_w = dΓ(ww†). То же — по стабилизатору S₆ одной
    оси (им ограничена динамика с κ = κ_b + κ₀Coh_E) и по S₅ двух осей; не по 168 коллинеациям
    и не по S₄, закрепляющему три оси: Фано видно лишь тому, кто различает тройки осей.
    """
    rng = np.random.default_rng(401)
    perms = [np.eye(7)[:, list(p)] for p in itertools.permutations(range(7))]
    for _ in range(2):
        G = random_state(rng)
        D = np.diag(np.exp(2j * np.pi * rng.random(7)))
        avg = np.mean([_cal_a(D @ P @ G @ P.T @ D.conj().T) for P in perms])
        assert abs(avg - 96 / 5 * _e3(G)) < 1e-12
        s6 = [P for P in perms if P[4, 4] == 1]
        assert abs(np.mean([_cal_a(D @ P @ G @ P.T @ D.conj().T) for P in s6]) - 96 / 5 * _e3(G)) < 1e-12
    G = random_state(rng)
    lines = [set(x - 1 for x in l) for l in LINES]
    coll = [P for P in perms if all(set(int(np.argmax(P[:, i])) for i in l) in lines for l in lines)]
    fix3 = [P for P in perms if P[0, 0] == P[1, 1] == P[2, 2] == 1]
    assert len(coll) == 168 and len(fix3) == 24
    for grp in (coll, fix3):
        assert abs(np.mean([_cal_a(P @ G @ P.T) for P in grp]) - 96 / 5 * _e3(G)) > 1e-3
    # Tr(Π₇ dΓ(M)) = 3 Tr M
    trip = list(itertools.combinations(range(7), 3))
    psi = _assoc4() / 2
    Q, _ = np.linalg.qr(np.array([[psi[a, b, c, l] for (a, b, c) in trip] for l in range(7)]).T)
    P7 = Q @ Q.T
    M = rng.normal(size=(7, 7)) + 1j * rng.normal(size=(7, 7))

    def lam3(X):
        return np.array([[np.linalg.det(X[np.ix_(a, b)]) for b in trip] for a in trip])
    t = 1e-6
    dG = (lam3(np.eye(7) + t * M) - lam3(np.eye(7) - t * M)) / (2 * t)
    assert abs(np.trace(P7 @ dG) - 3 * np.trace(M)) < 1e-7


def test_symmetric_sources_carry_no_associator_weight_and_fano_readouts_carry_any():
    """T-331(f) [Т]: вес ассоциатора κ[F] канонически определён на вещественном секторе и равен нулю у всякого
    S₇-инвариантного функционала; различающие тройки осей (Фано-считывания) дают разные веса.

    G₂-инвариантных кубиков на бесследовых вещественных Δ два (tr Δ³ и 𝒜(Δ)), так что κ[F] —
    коэффициент при −𝒜 в G₂-среднем кубического члена F при I/7; κ[−𝒜] = 1, κ[V_Gap] = κ.
    S₇-инвариантные кубики (оси, треугольники, диагональные тройки, их образы при диагональной
    калибровке) — вес 0. Фано-разрешения: Σ_p det Γ|_p (момент крауссова разложения D_Ω по проекторам
    линий) — 1/144; Σ_p (Tr Π_pΔ)³ (кубик Фано-считывания) — 1/72; ⟨φ|Λ³Γ|φ⟩/7 — 1/168; энтропия
    Фано-считывания — 49/11664. Разложение по осевым проекторам даёт тот же D_Ω и вес 0.
    """
    assert _g2_invariant_counts()[(3, 0, 0)] == 2
    B, TA, T3, To, w = _associator_weight_tools()
    assert abs(float(np.sum(T3 * To))) < 1e-10 and abs(w(-TA) - 1) < 1e-12
    mask = np.array([[[1.0 if len({i, j, k}) == 3 else 0.0 for k in range(7)] for j in range(7)] for i in range(7)])
    rng = np.random.default_rng(402)
    D = np.diag(np.exp(2j * np.pi * rng.random(7)))
    Bd = np.array([D.conj() @ b @ D for b in B])
    J = np.ones((7, 7))
    s7 = [np.einsum('pii,qii,rii->pqr', B, B, B),
          np.real(np.einsum('pij,qjk,rki,ijk->pqr', Bd, Bd, Bd, mask)),
          np.einsum('p,q,r->pqr', *[np.real(np.einsum('pij,ij->p', Bd, J))] * 3),
          np.real(np.einsum('pab,bc,qcd,de,rea->pqr', Bd, J, Bd, J, Bd))]
    for T in s7:
        assert abs(w(_sym3(T))) < 1e-12
    eps = np.zeros((3, 3, 3))
    for p in itertools.permutations(range(3)):
        eps[p] = round(np.linalg.det(np.eye(3)[list(p)]))
    lines = [[x - 1 for x in l] for l in LINES]
    Tdet = sum(np.einsum('abc,def,pad,qbe,rcf->pqr', eps, eps, *[B[:, l][:, :, l]] * 3) / 6 for l in lines)
    vread = np.array([[np.trace(b[np.ix_(l, l)]) for l in lines] for b in B])
    Tread = np.einsum('pl,ql,rl->pqr', vread, vread, vread)
    Tphi = np.einsum('abc,def,pad,qbe,rcf->pqr', PHI3, PHI3, B, B, B) / 42
    assert abs(w(Tdet) - 1 / 144) < 1e-12 and abs(w(Tread) - 1 / 72) < 1e-12
    assert abs(w(Tphi) - 1 / 168) < 1e-12 and abs(49 / 162 * w(Tread) - 49 / 11664) < 1e-14
    # вещественное тождество калибровок: ⟨φ|Λ³R|φ⟩ + 𝒜(R)/24 = e₃(R) (φ² + |χ|² = |x∧y∧z|²)
    for _ in range(3):
        W = rng.normal(size=(7, 7))
        R = W @ W.T / np.trace(W @ W.T)
        lhs = np.einsum('abc,def,ad,be,cf->', PHI3, PHI3, R, R, R) / 6 + _cal_a(R) / 24
        assert abs(lhs - _e3(R)) < 1e-12
    # два разложения одного D_Ω = (2/3)(diag − id): по осям и (с весом 1/3) по линиям Фано
    G = random_state(rng)
    Pl = [np.diag([1.0 if i in l else 0.0 for i in range(7)]) for l in lines]
    ax = (2 / 3) * (np.diag(np.diag(G)) - G)
    ln = (1 / 3) * sum(P @ G @ P - (P @ G + G @ P) / 2 for P in Pl)
    assert np.linalg.norm(ax - ln) < 1e-14


def test_fixed_points_of_self_models_and_the_gap_reflection_hierarchy():
    """Теоремы 10.1–10.2 термодинамики Gap в верной форме [Т].

    10.1: неподвижная точка всякой непрерывной самомодели есть (Брауэр); у φ_coh она одна — I/7, у φ_J одна —
    Γ_η∞ = (1 − η∞)I/7 + η∞uu†, η∞ — корень 6(1 − c)η³ + η − 1 = 0 (P = 5/14 при α = 0), у φ_s их не меньше
    восьми (I/7 и e_m). Липшицевы константы 54/49 и 1,129 > 1 — Банах неприменим.
    10.2: у самомоделей замещающей формы с вещественным якорем Im φ(Γ) = k c Im Γ точно, так что оператор Gap
    сжимается при каждой рефлексии в k c ≤ 2/7 раза и сходится к 0; фазовый Gap у φ_J ≤ (49/2)(2/7)ⁿ при n ≥ 4,
    у φ_coh фазы не меняются. Итерации φ_J сходятся к Γ_η∞ при α < α* (корень 27α³ − 8α² − 8α − 2 = 0,
    α* = 0,790) и уходят в 2-цикл при α > α*: собственное значение вдоль семейства −6η²(2 − 3c)/(1 + 6η²).
    """
    u = np.ones(7) / np.sqrt(7)
    uu = np.outer(u, u).astype(complex)

    def phi(G, alpha, anchor):
        c = (1 - alpha) / 3
        R = 1 / (7 * purity(G))
        D = np.diag(np.diag(G))
        return (1 - R) * (D + c * (G - D)) + R * anchor(G)
    a_star = [x.real for x in np.roots([27, -8, -8, -2]) if abs(x.imag) < 1e-12][0]
    assert abs(a_star - 0.7900) < 1e-4
    rng = np.random.default_rng(403)
    dist = {}
    for alpha in (0.0, 0.25, 0.5, 0.75, 0.8, 0.9, 1.0):
        c = (1 - alpha) / 3
        eta = [x.real for x in np.roots([6 * (1 - c), 0, 1, -1]) if abs(x.imag) < 1e-12 and x.real > 0][0]
        Gs = (1 - eta) * np.eye(7) / 7 + eta * uu
        assert np.linalg.norm(phi(Gs, alpha, lambda G: uu) - Gs) < 1e-14
        slope = -6 * eta ** 2 * (2 - 3 * c) / (1 + 6 * eta ** 2)
        assert (abs(slope) < 1) == (alpha < a_star)
        dist[alpha] = 0.0
        for _ in range(20):
            X = random_state(rng) if rng.random() < 0.5 else random_pure(rng)
            for n in range(1, 3001):
                k = 1 - 1 / (7 * purity(X))
                Xn = phi(X, alpha, lambda G: uu)
                assert abs(np.linalg.norm(Xn.imag) - k * c * np.linalg.norm(X.imag)) < 1e-13
                X = Xn
                if 4 <= n <= 20:
                    off = ~np.eye(7, dtype=bool)
                    assert np.min(X[off].real) >= 1 / 49 - 1e-15
                    assert np.max(np.abs(np.sin(np.angle(X[off])))) <= 24.5 * (2 / 7) ** n + 1e-15
            dist[alpha] = max(dist[alpha], np.linalg.norm(X - Gs))
            conv = np.linalg.norm(X - Gs) < 1e-13
            assert conv == (alpha < a_star)
            if not conv:
                assert np.linalg.norm(phi(phi(X, alpha, lambda G: uu), alpha, lambda G: uu) - X) < 1e-10
    assert abs(dist[0.8] - 0.056) < 5e-3 and abs(dist[0.9] - 0.21) < 1e-2 and abs(dist[1.0] - 0.31) < 1e-2
    assert abs((1 + 6 * 0.25) / 7 - 5 / 14) < 1e-15
    # φ_s: I/7 и базисные состояния — восемь неподвижных точек
    sig = lambda G: G @ G / purity(G)
    for m in range(7):
        e = np.zeros((7, 7), complex)
        e[m, m] = 1
        assert np.linalg.norm(phi(e, 0.5, sig) - e) < 1e-14
    assert np.linalg.norm(phi(np.eye(7) / 7, 0.5, sig) - np.eye(7) / 7) < 1e-15
    # φ_coh: фазы когерентностей не меняются
    X = random_state(rng)
    Y = phi(X, 0.5, lambda G: np.eye(7) / 7)
    off = ~np.eye(7, dtype=bool)
    assert np.max(np.abs(np.angle(Y[off] / X[off]))) < 1e-12


def test_one_clause_principle_for_the_anchor_is_maximal_integration():
    """T-334(6) [Т]: (Eq-V) ⇔ якорь — состояние наибольшей интеграции Φ = 6 ⇔ C_rel = log 7 ⇔ s = 6/7.

    Φ = P_coh/P_diag ≤ (1 − P_diag)/P_diag ≤ 6, равенство только у чистого состояния с равномерной
    диагональью, т. е. у D uu† D†. На 2000 случайных состояниях (чистых и смешанных) Φ < 6, C_rel < log 7.
    """
    rng = np.random.default_rng(404)
    u = np.ones(7) / np.sqrt(7)
    for _ in range(2000):
        G = random_pure(rng) if rng.random() < 0.5 else random_state(rng)
        ev = np.clip(np.linalg.eigvalsh(G), 1e-300, None)
        d = np.real(np.diag(G))
        crel = -np.sum(d * np.log(d)) + np.sum(ev * np.log(ev))
        assert integration(G) < 6 - 1e-9 and crel < np.log(7) - 1e-9
    D = np.diag(np.exp(2j * np.pi * rng.random(7)))
    M = D @ np.outer(u, u) @ D.conj().T
    assert abs(integration(M) - 6) < 1e-12
    assert abs(purity(M) - np.sum(np.real(np.diag(M)) ** 2) - 6 / 7) < 1e-12
    ratios = [16.63 / 13.11, 29.25 / 23.21, 59.34 / 47.35]      # κ_c(φ_J) / порог T-336 при H = 0
    assert all(1.25 < r < 1.27 for r in ratios)



# ---------------------------------------------------------------------------
# T-345 (26.09.2026): вкус с часов — что может нарушить семейную ℤ₃ и что исключают данные.
# Данные: PDG 2024 (обзор «CKM quark-mixing matrix», ур. 12.26–12.28); массы — Huang, Zhou,
# PRD 103, 016010 (2021), полная СМ при μ = M_Z; NuFIT 6.0 (JHEP 12 (2024) 216).

def _clock_bases():
    z = np.exp(2j * np.pi / 7)
    tau = np.array([[z ** (-k * n) for k in range(7)] for n in range(7)]) / np.sqrt(7)   # строка n — |τ_n⟩
    return z, tau


def _circulant(offsets):
    N = np.zeros((7, 7))
    for t in range(7):
        for d in offsets:
            N[(t + d) % 7, t] += 1
    return N


def _left_ckm(Mu, Md):
    _, Uu = np.linalg.eigh(Mu @ Mu.conj().T)
    _, Ud = np.linalg.eigh(Md @ Md.conj().T)
    return Uu.conj().T @ Ud


def test_tick_commuting_clock_structures_are_generation_diagonal():
    """T-345(a) [Т]: всё, что коммутирует с тиком часов, диагонально в базисе гармоник.

    Инцидентность Фано {0,1,3}, множество вычетов QR = {1,2,4} (суммы Гаусса), коллинеарность
    2I + J, H_O и проектор тривиальной гармоники — циркулянты времени; в энергетическом базисе
    они диагональны. |собственное число| круговой инцидентности Фано = √2 на всех шести
    нетривиальных гармониках (разностное множество, λ = 1); у QR-циркулянта — b₇ = (−1 + i√7)/2
    на вычетах. Любые юкавы из таких структур в любом числе каналов дают |V| — перестановку.
    """
    z, tau = _clock_bases()
    U = tau.T                                    # столбец n — |τ_n⟩ в энергетическом базисе
    shift = _circulant([1])
    for N in (_circulant([0, 1, 3]), _circulant([1, 2, 4]), 2 * np.eye(7) + np.ones((7, 7)),
              np.ones((7, 7)) / 7):
        assert np.allclose(N @ shift, shift @ N)
        E = U.conj().T @ N @ U
        assert np.allclose(E, np.diag(np.diag(E)), atol=1e-12)
    ev = np.diag(U.conj().T @ _circulant([0, 1, 3]) @ U)
    assert np.allclose(np.abs(ev[1:]), np.sqrt(2))
    evq = np.diag(U.conj().T @ _circulant([1, 2, 4]) @ U)
    b7 = (-1 + 1j * np.sqrt(7)) / 2
    assert all(min(abs(evq[k] - b7), abs(evq[k] - np.conj(b7))) < 1e-12 for k in range(1, 7))
    assert abs(abs(evq[1]) - abs(evq[3])) < 1e-12              # равные модули: массы вырождены
    rng = np.random.default_rng(345)
    for _ in range(50):                                       # диагональные юкавы → |V| = перестановка
        Mu = np.diag(rng.normal(size=3) + 1j * rng.normal(size=3))
        Md = np.diag(rng.normal(size=3) + 1j * rng.normal(size=3))
        A = np.abs(_left_ckm(Mu, Md))
        assert np.allclose(np.sort(A.ravel())[-3:], 1) and np.allclose(np.sort(A.ravel())[:6], 0, atol=1e-12)


def test_the_automorphism_fixed_instant_is_the_democratic_rank_one_matrix():
    """T-345(b) [Т]: из мгновений |τ_n⟩ умножения t → 2t, 4t оставляют только τ₀; на гармониках
    QR = {1,2,4} проектор |τ₀⟩⟨τ₀| — демократическая матрица J/7 ранга 1 (одно тяжёлое поколение)."""
    z, tau = _clock_bases()
    fixed = [n for n in range(7) if (2 * n) % 7 == n]
    assert fixed == [0]
    P0 = np.outer(tau[0], tau[0].conj())
    C = P0[np.ix_([1, 2, 4], [1, 2, 4])]
    assert np.allclose(C, np.ones((3, 3)) / 7)
    assert np.linalg.matrix_rank(C) == 1


def test_flavour_matrices_in_a_common_plane_give_a_unit_ckm_entry():
    """T-345(c) [Т]: если образы всех матриц обоих секторов лежат в общей 2-плоскости,
    в каждом секторе есть безмассовое состояние и у |V| есть элемент 1. Данные: min |V_ij| = |V_ub| = 0,00373."""
    rng = np.random.default_rng(3451)
    for _ in range(50):
        Q, _ = np.linalg.qr(rng.normal(size=(3, 2)) + 1j * rng.normal(size=(3, 2)))
        mats = [Q @ (rng.normal(size=(2, 3)) + 1j * rng.normal(size=(2, 3))) for _ in range(2)]
        V = np.abs(_left_ckm(*mats))
        assert abs(V.max() - 1) < 1e-9
        assert np.linalg.svd(mats[0], compute_uv=False).min() < 1e-9


def test_two_channels_with_a_rank_one_channel_cannot_fit_quarks_and_leptons():
    """T-345(d) [Т]: M_f = α_f A + β_f B, A ранга 1 несёт тяжёлое поколение, B общая для u, d, e.

    (1) Формула: при x = β/α малом m₁/m₂ = |det B̃ − x c| / s₁(B̃)² · (1 + O(x)), где B̃ — сжатие B
    на дополнения A, c — постоянная: линейна по комплексному x. Проверено на случайных A, B.
    (2) Данные (Huang–Zhou, M_Z): h = m₂/m₃ = 0,00368 / 0,01872 / 0,05887, R = m₁/m₂ = 0,00198 /
    0,0502 / 0,00475 для u / d / e. Неравенства треугольника: |κ| ≥ 2,15 из u и d и |κ| ≤ 0,122 из u и e.
    """
    rng = np.random.default_rng(3452)
    for _ in range(40):
        a = rng.normal(size=3) + 1j * rng.normal(size=3); b = rng.normal(size=3) + 1j * rng.normal(size=3)
        a /= np.linalg.norm(a); b /= np.linalg.norm(b)
        A = np.outer(a, b.conj())
        B = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
        Qa = np.linalg.svd(np.eye(3) - np.outer(a, a.conj()))[0][:, :2]
        Qb = np.linalg.svd(np.eye(3) - np.outer(b, b.conj()))[0][:, :2]
        Bt = Qa.conj().T @ B @ Qb
        s1 = np.linalg.svd(Bt, compute_uv=False)[0]
        # c из двух точек малого x: det эффективного лёгкого блока линеен по x
        def ratio(x):
            s = np.sort(np.linalg.svd(A + x * B, compute_uv=False)); return s[0] / s[1]
        xs = 1e-4 * np.exp(1j * rng.uniform(0, 2 * np.pi))
        Cm = (Qa.conj().T @ B @ b[:, None]) @ (a[None, :].conj() @ B @ Qb)
        c = np.trace(np.array([[Bt[1, 1], -Bt[0, 1]], [-Bt[1, 0], Bt[0, 0]]]) @ Cm)
        pred = abs(np.linalg.det(Bt) - xs * c) / s1 ** 2
        assert abs(ratio(xs) / pred - 1) < 1e-2
    h = {'u': 0.620 / 168.26, 'd': 53.16e-3 / 2.839, 'e': 0.101766 / 1.72856}
    R = {'u': 1.23e-3 / 0.620, 'd': 2.67e-3 / 53.16e-3, 'e': 0.48307e-3 / 0.101766}
    kmin = (R['d'] - R['u']) / (h['u'] + h['d'])
    kmax = (R['e'] + R['u']) / (h['e'] - h['u'])
    assert kmin > 2.1 and kmax < 0.125 and kmin / kmax > 17


def test_fritzsch_six_zero_texture_overshoots_vcb():
    """T-345(e) [Т]: текстура Фрича (M₁₁ = M₁₃ = M₂₂ = 0, эрмитова) с массами M_Z (Huang–Zhou)
    даёт min по фазам |V_cb| = 0,073 > 0,0418 (PDG 2024) — страница CKM [T] → [✗]."""
    def U(m, p1, p2):
        m1, m2, m3 = m
        C = m1 - m2 + m3
        A2 = m1 * m2 * m3 / C
        B2 = -(-m1 * m2 + m1 * m3 - m2 * m3) - A2
        P = np.diag([1, np.exp(1j * p1), np.exp(1j * (p1 + p2))])
        M = P @ np.array([[0, np.sqrt(A2), 0], [np.sqrt(A2), 0, np.sqrt(B2)], [0, np.sqrt(B2), C]]) @ P.conj().T
        w, v = np.linalg.eigh(M)
        return v[:, np.argsort(np.abs(w))]
    Uu = U((1.23e-3, 0.620, 168.26), 0, 0)
    vcb = min(abs((Uu.conj().T @ U((2.67e-3, 53.16e-3, 2.839), p, q))[1, 2])
              for p in np.linspace(0, 2 * np.pi, 91) for q in np.linspace(0, 2 * np.pi, 91))
    assert 0.070 < vcb < 0.076


def test_ckm_phase_does_not_run_in_the_sm():
    """T-345(e) [Т]: одна петля СМ, M_Z → 2·10¹⁶ ГэВ: sin δ меняется на 2·10⁻⁵ (Δδ ≈ 0,003°),
    |V_us| — на 2·10⁻⁵, |V_cb| растёт на 13 %. «Двухпетлевая поправка 12,6°» к δ страницы CKM ложна."""
    from scipy.integrate import solve_ivp
    v = 246.22
    s12, s13, s23, dl = 0.22501, 0.003732, 0.04183, 1.147
    c12, c13, c23 = [np.sqrt(1 - x * x) for x in (s12, s13, s23)]
    e = np.exp(1j * dl)
    V0 = np.array([[c12 * c13, s12 * c13, s13 / e],
                   [-s12 * c23 - c12 * s23 * s13 * e, c12 * c23 - s12 * s23 * s13 * e, s23 * c13],
                   [s12 * s23 - c12 * c23 * s13 * e, -c12 * s23 - s12 * c23 * s13 * e, c23 * c13]])
    Yu = np.diag([1.23e-3, 0.620, 168.26]) * np.sqrt(2) / v
    Yd = V0 @ np.diag([2.67e-3, 53.16e-3, 2.839]) * np.sqrt(2) / v
    Ye = np.diag([0.48307e-3, 0.101766, 1.72856]) * np.sqrt(2) / v
    g0 = np.array([np.sqrt(5 / 3) * 0.3583, 0.6517, np.sqrt(4 * np.pi * 0.1179)])
    bb = np.array([41 / 10, -19 / 6, -7])

    def pack(Yu, Yd, Ye, g):
        c = np.concatenate([Yu.ravel(), Yd.ravel(), Ye.ravel()]); return np.concatenate([c.real, c.imag, g])

    def unpack(y):
        c = y[:27] + 1j * y[27:54]; return c[:9].reshape(3, 3), c[9:18].reshape(3, 3), c[18:27].reshape(3, 3), y[54:]

    def rhs(t, y):
        Yu, Yd, Ye, g = unpack(y)
        Hu, Hd, He = Yu @ Yu.conj().T, Yd @ Yd.conj().T, Ye @ Ye.conj().T
        T = np.real(3 * np.trace(Hu) + 3 * np.trace(Hd) + np.trace(He))
        g1, g2, g3 = g ** 2; k = 1 / (16 * np.pi ** 2); I = np.eye(3)
        return pack(k * ((1.5 * (Hu - Hd) + (T - (17 / 20 * g1 + 9 / 4 * g2 + 8 * g3)) * I) @ Yu),
                    k * ((1.5 * (Hd - Hu) + (T - (1 / 4 * g1 + 9 / 4 * g2 + 8 * g3)) * I) @ Yd),
                    k * ((1.5 * He + (T - (9 / 4 * g1 + 9 / 4 * g2)) * I) @ Ye), k * bb * g ** 3)

    def obs(Yu, Yd):
        V = _left_ckm(Yu, Yd); a = np.abs(V)
        J = np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1]))
        s13 = a[0, 2]; s12 = a[0, 1] / np.sqrt(1 - s13 ** 2); s23 = a[1, 2] / np.sqrt(1 - s13 ** 2)
        c = lambda x: np.sqrt(1 - x * x)
        return a[0, 1], a[1, 2], J / (c(s12) * c(s23) * c(s13) ** 2 * s12 * s23 * s13)
    sol = solve_ivp(rhs, [0, np.log(2e16 / 91.1876)], pack(Yu, Yd, Ye, g0), rtol=1e-9, atol=1e-12)
    Yu2, Yd2, _, _ = unpack(sol.y[:, -1])
    vus0, vcb0, sd0 = obs(Yu, Yd)
    vus1, vcb1, sd1 = obs(Yu2, Yd2)
    assert abs(sd1 - sd0) < 1e-4 and abs(vus1 - vus0) < 1e-4
    assert 1.10 < vcb1 / vcb0 < 1.16
    assert np.degrees(abs(np.arcsin(sd1) - np.arcsin(sd0))) < 0.01


def test_parameter_free_clock_pairs_miss_the_up_quark_ratios():
    """T-345(d) [Т], частный перебор: пары (демократическая |τ₀⟩⟨τ₀|, H_O) и (H_O, время T) на
    гармониках QR = {1,2,4}: M = A + xB по всей комплексной плоскости x (|x| от e⁻¹¹ до e⁶) не
    достигает (m_u/m_t, m_c/m_t) ближе множителя e^2,4 ≈ 11 (полный перебор 112 пар — там же)."""
    z, tau = _clock_bases()
    Hc = np.diag([1., 2., 4.]).astype(complex)
    P0 = np.outer(tau[0], tau[0].conj())[np.ix_([1, 2, 4], [1, 2, 4])]
    Tfull = sum(n * np.outer(tau[n], tau[n].conj()) for n in range(7))
    Tc = Tfull[np.ix_([1, 2, 4], [1, 2, 4])]
    target = np.log([1.23e-3 / 168.26, 0.620 / 168.26])
    LR = np.linspace(-11, 6, 240); PH = np.exp(1j * np.linspace(0, 2 * np.pi, 120, endpoint=False))
    X = (np.exp(LR)[:, None] * PH[None, :]).ravel()
    for A, B in ((P0, Hc), (Hc, P0), (Hc, Tc), (P0, Tc)):
        s = np.linalg.svd(A[None] + X[:, None, None] * B[None], compute_uv=False)
        d = np.max(np.abs(np.log(s[:, [2, 1]] / s[:, [0]]) - target), axis=1)
        assert d.min() > 2.0
# ── T13 (усилена 26.09.2026) и T-331(g): острый минимальный инструмент и расходимости его считывания ──────

def _sharp_minimal_kraus_solutions():
    """Все острые минимальные крауссовы разложения шуровского канала Φ_c = c·id + (1 − c)·diag на ℂ⁷:
    семь операторов √x_S Π_S (Π_S — координатный проектор), N X Nᵀ = (1 − c)I + cJ, N — матрица
    инцидентности 7×7. Обратимость N даёт |S ∩ T| = t k_S k_T при S ≠ T, t = c/(1 + 6c) — рационально,
    ≤ 7/(k_S k_T); перебор по размерам и по системам множеств (первый блок закреплён: с точностью до S₇)."""
    from fractions import Fraction as Fr
    subsets = [frozenset(s) for r in range(1, 8) for s in itertools.combinations(range(7), r)]

    def realise(ks, t):
        cols = []

        def rec():
            m = len(cols)
            if m == 7:
                N = np.array([[1.0 if i in S else 0.0 for S in cols] for i in range(7)])
                return abs(np.linalg.det(N)) > 0.5
            for S in subsets:
                if len(S) != ks[m] or S in cols or (m == 0 and S != frozenset(range(ks[0]))):
                    continue
                if any(len(S & T) != t * ks[m] * len(T) for T in cols):
                    continue
                cols.append(S)
                if rec():
                    return True
                cols.pop()
            return False
        return [sorted(S) for S in cols] if rec() else None
    out = []
    for ks in itertools.combinations_with_replacement(range(7, 0, -1), 7):
        ts = {Fr(m, ks[a] * ks[b]) for a, b in itertools.combinations(range(7), 2) for m in range(1, 8)}
        for t in sorted(x for x in ts if 0 < x < Fr(1, 7)):
            if all((t * ks[a] * ks[b]).denominator == 1 for a, b in itertools.combinations(range(7), 2)):
                sol = realise(list(ks), t)
                if sol is not None:
                    out.append((t / (1 - 6 * t), ks, sol))
    return out


def test_sharp_minimal_kraus_representations_are_the_fano_planes():
    """T13 (усилена 26.09.2026) [Т]: острое минимальное крауссово разложение Φ_Ω = id + D_Ω (c = 1/3) —
    семь проекторов линий одной из 30 плоскостей Фано с весом 1/3; ранги и веса не предполагаются.

    При 0 < c < 1 острое минимальное разложение есть лишь при c ∈ {1/3, 1/2, 5/6} (симметричные схемы
    (7,3,1), (7,4,2), (7,6,5)); в семействе 𝒫_α (c = (1 − α)/3) — лишь при α = 0 (и α = 1: оси).
    Из 30 плоскостей одна инвариантна относительно 168 коллинеаций октонионной — сами линии Фано.
    Синдромные измерения кода Хэмминга дают пары {Π_p, I − Π_p}: случайная проверка — Φ_{3/7}, у которого
    острого минимального разложения нет; полный синдром — дефазировку Φ₀. Без остроты минимальные
    разложения — U(7)-орбита, например циклическое √(3/7)I, √(2/21)diag(ω^{ai}), чьи исходы от Γ не зависят.
    """
    from fractions import Fraction as Fr
    sols = _sharp_minimal_kraus_solutions()
    assert sorted((c, ks[0], len(set(ks))) for c, ks, _ in sols) == [(Fr(1, 3), 3, 1), (Fr(1, 2), 4, 1), (Fr(5, 6), 6, 1)]
    # c = 1/3: все системы семи троек, попарно пересекающихся в одной точке, — ровно 30 плоскостей Фано
    triples = [frozenset(s) for s in itertools.combinations(range(7), 3)]
    fams = []

    def grow(fam, start):
        if len(fam) == 7:
            fams.append(frozenset(fam))
            return
        for q in range(start, 35):
            if all(len(triples[q] & T) == 1 for T in fam):
                grow(fam + [triples[q]], q + 1)
    grow([], 0)
    lines0 = frozenset(frozenset(x - 1 for x in l) for l in LINES)
    assert len(fams) == 30 and lines0 in fams
    for fam in fams:                                     # каждая даёт Φ_{1/3}: пара на одной линии
        Nm = np.array([[1.0 if i in S else 0.0 for S in fam] for i in range(7)])
        assert np.allclose(Nm @ Nm.T / 3, (2 / 3) * np.eye(7) + np.ones((7, 7)) / 3)
    coll = [s for s in itertools.permutations(range(7))
            if frozenset(frozenset(s[i] for i in l) for l in lines0) == lines0]
    assert len(coll) == 168
    inv = [f for f in fams if all(frozenset(frozenset(s[i] for i in l) for l in f) == f for s in coll)]
    assert inv == [lines0]
    # синдромная проверка: {Π_p, I − Π_p} с вероятностью 1/7 → когерентности × 3/7; полный синдром различает оси
    Pl = [np.diag([1.0 if i in l else 0.0 for i in range(7)]) for l in lines0]
    rng = np.random.default_rng(411)
    G = random_state(rng)
    syn = sum(P @ G @ P + (np.eye(7) - P) @ G @ (np.eye(7) - P) for P in Pl) / 7
    off = ~np.eye(7, dtype=bool)
    assert np.allclose(syn[off], 3 / 7 * G[off]) and np.allclose(np.diag(syn), np.diag(G))
    assert len({tuple(1 if i in l else 0 for l in lines0) for i in range(7)}) == 7
    # несострое минимальное разложение того же Φ_{1/3}: исходы не зависят от Γ
    om = np.exp(2j * np.pi / 7)
    K = [np.sqrt(3 / 7) * np.eye(7)] + [np.sqrt(2 / 21) * np.diag(om ** (a * np.arange(7))) for a in range(1, 7)]
    fano = sum(P @ G @ P for P in Pl) / 3
    assert np.linalg.norm(sum(k @ G @ k.conj().T for k in K) - fano) < 1e-14
    assert np.allclose([np.trace(k.conj().T @ k @ G).real for k in K], [3 / 7] + [2 / 21] * 6)


def test_line_instrument_divergences_fix_no_coupling_and_no_gap_phase():
    """T-331(g) [Т]: канонический инструмент линий фиксирует носитель считывания, но не κ.

    Кубик считывания Σ_p (Tr Π_pΔ)³ плоскости, делящей с октонионной 7, 3, 1, 0 линий (1, 7, 14, 8
    плоскостей), весит 1/72, 1/252, −1/1008, −1/288 (a = 1/504 на линию, −a/4 на треугольник), среднее 0.
    f-расходимость считывания от считывания I/7 весит (49/11664) f'''(1) (f''(1) = 1): KL −49/11664,
    обратная KL −49/5832, Реньи порядка α: −α(2 − α)·49/11664 (Пирсон и α = 2 — ноль, α > 2 — плюс).
    Информационный выигрыш Гроневолда I_G весит −245/46656. Все исходы инструмента — функции диагонали Γ.
    """
    from fractions import Fraction as Fr
    B, TA, T3, To, w = _associator_weight_tools()
    lines0 = frozenset(frozenset(x - 1 for x in l) for l in LINES)
    planes = {frozenset(frozenset(s[i] for i in l) for l in lines0) for s in itertools.permutations(range(7))}

    def t_read(P):
        v = np.array([[np.trace(b[np.ix_(sorted(l), sorted(l))]) for l in P] for b in B])
        return np.einsum('pl,ql,rl->pqr', v, v, v)
    tally = {}
    for P in planes:
        key = (len(P & lines0), Fr(w(t_read(P))).limit_denominator(5000))
        tally[key] = tally.get(key, 0) + 1
    assert tally == {(7, Fr(1, 72)): 1, (3, Fr(1, 252)): 7, (1, Fr(-1, 1008)): 14, (0, Fr(-1, 288)): 8}
    lines = [sorted(l) for l in lines0]
    Pl = [np.diag([1.0 if i in l else 0.0 for i in range(7)]) for l in lines]
    w_read = w(t_read(lines0))                      # кубик Σ_p (Tr Π_pΔ)³; Σ_p δ_p³ весит w_read/27
    # кубический член расходимостей: f'''(1)/6 · Σ_p (1/7)(7δ_p)³, δ_p = Tr(Π_pΔ)/3 — сверка разностями
    read = lambda G: np.array([np.trace(P @ G).real / 3 for P in Pl])
    u = np.ones(7) / 7
    divs = {'kl': (lambda p: np.sum(p * np.log(p / u)), -1.0),
            'rkl': (lambda p: np.sum(u * np.log(u / p)), -2.0),
            'renyi_half': (lambda p: np.log(np.sum(p ** 0.5 * u ** 0.5)) / (-0.5), -0.5 * 1.5),
            'renyi_3': (lambda p: np.log(np.sum(p ** 3 * u ** -2)) / 2, 3.0),
            'pearson': (lambda p: np.sum((p - u) ** 2 / u) / 2, 0.0)}
    rng = np.random.default_rng(412)
    for name, (Df, f3) in divs.items():
        for _ in range(3):
            D = np.einsum('p,pij->ij', rng.normal(size=27), B)
            D /= np.linalg.norm(D)
            eps = np.linspace(-0.02, 0.02, 21)
            g = np.array([Df(read(np.eye(7) / 7 + e * D)) for e in eps])
            c3 = np.polyfit(eps, g, 7)[-4]
            pred = f3 / 6 * 49 * np.sum(read(D) ** 3)
            assert abs(c3 - pred) < 1e-6 * max(1.0, abs(pred))
        assert abs(f3 * 49 / 6 * w_read / 27 - f3 * 49 / 11664) < 1e-14
    assert abs(-49 / 11664 * 2 - (-49 / 5832)) < 1e-18
    # Гроневолд: I_G = S(Γ) − Σ p_p S(Γ_p); кубик (49/6)Tr Δ³ − (49/18)Σ_p Tr(Δ|_p)³ + (49/6)Σ_p δ_p³
    Tblk = _sym3(sum(np.einsum('pab,qbc,rca->pqr', *[B[:, l][:, :, l]] * 3) for l in lines))
    assert abs(w(Tblk) - 1 / 288) < 1e-12
    assert abs(-(49 / 18) * w(Tblk) + 49 / 6 * w_read / 27 - (-245 / 46656)) < 1e-14
    # исходы инструмента (повторные применения, диагональные унитарные между ними) видят лишь диагональ
    G = random_state(rng)
    G2 = np.diag(np.diag(G))                             # то же распределение осей, без когерентностей
    for _ in range(20):
        seq = rng.integers(0, 7, size=4)
        K = np.eye(7, dtype=complex)
        for p in seq:
            K = np.diag(np.exp(1j * rng.random(7))) @ (Pl[p] / np.sqrt(3)) @ K
        assert abs(np.trace(K @ G @ K.conj().T) - np.trace(K @ G2 @ K.conj().T)) < 1e-15


def _real_commutant_dim(ops, n):
    G = np.zeros((n * n, n * n))
    I = np.eye(n)
    for X in ops:
        ad = np.kron(X, I) - np.kron(I, X.T)
        G += ad.T @ ad
    return int(np.sum(np.linalg.eigvalsh(G) < 1e-8))


def test_spinor_factor_premise_and_fermion_module_premise_are_independent():
    """Посылки УГМ (reference/premises): (P) и (Кл₀) независимы — модели «все, кроме одной».

    (Кл₀) без (P): Fₙ = ℂⁿ ⊗ 𝒮_ℂ при n = 3 — всё о поколении верно (48e(f)), но SL(W)-инвариантных
    квадратичных форм на Herm(ℂ³) нет (0), причинной формы нет — (P) ложна.
    (P) без (Кл₀): F = W ⊗_ℂ M с M = ℂ⁷ (векторы голонома, 𝔤₂ и i пространства ℋ): коммутант этой
    внутренней структуры в End_ℝ(ℝ¹⁴) двумерен (= ℂ), значит преобразования W, сохраняющие её, —
    GL(W), и при W = ℂ² инвариантная форма одна (det) — (P) выполнена; но dim_ℝ ℂ⁷ = 14 не кратно 16,
    ℂ⁷ не модуль Cl₇ — (Кл₀) ложна. Объединение (P) и (Кл₀) в одну фразу возможно (так и записана (P)),
    сокращения числа независимых входов — нет.
    """
    J = np.kron(np.array([[0.0, -1.0], [1.0, 0.0]]), np.eye(7))
    ops = [np.kron(np.eye(2), X) for X in G2] + [J]
    assert _real_commutant_dim(ops, 14) == 2
    assert _real_commutant_dim([np.kron(np.eye(2), X) for X in G2], 14) == 4        # без i: M₂(ℝ)
    assert 14 % 16 != 0 and 32 % 16 == 0
    assert len(_invariant_quadratic_forms(2)) == 1 and len(_invariant_quadratic_forms(3)) == 0


def _top_window_sink(d, s, kap, alpha, n=20001):
    """Верхний сток в окне при постоянном якоре (T-335): η = F(P), F = B/A, P = d + η²s; None, если нет."""
    c = (1 - alpha) / 3
    Fp = lambda P: np.divide(*_anchor_window_parts(P, kap, c)[::-1])
    h = lambda e: Fp(d + e * e * s) - e
    eta = np.linspace(1e-6, 1, n)
    P = d + eta ** 2 * s
    v = h(eta)
    idx = np.where((P[:-1] > 2 / 7) & (v[:-1] > 0) & (v[1:] <= 0))[0]
    if not len(idx):
        return None
    lo, hi = eta[idx[-1]], eta[idx[-1] + 1]
    for _ in range(80):
        m = (lo + hi) / 2
        lo, hi = (m, hi) if h(m) > 0 else (lo, m)
    return lo


def test_anchor_principle_is_independent_and_attractor_integration_does_not_replace_it():
    """Посылки УГМ: (МаксΦ) независима от аксиом и от жизни в окне; максимум Φ аттрактора её не заменяет.

    Якорь ρ_t = (1 − t)I/7 + t uu†, t = 0,9 (α = ½, κ = 100 > κ_c(0,9) = 75,56): (Eq) выполнено,
    Φ(ρ_t) = 6t² = 4,86 < 6, а сток в окне есть — P ∈ (2/7, 3/7]. Унитальный якорь I/7: Φ = 0, (Eq) верно,
    голоном мёртв. Аттрактор постоянного якоря зависит лишь от d = Σ(ρ_a)ᵢᵢ² и s = P(ρ_a) − d, и его
    интеграция равна η²s/d; при фиксированном d она растёт с s (чистый якорь лучше). Принцип
    «наибольшая интеграция аттрактора» выбирает uu† лишь при κ выше κ_* ≈ 1,012 κ_c(α): при α = 0,
    κ = 16,8 чистый якорь с d = 1/7 + 10⁻⁴ даёт Φ_att = 1,25155 > 1,25148 у uu†; при κ = 20 uu† выигрывает
    у всех якорей сетки (чистых и смешанных).
    """
    alpha, kap, t = 0.5, 100.0, 0.9
    u = np.ones(7) / np.sqrt(7)
    rho = (1 - t) * np.eye(7) / 7 + t * np.outer(u, u)
    assert np.allclose(np.diag(rho), 1 / 7) and abs(integration(rho) - 6 * t * t) < 1e-12
    e = _top_window_sink(1 / 7, 6 * t * t / 7, kap, alpha)
    G0 = (1 - e) * np.eye(7) / 7 + e * rho
    f = _living_generator(np.zeros((7, 7)), lambda Y: rho.astype(complex), kap, alpha)
    G = _stationary(f, G0.astype(complex))
    assert np.linalg.norm(f(G)) < 1e-10 and 2 / 7 < purity(G) <= 3 / 7 and np.allclose(G, G0, atol=1e-6)
    assert integration(np.eye(7) / 7) == 0
    phi_att = lambda d, s, k, a: (lambda x: None if x is None else x * x * s / d)(_top_window_sink(d, s, k, a))
    a0, b0 = phi_att(1 / 7, 6 / 7, 16.8, 0.0), phi_att(1 / 7 + 1e-4, 6 / 7 - 1e-4, 16.8, 0.0)
    assert b0 > a0 + 3e-5
    best = phi_att(1 / 7, 6 / 7, 20.0, 0.0)
    for d in np.linspace(1 / 7 + 1e-4, 0.5, 40):
        for frac in (1.0, 0.9, 0.6):
            v = phi_att(d, frac * (1 - d), 20.0, 0.0)
            assert v is None or v < best
    for a, kc in ((0.0, 16.63), (0.5, 29.25), (1.0, 59.34)):                     # κ_* ∈ (1,005; 1,02)·κ_c
        slope = [phi_att(1 / 7 + 1e-6, 6 / 7 - 1e-6, r * kc, a) - phi_att(1 / 7, 6 / 7, r * kc, a)
                 for r in (1.005, 1.02)]
        assert slope[0] > 0 > slope[1]
    for s_lo, s_hi in ((0.5, 0.6), (0.7, 0.8)):
        x_lo, x_hi = _top_window_sink(0.2, s_lo, 60.0, 0.0), _top_window_sink(0.2, s_hi, 60.0, 0.0)
        assert x_lo is not None and x_hi * x_hi * s_hi > x_lo * x_lo * s_lo


def test_t222_window_has_no_resource_optimum_and_the_renyi_family_splits():
    """T-222 (переформулирована 26.09.2026): окно 2/7 < P ≤ 3/7 не выделяет ресурсного оптимума.

    (i) Всякое состояние окна строго доминируется подмесом I/7: ρ_t = (1 − t)ρ + t I/7 остаётся в окне,
    и H_α растёт при α ∈ {½, 1, 2, 3, ∞} (F_α = k_BT(log 7 − H_α) падает). (iii) На сфере P = 2/7
    F_1 и F_∞ минимизируются разными спектрами: s_1 (спектр Γ_{1/√6}) — H_1 = 1,6019, H_∞ = 0,7077;
    трёхуровневый s_3 — H_1 = 1,3909, H_∞ = 1,1783; s_1 — максимум H_1 на сфере (случайные спектры
    не превосходят). (iv) s_1 не мажорируется (⅓, ⅓, ⅓, 0, 0, 0, 0): 0,4928 > ⅓. Прежняя T-222
    («ρ* = φ(Γ) — Парето-оптимум всех монотонов, терминальный объект») отозвана этими числами.
    """
    def renyi(lam, a):
        lam = np.asarray(lam, float)
        lam = lam[lam > 1e-15]
        if a == 1:
            return float(-(lam * np.log(lam)).sum())
        if a == np.inf:
            return float(-np.log(lam.max()))
        return float(np.log((lam ** a).sum()) / (1 - a))
    alphas = (0.5, 1, 2, 3, np.inf)
    rng = np.random.default_rng(222)
    uni = np.full(7, 1 / 7)
    checked = 0
    while checked < 200:
        lam = rng.dirichlet(np.full(7, 0.4))
        P = float((lam ** 2).sum())
        if not 2 / 7 < P <= 3 / 7:
            continue
        t = 0.5 * (1 - np.sqrt((1 / 7) / (P - 1 / 7)))                    # half-way to the sphere
        lt = (1 - t) * lam + t * uni
        Pt = float((lt ** 2).sum())
        assert 2 / 7 < Pt < P
        for a in alphas:
            assert renyi(lt, a) > renyi(lam, a) + 1e-9
        checked += 1
    r6, r3 = np.sqrt(6), np.sqrt(3)
    s1 = np.array([(1 + r6) / 7] + [(6 - r6) / 42] * 6)
    s3 = np.array([(3 + 2 * r3) / 21] * 3 + [(2 - r3) / 14] * 4)
    eta = 1 / r6
    gam = np.array([(1 + 6 * eta) / 7] + [(1 - eta) / 7] * 6)          # spectrum of Γ_{1/√6}
    for s in (s1, s3, gam):
        assert abs(s.sum() - 1) < 1e-12 and abs((s ** 2).sum() - 2 / 7) < 1e-12
    assert np.allclose(np.sort(gam), np.sort(s1))
    assert abs(renyi(s1, 1) - 1.6019) < 1e-4 and abs(renyi(s3, 1) - 1.3909) < 1e-4
    assert abs(renyi(s1, np.inf) - 0.7077) < 1e-4 and abs(renyi(s3, np.inf) - 1.1783) < 1e-4
    assert renyi(s1, 1) > renyi(s3, 1) and renyi(s3, np.inf) > renyi(s1, np.inf)
    best_h1 = 0.0
    for _ in range(20000):
        lam = rng.dirichlet(np.full(7, 0.7))
        c = np.sqrt((1 / 7) / ((lam ** 2).sum() - 1 / 7))
        mu = uni + c * (lam - uni)
        if mu.min() < 0:
            continue
        best_h1 = max(best_h1, renyi(mu, 1))
    assert 1.5 < best_h1 <= renyi(s1, 1) + 1e-12
    third = np.array([1 / 3] * 3 + [0.0] * 4)
    majorized = all(np.sort(s1)[::-1][:k].sum() <= np.sort(third)[::-1][:k].sum() + 1e-12 for k in range(1, 8))
    assert not majorized and s1.max() > 1 / 3


def test_t346_regeneration_rate_is_fixed_by_no_route():
    """T-346: темп регенерации κ не фиксируется ни одним из пяти путей — числа каждого запрета.

    (a) Порог κ_c(α) = 2/(3 max Q) — единственный вещественный корень неприводимого целого многочлена
    степени 7 с группой Галуа S₇ (разложения mod p типов (7) и (2,5)): в радикалах не выражается.
    (b) Ветвь стока η₊(κ) строго растёт; Φ(κ) = 6η₊² строго вогнута, растёт от Φ_c = 1,2261 к Φ_∞ = 3/2
    (α = 0); зазор якобиана, Ω_c, зазор/κ и Ω_c/κ монотонны — внутреннего экстремума нет. Оптимум
    (Φ − a)/κ есть при всяком κ > κ_c ровно для одного a = Φ − κΦ′: a = 0 → 1,0102κ_c, a = 1 → 1,1512κ_c.
    (c) При κ = κ_c: Ω_c = 0, и всякий диагональный H с ненулевым разбросом снимает все состояния с
    P > 2/7; Ω_c ≈ C√(κ − κ_c), C = 0,547 / 0,472 / 0,393. (d) Во всяком стационарном состоянии V_full
    κg_V ≥ 4/(3(√6 − 2 + c)) = 1,703 / 2,164 / 2,966, а равновесие любых унитарно-инвариантных норм
    κg_V‖φ − id‖ = ‖D_Ω‖ даёт κg_V ≤ 1 (сингулярные числа R ×6, 1 − kc ≥ ⅔ ×42 против 0 ×6, ⅔ ×42).
    Канонический κ(Γ) = ω₀(1/7 + |γ_OE||γ_OU|/γ_OO·Coh_E) с φ_J держит окно лишь при ω₀ > 111,35 /
    196,45 / 399,40. (e) Огрубление, ковариантное относительно коллинеаций и калибровки, действует на
    семействе как η ↦ tη; κ′ = κ лишь при t = 1, при t = 0,99 от 2κ_c сток уходит с ветви за 8 шагов.
    """
    import sympy as sp
    from scipy.optimize import brentq, minimize_scalar
    polys = {0.0: [317898, -5257737, -455850, -245068, 65616, -13040, 672, -64],
             0.5: [33870825, -989701632, -31625712, -55111328, 13010688, -1893376, 110592, -8192],
             1.0: [181521, -10774620, 147258, -680400, 139644, -16848, 1056, -64]}
    primes = {0.0: (37, 53), 0.5: (13, 29), 1.0: (5, 89)}
    x = sp.symbols("x")
    lo, hi = 1 / np.sqrt(6), 1 / np.sqrt(3)
    kcs, cs = {}, {}
    for alpha, co in polys.items():
        c = (1 - alpha) / 3
        r = minimize_scalar(lambda e: -_q_window(e, c), bounds=(lo, hi), method="bounded",
                            options={"xatol": 1e-13})
        kc, es = (2 / 3) / (-r.fun), r.x
        kcs[alpha] = (kc, es)
        roots = np.roots(co)
        real = roots[np.abs(roots.imag) < 1e-9].real
        assert len(real) == 1 and abs(real[0] - kc) < 1e-6 * kc                    # единственный корень
        f = sp.Poly(co, x)
        p7, p25 = primes[alpha]
        for p, want in ((p7, [7]), (p25, [2, 5])):
            degs = sorted(sp.Poly(g, x, modulus=p).degree() for g, m in
                          sp.Poly(f.as_expr(), x, modulus=p).factor_list()[1] for _ in range(m))
            assert degs == want and co[0] % p != 0                                 # (7): неприводим; (2,5): транспозиция
        assert sp.discriminant(f) % p25 != 0
        # (b) ветвь стока, параметризованная η: κ(η) = 2/(3Q), Φ = 6η²
        einf = brentq(lambda e: _q_window(e, c), es, hi)
        e = np.linspace(es + 1e-6, einf - 1e-6, 100001)
        k = (2 / 3) / _q_window(e, c)
        dk = np.gradient(k, e)
        phik = 12 * e / dk
        assert np.all(dk > 0) and np.all(np.diff(phik)[5:-5] < 0)                   # η₊ растёт, Φ вогнута
        a = 6 * e ** 2 - k * phik
        assert np.all(np.diff(a) > 0) and a[0] < -1e3 and abs(a[-1] - 6 * einf ** 2) < 1e-2
        g, R = 6 * e ** 2 - 1, 1 / (1 + 6 * e ** 2)
        lam_y = k * e * np.gradient(_q_window(e, c), e)
        gap = np.minimum(np.minimum(-lam_y, k * g * R), 2 / 3 + k * g * (1 - (1 - R) * c))
        assert np.all(np.diff(gap) > 0) and np.all(np.diff(gap / k) > 0)
        if alpha == 0.0:
            assert abs(6 * es ** 2 - 1.2261) < 1e-4 and abs(einf - 0.5) < 1e-9
            for off, want in ((0.0, 1.0102), (1.0, 1.1512)):
                assert abs(k[np.argmax((6 * e ** 2 - off) / k)] / kc - want) < 5e-4
        # (c) Ω_c(κ) — наибольший разброс диагональных энергий, при котором окно живёт
        P = np.linspace(2 / 7 + 1e-9, 3 / 7, 200001)

        def om2(kap):
            A, B = _anchor_window_parts(P, kap, c)
            return np.max(6 / 7 * B ** 2 / (P - 1 / 7) - A ** 2)
        assert abs(om2(kc)) < 1e-8
        C = np.sqrt(om2(kc * 1.001) / (kc * 0.001))
        assert abs(C - {0.0: 0.5476, 0.5: 0.4722, 1.0: 0.3932}[alpha]) < 1e-3
        oms = [np.sqrt(om2(kc * s)) / (kc * s) for s in (1.01, 1.1, 2, 10, 100)]
        assert np.all(np.diff(oms) > 0)
        # при κ = κ_c и любом разбросе ω: G(P) < G₀(P) ≤ 0 на всём окне
        w = np.array([0.0, 1e-3, 0, 0, 0, 0, 0])
        A, B = _anchor_window_parts(P, kc, c)
        G = sum(B ** 2 / (A ** 2 + (w[i] - w[j]) ** 2) for i in range(7) for j in range(7) if i != j) / 49 - (P - 1 / 7)
        assert np.max(G) < 0
        # (d) нижняя граница κg_V в V_full и равновесие норм
        R = 1 / (7 * P)
        den = R * (1 + np.sqrt(6 * (7 * P - 1))) / 7 - 1 / 7 - (1 - R) * (1 - c) * P / 2
        req = np.where(den > 0, (P / 3) / np.where(den > 0, den, 1), np.inf)
        edge = 4 / (3 * (np.sqrt(6) - 2 + c))
        assert np.argmin(req) == 0 and abs(req[0] - edge) < 1e-6
        assert abs(edge - {0.0: 1.7032, 0.5: 2.1640, 1.0: 2.9663}[alpha]) < 1e-4
        for Pv in (0.29, 0.32, 0.4):
            Rv, kv = 1 / (7 * Pv), 1 - 1 / (7 * Pv)
            s_reg = np.sort([Rv] * 6 + [1 - kv * c] * 42)[::-1]
            s_d = np.sort([0.0] * 6 + [2 / 3] * 42)[::-1]
            assert np.all(np.cumsum(s_reg) >= np.cumsum(s_d))                     # Ки Фан: ‖D_Ω‖ ≤ ‖φ − id‖
        m = lambda eta: 1 / 7 + (eta ** 2 / 7) * (1 + 12 * eta ** 2) / (7 * (1 + 6 * eta ** 2))
        r = minimize_scalar(lambda eta: -m(eta) * _q_window(eta, c), bounds=(lo, hi), method="bounded",
                            options={"xatol": 1e-13})
        assert abs((2 / 3) / (-r.fun) - {0.0: 111.352, 0.5: 196.447, 1.0: 399.395}[alpha]) < 2e-3
        cs[alpha] = c
    # (d) частичные проверки операторов: сингулярные числа φ_Γ − id и D_Ω на бесследовых
    E = _jacobian_basis()
    c, P0 = cs[0.5], 0.32
    R0 = 1 / (7 * P0)
    u = np.ones(7) / np.sqrt(7)
    uu = np.outer(u, u)
    reg = lambda X: (1 - R0) * (np.diag(np.diag(X)) + c * (X - np.diag(np.diag(X)))) + R0 * np.trace(X) * uu - X
    dom = lambda X: (np.diag(np.diag(X)) + (X - np.diag(np.diag(X))) / 3) - X
    for op, want in ((reg, sorted([R0] * 6 + [1 - (1 - R0) * c] * 42)), (dom, sorted([0.0] * 6 + [2 / 3] * 42))):
        M = np.array([[np.real(np.trace(Ea.conj().T @ op(Eb))) for Eb in E] for Ea in E])
        assert np.allclose(np.sort(np.linalg.svd(M, compute_uv=False)), want, atol=1e-12)
    # (e) огрубление η ↦ tη уводит с ветви стока
    c = cs[0.0]
    kc, es = kcs[0.0]
    einf = brentq(lambda e: _q_window(e, c), es, hi)
    eta = brentq(lambda e: 2 * kc * _q_window(e, c) - 2 / 3, es, einf)
    k1 = (2 / 3) / _q_window(0.99 * eta, c)
    assert abs(k1 - 26.341) < 2e-3 and k1 < 2 * kc
    n = 0
    while eta > es:
        eta, n = 0.99 * eta, n + 1
    assert n == 8
def _generated_algebra_dim(ops, n):
    flat = [np.eye(n).ravel()]
    frontier = list(ops)
    while frontier:
        new = []
        for X in frontier:
            if np.linalg.matrix_rank(np.array(flat + [X.ravel()]), tol=1e-8) > len(flat):
                flat.append(X.ravel())
                new.append(X)
        frontier = [a @ b for a in new for b in ops]
    return len(flat)


def _hurwitz_radon(n):
    b = 0
    while n % 2 == 0:
        n //= 2
        b += 1
    a, r = divmod(b, 4)
    return 2 ** r + 8 * a


def test_fermion_module_premise_is_the_holons_product_acting_on_matter():
    """T-347(б): (Кл₀) ⟺ (Мод) — произведение голонома действует на материи; 𝒮 не выбирается.

    (Мод): линейное ρ: 𝕆 → End_ℝ(F), ρ(1) = 1, ρ(x)ρ(x) = ρ(x²) (левый альтернативный закон), ρ коммутирует
    с i пространства ℋ. L и R на 𝕆 ему подчиняются; ρ(e_k) — антикоммутирующие комплексные структуры;
    алгебра, порождённая семью L_{e_k} на ℝ⁸, — M₈(ℝ) (размерность 64, коммутант ℝ), так что неприводимые
    модули восьмимерны и их два: объём L_{e_1}⋯L_{e_7} = −1, объём R = +1. Октонионное сопряжение c
    переводит L_{e_k} в −R_{e_k}: система Клиффорда {iR_{e_k}, J, iJ} на ℂ⊗𝕆 — тоже Cl(9,0), её антикоммутант
    семи — снова двумерен, и её 𝔰𝔭𝔦𝔫(9) — ровно c·𝔰𝔭𝔦𝔫(9)_L·c: оба модуля дают одну и ту же группу T-326.
    Наименьшее ρ- и i-устойчивое пространство, содержащее ℋ (ранг 14), — всё 𝒮 (ранг 16).
    """
    L = [_lmul8(k) for k in range(8)]
    R = [_rmul8(k) for k in range(8)]
    rng = np.random.default_rng(346)
    for _ in range(5):
        x = rng.normal(size=8)
        x2 = omul(x, x)
        for M in (L, R):
            Mx = sum(x[k] * M[k] for k in range(8))
            assert np.allclose(Mx @ Mx, sum(x2[k] * M[k] for k in range(8)))
    for a in range(1, 8):
        for b in range(1, 8):
            assert np.allclose(L[a] @ L[b] + L[b] @ L[a], -2 * (a == b) * np.eye(8))
    vL = functools.reduce(np.matmul, L[1:])
    vR = functools.reduce(np.matmul, R[1:])
    assert np.allclose(vL, -np.eye(8)) and np.allclose(vR, np.eye(8))
    assert _generated_algebra_dim(L[1:], 8) == 64 and _real_commutant_dim(L[1:], 8) == 1
    cj = np.diag([1.0] + [-1.0] * 7)
    assert all(np.allclose(cj @ L[k] @ cj, -R[k]) for k in range(1, 8))
    d = _sm_on_complex_octonions()
    imul, conj, cl = d["imul"], d["conj"], d["cl"]
    gR = [imul @ cl(R[k]) for k in range(1, 8)] + [conj, imul @ conj]
    for a in range(9):
        for b in range(9):
            assert np.allclose(gR[a] @ gR[b] + gR[b] @ gR[a], 2 * (a == b) * np.eye(16))
    basis = [np.outer(np.eye(16)[i], np.eye(16)[j]) for i in range(16) for j in range(16)]
    rows = np.vstack([np.array([(S @ X + X @ S).ravel() for S in basis]).T for X in gR[:7]])
    assert 256 - np.linalg.matrix_rank(rows, tol=1e-9) == 2
    C = cl(cj)
    spinR = [gR[a] @ gR[b] / 2 for a in range(9) for b in range(a + 1, 9)]
    assert max(_span_residual(C @ X @ C, d["spin9"]) for X in spinR) < 1e-9
    V = np.array([np.eye(16)[i] for i in list(range(1, 8)) + list(range(9, 16))]).T
    assert np.linalg.matrix_rank(V) == 14
    ops = [cl(L[k]) for k in range(1, 8)] + [imul]
    for _ in range(2):
        V = np.hstack([V] + [o @ V for o in ops])
    assert np.linalg.matrix_rank(V, tol=1e-9) == 16


def test_no_holon_property_maximality_or_minimality_gives_the_bridge_premises():
    """T-347(а), (в)–(д): пути к (Кл₀), (P), (W) через свойства голонома, максимальность и минимальность закрыты.

    (а) Как 𝔤₂-модуль 𝒮 = ℂη₀ ⊕ ℋ: 𝔤₂ убивает η₀ и действует на ℋ как на голоном — симметрия голонома не
    отличает спинорный модуль от ℋ плюс прямая. Отличает центр накрытия: exp(π L_{e_1}L_{e_2}) = −1 на 𝕆,
    поворот на 2π в SO(7) = +1 на ℝ⁷; подлинно спинорные модули Spin(7) — 8, 48, 112, …, тензорные — 1, 7, 21, 27, 35.
    (в) Число Гурвица–Радона ρ(14) = ρ(98) = 2, ρ(8) = 8, ρ(16) = 9: на ℋ = ℝ¹⁴ помещается одна комплексная
    структура из антикоммутирующих, семь требуют 8 | dim; кватернионной структуры на ℂ⁷ нет:
    det(AĀ) = |det A|² ≥ 0 ≠ det(−1₇) = −1. Точные представления M₇(ℂ) имеют размерность 14k; общая с модулем 𝕆 — 112 | dim.
    (г) Наименьший спинорный сомножитель, совместимый с T-329, — n = 1: F₁ = 𝒮_ℂ, 16 вейлевских полей,
    ΣY = ΣY³ = 0, но dim Herm(ℂ¹) = 1 — нет пространственного направления; n = 2 — первое с ним (dim Herm = 4).
    (д) Модель ¬(Кл₀) с M = ℂ⁷ векторна: матрицы 𝔤₂ вещественны, ℂ⁷ ≅ своему сопряжённому; U(1) от i даёт
    Tr Q³ = Tr Q = 7 на компоненту W.
    """
    d = _sm_on_complex_octonions()
    for X in G2:
        M = np.zeros((8, 8))
        M[1:, 1:] = X
        Xc = d["cl"](M)
        assert np.abs(Xc[:, 0]).max() + np.abs(Xc[:, 8]).max() == 0.0
        assert np.isrealobj(X) and np.allclose(X, -X.T)
    L = [_lmul8(k) for k in range(8)]
    assert np.allclose(expm(np.pi * L[1] @ L[2]), -np.eye(8))
    E = np.zeros((7, 7))
    E[0, 1], E[1, 0] = -1.0, 1.0
    assert np.allclose(expm(2 * np.pi * E), np.eye(7))
    from fractions import Fraction as Fr
    rho0 = (Fr(5, 2), Fr(3, 2), Fr(1, 2))

    def dim_b3(lam):
        lv = [lam[i] + rho0[i] for i in range(3)]
        num = den = Fr(1)
        for i in range(3):
            num, den = num * lv[i], den * rho0[i]
            for j in range(i + 1, 3):
                num *= (lv[i] - lv[j]) * (lv[i] + lv[j])
                den *= (rho0[i] - rho0[j]) * (rho0[i] + rho0[j])
        return int(num / den)
    tri = [(a, b, c) for a in range(6) for b in range(a + 1) for c in range(b + 1)]
    spinorial = sorted(dim_b3(tuple(Fr(2 * t + 1, 2) for t in w)) for w in tri)
    tensorial = sorted(dim_b3(w) for w in tri)
    assert spinorial[:3] == [8, 48, 112] and tensorial[:5] == [1, 7, 21, 27, 35]
    assert {n: _hurwitz_radon(n) for n in (8, 14, 16, 98)} == {8: 8, 14: 2, 16: 9, 98: 2}
    rng = np.random.default_rng(7)
    for _ in range(5):
        A = rng.normal(size=(7, 7)) + 1j * rng.normal(size=(7, 7))
        assert np.linalg.det(A @ A.conj()).real > 0 and np.linalg.det(-np.eye(7)) < 0
    assert np.lcm(14, 16) == 112 and 14 % 16 != 0
    Y = {Fr(1, 6): 6, Fr(-1, 2): 2, Fr(-2, 3): 3, Fr(1, 3): 3, Fr(1): 1, Fr(0): 1}
    assert sum(Y.values()) == 16
    assert sum(y * m for y, m in Y.items()) == 0 and sum(y ** 3 * m for y, m in Y.items()) == 0
    assert [n * n for n in (1, 2, 3)] == [1, 4, 9]
    assert len(_invariant_quadratic_forms(2)) == 1
    q = np.ones(7)
    assert q.sum() == 7 and (q ** 3).sum() == 7


def _ptrace_last(rho, d_keep, d_drop=7):
    """След по последнему множителю ℂ^{d_drop}: состояние уровня M+1 → уровня M башни."""
    return np.einsum("ajbj->ab", rho.reshape(d_keep, d_drop, d_keep, d_drop))


def test_holon_tower_trace_entropy_is_nonpositive_and_monotone():
    """T-348(а): башня ⊗(M₇, tr₇) — след согласован, S_tr = S − M ln 7 ≤ 0, равенство только в I/7^M.

    Энтропия относительно нормированного следа есть −D(ρ‖I/7^M); сужение на меньший уровень
    (след по последнему голоному) её не уменьшает — это монотонность относительной энтропии.
    """
    rng = np.random.default_rng(348)
    a = rng.normal(size=(49, 49)) + 1j * rng.normal(size=(49, 49))
    assert abs(np.trace(np.kron(a, np.eye(7))).real / 343 - np.trace(a).real / 49) < 1e-12
    for M in (1, 2, 3):
        d = 7 ** M
        assert abs(entropy(np.eye(d) / d) - M * np.log(7)) < 1e-9          # S_tr(I/7^M) = 0
        for _ in range(3):
            rho = random_state(rng, d)
            s_tr = entropy(rho) - M * np.log(7)
            assert s_tr < 0
            if M > 1:
                red = _ptrace_last(rho, 7 ** (M - 1))
                assert entropy(red) - (M - 1) * np.log(7) >= s_tr - 1e-12
    # проекторы уровня M имеют след k/7^M; 7^M нечётно — след 1/2 недостижим ни на каком уровне
    for M in range(1, 9):
        assert 7 ** M % 2 == 1
        assert abs(min(abs(k / 7 ** M - 0.5) for k in range(7 ** M + 1)) - 0.5 / 7 ** M) < 1e-15
    # показания регистра глубины, вложенные измельчением (новый голоном — младшая цифра):
    # проектор на показания n/7^M ∈ [a, b) имеет след, отличающийся от b − a не более чем на 2/7^M
    for M in (2, 4, 6):
        n = np.arange(7 ** M) / 7 ** M
        for lo, hi in ((0.1, 0.35), (1 / 3, 0.9)):
            assert abs(np.mean((n >= lo) & (n < hi)) - (hi - lo)) <= 2 / 7 ** M


def test_living_holon_costs_at_least_0344_nats_below_the_trace():
    """T-348(г): каждый живой голоном (P > 2/7) снижает S_tr больше чем на D* = 0,34406 нат.

    D* = ln 7 − S((1+√6)/7, (6−√6)/42 ×6) — минимум D(ρ‖I/7) при P = 2/7 (одна доминирующая мода
    плюс шесть равных); максимум при P = 2/7 — 0,64817 на (a, a, a, b, 0, 0, 0), a = (21+√21)/84.
    Для двух голономов D(ρ₁₂‖I/49) = D(ρ₁‖I/7) + D(ρ₂‖I/7) + I(1:2) ≥ сумме — отсюда S_tr ≤ −L·D*.
    Верность I/7 бесконечному произведению живых голономов ≤ 0,85505^M → 0: оно не нормально на R.
    """
    lam = np.array([(1 + np.sqrt(6)) / 7] + [(6 - np.sqrt(6)) / 42] * 6)
    d_star = np.log(7) - entropy(np.diag(lam))
    assert abs((lam ** 2).sum() - 2 / 7) < 1e-12 and abs(d_star - 0.34406) < 1e-5
    a = (21 + np.sqrt(21)) / 84
    top = np.array([a, a, a, 1 - 3 * a, 0, 0, 0])
    assert abs((top ** 2).sum() - 2 / 7) < 1e-12
    assert abs(np.log(7) - entropy(np.diag(top)) - 0.64817) < 1e-5
    rng = np.random.default_rng(2348)
    hits = 0
    for _ in range(4000):
        x = rng.exponential(size=7) ** rng.uniform(0.5, 4)
        p = x / x.sum()
        P = (p ** 2).sum()
        if P > 2 / 7:
            hits += 1
            assert np.log(7) - entropy(np.diag(p)) > d_star
        if abs(P - 2 / 7) < 2e-3:
            assert d_star - 1e-3 < np.log(7) - entropy(np.diag(p)) < 0.64817 + 1e-3
    assert hits > 500
    fid = np.sqrt(lam).sum() ** 2 / 7
    assert abs(fid - 0.85504) < 1e-5 and fid ** 100 < 2e-7
    for _ in range(20):                                   # два голонома с живыми маргиналами
        v = rng.normal(size=(49, 3)) + 1j * rng.normal(size=(49, 3))
        rho = v @ v.conj().T
        rho /= np.trace(rho).real
        m1 = _ptrace_last(rho, 7)
        m2 = np.einsum("jajb->ab", rho.reshape(7, 7, 7, 7))
        if purity(m1) > 2 / 7 and purity(m2) > 2 / 7:
            assert entropy(rho) - 2 * np.log(7) < -2 * d_star


def test_lambda_as_a_holon_count_is_a_reparametrisation():
    """T-348(е): e^{S_dS} = 7^M при наблюдаемом Λ даёт M = 1,677·10¹²² — пересчёт Λ, не вывод.

    S_dS = 3π/(Λ ℓ_P²), Λ = 1,1056·10⁻⁵² м⁻², ℓ_P² = 2,6123·10⁻⁷⁰ м²; M ↦ Λ — строго
    убывающая биекция, и ни одно утверждение корпуса не фиксирует M.
    """
    lam_obs, lp2 = 1.1056e-52, 2.61226e-70
    s_ds = 3 * np.pi / (lam_obs * lp2)
    M = s_ds / np.log(7)
    assert abs(s_ds / 3.2633e122 - 1) < 1e-4 and abs(M / 1.6770e122 - 1) < 1e-4
    Ms = np.array([1e120, 1e121, M, 1e123])
    lams = 3 * np.pi / (lp2 * Ms * np.log(7))
    assert np.all(np.diff(lams) < 0) and abs(lams[2] / lam_obs - 1) < 1e-12


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
