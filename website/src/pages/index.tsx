import type {ReactNode} from 'react';
import {useState, useEffect, useRef} from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';
import Translate, {translate} from '@docusaurus/Translate';
import {DIMENSIONS, cellOf, tr} from '@site/src/data/coherences';

import styles from './index.module.css';

/**
 * The hero figure: the Fano plane with the canonical orientation of UHM.
 *
 * Index convention {A, S, D, L, E, U, O} = {1, …, 7} and the canonical lines
 * (1,2,4), (2,3,5), (3,4,6), (4,5,7), (5,6,1), (6,7,2), (7,1,3) — the same
 * table as `LINES` in scripts/check_core_numbers.py. A cyclic triple (i, j, k)
 * means e_i · e_j = e_k for the imaginary octonion units. The layout puts O at
 * the centre: the three lines through O are the medians, and D, L, U lie on
 * the inscribed circle (the line (3,4,6)).
 *
 * The animation plays the multiplication table one line at a time; the gauge
 * below shows purity P between 1/7 and 1 with the viability window
 * 2/7 < P ≤ 3/7, and a marker that stays inside it (an illustration of a
 * living state, not a simulation).
 */
const LABEL: Record<number, string> = {1: 'A', 2: 'S', 3: 'D', 4: 'L', 5: 'E', 6: 'U', 7: 'O'};
const LINES: [number, number, number][] = [
  [1, 2, 4], [2, 3, 5], [3, 4, 6], [4, 5, 7], [5, 6, 1], [6, 7, 2], [7, 1, 3],
];

const CX = 250;
const CY = 238;
const R_TRI = 190; // circumradius of the triangle
const vertex = (deg: number) => {
  const a = (deg * Math.PI) / 180;
  return {x: CX + R_TRI * Math.cos(a), y: CY + R_TRI * Math.sin(a)};
};
const V0 = vertex(-90);
const V1 = vertex(150);
const V2 = vertex(30);
const mid = (p: {x: number; y: number}, q: {x: number; y: number}) => ({x: (p.x + q.x) / 2, y: (p.y + q.y) / 2});
const M01 = mid(V0, V1);
const M12 = mid(V1, V2);
const M02 = mid(V0, V2);
const C = {x: CX, y: CY};
const R_IN = R_TRI / 2; // inscribed circle passes through the three midpoints

// Canonical assignment (verified: every canonical line maps to a drawn line).
const POS: Record<number, {x: number; y: number}> = {
  1: V0, // A
  2: V1, // S
  3: M12, // D
  4: M01, // L
  5: V2, // E
  6: M02, // U
  7: C, // O
};

// Straight lines in geometric order (end, middle, end); the circle is line (3,4,6).
const STRAIGHT: Record<string, [number, number, number]> = {
  '1,2,4': [1, 4, 2],
  '2,3,5': [2, 3, 5],
  '4,5,7': [4, 7, 5],
  '5,6,1': [5, 6, 1],
  '6,7,2': [6, 7, 2],
  '7,1,3': [1, 7, 3],
};

const isRotation = (a: number[], b: number[]) =>
  [0, 1, 2].some((s) => a.every((v, i) => v === b[(i + s) % 3]));

function arrowHead(x: number, y: number, dx: number, dy: number, key: string, cls: string) {
  const len = Math.hypot(dx, dy) || 1;
  const ux = dx / len;
  const uy = dy / len;
  const s = 7;
  const p1 = `${x + ux * s},${y + uy * s}`;
  const p2 = `${x - ux * s * 0.6 - uy * s * 0.7},${y - uy * s * 0.6 + ux * s * 0.7}`;
  const p3 = `${x - ux * s * 0.6 + uy * s * 0.7},${y - uy * s * 0.6 - ux * s * 0.7}`;
  return <polygon key={key} points={`${p1} ${p2} ${p3}`} className={cls} />;
}

function FanoFigure() {
  const [active, setActive] = useState(0);
  const [reduced, setReduced] = useState(false);

  useEffect(() => {
    const mq = window.matchMedia('(prefers-reduced-motion: reduce)');
    setReduced(mq.matches);
    if (mq.matches) return undefined;
    const id = window.setInterval(() => setActive((a) => (a + 1) % 7), 2600);
    return () => window.clearInterval(id);
  }, []);

  const [i, j, k] = LINES[active];

  const drawLine = (line: [number, number, number], idx: number) => {
    const on = idx === active;
    const cls = clsx(styles.fanoLine, on && styles.fanoLineActive);
    const arrows: ReactNode[] = [];
    const key = line.join(',');
    if (key === '3,4,6') {
      // Circle: arrows at the arcs between consecutive points of the cycle.
      const ang = (n: number) => Math.atan2(POS[n].y - CY, POS[n].x - CX);
      const cyc = [3, 4, 6];
      cyc.forEach((a, t) => {
        const b = cyc[(t + 1) % 3];
        const a0 = ang(a);
        const a1 = ang(b);
        // direction of travel a → b along the shorter arc that avoids the third point
        let d = a1 - a0;
        while (d <= -Math.PI) d += 2 * Math.PI;
        while (d > Math.PI) d -= 2 * Math.PI;
        const am = a0 + d / 2;
        const x = CX + R_IN * Math.cos(am);
        const y = CY + R_IN * Math.sin(am);
        const sgn = Math.sign(d);
        arrows.push(arrowHead(x, y, -Math.sin(am) * sgn, Math.cos(am) * sgn, `ar-${key}-${t}`, clsx(styles.fanoArrow, on && styles.fanoArrowActive)));
      });
      return (
        <g key={key}>
          <circle cx={CX} cy={CY} r={R_IN} className={cls} />
          {arrows}
        </g>
      );
    }
    const geo = STRAIGHT[key];
    const forward = isRotation(line, geo);
    const [p, q, r] = geo.map((n) => POS[n]);
    const dir = forward ? 1 : -1;
    const seg = (a: {x: number; y: number}, b: {x: number; y: number}, t: number) => {
      const m = mid(a, b);
      return arrowHead(m.x, m.y, (b.x - a.x) * dir, (b.y - a.y) * dir, `ar-${key}-${t}`, clsx(styles.fanoArrow, on && styles.fanoArrowActive));
    };
    return (
      <g key={key}>
        <line x1={p.x} y1={p.y} x2={r.x} y2={r.y} className={cls} />
        {seg(p, q, 0)}
        {seg(q, r, 1)}
      </g>
    );
  };

  return (
    <figure className={styles.fanoFigure}>
      <svg
        viewBox="0 0 500 440"
        className={styles.fanoSvg}
        role="img"
        aria-label={translate({
          id: 'homepage.fano.aria',
          message: 'The Fano plane with the seven dimensions A, S, D, L, E, U, O and the oriented lines of octonion multiplication',
        })}>
        <defs>
          <radialGradient id="fanoGlow" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stopColor="var(--ifm-color-primary)" stopOpacity="0.22" />
            <stop offset="100%" stopColor="var(--ifm-color-primary)" stopOpacity="0" />
          </radialGradient>
        </defs>
        <circle cx={CX} cy={CY} r={R_TRI * 1.05} fill="url(#fanoGlow)" />
        {LINES.map(drawLine)}
        {Object.entries(POS).map(([n, p]) => {
          const num = Number(n);
          const role = num === i || num === j ? 'factor' : num === k ? 'product' : 'idle';
          return (
            <g key={n} className={clsx(styles.fanoNode, role === 'factor' && styles.fanoFactor, role === 'product' && styles.fanoProduct)}>
              <circle cx={p.x} cy={p.y} r={num === 7 ? 21 : 18} />
              <text x={p.x} y={p.y} textAnchor="middle" dominantBaseline="central">{LABEL[num]}</text>
            </g>
          );
        })}
      </svg>
      <figcaption className={styles.fanoCaption}>
        <span className={styles.fanoProductText} aria-live="polite">
          e<sub>{LABEL[i]}</sub> · e<sub>{LABEL[j]}</sub> = e<sub>{LABEL[k]}</sub>
        </span>
        <span className={styles.fanoNote}>
          <Translate id="homepage.fano.caption">Seven dimensions, seven lines: each oriented line is one rule of octonion multiplication. O, at the centre, carries the clock.</Translate>
        </span>
      </figcaption>
      <PurityGauge />
    </figure>
  );
}

function PurityGauge() {
  // Map P ∈ [1/7, 1] onto the gauge width.
  const x = (p: number) => ((p - 1 / 7) / (1 - 1 / 7)) * 100;
  return (
    <div className={styles.gauge}>
      <div className={styles.gaugeTrack}>
        <div className={styles.gaugeWindow} style={{left: `${x(2 / 7)}%`, width: `${x(3 / 7) - x(2 / 7)}%`}} />
        <div className={styles.gaugeMarker} style={{left: `${x(2 / 7)}%`, width: `${x(3 / 7) - x(2 / 7)}%`}}>
          <span />
        </div>
      </div>
      <div className={styles.gaugeScale}>
        <span style={{left: '0%'}}>1/7</span>
        <span style={{left: `${x(2 / 7)}%`}}>2/7</span>
        <span style={{left: `${x(3 / 7)}%`}}>3/7</span>
        <span style={{left: '100%'}}>1</span>
      </div>
      <div className={styles.gaugeLabel}>
        <Translate id="homepage.gauge.label">Purity P = Tr Γ² — the viability window 2/7 &lt; P ≤ 3/7</Translate>
      </div>
    </div>
  );
}

// Coherence matrix Γ — names and meanings from the single source src/data/coherences.ts
function CoherenceMatrixVisualization() {
  const {i18n} = useDocusaurusContext();
  const locale = i18n.currentLocale;
  const dims = DIMENSIONS;
  const [tooltip, setTooltip] = useState<{
    row: string; col: string; name: string; desc: string;
    x: number; y: number;
  } | null>(null);
  const containerRef = useRef<HTMLDivElement>(null);

  const show = (el: HTMLElement, a: number, b: number) => {
    const container = containerRef.current;
    if (!container) return;
    const cRect = container.getBoundingClientRect();
    const tRect = el.getBoundingClientRect();
    const cell = cellOf(dims[a], dims[b]);
    setTooltip({
      row: dims[a], col: dims[b],
      name: tr(cell.name, locale),
      desc: tr(cell.meaning, locale),
      x: tRect.left - cRect.left + tRect.width / 2,
      y: tRect.top - cRect.top,
    });
  };

  return (
    <div className={styles.matrixContainer} ref={containerRef}>
      <div className={styles.matrixGrid}>
        {dims.map((row, a) => (
          dims.map((col, b) => (
            <button
              type="button"
              key={`${a}-${b}`}
              className={clsx(
                styles.matrixCell,
                a === b && styles.diagonal,
                a !== b && styles.offDiagonal,
              )}
              onMouseEnter={(e) => show(e.currentTarget, a, b)}
              onFocus={(e) => show(e.currentTarget, a, b)}
              onMouseLeave={() => setTooltip(null)}
              onBlur={() => setTooltip(null)}
            >
              <span className={styles.cellValue}>{`γ${row}${col}`}</span>
            </button>
          ))
        ))}
      </div>
      {tooltip && (
        <div
          className={styles.matrixTooltip}
          style={{left: tooltip.x, top: tooltip.y}}
        >
          <strong>γ{tooltip.row}{tooltip.col}: {tooltip.name}</strong>
          <span>{tooltip.desc}</span>
        </div>
      )}
      <div className={styles.matrixCaption}>
        <Translate id="homepage.matrix.caption">Coherence Matrix Γ ∈ ℂ⁷ˣ⁷</Translate>
      </div>
    </div>
  );
}

function HomepageHeader() {
  return (
    <header className={styles.hero}>
      <div className={styles.heroContent}>
        <div className={styles.heroText}>
          <Heading as="h1" className={styles.heroTitle}>
            <Translate id="homepage.hero.title">Unitary Holonomic Monism</Translate>
          </Heading>
          <p className={styles.heroSubtitle}>
            <Translate id="homepage.hero.subtitle.v2">One mathematical structure — for matter, time and the inner side of things.</Translate>
          </p>
          <p className={styles.heroDescription}>
            <Translate id="homepage.hero.description.v2">A single primitive — an ∞-topos over the states Γ of a seven-dimensional system — and five axioms. Proved from them: time as the reading of an internal clock and a viability window 2/7 &lt; P ≤ 3/7 for anything alive. Once matter is placed on the complexified octonions and spacetime is read from its Hermitian forms — two premises the theory names rather than hides — the Standard Model group with one complete generation of fermions and a 3+1 spacetime follow as theorems. Every claim carries its status: proved, conditional, hypothesis, or retracted.</Translate>
          </p>
          <div className={styles.heroButtons}>
            <Link className="button button--primary button--lg" to="/docs/intro">
              <Translate id="homepage.hero.cta">Introduction</Translate>
            </Link>
            <Link className="button button--secondary button--lg" to="/docs/reference/premises">
              <Translate id="homepage.hero.ctaPremises">What the theory assumes</Translate>
            </Link>
          </div>
        </div>
        <div className={styles.heroVisual}>
          <FanoFigure />
        </div>
      </div>
    </header>
  );
}

type Claim = {id: string; text: string; ref: string; link: string};

const proved: Claim[] = [
  {id: 'time', text: 'Time as the reading of an internal clock: the depth register gives the time line ℝ', ref: 'T-53b, T-118', link: '/docs/proofs/dynamics/emergent-time'},
  {id: 'window', text: 'Viability window 2/7 < P ≤ 3/7; inside it no single resource optimum', ref: 'P_crit, T-222', link: '/docs/core/dynamics/viability#критическая-чистота'},
  {id: 'sm', text: 'Standard Model group (kernel ℤ₆) and one complete generation with ν_R, anomaly-free, in ℂ⊗𝕆', ref: 'T-326, T-329', link: '/docs/physics/gauge-symmetry/standard-model'},
  {id: 'spacetime', text: 'Lorentzian 3+1 whose rotations commute with colour', ref: '48c', link: '/docs/core/foundations/spacetime'},
  {id: 'tower', text: 'A tower of holons closes to the hyperfinite II₁ factor — given the split property, the algebra of a de Sitter observer, trace to trace', ref: 'T-348', link: '/docs/proofs/dynamics/emergent-time#t-348'},
];

const conditional: Claim[] = [
  {id: 'bridge', text: 'The physical reading of the above rests on two bridge premises, (Cl₀) and (P); neither follows from the axioms', ref: 'T-347', link: '/docs/reference/premises'},
  {id: 'closure', text: 'The axioms follow from the properties of a viable holon under three named conditions', ref: 'T-190', link: '/docs/proofs/categorical/cohesive-closure#теорема-аксиоматическое-замыкание'},
  {id: 'interior', text: 'That the inner aspect of Γ is experience is an interpretation; its structure is tested empirically', ref: '[I]', link: '/docs/consciousness/empirical/overview'},
];

const open: Claim[] = [
  {id: 'kappa', text: 'The regeneration rate κ is free — no route fixes it', ref: 'T-346', link: '/docs/core/dynamics/evolution#t-346'},
  {id: 'theta', text: 'Strong CP: θ̄ is a free parameter; no value of the neutron EDM is predicted', ref: 'Thm 3.1c', link: '/docs/physics/gauge-symmetry/confinement#тета-не-из-потенциала'},
  {id: 'flavour', text: 'Yukawa couplings and the CKM matrix are not derived', ref: 'T-345', link: '/docs/physics/particle-physics/ckm-matrix#11-вкус-с-часов'},
  {id: 'lambda', text: 'The cosmological constant Λ is not fixed by the observer algebra', ref: 'T-348(f)', link: '/docs/proofs/dynamics/emergent-time#t-348'},
];

function ClaimList({items, group}: {items: Claim[]; group: string}) {
  return (
    <ul className={styles.claimList}>
      {items.map((c) => (
        <li key={c.id}>
          <Link to={c.link}>
            {translate({id: `homepage.status.${group}.${c.id}`, message: c.text})}
          </Link>
          <span className={styles.claimRef}>{translate({id: `homepage.status.${group}.${c.id}.ref`, message: c.ref})}</span>
        </li>
      ))}
    </ul>
  );
}

function StatusSection() {
  return (
    <section className={styles.statusSection}>
      <div className="container">
        <Heading as="h2" className={styles.sectionTitle}>
          <Translate id="homepage.status.title">Where the theory stands</Translate>
        </Heading>
        <p className={styles.sectionLead}>
          <Translate id="homepage.status.lead">Every statement of the corpus carries one of the registry's statuses. Here is the short account.</Translate>
        </p>
        <div className={styles.statusGrid}>
          <div className={clsx(styles.statusCol, styles.statusProved)}>
            <h3><span className={styles.statusBadge}>{translate({id: 'homepage.status.badge.proved', message: '[T]'})}</span> <Translate id="homepage.status.proved">Proved as mathematics</Translate></h3>
            <ClaimList items={proved} group="proved" />
          </div>
          <div className={clsx(styles.statusCol, styles.statusConditional)}>
            <h3><span className={styles.statusBadge}>{translate({id: 'homepage.status.badge.conditional', message: '[C] [I]'})}</span> <Translate id="homepage.status.conditional">Conditional or interpretive</Translate></h3>
            <ClaimList items={conditional} group="conditional" />
          </div>
          <div className={clsx(styles.statusCol, styles.statusOpen)}>
            <h3><span className={styles.statusBadge}>{translate({id: 'homepage.status.badge.open', message: '[Pr]'})}</span> <Translate id="homepage.status.open">Open or free</Translate></h3>
            <ClaimList items={open} group="open" />
          </div>
        </div>
        <div className={styles.statusFooter}>
          <Link className="button button--secondary" to="/docs/reference/status-registry">
            <Translate id="homepage.status.registry">Status registry</Translate>
          </Link>
          <Link className="button button--secondary" to="/docs/reference/falsifiability">
            <Translate id="homepage.status.falsifiability">How it can be refuted</Translate>
          </Link>
        </div>
      </div>
    </section>
  );
}

function MatrixSection() {
  return (
    <section className={styles.matrixSection}>
      <div className="container">
        <div className={styles.matrixLayout}>
          <div className={styles.matrixInfo}>
            <Heading as="h2"><Translate id="homepage.matrix.title">Coherence Matrix</Translate></Heading>
            <p>
              <Translate id="homepage.matrix.description.v3">The central object is the state of a holon: a 7×7 density matrix — Hermitian, positive, of trace one. The diagonal holds the populations of the seven dimensions; the 21 off-diagonal entries are the coherences between them. Hover over or tap a cell to read its meaning.</Translate>
            </p>
            <ul className={styles.matrixProperties}>
              <li><strong>P = Tr Γ²</strong> — <Translate id="homepage.matrix.purity.v2">purity, from 1/7 (maximally mixed) to 1 (pure)</Translate></li>
              <li><strong>2/7 &lt; P ≤ 3/7</strong> — <Translate id="homepage.matrix.threshold.v2">the viability window</Translate></li>
              <li><strong>C = Φ · R</strong> — <Translate id="homepage.matrix.consciousness.v2">consciousness measure: integration × reflection, threshold 1/3</Translate></li>
              <li><strong>L0 → L4</strong> — <Translate id="homepage.matrix.levels.v2">levels of interiority, separated by an A₄ (swallowtail) bifurcation</Translate></li>
            </ul>
          </div>
          <div className={styles.matrixVisual}>
            <CoherenceMatrixVisualization />
          </div>
        </div>
        <div className={styles.matrixButton}>
          <Link className="button button--secondary" to="/docs/core/dynamics/coherence-matrix">
            <Translate id="homepage.matrix.cta">Formal Definition</Translate>
          </Link>
        </div>
      </div>
    </section>
  );
}

type DocSection = {
  id: string;
  title: string;
  description: string;
  link: string;
  items: string[];
};

// Card ids carry a version suffix where the text changed, so the Russian
// catalogue cannot keep serving a stale translation under an old id.
const docSections: DocSection[] = [
  {
    id: 'primitive.v2',
    title: 'The Single Primitive',
    description: 'Five Axioms Ω⁷',
    link: '/docs/core/foundations/axiom-omega',
    items: [
      'The ∞-topos Sh∞(𝒞) over the states Γ — the single primitive',
      'Five axioms; every further input named on the premises page',
      'Distinguishability as the Bures metric',
    ],
  },
  {
    id: 'structure.v2',
    title: 'Structure',
    description: 'Seven Dimensions of the Holon',
    link: '/docs/core/structure/holon',
    items: [
      'Holon — the unit that models itself',
      'Seven dimensions: A, S, D, L, E, O, U',
      'All seven are necessary and functionally distinct (theorem 7/7)',
    ],
  },
  {
    id: 'octonionic.v2',
    title: 'Octonionic Foundation',
    description: 'Why Seven',
    link: '/docs/proofs/minimality/theorem-octonionic-derivation',
    items: [
      'Hurwitz: dim Im 𝕆 = 7; N ≥ 7 is a theorem, no decomposition below 7 — premise (Σ₆), T-349',
      'Fano plane, the canonical orientation and G₂',
      'Hamming code H(7,4) and the Cayley–Dickson boundary',
    ],
  },
  {
    id: 'dynamics.v2',
    title: 'Dynamics',
    description: 'Evolution Equation',
    link: '/docs/core/dynamics/evolution',
    items: [
      'dΓ/dτ = −i[H,Γ] + 𝒟[Γ] + ℛ[Γ,E]',
      'Dissipation by decoherence, regeneration by the self-model',
      'Living attractors in the window; the regeneration rate is free (T-346)',
    ],
  },
  {
    id: 'time.v2',
    title: 'Emergent Time',
    description: 'Time from Structure',
    link: '/docs/proofs/dynamics/emergent-time',
    items: [
      'Time is not postulated: the clock register of A5 (T-87)',
      'The time line ℝ from the depth register (T-53b, T-118)',
      'The arrow of time is indexed by stratal depth',
    ],
  },
  {
    id: 'viability.v2',
    title: 'Viability',
    description: 'Conditions of Existence',
    link: '/docs/core/dynamics/viability',
    items: [
      'Purity P — a measure of integrity',
      'Critical purity P_crit = 2/7 — theorem',
      'The window 2/7 < P ≤ 3/7 and its resource geometry (T-222)',
    ],
  },
  {
    id: 'gap',
    title: 'Gap Semantics',
    description: 'Interiority / Exteriority',
    link: '/docs/core/dynamics/gap-operator',
    items: ['Gap(i,j) = |sin(arg(γᵢⱼ))| — duality', 'Fano channel: dissipation via PG(2,2)', 'Phase diagram of coherent states'],
  },
  {
    id: 'consciousness.v2',
    title: 'Consciousness',
    description: 'From Qualia to Collective Mind',
    link: '/docs/consciousness/overview',
    items: [
      'Qualia structure from the geometry of Γ (enriched Yoneda)',
      'Empirical programme: calibration, structure, engineering',
      'AI consciousness: operational criteria',
    ],
  },
  {
    id: 'physics.v2',
    title: 'Physical Correspondence',
    description: 'From Γ to the Standard Model',
    link: '/docs/physics/overview',
    items: [
      'The Standard Model group and one generation in ℂ⊗𝕆 — under (Cl₀)',
      'Flavour: what the clock can and cannot fix (T-345)',
      'Strong CP and Λ: honest no-go results',
    ],
  },
  {
    id: 'proofs.v2',
    title: 'Proofs',
    description: 'Formal Theorems',
    link: '/docs/proofs/minimality/theorem-minimality-7',
    items: [
      'Minimality of the seven dimensions',
      'Critical purity, the viability window, the No-Zombie core',
      'Categorical formalism: the Grothendieck construction (T-211)',
    ],
  },
  {
    id: 'cybernetics.v2',
    title: 'Coherence Cybernetics',
    description: 'Engineering Applications',
    link: '/docs/applied/coherence-cybernetics/introduction',
    items: [
      'Measurement protocol for Γ in AI',
      'No-Zombie: mathematical core [T], reading [I]',
      'Paninteriorism ≠ panpsychism',
    ],
  },
  {
    id: 'reference.v2',
    title: 'Reference',
    description: 'Verification & Notation',
    link: '/docs/reference/falsifiability',
    items: [
      'Falsification criteria and their current verdicts',
      'Status registry: [T] [C] [H] [D] [I] [P] [Pr] [✗]',
      'Premises, glossary, notation',
    ],
  },
];

function DocumentationSection() {
  return (
    <section className={styles.docsSection}>
      <div className="container">
        <Heading as="h2" className={styles.sectionTitle}>
          <Translate id="homepage.docs.title">The corpus</Translate>
        </Heading>
        <div className={styles.docsGrid}>
          {docSections.map((section) => (
            <Link key={section.id} to={section.link} className={styles.docCard}>
              <h3>{translate({id: `homepage.docs.${section.id}.title`, message: section.title})}</h3>
              <p className={styles.docDescription}>
                {translate({id: `homepage.docs.${section.id}.description`, message: section.description})}
              </p>
              <ul className={styles.docItems}>
                {section.items.map((item, n) => (
                  <li key={n}>
                    {translate({id: `homepage.docs.${section.id}.item.${n}`, message: item})}
                  </li>
                ))}
              </ul>
            </Link>
          ))}
        </div>
      </div>
    </section>
  );
}

export default function Home(): ReactNode {
  return (
    <Layout
      title={translate({id: 'homepage.layout.title', message: 'A Formal Theory of Reality'})}
      description={translate({id: 'homepage.layout.description.v2', message: 'Unitary Holonomic Monism — one mathematical structure for matter, time and the inner side of things: an ∞-topos over 7×7 coherence matrices, five axioms, named premises, and a status on every claim.'})}>
      <HomepageHeader />
      <main>
        <StatusSection />
        <MatrixSection />
        <DocumentationSection />
      </main>
    </Layout>
  );
}
