"""embed_fonts.py: make a page work offline by inlining the Google Fonts it links to.

Finds the page's Google Fonts <link> (and any @import of fonts.googleapis.com), downloads the font files, and puts
them inside the page as data: URLs, so it opens with no internet. The preconnect links are removed. Only the
character sets in KEEP_SUBSETS are kept, which keeps the file small; add 'cyrillic', 'greek', 'vietnamese' ... if
the page needs them. Google Fonts' families are open-licensed (most under the SIL Open Font License); note each
family's license in the piece's sources or credits.
Run it in Thonny with the Run button after setting HTML_IN and HTML_OUT. Needs internet once, while it runs.
"""
import base64, os, re, sys, urllib.request

# ===================== SETTINGS =====================
HTML_IN = ''                               # the page to fix, e.g. '/Users/you/Desktop/my-infographic.html'
HTML_OUT = ''                              # where to save the offline copy ('' = next to it, ending -offline.html)
KEEP_SUBSETS = ['latin', 'latin-ext']      # Google's character sets to keep
USER_AGENT = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
              'Chrome/120.0 Safari/537.36')   # a modern browser, so Google serves small woff2 files
# ====================================================

CSS_LINK = re.compile(r'<link\b[^>]*\bhref\s*=\s*["\'](https://fonts\.googleapis\.com/css2?\?[^"\']+)["\'][^>]*>', re.I)
CSS_IMPORT = re.compile(r'@import\s+(?:url\()?\s*["\']?(https://fonts\.googleapis\.com/css2?\?[^"\')\s]+)["\']?\)?\s*;', re.I)
PRECONNECT = re.compile(r'<link\b[^>]*\brel\s*=\s*["\'](?:preconnect|dns-prefetch)["\'][^>]*\bhref\s*=\s*["\']https://fonts\.(?:googleapis|gstatic)\.com[^>]*>\s*'
                        r'|<link\b[^>]*\bhref\s*=\s*["\']https://fonts\.(?:googleapis|gstatic)\.com/?["\'][^>]*\brel\s*=\s*["\'](?:preconnect|dns-prefetch)["\'][^>]*>\s*', re.I)
BLOCK = re.compile(r'(?:/\*\s*([\w-]+)\s*\*/\s*)?(@font-face\s*\{[^}]*\})', re.S)
FONT_URL = re.compile(r'url\((https://fonts\.gstatic\.com/[^)]+)\)')


def get(url):
    req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def inline_css(css_url, cache):
    css = get(css_url.replace('&amp;', '&')).decode('utf-8')
    out, kept, dropped = [], 0, 0
    for subset, block in BLOCK.findall(css):
        if subset and KEEP_SUBSETS and subset not in KEEP_SUBSETS:
            dropped += 1
            continue
        def data_url(m):
            u = m.group(1)
            if u not in cache:
                kind = 'woff2' if u.endswith('.woff2') else ('woff' if u.endswith('.woff') else 'ttf')
                mime = {'woff2': 'font/woff2', 'woff': 'font/woff', 'ttf': 'font/ttf'}[kind]
                cache[u] = 'url(data:%s;base64,%s)' % (mime, base64.b64encode(get(u)).decode('ascii'))
            return cache[u]
        out.append(('/* %s */\n' % subset if subset else '') + FONT_URL.sub(data_url, block))
        kept += 1
    return '\n'.join(out), kept, dropped


def main():
    if not HTML_IN:
        sys.exit('Set HTML_IN (and optionally HTML_OUT) in the SETTINGS block at the top, then run again.')
    out_path = HTML_OUT or re.sub(r'\.html?$', '', HTML_IN) + '-offline.html'
    with open(HTML_IN, encoding='utf-8') as fh:
        html = fh.read()
    cache = {}
    found = CSS_LINK.findall(html) + CSS_IMPORT.findall(html)
    if not found:
        print('No Google Fonts links found; nothing to do.')
        return True
    for regex in (CSS_LINK, CSS_IMPORT):
        def repl(m):
            css, kept, dropped = inline_css(m.group(1), cache)
            print(f'  {m.group(1)[:90]}... -> {kept} font face(s) inlined, {dropped} other character set(s) left out')
            block = '/* Fonts from Google Fonts, inlined by tools/embed_fonts.py (open licenses) */\n' + css
            return block if regex is CSS_IMPORT else '<style>\n' + block + '\n</style>'
        html = regex.sub(repl, html)
    html = PRECONNECT.sub('', html)
    with open(out_path, 'w', encoding='utf-8') as fh:
        fh.write(html)
    size = os.path.getsize(out_path) / 1e6
    print(f'Saved {out_path} ({size:.2f} MB, {len(cache)} font file(s) inside).')
    leftover = re.findall(r'https://fonts\.(?:googleapis|gstatic)\.com', html)
    if leftover:
        print(f'Warning: {len(leftover)} Google Fonts address(es) still in the page; check it by hand.')
    return True


if __name__ == '__main__':
    main()
