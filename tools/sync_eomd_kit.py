"""Install a pinned EOMD kit. Set the version and press Run in Thonny."""

import shutil
import tempfile
from pathlib import Path

from check_vendor import MANIFEST_NAME, VENDOR_DIR, kit_file, read_manifest, verify_vendor

# SETTINGS (paths are relative to the ProofEr repository)
EOMD_DIR = "../EOMD"
KIT_VERSION = ""  # Set to the exact x.y.z version of a released MIT kit.

ROOT = Path(__file__).resolve().parents[1]


def sync_kit(source, destination, expected_version):
    raw, version, files = read_manifest(source)
    if not expected_version:
        raise ValueError("Set KIT_VERSION to the exact released kit version before syncing")
    if version != expected_version:
        raise ValueError(f"Expected kit {expected_version}, found {version}")

    # Check the existing copy before replacing it so a sync cannot discard local edits.
    verify_vendor(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".eomd-kit-sync-", dir=destination.parent) as temporary:
        staging = Path(temporary)
        incoming = staging / "incoming"
        incoming.mkdir()
        for name in files:
            target = incoming / name
            target.parent.mkdir(parents=True, exist_ok=True)
            # Byte-for-byte copying preserves all upstream copyright and MIT headers.
            shutil.copyfile(kit_file(source, name), target)
        (incoming / MANIFEST_NAME).write_bytes(raw)
        verify_vendor(incoming)

        previous = staging / "previous"
        try:
            if destination.exists():
                destination.rename(previous)
            incoming.rename(destination)
        except BaseException:
            if previous.exists() and not destination.exists():
                previous.rename(destination)
            raise
    return version, len(files)


def main():
    source = (ROOT / EOMD_DIR).resolve() / "kit"
    if not (source / MANIFEST_NAME).is_file():
        print(f"No EOMD kit manifest found at {source / MANIFEST_NAME}. Run again when the kit ships.")
        return 1
    try:
        version, count = sync_kit(source, ROOT / VENDOR_DIR, KIT_VERSION)
    except (OSError, ValueError) as error:
        print(f"Sync failed: {error}")
        return 1
    print(f"Synced EOMD kit {version}: {count} files verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
