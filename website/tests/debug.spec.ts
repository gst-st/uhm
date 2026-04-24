import { test, expect } from '@playwright/test';

const BASE_URL = 'http://localhost:3000';

test.describe('UHM Site Debug', () => {
  test('homepage loads correctly', async ({ page }) => {
    const errors: string[] = [];
    page.on('console', msg => {
      if (msg.type() === 'error') {
        errors.push(msg.text());
      }
    });
    page.on('pageerror', err => {
      errors.push(err.message);
    });

    await page.goto(BASE_URL);
    await page.waitForLoadState('networkidle');

    // Check title
    await expect(page).toHaveTitle(/UHM/);

    // Check logo is visible
    const logo = page.locator('nav img[alt="UHM Logo"]');
    await expect(logo).toBeVisible();

    // Check hero section
    const heroTitle = page.locator('h1.hero__title');
    await expect(heroTitle).toBeVisible();

    // Take screenshot
    await page.screenshot({ path: 'tests/screenshots/homepage.png', fullPage: true });

    // Report errors
    if (errors.length > 0) {
      console.log('Console errors:', errors);
    }
    expect(errors.filter(e => !e.includes('DevTools'))).toHaveLength(0);
  });

  test('docs intro page loads', async ({ page }) => {
    const errors: string[] = [];
    page.on('pageerror', err => errors.push(err.message));

    await page.goto(`${BASE_URL}/docs/intro`);
    await page.waitForLoadState('networkidle');

    // Check mermaid diagrams render
    const mermaidDiagram = page.locator('.mermaid svg, pre.mermaid');

    await page.screenshot({ path: 'tests/screenshots/intro.png', fullPage: true });

    // Check for parse errors in page
    const pageContent = await page.content();
    const hasParseError = pageContent.includes('Parse error') || pageContent.includes('Syntax error');

    if (hasParseError) {
      console.log('Found parse error on intro page');
    }

    expect(hasParseError).toBeFalsy();
  });

  test('all main sections accessible', async ({ page }) => {
    const sections = [
      '/docs/intro',
      '/docs/core/foundations/axiom-omega',
      '/docs/core/structure/holon',
      '/docs/core/dynamics/evolution',
      '/docs/core/consciousness/qualia',
      '/docs/applied/coherence-cybernetics/axiomatics',
      '/docs/reference/glossary',
    ];

    for (const section of sections) {
      const response = await page.goto(`${BASE_URL}${section}`);
      expect(response?.status()).toBe(200);

      // Check no 404 content
      const content = await page.textContent('body');
      expect(content).not.toContain('Page Not Found');
    }
  });

  test('mermaid diagrams in dynamics pages', async ({ page }) => {
    await page.goto(`${BASE_URL}/docs/core/dynamics/evolution`);
    await page.waitForLoadState('networkidle');

    await page.screenshot({ path: 'tests/screenshots/evolution.png', fullPage: true });

    const pageContent = await page.content();
    expect(pageContent).not.toContain('Parse error');
  });
});
