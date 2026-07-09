import type {ReactNode} from 'react';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import {COHERENCES, DIAGONAL, tr, type Cell} from '@site/src/data/coherences';

/**
 * Renders the canonical coherence-name table from the single source of truth
 * (src/data/coherences.ts). Used in the corpus so that the corpus and the
 * homepage can never drift apart on names/meanings.
 *
 * Props:
 *   - kind: 'coherences' (21 off-diagonal, default) | 'dimensions' (7 diagonal)
 */
export default function CoherenceTable({
  kind = 'coherences',
}: {
  kind?: 'coherences' | 'dimensions';
}): ReactNode {
  const {i18n} = useDocusaurusContext();
  const locale = i18n.currentLocale;
  const isRu = locale === 'ru';

  const rows: Cell[] = kind === 'dimensions' ? DIAGONAL : COHERENCES;
  const symbolHeader = isRu
    ? kind === 'dimensions'
      ? 'Измерение'
      : 'Когерентность'
    : kind === 'dimensions'
      ? 'Dimension'
      : 'Coherence';
  const nameHeader = isRu ? 'Название' : 'Name';
  const meaningHeader = isRu ? 'Фундаментальный смысл' : 'Fundamental meaning';

  return (
    <table>
      <thead>
        <tr>
          <th>{symbolHeader}</th>
          <th>{nameHeader}</th>
          <th>{meaningHeader}</th>
        </tr>
      </thead>
      <tbody>
        {rows.map((c) => (
          <tr key={c.key}>
            <td>
              <span className="math math-inline">
                γ<sub>{c.i}{c.j}</sub>
              </span>
            </td>
            <td>
              <strong>{tr(c.name, locale)}</strong>
            </td>
            <td>{tr(c.meaning, locale)}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
