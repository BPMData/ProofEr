"""
build.py -- builds "It's All in the Wall", the scannable remake of the clay cookware piece, into ONE offline HTML file.

Run it with Thonny's Run button. No extra packages needed.
Fonts: reuses the Newsreader + IBM Plex Sans @font-face blocks already embedded in the original piece
(SIL Open Font License 1.1), so nothing is downloaded.
Citations: write [[13]] (or [[2]][[14]]) in page.html; they become numbered links to the source list.
"""
# ============================ SETTINGS (edit these) ============================
FONT_SOURCE = "../../../pieces/clay-cookware.html"   # the original piece; its first <style> block holds the fonts
OUT = "../../../pieces/clay-cookware-v2.html"         # where the finished page goes
# ===============================================================================
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "src")


def read(p):
    with open(p, encoding="utf-8") as fh:
        return fh.read()


def cite(m):
    nums = re.findall(r"\d+", m.group(0))
    links = ",".join(f'<a href="#s{n}" aria-label="source {n}">{n}</a>' for n in nums)
    return f'<sup class="fn">{links}</sup>'


def main():
    html = read(os.path.join(SRC, "page.html"))
    css = read(os.path.join(SRC, "page.css"))
    js = read(os.path.join(SRC, "page.js"))
    original = read(os.path.normpath(os.path.join(HERE, FONT_SOURCE)))
    m = re.search(r"<style>(.*?)</style>", original, re.S)
    if not m or "@font-face" not in m.group(1):
        sys.exit("could not find the font block in " + FONT_SOURCE)
    fonts = m.group(1)

    html = re.sub(r"(?:\[\[\d+\]\])+", cite, html)
    used = sorted({int(n) for n in re.findall(r'href="#s(\d+)"', html + js)})
    listed = {int(n) for n in re.findall(r'<li id="s(\d+)"', html)}
    missing = [n for n in used if n not in listed]
    if missing:
        sys.exit(f"cited but not in the source list: {missing}")
    print("sources cited:", len(used), "of", len(listed))

    out = html.replace("{{FONTFACES}}", fonts).replace("{{CSS}}", css).replace("{{JS}}", js)
    for m in re.finditer(r'(?:src=|url\()\s*["\']?(https?://[^"\')\s]+)', out):
        sys.exit(f"remote load found: {m.group(1)}")
    dest = os.path.normpath(os.path.join(HERE, OUT))
    with open(dest, "w", encoding="utf-8") as fh:
        fh.write(out)
    print(f"wrote {os.path.relpath(dest, HERE)}: {len(out.encode()) // 1024} KB")


if __name__ == "__main__":
    main()
