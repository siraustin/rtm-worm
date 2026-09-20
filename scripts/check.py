#!/usr/bin/env python3
"""Offline structural checks; does not validate the truth or uptime of sources."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re

ROOT = Path(__file__).resolve().parents[1]
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input',
        'link', 'meta', 'param', 'source', 'track', 'wbr'}

class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.links = []
        self.scripts = []
        self.h1 = 0
        self.stack = []
        self.errors = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            if a['id'] in self.ids:
                self.errors.append('Duplicate ID: ' + a['id'])
            self.ids.add(a['id'])
        if tag == 'h1':
            self.h1 += 1
        for key in ('href', 'src'):
            if key in a:
                self.links.append(a[key])
        if tag == 'script':
            self.scripts.append(a.get('src'))
        if tag not in VOID:
            self.stack.append(tag)
    def handle_endtag(self, tag):
        if not self.stack or self.stack[-1] != tag:
            self.errors.append('Unbalanced closing tag: ' + tag)
        else:
            self.stack.pop()

def main():
    text = (ROOT / 'index.html').read_text(encoding='utf-8')
    page = Page()
    page.feed(text)
    page.close()
    errors = page.errors
    if page.stack:
        errors.append('Unclosed tags: ' + ', '.join(page.stack))
    if page.h1 != 1:
        errors.append('Expected exactly one h1')
    if '<html lang="en">' not in text or 'name="viewport"' not in text:
        errors.append('Missing language or viewport metadata')
    for link in page.links:
        u = urlsplit(link)
        if u.scheme:
            if u.scheme != 'https' or not u.netloc:
                errors.append('Unexpected external link: ' + link)
        elif u.netloc:
            errors.append('Protocol-relative URL: ' + link)
        elif u.path:
            target = (ROOT / unquote(u.path)).resolve()
            if not target.is_relative_to(ROOT) or not target.is_file():
                errors.append('Missing or out-of-root local file: ' + link)
        elif u.fragment and unquote(u.fragment) not in page.ids:
            errors.append('Broken fragment: ' + link)
    for key in ['story', 'rate', 'sources', 'trials', 'probability-result',
                'probability-controls', 'reset-trials']:
        if key not in page.ids:
            errors.append('Missing page contract ID: ' + key)
    if page.scripts != ['assets/probability.js']:
        errors.append('Unexpected executable scripts')
    for old in ['Keep rolling.', 'n * 1.7', 'That is the whole disaster.']:
        if old in text:
            errors.append('Obsolete simulation assertion: ' + old)
    js = (ROOT / 'assets/probability.js').read_text(encoding='utf-8')
    if re.search(r'\b(fetch|XMLHttpRequest|WebSocket|eval)\s*\(', js):
        errors.append('Unexpected network or dynamic-code API in probability illustration')
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'PASS: balanced HTML, {len(page.ids)} unique IDs, {len(page.links)} links, '
          'local assets, metadata, widget contract, no obsolete telemetry.')

if __name__ == '__main__':
    main()
