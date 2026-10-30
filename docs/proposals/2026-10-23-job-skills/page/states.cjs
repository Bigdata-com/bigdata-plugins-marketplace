const { chromium } = require('/Users/mkangrga/.nvm/versions/node/v22.14.0/lib/node_modules/@playwright/cli/node_modules/playwright');
(async () => {
  const b = await chromium.launch(); const file = process.argv[2].indexOf('http') === 0 ? process.argv[2] : 'file://' + process.argv[2], out = process.argv[3];
  let p = await b.newPage({ viewport: { width: 1440, height: 1000 } });
  await p.goto(file); await p.waitForTimeout(1200);
  await p.screenshot({ path: out + '/desktop-top.png' });
  // table row open
  await p.$('#skills-table tbody tr.k-row:nth-child(5)').then(r => r.scrollIntoViewIfNeeded()); await p.click('#skills-table tbody tr.k-row:nth-child(5)', { force: true }); await p.waitForTimeout(300);
  const row = await p.$('#skills-table tbody tr.k-row:nth-child(5)'); await row.scrollIntoViewIfNeeded(); await p.waitForTimeout(200);
  await p.screenshot({ path: out + '/desktop-row-open.png' });
  // filter
  await p.fill('#skills-table-filter', 'earnings'); await p.waitForTimeout(300); await p.screenshot({ path: out + '/desktop-filtered.png' }); await p.fill('#skills-table-filter', '');
  // a built skill fold open

  // a spec fold open
  
  // file browser: open a skill via the tree and screenshot it
  p.on('response', r => { if (r.status() === 404) console.log('404:', r.url()); });
  await p.evaluate(() => document.querySelectorAll('#fb-tree .fb-dir').forEach(e => e.classList.remove('closed')));
  const fbSec = await p.$('#browse'); await fbSec.scrollIntoViewIfNeeded(); await p.waitForTimeout(1200); await fbSec.screenshot({ path: out + '/desktop-browser-default.png' });
  await p.click('#fb-tree a[data-path="skills/bigdata-stock-move/SKILL.md"]', { force: true }); await p.waitForTimeout(1200); await fbSec.screenshot({ path: out + '/desktop-browser-skill.png' });
  await p.click('#fb-tree a[data-path="skills/bigdata-stock-move/references/after-a-price-move.md"]', { force: true }); await p.waitForTimeout(1200); await fbSec.screenshot({ path: out + '/desktop-browser-reference.png' });
  await p.fill('#fb-filter', 'openai'); await p.waitForTimeout(400); await fbSec.screenshot({ path: out + '/desktop-browser-filter.png' }); await p.fill('#fb-filter', '');
  // results section
  const rs = await p.$('#results'); await rs.scrollIntoViewIfNeeded(); await p.waitForTimeout(300); await rs.screenshot({ path: out + '/desktop-results.png' });
  // search open
  await p.keyboard.press('Meta+K'); await p.waitForTimeout(200); await p.keyboard.type('packag'); await p.waitForTimeout(300); await p.screenshot({ path: out + '/desktop-search.png' }); await p.keyboard.press('Escape');
  // tooltip
  const term = await p.$('.term'); if (term) { await term.scrollIntoViewIfNeeded(); await term.hover(); await p.waitForTimeout(400); await p.screenshot({ path: out + '/desktop-tooltip.png' }); }
  // overflow with folds open at 1440
  const w1 = await p.evaluate(() => { document.querySelectorAll('details').forEach(e => e.open = true); return document.documentElement.scrollWidth; });
  console.log('scrollWidth 1440 all folds open:', w1);
  await p.close();
  p = await b.newPage({ viewport: { width: 400, height: 860 } });
  await p.goto(file); await p.waitForTimeout(1200);
  await p.screenshot({ path: out + '/phone-top.png' });
  const t = await p.$('#skills-list details:nth-of-type(5)'); await t.evaluate(e => e.open = true); await t.scrollIntoViewIfNeeded(); await p.waitForTimeout(300); await p.screenshot({ path: out + '/phone-table-row.png' });
  const w2 = await p.evaluate(() => { document.querySelectorAll('details').forEach(e => e.open = true); return document.documentElement.scrollWidth; });
  console.log('scrollWidth 400 all folds open:', w2);
  const fbm = await p.$('#browse'); await fbm.scrollIntoViewIfNeeded(); await p.evaluate(() => document.querySelectorAll('#fb-tree .fb-dir').forEach(e => e.classList.remove('closed'))); await p.click('#fb-tree a[data-path="skills/bigdata-quick-take/SKILL.md"]', { force: true }); await p.waitForTimeout(1200); await p.screenshot({ path: out + '/phone-browser.png' });

  await b.close();
})();
