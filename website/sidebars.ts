import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

/**
 * UHM Theory Documentation Sidebars
 *
 * Six main sections:
 * - theory: Core UHM theory (foundations, structure, dynamics, operators, categories)
 * - consciousness: Consciousness section (foundations, hierarchy, phenomenology, states, subjects, comparative, ethics-meaning)
 * - proofs: Formal proofs organized by domain (minimality, dynamics, categorical, consciousness, physics)
 * - physics: Physical correspondences (QM, gauge symmetry, particle physics, gravity, cosmology, dual aspect)
 * - cybernetics: Coherence Cybernetics (formal theory, operators, topology, predictions)
 * - research: Applied research (measurement protocols, engineering, diagnostics)
 * - reference: Glossary, notation, falsifiability, specification, computational, status registry
 */
const sidebars: SidebarsConfig = {
  theory: [
    'intro',
    {
      type: 'category',
      label: 'Основания',
      collapsed: false,
      items: [
        'core/foundations/axiom-omega',
        'core/foundations/axiom-septicity',
        'core/foundations/consequences',
        'core/foundations/spacetime',
      ],
    },
    {
      type: 'category',
      label: 'Структура реальности',
      items: [
        'core/structure/holon',
        {
          type: 'category',
          label: 'Семь измерений',
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
      label: 'Динамика',
      items: [
        'core/dynamics/coherence-matrix',
        'core/dynamics/evolution',
        'core/dynamics/viability',
        'core/dynamics/gap-thermodynamics',
        'core/dynamics/gap-dynamics',
        'core/dynamics/gap-operator',
        'core/dynamics/gap-phase-diagram',
        'core/dynamics/composite-systems',
      ],
    },
    {
      type: 'category',
      label: 'Операторы',
      items: [
        'core/operators/phi-operator',
        'core/operators/lindblad-operators',
        'core/operators/emergent-time',
      ],
    },
    {
      type: 'category',
      label: 'Категорный формализм',
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
      label: 'Математические основания',
      collapsed: false,
      items: [
        'consciousness/foundations/two-aspect-monism',
        'consciousness/foundations/interiority-theory',
        'consciousness/foundations/self-observation',
      ],
    },
    {
      type: 'category',
      label: 'Иерархия L0→L4',
      items: [
        'consciousness/hierarchy/interiority-hierarchy',
        'consciousness/hierarchy/depth-tower',
        'consciousness/hierarchy/gap-characterization',
        'consciousness/hierarchy/swallowtail-transitions',
      ],
    },
    {
      type: 'category',
      label: 'Структура опыта',
      items: [
        'consciousness/phenomenology/qualia-structure',
        'consciousness/phenomenology/emotional-taxonomy',
        'consciousness/phenomenology/temporal-consciousness',
        'consciousness/phenomenology/intentionality',
      ],
    },
    {
      type: 'category',
      label: 'Состояния сознания',
      items: [
        'consciousness/states/altered-states',
        'consciousness/states/unconscious',
        'consciousness/states/attention-memory',
        'consciousness/states/pathological',
      ],
    },
    {
      type: 'category',
      label: 'Субъекты сознания',
      items: [
        'consciousness/subjects/pre-linguistic',
        'consciousness/subjects/animal-consciousness',
        'consciousness/subjects/ai-consciousness',
        'consciousness/subjects/collective-consciousness',
      ],
    },
    {
      type: 'category',
      label: 'Сравнение теорий',
      items: [
        'consciousness/comparative/consciousness-theories',
        'consciousness/comparative/panpsychism-analysis',
        'consciousness/comparative/cognitive-hierarchy',
      ],
    },
    {
      type: 'category',
      label: 'Этика и смысл',
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
      label: 'Минимальность',
      collapsed: false,
      items: [
        'proofs/minimality/theorem-minimality-7',
        'proofs/minimality/theorem-octonionic-derivation',
      ],
    },
    {
      type: 'category',
      label: 'Динамика',
      items: [
        'proofs/dynamics/theorem-purity-critical',
        'proofs/dynamics/emergent-time',
        'proofs/dynamics/fep-derivation',
      ],
    },
    {
      type: 'category',
      label: 'Категорные доказательства',
      items: [
        'proofs/categorical/categorical-formalism',
        'proofs/categorical/formalization-phi',
        'proofs/categorical/uniqueness-theorem',
      ],
    },
    {
      type: 'category',
      label: 'Сознание',
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
      label: 'Физика',
      items: [
        'proofs/physics/physics-correspondence',
        'proofs/physics/emergent-manifold',
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
      label: 'Квантовая механика',
      items: [
        'physics/quantum-mechanics/qm-reduction',
        'physics/quantum-mechanics/measurement',
      ],
    },
    {
      type: 'category',
      label: 'Калибровочные симметрии',
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
      label: 'Физика частиц',
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
      label: 'Гравитация',
      items: [
        'physics/gravity/emergent-geometry',
        'physics/gravity/einstein-equations',
        'physics/gravity/cosmological-constant',
        'physics/gravity/quantum-gravity',
      ],
    },
    {
      type: 'category',
      label: 'Космология (физика)',
      items: [
        'physics/cosmology-phys/origin',
        'physics/cosmology-phys/dark-matter',
        'physics/cosmology-phys/berry-phase',
      ],
    },
    {
      type: 'category',
      label: 'Дуальный аспект',
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
      label: 'Формальные основания',
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
      label: 'Алгебра Gap-оператора',
      items: [
        'applied/coherence-cybernetics/gap-algebra',
        'applied/coherence-cybernetics/bifurcation',
        'applied/coherence-cybernetics/non-markovian',
        'applied/coherence-cybernetics/model-systems',
      ],
    },
    {
      type: 'category',
      label: 'Вариационная структура',
      items: [
        'applied/coherence-cybernetics/lagrangian',
        'applied/coherence-cybernetics/variational',
        'applied/coherence-cybernetics/effective-temperature',
      ],
    },
    {
      type: 'category',
      label: 'Топологическая защита',
      items: [
        'applied/coherence-cybernetics/topological-protection',
        'applied/coherence-cybernetics/phase-diagram-cc',
        'applied/coherence-cybernetics/goldstone-modes',
        'applied/coherence-cybernetics/g2-noether-cc',
      ],
    },
    {
      type: 'category',
      label: 'Контекст и сравнение',
      items: [
        'applied/coherence-cybernetics/cybernetics-history',
        {
          type: 'link',
          label: '→ Теории сознания',
          href: '/docs/consciousness/comparative/consciousness-theories',
        },
        {
          type: 'link',
          label: '→ Панпсихизм',
          href: '/docs/consciousness/comparative/panpsychism-analysis',
        },
      ],
    },
    {
      type: 'category',
      label: 'Сенсомоторная теория и стабильность',
      items: [
        'applied/coherence-cybernetics/sensorimotor',
        'applied/coherence-cybernetics/stability',
        'applied/coherence-cybernetics/diagnostics',
        'applied/coherence-cybernetics/learning-bounds',
      ],
    },
    {
      type: 'category',
      label: 'Предсказания и программы',
      items: [
        'applied/coherence-cybernetics/predictions',
        {
          type: 'link',
          label: '→ Когнитивная иерархия',
          href: '/docs/consciousness/comparative/cognitive-hierarchy',
        },
        'applied/coherence-cybernetics/research-programs',
      ],
    },
    {
      type: 'category',
      label: 'Приложения и реализация',
      items: [
        'applied/coherence-cybernetics/applications',
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
