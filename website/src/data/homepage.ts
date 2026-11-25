import type {Bilingual} from './coherences';

// Homepage copy is strictly paired EN/RU so both locales share the exact post-v11 claims, numbers, and links.
export const homeCopy = {
  name: {en: 'Unitary Holonomic Monism · Post-v11 Architecture', ru: 'Унитарный Голономный Монизм · Архитектура v11'},
  title: {en: 'From relations', ru: 'От отношений'},
  titleAccent: {en: 'to a whole.', ru: 'к целому.'},
  intro: {
    en: 'A stratified, machine-verified research programme — from a seven-dimensional coherence space 𝒟(ℂ⁷) through an explicit Clifford / Pati–Salam lift to background-free 4D gravity and formal bounds on consciousness.',
    ru: 'Стратифицированная, машинно верифицируемая исследовательская программа — от семимерного пространства когерентности 𝒟(ℂ⁷) через явный лифт Клиффорда / Пати–Салама к бесфоновой 4D гравитации и формальным границам сознания.',
  },
  description: {
    en: 'Every theorem, explicit bridge postulate, strict falsification [✗], and open barrier [P] is separated across three ontological strata — backed by a 100% choice-free Lean 4 kernel (0 Classical.choice) and reproducible numerical audit suites.',
    ru: 'Каждая теорема, явный связующий постулат, строгое опровержение [✗] и открытый барьер [P] разведены по трём онтологическим стратам — с опорой на полностью безвыборное ядро Lean 4 (0 Classical.choice) и воспроизводимые вычислительные стенды.',
  },
  explore: {en: 'Explore the architecture', ru: 'Исследовать архитектуру'},
  kernel: {en: 'Mathematical kernel', ru: 'Математическое ядро'},
  frontierLedger: {en: 'Frontier ledger', ru: 'Реестр рубежей'},
  premises: {en: 'Premises', ru: 'Предпосылки'},
  registry: {en: 'Status registry', ru: 'Реестр статусов'},
  interactive: {en: 'Live seven-dimensional state instrument', ru: 'Интерактивный прибор семимерного состояния'},
  interactiveHint: {en: 'Vary coherence s · inspect PG(2,2) Fano · test Born readouts.', ru: 'Меняйте когерентность s · исследуйте Фано PG(2,2) · проверяйте измерения Борна.'},
  factNote: {en: 'Post-v11 verified baseline', ru: 'Верифицированный срез v11'},
  factStateLabel: {en: 'roles · coherence pairs · real parameters in 𝒟(ℂ⁷)', ru: 'ролей · пар когерентностей · вещественных параметров в 𝒟(ℂ⁷)'},
  factStrataLabel: {en: 'explicit ontological strata (zero overclaiming)', ru: 'явных онтологических страты (ноль завышенных заявлений)'},
  factLeanLabel: {en: 'Lean 4 modules · 0 Classical.choice (15,544 decls)', ru: 'модуля Lean 4 · 0 Classical.choice (15 544 деклараций)'},
  factSuitesLabel: {en: 'deep frontier suites · 165/165 core checks passing', ru: 'глубоких рубежа проверок · 165/165 чисел ядра'},
  frameworkLabel: {en: '01 / Stratified architecture', ru: '01 / Стратифицированная архитектура'},
  frameworkTitle: {en: 'Four core objects. Three explicit strata.', ru: 'Четыре базовых объекта. Три явные страты.'},
  frameworkLead: {
    en: 'UHM models organization through states, channels, self-models, and measurements, then draws an explicit epistemic boundary between what follows from 𝒟(ℂ⁷) internally and what requires external lifts or new physics.',
    ru: 'УГМ описывает организацию через состояния, каналы, самомодели и измерения, а затем проводит жёсткую эпистемическую границу между тем, что следует из 𝒟(ℂ⁷) внутренне, и тем, что требует явных лифтов или новой физики.',
  },
  matrixLabel: {en: '02 / The language of relations', ru: '02 / Язык отношений'},
  matrixTitle: {en: 'Seven roles. Twenty-one coherences. One Fano geometry.', ru: 'Семь ролей. Двадцать одна когерентность. Одна геометрия Фано.'},
  matrixText: {
    en: 'A holon is represented by a 7 × 7 density matrix Γ. Seven diagonal populations and 21 complex coherence pairs form 48 real parameters, while the oriented Fano plane PG(2,2) links every off-diagonal pair to a unique third role.',
    ru: 'Холон представлен матрицей плотности Γ размера 7 × 7. Семь диагональных населённостей и 21 пара комплексных когерентностей дают 48 вещественных параметров, а ориентированная плоскость Фано PG(2,2) связывает каждую внедиагональную пару с единственной третьей ролью.',
  },
  matrixHelp: {en: 'Select any cell to read its semantic role, Hermitian conjugate, and Fano product. Arrow keys move across the matrix.', ru: 'Выберите ячейку, чтобы увидеть её смысловую роль, эрмитово сопряжение и произведение Фано. Стрелки перемещают фокус.'},
  matrixTable: {en: 'Semantic map of the coherence matrix; select a cell', ru: 'Смысловая карта матрицы когерентности; выберите ячейку'},
  interpretation: {en: 'Semantic interpretation', ru: 'Семантическое прочтение'},
  diagonal: {en: 'Diagonal population', ru: 'Диагональная населённость'},
  coherence: {en: 'Complex coherence', ru: 'Комплексная когерентность'},
  fanoRuleLabel: {en: 'Fano triple', ru: 'Тройка Фано'},
  matrixNote: {
    en: 'Role names are an interpretive frame [I]. Functional meaning is never derived from a matrix entry alone without an explicit measurement bridge.',
    ru: 'Имена ролей задают интерпретационную рамку [I]. Функциональный смысл не выводится из одного элемента матрицы без явного моста измерения.',
  },
  matrixLink: {en: 'State space and semantic dictionary', ru: 'Пространство состояний и словарь смыслов'},
  bridgesLabel: {en: '03 / Frontiers & potential', ru: '03 / Рубежи и потенциал'},
  bridgesTitle: {en: 'Where the programme reaches today — and what it unlocks.', ru: 'Куда программа дошла сегодня — и какой потенциал открывает.'},
  bridgesLead: {
    en: 'Four coupled research wings turn abstract state geometry into sharp physical predictions, strict no-go theorems, formal consciousness bounds, and verifiable cybernetic architectures.',
    ru: 'Четыре сопряжённых исследовательских крыла превращают геометрию состояний в точные физические проверки, жёсткие теоремы запрета, формальные границы сознания и верифицируемые кибернетические архитектуры.',
  },
  statusLabel: {en: '04 / Epistemic ledger & verification', ru: '04 / Эпистемический реестр и верификация'},
  statusTitle: {en: 'A theory judged by what it proves — and what it rules out.', ru: 'Теория, о которой судят по доказанному — и по тому, что она смеет опровергнуть.'},
  statusLead: {
    en: 'Unlike speculative frameworks, UHM maintains an explicit falsification ledger [✗] alongside its proved theorems [T], explicit bridge choices [C/D/I], and open problems [P].',
    ru: 'В отличие от спекулятивных схем, УГМ ведёт открытый реестр строгих опровержений [✗] наравне с доказанными теоремами [T], явными мостами [C/D/I] и открытыми проблемами [P].',
  },
  verificationTitle: {en: 'Four-corpus machine-checked verification backbone', ru: 'Четырёхкорпусный контур машинной верификации'},
  verificationText: {
    en: 'Holon is cross-linked and audited alongside math-foundations (64 Lean 4 modules, 169 strictly zero-axiom theorems, 689 #print axioms checks, 0 Classical.choice), math-msfs (EN/RU preprint & Verum corpus), and diakrisis (13-axiom 2-categorical metatheory).',
    ru: 'Holon сквозно связан и проверяется вместе с math-foundations (64 модуля Lean 4, 169 строго безаксиомных теорем, 689 проверок #print axioms, 0 Classical.choice), math-msfs (препринт EN/RU и корпус Verum) и diakrisis (13-аксиомная 2-категорная метатеория).',
  },
  verificationLink: {en: 'Network results & Lean audit', ru: 'Сетевые результаты и аудит Lean'},
  falsifiability: {en: 'Tests and falsification criteria', ru: 'Проверки и критерии опровержения'},
  corpusLabel: {en: '05 / Navigate the corpus', ru: '05 / Навигация по корпусу'},
  corpusTitle: {en: 'Choose your path through the theory.', ru: 'Выберите свой путь по теории.'},
  corpusLead: {
    en: 'Enter through the choice-free mathematical kernel, inspect the v1–v11 physical frontier ledger, or explore consciousness and coherence cybernetics.',
    ru: 'Начните с безвыборного математического ядра, изучите сводку физических рубежей v1–v11 или перейдите к сознанию и когерентной кибернетике.',
  },
  filters: {en: 'Filter the corpus by subject', ru: 'Разделы корпуса по темам'},
  all: {en: 'All', ru: 'Все'},
  foundations: {en: 'Foundations', ru: 'Основания'},
  dynamics: {en: 'Dynamics', ru: 'Динамика'},
  mind: {en: 'Consciousness', ru: 'Сознание'},
  physics: {en: 'Physics', ru: 'Физика'},
  research: {en: 'Research', ru: 'Исследования'},
  readingStart: {en: 'Recommended entry', ru: 'Рекомендуемый вход'},
  readingTitle: {en: 'Start with the idea. Audit every step to the Lean kernel.', ru: 'Начните с идеи. Проверьте каждый шаг до ядра Lean 4.'},
  readingText: {
    en: 'The introduction maps the programme; the mathematical kernel fixes every definition, and the frontier ledger records every theorem, falsification, and open wall.',
    ru: 'Введение задаёт общую карту, математическое ядро фиксирует каждое определение, а реестр рубежей документирует каждую теорему, опровержение и открытую стену.',
  },
  introduction: {en: 'Read the introduction', ru: 'Читать введение'},
  metadataTitle: {en: 'Stratified Ontology, Choice-Free Proofs & Physical Frontiers', ru: 'Стратифицированная онтология, безвыборные доказательства и физический рубеж'},
  metadataDescription: {
    en: 'Unitary Holonomic Monism (UHM): a stratified, machine-verified research programme connecting 𝒟(ℂ⁷) coherence geometry, Kähler–Dirac / CCvS Pati–Salam lifts, 4D simplicial Regge gravity, consciousness bounds, and a choice-free Lean 4 kernel.',
    ru: 'Унитарный Голономный Монизм (УГМ): стратифицированная машинно верифицируемая программа, связывающая геометрию 𝒟(ℂ⁷), лифт CCvS Пати–Салама, 4D симплициальную гравитацию Редже, границы сознания и безвыборное ядро Lean 4.',
  },
} satisfies Record<string, Bilingual>;

export type HomeCopyKey = keyof typeof homeCopy;
export type Subject = 'foundations' | 'dynamics' | 'mind' | 'physics' | 'research';

type Entry = {id: string; symbol: string; title: Bilingual; text: Bilingual; link: string};
type FrontierEntry = Entry & {stratum: Bilingual; highlight: Bilingual};

export const framework: Entry[] = [
  {
    id: 'state',
    symbol: 'Γ',
    title: {en: 'State', ru: 'Состояние'},
    text: {
      en: 'A positive unit-trace 7 × 7 density matrix Γ ∈ 𝒟(ℂ⁷) encoding 7 populations and 21 complex coherences (48 real parameters), saturating Φ ≤ 7P − 1.',
      ru: 'Положительная матрица плотности Γ ∈ 𝒟(ℂ⁷) с единичным следом: 7 населённостей и 21 комплексная когерентность (48 вещественных параметров), точная граница Φ ≤ 7P − 1.',
    },
    link: '/docs/reference/mathematical-kernel#states-processes',
  },
  {
    id: 'process',
    symbol: '𝒦',
    title: {en: 'Process', ru: 'Процесс'},
    text: {
      en: 'Linear CPTP channels and a specified open-system law combining Hamiltonian rotation, dissipation, and state-dependent regeneration with explicit well-posedness.',
      ru: 'Линейные CPTP-каналы и заданный закон эволюции открытой системы, объединяющий гамильтоново вращение, диссипацию и регенерацию с явными условиями корректности.',
    },
    link: '/docs/core/dynamics/evolution',
  },
  {
    id: 'self',
    symbol: 'M(Γ)',
    title: {en: 'Self-model', ru: 'Самомодель'},
    text: {
      en: 'A bounded feedback operator participating in regeneration and reflection (R = 1 / 7P), cleanly separated across finite-step, limit, and reset constructions.',
      ru: 'Ограниченный оператор обратной связи, участвующий в регенерации и рефлексии (R = 1 / 7P), строго разделённый на конечношаговые, предельные и сбросовые конструкции.',
    },
    link: '/docs/core/operators/phi-operator',
  },
  {
    id: 'observation',
    symbol: 'p(y | Γ)',
    title: {en: 'Observation', ru: 'Наблюдение'},
    text: {
      en: 'Born-rule POVMs linking Γ to empirical data, quantum Darwinism fiber stability, and identifiability bounds governing full 48-parameter tomography.',
      ru: 'POVM-измерения по правилу Борна, связывающие Γ с данными, квантовый дарвинизм и границы идентифицируемости для полной 48-параметрической томографии.',
    },
    link: '/docs/applied/research/reconstruction-identifiability',
  },
];

export const bridges: FrontierEntry[] = [
  {
    id: 'particles',
    symbol: '01',
    stratum: {en: 'Stratum B · F-42', ru: 'Страта B · F-42'},
    title: {en: 'Gauge symmetry, CCvS Pati–Salam & leptogenesis', ru: 'Калибровочная симметрия, CCvS Пати–Салама и лептогенез'},
    text: {
      en: 'The Kähler–Dirac Cl₀,₇ spinor lift S_{φ} ≅ 4_{ℂ} (Stab_{Spin(7)}(e_{O}) = Spin(6) ≅ SU(4)_{C}) restores KO-dim 6 on ℂ³², bypasses the F-41 heterotic no-go, unifies at α_{GUT}^{−1} = 45.15 (exact 4-color 2-loop RGE), stabilizes m_{h} = 125.25 GeV via Δ_{R}, and yields 2D LPM leptogenesis within 2.37% of Planck.',
      ru: 'Спинорный лифт Кэлера–Дирака Cl₀,₇ S_{φ} ≅ 4_{ℂ} (Stab_{Spin(7)}(e_{O}) ≅ SU(4)_{C}) восстанавливает KO-6 на ℂ³², обходит запрет F-41, объединяется при α_{GUT}^{−1} = 45.15 (4-цветный 2-петлевой РГ), стабилизирует m_{h} = 125.25 ГэВ через Δ_{R} и даёт 2D LPM лептогенез в 2.37% от Planck.',
    },
    highlight: {en: 'Open: Heavy-Threshold Split (10¹⁵ GeV), Re τ = 1/4 CP & N_{g} = 3', ru: 'Открыто: порог Split (10¹⁵ ГэВ), CP Re τ = 1/4 и N_{g} = 3'},
    link: '/docs/physics/overview',
  },
  {
    id: 'gravity',
    symbol: '02',
    stratum: {en: 'Stratum C · Super-F-40', ru: 'Страта C · Super-F-40'},
    title: {en: '4D quantum gravity & simplicial Regge–Schläfli', ru: '4D квантовая гравитация и симплициальный Редже–Шлефли'},
    text: {
      en: 'Induced 4D GR matches Ward identities through O(h⁴), while Super-F-40 closes every 4D Dirac spectral action (positive or signed) and fixed 4D lattices (naive, overlap, Delaunay) via universal zero-sum ghost and diffeo-mass obstructions — isolating background-free 4D deformed S⁴ Regge–Schläfli (10 conformal vs 30 positive TT modes).',
      ru: 'Индуцированная 4D ОТО сходится до O(h⁴), а Super-F-40 закрывает все 4D дираковские спектральные действия и фиксированные решётки (наивную, overlap, Делоне), выделяя бесфоновый 4D деформированный S⁴ Редже–Шлефли (10 конформных vs 30 положительных TT спин-2 мод).',
    },
    highlight: {en: 'Open: continuum UV fixed point lim Z_{N} of 4D Regge/CDT', ru: 'Открыто: континуальный UV-предел lim Z_{N} в 4D Редже/CDT'},
    link: '/docs/physics/gravity/quantum-gravity',
  },
  {
    id: 'mind',
    symbol: '03',
    stratum: {en: 'Stratum A · L₀–L₄', ru: 'Страта A · L₀–L₄'},
    title: {en: 'Consciousness, interiority & operational criteria', ru: 'Сознание, интериорность и операционные критерии'},
    text: {
      en: 'Formalizes viability (P > 2/7), reflection (R ≥ 1/3 → P ∈ (2/7, 3/7]), integration (Φ ≤ 7P − 1), and the L₀–L₄ functional hierarchy with explicit enriched-Yoneda relational geometry — cleanly separating proven algebraic bounds from the empirical two-aspect bridge.',
      ru: 'Формализует жизнеспособность (P > 2/7), рефлексию (R ≥ 1/3 → P ∈ (2/7, 3/7]), интеграцию (Φ ≤ 7P − 1) и функциональную иерархию L₀–L₄ с точной реляционной геометрией Йонеды, чётко отделяя теоремы от эмпирического моста.',
    },
    highlight: {en: 'Potential: falsifiable neural & artificial interiority protocols', ru: 'Потенциал: фальсифицируемые протоколы для мозга и ИИ'},
    link: '/docs/consciousness/overview',
  },
  {
    id: 'cybernetics',
    symbol: '04',
    stratum: {en: 'Applied · Choice-Free', ru: 'Прикладное · Без AC'},
    title: {en: 'Coherence cybernetics & verifiable AGI architectures', ru: 'Когерентная кибернетика и верифицируемые архитектуры AGI'},
    text: {
      en: 'Translates viability corridors, bounded self-models, and choice-free formal verification (64 Lean 4 modules, TranslationAdequacy) into operational criteria for self-monitoring agents, calibrated reconstruction, and non-hallucinating autonomous reasoning.',
      ru: 'Переводит коридоры жизнеспособности, ограниченные самомодели и безвыборную верификацию (64 модуля Lean 4, TranslationAdequacy) в операционные критерии для самонаблюдающих агентов, томографии и негаллюцинирующего автономного вывода.',
    },
    highlight: {en: 'Potential: mathematically auditable autonomous cognition', ru: 'Потенциал: математически аудируемая автономная когниция'},
    link: '/docs/applied/coherence-cybernetics/introduction',
  },
];

export const statusGroups = [
  {
    id: 'mathematics',
    badge: '[T]',
    title: {en: 'Proved & machine-checked', ru: 'Доказано и проверено машинно'},
    items: [
      {
        text: {en: 'Choice-free Lean 4 kernel: 64 modules, 15,544 decls, 689 audited, 169 zero-axiom (0 Classical.choice).', ru: 'Безвыборное ядро Lean 4: 64 модуля, 15 544 деклараций, 689 проверок, 169 безаксиомных (0 Classical.choice).'},
        link: '/docs/reference/network-results',
      },
      {
        text: {en: 'Exact integration bound Φ ≤ 7P − 1, viability interval (2/7, 3/7], and F-42 KO-6 / ℂ³² CCvS lift.', ru: 'Точная граница Φ ≤ 7P − 1, окно (2/7, 3/7] и лифт F-42 (KO-6 на ℂ³², орбита vs полные флуктуации).'},
        link: '/docs/reference/mathematical-kernel#thresholds',
      },
      {
        text: {en: '4D deformed S⁴ Regge–Schläfli (1.50×10⁻¹⁵; 10 conformal vs 30 TT spin-2 modes) & 2D LPM leptogenesis (−2.37%).', ru: '4D деформированный S⁴ Редже–Шлефли (1.50×10⁻¹⁵; 10 конформных vs 30 TT мод) и 2D LPM лептогенез (−2.37%).'},
        link: '/docs/reference/frontier-ledger#toe-frontier-summary',
      },
    ],
  },
  {
    id: 'falsified',
    badge: '[✗]',
    title: {en: 'Strictly falsified (closed)', ru: 'Строго опровергнуто (закрыто)'},
    items: [
      {
        text: {en: 'Super-F-40: ALL 4D Dirac spectral actions (positive or signed) & fixed 4D lattices fail as UV gravity.', ru: 'Super-F-40: ВСЕ 4D дираковские спектральные действия (любой χ) и фиксированные решётки не дают UV-гравитацию.'},
        link: '/docs/physics/gravity/quantum-gravity',
      },
      {
        text: {en: 'F-41 (0 axioms): 126̄_{H} / 210_{H} excluded from all ADE unfoldings & heterotic strings (c = 225/13 > 16); ⟨16̄_{H}⟩ breaks ℤ₂^{DM}.', ru: 'F-41 (0 аксиом): 126̄_{H} / 210_{H} невозможны в ADE и гетеротической струне (c = 225/13 > 16); ⟨16̄_{H}⟩ ломает ℤ₂^{DM}.'},
        link: '/docs/physics/cosmology-phys/dark-matter',
      },
      {
        text: {en: 'Retracted V10.2.A (Re τ₁₂ metric-vs-C₃-axion error), light (6,1,1)_{ℂ} proton decay, and internal Λ/WGC routes.', ru: 'Отозвано V10.2.A (ошибка Re τ₁₂ vs аксион C₃), лёгкий (6,1,1)_{ℂ} распад протона и внутренние маршруты Λ/WGC.'},
        link: '/docs/reference/frontier-ledger#toe-frontier-summary',
      },
    ],
  },
  {
    id: 'bridges',
    badge: '[C] [D] [I]',
    title: {en: 'Explicit lifts & choices', ru: 'Явные лифты и постулаты'},
    items: [
      {
        text: {en: 'Postulate (QG) for 𝒟(ℂ⁷), seven semantic roles, and Stratum B Clifford/CCvS lift (Cl₀) + KO-6 + (P).', ru: 'Постулат (QG) для 𝒟(ℂ⁷), семь смысловых ролей и лифт Страты B (Cl₀) + KO-6 + (P).'},
        link: '/docs/reference/premises',
      },
      {
        text: {en: 'Heavy-Threshold Split (10¹⁵ GeV) & Δ_{R} portal matching m_{h} = 125.25 GeV and preserving M_{PS} > M_{N1}.', ru: 'Пороговое расщепление Split (10¹⁵ ГэВ) и портал Δ_{R} для m_{h} = 125.25 ГэВ и M_{PS} > M_{N1}.'},
        link: '/docs/physics/gauge-symmetry/rg-flow',
      },
      {
        text: {en: 'Two-aspect interpretation of interiority and empirical POVM readout protocols.', ru: 'Двухаспектная интерпретация интериорности и эмпирические протоколы POVM-реконструкции.'},
        link: '/docs/consciousness/foundations/two-aspect-monism',
      },
    ],
  },
  {
    id: 'open',
    badge: '[P]',
    title: {en: 'Open frontier', ru: 'Открытый рубеж'},
    items: [
      {
        text: {en: 'Non-perturbative continuum limit lim Z_{N} of 4D Regge/CDT gravity preserving G_{EE} = G_{Sak}.', ru: 'Непертурбативный континуальный предел lim Z_{N} 4D Редже/CDT с сохранением G_{EE} = G_{Sak}.'},
        link: '/docs/physics/gravity/quantum-gravity',
      },
      {
        text: {en: 'Non-heterotic microscopic origin of spontaneous CP (Re τ = 1/4), N_{g} = 3, and 10¹⁵ GeV (6,1,1)_{ℂ} splitting.', ru: 'Не-гетеротический источник спонтанного CP (Re τ = 1/4), N_{g} = 3 и расщепления (6,1,1)_{ℂ} на 10¹⁵ ГэВ.'},
        link: '/docs/physics/particle-physics/ckm-matrix',
      },
      {
        text: {en: 'Cosmological constant Λ ~ 10⁻¹²³, dynamical origin of 1_{F} dark matter, and empirical consciousness tests.', ru: 'Космологическая постоянная Λ ~ 10⁻¹²³, происхождение тёмной материи 1_{F} и эмпирические тесты сознания.'},
        link: '/docs/reference/falsifiability',
      },
    ],
  },
];

export const verificationMetrics: readonly {value: Bilingual; label: Bilingual}[] = [
  {value: {en: '64', ru: '64'}, label: {en: 'Lean 4 modules', ru: 'Модулей Lean 4'}},
  {value: {en: '15,544', ru: '15 544'}, label: {en: 'Checked decls', ru: 'Деклараций'}},
  {value: {en: '169', ru: '169'}, label: {en: 'Zero-axiom proofs', ru: '0-аксиом теорем'}},
  {value: {en: '0', ru: '0'}, label: {en: 'Classical.choice', ru: 'Classical.choice'}},
  {value: {en: '165/165', ru: '165/165'}, label: {en: 'Core numbers', ru: 'Чисел ядра'}},
  {value: {en: '1,138', ru: '1 138'}, label: {en: 'Kernel checks', ru: 'Проверок ядра'}},
];

export const corpus: (Entry & {subject: Subject})[] = [
  {id: 'kernel', symbol: '𝒟', subject: 'foundations', title: {en: 'Mathematical kernel', ru: 'Математическое ядро'}, text: {en: 'States, channels, Bures site scope, and the exact boundaries of each bridge.', ru: 'Состояния, каналы, границы сайта Бюреса и точная область каждой связи.'}, link: '/docs/reference/mathematical-kernel'},
  {id: 'structure', symbol: 'Γ', subject: 'foundations', title: {en: 'The holon & its structure', ru: 'Холон и его структура'}, text: {en: 'Seven semantic roles, 48 parameters, and the complete native Stratum A specification.', ru: 'Семь смысловых ролей, 48 параметров и полная спецификация Страты A.'}, link: '/docs/core/structure/holon'},
  {id: 'octonions', symbol: '𝕆', subject: 'foundations', title: {en: 'Octonions & Fano geometry', ru: 'Октонионы и геометрия Фано'}, text: {en: 'PG(2,2) incidence, G₂ symmetry, and conditional 7D minimality theorems.', ru: 'Инцидентность PG(2,2), симметрия G₂ и условные теоремы минимальности 7D.'}, link: '/docs/proofs/minimality/theorem-octonionic-derivation'},
  {id: 'evolution', symbol: '∂τ', subject: 'dynamics', title: {en: 'Evolution & viability', ru: 'Эволюция и жизнеспособность'}, text: {en: 'Hamiltonian motion, dissipation, bounded regeneration, and invariant viability domains.', ru: 'Гамильтонова динамика, диссипация, ограниченная регенерация и области жизнеспособности.'}, link: '/docs/core/dynamics/evolution'},
  {id: 'clock', symbol: 'τ', subject: 'dynamics', title: {en: 'Clocks, time & Gap', ru: 'Часы, время и Gap'}, text: {en: 'Clock registers, conditional histories, complex phases, and identification limits.', ru: 'Часовые регистры, условные истории, комплексные фазы и пределы идентификации.'}, link: '/docs/core/operators/emergent-time'},
  {id: 'consciousness', symbol: 'E', subject: 'mind', title: {en: 'Consciousness & interiority', ru: 'Сознание и интериорность'}, text: {en: 'Two-aspect monism, operational access bounds, and testable empirical questions.', ru: 'Двухаспектный монизм, операционные границы доступа и проверяемые вопросы.'}, link: '/docs/consciousness/overview'},
  {id: 'hierarchy', symbol: 'Lₙ', subject: 'mind', title: {en: 'Reflection & L-hierarchy', ru: 'Рефлексия и L-иерархия'}, text: {en: 'L₀–L₄ capability gates, explicit realizations, and reflection-depth conditions.', ru: 'Пороги способностей L₀–L₄, явные реализации и условия глубины рефлексии.'}, link: '/docs/consciousness/hierarchy/interiority-hierarchy'},
  {id: 'physics', symbol: '𝒢', subject: 'physics', title: {en: 'Physical bridges & CCvS', ru: 'Физические мосты и CCvS'}, text: {en: 'Stratum B Clifford/Pati–Salam lift, 2-loop RGE, Higgs, neutrinos, and 4D gravity.', ru: 'Лифт Клиффорда/Пати–Салама Страты B, 2-петлевой РГ, Хиггс, нейтрино и 4D гравитация.'}, link: '/docs/physics/overview'},
  {id: 'frontier', symbol: '⊞', subject: 'physics', title: {en: 'Frontier ledger (v1–v11)', ru: 'Реестр рубежей (v1–v11)'}, text: {en: 'Stratified ontology A/B/C, Super-F-40, F-41, F-42, falsified dead ends, and open walls.', ru: 'Стратифицированная онтология A/B/C, Super-F-40, F-41, F-42, опровержения и открытые стены.'}, link: '/docs/reference/frontier-ledger'},
  {id: 'measurement', symbol: 'y', subject: 'research', title: {en: 'Reconstruction & measurement', ru: 'Реконструкция и измерение'}, text: {en: 'Informational completeness, POVM uncertainty bounds, and identifiable tomography.', ru: 'Информационная полнота, границы неопределённости POVM и идентифицируемая томография.'}, link: '/docs/applied/research/reconstruction-identifiability'},
  {id: 'cybernetics', symbol: '↺', subject: 'research', title: {en: 'Coherence cybernetics', ru: 'Когерентная кибернетика'}, text: {en: 'Control protocols, autonomous stability, and verifiable cognitive-architecture criteria.', ru: 'Протоколы управления, устойчивость автономии и критерии верифицируемых когнитивных архитектур.'}, link: '/docs/applied/coherence-cybernetics/introduction'},
  {id: 'verification', symbol: '⊢', subject: 'research', title: {en: 'Network results & Lean audit', ru: 'Сетевые результаты и аудит Lean'}, text: {en: 'Four-corpus provenance, 64 choice-free Lean 4 modules, counterexamples, and falsifiability.', ru: 'Четырёхкорпусный провенанс, 64 безвыборных модуля Lean 4, контрпримеры и фальсифицируемость.'}, link: '/docs/reference/network-results'},
];
