import type {Bilingual} from './coherences';

// Homepage copy is paired so that both locales share the same claims and links.
export const homeCopy = {
  name: {en: 'Unitary Holonomic Monism', ru: 'Унитарный Голономный Монизм'},
  title: {en: 'From relations', ru: 'От отношений'},
  titleAccent: {en: 'to a whole.', ru: 'к целому.'},
  intro: {en: 'An ontology of the whole. A mathematics of states. A research programme connecting matter, time and experience.', ru: 'Онтология целого. Математика состояний. Исследовательская программа, связывающая материю, время и опыт.'},
  description: {en: 'UHM explores how a system’s organization, change and relation to itself can be expressed in a common language. Start with a state, explore its relations, then follow the bridges to physics and consciousness.', ru: 'УГМ исследует, как выразить организацию системы, её изменение и отношение к себе на общем языке. Начните с состояния, исследуйте его связи, затем перейдите к физике и сознанию.'},
  explore: {en: 'Explore the framework', ru: 'Исследовать фреймворк'},
  kernel: {en: 'Read the mathematics', ru: 'Перейти к математике'},
  premises: {en: 'Premises', ru: 'Предпосылки'},
  registry: {en: 'Result registry', ru: 'Реестр результатов'},
  interactive: {en: 'A state you can explore', ru: 'Состояние, которое можно исследовать'},
  interactiveHint: {en: 'Change the coherence. Compare the views.', ru: 'Меняйте когерентность. Сравнивайте представления.'},
  roles: {en: 'selected semantic roles', ru: 'выбранных смысловых ролей'},
  pairs: {en: 'complex coherence pairs', ru: 'комплексная пара когерентностей'},
  parameters: {en: 'independent real parameters', ru: 'независимых вещественных параметров'},
  factNote: {en: 'The native seven-dimensional state model', ru: 'Базовая семимерная модель состояния'},
  frameworkLabel: {en: '01 / The framework', ru: '01 / Фреймворк'},
  frameworkTitle: {en: 'A common language for a system and its relations.', ru: 'Общий язык для системы и её отношений.'},
  frameworkLead: {en: 'The ontological proposal treats the whole and its internal relations as primary. Its mathematical realization specifies four distinct ingredients.', ru: 'Онтологическая гипотеза ставит в основание целое и его внутренние отношения. Математическая реализация задаёт четыре отдельных компонента.'},
  categoricalTitle: {en: 'From local descriptions to global consistency', ru: 'От локальных описаний к глобальной согласованности'},
  categoricalText: {en: 'The sheaf layer organizes compatible local descriptions, including the higher coherence data needed for gluing. Its site of open sets specifies where descriptions apply and how they overlap.', ru: 'Пучковый слой организует совместимые локальные описания, включая высшие согласования, необходимые для склейки. Сайт открытых множеств задаёт области описаний и их пересечения.'},
  categoricalLink: {en: 'Explore the categorical foundation', ru: 'Категориальные основания'},
  matrixLabel: {en: '02 / The language of relations', ru: '02 / Язык отношений'},
  matrixTitle: {en: 'Seven roles. An entire field of relations.', ru: 'Семь ролей. Целое поле отношений.'},
  matrixText: {en: 'A holon is represented by a density matrix Γ. Seven diagonal populations and 21 independent complex coherence pairs describe its state in a chosen frame. Hermiticity and unit trace leave 48 independent real parameters.', ru: 'Холон представлен матрицей плотности Γ. Семь диагональных населённостей и 21 независимая комплексная пара когерентностей описывают его состояние в выбранном базисе. Эрмитовость и единичный след оставляют 48 независимых вещественных параметров.'},
  matrixHelp: {en: 'Select a cell to explore its meaning. Use arrow keys to move through the matrix.', ru: 'Выберите ячейку, чтобы исследовать её смысл. Для перемещения по матрице используйте клавиши со стрелками.'},
  matrixTable: {en: 'Semantic map of the coherence matrix; select a cell', ru: 'Смысловая карта матрицы когерентности; выберите ячейку'},
  interpretation: {en: 'Semantic interpretation', ru: 'Семантическое прочтение'},
  diagonal: {en: 'Diagonal population', ru: 'Диагональная населённость'},
  coherence: {en: 'Complex coherence', ru: 'Комплексная когерентность'},
  matrixNote: {en: 'The role names are an interpretive frame. A matrix entry alone does not establish a physical or experiential meaning.', ru: 'Имена ролей задают интерпретацию. Значение элемента матрицы само по себе не устанавливает его физический смысл или связь с переживанием.'},
  matrixLink: {en: 'State space and semantic dictionary', ru: 'Пространство состояний и словарь смыслов'},
  bridgesLabel: {en: '03 / Bridges to the world', ru: '03 / Связи с миром'},
  bridgesTitle: {en: 'One programme. Different kinds of questions.', ru: 'Одна программа. Разные исследовательские вопросы.'},
  bridgesLead: {en: 'The ambition is a unified account of reality. Each bridge names the extra structure and evidence it needs.', ru: 'Цель — единое описание реальности. Для каждой связи указаны необходимые дополнительные структуры и свидетельства.'},
  statusLabel: {en: '04 / What is established', ru: '04 / Что установлено'},
  statusTitle: {en: 'A theory with visible assumptions.', ru: 'Теория с явными предпосылками.'},
  statusLead: {en: 'The registry records the assumptions and status of the principal results. Mathematical proofs, model choices and empirical hypotheses have different roles.', ru: 'Реестр фиксирует предпосылки и статус основных результатов. Математические доказательства, выбор модели и эмпирические гипотезы выполняют разные функции.'},
  falsifiability: {en: 'Tests and falsification criteria', ru: 'Проверки и критерии опровержения'},
  corpusLabel: {en: '05 / The corpus', ru: '05 / Корпус теории'},
  corpusTitle: {en: 'Choose your path through the theory.', ru: 'Выберите свой путь по теории.'},
  corpusLead: {en: 'Begin with the kernel, follow a physical construction, or examine how the framework can be tested.', ru: 'Начните с математического ядра, проследите физическую конструкцию или изучите способы проверки фреймворка.'},
  filters: {en: 'Filter the corpus by subject', ru: 'Разделы корпуса по темам'},
  all: {en: 'All', ru: 'Все'},
  foundations: {en: 'Foundations', ru: 'Основания'},
  dynamics: {en: 'Dynamics', ru: 'Динамика'},
  mind: {en: 'Consciousness', ru: 'Сознание'},
  physics: {en: 'Physics', ru: 'Физика'},
  research: {en: 'Research', ru: 'Исследования'},
  readingStart: {en: 'A first reading', ru: 'Первое знакомство'},
  readingTitle: {en: 'Start with the idea. Follow it to the proof.', ru: 'Начните с идеи. Проследите её до доказательства.'},
  readingText: {en: 'The introduction gives the overall picture; the mathematical kernel specifies the objects, and the registry makes each result traceable.', ru: 'Введение даёт общую картину, математическое ядро определяет объекты, а реестр позволяет проследить обоснование каждого результата.'},
  introduction: {en: 'Read the introduction', ru: 'Читать введение'},
  metadataTitle: {en: 'Relations, states and the whole', ru: 'Отношения, состояния и целое'},
  metadataDescription: {en: 'Explore Unitary Holonomic Monism: an interactive coherence matrix, a mathematical framework of states and processes, and explicit research bridges to physics and consciousness.', ru: 'Исследуйте Унитарный Голономный Монизм: интерактивная матрица когерентности, математический фреймворк состояний и процессов, исследовательские связи с физикой и сознанием.'},
} satisfies Record<string, Bilingual>;

export type HomeCopyKey = keyof typeof homeCopy;
export type Subject = 'foundations' | 'dynamics' | 'mind' | 'physics' | 'research';

type Entry = {id: string; symbol: string; title: Bilingual; text: Bilingual; link: string};

export const framework: Entry[] = [
  {id: 'state', symbol: 'Γ', title: {en: 'State', ru: 'Состояние'}, text: {en: 'A density matrix encodes populations and coherences in a chosen frame. Its positivity and normalization define the admissible states.', ru: 'Матрица плотности кодирует населённости и когерентности в выбранном базисе. Положительность и нормировка определяют допустимые состояния.'}, link: '/docs/reference/mathematical-kernel#states-processes'},
  {id: 'process', symbol: '𝒦', title: {en: 'Process', ru: 'Процесс'}, text: {en: 'Channels describe allowed linear transformations. A specified evolution law adds Hamiltonian change, dissipation and regeneration.', ru: 'Каналы описывают допустимые линейные преобразования. Заданный закон эволюции объединяет гамильтоново изменение, диссипацию и регенерацию.'}, link: '/docs/core/dynamics/evolution'},
  {id: 'self', symbol: 'M(Γ)', title: {en: 'Self-model', ru: 'Самомодель'}, text: {en: 'A numerical self-model participates in feedback. Its state-preserving properties and stability need explicit conditions.', ru: 'Численная самомодель участвует в обратной связи. Сохранение допустимых состояний и устойчивость требуют явных условий.'}, link: '/docs/core/operators/phi-operator'},
  {id: 'observation', symbol: 'p(y | Γ)', title: {en: 'Observation', ru: 'Наблюдение'}, text: {en: 'An observation law connects states to data. Identifiability controls what can be recovered; stability and statistical analysis quantify uncertainty.', ru: 'Закон наблюдения связывает состояния с данными. Идентифицируемость определяет, что можно восстановить; устойчивость и статистический анализ оценивают неопределённость.'}, link: '/docs/applied/research/reconstruction-identifiability'},
];

export const bridges: Entry[] = [
  {id: 'physics', symbol: '01', title: {en: 'Matter & spacetime', ru: 'Материя и пространство-время'}, text: {en: 'Octonionic representations, symmetry and Lorentzian geometry. Physical correspondence requires supplied actions, clocks and calibrated parameters.', ru: 'Октонионные представления, симметрия и лоренцева геометрия. Физическое соответствие требует заданных действий, часов и калиброванных параметров.'}, link: '/docs/physics/overview'},
  {id: 'mind', symbol: '02', title: {en: 'Experience & self-reference', ru: 'Опыт и самореференция'}, text: {en: 'Interiority, distinctions and reports are studied through explicit representations. Their identification with experience is an ontological and empirical bridge.', ru: 'Интериорность, различения и отчёты изучаются через явные представления. Их отождествление с опытом — онтологическая и эмпирическая связь.'}, link: '/docs/consciousness/overview'},
  {id: 'engineering', symbol: '03', title: {en: 'Measurement & engineering', ru: 'Измерение и инженерия'}, text: {en: 'Coherence cybernetics turns model assumptions into reconstruction protocols, stability conditions and testable operational criteria.', ru: 'Когерентная кибернетика переводит предпосылки модели в протоколы реконструкции, условия устойчивости и проверяемые операционные критерии.'}, link: '/docs/applied/coherence-cybernetics/introduction'},
];

export const statusGroups = [
  {id: 'mathematics', badge: '[T]', title: {en: 'Mathematical results', ru: 'Математические результаты'}, items: [
    {text: {en: 'A specified Bures site and its sheaf semantics.', ru: 'Явно заданный сайт Бюреса и его пучковая семантика.'}, link: '/docs/reference/mathematical-kernel#bures-site'},
    {text: {en: 'The exact integration bound Φ ≤ 7P − 1.', ru: 'Точная граница интеграции Φ ≤ 7P − 1.'}, link: '/docs/reference/mathematical-kernel#thresholds'},
    {text: {en: 'State preservation for dynamics satisfying the stated assumptions.', ru: 'Сохранение состояний динамикой при указанных предпосылках.'}, link: '/docs/reference/mathematical-kernel#dynamics'},
  ]},
  {id: 'bridges', badge: '[D] [P] [H] [I]', title: {en: 'Choices & bridges', ru: 'Выбор модели и интерпретации'}, items: [
    {text: {en: 'Seven labelled roles and selected operational criteria.', ru: 'Семь именованных ролей и выбранные операционные критерии.'}, link: '/docs/core/structure/holon'},
    {text: {en: 'Physical representations and a separately specified clock.', ru: 'Физические представления и отдельно заданные часы.'}, link: '/docs/reference/premises'},
    {text: {en: 'The interpretation of the inner aspect as experience.', ru: 'Прочтение внутреннего аспекта как переживания.'}, link: '/docs/consciousness/foundations/two-aspect-monism'},
  ]},
  {id: 'open', badge: '[Pr]', title: {en: 'Open research', ru: 'Открытые исследования'}, items: [
    {text: {en: 'Observation laws and independent empirical validation.', ru: 'Законы наблюдения и независимая эмпирическая проверка.'}, link: '/docs/applied/research/reconstruction-identifiability'},
    {text: {en: 'The physical choice of self-model and regeneration rate.', ru: 'Физический выбор самомодели и скорости регенерации.'}, link: '/docs/core/dynamics/evolution'},
    {text: {en: 'Flavour parameters and the cosmological constant.', ru: 'Параметры ароматов и космологическая постоянная.'}, link: '/docs/physics/overview'},
  ]},
];

export const corpus: (Entry & {subject: Subject})[] = [
  {id: 'kernel', symbol: '𝒟', subject: 'foundations', title: {en: 'Mathematical kernel', ru: 'Математическое ядро'}, text: {en: 'States, channels, a genuine site and the exact scope of each bridge.', ru: 'Состояния, каналы, корректный сайт и точная область каждой связи.'}, link: '/docs/reference/mathematical-kernel'},
  {id: 'structure', symbol: 'Γ', subject: 'foundations', title: {en: 'The holon & its structure', ru: 'Холон и его структура'}, text: {en: 'Seven semantic roles, relations and the complete model specification.', ru: 'Семь смысловых ролей, отношения и полная спецификация модели.'}, link: '/docs/core/structure/holon'},
  {id: 'octonions', symbol: '𝕆', subject: 'foundations', title: {en: 'Octonions & dimensionality', ru: 'Октонионы и размерность'}, text: {en: 'Fano geometry, algebraic constructions and conditional minimality.', ru: 'Геометрия Фано, алгебраические конструкции и условная минимальность.'}, link: '/docs/proofs/minimality/theorem-octonionic-derivation'},
  {id: 'evolution', symbol: '∂τ', subject: 'dynamics', title: {en: 'Evolution & viability', ru: 'Эволюция и жизнеспособность'}, text: {en: 'Hamiltonian motion, dissipation, feedback and invariant state domains.', ru: 'Гамильтонова динамика, диссипация, обратная связь и инвариантные области состояний.'}, link: '/docs/core/dynamics/evolution'},
  {id: 'clock', symbol: 'τ', subject: 'dynamics', title: {en: 'Clocks & time', ru: 'Часы и время'}, text: {en: 'Clock registers, conditional readings and directed process histories.', ru: 'Часовые регистры, условные показания и направленные истории процессов.'}, link: '/docs/core/operators/emergent-time'},
  {id: 'gap', symbol: 'Δ', subject: 'dynamics', title: {en: 'Gap & phase structure', ru: 'Gap и фазовая структура'}, text: {en: 'Complex coherences, partial statistics and their limits of identification.', ru: 'Комплексные когерентности, частичные статистики и пределы идентификации.'}, link: '/docs/core/dynamics/gap-operator'},
  {id: 'consciousness', symbol: 'E', subject: 'mind', title: {en: 'Consciousness & interiority', ru: 'Сознание и интериорность'}, text: {en: 'Experiential interpretations, operational levels and empirical questions.', ru: 'Интерпретации опыта, операционные уровни и эмпирические вопросы.'}, link: '/docs/consciousness/overview'},
  {id: 'hierarchy', symbol: 'Lₙ', subject: 'mind', title: {en: 'Reflection & hierarchy', ru: 'Рефлексия и иерархия'}, text: {en: 'Capability gates, explicit realizations and conditions on depth.', ru: 'Критерии способностей, явные реализации и условия на глубину.'}, link: '/docs/consciousness/hierarchy/interiority-hierarchy'},
  {id: 'physics', symbol: '𝒢', subject: 'physics', title: {en: 'Physical correspondence', ru: 'Физические соответствия'}, text: {en: 'Symmetry, particles and spacetime under explicit bridge assumptions.', ru: 'Симметрия, частицы и пространство-время при явных связующих предпосылках.'}, link: '/docs/physics/overview'},
  {id: 'measurement', symbol: 'y', subject: 'research', title: {en: 'Reconstruction & measurement', ru: 'Реконструкция и измерение'}, text: {en: 'Informational completeness, uncertainty and identifiable observations.', ru: 'Информационная полнота, неопределённость и идентифицируемые наблюдения.'}, link: '/docs/applied/research/reconstruction-identifiability'},
  {id: 'cybernetics', symbol: '↺', subject: 'research', title: {en: 'Coherence cybernetics', ru: 'Когерентная кибернетика'}, text: {en: 'Research protocols, control, learning and stability.', ru: 'Исследовательские протоколы, управление, обучение и устойчивость.'}, link: '/docs/applied/coherence-cybernetics/introduction'},
  {id: 'verification', symbol: '⊢', subject: 'research', title: {en: 'Evidence & falsifiability', ru: 'Проверка и опровержимость'}, text: {en: 'Premises, result statuses, counterexamples and numerical checks.', ru: 'Предпосылки, статусы результатов, контрпримеры и численные проверки.'}, link: '/docs/reference/falsifiability'},
];
