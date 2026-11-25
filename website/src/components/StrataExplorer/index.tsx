import {useState} from 'react';
import Link from '@docusaurus/Link';
import clsx from 'clsx';
import RichText from '@site/src/components/RichText';
import {tr} from '@site/src/data/coherences';
import type {Bilingual} from '@site/src/data/coherences';
import styles from './styles.module.css';

export type StratumId = 'A' | 'B' | 'C';

type StratumSpec = {
  id: StratumId;
  code: Bilingual;
  shortTitle: Bilingual;
  formula: string;
  tag: Bilingual;
  premises: Bilingual;
  verified: Bilingual;
  boundary: Bilingual;
  link: string;
  linkLabel: Bilingual;
};

const STRATA: readonly StratumSpec[] = [
  {
    id: 'A',
    code: {en: 'Stratum A', ru: 'Страта A'},
    shortTitle: {en: 'Core 𝒟(ℂ⁷) + PG(2,2)', ru: 'Ядро 𝒟(ℂ⁷) + PG(2,2)'},
    formula: 'D₇ · G₂ · SU(3)c',
    tag: {en: 'Internal UHM axioms', ru: 'Внутренние аксиомы УГМ'},
    premises: {
      en: '7D coherence state space 𝒟(ℂ⁷), oriented Fano plane PG(2,2), linear CPTP channels, and operational probes (postulate QG).',
      ru: 'Семимерное пространство состояний 𝒟(ℂ⁷), ориентированная плоскость Фано PG(2,2), CPTP-каналы и операционные зонды (постулат QG).',
    },
    verified: {
      en: 'G₂ = Aut(𝕆), SU(3)_{C} × U(1) stabilizer, exact bound Φ ≤ 7P − 1, viability window 2/7 < P ≤ 3/7, quantum Darwinism fiber, and no-go theorems F-1..F-35.',
      ru: 'G₂ = Aut(𝕆), стабилизатор SU(3)_{C} × U(1), точная граница Φ ≤ 7P − 1, окно жизнеспособности 2/7 < P ≤ 3/7, квантовый дарвинизм и запреты F-1..F-35.',
    },
    boundary: {
      en: 'Provably does NOT derive 4D Lorentz spin, KO-dim 6, Pati–Salam/Spin(10) matter, 4D metric gravity, CKM CP, Λ, or dark matter (Thms 48d/e, T-178, T-350).',
      ru: 'Доказуемо НЕ выводит 4D лоренцев спин, KO-размерность 6, материю Пати–Салама/Spin(10), 4D метрическую гравитацию, CKM CP, Λ и тёмную материю (Thms 48d/e, T-178, T-350).',
    },
    link: '/docs/reference/mathematical-kernel',
    linkLabel: {en: 'Mathematical kernel', ru: 'Математическое ядро'},
  },
  {
    id: 'B',
    code: {en: 'Stratum B', ru: 'Страта B'},
    shortTitle: {en: 'Clifford / CCvS Pati–Salam Lift', ru: 'Лифт Клиффорда / CCvS Пати–Салама'},
    formula: 'Cl₀,₇ → ℂ³² · KO-6 · G₄₂₂',
    tag: {en: 'Explicit lift (Cl₀) + KO-6 + (P)', ru: 'Явный лифт (Cl₀) + KO-6 + (P)'},
    premises: {
      en: 'Kähler–Dirac Cl₀,₇ spinor S_{φ} ≅ 4_{ℂ} (Stab_{Spin(7)}(e_{O}) = Spin(6) ≅ SU(4)_{C}), KO-dim 6 real structure J_{F}, and Pati–Salam algebra ℍ_{L} ⊕ ℍ_{R} ⊕ M₄(ℂ) on ℂ³².',
      ru: 'Спинор Кэлера–Дирака Cl₀,₇ S_{φ} ≅ 4_{ℂ} (Stab_{Spin(7)}(e_{O}) = Spin(6) ≅ SU(4)_{C}), вещественная структура J_{F} (KO-6) и алгебра Пати–Салама ℍ_{L} ⊕ ℍ_{R} ⊕ M₄(ℂ) на ℂ³².',
    },
    verified: {
      en: 'F-42A..C (Lean 4), exact 4-color 2-loop RGE (α_{GUT}^{−1} = 45.15, M_{PS} = 1.45×10¹¹ GeV), Δ_{R} Higgs stabilization at m_{h} = 125.25 GeV, and 2D LPM leptogenesis (−2.37% vs Planck).',
      ru: 'F-42A..C (Lean 4), точный 4-цветный 2-петлевой РГ (α_{GUT}^{−1} = 45.15, M_{PS} = 1.45×10¹¹ ГэВ), стабилизация Хиггса Δ_{R} при m_{h} = 125.25 ГэВ и 2D LPM лептогенез (−2.37% от Planck).',
    },
    boundary: {
      en: 'Closed for UV gravity by Super-F-40; light (6,1,1)_{ℂ} excluded by Super-K; requires Heavy-Threshold Split (10¹⁵ GeV) and leaves N_{g} = 3 and v_{EW}/M_{Pl} open.',
      ru: 'Закрыто для UV-гравитации теоремой Super-F-40; лёгкий (6,1,1)_{ℂ} исключён Super-K; требует порога Heavy-Threshold Split (10¹⁵ ГэВ) и не фиксирует N_{g} = 3 и v_{EW}/M_{Pl}.',
    },
    link: '/docs/physics/gauge-symmetry/rg-flow',
    linkLabel: {en: 'CCvS & 2-loop RG flow', ru: 'CCvS и 2-петлевой РГ-поток'},
  },
  {
    id: 'C',
    code: {en: 'Stratum C', ru: 'Страта C'},
    shortTitle: {en: 'Background-Free 4D Gravity & External Sectors', ru: 'Бесфоновая 4D гравитация и внешние сектора'},
    formula: 'S⁴ Regge–Schläfli · SU(2)d · 1F',
    tag: {en: 'Open physical frontier [P]', ru: 'Открытый физический рубеж [P]'},
    premises: {
      en: 'Background-free 4D simplicial Regge/CDT kinematics, external CP spurion for Re τ = 1/4, unimodular sequestering / SU(2)_{d} dark energy, and singlet 1_{F} FIMP dark matter.',
      ru: 'Бесфоновая 4D симплициальная кинематика Редже/CDT, внешний CP-спурион для Re τ = 1/4, унимодулярное секвестрирование / SU(2)_{d} и синглетная тёмная материя 1_{F} FIMP.',
    },
    verified: {
      en: '4D deformed S⁴ Regge–Schläfli (∂β₅: Schläfli 1.50×10⁻¹⁵, 10 conformal vs 30 positive TT spin-2 modes), CMB-S4 ΔN_{eff} & Lyman-α tests (F-39A,B), and honest closures F-41 & V10.2.A.',
      ru: '4D деформированный S⁴ Редже–Шлефли (∂β₅: Шлефли 1.50×10⁻¹⁵, 10 конформных vs 30 положительных TT спин-2 мод), тесты CMB-S4 ΔN_{eff} и Lyman-α (F-39A,B), честные закрытия F-41 и V10.2.A.',
    },
    boundary: {
      en: 'Non-perturbative 4D Regge/CDT continuum limit lim Z_{N}, microscopic CP origin of Re τ = 1/4, and dynamical origin of 1_{F} / SU(2)_{d} remain genuinely open research problems [P].',
      ru: 'Непертурбативный континуальный предел 4D Редже/CDT lim Z_{N}, микроскопический источник CP (Re τ = 1/4) и происхождение 1_{F} / SU(2)_{d} остаются открытыми проблемами [P].',
    },
    link: '/docs/reference/frontier-ledger#stratified-ontology',
    linkLabel: {en: 'Full stratified frontier ledger', ru: 'Полный стратифицированный реестр'},
  },
];

const LABELS = {
  en: {
    eyebrow: 'STRATIFIED EPISTEMIC ARCHITECTURE · ZERO OVERCLAIMING',
    title: 'Three explicit strata separate internal theorems from external bridges.',
    selectLabel: 'Select an ontological stratum',
    premises: 'Formal premises',
    verified: 'Verified core',
    boundary: 'Explicit boundary',
    gateAB: 'Lift: (Cl₀) + KO-6 + (P)',
    gateBC: 'Wall: Super-F-40 & F-41',
    sheafFootnote: 'Optional envelope: Sh∞(Open_{B}(D₇)) ≃ Sh∞(B⁴⁸) is a topological sheaf layer blind to ℂ and the Bures metric; dynamical physics lives in the strata above.',
    sheafLink: 'Bures site & sheaf scope',
  },
  ru: {
    eyebrow: 'СТРАТИФИЦИРОВАННАЯ ОНТОЛОГИЯ · НОЛЬ ЗАВЫШЕННЫХ ЗАЯВЛЕНИЙ',
    title: 'Три явные страты отделяют внутренние теоремы от внешних мостов.',
    selectLabel: 'Выберите онтологическую страту',
    premises: 'Формальные предпосылки',
    verified: 'Верифицированное ядро',
    boundary: 'Явная граница',
    gateAB: 'Лифт: (Cl₀) + KO-6 + (P)',
    gateBC: 'Стена: Super-F-40 и F-41',
    sheafFootnote: 'Опциональная оболочка: Sh∞(Open_{B}(D₇)) ≃ Sh∞(B⁴⁸) — топологический пучковый слой, не различающий ℂ и метрику Бюреса; динамика и физика живут в стратах выше.',
    sheafLink: 'Сайт Бюреса и границы пучка',
  },
};

export default function StrataExplorer({locale}: {locale: string}) {
  const [active, setActive] = useState<StratumId>('A');
  const lang = locale === 'ru' ? 'ru' : 'en';
  const copy = LABELS[lang];
  const current = STRATA.find((s) => s.id === active) ?? STRATA[0];

  return (
    <div className={styles.wrapper} data-testid="strata-explorer">
      <div className={styles.header}>
        <div>
          <p className={styles.eyebrow}>{copy.eyebrow}</p>
          <h3 className={styles.title}>{copy.title}</h3>
        </div>
        <div className={styles.tabs} role="group" aria-label={copy.selectLabel}>
          {STRATA.map((s) => (
            <button
              key={s.id}
              type="button"
              aria-pressed={active === s.id}
              className={clsx(styles.tab, active === s.id && styles.tabActive)}
              onClick={() => setActive(s.id)}
              data-testid={`stratum-tab-${s.id}`}
            >
              <span>{tr(s.code, lang)}</span>
            </button>
          ))}
        </div>
      </div>

      <div className={styles.grid}>
        <svg viewBox="0 0 360 258" className={styles.diagram} role="img" aria-label={copy.title}>
          <g
            className={clsx(styles.layer, active === 'C' && styles.layerActive)}
            data-stratum="C"
            onClick={() => setActive('C')}
          >
            <rect x="16" y="14" width="328" height="58" rx="10" className={styles.layerBoxC} />
            <text x="32" y="36" className={styles.layerCode}>C</text>
            <text x="58" y="35" className={styles.layerName}>{tr(STRATA[2].shortTitle, lang)}</text>
            <text x="58" y="54" className={styles.layerFormula}>{STRATA[2].formula}</text>
          </g>

          <g className={styles.gate}>
            <line x1="180" y1="76" x2="180" y2="96" className={styles.gateLine} />
            <rect x="92" y="77" width="176" height="18" rx="9" className={styles.gatePill} />
            <text x="180" y="89" textAnchor="middle" className={styles.gateText}>{copy.gateBC}</text>
          </g>

          <g
            className={clsx(styles.layer, active === 'B' && styles.layerActive)}
            data-stratum="B"
            onClick={() => setActive('B')}
          >
            <rect x="16" y="100" width="328" height="58" rx="10" className={styles.layerBoxB} />
            <text x="32" y="122" className={styles.layerCode}>B</text>
            <text x="58" y="121" className={styles.layerName}>{tr(STRATA[1].shortTitle, lang)}</text>
            <text x="58" y="140" className={styles.layerFormula}>{STRATA[1].formula}</text>
          </g>

          <g className={styles.gate}>
            <line x1="180" y1="162" x2="180" y2="182" className={styles.gateLine} />
            <rect x="92" y="163" width="176" height="18" rx="9" className={styles.gatePill} />
            <text x="180" y="175" textAnchor="middle" className={styles.gateText}>{copy.gateAB}</text>
          </g>

          <g
            className={clsx(styles.layer, active === 'A' && styles.layerActive)}
            data-stratum="A"
            onClick={() => setActive('A')}
          >
            <rect x="16" y="186" width="328" height="58" rx="10" className={styles.layerBoxA} />
            <text x="32" y="208" className={styles.layerCode}>A</text>
            <text x="58" y="207" className={styles.layerName}>{tr(STRATA[0].shortTitle, lang)}</text>
            <text x="58" y="226" className={styles.layerFormula}>{STRATA[0].formula}</text>
          </g>
        </svg>

        <div className={styles.detail} data-testid="stratum-detail" aria-live="polite">
          <div className={styles.detailHead}>
            <span className={styles.detailBadge} data-stratum={current.id}>{tr(current.code, lang)}</span>
            <span className={styles.detailTag}>{tr(current.tag, lang)}</span>
          </div>
          <h4>{tr(current.shortTitle, lang)}</h4>
          <dl className={styles.detailList}>
            <div>
              <dt>{copy.premises}</dt>
              <dd><RichText text={tr(current.premises, lang)} /></dd>
            </div>
            <div>
              <dt>{copy.verified}</dt>
              <dd><RichText text={tr(current.verified, lang)} /></dd>
            </div>
            <div className={styles.boundaryRow}>
              <dt>{copy.boundary}</dt>
              <dd><RichText text={tr(current.boundary, lang)} /></dd>
            </div>
          </dl>
          <Link className={styles.detailLink} to={current.link}>
            {tr(current.linkLabel, lang)} →
          </Link>
        </div>
      </div>

      <div className={styles.footnote}>
        <p><RichText text={copy.sheafFootnote} /></p>
        <Link to="/docs/reference/mathematical-kernel#bures-site">{copy.sheafLink} →</Link>
      </div>
    </div>
  );
}
