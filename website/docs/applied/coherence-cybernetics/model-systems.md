---
sidebar_position: 9
title: "Model Systems"
description: "Exactly solvable model systems with complete Gap profiles: uniform system, pure states, alexithymia, dynamical systems"
---

# Model Systems

:::info Bridge from the Previous Chapter
In the [previous chapter](./non-markovian) we studied the non-Markovian dynamics of the Gap — memory kernels, coherence oscillations, "grief cycles" and therapeutic windows. We saw formulas and theorems. But how do we convince ourselves they are correct? A physicist verifies a theory on **exact solutions**: if a formula fails in the simplest case, it cannot work anywhere. That is exactly what this chapter is about — five model systems for which all quantities are computed analytically.
:::

### Chapter Roadmap

In this chapter we:

1. **Explain why model systems are needed** — the "hydrogen atoms" of coherence cybernetics (introduction)
2. **Compute everything for the uniform system** $\Gamma = I/7$ — the absolute minimum of purity, the "heat death" of the holon (section 1)
3. **Compute everything for the pure state** — the absolute maximum of purity, ideal order with zero Gap (section 2)
4. **Show that purity and Gap are orthogonal** using Fibonacci phases — $P = 1$, but Gap is nontrivial (section 3)
5. **Model alexithymia** — one broken channel $\mathrm{Gap}(S,E) = 1$ and its cascading consequences (section 4)
6. **Run unitary dynamics** — how Gap evolves without losses, and why the time-averaged Gap tends to $2/\pi$ for irrational frequencies (section 5)
7. **Sketch the horizon**: minimal consciousness, numerical experiments, open models

> *"If you cannot solve the general problem, find a special case you can solve and see what it teaches you."* — George Pólya

This document contains **five exactly solvable model systems** with complete Gap profiles. Each system illustrates a fundamental regime of [Gap dynamics](/docs/core/dynamics/gap-dynamics) and admits analytic computation of all key quantities: purity $P$, E-coherence $\mathrm{Coh}_E$, regeneration rate $\kappa$, and the full Gap operator $\hat{\mathcal{G}}$.

---

## Why Model Systems Are Needed {#зачем-модели}

A physicist first encountering quantum mechanics does not start with proteins or crystals — they start with the **hydrogen atom**. Not because hydrogen is the most important thing in the world, but because hydrogen *has an exact solution*. The exact solution provides an anchor: we know that in this specific case our formulas are correct, and from that anchor we can proceed further — to helium, to molecules, to solids.

In coherence cybernetics (CC) the role of the hydrogen atom is played by **model systems** — specially chosen coherence matrices $\Gamma$ for which all key quantities are computed in closed form. Each model system answers its own question:

- **Uniform system** ($P = 1/7$): what happens when structure is completely destroyed?
- **Pure state** ($P = 1$): what happens under absolute order?
- **Fibonacci phases**: how does phase structure generate Gap when amplitudes are unchanged?
- **Alexithymia**: how does one broken channel threaten the whole?
- **Unitary dynamics**: how does the system evolve without losses?

These five models are not abstract exercises. They set a **scale**: any real matrix $\Gamma$ can be located between the "dead" ($I/7$) and "frozen" ($|\psi\rangle\langle\psi|$) extremes, and we can understand where it stands on this spectrum.

:::info Analogy: the theorist's laboratory
An experimentalist tests a theory on an apparatus. A theorist tests a theory on **model systems**. If a formula is correct, it must give the right answers in every exactly solvable case. If it gives an absurd result even in one — the formula is wrong.
:::

---

## Five States of Being {#пять-состояний}

Before diving into formulas, it is helpful to picture our five models as five *archetypal states* of a conscious (or non-conscious) system. Let us call them:

| # | Model | Archetype | Analogy | State |
|---|-------|-----------|---------|-------|
| 1 | $\Gamma = I/7$ | **Dead system** | Heat death of the Universe | Maximum chaos, no structure |
| 2 | $\Gamma = \|\psi\rangle\langle\psi\|$ | **Frozen system** | Absolute zero | Ideal order, no internal tension |
| 3 | Fibonacci phases | **Structured beauty** | Crystal with a nontrivial lattice | Order + phase texture |
| 4 | Alexithymia | **Blind spot** | Damaged nerve | Partial severance of internal connection |
| 5 | Unitary dynamics | **Ideal pendulum** | Planetary orbit without friction | Perpetual motion, no losses |

Note: none of these models describes a **living, conscious system** in the full CC sense. That requires the joint action of unitary evolution, Fano dissipation, regeneration $\mathcal{R}$, and self-modelling $\varphi$. Nevertheless, each model illuminates one specific aspect — like a single spotlight on a stage.

---

:::note Limitations of model systems
All five model systems are **purely mathematical** illustrations, not full holon models with CC dynamics. In particular:
- Models 1–3 consider **fixed** matrices $\Gamma$ without dynamics ($d\Gamma/d\tau = 0$).
- Model 4 (alexithymia) describes a **static** phase defect; the cascading effect (section 4.4) is discussed qualitatively but not modelled.
- Model 5 (dynamical) includes **only unitary** evolution, without dissipation ($\Gamma_2 = 0$) and regeneration ($\kappa = 0$).

None of the models includes the **complete** CC dynamics: joint unitary evolution + dissipation (Fano channel) + regeneration ($\mathcal{R}$) + self-modelling ($\varphi$). Building a complete model system with CC dynamics is an [open problem](./implementation).
:::

:::note On notation
- $\Gamma$ — [coherence matrix](/docs/core/dynamics/coherence-matrix), $\gamma_{ij}$ — its elements
- $P = \mathrm{Tr}(\Gamma^2)$ — [purity](/docs/core/dynamics/viability#определение-чистоты)
- $\mathrm{Gap}(i,j) = |\sin(\theta_{ij})|$ where $\theta_{ij} = \arg(\gamma_{ij})$ — [Gap measure](/docs/core/dynamics/gap-operator#определение)
- $\hat{\mathcal{G}} = \mathrm{Im}(\Gamma)$ — [Gap operator](/docs/core/dynamics/gap-operator)
- Dimensions: $A{=}1, S{=}2, D{=}3, L{=}4, E{=}5, U{=}6, O{=}7$ (octonionic assignment: $O \leftrightarrow e_7$, $U \leftrightarrow e_6$ — see [dimensions.md](/docs/core/structure/dimensions))
- Fano lines: $\{1,2,4\}, \{2,3,5\}, \{3,4,6\}, \{4,5,7\}, \{5,6,1\}, \{6,7,2\}, \{7,1,3\}$ = $\{A,S,L\}, \{S,D,E\}, \{D,L,U\}, \{L,E,O\}, \{E,U,A\}, \{U,O,S\}, \{O,A,D\}$
:::

---

## 1. Uniform System: $\Gamma = I/7$ {#однородная-система}

*Question this model answers:* **what does the complete absence of structure look like?**

Imagine a room in which every radio station is playing simultaneously at the same volume. You hear none of them — only white noise. The uniform system is that same white noise in the space of coherences: all dimensions are present with equal weight, but there are no connections between them. This is the *heat death* of the holon.

### 1.1 Definition [D]

The maximally mixed state — uniform distribution over all seven dimensions with no coherences:

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

### 1.2 Analytic Results [T]

| Quantity | Formula | Value |
|----------|---------|-------|
| Purity | $P = \mathrm{Tr}(\Gamma^2) = 7 \cdot (1/7)^2$ | $1/7 \approx 0.143$ |
| Entropy | $S_{vN} = \log 7$ | $\approx 1.946$ |
| Gap operator | $\hat{\mathcal{G}} = \mathrm{Im}(\Gamma) = 0$ | $0_{7 \times 7}$ |
| $\mathrm{Gap}(i,j)$ | $\gamma_{ij} = 0$ for $i \neq j$ | $0$ for all pairs |
| $\mathrm{Coh}_E$ | $(1/7)^2 / (1/7) = 1/7$ | $\approx 0.143$ |
| $\kappa$ | $\kappa_{\text{bootstrap}} + \kappa_0 / 7$ | minimal |

:::warning Non-viability [T]
$P = 1/7 < P_{\text{crit}} = 2/7$. The system is **non-viable** — purity is at its absolute minimum. This is the "dead" state of maximum entropy, failing to satisfy the [(V) viability condition](/docs/core/foundations/axiom-septicity#v-жизнеспособность).
:::

### 1.3 Physical Interpretation [I]

The uniform state is the limiting case of complete decoherence. All dimensions are fully independent ($\gamma_{ij} = 0$ for $i \neq j$), information is evenly distributed. The Gap is identically zero — not because the system is "transparent", but because **there is nothing to be transparent**: coherences are absent.

#### Psychological analogy

If one could imagine "consciousness" in this state (which is contradictory since $P < P_{\text{crit}}$), it would be totally diffuse: seven modalities — Action, Structure, Dynamics, Logic, Experience, Unity, Objectness — all present in equal measure, but *none connected to any other*. There is no thought, because thought is correlation. There is no feeling, because feeling is the elevation of one of the seven above the rest. This is not a coma (a coma is a *reduction* in activity); this is maximum activity without direction — like infinite brain noise.

#### What we learn from this model

1. **Lower bound on purity**: $P = 1/7$ is the absolute minimum for $\Gamma \in D(\mathbb{C}^7)$. There is nowhere lower.
2. **Gap = 0 does not mean health**: zero Gap at $P = 1/7$ is not "transparency" — it is the *absence of material for transparency*.
3. **Scale**: any real system with $P > 1/7$ already has *some* structure, some escape from this minimum.

#### Limitations

The model is completely static. It does not answer: *how* does a system reach this state? (Answer: through Fano dissipation without regeneration — that is how the Fano channel works.) Nor does it answer: *can* the system escape? (Answer: only if $\kappa > 0$, through regeneration.)

### 1.4 Python Implementation

```verum
mount std.math.linalg.{StaticMatrix, identity, eigvalsh};
mount std.math.complex.Complex;

pub type ModelReport is {
    p:         Float,
    s_vn:      Float,
    gap_total: Float,
    coh_e:     Float,
    viable:    Bool,
};

/// Model 1: Maximally mixed state Γ = I/7.
pub pure fn uniform_system() -> ModelReport {
    let gamma = identity::<Complex, 7>() / Complex.from_real(7.0);

    let p = (&gamma @ &gamma).trace().real();                     // 1/7
    let s_vn = eigvalsh(&gamma).iter()
        .map(|λ| -λ * (λ + 1.0e-30).ln())
        .sum();

    // Gap operator = Im(Γ) — zero matrix for real diagonal.
    let gap_total = gamma.imag_part().frobenius_norm_sq();

    const E: Int = 4;
    let coh_e = (gamma[E, E].real().pow(2)
                + 2.0 * (0..7).filter(|i| *i != E)
                               .map(|i| gamma[E, *i].abs().pow(2))
                               .sum()) / p;

    ModelReport { p: p, s_vn: s_vn, gap_total: gap_total, coh_e: coh_e,
                  viable: p > 2.0 / 7.0 }
}

fn main() using [IO] {
    let r = uniform_system();
    IO.println(f"P = {r.p:.4f}, Coh_E = {r.coh_e:.4f}, viable = {r.viable}");
    // P = 0.1429, Coh_E = 0.1429, viable = false
}
```

---

## 2. Pure State: Uniform Superposition {#чистое-однородное}

*Question this model answers:* **what happens under absolute order — when all coherences are transparent (Gap → 0 for all channels)?**

If Model 1 is white noise, then Model 2 is a perfectly pure tone. All seven dimensions ring in unison, in phase, at equal amplitude. The result: maximum purity ($P = 1$) and zero Gap. This is the *absolute zero* of coherence cybernetics — ideal order, the absence of internal tension, crystalline transparency.

### 2.1 Definition [D]

A pure state with equal amplitudes and zero phases:

$$
|\psi\rangle = \frac{1}{\sqrt{7}} \sum_{i=1}^{7} |i\rangle
$$

Coherence matrix:

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

All elements $\gamma_{ij} = 1/7$ — real and positive.

### 2.2 Analytic Results [T]

| Quantity | Formula | Value |
|----------|---------|-------|
| Purity | $P = \mathrm{Tr}(\Gamma^2) = \mathrm{Tr}(\Gamma) = 1$ | $1$ (maximum) |
| Entropy | $S_{vN} = 0$ | $0$ (minimum) |
| Phases | $\theta_{ij} = \arg(1/7) = 0$ | $0$ for all pairs |
| $\mathrm{Gap}(i,j)$ | $\lvert\sin(0)\rvert = 0$ | $0$ for all pairs |
| $\hat{\mathcal{G}}$ | $\mathrm{Im}(\Gamma) = 0$ | $0_{7 \times 7}$ |
| $\mathrm{Coh}_E$ | $((1/7)^2 + 2 \cdot 6 \cdot (1/7)^2) / 1 = 13/49$ | $\approx 0.265$ |
| $\kappa$ | $\kappa_{\text{bootstrap}} + \kappa_0 \cdot 13/49$ | moderate |

:::tip Maximum purity, zero Gap [T]
$P = 1$: the system is maximally pure and viable ($P \gg P_{\text{crit}} = 2/7$). At the same time $\mathrm{Gap}(i,j) = 0$ for all pairs — complete transparency. All dimensions are coherent and "see each other" without remainder.
:::

### 2.3 Physical Interpretation [I]

#### Psychological analogy

The pure uniform state is an idealisation of *total self-knowledge*. Every cognitive modality is completely transparent to every other. Structure sees Experience, Logic sees Action, Unity sees Objectness — without distortions, without phase shifts, without Gap.

Sounds wonderful? Not so fast. Note: **Gap is identically zero**. But Gap is a measure of *internal tension*, the source of dynamics, the reason the system seeks, moves, grows. If Gap = 0, the system has *nowhere to aspire*. It is perfect — and dead in another sense: not in the sense of chaos (like $I/7$), but in the sense of lacking *direction*.

This is a deep analogy with thermodynamics: $I/7$ is heat death (maximum entropy), while the pure state is absolute zero (minimum entropy). Both states are *extremal*, and both lack useful dynamics.

#### What we learn from this model

1. **Upper bound on purity**: $P = 1$ is the absolute maximum. There is nowhere higher.
2. **Gap = 0 at P = 1 is not the same as Gap = 0 at P = 1/7**: in the first case there is no Gap because everything is transparent; in the second — because there are no coherences at all. The same zero, two fundamentally different meanings.
3. **Perfection is barren**: a system without Gap has no *driver* for change. For a "living" system a nonzero Gap is needed — internal tension that generates evolution.

#### Limitations

The pure state is unstable: any interaction with the environment (dissipation) immediately reduces $P$. Therefore the pure state is an *instantaneous limit*, not a stable state. A real system is never in a pure state — it always has nonzero entropy.

### 2.4 Remark on Coh_E [T]

The E-coherence of the pure uniform state is determined via the [HS-projection π_E](/docs/core/foundations/axiom-septicity#e-coherence-definition):

$$
\widetilde{\mathrm{Coh}}_E^{7D} = \frac{\gamma_{EE}^2 + 2\sum_{i \neq E}|\gamma_{Ei}|^2}{\mathrm{Tr}(\Gamma^2)} = \frac{(1/7)^2 + 2 \cdot 6 \cdot (1/7)^2}{1} = \frac{13}{49} \approx 0.265
$$

This is not the maximum E-coherence: achieving $\mathrm{Coh}_E = 1$ requires concentrating all coherence on the E-dimension.

### 2.5 Python Implementation

```verum
/// Model 2: Pure state with uniform superposition |ψ⟩ = (1/√7) Σ|k⟩.
pub fn pure_uniform() using [IO]
    -> (StaticMatrix<Complex, 7, 7>, StaticMatrix<Float, 7, 7>)
{
    let psi = StaticVector.<Complex, 7>.repeat(Complex.one() / 7.0.sqrt());
    let gamma = psi.outer(psi.conjugate());

    let p = (&gamma @ &gamma).trace().real();                                       // 1.0
    let theta = gamma.map(|c| c.arg());                                             // zero
    let gap_matrix = theta.map(|φ| φ.sin().abs());                                  // zero

    const E: Int = 4;
    let coh_e = (gamma[E, E].real().pow(2)
                + 2.0 * (0..7).filter(|i| *i != E)
                               .map(|i| gamma[E, *i].abs().pow(2))
                               .sum()) / p;

    IO.println(f"P = {p:.4f}");
    IO.println(f"Coh_E = {coh_e:.4f}");
    IO.println(f"Gap (max) = {gap_matrix.max_element():.6f}");
    IO.println(f"All θ_ij = 0: {gap_matrix.frobenius_norm() < 1.0e-12}");
    (gamma, gap_matrix)
}
// Expected: P = 1.0000, Coh_E = 0.2653, Gap (max) = 0.000000
```

---

## 3. Pure State with Fibonacci Phases {#фибоначчи-фазы}

*Question this model answers:* **can one have maximum order ($P = 1$) and simultaneously a nontrivial internal texture (nonzero Gap)?**

The answer is yes. And Fibonacci shows how.

Model 2 was perfectly transparent: all phases zero, Gap = 0. But purity is determined by *amplitudes*, and Gap by *phases*. Can we "rotate" the phases without changing the amplitudes and obtain a nontrivial Gap at $P = 1$? That is exactly what Fibonacci phases do — and the result is strikingly beautiful.

### 3.1 Definition [D]

A pure state with equal amplitudes and phases defined by Fibonacci numbers modulo 7:

$$
|\psi_F\rangle = \frac{1}{\sqrt{7}} \sum_{k=1}^{7} e^{i \varphi_k} |k\rangle
$$

where the phases are defined via Fibonacci numbers $F_n$ (mod 7):

| $k$ | Dimension | $F_k$ | $F_k \bmod 7$ | $\varphi_k = 2\pi \cdot (F_k \bmod 7) / 7$ |
|-----|-----------|-------|----------------|----------------------------------------------|
| 1 | A | 1 | 1 | $2\pi/7$ |
| 2 | S | 1 | 1 | $2\pi/7$ |
| 3 | D | 2 | 2 | $4\pi/7$ |
| 4 | L | 3 | 3 | $6\pi/7$ |
| 5 | E | 5 | 5 | $10\pi/7$ |
| 6 | O | 8 | 1 | $2\pi/7$ |
| 7 | U | 13 | 6 | $12\pi/7$ |

#### Why Fibonacci?

The choice of Fibonacci phases is not accidental. The Fibonacci sequence modulo 7 has period 16 (Pisano period $\pi(7) = 16$) and generates a rich yet ordered structure of phase differences. Three dimensions (A, S, O) turn out to be in phase ($\varphi_A = \varphi_S = \varphi_O$), creating a cluster of zero Gap. The remaining pairs have nonzero differences, generating a Gap texture with three distinct values: $|\sin(2\pi/7)| \approx 0.782$, $|\sin(4\pi/7)| \approx 0.975$, and $|\sin(6\pi/7)| \approx 0.434$.

This resembles a crystal: ideal order ($P = 1$), but with a nontrivial phase *lattice*.

### 3.2 Coherence Matrix [T]

Matrix elements: $\gamma_{kl} = \frac{1}{7} e^{i(\varphi_k - \varphi_l)}$. All $|\gamma_{kl}| = 1/7$. Phase of coherence:

$$
\theta_{kl} = \varphi_k - \varphi_l = \frac{2\pi}{7}\left[(F_k \bmod 7) - (F_l \bmod 7)\right]
$$

Index differences $(F_k \bmod 7) - (F_l \bmod 7)$ modulo 7:

$$
\Delta_{kl} = (F_k - F_l) \bmod 7
$$

Explicit table $\Delta_{kl}$:

| | A(1) | S(1) | D(2) | L(3) | E(5) | O(1) | U(6) |
|---|---|---|---|---|---|---|---|
| **A(1)** | 0 | 0 | 6 | 5 | 3 | 0 | 2 |
| **S(1)** | 0 | 0 | 6 | 5 | 3 | 0 | 2 |
| **D(2)** | 1 | 1 | 0 | 6 | 4 | 1 | 3 |
| **L(3)** | 2 | 2 | 1 | 0 | 5 | 2 | 4 |
| **E(5)** | 4 | 4 | 3 | 2 | 0 | 4 | 6 |
| **O(1)** | 0 | 0 | 6 | 5 | 3 | 0 | 2 |
| **U(6)** | 5 | 5 | 4 | 3 | 1 | 5 | 0 |

### 3.3 Gap Profile [T]

$\mathrm{Gap}(k,l) = |\sin(2\pi\Delta_{kl}/7)|$. Using values $\sin(2\pi n/7)$:

| $n \bmod 7$ | $\sin(2\pi n / 7)$ | $\lvert\sin(2\pi n / 7)\rvert$ |
|-------------|---------------------|----------------------|
| 0 | $0$ | $0$ |
| 1 | $\sin(2\pi/7) \approx 0.7818$ | $0.7818$ |
| 2 | $\sin(4\pi/7) \approx 0.9749$ | $0.9749$ |
| 3 | $\sin(6\pi/7) \approx 0.4339$ | $0.4339$ |
| 4 | $-\sin(6\pi/7) \approx -0.4339$ | $0.4339$ |
| 5 | $-\sin(4\pi/7) \approx -0.9749$ | $0.9749$ |
| 6 | $-\sin(2\pi/7) \approx -0.7818$ | $0.7818$ |

Full Gap matrix $\mathrm{Gap}(k,l)$:

| | A | S | D | L | E | O | U |
|---|---|---|---|---|---|---|---|
| **A** | 0 | 0 | 0.782 | 0.975 | 0.434 | 0 | 0.975 |
| **S** | 0 | 0 | 0.782 | 0.975 | 0.434 | 0 | 0.975 |
| **D** | 0.782 | 0.782 | 0 | 0.782 | 0.434 | 0.782 | 0.434 |
| **L** | 0.975 | 0.975 | 0.782 | 0 | 0.975 | 0.975 | 0.434 |
| **E** | 0.434 | 0.434 | 0.434 | 0.975 | 0 | 0.434 | 0.782 |
| **O** | 0 | 0 | 0.782 | 0.975 | 0.434 | 0 | 0.975 |
| **U** | 0.975 | 0.975 | 0.434 | 0.434 | 0.782 | 0.975 | 0 |

#### What the Gap matrix reveals

Let us look at this matrix with our eyes, not just formulas:

- **Cluster {A, S, O}** — three dimensions with zero mutual Gap. They are in phase and completely transparent to each other. This is the *coherence core* of the model.
- **L and U** — two dimensions with maximum Gap values (~0.975) relative to the {A, S, O} cluster. They are *most hidden* from the core.
- **E (Experience)** — has the softest Gap values (~0.434) relative to most dimensions. Experience is "semi-transparent" — partially visible, partially hidden.
- **D (Dynamics)** — uniformly distributed Gap (~0.434–0.782), a "mediator" between the cluster and the periphery.

These are not just numbers — they are the *architecture of an inner world*.

### 3.4 Connection to Fano Geometry [C]

Fano lines contain pairs $(k,l)$ with specific Gap values. For each line we compute the mean Gap:

| Fano line | Pairs | Gap values | Mean Gap |
|-----------|-------|------------|----------|
| $\{1,2,4\} = \{A,S,L\}$ | (A,S), (A,L), (S,L) | 0, 0.975, 0.975 | 0.650 |
| $\{2,3,5\} = \{S,D,E\}$ | (S,D), (S,E), (D,E) | 0.782, 0.434, 0.434 | 0.550 |
| $\{3,4,6\} = \{D,L,O\}$ | (D,L), (D,O), (L,O) | 0.782, 0.782, 0.975 | 0.846 |
| $\{4,5,7\} = \{L,E,U\}$ | (L,E), (L,U), (E,U) | 0.975, 0.434, 0.782 | 0.730 |
| $\{5,6,1\} = \{E,O,A\}$ | (E,O), (E,A), (O,A) | 0.434, 0.434, 0 | 0.289 |
| $\{6,7,2\} = \{O,U,S\}$ | (O,U), (O,S), (U,S) | 0.975, 0, 0.975 | 0.650 |
| $\{7,1,3\} = \{U,A,D\}$ | (U,A), (U,D), (A,D) | 0.975, 0.434, 0.782 | 0.730 |

:::tip Observation [C]
The Fano line $\{E, O, A\}$ has the **minimum** mean Gap (0.289) — it is the most "transparent". This is a consequence of $F_1 \equiv F_6 \equiv F_2 \equiv 1 \pmod{7}$: dimensions A, S and O share the same phase, and the Gap between them is identically zero.
:::

#### The golden ratio in the Gap texture?

An intriguing question: is there a connection between the Fibonacci sequence and the golden ratio $\phi = (1+\sqrt{5})/2$ in this model? Formally — no: we use Fibonacci *modulo 7*, which erases the asymptotics $F_n \sim \phi^n/\sqrt{5}$. However, the *arithmetic* structure of Fibonacci mod 7 (Pisano period, coincidences $F_1 = F_2 = F_6 \bmod 7$) inherits combinatorial properties of the golden ratio, generating an aesthetically beautiful Gap texture. This is one of those mathematical "rhymes" that is hard to call coincidence yet even harder to explain.

### 3.5 Summary [T]

| Quantity | Value |
|----------|-------|
| $P$ | $1$ (pure state) |
| $\|\hat{\mathcal{G}}\|_F^2$ | $\frac{1}{49}\sum_{k<l} \sin^2(2\pi\Delta_{kl}/7) \approx 0.1049$ |
| $\mathrm{Coh}_E$ | $13/49 \approx 0.265$ (invariant of pure state with $\lvert\gamma_{kl}\rvert=1/7$) |
| $\kappa$ | $\kappa_{\text{bootstrap}} + \kappa_0 \cdot 13/49$ |
| Mean Gap | $\frac{1}{21}\sum_{k<l}\mathrm{Gap}(k,l) \approx 0.620$ |

#### What we learn from this model

1. **Purity and Gap are orthogonal characteristics**: models 2 and 3 have the same purity $P = 1$, the same $\mathrm{Coh}_E = 13/49$, the same $\kappa$ — but radically different Gap profiles. Gap measures *phase texture*, purity measures *amplitude organisation*.
2. **Phases are character**: two holons with the same energetics ($P$, $\kappa$) can have entirely different "personalities" — different Gap patterns. Phases determine *which* pairs of dimensions see each other and which are separated by a barrier.
3. **Clustering**: Fibonacci phases generate a natural cluster {A, S, O} — three dimensions synchronised in phase. This suggests that in real holons, clusters of in-phase dimensions may be meaningful psychological formations.

#### Limitations

The model does not account for dynamics: the cluster {A, S, O} and the high Gap values of L, U are an *initial condition*, not a stable configuration. Under Fano dissipation the phase texture will evolve, and the question of which clusters are stable remains open.

### 3.6 Python Implementation

```verum
mount std.math.constants.PI;

/// Model 3: Pure state with Fibonacci phases mod 7.
pub fn fibonacci_phases() using [IO]
    -> (StaticMatrix<Complex, 7, 7>, StaticMatrix<Float, 7, 7>)
{
    // F₁…F₇ mod 7.
    const FIB_MOD7: [Int; 7] = [1, 1, 2, 3, 5, 1, 6];

    let psi = StaticVector.<Complex, 7>.from_array(
        FIB_MOD7.map(|f| (Complex.i() * Complex.from_real(2.0 * PI * (f as Float) / 7.0)).exp())
    ) / Complex.from_real(7.0.sqrt());

    let gamma = psi.outer(psi.conjugate());
    let p = (&gamma @ &gamma).trace().real();
    let theta = gamma.map(|c| c.arg());
    let gap_matrix = theta.map(|φ| φ.sin().abs());

    // Octonionic labelling: U = e₆ (idx 5), O = e₇ (idx 6).
    const DIMS: [Text; 7] = ["A", "S", "D", "L", "E", "U", "O"];

    IO.println("Gap matrix:");
    IO.println(f"    {DIMS.map(|d| f"{d:>5}").join("  ")}");
    for i in 0..7 {
        let row = (0..7).map(|j| f"{gap_matrix[i, j]:5.3f}").join("  ");
        IO.println(f"{DIMS[i]:>2}  {row}");
    }

    // Gap operator: ‖Im Γ‖_F².
    let g_total = gamma.imag_part().frobenius_norm_sq();
    IO.println(f"\nP = {p:.4f}");
    IO.println(f"||G_hat||_F^2 = {g_total:.4f}");

    const E: Int = 4;
    let coh_e = (gamma[E, E].real().pow(2)
                + 2.0 * (0..7).filter(|i| *i != E)
                               .map(|i| gamma[E, *i].abs().pow(2))
                               .sum()) / p;
    IO.println(f"Coh_E = {coh_e:.4f}");

    // Mean Gap over 21 independent off-diagonal pairs.
    let mut sum_gap = 0.0;
    let mut count  = 0;
    for i in 0..7 { for j in (i + 1)..7 { sum_gap += gap_matrix[i, j]; count += 1; } }
    IO.println(f"Mean Gap = {sum_gap / (count as Float):.4f}");

    // Fano-line analysis.
    const FANO_LINES: [(Int, Int, Int); 7] = [
        (0, 1, 3), (1, 2, 4), (2, 3, 5), (3, 4, 6), (4, 5, 0), (5, 6, 1), (6, 0, 2),
    ];
    IO.println("\nGap by Fano lines:");
    for (i, j, k) in FANO_LINES {
        let mean = (gap_matrix[i, j] + gap_matrix[i, k] + gap_matrix[j, k]) / 3.0;
        IO.println(f"  {{{DIMS[i]},{DIMS[j]},{DIMS[k]}}}: mean Gap = {mean:.3f}");
    }

    (gamma, gap_matrix)
}
```

---

## 4. Alexithymia Model: $\mathrm{Gap}(S,E) = 1$ {#алекситимия}

*Question this model answers:* **what happens when one communication channel between dimensions is completely severed?**

The previous models were "global" — we varied properties of $\Gamma$ as a whole. The alexithymia model, by contrast, is local: we take a normal coherence matrix and break *one specific element*. This is a model of *damage*, *defect*, *blind spot* — and that is precisely why it is clinically relevant.

### 4.1 Definition [D]

**Alexithymia** (from Greek a- "without", lexis "word", thymos "feeling") — the inability to recognise and verbalise one's own emotions. In Gap-dynamics terms: maximal opacity between the Structure (S) and Experience (E) dimensions.

:::tip Model definition [D]
An alexithymic state — a coherence matrix $\Gamma_{\text{alex}}$ in which:

$$
\mathrm{Gap}(S,E) = |\sin(\theta_{SE})| = 1 \quad \Rightarrow \quad \theta_{SE} = \pm\pi/2
$$

meaning $\gamma_{SE} = |\gamma_{SE}| \cdot e^{\pm i\pi/2} = \pm i\,|\gamma_{SE}|$ — **purely imaginary** coherence.
:::

#### Psychological analogy

Imagine a person who feels — but cannot *name* what they feel. The body reacts: the heart beats faster, the hands sweat, the throat tightens. But when asked "What do you feel?", they answer: "I don't know. Just... something's off." The channel between *experience* (E) and *structuring* (S) is blocked. Information exists, but it is *unreadable*.

In terms of $\Gamma$: coherence $\gamma_{SE}$ is nonzero in magnitude — the connection *exists*. But its phase is rotated by $\pi/2$ — information arrives in an *unreadable format*. $\mathrm{Gap}(S,E) = 1$ — maximum opacity.

This is not a broken wire. This is a wire carrying a signal at perpendicular polarisation. The receiver cannot decode it.

### 4.2 Concrete Realisation [D]

We define the coherence matrix with one alexithymic defect. The base state — partially coherent with real coherences, except for the (S,E) pair:

$$
\gamma_{kl} = \begin{cases}
1/7 & k = l \\
c \cdot i & (k,l) = (S,E) \text{ or } (k,l) = (E,S) \text{ (by hermiticity: } \gamma_{ES} = -ci\text{)} \\
c & k \neq l, \; (k,l) \neq (S,E), (E,S)
\end{cases}
$$

where $c > 0$ is the coherence parameter. For hermiticity: $\gamma_{SE} = ci$, $\gamma_{ES} = \overline{\gamma_{SE}} = -ci$.

:::warning Positivity check
The matrix $\Gamma_{\text{alex}}$ must be positive semidefinite. This imposes constraints on $c$. For $c = 0.08$ (with $\gamma_{ii} = 1/7 \approx 0.143$) the matrix is admissible.
:::

### 4.3 Effect on E-coherence [T]

E-coherence via [HS-projection π_E](/docs/core/foundations/axiom-septicity#e-coherence-definition):

$$
\widetilde{\mathrm{Coh}}_E^{7D} = \frac{\gamma_{EE}^2 + 2\sum_{i \neq E}|\gamma_{Ei}|^2}{\mathrm{Tr}(\Gamma^2)}
$$

For the alexithymic state the coherence $|\gamma_{SE}| = c$ is preserved in magnitude, but the phase $\theta_{SE} = \pi/2$ makes the contribution to the Gap operator maximal. Comparison with the normal state ($\theta_{SE} = 0$):

| Quantity | Normal | Alexithymic |
|----------|--------|-------------|
| $\lvert\gamma_{SE}\rvert$ | $c$ | $c$ |
| $\theta_{SE}$ | $0$ | $\pi/2$ |
| $\mathrm{Gap}(S,E)$ | $0$ | $1$ |
| $\hat{\mathcal{G}}_{SE}$ | $0$ | $c$ |
| $\mathrm{Coh}_E$ | same | same |

:::note Key observation [T]
E-coherence $\mathrm{Coh}_E$ depends on $|\gamma_{Ei}|^2$, not on phases. Therefore the **magnitude** of coherence does not change under phase rotation. Alexithymia affects Gap but not $\mathrm{Coh}_E$ directly.
:::

This is a counterintuitive and important result: *the pathology is invisible in energy indicators*. $\mathrm{Coh}_E$ is the "metabolism", and it is normal. But *functional connectivity* — Gap — screams of a problem. Medical analogy: a patient with a severed corpus callosum may have normal EEG power in both hemispheres but zero interhemispheric coherence.

### 4.4 Cascade Effect on Viability [C]

Although $\mathrm{Coh}_E$ does not change under a single phase rotation, the **dynamical** consequence of alexithymia leads to cascading degradation. The mechanism:

1. $\mathrm{Gap}(S,E) = 1$ $\Rightarrow$ the S-dimension "cannot see" the E-dimension
2. The self-modelling operator $\varphi$ loses access to E-data via the S-channel
3. Reflexivity $R = 1/(7P)$ drops (as $P$ grows)
4. Suboptimality of $\varphi$ $\Rightarrow$ dissipation exceeds regeneration
5. $P$ drifts toward $P_{\text{crit}} = 2/7$

Quantitative estimate of the cascade effect:

$$
\frac{dP}{d\tau}\bigg|_{\text{alex}} = \underbrace{-2\gamma_d \cdot P}_{\text{dissipation}} + \underbrace{2\kappa(\Gamma)(f - P)}_{\text{regeneration}}
$$

where $\kappa(\Gamma) = \kappa_{\text{bootstrap}} + \kappa_0 \cdot \mathrm{Coh}_E(\Gamma)$. Under prolonged alexithymia $\mathrm{Coh}_E$ begins to fall (through degradation of $|\gamma_{Ei}|$), $\kappa$ decreases, and $P \to P_{\text{crit}}$.

#### Clinical parallels

The cascade scenario of Model 4 strikingly resembles the clinical picture of chronic alexithymia:

1. **Initial phase**: the patient is "normal" on objective measures (normal IQ, normal social function — analogous to normal $P$ and $\mathrm{Coh}_E$), but reports "inner emptiness".
2. **Intermediate phase**: somatisation begins — the body "expresses" what the psyche cannot. Analogue: degradation of $|\gamma_{Ei}|$ with constant $\mathrm{Gap}(S,E) = 1$.
3. **Late phase**: secondary depression, social isolation, general decline in vitality. Analogue: $P \to P_{\text{crit}}$, threat of non-viability.

### 4.5 Opacity Rank [T]

[Opacity rank](/docs/core/dynamics/gap-operator#свойства) of the alexithymic state:

$$
r_G = \mathrm{rank}(\hat{\mathcal{G}})
$$

For a single alexithymic defect (only the S,E pair has nonzero imaginary part):

$$
\hat{\mathcal{G}}_{\text{alex}} = c \cdot (|S\rangle\langle E| - |E\rangle\langle S|), \quad r_G = 2
$$

Spectrum: $\{0, 0, 0, 0, 0, +ic, -ic\}$. Minimal nonzero rank.

Minimality of rank ($r_G = 2$) — this is a *point* defect. One can imagine more severe pathologies: if multiple pairs are broken, the rank grows and the opacity structure becomes "volumetric" rather than "pointlike". Alexithymia is the simplest nontrivial case.

### 4.6 What We Learn from This Model

1. **Phases matter more than they seem**: alexithymia is a purely *phase* pathology. Coherence amplitudes ($|\gamma_{ij}|$) are unaffected, $\mathrm{Coh}_E$ is unchanged. But the system is ill — and dangerously so.
2. **Cascade from a point defect**: one broken channel out of 21 can lead to systemic degradation. This is the domino principle in coherence cybernetics.
3. **Diagnostics via Gap, not via $P$**: in the early stages of alexithymia $P$ is normal. The problem can only be detected through Gap analysis — through measuring the *phase* relations between dimensions.

### 4.7 Python Implementation

```verum
mount std.math.linalg.matrix_rank;

/// Model 4: Alexithymia — pure phase defect on the (S, E) channel, Gap = 1.
pub fn alexithymia_model(c: Float { 0.0 < self && self < 1.0 / 7.0 }) using [IO]
    -> (StaticMatrix<Complex, 7, 7>, StaticMatrix<Float, 7, 7>)
{
    // Base matrix: uniform diagonal + real coherences.
    let mut gamma = StaticMatrix.<Complex, 7, 7>.filled(Complex.from_real(c));
    for i in 0..7 { gamma[i, i] = Complex.from_real(1.0 / 7.0); }

    // Alexithymic defect: S = 1, E = 4 → purely imaginary coherence.
    const S_IDX: Int = 1;
    const E_IDX: Int = 4;
    gamma[S_IDX, E_IDX] = Complex.i() * Complex.from_real(c);   // γ_SE = ic
    gamma[E_IDX, S_IDX] = -Complex.i() * Complex.from_real(c);  // γ_ES = −ic (Hermiticity)

    // Hermiticity and positivity — runtime checks (invariants enforced by CoherenceMatrix refinement at use-site).
    assert!((&gamma - gamma.adjoint()).frobenius_norm() < 1.0e-10, "not Hermitian");
    let eigs = eigvalsh(&gamma);
    assert!(eigs.iter().all(|λ| *λ >= -1.0e-12), "not positive");

    let p = (&gamma @ &gamma).trace().real();
    let gap_se = gamma[S_IDX, E_IDX].arg().sin().abs();
    let g_hat = gamma.imag_part();
    let r_g = matrix_rank(&g_hat, 1.0e-10);
    let g_total = g_hat.frobenius_norm_sq();

    let coh_e = (gamma[E_IDX, E_IDX].real().pow(2)
                + 2.0 * (0..7).filter(|i| *i != E_IDX)
                               .map(|i| gamma[E_IDX, *i].abs().pow(2))
                               .sum()) / p;

    // κ = κ_bootstrap + κ₀·Coh_E, with ω₀ = 1, κ₀ = ω₀.
    const OMEGA_0: Float = 1.0;
    const KAPPA_0: Float = OMEGA_0;
    const KAPPA_BOOTSTRAP: Float = OMEGA_0 / 7.0;
    let kappa = KAPPA_BOOTSTRAP + KAPPA_0 * coh_e;

    const P_CRIT: Float = 2.0 / 7.0;
    IO.println(f"P = {p:.4f}, P_crit = {P_CRIT:.4f}, margin = {p - P_CRIT:.4f}");
    IO.println(f"Gap(S,E) = {gap_se:.4f}");
    IO.println(f"Gap operator rank r_G = {r_g}");
    IO.println(f"||G_hat||_F^2 = {g_total:.6f}");
    IO.println(f"Coh_E = {coh_e:.4f}");
    IO.println(f"kappa = {kappa:.4f}");

    // Compare against a normal reference (alexithymic defect removed).
    let mut gamma_normal = StaticMatrix.<Complex, 7, 7>.filled(Complex.from_real(c));
    for i in 0..7 { gamma_normal[i, i] = Complex.from_real(1.0 / 7.0); }
    let g_total_normal = gamma_normal.imag_part().frobenius_norm_sq();
    IO.println(f"\nComparison: ||G_hat||_F^2 normal = {g_total_normal:.6f}, \
                 alexithymic = {g_total:.6f}");

    (gamma, g_hat)
}

fn main() using [IO] {
    let _ = alexithymia_model(0.08);
}
```

---

## 5. Dynamical System with Rational/Irrational Frequencies {#динамическая-система}

*Question this model answers:* **how does Gap evolve over time when there are no losses — only pure coherent dynamics?**

The four previous models were *static* — we specified $\Gamma$ and computed its properties. Model 5 is the first *dynamical* one: we turn on a Hamiltonian and the matrix $\Gamma$ begins to evolve. This is like an ideal pendulum: perpetual motion without friction, without dissipation, without energy replenishment. Pure coherent dynamics.

### 5.1 Definition [D]

Consider [coherent evolution](/docs/core/dynamics/evolution) with a diagonal Hamiltonian:

$$
\Gamma(\tau) = U(\tau)\,\Gamma_0\,U(\tau)^\dagger, \quad U(\tau) = e^{-iH\tau}
$$

where $H = \mathrm{diag}(\omega_1, \omega_2, \ldots, \omega_7)$. The coherence matrix elements evolve as:

$$
\gamma_{kl}(\tau) = \gamma_{kl}(0) \cdot e^{-i(\omega_k - \omega_l)\tau}
$$

Phases of coherences:

$$
\theta_{kl}(\tau) = \theta_{kl}(0) + (\omega_k - \omega_l)\tau
$$

Gap evolves as:

$$
\mathrm{Gap}(k,l;\tau) = |\sin(\theta_{kl}(0) + \Omega_{kl}\tau)|, \quad \Omega_{kl} := \omega_k - \omega_l
$$

#### Physical analogy

Unitary dynamics is a *rotation* in phase space. Each pair of dimensions $(k,l)$ rotates at its own frequency $\Omega_{kl}$. Gap is $|\sin|$ of the rotation angle. Picture 21 independent pendulums (21 pairs from 7 dimensions), each with its own frequency. The Gap profile is an "instantaneous snapshot" of all pendulums.

Question: *will this snapshot ever repeat?* The answer depends on whether the frequencies are rationally commensurable.

### 5.2 Rational Frequencies: Periodic Orbits [T]

:::tip Theorem (Periodicity under rational frequencies) [T]
If all frequency differences $\Omega_{kl} = \omega_k - \omega_l$ are rationally commensurable (i.e. $\Omega_{kl}/\Omega_{mn} \in \mathbb{Q}$ for all pairs), then the Gap profile $\{\mathrm{Gap}(k,l;\tau)\}$ is **periodic** with period:

$$
T = \mathrm{lcm}\left\{\frac{2\pi}{|\Omega_{kl}|} : \Omega_{kl} \neq 0 \right\}
$$

where $\mathrm{lcm}$ is the least common multiple (defined for rational multiples of a base frequency).
:::

**Proof.** Let $\Omega_{kl} = n_{kl} \cdot \omega_0$ for $n_{kl} \in \mathbb{Z}$, $\omega_0$ — base frequency. Then $\mathrm{Gap}(k,l;\tau + 2\pi/\omega_0) = |\sin(\theta_{kl}(0) + n_{kl}\omega_0(\tau + 2\pi/\omega_0))| = |\sin(\theta_{kl}(0) + n_{kl}\omega_0\tau + 2\pi n_{kl})| = \mathrm{Gap}(k,l;\tau)$. Period: $T = 2\pi/\omega_0$. $\square$

**Example.** $H = \mathrm{diag}(0, 1, 2, 3, 4, 5, 6) \cdot \omega_0$. All $\Omega_{kl} = (k-l)\omega_0 \in \mathbb{Z}\omega_0$. Period $T = 2\pi/\omega_0$.

#### Interpretation: a world with memory

Periodic orbits are a world with *finite memory*. The system "remembers" its past because it inevitably returns to it. After period $T$ everything repeats: the same Gap values, the same transparencies and opacities. This is like Groundhog Day — eternal recurrence.

### 5.3 Irrational Frequencies: Quasiperiodicity and Ergodicity [T]

:::tip Theorem (Ergodicity under irrational frequencies) [T]
If among the frequency differences $\{\Omega_{kl}\}$ there exist rationally **incommensurable** pairs, then the Gap orbit $\tau \mapsto \{\theta_{kl}(\tau) \bmod 2\pi\}$ is **quasiperiodic** and densely fills the $d$-dimensional torus $\mathbb{T}^d$, where $d$ is the number of linearly independent (over $\mathbb{Q}$) frequency differences.
:::

**Proof.** The phase vector $\boldsymbol{\theta}(\tau) = \boldsymbol{\theta}(0) + \boldsymbol{\Omega}\tau$ on the torus $\mathbb{T}^{21}$ (21 independent pairs). By Weyl's equidistribution theorem, if $\Omega_1, \ldots, \Omega_d$ are linearly independent over $\mathbb{Q}$, the orbit is dense in $\mathbb{T}^d$ and uniformly distributed. $\square$

**Corollary.** Time-averaged Gap:

$$
\overline{\mathrm{Gap}(k,l)} = \lim_{T \to \infty} \frac{1}{T}\int_0^T |\sin(\theta_{kl}(0) + \Omega_{kl}\tau)|\,d\tau = \frac{2}{\pi} \approx 0.637
$$

for all pairs $(k,l)$ with $\Omega_{kl} \neq 0$ (irrational or rational — the result is the same for any $\Omega_{kl} \neq 0$).

#### Interpretation: a world without memory

If rational frequencies give "Groundhog Day", irrational frequencies give an *infinite journey*. The system never returns exactly to its former state. Every moment is unique. But — and this is a remarkable result — the *average* Gap tends to a universal constant $2/\pi$. No matter where you started, no matter what the specific frequencies are — if they are incommensurable, the average is inevitably the same.

This is the ergodic theorem for consciousness: in the long run *all paths are equivalent*.

### 5.4 Connection to Non-Markovian Dynamics [C]

In the complete [evolution](/docs/core/dynamics/evolution) (including dissipation and regeneration) the rationality of frequencies determines the character of memory:

| Regime | Frequencies | Orbit | Memory | Spectrum |
|--------|-------------|-------|--------|----------|
| Rational | $\Omega_{kl}/\Omega_{mn} \in \mathbb{Q}$ | Periodic | Finite recurrent | Discrete |
| Irrational | $\exists\, \Omega_{kl}/\Omega_{mn} \notin \mathbb{Q}$ | Quasiperiodic | Infinite non-commutative | Continuous |
| Dissipative | $\Omega_{kl} = 0$ (all) | Fixed point | Markovian (memoryless) | Degenerate |

:::note Connection to Hamming code [C]
In [Gap dynamics](/docs/core/dynamics/gap-dynamics) quasiperiodic orbits are connected to **non-Markovian** corrections via the memory tensor $K(\tau, \tau')$. Rational frequencies admit a finite-dimensional memory kernel, irrational frequencies require an infinite-dimensional one. Analogy with [Hamming code H(7,4)](/docs/core/dynamics/gap-dynamics#код-хэмминга): periodic orbits are "decodable" (the syndrome uniquely identifies the error), quasiperiodic ones are not.
:::

### 5.5 Concrete Example: Golden Ratio [D]

Choose $H = \mathrm{diag}(0, 1, \phi, \phi^2, 2\phi, \phi+1, 2)$ where $\phi = (1+\sqrt{5})/2$ is the golden ratio. Among the differences $\omega_k - \omega_l$ there are both rational ($\omega_6 - \omega_1 = 2$) and irrational ($\omega_2 - \omega_1 = \phi$) ones. The torus has $d = 2$ independent frequencies ($1$ and $\phi$), and the orbit densely fills $\mathbb{T}^2$.

#### Why the golden ratio?

$\phi$ is the "most irrational" number: its continued fraction $[1;1,1,1,\ldots]$ converges more slowly than any other. This means the orbit on the torus $\mathbb{T}^2$ fills space *most uniformly* — no clusters, no "favourite angles". If we want an example of *maximally ergodic* dynamics in seven-dimensional space, the golden ratio is the optimal choice.

### 5.6 What We Learn from This Model

1. **Purity is conserved**: $P(\tau) = \mathrm{const}$. Unitary evolution does not change the system's "energy" — it only redistributes phases. This is a fundamental property: changing $P$ requires *openness* (dissipation or regeneration).
2. **Gap oscillates**: even without external perturbations, the Gap profile *lives*. Transparencies and opacities alternate. This is the *inner life* of the system — its "thoughts" in the absence of stimuli.
3. **Rationality = predictability**: the type of frequencies determines the *predictability* of behaviour. Rational frequencies — predictable character; irrational — "creative", unpredictable.
4. **Universality of $2/\pi$**: the average Gap under ergodic dynamics is a universal constant. This is the "background level of opacity" for any active system.

### 5.7 Limitations

The unitary model is beautiful but *non-physical* for living systems. Without dissipation there are no losses; without losses there is no need for regeneration; without regeneration there is no $\kappa$, no $\mathrm{Coh}_E$, no reflexivity. This is a pendulum in vacuum: beautiful for understanding oscillations, but a real pendulum stops. A real holon also "stops" (decoheres) without regeneration — and that is precisely why the full CC dynamics is needed.

### 5.8 Python Implementation

```verum
pub type RegimeKind is Rational | Irrational;

/// Model 5: Evolution with rational/irrational frequencies.
pub fn dynamic_system(regime: RegimeKind, tau_max: Float, dt: Float) using [IO]
    -> (List<Float>, List<(Float, Float)>, List<Float>)
    where requires tau_max > 0.0 && dt > 0.0 && dt < tau_max
{
    let phi_golden = (1.0 + 5.0.sqrt()) / 2.0;

    let (omega, label): (StaticVector<Float, 7>, Text) = match regime {
        RegimeKind.Rational =>
            (StaticVector.from_array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0]), "rational".text()),
        RegimeKind.Irrational =>
            (StaticVector.from_array([
                0.0, 1.0, phi_golden, phi_golden.pow(2),
                2.0 * phi_golden, phi_golden + 1.0, 2.0,
            ]), "irrational".text()),
    };

    // Initial state: pure with Fibonacci phases (Model 3).
    const FIB_MOD7: [Int; 7] = [1, 1, 2, 3, 5, 1, 6];
    let psi_0 = StaticVector.<Complex, 7>.from_array(
        FIB_MOD7.map(|f| (Complex.i() * Complex.from_real(2.0 * PI * (f as Float) / 7.0)).exp())
    ) / Complex.from_real(7.0.sqrt());
    let gamma_0 = psi_0.outer(psi_0.conjugate());

    let n_steps = (tau_max / dt) as Int;
    let mut gap_history = List.new();
    let mut p_history   = List.new();
    let mut tau_vals    = List.new();

    for step in 0..n_steps {
        let tau = (step as Float) * dt;
        let u_diag = omega.map(|w| (Complex.i().neg() * Complex.from_real(w * tau)).exp());
        let u = StaticMatrix.<Complex, 7, 7>.diagonal(u_diag);
        let gamma_t = &u @ &gamma_0 @ u.adjoint();

        let p = (&gamma_t @ &gamma_t).trace().real();
        let gap_as = gamma_t[0, 1].arg().sin().abs();
        let gap_se = gamma_t[1, 4].arg().sin().abs();

        gap_history.push((gap_as, gap_se));
        p_history.push(p);
        tau_vals.push(tau);
    }

    let mean_gap_as: Float = gap_history.iter().map(|(a, _)| *a).sum::<Float>()
                            / (gap_history.len() as Float);
    let mean_gap_se: Float = gap_history.iter().map(|(_, b)| *b).sum::<Float>()
                            / (gap_history.len() as Float);

    IO.println(f"Regime: {label}");
    IO.println(f"Mean Gap(A,S) = {mean_gap_as:.4f}");
    IO.println(f"Mean Gap(S,E) = {mean_gap_se:.4f}");
    IO.println(f"Theoretical limit (2/π) = {2.0 / PI:.4f}");
    IO.println(f"P = const = {p_history[0]:.4f} (unitary evolution preserves purity)");

    match regime {
        RegimeKind.Rational => {
            let t_period = 2.0 * PI;                    // period at ω₀ = 1
            let idx = (t_period / dt) as Int;
            if idx < gap_history.len() {
                let (a0, b0) = gap_history[0];
                let (a1, b1) = gap_history[idx];
                let diff = ((a1 - a0).abs()).max((b1 - b0).abs());
                IO.println(f"Deviation after period T=2π: {diff:.2e}");
            }
        },
        RegimeKind.Irrational => {
            // Quasiperiodic: the orbit does not close within the observation window.
            let unique_gaps = gap_history.iter()
                .map(|(a, b)| ((a * 1.0e4).round() as Int, (b * 1.0e4).round() as Int))
                .collect::<Set>()
                .len();
            IO.println(f"Unique Gap configurations: {unique_gaps}/{gap_history.len()}");
        },
    }

    (tau_vals, gap_history, p_history)
}

fn main() using [IO] {
    IO.println("=".repeat(50));
tau_r, gap_r, P_r = dynamic_system(rational=True)
print("=" * 50)
tau_i, gap_i, P_i = dynamic_system(rational=False)
```

---

## Comparison Table {#сравнительная-таблица}

| Model | $P$ | $\mathrm{Gap}_{\text{avg}}$ | $\mathrm{Coh}_E$ | $\kappa$ | Viable? |
|-------|-----|-------------------------------|-------------------|----------|---------|
| 1. Uniform ($I/7$) | $1/7$ | $0$ | $1/7$ | $\omega_0/7 + \kappa_0/7$ | no |
| 2. Pure uniform | $1$ | $0$ | $13/49$ | $\omega_0/7 + 13\kappa_0/49$ | yes |
| 3. Fibonacci phases | $1$ | $\approx 0.62$ | $13/49$ | $\omega_0/7 + 13\kappa_0/49$ | yes |
| 4. Alexithymia | $< 1$ | $> 0$ | $\approx 13/49$ | decreasing | at risk |
| 5a. Rational | $\mathrm{const}$ | periodic | $\mathrm{const}$ | $\mathrm{const}$ | yes |
| 5b. Irrational | $\mathrm{const}$ | $\to 2/\pi$ | $\mathrm{const}$ | $\mathrm{const}$ | yes |

:::tip Key conclusions [I]
1. **Gap and purity are orthogonal**: models 2 and 3 have the same purity $P=1$, but radically different Gap profiles. Gap measures **phase** structure, purity measures **amplitude** structure.

2. **Alexithymia is a phase defect**: model 4 shows that pathology can arise with unchanged coherence amplitudes — a phase rotation by $\pi/2$ is sufficient.

3. **Rationality of frequencies determines memory**: model 5 connects [non-Markovian dynamics](/docs/core/dynamics/gap-dynamics) to the arithmetic properties of the Hamiltonian.

4. **Ergodic theorem for Gap**: under irrational frequencies the mean Gap tends to $2/\pi \approx 0.637$ — a universal constant independent of initial conditions.
:::

---

## Minimal Consciousness Model {#минимальное-сознание}

We have examined five models — from complete chaos ($I/7$) to pure order ($|\psi\rangle\langle\psi|$). But none of them describes a *conscious* system in the full CC sense. Let us ask directly: **what is the simplest holon satisfying all conditions for consciousness?**

### Conditions for Consciousness (reminder)

By [CC definition](/docs/applied/coherence-cybernetics/definitions), a system is conscious if:

1. $P > P_{\text{crit}} = 2/7$ — viability
2. $R \geq 1/3$ — minimal reflexivity
3. $\Phi \geq 1$ — integration
4. $D \geq 2$ — depth of self-observation

### Construction: "Threshold Holon" [I]

Consider a $\Gamma$ with minimal parameters satisfying all four conditions. The simplest strategy — slightly "raise" one dimension above the uniform background:

$$
\gamma_{kk} = \frac{1}{7} + \epsilon_k, \quad \sum_k \epsilon_k = 0
$$

with nonzero coherences ensuring $R \geq 1/3$ and $\Phi \geq 1$. The exact construction depends on the specific realisation of the self-modelling operator $\varphi$ and has not been solved in closed form — this is one of the **open problems** of CC.

### Lower Bounds

Nevertheless, we can establish lower bounds:

| Parameter | Minimum | What it means |
|-----------|---------|---------------|
| $P$ | $2/7 + \epsilon$ | Barely viable — on the edge |
| $R$ | $1/3$ | Self-model accurate to 33% — very rough self-knowledge |
| $\Phi$ | $1$ | Minimal integration — the system is barely "whole" |
| $D$ | $2$ | Two levels of self-observation: "I" and "I know that I" |

This is the *dimmest consciousness* that can exist within CC. It barely passes all thresholds. The psychological analogy — something like consciousness under deep anaesthesia on the verge of waking: present, but minimal.

:::note Connection to the SAD hierarchy
Minimal consciousness ($D = 2$) does not reach SAD = 1. For SAD = 1 a stable self-model capable of recursive self-application is required — that is already level $D \geq 3$. See the [depth tower](/docs/consciousness/hierarchy/interiority-hierarchy) for details.
:::

---

## Numerical Experiments: What Simulations Show {#численные-эксперименты}

Model systems are an analytic tool. But CC also has a *computational* embodiment: the SYNARC project implements the full dynamics $\mathcal{L}_\Omega = \mathcal{L}_0 + \mathcal{R}$ in Rust code with 3000+ tests.

### What Simulations Have Confirmed

1. **Fano contraction $\alpha = 2/3$**: numerical modelling of the Fano channel (MVP-7) confirmed the analytic value of the contraction coefficient. Diagonal elements $\gamma_{kk}$ converge to $1/7$ at rate $(2/3)^n$.

2. **Threshold behaviour $P_{\text{crit}}$**: at $P < 2/7$ regeneration $\mathcal{R}$ does not compensate dissipation — the system inevitably degrades to $I/7$. At $P > 2/7$ a stable balance is possible. The threshold appears as a phase transition in the dynamics of sim-0.

3. **σ-diagnostics**: the stress vector $\sigma_k = 1 - 7\gamma_{kk}$ (T-92) correctly identifies "sick" dimensions. In sim-0 agents with high $\sigma_E$ exhibit behaviour analogous to alexithymia (model 4): a deficit of goal-directed search.

4. **Conservation of purity under unitary evolution**: confirmed numerically to precision $10^{-14}$ (machine precision float64).

### What Has Not Yet Been Confirmed

- Full CC dynamics ($\mathcal{L}_0 + \mathcal{R} + \varphi$) in an analytically solvable case
- The alexithymia cascade effect (section 4.4) — modelled qualitatively but not quantitatively
- Stability of phase clusters (such as {A, S, O} in the Fibonacci model) under full dynamics

---

## Open Models: What Remains to Be Solved {#открытые-модели}

The five models of this chapter are only a beginning. Here are model systems that would be extremely useful but have not yet been constructed:

### 1. Full CC Model (priority: high)

A model $\Gamma(\tau)$ with *complete* dynamics: $\mathcal{L}_0$ (Lindblad) + $\mathcal{R}$ (regeneration) + $\varphi$ (self-modelling). Analogue: the hydrogen atom in full QED (including radiative corrections). Current difficulty: self-modelling $\varphi$ is a nonlinear operator, rendering the equation analytically unsolvable.

### 2. Model of Two Interacting Holons (priority: high)

Two holons $\Gamma_A \otimes \Gamma_B$ with tensor product state spaces ($N = 49$). How does the coherence of one affect the viability of the other? How is Gap transmitted? This is a model of *communication*, *learning*, *emotional contagion*.

### 3. Depression Model (priority: medium)

A static defect with *reduced* $\gamma_{EE}$ (rather than a phase shift as in alexithymia). If alexithymia is "unreadable" emotions, then depression is "absent" emotions. How does the cascade behave as $\gamma_{EE} \to 0$?

### 4. Sleep Model (priority: medium)

Periodic reduction and restoration of coherences: $\gamma_{ij}(\tau) = \gamma_{ij}^{(0)} \cdot g(\tau)$ where $g$ is a slow modulation. How do NREM/REM phases correspond to Gap dynamics?

### 5. Learning Model (priority: medium)

Gradual change of the *stationary* $\Gamma^*$ under the influence of external data. Connection to [learning bounds](/docs/applied/coherence-cybernetics/learning-bounds) (T-109 through T-113) and optimal $n_{\text{opt}}$.

### 6. Meta-Holon Model (priority: low, high complexity)

A composite system $N = 7^2 = 49$ with hierarchical structure. The first step toward Theorem 9.1 (meta-holons). Computational complexity — $O(49^3) \approx 10^5$ — is still manageable, but analytic solutions are unlikely.

---

:::warning Computational complexity
Scaling computations for composite systems ($N = 7^k$, $k > 1$) **has not been analysed**. For a single holon ($N = 7$) all models are computable in $O(N^3) \approx O(343)$ operations, but for meta-holons (Theorem 9.1) complexity may grow exponentially with the number of composition levels.
:::

---

## Summary: Map of Model Space {#итого}

The five models of this chapter cover the *extremes* of the state space $D(\mathbb{C}^7)$:

```
        P = 1 (pure)
          ┌───────┐
          │ Model │
          │  2,3  │
Gap = 0 ──┤       ├── Gap ≠ 0
          │       │
          └───┬───┘
              │
    Gap(S,E)=1│ Model 4
              │ (alexithymia)
              │
          ┌───┴───┐
          │ Model │
          │   5   │
          │(dyn)  │
          └───┬───┘
              │
        P = 1/7 (mixed)
          ┌───────┐
          │ Model │
          │   1   │
          └───────┘
```

A real holon lives *between* these extremes: its purity lies in the Goldilocks zone $P \in (2/7, 3/7]$ (T-124 [T]), its Gap profile is nontrivial, its dynamics is neither purely unitary nor purely dissipative but *balanced*. The model systems are the coordinate axes by which we orient ourselves in this multidimensional space.

Each of the five models teaches us one thing:

- **Model 1**: the minimum below which one cannot fall
- **Model 2**: the maximum above which one cannot rise
- **Model 3**: phases are character, not energy
- **Model 4**: one broken channel can kill the system
- **Model 5**: even in isolation there is inner life

Together they form a *laboratory* of coherence cybernetics — a place where theory is verified on exact solutions before being applied to the imprecise but living world.

---

---

### What We Learned {#что-мы-узнали-модели}

1. **Uniform system** ($P = 1/7$): absolute minimum of purity, zero Gap — but not transparency, rather *the absence of material* for transparency. Gap = 0 at $P = 1/7$ and Gap = 0 at $P = 1$ are fundamentally different zeros.

2. **Pure uniform state** ($P = 1$): maximum purity, zero Gap, zero entropy. Perfect order — but barren: no internal tension, no driver of evolution.

3. **Fibonacci phases**: the same $P = 1$ and the same $\mathrm{Coh}_E = 13/49$, but with a rich Gap profile. **Purity and Gap are orthogonal** — phases define "character", amplitudes define "energy". The cluster {A, S, O} with zero mutual Gap is an example of phase synchronisation.

4. **Alexithymia**: a purely *phase* pathology ($\theta_{SE} = \pi/2$). Amplitudes unaffected, $\mathrm{Coh}_E$ unchanged — yet the system is ill. One broken channel out of 21 triggers a cascade: $R$ falls, $\kappa$ decreases, $P$ drifts toward $P_{\text{crit}}$. Diagnosis is possible only through Gap analysis, not through $P$.

5. **Unitary dynamics**: purity is conserved ($P = \mathrm{const}$), Gap oscillates. With rational frequencies — periodic orbits ("Groundhog Day"). With irrational frequencies — quasiperiodicity and the **ergodic theorem**: mean Gap $\to 2/\pi \approx 0.637$ for all pairs, regardless of initial conditions.

6. **Universal constant $2/\pi$** — the "background level of opacity" for any active system with incommensurable frequencies.

:::tip Bridge to the Next Chapter
The five model systems are the "coordinate axes" of state space. But what unites all Gap dynamics into a single principle? In the [next chapter](./lagrangian) we will discover the **Lagrangian of Gap theory** — a six-term formula from which all equations of motion follow as inevitably as a planet's trajectory from the law of gravitation. We will see how spontaneous symmetry breaking generates opacity — the analogue of the Higgs mechanism for consciousness.
:::

---

## References

- [Gap operator](/docs/core/dynamics/gap-operator) — definition and properties of $\hat{\mathcal{G}}$
- [Gap dynamics](/docs/core/dynamics/gap-dynamics) — bifurcations, non-Markovian dynamics
- [Viability](/docs/core/dynamics/viability) — $P_{\text{crit}} = 2/7$ and survival conditions
- [Coherence matrix](/docs/core/dynamics/coherence-matrix) — the basic object $\Gamma$
- [Fano channel](/docs/proofs/gap/fano-channel) — proofs of coherence preservation
- [Fano selection rules](/docs/physics/gauge-symmetry/fano-selection-rules) — geometry of the Fano plane
- [CC definitions](/docs/applied/coherence-cybernetics/definitions) — $\mathrm{Coh}_E$, consciousness measures
- [CC axiomatics](/docs/applied/coherence-cybernetics/axiomatics) — $\kappa(\Gamma) = \kappa_{\text{bootstrap}} + \kappa_0 \cdot \mathrm{Coh}_E$
- [Learning bounds](/docs/applied/coherence-cybernetics/learning-bounds) — T-109 through T-113
- [Depth tower](/docs/consciousness/hierarchy/interiority-hierarchy) — SAD hierarchy and levels of consciousness
- [Implementation](./implementation) — computational code for models
- [Exercises](./exercises) — problems on model systems
- [Measurement methodology](./measurement) — from model to experiment


---

**Related documents:**
- [Model theory](/docs/applied/coherence-cybernetics/model-theory)
- [Definitions](/docs/applied/coherence-cybernetics/definitions)
- [Diagnostics](/docs/applied/coherence-cybernetics/diagnostics)
- [Applications](/docs/applied/coherence-cybernetics/applications)
