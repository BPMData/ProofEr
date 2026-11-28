"""Verify the vendored EOMD kit. Run in Thonny or with Python, without arguments."""

import hashlib
import json
import re
from pathlib import Path

# SETTINGS (paths are relative to the ProofEr repository)
VENDOR_DIR = "vendor/eomd-kit"

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_NAME = "KIT.json"


def _unique_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate manifest key: {key!r}")
        result[key] = value
    return result


def read_manifest(kit_dir):
    """Return the original manifest bytes, version, and validated payload hashes."""
    path = kit_file(kit_dir, MANIFEST_NAME)
    raw = path.read_bytes()
    manifest = json.loads(raw, object_pairs_hook=_unique_keys)
    if not isinstance(manifest, dict):
        raise ValueError("KIT.json must contain an object")

    version = manifest.get("version")
    if not isinstance(version, str) or not re.fullmatch(r"(0|[1-9][0-9]*)(\.(0|[1-9][0-9]*)){2}", version):
        raise ValueError("KIT.json version must be x.y.z")
    if manifest.get("license") != "MIT":
        raise ValueError("KIT.json must declare the MIT license")
    files = manifest.get("files")
    if not isinstance(files, dict):
        raise ValueError("KIT.json files must map paths to SHA-256 hashes")

    seen = {MANIFEST_NAME.casefold()}
    for name, digest in files.items():
        parts = name.split("/")
        if any(
            part in ("", ".", "..")
            or part.casefold() == ".git"
            or part.endswith((".", " "))
            or re.search(r'[\\:*?"<>|\x00-\x1f]', part)
            for part in parts
        ):
            raise ValueError(f"Invalid path under kit/: {name!r}")
        if name.casefold() in seen or parts[0].casefold() == MANIFEST_NAME.casefold():
            raise ValueError(f"Reserved or conflicting kit path: {name!r}")
        seen.add(name.casefold())
        if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-fA-F]{64}", digest):
            raise ValueError(f"Invalid SHA-256 for {name!r}")
    return raw, version, files


def kit_file(kit_dir, name):
    """Resolve a validated kit-relative path using only regular files and directories."""
    path = candidate = kit_dir / name
    while True:
        if candidate.is_symlink():
            raise ValueError(f"Symlinks are not allowed in the kit: {candidate}")
        if candidate == kit_dir:
            break
        candidate = candidate.parent
    if not path.is_file():
        raise ValueError(f"Missing or non-regular kit file: {path}")
    return path


def verify_hash(path, expected):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    actual = digest.hexdigest()
    if actual != expected.lower():
        raise ValueError(f"SHA-256 mismatch for {path}: expected {expected}, got {actual}")


def _kit_paths(kit_dir):
    pending = [kit_dir]
    while pending:
        for path in pending.pop().iterdir():
            if path.is_symlink():
                raise ValueError(f"Symlinks are not allowed in the kit: {path}")
            if path.is_dir():
                pending.append(path)
            elif path.is_file():
                yield path.relative_to(kit_dir).as_posix()
            else:
                raise ValueError(f"Non-regular file in the kit: {path}")


def verify_vendor(kit_dir):
    """Return the verified version and file count, or None before the first sync."""
    if kit_dir.parent.is_symlink() or kit_dir.is_symlink():
        raise ValueError(f"Vendor paths must not be symlinks: {kit_dir}")
    if not kit_dir.exists():
        return None
    actual = set(_kit_paths(kit_dir))
    if not actual:
        return None
    _, version, files = read_manifest(kit_dir)
    unexpected = actual - files.keys() - {MANIFEST_NAME}
    if unexpected:
        raise ValueError(f"Files missing from KIT.json: {', '.join(sorted(unexpected))}")
    for name, expected in files.items():
        verify_hash(kit_file(kit_dir, name), expected)
    return version, len(files)


def main():
    try:
        result = verify_vendor(ROOT / VENDOR_DIR)
    except (OSError, ValueError) as error:
        print(f"FAIL: {error}")
        return 1
    if result is None:
        print("PASS: no EOMD kit vendored yet")
    else:
        version, count = result
        print(f"PASS: EOMD kit {version}, {count} files verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
