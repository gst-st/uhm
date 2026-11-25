import type {ReactNode} from 'react';
import {Fragment} from 'react';

const TOKEN_RE = /(_\{[^}]+\}|\^\{[^}]+\})/g;

/**
 * Lightweight zero-dependency typographic renderer for explicit `_{sub}` and `^{sup}`
 * markers in UI copy, producing real HTML `<sub>` and `<sup>` elements without raw underscores.
 */
export default function RichText({text}: {text: string}): ReactNode {
  const parts = text.split(TOKEN_RE);
  if (parts.length === 1) return text;
  return parts.map((part, idx) => {
    if (part.startsWith('_{') && part.endsWith('}')) {
      return <sub key={idx}>{part.slice(2, -1)}</sub>;
    }
    if (part.startsWith('^{') && part.endsWith('}')) {
      return <sup key={idx}>{part.slice(2, -1)}</sup>;
    }
    return <Fragment key={idx}>{part}</Fragment>;
  });
}
