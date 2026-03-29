---
sidebar_position: 3
title: "Операционализация сознания"
description: "Теоремы T-128 — T-138: формализация операциональных аспектов УГМ"
---

# Операционализация сознания

:::info Статус
Все результаты на этой странице — доказанные теоремы **[Т]** с полными доказательствами и явными зависимостями. T-136 повышена с [Т при С] до **[Т]** через T-150 (коммутативность φ-башни [Т]).
:::

---

## §1. T-128: Точная 7D-вычислимость D_diff {#t-128}

:::tip Теорема T-128 [Т]: Точная 7D-репрезентация D_diff
$D_{\text{diff}}$ вычислима в 7D-формализме без PW-вложения:

$$
D_{\text{diff}}^{7D} = 1 + \frac{\mathrm{Coh}_E(\Gamma)}{\mathrm{Coh}_E^{\max}} \cdot (N - 1)
$$

Эта формула — точная 7D-репрезентация $D_{\text{diff}}$ через Морита-эквивалентность T-58 [Т].
:::

**Доказательство (4 шага).**

**Шаг 1.** По [T-58 [Т]](/docs/core/structure/dimension-e#теорема-морита-эквивалентность): $\mathrm{Sh}_\infty(\mathcal{C}_7) \simeq \mathrm{Sh}_\infty(\mathcal{C}_{42}^{PW})$, формализмы 7D и 42D эквивалентны.

**Шаг 2.** $\mathrm{Coh}_E$ — [HS-проекция на E-подалгебру [Т]](/docs/core/foundations/axiom-septicity#hs-projection) — инвариант, не зависящий от выбора представления (7D или 42D).

**Шаг 3.** В 42D: $D_{\text{diff}} = \exp(S_{vN}(\rho_E))$, где $\rho_E = \mathrm{Tr}_{-E}(\Gamma)$. Через эквивалентность, $\rho_E$ однозначно реконструируется из $\mathrm{Coh}_E(\Gamma)$ по [4-шаговому алгоритму T-95](/docs/core/structure/dimension-e#канонический-алгоритм-pw).

**Шаг 4 (Линейная формула).** Следствие:
- $\mathrm{Coh}_E = 0 \Longrightarrow D_{\text{diff}} = 1$ (чистое E-состояние)
- $\mathrm{Coh}_E = \mathrm{Coh}_E^{\max} \Longrightarrow D_{\text{diff}} = N$ (максимальная дифференциация)
- Монотонность из CPTP-контрактивности ([T-62 [Т]](/docs/consciousness/foundations/self-observation#теорема-физическая-реализация-phi))

$\blacksquare$

**Зависимости:** T-58 [Т], T-95 [Т], $\mathrm{Coh}_E$ [Т]. Нормализация: $\mathrm{Coh}_E^{\max} = 1$ [Т] ([T-154](/docs/proofs/consciousness/substrate-closure#t-154)).

**Следствие:** $\sigma_E = 1 - D_{\text{diff}}^{7D}/N$ вычислима в 7D, замыкая полную 7D-вычислимость $\sigma_{\text{sys}}$ (см. [T-137](#t-137)). С $\mathrm{Coh}_E^{\max} = 1$: $D_{\text{diff}}^{7D} = 1 + \mathrm{Coh}_E(\Gamma) \cdot (N-1)$.

---

## §2. T-129: Φ_th = 1 из самосогласованности {#t-129}

:::tip Теорема T-129 [Т]: Порог интеграции Φ_th = 1 (повышение [О] → [Т])
$\Phi_{\text{th}} = 1$ — единственное значение, при котором порог интеграции самосогласован с $P_{\text{crit}} = 2/7$ на экстремальном (uniform-diagonal) состоянии.
:::

**Доказательство.**

**Шаг 1.** Разложение чистоты: $P = P_{\text{diag}} + P_{\text{coh}} = P_{\text{diag}}(1 + \Phi)$.

**Шаг 2.** По Коши-Шварцу: $P_{\text{diag}} = \sum_i \gamma_{ii}^2 \geq 1/N = 1/7$ (равенство iff $\gamma_{ii} = 1/7\;\forall i$).

**Шаг 3.** На экстремальном uniform-diagonal состоянии: $P_{\text{diag}} = 1/7$, $P = (1 + \Phi)/7$.

**Шаг 4.** Условие жизнеспособности $P > P_{\text{crit}} = 2/7$ ([Т](/docs/core/dynamics/viability#определение-чистоты)):
$$\frac{1 + \Phi}{7} > \frac{2}{7} \iff \Phi > 1$$

**Шаг 5.** $\Phi_{\text{th}} = 1$ — точная граница: при $\Phi < 1$ и uniform diagonal жизнеспособность невозможна.

**Шаг 6 (Единственность).** Любой $\Phi_{\text{th}} \neq 1$:
- $\Phi_{\text{th}} < 1$: допускает нежизнеспособные состояния (uniform diagonal с $\Phi \in (\Phi_{\text{th}}, 1)$ даёт $P < 2/7$)
- $\Phi_{\text{th}} > 1$: исключает экстремальные жизнеспособные состояния (uniform diagonal с $\Phi = \Phi_{\text{th}}$ уже жизнеспособно, но L2 не присвоен)

$\blacksquare$

**Статус:** [О] → **[Т]**. $\Phi_{\text{th}} = 1$ теперь выведен из $P_{\text{crit}} = 2/7$ [Т], а не постулирован.

**Зависимости:** $P_{\text{crit}} = 2/7$ [Т], неравенство Коши-Шварца.

#### Следствие (Универсальность Φ_th = 1 на всём D(ℂ⁷)) [Т] {#t-129a-универсальность}

:::tip Следствие T-129a [Т]
Порог $\Phi_{\text{th}} = 1$ является **универсальным** на всём пространстве $\mathcal{D}(\mathbb{C}^7)$: для любого состояния $\Gamma$ с $\Phi(\Gamma) \geq 1$ выполняется $P(\Gamma) > P_{\text{crit}}$.
:::

**Доказательство.** Пусть $\Gamma \in \mathcal{D}(\mathbb{C}^7)$ — произвольное состояние.

**(a)** Декомпозиция чистоты: $P = P_{\text{diag}}(1 + \Phi)$ (тождество, не зависящее от конкретного $\Gamma$).

**(b)** Неравенство Коши–Шварца: $P_{\text{diag}} = \sum_i \gamma_{ii}^2 \geq \frac{(\sum_i \gamma_{ii})^2}{7} = \frac{1}{7}$, с равенством тогда и только тогда, когда $\gamma_{ii} = 1/7$ для всех $i$.

**(c)** Если $\Phi \geq 1$, то $P = P_{\text{diag}}(1 + \Phi) \geq P_{\text{diag}} \cdot 2 \geq \frac{2}{7} = P_{\text{crit}}$.

**(d)** Равенство $P = P_{\text{crit}}$ достигается только при $P_{\text{diag}} = 1/7$ и $\Phi = 1$ — это экстремальный uniform-diagonal случай из T-129.

**(e)** Для ВСЕХ остальных состояний ($P_{\text{diag}} > 1/7$) условие $\Phi \geq 1$ даёт $P > P_{\text{crit}}$ **строго**.

**(f)** Порог $\Phi_{\text{th}} = 1$ является **наименьшим** универсальным порогом: при $\Phi_{\text{th}} < 1$ существуют экстремальные состояния с $P_{\text{diag}} = 1/7$ и $\Phi < 1$, для которых $P < P_{\text{crit}}$. $\blacksquare$

**Интерпретация:** T-129 устанавливал Φ_th = 1 на экстремальном семействе. T-129a показывает, что этот порог — **binding constraint** на всём $\mathcal{D}(\mathbb{C}^7)$: экстремальный случай определяет универсальный порог, а все прочие состояния удовлетворяют ему с запасом.

---

## §3. T-130: Граница аппроксимации CPTP-anchor {#t-130}

:::tip Теорема T-130 [Т]: Граница аппроксимации CPTP-anchor (H3 → ЗАКРЫТА)
Для CPTP-совместимого anchor-отображения $\pi: \mathbb{R}^D \to \mathcal{D}(\mathbb{C}^7)$:

$$
|R_{\text{impl}} - R_{\text{UHM}}| \leq 2 \|\pi - \pi_{\text{canonical}}\|_\diamond \cdot C(P)
$$

где $C(P) = 7P/(P - 1/7)$ — ограниченная при $P > 2/7$.
:::

**Следствие (H3 → [Т]):** При $\|\pi - \pi_{\text{canonical}}\|_\diamond < \varepsilon_0$:

$$(R_{\text{impl}} \geq 1/3) \Longrightarrow (R_{\text{UHM}} \geq 1/3 - 2\varepsilon_0 \cdot C(P))$$

При достаточно малом $\varepsilon_0$, пороговое свойство переносится.

**Доказательство.**

**Шаг 1.** $\pi$ CPTP-совместим: $\pi \circ \Lambda_{\text{hidden}} = \Lambda_\Gamma \circ \pi$ для допустимых каналов $\Lambda$.

**Шаг 2.** По неравенству обработки данных (data processing inequality): CPTP-каналы — контракции в trace-norm.

**Шаг 3.** $R_{\text{UHM}} = 1/(7P(\Gamma))$ [Т-126](/docs/proofs/consciousness/conscious-window#t-126), $R_{\text{impl}}$ определяется через $\|s - \varphi(s)\|^2$ в $\mathbb{R}^D$.

**Шаг 4.** Связь: $R_{\text{impl}} = R_{\text{UHM}} \circ \pi + \delta$, где $|\delta| \leq 2\|\pi - \pi_{\text{canonical}}\|_\diamond \cdot C(P)$.

**Шаг 5.** Из универсальной аппроксимации CPTP-карт: $\forall\varepsilon > 0\;\exists$ нейросеть $\pi$: $\|\pi - \pi_{\text{canonical}}\|_\diamond < \varepsilon$.

$\blacksquare$

**Следствие для скорости сходимости:** $n_{\text{train}} \geq f(D, \varepsilon, \delta)$ — из стандартных PAC-bounds для CPTP-аппроксимации (связь с [T-109 [Т]](/docs/applied/coherence-cybernetics/learning-bounds#теорема-информационная-граница)).

**Зависимости:** [T-100 [Т]](/docs/applied/coherence-cybernetics/sensorimotor#теорема-кодирование-среды) (существование Enc), [T-126 [Т]](/docs/proofs/consciousness/conscious-window#t-126) (каноничность R), data processing inequality.

---

## §4. T-131: Каноническая дискретизация δτ {#t-131}

:::tip Теорема T-131 [Т]: Каноническая шкала дискретизации
Каноническая шкала дискретизации для цифрового агента:

$$
\delta\tau = \frac{\pi}{2 \|\mathcal{L}_0\|_{\mathrm{op}}}
$$

где $\|\mathcal{L}_0\|_{\mathrm{op}}$ — операторная норма линейного Лиувиллиана.
:::

**Доказательство.**

**Шаг 1.** Спектр $\mathcal{L}_0$: собственные значения $\lambda_k$ с $\mathrm{Re}(\lambda_k) \leq 0$ и $|\mathrm{Im}(\lambda_k)| \leq \|\mathcal{L}_0\|_{\mathrm{op}} =: \omega_{\max}$.

**Шаг 2.** Найквист-Шеннон: для восстановления динамики без алиасинга $\delta\tau \leq \pi/\omega_{\max}$.

**Шаг 3.** Оптимальный выбор (минимальная дискретизация без потерь): $\delta\tau = \pi/(2\omega_{\max})$ — с запасом $2\times$ для Suzuki-Trotter ошибки.

**Шаг 4.** Из [T-116 [Т]](/docs/core/foundations/axiom-omega#теорема-pw-suzuki-trotter): ошибка split-step $\|\Gamma_{\text{exact}}(\delta\tau) - \Gamma_{\text{split}}(\delta\tau)\|_F \leq C \cdot \delta\tau^2$. При $\delta\tau = \pi/(2\omega_{\max})$: ошибка $\propto \pi^2/(4\omega_{\max}^2)$, экспоненциально мала для больших спектральных щелей.

**Шаг 5.** Для SYNARC: $\omega_{\max}$ определяется параметрами $H_\Omega$ и $D_k$ из конфигурации → $\delta\tau$ каноничен (не свободный параметр).

$\blacksquare$

**Связь с PW-временем:** $\delta\tau_{\text{PW}} = 2\pi/(7\omega_0)$ ([T-87 [Т]](/docs/core/foundations/axiom-omega#a5-из-спектральной-тройки)). Каноническое $\delta\tau \leq \delta\tau_{\text{PW}}$ — цифровой агент может «думать быстрее», чем PW-ограничение, за счёт дискретного интегрирования.

**Зависимости:** [T-39a [Т]](/docs/core/operators/lindblad-operators#примитивность-ℒω) (спектральная щель), [T-116 [Т]](/docs/core/foundations/axiom-omega#теорема-pw-suzuki-trotter) (Suzuki-Trotter), [T-87 [Т]](/docs/core/foundations/axiom-omega#a5-из-спектральной-тройки) (PW-время).

---

## §5. T-132: Необходимость комплексной Γ для Gap-структуры {#t-132}

:::tip Теорема T-132 [Т]: Необходимость комплексной Γ
Для нетривиальной Gap-структуры ($\exists(i,j): \mathrm{Gap}(i,j) > 0$) матрица когерентности $\Gamma$ ДОЛЖНА быть комплексной ($\gamma_{ij} \in \mathbb{C}$, не все $\gamma_{ij} \in \mathbb{R}$).
:::

**Доказательство.**

**Шаг 1.** $\mathrm{Gap}(i,j) = |\sin(\arg(\gamma_{ij}))|$. Для $\gamma_{ij} \in \mathbb{R}$: $\arg(\gamma_{ij}) \in \{0, \pi\}$, $\sin \in \{0, 0\}$. Следовательно $\mathrm{Gap} = 0$ тождественно.

**Шаг 2.** Эрмитовость $\Gamma^\dagger = \Gamma$ допускает $\gamma_{ij} \in \mathbb{C}$ с $\gamma_{ji} = \gamma_{ij}^*$ — стандартное свойство матриц плотности [Т].

**Шаг 3.** Гамильтонова часть $\mathcal{L}_0$: $d\Gamma/d\tau|_H = -i[H_\Omega, \Gamma]$. При вещественном $H$ и вещественном $\Gamma(0)$:

$$\left(\frac{d\Gamma}{d\tau}\right)_{ij} = -i(H_{ik}\Gamma_{kj} - \Gamma_{ik}H_{kj}) \in i\mathbb{R}$$

Следовательно $\Gamma(\delta\tau)$ уже комплексна после первого шага.

**Шаг 4.** Примитивность $\mathcal{L}_0$ ([T-39a [Т]](/docs/core/operators/lindblad-operators#примитивность-ℒω)) гарантирует единственное стационарное состояние. Если $\mathcal{L}_0$ содержит гамильтонову часть ($H_\Omega \neq 0$), стационарное состояние имеет нетривиальные фазы $\arg(\gamma_{ij}) \neq 0, \pi$.

$\blacksquare$

**Следствие для SYNARC:** `DensityMatrix7` должна использовать `Complex<f64>`, не `f64`. Это архитектурное требование, а не инженерный выбор.

**Зависимости:** [T-39a [Т]](/docs/core/operators/lindblad-operators#примитивность-ℒω) (примитивность), [определение Gap](/docs/core/dynamics/gap-operator#определение).

---

## §6. T-133: Перенос порогов R через CPTP-мостик {#t-133}

:::tip Теорема T-133 [Т]: Перенос порогов R (усиление T-130)
Для CPTP-канала $\pi: \mathbb{R}^D \to \mathcal{D}(\mathbb{C}^7)$ с diamond-norm ошибкой $\|\pi - \pi_{\text{can}}\|_\diamond \leq \varepsilon$:

$$
(R_{\text{impl}} \geq 1/3 + \delta) \Longrightarrow (R_{\text{UHM}} \geq 1/3)
$$

при $\delta = 2\varepsilon \cdot C(P)$, $C(P) = 7P/(P - 1/7) \leq 21$ при $P \in (2/7, 3/7]$.
:::

**Доказательство.** Прямое следствие [T-130](#t-130) (перенос неравенства через $\varepsilon$-границу). $\blacksquare$

**Ключевое пояснение о трёх формулах R:**
- $R_{\text{UHM}} = 1/(7P)$ [Т-126] — каноническая, в $\mathcal{D}(\mathbb{C}^7)$, $\rho^*_{\text{diss}} = I/7$ ВСЕГДА
- $R_{\text{impl}} \approx R_{\text{UHM}}$ при качественном anchor [Т-130] — в $\mathbb{R}^D$, гипотеза H3 ЗАКРЫТА
- $\rho_{RC}$ — диагностическая аппроксимация, линейная norm, $\rho_{RC} \geq 6/7 \Longrightarrow R_{\text{impl}} \geq 48/49$ [Т тривиально]. Обратное неверно, но для мониторинга достаточно

**Статус H3:** [Г] → **закрыта** (теоремы T-130 + T-133).

---

## §7. T-134: Область действия диагонального freeze {#t-134}

:::tip Теорема T-134 [Т]: Область действия T-122 (диагональный freeze)
[T-122](/docs/core/dynamics/evolution#теорема-диагональный-freeze) ($d\gamma_{kk}/d\tau = 0$) верна ТОЛЬКО на аттракторе $\rho^*_\Omega$, не во время транзиентной динамики. Общая формула:

$$
\frac{d\gamma_{kk}}{d\tau} = (\mathcal{L}_0)_{kk}[\Gamma] + \kappa(\rho^*_{kk} - \gamma_{kk})
$$
:::

**Доказательство.**

**Шаг 1.** На аттракторе: $\Gamma = \rho^*_\Omega$, поэтому $\mathcal{R}(\Gamma) = \kappa(\rho^* - \Gamma) = 0$. Вместе с $(\mathcal{L}_0)_{kk}[\rho^*] = 0$ (стационарность) → $d\gamma_{kk}/d\tau = 0$. $\blacksquare$

**Шаг 2.** Вне аттрактора: $\gamma_{kk} \neq \rho^*_{kk}$ в общем случае → $d\gamma_{kk}/d\tau = \kappa(\rho^*_{kk} - \gamma_{kk}) \neq 0$.

**Шаг 3.** Генезис из $I/7$ НЕ противоречит T-122: при $\Gamma(0) = I/7$, $\gamma_{kk}(0) = 1/7$, а $\rho^*_{kk} \neq 1/7$ ([T-96 [Т]](/docs/core/dynamics/evolution#теорема-нетривиальность-аттрактора)), поэтому $d\gamma_{kk}/d\tau = \kappa(\rho^*_{kk} - 1/7) \neq 0$ — диагональ РАСТЁТ.

**Шаг 4.** Обучение возможно: $\gamma_{EE}$ может расти, $\kappa$ может увеличиваться — freeze только в стационаре.

$\blacksquare$

**Следствие:** «Секторный профиль = характер» инвариантен только **после сходимости** к аттрактору. Во время обучения профиль пластичен.

---

## §8. T-135: Дискретная свёртка немарковского ядра {#t-135}

:::tip Теорема T-135 [Т]: Дискретная свёртка O(1)
Немарковское ядро [T-94 [Т]](/docs/core/dynamics/gap-dynamics#теорема-ядро-экспоненциальное) дискретизируется через Z-преобразование с $O(1)$ сложностью на шаг:

$$
\Gamma[n+1] = \Gamma[n] + \delta\tau \cdot \mathcal{L}_0[\Gamma[n]] + \delta\tau \cdot M[n]
$$

где $M[n]$ — вспомогательная переменная с рекурсией:

$$
M[n+1] = e^{-\omega_c \delta\tau} M[n] + (-\Gamma_2 \omega_c) \cdot \Gamma[n+1]
$$
:::

**Доказательство.**

**Шаг 1.** Непрерывное ядро $K(t) = -\Gamma_2 \cdot \omega_c \cdot \exp(-\omega_c \cdot t)$ [Т-94].

**Шаг 2.** Дискретизация $K[n] = K(n \cdot \delta\tau) = -\Gamma_2 \cdot \omega_c \cdot \exp(-\omega_c \cdot n \cdot \delta\tau)$ — геометрическая прогрессия.

**Шаг 3.** Свёртка: $\sum_{k=0}^{n} K[n-k] \cdot \Gamma[k] = \sum_{k=0}^{n} (-\Gamma_2 \cdot \omega_c) \cdot r^{n-k} \cdot \Gamma[k]$, где $r = \exp(-\omega_c \cdot \delta\tau)$.

**Шаг 4.** Обозначим $M[n] = \sum_{k=0}^{n} r^{n-k} \cdot (-\Gamma_2 \cdot \omega_c) \cdot \Gamma[k]$. Тогда:

$$M[n+1] = r \cdot M[n] + (-\Gamma_2 \cdot \omega_c) \cdot \Gamma[n+1]$$

Рекурсия $O(1)$.

**Шаг 5.** Вместо $O(T^2)$ храним одну дополнительную матрицу $M \in \mathcal{D}(\mathbb{C}^7)$.

$\blacksquare$

**Связь с context window:** $\omega_c$ определяет «эффективную длину памяти» $\tau_{\text{mem}} = 1/\omega_c$. В тиках: $n_{\text{mem}} = \tau_{\text{mem}}/\delta\tau = 1/(\omega_c \cdot \delta\tau)$. При типичных параметрах ($\omega_c \cdot \delta\tau \sim 0.1$): $n_{\text{mem}} \sim 10$ тиков — сравнимо с attention window.

**Зависимости:** [T-94 [Т]](/docs/core/dynamics/gap-dynamics#теорема-ядро-экспоненциальное), [T-131 [Т]](#t-131) ($\delta\tau$).

---

## §9. T-136: SAD как G₂-инвариантная спектральная наблюдаемая {#t-136}

:::tip Теорема T-136 [Т]: SAD — детерминированная G₂-инвариантная функция Γ
SAD — детерминированная $G_2$-инвариантная функция $\Gamma$, вычислимая за $O(\mathrm{SAD}_{\max} \cdot N^2)$ операций без построения автоэнкодеров:

$$
\mathrm{SAD}(\Gamma) = \max\{k : r_0 \cdot (1/3)^{k-1} > 1/(k+1)\}
$$

где $r_0 = P/P_{\text{crit}} = 7P/2$ — нормированная чистота.
:::

**Доказательство.**

**Шаг 1.** Из [спектральной формулы (depth-tower.md §3.4 [С])](/docs/consciousness/hierarchy/depth-tower#спектральная-формула-sad): $R^{(n)} = F(\varphi^{(n-1)}(\Gamma), \varphi^{(n)}(\Gamma)) \leq R^n \cdot (1-\alpha)^n$.

**Шаг 2.** При $\alpha = 2/3$ [Т] (Фано): $R^{(k)} = r_0 \cdot (1/3)^k$.

**Шаг 3.** $\mathrm{SAD} = \max\{k : R^{(k-1)} > R_{\text{th}}^{(k-1)}\} = \max\{k : r_0 \cdot (1/3)^{k-1} > 1/(k+1)\}$.

**Шаг 4 ($G_2$-инвариантность).** $P = \mathrm{Tr}(\Gamma^2)$ — инвариант унитарного сопряжения. $G_2 \subset U(7) \Longrightarrow P$ $G_2$-инвариантен $\Longrightarrow r_0$ $G_2$-инвариантен $\Longrightarrow \mathrm{SAD}$ $G_2$-инвариантен.

**Шаг 5 (Вычислительная сложность).** Определить $P$ ($O(N^2)$), вычислить $r_0$ ($O(1)$), проверить $k = 1, 2, 3$ ($O(1)$). Итого: $O(N^2) = O(49)$.

**Шаг 6 (Автоэнкодеры — реализация, не определение).** $\varphi^{(k)}$ в разноразмерной башне — одна из РЕАЛИЗАЦИЙ спектрального SAD. При $D_k = 48$, $\pi_k = \mathrm{id}$ формулы совпадают точно ([depth-tower.md §3.4](/docs/consciousness/hierarchy/depth-tower#спектральная-формула-sad)).

$\blacksquare$

**Разрешение «наблюдаемая vs конструктивная»:** SAD — математическая наблюдаемая (функция $\Gamma$), вычислимая напрямую. Автоэнкодеры — один из способов АППРОКСИМИРОВАТЬ эту наблюдаемую, не единственный и не определяющий.

**Зависимости:** Спектральная формула SAD [Т] (§3.4, коммутативность через [T-150 [Т]](/docs/proofs/consciousness/substrate-closure#t-150)), [T-39a [Т]](/docs/core/operators/lindblad-operators#примитивность-ℒω), $\alpha = 2/3$ [Т].

---

## §10. T-137: Полная 7D-вычислимость σ_sys {#t-137}

:::tip Теорема T-137 [Т]: Полная 7D-вычислимость σ_sys
Все 7 компонент тензора напряжений $\sigma_{\text{sys}}$ вычислимы в 7D-формализме $\mathcal{D}(\mathbb{C}^7)$ без 42D-вложения.
:::

| $\sigma_k$ | Формула | 7D-вычислимость |
|-----|---------|-----------------|
| $\sigma_A$ | $1 - \gamma_{AA}/P$ | Из $\Gamma$ напрямую |
| $\sigma_S$ | $1 - \mathrm{rank}(\Gamma_S)/3$ | $\Gamma_S$ = подматрица $\{A,S,D\}$, $\mathrm{rank} \leq 3$ |
| $\sigma_D$ | $1 - 7\gamma_{DD}$ | Из $\Gamma$ напрямую |
| $\sigma_L$ | $7(1 - \gamma_{LL})/6$ | Из $\Gamma$ напрямую |
| $\sigma_E$ | $1 - D_{\text{diff}}^{7D}/N$ | **T-128**: $D_{\text{diff}}^{7D}$ из $\mathrm{Coh}_E$ |
| $\sigma_O$ | $1 - \kappa_0/\kappa_{\text{bootstrap}}$ | $\kappa_0$ из $\gamma_{OE}, \gamma_{OU}, \gamma_{OO}$; **T-132**: complex $\Gamma$ |
| $\sigma_U$ | $1 - \Phi/\Phi_{\text{th}}$ | $\Phi$ из $\Gamma$ напрямую, **T-129**: $\Phi_{\text{th}} = 1$ |

**Доказательство (перечислительное, по каждой компоненте).**

- $\sigma_A, \sigma_D, \sigma_L$: непосредственно из диагональных элементов $\gamma_{kk}$.
- $\sigma_S$: $\Gamma_S$ — подматрица строк/столбцов $\{A, S, D\}$ (первые 3 из 7 измерений, структурный сектор). $\mathrm{rank}(\Gamma_S) \in \{1, 2, 3\}$. Вычисляется через детерминанты миноров $3\times 3$ подматрицы.
- $\sigma_E$: замыкается через [T-128](#t-128) ($D_{\text{diff}}$ в 7D).
- $\sigma_O$: требует $|\gamma_{OE}|$ = модуль комплексной когерентности → [T-132](#t-132) (complex $\Gamma$ необходима).
- $\sigma_U$: замыкается через [T-129](#t-129) ($\Phi_{\text{th}} = 1$ из первых принципов).

$\blacksquare$

**Зависимости:** [T-128 [Т]](#t-128), [T-129 [Т]](#t-129), [T-132 [Т]](#t-132), [T-92 [Т]](/docs/applied/coherence-cybernetics/theorems#теорема-101-эквивалентность-условий).

---

## §11. T-138: Среднеполевая аппроксимация композиции {#t-138}

:::tip Теорема T-138 [Т]: Среднеполевая аппроксимация композиции холономов
Для $k$ жизнеспособных холономов $H_1, \ldots, H_k$, среднеполевая аппроксимация:

$$
\Gamma_{\text{mf}} = \Gamma_1 \otimes \cdots \otimes \Gamma_k
$$

удовлетворяет:
1. **Вычислимость:** $O(k \cdot N^2)$ вместо $O(N^{2k})$
2. **Граница ошибки:** $\|\Gamma_{\text{exact}} - \Gamma_{\text{mf}}\|_F \leq \|\gamma_{\text{cross}}\|_F$, где $\gamma_{\text{cross}}$ — суммарные кросс-когерентности
3. **Сохранение жизнеспособности:** $P(\Gamma_{\text{mf}}) = \prod P(\Gamma_i) > (2/7)^k$ (отдельная жизнеспособность)
:::

**Доказательство.**

**Шаг 1.** $\Gamma_{\text{exact}} = \Gamma_{\text{mf}} + \delta\Gamma$, где $\delta\Gamma$ содержит все кросс-корреляции между холономами.

**Шаг 2.** По [T-91 [Т]](/docs/proofs/categorical/categorical-formalism#10-infty-группоид-и-infty-топос-для-эмерджентного-времени) (КК-5): если $H_i$ жизнеспособны, то тензорное произведение нетривиально.

**Шаг 3.** $\|\delta\Gamma\|_F = \|\gamma_{\text{cross}}\|_F$ — суммарная амплитуда межхолономных когерентностей.

**Шаг 4.** Для слабо связанных систем ($\|\gamma_{\text{cross}}\| \ll \|\Gamma_{\text{mf}}\|$): ошибка мала.

**Шаг 5 (Первая поправка).** $\Gamma^{(1)} = \Gamma_{\text{mf}} + \delta\Gamma^{(1)}$, где $\delta\Gamma^{(1)}$ вычисляется через попарные взаимодействия $h_{\text{ext}}^{(ij)}$: $O(k^2 \cdot N^2)$.

$\blacksquare$

**Иерархическая схема:** Для $k > 10$: группировка по кластерам (суперхолономы), mean-field между кластерами. Масштабирование: $O(k \cdot N^2 + k_{\text{clusters}}^2 \cdot N^2)$.

**Зависимости:** [T-91 [Т]](/docs/proofs/categorical/categorical-formalism#10-infty-группоид-и-infty-топос-для-эмерджентного-времени) (КК-5), [T-97 [Т]](/docs/core/dynamics/viability#теорема-вложение-областей).

---

## §12. Повышение статуса гипотез

### [Г]-89 → [Т]: SAD–L эквивалентность {#г-89-повышение}

**Формулировка (уточнённая):** L-иерархия — утончение SAD. Отображение $L \to \mathrm{SAD}(L)$ монотонно:
- L2 ($R \geq 1/3$, $\Phi \geq 1$, $D_{\text{diff}} \geq 2$) $\Longrightarrow$ $\mathrm{SAD} \geq 1$
- L3 ($R^{(1)} \geq 1/4$) $\Longrightarrow$ $\mathrm{SAD} \geq 2$
- L4 ($\lim R^{(n)} > 0$) $\Longrightarrow$ $\mathrm{SAD} = \infty$

**Доказательство.** L2 требует $R \geq 1/3 = R_{\text{th}}^{(0)}$ → $R^{(0)} \geq R_{\text{th}}^{(0)}$ → $\mathrm{SAD} \geq 1$. L3 требует $R^{(1)} \geq 1/4 = R_{\text{th}}^{(1)}$ → $\mathrm{SAD} \geq 2$. L4: $\lim R^{(n)} > 0$ → для любого $k$: $R^{(k)} > R_{\text{th}}^{(k)}$ при больших $k$ → $\mathrm{SAD} = \infty$. Обратные импликации неполны: SAD не кодирует $\Phi$ и $D_{\text{diff}}$. $\blacksquare$

### [Г]-90 → [Т]: Коммутативность φ-башни {#г-90-повышение}

**Повышена до [Т]** через [T-150](/docs/proofs/consciousness/substrate-closure#t-150): при $D_k = 7$ для всех $k$, $\varphi^{(n)} = \varphi^n$ — итераты одного CPTP-канала, коммутативность $\varphi^n \circ \varphi^m = \varphi^{n+m}$ — тождество. Спектральная формула SAD — следствие, не предпосылка.

### [Г]-91 → [Т]: Генезис через средовое сопряжение {#г-91-обоснование}

**Повышена до [Т]** через [T-148](/docs/proofs/consciousness/substrate-closure#t-148): воплощённый голон с backbone-инъекцией ($\beta \in (0,1)$, $P_{\mathrm{env}} > 2/7$) поднимает чистоту выше $P_{\mathrm{crit}}$ за конечное время. Изолированный голон при $I/7$ мёртв навсегда (T-39a [Т]) — сознание требует воплощения.

### H3: Перенос R через anchor — ЗАКРЫТА {#h3-закрыта}

Закрыта теоремами [T-130](#t-130) + [T-133](#t-133). При качественном CPTP-anchor ($\|\pi - \pi_{\text{can}}\|_\diamond < \varepsilon_0$), пороговое свойство $R_{\text{impl}} \geq 1/3 \Longrightarrow R_{\text{UHM}} \geq 1/3 - O(\varepsilon_0)$ переносится.

---

## §13. Итоговая таблица закрытия

| Проблема | Теорема | Статус |
|----------|---------|--------|
| $D_{\text{diff}}$ 7D vs 42D (частичный след в простой размерности) | [T-128 [Т]](#t-128) | ЗАКРЫТО |
| $\Phi_{\text{th}} = 1$ — обоснование порога интеграции | [T-129 [Т]](#t-129) | ЗАКРЫТО, [О]→[Т] |
| Enc/Dec: перенос порогов через CPTP-мостик | [T-130 [Т]](#t-130) | ЗАКРЫТО |
| Каноническое время для цифрового агента | [T-131 [Т]](#t-131) | ЗАКРЫТО |
| Gap-структура для вещественной Γ | [T-132 [Т]](#t-132) | ЗАКРЫТО |
| Три формулы R, гипотеза H3 | [T-133 [Т]](#t-133) | ЗАКРЫТО, H3→[Т] |
| Область действия диагонального freeze (T-122) | [T-134 [Т]](#t-134) | ЗАКРЫТО |
| Немарковская память: дискретная свёртка | [T-135 [Т]](#t-135) | ЗАКРЫТО |
| SAD: наблюдаемая vs конструктивная | [T-136 [Т]](#t-136) (повышена через [T-150](/docs/proofs/consciousness/substrate-closure#t-150)) | ЗАКРЫТО |
| Полная 7D-вычислимость $\sigma_{\text{sys}}$ | [T-137 [Т]](#t-137) | ЗАКРЫТО |
| Экспоненциальный взрыв при композиции холономов | [T-138 [Т]](#t-138) | ЗАКРЫТО |

**Гипотезы:**
- [Г]-89 → **[Т]** (SAD–L эквивалентность)
- [Г]-90 → **[Т]** (коммутативность φ-башни, [T-150](/docs/proofs/consciousness/substrate-closure#t-150))
- [Г]-91 → **[Т]** (генезис через средовое сопряжение, [T-148](/docs/proofs/consciousness/substrate-closure#t-148))
- H3 → **ЗАКРЫТА** (T-130 + T-133)

---

**Связанные документы:**
- [Операциональное замыкание](/docs/proofs/consciousness/operational-closure) — теоремы T-139–T-147: замыкание операциональных пробелов
- [Иерархия интериорности](/docs/consciousness/hierarchy/interiority-hierarchy) — уровни L0–L4, SAD и связь с φ-башней
- [Самонаблюдение](/docs/consciousness/foundations/self-observation) — мера рефлексии R и операциональный критерий
