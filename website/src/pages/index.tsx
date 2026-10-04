import type {KeyboardEvent, ReactNode} from 'react';
import {useRef, useState} from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';
import OntologyExplorer from '@site/src/components/OntologyExplorer';
import {DIMENSIONS, cellOf, tr} from '@site/src/data/coherences';
import {homeCopy, framework, bridges, statusGroups, corpus} from '@site/src/data/homepage';
import type {HomeCopyKey, Subject} from '@site/src/data/homepage';
import styles from './index.module.css';

type Text = (key: HomeCopyKey) => string;
type LocalProps = {locale: string; text: Text};

function Arrow({diagonal = false}: {diagonal?: boolean}) {
  return <svg className={styles.arrow} viewBox="0 0 24 24" fill="none" aria-hidden="true">
    <path d={diagonal ? 'M6 18 18 6M6 6h12v12' : 'M4 12h15m-6-6 6 6-6 6'} stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" />
  </svg>;
}

function SectionIntro({number, title, lead, id}: {number: string; title: string; lead?: string; id?: string}) {
  return <div className={styles.sectionIntro}>
    <p className={styles.eyebrow}>{number}</p>
    <Heading as="h2" id={id}>{title}</Heading>
    {lead && <p className={styles.sectionLead}>{lead}</p>}
  </div>;
}

function HomepageHeader({text}: Pick<LocalProps, 'text'>) {
  return <header className={styles.hero}>
    <div className={styles.heroInner}>
      <div className={styles.heroText}>
        <p className={styles.eyebrow}><span className={styles.brandMark} aria-hidden="true">◈</span>{text('name')}</p>
        <Heading as="h1" className={styles.heroTitle}>{text('title')}<br /><span>{text('titleAccent')}</span></Heading>
        <p className={styles.heroIntro}>{text('intro')}</p>
        <p className={styles.heroDescription}>{text('description')}</p>
        <div className={styles.heroActions}>
          <Link className={styles.primaryButton} to="#framework">{text('explore')}<Arrow /></Link>
          <Link className={styles.textLink} to="/docs/reference/mathematical-kernel">{text('kernel')}<Arrow diagonal /></Link>
        </div>
        <nav className={styles.heroReferences} aria-label={text('premises')}>
          <Link to="/docs/reference/premises">{text('premises')}</Link>
          <span aria-hidden="true">/</span>
          <Link to="/docs/reference/status-registry">{text('registry')}</Link>
        </nav>
      </div>
      <div className={styles.heroVisual}>
        <div className={styles.instrumentHeading}><span>{text('interactive')}</span><span aria-hidden="true">Γ ∈ 𝒟₇</span></div>
        <OntologyExplorer />
        <p className={styles.instrumentHint}>{text('interactiveHint')}</p>
      </div>
    </div>
    <div className={styles.factStrip}>
      <p>{text('factNote')}</p>
      {([['7', 'roles'], ['21', 'pairs'], ['48', 'parameters']] as const).map(([value, key]) =>
        <div className={styles.fact} key={key}><strong>{value}</strong><span>{text(key)}</span></div>)}
    </div>
  </header>;
}

function FrameworkSection({locale, text}: LocalProps) {
  return <section className={styles.section} aria-labelledby="framework">
    <div className={styles.container}>
      <SectionIntro id="framework" number={text('frameworkLabel')} title={text('frameworkTitle')} lead={text('frameworkLead')} />
      <div className={styles.frameworkGrid}>
        {framework.map((item, index) => <Link to={item.link} key={item.id} className={styles.frameworkCard}>
          <div className={styles.frameworkTop}><span className={styles.mathSymbol}>{item.symbol}</span><span className={styles.itemNumber}>0{index + 1}</span></div>
          <Heading as="h3">{tr(item.title, locale)}<Arrow diagonal /></Heading>
          <p>{tr(item.text, locale)}</p>
        </Link>)}
      </div>
      <div className={styles.categoricalBand}>
        <div className={styles.sheafMotif} aria-hidden="true">
          <svg viewBox="0 0 180 116"><ellipse cx="62" cy="56" rx="38" ry="36" /><ellipse cx="111" cy="56" rx="38" ry="36" /><ellipse cx="87" cy="68" rx="38" ry="36" /><circle cx="87" cy="57" r="5" /></svg>
          <span>Sh∞(Open(𝒟ₙ))</span>
        </div>
        <div><Heading as="h3">{text('categoricalTitle')}</Heading><p>{text('categoricalText')}</p><Link className={styles.textLink} to="/docs/reference/mathematical-kernel#bures-site">{text('categoricalLink')}<Arrow /></Link></div>
      </div>
    </div>
  </section>;
}

function SemanticMatrix({locale, text}: LocalProps) {
  const [selected, setSelected] = useState<[number, number]>([0, 1]);
  const table = useRef<HTMLTableElement>(null);
  const moveFocus = (event: KeyboardEvent<HTMLButtonElement>, i: number, j: number) => {
    let next: [number, number];
    switch (event.key) {
      case 'ArrowLeft': next = [i, (j + 6) % 7]; break;
      case 'ArrowRight': next = [i, (j + 1) % 7]; break;
      case 'ArrowUp': next = [(i + 6) % 7, j]; break;
      case 'ArrowDown': next = [(i + 1) % 7, j]; break;
      case 'Home': next = [event.ctrlKey ? 0 : i, 0]; break;
      case 'End': next = [event.ctrlKey ? 6 : i, 6]; break;
      default: return;
    }
    event.preventDefault();
    setSelected(next);
    table.current?.querySelector<HTMLButtonElement>(`[data-semantic-cell="${next[0]}-${next[1]}"]`)?.focus();
  };
  const [a, b] = selected;
  const row = DIMENSIONS[a];
  const column = DIMENSIONS[b];
  const cell = cellOf(row, column);
  return <div className={styles.semanticInstrument} data-testid="semantic-matrix">
    <div className={styles.matrixHeader}><span>Γ = Γ†</span><span>Γ ⪰ 0</span><span>Tr Γ = 1</span></div>
    <table ref={table} className={styles.semanticTable} aria-label={text('matrixTable')}>
      <thead><tr><th scope="col"><span aria-hidden="true">Γ</span></th>{DIMENSIONS.map(d => <th scope="col" key={d}>{d}</th>)}</tr></thead>
      <tbody>{DIMENSIONS.map((r, i) => <tr key={r}>
        <th scope="row">{r}</th>
        {DIMENSIONS.map((c, j) => <td key={c}><button type="button"
          className={clsx(styles.semanticCell, i === j && styles.diagonal, a === i && b === j && styles.cellSelected, a === j && b === i && styles.cellConjugate)}
          onClick={() => setSelected([i, j])} onFocus={() => setSelected([i, j])}
          onKeyDown={event => moveFocus(event, i, j)} tabIndex={a === i && b === j ? 0 : -1} data-semantic-cell={`${i}-${j}`}
          aria-pressed={a === i && b === j} aria-controls="coherence-reading"
          aria-label={`γ${r}${c}: ${tr(cellOf(r, c).name, locale)}`}>
          <span aria-hidden="true">γ<sub>{r}{c}</sub></span>
        </button></td>)}
      </tr>)}</tbody>
    </table>
    <div className={styles.cellReading} id="coherence-reading" aria-live="polite" aria-atomic="true">
      <div className={styles.cellReadingTop}><span>{text(cell.diagonal ? 'diagonal' : 'coherence')}</span><span>γ<sub>{row}{column}</sub>{!cell.diagonal && <> = γ̅<sub>{column}{row}</sub></>}</span></div>
      <strong>{tr(cell.name, locale)}</strong><p>{tr(cell.meaning, locale)}</p>
    </div>
    <p className={styles.semanticTag}>{text('interpretation')} · [I]</p>
  </div>;
}

function MatrixSection(props: LocalProps) {
  const {text} = props;
  return <section className={clsx(styles.section, styles.matrixSection)} id="relations">
    <div className={clsx(styles.container, styles.matrixLayout)}>
      <div>
        <SectionIntro number={text('matrixLabel')} title={text('matrixTitle')} lead={text('matrixText')} />
        <p className={styles.matrixHelp}>{text('matrixHelp')}</p>
        <div className={styles.roleKey}>{DIMENSIONS.map(d => <span key={d}><strong>{d}</strong>{tr(cellOf(d, d).name, props.locale)}</span>)}</div>
        <p className={styles.modelNote}>{text('matrixNote')}</p>
        <Link className={styles.textLink} to="/docs/core/dynamics/coherence-matrix">{text('matrixLink')}<Arrow /></Link>
      </div>
      <SemanticMatrix {...props} />
    </div>
  </section>;
}

function BridgesSection({locale, text}: LocalProps) {
  return <section className={styles.section} id="bridges">
    <div className={styles.container}>
      <SectionIntro number={text('bridgesLabel')} title={text('bridgesTitle')} lead={text('bridgesLead')} />
      <div className={styles.bridgesGrid}>{bridges.map(item => <Link className={styles.bridgeCard} to={item.link} key={item.id}>
        <div className={styles.bridgeTop}><span>{item.symbol}</span><Arrow diagonal /></div>
        <Heading as="h3">{tr(item.title, locale)}</Heading><p>{tr(item.text, locale)}</p>
      </Link>)}</div>
    </div>
  </section>;
}

function StatusSection({locale, text}: LocalProps) {
  return <section className={clsx(styles.section, styles.statusSection)} id="results">
    <div className={styles.container}>
      <SectionIntro number={text('statusLabel')} title={text('statusTitle')} lead={text('statusLead')} />
      <div className={styles.statusGrid}>{statusGroups.map(group => <div key={group.id} className={styles.statusColumn}>
        <span className={styles.statusBadge} data-kind={group.id}>{group.badge}</span><Heading as="h3">{tr(group.title, locale)}</Heading>
        <ul>{group.items.map(item => <li key={item.link}><Link to={item.link}>{tr(item.text, locale)}</Link></li>)}</ul>
      </div>)}</div>
      <div className={styles.statusLinks}><Link className={styles.textLink} to="/docs/reference/status-registry">{text('registry')}<Arrow /></Link><Link className={styles.textLink} to="/docs/reference/falsifiability">{text('falsifiability')}<Arrow /></Link></div>
    </div>
  </section>;
}

const subjects: ('all' | Subject)[] = ['all', 'foundations', 'dynamics', 'mind', 'physics', 'research'];
function CorpusSection({locale, text}: LocalProps) {
  const [filter, setFilter] = useState<'all' | Subject>('all');
  const entries = corpus.filter(item => filter === 'all' || item.subject === filter);
  return <section className={styles.section} id="corpus">
    <div className={styles.container}>
      <SectionIntro number={text('corpusLabel')} title={text('corpusTitle')} lead={text('corpusLead')} />
      <div className={styles.filters} role="group" aria-label={text('filters')}>
        {subjects.map(subject => <button type="button" key={subject} aria-pressed={subject === filter} aria-controls="corpus-list" onClick={() => setFilter(subject)} data-testid={`filter-${subject}`}>{text(subject)}</button>)}
      </div>
      <div className={styles.corpusGrid} id="corpus-list" aria-live="polite" aria-relevant="additions text">
        {entries.map(item => <Link key={item.id} to={item.link} className={styles.docCard} data-testid="corpus-card">
          <span className={styles.docSymbol} aria-hidden="true">{item.symbol}</span>
          <div><span className={styles.docCategory}>{text(item.subject)}</span><Heading as="h3">{tr(item.title, locale)}</Heading><p>{tr(item.text, locale)}</p></div>
          <Arrow diagonal />
        </Link>)}
      </div>
      <aside className={styles.readingPath}>
        <div><p className={styles.eyebrow}>{text('readingStart')}</p><Heading as="h2">{text('readingTitle')}</Heading><p>{text('readingText')}</p></div>
        <Link className={styles.primaryButton} to="/docs/intro">{text('introduction')}<Arrow /></Link>
      </aside>
    </div>
  </section>;
}

export default function Home(): ReactNode {
  const {i18n} = useDocusaurusContext();
  const locale = i18n.currentLocale;
  const text: Text = key => tr(homeCopy[key], locale);
  const local = {locale, text};
  return <Layout title={text('metadataTitle')} description={text('metadataDescription')}>
    <main className={styles.home}>
      <HomepageHeader text={text} />
      <FrameworkSection {...local} />
      <MatrixSection {...local} />
      <BridgesSection {...local} />
      <StatusSection {...local} />
      <CorpusSection {...local} />
    </main>
  </Layout>;
}
