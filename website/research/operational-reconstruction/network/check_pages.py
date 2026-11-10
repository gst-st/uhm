"""Compare new EN/RU proof links, equation tokens and anchors against both published HTML trees."""
from html.parser import HTMLParser
from pathlib import Path
import re

SITE=Path(__file__).resolve().parents[3]
PAGES=('consciousness/foundations/phenomenal-distinction','networks/reference-comparison','proofs/physics/physics-correspondence','core/foundations/operational-processes','physics/overview','networks/three-node-transport','geometry/response-metric','reference/network-results',
       'consciousness/empirical/practice-and-report','networks/cycle-observations','geometry/network-scales','geometry/common-limit',
       'consciousness/empirical/breath-observers','consciousness/empirical/practice-models')

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids=set()
        self.headings=[]
        self.active=None
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        if attrs.get('id'):
            self.ids.add(attrs['id'])
        if tag in ('h1','h2'):
            self.active=[]
    def handle_endtag(self,tag):
        if self.active is not None and tag in ('h1','h2'):
            self.headings.append(''.join(self.active))
            self.active=None
    def handle_data(self,text):
        if self.active is not None:
            self.active.append(text)

def scope(text):
    # Only the one translated prose quantifier is allowed inside these equations.
    text=text.replace(r'\text{для каждого }',r'\text{for every }')
    return (re.findall(r'\{#([^}]+)\}',text),
            re.findall(r'\]\(([^)]+)\)',text),
            re.findall(r'\$\$(.+?)\$\$|(?<!\$)\$([^\n$]+)\$(?!\$)',text,re.S),
            re.findall(r'`([^\n`]+)`',text))

def main():
    for name in PAGES:
        pair=[]
        for locale,docs in [('',SITE/'docs'),('ru',SITE/'i18n/ru/docusaurus-plugin-content-docs/current')]:
            src=(docs/(name+'.md')).read_text()
            spec=scope(src)
            pair.append(spec)
            build=SITE/'build'/locale/'docs'
            html=build/(name+'.html')
            if not html.is_file():
                html=build/name/'index.html'
            view=Page()
            view.feed(html.read_text())
            if not view.headings or not set(spec[0])<=view.ids:
                raise ValueError((html,spec[0],view.headings))
        if pair[0]!=pair[1]:
            raise ValueError('localization differs in mathematics, anchors, links or declaration names: '+name)
        print(name,'EN/RU verified')
if __name__=='__main__':
    main()
