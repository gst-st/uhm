// Test the built EN/RU homepages with a real browser, including keyboard use.
// Run `npm run build` first. Optionally set HOMEPAGE_BROWSER_PATH to Chromium.
import assert from 'node:assert/strict';
import {createServer} from 'node:http';
import {readFile, stat, mkdir} from 'node:fs/promises';
import {resolve, dirname, extname, sep, join} from 'node:path';
import {fileURLToPath} from 'node:url';
import {chromium} from 'playwright-core';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '../build');
const types = {'.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json', '.svg': 'image/svg+xml', '.png': 'image/png', '.woff2': 'font/woff2', '.woff': 'font/woff', '.ttf': 'font/ttf', '.ico': 'image/x-icon'};
const screenshots = process.env.HOMEPAGE_SCREENSHOTS;
if (screenshots) await mkdir(screenshots, {recursive: true});
const server = createServer(async (req, res) => {
  try {
    const route = decodeURIComponent(new URL(req.url, 'http://localhost').pathname);
    let file = resolve(root, '.' + route);
    if (file !== root && !file.startsWith(root + sep)) {res.writeHead(403).end(); return;}
    if ((await stat(file).catch(() => null))?.isDirectory()) file = join(file, 'index.html');
    else if (!extname(file)) file += '.html';
    res.writeHead(200, {'content-type': types[extname(file)] || 'application/octet-stream'}).end(await readFile(file));
  } catch {res.writeHead(404).end();}
});
await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
let browser;
try {
  browser = process.env.HOMEPAGE_BROWSER_PATH
    ? await chromium.launch({executablePath: process.env.HOMEPAGE_BROWSER_PATH})
    : await chromium.launch({channel: 'chrome'}).catch(() => chromium.launch());
  const base = `http://127.0.0.1:${server.address().port}`;
  for (const locale of ['en', 'ru']) {
    for (const scenario of [
      {name: 'desktop-light', width: 1440, height: 1050, theme: 'light'},
      {name: 'desktop-dark', width: 1440, height: 1050, theme: 'dark'},
      {name: 'mobile-light', width: 390, height: 844, theme: 'light'},
      {name: 'narrow-dark', width: 320, height: 740, theme: 'dark'},
    ]) {
      const page = await browser.newPage({viewport: {width: scenario.width, height: scenario.height}, reducedMotion: 'reduce'});
      await page.addInitScript(theme => localStorage.setItem('theme', theme), scenario.theme);
      const errors = [];
      page.on('pageerror', error => errors.push(error.message));
      await page.goto(base + (locale === 'ru' ? '/ru/' : '/'), {waitUntil: 'networkidle'});
      const hero = page.getByTestId('ontology-explorer');
      await hero.waitFor();
      assert.match(await page.locator('main h1').innerText(), locale === 'ru' ? /От отношений/ : /From relations/);
      assert.equal(await page.locator('main h1').count(), 1);
      const headlineSize = await page.locator('main h1').evaluate(el => parseFloat(getComputedStyle(el).fontSize));
      assert(headlineSize >= (scenario.width >= 1000 ? 48 : 32), `Global CSS collapsed the hero typography: ${headlineSize}px`);
      assert.equal(await page.locator('html').getAttribute('data-theme'), scenario.theme);
      assert.equal(await page.getByTestId('corpus-card').count(), 12);
      assert.equal(await page.getByTestId('ontology-stage').getAttribute('data-animating'), 'false');
      assert.equal(await page.getByTestId('ontology-motion').isDisabled(), true);
      const metrics = async () => Promise.all(['purity', 'integration', 'reflection'].map(async key => Number((await page.getByTestId(`ontology-${key}`).innerText()).replace(',', '.'))));
      assert.deepEqual(await metrics(), [.357, 1.5, .4]);
      const layout = await page.evaluate(() => ({width: innerWidth, body: document.body.scrollWidth, root: document.documentElement.scrollWidth}));
      assert(layout.body <= layout.width + 1 && layout.root <= layout.width + 1, `Horizontal overflow: ${JSON.stringify(layout)}`);
      const links = await page.locator('main a[href]').evaluateAll(nodes => nodes.map(n => n.getAttribute('href')));
      assert(links.filter(link => link.includes('/docs/')).every(link => locale === 'ru' ? link.startsWith('/ru/docs/') : link.startsWith('/docs/')), `Wrong locale in links: ${locale}`);
      if (screenshots) {
        await page.screenshot({path: join(screenshots, `${locale}-${scenario.name}.png`), fullPage: true});
        await page.screenshot({path: join(screenshots, `${locale}-${scenario.name}-viewport.png`)});
        await hero.screenshot({style: ".navbar { visibility: hidden !important; }", path: join(screenshots, `${locale}-${scenario.name}-instrument.png`)});
      }
      // Exact endpoint states via native keyboard interaction with the slider.
      const slider = page.getByTestId('ontology-slider');
      await slider.focus(); await slider.press('End');
      assert.deepEqual(await metrics(), [1, 6, .143]);
      await slider.press('Home');
      assert.deepEqual(await metrics(), [.143, 0, 1]);
      // A real and an imaginary coherence produce distinct valid readouts.
      await slider.press('End');
      await page.getByTestId('ontology-view-readout').click();
      assert.equal(await page.getByTestId('ontology-readout-plus').getAttribute('aria-live'), 'off');
      const probability = async key => Number((await page.getByTestId(`ontology-readout-${key}`).innerText()).replace(',', '.'));
      const total = (await probability('plus')) + (await probability('minus')) + (await probability('rest'));
      assert(Math.abs(total - 1) < .002, `Readout probabilities sum to ${total}`);
      const realProbability = await probability('plus');
      await page.getByTestId('ontology-readout-imaginary').click();
      assert(Math.abs((await probability('plus')) - realProbability) > .01, 'Changing the measurement setting must change this phase-sensitive readout');
      if (screenshots && scenario.name === 'desktop-light') await hero.screenshot({style: ".navbar { visibility: hidden !important; }", path: join(screenshots, `${locale}-readout.png`)});
      await slider.focus(); await slider.press('Home');
      await page.getByTestId('ontology-view-matrix').click();
      const entry = page.getByTestId('ontology-entry');
      assert.match(await entry.innerText(), /0[.,]000/);
      const matrixFocus = hero.locator('[data-cell="0-1"]');
      const cellBounds = await matrixFocus.locator('rect').first().boundingBox();
      assert(cellBounds.width >= 24 && cellBounds.height >= 24, 'Matrix cells must stay usable on narrow screens');
      await matrixFocus.focus(); await matrixFocus.press('ArrowDown');
      assert.equal(await hero.locator('[data-cell="1-1"]').getAttribute('aria-pressed'), 'true');
      await page.getByTestId('ontology-view-fano').click();
      assert.equal(await page.getByTestId('ontology-stage').getAttribute('data-view'), 'fano');
      if (screenshots && scenario.name === 'desktop-light') await hero.screenshot({style: ".navbar { visibility: hidden !important; }", path: join(screenshots, `${locale}-fano.png`)});
      assert.equal(await hero.locator('[role="group"] button').count() > 7, true);
      const semantics = page.getByTestId('semantic-matrix');
      assert.equal(await semantics.locator('button[tabindex="0"]').count(), 1);
      const semanticSelected = semantics.locator('button[tabindex="0"]');
      await semanticSelected.focus(); await semanticSelected.press('ArrowDown');
      assert.equal(await semantics.locator('[data-semantic-cell="1-1"]').getAttribute('aria-pressed'), 'true');
      await page.keyboard.press('Tab');
      assert.equal(await semantics.evaluate(el => el.contains(document.activeElement)), false);
      await page.getByTestId('filter-physics').click();
      assert.equal(await page.getByTestId('corpus-card').count(), 1);
      await page.getByTestId('filter-all').click();
      assert.equal(await page.getByTestId('corpus-card').count(), 12);
      // A changed OS preference starts/stops motion; explicit pause survives it.
      await page.getByTestId('ontology-view-relations').click();
      await hero.scrollIntoViewIfNeeded();
      await page.emulateMedia({reducedMotion: 'no-preference'});
      await page.waitForFunction(() => document.querySelector('[data-testid="ontology-stage"]')?.dataset.animating === 'true');
      await page.getByTestId('ontology-motion').click();
      assert.equal(await page.getByTestId('ontology-stage').getAttribute('data-animating'), 'false');
      await page.emulateMedia({reducedMotion: 'reduce'});
      assert.deepEqual(errors, [], `${locale}/${scenario.name}: browser errors`);
      console.log(`PASS ${locale}/${scenario.name}: layout, locale, invariants, views, keyboard, filters, reduced motion`);
      await page.close();
    }
  }
} finally {
  if (browser) await browser.close();
  await new Promise(resolve => server.close(resolve));
}
