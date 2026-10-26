"""check_offline.py: does a finished piece load anything from the internet?

A ProofEr piece must work with the network off: fonts, data, code and images all inside the one HTML file. This
script lists every remote load it finds (stylesheets, scripts, images, fonts, frames, CSS @import and url()).
Plain links the reader clicks (<a href>) are fine: sources should link out.
Run it in Thonny with the Run button (set CHECK below), or CI runs it on everything in pieces/ and fails on a hit.
"""
import glob, os, re, sys

# ===================== SETTINGS =====================
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # the repo root (this script sits in tools/)
CHECK = [os.path.join(ROOT, 'pieces', '*.html')]                     # files or glob patterns to check
# ====================================================

REMOTE = r'(?:https?:)?//[^\s"\'<>)]+'
PATTERNS = [
    ('stylesheet or preconnect', re.compile(r'<link\b[^>]*\bhref\s*=\s*["\'](' + REMOTE + ')', re.I)),
    ('script', re.compile(r'<script\b[^>]*\bsrc\s*=\s*["\'](' + REMOTE + ')', re.I)),
    ('image, media or frame', re.compile(r'<(?:img|source|video|audio|iframe|embed|track)\b[^>]*\bsrc\s*=\s*["\'](' + REMOTE + ')', re.I)),
    ('CSS @import', re.compile(r'@import\s+(?:url\()?\s*["\']?(' + REMOTE + ')', re.I)),
    ('CSS url()', re.compile(r'url\(\s*["\']?(' + REMOTE + r')', re.I)),
    ('fetch / import in code', re.compile(r'(?:fetch|import)\s*\(\s*["\'](' + REMOTE + ')', re.I)),
]


def check_file(path):
    with open(path, encoding='utf-8', errors='replace') as fh:
        text = fh.read()
    hits = []
    for kind, rx in PATTERNS:
        for m in rx.finditer(text):
            line = text.count('\n', 0, m.start()) + 1
            hits.append((line, kind, m.group(1)[:120]))
    return sorted(set(hits))


def main():
    files = sorted({f for pat in CHECK for f in glob.glob(pat)})
    gh = os.environ.get('GITHUB_ACTIONS') == 'true'
    bad = 0
    for f in files:
        rel = os.path.relpath(f, ROOT).replace(os.sep, '/')
        hits = check_file(f)
        bad += bool(hits)
        print(f'{rel}: ' + ('offline OK' if not hits else f'{len(hits)} remote load(s)'))
        for line, kind, url in hits:
            print(f'::error file={rel},line={line}::{kind} loads {url}' if gh else f'  line {line}: {kind}: {url}')
    if not files:
        print('Nothing to check yet.')
    print(f'{len(files)} file(s) checked, {bad} with remote loads.')
    return bad == 0


if __name__ == '__main__':
    sys.exit(0 if main() else 1)
