# UHM Documentation

Documentation website for **Unitary Holonomic Monism (UHM)** — a mathematical research programme on organization, state dynamics and consciousness.

## Overview

The rigorous kernel separates finite-dimensional density matrices and linear CPTP processes from the open-cover site of their Bures state space and its sheaf ∞-topos. The native model chooses seven labelled roles, a numerical self-model and dynamics. Seven-dimensional necessity has explicit additional hypotheses; physical state encoding and the phenomenal bridge remain separate model-identification questions.

Start with [the mathematical kernel](docs/reference/mathematical-kernel.md), [the premise ledger](docs/reference/premises.md), and [the corrected categorical formalism](docs/proofs/categorical/categorical-formalism.md). Results distinguish proven mathematics from definitions, conditional bridges, interpretations and open research programmes. The majority cut `P > 2/7` is a chosen structural criterion, rather than a universal proof of physical existence or consciousness.

## Installation

```bash
npm install
```

## Development

```bash
npm start
```

Opens a local development server at `http://localhost:3000`. Changes are reflected live.

## Build

```bash
npm run build
```

Generates static content in the `build` directory.

## Verification

```bash
npm run test:math
npm run test:status
npm run build
npm run test:render
npm run test:mermaid
```

The numerical checks exercise specified identities, counterexamples and the density-preserving integration scheme. They supplement proofs and do not certify physical or phenomenal identifications. Python checks require NumPy and SciPy; diagram checks require Chrome or the configured Playwright browser. Set `MERMAID_BROWSER_PATH` to use another already installed Chromium executable.

## Deployment

The site is deployed to GitHub Pages via GitHub Actions (see `.github/workflows/deploy.yml`).

Manual deployment:
```bash
GIT_USER=<username> npm run deploy
```

## Project Structure

```
docs/
├── core/                 # Core theory
│   ├── foundations/      # Typed foundation and model requirements
│   ├── structure/        # Holon and 7 dimensions
│   ├── dynamics/         # Evolution equations
│   └── consciousness/    # Interiority hierarchy
├── proofs/               # Formal proofs and theorems
├── applied/              # Applications (Coherence Cybernetics)
├── formal/               # Mathematical specification
└── reference/            # Glossary, notation, falsifiability
```

## License

- **Documentation (theory)**: [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)
- **Code**: [MIT](https://opensource.org/licenses/MIT)

See [LICENSE](../LICENSE) for details.

## Links

- Website: https://holon.sh
- Theory version: 0.8.1
