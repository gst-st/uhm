import { chromium } from '@playwright/test';

async function captureScreenshots() {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });

  // Start serve in background
  console.log('Navigating to http://localhost:3000...');

  try {
    await page.goto('http://localhost:3000', { waitUntil: 'networkidle', timeout: 30000 });

    // Check for errors
    const content = await page.content();
    if (content.includes('Page Not Found')) {
      console.error('ERROR: Page Not Found');
    }

    // Screenshot homepage
    await page.screenshot({ path: 'tests/screenshots/homepage-new.png', fullPage: true });
    console.log('Saved: tests/screenshots/homepage-new.png');

    // Check intro page
    await page.goto('http://localhost:3000/docs/intro', { waitUntil: 'networkidle' });
    await page.screenshot({ path: 'tests/screenshots/intro-new.png', fullPage: true });
    console.log('Saved: tests/screenshots/intro-new.png');

    // Check for parse errors
    const introContent = await page.content();
    if (introContent.includes('Parse error')) {
      console.error('ERROR: Parse error found on intro page');
    } else {
      console.log('No parse errors on intro page');
    }

  } catch (error) {
    console.error('Error:', error instanceof Error ? error.message : String(error));
  }

  await browser.close();
}

captureScreenshots();
