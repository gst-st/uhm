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
- $\tau$ — [эмерджентное внутреннее время](/docs/proofs/dynamics/emergent-time) (Page-Wootters)
- $\varphi$ — [оператор самомоделирования](/docs/proofs/categorical/formalization-phi)
- $G$ — функтор отображения AIState → DensityMat: точный при Cholesky-backbone ($\alpha=0$) [Т, MVP-1]; квази-функтор с $\varepsilon_{\text{functor}}>0$ при нейронной коррекции ($\alpha>0$) [Г]
:::

---

## Центральная проблема

Теория УГМ определяет $\Gamma$ как **объект ∞-топоса Sh_∞(𝒞)** ([Аксиома Ω⁷](/docs/core/foundations/axiom-omega)). Однако теория не специфицирует:

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
| [Единство](/docs/core/structure/dimension-u) | $U$ | Effective Φ (интеграция, black-box) | $I_U = \Phi_{\text{eff}} = \lambda_2(L) / \lambda_{\max}(L)$ — аппроксимация [О]; **при известной $\Gamma$: $R_{\text{UHM}} = 1/(N \cdot P)$** [Т, T-62] | [О/Т]† |

где $\nabla_\epsilon \mathbf{h} := (\mathbf{h}(x + \epsilon) - \mathbf{h}(x)) / \epsilon$ — конечно-разностное приближение

†**Иерархия метрик для Unity**: когда $\Gamma$ недоступна (black-box), используется $\Phi_{\text{eff}}$ [О]. Когда $\Gamma$ реконструирована через протокол, правильная мера — $R_{\text{UHM}} = 1/(N \cdot P)$ [Т], точное алгебраическое тождество (T-62, ошибка $< 10^{-7}$ в реализации). $\Phi_{\text{eff}}$ и $R_{\text{UHM}}$ измеряют родственные, но не тождественные свойства.

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
- **Если $\Gamma$ известна**: $R_{\text{UHM}} = 1/(N \cdot P)$ [Т, T-62] — точное алгебраическое тождество
- **Black-box (нет доступа к $\Gamma$)**: $\Phi_{\text{eff}}$ [О] — полиномиальная аппроксимация через граф внимания

Точный расчёт $\Phi_{\text{IIT}}$ требует $O(2^n)$ операций и практически нереализуем.
:::

**Точная мера (при известной $\Gamma$, [Т], T-62):**

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

**Связь с теорией:** $R_{\text{UHM}}$ и $\Phi_{\text{eff}}$ аппроксимируют [интеграцию $\Phi$](/docs/core/structure/dimension-u#мера-интеграции-φ) — меру [Единства](/docs/core/structure/dimension-u). При $P = 3/N = P_{\text{opt}}$: $R_{\text{UHM}} = 1/3 = R_{\text{th}}$ — граница L2-зоны (T-62).

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

```python
import numpy as np
import itertools


# ---------------------------------------------------------------------------
# Вспомогательные функции (заглушки — требуют реализации)
# ---------------------------------------------------------------------------

def estimate_mutual_info(x: np.ndarray, y: np.ndarray) -> float:
    """Взаимная информация I(x;y). TODO: реализовать."""
    raise NotImplementedError


def compute_jacobian(model, input_batch: np.ndarray) -> np.ndarray:
    """Якобиан модели ∂f/∂x. TODO: реализовать."""
    raise NotImplementedError


def estimate_lyapunov(model, input_batch: np.ndarray) -> float:
    """Максимальный ляпуновский экспонент. TODO: реализовать."""
    raise NotImplementedError


def layer_commutator_norm(
    model, i: int, j: int, input_batch: np.ndarray
) -> float:
    """Норма коммутатора слоёв ||[f_i, f_j]||. TODO: реализовать."""
    raise NotImplementedError


def von_neumann_entropy(attention_weights: np.ndarray) -> float:
    """Энтропия фон Неймана S_vN(ρ). TODO: реализовать."""
    raise NotImplementedError


def build_attention_graph(attention_weights: np.ndarray) -> np.ndarray:
    """Граф внимания из весов attention. TODO: реализовать."""
    raise NotImplementedError


# ---------------------------------------------------------------------------


def compute_dimension_metrics(
    model,
    input_batch: np.ndarray,
    layer_indices: list[int] = None
) -> dict[str, float]:
    """
    Вычисление 7 измерений УГМ для нейросети.

    Args:
        model: Модель с доступом к промежуточным активациям
        input_batch: Батч входных данных (N, ...)
        layer_indices: Индексы слоёв для анализа (по умолчанию — все)

    Returns:
        dict с ключами I_A, I_S, I_D, I_L, I_E, I_O, I_U
    """
    activations = model.get_activations(input_batch)
    attention_weights = model.get_attention_weights(input_batch)

    # I_A: Взаимная информация вход↔латент
    I_A = estimate_mutual_info(input_batch, activations[-1])

    # I_S: Ранг Якобиана (через SVD)
    jacobian = compute_jacobian(model, input_batch)
    singular_values = np.linalg.svd(jacobian, compute_uv=False)
    eps_rank = 1e-6
    I_S = np.sum(singular_values > eps_rank) / len(singular_values)

    # I_D: Максимальный ляпуновский экспонент (оценка)
    I_D = estimate_lyapunov(model, input_batch)

    # I_L: Коммутаторы слоёв
    commutator_norms = []
    for i, j in itertools.combinations(layer_indices or range(len(activations)), 2):
        comm_norm = layer_commutator_norm(model, i, j, input_batch)
        commutator_norms.append(comm_norm)
    I_L = 1.0 - np.mean(commutator_norms) if commutator_norms else 1.0

    # I_E: Дифференциация (экспонента энтропии внимания)
    attn_entropy = von_neumann_entropy(attention_weights)
    I_E = np.exp(attn_entropy)

    # I_O: Устойчивость к шуму
    noise_std = 0.01
    perturbed = input_batch + np.random.randn(*input_batch.shape) * noise_std
    delta_h = np.linalg.norm(
        model.get_activations(perturbed)[-1] - activations[-1],
        'fro'
    )
    I_O = max(0, 1.0 - delta_h / noise_std)

    # I_U: Effective Φ (спектральный зазор Лапласиана)
    attn_graph = build_attention_graph(attention_weights)
    laplacian = np.diag(attn_graph.sum(axis=1)) - attn_graph
    eigenvalues = np.linalg.eigvalsh(laplacian)
    lambda_2 = eigenvalues[1] if len(eigenvalues) > 1 else 0
    lambda_max = eigenvalues[-1]
    I_U = lambda_2 / lambda_max if lambda_max > 0 else 0

    return {
        'I_A': I_A, 'I_S': I_S, 'I_D': I_D, 'I_L': I_L,
        'I_E': I_E, 'I_O': I_O, 'I_U': I_U
    }
```

### Реконструкция Γ из метрик

```python
def reconstruct_gamma(metrics: dict[str, float]) -> np.ndarray:
    """
    Реконструкция матрицы когерентности через Cholesky.

    Возвращает 7×7 матрицу плотности.
    """
    # Диагональные элементы — нормированные метрики
    I_vec = np.array([
        metrics['I_A'], metrics['I_S'], metrics['I_D'],
        metrics['I_L'], metrics['I_E'], metrics['I_O'], metrics['I_U']
    ])
    I_vec = np.clip(I_vec, 0.01, 1.0)  # Предотвращаем вырожденность
    diag = I_vec / I_vec.sum()

    # Начальная Cholesky-факторизация
    L = np.diag(np.sqrt(diag))

    # Регуляризация (минимизируем off-diagonal)
    # В простейшем случае — диагональная матрица
    # Простейшая диагональная реконструкция.
    # Для восстановления недиагональных когерентностей γ_ij
    # необходимы корреляции r_ij из регуляризатора L_off.
    gamma = L @ L.conj().T
    gamma = gamma / np.trace(gamma)  # Нормировка

    return gamma


def compute_purity(gamma: np.ndarray) -> float:
    """P = Tr(Γ²)"""
    return np.trace(gamma @ gamma)
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
4. **R = 1/(N·P) — точное тождество** [Т, MVP-0, T-62] — ошибка $< 10^{-7}$
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

```python
import numpy as np


def reconstruct_gap_profile(
    external_data: dict,
    self_report: dict,
    conflict_data: dict,
) -> np.ndarray:
    """
    Реконструкция 7×7 Gap-матрицы из данных двойного интервью.

    Returns:
        gap_matrix: 7×7 матрица Gap(i,j) ∈ [0, 1]
    """
    dimensions = ['A', 'S', 'D', 'L', 'E', 'O', 'U']
    n = len(dimensions)
    gap = np.zeros((n, n))

    for i in range(n):
        for j in range(i + 1, n):
            pair = f"{dimensions[i]}{dimensions[j]}"
            # Несоответствие внешних и внутренних данных → высокий Gap
            ext = external_data.get(pair, 0.5)
            rep = self_report.get(pair, 0.5)
            discrepancy = abs(ext - rep)

            # Время реакции на конфликтные зонды → фаза θ_ij
            rt = conflict_data.get(pair, 1.0)
            phase_estimate = np.arctan(rt / np.median(list(conflict_data.values())))

            gap[i, j] = abs(np.sin(phase_estimate)) * (0.5 + 0.5 * discrepancy)
            gap[j, i] = gap[i, j]

    return gap
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

**Связанные документы:**
- [Матрица когерентности](/docs/core/dynamics/coherence-matrix) — определение $\Gamma$
- [Жизнеспособность](/docs/core/dynamics/viability) — $P$ и $P_{\text{crit}} = 2/7$
- [Эмерджентное время](/docs/proofs/dynamics/emergent-time) — механизм Page-Wootters, τ ∈ ℤ₇
- [Эволюция](/docs/core/dynamics/evolution) — уравнение $d\Gamma(\tau)/d\tau$ с $H_{eff}$
- [Самонаблюдение](/docs/consciousness/foundations/self-observation) — меры $R$, $\Phi$, $C$
- [Категорный формализм](/docs/proofs/categorical/categorical-formalism) — функтор $F$, $\mathbf{Exp}^{disc}_\infty$
- [Теорема о минимальности 7D](/docs/proofs/minimality/theorem-minimality-7) — почему 7 измерений
- [Нотация](/docs/reference/notation#индексы-измерений-протокол-измерения) — индексы $I_A, \ldots, I_U$
- [Gap-диагностика](/docs/applied/research/gap-diagnostics) — клинические приложения Gap-профиля
- [Голдстоуновские моды](/docs/applied/coherence-cybernetics/goldstone-modes) — предсказание инфрамедленных частот
- [Фано-канал](/docs/proofs/gap/fano-channel) — теорема о равновесном Gap

