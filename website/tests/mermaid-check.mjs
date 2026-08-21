// mermaid-check.mjs — validate every ```mermaid block in docs/ and i18n/
// with the SITE'S OWN mermaid (node_modules/mermaid) via a real browser:
// both parse AND render phases. Exits non-zero on any broken diagram.
//
// Usage:  npm run test:mermaid
// Boxed lesson (2026-08): user reports of "broken diagrams" traced to five
// blocks — an outdated `radar` header (v11 wants radar-beta), typographic
// em-dash edges `A — "x" --- B`, and unquoted Cyrillic quadrantChart axes.
// grep-lint cannot catch these; only the real parser can. Keep this green.
import { chromium } from "playwright-core";
import { readFileSync, readdirSync, statSync } from "fs";
import { join, dirname, relative } from "path";
import { fileURLToPath } from "url";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const MERMAID = join(ROOT, "node_modules/mermaid/dist/mermaid.min.js");

function* mdFiles(dir) {
  for (const name of readdirSync(dir)) {
    const p = join(dir, name);
    const st = statSync(p);
    if (st.isDirectory()) yield* mdFiles(p);
    else if (/\.mdx?$/.test(name)) yield p;
  }
}

const blocks = [];
for (const base of ["docs", "i18n"]) {
  for (const file of mdFiles(join(ROOT, base))) {
    const lines = readFileSync(file, "utf8").split("\n");
    for (let i = 0; i < lines.length; i++) {
      if (lines[i].trim().startsWith("```mermaid")) {
        const start = i + 1;
        let j = start;
        while (j < lines.length && !lines[j].trim().startsWith("```")) j++;
        blocks.push({ file: relative(ROOT, file), line: start + 1, code: lines.slice(start, j).join("\n") });
        i = j;
      }
    }
  }
}

const browser = await chromium.launch({ channel: "chrome" }).catch(() => chromium.launch());
const page = await browser.newPage();
await page.setContent("<html><body></body></html>");
await page.addScriptTag({ path: MERMAID });
await page.evaluate(() => window.mermaid.initialize({ startOnLoad: false, securityLevel: "loose" }));

let bad = 0;
for (let i = 0; i < blocks.length; i++) {
  const b = blocks[i];
  const err = await page.evaluate(async (arg) => {
    try {
      await window.mermaid.parse(arg.code);
      await window.mermaid.render("m" + arg.i, arg.code);
      return null;
    } catch (e) {
      return String((e && e.message) || e);
    }
  }, { code: b.code, i });
  if (err !== null) {
    bad++;
    console.error(`FAIL ${b.file}:${b.line}\n  ${err.split("\n").slice(0, 3).join("\n  ")}`);
  }
}
await browser.close();
console.log(`mermaid-check: ${blocks.length} blocks, ${bad} broken`);
process.exit(bad === 0 ? 0 : 1);
