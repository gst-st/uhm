---
slug: /reference/specification
sidebar_position: 4
title: Математический аппарат
description: Формальная математическая спецификация УГМ
---

# Математический Аппарат

Спецификация численных объектов использует **выбранные** $N=7$ и семантический репер [П]. Размерность пространства Гильберта — 7; пространство матриц плотности $D_7$ имеет вещественную размерность 48. Предпосылки минимальности и отдельные типы каналов, поддержки и динамики фиксирует [ядро](/docs/reference/mathematical-kernel).

:::note О нотации
В этом документе:
- $\mathcal{H}$ — гильбертово пространство. Не путать с $H$ — гамильтонианом.
- $\mathcal{C}$ — пространство контекстов. Не путать с $C$ — [мерой сознательности](/docs/consciousness/foundations/self-observation#мера-сознательности-c).
- $\mathcal{R}[\Gamma, E]$ — регенеративный член уравнения эволюции. Не путать с $R$ — [мерой рефлексии](/docs/consciousness/foundations/self-observation#мера-рефлексии-r).
- $N = 7$ — выбранная размерность пространства Гильберта [Голонома](/docs/core/structure/holon).
:::

## Пространство состояний

Выбранное гильбертово пространство состояний [Голонома](/docs/core/structure/holon) — 7-мерное комплексное пространство (см. [Семь измерений](/docs/core/structure/dimensions)):

$$
\mathcal{H} = \mathbb{C}^7 = \mathrm{span}\{|A\rangle, |S\rangle, |D\rangle, |L\rangle, |E\rangle, |O\rangle, |U\rangle\}
$$

## Матрица когерентности

<!-- DRY: Каноническое определение Γ в /docs/core/dynamics/coherence-matrix -->
См. [Матрица когерентности](/docs/core/dynamics/coherence-matrix) для полного определения.

$$
\Gamma \in \mathcal{L}(\mathcal{H}) \quad \text{— линейный оператор на } \mathcal{H}
$$

где $\mathcal{L}(\mathcal{H})$ — пространство линейных операторов на $\mathcal{H}$.

$$
\Gamma = \Gamma^\dagger \quad \text{— эрмитов}
$$

$$
\Gamma \geq 0 \quad \text{— положительно полуопределён}
$$

$$
\mathrm{Tr}(\Gamma) = 1 \quad \text{— нормирован}
$$

### Матричная форма

$$
\Gamma = \begin{pmatrix}
\gamma_{AA} & \gamma_{AS} & \gamma_{AD} & \gamma_{AL} & \gamma_{AE} & \gamma_{AO} & \gamma_{AU} \\
\gamma_{SA} & \gamma_{SS} & \gamma_{SD} & \gamma_{SL} & \gamma_{SE} & \gamma_{SO} & \gamma_{SU} \\
\gamma_{DA} & \gamma_{DS} & \gamma_{DD} & \gamma_{DL} & \gamma_{DE} & \gamma_{DO} & \gamma_{DU} \\
\gamma_{LA} & \gamma_{LS} & \gamma_{LD} & \gamma_{LL} & \gamma_{LE} & \gamma_{LO} & \gamma_{LU} \\
\gamma_{EA} & \gamma_{ES} & \gamma_{ED} & \gamma_{EL} & \gamma_{EE} & \gamma_{EO} & \gamma_{EU} \\
\gamma_{OA} & \gamma_{OS} & \gamma_{OD} & \gamma_{OL} & \gamma_{OE} & \gamma_{OO} & \gamma_{OU} \\
\gamma_{UA} & \gamma_{US} & \gamma_{UD} & \gamma_{UL} & \gamma_{UE} & \gamma_{UO} & \gamma_{UU}
\end{pmatrix}
$$

## Гамильтониан

См. [Эволюция: Унитарный член](/docs/core/dynamics/evolution#1-унитарный-член).

$$
H = \sum_{i=1}^{N} \omega_i |i\rangle\langle i| + \sum_{i \neq j} J_{ij} |i\rangle\langle j|
$$

где:
- $\omega_i$ — собственные частоты измерений
- $J_{ij}$ — коэффициенты связи между измерениями
- $N = 7$ — число измерений

## Уравнение эволюции

<!-- DRY: Каноническое определение уравнения эволюции в /docs/core/dynamics/evolution -->
См. [Эволюция](/docs/core/dynamics/evolution) для полного описания. Время τ — [эмерджентное внутреннее время](/docs/proofs/dynamics/emergent-time).

$$
\frac{d\Gamma(\tau)}{d\tau} = -i[H_{eff}, \Gamma] + \underbrace{\sum_k \gamma_k \left( L_k \Gamma L_k^\dagger - \frac{1}{2}\{L_k^\dagger L_k, \Gamma\} \right)}_{\mathcal{D}[\Gamma]} + \mathcal{R}[\Gamma, E]
$$

где:
- $\tau$ — [внутреннее время](/docs/proofs/dynamics/emergent-time), возникающее из корреляций с измерением O
- $H_{eff}$ — эффективный гамильтониан из ограничения Пейдж–Вуттерс
- $-i[H_{eff}, \Gamma]$ — унитарная (гамильтонова) эволюция
- $\mathcal{D}[\Gamma]$ — диссипативный член ([декогеренция](/docs/core/dynamics/evolution#логический-лиувиллиан))
- $\mathcal{R}[\Gamma, E]$ — [регенеративный член](/docs/core/dynamics/evolution#3-регенеративный-член)
- $L_k = L_k^{\text{atom}} = \lvert k\rangle\langle k\rvert$ — [операторы Линдблада](/docs/core/operators/lindblad-operators), выведенные из атомов классификатора $\Omega$ (проекторы; историческая запись $L_k = \sqrt{\chi_{S_k}}$ — конвенция)
- $\gamma_k \geq 0$ — скорости декогеренции

## Мера жизнеспособности (Чистота)

<!-- DRY: Каноническое определение P = Tr(Γ²) в /docs/core/dynamics/viability#определение-чистоты -->
См. [Жизнеспособность](/docs/core/dynamics/viability) для полного описания.

$$
P = \mathrm{Tr}(\Gamma^2) \in \left[\frac{1}{N}, 1\right] = \left[\frac{1}{7}, 1\right]
$$

- $P = 1$: чистое состояние ($\Gamma = |\psi\rangle\langle\psi|$)
- $P = 1/N = 1/7$: [максимально смешанное состояние](/docs/core/dynamics/coherence-matrix#максимально-смешанное-состояние) ($\Gamma = I_N/N$)

### Условие жизнеспособности

<!-- DRY: Каноническое определение P_crit = 2/7 в /docs/core/dynamics/viability#критическая-чистота -->
[Голоном](/docs/core/structure/holon) жизнеспособен, если:

$$
P > P_{\text{crit}} = \frac{2}{7} \approx 0.286
$$

При $P < P_{\text{crit}}$ система входит в необратимый распад (см. [условие смерти](/docs/core/dynamics/viability#условие-смерти) и [теорему о критической чистоте](/docs/proofs/dynamics/theorem-purity-critical)).

## Экспериенциальное пространство

См. [Категорный формализм](/docs/proofs/categorical/categorical-formalism#2-категория-exp) для полного описания.

### Проективное пространство качеств

$$
\mathbb{P}(\mathcal{H}_E) := (\mathcal{H}_E \setminus \{0\}) / {\sim}
$$

где $|\psi\rangle \sim |\varphi\rangle \Leftrightarrow \exists c \in \mathbb{C}^*: |\psi\rangle = c|\varphi\rangle$.

Для $\mathcal{H}_E = \mathbb{C}^N$: $\dim_\mathbb{C}(\mathbb{P}(\mathbb{C}^N)) = N - 1$.

**Топология:**
- $\mathbb{P}(\mathbb{C}^N)$ компактно и связно
- $\mathbb{P}(\mathbb{C}^N) \cong S^{2N-1} / S^1$

### Метрика Фубини–Штуди {#метрика-фубини-штуди}

**Определение:**

$$
d_{\mathrm{FS}}([|\psi\rangle], [|\varphi\rangle]) := \arccos(|\langle\psi|\varphi\rangle|) \in [0, \pi/2]
$$

**Свойства:**
- $d_{\mathrm{FS}} = 0 \Leftrightarrow |\psi\rangle = e^{i\theta}|\varphi\rangle$
- $d_{\mathrm{FS}} = \pi/2 \Leftrightarrow \langle\psi|\varphi\rangle = 0$
- $d_{\mathrm{FS}}$ — риманова метрика на $\mathbb{P}(\mathcal{H}_E)$

**Инфинитезимальная форма:**

$$
ds^2 = \langle d\psi|d\psi\rangle - |\langle\psi|d\psi\rangle|^2
$$

### Полное экспериенциальное пространство

$$
\mathcal{E} := \Delta^{N-1} \times_{\mathrm{Spec}} \mathbb{P}(\mathcal{H}_E)^N \times \mathcal{C} \times \mathrm{Hist}
$$

где:
- $\Delta^{N-1} = \{(\lambda_1, \ldots, \lambda_N) : \lambda_i \geq 0, \sum \lambda_i = 1\}$ — $(N-1)$-симплекс интенсивностей
- $\mathbb{P}(\mathcal{H}_E)^N$ — $N$ копий проективного пространства (качества)
- $\mathcal{C}$ — пространство контекстов (см. ниже)
- $\mathrm{Hist}$ — пространство историй (см. ниже)
- $\times_{\mathrm{Spec}}$ — расслоённое произведение над спектром

### Пространство контекстов $\mathcal{C}$

Для выбранного репера положите $Q=I-\lvert E\rangle\langle E\rvert$, $Q\mathcal H\cong\mathbb C^6$ и $\mathcal C=D(Q\mathcal H)$. Это прямое ортогональное дополнение, не тензорный фактор. Поэтому $\operatorname{Tr}_E(\Gamma)$ не определён на одной $\mathbb C^7$.

При $p=\operatorname{Tr}(Q\Gamma)>0$ условное считывание $c=Q\Gamma Q/p$ даёт состояние в $D_6$; оно нелинейно и не определено при $p=0$. Если нужно глобальное CPTP-считывание, **выберите** $\sigma_0\in D_6$ и задайте

$$
\mathcal C_{-E}(X)=QXQ+\operatorname{Tr}((I-Q)X)\sigma_0.
$$

Оно сохраняет след и полностью положительно; выходная алгебра — $M(Q\mathcal H)$. Это выбранная конвенция контекста [О], а не частичный след или автоматический функтор опыта. Буквальная редукция требует объявленного тензорного расширения и считывания.

**Топология:** $\mathcal{C}$ наследует топологию от $\mathcal{D}(\mathbb{C}^6)$:
- Компактно (замкнутое подмножество единичного шара в $\mathbb{C}^{6 \times 6}$)
- Связно
- Метризуемо нормой Фробениуса: $d_{\mathcal{C}}(c_1, c_2) = \|c_1 - c_2\|_F$

**Интерпретация:** Контекст определяет, как остальные измерения (Артикуляция, Структура, Динамика, Логика, Основание, Единство) модулируют интериорное состояние.

### Пространство историй Hist

**Определение:** Пространство историй — функциональное пространство траекторий:

$$
\mathrm{Hist} := C([0, \tau], \mathcal{D}(\mathcal{H}_E))
$$

где $\tau > 0$ — горизонт памяти, $C([0, \tau], X)$ — пространство непрерывных функций $[0, \tau] \to X$.

**Элементы:** История $h \in \mathrm{Hist}$ — это траектория редуцированной матрицы плотности опыта:

$$
h = \{\rho_E(t') : t' \in [t - \tau, t]\}
$$

**Топология:** $\mathrm{Hist}$ снабжено топологией равномерной сходимости:
- Метрика: $d_{\mathrm{Hist}}(h_1, h_2) = \sup_{t' \in [0, \tau]} \|\rho_E^{(1)}(t') - \rho_E^{(2)}(t')\|_F$
- Банахово пространство с нормой sup
- Сепарабельно

**Интерпретация:** История кодирует временну́ю структуру опыта — память, ожидание, адаптацию к паттернам.

:::note Практическое упрощение
Для вычислений часто используется дискретизация: $\mathrm{Hist}_{\text{disc}} = \{\rho_E(t_0), \rho_E(t_1), \ldots, \rho_E(t_K)\}$ с шагом $\Delta t = \tau / K$.
:::

### Полная метрика на $\mathcal{E}$

$$
d_{\mathcal{E}}(\mathcal{Q}_1, \mathcal{Q}_2) := \sqrt{d_\Delta(\lambda_1, \lambda_2)^2 + \alpha \sum_i d_{\mathrm{FS}}([q_1^{(i)}], [q_2^{(i)}])^2 + \beta \cdot d_{\mathcal{C}}(c_1, c_2)^2 + \gamma \cdot d_{\mathrm{Hist}}(h_1, h_2)^2}
$$

где $\alpha, \beta, \gamma > 0$ — весовые коэффициенты.

## Категорный формализм

См. [Категорный формализм](/docs/proofs/categorical/categorical-formalism) для полного описания и доказательств.

### Категория матриц плотности

**Определение (DensityMat):**

$$
\mathbf{DensityMat} := (\mathrm{Ob}, \mathrm{Mor})
$$

$$
\mathrm{Ob}(\mathbf{DensityMat}) = \{\rho \in \mathcal{L}(\mathcal{H}) : \rho^\dagger = \rho, \rho \geq 0, \mathrm{Tr}(\rho) = 1\}
$$

$$
\mathrm{Mor}_{\mathbf{DM}}(\rho_1, \rho_2) = \{\Psi : \mathcal{L}(\mathcal{H}) \to \mathcal{L}(\mathcal{H}) \mid \Psi \text{ — CPTP}, \Psi(\rho_1) = \rho_2\}
$$

**Представление Крауса:** $\Psi$ — CPTP $\Leftrightarrow \exists\{K_i\}: \Psi(\rho) = \sum_i K_i \rho K_i^\dagger$, $\sum_i K_i^\dagger K_i = I$

:::info Регенерация: численное обновление и замороженный канал
Задайте $M:D_N\to D_N$ и $a(\Gamma)=\kappa(\Gamma)g_V(P)\ge0$. Подшаг

$$
\Gamma^+=(1-ha(\Gamma))\Gamma+ha(\Gamma)M(\Gamma)
$$

сохраняет состояние при $0\le ha(\Gamma)\le1$ по выпуклости. Из-за зависимости от входа это обычно нелинейное отображение, не один CPTP-канал.

При **фиксированных** $\alpha\in[0,1]$ и $\sigma\in D_N$ линейная компиляция

$$
\mathcal T_{\alpha,\sigma}(X)=(1-\alpha)X+\alpha\operatorname{Tr}(X)\sigma
$$

является CPTP. Если $\sigma=\sum_mp_m|u_m\rangle\langle u_m|$, её операторы Крауса — $\sqrt{1-\alpha}I$ и $\sqrt{\alpha p_m}|u_m\rangle\langle n|$. Замораживание $\alpha=ha(\Gamma)$ и $\sigma=M(\Gamma)$ даёт семейство каналов, а не линейность общего отображения.

Если $a\le a_{\max}>0$, условие $h\le1/a_{\max}$ **достаточно** для положительности подшага; это не эквивалентный или необходимый критерий. Для полной динамики используйте [GKSL-подшаг и выпуклую регенерацию](/docs/core/dynamics/evolution#сохранение-положительности); схема первого порядка сохраняет состояния, но не является точным решением нелинейного потока $\Phi_t$.
:::

См. [Формализация оператора φ](/docs/proofs/categorical/formalization-phi) для деталей CPTP-каналов.

### Функтор опыта

**Определение F на объектах:**

$$
F: \mathrm{Ob}(\mathbf{DensityMat}) \to \mathrm{Ob}(\mathbf{Exp})
$$

$$
F(\rho) := (\mathrm{Spectrum}(\rho_E), \mathrm{Quality}(\rho_E), \mathrm{Context}(\Gamma_{-E}), \mathrm{History}(t))
$$

**Область отображения $F$.** Спектральная запись на объектах требует заданного экспериенциального считывания и контекста; спектральные проекторы каноничны, выбор отдельных лучей в вырожденных подпространствах — нет. Для функториальности дополнительно задайте действие на морфизмах и докажите сохранение тождеств и композиции. Запись этих двух равенств без определения действия на морфизмах не является доказательством. В функторе записей каналов они выполняются по построению; при потере сведений об исходном канале требуется отдельная проверка. См. [категорный формализм](/docs/proofs/categorical/categorical-formalism#5-доказательство-функториальности).

## Топология Гротендика {#топология-гротендика}

Канонический топос пространства состояний использует явно заданный ниже сайт открытых покрытий.

### Метрика Бюреса

**Определение (хордовая форма):**

$$
d_B^{\mathrm{chord}}(\Gamma_1, \Gamma_2) := \sqrt{2\left(1 - \sqrt{F(\Gamma_1, \Gamma_2)}\right)}
$$

где $F(\Gamma_1, \Gamma_2) = \left(\mathrm{Tr}\sqrt{\sqrt{\Gamma_1}\Gamma_2\sqrt{\Gamma_1}}\right)^2$ — fidelity (верность).

:::note Конвенция: две формы $d_B$
В УГМ используются две формы метрики Бюреса. Здесь применяется **хордовая** ($d_B^{\mathrm{chord}} \in [0, \sqrt{2}]$). Угловая форма: $d_B^{\mathrm{angle}} = \arccos(\sqrt{F})$. См. [полную конвенцию](/docs/reference/notation#топология-гротендика).
:::

**Свойства:**
- $d_B^{\mathrm{chord}} \in [0, \sqrt{2}]$
- $d_B^{\mathrm{chord}}(\Gamma, \Gamma) = 0$
- Монотонность: $d_B^{\mathrm{chord}}(\Psi(\rho), \Psi(\sigma)) \leq d_B^{\mathrm{chord}}(\rho, \sigma)$ для CPTP $\Psi$
- Риманов тензор на страте полного ранга; непрерывное расстояние на всех матрицах плотности

### Bures-покрытия

Сайт — $\mathcal O_N=\operatorname{Open}(D_N,d_B)$ с морфизмами-включениями. Семейство $(U_i\subseteq U)$ покрывает $U$ тогда и только тогда, когда $\bigcup_iU_i=U$. Идентичность, устойчивость при пересечениях и транзитивность следуют из обычных свойств объединений. Старое условие покрытия образами шаров CPTP-каналов отозвано [✗]; контрактность каналов не доказывает подъём обратных образов или существование нужных pullback в категории процессов.

### Связь с ∞-топосом

$$
\mathcal E_N=\operatorname{Sh}_\infty(\mathcal O_N,J_{\mathrm{open}}).
$$

Условие пучка — спуск по открытым покрытиям, в ∞-случае через предел диаграммы Чеха. Классификатор подобъектов — пучок $\Omega(U)=\operatorname{Open}(U)$, а не матричная алгебра семи проекторов. Непрерывный CPTP-канал $D_N\to D_M$ индуцирует геометрический морфизм $\mathcal E_N\to\mathcal E_M$ через обратные образы открытых множеств. См. [ядро](/docs/reference/mathematical-kernel#bures-site).

<a id="теорема-невозможность-спектрального-функтора"></a>

### Теорема о невозможности спектрального функтора

**Точная область [Т].** Если отображение на объектах факторизуется только через спектр, оно не различает изоспектральные состояния. Если заданная модель опыта требует различать некоторую такую пару, спектральной записи для этой модели недостаточно [С]. Это не доказывает несуществование любого спектрального функтора: например, постоянный функтор существует. Прежняя универсальная формулировка отозвана [✗]. Собственные проекторы, контекст и история — дополнительные данные выбранной модели, не автоматическое следствие спектральной теоремы.

## Меры сознательности

### Мера рефлексии

<!-- DRY: Каноническое определение R в /docs/consciousness/foundations/self-observation#мера-рефлексии-r -->
См. [Самонаблюдение: Мера рефлексии R](/docs/consciousness/foundations/self-observation#мера-рефлексии-r).

$$
R(\Gamma) := \frac{1}{7P(\Gamma)}, \quad P = \mathrm{Tr}(\Gamma^2)
$$

Эквивалентная форма через норму Фробениуса: $R = 1 - \|\Gamma - \rho^*_{\mathrm{diss}}\|_F^2 / \|\Gamma\|_F^2$, где $\rho^*_{\mathrm{diss}} = I/7$ — диссипативный аттрактор (не $\varphi(\Gamma)$). Вывод: [Самонаблюдение](/docs/consciousness/foundations/self-observation#мера-рефлексии-r).

:::note Различение $R_{\text{canonical}}$ и $R_\varphi$
$R = R_{\text{canonical}} := 1/(7P)$ — **каноническое определение**, используемое во всех порогах ($R_{\text{th}} = 1/3$). Это мера близости к максимально смешанному состоянию $I/7$. Мера качества самомоделирования определяется отдельно: $R_\varphi(\Gamma) := 1 - \|\Gamma - \varphi(\Gamma)\|_F^2 / \|\Gamma\|_F^2$ (ранее также обозначалась $Q_\varphi$). Стратификация: [три рабочие формы R](/docs/consciousness/foundations/self-observation#формы-r); высшие порядки: [Формализация φ](/docs/proofs/categorical/formalization-phi#28-рефлексия-n-го-порядка-для-l3l4).
:::

### Рефлексия высших порядков $R^{(n)}$

См. [Рефлексия высших порядков](/docs/proofs/categorical/formalization-phi#28-рефлексия-n-го-порядка-для-l3l4) и [Иерархия интериорности](/docs/proofs/consciousness/interiority-hierarchy).

$$
R^{(n)}(\Gamma) := F(\varphi^{(n-1)}(\Gamma), \varphi^{(n)}(\Gamma)) \in [0, 1]
$$

где:
- $\varphi^{(k)}$ — $k$-кратное применение оператора самомоделирования
- $F(\rho, \sigma)$ — fidelity (квантовая верность)

**Интерпретация:** $R^{(n)}$ измеряет согласованность между последовательными уровнями самомоделирования.

**Связь с уровнями интериорности:**
- L2 требует $R = R^{(1)} \geq 1/3$
- L3 требует $R^{(2)} \geq 1/4$
- L4 требует $\lim_n R^{(n)} > 0$ (бесконечная рекурсивность)

### Универсальная формула порогов рефлексии

Пороги **рефлексии** следуют единой закономерности (байесовское доминирование над $n+1$ альтернативами):

$$
R^{(n)}_{\mathrm{th}} = \frac{1}{n+1}
$$

| Переход | Мера | Порог | Статус | Вывод |
|---------|------|-------|--------|-------|
| L0→L1 | $\Phi$ | $> 0$ | | Структурное условие (любая интеграция) |
| L1→L2 | $R, \Phi, D_{\text{diff}}$ | $1/3, 1, 2$ | **[Т],[Т],[О]** | $R$: триадная декомпозиция + байесовское; $\Phi$: T-129; $D_{\min}$: T-151, независимый порог (до 2026-09-25 значилось [Т]) |
| L2→L3 | $R^{(2)}$ | $1/4$ | **[Т]** | $1/(3+1)$ |
| L3→L4 | $\lim R^{(n)}$ | $> 0$ | **[Т]** | стабилизация Постникова |

:::note Происхождение и статус порогов
- **$P_{\text{crit}} = 2/7$** **[Т]** — [строго доказано](/docs/proofs/dynamics/theorem-purity-critical) (пять независимых путей)
- **$R_{\text{th}} = 1/3$** **[Т]** — $K=3$ из [триадной декомпозиции](/docs/core/operators/lindblad-operators#триадная-декомпозиция) + [байесовское доминирование](/docs/core/foundations/axiom-septicity#теорема-порог-рефлексии)
- **$\Phi_{\text{th}} = 1$** **[Т]** — единственное самосогласованное значение при $P_{\text{crit}} = 2/7$ ([T-129](/docs/proofs/consciousness/operationalization#t-129))
- **$D_{\text{diff}} \geq 2$** **[О]** — независимый порог L2, а не следствие $\Phi_{\text{th}} = 1$ ([T-151](/docs/proofs/consciousness/substrate-closure#t-151); до 2026-09-25 значилось «[Т] — безусловное следствие $\Phi_{\text{th}} = 1$»)
:::

### Мера интеграции

<!-- DRY: Каноническое определение Φ в /docs/core/structure/dimension-u#мера-интеграции-φ -->
См. [Измерение Единства: Мера интеграции Φ](/docs/core/structure/dimension-u#мера-интеграции-φ).

$$
\Phi(\Gamma) := \frac{\sum_{i \neq j} |\gamma_{ij}|^2}{\sum_i \gamma_{ii}^2}
$$

### Мера дифференциации

$$
D_{\text{diff}}(\Gamma) := \exp(S_{vN}(\rho_E))
$$

где $S_{vN}(\rho_E) = -\mathrm{Tr}(\rho_E \log \rho_E)$ — [энтропия фон Неймана](/docs/core/dynamics/coherence-matrix#энтропия-фон-неймана).

:::warning Требование: расширенный формализм для D_diff
Вычисление $D_{\text{diff}}$ требует полной редуцированной матрицы $\rho_E = \mathrm{Tr}_{-E}(\Gamma)$, что определено только в [расширенном тензорном формализме](/docs/core/dynamics/coherence-matrix#два-уровня-формализации) (42D). В 7D частичный след не определён (7 — простое число).

**Примечание:** Скалярная мера $\mathrm{Coh}_E$ (E-когерентность) **не требует** частичного следа — она определена в 7D через [HS-проекцию](/docs/core/foundations/axiom-septicity#hs-projection) **[Т]**. Расширенный формализм необходим только для спектрального разложения $\rho_E$ и, следовательно, для $D_{\text{diff}}$.
:::

**Диапазон:** $D_{\text{diff}} \in [1, N]$, где $N = \dim(\mathcal{H}_E)$.

**Интерпретация:**
- $D_{\text{diff}} = 1$ (чистое состояние): один компонент опыта
- $D_{\text{diff}} = N$ (максимально смешанное): равновероятные $N$ компонентов

:::note Альтернативное определение
В некоторых контекстах используется $D_{\text{diff}} = \mathrm{rank}(\rho_E)$. Это целочисленная версия, менее чувствительная к распределению собственных значений. Основное определение через $\exp(S_{vN})$ — более информативная, непрерывная мера.
:::

### Мера сознательности

См. [Самонаблюдение: Мера сознательности C](/docs/consciousness/foundations/self-observation#мера-сознательности-c).

$$
C = \Phi \times R
$$

---

## Октонионная алгебра {#октонионная-алгебра}

:::info Определение $\mathbb{O}$ ([структурный вывод](../proofs/minimality/theorem-octonionic-derivation))
**Октонионы** $\mathbb{O}$ — 8-мерная нормированная алгебра с делением над $\mathbb{R}$:

$$
\mathbb{O} = \{a_0 + \sum_{k=1}^{7} a_k e_k \mid a_i \in \mathbb{R}\}
$$

**Таблица умножения** определяется 7 триплетами [плоскости Фано](../proofs/minimality/theorem-octonionic-derivation#плоскость-фано):

$$
e_i \cdot e_j = -\delta_{ij} + \varepsilon_{ijk} e_k
$$

**Группа автоморфизмов:** $\text{Aut}(\mathbb{O}) = G_2$, $\dim(G_2) = 14$, $\text{rank}(G_2) = 2$.

**Связь с УГМ:** $N = \dim(\text{Im}(\mathbb{O})) = 7$ — [двухтрековое обоснование](../core/foundations/axiom-omega#октонионная-структура) Аксиомы 3.
:::

---

**Связанные документы:**
- [Голоном](/docs/core/structure/holon) — определение $\mathbb{H}$
- [Семь измерений](/docs/core/structure/dimensions) — базис $\mathcal{H}$
- [Матрица когерентности](/docs/core/dynamics/coherence-matrix) — определение $\Gamma$
- [Эволюция](/docs/core/dynamics/evolution) — динамика $d\Gamma(\tau)/d\tau$
- [Эмерджентное время](/docs/proofs/dynamics/emergent-time) — вывод τ из структуры Γ
- [Жизнеспособность](/docs/core/dynamics/viability) — мера $P$ и $P_{\text{crit}}$
- [Самонаблюдение](/docs/consciousness/foundations/self-observation) — меры $R$, $C$, $D_{\text{diff}}$
- [Измерение Единства](/docs/core/structure/dimension-u) — мера $\Phi$
- [Формализация оператора φ](/docs/proofs/categorical/formalization-phi) — типизированная поддержка, численные самомодели и замороженные CPTP-реализации
- [Категорный формализм](/docs/proofs/categorical/categorical-formalism) — функтор $F$, ∞-группоид $\mathbf{Exp}_\infty$
- [Иерархия интериорности](/docs/proofs/consciousness/interiority-hierarchy) — вложенная иерархия и калиброванные сертификаты метамоделей
- [Бимодульная конструкция](/docs/proofs/physics/bimodule-construction) — SM-представления из бимодулей импортированного конечного пространства $H_F$ Конна; вывод из спектральной тройки УГМ (T-178) отозван [✗] (2026-09-25) — у $H_{\text{int}} = \mathbb{C}^7$ 7 состояний, а поколению нужно 32, и вещественной структуры KO-размерности 6 на $\mathbb{C}^7$ нет; T-179 отозвана в данной формулировке (T-178–T-181)
- [Вычислительная реализация](./computational) — Python-код
