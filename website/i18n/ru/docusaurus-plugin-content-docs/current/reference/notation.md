---
sidebar_position: 2
title: Нотация
description: Математические обозначения теории УГМ
---

# Математическая Нотация

Область численных формул ниже — выбранная модель $N=7$ с заданным семантическим репером [П]. Категория процессов, Bures-сайт, логическая поддержка и динамика имеют разные типы; их согласованный интерфейс задаёт [математическое ядро](/docs/reference/mathematical-kernel).

:::warning Потенциальные конфликты нотации
В теории УГМ некоторые символы имеют несколько значений в зависимости от контекста:
- $D$ — [измерение Динамики](/docs/core/structure/dimension-d) **vs** $D_{\text{diff}}$ — [мера дифференциации](/docs/consciousness/foundations/self-observation#мера-сознательности-c)
- $\mathcal{H}$ — гильбертово пространство **vs** $H$ — гамильтониан **vs** $\mathcal{H}_\Gamma$ — гессиан свободной энергии (в [Freedom](/docs/core/foundations/consequences#freedom-конечномерное))
- $\Phi$ — [мера интеграции](/docs/core/structure/dimension-u#мера-интеграции-φ). Для обозначения произвольных CPTP-каналов используется $\Psi$
- $R$ — **каноническая** [мера рефлексии](/docs/consciousness/foundations/self-observation#мера-рефлексии-r) $1/(7P) \in [1/7, 1]$ (сознательная полоса $[1/3, 1/2)$) **vs** $R_\varphi$ — рефлексия как **качество самомодели** (может быть отрицательным; диапазон зависит от $M$) (ранее также обозначалась $Q_\varphi$) **vs** $R^{(n)}$ — fidelity-башня ($n \geq 2$) **vs** $R_{ij}$ — секторная рефлексия **vs** $\mathcal{R}$ — регенеративный член. Формы мер разведены в [трёх рабочих формах R](/docs/consciousness/foundations/self-observation#формы-r)
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

<!-- DRY: Каноническое определение Γ в /docs/core/dynamics/coherence-matrix -->
<!-- DRY: Каноническое определение P = Tr(Γ²) в /docs/core/dynamics/viability#определение-чистоты -->

| Символ | Значение | Определение |
|--------|----------|-------------|
| $\mathcal{C}$ | [Примитивная категория](/docs/core/foundations/axiom-omega#примитив) | Заданная малая индексирующая категория; сама по себе не определяет $N$, каналы или динамику |
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
| $T$ | [Терминальный объект](/docs/reference/mathematical-kernel#terminal-time) | $1_{\mathcal E}$ в топосе; одномерная система в категории процессов. Не $\Gamma_*$ и не $I/7$ |
| $S_\alpha$ | [Страта](/docs/core/foundations/spacetime#стратификация-x) | Заданная стратификация $X=\bigsqcup_\alpha S_\alpha$; из нерва или терминальности не следует |
| $d_{strat}$ | [Стратифицированная метрика](/docs/core/foundations/spacetime#метрика-конна) | $d_{strat}(\omega_1, \omega_2) = \inf_\gamma \int_\gamma ds_\alpha$ |
| $\text{Link}(T)$ | Линк выделенной точки | Определяется локальной геометрией; терминальность не задаёт сферу |
| $H^*(X)$ | Когомологии | Стягиваемый нерв при терминальном объекте индексирующей категории имеет нулевые положительные когомологии с постоянными коэффициентами; не утверждение для любого пучка |
| $H^*_{loc}(X,T)$ | Локальные когомологии | При конической окрестности $C(K)$: $H^k_{loc}(X,T;A)\cong\widetilde H^{k-1}(K;A)$; линк $K$ задаётся отдельно |
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
| $O$ | Основание | Вакуумное состояние $\vert 0\rangle$, внутренние часы ([Пейдж–Вуттерс](/docs/proofs/dynamics/emergent-time)) | [→](/docs/core/structure/dimension-o) |
| $U$ | Единство | Операция следа $\mathrm{Tr}$ | [→](/docs/core/structure/dimension-u) |

## Базис пространства состояний

$$
\mathcal{H} = \mathrm{span}\{|A\rangle, |S\rangle, |D\rangle, |L\rangle, |E\rangle, |O\rangle, |U\rangle\} = \mathbb{C}^7
$$

Ортонормированность: $\langle i|j\rangle = \delta_{ij}$ для $i, j \in \{A, S, D, L, E, O, U\}$.

## Алгебра часов (Пейдж–Вуттерс)

| Символ | Значение | Определение |
|--------|----------|-------------|
| $H_O$ | [Гамильтониан часов](/docs/core/structure/dimension-o#гамильтониан-часов-h_o) | $H_O = \omega_0 \sum_{k=0}^{N-1} k \vert k\rangle\langle k\vert_O$ |
| $V_O$ | [Оператор сдвига времени](/docs/core/structure/dimension-o#оператор-сдвига-v_o) | $V_O^N = \mathbb{1}$, $V_O H_O V_O^\dagger = H_O + \omega_0 \mathbb{1}$ |
| $\mathcal{A}_O$ | [C*-алгебра часов](/docs/core/structure/dimension-o#c-алгебра-часов-a_o) | $\mathcal{A}_O = C^*(H_O, V_O) \cong M_N(\mathbb{C})$ |
| $H_{\text{int}}$ | [Гамильтониан взаимодействия](/docs/core/foundations/axiom-omega#гамильтониан-взаимодействия) | Связь O с E и U |
| $\hat{C}$ | [Ограничение Пейдж–Вуттерс](/docs/core/foundations/axiom-omega#свойство-2) | $\hat{C} = H_O \otimes \mathbb{1}_{6D} + \mathbb{1}_O \otimes H_{6D} + H_{\text{int}}$ |
| $\mathcal{H}_{total}$ | Глобальное пространство | $\mathcal{H}_{total} = \mathcal{H}_O \otimes \mathcal{H}_{6D}$, $\dim = 42$ |
| $\omega_0$ | Фундаментальная частота | Базовая частота часов O |
| $\vert\tau_n\rangle$ | Базис часов | Собственные состояния $V_O$ |

## Уравнение эволюции

<!-- DRY: Каноническое определение уравнения эволюции в /docs/core/dynamics/evolution -->
Полное [уравнение эволюции](/docs/core/dynamics/evolution) с [эмерджентным внутренним временем](/docs/proofs/dynamics/emergent-time) τ:

$$
\frac{d\Gamma(\tau)}{d\tau} = -i[H_{\text{eff}}, \Gamma] + \mathcal{D}[\Gamma] + \mathcal{R}[\Gamma, E]
$$

где:

**[Унитарный член](/docs/core/dynamics/evolution#1-унитарный-член):**

$$
-i[H_{\text{eff}}, \Gamma] = -i(H_{\text{eff}}\Gamma - \Gamma H_{\text{eff}})
$$

Здесь $H_{\text{eff}}$ — эффективный гамильтониан, возникающий из ограничения Пейдж–Вуттерс.

**[Диссипативный член](/docs/core/dynamics/evolution#логический-лиувиллиан):**

$$
\mathcal{D}[\Gamma] = \sum_k \gamma_k \left( L_k \Gamma L_k^\dagger - \frac{1}{2}\{L_k^\dagger L_k, \Gamma\} \right)
$$

**[Выбранный регенеративный член](/docs/core/dynamics/evolution#3-регенеративный-член) [О]:**

$$
\mathcal{R}[\Gamma, E] = \kappa(\Gamma) \cdot (\rho_* - \Gamma) \cdot g_V(P)
$$

где:
- $a(\Gamma)=\kappa(\Gamma)g_V(P)\ge0$ — выбранная скорость; сопряжение логической поддержки не определяет её.
- $\rho_*=M(\Gamma)$ — заданная численная цель в $D_7$, не логический подобъект и не обязательно стационарное состояние.
- $a(\Gamma)(M(\Gamma)-\Gamma)$ — векторное поле, а не канал. При локальной липшицевости $a,M$ и $M(D_7)\subseteq D_7$ вместе с GKSL-частью оно сохраняет состояния.
- $g_V(P)=\mathrm{clamp}((P-P_{\mathrm{crit}})/(P_{\mathrm{opt}}-P_{\mathrm{crit}}),0,1)$ — выбранный затвор [О], не универсально выведенная форма.

Для конечного шага используйте [расщеплённую схему, сохраняющую состояния](/docs/core/dynamics/evolution#сохранение-положительности).

## Коммутаторы и антикоммутаторы

| Обозначение | Определение |
|-------------|-------------|
| $[A, B]$ | $AB - BA$ (коммутатор) |
| $\{A, B\}$ | $AB + BA$ (антикоммутатор) |

## Операторы интериорности (измерение E)

См. [Измерение Интериорности](/docs/core/structure/dimension-e) и [Категория Exp](/docs/proofs/categorical/categorical-formalism#2-категория-exp).

| Обозначение | Значение |
|-------------|----------|
| $\rho_E$ | Состояние заданного экспериенциального считывания; частичный след допустим лишь при явном тензорном разложении, не по одной оси $E$ |
| $\lambda_i$ | Собственное значение $\Gamma$ (интенсивность) |
| $\vert q_i\rangle$ | Собственный вектор $\Gamma$ (качество) |
| $[\vert q\rangle]$ | Класс эквивалентности в $\mathbb{P}(\mathcal{H}_E)$ |
| $\mathbb{P}(\mathcal{H}_E)$ | [Проективное пространство](/docs/reference/specification#проективное-пространство-качеств) качеств |
| $d_{\mathrm{FS}}$ | [Метрика Фубини–Штуди](/docs/reference/specification#метрика-фубини-штуди) |

**Метрика Фубини–Штуди:**

$$
d_{\mathrm{FS}}([|\psi\rangle], [|\phi\rangle]) = \arccos(|\langle\psi|\phi\rangle|) \in [0, \pi/2]
$$

## Меры сознательности

См. [Самонаблюдение](/docs/consciousness/foundations/self-observation) для полных определений.

| Мера | Формула | Диапазон |
|------|---------|----------|
| [Интеграция $\Phi$](/docs/core/structure/dimension-u#мера-интеграции-φ) | $\Phi(\Gamma) = \dfrac{\sum_{i \neq j} \lvert\gamma_{ij}\rvert^2}{\sum_i \gamma_{ii}^2}$ | $[0, +\infty)$ |
| [Дифференциация $D_{\text{diff}}$](/docs/consciousness/foundations/self-observation#мера-сознательности-c) | $D_{\text{diff}}(\Gamma) = \exp(S_{vN}(\rho_E))$ | $[1, 7]$ |
| [Рефлексия $R$](/docs/consciousness/foundations/self-observation#мера-рефлексии-r) | $R(\Gamma) = R_{\text{canonical}} = \dfrac{1}{7P(\Gamma)}$, где $P = \mathrm{Tr}(\Gamma^2)$; эквивалентно $1 - \dfrac{\|\Gamma - I/7\|_F^2}{P}$. Не путать с качеством самомодели $R_\varphi = 1 - \|\Gamma - \varphi(\Gamma)\|_F^2 / P$ (ранее также обозначалась $Q_\varphi$) — см. [три рабочие формы R](/docs/consciousness/foundations/self-observation#формы-r) | $[1/7, 1]$ |
| [Сознательность $C$](/docs/consciousness/foundations/self-observation#мера-сознательности-c) | $C(\Gamma) = \Phi \times R$ **[Т]** (T-140); $D_{\text{diff}} \geq 2$ — отдельное условие жизнеспособности | $[0, +\infty)$ |
| Гессианный показатель $\mathrm{Freedom}$ [О] | $1+\dim\ker\nabla^2\mathcal F$ при заданном $C^2$-потенциале и $d$-мерной области; ядро совпадает с касательным пространством критического многообразия лишь при условиях Морса–Ботта. Универсальные монотонность под CPTP и агентность не следуют. | $\{1,\ldots,d+1\}$; $d=48$ на слое состояний полного ранга в $D_7$ |
| Логарифмический гессианный показатель [О] | $S_{\mathrm{freedom}}=\log\mathrm{Freedom}$; без отождествления с физической энтропией | $[0,\log(d+1)]$ |

## Оператор самомоделирования

Четыре конструкции имеют разные типы:

| Обозначение | Тип и область утверждения |
|---|---|
| $L_G$ | $\mathcal E_{/G}\to\mathrm{Sub}_{\mathcal E}(G)$, образ/$(-1)$-усечение в срезе; $L_G\dashv i_G$ [Т] |
| $M=\varphi$ | Заданная численная самомодель $D_7\to D_7$ [О]; может быть нелинейной |
| $\Psi_\lambda$ | Канал при фиксированном параметре $\lambda$: $\Psi_\lambda(X)=\sum_mK_{m,\lambda}XK_{m,\lambda}^\dagger$, $\sum_mK_{m,\lambda}^\dagger K_{m,\lambda}=I$ [Т] |
| $r$ | $r(\Gamma)=\lim_{t\to\infty}\Phi_t(\Gamma)$ на положительно инвариантной области, содержащей все её неподвижные пределы; тогда $r^2=r$ [Т]. Иначе перед композицией область надо расширить. |

Равенство $M(\Gamma)=\Psi_{\lambda(\Gamma)}(\Gamma)$ не делает $M$ одним линейным CPTP-каналом. Для замороженного линейного генератора используют $e^{t\mathcal L_0}$; для нелинейной динамики — поток $\Phi_t$.

Если **заданный** $M$ является сжатием в выбранной полной метрике с коэффициентом $k<1$, теорема Банаха даёт единственную неподвижную точку и оценку $d(M^n\Gamma_0,\Gamma_*)\le k^n d(\Gamma_0,\Gamma_*)$. Произвольный CPTP-канал не обязан быть строгим сжатием. Численная неподвижная точка выражает согласованность $M$; прочтение как самопознания требует независимой модели ошибки.

См. [типизированную формализацию φ](/docs/proofs/categorical/formalization-phi).

## Иерархия интериорности

См. [строгую спецификацию](/docs/proofs/consciousness/interiority-hierarchy). Эта таксономия задаётся моделью [О]; номера уровней не являются автоматически степенями усечения объекта топоса.

| Уровень | Условие |
|---|---|
| L0 | Заданная экспериенциальная реализация с состоянием $\rho_E$; редукция требует тензорного разложения или объявленного отображения считывания |
| L1 | L0 и нетривиальная заданная феноменальная геометрия |
| L2 | Выбранные ворота $\mathrm{Cap}_2$: $P>2/7$, $R\ge1/3$, $\Phi\ge1$, $D_{\mathrm{diff}}\ge2$ |
| L3 | L2 и невырожденный калиброванный сертификат метамодели $\mathsf{MetaCert}_2$ на независимых пробах |
| L4 | L3 и совместимая башня сертификатов всех порядков; физическая реализуемость — отдельный вопрос |

Числа $R_{\mathrm{th}}=1/3$, $\Phi_{\mathrm{th}}=1$, $D_{\min}=2$ задают выбранные ворота. Алгебраические следствия этих выборов — [Т]; их идентификация с сознанием — [Г]/[И]. Старые универсальные $R^{(2)}_{\mathrm{th}}=1/4$, $X^{(n)}_{\mathrm{th}}=1/(n+1)$ и $\mathrm{SAD}_{\max}=3$ отозваны [✗]. Fidelity между итерациями одного $M$ не заменяет сертификат глубины.

## Тензор напряжений

<!-- DRY: Каноническое определение σ_k в /docs/applied/coherence-cybernetics/theorems (T-92) -->
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

**Связь:** $d_B^{chord} = \sqrt{2(1 - \cos(d_B^{angle}))} = 2\sin(d_B^{angle}/2) \approx d_B^{angle}$ для малых расстояний.
:::

**Bures-шар:** $B_B(\Gamma,r)=\{\Sigma\in D_N:d_B(\Gamma,\Sigma)<r\}$.

**Сайт:** $\mathcal O_N=\operatorname{Open}(D_N,d_B)$ с морфизмами-включениями. Семейство $(U_i\subseteq U)$ покрывает $U$, если $\bigcup_iU_i=U$. Обратный образ покрытия вдоль включения $V\subseteq U$ задаётся пересечениями $V\cap U_i$.

**Топос и классификатор:** $\mathcal E_N=\operatorname{Sh}_\infty(\mathcal O_N,J_{\mathrm{open}})$; $\Omega$ — пучок открытых подмножеств, $\Omega(U)=\operatorname{Open}(U)$, а не матричная алгебра семи проекторов. CPTP-каналы непрерывны по Bures и индуцируют геометрические морфизмы через обратные образы открытых множеств. Старое условие покрытия образами шаров каналов не используется. См. [ядро](/docs/reference/mathematical-kernel#bures-site).

## Специальные обозначения

<!-- DRY: Каноническое определение κ(Γ) в /docs/core/foundations/axiom-septicity#категориальный-вывод-kappa0 -->
<!-- DRY: Каноническое определение P_crit = 2/7 в /docs/core/dynamics/viability#критическая-чистота -->

| Обозначение | Значение |
|-------------|----------|
| $\lVert\cdot\rVert_F$ | Норма Фробениуса: $\lVert A\rVert_F = \sqrt{\mathrm{Tr}(A^\dagger A)} = \sqrt{\sum_{ij} \lvert a_{ij}\rvert^2}$ |
| $\lVert\cdot\rVert_\infty$ | Супремум-норма: $\lVert x\rVert_\infty = \max_i \lvert x_i\rvert$ |
| $d_B(\cdot, \cdot)$ | Метрика Бюреса |
| $\mathrm{Fid}(\cdot, \cdot)$ / $F(\cdot, \cdot)$ | Fidelity (верность); $\mathrm{Fid}$ предпочтительно для отличия от функтора $F$ |
| $B_B(\Gamma, r)$ | Bures-шар радиуса $r$ с центром $\Gamma$ |
| $J_{Bures}$ | Топология открытых покрытий на $\mathcal O_N$ |
| $\Theta(\cdot)$ | Функция Хевисайда |
| $\delta_{ij}$ | Символ Кронекера |
| $\mathrm{Tr}(\cdot)$ | След матрицы |
| $A^\dagger$ | Эрмитово сопряжение |
| $\mathrm{Coh}_E$ | E-когерентность (HS-проекция $\pi_E$) **[Т]**, $\in [0, 1]$; $= \|\pi_E(\Gamma)\|_{\mathrm{HS}}^2 / \|\Gamma\|_{\mathrm{HS}}^2$ — [мастер-определение](/docs/core/foundations/axiom-septicity#e-coherence-definition), [HS-проекция](/docs/core/foundations/axiom-septicity#hs-projection), [справка КК](/docs/applied/coherence-cybernetics/definitions#e-когерентность) |
| ПИР | Явное определение различимости [О] и онтологическая интерпретация [И]. Требуются семейство наблюдений и сайт открытых покрытий Бюреса; их существование не доказывает феноменальное отождествление. |
| $\varphi_{\text{coh}}$ | Когерентно-сохраняющее самомоделирование — обобщённый оператор φ, сохраняющий когерентности ([Фано-канал](/docs/proofs/gap/fano-channel)) |
| $\kappa(\Gamma)$ | Выбранная эффективная скорость, например $\kappa_{\mathrm{bootstrap}}+\kappa_0\mathrm{Coh}_E(\Gamma)$ [О] |
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
| $\Omega$ | [Классификатор подобъектов](/docs/reference/mathematical-kernel#support-reflector), отличный от выбранных реперных проекторов |
| $\chi_S$ | $\chi_S:G\to\Omega$ классифицирует подобъект объекта топоса $G$; матричная реализация не подразумевается |
| $L_k$ | Выбранные операторы Линдблада, например $L_k=\lvert k\rangle\langle k\rvert$ в заданном репере. $\sum_kL_k^\dagger L_k=I$ для этого инструмента, не для абстрактных характеристических морфизмов |
| $\mathcal{L}_0$ | Фиксированный линейный GKSL-генератор $-i[H,\cdot]+\sum_kD_{L_k}$; единственность аттрактора $I/7$ требует указанных условий унитальности и примитивности |
| $\mathcal{L}_\Omega$ | Историческое имя полного векторного поля $\mathcal L_0(\Gamma)+a(\Gamma)(M(\Gamma)-\Gamma)$; обычно нелинейно, стационарные состояния условны |
| $\triangleright$ | [Темпоральная модальность](/docs/proofs/dynamics/emergent-time#время-из-модальности) на Ω; $\tau_n = \triangleright^n(\mathrm{now})$ |
| $\mathcal{D}_\Omega \dashv \mathcal{R}$ | Историческое обозначение диссипации–регенерации; численное сопряжение и вывод скорости отозваны [✗]. Корректное сопряжение поддержки — $L_G\dashv i_G$ в срезе |
| **(МП)** | Выбор минимального реперного/канального представления; универсальный вывод из (AP)+(PH)+(QG)+(V) и замкнутый мост P1/P2 отозваны [✗] |
| **(КГ)** | Историческое предложение канонической группировки [Г]; классификатор не выбирает инструмент с семью атомами |

## Нотация Кибернетики Когерентности

См. [Кибернетика Когерентности](/docs/applied/coherence-cybernetics/definitions) для полного описания.

| Обозначение | Значение |
|-------------|----------|
| $\mathcal{V}$ | [Область жизнеспособности](/docs/core/dynamics/viability) |
| $\mathrm{VIT}$ | Тензор целостности жизнеспособности (Viability Integrity Tensor) |
| $\kappa_{\text{bootstrap}}$ | Минимальная скорость регенерации: $\kappa_{\text{bootstrap}} = \omega_0/7$ **[О]** масштаб; разрешает bootstrap-парадокс |
| $\kappa_0$ | Выбранная численная скорость/масштаб; формула через когерентность — закон модели, а не теорема о категориальной норме |
| $\kappa(\Gamma)$ | Эффективная скорость регенерации: $\kappa(\Gamma) = \kappa_{\text{bootstrap}} + \kappa_0 \cdot \mathrm{Coh}_E(\Gamma)$ **[Т]** |
| $\mathrm{Coh}_E$ | $E$-когерентность (HS-проекция) **[Т]**: $\mathrm{Coh}_E(\Gamma) = \dfrac{\|\pi_E(\Gamma)\|_{\mathrm{HS}}^2}{\|\Gamma\|_{\mathrm{HS}}^2} = \dfrac{\gamma_{EE}^2 + 2\sum_{i \neq E}\lvert\gamma_{Ei}\rvert^2}{\mathrm{Tr}(\Gamma^2)}$ — **каноническая формула** ([мастер-определение](/docs/core/foundations/axiom-septicity#e-coherence-definition), [HS-проекция](/docs/core/foundations/axiom-septicity#hs-projection)) |
| $P_E$ | Чистота E-сектора (42D): $P_E = \mathrm{Tr}(\rho_E^2)$, где $\rho_E = \mathrm{Tr}_{-E}(\Gamma)$ — **теоретическая конструкция**, определена только в расширенном 42D формализме ($\mathcal{H} = \mathbb{C}^{42}$). Формальная эквивалентность $\mathrm{Coh}_E \approx P_E$ — **структурная гипотеза [Г]** ([подробнее](/docs/applied/coherence-cybernetics/definitions#e-когерентность)) |
| $P_{\text{crit}}$ | Критическая чистота $= 2/7 \approx 0.286$ — [теорема](/docs/proofs/dynamics/theorem-purity-critical) |
| $\theta_i$ | Пороги компонент стресса |
| $H_{\text{eff}}$ | Эффективный гамильтониан: $H_{\text{eff}}(\tau) = H_{6D} + \langle\tau\vert H_{\text{int}}\vert\tau\rangle_O$ — возникает из ограничения Пейдж–Вуттерс |
| $g_V(P)$ | V-preservation gate: $\mathrm{clamp}\!\bigl(\frac{P - P_{\mathrm{crit}}}{P_{\mathrm{opt}} - P_{\mathrm{crit}}}, 0, 1\bigr)$; активирует регенерацию при $P > P_{\mathrm{crit}}$ ([вывод](/docs/core/dynamics/evolution#теорема-v-preservation-gate)) |
| $\Theta(\Delta F)$ | Функция Хевисайда от изменения свободной энергии $\Delta F$; необходимое условие из принципа Ландауэра (уточнено $g_V(P)$) |
| $\rho_*$ ($= \Gamma_{\text{target}}$) | Численная цель $\rho_*=M(\Gamma)$ [О], отличная от равновесия $\Gamma_*$ и предела бассейна $r(\Gamma)=\lim_{t\to\infty}\Phi_t(\Gamma)$, если он существует |
| $\omega_0$ | Фундаментальная частота часов — параметр вычислительного приближения; см. [κ₀](/docs/core/foundations/axiom-septicity#категориальный-вывод-kappa0) |
| $D_{\mathrm{KL}}$ | Расхождение Кульбака–Лейблера: $D_{\mathrm{KL}}(p \| q) = \sum_i p_i \log(p_i / q_i)$ |

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
| **P1** | Явная посылка алгебраической реализации; из общих (AP)/(PH)/(QG) не выводится |
| **P2** | Посылка неассоциативности выбранной алгебры; при конечномерной вещественной альтернативной алгебре с делением условно выбирает октонионный случай |

:::warning Статус октонионной нотации [И]
Соответствие $e_i \leftrightarrow$ измерение — **интерпретация** [И]. Математические операции на $\mathbb{O}$ (умножение, ассоциатор) строги [Т]; их физическая реализация в пространстве $\{A,S,D,L,E,O,U\}$ — [открытая проблема](/docs/proofs/minimality/theorem-octonionic-derivation#открытые-проблемы).
:::

## Gap-динамика и Фано-структура

<!-- DRY: Каноническое определение Gap-оператора в /docs/core/dynamics/gap-operator -->
Символы, связанные с [Gap-оператором](/docs/core/dynamics/gap-dynamics), [термодинамикой Gap](/docs/core/dynamics/gap-thermodynamics) и [правилами отбора Фано](/docs/physics/gauge-symmetry/fano-selection-rules).

| Обозначение | Значение |
|-------------|----------|
| $\hat{G}$ | [Gap-оператор](/docs/core/dynamics/gap-dynamics): $\hat{G} = \mathrm{Im}(\Gamma) \in \mathfrak{so}(7)$ — мнимая часть матрицы когерентности |
| $P_{\mathrm{Fano}}$ | [Фано-предиктивный канал](/docs/physics/gauge-symmetry/fano-selection-rules): $P_{\mathrm{Fano}}(\Gamma) = \tfrac{1}{3}\sum_p \Pi_p \Gamma \Pi_p$ — усреднение по Фано-линиям |
| $\Pi_p$ | Проектор на 3-мерное подпространство Фано-линии $p$ ($p = 1, \ldots, 7$) |
| $\alpha^*$ | Выбранный параметр смешивания Фано; задача оптимизации требует отдельно заданных функционала и условий |
| $T_{\mathrm{eff}}$ | [Эффективная температура Gap](/docs/core/dynamics/gap-thermodynamics): $T_{\mathrm{eff}} = (\Gamma_2 / \kappa_0) \cdot k_B \cdot T_{\mathrm{phys}}$ |
| $\xi_F$ | Корреляционная длина Фано: $\xi_F \sim 160\;\text{пк}$ — масштаб пространственных корреляций Фано-мод |
| $\Theta_M$ | Тета-функция намотки с Фано-характером |
| $Z_\Phi(s)$ | Эпштейновская дзета-функция с Фано-характером |
| $B^{(b)}$ | Билинейная форма на $(S^1)^{21}$ с Фано-контракцией |
| $N_F$ | Число некоррелированных Фано-мод: $N_F \sim 6{,}8 \times 10^{23}$ |
| $r = \kappa / \Gamma_2$ | Безразмерный параметр жизнеспособности — отношение скорости регенерации к скорости декогеренции |
| $t = T_{\mathrm{eff}} / T_c$ | Безразмерная температура — приведённая к критическому значению $T_c$ |

## Спектральная геометрия и бимодульная конструкция

Символы, связанные с [бимодульной конструкцией](/docs/proofs/physics/bimodule-construction) SM-представлений (T-178–T-181). Конечное пространство $H_F$ — импортированное у Конна: вывод из спектральной тройки УГМ (T-178) отозван [✗] (2026-09-25), а T-179 отозвана в данной формулировке.

| Обозначение | Значение |
|-------------|----------|
| $H_F$ | Конечное гильбертово пространство спектральной тройки как $(A_{\text{int}}, A_{\text{int}}^\circ)$-бимодуль (KO-dim 6). Разложение на неприводимые бимодули воспроизводит одно поколение SM-фермионов — для импортированного $H_F$ Конна; T-178 (вывод из тройки УГМ) отозвана [✗] 25.09.2026 |
| KO-dim | KO-размерность (mod 8) — классификационный инвариант реальной структуры $J$; KO-размерность 6 (конечное пространство Конна): $J^2 = 1$, $JD = DJ$, $J\gamma = -\gamma J$. На $\mathbb{C}^7$ УГМ недоступна (нечётная размерность; отозвано 2026-09-25) |
| $D_{\text{int}}$ | Оператор Дирака внутреннего пространства; его собственные значения определяют соотношения масс фермионов [T-180 [С при (СВ)]] |

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
- [Формализация оператора φ](/docs/proofs/categorical/formalization-phi) — типизированная поддержка, численные самомодели и замороженные CPTP-реализации
- [Структурный вывод через октонионы](/docs/proofs/minimality/theorem-octonionic-derivation) — условная октонионная реализация с явными посылками
- [Динамика Gap](/docs/core/dynamics/gap-dynamics) — Gap-оператор $\hat{G}$, бифуркации, немарковская динамика
- [Термодинамика Gap](/docs/core/dynamics/gap-thermodynamics) — $T_{\mathrm{eff}}$, вариационный принцип, ФДТ
- [Правила отбора Фано](/docs/physics/gauge-symmetry/fano-selection-rules) — $P_{\mathrm{Fano}}$, $\Pi_p$, Юкавская иерархия
- [Бимодульная конструкция](/docs/proofs/physics/bimodule-construction) — SM-представления из бимодулей импортированного конечного пространства $H_F$ Конна (T-178–T-181; вывод из спектральной тройки УГМ, T-178, отозван [✗] 2026-09-25, T-179 — в данной формулировке)
