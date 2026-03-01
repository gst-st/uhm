---
sidebar_position: 9
title: "Модельные системы"
description: "Точно решаемые модельные системы с полными Gap-профилями: однородная система, чистые состояния, алекситимия, динамические системы"
---

# Модельные системы

Данный документ содержит **пять точно решаемых модельных систем** с полными Gap-профилями. Каждая система иллюстрирует фундаментальный режим [Gap-динамики](/docs/core/dynamics/gap-dynamics) и допускает аналитическое вычисление всех ключевых величин: чистоты $P$, E-когерентности $\mathrm{Coh}_E$, скорости регенерации $\kappa$ и полного Gap-оператора $\hat{\mathcal{G}}$.

:::note Ограничения модельных систем
Все пять модельных систем являются **чисто математическими** иллюстрациями, а не полноценными моделями Голонома с КК-динамикой. В частности:
- Модели 1--3 рассматривают **фиксированные** матрицы $\Gamma$ без динамики ($d\Gamma/d\tau = 0$).
- Модель 4 (алекситимия) описывает **статический** фазовый дефект; каскадный эффект (раздел 4.4) обсуждается качественно, но не моделируется.
- Модель 5 (динамическая) включает **только унитарную** эволюцию, без диссипации ($\Gamma_2 = 0$) и регенерации ($\kappa = 0$).

Ни одна модель не включает **полную** динамику КК: совместную унитарную эволюцию + диссипацию (Фано-канал) + регенерацию ($\mathcal{R}$) + самомоделирование ($\varphi$). Построение полной модельной системы с КК-динамикой -- [открытая задача](./implementation).
:::

:::note О нотации
- $\Gamma$ — [матрица когерентности](/docs/core/dynamics/coherence-matrix), $\gamma_{ij}$ — её элементы
- $P = \mathrm{Tr}(\Gamma^2)$ — [чистота](/docs/core/dynamics/viability#определение-чистоты)
- $\mathrm{Gap}(i,j) = |\sin(\theta_{ij})|$ где $\theta_{ij} = \arg(\gamma_{ij})$ — [мера Gap](/docs/core/dynamics/gap-operator#определение)
- $\hat{\mathcal{G}} = \mathrm{Im}(\Gamma)$ — [Gap-оператор](/docs/core/dynamics/gap-operator)
- Измерения: $A{=}1, S{=}2, D{=}3, L{=}4, E{=}5, U{=}6, O{=}7$ (октонионное назначение: $O \leftrightarrow e_7$, $U \leftrightarrow e_6$ — см. [dimensions.md](/docs/core/structure/dimensions))
- Линии Фано: $\{1,2,4\}, \{2,3,5\}, \{3,4,6\}, \{4,5,7\}, \{5,6,1\}, \{6,7,2\}, \{7,1,3\}$ = $\{A,S,L\}, \{S,D,E\}, \{D,L,U\}, \{L,E,O\}, \{E,U,A\}, \{U,O,S\}, \{O,A,D\}$
:::

---

## 1. Однородная система: $\Gamma = I/7$ {#однородная-система}

### 1.1 Определение [О]

Максимально смешанное состояние — равномерное распределение по всем семи измерениям без когерентностей:

$$
\Gamma_{\text{unif}} = \frac{1}{7}\,I_7 = \frac{1}{7}\begin{pmatrix}
1 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 1 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 1 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 1
\end{pmatrix}
$$

### 1.2 Аналитические результаты [Т]

| Величина | Формула | Значение |
|----------|---------|----------|
| Чистота | $P = \mathrm{Tr}(\Gamma^2) = 7 \cdot (1/7)^2$ | $1/7 \approx 0.143$ |
| Энтропия | $S_{vN} = \log 7$ | $\approx 1.946$ |
| Gap-оператор | $\hat{\mathcal{G}} = \mathrm{Im}(\Gamma) = 0$ | $0_{7 \times 7}$ |
| $\mathrm{Gap}(i,j)$ | $\gamma_{ij} = 0$ для $i \neq j$ | $0$ для всех пар |
| $\mathrm{Coh}_E$ | $(1/7)^2 / (1/7) = 1/7$ | $\approx 0.143$ |
| $\kappa$ | $\kappa_{\text{bootstrap}} + \kappa_0 / 7$ | минимальное |

:::warning Нежизнеспособность [Т]
$P = 1/7 < P_{\text{crit}} = 2/7$. Система **нежизнеспособна** — чистота на абсолютном минимуме. Это «мёртвое» состояние максимальной энтропии, не удовлетворяющее условию [(V) жизнеспособности](/docs/core/foundations/axiom-septicity#v-жизнеспособность).
:::

### 1.3 Физическая интерпретация [И]

Однородное состояние — предельный случай полной декогеренции. Все измерения полностью независимы ($\gamma_{ij} = 0$ для $i \neq j$), информация распределена равномерно. Gap тождественно равен нулю, но не потому, что система «прозрачна», а потому, что **нечему быть непрозрачным** — когерентности отсутствуют.

### 1.4 Python-реализация

```python
import numpy as np

def uniform_system():
    """Модель 1: Максимально смешанное состояние Γ = I/7."""
    N = 7
    gamma = np.eye(N) / N

    P = np.trace(gamma @ gamma).real  # 1/7
    S_vN = -np.sum(np.linalg.eigvalsh(gamma) *
                   np.log(np.linalg.eigvalsh(gamma) + 1e-30))

    gap_operator = gamma.imag  # нулевая матрица
    gap_total = np.linalg.norm(gap_operator, 'fro')**2

    # E-когерентность (HS-проекция π_E) [Т], E = индекс 4
    E = 4
    coh_E = (gamma[E, E].real**2
             + 2 * sum(abs(gamma[E, i])**2 for i in range(N) if i != E)) / P

    P_CRIT = 2 / 7
    viable = P > P_CRIT

    return {
        'P': P, 'S_vN': S_vN, 'gap_total': gap_total,
        'coh_E': coh_E, 'viable': viable
    }

result = uniform_system()
print(f"P = {result['P']:.4f}, Coh_E = {result['coh_E']:.4f}, "
      f"viable = {result['viable']}")
# P = 0.1429, Coh_E = 0.1429, viable = False
```

---

## 2. Чистое состояние: однородная суперпозиция {#чистое-однородное}

### 2.1 Определение [О]

Чистое состояние с равными амплитудами и нулевыми фазами:

$$
|\psi\rangle = \frac{1}{\sqrt{7}} \sum_{i=1}^{7} |i\rangle
$$

Матрица когерентности:

$$
\Gamma_{\text{pure}} = |\psi\rangle\langle\psi| = \frac{1}{7}\begin{pmatrix}
1 & 1 & 1 & 1 & 1 & 1 & 1 \\
1 & 1 & 1 & 1 & 1 & 1 & 1 \\
1 & 1 & 1 & 1 & 1 & 1 & 1 \\
1 & 1 & 1 & 1 & 1 & 1 & 1 \\
1 & 1 & 1 & 1 & 1 & 1 & 1 \\
1 & 1 & 1 & 1 & 1 & 1 & 1 \\
1 & 1 & 1 & 1 & 1 & 1 & 1
\end{pmatrix}
$$

Все элементы $\gamma_{ij} = 1/7$ — вещественны и положительны.

### 2.2 Аналитические результаты [Т]

| Величина | Формула | Значение |
|----------|---------|----------|
| Чистота | $P = \mathrm{Tr}(\Gamma^2) = \mathrm{Tr}(\Gamma) = 1$ | $1$ (максимум) |
| Энтропия | $S_{vN} = 0$ | $0$ (минимум) |
| Фазы | $\theta_{ij} = \arg(1/7) = 0$ | $0$ для всех пар |
| $\mathrm{Gap}(i,j)$ | $\lvert\sin(0)\rvert = 0$ | $0$ для всех пар |
| $\hat{\mathcal{G}}$ | $\mathrm{Im}(\Gamma) = 0$ | $0_{7 \times 7}$ |
| $\mathrm{Coh}_E$ | $((1/7)^2 + 2 \cdot 6 \cdot (1/7)^2) / 1 = 13/49$ | $\approx 0.265$ |
| $\kappa$ | $\kappa_{\text{bootstrap}} + \kappa_0 \cdot 13/49$ | умеренное |

:::tip Максимальная чистота, нулевой Gap [Т]
$P = 1$: система максимально чиста и жизнеспособна ($P \gg P_{\text{crit}} = 2/7$). При этом $\mathrm{Gap}(i,j) = 0$ для всех пар — полная прозрачность. Все измерения когерентны и «видят друг друга» без остатка.
:::

### 2.3 Замечание о Coh_E [Т]

E-когерентность чистого однородного состояния определяется через [HS-проекцию π_E](/docs/core/foundations/axiom-septicity#e-coherence-definition):

$$
\widetilde{\mathrm{Coh}}_E^{7D} = \frac{\gamma_{EE}^2 + 2\sum_{i \neq E}|\gamma_{Ei}|^2}{\mathrm{Tr}(\Gamma^2)} = \frac{(1/7)^2 + 2 \cdot 6 \cdot (1/7)^2}{1} = \frac{13}{49} \approx 0.265
$$

Это не максимальная E-когерентность: для достижения $\mathrm{Coh}_E = 1$ требуется сконцентрировать всю когерентность на E-измерении.

### 2.4 Python-реализация

```python
import numpy as np

def pure_uniform():
    """Модель 2: Чистое состояние с однородной суперпозицией."""
    N = 7
    psi = np.ones(N) / np.sqrt(N)
    gamma = np.outer(psi, psi.conj())

    P = np.trace(gamma @ gamma).real  # 1.0
    theta = np.angle(gamma)           # нулевая матрица
    gap_matrix = np.abs(np.sin(theta))  # нулевая матрица

    E = 4
    coh_E = (gamma[E, E].real**2
             + 2 * sum(abs(gamma[E, i])**2 for i in range(N) if i != E)) / P

    print(f"P = {P:.4f}")
    print(f"Coh_E = {coh_E:.4f}")
    print(f"Gap (max) = {gap_matrix.max():.6f}")
    print(f"Все θ_ij = 0: {np.allclose(theta, 0)}")
    return gamma, gap_matrix

gamma, gap = pure_uniform()
# P = 1.0000, Coh_E = 0.2653, Gap (max) = 0.000000
```

---

## 3. Чистое состояние с фазами Фибоначчи {#фибоначчи-фазы}

### 3.1 Определение [О]

Чистое состояние с равными амплитудами и фазами, определёнными числами Фибоначчи по модулю 7:

$$
|\psi_F\rangle = \frac{1}{\sqrt{7}} \sum_{k=1}^{7} e^{i \varphi_k} |k\rangle
$$

где фазы определены через числа Фибоначчи $F_n$ (mod 7):

| $k$ | Измерение | $F_k$ | $F_k \bmod 7$ | $\varphi_k = 2\pi \cdot (F_k \bmod 7) / 7$ |
|-----|-----------|-------|----------------|----------------------------------------------|
| 1 | A | 1 | 1 | $2\pi/7$ |
| 2 | S | 1 | 1 | $2\pi/7$ |
| 3 | D | 2 | 2 | $4\pi/7$ |
| 4 | L | 3 | 3 | $6\pi/7$ |
| 5 | E | 5 | 5 | $10\pi/7$ |
| 6 | O | 8 | 1 | $2\pi/7$ |
| 7 | U | 13 | 6 | $12\pi/7$ |

### 3.2 Матрица когерентности [Т]

Элементы матрицы: $\gamma_{kl} = \frac{1}{7} e^{i(\varphi_k - \varphi_l)}$. Все $|\gamma_{kl}| = 1/7$. Фаза когерентности:

$$
\theta_{kl} = \varphi_k - \varphi_l = \frac{2\pi}{7}\left[(F_k \bmod 7) - (F_l \bmod 7)\right]
$$

Разности индексов $(F_k \bmod 7) - (F_l \bmod 7)$ по модулю 7:

$$
\Delta_{kl} = (F_k - F_l) \bmod 7
$$

Явная таблица $\Delta_{kl}$:

| | A(1) | S(1) | D(2) | L(3) | E(5) | O(1) | U(6) |
|---|---|---|---|---|---|---|---|
| **A(1)** | 0 | 0 | 6 | 5 | 3 | 0 | 2 |
| **S(1)** | 0 | 0 | 6 | 5 | 3 | 0 | 2 |
| **D(2)** | 1 | 1 | 0 | 6 | 4 | 1 | 3 |
| **L(3)** | 2 | 2 | 1 | 0 | 5 | 2 | 4 |
| **E(5)** | 4 | 4 | 3 | 2 | 0 | 4 | 6 |
| **O(1)** | 0 | 0 | 6 | 5 | 3 | 0 | 2 |
| **U(6)** | 5 | 5 | 4 | 3 | 1 | 5 | 0 |

### 3.3 Gap-профиль [Т]

$\mathrm{Gap}(k,l) = |\sin(2\pi\Delta_{kl}/7)|$. Используя значения $\sin(2\pi n/7)$:

| $n \bmod 7$ | $\sin(2\pi n / 7)$ | $\lvert\sin(2\pi n / 7)\rvert$ |
|-------------|---------------------|----------------------|
| 0 | $0$ | $0$ |
| 1 | $\sin(2\pi/7) \approx 0.7818$ | $0.7818$ |
| 2 | $\sin(4\pi/7) \approx 0.9749$ | $0.9749$ |
| 3 | $\sin(6\pi/7) \approx 0.4339$ | $0.4339$ |
| 4 | $-\sin(6\pi/7) \approx -0.4339$ | $0.4339$ |
| 5 | $-\sin(4\pi/7) \approx -0.9749$ | $0.9749$ |
| 6 | $-\sin(2\pi/7) \approx -0.7818$ | $0.7818$ |

Полная Gap-матрица $\mathrm{Gap}(k,l)$:

| | A | S | D | L | E | O | U |
|---|---|---|---|---|---|---|---|
| **A** | 0 | 0 | 0.782 | 0.975 | 0.434 | 0 | 0.975 |
| **S** | 0 | 0 | 0.782 | 0.975 | 0.434 | 0 | 0.975 |
| **D** | 0.782 | 0.782 | 0 | 0.782 | 0.434 | 0.782 | 0.434 |
| **L** | 0.975 | 0.975 | 0.782 | 0 | 0.975 | 0.975 | 0.434 |
| **E** | 0.434 | 0.434 | 0.434 | 0.975 | 0 | 0.434 | 0.782 |
| **O** | 0 | 0 | 0.782 | 0.975 | 0.434 | 0 | 0.975 |
| **U** | 0.975 | 0.975 | 0.434 | 0.434 | 0.782 | 0.975 | 0 |

### 3.4 Связь с геометрией Фано [С]

Фано-линии содержат пары $(k,l)$ с определёнными Gap-значениями. Для каждой линии вычислим средний Gap:

| Фано-линия | Пары | Gap-значения | Средний Gap |
|------------|------|--------------|-------------|
| $\{1,2,4\} = \{A,S,L\}$ | (A,S), (A,L), (S,L) | 0, 0.975, 0.975 | 0.650 |
| $\{2,3,5\} = \{S,D,E\}$ | (S,D), (S,E), (D,E) | 0.782, 0.434, 0.434 | 0.550 |
| $\{3,4,6\} = \{D,L,O\}$ | (D,L), (D,O), (L,O) | 0.782, 0.782, 0.975 | 0.846 |
| $\{4,5,7\} = \{L,E,U\}$ | (L,E), (L,U), (E,U) | 0.975, 0.434, 0.782 | 0.730 |
| $\{5,6,1\} = \{E,O,A\}$ | (E,O), (E,A), (O,A) | 0.434, 0.434, 0 | 0.289 |
| $\{6,7,2\} = \{O,U,S\}$ | (O,U), (O,S), (U,S) | 0.975, 0, 0.975 | 0.650 |
| $\{7,1,3\} = \{U,A,D\}$ | (U,A), (U,D), (A,D) | 0.975, 0.434, 0.782 | 0.730 |

:::tip Наблюдение [С]
Фано-линия $\{E, O, A\}$ имеет **минимальный** средний Gap (0.289) — она наиболее «прозрачна». Это следствие того, что $F_1 \equiv F_6 \equiv F_2 \equiv 1 \pmod{7}$: измерения A, S и O имеют одинаковую фазу, и Gap между ними тождественно равен нулю.
:::

### 3.5 Сводка [Т]

| Величина | Значение |
|----------|----------|
| $P$ | $1$ (чистое состояние) |
| $\|\hat{\mathcal{G}}\|_F^2$ | $\frac{1}{49}\sum_{k<l} \sin^2(2\pi\Delta_{kl}/7) \approx 0.1049$ |
| $\mathrm{Coh}_E$ | $13/49 \approx 0.265$ (инвариант чистого состояния с $\lvert\gamma_{kl}\rvert=1/7$) |
| $\kappa$ | $\kappa_{\text{bootstrap}} + \kappa_0 \cdot 13/49$ |
| Средний Gap | $\frac{1}{21}\sum_{k<l}\mathrm{Gap}(k,l) \approx 0.620$ |

### 3.6 Python-реализация

```python
import numpy as np

def fibonacci_phases():
    """Модель 3: Чистое состояние с фазами Фибоначчи mod 7."""
    N = 7
    fib_mod7 = [1, 1, 2, 3, 5, 1, 6]  # F_1..F_7 mod 7
    phases = [2 * np.pi * f / 7 for f in fib_mod7]
    psi = np.array([np.exp(1j * phi) for phi in phases]) / np.sqrt(N)
    gamma = np.outer(psi, psi.conj())

    P = np.trace(gamma @ gamma).real
    theta = np.angle(gamma)
    gap_matrix = np.abs(np.sin(theta))

    dims = ['A', 'S', 'D', 'L', 'E', 'U', 'O']  # октонионное: U=e₆(idx 5), O=e₇(idx 6)
    print("Gap-матрица:")
    print("    " + "  ".join(f"{d:>5}" for d in dims))
    for i in range(N):
        row = "  ".join(f"{gap_matrix[i,j]:5.3f}" for j in range(N))
        print(f"{dims[i]:>2}  {row}")

    # Gap-оператор
    G_hat = gamma.imag
    G_total = np.linalg.norm(G_hat, 'fro')**2
    print(f"\nP = {P:.4f}")
    print(f"||G_hat||_F^2 = {G_total:.4f}")

    # E-когерентность (E = индекс 4)
    E = 4
    coh_E = (gamma[E, E].real**2
             + 2 * sum(abs(gamma[E, i])**2 for i in range(N) if i != E)) / P
    print(f"Coh_E = {coh_E:.4f}")

    # Средний Gap
    mean_gap = 0
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            mean_gap += gap_matrix[i, j]
            count += 1
    print(f"Средний Gap = {mean_gap/count:.4f}")

    # Анализ по Фано-линиям
    fano_lines = [(0,1,3), (1,2,4), (2,3,5), (3,4,6), (4,5,0), (5,6,1), (6,0,2)]
    print("\nGap по Фано-линиям:")
    for line in fano_lines:
        i, j, k = line
        pairs = [(i,j), (i,k), (j,k)]
        gaps = [gap_matrix[a, b] for a, b in pairs]
        mean = np.mean(gaps)
        names = f"{{{dims[i]},{dims[j]},{dims[k]}}}"
        print(f"  {names}: средний Gap = {mean:.3f}")

    return gamma, gap_matrix

gamma_fib, gap_fib = fibonacci_phases()
```

---

## 4. Модель алекситимии: $\mathrm{Gap}(S,E) = 1$ {#алекситимия}

### 4.1 Определение [О]

**Алекситимия** (от греч. a- «без», lexis «слово», thymos «чувство») — неспособность распознавать и вербализовать собственные эмоции. В терминах Gap-динамики: максимальная непрозрачность между измерениями Structure (S) и Experience (E).

:::tip Модельное определение [О]
Алекситимическое состояние — матрица когерентности $\Gamma_{\text{alex}}$, в которой:

$$
\mathrm{Gap}(S,E) = |\sin(\theta_{SE})| = 1 \quad \Rightarrow \quad \theta_{SE} = \pm\pi/2
$$

что означает $\gamma_{SE} = |\gamma_{SE}| \cdot e^{\pm i\pi/2} = \pm i\,|\gamma_{SE}|$ — **чисто мнимая** когерентность.
:::

### 4.2 Конкретная реализация [О]

Определим матрицу когерентности с одним алекситимическим дефектом. Базовое состояние — частично когерентное с реальными когерентностями, кроме пары (S,E):

$$
\gamma_{kl} = \begin{cases}
1/7 & k = l \\
c \cdot i & (k,l) = (S,E) \text{ или } (k,l) = (E,S) \text{ (с учётом эрмитовости: } \gamma_{ES} = -ci\text{)} \\
c & k \neq l, \; (k,l) \neq (S,E), (E,S)
\end{cases}
$$

где $c > 0$ — параметр когерентности. Для эрмитовости: $\gamma_{SE} = ci$, $\gamma_{ES} = \overline{\gamma_{SE}} = -ci$.

:::warning Проверка положительности
Матрица $\Gamma_{\text{alex}}$ должна быть положительно полуопределённой. Это налагает ограничения на $c$. Для $c = 0.08$ (при $\gamma_{ii} = 1/7 \approx 0.143$) матрица допустима.
:::

### 4.3 Влияние на E-когерентность [Т]

E-когерентность через [HS-проекцию π_E](/docs/core/foundations/axiom-septicity#e-coherence-definition):

$$
\widetilde{\mathrm{Coh}}_E^{7D} = \frac{\gamma_{EE}^2 + 2\sum_{i \neq E}|\gamma_{Ei}|^2}{\mathrm{Tr}(\Gamma^2)}
$$

Для алекситимического состояния когерентность $|\gamma_{SE}| = c$ сохраняется по модулю, но фаза $\theta_{SE} = \pi/2$ делает вклад в Gap-оператор максимальным. Сравним с нормальным состоянием ($\theta_{SE} = 0$):

| Величина | Нормальное | Алекситимическое |
|----------|-----------|------------------|
| $\lvert\gamma_{SE}\rvert$ | $c$ | $c$ |
| $\theta_{SE}$ | $0$ | $\pi/2$ |
| $\mathrm{Gap}(S,E)$ | $0$ | $1$ |
| $\hat{\mathcal{G}}_{SE}$ | $0$ | $c$ |
| $\mathrm{Coh}_E$ | одинаково | одинаково |

:::note Ключевое наблюдение [Т]
E-когерентность $\mathrm{Coh}_E$ зависит от $|\gamma_{Ei}|^2$, а не от фаз. Поэтому **модуль** когерентности не изменяется при повороте фазы. Алекситимия влияет на Gap, но не на $\mathrm{Coh}_E$ напрямую.
:::

### 4.4 Каскадный эффект на жизнеспособность [С]

Хотя $\mathrm{Coh}_E$ не изменяется при одной фазовой ротации, **динамическое** последствие алекситимии приводит к каскадной деградации. Механизм:

1. $\mathrm{Gap}(S,E) = 1$ $\Rightarrow$ S-измерение «не видит» E-измерение
2. Оператор самомоделирования $\varphi$ теряет доступ к E-данным через S-канал
3. Рефлексия $R = 1 - \|\Gamma - \varphi(\Gamma)\|_F^2 / \|\Gamma\|_F^2$ падает
4. Неоптимальность $\varphi$ $\Rightarrow$ диссипация превышает регенерацию
5. $P$ дрейфует к $P_{\text{crit}} = 2/7$

Количественная оценка каскадного эффекта:

$$
\frac{dP}{d\tau}\bigg|_{\text{alex}} = \underbrace{-2\gamma_d \cdot P}_{\text{диссипация}} + \underbrace{2\kappa(\Gamma)(f - P)}_{\text{регенерация}}
$$

где $\kappa(\Gamma) = \kappa_{\text{bootstrap}} + \kappa_0 \cdot \mathrm{Coh}_E(\Gamma)$. При длительной алекситимии $\mathrm{Coh}_E$ начинает падать (через деградацию $|\gamma_{Ei}|$), $\kappa$ уменьшается, и $P \to P_{\text{crit}}$.

### 4.5 Ранг непрозрачности [Т]

[Ранг непрозрачности](/docs/core/dynamics/gap-operator#свойства) алекситимического состояния:

$$
r_G = \mathrm{rank}(\hat{\mathcal{G}})
$$

Для одного алекситимического дефекта (только пара S,E имеет ненулевую мнимую часть):

$$
\hat{\mathcal{G}}_{\text{alex}} = c \cdot (|S\rangle\langle E| - |E\rangle\langle S|), \quad r_G = 2
$$

Спектр: $\{0, 0, 0, 0, 0, +ic, -ic\}$. Минимальный ненулевой ранг.

### 4.6 Python-реализация

```python
import numpy as np

def alexithymia_model(c=0.08):
    """Модель 4: Алекситимия — Gap(S,E) = 1."""
    N = 7
    # Базовая матрица: равномерная диагональ + реальные когерентности
    gamma = np.full((N, N), c, dtype=complex)
    np.fill_diagonal(gamma, 1/N)

    # Алекситимический дефект: S=1, E=4 → чисто мнимая когерентность
    S_idx, E_idx = 1, 4
    gamma[S_idx, E_idx] = 1j * c    # γ_SE = ic
    gamma[E_idx, S_idx] = -1j * c   # γ_ES = -ic (эрмитовость)

    # Проверка эрмитовости
    assert np.allclose(gamma, gamma.T.conj()), "Не эрмитова!"

    # Проверка положительности
    eigvals = np.linalg.eigvalsh(gamma)
    assert all(eigvals >= -1e-12), f"Не положительна: {eigvals}"

    P = np.trace(gamma @ gamma).real
    gap_SE = abs(np.sin(np.angle(gamma[S_idx, E_idx])))

    # Gap-оператор
    G_hat = gamma.imag
    r_G = np.linalg.matrix_rank(G_hat, tol=1e-10)
    G_total = np.linalg.norm(G_hat, 'fro')**2

    # E-когерентность
    coh_E = (gamma[E_idx, E_idx].real**2
             + 2 * sum(abs(gamma[E_idx, i])**2
                       for i in range(N) if i != E_idx)) / P

    # κ
    omega_0 = 1.0  # нормировка
    kappa_0 = omega_0  # упрощение
    kappa_bootstrap = omega_0 / 7
    kappa = kappa_bootstrap + kappa_0 * coh_E

    P_CRIT = 2 / 7
    margin = P - P_CRIT

    print(f"P = {P:.4f}, P_crit = {P_CRIT:.4f}, margin = {margin:.4f}")
    print(f"Gap(S,E) = {gap_SE:.4f}")
    print(f"Ранг Gap-оператора r_G = {r_G}")
    print(f"||G_hat||_F^2 = {G_total:.6f}")
    print(f"Coh_E = {coh_E:.4f}")
    print(f"kappa = {kappa:.4f}")

    # Сравнение с нормальным состоянием (без алекситимии)
    gamma_normal = np.full((N, N), c, dtype=complex)
    np.fill_diagonal(gamma_normal, 1/N)
    G_hat_normal = gamma_normal.imag
    G_total_normal = np.linalg.norm(G_hat_normal, 'fro')**2
    print(f"\nСравнение: ||G_hat||_F^2 нормальное = {G_total_normal:.6f}, "
          f"алекситимическое = {G_total:.6f}")

    return gamma, G_hat

gamma_alex, G_alex = alexithymia_model()
```

---

## 5. Динамическая система с рациональными/иррациональными частотами {#динамическая-система}

### 5.1 Определение [О]

Рассмотрим [когерентную эволюцию](/docs/core/dynamics/evolution) с диагональным гамильтонианом:

$$
\Gamma(\tau) = U(\tau)\,\Gamma_0\,U(\tau)^\dagger, \quad U(\tau) = e^{-iH\tau}
$$

где $H = \mathrm{diag}(\omega_1, \omega_2, \ldots, \omega_7)$. Элементы матрицы когерентности эволюционируют как:

$$
\gamma_{kl}(\tau) = \gamma_{kl}(0) \cdot e^{-i(\omega_k - \omega_l)\tau}
$$

Фазы когерентностей:

$$
\theta_{kl}(\tau) = \theta_{kl}(0) + (\omega_k - \omega_l)\tau
$$

Gap эволюционирует как:

$$
\mathrm{Gap}(k,l;\tau) = |\sin(\theta_{kl}(0) + \Omega_{kl}\tau)|, \quad \Omega_{kl} := \omega_k - \omega_l
$$

### 5.2 Рациональные частоты: периодические орбиты [Т]

:::tip Теорема (Периодичность при рациональных частотах) [Т]
Если все разности частот $\Omega_{kl} = \omega_k - \omega_l$ рационально соизмеримы (т.е. $\Omega_{kl}/\Omega_{mn} \in \mathbb{Q}$ для всех пар), то Gap-профиль $\{\mathrm{Gap}(k,l;\tau)\}$ **периодичен** с периодом:

$$
T = \mathrm{lcm}\left\{\frac{2\pi}{|\Omega_{kl}|} : \Omega_{kl} \neq 0 \right\}
$$

где $\mathrm{lcm}$ — наименьшее общее кратное (определено для рациональных кратных базовой частоты).
:::

**Доказательство.** Пусть $\Omega_{kl} = n_{kl} \cdot \omega_0$ для $n_{kl} \in \mathbb{Z}$, $\omega_0$ — базовая частота. Тогда $\mathrm{Gap}(k,l;\tau + 2\pi/\omega_0) = |\sin(\theta_{kl}(0) + n_{kl}\omega_0(\tau + 2\pi/\omega_0))| = |\sin(\theta_{kl}(0) + n_{kl}\omega_0\tau + 2\pi n_{kl})| = \mathrm{Gap}(k,l;\tau)$. Период: $T = 2\pi/\omega_0$. $\square$

**Пример.** $H = \mathrm{diag}(0, 1, 2, 3, 4, 5, 6) \cdot \omega_0$. Все $\Omega_{kl} = (k-l)\omega_0 \in \mathbb{Z}\omega_0$. Период $T = 2\pi/\omega_0$.

### 5.3 Иррациональные частоты: квазипериодичность и эргодичность [Т]

:::tip Теорема (Эргодичность при иррациональных частотах) [Т]
Если среди разностей частот $\{\Omega_{kl}\}$ существуют рационально **несоизмеримые** пары, то Gap-орбита $\tau \mapsto \{\theta_{kl}(\tau) \bmod 2\pi\}$ **квазипериодична** и плотно заполняет $d$-мерный тор $\mathbb{T}^d$, где $d$ — число линейно независимых (над $\mathbb{Q}$) разностей частот.
:::

**Доказательство.** Вектор фаз $\boldsymbol{\theta}(\tau) = \boldsymbol{\theta}(0) + \boldsymbol{\Omega}\tau$ на торе $\mathbb{T}^{21}$ (21 независимая пара). По теореме Вейля о равномерном распределении, если $\Omega_1, \ldots, \Omega_d$ линейно независимы над $\mathbb{Q}$, орбита плотна в $\mathbb{T}^d$ и равномерно распределена. $\square$

**Следствие.** Средний по времени Gap:

$$
\overline{\mathrm{Gap}(k,l)} = \lim_{T \to \infty} \frac{1}{T}\int_0^T |\sin(\theta_{kl}(0) + \Omega_{kl}\tau)|\,d\tau = \frac{2}{\pi} \approx 0.637
$$

для всех пар $(k,l)$ с $\Omega_{kl} \neq 0$ (иррациональные или рациональные — результат одинаков для любого $\Omega_{kl} \neq 0$).

### 5.4 Связь с немарковской динамикой [С]

В полной [эволюции](/docs/core/dynamics/evolution) (включая диссипацию и регенерацию) рациональность частот определяет характер памяти:

| Режим | Частоты | Орбита | Память | Спектр |
|-------|---------|--------|--------|--------|
| Рациональный | $\Omega_{kl}/\Omega_{mn} \in \mathbb{Q}$ | Периодическая | Конечная рекуррентная | Дискретный |
| Иррациональный | $\exists\, \Omega_{kl}/\Omega_{mn} \notin \mathbb{Q}$ | Квазипериодическая | Бесконечная некоммутативная | Непрерывный |
| Диссипативный | $\Omega_{kl} = 0$ (все) | Фиксированная точка | Марковский (без памяти) | Вырожденный |

:::note Связь с кодом Хэмминга [С]
В [Gap-динамике](/docs/core/dynamics/gap-dynamics) квазипериодические орбиты связаны с **немарковскими** поправками через тензор памяти $K(\tau, \tau')$. Рациональные частоты допускают конечномерное ядро памяти, иррациональные — требуют бесконечномерного. Аналогия с [кодом Хэмминга H(7,4)](/docs/core/dynamics/gap-dynamics#код-хэмминга): периодические орбиты «декодируемы» (синдром определяет ошибку однозначно), квазипериодические — нет.
:::

### 5.5 Конкретный пример: золотое сечение [О]

Выберем $H = \mathrm{diag}(0, 1, \phi, \phi^2, 2\phi, \phi+1, 2)$ где $\phi = (1+\sqrt{5})/2$ — золотое сечение. Среди разностей $\omega_k - \omega_l$ есть как рациональные ($\omega_6 - \omega_1 = 2$), так и иррациональные ($\omega_2 - \omega_1 = \phi$). Тор имеет $d = 2$ независимых частоты ($1$ и $\phi$), орбита плотно заполняет $\mathbb{T}^2$.

### 5.6 Python-реализация

```python
import numpy as np

def dynamic_system(rational=True, tau_max=100.0, dt=0.01):
    """Модель 5: Эволюция с рациональными/иррациональными частотами."""
    N = 7
    phi_golden = (1 + np.sqrt(5)) / 2

    if rational:
        # Рациональные: все частоты — целые кратные ω₀
        omega = np.array([0, 1, 2, 3, 4, 5, 6], dtype=float)
        label = "рациональные"
    else:
        # Иррациональные: включают золотое сечение
        omega = np.array([0, 1, phi_golden, phi_golden**2,
                          2*phi_golden, phi_golden+1, 2], dtype=float)
        label = "иррациональные"

    # Начальное состояние: чистое с фазами Фибоначчи (модель 3)
    fib_mod7 = [1, 1, 2, 3, 5, 1, 6]
    phases_init = [2 * np.pi * f / 7 for f in fib_mod7]
    psi_0 = np.array([np.exp(1j * ph) for ph in phases_init]) / np.sqrt(N)
    gamma_0 = np.outer(psi_0, psi_0.conj())

    steps = int(tau_max / dt)
    gap_history = []  # хранить Gap(A,S) и Gap(S,E)
    P_history = []

    tau_vals = np.arange(0, tau_max, dt)
    for tau in tau_vals:
        U = np.diag(np.exp(-1j * omega * tau))
        gamma_t = U @ gamma_0 @ U.T.conj()

        P = np.trace(gamma_t @ gamma_t).real
        theta = np.angle(gamma_t)
        gap_AS = abs(np.sin(theta[0, 1]))  # A-S
        gap_SE = abs(np.sin(theta[1, 4]))  # S-E

        gap_history.append((gap_AS, gap_SE))
        P_history.append(P)

    gap_history = np.array(gap_history)

    # Средний Gap по времени
    mean_gap_AS = np.mean(gap_history[:, 0])
    mean_gap_SE = np.mean(gap_history[:, 1])

    print(f"Режим: {label}")
    print(f"Средний Gap(A,S) = {mean_gap_AS:.4f}")
    print(f"Средний Gap(S,E) = {mean_gap_SE:.4f}")
    print(f"Теоретический предел (2/π) = {2/np.pi:.4f}")
    print(f"P = const = {P_history[0]:.4f} "
          f"(унитарная эволюция сохраняет чистоту)")

    # Проверка периодичности
    if rational:
        T_period = 2 * np.pi  # период при ω₀ = 1
        idx_period = int(T_period / dt)
        if idx_period < len(gap_history):
            diff = np.max(np.abs(
                gap_history[idx_period] - gap_history[0]))
            print(f"Отклонение после периода T=2π: {diff:.2e}")
    else:
        # Квазипериодический: проверяем, что орбита не замыкается
        # за время наблюдения
        unique_gaps = len(set(
            tuple(np.round(g, 4)) for g in gap_history))
        print(f"Уникальных Gap-конфигураций: {unique_gaps}/{len(gap_history)}")

    return tau_vals, gap_history, P_history

# Запуск обоих режимов
print("=" * 50)
tau_r, gap_r, P_r = dynamic_system(rational=True)
print("=" * 50)
tau_i, gap_i, P_i = dynamic_system(rational=False)
```

---

## Сравнительная таблица {#сравнительная-таблица}

| Модель | $P$ | $\mathrm{Gap}_{\text{avg}}$ | $\mathrm{Coh}_E$ | $\kappa$ | Жизнеспособна? |
|--------|-----|-------------------------------|-------------------|----------|----------------|
| 1. Однородная ($I/7$) | $1/7$ | $0$ | $1/7$ | $\omega_0/7 + \kappa_0/7$ | нет |
| 2. Чистая однородная | $1$ | $0$ | $13/49$ | $\omega_0/7 + 13\kappa_0/49$ | да |
| 3. Фибоначчи-фазы | $1$ | $\approx 0.62$ | $13/49$ | $\omega_0/7 + 13\kappa_0/49$ | да |
| 4. Алекситимия | $< 1$ | $> 0$ | $\approx 13/49$ | уменьшается | под угрозой |
| 5a. Рациональные | $\mathrm{const}$ | периодический | $\mathrm{const}$ | $\mathrm{const}$ | да |
| 5b. Иррациональные | $\mathrm{const}$ | $\to 2/\pi$ | $\mathrm{const}$ | $\mathrm{const}$ | да |

:::tip Ключевые выводы [И]
1. **Gap и чистота ортогональны**: модели 2 и 3 имеют одинаковую чистоту $P=1$, но радикально различные Gap-профили. Gap измеряет **фазовую** структуру, чистота — **амплитудную**.

2. **Алекситимия — фазовый дефект**: модель 4 показывает, что патология может возникнуть при неизменных амплитудах когерентностей — достаточно ротации фазы на $\pi/2$.

3. **Рациональность частот определяет память**: модель 5 связывает [немарковскую динамику](/docs/core/dynamics/gap-dynamics) с арифметическими свойствами гамильтониана.

4. **Эргодическая теорема для Gap**: при иррациональных частотах средний Gap стремится к $2/\pi \approx 0.637$ — универсальная константа, не зависящая от начальных условий.
:::

---

:::warning Вычислительная сложность
Масштабирование вычислений для композитных систем ($N = 7^k$, $k > 1$) **не проанализировано**. Для единичного Голонома ($N = 7$) все модели вычислимы за $O(N^3) \approx O(343)$ операций, но для мета-Голономов (Теорема 9.1) сложность может расти экспоненциально с числом уровней композиции.
:::

## Ссылки

- [Gap-оператор](/docs/core/dynamics/gap-operator) — определение и свойства $\hat{\mathcal{G}}$
- [Gap-динамика](/docs/core/dynamics/gap-dynamics) — бифуркации, немарковская динамика
- [Жизнеспособность](/docs/core/dynamics/viability) — $P_{\text{crit}} = 2/7$ и условия выживания
- [Матрица когерентности](/docs/core/dynamics/coherence-matrix) — базовый объект $\Gamma$
- [Фано-канал](/docs/proofs/gap/fano-channel) — доказательства сохранения когерентностей
- [Правила отбора Фано](/docs/physics/gauge-symmetry/fano-selection-rules) — геометрия плоскости Фано
- [Определения КК](/docs/applied/coherence-cybernetics/definitions) — $\mathrm{Coh}_E$, меры сознательности
- [Аксиоматика КК](/docs/applied/coherence-cybernetics/axiomatics) — $\kappa(\Gamma) = \kappa_{\text{bootstrap}} + \kappa_0 \cdot \mathrm{Coh}_E$
