import {useEffect, useId, useRef, useState} from 'react';
import type {KeyboardEvent} from 'react';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Link from '@docusaurus/Link';
import {cellOf, tr} from '@site/src/data/coherences';
import {BASIS, FANO_LINES, illustrativeState, pairReadout} from './model';
import type {ReadoutSetting} from './model';
import styles from './styles.module.css';

type View = 'relations' | 'matrix' | 'fano' | 'readout';
const POSITIONS = BASIS.map((_, j) => {
  const angle = -Math.PI / 2 + j * 2 * Math.PI / 7;
  return {x: 240 + 114 * Math.cos(angle), y: 153 + 114 * Math.sin(angle)};
});
const PAIRS = BASIS.flatMap((_, i) => BASIS.slice(i + 1).map((__, offset) => [i, i + offset + 1] as const));
const COPY = {
  en: {
    title: 'One state. Four perspectives.', tag: 'EXPLORE THE MODEL',
    views: {relations: 'Relations', matrix: 'Matrix', fano: 'Fano', readout: 'Readout'},
    viewLabel: 'Representation of the illustrative state',
    play: 'Animate phases', pause: 'Pause phases', reduced: 'Motion reduced',
    graph: 'Seven selected roles and their 21 pairwise coherences. Choose a role to explore its meaning.',
    matrix: 'Complex density matrix. Arrow direction is phase; opacity is magnitude. Use arrow keys to move between cells.',
    fano: 'Seven oriented Fano triples. Choose a triple to inspect its multiplication rule.',
    roles: 'Selected semantic role', pairs: 'Pairwise coherence',
    relationLegend: '21 pairs · brightness = magnitude · motion = phase', matrixLegend: 'Direction = phase · brightness = magnitude',
    fanoLegend: '7 triples · a chosen octonion presentation',
    strength: 'Coherence strength', purity: 'Purity', integration: 'Integration', reflection: 'Reflection score',
    window: 'Selected interval', inside: 'inside', outside: 'outside',
    windowNote: 'This interval alone does not establish consciousness.',
    family: 'Illustrative family', familyNote: 'Equal populations; phases follow a chosen diagonal Hamiltonian.',
    fanoNote: 'The triples encode a chosen multiplication table. They are distinct from the 21 pairwise coherences.',
    semanticNote: 'Role meanings are the framework’s interpretation of a chosen basis.',
    population: 'Population', coherence: 'Coherence', line: 'Oriented triple',
    sHelp: 'Choose a valid state from the family, from fully mixed at zero to pure at one.',
    phaseZero: 'Phase is undefined when the coherence is zero.',
    matrixEntry: 'Matrix entry',
    setting: 'Chosen measurement on A, S', real: 'Real part', imaginary: 'Imaginary part',
    readoutLegend: 'Born probabilities · pₖ = Tr(ΓΠₖ) · Σpₖ = 1',
    state: 'State', measurement: 'Measurement', data: 'Probabilities', rest: 'Other five roles',
    readoutTitle: 'A state becomes observable through a measurement.',
    readoutNote: 'These two settings reveal Re ΓAS and Im ΓAS. They do not reconstruct the full state.',
    readoutLink: 'What makes reconstruction possible',
  },
  ru: {
    title: 'Одно состояние. Четыре представления.', tag: 'ИССЛЕДУЙТЕ МОДЕЛЬ',
    views: {relations: 'Связи', matrix: 'Матрица', fano: 'Фано', readout: 'Данные'},
    viewLabel: 'Представление иллюстративного состояния',
    play: 'Анимировать фазы', pause: 'Остановить фазы', reduced: 'Движение ограничено',
    graph: 'Семь выбранных ролей и 21 попарная когерентность. Выберите роль, чтобы раскрыть её смысл.',
    matrix: 'Комплексная матрица плотности. Направление стрелки — фаза, яркость — модуль. Перемещайтесь между ячейками клавишами со стрелками.',
    fano: 'Семь ориентированных троек Фано. Выберите тройку, чтобы увидеть правило умножения.',
    roles: 'Выбранная смысловая роль', pairs: 'Попарная когерентность',
    relationLegend: '21 пара · яркость = модуль · движение = фаза', matrixLegend: 'Направление = фаза · яркость = модуль',
    fanoLegend: '7 троек · выбранная таблица октонионов',
    strength: 'Сила когерентности', purity: 'Чистота', integration: 'Интеграция', reflection: 'Показатель рефлексии',
    window: 'Выбранный интервал', inside: 'внутри', outside: 'вне',
    windowNote: 'Один этот интервал не устанавливает наличие сознания.',
    family: 'Иллюстративное семейство', familyNote: 'Равные населённости; фазы меняет выбранный диагональный гамильтониан.',
    fanoNote: 'Тройки задают выбранную таблицу умножения. Они отличаются от 21 попарной когерентности.',
    semanticNote: 'Смыслы ролей — интерпретация выбранного базиса во фреймворке.',
    population: 'Населённость', coherence: 'Когерентность', line: 'Ориентированная тройка',
    sHelp: 'Выберите допустимое состояние семейства: от полностью смешанного при нуле до чистого при единице.',
    phaseZero: 'У нулевой когерентности фаза не определена.',
    matrixEntry: 'Элемент матрицы',
    setting: 'Выбранное измерение на A, S', real: 'Вещественная часть', imaginary: 'Мнимая часть',
    readoutLegend: 'Вероятности Борна · pₖ = Tr(ΓΠₖ) · Σpₖ = 1',
    state: 'Состояние', measurement: 'Измерение', data: 'Вероятности', rest: 'Другие пять ролей',
    readoutTitle: 'Измерение связывает состояние с наблюдением.',
    readoutNote: 'Эти две настройки раскрывают Re ΓAS и Im ΓAS. Для восстановления всего состояния их недостаточно.',
    readoutLink: 'Условия реконструкции',
  },
};

function activate(event: KeyboardEvent<SVGGElement>, action: () => void) {
  if (event.key === 'Enter' || event.key === ' ') {
    event.preventDefault();
    action();
  }
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
      // 20 updates/s keeps an exact slowly varying orbit inexpensive on mobile.
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
  const phaseColor = (phase: number) => `hsl(${273 + 22 * Math.sin(phase)} 58% 61%)`;
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
              <div><span className={styles.stateSymbol}>Γ</span><small>{copy.state}</small></div><span className={styles.flowArrow} aria-hidden="true">→</span><div><span className={styles.measurementSymbol}>Π₊, Π₋, Πᵣ</span><small>{copy.measurement}</small></div><span className={styles.flowArrow} aria-hidden="true">→</span><div><span className={styles.dataSymbol}>pₖ</span><small>{copy.data}</small></div>
            </div>
            <div className={styles.readoutSettings} role="group" aria-label={copy.setting}>
              {(['real', 'imaginary'] as ReadoutSetting[]).map((setting) => <button type="button" key={setting} aria-label={`${copy.setting}: ${setting === 'real' ? copy.real : copy.imaginary}`} aria-pressed={readoutSetting === setting} onClick={() => setReadoutSetting(setting)} className={readoutSetting === setting ? styles.selectedSetting : undefined} data-testid={`ontology-readout-${setting}`}>{setting === 'real' ? 'Re ΓAS' : 'Im ΓAS'}</button>)}
            </div>
            <div className={styles.probabilities}>
              {(['plus', 'minus', 'rest'] as const).map((outcome) => <div key={outcome} className={styles.probabilityRow}>
                <span className={styles.outcomeLabel}>{outcome === 'plus' ? 'p₊' : outcome === 'minus' ? 'p₋' : 'pᵣ'}</span><div className={styles.probabilityTrack} aria-hidden="true"><span style={{width: `${readout[outcome] * 100}%`}} className={outcome === 'rest' ? styles.restBar : undefined} /></div><output aria-live="off" data-testid={`ontology-readout-${outcome}`} aria-label={outcome === 'rest' ? copy.rest : outcome === 'plus' ? 'p₊' : 'p₋'}>{number(readout[outcome])}</output>
              </div>)}
            </div>
            <div className={styles.readoutEquation}>p₊ = 1/7 + {readoutSetting === 'real' ? 'Re' : 'Im'} Γ<sub>AS</sub> <span>·</span> pᵣ = 5/7</div>
          </div>
        ) : view !== 'matrix' ? (
          <svg viewBox="70 0 340 310" className={styles.diagram} role="group" aria-label={view === 'relations' ? copy.graph : copy.fano}>
            <defs>
              <radialGradient id={`${id}-glow`}><stop offset="0" stopColor="var(--ifm-color-primary)" stopOpacity=".10" /><stop offset="1" stopColor="var(--ifm-color-primary)" stopOpacity="0" /></radialGradient>
            </defs>
            <circle cx="240" cy="153" r="153" fill={`url(#${id}-glow)`} />
            <circle cx="240" cy="153" r="139" className={styles.orbit} />
            <circle cx="240" cy="153" r="114" className={styles.innerOrbit} />
            {view === 'relations' && PAIRS.map(([i, j]) => {
              const p = POSITIONS[i]; const q = POSITIONS[j];
              const phase = state.phases[i] - state.phases[j];
              const active = i === selected || j === selected;
              const midX = (p.x + q.x) / 2; const midY = (p.y + q.y) / 2;
              return <g key={`${i}-${j}`} opacity={strength * (active ? 0.84 : 0.28)}>
                <line x1={p.x} y1={p.y} x2={q.x} y2={q.y} stroke={phaseColor(phase)} strokeWidth={active ? 1.65 : 0.85} />
                {active && <circle cx={midX + (q.x - p.x) * 0.2 * Math.sin(phase)} cy={midY + (q.y - p.y) * 0.2 * Math.sin(phase)} r="2" fill="var(--ifm-color-primary)" />}
              </g>;
            })}
            {view === 'fano' && FANO_LINES.map((triple, index) => {
              const points = triple.map((n) => POSITIONS[n - 1]);
              return <g key={index}><polygon points={points.map((p) => `${p.x},${p.y}`).join(' ')} className={index === line ? styles.activeTriple : styles.triple} />{index === line && points.map((p, t) => {
                const q = points[(t + 1) % 3];
                const distance = Math.hypot(q.x - p.x, q.y - p.y);
                const dx = (q.x - p.x) / distance; const dy = (q.y - p.y) / distance;
                const x = p.x * .58 + q.x * .42; const y = p.y * .58 + q.y * .42;
                return <path key={t} d={`M${x - 4 * dx + 3 * dy} ${y - 4 * dy - 3 * dx} L${x + 4 * dx} ${y + 4 * dy} L${x - 4 * dx - 3 * dy} ${y - 4 * dy + 3 * dx}`} className={styles.tripleArrow} />;
              })}</g>;
            })}
            <circle cx="240" cy="153" r="38" className={styles.core} />
            <text x="240" y="158" textAnchor="middle" className={styles.gamma}>Γ</text>
            <text x="240" y="176" textAnchor="middle" className={styles.coreLabel}>Tr Γ = 1</text>
            {POSITIONS.map((point, index) => {
              const on = view === 'fano' ? FANO_LINES[line].includes(index + 1) : selected === index;
              const name = tr(cellOf(BASIS[index], BASIS[index]).name, locale);
              return <g key={BASIS[index]} className={`${styles.node} ${view === 'relations' ? styles.interactiveNode : ''} ${on ? styles.nodeSelected : ''}`} role={view === 'relations' ? 'button' : undefined} tabIndex={view === 'relations' ? 0 : undefined} aria-label={`${BASIS[index]} — ${name}`} aria-pressed={view === 'relations' ? selected === index : undefined} onClick={view === 'relations' ? () => setSelected(index) : undefined} onKeyDown={view === 'relations' ? (event) => activate(event, () => setSelected(index)) : undefined} data-testid={`ontology-node-${BASIS[index]}`}>
                <circle cx={point.x} cy={point.y} r="20" />
                <text x={point.x} y={point.y + 1} dominantBaseline="central" textAnchor="middle">{BASIS[index]}</text>
                <text x={240 + (point.x - 240) * 1.25} y={153 + (point.y - 153) * 1.25 + 4} textAnchor="middle" className={styles.nodeIndex}>{index + 1}</text>
              </g>;
            })}
            <text x="82" y="296" className={styles.diagramLabel}>{view === 'fano' ? 'F₂³ ∖ {0}' : 'Γ ∈ D₇'}</text>
            <text x="398" y="296" textAnchor="end" className={styles.diagramLabel}>{view === 'fano' ? '7 × 3' : 'Γ = Γ† ≥ 0'}</text>
          </svg>
        ) : (
          <svg viewBox="85 0 310 310" className={styles.diagram} role="group" aria-label={copy.matrix}>
            {BASIS.map((label, index) => <g key={label} className={styles.matrixAxis}><text x={132 + index * 36} y="23" textAnchor="middle">{label}</text><text x="101" y={51 + index * 36} textAnchor="middle" dominantBaseline="central">{label}</text></g>)}
            {state.matrix.map((values, i) => values.map((value, j) => {
              const diagonal = i === j; const magnitude = diagonal ? 1 : strength;
              const on = i === row && j === column;
              const x = 116 + j * 36; const y = 35 + i * 36;
              const phase = Math.atan2(value.im, value.re);
              const tipX = x + 16 + 10 * Math.cos(phase); const tipY = y + 16 - 10 * Math.sin(phase);
              return <g key={`${i}-${j}`} className={styles.matrixCell} role="button" tabIndex={on ? 0 : -1} data-cell={`${i}-${j}`} aria-pressed={on} aria-label={`${copy.matrixEntry} ${BASIS[i]} ${BASIS[j]}: ${tr(cellOf(BASIS[i], BASIS[j]).name, locale)}`} onFocus={() => setMatrixCell([i, j])} onClick={() => setMatrixCell([i, j])} onKeyDown={(event) => matrixSelect(event, i, j)}>
                <rect x={x} y={y} width="32" height="32" rx="6" className={styles.cellBase} />
                <rect x={x} y={y} width="32" height="32" rx="6" fill={diagonal ? 'var(--ifm-color-primary)' : phaseColor(phase)} opacity={magnitude * (diagonal ? 0.25 : 0.36)} />
                {on && <rect x={x - 1.5} y={y - 1.5} width="35" height="35" rx="7" className={styles.cellSelection} />}
                {diagonal ? <text x={x + 16} y={y + 17} textAnchor="middle" dominantBaseline="central" className={styles.cellNumber}>¹⁄₇</text> : magnitude > 0 && <g opacity={0.38 + 0.62 * magnitude} className={styles.phaseArrow}><line x1={x + 16 - 5 * Math.cos(phase)} y1={y + 16 + 5 * Math.sin(phase)} x2={tipX} y2={tipY} /><path d={`M ${tipX - 4 * Math.cos(phase - 0.6)} ${tipY + 4 * Math.sin(phase - 0.6)} L ${tipX} ${tipY} L ${tipX - 4 * Math.cos(phase + 0.6)} ${tipY + 4 * Math.sin(phase + 0.6)}`} /></g>}
              </g>;
            }))}
            <path d="M109 33h-5v256h5 M375 33h5v256h-5" className={styles.matrixBracket} />
            <text x="96" y="296" className={styles.diagramLabel}>Γᵢⱼ = Γ̄ⱼᵢ</text><text x="384" y="296" textAnchor="end" className={styles.diagramLabel}>Tr Γ = 1</text>
          </svg>
        )}
        <div className={styles.legend}>{view === 'relations' ? copy.relationLegend : view === 'matrix' ? copy.matrixLegend : view === 'readout' ? copy.readoutLegend : copy.fanoLegend}</div>
      </div>

      <div className={styles.explanation}>
        {view === 'relations' && <><span className={styles.selectionMark}>{BASIS[selected]}</span><div><strong>{tr(role.name, locale)}</strong><p>{tr(role.meaning, locale)}. <span>{copy.semanticNote}</span></p></div></>}
        {view === 'matrix' && <><span className={styles.selectionMark}>{BASIS[row]}{BASIS[column]}</span><div><strong>{tr(cell.name, locale)}</strong><p>{tr(cell.meaning, locale)}.</p><code data-testid="ontology-entry">Γ{subscript(BASIS[row] + BASIS[column])} = {number(entry.re)} {entry.im < 0 ? '−' : '+'} {number(Math.abs(entry.im))}i</code>{strength === 0 && row !== column && <p>{copy.phaseZero}</p>}</div></>}
        {view === 'fano' && <div className={styles.fanoDescription}><div className={styles.lineSelector} role="group" aria-label={copy.line}>{FANO_LINES.map((triple, index) => <button type="button" key={index} aria-label={`${copy.line} ${triple.map((n) => BASIS[n - 1]).join(', ')}`} aria-pressed={line === index} onClick={() => setLine(index)} className={line === index ? styles.activeLine : undefined}>{index + 1}</button>)}</div><strong className={styles.product}>e<sub>{BASIS[a]}</sub> e<sub>{BASIS[b]}</sub> = e<sub>{BASIS[c]}</sub></strong><p>{copy.fanoNote}</p></div>}
        {view === 'readout' && <div><strong>{copy.readoutTitle}</strong><p>{copy.readoutNote} <Link to="/docs/applied/research/reconstruction-identifiability">{copy.readoutLink} →</Link></p></div>}
      </div>

      <div className={styles.controls}>
        <label htmlFor={`${id}-strength`}>{copy.strength} <span>s = <output data-testid="ontology-strength">{strength.toFixed(2)}</output></span></label>
        <input id={`${id}-strength`} type="range" min="0" max="1" step="0.01" value={strength} onChange={(event) => setStrength(Number(event.target.value))} aria-describedby={`${id}-family`} aria-valuetext={`${strength.toFixed(2)}. ${copy.sHelp}`} data-testid="ontology-slider" />
      </div>

      <dl className={styles.metrics}>
        <div><dt title="P = (1 + 6s²)/7"><span>P</span> {copy.purity}</dt><dd data-testid="ontology-purity">{number(state.purity)}</dd></div>
        <div><dt title="Φ = 6s²"><span>Φ</span> {copy.integration}</dt><dd data-testid="ontology-integration">{number(state.integration)}</dd></div>
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
