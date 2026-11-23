# `architecture/` — TALOS Architecture Specification & Reference Emulator

This directory contains the technical LaTeX specification of **TALOS** (the seven-mode coherence-flow architecture for UHM holons, co-designed with SYNARC-$\Omega$), its verified V0 reference emulator, and supporting mathematical/computational laboratories.

The Russian 1:1 companion specification lives in [`../architecture-ru/`](../architecture-ru/).

## Core Architecture Specification

- [`main.tex`](main.tex), [`references.bib`](references.bib), [`sections/`](sections/) — English specification of TALOS (`pdflatex` / `latexmk`).
- [`../architecture-ru/main.tex`](../architecture-ru/main.tex) — Russian 1:1 specification (`xelatex`).

### Key Verified Mathematical & Engineering Primitives

1. **Canonical Singer cyclic Fano plane $\mathrm{PG}(2,2)$** on `(A, S, D, L, E, U, O) = (1..7)` (0-indexed `0..6`):
   - Seven lines: `{A,S,L}`, `{S,D,E}`, `{D,L,U}`, `{L,E,O}`, `{E,U,A}`, `{U,O,S}`, `{O,A,D}`.
   - Uniqueness at $N=7$ across all prime powers $q \ge 2$ via binary incidence-code fusion (`FoundationalBounds.pg2_5_refutes_N31_hamming_fusion`, `FoundationalBounds.pg2EvenHammingUniqueSeven`, verified in `website/research/operational-reconstruction/verify_foundational_bounds.py`).
2. **Binary coding duality over $\mathbb{F}_2$:**
   - The $7 \times 7$ Fano incidence matrix $M$ ($\operatorname{rank}_{\mathbb{F}_2}(M)=4$, rows = weight-3 lines) generates the Hamming $[7,4,3]$ code.
   - The $3 \times 7$ parity-check matrix $H$ ($\operatorname{rank}_{\mathbb{F}_2}(H)=3$, rows = three independent weight-4 line complements spanning the dual simplex code $[7,3,4]$) satisfies $H M^T \equiv 0 \pmod 2$ and uniquely maps all 7 single-sector faults to distinct nonzero 3-bit syndromes.
3. **Genuine Fano pinching & discrete covariance:**
   - $\mathcal{P}_{\mathrm{Fano}}(\Gamma) = \frac{1}{3}\sum_{\ell=1}^{7} \Pi_\ell \Gamma \Pi_\ell$ preserves all populations and scales every off-diagonal coherence by $1/3$, yielding exact $\Phi$-contraction $\Phi(\mathcal{P}_{\mathrm{Fano}}(\Gamma)) = \frac{1}{9}\Phi(\Gamma)$ on all $\Gamma \in \mathcal{D}(\mathbb{C}^7)$.
   - The Fano Lindblad dissipator $\mathcal{D}_{\mathrm{Fano}}[\Gamma] = \gamma(\mathcal{P}_{\mathrm{Fano}}(\Gamma) - \Gamma)$ decays off-diagonals at uniform rate $2\gamma/3$ and is covariant under the discrete collineation group $\mathrm{PSL}(2,7)$ (order 168) and diagonal phase rephasing $U(1)^7$ — **not** under continuous $G_2$ rotations of the coordinate basis; hence all $48$ real parameters of $\Gamma \in \mathcal{D}(\mathbb{C}^7)$ are dynamically active.
4. **Canonical observables & thermodynamics in bits:**
   - Exact integration $\Phi = (P - P_{\mathrm{diag}})/P_{\mathrm{diag}}$ (reducing to $7P - 1$ only on uniform diagonals $\gamma_{kk}=1/7$), reflection $R = 1/(7P)$ ($R \ge 1/3 \iff P \le 3/7$), $\mathrm{Coh}_E = (\gamma_{EE}^2 + 2\sum_{j\neq E}|\gamma_{Ej}|^2)/P$, $D_{\mathrm{diff}} = 1 + 6\,\mathrm{Coh}_E$, and exact von Neumann entropy $S_{\mathrm{vN}} = -\operatorname{Tr}(\Gamma \log_2 \Gamma) \le \log_2 7 \approx 2.807$ bits ($k_B T \ln 7 \approx 8.06 \times 10^{-21}$ J at 300 K).

## Reference V0 Emulator

Run the NumPy-only reference kernel and self-test suite:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B architecture/talos_v0_emulator.py
```

The emulator verifies:
1. Canonical Singer Fano $S(2,3,7)$ incidence, 21 mediators, $M$/$H$ duality ($H M^T \equiv 0 \pmod 2$), and bijective 3-bit single-sector syndrome decoding.
2. Exact Fano pinching ($\Phi \to \Phi/9$), Fano Lindblad dissipator equivalence ($\mathcal{D}_{\mathrm{Fano}} = \frac{2}{3}\mathcal{D}_{\mathrm{atom}}$), discrete $\mathrm{PSL}(2,7)\ltimes U(1)^7$ covariance, and explicit non-covariance under continuous $G_2$ rotations.
3. Exact canonical observables on both uniform and non-uniform diagonal states (verifying $\Phi \neq 7P - 1$ off the uniform stratum) and $S_{\mathrm{vN}} \le \log_2 7$ bits.
4. Canonical nonlinear anchored self-model $\varphi_J(\Gamma) = (1 - R(\Gamma))\mathcal{P}_{\mathrm{Fano}}(\Gamma) + R(\Gamma)|\psi\rangle\langle\psi|$, CPTP Strang-split attractor convergence inside the full 4-gate viable window, unitary spectrum conservation, and analytical power-port severance latency.
5. Thermodynamic entropy production rate in bits ($\dot S_{\mathcal{D}} > 0$, $\Delta\tau$-independent).
6. Vectorized SIMT ecology batch (`1000` holons, `0.784 MB`).

## Building the Specifications

```bash
# English specification
cd architecture && pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex

# Russian 1:1 specification (requires XeLaTeX + CMU OpenType fonts)
cd architecture-ru && xelatex main.tex && bibtex main && xelatex main.tex && xelatex main.tex
```

## Supporting Mathematical Laboratories

- `fano_verify.py`, `symmetry_lab.py` — finite geometry, Fano incidence, and symmetry verification.
- `holarch_lab.py`, `holarchy_ladder_lab.py`, `interiority_lab.py`, `wf_toy_a1.py` — holon dynamics, hierarchical composition, and toy dynamical models.
- `category_lab.py`, `category_lab2.py`, `category_lab3.py` — categorical colimit, fixed-point, and operadic composition scripts.
- `prime_radiant.py`, `prime_radiant.verum`, `prime-radiant-rs/` — Prime Radiant reference implementations (Python, Verum, Rust).
- `boundary_svg.py`, `chord_svg.py`, `fold_svg.py`, `turnover_svg.py` — technical SVG figure generators.
