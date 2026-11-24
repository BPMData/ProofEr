"""Disaster Artist: measure each painting's dominant colours for the compare plates.

Run it in Thonny (the Run button). Every setting is in the SETTINGS block below.

What it does
- For each slug in SLUGS, opens IMG_DIR/<slug>.jpg (the display tier made by make_image_tiers.py).
- Trims CROP_MARGIN of each edge (drops frames and scan borders), samples SAMPLE_PIXELS pixels at random
  (fixed seed, so reruns give the same answer) and groups them into K colours with k-means in Lab space,
  which matches how people see colour differences better than RGB does.
- Writes OUT_JSON: slug -> colours sorted by share of the canvas, each with hex, share (0-1) and a rough
  everyday colour name, so a caption can say "orange-on-green with blue trim" from measured numbers.
- Prints the result as a table.

Needs Pillow and numpy only.
"""

# ---------------- SETTINGS ----------------
from pathlib import Path

PIECE_DIR = Path(__file__).resolve().parent.parent  # proj/disaster-artist
IMG_DIR = PIECE_DIR / "img" / "full"
OUT_JSON = PIECE_DIR / "img" / "swatches.json"

SLUGS = [
    "self-portrait-dedicated-to-gauguin",   # the monk (Harvard)
    "gauguin-les-miserables",               # the messiah (Van Gogh Museum)
    "gauguin-christ-garden-of-olives",      # the escalation (Norton)
]
K = 6                  # colours per painting
CROP_MARGIN = 0.04     # share of width/height trimmed from each edge
SAMPLE_PIXELS = 60000
MIN_SHARE = 0.03       # colours covering less than this are dropped from the output
SEED = 1888
ITERATIONS = 40
# ------------------------------------------

import json

import numpy as np
from PIL import Image

# Rough everyday names, by hue angle in Lab (a*, b*) with lightness and chroma checks.
NAMED = [
    ("red", 20), ("orange", 55), ("ochre", 75), ("yellow", 95), ("yellow-green", 115),
    ("green", 150), ("teal", 200), ("blue", 280), ("violet", 320), ("pink", 355),
]


def srgb_to_lab(rgb: np.ndarray) -> np.ndarray:
    c = rgb / 255.0
    c = np.where(c > 0.04045, ((c + 0.055) / 1.055) ** 2.4, c / 12.92)
    m = np.array([[0.4124, 0.3576, 0.1805], [0.2126, 0.7152, 0.0722], [0.0193, 0.1192, 0.9505]])
    xyz = c @ m.T / np.array([0.95047, 1.0, 1.08883])
    f = np.where(xyz > 0.008856, np.cbrt(xyz), 7.787 * xyz + 16 / 116)
    L = 116 * f[:, 1] - 16
    a = 500 * (f[:, 0] - f[:, 1])
    b = 200 * (f[:, 1] - f[:, 2])
    return np.stack([L, a, b], axis=1)


def colour_name(lab: np.ndarray) -> str:
    L, a, b = lab
    chroma = float(np.hypot(a, b))
    if chroma < 10:
        if L < 25:
            return "soot black"
        if L > 80:
            return "off-white"
        return "grey"
    hue = (np.degrees(np.arctan2(b, a)) + 360) % 360
    name = min(NAMED, key=lambda n: min(abs(hue - n[1]), 360 - abs(hue - n[1])))[0]
    if L < 35:
        name = f"dark {name}"
    elif L > 75 and chroma < 35:
        name = f"pale {name}"
    return name


def kmeans(lab: np.ndarray, k: int, rng: np.random.Generator) -> tuple[np.ndarray, np.ndarray]:
    # k-means++ start, then Lloyd iterations
    centres = [lab[rng.integers(len(lab))]]
    for _ in range(1, k):
        d = np.min(((lab[:, None, :] - np.array(centres)[None]) ** 2).sum(-1), axis=1)
        centres.append(lab[rng.choice(len(lab), p=d / d.sum())])
    centres = np.array(centres)
    for _ in range(ITERATIONS):
        labels = np.argmin(((lab[:, None, :] - centres[None]) ** 2).sum(-1), axis=1)
        new = np.array([lab[labels == i].mean(0) if np.any(labels == i) else centres[i] for i in range(k)])
        if np.allclose(new, centres, atol=0.05):
            break
        centres = new
    return centres, labels


def swatches_for(path: Path) -> list[dict]:
    with Image.open(path) as im:
        im = im.convert("RGB")
        w, h = im.size
        mx, my = int(w * CROP_MARGIN), int(h * CROP_MARGIN)
        px = np.asarray(im.crop((mx, my, w - mx, h - my)), dtype=np.float64).reshape(-1, 3)
    rng = np.random.default_rng(SEED)
    if len(px) > SAMPLE_PIXELS:
        px = px[rng.choice(len(px), SAMPLE_PIXELS, replace=False)]
    lab = srgb_to_lab(px)
    centres, labels = kmeans(lab, K, rng)
    out = []
    for i in range(K):
        mask = labels == i
        share = float(mask.mean())
        if share < MIN_SHARE:
            continue
        mean_rgb = px[mask].mean(0).round().astype(int)  # the cluster's average in the painting's own RGB
        out.append({
            "hex": "#{:02X}{:02X}{:02X}".format(*mean_rgb),
            "share": round(share, 3),
            "name": colour_name(centres[i]),
        })
    return sorted(out, key=lambda s: -s["share"])


def main() -> None:
    result = {}
    for slug in SLUGS:
        path = IMG_DIR / f"{slug}.jpg"
        if not path.exists():
            print(f"missing {path} (run scripts/make_image_tiers.py first, or fix the slug)")
            continue
        result[slug] = swatches_for(path)
        print(f"\n{slug}")
        for s in result[slug]:
            print(f"  {s['hex']}  {s['share'] * 100:5.1f}%  {s['name']}")
    if result:
        OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
        OUT_JSON.write_text(json.dumps(result, indent=2) + "\n")
        print(f"\nWritten to {OUT_JSON}")


if __name__ == "__main__":
    main()
