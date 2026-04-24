# UHM Documentation

Documentation website for **Unitary Holonomic Monism (UHM)** — a formal theory of reality and consciousness.

## Overview

UHM describes the structure, dynamics, and phenomenology of reality through a single mathematical object — the Coherence Matrix (Γ).

Key concepts:
- **Holon** — minimal self-sufficient unit of reality
- **7 Dimensions** — A (Articulation), S (Structure), D (Dynamics), L (Logic), E (Experience), O (Ground), U (Unity)
- **Interiority Hierarchy** — L0 (interiority) → L1 (phenomenal geometry) → L2 (cognitive qualia)
- **Viability** — condition for system existence: P > P_crit = 2/7

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
│   ├── foundations/      # Axioms Ω and Septicity
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
- Theory version: 0.1.3
