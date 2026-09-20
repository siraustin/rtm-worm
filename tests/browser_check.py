#!/usr/bin/env python3
"""Optional offline rendering checks. Requires Playwright and Chromium.

Run: python3 tests/browser_check.py
Uses RTM_CHROMIUM_PATH, a system Chromium, or Playwright's bundled browser.
No network navigation: this checks DOM/layout, not HTTP delivery or deployment.
"""
import os
import shutil
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / 'index.html').read_text(encoding='utf-8').replace(
    '<link rel="stylesheet" href="assets/site.css">',
    '<style>' + (ROOT / 'assets/site.css').read_text(encoding='utf-8') + '</style>'
).replace('<script src="assets/probability.js" defer></script>', '')

def load(page, js=True):
    page.set_content(HTML, wait_until='load')
    if js:
        page.add_script_tag(content=(ROOT / 'assets/probability.js').read_text(encoding='utf-8'))

def main():
    executable = os.environ.get('RTM_CHROMIUM_PATH') or shutil.which('chromium')
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=executable, headless=True)
        try:
            for width, height in [(1440, 1000), (390, 844)]:
                context = browser.new_context(viewport={'width': width, 'height': height})
                page = context.new_page()
                errors = []
                page.on('pageerror', lambda error: errors.append(str(error)))
                load(page)
                assert page.locator('#probability-controls').is_visible()
                assert '66.0%' in page.locator('#probability-result').inner_text()
                assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
                page.locator('#trials').fill('100')
                assert '>99.9%' in page.locator('#probability-result').inner_text()
                page.locator('#reset-trials').click()
                assert '0.0%' in page.locator('#probability-result').inner_text()
                page.locator('summary').click()
                assert page.locator('details').get_attribute('open') is not None
                assert not errors, errors
                context.close()
                print(f'PASS: {width}x{height} layout, widget, reset, disclosure, no script errors')
            context = browser.new_context(java_script_enabled=False)
            page = context.new_page()
            load(page, js=False)
            assert page.locator('#probability-controls').is_hidden()
            assert page.locator('#s18').is_visible()
            assert 'Seven trials' in page.locator('.interactive').inner_text()
            context.close()
            context = browser.new_context(reduced_motion='reduce')
            page = context.new_page()
            load(page)
            assert page.evaluate('getComputedStyle(document.documentElement).scrollBehavior') == 'auto'
            page.emulate_media(media='print')
            assert page.locator('#probability-controls').is_hidden()
            context.close()
            print('PASS: no-JavaScript reading, reduced motion, print-control hiding')
        finally:
            browser.close()

if __name__ == '__main__':
    main()
