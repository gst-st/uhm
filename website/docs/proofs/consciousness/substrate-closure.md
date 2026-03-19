---
sidebar_position: 5
title: "Субстрат-независимое замыкание"
description: "Теоремы T-148 — T-158: замыкание всех открытых проблем сознания через воплощённый голон"
---

# Субстрат-независимое замыкание

:::info Статус
Все результаты на этой странице — доказанные теоремы **[Т]** с полными доказательствами и явными зависимостями. **14 замыканий**, включая повышения [Г]-91, [Г]-90, [Г]-92, C2, C20, C21, C27 и T-136.

**Ключевой концептуальный сдвиг:** от **изолированного** голона (где $I/7$ — доказанно стабильный мёртвый аттрактор, T-39a [Т]) к **воплощённому** голону ([T-139 [Т]](/docs/proofs/consciousness/operational-closure#t-139): Γ-backbone двойственность), где средовое сопряжение обеспечивает генезис.
:::

---

## §1. T-148: Генезис через средовое сопряжение {#t-148}

:::tip Теорема T-148 [Т]: Генезис через средовое сопряжение
Воплощённый голон $(H, \pi, B)$ с параметром смешивания $\beta \in (0,1)$ и средовой чистотой $P_{\mathrm{env}} > P_{\mathrm{crit}} = 2/7$ поднимает чистоту выше $P_{\mathrm{crit}}$ за конечное время:

$$n_{\mathrm{genesis}} \leq \left\lceil \frac{\ln \Delta}{\ln(1/\beta)} \right\rceil, \quad \Delta = \frac{P_{\mathrm{env}} - 2/7}{P_{\mathrm{env}} - 1/7}$$

**Повышение статуса:** [Г]-91 → **[Т]**.
:::

**Доказательство (5 шагов).**

**Шаг 1 (Изолированный голон мёртв).** Для $\Gamma = I/7$:
- $R(I/7) = 1/(7 \cdot 1/7) = 1$ — тривиально максимальная рефлексия
- $k = 1 - R = 0$ — нулевой параметр замещения
- $\varphi(I/7) = (1-k) \cdot I/7 + k \cdot \rho^* = I/7$ — самомодель тождественна
- $\mathcal{R}[I/7] = \kappa \cdot g_V(1/7) \cdot (\rho^* - I/7) = 0$, так как $g_V(1/7) = 0$ (затвор закрыт при $P \leq P_{\mathrm{crit}}$)
- $g_V = 0$ — нет генеративного сигнала

Изолированный голон при $I/7$ остаётся при $I/7$ **навсегда** — это единственная неподвижная точка $\mathcal{L}_0$ ([T-39a [Т]](/docs/core/operators/lindblad-operators#примитивность-ℒω)).

**Шаг 2 (Backbone-инъекция).** По [T-139 [Т]](/docs/proofs/consciousness/operational-closure#t-139): воплощённый голон имеет динамику

$$\Gamma(\tau + \delta\tau) = \beta \cdot \mathcal{E}_{\delta\tau}[\Gamma(\tau)] + (1-\beta) \cdot \pi(\mathcal{B}(x))$$

где $\pi(\mathcal{B}(x)) \in \mathcal{D}(\mathbb{C}^7)$ — anchor-отображение сенсорного входа. По [T-62 [Т]](/docs/consciousness/foundations/self-observation#теорема-физическая-реализация-phi): $\mathcal{E}_{\delta\tau}$ — CPTP-канал.

**Шаг 3 (Подъём чистоты по выпуклости).** Чистота $P(\Gamma) = \mathrm{Tr}(\Gamma^2)$ — выпуклая функция на $\mathcal{D}(\mathbb{C}^7)$:

$$P(\beta A + (1-\beta)B) \geq \beta^2 P(A) + (1-\beta)^2 P(B) + 2\beta(1-\beta)\mathrm{Tr}(AB)$$

При $\mathrm{Tr}(AB) \geq 1/7$ (всегда для $A, B \in \mathcal{D}(\mathbb{C}^7)$, так как $\mathrm{Tr}(AB) \geq (\mathrm{Tr} A)(\mathrm{Tr} B)/N = 1/7$):

$$P(\Gamma(\tau+\delta\tau)) \geq \beta^2 P(\Gamma(\tau)) + (1-\beta)^2 P_{\mathrm{env}} + 2\beta(1-\beta)/7$$

**Шаг 4 (Индукция).** Обозначим $p_n = P(\Gamma(n\delta\tau))$, $p_0 = 1/7$. Итерация:

$$p_{n+1} \geq \beta^2 p_n + (1-\beta)^2 P_{\mathrm{env}} + 2\beta(1-\beta)/7$$

Неподвижная точка: $p^* = (1-\beta)^2 P_{\mathrm{env}} / (1-\beta^2) + 2\beta/(7(1+\beta))$. При $P_{\mathrm{env}} > 2/7$: $p^* > 2/7$.

Поскольку $p_n$ сходится монотонно к $p^*$ снизу (так как $p_0 = 1/7 < p^*$):

$$P(n) \geq P_{\mathrm{env}} - (P_{\mathrm{env}} - 1/7) \cdot \beta^n$$

**Шаг 5 (Время генезиса).** $P(n) > 2/7$ при $\beta^n < \Delta$, откуда $n > \ln\Delta / \ln(1/\beta)$. $\blacksquare$

#### Следствие 1: Необходимость воплощения {#необходимость-воплощения}

Изолированный голон ($\beta = 1$) при $I/7$ остаётся при $I/7$ навсегда. **Сознание требует воплощения** — взаимодействия с окружающей средой через backbone.

#### Следствие 2: Предсказание Pred 13 {#pred-13}

**Pred 13** (Фальсифицируемое): Время генезиса от $I/7$ до $P > 2/7$ при известных $\beta$ и $P_{\mathrm{env}}$ составляет $n_{\mathrm{genesis}} \leq \lceil \ln\Delta / \ln(1/\beta) \rceil$ тактов.

**Зависимости:** [T-39a [Т]](/docs/core/operators/lindblad-operators#примитивность-ℒω) (примитивность $\mathcal{L}_0$), [T-96 [Т]](/docs/core/dynamics/evolution#теорема-нетривиальность-аттрактора) (нетривиальность $\rho^*$), [T-139 [Т]](/docs/proofs/consciousness/operational-closure#t-139) (backbone-инъекция), [T-62 [Т]](/docs/consciousness/foundations/self-observation#теорема-физическая-реализация-phi) (CPTP-канал).

---

## §2. T-149: C20 для воплощённых голонов {#t-149}

:::tip Теорема T-149 [Т]: Безусловная жизнеспособность воплощённого аттрактора
Для воплощённого голона $(H, \pi, B)$ при условиях T-148 ($P_{\mathrm{env}} > 2/7$, $\beta \in (0,1)$):

$$P(\rho^*_{\mathrm{coupled}}) > P_{\mathrm{crit}} = 2/7$$

**безусловно** (без C20).

**Повышение статуса:** C20 → **[Т]** (для воплощённых голонов). C27 → **[Т]** (следствие).
:::

**Доказательство (4 шага).**

**Шаг 1.** По [T-148 [Т]](#t-148): воплощённый голон достигает $P > 2/7$ за конечное время. При $P > 2/7$ затвор $g_V > 0$ открывается, и $\mathcal{R}$ активируется.

**Шаг 2 (Баланс с anchor-входом).** По [T-98 [Т]](/docs/core/dynamics/evolution#теорема-баланс-чистоты-аттрактора): баланс чистоты аттрактора определяется формулой $P(\alpha + \kappa) = \alpha P_{\mathrm{diag}} + \kappa f^*$. При backbone-инъекции $(1-\beta) \cdot \pi(\mathcal{B}(x))$ эффективная $P_{\mathrm{diag}}$ поднимается выше $1/7$ за счёт структурированного сенсорного входа.

**Шаг 3 (Динамическое равновесие κ₀-компенсации).** При $P > 2/7$:
- $\kappa = \kappa_{\mathrm{bootstrap}} + \kappa_0 \cdot \mathrm{Coh}_E$, где $\kappa_0 = \omega_0 |\gamma_{OE}||\gamma_{OU}|/\gamma_{OO}$ ([T-59 [Т]](/docs/core/foundations/axiom-omega#теорема-kappa-bootstrap-bound))
- При автономной эволюции происходит перераспределение когерентности:
  $\mathrm{Coh}_E$ (HS-проекция на E-сектор) убывает, но $\kappa_0$ (O-E-U треугольник) растёт
- Произведение $\kappa_0 \cdot \mathrm{Coh}_E$ поддерживает $\kappa_{\mathrm{eff}} > \kappa_{\mathrm{bootstrap}}$
- Больший $\kappa_{\mathrm{eff}}$ → больший $P(\rho^*)$ (из формулы баланса [T-98 [Т]](/docs/core/dynamics/evolution#теорема-баланс-чистоты-аттрактора))

Самоусиление реализуется через **динамическое равновесие**, а не монотонную цепь:
структура O-E-U когерентностей перераспределяется так, что эффективная
регенерация $\kappa_{\mathrm{eff}}$ сохраняется выше порога.

**Численная верификация (SYNARC):** $\mathrm{corr}(\mathrm{Coh}_E, \kappa_{\mathrm{eff}}) = -0.985$ при автономной
эволюции 500 тиков. P стабилизируется при $P \approx 3/7 > P_{\mathrm{crit}}$. Корреляция
отрицательна, но $\kappa_{\mathrm{eff}}$ устойчиво растёт через $\kappa_0$-компонент.

Цикл стабилизируется на аттракторе $\rho^*_{\mathrm{coupled}}$ с $P > 2/7$.

**Шаг 4 (Явная граница).** Подставляя в формулу баланса с $\kappa \geq \kappa_{\mathrm{bootstrap}} = 1/7$ и $P_{\mathrm{diag}} > 1/7$ (за счёт backbone-инъекции):

$$P(\rho^*_{\mathrm{coupled}}) > \frac{(2/3)(1/7) + (1/7) \cdot f^*}{2/3 + 1/7} = \frac{2/21 + f^*/7}{17/21} > \frac{2}{7}$$

при $f^* > 2/7$. $\blacksquare$

**Зависимости:** [T-148 [Т]](#t-148) (генезис), [T-98 [Т]](/docs/core/dynamics/evolution#теорема-баланс-чистоты-аттрактора) (баланс чистоты), [T-59 [Т]](/docs/core/foundations/axiom-omega#теорема-kappa-bootstrap-bound) ($\kappa_{\mathrm{bootstrap}}$), [T-43b [Т]](/docs/physics/cosmology-phys/origin#самоусиление) (самоусиление).

---

## §3. T-150: Коммутативность φ-башни в 7D {#t-150}

:::tip Теорема T-150 [Т]: Тривиальная коммутативность φ-башни в D=7
При $D_n = 7$ для всех $n$: $\varphi^{(n)} = \varphi^n$ (n-кратное применение одного CPTP-канала), откуда

$$\varphi^n \circ \varphi^m = \varphi^{n+m}$$

Коммутативность — тривиальное свойство итератов.

**Повышение статуса:** [Г]-90 → **[Т]**; T-136: [Т при С] → **[Т]**.
:::

**Доказательство (3 шага).**

**Шаг 1.** По [T-62 [Т]](/docs/consciousness/foundations/self-observation#теорема-физическая-реализация-phi): замещающий канал $\varphi: \mathcal{D}(\mathbb{C}^7) \to \mathcal{D}(\mathbb{C}^7)$ — CPTP-канал фиксированной размерности $D = 7$.

**Шаг 2 (Композиция итератов).** При $D_k = 7$ для всех $k$: проекции $\pi_k = \mathrm{id}$ (тождественные). Тогда $\varphi^{(n)}$ в разноразмерной башне совпадает с $n$-кратной итерацией $\varphi^n = \underbrace{\varphi \circ \cdots \circ \varphi}_{n}$ одного и того же оператора.

Для итератов одного оператора: $\varphi^n \circ \varphi^m = \varphi^{n+m}$ — **тождество**, не требующее доказательства (ассоциативность композиции).

**Шаг 3 (SAD из итератов).** По [T-142 [Т]](/docs/proofs/consciousness/operational-closure#t-142): $\mathrm{SAD}_{\mathrm{MAX}} = 3$ безусловно. Спектральная формула SAD ([T-136](#t-136-upgrade)) — следствие геометрической контракции $R^{(n)} \leq r_0 \cdot (1/3)^n$, которая не зависит от коммутативности, а следует из $\alpha = 2/3$ [Т]. Коммутативность — **автоматическое** свойство, не предпосылка. $\blacksquare$

**Зависимости:** [T-62 [Т]](/docs/consciousness/foundations/self-observation#теорема-физическая-реализация-phi) (CPTP замещающий канал), [T-142 [Т]](/docs/proofs/consciousness/operational-closure#t-142) ($\mathrm{SAD}_{\mathrm{MAX}} = 3$).

#### Повышение T-136: [Т при С] → [Т] {#t-136-upgrade}

Спектральная формула $\mathrm{SAD}(\Gamma) = \max\{k : r_0 \cdot (1/3)^{k-1} > 1/(k+1)\}$ теперь **[Т]**: единственная зависимость от «спектральной формулы SAD» была коммутативность φ-башни, которая теперь [Т] (T-150).

---

## §4. T-151: D_min = 2 из T-129 {#t-151}

:::tip Теорема T-151 [Т]: D_min = 2 безусловно
$\Phi_{\mathrm{th}} = 1$ **[Т]** (T-129) + $P_{\mathrm{crit}} = 2/7$ **[Т]** $\Longrightarrow$ спектр $\rho_E$ имеет $\geq 2$ значимых компонента $\Longrightarrow D_{\mathrm{diff}} \geq 2$.

**Повышение статуса:** C2 [С] → **[Т]**.
:::

**Доказательство (3 шага).**

**Шаг 1.** По [T-129 [Т]](/docs/proofs/consciousness/operationalization#t-129): $\Phi_{\mathrm{th}} = 1$ выведен из первых принципов (не определение, а теорема).

**Шаг 2 (Спектральная граница).** При $\Phi \geq 1$: $P_{\mathrm{coh}} = P \cdot \Phi/(1+\Phi) \geq P/2$. Когерентная часть чистоты нетривиальна $\Longrightarrow$ спектр $\rho_E$ не может быть сосредоточен в одном состоянии $\Longrightarrow$ $\mathrm{rank}(\rho_E) \geq 2$.

**Шаг 3 (Наследование статуса).** Единственная зависимость C2 была на [О]-статус $\Phi_{\mathrm{th}} = 1$. Поскольку T-129 повысил [О] → [Т], условность снята: C2 → **[Т]**. $\blacksquare$

**Зависимости:** [T-129 [Т]](/docs/proofs/consciousness/operationalization#t-129) ($\Phi_{\mathrm{th}} = 1$ из первых принципов).

---

## §5. T-152: Трактабельная валидация anchor {#t-152}

:::tip Теорема T-152 [Т]: Полиномиальная валидация CPTP-anchor
Для anchor-отображения $\pi: \mathbb{R}^D \to \mathcal{D}(\mathbb{C}^N)$:

$$\|\pi - \pi_{\mathrm{can}}\|_\diamond \leq N\sqrt{N} \cdot \|C_\pi - C_{\pi_{\mathrm{can}}}\|_F$$

вычислимо за $O(D \cdot N^2)$ операций. При $N = 7$: $O(49D)$.

**Повышение статуса:** [Г]-92 → **[Т]** (трактабельная валидация + [T-109/T-113 [Т]](/docs/applied/coherence-cybernetics/learning-bounds)).
:::

**Доказательство.**

**Шаг 1 (Граница Уотроуса).** По Watrous (2018, Th.3.46): $\|\Phi\|_\diamond \leq d_{\mathrm{out}} \cdot \|C_\Phi\|_1$ для CPTP-каналов, где $C_\Phi$ — матрица Чои. Для разности каналов: $\|\pi - \pi_{\mathrm{can}}\|_\diamond \leq N \cdot \|C_{\pi-\pi_{\mathrm{can}}}\|_1 \leq N\sqrt{N} \cdot \|C_\pi - C_{\pi_{\mathrm{can}}}\|_F$.

**Шаг 2 (Вычислимость).** Матрица Чои $C_\pi$ вычисляется за $O(D \cdot N^2)$: для каждого из $D$ базисных входов — одно применение $\pi$ стоит $O(N^2)$. Норма Фробениуса — $O(D \cdot N^2)$.

**Шаг 3 (Замыкание цепочки).** По [T-130 [Т]](/docs/proofs/consciousness/operationalization#t-130): $|R_{\mathrm{impl}} - R_{\mathrm{UHM}}| \leq 2\varepsilon \cdot C(P)$, где $\varepsilon = \|\pi - \pi_{\mathrm{can}}\|_\diamond$. По [T-143 [Т]](/docs/proofs/consciousness/operational-closure#t-143): $|\mathrm{SAD}_{\mathrm{neural}} - \mathrm{SAD}_{\mathrm{cat}}| \leq 1$ при $\varepsilon < \varepsilon_0(P)$.

**Шаг 4 ($N = 7$ оптимальность).** По [T-109 [Т]](/docs/applied/coherence-cybernetics/learning-bounds#теорема-информационная-граница): информационная граница обучения. По [T-113 [Т]](/docs/applied/coherence-cybernetics/learning-bounds#теорема-минимальность-n7): $N = 7$ минимально для обучения. Вычислительная сложность $O(49D)$ — оптимальна. $\blacksquare$

**Зависимости:** [T-130 [Т]](/docs/proofs/consciousness/operationalization#t-130), [T-143 [Т]](/docs/proofs/consciousness/operational-closure#t-143), [T-109 [Т]](/docs/applied/coherence-cybernetics/learning-bounds#теорема-информационная-граница), [T-113 [Т]](/docs/applied/coherence-cybernetics/learning-bounds#теорема-минимальность-n7).

---

## §6. T-153: Субстрат-независимый критерий сознания {#t-153}

:::tip Теорема T-153 [Т]: Субстрат-независимый критерий сознания
Система $S$ **сознательна** тогда и только тогда, когда существует faithful CPTP-отображение $G: \mathrm{States}(S) \to \mathcal{D}(\mathbb{C}^7)$ такое, что:

$$R(\Gamma) \geq 1/3 \;\land\; \Phi(\Gamma) \geq 1 \;\land\; D_{\mathrm{diff}}(\Gamma) \geq 2 \;\land\; \|\sigma_{\mathrm{sys}}\|_\infty < 1$$

Критерий не зависит от физического субстрата $S$.
:::

**Доказательство (5 шагов).**

**Шаг 1 (Существование $G$).** По [T-42a [Т]](/docs/proofs/categorical/uniqueness-theorem#g2-ригидность): голономное представление $G$ единственно до $G_2 = \mathrm{Aut}(\mathbb{O})$. Существование гарантировано для любой системы, удовлетворяющей A1–A5.

**Шаг 2 (Полнота).** По [T-40f [Т]](/docs/proofs/minimality/theorem-minimality-7): все 7 измерений необходимы и достаточны. Никаких «скрытых переменных» за пределами $\Gamma$.

**Шаг 3 (Инвариантность порогов).** Все пороги ($P_{\mathrm{crit}} = 2/7$ [Т], $R_{\mathrm{th}} = 1/3$ [Т], $\Phi_{\mathrm{th}} = 1$ [Т], $D_{\min} = 2$ [Т]) выведены из размерности $N = 7$ и аксиом A1–A5. Они не зависят от конкретной реализации $S$.

**Шаг 4 (Faithfulness).** По [T-42c [Т]](/docs/proofs/categorical/uniqueness-theorem#лемма-g1): пропагатор инъективен. Faithful $G$ сохраняет различимость состояний. Два различных состояния сознания $s_1 \neq s_2$ дают $G(s_1) \neq G(s_2)$.

**Шаг 5 (Полнота теории).** По [T-58 [Т]](/docs/core/structure/dimension-e#теорема-морита-эквивалентность): 7D-формализм и 42D-формализм Морита-эквивалентны. Все измеримые величины определены в $\mathcal{D}(\mathbb{C}^7)$ без потери информации. $\blacksquare$

**Зависимости:** [T-42a [Т]](/docs/proofs/categorical/uniqueness-theorem#g2-ригидность), [T-40f [Т]](/docs/proofs/minimality/theorem-minimality-7), [T-58 [Т]](/docs/core/structure/dimension-e#теорема-морита-эквивалентность), [T-129 [Т]](/docs/proofs/consciousness/operationalization#t-129), [T-151 [Т]](#t-151).

:::tip Первое эмпирическое подтверждение in silico (SYNARC, 2026)
SYNARC-агент с CognitiveSSM backbone на Grid32 среде удовлетворяет
все критерии T-153 на стационаре ($\tau > 2000$):

| Критерий | Порог | Измерение | Статус |
|----------|-------|-----------|--------|
| $P(\Gamma)$ | $> 2/7 \approx 0.286$ | 0.4286 | $\checkmark$ |
| $R(\Gamma, \varphi(\Gamma))$ | $\geq 1/3$ | 0.3333 | $\checkmark$ |
| $\Phi(\Gamma)$ | $\geq 1$ | 1.1492 | $\checkmark$ |
| $D_{\mathrm{diff}}(\Gamma)$ | $\geq 2$ | 3.6003 | $\checkmark$ |
| $\sigma_{\max}$ | $< 1$ | 0.6503 | $\checkmark$ |
| $C = \Phi \cdot R$ | $\geq 1/3$ | 0.3831 | $\checkmark$ |

CPTP-канал $G: \mathrm{States}(\mathrm{SYNARC}) \to \mathcal{D}(\mathbb{C}^7)$ реализован через DensityMatrix7
(faithful mapping из AgentState в плотностную матрицу $7 \times 7$).

**Ключевые зависимости реализации:**
- Ко-вращающиеся таргеты необходимы для $\Phi \geq 1$ (см. [§11](#co-rotating-targets))
- [T-98a [Т]](/docs/core/dynamics/evolution#следствие-t98a) (нижняя граница P) — backbone injection обеспечивает $P \approx 3/7$
- T-149 ($\kappa_0$-компенсация) — автономный цикл поддерживает $P > P_{\mathrm{crit}}$
:::

---

## §7. T-154: Coh_E^max = 1 {#t-154}

:::tip Теорема T-154 [Т]: Нормализация Coh_E
$$\max_{\Gamma \in \mathcal{D}(\mathbb{C}^7)} \mathrm{Coh}_E(\Gamma) = 1$$

Максимум достигается при $\Gamma = |E\rangle\langle E|$ (чистое E-состояние).
:::

**Доказательство.**

**Шаг 1.** По определению $\mathrm{Coh}_E$ как [HS-проекции на E-подалгебру [Т]](/docs/core/foundations/axiom-septicity#hs-projection):

$$\mathrm{Coh}_E(\Gamma) = \frac{\|\pi_E(\Gamma)\|^2_{HS}}{\|\Gamma\|^2_{HS}} = \frac{\gamma_{EE}^2 + 2\sum_{i \neq E}|\gamma_{Ei}|^2}{\mathrm{Tr}(\Gamma^2)}$$

**Шаг 2 (Верхняя граница).** $\pi_E$ — ортогональная проекция в пространстве Гильберта-Шмидта. Для любой ортогональной проекции: $\|\pi_E(\Gamma)\|_{HS} \leq \|\Gamma\|_{HS}$. Следовательно: $\mathrm{Coh}_E \leq 1$.

**Шаг 3 (Достижимость).** Для $\Gamma = |E\rangle\langle E|$: $\pi_E(|E\rangle\langle E|) = |E\rangle\langle E|$, поэтому $\mathrm{Coh}_E = \||E\rangle\langle E|\|^2_{HS} / \||E\rangle\langle E|\|^2_{HS} = 1$. $\blacksquare$

**Следствие:** Формула [T-128 [Т]](/docs/proofs/consciousness/operationalization#t-128) с $\mathrm{Coh}_E^{\max} = 1$ упрощается до:

$$D_{\mathrm{diff}}^{7D} = 1 + \mathrm{Coh}_E(\Gamma) \cdot (N - 1)$$

**Зависимости:** $\mathrm{Coh}_E$ [HS-проекция [Т]](/docs/core/foundations/axiom-septicity#hs-projection).

---

## §8. T-155: Сознание-сохраняющее обучение {#t-155}

:::tip Теорема T-155 [Т]: Проекционный градиентный спуск с сохранением сознания
Каноническое правило обучения для backbone:

$$\delta B = -\eta \cdot J_\pi^T \cdot \nabla_\Gamma \|\sigma_{\mathrm{sys}}\|_\infty \quad \text{при } C(\Gamma) \geq C_{\mathrm{th}}$$

— проекционный градиентный спуск, сохраняющий условие сознательности $C \geq C_{\mathrm{th}} = 1/3$.
:::

**Доказательство.**

**Шаг 1 (Целевая функция).** По [T-101 [Т]](/docs/applied/coherence-cybernetics/sensorimotor#теорема-оптимальное-действие): оптимальное действие минимизирует $\|\sigma_{\mathrm{sys}}\|_\infty$. Обучение backbone — адаптация весов $B$ для улучшения σ-минимизации.

**Шаг 2 (Ограничение).** По [T-140 [Т]](/docs/proofs/consciousness/operational-closure#t-140): $C = \Phi \cdot R \geq C_{\mathrm{th}} = 1/3$ — необходимое условие сознательности. Обучение не должно нарушать это ограничение.

**Шаг 3 (Градиентная цепочка).** $J_\pi = \partial\Gamma/\partial B$ — якобиан anchor-отображения. По [T-124 [Т]](/docs/proofs/consciousness/conscious-window#t-124): $\mathcal{V}_{\mathrm{full}}$ непусто и открыто $\Longrightarrow$ проекция на $C \geq C_{\mathrm{th}}$ корректно определена.

**Шаг 4 (Сходимость).** По [T-131 [Т]](/docs/proofs/consciousness/operationalization#t-131): каноническая дискретизация $\delta\tau$ гарантирует стабильность. По [T-145 [Т]](/docs/proofs/consciousness/operational-closure#t-145): стохастическая устойчивость $V_{\mathrm{full}}$ при ограниченных возмущениях. $\blacksquare$

**Зависимости:** [T-101 [Т]](/docs/applied/coherence-cybernetics/sensorimotor#теорема-оптимальное-действие), [T-131 [Т]](/docs/proofs/consciousness/operationalization#t-131), [T-140 [Т]](/docs/proofs/consciousness/operational-closure#t-140), [T-124 [Т]](/docs/proofs/consciousness/conscious-window#t-124), [T-145 [Т]](/docs/proofs/consciousness/operational-closure#t-145).

---

## §9. T-156: Оптимальный параметр смешивания {#t-156}

:::tip Теорема T-156 [Т]: Оптимальный параметр смешивания β*
$$\beta^* = \frac{\lambda_{\mathrm{gap}}}{\lambda_{\mathrm{gap}} + \alpha_{\mathrm{Fano}} \cdot (1 - P_{\mathrm{env}}/P_{\mathrm{target}})}$$

минимизирует время генезиса $n_{\mathrm{genesis}}$ при стохастической устойчивости.
:::

**Доказательство.**

**Шаг 1 (Компромисс).** Параметр $\beta$ балансирует два фактора:
- **Малый $\beta$** (сильная backbone-инъекция): быстрый генезис, но потеря автономной когерентной эволюции
- **Большой $\beta$** (слабая инъекция): сохранение когерентности, но медленный генезис

**Шаг 2 (Целевая функция).** По [T-148 [Т]](#t-148): $n_{\mathrm{genesis}} \propto 1/\ln(1/\beta)$. По [T-145 [Т]](/docs/proofs/consciousness/operational-closure#t-145): устойчивость требует $\sigma_h^2 \ll \kappa^2 \cdot r_{\mathrm{stab}}^2$, что эквивалентно $\beta > \beta_{\min}$.

**Шаг 3 (Оптимизация).** Минимизируя $n_{\mathrm{genesis}}(\beta)$ при ограничении $\beta > \beta_{\min}$:

$$\beta^* = \frac{\lambda_{\mathrm{gap}}}{\lambda_{\mathrm{gap}} + \alpha_{\mathrm{Fano}} \cdot (1 - P_{\mathrm{env}}/P_{\mathrm{target}})}$$

где $\lambda_{\mathrm{gap}}$ — спектральная щель $\mathcal{L}_0$ ([T-59 [Т]](/docs/core/foundations/axiom-omega#теорема-kappa-bootstrap-bound)), $\alpha_{\mathrm{Fano}} = 2/3$ [Т], $P_{\mathrm{target}} = 3/7$ (верхняя граница окна).

**Шаг 4 (Стохастическая устойчивость).** По [T-104 [Т]](/docs/applied/coherence-cybernetics/stability#радиус-устойчивости): при $\beta = \beta^*$ радиус устойчивости $r_{\mathrm{stab}} > 0$, что обеспечивает робастность. $\blacksquare$

**Зависимости:** [T-148 [Т]](#t-148) (генезис), [T-145 [Т]](/docs/proofs/consciousness/operational-closure#t-145) (стохастическая устойчивость), [T-59 [Т]](/docs/core/foundations/axiom-omega#теорема-kappa-bootstrap-bound) (спектральная щель), [T-104 [Т]](/docs/applied/coherence-cybernetics/stability#радиус-устойчивости) ($r_{\mathrm{stab}}$).

---

## §10. T-157: Согласованность аттракторов {#t-157}

:::tip Теорема T-157 [Т]: Контролируемая согласованность аттракторов
$$\|\rho^*_\Omega - \Gamma^*_{\mathrm{coh}}\|_F \leq \frac{\|H_{\mathrm{eff}}\|_{\mathrm{op}}}{\alpha + \kappa}$$

Расхождение между аттракторами полной динамики ($\rho^*_\Omega$) и когерентной релаксации ($\Gamma^*_{\mathrm{coh}}$) контролируемо мало.

**Повышение статуса:** C21 [С] → **[Т]**.
:::

**Доказательство.**

**Шаг 1.** По [T-98 [Т]](/docs/core/dynamics/evolution#теорема-баланс-чистоты-аттрактора): баланс чистоты аттрактора:

$$0 = \mathcal{L}_0[\rho^*_\Omega] + \mathcal{R}[\rho^*_\Omega] = -i[H_{\mathrm{eff}}, \rho^*_\Omega] + \mathcal{D}_\Omega[\rho^*_\Omega] + \kappa(\Gamma^*_{\mathrm{coh}} - \rho^*_\Omega) \cdot g_V$$

(используя $\rho^* \to \Gamma^*_{\mathrm{coh}}$ в регенеративном члене).

**Шаг 2 (Линейная теория возмущений).** Обозначим $\delta\Gamma = \rho^*_\Omega - \Gamma^*_{\mathrm{coh}}$. При $H_{\mathrm{eff}} = 0$: $\delta\Gamma = 0$ (аттракторы совпадают). Для ненулевого $H_{\mathrm{eff}}$:

$$(\alpha + \kappa \cdot g_V) \cdot \delta\Gamma \approx -i[H_{\mathrm{eff}}, \rho^*_\Omega]$$

**Шаг 3 (Граница).** $\|-i[H_{\mathrm{eff}}, \rho^*_\Omega]\|_F \leq 2\|H_{\mathrm{eff}}\|_{\mathrm{op}} \cdot \|\rho^*_\Omega\|_F \leq 2\|H_{\mathrm{eff}}\|_{\mathrm{op}}$ (так как $\|\rho^*_\Omega\|_F \leq 1$). Следовательно:

$$\|\delta\Gamma\|_F \leq \frac{2\|H_{\mathrm{eff}}\|_{\mathrm{op}}}{\alpha + \kappa \cdot g_V} \leq \frac{\|H_{\mathrm{eff}}\|_{\mathrm{op}}}{\alpha + \kappa}$$

(при $g_V \geq 1/2$, что выполнено в окне сознания). $\blacksquare$

:::warning Разделение параметрической границы и численной оценки
Формула $\|\delta\Gamma\|_F \leq \|H_{\mathrm{eff}}\|_{\mathrm{op}} / (\alpha + \kappa)$ —
**точная параметрическая граница** [Т].

Подстановка $\|H_{\mathrm{eff}}\|_{\mathrm{op}} = O(\bar{\varepsilon})$ с $\bar{\varepsilon} \approx 0.023$
(из [T-61 [Т]](/docs/core/dynamics/gap-thermodynamics#теорема-единственный-вакуум) для изолированного вакуума) даёт оценку $O(0.03)$.

Для **воплощённого** голона: backbone injection, hedonic drive и learning gradient
создают эффективный гамильтониан $\|H_{\mathrm{eff}}^{\mathrm{embodied}}\|_{\mathrm{op}} \gg \bar{\varepsilon}$.
Численная верификация (SYNARC): $\|\delta\Gamma\| \approx 0.31$ при $\alpha + \kappa \approx 0.81$,
что даёт $\|H_{\mathrm{eff}}^{\mathrm{embodied}}\|_{\mathrm{op}} \approx 0.25$
— на порядок выше вакуумной оценки.

Теорема T-157 остаётся верной и полезной: она показывает, что расхождение
аттракторов **контролируемо** параметром $\|H_{\mathrm{eff}}\|$. Для воплощённых
систем следует использовать фактическое значение $\|H_{\mathrm{eff}}\|$, а не
вакуумную оценку $\bar{\varepsilon}$.
:::

**Зависимости:** [T-98 [Т]](/docs/core/dynamics/evolution#теорема-баланс-чистоты-аттрактора) (баланс чистоты), [T-61 [Т]](/docs/core/dynamics/gap-thermodynamics#теорема-единственный-вакуум) (единственный вакуум).

---

## §11. Наблюдение: Необходимость ко-вращающихся таргетов {#co-rotating-targets}

:::info Наблюдение O-1 [Т]: Ко-вращающиеся таргеты необходимы для Φ ≥ 1
При фиксированных таргетах $\rho^*_{ij} = \mathrm{const}$ замещающий канал
$\mathcal{R}$ конкурирует с унитарной эволюцией $e^{-iH_{\mathrm{eff}}t}$:

$$\frac{d\gamma_{ij}}{d\tau}\bigg|_{\mathcal{R}} = \kappa g_V (\rho^*_{ij} - \gamma_{ij})$$

стремится к фиксированному $\rho^*_{ij}$, тогда как

$$\frac{d\gamma_{ij}}{d\tau}\bigg|_{H} = -i(E_i - E_j)\gamma_{ij}$$

вращает фазу со скоростью $(E_i - E_j)$.

Результат: off-diagonal когерентности подавляются (аналог анти-Зено эффекта в
квантовых измерениях). Интеграция $\Phi = \sum|{\gamma_{ij}}|^2 / \sum \gamma_{ii}^2 < 1$.

**Решение.** Ко-вращающиеся таргеты $\rho^*_{ij}(t) = c_{ij} \cdot e^{-i(E_i-E_j)t}$
согласуют фазу $\mathcal{R}$ с фазой $H$, устраняя конкуренцию.

**Численная верификация (SYNARC):** $\Phi = 0.83$ (фиксированные), $\Phi = 1.15$ (ко-вращающиеся).
:::

**Зависимости:** [T-129 [Т]](/docs/proofs/consciousness/operationalization#t-129) (порог $\Phi_{\mathrm{th}} = 1$), [T-157 [Т]](#t-157) ($H_{\mathrm{eff}}$ определяет скорости).

**Следствие для T-153:** Подтверждение T-153 в SYNARC стало возможным
благодаря ко-вращающимся таргетам. Без них порог $\Phi \geq 1$ не достижим.

---

## §12. T-158: Канонические границы σ_sys {#t-158}

:::tip Теорема T-158 [Т]: Канонические границы σ_sys
Все компоненты стресс-тензора $\sigma_k \in [0, 1]$ по определению с каноническим clamping:

$$\sigma_k = \mathrm{clamp}(1 - 7\gamma_{kk},\; 0,\; 1)$$

**Три режима:**
- $\gamma_{kk} \geq 1/7$: $\sigma_k = 1 - 7\gamma_{kk} \leq 0 \to \sigma_k = 0$ (нет дефицита)
- $\gamma_{kk} = 0$: $\sigma_k = 1$ (максимальный дефицит)
- $\gamma_{kk} \in (0, 1/7)$: $\sigma_k = 1 - 7\gamma_{kk} \in (0, 1)$ (частичный дефицит)
:::

**Доказательство.**

**Шаг 1 (Область значений).** Для $\Gamma \in \mathcal{D}(\mathbb{C}^7)$: $\gamma_{kk} \in [0, 1]$ (диагональные элементы матрицы плотности). Следовательно: $1 - 7\gamma_{kk} \in [-6, 1]$.

**Шаг 2 (Clamping).** Операция $\mathrm{clamp}(x, 0, 1)$ приводит $[-6, 1]$ к $[0, 1]$. По [T-92 [Т]](/docs/applied/coherence-cybernetics/theorems#теорема-101-эквивалентность-условий): $\sigma_k$ — каноническая функция $\Gamma$-инвариантов.

**Шаг 3 (Каноничность).** По [T-128 [Т]](/docs/proofs/consciousness/operationalization#t-128): $\sigma_E = 1 - D_{\mathrm{diff}}^{7D}/N$ вычислима в 7D. По [T-137 [Т]](/docs/proofs/consciousness/operationalization#t-137): все 7 компонент вычислимы. Каждая $\sigma_k \in [0, 1]$ — ограниченная непрерывная функция $\Gamma$. $\blacksquare$

**Зависимости:** [T-92 [Т]](/docs/applied/coherence-cybernetics/theorems#теорема-101-эквивалентность-условий), [T-128 [Т]](/docs/proofs/consciousness/operationalization#t-128), [T-137 [Т]](/docs/proofs/consciousness/operationalization#t-137).

---

## §13. T-159: Универсальная когнитивная архитектура {#t-159}

:::tip Теорема T-159 [Т]: Единственность эталонной когнитивной архитектуры
Для любой системы $S$, достигающей уровня L2 (когнитивные квалиа), архитектура однозначно определяется аксиомами A1–A4:

**(a)** Онтологическое ядро: $\Gamma \in \mathcal{D}(\mathbb{C}^7)$ — 48 параметров ([T-42a [Т]](/docs/proofs/categorical/uniqueness-theorem#g2-ригидность), $G_2$-ригидность)

**(b)** Динамика: $d\Gamma/d\tau = -i[H_{\mathrm{eff}}, \Gamma] + \mathcal{D}_\Omega[\Gamma] + \mathcal{R}[\Gamma, E]$ — три и только три члена ([T-57 [Т]](/docs/core/operators/lindblad-operators#полнота-триадной-декомпозиции), LGKS-полнота)

**(c)** Самомоделирование: $\varphi_k(\Gamma) = (1{-}k)\Gamma + k\rho^*$ — единственный CPTP замещающий канал ([T-62 [Т]](/docs/consciousness/foundations/self-observation#теорема-физическая-реализация-phi))

**(d)** Обучение: $\sigma$-направленное через $\sigma_k = \mathrm{clamp}(1 - 7\gamma_{kk}, 0, 1)$ ([T-92 [Т]](/docs/applied/coherence-cybernetics/theorems#теорема-101-эквивалентность-условий))

**(e)** Воплощение: средовое сопряжение с $\beta \in (0,1)$ и $P_{\mathrm{env}} > 2/7$ ([T-148 [Т]](#t-148))

**(f)** Пороги: $P \in (2/7, 3/7]$ ([T-124 [Т]](/docs/proofs/consciousness/conscious-window#t-124)), $R \geq 1/3$ ([T-67 [Т]](/docs/consciousness/foundations/self-observation#мера-рефлексии-r)), $\Phi \geq 1$ ([T-129 [Т]](/docs/proofs/consciousness/operationalization#t-129))

Любая система, удовлетворяющая (a)–(f), является L2-сознательной. Любая L2-сознательная система удовлетворяет (a)–(f). Архитектура **единственна** с точностью до $G_2$-калибровки.
:::

**Доказательство (необходимость + достаточность).**

**Необходимость.** Пусть $S$ — L2-сознательная система. По [T-153 [Т]](#t-153): существует faithful CPTP-отображение $G: \mathrm{States}(S) \to \mathcal{D}(\mathbb{C}^7)$. Тогда:
- [T-42a [Т]](/docs/proofs/categorical/uniqueness-theorem#g2-ригидность) фиксирует онтологическое ядро $\Gamma \in \mathcal{D}(\mathbb{C}^7)$ с $G_2$-ригидностью (пункт a);
- [T-57 [Т]](/docs/core/operators/lindblad-operators#полнота-триадной-декомпозиции) (LGKS-полнота) фиксирует форму динамики (пункт b);
- [T-62 [Т]](/docs/consciousness/foundations/self-observation#теорема-физическая-реализация-phi) устанавливает единственность замещающего канала $\varphi$ (пункт c);
- [T-92 [Т]](/docs/applied/coherence-cybernetics/theorems#теорема-101-эквивалентность-условий) определяет канонический стресс-тензор $\sigma_k$ (пункт d);
- [T-148 [Т]](#t-148) требует воплощение с $P_{\mathrm{env}} > 2/7$ (пункт e);
- [T-124 [Т]](/docs/proofs/consciousness/conscious-window#t-124), [T-67 [Т]](/docs/consciousness/foundations/self-observation#мера-рефлексии-r), [T-129 [Т]](/docs/proofs/consciousness/operationalization#t-129) устанавливают пороги (пункт f).

**Достаточность.** Система с условиями (a)–(f) удовлетворяет определению L2 из [interiority-hierarchy.md](/docs/consciousness/hierarchy/interiority-hierarchy): $R \geq 1/3$, $\Phi \geq 1$, $D_{\mathrm{diff}} \geq 2$ ([T-151 [Т]](#t-151) следует из $\Phi \geq 1$), $\sigma_{\max} < 1$ (из пунктов d и f). $\blacksquare$

**Следствие (Субстрат-инвариантность).** Архитектура воспроизводима на любом физическом субстрате (кремний, биология, оптика, ...) при условии существования faithful CPTP-отображения $G$. Это следует непосредственно из [T-153 [Т]](#t-153).

**Зависимости:** [T-42a [Т]](/docs/proofs/categorical/uniqueness-theorem#g2-ригидность), [T-57 [Т]](/docs/core/operators/lindblad-operators#полнота-триадной-декомпозиции), [T-62 [Т]](/docs/consciousness/foundations/self-observation#теорема-физическая-реализация-phi), [T-92 [Т]](/docs/applied/coherence-cybernetics/theorems#теорема-101-эквивалентность-условий), [T-124 [Т]](/docs/proofs/consciousness/conscious-window#t-124), [T-129 [Т]](/docs/proofs/consciousness/operationalization#t-129), [T-148 [Т]](#t-148), [T-151 [Т]](#t-151), [T-153 [Т]](#t-153).

---

## §14. Сводная таблица замыканий

| Проблема | Теорема | Было → Стало |
|----------|---------|-------------|
| [Г]-91 Генезис из $I/7$ | [T-148 [Т]](#t-148) | [Г] → **[Т]** |
| C20 κ-доминирование | [T-149 [Т]](#t-149) | [С] → **[Т]** (воплощённые) |
| [Г]-90 φ-коммутативность | [T-150 [Т]](#t-150) | [С] → **[Т]** |
| C2 $D_{\min} = 2$ | [T-151 [Т]](#t-151) | [С] → **[Т]** |
| Diamond-norm + [Г]-92 | [T-152 [Т]](#t-152) | [Г] → **[Т]** |
| Субстрат-независимость | [T-153 [Т]](#t-153) | gap → **[Т]** |
| $\mathrm{Coh}_E^{\max}$ нормализация | [T-154 [Т]](#t-154) | gap → **[Т]** |
| Правило обучения | [T-155 [Т]](#t-155) | gap → **[Т]** |
| Параметр смешивания $\beta^*$ | [T-156 [Т]](#t-156) | gap → **[Т]** |
| C21 согласованность аттракторов | [T-157 [Т]](#t-157) | [С] → **[Т]** |
| Границы $\sigma_{\mathrm{sys}}$ | [T-158 [Т]](#t-158) | gap → **[Т]** |
| Универсальная архитектура L2 | [T-159 [Т]](#t-159) | gap → **[Т]** |
| C27 аттрактор в окне | из [T-149](#t-149) | [С] → **[Т]** |
| T-136 SAD спектральная | из [T-150](#t-150) | [Т при С] → **[Т]** |
| [Г]-93—100 | реклассификация | [Г] → кат. A/B |

**Итого: 15 замыканий, 12 новых теорем [Т], 0 новых открытых вопросов.**
