"""add_view_counter.py: puts the invisible GoatCounter view counter into published pieces.

The counter shows nothing on the page. When someone opens a piece on the live site, it sends one tiny "page viewed"
ping to Bryan's private dashboard (https://bpmdata.goatcounter.com): no cookies, no banner, nothing loaded in.
GoatCounter's own count.js is NOT loaded from their server; this is a few inlined lines that send the same ping, so
the page itself stays fully offline. Opened from a file, from localhost, or with trackers blocked, it does nothing
and the page works the same.
Safe to run again: pages that already have the counter are skipped. check_offline.py knows about this ping.
Run it in Thonny with the Run button.
"""
import glob, os

# ===================== SETTINGS =====================
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # the repo root (this script sits in tools/)
PAGES = [os.path.join(ROOT, 'pieces', '*.html')]                     # files or glob patterns to add the counter to
COUNT_URL = 'https://bpmdata.goatcounter.com/count'                  # your GoatCounter "count" address
# ====================================================

MARKER = 'proofer-view-counter'
SNIPPET = f'''<!-- {MARKER}: invisible GoatCounter view count (no cookies, nothing shown; skipped offline). tools/add_view_counter.py -->
<script>
(function () {{
  try {{
    var l = location;
    if (!/^https?:$/.test(l.protocol) || /^(localhost|127\\.|\\[::1\\]|.*\\.localhost$)/.test(l.hostname)) return;
    var e = encodeURIComponent;
    new Image().src = '{COUNT_URL}?p=' + e(l.pathname) + '&t=' + e(document.title) +
      '&r=' + e(document.referrer) + '&s=' + e(screen.width) + '&rnd=' + Math.random().toString(36).slice(2);
  }} catch (err) {{}}
}})();
</script>
'''


def add(path):
    with open(path, encoding='utf-8') as fh:
        text = fh.read()
    if MARKER in text:
        return 'already has it'
    i = text.lower().rfind('</body>')
    if i < 0:
        return 'NO </body> FOUND, skipped'
    with open(path, 'w', encoding='utf-8') as fh:
        fh.write(text[:i] + SNIPPET + text[i:])
    return 'counter added'


def main():
    files = sorted({f for pat in PAGES for f in glob.glob(pat)})
    for f in files:
        print(f'{os.path.relpath(f, ROOT)}: {add(f)}')
    print(f'{len(files)} file(s) looked at.')


if __name__ == '__main__':
    main()
