import type {ReactNode, JSX} from 'react';
import {useState, useEffect, useRef} from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';
import Translate, {translate} from '@docusaurus/Translate';

import styles from './index.module.css';

/**
 * Визуализация УГМ
 *
 * Минималистичная гептаграмма {7/3} — Звезда Магов:
 * - Гептаграмма {7/3} — священная звезда семи измерений
 * - Фрактальность — мини-гептаграммы в вершинах (самоподобие)
 * - Лучи от центра — потоки самомоделирования (φ)
 * - ∞ в центре — бесконечность как источник
 * - Вращение — стрела времени
 */
function CoherenceVisualization() {
  const cx = 250, cy = 250;
  const [time, setTime] = useState(0);
  const animationRef = useRef<number | undefined>(undefined);
  const startTimeRef = useRef<number>(Date.now());

  useEffect(() => {
    const animate = () => {
      const elapsed = (Date.now() - startTimeRef.current) / 1000;
      setTime(elapsed);
      animationRef.current = requestAnimationFrame(animate);
    };
    animationRef.current = requestAnimationFrame(animate);
    return () => {
      if (animationRef.current) {
        cancelAnimationFrame(animationRef.current);
      }
    };
  }, []);

  // Геометрические параметры
  const rotationSpeed = 1.5;
  const coreR = 35;           // ядро ∞
  const innerR = 65;          // внутреннее кольцо
  const starR = 125;          // радиус гептаграммы (лучи)
  const boundaryR = 170;      // граница

  // Дыхание системы
  const breath = 1 + Math.sin(time * 0.35) * 0.02;

  // Гептаграмма {7/3}
  const renderHeptagram = () => {
    const lines: JSX.Element[] = [];
    const r = starR * breath;

    for (let i = 0; i < 7; i++) {
      const j = (i + 3) % 7;
      const a1 = ((i * 360 / 7) - 90) * Math.PI / 180;
      const a2 = ((j * 360 / 7) - 90) * Math.PI / 180;

      const x1 = cx + Math.cos(a1) * r;
      const y1 = cy + Math.sin(a1) * r;
      const x2 = cx + Math.cos(a2) * r;
      const y2 = cy + Math.sin(a2) * r;

      const pulse = Math.sin(time * 0.4 + i * 0.5);
      const opacity = 0.25 + pulse * 0.15;

      lines.push(
        <line key={`star-${i}`}
          x1={x1} y1={y1} x2={x2} y2={y2}
          stroke="var(--ifm-color-primary)"
          strokeWidth={1.5}
          opacity={opacity}
        />
      );
    }
    return lines;
  };

  // Лучи от центра (самомоделирование φ)
  const renderRays = () => {
    const elements: JSX.Element[] = [];

    for (let i = 0; i < 7; i++) {
      const angle = ((i * 360 / 7) - 90) * Math.PI / 180;

      const phase = i * (Math.PI * 2 / 7);
      const pulse = Math.sin(time * 0.6 + phase);
      const rayLen = (starR + pulse * 6) * breath;

      const x1 = cx + Math.cos(angle) * coreR;
      const y1 = cy + Math.sin(angle) * coreR;
      const x2 = cx + Math.cos(angle) * rayLen;
      const y2 = cy + Math.sin(angle) * rayLen;

      // Луч
      elements.push(
        <line key={`ray-${i}`}
          x1={x1} y1={y1} x2={x2} y2={y2}
          stroke="var(--ifm-color-primary)"
          strokeWidth={1.5}
          strokeLinecap="round"
          opacity={0.35 + pulse * 0.15}
        />
      );

      // Узел на конце
      elements.push(
        <circle key={`node-${i}`}
          cx={x2} cy={y2}
          r={3.5 * breath}
          fill="var(--ifm-color-primary)"
          opacity={0.5 + pulse * 0.2}
        />
      );
    }
    return elements;
  };

  // Дуги когерентности
  const renderArcs = () => {
    const arcs: JSX.Element[] = [];
    const r = innerR * breath;

    for (let i = 0; i < 7; i++) {
      const a1 = ((i * 360 / 7) - 90) * Math.PI / 180;
      const a2 = (((i + 1) * 360 / 7) - 90) * Math.PI / 180;

      const x1 = cx + Math.cos(a1) * r;
      const y1 = cy + Math.sin(a1) * r;
      const x2 = cx + Math.cos(a2) * r;
      const y2 = cy + Math.sin(a2) * r;

      const midA = (a1 + a2) / 2;
      const ctrlR = r * 1.15;
      const ctrlX = cx + Math.cos(midA) * ctrlR;
      const ctrlY = cy + Math.sin(midA) * ctrlR;

      const pulse = Math.sin(time * 0.5 + i * 0.7);

      arcs.push(
        <path key={`arc-${i}`}
          d={`M ${x1} ${y1} Q ${ctrlX} ${ctrlY} ${x2} ${y2}`}
          fill="none"
          stroke="var(--ifm-color-primary)"
          strokeWidth={1}
          opacity={0.15 + pulse * 0.1}
        />
      );
    }
    return arcs;
  };

  // Мини-гептаграммы в вершинах (фрактальность)
  const renderMiniHeptagrams = () => {
    const elements: JSX.Element[] = [];
    const mainR = starR * breath;
    const miniR = 8; // маленький радиус

    for (let v = 0; v < 7; v++) {
      const va = ((v * 360 / 7) - 90) * Math.PI / 180;
      const vx = cx + Math.cos(va) * mainR;
      const vy = cy + Math.sin(va) * mainR;

      // Мини-гептаграмма {7/3}
      for (let i = 0; i < 7; i++) {
        const j = (i + 3) % 7;
        const a1 = ((i * 360 / 7) - 90) * Math.PI / 180;
        const a2 = ((j * 360 / 7) - 90) * Math.PI / 180;

        const x1 = vx + Math.cos(a1) * miniR;
        const y1 = vy + Math.sin(a1) * miniR;
        const x2 = vx + Math.cos(a2) * miniR;
        const y2 = vy + Math.sin(a2) * miniR;

        const pulse = Math.sin(time * 0.5 + v * 0.9);

        elements.push(
          <line key={`mini-${v}-${i}`}
            x1={x1} y1={y1} x2={x2} y2={y2}
            stroke="var(--ifm-color-primary)"
            strokeWidth={0.5}
            opacity={0.12 + pulse * 0.08}
          />
        );
      }
    }
    return elements;
  };

  return (
    <svg viewBox="0 0 500 500" className={styles.orbitalSvg}>
      <defs>
        <radialGradient id="bgGrad" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stopColor="var(--ifm-color-primary)" stopOpacity="0.5" />
          <stop offset="50%" stopColor="var(--ifm-color-primary)" stopOpacity="0.15" />
          <stop offset="100%" stopColor="var(--ifm-color-primary)" stopOpacity="0" />
        </radialGradient>
        <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
          <feGaussianBlur stdDeviation="3" result="blur"/>
          <feMerge>
            <feMergeNode in="blur"/>
            <feMergeNode in="SourceGraphic"/>
          </feMerge>
        </filter>
        <filter id="coreGlow" x="-100%" y="-100%" width="300%" height="300%">
          <feGaussianBlur stdDeviation="5" result="blur"/>
          <feMerge>
            <feMergeNode in="blur"/>
            <feMergeNode in="SourceGraphic"/>
          </feMerge>
        </filter>
      </defs>

      {/* Фоновое свечение */}
      <circle cx={cx} cy={cy} r={boundaryR * breath} fill="url(#bgGrad)" />

      {/* Внешний гептагон */}
      <polygon
        points={Array.from({ length: 7 }, (_, i) => {
          const a = ((i * 360 / 7) - 90) * Math.PI / 180;
          return `${cx + Math.cos(a) * boundaryR * breath},${cy + Math.sin(a) * boundaryR * breath}`;
        }).join(' ')}
        fill="none"
        stroke="var(--ifm-color-primary)"
        strokeWidth={1}
        opacity={0.2}
      />

      {/* Вращающаяся группа */}
      <g style={{
        transform: `rotate(${time * rotationSpeed}deg)`,
        transformOrigin: `${cx}px ${cy}px`
      }}>
        {/* Внутреннее кольцо */}
        <circle cx={cx} cy={cy} r={innerR * breath}
          fill="none"
          stroke="var(--ifm-color-primary)"
          strokeWidth={0.5}
          strokeDasharray="2 4"
          opacity={0.2} />

        {/* Среднее кольцо */}
        <circle cx={cx} cy={cy} r={starR * breath}
          fill="none"
          stroke="var(--ifm-color-primary)"
          strokeWidth={0.5}
          opacity={0.1} />

        {/* Дуги когерентности */}
        <g filter="url(#glow)">{renderArcs()}</g>

        {/* Гептаграмма */}
        <g filter="url(#glow)">{renderHeptagram()}</g>

        {/* Мини-гептаграммы в вершинах (фрактальность) */}
        {renderMiniHeptagrams()}

        {/* Лучи */}
        <g filter="url(#glow)">{renderRays()}</g>
      </g>

      {/* Центральное ядро ∞ */}
      {(() => {
        const wx = Math.sin(time * 0.31) * 2;
        const wy = Math.sin(time * 0.23) * 2;
        const x = cx + wx;
        const y = cy + wy;
        const r = coreR * breath;

        return (
          <g className={styles.coreGroup}>
            <circle cx={x} cy={y} r={r * 1.3}
              fill="var(--ifm-color-primary)"
              opacity={0.12}
              filter="url(#coreGlow)" />
            <circle cx={x} cy={y} r={r}
              fill="var(--ifm-color-primary)"
              className={styles.coreCircle} />
            <text x={x} y={y}
              className={styles.coreSymbol}
              textAnchor="middle"
              dominantBaseline="central">
              ∞
            </text>
          </g>
        );
      })()}
    </svg>
  );
}

// Интерпретации элементов матрицы когерентности
const matrixInfo: Record<string, { name: string; desc: string }> = {
  // Диагональ (населённости)
  AA: { name: 'Articulation', desc: 'Distinguishing activity' },
  SS: { name: 'Structure', desc: 'Form stability' },
  DD: { name: 'Dynamics', desc: 'Process activity' },
  LL: { name: 'Logic', desc: 'Internal consistency' },
  EE: { name: 'Interiority', desc: 'Intensity of interior states' },
  OO: { name: 'Ground', desc: 'Connection to source' },
  UU: { name: 'Unity', desc: 'Integration' },
  // Coherences (21 pairs)
  AS: { name: 'Morphogenesis', desc: 'Distinctions → stable forms' },
  AD: { name: 'Actualization', desc: 'Distinction → actual process' },
  AL: { name: 'Predication', desc: 'Distinction → logical predicate' },
  AE: { name: 'Apperception', desc: 'Distinction → interiority' },
  AO: { name: 'Spontaneity', desc: 'Distinctions from ground' },
  AU: { name: 'Differentiation', desc: 'Distinction within the whole' },
  SD: { name: 'Persistence', desc: 'Form through process' },
  SL: { name: 'Nomos', desc: 'Structure with necessity' },
  SE: { name: 'Representation', desc: 'Structure in interiority' },
  SO: { name: 'Archetype', desc: 'Forms from ground' },
  SU: { name: 'Symmetry', desc: 'Structural unity' },
  DL: { name: 'Regulation', desc: 'Logically governed process' },
  DE: { name: 'Affection', desc: 'Process → interiority' },
  DO: { name: 'Genesis', desc: 'Generation from ground' },
  DU: { name: 'Teleology', desc: 'Directed change' },
  LE: { name: 'Evidence', desc: 'Logic in interiority' },
  LO: { name: 'Foundation', desc: 'Logic from ground' },
  LU: { name: 'Consistency', desc: 'Non-contradiction of the whole' },
  EO: { name: 'Immanence', desc: 'Ground in interiority' },
  EU: { name: 'Synthesis', desc: 'Integration into whole' },
  OU: { name: 'Plenitude', desc: 'Source ≡ whole' },
};

// Матрица когерентности Γ
function CoherenceMatrixVisualization() {
  const dims = ['A', 'S', 'D', 'L', 'E', 'O', 'U'];
  const [tooltip, setTooltip] = useState<{
    row: string; col: string; name: string; desc: string;
    x: number; y: number;
  } | null>(null);
  const containerRef = useRef<HTMLDivElement>(null);

  const getInfo = (i: number, j: number) => {
    const key = i <= j ? `${dims[i]}${dims[j]}` : `${dims[j]}${dims[i]}`;
    return matrixInfo[key];
  };

  const handleMouseEnter = (e: React.MouseEvent, i: number, j: number) => {
    const container = containerRef.current;
    if (!container) return;
    const cRect = container.getBoundingClientRect();
    const tRect = (e.currentTarget as HTMLElement).getBoundingClientRect();
    const info = getInfo(i, j);
    setTooltip({
      row: dims[i], col: dims[j],
      name: info.name, desc: info.desc,
      x: tRect.left - cRect.left + tRect.width / 2,
      y: tRect.top - cRect.top,
    });
  };

  return (
    <div className={styles.matrixContainer} ref={containerRef}>
      <div className={styles.matrixGrid}>
        {dims.map((row, i) => (
          dims.map((col, j) => (
            <div
              key={`${i}-${j}`}
              className={clsx(
                styles.matrixCell,
                i === j && styles.diagonal,
                i !== j && styles.offDiagonal
              )}
              onMouseEnter={(e) => handleMouseEnter(e, i, j)}
              onMouseLeave={() => setTooltip(null)}
            >
              <span className={styles.cellValue}>{`γ${row}${col}`}</span>
            </div>
          ))
        ))}
      </div>
      {tooltip && (
        <div
          className={styles.matrixTooltip}
          style={{ left: tooltip.x, top: tooltip.y }}
        >
          <strong>γ{tooltip.row}{tooltip.col}: {tooltip.name}</strong>
          <span>{tooltip.desc}</span>
        </div>
      )}
      <div className={styles.matrixCaption}>
        Coherence Matrix Γ ∈ ℂ⁷ˣ⁷
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
            <Translate id="homepage.hero.subtitle">What if reality has a single mathematical structure?</Translate>
          </p>
          <p className={styles.heroDescription}>
            <Translate id="homepage.hero.description">Five axioms generate an ∞-topos from which seven dimensions, time, space, and quantum mechanics inevitably follow — without a single arbitrary parameter. The inner aspect of a system turns out to be not a byproduct, but a necessary condition for its existence.</Translate>
          </p>
          <div className={styles.heroButtons}>
            <Link className="button button--primary button--lg" to="/docs/intro">
              <Translate id="homepage.hero.cta">Introduction</Translate>
            </Link>
          </div>
        </div>
        <div className={styles.heroVisual}>
          <CoherenceVisualization />
        </div>
      </div>
    </header>
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
              <Translate id="homepage.matrix.description">The central mathematical object — a 7×7 Hermitian matrix. Diagonal — populations of dimensions (A, S, D, L, E, O, U). Off-diagonal elements — coherences between them.</Translate>
            </p>
            <ul className={styles.matrixProperties}>
              <li><strong>Purity P = Tr(Γ²)</strong> — <Translate id="homepage.matrix.purity">measure of integrity</Translate></li>
              <li><strong>P_crit = 2/7</strong> — <Translate id="homepage.matrix.threshold">viability condition</Translate></li>
              <li><strong>C = Φ × R</strong> — <Translate id="homepage.matrix.consciousness">integration × reflexion</Translate></li>
              <li><strong>L0→L4</strong> — <Translate id="homepage.matrix.levels">from interiority to unity</Translate></li>
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
  title: string;
  description: string;
  link: string;
  items: string[];
};

const docSections: DocSection[] = [
  {
    title: 'The Single Primitive',
    description: 'Five Axioms Ω⁷',
    link: '/docs/core/foundations/axiom-omega',
    items: ['∞-topos Sh∞(𝒞) — everything else is derived', 'Logic, time and space are consequences', 'Principle of informational distinguishability'],
  },
  {
    title: 'Structure',
    description: 'Seven Dimensions of the Holon',
    link: '/docs/core/structure/holon',
    items: ['Holon — integral unit of being', 'Seven dimensions: A, S, D, L, E, O, U', 'Coherence matrix Γ ∈ ℂ⁷ˣ⁷'],
  },
  {
    title: 'Octonionic Foundation',
    description: 'Why Exactly 7',
    link: '/docs/proofs/minimality/theorem-octonionic-derivation',
    items: ['P1 + P2 → 𝕆 → dim(Im(𝕆)) = 7', 'Fano plane and G₂ symmetry', 'Hamming code H(7,4) and Cayley-Dickson boundary'],
  },
  {
    title: 'Dynamics',
    description: 'Evolution Equation',
    link: '/docs/core/dynamics/evolution',
    items: ['dΓ/dτ = −i[H,Γ] + 𝒟[Γ] + ℛ[Γ,E]', 'Dissipation from decoherence, regeneration from interiority', 'Global attractor'],
  },
  {
    title: 'Emergent Time',
    description: 'Time from Structure',
    link: '/docs/proofs/dynamics/emergent-time',
    items: ['Time is not postulated — it is derived', 'O-dimension as internal clock', 'Discreteness τ ∈ ℤ₇ and arrow of time'],
  },
  {
    title: 'Viability',
    description: 'Conditions of Existence',
    link: '/docs/core/dynamics/viability',
    items: ['Purity P — measure of integrity', 'P_crit = 2/7 (theorem, five paths)', 'Domain of stability'],
  },
  {
    title: 'Gap Semantics',
    description: 'Interiority / Exteriority',
    link: '/docs/core/dynamics/gap-operator',
    items: ['Gap(i,j) = |sin(arg(γᵢⱼ))| — duality', 'Fano channel: dissipation via PG(2,2)', 'Phase diagram of coherent states'],
  },
  {
    title: 'Consciousness',
    description: 'From Qualia to Collective Mind',
    link: '/docs/consciousness/overview',
    items: ['21-pair qualia taxonomy from Γ', 'Emotions, attention, memory — from formalism', 'AI consciousness: operational criteria'],
  },
  {
    title: 'Physical Correspondence',
    description: 'From Γ to the Standard Model',
    link: '/docs/physics/overview',
    items: ['G₂ gauge symmetry and generations', 'Yukawa hierarchy from Fano textures', 'Cosmological constant: Λ budget'],
  },
  {
    title: 'Proofs',
    description: 'Formal Theorems',
    link: '/docs/proofs/minimality/theorem-minimality-7',
    items: ['Minimality of 7 dimensions (Track A)', '180+ results: from P_crit = 2/7 to substrate independence', 'Categorical formalism and lax 2-functor'],
  },
  {
    title: 'Coherence Cybernetics',
    description: 'Engineering Applications',
    link: '/docs/applied/coherence-cybernetics/introduction',
    items: ['Measurement protocol for Γ in AI', 'Conditional No-Zombie theorem', 'Paninteriorism ≠ panpsychism'],
  },
  {
    title: 'Reference',
    description: 'Verification & Notation',
    link: '/docs/reference/falsifiability',
    items: ['Falsifiable predictions of the theory', 'Status registry [Т]/[С]/[О]/[И]/[Г]/[П]', 'Glossary, notation, specification'],
  },
];

function DocumentationSection() {
  return (
    <section className={styles.docsSection}>
      <div className="container">
        <div className={styles.docsGrid}>
          {docSections.map((section) => (
            <Link key={section.title} to={section.link} className={styles.docCard}>
              <h3>{section.title}</h3>
              <p className={styles.docDescription}>{section.description}</p>
              <ul className={styles.docItems}>
                {section.items.map((item, i) => (
                  <li key={i}>{item}</li>
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
      description={translate({id: 'homepage.layout.description', message: 'Unitary Holonomic Monism — an axiomatic theory based on the ∞-topos Sh∞(𝒞). Time, structure and consciousness are derived as consequences of five axioms.'})}>
      <HomepageHeader />
      <main>
        <MatrixSection />
        <DocumentationSection />
      </main>
    </Layout>
  );
}
