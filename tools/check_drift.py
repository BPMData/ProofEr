"""Report differences between ProofEr and EOMD. Run in Thonny without arguments."""

import difflib
import hashlib
import subprocess
from pathlib import Path

# SETTINGS (paths are relative to the ProofEr repository)
EOMD_DIR = "../EOMD"

ROOT = Path(__file__).resolve().parents[1]
MERGE_MAP = ROOT / "notes/merge-map.md"

# These name collisions grew out of shared code or instructions. Review their drift
# too, even though their workflows now have different meanings.
COMPARE_COLLISIONS = {
    ".agents/hooks/stage_gate.py",
    ".agents/hooks/test_stage_gate.py",
    ".agents/skills/auto-piece/SKILL.md",
    ".agents/skills/new-piece/SKILL.md",
    ".claude/skills/auto-piece/SKILL.md",
    ".claude/skills/new-piece/SKILL.md",
    ".claude/skills/toolbox/SKILL.md",
}

# Approved differences keyed by ProofEr path. Pin both copies so a new edit to an
# already different pair still reports drift. The merge map gives the reasons.
INTENDED_DIFFERENCES = {
    ".agents/": "64e4ee7b450cb32e",
    ".agents/hooks.json": "16765a611cd67774",
    ".agents/hooks/stage_gate.py": "62affc29b916b841",
    ".agents/hooks/test_stage_gate.py": "0a3b367a743741ab",
    ".agents/skills/auto-piece/SKILL.md": "6da79b41b2144a77",
    ".agents/skills/new-piece/SKILL.md": "0ecb641f5ee4ebfd",
    ".claude/": "54da32c50eac6597",
    ".claude/agents/": "7543b7229d6243d0",
    ".claude/agents/fresh-eyes-reviewer.md": "6fb96c03e19d508a",
    ".claude/hooks/stage_log.py": "432ff47ee73df815",
    ".claude/skills/auto-piece/SKILL.md": "5b688d94eca1ed57",
    ".claude/skills/new-piece/SKILL.md": "76d48bb6527b23dd",
    ".claude/skills/toolbox/SKILL.md": "8de73d9010b42219",
    ".claude/skills/toolbox/choice-panel.html": "24d35e7be28c29a4",
    ".codex/config.toml": "46eb7fce9fe9eadb",
    ".git-blame-ignore-revs": "7eea5ae7469026ca",
    ".github/": "d3223e548317f18d",
    ".github/workflows/ci.yml": "28d9618a80f5fbe6",
    ".github/workflows/eval.yml": "16fb7eb0e0ba1e2a",
    ".gitignore": "650f8b617a117e53",
    ".prettierignore": "6204301ccb5e8f3c",
    "AGENTS.md": "f219ad18f8f31852",
    "CLAUDE.md": "59292f1d79f5278b",
    "README.md": "afce448ceea07265",
    "STATUS.md": "88b9c0ae9ea2e990",
    "brief/CRAFT.md": "c39e8dcd1830b4f3",
    "brief/INTERVIEW.md": "8044012e65fe5782",
    "brief/LAYOUT.md": "d13c0a9dca18d8b7",
    "brief/TEMPLATE.md": "f6b954d3da5d554b",
    "brief/clients/bryan.md": "1545425e1cd52db3",
    "brief/taste/house.md": "6f140ffab92bfacf",
    "index.html": "ff1090a22bf21e01",
    "notes/": "5ee3e2be89dcf2ae",
    "notes/architecture.md": "2b47c7e7a83dad3c",
    "package-lock.json": "cd46c8d9ee6d750b",
    "package.json": "6e9bb4268b346b4f",
    "pieces/": "450445c531ce69a0",
    "tools/CLAUDE.md": "c0c9ea61141a993a",
    "tools/check_stage_reads.py": "675da4f6f581cc9d",
    "tools/eval_new_piece.py": "3b0718aa3f0d4b73",
}


def shared_pairs(map_path):
    for line in map_path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| `"):
            continue
        left, right, category, *_ = (cell.strip() for cell in line.split("|")[1:-1])
        left = left.strip("`")
        if category.startswith("same purpose,") or left in COMPARE_COLLISIONS:
            yield left, right.strip("`")


def snapshot(root, name):
    path = root / name
    if not name.endswith("/"):
        return path.read_bytes()
    if not path.is_dir():
        raise FileNotFoundError(path)
    # Folder rows compare the tracked inventory. Child file rows compare bytes.
    listing = subprocess.check_output(
        ["git", "-C", str(root), "ls-files", "-z", "--", name],
        stderr=subprocess.PIPE,
    )
    prefix = name.encode("utf-8")
    return b"\n".join(sorted(entry[len(prefix):] for entry in listing.split(b"\0") if entry))


def fingerprint(left, right):
    combined = hashlib.sha256(left).digest() + hashlib.sha256(right).digest()
    return hashlib.sha256(combined).hexdigest()[:16]


def diff_summary(name, left, right):
    if name.endswith("/"):
        left_paths = set(left.decode("utf-8").splitlines())
        right_paths = set(right.decode("utf-8").splitlines())
        summary = []
        for repo, paths in (("ProofEr", left_paths - right_paths), ("EOMD", right_paths - left_paths)):
            if paths:
                summary.append(f"{len(paths)} only in {repo} (e.g. {min(paths)})")
        return ", ".join(summary)

    try:
        left_lines = left.decode("utf-8").splitlines(keepends=True)
        right_lines = right.decode("utf-8").splitlines(keepends=True)
    except UnicodeDecodeError:
        return f"bytes differ (ProofEr {len(left)}, EOMD {len(right)})"
    changes = list(difflib.unified_diff(left_lines, right_lines, n=0))[2:]
    added = sum(line.startswith("+") for line in changes)
    removed = sum(line.startswith("-") for line in changes)
    first_hunk = next((line.strip() for line in changes if line.startswith("@@")), "")
    return f"ProofEr → EOMD: +{added}/-{removed} lines, first change {first_hunk}"


def main():
    eomd = (ROOT / EOMD_DIR).resolve()
    if not eomd.is_dir():
        print(f"WARNING: EOMD checkout not found at {eomd}")
        return
    try:
        pairs = list(shared_pairs(MERGE_MAP))
    except (OSError, ValueError) as error:
        print(f"WARNING: could not read the merge map: {error}")
        return
    if not pairs:
        print("WARNING: no comparable paths in the merge map")
        return

    counts = dict(match=0, intended=0, drift=0)
    for left_name, right_name in pairs:
        label = f"{left_name} ↔ {right_name}"
        try:
            left = snapshot(ROOT, left_name)
            right = snapshot(eomd, right_name)
        except (OSError, subprocess.CalledProcessError) as error:
            counts["drift"] += 1
            print(f"WARNING drift: {label}: {error}")
            continue
        if left == right:
            counts["match"] += 1
            print(f"match: {label}")
            continue
        stamp = fingerprint(left, right)
        state = "intended" if INTENDED_DIFFERENCES.get(left_name) == stamp else "drift"
        counts[state] += 1
        prefix = "WARNING " if state == "drift" else ""
        print(f"{prefix}{state}: {label}: {diff_summary(left_name, left, right)} [{stamp}]")
    print(", ".join(f"{count} {state}" for state, count in counts.items()))


if __name__ == "__main__":
    main()
