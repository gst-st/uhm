import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  theory: [
    'intro',
    {
      type: 'category',
      label: 'Foundations',
      collapsed: false,
      items: [
        'core/foundations/mathematical-foundations',
        'core/foundations/axiom-omega',
        'core/foundations/axiom-septicity',
        'core/foundations/consequences',
        'core/foundations/spacetime',
      ],
    },
    {
      type: 'category',
      label: 'Structure of Reality',
      items: [
        'core/structure/holon',
        {
          type: 'category',
          label: 'Seven Dimensions',
          items: [
            'core/structure/dimensions',
            'core/structure/dimension-a',
            'core/structure/dimension-s',
            'core/structure/dimension-d',
            'core/structure/dimension-l',
            'core/structure/dimension-e',
            'core/structure/dimension-o',
            'core/structure/dimension-u',
          ],
        },
        'core/structure/symbolic-systems',
      ],
    },
    {
      type: 'category',
      label: 'Dynamics',
      items: [
        'core/dynamics/coherence-matrix',
        'core/dynamics/evolution',
        'core/dynamics/viability',
        'core/dynamics/gap-operator',
        'core/dynamics/gap-dynamics',
        'core/dynamics/gap-thermodynamics',
        'core/dynamics/gap-phase-diagram',
        'core/dynamics/composite-systems',
      ],
    },
    {
      type: 'category',
      label: 'Operators',
      items: [
        'core/operators/phi-operator',
        'core/operators/lindblad-operators',
        'core/operators/emergent-time',
      ],
    },
    {
      type: 'category',
      label: 'Categorical Formalism',
      items: [
        'core/categories/functor-f',
        'core/categories/category-exp',
        'core/categories/category-hol',
      ],
    },
  ],

  consciousness: [
    'consciousness/overview',
    {
      type: 'category',
      label: 'Mathematical Foundations',
      collapsed: false,
      items: [
        'consciousness/foundations/two-aspect-monism',
        'consciousness/foundations/interiority-theory',
        'consciousness/foundations/self-observation',
      ],
    },
    {
      type: 'category',
      label: 'Hierarchy L0→L4',
      items: [
        'consciousness/hierarchy/interiority-hierarchy',
        'consciousness/hierarchy/depth-tower',
        'consciousness/hierarchy/gap-characterization',
        'consciousness/hierarchy/swallowtail-transitions',
      ],
    },
    {
      type: 'category',
      label: 'Structure of Experience',
      items: [
        'consciousness/phenomenology/qualia-structure',
        'consciousness/phenomenology/emotional-taxonomy',
        'consciousness/phenomenology/temporal-consciousness',
        'consciousness/phenomenology/intentionality',
      ],
    },
    {
      type: 'category',
      label: 'States of Consciousness',
      items: [
        'consciousness/states/altered-states',
        'consciousness/states/unconscious',
        'consciousness/states/attention-memory',
        'consciousness/states/pathological',
      ],
    },
    {
      type: 'category',
      label: 'Theory Comparison',
      items: [
        'consciousness/comparative/consciousness-theories',
        'consciousness/comparative/panpsychism-analysis',
        'consciousness/comparative/cognitive-hierarchy',
        'consciousness/comparative/cognitome-anokhin',
        'consciousness/comparative/general-systems-theory',
      ],
    },
    {
      type: 'category',
      label: 'Subjects of Consciousness',
      items: [
        'consciousness/subjects/pre-linguistic',
        'consciousness/subjects/animal-consciousness',
        'consciousness/subjects/ai-consciousness',
        'consciousness/subjects/collective-consciousness',
      ],
    },
    {
      type: 'category',
      label: 'Ethics & Meaning',
      items: [
        'consciousness/ethics-meaning/value-consciousness',
        'consciousness/ethics-meaning/meaning',
        'consciousness/ethics-meaning/freedom',
        'consciousness/ethics-meaning/death-continuity',
      ],
    },
  ],

  proofs: [
    {
      type: 'category',
      label: 'Minimality',
      collapsed: false,
      items: [
        'proofs/minimality/theorem-minimality-7',
        'proofs/minimality/theorem-octonionic-derivation',
      ],
    },
    {
      type: 'category',
      label: 'Dynamics',
      items: [
        'proofs/dynamics/theorem-purity-critical',
        'proofs/dynamics/emergent-time',
        'proofs/dynamics/fep-derivation',
      ],
    },
    {
      type: 'category',
      label: 'Categorical Proofs',
      items: [
        'proofs/categorical/categorical-formalism',
        'proofs/categorical/formalization-phi',
        'proofs/categorical/uniqueness-theorem',
      ],
    },
    {
      type: 'category',
      label: 'Consciousness',
      items: [
        'proofs/consciousness/interiority-hierarchy',
        'proofs/consciousness/conscious-window',
        'proofs/consciousness/operationalization',
        'proofs/consciousness/operational-closure',
        'proofs/consciousness/substrate-closure',
      ],
    },
    {
      type: 'category',
      label: 'Physics',
      items: [
        'proofs/physics/physics-correspondence',
        'proofs/physics/emergent-manifold',
        'proofs/physics/bimodule-construction',
        'proofs/physics/toe-embeddings',
      ],
    },
    {
      type: 'category',
      label: 'Gap',
      items: [
        'proofs/gap/fano-channel',
        'proofs/gap/lambda-budget',
      ],
    },
  ],

  physics: [
    'physics/overview',
    {
      type: 'category',
      label: 'Quantum Mechanics',
      items: [
        'physics/quantum-mechanics/qm-reduction',
        'physics/quantum-mechanics/measurement',
      ],
    },
    {
      type: 'category',
      label: 'Gauge Symmetries',
      items: [
        'physics/gauge-symmetry/g2-structure',
        'physics/gauge-symmetry/standard-model',
        'physics/gauge-symmetry/fano-selection-rules',
        'physics/gauge-symmetry/confinement',
        'physics/gauge-symmetry/noether-charges',
        'physics/gauge-symmetry/rg-flow',
      ],
    },
    {
      type: 'category',
      label: 'Particle Physics',
      items: [
        'physics/particle-physics/fermion-generations',
        'physics/particle-physics/ckm-matrix',
        'physics/particle-physics/yukawa-hierarchy',
        'physics/particle-physics/higgs-sector',
        'physics/particle-physics/neutrino-masses',
        'physics/particle-physics/susy',
        'physics/particle-physics/proton-decay',
      ],
    },
    {
      type: 'category',
      label: 'Gravity',
      items: [
        'physics/gravity/emergent-geometry',
        'physics/gravity/einstein-equations',
        'physics/gravity/cosmological-constant',
        'physics/gravity/quantum-gravity',
      ],
    },
    {
      type: 'category',
      label: 'Cosmology',
      items: [
        'physics/cosmology-phys/origin',
        'physics/cosmology-phys/dark-matter',
        'physics/cosmology-phys/berry-phase',
      ],
    },
    {
      type: 'category',
      label: 'Dual Aspect',
      items: [
        'physics/dual-aspect/gap-semantics',
        'physics/dual-aspect/zeta-regularization',
      ],
    },
  ],

  cybernetics: [
    'applied/coherence-cybernetics/introduction',
    {
      type: 'category',
      label: 'Formal Foundations',
      collapsed: false,
      items: [
        'applied/coherence-cybernetics/axiomatics',
        'applied/coherence-cybernetics/definitions',
        'applied/coherence-cybernetics/theorems',
        'applied/coherence-cybernetics/model-theory',
      ],
    },
    {
      type: 'category',
      label: 'Gap Operator Algebra',
      items: [
        'applied/coherence-cybernetics/gap-algebra',
        'applied/coherence-cybernetics/bifurcation',
        'applied/coherence-cybernetics/non-markovian',
        'applied/coherence-cybernetics/model-systems',
      ],
    },
    {
      type: 'category',
      label: 'Variational Structure',
      items: [
        'applied/coherence-cybernetics/lagrangian',
        'applied/coherence-cybernetics/variational',
        'applied/coherence-cybernetics/effective-temperature',
      ],
    },
    {
      type: 'category',
      label: 'Topological Protection',
      items: [
        'applied/coherence-cybernetics/topological-protection',
        'applied/coherence-cybernetics/phase-diagram-cc',
        'applied/coherence-cybernetics/goldstone-modes',
        'applied/coherence-cybernetics/g2-noether-cc',
      ],
    },
    {
      type: 'category',
      label: 'Context & Comparison',
      items: [
        'applied/coherence-cybernetics/cybernetics-history',
        {
          type: 'link',
          label: '→ Consciousness Theories',
          href: '/docs/consciousness/comparative/consciousness-theories',
        },
        {
          type: 'link',
          label: '→ Panpsychism',
          href: '/docs/consciousness/comparative/panpsychism-analysis',
        },
      ],
    },
    {
      type: 'category',
      label: 'Sensorimotor Theory & Stability',
      items: [
        'applied/coherence-cybernetics/sensorimotor',
        'applied/coherence-cybernetics/stability',
        'applied/coherence-cybernetics/diagnostics',
        'applied/coherence-cybernetics/learning-bounds',
      ],
    },
    {
      type: 'category',
      label: 'Predictions & Programs',
      items: [
        'applied/coherence-cybernetics/predictions',
        'applied/coherence-cybernetics/philosophy',
        'applied/coherence-cybernetics/comparison',
        {
          type: 'link',
          label: '→ Cognitive Hierarchy',
          href: '/docs/consciousness/comparative/cognitive-hierarchy',
        },
        'applied/coherence-cybernetics/research-programs',
      ],
    },
    {
      type: 'category',
      label: 'Applications & Implementation',
      items: [
        'applied/coherence-cybernetics/applications',
        'applied/coherence-cybernetics/interdisciplinary',
        'applied/coherence-cybernetics/measurement',
        'applied/coherence-cybernetics/exercises',
        'applied/coherence-cybernetics/implementation',
      ],
    },
  ],

  research: [
    'applied/research/measurement-protocol',
    'applied/research/engineering-insights',
    'applied/research/poincare-perelman',
    'applied/research/gap-diagnostics',
    'applied/research/symbolic-correspondence',
  ],

  reference: [
    'reference/glossary',
    'reference/notation',
    'reference/falsifiability',
    'reference/specification',
    'reference/computational',
    'reference/status-registry',
  ],
};

export default sidebars;
