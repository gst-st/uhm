import {useEffect, useId, useRef, useState} from 'react';
import type {KeyboardEvent} from 'react';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Link from '@docusaurus/Link';
import RichText from '@site/src/components/RichText';
import {cellOf, tr} from '@site/src/data/coherences';
import {BASIS, FANO_LINES, illustrativeState, pairReadout} from './model';
import type {ReadoutSetting} from './model';
import styles from './styles.module.css';

type View = 'relations' | 'matrix' | 'fano' | 'readout';

const CX = 240;
const CY = 153;
const POSITIONS = BASIS.map((_, j) => {
  const angle = -Math.PI / 2 + j * 2 * Math.PI / 7;
  return {x: CX + 112 * Math.cos(angle), y: CY + 112 * Math.sin(angle)};
});

/**
 * Canonical PG(2,2) Fano plane geometry with O (Ground, index 6 / 1-based 7)
 * at the exact barycenter:
 *   - Outer equilateral triangle vertices: D (top), E (bottom-left), U (bottom-right)
 *   - Edge midpoints on the inscribed circle [1,2,4] = (A, S, L): A (bottom), S (left), L (right)
 *   - Every one of the 7 oriented triples in FANO_LINES is a straight line (3 sides + 3 medians)
 *     or the inscribed circle, with 100% consistent clockwise / vertex-to-midpoint orientation!
 */
const FANO_CX = 240;
const FANO_CY = 166;
const FANO_R = 118;
const FANO_IN_R = FANO_R / 2;
const FANO_DX = FANO_R * Math.sqrt(3) / 2;
const FANO_POSITIONS: readonly {x: number; y: number}[] = [
  {x: FANO_CX, y: FANO_CY + FANO_IN_R},                         // 0: A (1) — bottom midpoint (E–U)
  {x: FANO_CX - FANO_DX / 2, y: FANO_CY - FANO_IN_R / 2},       // 1: S (2) — left midpoint (D–E)
  {x: FANO_CX, y: FANO_CY - FANO_R},                            // 2: D (3) — top vertex
  {x: FANO_CX + FANO_DX / 2, y: FANO_CY - FANO_IN_R / 2},       // 3: L (4) — right midpoint (U–D)
  {x: FANO_CX - FANO_DX, y: FANO_CY + FANO_IN_R},               // 4: E (5) — bottom-left vertex
  {x: FANO_CX + FANO_DX, y: FANO_CY + FANO_IN_R},               // 5: U (6) — bottom-right vertex
  {x: FANO_CX, y: FANO_CY},                                     // 6: O (7) — center (Ground)
];

/** Ordered geometric traversal [start, mid, end] matching the exact cyclic orientation of each FANO_LINES[k]. */
const FANO_GEOMETRY: readonly (
  | {kind: 'circle'; nodes: readonly [number, number, number]}
  | {kind: 'line'; ordered: readonly [number, number, number]}
)[] = [
  {kind: 'circle', nodes: [0, 1, 3]},     // [1,2,4]: A → S → L (inscribed circle, clockwise)
  {kind: 'line', ordered: [4, 1, 2]},     // [2,3,5]: E → S → D (left side, clockwise)
  {kind: 'line', ordered: [2, 3, 5]},     // [3,4,6]: D → L → U (right side, clockwise)
  {kind: 'line', ordered: [4, 6, 3]},     // [4,5,7]: E → O → L (median through O)
  {kind: 'line', ordered: [5, 0, 4]},     // [5,6,1]: U → A → E (bottom side, clockwise)
  {kind: 'line', ordered: [5, 6, 1]},     // [6,7,2]: U → O → S (median through O)
  {kind: 'line', ordered: [2, 6, 0]},     // [7,1,3]: D → O → A (median through O)
];

const PAIRS = BASIS.flatMap((_, i) => BASIS.slice(i + 1).map((__, offset) => [i, i + offset + 1] as const));

const COPY = {
  en: {
    title: 'One state. Four perspectives.', tag: 'INTERACTIVE STATE INSTRUMENT',
    views: {relations: 'Relations', matrix: 'Matrix', fano: 'Fano PG(2,2)', readout: 'Readout'},
    viewLabel: 'Representation of the illustrative state',
    play: 'Animate phases', pause: 'Pause phases', reduced: 'Motion reduced',
    graph: 'Seven selected roles and their 21 pairwise coherences. Choose a role to explore its meaning.',
    matrix: 'Complex density matrix. Arrow direction is phase; dashed cell is Hermitian conjugate. Use arrow keys to move.',
    fano: 'Canonical PG(2,2) Fano plane with Ground O at the center. Choose a line or circle to inspect its octonion rule.',
    roles: 'Selected semantic role', pairs: 'Pairwise coherence',
    relationLegend: '21 coherence arcs · inner ring = purity P · pulses = phase',
    matrixLegend: 'Arrow = phase · solid = selected · dashed = conjugate Γ̄ⱼᵢ',
    fanoLegend: 'PG(2,2): 6 lines + 1 inscribed circle · O (Ground) at center',
    strength: 'Coherence strength', purity: 'Purity', integration: 'Integration', reflection: 'Reflection score',
    window: 'Viability window', inside: 'inside', outside: 'outside',
    windowNote: 'Saturates Φ = 7P − 1 on equal populations; this interval alone does not establish consciousness.',
    family: 'Illustrative family', familyNote: 'Equal populations; phases follow a chosen diagonal Hamiltonian.',
    fanoNote: 'Each oriented line or circle encodes e_{a}e_{b} = e_{c} (G₂ symmetry; Stab_{Spin(7)}(e_{O}) = Spin(6) ≅ SU(4)_{C}).',
    semanticNote: 'Role meanings are the framework’s interpretation of a chosen basis.',
    population: 'Population', coherence: 'Coherence', line: 'Oriented triple',
    sHelp: 'Choose a valid state from the family, from fully mixed at zero to pure at one.',
    phaseZero: 'Phase is undefined when the coherence is zero.',
    matrixEntry: 'Matrix entry',
    setting: 'Chosen measurement on A, S', real: 'Real part', imaginary: 'Imaginary part',
    readoutLegend: 'Born probabilities · pₖ = Tr(ΓΠₖ) · Σpₖ = 1',
    state: 'State', measurement: 'Measurement', data: 'Probabilities', rest: 'Other five roles',
    spectrum: 'Spectrum',
    readoutTitle: 'A state becomes observable through a measurement.',
    readoutNote: 'These two settings reveal Re ΓAS and Im ΓAS. Full state tomography requires an informationally complete POVM.',
    readoutLink: 'Reconstruction conditions',
  },
  ru: {
    title: 'Одно состояние. Четыре представления.', tag: 'ИНТЕРАКТИВНЫЙ ИНСТРУМЕНТ',
    views: {relations: 'Связи', matrix: 'Матрица', fano: 'Фано PG(2,2)', readout: 'Данные'},
    viewLabel: 'Представление иллюстративного состояния',
    play: 'Анимировать фазы', pause: 'Остановить фазы', reduced: 'Движение ограничено',
    graph: 'Семь выбранных ролей и 21 попарная когерентность. Выберите роль, чтобы раскрыть её смысл.',
    matrix: 'Комплексная матрица плотности. Стрелка — фаза, пунктир — эрмитово сопряжённый элемент. Перемещайтесь стрелками.',
    fano: 'Каноническая плоскость Фано PG(2,2) с Основанием O в центре. Выберите прямую или окружность для правила октонионов.',
    roles: 'Выбранная смысловая роль', pairs: 'Попарная когерентность',
    relationLegend: '21 дуга когерентности · кольцо ядра = чистота P · импульсы = фаза',
    matrixLegend: 'Стрелка = фаза · сплошная = выбранный · пунктир = сопряжённый Γ̄ⱼᵢ',
    fanoLegend: 'PG(2,2): 6 прямых + вписанная окружность · O (Основание) в центре',
    strength: 'Сила когерентности', purity: 'Чистота', integration: 'Интеграция', reflection: 'Рефлексия',
    window: 'Окно жизнеспособности', inside: 'внутри', outside: 'вне',
    windowNote: 'На равных населённостях насыщает точную границу Φ = 7P − 1; сам интервал не доказывает наличие сознания.',
    family: 'Иллюстративное семейство', familyNote: 'Равные населённости; фазы меняет выбранный диагональный гамильтониан.',
    fanoNote: 'Каждая ориентированная прямая или окружность задаёт e_{a}e_{b} = e_{c} (симметрия G₂; Stab_{Spin(7)}(e_{O}) ≅ SU(4)_{C}).',
    semanticNote: 'Смыслы ролей — интерпретация выбранного базиса во фреймворке.',
    population: 'Населённость', coherence: 'Когерентность', line: 'Ориентированная тройка',
    sHelp: 'Выберите допустимое состояние семейства: от полностью смешанного при нуле до чистого при единице.',
    phaseZero: 'У нулевой когерентности фаза не определена.',
    matrixEntry: 'Элемент матрицы',
    setting: 'Выбранное измерение на A, S', real: 'Вещественная часть', imaginary: 'Мнимая часть',
    readoutLegend: 'Вероятности Борна · pₖ = Tr(ΓΠₖ) · Σpₖ = 1',
    state: 'Состояние', measurement: 'Измерение', data: 'Вероятности', rest: 'Другие пять ролей',
    spectrum: 'Спектр',
    readoutTitle: 'Измерение связывает состояние с наблюдением.',
    readoutNote: 'Эти две настройки раскрывают Re ΓAS и Im ΓAS. Для полной томографии состояния нужен информационно полный POVM.',
    readoutLink: 'Условия реконструкции',
  },
};

function activate(event: KeyboardEvent<SVGGElement>, action: () => void) {
  if (event.key === 'Enter' || event.key === ' ') {
    event.preventDefault();
    action();
  }
}

function chevronPath(x: number, y: number, dx: number, dy: number, size = 4.6) {
  return `M${(x - size * dx + size * 0.72 * dy).toFixed(2)} ${(y - size * dy - size * 0.72 * dx).toFixed(2)} L${(x + size * dx).toFixed(2)} ${(y + size * dy).toFixed(2)} L${(x - size * dx - size * 0.72 * dy).toFixed(2)} ${(y - size * dy + size * 0.72 * dx).toFixed(2)}`;
}

export default function OntologyExplorer() {
  const {i18n} = useDocusaurusContext();
  const locale = i18n.currentLocale === 'ru' ? 'ru' : 'en';
  const copy = COPY[locale];
  const rawId = useId();
  const id = `ontology-${rawId.replace(/:/g, '')}`;
  const rootRef = useRef<HTMLElement>(null);
  const [view, setView] = useState<View>('relations');
  const [strength, setStrength] = useState(0.5);
  const [selected, setSelected] = useState(0);
  const [matrixCell, setMatrixCell] = useState<[number, number]>([0, 1]);
  const [line, setLine] = useState(0);
  const [readoutSetting, setReadoutSetting] = useState<ReadoutSetting>('real');
  const [time, setTime] = useState(0);
  const [playing, setPlaying] = useState(true);
  const [reduced, setReduced] = useState(false);
  const [visible, setVisible] = useState(false);
  const [pageVisible, setPageVisible] = useState(true);
  const state = illustrativeState(strength, time);
  const readout = pairReadout(state.matrix, readoutSetting);
  const motionActive = playing && !reduced && visible && pageVisible && view !== 'fano';

  useEffect(() => {
    const preference = window.matchMedia('(prefers-reduced-motion: reduce)');
    const update = () => setReduced(preference.matches);
    const visibility = () => setPageVisible(document.visibilityState === 'visible');
    update();
    visibility();
    preference.addEventListener('change', update);
    document.addEventListener('visibilitychange', visibility);
    const observer = new IntersectionObserver(([entry]) => setVisible(entry.isIntersecting), {threshold: 0.05});
    if (rootRef.current) observer.observe(rootRef.current);
    return () => {
      preference.removeEventListener('change', update);
      document.removeEventListener('visibilitychange', visibility);
      observer.disconnect();
    };
  }, []);

  useEffect(() => {
    if (!motionActive) return undefined;
    let frame = 0;
    let previous = 0;
    let accumulated = 0;
    const tick = (now: number) => {
      if (previous) accumulated += Math.min((now - previous) / 1000, 0.1);
      previous = now;
      if (accumulated >= 0.05) {
        const elapsed = accumulated;
        accumulated = 0;
        setTime((current) => current + elapsed * 0.32);
      }
      frame = window.requestAnimationFrame(tick);
    };
    frame = window.requestAnimationFrame(tick);
    return () => window.cancelAnimationFrame(frame);
  }, [motionActive]);

  const role = cellOf(BASIS[selected], BASIS[selected]);
  const [row, column] = matrixCell;
  const cell = cellOf(BASIS[row], BASIS[column]);
  const entry = state.matrix[row][column];
  const [a, b, c] = FANO_LINES[line].map((n) => n - 1);
  // Harmonious amethyst ↔ teal phase hue shift
  const phaseColor = (phase: number) => {
    const t = 0.5 + 0.5 * Math.sin(phase);
    const hue = 284 - 108 * t; // 284° amethyst -> 176° scientific teal
    return `hsl(${hue.toFixed(1)} 52% 56%)`;
  };
  const matrixSelect = (event: KeyboardEvent<SVGGElement>, i: number, j: number) => {
    const moves: Record<string, [number, number]> = {ArrowLeft: [0, -1], ArrowRight: [0, 1], ArrowUp: [-1, 0], ArrowDown: [1, 0]};
    const move = moves[event.key];
    if (move) {
      event.preventDefault();
      const next: [number, number] = [(i + move[0] + 7) % 7, (j + move[1] + 7) % 7];
      setMatrixCell(next);
      rootRef.current?.querySelector<SVGGElement>(`[data-cell="${next[0]}-${next[1]}"]`)?.focus();
    } else activate(event, () => setMatrixCell([i, j]));
  };
  const number = (value: number) => value.toLocaleString(locale, {minimumFractionDigits: 3, maximumFractionDigits: 3});
  const switchView = (next: View) => setView(next);

  const purityRadius = 42;
  const purityCirc = 2 * Math.PI * purityRadius;
  const purityArc = purityCirc * state.purity;
  const dominantEig = state.eigenvalues[0];
  const tailEig = state.eigenvalues[1];

  return (
    <figure className={styles.explorer} ref={rootRef} data-testid="ontology-explorer" aria-labelledby={`${id}-title`}>
      <div className={styles.heading}>
        <div><span className={styles.eyebrow}>{copy.tag}</span><h2 id={`${id}-title`}>{copy.title}</h2></div>
        <div className={styles.headingTools}><span className={styles.dimension} aria-label="7 × 7">7 × 7</span><button className={styles.motion} type="button" onClick={() => setPlaying((value) => !value)} aria-label={reduced ? copy.reduced : playing ? copy.pause : copy.play} aria-pressed={playing && !reduced} disabled={reduced} title={reduced ? copy.reduced : playing ? copy.pause : copy.play} data-testid="ontology-motion">
          {playing && !reduced ? <svg viewBox="0 0 16 16" aria-hidden="true"><path d="M5 3v10M11 3v10" /></svg> : <svg viewBox="0 0 16 16" aria-hidden="true"><path d="m5 3 8 5-8 5z" /></svg>}
        </button></div>
      </div>
      <div className={styles.toolbar}>
        <div className={styles.views} role="group" aria-label={copy.viewLabel}>
          {(['relations', 'matrix', 'fano', 'readout'] as View[]).map((next) => (
            <button key={next} type="button" aria-pressed={view === next} className={view === next ? styles.activeView : undefined} onClick={() => switchView(next)} data-testid={`ontology-view-${next}`}>{copy.views[next]}</button>
          ))}
        </div>
      </div>

      <div className={styles.stage} data-testid="ontology-stage" data-view={view} data-animating={motionActive}>
        {view === 'readout' ? (
          <div className={styles.readoutStage}>
            <div className={styles.observationFlow} aria-label={`${copy.state} → ${copy.measurement} → ${copy.data}`}>
              <div><span className={styles.stateSymbol}>Γ</span><small>{copy.state}</small></div>
              <span className={styles.flowArrow} aria-hidden="true">→</span>
              <div><span className={styles.measurementSymbol}>Π₊, Π₋, Πᵣ</span><small>{copy.measurement}</small></div>
              <span className={styles.flowArrow} aria-hidden="true">→</span>
              <div><span className={styles.dataSymbol}>pₖ</span><small>{copy.data}</small></div>
            </div>
            <div className={styles.readoutSettings} role="group" aria-label={copy.setting}>
              {(['real', 'imaginary'] as ReadoutSetting[]).map((setting) => <button type="button" key={setting} aria-label={`${copy.setting}: ${setting === 'real' ? copy.real : copy.imaginary}`} aria-pressed={readoutSetting === setting} onClick={() => setReadoutSetting(setting)} className={readoutSetting === setting ? styles.selectedSetting : undefined} data-testid={`ontology-readout-${setting}`}>{setting === 'real' ? 'Re ΓAS' : 'Im ΓAS'}</button>)}
            </div>
            <div className={styles.probabilities}>
              {(['plus', 'minus', 'rest'] as const).map((outcome) => <div key={outcome} className={styles.probabilityRow}>
                <span className={styles.outcomeLabel}>{outcome === 'plus' ? 'p₊' : outcome === 'minus' ? 'p₋' : 'pᵣ'}</span>
                <div className={styles.probabilityTrack} aria-hidden="true"><span style={{width: `${readout[outcome] * 100}%`}} className={outcome === 'rest' ? styles.restBar : undefined} /></div>
                <output aria-live="off" data-testid={`ontology-readout-${outcome}`} aria-label={outcome === 'rest' ? copy.rest : outcome === 'plus' ? 'p₊' : 'p₋'}>{number(readout[outcome])}</output>
              </div>)}
            </div>
            <div className={styles.spectrumStrip} aria-hidden="true">
              <span className={styles.spectrumLabel}>{copy.spectrum}</span>
              <div className={styles.spectrumBar}>
                <span className={styles.spectrumDominant} style={{width: `${dominantEig * 100}%`}} />
                <span className={styles.spectrumTail} style={{width: `${(1 - dominantEig) * 100}%`}} />
              </div>
              <span className={styles.spectrumReadout}>λ₁={dominantEig.toFixed(2)} · 6×{tailEig.toFixed(2)}</span>
            </div>
            <div className={styles.readoutEquation}>p₊ = 1/7 + {readoutSetting === 'real' ? 'Re' : 'Im'} Γ<sub>AS</sub> <span>·</span> pᵣ = 5/7</div>
          </div>
        ) : view === 'relations' ? (
          <svg viewBox="70 0 340 310" className={styles.diagram} role="group" aria-label={copy.graph}>
            <defs>
              <radialGradient id={`${id}-glow`}>
                <stop offset="0" stopColor={state.inSelectedWindow ? 'var(--home-teal, #386d68)' : 'var(--ifm-color-primary)'} stopOpacity={0.07 + 0.13 * strength} />
                <stop offset="1" stopColor="var(--ifm-color-primary)" stopOpacity="0" />
              </radialGradient>
            </defs>
            <circle cx={CX} cy={CY} r="150" fill={`url(#${id}-glow)`} />
            <circle cx={CX} cy={CY} r="136" className={styles.orbit} />
            <circle cx={CX} cy={CY} r="112" className={styles.innerOrbit} />
            {PAIRS.map(([i, j]) => {
              const p = POSITIONS[i];
              const q = POSITIONS[j];
              const phase = state.phases[i] - state.phases[j];
              const active = i === selected || j === selected;
              const chordDist = Math.hypot(q.x - p.x, q.y - p.y);
              // Gentle inward bow for longer chords keeps all 21 relations visually legible
              const bow = chordDist > 130 ? 0.16 : 0.08;
              const midX = (p.x + q.x) / 2;
              const midY = (p.y + q.y) / 2;
              const ctrlX = midX + (CX - midX) * bow;
              const ctrlY = midY + (CY - midY) * bow;
              const t = 0.5 + 0.24 * Math.sin(phase);
              const invT = 1 - t;
              const pulseX = invT * invT * p.x + 2 * invT * t * ctrlX + t * t * q.x;
              const pulseY = invT * invT * p.y + 2 * invT * t * ctrlY + t * t * q.y;
              const strokeColor = phaseColor(phase);
              return <g key={`${i}-${j}`} opacity={strength * (active ? 0.9 : 0.24)}>
                <path d={`M${p.x.toFixed(1)} ${p.y.toFixed(1)} Q${ctrlX.toFixed(1)} ${ctrlY.toFixed(1)} ${q.x.toFixed(1)} ${q.y.toFixed(1)}`} fill="none" stroke={strokeColor} strokeWidth={active ? 1.85 : 0.85} strokeLinecap="round" />
                {active && strength > 0.02 && <circle cx={pulseX} cy={pulseY} r="2.7" fill={strokeColor} />}
              </g>;
            })}
            {/* Live Purity ring surrounding the central Γ core */}
            <circle cx={CX} cy={CY} r={purityRadius} className={styles.purityTrack} />
            <circle
              cx={CX}
              cy={CY}
              r={purityRadius}
              className={state.inSelectedWindow ? styles.purityArcWindow : styles.purityArc}
              strokeDasharray={`${purityArc.toFixed(2)} ${purityCirc.toFixed(2)}`}
              transform={`rotate(-90 ${CX} ${CY})`}
            />
            <circle cx={CX} cy={CY} r="36" className={styles.core} />
            <text x={CX} y={CY + 3} textAnchor="middle" className={styles.gamma}>Γ</text>
            <text x={CX} y={CY + 20} textAnchor="middle" className={styles.coreLabel}>P = {state.purity.toFixed(2)}</text>
            {POSITIONS.map((point, index) => {
              const on = selected === index;
              const name = tr(cellOf(BASIS[index], BASIS[index]).name, locale);
              return <g key={BASIS[index]} className={`${styles.node} ${styles.interactiveNode} ${on ? styles.nodeSelected : ''}`} role="button" tabIndex={0} aria-label={`${BASIS[index]} — ${name}`} aria-pressed={on} onClick={() => setSelected(index)} onKeyDown={(event) => activate(event, () => setSelected(index))} data-testid={`ontology-node-${BASIS[index]}`}>
                <circle cx={point.x} cy={point.y} r="19.5" />
                <text x={point.x} y={point.y + 1} dominantBaseline="central" textAnchor="middle">{BASIS[index]}</text>
                <text x={CX + (point.x - CX) * 1.27} y={CY + (point.y - CY) * 1.27 + 3} textAnchor="middle" className={styles.nodeIndex}>{index + 1}</text>
              </g>;
            })}
            <text x="82" y="297" className={styles.diagramLabel}>Γ ∈ D₇</text>
            <text x="398" y="297" textAnchor="end" className={styles.diagramLabel}>Γ = Γ† ⪰ 0 · Tr Γ = 1</text>
          </svg>
        ) : view === 'fano' ? (
          <svg viewBox="70 0 340 310" className={styles.diagram} role="group" aria-label={copy.fano}>
            <defs>
              <radialGradient id={`${id}-fano-glow`}>
                <stop offset="0" stopColor="var(--home-teal, #386d68)" stopOpacity=".10" />
                <stop offset="1" stopColor="var(--ifm-color-primary)" stopOpacity="0" />
              </radialGradient>
            </defs>
            <circle cx={FANO_CX} cy={FANO_CY} r="138" fill={`url(#${id}-fano-glow)`} />
            {/* Render all 6 straight projective lines + 1 inscribed circle */}
            {FANO_GEOMETRY.map((geom, index) => {
              const active = index === line;
              if (geom.kind === 'circle') {
                // Clockwise tangent chevrons at 150°, 270°, 30° around inscribed circle A → S → L → A
                const arrowAngles = [150, 270, 30].map((deg) => deg * Math.PI / 180);
                return <g key={index} className={styles.fanoClickable} onClick={() => setLine(index)}>
                  <circle cx={FANO_CX} cy={FANO_CY} r={FANO_IN_R} className={active ? styles.activeFanoLine : styles.fanoLine} />
                  {active && arrowAngles.map((theta, k) => {
                    const ax = FANO_CX + FANO_IN_R * Math.cos(theta);
                    const ay = FANO_CY + FANO_IN_R * Math.sin(theta);
                    // Clockwise tangent in screen coordinates (x right, y down): (-sin θ, cos θ)
                    const dx = -Math.sin(theta);
                    const dy = Math.cos(theta);
                    return <path key={k} d={chevronPath(ax, ay, dx, dy, 4.8)} className={styles.tripleArrow} />;
                  })}
                </g>;
              }
              const [i0, i1, i2] = geom.ordered;
              const p0 = FANO_POSITIONS[i0];
              const p1 = FANO_POSITIONS[i1];
              const p2 = FANO_POSITIONS[i2];
              const segLen = Math.hypot(p2.x - p0.x, p2.y - p0.y);
              const dx = (p2.x - p0.x) / segLen;
              const dy = (p2.y - p0.y) / segLen;
              const m1x = (p0.x + p1.x) / 2;
              const m1y = (p0.y + p1.y) / 2;
              const m2x = (p1.x + p2.x) / 2;
              const m2y = (p1.y + p2.y) / 2;
              return <g key={index} className={styles.fanoClickable} onClick={() => setLine(index)}>
                <line x1={p0.x} y1={p0.y} x2={p2.x} y2={p2.y} className={active ? styles.activeFanoLine : styles.fanoLine} />
                {active && <>
                  <path d={chevronPath(m1x, m1y, dx, dy, 4.8)} className={styles.tripleArrow} />
                  <path d={chevronPath(m2x, m2y, dx, dy, 4.8)} className={styles.tripleArrow} />
                </>}
              </g>;
            })}
            {/* Seven PG(2,2) points with O (Ground) at the exact center */}
            {FANO_POSITIONS.map((point, index) => {
              const on = FANO_LINES[line].includes(index + 1);
              const isCenter = index === 6;
              const name = tr(cellOf(BASIS[index], BASIS[index]).name, locale);
              return <g
                key={BASIS[index]}
                className={`${styles.node} ${styles.interactiveNode} ${on ? styles.nodeSelected : ''} ${isCenter ? styles.fanoCenter : ''}`}
                role="button"
                tabIndex={0}
                aria-label={`${BASIS[index]} — ${name}`}
                onClick={() => {
                  const nextLine = FANO_LINES.findIndex((t, idx) => idx > line && t.includes(index + 1));
                  const fallback = FANO_LINES.findIndex((t) => t.includes(index + 1));
                  setLine(nextLine >= 0 ? nextLine : fallback);
                }}
                onKeyDown={(event) => activate(event, () => {
                  const nextLine = FANO_LINES.findIndex((t, idx) => idx > line && t.includes(index + 1));
                  const fallback = FANO_LINES.findIndex((t) => t.includes(index + 1));
                  setLine(nextLine >= 0 ? nextLine : fallback);
                })}
                data-testid={`ontology-fano-node-${BASIS[index]}`}
              >
                <circle cx={point.x} cy={point.y} r={isCenter ? 19.5 : 18} />
                <text x={point.x} y={point.y + 1} dominantBaseline="central" textAnchor="middle">{BASIS[index]}</text>
              </g>;
            })}
            <text x="82" y="297" className={styles.diagramLabel}>PG(2,2) = F₂³ ∖ {'{0}'}</text>
            <text x="398" y="297" textAnchor="end" className={styles.diagramLabel}>|PSL(2,7)| = 168</text>
          </svg>
        ) : (
          <svg viewBox="85 0 310 310" className={styles.diagram} role="group" aria-label={copy.matrix}>
            {BASIS.map((label, index) => <g key={label} className={styles.matrixAxis}><text x={132 + index * 36} y="23" textAnchor="middle">{label}</text><text x="101" y={51 + index * 36} textAnchor="middle" dominantBaseline="central">{label}</text></g>)}
            {state.matrix.map((values, i) => values.map((value, j) => {
              const diagonal = i === j;
              const magnitude = diagonal ? 1 : strength;
              const on = i === row && j === column;
              const conj = !diagonal && i === column && j === row;
              const x = 116 + j * 36;
              const y = 35 + i * 36;
              const phase = Math.atan2(value.im, value.re);
              const tipX = x + 16 + 9.5 * Math.cos(phase);
              const tipY = y + 16 - 9.5 * Math.sin(phase);
              return <g key={`${i}-${j}`} className={styles.matrixCell} role="button" tabIndex={on ? 0 : -1} data-cell={`${i}-${j}`} aria-pressed={on} aria-label={`${copy.matrixEntry} ${BASIS[i]} ${BASIS[j]}: ${tr(cellOf(BASIS[i], BASIS[j]).name, locale)}`} onFocus={() => setMatrixCell([i, j])} onClick={() => setMatrixCell([i, j])} onKeyDown={(event) => matrixSelect(event, i, j)}>
                <rect x={x} y={y} width="32" height="32" rx="6" className={styles.cellBase} />
                <rect x={x} y={y} width="32" height="32" rx="6" fill={diagonal ? 'var(--ifm-color-primary)' : phaseColor(phase)} opacity={magnitude * (diagonal ? 0.24 : 0.34)} />
                {conj && <rect x={x - 1} y={y - 1} width="34" height="34" rx="6.5" className={styles.cellConjugateSelection} />}
                {on && <rect x={x - 1.5} y={y - 1.5} width="35" height="35" rx="7" className={styles.cellSelection} />}
                {diagonal ? (
                  <text x={x + 16} y={y + 17} textAnchor="middle" dominantBaseline="central" className={styles.cellNumber}>¹⁄₇</text>
                ) : magnitude > 0 && (
                  <g opacity={0.36 + 0.64 * magnitude} className={styles.phaseArrow}>
                    <circle cx={x + 16} cy={y + 16} r="10.5" className={styles.phaseDial} />
                    <line x1={x + 16 - 4.5 * Math.cos(phase)} y1={y + 16 + 4.5 * Math.sin(phase)} x2={tipX} y2={tipY} />
                    <path d={`M ${tipX - 3.8 * Math.cos(phase - 0.6)} ${tipY + 3.8 * Math.sin(phase - 0.6)} L ${tipX} ${tipY} L ${tipX - 3.8 * Math.cos(phase + 0.6)} ${tipY + 3.8 * Math.sin(phase + 0.6)}`} />
                  </g>
                )}
              </g>;
            }))}
            <path d="M109 33h-5v256h5 M375 33h5v256h-5" className={styles.matrixBracket} />
            <text x="96" y="297" className={styles.diagramLabel}>Γᵢⱼ = Γ̄ⱼᵢ</text>
            <text x="384" y="297" textAnchor="end" className={styles.diagramLabel}>Tr Γ = 1</text>
          </svg>
        )}
        <div className={styles.legend}>{view === 'relations' ? copy.relationLegend : view === 'matrix' ? copy.matrixLegend : view === 'readout' ? copy.readoutLegend : copy.fanoLegend}</div>
      </div>

      <div className={styles.explanation}>
        {view === 'relations' && <><span className={styles.selectionMark}>{BASIS[selected]}</span><div><strong>{tr(role.name, locale)}</strong><p>{tr(role.meaning, locale)}. <span>{copy.semanticNote}</span></p></div></>}
        {view === 'matrix' && <><span className={styles.selectionMark}>{BASIS[row]}{BASIS[column]}</span><div><strong>{tr(cell.name, locale)}</strong><p>{tr(cell.meaning, locale)}.</p><code data-testid="ontology-entry">Γ{subscript(BASIS[row] + BASIS[column])} = {number(entry.re)} {entry.im < 0 ? '−' : '+'} {number(Math.abs(entry.im))}i</code>{strength === 0 && row !== column && <p>{copy.phaseZero}</p>}</div></>}
        {view === 'fano' && <div className={styles.fanoDescription}><div className={styles.lineSelector} role="group" aria-label={copy.line}>{FANO_LINES.map((triple, index) => <button type="button" key={index} aria-label={`${copy.line} ${triple.map((n) => BASIS[n - 1]).join(', ')}`} aria-pressed={line === index} onClick={() => setLine(index)} className={line === index ? styles.activeLine : undefined}>{index + 1}</button>)}</div><strong className={styles.product}>e<sub>{BASIS[a]}</sub> e<sub>{BASIS[b]}</sub> = e<sub>{BASIS[c]}</sub></strong><p><RichText text={copy.fanoNote} /></p></div>}
        {view === 'readout' && <div><strong>{copy.readoutTitle}</strong><p>{copy.readoutNote} <Link to="/docs/applied/research/reconstruction-identifiability">{copy.readoutLink} →</Link></p></div>}
      </div>

      <div className={styles.controls}>
        <label htmlFor={`${id}-strength`}>{copy.strength} <span>s = <output data-testid="ontology-strength">{strength.toFixed(2)}</output></span></label>
        <input id={`${id}-strength`} type="range" min="0" max="1" step="0.01" value={strength} onChange={(event) => setStrength(Number(event.target.value))} aria-describedby={`${id}-family`} aria-valuetext={`${strength.toFixed(2)}. ${copy.sHelp}`} data-testid="ontology-slider" />
      </div>

      <dl className={styles.metrics}>
        <div><dt title="P = (1 + 6s²)/7"><span>P</span> {copy.purity}</dt><dd data-testid="ontology-purity">{number(state.purity)}</dd></div>
        <div><dt title="Φ = 6s² = 7P − 1"><span>Φ</span> {copy.integration}</dt><dd data-testid="ontology-integration">{number(state.integration)}</dd></div>
        <div><dt title="R = 1/(1 + 6s²)"><span>R</span> {copy.reflection}</dt><dd data-testid="ontology-reflection">{number(state.reflection)}</dd></div>
      </dl>
      <div className={styles.gauge}>
        <div className={styles.gaugeHeading}><span>{copy.window} <b>2/7 &lt; P ≤ 3/7</b></span><span className={state.inSelectedWindow ? styles.inWindow : styles.outWindow} data-testid="ontology-window">{state.inSelectedWindow ? copy.inside : copy.outside}</span></div>
        <div className={styles.gaugeTrack} aria-hidden="true"><span className={styles.gaugeWindow} /><span className={styles.gaugeMarker} style={{left: `${strength * strength * 100}%`}} /></div>
        <div className={styles.gaugeScale}><span>1/7</span><span style={{left: '16.6667%'}}>2/7</span><span style={{left: '33.3333%'}}>3/7</span><span>1</span></div>
        <p>{copy.windowNote}</p>
      </div>
      <figcaption className={styles.family} id={`${id}-family`}><span>{copy.family}</span><code>Γ = (1 − s)I₇/7 + s|ψ⟩⟨ψ|</code><p>{copy.familyNote}</p></figcaption>
    </figure>
  );
}

function subscript(value: string) { return <sub>{value}</sub>; }
