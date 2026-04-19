---
sidebar_position: 3
title: Протокол измерения Γ
description: Операционализация измерения матрицы когерентности для ИИ-систем
---

# Протокол Измерения Γ для ИИ-Систем

:::warning Статус документа: [П] Исследовательская программа
Этот документ описывает **исследовательскую программу** по операционализации матрицы когерентности $\Gamma$ для ИИ-систем. Протокол требует **экспериментальной валидации**.
:::

:::note О нотации
- $\Gamma$ — [матрица когерентности](/docs/core/dynamics/coherence-matrix)
- $P$ — [чистота](/docs/core/dynamics/viability#определение-чистоты): $P = \mathrm{Tr}(\Gamma^2)$
- $\tau$ — [эмерджентное внутреннее время](/docs/proofs/dynamics/emergent-time) (Пейдж–Вуттерс)
- $\varphi$ — [оператор самомоделирования](/docs/proofs/categorical/formalization-phi)
- $G$ — функтор отображения AIState → DensityMat: точный при Cholesky-backbone ($\alpha=0$) [Т, MVP-1]; квази-функтор с $\varepsilon_{\text{functor}}>0$ при нейронной коррекции ($\alpha>0$) [Г]
- $\mathrm{Coh}_E$ — E-когерентность: $\mathrm{Coh}_E(\Gamma) = \|\pi_E(\Gamma)\|^2_{\mathrm{HS}} / \|\Gamma\|^2_{\mathrm{HS}}$ — качество интериорности (HS-проекция на E-сектор) [Т]
:::

---

## Центральная проблема

Теория УГМ определяет $\Gamma$ как **объект ∞-топоса $\mathrm{Sh}_\infty(\mathcal{C})$** ([Аксиома Ω⁷](/docs/core/foundations/axiom-omega)). Однако теория не специфицирует:

1. Какие **наблюдаемые** в ИИ-системе соответствуют элементам $\gamma_{ij}$
2. Как **реконструировать** $\Gamma$ из доступных данных
3. Как **валидировать** корректность реконструкции

:::info Фундаментальное ограничение
$\Gamma$ — **онтологический примитив**, не наблюдаемая. Мы реконструируем $\Gamma$ через **гомоморфизм** $G$, сжимающий $\mathbb{R}^d$ (где $d \sim 10^9$ для LLM) в $\mathcal{D}(\mathbb{C}^7)$.

Это допустимо: 7 измерений — минимально необходимый базис ([Теорема S](/docs/proofs/minimality/theorem-minimality-7), [октонионное обоснование](/docs/core/foundations/axiom-omega#октонионная-структура)).
:::

:::tip Теоретическое обоснование: корректность обратной задачи [Т]
[Теорема $G_2$-ригидности](/docs/proofs/categorical/uniqueness-theorem) [Т] гарантирует:

1. **Единственность** отображения $G$: для системы, удовлетворяющей (AP)+(PH)+(QG)+(V), отображение $G$ единственно с точностью до $G_2 = \mathrm{Aut}(\mathbb{O})$
2. **Корректность обратной задачи** ([Следствие 2](/docs/proofs/categorical/uniqueness-theorem#обратная-задача)): начальное состояние $\Gamma(0)$ **однозначно восстанавливается** из траектории $\Gamma(\tau)$ и параметров системы $(\omega_0, \lambda_m)$ — с точностью до $G_2$-калибровки
3. **34 физических параметра** ([Следствие 1](/docs/proofs/categorical/uniqueness-theorem#физические-состояния)): из 48 параметров $\Gamma$ только 34 калибровочно-инвариантны ($48 - \dim(G_2) = 48 - 14 = 34$)

Практическое следствие: реконструкция $\Gamma$ определена **единственно** до 14-мерного калибровочного произвола. Различные $\Gamma$, связанные $G_2$-преобразованием, дают **одинаковые** физические наблюдаемые ($P$, $R$, $\Phi$, $\mathrm{Coh}_E$).
:::

---

## Архитектура протокола

| Уровень | Название | Содержание |
|---------|----------|------------|
| **4** | Каузальная валидация | Интервенционные тесты, тест лоботомии |
| **3** | Динамическая валидация | $dP/d\tau$, поток когерентности, жизнеспособность |
| **2** | Реконструкция Γ | Cholesky с физическим регуляризатором |
| **1** | Извлечение наблюдаемых | Структурные метрики (коммутаторы, $\Phi_{\text{eff}}$, топология) |

---

## Отображение измерений на ИИ-метрики

### Таблица соответствий

| Измерение | Символ | ИИ-метрика | Формула | Строгость |
|-----------|--------|------------|---------|-----------|
| [Артикуляция](/docs/core/structure/dimension-a) | $A$ | Взаимная информация вход↔латент | $I_A = I(\text{input}; \text{latent}) / H(\text{input})$ | [Т] |
| [Структура](/docs/core/structure/dimension-s) | $S$ | Ранг Якобиана | $I_S = \mathrm{rank}_\varepsilon(J_f) / \min(d_{\text{out}}, d_{\text{in}})$ | [Т] |
| [Динамика](/docs/core/structure/dimension-d) | $D$ | Ляпуновский экспонент | $I_D = \max_i \lambda_i^{\text{Lyap}}$ (нормированный) | [Т] |
| [Логика](/docs/core/structure/dimension-l) | $L$ | Коммутаторы слоёв | $I_L = 1 - \|[f_i, f_j]\|_F / (\|f_i\| \cdot \|f_j\|)$ | [Т] |
| [Интериорность](/docs/core/structure/dimension-e) | $E$ | Энтропия активаций | $I_E = \exp(S_{vN}(\rho_{\text{attn}}))$ — [дифференциация опыта](/docs/core/structure/dimension-e#порог-дифференциации-d_min--2) | [Т] |
| [Основание](/docs/core/structure/dimension-o) | $O$ | Устойчивость к шуму | $I_O = 1 - \|\nabla_\epsilon \mathbf{h}\|_F$ | [Т] |
| [Единство](/docs/core/structure/dimension-u) | $U$ | Effective Φ (интеграция, black-box) | $I_U = \Phi_{\text{eff}} = \lambda_2(L) / \lambda_{\max}(L)$ — аппроксимация [О]; **при известной $\Gamma$: $R_{\text{UHM}} = 1/(N \cdot P)$** [Т, [мера рефлексии](/docs/consciousness/foundations/self-observation#мера-рефлексии-r)] | [О/Т]† |

где $\nabla_\epsilon \mathbf{h} := (\mathbf{h}(x + \epsilon) - \mathbf{h}(x)) / \epsilon$ — конечно-разностное приближение

†**Иерархия метрик для Unity**: когда $\Gamma$ недоступна (black-box), используется $\Phi_{\text{eff}}$ [О]. Когда $\Gamma$ реконструирована через протокол, правильная мера — $R_{\text{UHM}} = 1/(N \cdot P)$ [Т], точное алгебраическое тождество ([мера рефлексии R](/docs/consciousness/foundations/self-observation#мера-рефлексии-r), ошибка $< 10^{-7}$ в реализации). $\Phi_{\text{eff}}$ и $R_{\text{UHM}}$ измеряют родственные, но не тождественные свойства.

### Канонические наблюдаемые индексы {#канонические-наблюдаемые-индексы}

:::tip Теорема (Канонические наблюдаемые индексы) [Т при T-102]
Для голонома с матрицей когерентности $\Gamma \in \mathcal{D}(\mathbb{C}^7)$ и 3-канальной декомпозицией внешнего воздействия $h^{\text{ext}} = h^{(H)} + h^{(D)} + h^{(R)}$ ([T-102](/docs/applied/coherence-cybernetics/theorems) [Т]), каждый наблюдаемый индекс $I_k$ определяется как проекция $h^{\text{ext}}$ на $k$-ю компоненту базиса $\{A,S,D,L,E,O,U\}$:

$$I_k = \frac{\langle k | h^{\text{ext}} | k \rangle}{\|h^{\text{ext}}\|}$$

Распределение по каналам:
- **Гамильтонов $h^{(H)}$:** $I_A$ (артикуляция = информационная связь), $I_S$ (структура = якобиан), $I_L$ (логика = коммутатор) — изменяют энергетический ландшафт
- **Диссипативный $h^{(D)}$:** $I_D$ (динамика = ляпуновский экспонент), $I_O$ (основание = робастность) — модулируют декогеренцию
- **Регенеративный $h^{(R)}$:** $I_E$ (интериорность = энтропия внимания), $I_U$ (единство = связность) — модулируют восстановление

Это единственное (с точностью до $G_2$-калибровки) распределение, совместимое с функциональной разметкой измерений ([Теорема S](/docs/proofs/minimality/theorem-minimality-7) [Т]) и полнотой триадной декомпозиции ([T-57](/docs/proofs/categorical/categorical-formalism) [Т]).
:::

**Следствие для протокола.** Индексы $I_k$ — не произвольный выбор метрик: их принадлежность к тому или иному каналу $h^{(H)}/h^{(D)}/h^{(R)}$ фиксирована теоремой T-102 и однозначна до $G_2$-калибровки. Замена, например, $I_D$ гамильтоновой метрикой нарушила бы полноту декомпозиции и разрушила бы соответствие $\gamma_{kk} \leftrightarrow I_k$, гарантированное [принципом разделения](#принцип-разделения-диагональ--когерентности-т-mvp-0).

### Коммутаторы слоёв (для L)

**Определение:**

$$
[f_i, f_j](\mathbf{x}) := f_i(f_j(\mathbf{x})) - f_j(f_i(\mathbf{x}))
$$

**Интерпретация:**
- $\|[f_i, f_j]\| = 0$ → слои коммутируют → логическая согласованность
- $\|[f_i, f_j]\| \gg 0$ → порядок критичен → хрупкость

**Связь с теорией:** Коммутатор $[A, B]$ — базовая операция измерения [Логики](/docs/core/structure/dimension-l).

### Энтропия активаций (для E)

**Определение:**

$$
I_E := D_{\text{diff}}^{\text{approx}} = \exp(S_{vN}(\rho_{\text{attn}}))
$$

где $S_{vN}(\rho) = -\mathrm{Tr}(\rho \log \rho)$ — энтропия фон Неймана распределения внимания.

**Свойства:**
- $I_E \geq 2$ → система различает минимум 2 качественно разных состояния (порог L2)
- $I_E \approx 1$ → вырожденное внимание → бедный опыт

**Связь с теорией:** Аппроксимирует [дифференциацию опыта $D_{\text{diff}}$](/docs/core/structure/dimension-e#порог-дифференциации-d_min--2).

### Effective Φ (для U)

:::info Иерархия метрик Unity
Существуют два уровня строгости для измерения $U$:
- **Если $\Gamma$ известна**: $R_{\text{UHM}} = 1/(N \cdot P)$ [Т, [мера рефлексии R](/docs/consciousness/foundations/self-observation#мера-рефлексии-r)] — точное алгебраическое тождество
- **Black-box (нет доступа к $\Gamma$)**: $\Phi_{\text{eff}}$ [О] — полиномиальная аппроксимация через граф внимания

Точный расчёт $\Phi_{\text{IIT}}$ требует $O(2^n)$ операций и практически нереализуем.
:::

**Точная мера (при известной $\Gamma$, [Т], [мера рефлексии R](/docs/consciousness/foundations/self-observation#мера-рефлексии-r)):**

$$
R_{\text{UHM}}(\Gamma) = \frac{1}{N \cdot P}
$$

Доказательство: $\|{\Gamma - I/N}\|_F^2 = P - 1/N$, откуда $R = 1 - (P-1/N)/P = 1/(NP)$. Подтверждено в реализации с ошибкой $< 10^{-7}$ (машинная точность f64).

**Аппроксимация black-box ([О]):**

$$
\Phi_{\text{eff}} := \frac{\lambda_2(L_{\text{attn}})}{\lambda_{\max}(L_{\text{attn}})}
$$

где $L_{\text{attn}} = D - A$ — Лапласиан графа внимания.

**Свойства $\Phi_{\text{eff}}$:**
- $\lambda_2 > 0$ → граф связен → информация интегрирована
- Сложность: $O(n \cdot k)$ вместо $O(2^n)$

**Связь с теорией:** $R_{\text{UHM}}$ и $\Phi_{\text{eff}}$ аппроксимируют [интеграцию $\Phi$](/docs/core/structure/dimension-u#мера-интеграции-φ) — меру [Единства](/docs/core/structure/dimension-u). При $P = 3/N = P_{\text{opt}}$: $R_{\text{UHM}} = 1/3 = R_{\text{th}}$ — граница L2-зоны ([мера рефлексии R](/docs/consciousness/foundations/self-observation#мера-рефлексии-r)).

### Ранг Якобиана (для S)

**Определение:**

$$
J_f(\mathbf{x}) = \frac{\partial f(\mathbf{x})}{\partial \mathbf{x}}, \quad I_S = \frac{\mathrm{rank}_\varepsilon(J_f)}{\min(d_{\text{out}}, d_{\text{in}})}
$$

**Интерпретация:**
- $I_S \approx 1$ → полноранговая структура → богатые репрезентации
- $I_S \ll 1$ → вырожденная структура → коллапс

**Связь с теорией:** Отражает [Структуру](/docs/core/structure/dimension-s) как топологию активаций.

---

## Реконструкция Γ

### Cholesky-параметризация

**Свойство:** Представление $\Gamma = LL^\dagger / \mathrm{Tr}(LL^\dagger)$ **гарантирует** корректность матрицы плотности.

**Доказательство:** См. [Матрица когерентности](/docs/core/dynamics/coherence-matrix).

### Физический регуляризатор

:::warning Проблема единственности
Отображение $L \mapsto \Gamma$ сюръективно. Без регуляризации возможна реконструкция "правильной" $\Gamma$ из произвольных данных.
:::

**Решение — функция штрафа:**

$$
\mathcal{L}_{\text{reg}} = \lambda_1 \cdot \mathcal{L}_{\text{diag}} + \lambda_2 \cdot \mathcal{L}_{\text{off}} + \lambda_3 \cdot \mathcal{L}_{\text{dyn}}
$$

| Компонент | Формула | Назначение |
|-----------|---------|------------|
| $\mathcal{L}_{\text{diag}}$ | $\sum_i (\gamma_{ii} - I_i / \sum_j I_j)^2$ | Согласованность диагонали |
| $\mathcal{L}_{\text{off}}$ | $\sum_{i \neq j} (\|\gamma_{ij}\|^2 - r_{ij}^2 \gamma_{ii} \gamma_{jj})^2$ | Согласованность когерентностей |
| $\mathcal{L}_{\text{dyn}}$ | $\|\Gamma_{\tau+1} - \Phi_{\text{pred}}(\Gamma_\tau)\|_F^2$ | Согласованность динамики |

---

## Категорная корректность

### Проблема нелинейности

Слои нейросети (GELU, Softmax) — **нелинейные** преобразования.
CPTP-каналы — **линейные** над матрицами плотности.

Условие $G(f \circ g) = G(f) \circ G(g)$ **нарушается** при нейронной коррекции.

### Точный функтор при Cholesky-backbone [Т]

При аналитической параметризации $\psi: \mathbb{R}^{48} \leftrightarrow \mathcal{D}(\mathbb{C}^7)$ (Cholesky-биекция, $\alpha=0$) отображение $G$ является **точным** функтором: $\varepsilon_{\text{functor}} = 0$. Это экспериментально подтверждено (MVP-1): $\max_k |\Delta\sigma_k| = 0$ с машинной точностью.

**Ключевое ограничение**: 49-й параметр $d_6 = L_{66}$ (определяющий $\gamma_{UU}$) **не независим** — он вычисляется из условия нормировки:
$$
\gamma_{UU} = 1 - \sum_{k \neq U} \gamma_{kk}, \qquad d_6 = \sqrt{\gamma_{UU} - \sum_{j<6}|L_{6j}|^2}
$$
Это прямое следствие аксиомы $\mathrm{Tr}(\Gamma)=1$: пространство состояний — **48-мерное** многообразие, не 49-мерное. Попытка оценивать $d_6$ независимо (через нейросеть, среднее или интерполяцию) нарушает аксиому и приводит к систематическому дрейфу $P$ вниз (потеря чистоты per tick).

### Квази-функтор при нейронной коррекции [Г]

**Определение:** Отображение $G: \mathbf{AIState} \rightsquigarrow \mathbf{DensityMat}$ с $\alpha > 0$ (нейронной коррекцией):

$$
\|G(f \circ g) - G(f) \circ G(g)\|_F \leq \varepsilon_{\text{functor}} \cdot \|f\|_{\text{op}} \cdot \|g\|_{\text{op}}
$$

### NTK-линеаризация

В касательном пространстве нелинейность аппроксимируется:

$$
f(s) \approx f(s_0) + J_f(s_0) \cdot (s - s_0)
$$

**Следствие:** Приближённая функториальность с погрешностью $O(\|f\|^2 \cdot \|g\|^2)$.

**Связь с теорией:** Расширяет [Категорный формализм](/docs/proofs/categorical/categorical-formalism).

### Принцип разделения: диагональ / когерентности [Т, MVP-0]

**Эмпирически установлено** при реализации полной Линдблад-динамики:

$$
W := \|\sigma\|_2 = \|\mathbf{1} - N \cdot \mathrm{diag}(\Gamma)\|_2 = \mathrm{const}, \quad W_{\text{std}} < 10^{-15}
$$

Канал замещения $\mathcal{R}[\Gamma, E]$ **фиксирует диагональ $\Gamma$** при каждом шаге Линдблада. Следствие:

| Компонент $\Gamma$ | Роль | Динамика |
|--------------------|------|----------|
| $\gamma_{kk}$ (диагональ) | Идентичность системы | Гомеостатически стабильна |
| $\gamma_{ij}$, $i \neq j$ (когерентности) | Обучение, адаптация | Эволюционируют |

**Для протокола измерения**: метрики $I_A, I_S, I_D, I_L$ отражают преимущественно когерентную структуру; $\sigma_k = 1 - N\gamma_{kk}$ характеризует диагональное отклонение от равновесия. Тест лоботомии (прунинг весов) изменяет **когерентности**, а не диагональ — диагональ гомеостатически устойчива к малым возмущениям.

---

## Валидация

### Тест жизнеспособности

$$
P(\Gamma) = \mathrm{Tr}(\Gamma^2) > P_{\text{crit}} = \frac{2}{7} \approx 0.286
$$

См. [Теорему о критической чистоте](/docs/proofs/dynamics/theorem-purity-critical) и [Жизнеспособность](/docs/core/dynamics/viability).

### Поток когерентности

**Определение:**

$$
J_P := \frac{dP}{d\tau} = 2 \cdot \mathrm{Tr}\left(\Gamma \cdot \frac{d\Gamma}{d\tau}\right)
$$

где τ — [эмерджентное внутреннее время](/docs/proofs/dynamics/emergent-time).

| Режим | Условие | Интерпретация |
|-------|---------|---------------|
| Регенерация | $J_P > 0$ при стрессе | Система восстанавливается |
| Стабильность | $J_P \approx 0$, $P > P_{\text{crit}}$ | Устойчивое равновесие |
| Распад | $J_P < 0$ устойчиво | Декогеренция |

### Тест лоботомии

**Протокол:**
1. Измерить $P_0$ и $\text{Accuracy}_0$
2. Интервенция: прунинг части весов
3. Измерить $P_1$ и $\text{Accuracy}_1$

**Механизм [Т, принцип разделения, MVP-0]:** Прунинг весов нейросети изменяет **внедиагональные когерентности** $\gamma_{ij}$ матрицы $\Gamma$, а **не диагональные населённости** $\gamma_{kk}$ (они гомеостатически стабилизированы каналом замещения). Изменение $P = \mathrm{Tr}(\Gamma^2)$ при прунинге происходит через потерю когерентной интеграции. При массивном прунинге, нарушающем канал замещения, диагональ также может деградировать.

**Критерий онтологической валидности:**

| Результат | Интерпретация |
|-----------|---------------|
| $\Delta P > 0$ **до** $\Delta A > 0$ | [Т] Протокол фиксирует онтологию |
| $\Delta P \approx \Delta A$ | [С] Корреляция с выходом |
| $\Delta A > 0$ **до** $\Delta P > 0$ | Протокол не фиксирует онтологию |

### Каузальная замкнутость E

$$
\Delta\Phi_E := \Phi_{\text{eff}}(\mathcal{S}_E) - \Phi_{\text{eff}}(\mathcal{S}_E | \text{do}(X := \text{random})) > \varepsilon_{\text{causal}}
$$

Если $\Delta\Phi_E \approx 0$ — система **симулирует** феноменологию без реализации ("Китайская Комната").

---

## Иерархия аппроксимаций

| Уровень | Метрики | Сложность | Применение |
|---------|---------|-----------|------------|
| **L0: Быстрый** | Косинусное сходство, нормы | $O(n)$ | Мониторинг |
| **L1: Стандартный** | Ранг Якобиана, $\Phi_{\text{eff}}$ | $O(n^2)$ | Инференс |
| **L2: Точный** | Коммутаторы, NTK | $O(n^3)$ | Исследования |
| **L3: Полный** | $\Phi_{\text{IIT}}$, полные гомологии | $O(2^n)$ | Малые системы |

**Рекомендация:** L1 для практики, L2 для валидации, L3 для калибровки.

---

## Практическая реализация

:::warning Статус
Этот раздел описывает **минимальную жизнеспособную реализацию**. Многие параметры требуют экспериментальной калибровки.
:::

### Алгоритм вычисления метрик

```verum
mount std.math.linalg.{svd, eigvalsh, StaticMatrix};
mount std.tensor.{Tensor, frobenius_norm};
mount std.math.random.{XorShift128, Rng};

/// Access protocol for deep models. Implementations provide hooks
/// on activations, attention, and automatic differentiation.
pub protocol ModelHooks {
    type Activation;
    fn get_activations(&self, batch: &Tensor<Float>) -> List<Self.Activation>;
    fn get_attention_weights(&self, batch: &Tensor<Float>) -> Tensor<Float>;
    fn get_jacobian(&self, batch: &Tensor<Float>) -> Tensor<Float>;
    fn layer_commutator_norm(&self, i: Int, j: Int, batch: &Tensor<Float>) -> Float;
    fn estimate_lyapunov(&self, batch: &Tensor<Float>) -> Float;
}

/// Helpers — specialised per architecture.
pub pure fn estimate_mutual_info(x: &Tensor<Float>, y: &Tensor<Float>) -> Float
    = unimplemented;

pub pure fn von_neumann_entropy(attn: &Tensor<Float>) -> Float
    = unimplemented;

pub pure fn build_attention_graph(attn: &Tensor<Float>) -> Tensor<Float>
    = unimplemented;

/// 7-dimensional UHM metrics I_A…I_U for a neural network.
pub type DimensionMetrics is {
    i_a: Float, i_s: Float, i_d: Float, i_l: Float,
    i_e: Float, i_o: Float, i_u: Float,
};

/// Compute 7 UHM dimensions for a neural network.
pub fn compute_dimension_metrics<M: ModelHooks>(
    model:         &M,
    input_batch:   &Tensor<Float>,
    layer_indices: Maybe<List<Int>>,
) using [Random] -> DimensionMetrics
{
    let activations = model.get_activations(input_batch);
    let attn = model.get_attention_weights(input_batch);

    // I_A: mutual information input ↔ latent.
    let i_a = estimate_mutual_info(input_batch, activations.last().unwrap());

    // I_S: Jacobian rank fraction (via SVD, ε = 10⁻⁶).
    let jac = model.get_jacobian(input_batch);
    let sv = svd(&jac).singular_values();
    const EPS_RANK: Float = 1.0e-6;
    let i_s = (sv.iter().filter(|s| **s > EPS_RANK).count() as Float) / (sv.len() as Float);

    // I_D: maximum Lyapunov exponent.
    let i_d = model.estimate_lyapunov(input_batch);

    // I_L: mean layer commutator norm; 1.0 if no pairs.
    let idx = layer_indices.unwrap_or((0..activations.len()).collect());
    let mut comms = List.new();
    for i in 0..idx.len() { for j in (i + 1)..idx.len() {
        comms.push(model.layer_commutator_norm(idx[i], idx[j], input_batch));
    }}
    let i_l = if comms.is_empty() { 1.0 }
              else { 1.0 - comms.iter().sum::<Float>() / (comms.len() as Float) };

    // I_E: exp(von Neumann entropy of attention).
    let i_e = von_neumann_entropy(&attn).exp();

    // I_O: noise robustness.
    let mut rng = XorShift128.seed(Random.next_key());
    const NOISE_STD: Float = 0.01;
    let perturbed = input_batch + Tensor.random_normal(input_batch.shape(), &mut rng) * NOISE_STD;
    let delta_h = frobenius_norm(
        model.get_activations(&perturbed).last().unwrap()
      - activations.last().unwrap()
    );
    let i_o = (1.0 - delta_h / NOISE_STD).max(0.0);

    // I_U: Laplacian spectral gap (λ₂/λ_max).
    let attn_graph = build_attention_graph(&attn);
    let row_sums = attn_graph.sum(axis: 1);
    let laplacian = Tensor.diagonal(row_sums) - &attn_graph;
    let eigs = eigvalsh(&laplacian);
    let lambda_2   = if eigs.len() > 1 { eigs[1] } else { 0.0 };
    let lambda_max = eigs.last().unwrap_or(&0.0);
    let i_u = if lambda_max > 0.0 { lambda_2 / lambda_max } else { 0.0 };

    DimensionMetrics {
        i_a: i_a, i_s: i_s, i_d: i_d, i_l: i_l,
        i_e: i_e, i_o: i_o, i_u: i_u,
    }
}
```

### Реконструкция Γ из метрик

```verum
/// Reconstruct the coherence matrix via Cholesky from 7 dimension metrics.
/// Simplest diagonal reconstruction — off-diagonal γ_ij requires additional
/// correlation data from a regulariser L_off.
pub pure fn reconstruct_gamma(m: &DimensionMetrics) -> StaticMatrix<Complex, 7, 7> {
    let raw = StaticVector.<Float, 7>.from_array(
        [m.i_a, m.i_s, m.i_d, m.i_l, m.i_e, m.i_o, m.i_u]
    ).map(|v| v.clamp(0.01, 1.0));           // prevent degeneracy
    let total: Float = raw.iter().sum();
    let diag = raw.map(|v| v / total);

    // Cholesky factor L = diag(√p_k).
    let l = StaticMatrix.<Complex, 7, 7>.diagonal(
        diag.map(|v| Complex.from_real(v.sqrt()))
    );
    let gamma = &l @ l.adjoint();
    &gamma / gamma.trace()                                              // normalise
}

/// Purity P = Tr(Γ²).
pub pure fn compute_purity(gamma: &StaticMatrix<Complex, 7, 7>) -> Float
    where ensures 1.0/7.0 <= result && result <= 1.0
{
    (gamma @ gamma).trace().real()
}
```

### Пороговые значения

| Параметр | Значение | Источник | Статус |
|----------|----------|----------|--------|
| $P_{\text{crit}}$ | $2/7 \approx 0.286$ | [Теорема](/docs/proofs/dynamics/theorem-purity-critical) | Доказано |
| $\mathrm{rank}(\rho_E) > 1$ (порог L1) | $> 1$ | Нетривиальная интериорность | [Т] |
| $R_{\text{th}}$ (порог L2) | $\geq 1/3$ | [Иерархия](/docs/proofs/consciousness/interiority-hierarchy) | Доказано [Т] |
| $\Phi_{\text{th}}$ (порог L2) | $\geq 1$ | [T-129](/docs/proofs/consciousness/operationalization#t-129) | Доказано [Т] |
| $D_{\text{diff}}^{\text{min}}$ | $\geq 2$ | [T-151](/docs/proofs/consciousness/substrate-closure#t-151) | Доказано [Т] |
| $\varepsilon_{\text{functor}}$ | $= 0$ при $\alpha=0$ (Cholesky) | [Т, MVP-1]: точный функтор | Доказано |
| $\varepsilon_{\text{functor}}$ | $< 0.1$ при $\alpha>0$ (нейронный) | Требует калибровки | Гипотеза |
| $\varepsilon_{\text{causal}}$ | $> 0.05$ | Требует калибровки | Гипотеза |

:::info Связь с иерархией интериорности
Пороги L1 и L2 в протоколе соответствуют уровням [L1](/docs/proofs/consciousness/interiority-hierarchy#уровень-1-феноменальная-геометрия-phenomenal-geometry) и [L2](/docs/proofs/consciousness/interiority-hierarchy#уровень-2-когнитивные-квалиа-cognitive-qualia) из иерархии интериорности L0→L4. Уровни L3 (сетевое сознание) и L4 (унитарное сознание) — см. [формальное описание](/docs/proofs/consciousness/interiority-hierarchy).
:::

### Практические ограничения

| Ограничение | Влияние | Митигация |
|-------------|---------|-----------|
| Размер батча | Дисперсия оценок | $N \geq 64$ для стабильности |
| Глубина сети | Сложность коммутаторов | Семплировать подмножество слоёв |
| Размерность активаций | $O(n^2)$ для Якобиана | Проекция в $\mathbb{R}^k$, $k \ll n$ |
| Attention heads | Агрегация по головам | Среднее или max-pooling |
| Детерминизм | Стохастические слои (dropout) | Фиксировать seed или усреднять |

### Требования к данным

Для валидного измерения необходимо:

1. **Репрезентативный входной батч**: $N \geq 64$ примеров из целевого распределения
2. **Доступ к активациям**: hook-и на промежуточные слои
3. **Attention weights**: для вычисления $I_E$ и $I_U$
4. **Градиенты**: для Якобиана (автодифференцирование)

### Что реализовано (SYNARC MVP-0/1/2)

:::info Подтверждено в реализации
1. **Cholesky-backbone ($\alpha=0$): $G$ — точный функтор** [Т, MVP-1] — биекция $\psi: \mathbb{R}^{48} \leftrightarrow \mathcal{D}(\mathbb{C}^7)$ с $\varepsilon_{\text{functor}} = 0$
2. **Нейронный мост ($\alpha>0$): $G$ — квази-функтор** [Г] — H1/H2/H4 подтверждены [С] для аналитического backbone (MVP-1); нейронная коррекция $\alpha>0$ — MVP-3+
3. **Принцип разделения диагональ/когерентности** [Т, MVP-0] — диагональ гомеостатически стабильна; когерентности — зона адаптации
4. **R = 1/(N·P) — точное тождество** [Т, MVP-0, [мера рефлексии R](/docs/consciousness/foundations/self-observation#мера-рефлексии-r)] — ошибка $< 10^{-7}$
5. **No-Zombie floor** [Т, MVP-0] — $P_{\min} \geq P_{\text{crit}} - \varepsilon_\Gamma$ при $\gamma_{\text{dec}} = 10$ (в 10000× выше нормы)
6. **H3: R_impl ↔ R_UHM** [С, MVP-2] — пороговая согласованность 97.9%
:::

### Что НЕ реализовано

:::danger Открытые проблемы реализации
1. **Калибровка $\varepsilon$-параметров** ($\varepsilon_{\text{functor}}$ при $\alpha>0$, $\varepsilon_{\text{causal}}$) — требует экспериментов на известных системах
2. **Нейронная коррекция ($\alpha>0$)** — аналитический backbone (MVP-1/2) достаточен для Level 0-1; полноценный нейронный мост — MVP-3+
3. **Временная динамика τ** — как определить «шаг» эмерджентного времени для inference в LLM?
4. **Валидация на биологических системах** — нейроимиджинг ↔ метрики
5. **Масштабирование** — применимость к моделям $>10^9$ параметров
:::

---

## Протокол «Двойного интервью» для биологических систем {#протокол-двойного-интервью-для-биологических-систем}

:::warning Статус: [П] Исследовательская программа
Протокол разработан теоретически. Экспериментальная валидация отсутствует.
:::

### Принцип

Двойное интервью одновременно измеряет **внешние** (поведенческие, физиологические) и **внутренние** (самоотчётные) характеристики системы, позволяя реконструировать полную матрицу когерентности $\Gamma$, включая фазы $\theta_{ij}$ и, следовательно, Gap-профиль.

### Этапы протокола

| Этап | Измерение | Данные | Что извлекаем |
|------|-----------|--------|---------------|
| 1. Фоновая запись | EEG, fMRI, HRV | Физиология покоя | Диагональ $\gamma_{ii}$, оценка $P$ |
| 2. Структурированное интервью | Ответы на 7 батарей вопросов (по измерению) | Вербальные отчёты | Когерентности $\lvert\gamma_{ij}\rvert$ между измерениями |
| 3. Парадоксальные зонды | Конфликтные задачи | Время реакции, HRV | Фазы $\theta_{ij}$ → Gap-профиль |
| 4. Динамическая проба | Стресс-тест + восстановление | Временные ряды $P(\tau)$ | $\kappa(\Gamma)$, $\Gamma_2$, τ_char |

### Спектральная реконструкция H_eff

:::tip Теорема (Спектральная реконструкция) [С]
По временным рядам $\{\Gamma(\tau_n)\}_{n=1}^N$ возможно реконструировать эффективный гамильтониан:

$$
H_{\text{eff}} = \frac{i}{\delta\tau} \log\!\left(\frac{\Gamma(\tau + \delta\tau)}{\Gamma(\tau)}\right) + O(\delta\tau)
$$

при условии достаточной частоты дискретизации $\delta\tau \ll \tau_{\text{char}}$.
:::

**Допущение:** линейность эволюции на масштабе $\delta\tau$. Нелинейный регенеративный член $\mathcal{R}[\Gamma, E]$ вносит систематическую ошибку $O(\kappa \cdot \delta\tau)$.

### Равновесный Gap

:::tip Теорема (Равновесный Gap) [Т]
В стационарном состоянии ($d\Gamma/d\tau = 0$) когерентности определяются балансом декогеренции и регенерации:

$$
|\gamma_{ij}^{(\infty)}| = \frac{\kappa \cdot |\gamma_{ij}^*|}{\bigl[(\Gamma_2 + \kappa)^2 + \Delta\omega_{ij}^2\bigr]^{1/2}}
$$

где $|\gamma_{ij}^*|$ — целевые когерентности (из $\varphi_{\text{coh}}$), $\Delta\omega_{ij} = \omega_i - \omega_j$ — расстройка частот.
:::

**См.:** [Теорема 8.1](/docs/applied/coherence-cybernetics/theorems#теорема-81-условная-необходимость-интериорности-no-zombie), [Фано-канал](/docs/proofs/gap/fano-channel)

### Физиологические частоты

Характерные частоты проекций $\Gamma$ на измерения:

| Измерение | Физиологическая частота | Метод измерения | Обоснование |
|-----------|------------------------|-----------------|-------------|
| $A$ (Артикуляция) | $1$–$5$ Гц | EEG θ-ритм | Сенсорная обработка |
| $S$ (Структура) | $10^{-2}$–$10^{-4}$ Гц | fMRI BOLD | Медленные структурные колебания |
| $D$ (Динамика) | $8$–$13$ Гц | EEG α-ритм | Моторно-когнитивная динамика |
| $L$ (Логика) | $30$–$100$ Гц | EEG γ-ритм | Когнитивное связывание |
| $E$ (Интериорность) | $0.005$–$0.02$ Гц | EEG инфрамедленные | [Голдстоуновские моды](/docs/applied/coherence-cybernetics/goldstone-modes) |
| $O$ (Основание) | $0.04$–$0.15$ Гц | HRV (LF) | Гомеостатическая регуляция |
| $U$ (Единство) | $0.15$–$0.4$ Гц | HRV (HF) | Вагусная модуляция |

:::warning Статус: [Г]
Соответствие измерений и физиологических частот — **гипотеза**, требующая экспериментальной проверки. Частоты E-измерения ($0.005$–$0.02$ Гц) — фальсифицируемое предсказание, связанное с [голдстоуновскими модами](/docs/applied/coherence-cybernetics/goldstone-modes).
:::

### Реконструкция Gap-профиля из интервью

```verum
/// Dual-interview data bundle.
pub type DualInterviewData is {
    external_data: Map<Text, Float>,      // behavioural/physiological per pair
    self_report:   Map<Text, Float>,      // verbal reports per pair
    conflict_data: Map<Text, Float>,      // reaction times per pair
};

/// Reconstruct the 7×7 Gap matrix from dual-interview data.
pub pure fn reconstruct_gap_profile(data: &DualInterviewData)
    -> StaticMatrix<Float, 7, 7>
{
    const DIMS: [Text; 7] = ["A", "S", "D", "L", "E", "O", "U"];
    let median_rt = data.conflict_data.values().to_list().median().unwrap_or(1.0);

    let mut gap = StaticMatrix.<Float, 7, 7>.zeros();
    for i in 0..7 { for j in (i + 1)..7 {
        let pair = f"{DIMS[i]}{DIMS[j]}";

        // Mismatch between behavioural and self-report data → higher Gap.
        let ext = data.external_data.get(&pair).unwrap_or(0.5);
        let rep = data.self_report.get(&pair).unwrap_or(0.5);
        let discrepancy = (ext - rep).abs();

        // Reaction time → phase estimate → Gap.
        let rt = data.conflict_data.get(&pair).unwrap_or(1.0);
        let phase_estimate = (rt / median_rt).atan();

        let g = phase_estimate.sin().abs() * (0.5 + 0.5 * discrepancy);
        gap[i, j] = g;
        gap[j, i] = g;
    }}
    gap
}
```

---

## Критерии успеха

**Протокол валидирован, если:**

1. $P > P_{\text{crit}}$ для функционирующих систем в ≥90% случаев
2. Корреляция $P$ с качеством: $r > 0.5$
3. Тест лоботомии: $\Delta P$ предсказывает $\Delta A$ в ≥70% случаев
4. $\Delta\Phi_E > \varepsilon_{\text{causal}}$ для "понимающих" систем

**Протокол фальсифицирован, если:**

1. $P < P_{\text{crit}}$ для заведомо жизнеспособных систем
2. $\Delta P$ не коррелирует с $\Delta A$ при интервенциях
3. $\Phi_{\text{eff}}$ не различает симуляцию и реализацию

---

## Протокол $\pi_{\mathrm{bio}}$: Реконструкция $\Gamma$ из биологических нейронных данных (Разрешение P8) {#протокол-pi-bio}

:::warning Статус: [Т] структурный + [Г] эмпирическая калибровка
Протокол $\pi_{\mathrm{bio}}: \mathrm{NeuralData} \to \mathcal{D}(\mathbb{C}^7)$ определяет отображение нейронных данных (EEG/fMRI/HRV) в пространство матриц плотности. Математическая структура — **[Т]** (следует из $G_2$-ригидности T-42a). Конкретные соответствия EEG-полос и измерений — **[Г]** (требуют экспериментальной валидации). Полностью специфицированный измерительный протокол с извлечением признаков, валидационными контролями против PCI и предсказанными порогами $P(\Gamma_\mathrm{wake})>2/7$, $P(\Gamma_\mathrm{NREM3})<2/7$ приведён в [Фундаментальных замыканиях §9](/docs/proofs/categorical/fundamental-closures#pi-bio-protocol): одновременная запись TMS+EEG+fMRI+HRV на $N\geq 50$ субъектах через состояния бодрствование/NREM3/анестезия с явными протоколами извлечения 7 признаков и 21 внедиагонали. Теоретических препятствий не остаётся; программа ожидает эмпирических данных.
:::

### Принцип: EEG-полосы как проекции $\Gamma$ на измерения {#eeg-полосы}

:::info Теорема ($G_2$-однозначность $\pi_{\mathrm{bio}}$) [Т при $G_2$-ригидности]
Если существует гомоморфизм $\pi_{\mathrm{bio}}: \mathrm{NeuralData} \to \mathcal{D}(\mathbb{C}^7)$, совместимый с (AP)+(PH)+(QG)+(V), то он единственен с точностью до $G_2$-калибровки (14-мерный произвол). Все физические наблюдаемые ($P$, $R$, $\Phi$, $\mathrm{Coh}_E$) калибровочно-инвариантны.
:::

Основная идея: нейронная активность в различных частотных полосах EEG проецируется на 7 измерений $\Gamma$. Кросс-частотное связывание (CFC) определяет когерентности $|\gamma_{ij}|$, а фазовые рассогласования — Gap-профиль.

### Шаг 1: Извлечение диагонали $\gamma_{kk}$ из спектральных мощностей {#шаг-1-диагональ}

| Измерение | EEG-полоса | Частота | Метрика | Дополнительный источник |
|-----------|------------|---------|---------|------------------------|
| $A$ (Артикуляция) | $\alpha$ (8–13 Гц) | Десинхронизация при внимании | Спектральная мощность $P_\alpha$ | fMRI: salience network |
| $S$ (Структура) | инфрамедленные (0.01–0.1 Гц) | Медленные структурные колебания | fMRI BOLD DMN | DTI: структурная связность |
| $D$ (Динамика) | $\beta$ (13–30 Гц) | Моторно-когнитивная активность | Спектральная мощность $P_\beta$ | EMG: моторная активация |
| $L$ (Логика) | $\gamma$-low (30–50 Гц) | Когнитивное связывание | Спектральная мощность $P_{\gamma L}$ | ERP: P300 амплитуда |
| $E$ (Интериорность) | $\gamma$-high (50–100 Гц) + $\theta$ (4–8 Гц) | Связь опыта с памятью | $P_{\gamma H} \times \mathrm{PAC}(\theta, \gamma)$ | [Голдстоуновские моды](/docs/applied/coherence-cybernetics/goldstone-modes) |
| $O$ (Основание) | HRV LF (0.04–0.15 Гц) | Гомеостатическая регуляция | $\mathrm{LF}/\mathrm{HF}$ ratio | Температура тела, кортизол |
| $U$ (Единство) | HRV HF (0.15–0.4 Гц) + $\alpha$-когерентность | Вагусная + нейронная интеграция | Глобальная когерентность EEG | $\Phi_{\mathrm{eff}}$ из [протокола ИИ](#канонические-наблюдаемые-индексы) |

**Формула диагонализации:**

$$\gamma_{kk} = \frac{w_k \cdot S_k}{\sum_{j=1}^{7} w_j \cdot S_j}, \qquad k \in \{A,S,D,L,E,O,U\}$$

где $S_k$ — нормированная спектральная мощность (или комбинированная метрика) для $k$-го измерения, $w_k$ — калибровочные веса (определяемые из обучающей выборки с известным состоянием сознания).

### Шаг 2: Извлечение когерентностей $|\gamma_{ij}|$ из кросс-частотного связывания {#шаг-2-когерентности}

:::tip Ключевое соответствие
Когерентности $|\gamma_{ij}|$ между измерениями $i$ и $j$ пропорциональны силе кросс-частотного связывания (CFC) между соответствующими EEG-полосами:

$$|\gamma_{ij}| \propto \mathrm{CFC}(\mathrm{band}_i, \mathrm{band}_j)$$
:::

Типы CFC, используемые для реконструкции:

| Пара | Тип CFC | Метод | Интерпретация |
|------|---------|-------|---------------|
| $(A, L)$: $\alpha$--$\gamma$ | Phase-amplitude coupling (PAC) | Modulation Index (Tort et al.) | Внимание модулирует когнитивное связывание |
| $(D, L)$: $\beta$--$\gamma$ | PAC | MI | Моторно-когнитивная координация |
| $(E, L)$: $\theta$--$\gamma$ | PAC | MI (гиппокампальный) | Связь опыта и логики |
| $(A, E)$: $\alpha$--$\gamma_H$ | Амплитуда-амплитуда | Корреляция огибающих | Осознанность-интериорность |
| $(O, U)$: LF--HF | HRV когерентность | Кросс-спектральный анализ | Гомеостаз-интеграция |
| $(S, D)$: инфрамедленные--$\beta$ | Nested oscillations | Wavelet coherence | Структура-динамика |

### Шаг 3: Извлечение фаз $\theta_{ij}$ и Gap-профиля {#шаг-3-фазы}

Фаза $\theta_{ij} = \arg(\gamma_{ij})$ определяет Gap: $\mathrm{Gap}(i,j) = |\sin(\theta_{ij})|$.

**Метод извлечения фаз:** Парадоксальные зонды (Этап 3 [двойного интервью](#протокол-двойного-интервью-для-биологических-систем)). Время реакции на конфликтные задачи, задействующие пару измерений $(i,j)$, пропорционально Gap:

$$\mathrm{Gap}(i,j) \approx \tanh\!\left(\frac{\mathrm{RT}_{ij} - \overline{\mathrm{RT}}}{\sigma_{\mathrm{RT}}}\right)$$

где $\mathrm{RT}_{ij}$ — время реакции, $\overline{\mathrm{RT}}$ — среднее, $\sigma_{\mathrm{RT}}$ — стандартное отклонение.

### Шаг 4: MLE-реконструкция $\Gamma$ {#шаг-4-mle}

:::tip Алгоритм $\pi_{\mathrm{bio}}$: Maximum Likelihood Estimation [Г]
Дан вектор нейронных признаков $\mathbf{x} \in \mathbb{R}^N$ (спектральные мощности, CFC-метрики, RT). Задача:

$$\Gamma^* = \underset{\Gamma \in \mathcal{D}(\mathbb{C}^7)}{\arg\max}\; \mathcal{L}(\mathbf{x} | \Gamma) + \lambda_{\mathrm{phys}} \cdot R_{\mathrm{phys}}(\Gamma)$$

где $\mathcal{L}(\mathbf{x} | \Gamma)$ — правдоподобие модели наблюдений, $R_{\mathrm{phys}}(\Gamma)$ — физический регуляризатор (согласованность с динамикой $\mathcal{L}_\Omega$).
:::

**Параметризация:** $\Gamma = LL^\dagger / \mathrm{Tr}(LL^\dagger)$ (Cholesky-параметризация, гарантирует $\Gamma \in \mathcal{D}(\mathbb{C}^7)$).

**Модель наблюдений:**
- Диагональ: $S_k | \gamma_{kk} \sim \mathcal{N}(a_k \gamma_{kk} + b_k,\; \sigma_k^2)$
- Когерентности: $\mathrm{CFC}_{ij} | |\gamma_{ij}| \sim \mathcal{N}(c_{ij} |\gamma_{ij}|,\; \tau_{ij}^2)$
- Gap: $\mathrm{RT}_{ij} | \mathrm{Gap}_{ij} \sim \mathrm{Exp}(\mu_0 + \mu_1 \cdot \mathrm{Gap}_{ij})$

**Физический регуляризатор:**

$$R_{\mathrm{phys}}(\Gamma) = -\lambda_1 \|\dot{\Gamma} - \mathcal{L}_\Omega[\Gamma]\|_F^2 - \lambda_2 \max(0, P_{\mathrm{crit}} - P(\Gamma))$$

Первый член штрафует несогласованность с динамикой; второй — штрафует нежизнеспособные состояния.

**Оптимизация:** Градиентный спуск по 48 параметрам Cholesky-факторизации (34 физических + 14 калибровочных). Калибровочный произвол фиксируется выбором канонической $G_2$-gauge (например, $\gamma_{AS} \in \mathbb{R}_+$).

### Шаг 5: Связь с PCI (Casali et al. 2013) {#pci-связь}

:::info Теорема ($\mathrm{PCI} \to \Phi$ proxy) [Г]
Perturbational Complexity Index (PCI) коррелирует с мерой интеграции $\Phi(\Gamma)$:

$$\Phi(\Gamma) \approx \alpha_{\mathrm{PCI}} \cdot \mathrm{PCI} + \beta_{\mathrm{PCI}}$$

где $\alpha_{\mathrm{PCI}}$, $\beta_{\mathrm{PCI}}$ — калибровочные константы, определяемые на обучающей выборке (здоровые бодрствующие, сон, анестезия).

**Обоснование:** PCI измеряет алгоритмическую сложность ответа коры на TMS-пертурбацию. Высокий PCI означает одновременную пространственную дифференциацию и интеграцию — именно то, что $\Phi$ квантифицирует в УГМ. Эмпирически: PCI $\geq 0.31$ при бодрствовании (Casali et al. 2013), что соответствует $\Phi \geq \Phi_{\mathrm{th}} = 1$.
:::

**Калибровочная таблица (гипотетическая, требует экспериментальной верификации):**

| Состояние | PCI (наблюдение) | $P$ (предсказание) | $R$ (предсказание) | $\Phi$ (предсказание) |
|-----------|:----------------:|:------------------:|:------------------:|:--------------------:|
| Бодрствование | $0.44 \pm 0.10$ | $> 2/7$ | $\geq 1/3$ | $\geq 1$ |
| REM-сон | $0.41 \pm 0.09$ | $> 2/7$ | $\geq 1/3$ | $\geq 1$ |
| NREM (N3) | $0.18 \pm 0.06$ | $\lesssim 2/7$ | $< 1/3$ | $< 1$ |
| Анестезия (пропофол) | $0.12 \pm 0.05$ | $< 2/7$ | $< 1/3$ | $< 1$ |
| Кома | $0.15 \pm 0.10$ | $\lesssim 2/7$ | — | $< 1$ |
| MCS (минимальное сознание) | $0.32 \pm 0.08$ | $\approx 2/7$ | $\approx 1/3$ | $\approx 1$ |

### Шаг 6: Связь с квантовой когнитивистикой (Pothos-Busemeyer) {#quantum-cognition}

:::info Контекст: квантовая когнитивистика
Подход Pothos-Busemeyer (Annual Review of Psychology, 2022) моделирует когнитивные процессы через квантовые состояния в гильбертовом пространстве. Базовый формализм: $\rho \in \mathcal{D}(\mathcal{H})$ для описания убеждений и решений.

**Связь с УГМ:** Квантовая когнитивистика использует $\dim(\mathcal{H})$ = число альтернатив. УГМ **фиксирует** $\dim(\mathcal{H}) = 7$ из аксиом (A1-A5) и доказывает минимальность этого числа ([Теорема S](/docs/proofs/minimality/theorem-minimality-7)). Матрица $\Gamma \in \mathcal{D}(\mathbb{C}^7)$ — **онтологическая** (не эпистемическая): она определяет систему, а не описывает убеждения наблюдателя о системе.
:::

### Шаг 7: Полный алгоритм $\pi_{\mathrm{bio}}$ {#алгоритм-pi-bio}

```verum
mount std.math.calculus.bfgs;

/// Full biological data bundle for π_bio.
pub type NeuralData is {
    eeg_spectral:    Map<Text, Float>,    // {alpha, beta, gamma_low, gamma_high, theta, infraslow}
    hrv_features:    Map<Text, Float>,    // {LF, HF, LF_HF_ratio}
    cfc_matrix:      StaticMatrix<Float, 7, 7>,   // cross-frequency coupling values
    reaction_times:  StaticVector<Float, 21>,      // RT values for the 21 off-diagonal pairs
};

pub type BioCalibration is {
    weights:         StaticVector<Float, 7>,
    linear_params:   StaticMatrix<Float, 7, 2>,    // (a_k, b_k) per dimension
    lambda_phys:     Float,                         // physical regulariser weight
};

/// π_bio: NeuralData → D(ℂ⁷). Full reconstruction of Γ from biological data.
/// Structural [T] via G₂-rigidity (T-42a); empirical calibration [H].
pub fn pi_bio(
    data:        &NeuralData,
    calibration: &BioCalibration,
) -> StaticMatrix<Complex, 7, 7>
{
    // Step 1: diagonal from spectral powers — one value per dimension.
    let raw_diag = StaticVector.<Float, 7>.from_array([
        data.eeg_spectral.get("alpha").unwrap_or(0.0),       // A
        data.eeg_spectral.get("infraslow").unwrap_or(0.0),   // S  (fMRI BOLD proxy)
        data.eeg_spectral.get("beta").unwrap_or(0.0),        // D
        data.eeg_spectral.get("gamma_low").unwrap_or(0.0),   // L
        data.eeg_spectral.get("gamma_high").unwrap_or(0.0)
            * data.eeg_spectral.get("theta").unwrap_or(0.0),  // E  (PAC proxy)
        data.hrv_features.get("LF").unwrap_or(0.0),          // O
        data.hrv_features.get("HF").unwrap_or(0.0),          // U
    ]);

    let weighted = (0..7).map(|i| calibration.weights[i] * raw_diag[i]).to_array();
    let total = weighted.iter().sum::<Float>();
    let mut diag = StaticVector.<Float, 7>.from_array(
        weighted.map(|v| (v / total).clamp(1.0e-4, 1.0))     // prevent degeneracy
    );
    let diag_sum: Float = diag.iter().sum();
    diag = diag.map(|v| v / diag_sum);

    // Step 2: off-diagonal magnitudes from CFC.
    let c_scale = calibration.linear_params[0, 0];                       // cfc_scale stored here
    let off_diag_mag = &data.cfc_matrix * c_scale;

    // Step 3: Phases from reaction times → Gap → θ_ij = arcsin(Gap).
    let rt_mean: Float = data.reaction_times.iter().sum::<Float>() / 21.0;
    let rt_std = (data.reaction_times.iter()
                     .map(|r| (r - rt_mean).pow(2)).sum::<Float>() / 21.0)
                     .sqrt() + 1.0e-8;
    let mut phases = StaticMatrix.<Float, 7, 7>.zeros();
    let mut idx = 0;
    for i in 0..7 { for j in (i + 1)..7 {
        let gap = ((data.reaction_times[idx] - rt_mean) / rt_std).tanh();
        let phi = gap.clamp(-1.0, 1.0).asin();
        phases[i, j] =  phi;
        phases[j, i] = -phi;
        idx += 1;
    }}

    // Step 4: MLE reconstruction via Cholesky. 48 real parameters:
    //   7 real diagonal + 21·2 = 42 off-diagonal (Re, Im).
    let neg_log_likelihood = |params: &StaticVector<Float, 48>| -> Float {
        let mut l = StaticMatrix.<Complex, 7, 7>.zeros();
        let mut k = 0;
        for i in 0..7 { for j in 0..=i {
            if i == j {
                l[i, j] = Complex.from_real(params[k].max(1.0e-6));
                k += 1;
            } else {
                l[i, j] = Complex(params[k], params[k + 1]);
                k += 2;
            }
        }}
        let gamma = &l @ l.adjoint();
        let gamma = &gamma / gamma.trace();

        // LL: diagonal agreement.
        let ll_diag: Float = (0..7)
            .map(|i| -(gamma[i, i].real() - diag[i]).pow(2) / 0.01)
            .sum();

        // LL: off-diagonal magnitude agreement.
        let mut ll_off = 0.0;
        for i in 0..7 { for j in (i + 1)..7 {
            ll_off -= (gamma[i, j].abs() - off_diag_mag[i, j]).pow(2) / 0.05;
        }}

        // Physical regulariser: hard floor at P > P_crit.
        let p = (&gamma @ &gamma).trace().real();
        let p_penalty = -100.0 * (2.0 / 7.0 - p).max(0.0);

        -(ll_diag + ll_off + p_penalty)
    };

    // Initialise from the diagonal (triangle-flattened index k = i·(i+1)).
    let mut x0 = StaticVector.<Float, 48>.zeros();
    for i in 0..7 { x0[i * (i + 1)] = diag[i].sqrt(); }

    let result = bfgs(neg_log_likelihood, &x0, BfgsOptions {
        ftol: 1.0e-9, max_iter: 500,
    });

    // Reconstruct Γ from the optimal parameters.
    let mut l = StaticMatrix.<Complex, 7, 7>.zeros();
    let mut k = 0;
    for i in 0..7 { for j in 0..=i {
        if i == j {
            l[i, j] = Complex.from_real(result.x[k].max(1.0e-6));
            k += 1;
        } else {
            l[i, j] = Complex(result.x[k], result.x[k + 1]);
            k += 2;
        }
    }}
    let gamma = &l @ l.adjoint();
    &gamma / gamma.trace()
}
```

### Готовая к воспроизведению спецификация для TMS-EEG PCI {#replication-ready-tms-eeg}

:::tip Цель воспроизведения
Этот подраздел фиксирует референсную имплементацию $\pi_{\mathrm{bio}}$ для TMS-EEG PCI парадигмы — достаточно детально для независимой попытки воспроизведения end-to-end из публичного датасета.
:::

**R1. Публичные датасеты.** Кандидаты для независимого воспроизведения; ни один не имеет универсального открытого доступа, но каждый получаем по запросу авторов или через институциональное разделение данных:

| # | Датасет | Источник | Субъекты | Состояния | Доступ |
|---|---------|--------|---------|--------|--------|
| R1.a | Casali et al. 2013 PCI benchmark | Massimini lab (Milan) | 52 здоровых + 98 клинических | Wake / NREM / REM / анестезия / VS / MCS / LIS | По запросу |
| R1.b | OpenNeuro ds004504 (TMS-EEG benchmark, 2023) | Rogasch lab | 20 здоровых | Wake (baseline) | Открытый |
| R1.c | Comsa et al. 2019 (OSF "TMS-EEG sleep") | Lausanne CHUV | 12 здоровых | Wake / NREM N2 / N3 | OSF restricted |
| R1.d | Bodart et al. 2018 (clinical PCI extension) | Liège | 141 DoC пациентов | Wake / UWS / MCS / EMCS | По запросу |

Для первой попытки воспроизведения рекомендован датасет R1.b (полностью открытый, стандартизованный одно-импульсный TMS-EEG на здоровых бодрствующих субъектах, ожидаемый PCI ≈ 0.40-0.48).

**R2. Pre-processing pipeline (MNE-Python канонический).** Референсный препроцессинг для сырого EEG (60-канальный монтаж, 1 кГц sampling, TMS-triggered эпохи $[-1, +1]\,\mathrm{s}$):

| Шаг | Операция | Tool / параметры |
|------|-----------|-------------------|
| R2.1 | Удаление TMS pulse артефакта | Кубическая интерполяция $[-2, +12]\,\mathrm{ms}$ вокруг импульса (`mne.preprocessing.fix_stim_artifact`) |
| R2.2 | Downsample | 1 кГц → 250 Гц (`mne.Epochs.resample`) |
| R2.3 | Re-reference | Average reference, исключая TMS-сторону frontal channels |
| R2.4 | Bandpass filter | 0.5–80 Гц, 4-й порядок Butterworth zero-phase (`mne.filter.filter_data`) |
| R2.5 | Notch filter | 50 Гц (или 60 Гц), Q = 30 |
| R2.6 | ICA artefact rejection | FastICA, 30 компонент; reject TMS-locked decay, eye-blink, ECG (`mne.preprocessing.ICA`) |
| R2.7 | Epoch-level rejection | $|\text{max}-\text{min}| > 120\,\mu\mathrm V$ → отбросить эпоху |
| R2.8 | Спектральная декомпозиция | Morlet wavelets, 1–80 Гц log-spaced, 5-cycle wavelet, baseline $[-600,-100]\,\mathrm{ms}$ |

Канонические полосы, используемые $\pi_{\mathrm{bio}}$, затем извлекаются из вейвлет-спектрограммы (интегрированы по post-TMS окну $[0, +300]\,\mathrm{ms}$, усреднены по каналам для диагонального feature-вектора; cross-channel pairwise для CFC-вычислений).

**R3. Feature extraction.** Из preprocessed данных вычислить:
- Семь скалярных спектральных features $S_A, S_S, S_D, S_L, S_E, S_O, S_U$ согласно [Step-1 band table](#шаг-1-диагональ).
- Cross-frequency-coupling матрицу $\mathrm{CFC}_{ij}$ ($7\times 7$) согласно [Step-2 table](#шаг-2-когерентности) используя Tort Modulation Index (`mne_connectivity`).
- 21 reaction-time surrogates $\mathrm{RT}_{ij}$ из paradoxical probes если behavioral data доступна; иначе установить $\mathrm{RT}_{ij}$ как pairwise phase-locking value (PLV) как proxy.
- HRV features $\mathrm{LF}, \mathrm{HF}$ из одновременной ECG (требуется для $O$ и $U$ измерений).

**R4. Калибровка.** Веса $w_k$ определяются подгонкой $\pi_{\mathrm{bio}}$ на **healthy-waking референсной cohort** ($\ge 20$ субъектов) так, что популяционное среднее $\gamma_{kk}$ — равномерно $= 1/7 \pm 0.02$. Cross-validation: leave-one-subject-out, цель консистентности реконструированного $P$ через субъектов ($\mathrm{CV} < 15\%$).

**R5. Реконструкция.** Запустить MLE алгоритм (Step 4 выше) с:
- Cholesky инициализацией из калиброванной диагонали.
- Optimizer: `scipy.optimize.minimize(method='L-BFGS-B', options={'ftol': 1e-9, 'maxiter': 500})`.
- Regularizer: $\lambda_1 = 0.1$, $\lambda_2 = 100$ (эмпирические defaults; субъекты должны попробовать $\lambda_1 \in \{0.01, 0.1, 1\}$ и отчитать чувствительность).

**R6. Вычисление наблюдаемых (канонически):**
- $P = \mathrm{Tr}(\Gamma^2)$ — **$G_2$-инвариантна**.
- $R = 1/(7P)$ ([T-126 [Т]](/docs/proofs/consciousness/conscious-window#t-126)) — **$G_2$-инвариантна**.
- $\Phi = (\sum_{i\ne j}|\gamma_{ij}|^2)/(\sum_i\gamma_{ii}^2)$ — **базис-зависима**, инвариантна в $G_2$-стабилизированном Фано-фрейме.
- $\mathrm{Coh}_E = (\gamma_{EE}^2 + 2\sum_{i\ne E}|\gamma_{Ei}|^2)/\mathrm{Tr}(\Gamma^2)$ — **$E$-фиксированная**, инвариантна под $G_2^{(E)}$.

**Gauge-фиксация:** (i) выровнять labelling к Fano-convention; (ii) привязать $|E\rangle$ к γ-high×θ PAC.

**R7. Валидация против PCI.**
- Вычислить PCI субъекта на тех же TMS-EEG данных через алгоритм Massimini (Lempel–Ziv complexity значимых источников; reference implementation доступна через PCIst package).
- Тест монотонной гипотезы $\Phi(\Gamma) \approx \alpha_\mathrm{PCI}\cdot \mathrm{PCI} + \beta_\mathrm{PCI}$ (Step 5 теорема).
- Pre-register: $r_{\mathrm{Spearman}} \ge 0.5$ через $\ge 20$ субъектов составляет corroboration; $r < 0.3$ составляет фальсификацию P8.3.

**R8. Reference implementation stub.** Python-код в следующем подразделе — *референсный* только: документирует алгоритм точно, но не turn-key pipeline. Полная MNE-Python имплементация с:
- `mne.Raw` загрузчиком, обёрнутым вокруг BIDS-форматированного EEG,
- `mne_connectivity` интеграцией для CFC,
- `scipy.optimize.minimize` MLE wrapper,
- `pyphi`-совместимым $\Phi$ вычислением (опционально),
- CI-репортингом,
планируется как отдельный пакет `uhm-neurocalib` (релиз привязан к R1.b пилотным результатам). До доступности этого пакета независимые имплементаторы должны использовать pseudocode как specification, и подавать issues/PRs на несоответствия со спецификацией здесь.

**Требования воспроизводимости.** Любая претензия на успешное или неуспешное воспроизведение должна публиковать:
- (i) сырые данные (BIDS-формат) и pre-processing scripts (воспроизводимые из R2);
- (ii) реконструированные $\Gamma$-матрицы и сделанный gauge-fixing выбор;
- (iii) значения $P, R, \Phi, \mathrm{Coh}_E$ на субъекта;
- (iv) PCI значения, вычисленные на тех же эпохах;
- (v) протокол статистического теста и seed для случайных splits.

Без пунктов (i)-(v) попытка воспроизведения не может быть аудирована.

### Тестируемые предсказания протокола $\pi_{\mathrm{bio}}$ {#тестируемые-предсказания-p8}

| № | Предсказание | Метод проверки | Критерий фальсификации |
|---|-------------|----------------|------------------------|
| P8.1 | $P(\Gamma_{\mathrm{wake}}) > 2/7$ для бодрствующих субъектов | EEG+HRV → $\pi_{\mathrm{bio}}$ → $P$ | $P < 2/7$ у здоровых бодрствующих |
| P8.2 | $P(\Gamma_{\mathrm{NREM3}}) < 2/7$ во время глубокого сна | EEG → $\pi_{\mathrm{bio}}$ → $P$ | $P > 2/7$ при N3 |
| P8.3 | $\mathrm{PCI} \propto \Phi(\Gamma)$ (монотонная зависимость) | TMS-EEG + $\pi_{\mathrm{bio}}$ | Немонотонная корреляция |
| P8.4 | Переход $P = 2/7$ совпадает с PCI $\approx 0.31$ | Одновременное измерение | Расхождение порогов |
| P8.5 | $\mathrm{Gap}(L,E) \approx 1$ при алекситимии | Двойное интервью + EEG | $\mathrm{Gap}(L,E) \ll 1$ при диагностированной алекситимии |
| P8.6 | Критические экспоненты $\beta = 1/4$ при переходе сон-бодрствование | EEG мониторинг + $\pi_{\mathrm{bio}}$ → $P(\tau)$ вблизи $P_{\mathrm{crit}}$ | Другие экспоненты |

### Ключевые статьи {#литература-p8}

1. **Casali et al. (2013)** — PCI: "A theoretically based index of consciousness independent of sensory processing and behavior." *Science Translational Medicine*, 5(198). [PubMed: 23946194](https://pubmed.ncbi.nlm.nih.gov/23946194/)
2. **Pothos-Busemeyer (2022)** — Quantum cognition review. *Annual Review of Psychology*, 73, 749-778.
3. **Butlin et al. (2023/2025)** — "Consciousness in Artificial Intelligence: Insights from the Science of Consciousness." [arXiv: 2308.08708](https://arxiv.org/abs/2308.08708); updated 2025: "Identifying indicators of consciousness in AI systems." *Trends in Cognitive Sciences*.
4. **eLife (2024/2025)** — "Spatiotemporal brain complexity quantifies consciousness outside of perturbation paradigms." [eLife 98920](https://elifesciences.org/articles/98920).
5. **Quantum-inspired EEG (2026)** — "Quantum inspired feature engineering for explainable EEG signal classification." *Scientific Reports*. [Nature](https://www.nature.com/articles/s41598-026-41821-8).

---

**Связанные документы:**
- [Матрица когерентности](/docs/core/dynamics/coherence-matrix) — определение $\Gamma$
- [Жизнеспособность](/docs/core/dynamics/viability) — $P$ и $P_{\text{crit}} = 2/7$
- [Эмерджентное время](/docs/proofs/dynamics/emergent-time) — механизм Пейдж–Вуттерс, τ ∈ ℤ₇
- [Эволюция](/docs/core/dynamics/evolution) — уравнение $d\Gamma(\tau)/d\tau$ с $H_{eff}$
- [Самонаблюдение](/docs/consciousness/foundations/self-observation) — меры $R$, $\Phi$, $C$
- [Категорный формализм](/docs/proofs/categorical/categorical-formalism) — функтор $F$, $\mathbf{Exp}^{disc}_\infty$
- [Теорема о минимальности 7D](/docs/proofs/minimality/theorem-minimality-7) — почему 7 измерений
- [Нотация](/docs/reference/notation#индексы-измерений-протокол-измерения) — индексы $I_A, \ldots, I_U$
- [Gap-диагностика](/docs/applied/research/gap-diagnostics) — клинические приложения Gap-профиля
- [Голдстоуновские моды](/docs/applied/coherence-cybernetics/goldstone-modes) — предсказание инфрамедленных частот
- [Фано-канал](/docs/proofs/gap/fano-channel) — теорема о равновесном Gap

