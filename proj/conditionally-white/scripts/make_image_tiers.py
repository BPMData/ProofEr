"""Conditionally White: make the display and thumbnail tiers from the raw archival downloads.

Run it in Thonny (the Run button). Every setting is in the SETTINGS block below.

What it does
- Reads every image in SRC_DIR (the raw downloads, kept untouched as the archive).
- Writes a display master to FULL_DIR (longest side FULL_MAX px, JPEG quality FULL_QUALITY).
- Writes a thumbnail to THUMB_DIR (longest side THUMB_MAX px, JPEG quality THUMB_QUALITY).
- Writes SIZES_JSON: slug -> pixel sizes of each tier, so the page can set width/height on every <img>.
- Prints the total thumbnail weight, to check against the initial-load budget.
"""

# ---------------- SETTINGS ----------------
from pathlib import Path

PIECE_DIR = Path(__file__).resolve().parent.parent  # proj/conditionally-white
SRC_DIR = PIECE_DIR / "img" / "src"
FULL_DIR = PIECE_DIR / "img" / "full"
THUMB_DIR = PIECE_DIR / "img" / "thumb"
SIZES_JSON = PIECE_DIR / "img" / "sizes.json"

FULL_MAX = 1800        # longest side, pixels (keeps archival text scans crisp)
FULL_QUALITY = 82
THUMB_MAX = 640
THUMB_QUALITY = 72
THUMB_BUDGET_KB = 1500  # larger archive (60+ plates); warn if thumbs exceed this

OVERWRITE = False      # True remakes tiers that already exist
# ------------------------------------------

import json
import re

from PIL import Image, ImageOps

Image.MAX_IMAGE_PIXELS = None  # archival scans can be very large; local trusted files
EXTS = {".jpg", ".jpeg", ".png", ".tif", ".tiff", ".webp"}


def slug_for(path: Path) -> str:
    s = path.stem.lower().replace("_", "-").replace(" ", "-")
    return re.sub(r"[^a-z0-9-]+", "", s).strip("-")


def to_rgb(img: Image.Image) -> Image.Image:
    img = ImageOps.exif_transpose(img)
    if img.mode in ("RGBA", "LA", "P"):
        img = img.convert("RGBA")
        bg = Image.new("RGB", img.size, (242, 237, 227))  # --paper
        bg.paste(img, mask=img.split()[-1])
        return bg
    return img.convert("RGB")


def save_tier(img: Image.Image, out: Path, max_side: int, quality: int, icc) -> tuple[int, int]:
    tier = img.copy()
    tier.thumbnail((max_side, max_side), Image.LANCZOS)
    out.parent.mkdir(parents=True, exist_ok=True)
    kwargs = {"quality": quality, "optimize": True, "progressive": True}
    if icc:
        kwargs["icc_profile"] = icc
    tier.save(out, "JPEG", **kwargs)
    return tier.size


def main() -> None:
    if not SRC_DIR.is_dir():
        print(f"No source folder yet: {SRC_DIR}")
        return
    sizes = json.loads(SIZES_JSON.read_text()) if SIZES_JSON.exists() else {}
    sources = sorted(p for p in SRC_DIR.iterdir() if p.suffix.lower() in EXTS)
    if not sources:
        print(f"No images in {SRC_DIR}")
        return
    for src in sources:
        slug = slug_for(src)
        full_out = FULL_DIR / f"{slug}.jpg"
        thumb_out = THUMB_DIR / f"{slug}.jpg"
        if not OVERWRITE and full_out.exists() and thumb_out.exists() and slug in sizes:
            print(f"skip  {slug}")
            continue
        with Image.open(src) as raw:
            icc = raw.info.get("icc_profile")
            img = to_rgb(raw)
            src_size = img.size
            full_size = save_tier(img, full_out, FULL_MAX, FULL_QUALITY, icc)
            thumb_size = save_tier(img, thumb_out, THUMB_MAX, THUMB_QUALITY, icc)
        sizes[slug] = {
            "src": {"file": src.name, "w": src_size[0], "h": src_size[1]},
            "full": {"w": full_size[0], "h": full_size[1], "kb": round(full_out.stat().st_size / 1024)},
            "thumb": {"w": thumb_size[0], "h": thumb_size[1], "kb": round(thumb_out.stat().st_size / 1024)},
        }
        print(f"made  {slug}: full {full_size}, thumb {thumb_size}")
    SIZES_JSON.parent.mkdir(parents=True, exist_ok=True)
    SIZES_JSON.write_text(json.dumps(sizes, indent=2, sort_keys=True) + "\n")
    total = sum(v["thumb"]["kb"] for v in sizes.values())
    note = "over budget" if total > THUMB_BUDGET_KB else "within budget"
    print(f"\n{len(sizes)} images; thumbnails total {total} KB ({note}, budget {THUMB_BUDGET_KB} KB)")
    print(f"Sizes written to {SIZES_JSON}")


if __name__ == "__main__":
    main()
