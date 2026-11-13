// node shoot.cjs <dir-with-html> <out-dir>
const { chromium } = require(process.env.PLAYWRIGHT || 'playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const [src, out] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage({ deviceScaleFactor: 1.5, viewport: { width: 1200, height: 440 } });
  for (const f of fs.readdirSync(src).filter(f => f.endsWith('.html'))) {
    await page.goto('file://' + path.resolve(src, f));
    await page.evaluate(() => document.fonts.ready);
    const box = await page.evaluate(() => ({ w: document.body.offsetWidth, h: document.body.offsetHeight }));
    await page.setViewportSize({ width: box.w, height: box.h });
    const name = f.replace('.html', '.png');
    await page.screenshot({ path: path.join(out, name), clip: { x: 0, y: 0, width: box.w, height: box.h } });
    console.log(name, box);
  }
  await browser.close();
})();
