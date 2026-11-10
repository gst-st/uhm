"""Keep explicit edition logs and archival panels out of both published corpora.

Domain history, counterexamples and negative results are scientific material.
Only unambiguous edition-log constructs are rejected here; a status tag is
not itself an archive. Semantic claims are checked by the status kernel and proofs.
"""
from pathlib import Path
import re
import sys

SITE = Path(__file__).resolve().parents[1]
ROOTS = (SITE/'docs', SITE/'i18n/ru/docusaurus-plugin-content-docs/current')
EDITION = re.compile(
    r'<summary>\s*(?:historical (?:calculations|model)|archived (?:model|calculation)|'
    r'исторические (?:расч[её]ты|выкладки)|архивн(?:ая модель|ые расч[её]ты))'
    r'|^#{1,6}\s+(?:Historical links|Исторические ссылки)\s*$'
    r'|^\*{1,2}(?:Status history|История статуса):\*'
    r'|\b(?:an earlier version of this|в ранних версиях корпуса)\b', re.I)
errors = []
pages = 0
for root in ROOTS:
    for path in sorted(root.rglob('*')):
        if path.suffix not in ('.md', '.mdx'):
            continue
        pages += 1
        for n, line in enumerate(path.read_text().splitlines(), 1):
            if EDITION.search(line):
                errors.append(f'{path.relative_to(SITE)}:{n}: edition history belongs in Git')
if errors:
    sys.exit('\n'.join(errors))
print(f'{pages} canon pages: no explicit archive panels or edition-log headings')
