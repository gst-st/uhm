// «Битые картинки в названиях» (28.07): 1045 заголовков корпуса несут
// математику. Тело страницы рендерит rehype-katex, но НАВИГАЦИЯ (правый
// TOC, крошки, сайдбар, пагинация) получает от mdx сырой LaTeX БЕЗ
// долларов («H_{eff}», «\mathcal{R}») — auto-render тут слеп, а гонку с
// гидрацией React (#418) выигрывает только MutationObserver. Поэтому:
// точечный художник — в текстовых узлах навигации находим латех-фрагменты
// (\команда{…}, X_{…}, X^{…}) и рендерим каждый куском KaTeX; остальной
// текст не трогаем. Ошибка рендера куска оставляет текст как был.
import katex from 'katex';

// \команда с ≤1 уровнем вложенных скобок · подстрочник/надстрочник с ≤1
// уровнем ({\text{…}} внутри) · греческие/латинские базы
const TAIL = String.raw`(?:\{(?:[^{}]|\{[^{}]*\})*\}|_\{(?:[^{}]|\{[^{}]*\})*\}|\^\{(?:[^{}]|\{[^{}]*\})*\}|_[A-Za-z0-9]|\^[A-Za-z0-9])`;
const FRAG = new RegExp(
  // \команда с любыми хвостами (включая голую \Lambda и \Lambda_{obs})
  String.raw`\\[a-zA-Z]+` + TAIL + '*' + '|' +
  // буквенная база с обязательным хвостом (H_{eff}, T_meta, x^2)
  String.raw`[A-Za-zΓΦΛΣΩΨγφλσρπμΔδ][A-Za-z0-9]*` + TAIL + '+',
  'g');

const SELECTORS = [
  '.table-of-contents',
  '.breadcrumbs',
  '.menu__list',
  '.pagination-nav',
];

let painting = false;

function paintTextNode(node) {
  const text = node.nodeValue;
  FRAG.lastIndex = 0;
  if (!FRAG.test(text)) return;
  FRAG.lastIndex = 0;
  const frag = document.createDocumentFragment();
  let last = 0;
  let m;
  while ((m = FRAG.exec(text)) !== null) {
    if (m.index > last) {
      frag.appendChild(document.createTextNode(text.slice(last, m.index)));
    }
    const span = document.createElement('span');
    try {
      katex.render(m[0], span, {throwOnError: true});
      frag.appendChild(span);
    } catch (e) {
      frag.appendChild(document.createTextNode(m[0]));
    }
    last = m.index + m[0].length;
  }
  if (last < text.length) {
    frag.appendChild(document.createTextNode(text.slice(last)));
  }
  node.parentNode.replaceChild(frag, node);
}

function paint() {
  if (painting) return;
  painting = true;
  try {
    for (const sel of SELECTORS) {
      for (const el of document.querySelectorAll(sel)) {
        const walker = document.createTreeWalker(
          el, NodeFilter.SHOW_TEXT, {
            acceptNode: (n) =>
              n.parentElement && n.parentElement.closest('.katex') ?
                NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT,
          });
        const nodes = [];
        while (walker.nextNode()) nodes.push(walker.currentNode);
        for (const n of nodes) paintTextNode(n);
      }
    }
  } finally {
    setTimeout(() => { painting = false; }, 0);
  }
}

if (typeof window !== 'undefined') {
  const observer = new MutationObserver(() => {
    if (!painting) paint();
  });
  const arm = () => {
    observer.observe(document.body, {childList: true, subtree: true});
    paint();
  };
  if (document.readyState === 'complete') arm();
  else window.addEventListener('load', arm);
}

export function onRouteDidUpdate() {
  setTimeout(paint, 50);
  setTimeout(paint, 600);
}
