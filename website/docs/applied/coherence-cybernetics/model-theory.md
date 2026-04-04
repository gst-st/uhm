---
sidebar_position: 5
title: Model Theory
description: Formal specification and categorical semantics of CC
---

# Model Theory of CC

:::info Bridge from the Previous Chapter
In the [previous chapter](./theorems) we proved the fundamental theorems of CC: from the existence of dynamics to the impossibility of zombies and emergence. Those theorems form a powerful formal apparatus. But to understand its *limits*, one must ask the question mathematicians have been asking since the 1930s: *what are* these theorems about? Does a concrete mathematical structure exist in which all CC axioms are true? Is it unique? How does CC *relate* to other theories of consciousness? Model theory answers these questions rigorously.
:::

:::tip Chapter Roadmap
In this chapter we:
1. **Understand what model theory is** and why CC needs it (section "[What Is Model Theory](#что-такое-теория-моделей)")
2. **Define the formal signature** of CC — its "alphabet": sorts, functions, predicates (section "[Signature of the Theory](#что-такое-сигнатура)")
3. **Build the standard model** $\mathfrak{M}_{\mathrm{CC}}$ — the canonical interpretation of all symbols (section "[Standard Model](#что-значит-иметь-модель)")
4. **Investigate soundness and completeness** — what can and cannot be proved (section "[Soundness and Completeness](#корректность-полнота-введение)")
5. **Examine non-standard models** — can CC be interpreted differently? (section "[Non-Standard Models](#нестандартные-модели)")
6. **Build categorical semantics** — the category of Holons $\mathbf{Hol}$ and its properties (section "[Categorical Semantics](#зачем-нужны-категории)")
7. **Define functor bridges** to IIT, FEP, GNW — CC as a metatheory (section "[Translatability](#переводимость)")
8. **Define the limits of explanation** — what CC can and cannot explain (section "Limits of Explanation")
:::

:::note A Note on Notation
In this document:
- $\Gamma$ — [coherence matrix](/docs/core/dynamics/coherence-matrix)
- $\mathbb{H}$ — [Holon](/docs/core/structure/holon)
- $\mathbf{Hol}$ — [category of Holons](/docs/proofs/categorical/categorical-formalism)
- $\mathbf{DensityMat}$ — [category of density matrices](/docs/proofs/categorical/categorical-formalism#1-категория-densitymat)
- $\mathbf{Exp}$ — [category of experiential states](/docs/proofs/categorical/categorical-formalism#2-категория-exp)
- $\varphi$ — [self-modelling operator](/docs/proofs/categorical/formalization-phi)
:::

## What Is Model Theory and Why CC Needs It {#что-такое-теория-моделей}

Consider a language — say, English. The language itself is a set of rules: grammar, syntax, phonetics. But a language *means* something only when its words denote objects in the world. The word "table" acquires meaning when we point to a concrete object: *this* table — wooden, on four legs, standing in the kitchen. The link between a word and an object is an *interpretation*.

Model theory, founded by Alfred Tarski in the 1930s, formalises precisely this connection — but for mathematical theories. If a theory is a set of axioms and inference rules (analogous to a grammar), then a **model** is a concrete mathematical structure in which all axioms turn out to be true (analogous to a world in which the language "works").

The central concept of model theory is the **satisfaction relation**, written $\mathfrak{M} \vDash \phi$: "model $\mathfrak{M}$ satisfies formula $\phi$". This is exactly "pointing to the table" — we check whether the statement of the theory actually holds in the given concrete structure.

### Why This Is Needed for CC

Coherence Cybernetics is a formal theory. It makes statements like "a viable system has purity $P > 2/7$" or "consciousness requires reflection $R \geq 1/3$". But *what* are these statements about? What are the "tables" and "chairs" of CC?

Model theory forces us to answer this question rigorously:

1. **Fix the language** — which symbols CC uses, which types of objects it has (signature).
2. **Build a canonical interpretation** — show that a concrete mathematical structure exists in which all axioms are true (standard model).
3. **Verify consistency** — ensure the axioms do not lead to contradictions (soundness).
4. **Understand the limits** — find out whether all truths of CC can be proved from the axioms (completeness), and whether other interpretations exist (non-standard models).

Without model theory, CC would be a collection of formulas with no explicit indication of *what* these formulas are about. With model theory, CC becomes a theory *about something concrete* — about coherence matrices $\Gamma \in \mathcal{D}(\mathbb{C}^7)$, their evolution, and the experiential structures they generate.

### Historical Perspective

The importance of model theory for the science of consciousness can hardly be overstated. In physics, the language of a theory (say, Maxwell's equations) and its models (electromagnetic fields in spacetime) are clearly separated — nobody confuses an equation with what it describes. But in consciousness science this confusion is pervasive: IIT, GNW, and FEP theories often do not distinguish the formal apparatus from its subject domain. CC, through model theory, makes this distinction explicit — and, as we shall see, this is precisely what makes it possible to build *functor bridges* between different theories of consciousness.

## CC as a Formal Theory: Levels of Rigour {#кк-как-формальная-теория}

Not all theories of consciousness are equally formalised. It is useful to distinguish levels of rigour:

| Level | Description | Examples |
|-------|-------------|---------|
| 0. Metaphor | Qualitative descriptions without formalisation | "Consciousness is a property of complex systems" |
| 1. Semi-formal | Some formulas, no complete axiomatics | GNW (Global Neuronal Workspace) |
| 2. Formal theory | Explicit axioms and consequences, but no meta-analysis | IIT 3.0, FEP |
| 3. Model-theoretic | Signature + axioms + standard model + soundness | **CC** |
| 4. Categorical | Functor connections between theories, structural theorems | CC (this chapter) |

CC is the only existing theory of consciousness that operates at levels 3 and 4. This does not mean CC is "better" than other theories in some absolute sense — but it means it is more *transparent* in its assumptions and more *testable* in its consequences.

:::info Comparison with IIT
IIT (Integrated Information Theory) operates at level 2: it defines $\Phi$ formally and derives consequences, but has no explicit signature, standard model, or completeness theorems. In particular, IIT does not separate syntax (formulas for $\Phi$) and semantics (what exactly those formulas are about). CC, by contrast, builds a *functor* $F_{\mathrm{IIT}}: \mathbf{Hol} \to \mathbf{IIT}$ that makes this relationship precise.
:::

## Signature of the Theory

### What Is a Signature {#что-такое-сигнатура}

A signature is the *alphabet* of a formal theory. Just as a natural language has nouns, verbs, and adjectives, the signature of a formal theory has:

- **Sorts** — types of objects the theory can speak about. These are the *nouns* of the CC language: "coherence matrix", "Holon", "real number". Sorts define the *ontology* of the theory — which entities exist in it.

- **Functions** — operations that transform some objects into others. These are the *verbs* of the CC language: "compute purity", "evolve", "find the spectrum". Each function has a *type* — which objects it takes as input and what it returns.

- **Predicates** — properties and relations that can be true or false. These are the *adjectives* of the CC language: "viable", "conscious", "having interiority". Predicates define the *classification* of objects.

- **Axioms** — statements accepted without proof, defining the "rules of the game". These are the *grammar* of the CC language.

The analogy with language is superficial but useful: just as knowing the alphabet and grammar allows one to understand texts, knowing the signature allows one to understand CC theorems. A person seeing the formula $P(\Gamma) > P_{\text{crit}}$ without the signature will understand nothing; with the signature — they will understand that $P$ is a function (purity) applied to an object of sort $\Gamma$ (coherence matrix) and the result is compared with a constant.

### Formal Definition {#определение-сигнатуры}

**Definition (Signature $\Sigma_{\mathrm{CC}}$):**

$$
\Sigma_{\mathrm{CC}} = \langle \mathrm{Sorts}, \mathrm{Functions}, \mathrm{Predicates}, \mathrm{Axioms} \rangle
$$

The signature $\Sigma_{\mathrm{CC}}$ fixes the *entire* language of CC. Every statement of the theory — from the simplest inequality to the deepest theorems about consciousness — is written using the symbols of this signature. Outside the signature CC can say nothing: this is the precise definition of the theory's subject domain.

### Sorts

The sorts of CC are minimal — there are exactly as many as are needed to formulate the axioms. Each sort corresponds to a well-defined mathematical object:

| Sort | Notation | Interpretation | Ref |
|------|----------|----------------|-----|
| $\Gamma$ | `CoherenceMatrix` | Coherence matrix | [→](/docs/core/dynamics/coherence-matrix) |
| $\mathbb{H}$ | `Holon` | Holon | [→](/docs/core/structure/holon) |
| $\mathcal{H}$ | `HilbertSpace` | State space $\mathbb{C}^7$ ([justification](/docs/core/foundations/axiom-omega#октонионная-структура)) | [→](/docs/core/structure/dimensions) |
| $\mathbb{R}$ | `Real` | Real numbers | — |
| $\mathbb{C}$ | `Complex` | Complex numbers | — |
| $\mathbb{N}$ | `Natural` | Natural numbers | — |

Two special features deserve attention. First, the sort $\Gamma$ is *not* an arbitrary matrix, but a density matrix: Hermitian, positive semi-definite, with unit trace. These constraints are not axioms of the theory, but part of the *definition* of the sort (analogously to how in arithmetic "natural number" is not just any symbol but a specific type of object).

Second, fixing $\mathcal{H} = \mathbb{C}^7$ is a consequence of the Axiom of Septicity, not an arbitrary choice. The dimension 7 is derived from the structure of the octonion algebra and is the only dimension compatible with the remaining axioms.

### Functions

Functions are the central element of the signature, because all quantitative results of CC are formulated through them. Each function has a strict *type signature*: which arguments it accepts and what it returns.

:::warning Potential notation conflicts
- $D_{\text{diff}}$ — differentiation measure. Not to be confused with $D$ — the [Dynamics dimension](/docs/core/structure/dimension-d).
- $R$ — reflection measure. Not to be confused with $\mathcal{R}$ — the [regenerative term](/docs/core/dynamics/evolution#3-регенеративный-член).
:::

| Function | Signature | Interpretation | Ref |
|----------|-----------|----------------|-----|
| $P$ | $\Gamma \to [1/7, 1]$ | Purity | [→](/docs/core/dynamics/viability#определение-чистоты) |
| $S_{vN}$ | $\Gamma \to [0, \log 7]$ | Von Neumann entropy | [→](/docs/reference/notation) |
| $\mathrm{Coh}_E$ | $\Gamma \to [1/7, 1]$ | E-coherence | [→](./definitions#e-когерентность) |
| $\mathrm{Spec}$ | $\Gamma \to \mathrm{List}(\mathbb{R} \times \mathcal{H})$ | Spectrum | — |
| $\varphi$ | $\Gamma \to \Gamma$ | Self-modelling operator | [→](/docs/proofs/categorical/formalization-phi) |
| $C$ | $\Gamma \to \mathbb{R}_{\geq 0}$ | Consciousness measure | [→](/docs/consciousness/foundations/self-observation#мера-сознательности-c) |
| $\Phi$ | $\Gamma \to \mathbb{R}_{\geq 0}$ | Integration measure | [→](/docs/core/structure/dimension-u#мера-интеграции-φ) |
| $D_{\text{diff}}$ | $\Gamma \to \{1, 2, \ldots, 7\}$ | Differentiation measure | [→](/docs/consciousness/foundations/self-observation#мера-сознательности-c) |
| $R$ | $\Gamma \to [0,1]$ | Reflection measure | [→](/docs/consciousness/foundations/self-observation#мера-рефлексии-r) |
| $\sigma_{\mathrm{sys}}$ | $\Gamma \to \mathbb{R}^7$ | Stress tensor | [→](./definitions#тензор-напряжений) |
| $\mathrm{compose}$ | $\mathrm{List}(\mathbb{H}) \to \mathbb{H}$ | Holon composition | [→](./theorems#теорема-91-фрактальное-замыкание) |
| $\mathrm{evolve}$ | $\Gamma \times \mathbb{R} \to \Gamma$ | Evolution | [→](/docs/core/dynamics/evolution) |
| $\kappa$ | $\Gamma \to \mathbb{R}_{\geq 0}$ | Regeneration rate | [→](./axiomatics#связь-регенерации-и-e-когерентности) |

It is worth noting the *closure* of the functions: the self-modelling operator $\varphi: \Gamma \to \Gamma$ returns an object of the same sort as it receives. This is not accidental — it reflects the fact that self-modelling is a *reflexive* operation: the system builds a model of *itself*, and the model is an object of the same type as the modelled thing. The function $\mathrm{evolve}$ is also closed: evolution does not take the system outside the space of coherence matrices.

### Predicates

The predicates of CC are *classifiers*. They divide the space of all possible Holons into meaningful classes:

| Predicate | Signature | Interpretation | Ref |
|-----------|-----------|----------------|-----|
| $\mathrm{Viable}$ | $\mathbb{H} \to \mathrm{Bool}$ | Viable | [→](/docs/core/dynamics/viability) |
| $\mathrm{Conscious}$ | $\mathbb{H} \to \mathrm{Bool}$ | Conscious (L2) | [→](/docs/proofs/consciousness/interiority-hierarchy#уровень-2-когнитивные-квалиа-cognitive-qualia) |
| $\mathrm{HasInteriority}$ | $\mathbb{H} \to \mathrm{Bool}$ | Has interiority (L0) | [→](/docs/proofs/consciousness/interiority-hierarchy#уровень-0-интериорность-interiority) |
| $\mathrm{InV}$ | $\Gamma \to \mathrm{Bool}$ | In region $\mathcal{V}$ | [→](/docs/core/dynamics/viability#область-жизнеспособности) |

These predicates form a *hierarchy*: every conscious Holon is viable, but not every viable Holon is conscious. Every conscious Holon has interiority, but not vice versa. This hierarchy reflects the [interiority levels L0→L1→L2→L3→L4](/docs/proofs/consciousness/interiority-hierarchy) in the language of predicates.

### Signature Axioms

The CC axioms are set out in detail in the chapter ["Axiomatics"](./axiomatics). Here we simply record their list as an element of the signature:

- **(Ω)** — Axiom of Being: $\Omega = \rho_\Omega \in \mathcal{D}(\mathcal{H}_\Omega)$ ([→](/docs/core/foundations/axiom-omega))
- **(AP)** — Axiom of Septicity: $\dim \mathcal{H} = 7$ ([→](/docs/core/foundations/axiom-septicity))
- **(PH)** — Axiom of Hierarchy: Holons form a fractal hierarchy ([→](/docs/core/structure/holon))
- **(QG)** — Axiom of Quantum Gravity ([→](/docs/physics/gravity/quantum-gravity))

Note that there are just four axioms. By comparison, ZFC (the foundation of all mathematics) has 9 axioms, general relativity has 2 (the equivalence principle and Einstein's equations). The minimality of the CC axiomatics is not a simplification for simplicity's sake, but a consequence of the deep internal structure: more than a hundred theorems are derived from four axioms.

## Standard Model

### What It Means to "Have a Model" {#что-значит-иметь-модель}

Consider an analogy. Euclidean geometry speaks of "points", "lines", and "planes" — but what are these objects? Euclid thought they were idealisations of physical points, lines, and surfaces. Hilbert showed that *any* objects satisfying the axioms can be called "points" and "lines" — for example, pairs of real numbers $\mathbb{R}^2$ and linear equations. This is a *model* of Euclidean geometry: a concrete mathematical structure in which the axioms are true.

For CC the situation is analogous: the axioms speak of abstract $\Gamma$, $\mathbb{H}$, $\varphi$. The standard model is a concrete realisation: $\Gamma$ = density matrices in $\mathbb{C}^{7 \times 7}$, evolution = solution of the Lindblad equation, and so on. The standard model is the "world" in which the CC language acquires meaning.

The word "standard" means *canonical* — the model the theory's authors had in mind. As we shall discuss, other models may exist (non-standard), but the standard model gives the *intended* interpretation.

### Formal Definition {#определение-стандартной-модели}

**Definition (Standard Model $\mathfrak{M}_{\mathrm{CC}}$):**

$$
\mathfrak{M}_{\mathrm{CC}} = \langle |\mathfrak{M}|, I \rangle
$$

**Universe (Carrier):**
$$
|\mathfrak{M}| = \mathcal{L}(\mathbb{C}^7) \cup \mathbb{R} \cup \mathbb{C} \cup \mathbb{N} \cup \ldots
$$

The universe is the "world" of the model, the totality of all objects the theory can speak about. Note that the universe includes $\mathcal{L}(\mathbb{C}^7)$ — the space of linear operators on $\mathbb{C}^7$, which *contains* density matrices as a subset but is not exhausted by them. This is important: the universe of the model is broader than the "interesting" objects of the theory.

### Interpretation {#функция-интерпретации}

**Interpretation $I$:**

The interpretation function $I$ is a *dictionary* translating the signature symbols into concrete mathematical objects:

| Symbol | Interpretation |
|--------|----------------|
| $I(\text{sort } \Gamma)$ | $\{M \in \mathbb{C}^{7 \times 7} : M^\dagger = M, M \geq 0, \mathrm{Tr}(M) = 1\}$ |
| $I(P)(M)$ | $\mathrm{Tr}(M^2)$ |
| $I(\mathrm{evolve})(M, t)$ | Solution of the [Lindblad equation](/docs/core/dynamics/evolution) |
| $I(\mathrm{Viable})(\mathbb{H})$ | $P(\Gamma_\mathbb{H}) > P_{\text{crit}} \land dP/d\tau > -\varepsilon_{\text{death}}$ |
| $I(\mathrm{compose})$ | Tensor product + interaction |

:::info Derived and empirical constants
- $P_{\text{crit}} = 2/7 \approx 0.286$ — [theorem](/docs/proofs/dynamics/theorem-purity-critical)
- $\varepsilon_{\text{death}} = 0.01 \cdot P_{\text{crit}} / \tau_{\text{char}}$ — decay rate threshold, see [viability](/docs/core/dynamics/viability)
:::

The key property of the standard model: the interpretation of each symbol is *consistent* — for every statement derivable from the axioms, its interpretation in $\mathfrak{M}_{\mathrm{CC}}$ is true. This property (soundness) is proved below.

### Why the Standard Model Is Non-Trivial {#нетривиальность-стандартной-модели}

At first glance, the standard model is a tautology: we *define* the interpretation so that the axioms are true. But this is a superficial impression. The non-triviality consists in the following:

1. **Existence of the model** = consistency. If the CC axioms contained a contradiction (for example, if some implied $P_{\text{crit}} = 2/7$ while others implied $P_{\text{crit}} = 3/7$), then no model would exist. The very fact that the standard model has been constructed proves consistency (relative to ZFC).

2. **Concreteness of the model** = computability. The CC model is not abstract — it consists of objects one can work with: matrices can be multiplied, eigenvalues computed, the Lindblad equation solved numerically. This makes the theory *falsifiable*.

3. **Uniqueness of interpretation** is non-obvious. Could purity $P$ be something *other* than $\mathrm{Tr}(\Gamma^2)$? Model theory allows this question to be posed rigorously — and answered (see the section on non-standard models).

## Soundness and Completeness

### What This Section Is About {#корректность-полнота-введение}

In mathematical logic, "soundness" and "completeness" are two fundamental properties of a formal theory:

- **Soundness**: everything that is provable is true. If a theorem $\phi$ follows from the CC axioms, then $\phi$ is indeed true in the standard model. This is a *safety* property: the theory does not produce false statements.

- **Completeness**: everything that is true is provable. If $\phi$ is true in the standard model, it can be derived from the axioms. This is a *power* property: the theory can prove everything it needs to.

There is a deep asymmetry between these properties, going back to Gödel's theorems. Soundness is usually easy to establish; completeness is generally unattainable for sufficiently rich theories.

### Theorem (Soundness)

:::info Theorem
All CC theorems are true in $\mathfrak{M}_{\mathrm{CC}}$.
:::

**Proof:** Each theorem is proved constructively from the axioms, which are true in $\mathfrak{M}_{\mathrm{CC}}$ by construction. ∎

:::warning Note on triviality
This "soundness" is trivial: the standard model $\mathfrak{M}_{\mathrm{CC}}$ was constructed so as to satisfy the axioms. Non-trivial soundness — joint consistency of all axioms — is an **open problem**. To resolve it, one must show that the axioms Ω, (AP), (PH), (QG) do not produce contradictions when applied jointly.
:::

### The Gödelian Context {#гёделевский-контекст}

Gödel's theorems (1931) showed that for any sufficiently rich consistent theory:

1. **First incompleteness theorem:** There exist true statements that are unprovable within the theory.
2. **Second incompleteness theorem:** The theory cannot prove its own consistency.

How does this relate to CC?

CC contains natural numbers $\mathbb{N}$ (a sort in the signature), so by Gödel's theorem it *cannot be complete*. There exist statements about Holons that are true in the standard model but underivable from the axioms. This is not a defect of CC — it is a fundamental limitation of *any* formal system containing arithmetic.

However, Gödelian incompleteness *does not concern* typical CC statements. Statements of the form "$P(\Gamma) > 2/7$" or "$R(\Gamma) \geq 1/3$" are arithmetic inequalities about concrete matrices, which are decidable. Incompleteness manifests only for *universally quantified* statements about *all* Holons — and even then, only for pathologically constructed sentences.

### Hypothesis (Relative Completeness)

:::warning Hypothesis (requires proof)
For any statement $\phi$ about viable Holons:
$$
\mathfrak{M}_{\mathrm{CC}} \vDash \phi \Rightarrow \mathrm{CC} \vdash \phi
$$
:::

**Status:** This hypothesis has **not been proved**. Its proof requires formalising the logic of CC and applying a completeness theorem. Completeness is relative to the class of viable Holons.

The word "relative" is key here: the hypothesis asserts completeness not for *all* statements in the CC language, but only for statements about *viable* Holons ($P > 2/7$). Restricting to viable Holons substantially narrows the class of structures considered and possibly makes the theory complete for this subclass — analogously to how the theory of real closed fields is complete (Tarski–Seidenberg theorem), although the general theory of fields is not.

### What Can and Cannot Be Proved {#границы-доказуемости}

Summary:

| Property | Status | Comment |
|----------|--------|---------|
| Soundness (trivial) | **Established** | By construction of the model |
| Joint consistency of axioms | **Open problem** | Requires proving $\mathrm{Con}(\Omega + AP + PH + QG)$ |
| Relative completeness | **Hypothesis** | For viable Holons |
| Absolute completeness | **Impossible** | Gödel's theorem |

## Can There Be Other Models {#нестандартные-модели}

### The Problem of Uniqueness of Interpretation

Until now we have spoken of the *standard* model $\mathfrak{M}_{\mathrm{CC}}$ — the canonical interpretation of CC in terms of $7 \times 7$ density matrices. But the central question in model theory is: is the model *unique*? Do other mathematical structures satisfy the CC axioms — possibly completely unlike density matrices?

By the Löwenheim–Skolem theorem, if a first-order theory has an infinite model, it has models of *any* infinite cardinality. This means that alongside the "standard" model (with the usual real numbers $\mathbb{R}$), there may exist models with non-standard real numbers containing infinitesimals and infinitely large elements.

### Types of Non-Standard CC Models

Several classes of potential non-standard models can be distinguished:

**1. Models with non-standard arithmetic.** If $\mathbb{R}$ is replaced by ${}^*\mathbb{R}$ (Robinson's non-standard analysis), one obtains a model in which purity $P$ can take values infinitely close to $2/7$ but not equal to $2/7$. Physically such models are probably vacuous, but mathematically they are legitimate.

**2. Models with different dimension.** The Axiom of Septicity (AP) fixes $\dim \mathcal{H} = 7$. But one can consider "CC-like" theories with $\dim \mathcal{H} = N$ for arbitrary $N$. Such theories are not models of CC (they violate the axiom), but are important as *counterfactuals*: they show *why* precisely $N = 7$ is necessary. The theorems on minimality of the Fano plane and the Hamming code $H(7,4)$ [give the answer](/docs/core/foundations/axiom-septicity): for $N \neq 7$ it is impossible to simultaneously ensure optimal error-correction, $S_7$-group symmetry, and the structure of the projective plane PG(2,2).

**3. Operator-algebraic models.** Instead of finite-dimensional matrices $\mathbb{C}^{7 \times 7}$ one can consider infinite-dimensional $C^*$-algebras. Such models may describe the "thermodynamic limit" — the collective behaviour of infinitely many Holons. This is related to [Theorem T-117 on emergent commutativity](/docs/proofs/physics/emergent-manifold), where macroscopic spacetime arises as the classical limit of a quantum system.

### Categoricity

A theory is called **categorical** if all its models of a given cardinality are isomorphic. If CC were categorical (in the appropriate cardinality), this would mean the standard model is essentially unique.

CC is probably *not* categorical in the sense of first-order logic (due to the Löwenheim–Skolem theorem). However, it may be categorical as a *second-order theory* — if one demands the standard interpretation of $\mathbb{R}$. This question remains open.

:::info Implication for the philosophy of consciousness
If CC is categorical (in a suitable sense), then consciousness is *uniquely determined* by the axioms: any structure satisfying the CC axioms is "conscious" in exactly the same sense as the standard model. If it is not categorical — "zombie-models" are possible: structures satisfying all axioms but lacking consciousness in "our" sense. Axiom Ω is *specifically designed* to exclude such models, postulating the identity of being and experience.
:::

## Categorical Semantics

### Why Categories Are Needed {#зачем-нужны-категории}

The model theory described above treats CC as an isolated theory: here are the axioms, here is the model, here are the theorems. But CC does not exist in a vacuum — it is connected to IIT, FEP, quantum theory, neuroscience. How can these connections be described *formally*?

This is where **category theory** enters — the mathematical language created for describing *relations between structures*. If ordinary mathematics is "the science of objects" (numbers, sets, functions), then category theory is "the science of relations between objects". Key concepts:

- **Category** — a collection of objects and morphisms (arrows) between them. One can think of a category as a "world": objects are "things" in this world, morphisms are "ways of transforming one thing into another".

- **Functor** — a "translation" from one category to another, preserving structure. If a category is a "world", a functor is a "dictionary" translating the things and relations of one world into another.

- **Natural transformation** — a "translation between translations": a way of comparing two functors.

For CC, the categorical language allows one to:
1. Define the *space* of Holons as a category $\mathbf{Hol}$.
2. Describe the *relations* between Holons as morphisms.
3. Build *translations* of CC into the language of other theories as functors.

### Category of Holons

**Definition (Category $\mathbf{Hol}$):**

See [Categorical Formalism](/docs/proofs/categorical/categorical-formalism) for the complete description.

$$
\mathrm{Ob}(\mathbf{Hol}) := \{\mathbb{H} : \mathbb{H} = \langle \Gamma, \mathcal{H}, H, \{L_k\}, E, \varphi \rangle, \mathrm{Viable}(\mathbb{H})\}
$$

$$
\mathrm{Hom}(\mathbb{H}_1, \mathbb{H}_2) := \{f: \Gamma_1 \to \Gamma_2 : f \text{ preserves structure}\}
$$

The objects of the category are viable Holons. The morphisms are maps that preserve the coherence structure. Intuitively, a morphism $f: \mathbb{H}_1 \to \mathbb{H}_2$ is a "way of seeing" $\mathbb{H}_1$ as a part or projection of $\mathbb{H}_2$, preserving all essential properties.

### Theorem (Symmetric Monoidality)

:::info Theorem
$$
(\mathbf{Hol}, \otimes, \mathbb{H}_{\text{unit}}, \alpha, \lambda, \rho, \sigma) \text{ is a symmetric monoidal category}
$$
:::

| Component | Definition |
|-----------|------------|
| $\otimes$ | $\mathbb{H}_1 \otimes \mathbb{H}_2 = \langle \Gamma_1 \otimes \Gamma_2, \mathcal{H}_1 \otimes \mathcal{H}_2, \ldots \rangle$ |
| $\mathbb{H}_{\text{unit}}$ | $\langle I/7, \mathbb{C}^7, 0, \{\}, \varnothing, \mathrm{id} \rangle$ |
| $\alpha$ | $(\mathbb{H}_1 \otimes \mathbb{H}_2) \otimes \mathbb{H}_3 \cong \mathbb{H}_1 \otimes (\mathbb{H}_2 \otimes \mathbb{H}_3)$ |
| $\sigma$ | $\mathbb{H}_1 \otimes \mathbb{H}_2 \cong \mathbb{H}_2 \otimes \mathbb{H}_1$ |

The symmetric monoidal structure means that Holons can be *composed* — combined into larger systems — and this composition behaves "correctly": order does not matter (symmetry), brackets do not matter (associativity), and there is an "empty" Holon that does not affect composition (unit).

Physical analogy: the monoidal structure on $\mathbf{Hol}$ is an *algebra of parts and wholes*. Two neurons can be combined into a neural network; two neural networks into a brain; two organisms into a social system. At each level the same operator $\otimes$ operates, and at each level a new Holon arises.

:::note On the monoidal unit
$\mathbb{H}_{\text{unit}}$ with $\Gamma = I/7$ has $P(I/7) = 1/7 < P_{\text{crit}} = 2/7$, which formally violates the viability condition. This is **not a defect** of the categorical structure: the monoidal unit is a formal element for defining isomorphisms $\mathbb{H} \otimes \mathbb{H}_{\text{unit}} \cong \mathbb{H}$, not a physical Holon. Viable Holons form a **full subcategory** $\mathbf{Hol}_{\mathcal{V}} \subset \mathbf{Hol}$.
:::

## Translatability: How CC Speaks the Languages of Other Theories {#переводимость}

### Functors as Translators {#функторы-как-переводчики}

If categories are "worlds", functors are "translations" between worlds. A functor $F: \mathbf{A} \to \mathbf{B}$ takes each object of world $\mathbf{A}$ and assigns to it an object of world $\mathbf{B}$, while preserving *relations*: if in $\mathbf{A}$ there is an arrow (morphism) from $X$ to $Y$, then in $\mathbf{B}$ there will be an arrow from $F(X)$ to $F(Y)$.

For CC, functors play the role of *translators*: they allow CC statements to be formulated in the language of other theories and vice versa. This is not a metaphor — it is a mathematically precise operation with provable properties.

The crucial question is: *which* properties are preserved in translation, and which are lost? Each functor is a *projection*, and every projection discards something. Understanding *what exactly* is lost is the key to understanding the relations between theories of consciousness.

### Functor to IIT

**Definition:**
$$
F_{\mathrm{IIT}}: \mathbf{Hol} \to \mathbf{IIT}
$$
$$
F_{\mathrm{IIT}}(\mathbb{H}) = (X, p(x), \Phi(X))
$$

where:
- $X = \mathrm{discretize}(S)$ — discretisation of the state
- $p(x) = \langle x|\Gamma|x \rangle$ — probability distribution (⟨x|Γ|x⟩ is already real and non-negative for Hermitian positive semi-definite Γ)
- $\Phi(X) = \Phi(\Gamma)$ — [integrated information](/docs/core/structure/dimension-u#мера-интеграции-φ)

What is *preserved* in the translation to IIT: the integration measure $\Phi$, the probabilistic structure of states. What is *lost*: the seven-dimensional coherence structure (IIT does not distinguish dimensions A, S, D, L, E, O, U), the dynamics of evolution (IIT works with static states), the reflexivity of operator $\varphi$ (IIT has no analogue of self-modelling).

:::info Corollary
IIT is a *projection* of CC: it sees the "shadow" of the Holon on the screen of integrated information, but not the full Holon. Therefore IIT correctly predicts *some* aspects of consciousness ($\Phi$), but cannot explain the *structure* of conscious experience (for that, the full seven-dimensional $\Gamma$ is needed).
:::

### Functor to FEP

**Definition:**
$$
F_{\mathrm{FEP}}: \mathbf{Hol} \to \mathbf{MarkovBlankets}
$$

:::warning Hypothesis
**Hypothesis (FEP as projection):**
$$
\mathrm{FEP} = \pi_D \circ \mathrm{CC}
$$
FEP is a projection onto the [D-dimension](/docs/core/structure/dimension-d) (Dynamics).

This statement is a *research hypothesis* requiring formal proof.
:::

The Free Energy Principle (FEP) of Karl Friston describes *self-organisation* — how systems maintain their existence by minimising free energy. In the CC language this corresponds to the *dynamic dimension* $D$: a viable system ($P > 2/7$) is a system successfully minimising "surprise" (in FEP terms) or "stress" $\sigma_{\mathrm{sys}}$ (in CC terms).

The hypothesis $\mathrm{FEP} = \pi_D \circ \mathrm{CC}$ asserts that FEP sees exactly one of the seven facets of the Holon — its dynamic component. This explains why FEP is successful in neuroscience (brain dynamics is its strength), but insufficient for a complete theory of consciousness (for that, the remaining six dimensions are also needed).

### Functor to GNW {#функтор-в-gnw}

The Global Neuronal Workspace Theory (GNW) of Bernard Baars and Stanislas Dehaene describes consciousness as *global availability* of information. In the CC language this corresponds to a *projection onto the subcategory with condition* $D_{\text{diff}} \geq 2$ and coherence sufficient for global binding.

The functor $F_{\mathrm{GNW}}$ can be defined as:

$$
F_{\mathrm{GNW}}: \mathbf{Hol}_{\mathcal{V}} \to \mathbf{AccessibleStates}
$$

$$
F_{\mathrm{GNW}}(\mathbb{H}) = (\mathrm{GlobalWorkspace}(\Gamma), \mathrm{AccessMap}(\Gamma))
$$

where $\mathrm{GlobalWorkspace}$ is the subspace of $\mathcal{H}$ defined by the eigenvectors of $\Gamma$ with the largest eigenvalues (dominant "contents" of consciousness), and $\mathrm{AccessMap}$ is the structure of connections between dimensions, defined by the off-diagonal elements of $\Gamma$.

### The Overall Picture: CC as Metatheory {#кк-как-метатеория}

The functors $F_{\mathrm{IIT}}$, $F_{\mathrm{FEP}}$, $F_{\mathrm{GNW}}$ are not ad hoc correspondences, but manifestations of a unified structure: **CC is a metatheory**, containing IIT, FEP, and GNW as projections.

$$
\begin{array}{ccc}
& \mathbf{Hol} & \\
F_{\mathrm{IIT}} \swarrow & \downarrow F_{\mathrm{FEP}} & \searrow F_{\mathrm{GNW}} \\
\mathbf{IIT} & \mathbf{MarkovBlankets} & \mathbf{AccessibleStates}
\end{array}
$$

Each functor is a *projection* onto a subset of the Holon's structure:
- $F_{\mathrm{IIT}}$ preserves $\Phi$ (integration), loses $R$ (reflection) and $\sigma$ (dynamics).
- $F_{\mathrm{FEP}}$ preserves dynamics ($D$-dimension), loses the internal structure of experience.
- $F_{\mathrm{GNW}}$ preserves global accessibility, loses the metric of the phenomenal space.

None of the projections yields a complete theory of consciousness. Only the full Holon — the seven-dimensional coherence matrix $\Gamma \in \mathcal{D}(\mathbb{C}^7)$ — contains all the information. In this sense CC is not "yet another" theory in the series IIT/FEP/GNW, but a *theory containing them as special cases*.

## Experiential Category

### Why a Separate Category of Experience Is Needed {#зачем-категория-опыта}

The functors $F_{\mathrm{IIT}}$, $F_{\mathrm{FEP}}$, etc. describe the "external" side of CC — its relations with other scientific theories. But CC is a theory of *consciousness*, and its central problem is not dynamics and not information, but *experience*: why do certain mathematical structures "feel"? To formalise this question a special category is needed — the category of *experiential states*.

### Category of Density Matrices

**Definition (Category $\mathbf{DensityMat}$):**

See [Categorical Formalism](/docs/proofs/categorical/categorical-formalism#1-категория-densitymat) for the complete description.

$$
\mathbf{DensityMat} := (\mathrm{Obj}, \mathrm{Mor})
$$

where:
- $\mathrm{Obj} = \{\rho : \rho^\dagger = \rho, \rho \geq 0, \mathrm{Tr}(\rho) = 1\}$
- $\mathrm{Mor}(\rho_1, \rho_2) = \{\Psi : \mathrm{CPTP}, \Psi(\rho_1) = \rho_2\}$

CPTP = Completely Positive Trace-Preserving (quantum channels).

The morphisms of this category — CPTP channels — deserve a separate comment. In quantum mechanics a CPTP channel is the most general physically admissible transformation of a state. It preserves *positivity* (probabilities remain non-negative), *complete positivity* (works correctly for composite systems too), and the *trace* (total probability equals 1). In CC this means that the transition between Holon states is always a *physically realisable* process. The evolution $\mathrm{evolve}(\Gamma, t)$ is a special case of a CPTP channel.

### Experience Functor

**Definition (Complete Experience Functor):**

See [Category Exp](/docs/proofs/categorical/categorical-formalism#2-категория-exp) for the complete description.

$$
F_{\mathcal{Q}}: \mathbf{DensityMat} \to \mathbf{Exp}
$$
$$
F_{\mathcal{Q}}(\rho) := (\mathrm{Spectrum}(\rho_E), \mathrm{Eigenvectors}(\rho_E), \mathrm{Context}(\Gamma_{-E}), \mathrm{History})
$$

The experience functor $F_{\mathcal{Q}}$ is the mathematical formalisation of the *transition from the system state to experience*. Its four-component structure is not accidental:

1. **Spectrum** $\mathrm{Spectrum}(\rho_E)$ — eigenvalues of the $E$-submatrix. They define the *intensities* of experience components: how vividly each "quality" (qualia) is present at the given moment.

2. **Eigenvectors** $\mathrm{Eigenvectors}(\rho_E)$ — directions in the $E$-subspace. They define the *content* of experience: *what exactly* is being experienced. Two states with the same spectrum but different eigenvectors are states of the same "brightness" but different "colour".

3. **Context** $\mathrm{Context}(\Gamma_{-E})$ — the remaining six dimensions of the coherence matrix. They define the *background* of experience: what the dynamics is (D), attention (A), social context (S), logical structure (L), wholeness (O), energy level (U).

4. **History** $\mathrm{History}$ — the temporal trajectory of preceding states. It defines the *temporal* structure of experience: the sense of duration, memory, anticipation.

### Theorem (Impossibility of the Spectral Functor)

:::warning [Theorem](/docs/reference/specification#теорема-невозможность-спектрального-функтора)
There is no functor $F: \mathbf{DensityMat} \to \mathbf{Exp}$ that factors *only* through the spectrum.
:::

**Proof:**
1. Suppose $F = G \circ \mathrm{Spec}$, where $\mathrm{Spec}: \rho \mapsto \mathrm{Spectrum}(\rho)$
2. Consider isospectral $\rho_1 \neq \rho_2$
3. Then $F(\rho_1) = G(\mathrm{Spec}(\rho_1)) = G(\mathrm{Spec}(\rho_2)) = F(\rho_2)$
4. But $\rho_1$ and $\rho_2$ may describe *distinguishable* experiences
5. Contradiction ∎

**Corollary:** The complete functor $F_{\mathcal{Q}}$ *must* account for eigenvectors, context, and history.

This theorem has a deep philosophical meaning: *experience is not reducible to quantitative characteristics*. Two states with the same eigenvalues (the same "amounts" of information, integration, coherence) can give rise to *different experiences* — because not only "how much" matters, but also "of what", "against what background", and "after what". This is the mathematical justification for the intuition about the *qualitativeness* of experience.

Analogy: two musical chords may have the same sound intensities (spectrum) but different notes (eigenvectors) — and be experienced completely differently. The theorem asserts that no "loudness detector" can replace a "harmony detector".

## Limits of Explanation

### The Categorical Gap

:::caution Acknowledgement
CC does *not explain* why a specific numerical value $\lambda = 0.347$ is experienced as *this particular* sensation.
:::

The theory establishes a *structural correspondence* between mathematics and phenomenology, but does not deduce one from the other.

This gap is not an accidental lacuna, but a fundamental feature of any mathematical theory of consciousness. To understand its nature, consider an analogy.

Physics describes electromagnetic waves with wavelength 700 nm. It explains how these waves arise, propagate, are absorbed by retinal receptors, and generate nerve impulses. But it *does not explain* why 700 nm is *red*. The link "700 nm → sensation of red" is not a deduction from Maxwell's equations, but an *empirical fact*. Maxwell's equations work in a world without observers; "red" requires an observer.

CC differs from physics in that it *starts* with the observer: axiom Ω postulates the identity of being and experience. But even with this postulate a gap remains: the *structure* of experience (the Fubini–Study metric, the level hierarchy) is defined, but the *quality* (qualia) is not.

### What the Theory Explains

1. The **structure** of phenomenal space ([L1](/docs/proofs/consciousness/interiority-hierarchy#уровень-1-феноменальная-геометрия-phenomenal-geometry): Fubini–Study metric)
2. The **relations** between qualities (L1: isomorphism with $\mathbb{P}(\mathcal{H}_E)$)
3. The **dynamics** of experience ([evolution equation](/docs/core/dynamics/evolution))
4. The **conditions** for consciousness ([L2](/docs/proofs/consciousness/interiority-hierarchy#уровень-2-когнитивные-квалиа-cognitive-qualia): $R \geq R_{\text{th}}$, $\Phi \geq \Phi_{\text{th}}$, $D_{\text{diff}} \geq 2$)
5. The **necessity** of interiority ([L0](/docs/proofs/consciousness/interiority-hierarchy#уровень-0-интериорность-interiority)) for viability ([Theorem 8.1 [T]](./theorems#теорема-81-условная-необходимость-интериорности-no-zombie))

### What the Theory Does Not Explain

1. *Why* mathematical structures "feel"
2. *Why* this particular structure, and not another

### The Nature of the Categorical Gap {#природа-категориального-разрыва}

It is important to understand that the categorical gap is not *epistemic* (we don't know something), but *ontological* (knowledge of a certain type is *impossible in principle*). This claim can be made precise:

**Statement (Non-derivability of quality):** There is no formal system $T$ containing arithmetic such that for some predicate $Q$ (quality of experience):
$$
T \vdash \forall \rho.\, Q(\rho) \leftrightarrow \Phi(\rho)
$$
where $\Phi$ is any computable function of $\rho$.

In other words: the quality of experience (qualia) *cannot be identified* with any computable characteristic of the density matrix. This does not mean that qualia are "non-material" — it means that the relation "quality ↔ structure" is a *basic* relation, not reducible to anything simpler.

CC circumvents this problem elegantly but radically: axiom Ω *postulates* the identity of being and experience. Not "being *generates* experience" (which would require explaining the mechanism), but "being *is* experience" (which is an axiom, requiring no explanation).

**Metatheoretical status:**
The categorical gap is not a *defect* of the theory, but a *limit of explanation*. The identity of being and experience is [Axiom Ω](/docs/core/foundations/axiom-omega), not a theorem.

### Comparison with Other Theories {#сравнение-с-другими-теориями}

It is useful to compare how different theories of consciousness deal with the categorical gap:

| Theory | Strategy | Problem |
|--------|----------|---------|
| **Physicalism** | Consciousness = brain process | Does not explain qualia |
| **Functionalism** | Consciousness = function | Chinese Room argument |
| **IIT** | Consciousness = $\Phi$ | Does not explain why $\Phi$ "feels" |
| **FEP** | Consciousness = free energy minimisation | Does not distinguish conscious from unconscious agents |
| **Panpsychism** | Consciousness is a fundamental property | Combination problem |
| **CC** | Being *is* experience (Ω) | Categorical gap (explicitly acknowledged) |

CC does not "solve" the hard problem of consciousness — it *reformulates* it: not "how does matter generate consciousness?" (a question without an answer), but "what is the mathematical structure of experience?" (a question CC answers).

## Summary: Architecture of CC Model Theory {#резюме}

CC model theory is not merely formal decoration for a substantive theory. It performs three critical functions:

1. **Fixing the ontology.** The signature $\Sigma_{\mathrm{CC}}$ precisely defines what CC speaks about and what it does not. Everything outside the signature is not the subject of CC.

2. **Guarantee of consistency.** The standard model $\mathfrak{M}_{\mathrm{CC}}$ proves that the axioms are compatible (at least relative to ZFC). A theory with no model is empty.

3. **Bridges between theories.** The functors $F_{\mathrm{IIT}}$, $F_{\mathrm{FEP}}$, $F_{\mathrm{GNW}}$ rigorously describe the relations of CC to other theories of consciousness — not as metaphors, but as mathematically precise projections with provable information-loss and information-preservation properties.

The key result of this chapter is a *complete picture* of the formal status of CC: a theory with an explicit signature, standard model, proved (trivial) soundness, hypothetical relative completeness, categorical semantics, and explicitly acknowledged limits of explanation. Such a level of formal transparency is unique among theories of consciousness.

---

## What We Have Learned

Let us summarise this chapter. We have examined CC "from above" — not as a collection of formulas, but as a formal theory with a clearly defined status:

1. **Signature** $\Sigma_{\mathrm{CC}}$ — the formal "alphabet" of CC: 6 sorts (including $\Gamma$ and $\mathbb{H}$), 12+ functions ($P$, $\Phi$, $R$, $\varphi$, $\sigma_{\mathrm{sys}}$...), 4 predicates ($\mathrm{Viable}$, $\mathrm{Conscious}$, ...) and 4 axioms. Every CC statement is written in the symbols of this signature.

2. **Standard model** $\mathfrak{M}_{\mathrm{CC}}$ — a concrete realisation: $\Gamma$ = density matrices in $\mathbb{C}^{7 \times 7}$, evolution = solution of the Lindblad equation. The existence of the model proves consistency (relative to ZFC). The concreteness of the model makes the theory computable and falsifiable.

3. **Soundness** is established (trivially — by construction). **Absolute completeness** is impossible (Gödel's theorem). **Relative completeness** for viable Holons is an open hypothesis.

4. **Non-standard models** are possible (Löwenheim–Skolem theorem), but physically probably vacuous. The question of categoricity remains open.

5. **Category of Holons** $\mathbf{Hol}$ is a symmetric monoidal category. Holons can be composed ($\otimes$), and this composition is associative, commutative, and has a unit.

6. **Functor bridges** $F_{\mathrm{IIT}}$, $F_{\mathrm{FEP}}$, $F_{\mathrm{GNW}}$ — CC as metatheory. Each existing theory of consciousness is a *projection* of CC, preserving part of the structure and losing the rest. IIT loses dynamics and reflection. FEP loses the internal structure of experience. GNW loses the metric of the phenomenal space.

7. **Categorical gap** — CC explains the *structure* of experience, but not the *quality* (qualia). The identity of being and experience is an axiom ($\Omega$), not a theorem. This is not a defect, but a fundamental limit of explanation.

:::info Bridge to the Next Chapter
We have completed the description of the *formal foundations* of CC: axioms, definitions, theorems, model theory. These are the first five chapters, from "why" to "about what". Now the *advanced mathematical apparatus* begins. In the [next chapter](./gap-algebra) we investigate the **Gap algebra** — the structure of the "gap" between dimensions, defined by the geometry of the Fano plane. The Gap algebra describes how coherences between dimensions evolve, which combinations are stable, and how bifurcations, phase transitions, and non-Markovian memory effects arise from this dynamics.
:::

---

**Related Documents:**
- [Axiomatics](./axiomatics) — axioms Ω and Septicity
- [Theorems](./theorems) — formal results of CC
- [Definitions](./definitions) — basic CC definitions
- [Categorical Formalism](/docs/proofs/categorical/categorical-formalism) — categories $\mathbf{Hol}$, $\mathbf{DensityMat}$, $\mathbf{Exp}$
- [Formalisation of operator φ](/docs/proofs/categorical/formalization-phi) — CPTP channels
- [Interiority Hierarchy](/docs/proofs/consciousness/interiority-hierarchy) — levels L0→L1→L2→L3→L4
- [Holon](/docs/core/structure/holon) — definition of $\mathbb{H}$
- [Coherence Matrix](/docs/core/dynamics/coherence-matrix) — definition of $\Gamma$
- [Viability](/docs/core/dynamics/viability) — measure $P$ and $P_{\text{crit}}$
- [Evolution](/docs/core/dynamics/evolution) — equation $d\Gamma/d\tau$
- [Seven Dimensions](/docs/core/structure/dimensions) — structure $\mathcal{H} = \mathbb{C}^7$
- [Glossary](/docs/reference/glossary) — terminology and related theories
- [Comparison with Alternatives](./comparison) — formal bridges CC↔IIT, CC↔FEP
- [Philosophical Foundations](./philosophy) — epistemological status of CC models
