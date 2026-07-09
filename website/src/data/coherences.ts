/**
 * SINGLE SOURCE OF TRUTH for the seven dimensions and the 21 coherences of Γ.
 *
 * Consumed by BOTH:
 *   - the homepage matrix visualization (src/pages/index.tsx), and
 *   - the corpus (docs/core/dynamics/coherence-matrix.md via <CoherenceTable/>).
 *
 * Editing a name/meaning here updates every place at once — the homepage and the
 * corpus can no longer drift apart. Names/meanings are the canonical values of
 * `core/dynamics/coherence-matrix.md`; keep them in sync with the theory here.
 */

export type Bilingual = {en: string; ru: string};

export type Cell = {
  key: string;        // e.g. 'AS' (row+col, row ≤ col alphabetically for pairs)
  i: string;          // row dimension letter
  j: string;          // col dimension letter
  diagonal: boolean;  // true for the 7 dimensions (i === j)
  name: Bilingual;
  meaning: Bilingual;
};

/** The seven dimensions, in canonical order. */
export const DIMENSIONS = ['A', 'S', 'D', 'L', 'E', 'O', 'U'] as const;

/** Diagonal (populations) — the seven dimensions. */
export const DIAGONAL: Cell[] = [
  {key: 'AA', i: 'A', j: 'A', diagonal: true, name: {en: 'Articulation', ru: 'Артикуляция'}, meaning: {en: 'Distinguishing activity', ru: 'Активность различения'}},
  {key: 'SS', i: 'S', j: 'S', diagonal: true, name: {en: 'Structure', ru: 'Структура'}, meaning: {en: 'Form stability', ru: 'Стабильность формы'}},
  {key: 'DD', i: 'D', j: 'D', diagonal: true, name: {en: 'Dynamics', ru: 'Динамика'}, meaning: {en: 'Process activity', ru: 'Активность процесса'}},
  {key: 'LL', i: 'L', j: 'L', diagonal: true, name: {en: 'Logic', ru: 'Логика'}, meaning: {en: 'Internal consistency', ru: 'Внутренняя согласованность'}},
  {key: 'EE', i: 'E', j: 'E', diagonal: true, name: {en: 'Interiority', ru: 'Интериорность'}, meaning: {en: 'Intensity of interior states', ru: 'Интенсивность внутренних состояний'}},
  {key: 'OO', i: 'O', j: 'O', diagonal: true, name: {en: 'Ground', ru: 'Основание'}, meaning: {en: 'Connection to source', ru: 'Связь с источником'}},
  {key: 'UU', i: 'U', j: 'U', diagonal: true, name: {en: 'Unity', ru: 'Единство'}, meaning: {en: 'Integration', ru: 'Интеграция'}},
];

/** The 21 off-diagonal coherences (canonical names + fundamental meanings). */
export const COHERENCES: Cell[] = [
  {key: 'AS', i: 'A', j: 'S', diagonal: false, name: {en: 'Morphogenesis', ru: 'Морфогенез'}, meaning: {en: 'Crystallization of distinctions into stable forms', ru: 'Кристаллизация различий в устойчивые формы'}},
  {key: 'AD', i: 'A', j: 'D', diagonal: false, name: {en: 'Actualization', ru: 'Актуализация'}, meaning: {en: 'Potential distinction actualized in process', ru: 'Потенциальное различение, актуализированное в процессе'}},
  {key: 'AL', i: 'A', j: 'L', diagonal: false, name: {en: 'Predication', ru: 'Предикация'}, meaning: {en: 'Distinction that has become a logical predicate', ru: 'Различение, ставшее логическим предикатом'}},
  {key: 'AE', i: 'A', j: 'E', diagonal: false, name: {en: 'Apperception', ru: 'Апперцепция'}, meaning: {en: 'Distinction that has entered interiority', ru: 'Различение, вошедшее в интериорность'}},
  {key: 'AO', i: 'A', j: 'O', diagonal: false, name: {en: 'Spontaneity', ru: 'Спонтанность'}, meaning: {en: 'Arising of distinctions from the ground without external cause', ru: 'Возникновение различений из основания без внешней причины'}},
  {key: 'AU', i: 'A', j: 'U', diagonal: false, name: {en: 'Differentiation', ru: 'Дифференциация'}, meaning: {en: 'Distinction that preserves wholeness', ru: 'Различение, сохраняющее целостность'}},
  {key: 'SD', i: 'S', j: 'D', diagonal: false, name: {en: 'Persistence', ru: 'Персистенция'}, meaning: {en: 'Form maintained through process', ru: 'Форма, сохраняющаяся через процесс'}},
  {key: 'SL', i: 'S', j: 'L', diagonal: false, name: {en: 'Nomos', ru: 'Номос'}, meaning: {en: 'Structure possessing logical necessity', ru: 'Структура, обладающая логической необходимостью'}},
  {key: 'SE', i: 'S', j: 'E', diagonal: false, name: {en: 'Representation', ru: 'Репрезентация'}, meaning: {en: 'Structure represented in interiority', ru: 'Структура, представленная в интериорности'}},
  {key: 'SO', i: 'S', j: 'O', diagonal: false, name: {en: 'Archetype', ru: 'Архетип'}, meaning: {en: 'Stable forms rooted in the ground', ru: 'Устойчивые формы, укоренённые в основании'}},
  {key: 'SU', i: 'S', j: 'U', diagonal: false, name: {en: 'Symmetry', ru: 'Симметрия'}, meaning: {en: 'Structural expression of unity', ru: 'Структурное выражение единства'}},
  {key: 'DL', i: 'D', j: 'L', diagonal: false, name: {en: 'Regulation', ru: 'Регуляция'}, meaning: {en: 'Logically governed process', ru: 'Логически управляемый процесс'}},
  {key: 'DE', i: 'D', j: 'E', diagonal: false, name: {en: 'Affection', ru: 'Аффекция'}, meaning: {en: 'Action of process on interiority', ru: 'Действие процесса на интериорность'}},
  {key: 'DO', i: 'D', j: 'O', diagonal: false, name: {en: 'Genesis', ru: 'Генезис'}, meaning: {en: 'Generative process from the ground', ru: 'Порождающий процесс из основания'}},
  {key: 'DU', i: 'D', j: 'U', diagonal: false, name: {en: 'Teleology', ru: 'Телеология'}, meaning: {en: 'Integrated directed change', ru: 'Интегрированное направленное изменение'}},
  {key: 'LE', i: 'L', j: 'E', diagonal: false, name: {en: 'Evidence', ru: 'Эвиденция'}, meaning: {en: 'Logical coherence in interiority', ru: 'Логическая связность в интериорности'}},
  {key: 'LO', i: 'L', j: 'O', diagonal: false, name: {en: 'Grounding', ru: 'Фундирование'}, meaning: {en: 'Logic rooted in the ground', ru: 'Логика, укоренённая в основании'}},
  {key: 'LU', i: 'L', j: 'U', diagonal: false, name: {en: 'Consistency', ru: 'Консистентность'}, meaning: {en: 'Logical non-contradiction of the whole', ru: 'Логическая непротиворечивость целого'}},
  {key: 'EO', i: 'E', j: 'O', diagonal: false, name: {en: 'Immanence', ru: 'Имманентность'}, meaning: {en: 'Ground present within interiority', ru: 'Основание, присутствующее внутри интериорности'}},
  {key: 'EU', i: 'E', j: 'U', diagonal: false, name: {en: 'Synthesis', ru: 'Синтез'}, meaning: {en: 'Integration of interior content into the whole', ru: 'Интеграция интериорного содержания в целое'}},
  {key: 'OU', i: 'O', j: 'U', diagonal: false, name: {en: 'Completeness', ru: 'Полнота'}, meaning: {en: 'Identity of source and whole', ru: 'Тождество источника и целого'}},
];

/** All 28 cells (7 diagonal + 21 coherences), keyed for O(1) lookup. */
export const CELLS: Record<string, Cell> = Object.fromEntries(
  [...DIAGONAL, ...COHERENCES].map((c) => [c.key, c]),
);

/** Lookup by an unordered (i,j) pair, e.g. cellOf('O','L') === LO. */
export function cellOf(a: string, b: string): Cell {
  const key = a <= b ? `${a}${b}` : `${b}${a}`;
  return CELLS[key];
}

/** Pick the field for the current locale, falling back to English. */
export function tr(value: Bilingual, locale: string): string {
  return locale === 'ru' ? value.ru : value.en;
}
