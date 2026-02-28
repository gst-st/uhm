---
sidebar_position: 2
title: Нотация
description: Математические обозначения теории УГМ
---

# Математическая Нотация

:::warning Потенциальные конфликты нотации
В теории УГМ некоторые символы имеют несколько значений в зависимости от контекста:
- $D$ — [измерение Динамики](/docs/core/structure/dimension-d) **vs** $D_{\text{diff}}$ — [мера дифференциации](/docs/consciousness/foundations/self-observation#мера-сознательности-c)
- $\mathcal{H}$ — гильбертово пространство **vs** $H$ — гамильтониан **vs** $\mathcal{H}_\Gamma$ — гессиан свободной энергии (в [Freedom](/docs/core/foundations/consequences#freedom-конечномерное))
- $\Phi$ — [мера интеграции](/docs/core/structure/dimension-u#мера-интеграции-φ). Для обозначения произвольных CPTP-каналов используется $\Psi$
- $R$ — [мера рефлексии](/docs/consciousness/foundations/self-observation#мера-рефлексии-r) **vs** $\mathcal{R}$ — регенеративный член
- $\mathcal{C}$ — примитивная категория (Аксиома Ω⁷) **vs** $C$ — [мера сознательности](/docs/consciousness/foundations/self-observation#мера-сознательности-c). Пространство контекстов в категории Exp обозначается $\Gamma_{-E}$
- $\gamma_{ij}$ — элементы матрицы когерентности **vs** $\gamma_k$ — скорости декогеренции в диссипаторе Линдблада (в разных документах). **Рекомендация:** для скоростей декогеренции использовать $\Gamma_2$ (как в [Теореме 8.1](/docs/applied/coherence-cybernetics/theorems#теорема-81-условная-необходимость-интериорности-no-zombie))

Контекст обычно делает значение однозначным.
:::

:::info Связь с IIT (Integrated Information Theory)
Мера интеграции $\Phi$ в УГМ **отличается** от $\Phi$ в теории Тонони (IIT):

| Параметр | УГМ | IIT |
|----------|-----|-----|
| **Определение** | $\Phi_{\text{UHM}} = \sum_{i \neq j} \lvert\gamma_{ij}\rvert^2 / \sum_i \gamma_{ii}^2$ | $\Phi_{\text{IIT}}$ = минимум взаимной информации при партициях |
| **Интерпретация** | Когерентность между измерениями | Интегрированная информация |
| **Вычислительная сложность** | $O(n^2)$ | NP-трудно |

УГМ обобщает IIT: мера сознательности $C = \Phi \times R$ **[Т T-140]** включает интеграцию $\Phi$ и рефлексию $R$. Дифференциация $D_{\text{diff}} \geq D_{\min}$ — отдельное условие жизнеспособности.
:::

## Основные символы

| Символ | Значение | Определение |
|--------|----------|-------------|
| $\mathcal{C}$ | [Примитивная категория](/docs/core/foundations/axiom-omega#примитив) | Малая категория с конечным числом объектов — **единственный примитив** |
| $\Gamma$ | [Матрица когерентности](/docs/core/dynamics/coherence-matrix) | $\Gamma \in \mathcal{L}(\mathcal{H})$, $\Gamma^\dagger = \Gamma$, $\Gamma \geq 0$, $\mathrm{Tr}(\Gamma) = 1$ |
| $\mathbb{H}$ | [Голоном](/docs/core/structure/holon) | Минимальная самодостаточная единица реальности |
| $\mathcal{H}$ | Гильбертово пространство | $\mathcal{H} = \mathbb{C}^7$ — см. [Семь измерений](/docs/core/structure/dimensions) |
| $P$ | [Чистота](/docs/core/dynamics/viability#определение-чистоты) | $P = \mathrm{Tr}(\Gamma^2) \in [1/7, 1]$ |
| $S_{vN}$ | Энтропия фон Неймана | $S_{vN} = -\mathrm{Tr}(\Gamma \log \Gamma) \in [0, \log 7]$ |
| $\tau$ | [Внутреннее время](/docs/proofs/dynamics/emergent-time) | Параметр эволюции, выведенный из структуры $\mathcal{C}$; $\tau \in \mathbb{Z}_7$ для 7D |
| $t, t'$ | Временной параметр в формулах | Используется в интегралах и историях; связано с $\tau$ через $t = n \cdot \delta\tau$ |
| $H_{\text{eff}}$ | [Эффективный гамильтониан](/docs/core/dynamics/evolution#вывод-h_eff) | $H_{\text{eff}}(\tau) = H_{6D} + \langle\tau\vert H_{\text{int}}\vert\tau\rangle_O$ |
| $d_B$ | [Метрика Бурес](/docs/proofs/dynamics/emergent-time#41-метрика-бурес) | Угловая: $d_B^{\mathrm{angle}} = \arccos(\sqrt{F})$; хордовая: $d_B^{\mathrm{chord}} = \sqrt{2(1-\sqrt{F})}$. См. [конвенцию ниже](#топология-гротендика) |

## Базовое пространство и стратификация

| Символ | Значение | Определение |
|--------|----------|-------------|
| $X$ | [Базовое пространство](/docs/core/foundations/spacetime#базовое-пространство) | $X = \|N(\mathcal{C})\|$ — геометрическая реализация нерва категории |
| $N(\mathcal{C})$ | [Нерв категории](/docs/core/foundations/spacetime#нерв-категории) | Симплициальное множество: n-симплексы = композируемые цепочки морфизмов |
| $T$ | [Терминальный объект](/docs/core/foundations/axiom-omega#свойство-3) | $T = \Gamma^*$ — глобальный аттрактор; $\forall\Gamma, \exists! f: \Gamma \to T$ |
| $S_\alpha$ | [Страта](/docs/core/foundations/spacetime#стратификация-x) | Компонента стратификации $X = \bigsqcup_\alpha S_\alpha$; $S_0 = \{T\}$ |
| $d_{strat}$ | [Стратифицированная метрика](/docs/core/foundations/spacetime#метрика-конна) | $d_{strat}(\omega_1, \omega_2) = \inf_\gamma \int_\gamma ds_\alpha$ |
| $\text{Link}(T)$ | Линк терминального объекта | $\text{Link}(T) \cong S^6$ — 6-сфера |
| $H^*(X)$ | [Когомологии](/docs/core/foundations/consequences#когомологический-монизм) | $H^n(X, \mathcal{F}) = 0$ для $n > 0$ (монизм) |
| $H^*_{loc}(X,T)$ | [Локальные когомологии](/docs/core/foundations/spacetime#локально-глобальная-дихотомия) | $H^*_{loc}(X,T) \cong \tilde{H}^{*-1}(S^6) \neq 0$ (физика) |
| $D^b(X)$ | [Производная категория](/docs/proofs/categorical/categorical-formalism#производные-категории) | Ограниченная производная категория пучков на X |
| $IC(S_\alpha)$ | IC-пучок | Intersection cohomology пучок страты $S_\alpha$ |

## Измерения

Семь базисных состояний [пространства $\mathcal{H}$](/docs/core/structure/dimensions):

| Символ | Измерение | Связанная структура | Подробнее |
|--------|-----------|---------------------|-----------|
| $A$ | Артикуляция | Проекторы, измерения | [→](/docs/core/structure/dimension-a) |
| $S$ | Структура | Гамильтониан $H$ | [→](/docs/core/structure/dimension-s) |
| $D$ | Динамика | Унитарная эволюция $U(\tau)$ | [→](/docs/core/structure/dimension-d) |
| $L$ | Логика | Алгебра операторов | [→](/docs/core/structure/dimension-l) |
| $E$ | Интериорность | Матрица плотности $\rho_E$ | [→](/docs/core/structure/dimension-e) |
| $O$ | Основание | Вакуумное состояние $\vert 0\rangle$, внутренние часы ([Page-Wootters](/docs/proofs/dynamics/emergent-time)) | [→](/docs/core/structure/dimension-o) |
| $U$ | Единство | Операция следа $\mathrm{Tr}$ | [→](/docs/core/structure/dimension-u) |

## Базис пространства состояний

$$
\mathcal{H} = \mathrm{span}\{|A\rangle, |S\rangle, |D\rangle, |L\rangle, |E\rangle, |O\rangle, |U\rangle\} = \mathbb{C}^7
$$

Ортонормированность: $\langle i|j\rangle = \delta_{ij}$ для $i, j \in \{A, S, D, L, E, O, U\}$.

## Алгебра часов (Page-Wootters)

| Символ | Значение | Определение |
|--------|----------|-------------|
| $H_O$ | [Гамильтониан часов](/docs/core/structure/dimension-o#гамильтониан-часов-h_o) | $H_O = \omega_0 \sum_{k=0}^{N-1} k \vert k\rangle\langle k\vert_O$ |
| $V_O$ | [Оператор сдвига времени](/docs/core/structure/dimension-o#оператор-сдвига-v_o) | $V_O^N = \mathbb{1}$, $V_O H_O V_O^\dagger = H_O + \omega_0 \mathbb{1}$ |
| $\mathcal{A}_O$ | [C*-алгебра часов](/docs/core/structure/dimension-o#c-алгебра-часов-a_o) | $\mathcal{A}_O = C^*(H_O, V_O) \cong M_N(\mathbb{C})$ |
| $H_{\text{int}}$ | [Гамильтониан взаимодействия](/docs/core/foundations/axiom-omega#гамильтониан-взаимодействия) | Связь O с E и U |
| $\hat{C}$ | [Ограничение Page-Wootters](/docs/core/foundations/axiom-omega#свойство-2) | $\hat{C} = H_O \otimes \mathbb{1}_{6D} + \mathbb{1}_O \otimes H_{6D} + H_{\text{int}}$ |
| $\mathcal{H}_{total}$ | Глобальное пространство | $\mathcal{H}_{total} = \mathcal{H}_O \otimes \mathcal{H}_{6D}$, $\dim = 42$ |
| $\omega_0$ | Фундаментальная частота | Базовая частота часов O |
| $\vert\tau_n\rangle$ | Базис часов | Собственные состояния $V_O$ |

## Уравнение эволюции

Полное [уравнение эволюции](/docs/core/dynamics/evolution) с [эмерджентным внутренним временем](/docs/proofs/dynamics/emergent-time) τ:

$$
\frac{d\Gamma(\tau)}{d\tau} = -i[H_{\text{eff}}, \Gamma] + \mathcal{D}[\Gamma] + \mathcal{R}[\Gamma, E]
$$

где:

**[Унитарный член](/docs/core/dynamics/evolution#1-унитарный-член):**
$$
-i[H_{\text{eff}}, \Gamma] = -i(H_{\text{eff}}\Gamma - \Gamma H_{\text{eff}})
$$

Здесь $H_{\text{eff}}$ — эффективный гамильтониан, возникающий из ограничения Page-Wootters.

**[Диссипативный член](/docs/core/dynamics/evolution#логический-лиувиллиан):**
$$
\mathcal{D}[\Gamma] = \sum_k \gamma_k \left( L_k \Gamma L_k^\dagger - \frac{1}{2}\{L_k^\dagger L_k, \Gamma\} \right)
$$

**[Регенеративный член](/docs/core/dynamics/evolution#3-регенеративный-член) [Т]:**
$$
\mathcal{R}[\Gamma, E] = \kappa(\Gamma) \cdot (\rho_* - \Gamma) \cdot g_V(P)
$$

где:
- $\kappa(\Gamma) \geq 0$ — скорость регенерации [Т] (сопряжение $\mathcal{D}_\Omega \dashv \mathcal{R}$)
- $\rho_* = \varphi(\Gamma)$ — категориальная самомодель текущего состояния [Т] ([оператор φ](/docs/core/operators/phi-operator))
- $(\rho_* - \Gamma)$ — единственная CPTP-релаксация [Т]
- $g_V(P) = \mathrm{clamp}\!\bigl(\frac{P - P_{\mathrm{crit}}}{P_{\mathrm{opt}} - P_{\mathrm{crit}}}\bigr)$ — V-preservation gate [Т] (Ландауэр + V-инвариантность, [вывод](/docs/core/dynamics/evolution#теорема-v-preservation-gate))

## Коммутаторы и антикоммутаторы

| Обозначение | Определение |
|-------------|-------------|
| $[A, B]$ | $AB - BA$ (коммутатор) |
| $\{A, B\}$ | $AB + BA$ (антикоммутатор) |

## Операторы интериорности (измерение E)

См. [Измерение Интериорности](/docs/core/structure/dimension-e) и [Категория Exp](/docs/proofs/categorical/categorical-formalism#2-категория-exp).

| Обозначение | Значение |
|-------------|----------|
| $\rho_E$ | Редуцированная матрица плотности измерения Интериорности |
| $\lambda_i$ | Собственное значение $\Gamma$ (интенсивность) |
| $\vert q_i\rangle$ | Собственный вектор $\Gamma$ (качество) |
| $[\vert q\rangle]$ | Класс эквивалентности в $\mathbb{P}(\mathcal{H}_E)$ |
| $\mathbb{P}(\mathcal{H}_E)$ | [Проективное пространство](/docs/reference/specification#проективное-пространство-качеств) качеств |
| $d_{\mathrm{FS}}$ | [Метрика Фубини-Штуди](/docs/reference/specification#метрика-фубини-штуди) |

**Метрика Фубини-Штуди:**
$$
d_{\mathrm{FS}}([|\psi\rangle], [|\phi\rangle]) = \arccos(|\langle\psi|\phi\rangle|) \in [0, \pi/2]
$$

## Меры сознательности

См. [Самонаблюдение](/docs/consciousness/foundations/self-observation) для полных определений.

| Мера | Формула | Диапазон |
|------|---------|----------|
| [Интеграция $\Phi$](/docs/core/structure/dimension-u#мера-интеграции-φ) | $\Phi(\Gamma) = \dfrac{\sum_{i \neq j} \lvert\gamma_{ij}\rvert^2}{\sum_i \gamma_{ii}^2}$ | $[0, +\infty)$ |
| [Дифференциация $D_{\text{diff}}$](/docs/consciousness/foundations/self-observation#мера-сознательности-c) | $D_{\text{diff}}(\Gamma) = \exp(S_{vN}(\rho_E))$ | $[1, 7]$ |
| [Рефлексия $R$](/docs/consciousness/foundations/self-observation#мера-рефлексии-r) | $R(\Gamma) = 1 - \dfrac{\|\Gamma - \varphi(\Gamma)\|_F^2}{\|\Gamma\|_F^2}$ | $[0, 1]$ |
| [Сознательность $C$](/docs/consciousness/foundations/self-observation#мера-сознательности-c) | $C(\Gamma) = \Phi \times D_{\text{diff}} \times R$ | $[0, +\infty)$ |
| Свобода воли $\mathrm{Freedom}(\Gamma)$ **[Т]** | $\mathrm{Freedom}(\Gamma) = \dim\ker(\mathcal{H}_\Gamma) + 1$, где $\mathcal{H}_\Gamma = \partial^2 \mathcal{F}/\partial\Gamma^2$ — [конечномерное определение](/docs/core/foundations/consequences#freedom-конечномерное). ∞-категорная мотивация: $\pi_0(\mathrm{Map}(\Gamma, T)^{\text{non-trivial}})$ | $\{1, \ldots, 7\}$ |
| Энтропия свободы $S_{\text{freedom}}$ | $S_{\text{freedom}} = \log(\text{Freedom}(\Gamma))$ | $[0, \log 7]$ |

## Оператор самомоделирования

См. [Формализация оператора φ](/docs/proofs/categorical/formalization-phi) для полного описания.

**CPTP-канал** (Completely Positive Trace-Preserving):
$$
\varphi(\Gamma) = \sum_m K_m \Gamma K_m^\dagger
$$

**Условие полноты** (сохранение следа):
$$
\sum_m K_m^\dagger K_m = I
$$

**Сходимость к неподвижной точке** $\Gamma^* = \varphi(\Gamma^*)$:
$$
\|\varphi^n(\Gamma_0) - \Gamma^*\|_F \leq k^n \cdot \|\Gamma_0 - \Gamma^*\|_F, \quad k \in [0, 1)
$$

## Иерархия интериорности

См. [Иерархия интериорности](/docs/proofs/consciousness/interiority-hierarchy) для формальных условий и доказательств.

| Уровень | Обозначение | Условие | n-усечение |
|---------|-------------|---------|------------|
| L0 | $\mathrm{Int}(S)$ — Интериорность | $\exists \rho_E$ | $\tau_{\leq 0}$ |
| L1 | $\mathrm{PG}(S)$ — Феноменальная геометрия | $\mathrm{rank}(\rho_E) > 1$ | $\tau_{\leq 1}$ |
| L2 | Когнитивные квалиа | $R \geq R_{\text{th}}$, $\Phi \geq \Phi_{\text{th}}$, $D_{\text{diff}} \geq 2$ | $\tau_{\leq 2}$ |
| L3 | Сетевое сознание | $R^{(2)} \geq R^{(2)}_{\text{th}}$ (метастабильно) | $\tau_{\leq 3}$ |
| L4 | Унитарное сознание | $\lim_{n \to \infty} R^{(n)} > 0$, $P > 6/7$ | $\tau_{\leq \infty}$ |

**Пороговые значения** ([все доказаны математически [Т]](/docs/core/foundations/axiom-septicity#пороги-l2-строгий-вывод), [обоснования порогов](/docs/proofs/consciousness/interiority-hierarchy#обоснование-порогов)):

| Порог | Значение | Статус |
|-------|----------|--------|
| $R_{\text{th}}$ | $1/3$ | [Т] Теорема ($K=3$ из триадной декомпозиции + байесовское доминирование) |
| $\Phi_{\text{th}}$ | $1$ | [Т] Теорема (T-129: единственное самосогласованное значение) |
| $R^{(2)}_{\text{th}}$ | $1/4$ | [Т] Теорема (порог L3) |
| $X^{(n)}_{\text{th}}$ | $1/(n+1)$ | [Т] Универсальная формула |

## Тензор напряжений

См. [Жизнеспособность](/docs/core/dynamics/viability) для полного описания.

$$
\sigma_{\mathrm{sys}}(\Gamma) = [\sigma_A, \sigma_S, \sigma_D, \sigma_L, \sigma_E, \sigma_O, \sigma_U]^T \in \mathbb{R}^7
$$

**Условие жизнеспособности:**
$$
\|\sigma_{\mathrm{sys}}(\Gamma)\|_\infty < 1
$$

**Запас жизнеспособности:**
$$
\mathrm{margin}(\Gamma) = 1 - \|\sigma_{\mathrm{sys}}(\Gamma)\|_\infty > 0
$$

## Топология Гротендика

См. [Топология Гротендика](/docs/core/foundations/axiom-omega#топология-гротендика) и [Категорный формализм](/docs/proofs/categorical/categorical-formalism#63-топология-гротендика-на-densitymat-и-exp).

**Метрика Бюреса (канонический вид):**
$$
d_B(\Gamma_1, \Gamma_2) = \arccos\left(\mathrm{Tr}\sqrt{\sqrt{\Gamma_1}\Gamma_2\sqrt{\Gamma_1}}\right) = \arccos(\sqrt{F})
$$

**Fidelity (верность):**
$$
\mathrm{Fid}(\Gamma_1, \Gamma_2) = \left(\mathrm{Tr}\sqrt{\sqrt{\Gamma_1}\Gamma_2\sqrt{\Gamma_1}}\right)^2
$$

:::note Обозначение Fid vs F
$\mathrm{Fid}$ используется для верности (fidelity) в контекстах, где $F$ может быть спутан с [функтором опыта](/docs/proofs/categorical/categorical-formalism#3-функтор-f-на-объектах) $F: \mathbf{DensityMat} \to \mathbf{Exp}$. В формулах, где контекст однозначен, допускается обозначение $F$.
:::

:::note Две формы метрики Бюреса
УГМ использует **обе формы** в зависимости от контекста:

| Форма | Формула | Применение |
|-------|---------|------------|
| **Угловая** | $d_B^{angle} = \arccos(\sqrt{F})$ | Геометрические теоремы ([эмерджентное время](/docs/proofs/dynamics/emergent-time#41-метрика-бурес)) |
| **Хордовая** | $d_B^{chord} = \sqrt{2(1-\sqrt{F})}$ | Вычисления, [ΔF](/docs/core/dynamics/evolution#каноническое-delta-f), [спецификация](/docs/reference/specification#топология-гротендика) |

**Связь:** $d_B^{chord} = \sqrt{2(1 - \cos(d_B^{angle}))} \approx \sqrt{2} \cdot d_B^{angle}$ для малых расстояний.
:::

**Bures-шар:**
$$
B_B(\Gamma, r) = \{\Sigma \in \mathcal{C} : d_B(\Gamma, \Sigma) < r\}
$$

**Bures-покрытие:** Семейство $\{\Phi_i: \Gamma_i \to \Gamma\}_{i \in I}$ покрывает $\Gamma$, если:
$$
\forall \epsilon > 0, \exists \delta > 0: \quad B_B(\Gamma, \delta) \subseteq \bigcup_{i \in I} \Phi_i(B_B(\Gamma_i, \epsilon))
$$

**Сайт:** Пара $(\mathcal{C}, J_{Bures})$ где $J_{Bures}$ — функция покрытий.

**Классификатор из топологии:**
$$
\Omega = \mathcal{O}(\mathcal{C}, d_B)
$$

## Специальные обозначения

| Обозначение | Значение |
|-------------|----------|
| $\lVert\cdot\rVert_F$ | Норма Фробениуса: $\lVert A\rVert_F = \sqrt{\mathrm{Tr}(A^\dagger A)} = \sqrt{\sum_{ij} \lvert a_{ij}\rvert^2}$ |
| $\lVert\cdot\rVert_\infty$ | Супремум-норма: $\lVert x\rVert_\infty = \max_i \lvert x_i\rvert$ |
| $d_B(\cdot, \cdot)$ | Метрика Бюреса |
| $\mathrm{Fid}(\cdot, \cdot)$ / $F(\cdot, \cdot)$ | Fidelity (верность); $\mathrm{Fid}$ предпочтительно для отличия от функтора $F$ |
| $B_B(\Gamma, r)$ | Bures-шар радиуса $r$ с центром $\Gamma$ |
| $J_{Bures}$ | Функция Bures-покрытий (топология Гротендика) |
| $\Theta(\cdot)$ | Функция Хевисайда |
| $\delta_{ij}$ | Символ Кронекера |
| $\mathrm{Tr}(\cdot)$ | След матрицы |
| $A^\dagger$ | Эрмитово сопряжение |
| $\mathrm{Coh}_E$ | E-когерентность (HS-проекция $\pi_E$) **[Т]**, $\in [1/7, 1]$; $= \|\pi_E(\Gamma)\|_{\mathrm{HS}}^2 / \|\Gamma\|_{\mathrm{HS}}^2$ — [мастер-определение](/docs/core/foundations/axiom-septicity#e-coherence-definition), [HS-проекция](/docs/core/foundations/axiom-septicity#hs-projection), [справка КК](/docs/applied/coherence-cybernetics/definitions#e-когерентность) |
| ПИР | Принцип Информационной Различимости **[О]** (T16) — [определение](/docs/core/foundations/axiom-septicity#формулировка-пир), встроенное в A1+A2: различимость по $J_{\text{Bures}}$-покрытиям тождественна онтологической различимости |
| $\varphi_{\text{coh}}$ | Когерентно-сохраняющее самомоделирование — обобщённый оператор φ, сохраняющий когерентности ([Фано-канал](/docs/proofs/gap/fano-channel)) |
| $\kappa(\Gamma)$ | Коэффициент регенерации: $\kappa(\Gamma) = \kappa_{\text{bootstrap}} + \kappa_0 \cdot \mathrm{Coh}_E$ |
| $D_{\text{diff}}$ | Дифференцировочная размерность — число измерений, в которых $\Gamma$ отклоняется от $I/N$ |
| $P_{\text{crit}}$ | Критическая чистота $= 2/N = 2/7$ — [теорема](/docs/proofs/dynamics/theorem-purity-critical) |
| $d_B^{chord}$ | Хордальная форма метрики Бюреса: $d_B^{chord} = \sqrt{2(1 - \sqrt{F(\rho, \sigma)})}$ |
| (AP), (PH), (QG), (V) | Четыре условия определения Голонома: автопоэзис, феноменальность, квантовая геометрия, жизнеспособность |

## Категорная нотация

См. [Категорный формализм](/docs/proofs/categorical/categorical-formalism) для полного описания.

| Обозначение | Значение |
|-------------|----------|
| $\mathcal{C}$ | [Примитивная категория УГМ](/docs/core/foundations/axiom-omega#примитив) — единственный примитив |
| $\mathbf{DensityMat}$ | [Категория матриц плотности](/docs/proofs/categorical/categorical-formalism#1-категория-densitymat) |
| $\mathbf{Exp}$ | [Категория экспериенциальных состояний](/docs/proofs/categorical/categorical-formalism#2-категория-exp) |
| $\mathbf{Hol}$ | Категория Голономов |
| $T$ | [Терминальный объект](/docs/core/foundations/axiom-omega#свойство-3) — $\forall\Gamma, \exists! f: \Gamma \to T$ |
| $F: \mathbf{DensityMat} \to \mathbf{Exp}$ | [Функтор опыта](/docs/proofs/categorical/categorical-formalism#3-функтор-f-на-объектах) |
| $\mathrm{CPTP}$ | Completely Positive Trace-Preserving каналы |
| $\mathrm{Mor}(\rho_1, \rho_2)$ | Морфизмы между объектами |
| $\otimes$ | Тензорное произведение (композиция Голономов) |
| $\mathbf{Exp}_\infty$ | [∞-группоид опыта](/docs/proofs/categorical/categorical-formalism#10-infty-группоид-и-infty-топос-для-эмерджентного-времени) |
| $\mathbf{Exp}^{disc}_\infty$ | [Дискретный ∞-группоид](/docs/proofs/categorical/categorical-formalism#exp-disc-infty) для $N < \infty$ |
| $\mathbf{Sh}_\infty(\mathbf{Exp})$ | [∞-топос ∞-пучков](/docs/proofs/categorical/categorical-formalism#10-infty-группоид-и-infty-топос-для-эмерджентного-времени) над Exp |
| $\Omega\mathbf{Exp}_\infty$ | Пространство петель — эмерджентная история |
| $D^b(X)$ | [Производная категория](/docs/proofs/categorical/categorical-formalism#производные-категории) пучков на X |
| $\mathbf{Perv}(X)$ | [Категория перверсных пучков](/docs/proofs/categorical/categorical-formalism#производные-категории) |
| $\mathcal{T}_H$ | [∞-топос Голономов](/docs/proofs/categorical/categorical-formalism#infty-топос-голономов) с HoTT как внутренней логикой |
| $\mathrm{Sh}_\infty(\mathcal{C})$ | ∞-топос пучков на категории $\mathcal{C}$, единственный примитив в $\Omega^7$ |
| $\mathrm{Map}(\Gamma, T)$ | Пространство морфизмов в ∞-категории (mapping space) |
| $\pi_n(X)$ | n-ая гомотопическая группа пространства $X$ |
| $\simeq$ | Слабая гомотопическая эквивалентность |
| $\Omega$ | [Классификатор подобъектов](/docs/core/foundations/axiom-omega#внутренняя-логика) — единый источник L, L_k, τ |
| $\chi_S$ | [Характеристический морфизм](/docs/core/structure/dimension-l#категориальное-определение) подобъекта S: $\chi_S: \Gamma \to \Omega$ |
| $L_k$ | [Операторы Линдблада](/docs/core/dynamics/evolution#логический-лиувиллиан): $L_k = P_k = \lvert k\rangle\langle k\rvert$ — операторные представители характеристических морфизмов атомов Ω ([вывод](/docs/core/foundations/axiom-omega#lk-из-omega)). Запись $L_k = \sqrt{\chi_{S_k}}$ — конвенция ($\sqrt{P} = P$ для проекторов) |
| $\mathcal{L}_\Omega$ | [Логический Лиувиллиан](/docs/core/dynamics/evolution#логический-лиувиллиан): $\mathcal{L}_\Omega[\Gamma] = -i[H_{\text{eff}}, \Gamma] + \sum_k (L_k \Gamma L_k^\dagger - \frac{1}{2}\{L_k^\dagger L_k, \Gamma\})$ |
| $\triangleright$ | [Темпоральная модальность](/docs/proofs/dynamics/emergent-time#время-из-модальности) на Ω; $\tau_n = \triangleright^n(\mathrm{now})$ |
| $\mathcal{D}_\Omega \dashv \mathcal{R}$ | [Сопряжение диссипации-регенерации](/docs/core/foundations/axiom-septicity#категориальный-вывод-kappa0); $\kappa_0 = \|\mathrm{Nat}(\mathcal{D}_\Omega, \mathcal{R})\|$ |
| **(МП)** | **Принцип минимального представления** (историческое условие, теперь **[Т]** T11–T13): среди эквивалентных BIBD$(7,3,\lambda)$-каналов выбирается $\lambda = 1$ — минимальное число операторов ($b=7$). Доказан как теорема из (AP)+(PH)+(QG)+(V); мост к P1+P2 полностью замкнут **[Т]**. [Мост к P1+P2](/docs/core/foundations/axiom-septicity#мост-p1p2) |
| **(КГ)** | **Каноническая группировка** (историческое): категориально натуральный механизм группировки атомов Ω в составные блоки. Заменено более слабым (МП), которое в свою очередь доказано как теорема T11–T13 |

## Нотация Кибернетики Когерентности

См. [Кибернетика Когерентности](/docs/applied/coherence-cybernetics/definitions) для полного описания.

| Обозначение | Значение |
|-------------|----------|
| $\mathcal{V}$ | [Область жизнеспособности](/docs/core/dynamics/viability) |
| $\mathrm{VIT}$ | Тензор целостности жизнеспособности (Viability Integrity Tensor) |
| $\kappa(\Gamma)$ | Скорость регенерации (функция состояния) |
| $\kappa_0$ | Базовая скорость регенерации: $\kappa_0 = \|\mathrm{Nat}(\mathcal{D}_\Omega, \mathcal{R})\|$ — [категориальный вывод](/docs/core/foundations/axiom-septicity#категориальный-вывод-kappa0) |
| $\mathrm{Coh}_E$ | $E$-когерентность (HS-проекция) **[Т]**: $\mathrm{Coh}_E(\Gamma) = \dfrac{\|\pi_E(\Gamma)\|_{\mathrm{HS}}^2}{\|\Gamma\|_{\mathrm{HS}}^2} = \dfrac{\gamma_{EE}^2 + 2\sum_{i \neq E}\lvert\gamma_{Ei}\rvert^2}{\mathrm{Tr}(\Gamma^2)}$ — **каноническая формула** ([мастер-определение](/docs/core/foundations/axiom-septicity#e-coherence-definition), [HS-проекция](/docs/core/foundations/axiom-septicity#hs-projection)) |
| $P_E$ | Чистота E-сектора (42D): $P_E = \mathrm{Tr}(\rho_E^2)$, где $\rho_E = \mathrm{Tr}_{-E}(\Gamma)$ — **теоретическая конструкция**, определена только в расширенном 42D формализме ($\mathcal{H} = \mathbb{C}^{42}$). Формальная эквивалентность $\mathrm{Coh}_E \approx P_E$ — **структурная гипотеза [Г]** ([подробнее](/docs/applied/coherence-cybernetics/definitions#e-когерентность)) |
| $P_{\text{crit}}$ | Критическая чистота $= 2/7 \approx 0.286$ — [теорема](/docs/proofs/dynamics/theorem-purity-critical) |
| $\theta_i$ | Пороги компонент стресса |
| $H_{\text{eff}}$ | Эффективный гамильтониан: $H_{\text{eff}}(\tau) = H_{6D} + \langle\tau\vert H_{\text{int}}\vert\tau\rangle_O$ — возникает из ограничения Page-Wootters |
| $g_V(P)$ | V-preservation gate: $\mathrm{clamp}\!\bigl(\frac{P - P_{\mathrm{crit}}}{P_{\mathrm{opt}} - P_{\mathrm{crit}}}, 0, 1\bigr)$; активирует регенерацию при $P > P_{\mathrm{crit}}$ ([вывод](/docs/core/dynamics/evolution#теорема-v-preservation-gate)) |
| $\Theta(\Delta F)$ | Функция Хевисайда от изменения свободной энергии $\Delta F$; необходимое условие из принципа Ландауэра (уточнено $g_V(P)$) |
| $\rho_*$ ($= \Gamma_{\text{target}}$) | Единственное стационарное состояние $\mathcal{L}_\Omega$ [Т]: $\rho_* = \varphi(\Gamma) = \lim_{\tau\to\infty} e^{\tau\mathcal{L}_\Omega}[\Gamma]$ — цель регенерации |
| $\omega_0$ | Фундаментальная частота часов — параметр вычислительного приближения; см. [κ₀](/docs/core/foundations/axiom-septicity#категориальный-вывод-kappa0) |
| $D_{\mathrm{KL}}$ | Расхождение Кульбака-Лейблера: $D_{\mathrm{KL}}(p \| q) = \sum_i p_i \log(p_i / q_i)$ |

## Индексы измерений (Протокол измерения) {#индексы-измерений-протокол-измерения}

Эмпирические индексы для измерения проекций Γ в ИИ-системах. См. [Протокол измерения](/docs/applied/research/measurement-protocol) для полного описания.

| Индекс | Измерение | ИИ-метрика | Формула |
|--------|-----------|------------|---------|
| $I_A$ | Артикуляция | Взаимная информация вход↔латент | $I_A = I(\text{input}; \text{latent}) / H(\text{input})$ |
| $I_S$ | Структура | Ранг Якобиана | $I_S = \mathrm{rank}_\varepsilon(J_f) / \min(d_{\text{out}}, d_{\text{in}})$ |
| $I_D$ | Динамика | Ляпуновский экспонент | $I_D = \max_i \lambda_i^{\text{Lyap}}$ (нормированный) |
| $I_L$ | Логика | Коммутаторы слоёв | $I_L = 1 - \|[f_i, f_j]\|_F / (\|f_i\| \cdot \|f_j\|)$ |
| $I_E$ | Интериорность | Дифференциация (энтропия) | $I_E = D_{\text{diff}}^{\text{approx}} = \exp(S_{vN}(\rho_{\text{attn}}))$ — [см. измерение E](/docs/core/structure/dimension-e#порог-дифференциации-d_min--2) |
| $I_O$ | Основание | Устойчивость к шуму | $I_O = 1 - \|\nabla_\epsilon \mathbf{h}\|_F$ |
| $I_U$ | Единство | Effective Φ (интеграция) | $I_U = \Phi_{\text{eff}} = \lambda_2(L_{\text{attn}}) / \lambda_{\max}(L_{\text{attn}})$ — [см. измерение U](/docs/core/structure/dimension-u#мера-интеграции-φ) |

**Связь с Γ:** Диагональные элементы $\gamma_{ii} \approx I_i^2$ (эмпирическая калибровка).

### Дополнительные прикладные символы

| Обозначение | Значение |
|-------------|----------|
| $G$ | Квази-функтор $\mathbf{AIState} \to \mathbf{DensityMat}$ — отображение состояния ИИ в матрицу плотности |
| $J_P$ | Поток когерентности: $J_P = dP/d\tau$ |
| $\varepsilon_{\text{functor}}$ | Верхняя граница ошибки квази-функтора $G$ |
| $P_{\text{norm}}$ | Нормализованная чистота: $(P - P_{\text{crit}}) / (1 - P_{\text{crit}})$ |
| $\mathbf{r}$ | Обобщённый вектор Блоха: $\Gamma = I/N + \sum_k r_k \lambda_k / 2$ |

## Октонионная нотация

См. [Структурный вывод через октонионы](/docs/proofs/minimality/theorem-octonionic-derivation) для полного описания.

| Обозначение | Значение |
|-------------|----------|
| $\mathbb{O}$ | Алгебра октонионов — 8-мерная нормативная алгебра с делением над $\mathbb{R}$ |
| $\mathrm{Im}(\mathbb{O})$ | Мнимая часть октонионов; $\dim(\mathrm{Im}(\mathbb{O})) = 7$ |
| $e_1, \ldots, e_7$ | Мнимые единицы октонионов; $e_i^2 = -1$, $e_i e_j = -e_j e_i$ ($i \neq j$) |
| $G_2$ | $\mathrm{Aut}(\mathbb{O})$ — 14-параметрическая группа автоморфизмов октонионов; $G_2 \subset SO(7)$ |
| $\mathrm{PG}(2,2)$ | Плоскость Фано — проективная плоскость над $\mathbb{F}_2$; 7 точек, 7 линий, 3 точки на линии |
| $[x, y, z]$ | Ассоциатор: $[x, y, z] = (xy)z - x(yz)$; мера неассоциативности |
| $H(7,4)$ | Код Хэмминга: 4 информационных + 3 контрольных бита; связь с PG(2,2) |
| **P1** | Теорема [Т]: пространство внутренних степеней свободы $\cong \mathrm{Im}(\mathbb{A})$ для алгебры с делением $\mathbb{A}$ (выводится по цепочке T15) |
| **P2** | Теорема [Т]: неассоциативность ($[x, y, z] \neq 0$ для некоторых $x, y, z$) (выводится по цепочке T15) |

:::warning Статус октонионной нотации [И]
Соответствие $e_i \leftrightarrow$ измерение — **интерпретация** [И]. Математические операции на $\mathbb{O}$ (умножение, ассоциатор) строги [Т]; их физическая реализация в пространстве $\{A,S,D,L,E,O,U\}$ — [открытая проблема](/docs/proofs/minimality/theorem-octonionic-derivation#открытые-проблемы).
:::

## Gap-динамика и Фано-структура

Символы, связанные с [Gap-оператором](/docs/core/dynamics/gap-dynamics), [термодинамикой Gap](/docs/core/dynamics/gap-thermodynamics) и [правилами отбора Фано](/docs/physics/gauge-symmetry/fano-selection-rules).

| Обозначение | Значение |
|-------------|----------|
| $\hat{G}$ | [Gap-оператор](/docs/core/dynamics/gap-dynamics): $\hat{G} = \mathrm{Im}(\Gamma) \in \mathfrak{so}(7)$ — мнимая часть матрицы когерентности |
| $P_{\mathrm{Fano}}$ | [Фано-предиктивный канал](/docs/physics/gauge-symmetry/fano-selection-rules): $P_{\mathrm{Fano}}(\Gamma) = \tfrac{1}{3}\sum_p \Pi_p \Gamma \Pi_p$ — усреднение по Фано-линиям |
| $\Pi_p$ | Проектор на 3-мерное подпространство Фано-линии $p$ ($p = 1, \ldots, 7$) |
| $\alpha^*$ | Оптимальный параметр самомоделирования: $\alpha^* = \operatorname{argmin} F[P_\alpha;\, \Gamma]$ |
| $T_{\mathrm{eff}}$ | [Эффективная температура Gap](/docs/core/dynamics/gap-thermodynamics): $T_{\mathrm{eff}} = (\Gamma_2 / \kappa_0) \cdot k_B \cdot T_{\mathrm{phys}}$ |
| $\xi_F$ | Корреляционная длина Фано: $\xi_F \sim 160\;\text{пк}$ — масштаб пространственных корреляций Фано-мод |
| $\Theta_M$ | Тета-функция намотки с Фано-характером |
| $Z_\Phi(s)$ | Эпштейновская дзета-функция с Фано-характером |
| $B^{(b)}$ | Билинейная форма на $(S^1)^{21}$ с Фано-контракцией |
| $N_F$ | Число некоррелированных Фано-мод: $N_F \sim 6{,}8 \times 10^{23}$ |
| $r = \kappa / \Gamma_2$ | Безразмерный параметр жизнеспособности — отношение скорости регенерации к скорости декогеренции |
| $t = T_{\mathrm{eff}} / T_c$ | Безразмерная температура — приведённая к критическому значению $T_c$ |

---

**Связанные документы:**
- [Глоссарий](./glossary) — определения терминов
- [Математический аппарат](/docs/reference/specification) — формальные определения
- [Вычислительная реализация](/docs/reference/computational) — Python-код
- [Матрица когерентности](/docs/core/dynamics/coherence-matrix) — определение $\Gamma$
- [Эволюция](/docs/core/dynamics/evolution) — уравнение $d\Gamma(\tau)/d\tau$
- [Эмерджентное время](/docs/proofs/dynamics/emergent-time) — вывод τ из структуры Γ
- [Жизнеспособность](/docs/core/dynamics/viability) — мера $P$ и $P_{\text{crit}}$
- [Самонаблюдение](/docs/consciousness/foundations/self-observation) — меры $R$, $\Phi$, $D_{\text{diff}}$, $C$
- [Иерархия интериорности](/docs/proofs/consciousness/interiority-hierarchy) — уровни L0→L1→L2→L3→L4
- [Категорный формализм](/docs/proofs/categorical/categorical-formalism) — функтор $F$, ∞-группоид $\mathbf{Exp}_\infty$
- [Формализация оператора φ](/docs/proofs/categorical/formalization-phi) — CPTP-каналы
- [Структурный вывод через октонионы](/docs/proofs/minimality/theorem-octonionic-derivation) — P1+P2 → 𝕆 → N=7
- [Динамика Gap](/docs/core/dynamics/gap-dynamics) — Gap-оператор $\hat{G}$, бифуркации, немарковская динамика
- [Термодинамика Gap](/docs/core/dynamics/gap-thermodynamics) — $T_{\mathrm{eff}}$, вариационный принцип, ФДТ
- [Правила отбора Фано](/docs/physics/gauge-symmetry/fano-selection-rules) — $P_{\mathrm{Fano}}$, $\Pi_p$, Юкавская иерархия
