#!/usr/bin/env python3
"""Programmatic stage-gate & receipt hook shared across Antigravity, Claude Code, and Codex CLI.

Enforces ProofEr's research -> figures -> layout/stills -> build -> QA pipeline:
- PostToolUse records verified subagent/workflow runs, inspected PNG screenshots, and offline checks.
- PreToolUse blocks writing figures.md, layout.md/stills, or pieces/<name>.html out of order.
- Stop blocks early completion in autonomous mode until check_offline.py and final PNG QA pass.
"""
from __future__ import annotations

import argparse
import glob
import hashlib
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

DESIGN_RESEARCH_STAGES = {"interview", "brief", "research", "figures"}
TOOL_ROOT = Path(__file__).resolve().parents[2]


def _read_text(path: Path, limit: int | None = None) -> str:
    try:
        with path.open("r", encoding="utf-8") as fh:
            return fh.read(limit) if limit else fh.read()
    except OSError:
        return ""


def _parse_brief_meta(root: Path, piece: str) -> tuple[str, bool, str]:
    """Return (stage, is_autonomous, mode) from proj/<piece>/brief.md."""
    brief = root / "proj" / piece / "brief.md"
    head = _read_text(brief, 2500)
    stage_m = re.search(r"Stage:\s*([a-zA-Z_-]+)", head)
    stage = stage_m.group(1).lower() if stage_m else ""
    mode_m = re.search(r"Mode:\s*([^\n·|]+)", head, re.I)
    mode = mode_m.group(1).strip().lower() if mode_m else ""
    auto = bool(
        re.search(r"(Autonomous:\s*(yes|true|on)|Mode:\s*autonomous)", head, re.I)
        or (root / "proj" / piece / ".autonomous").exists()
    )
    return stage, auto, mode


def _newest_active_piece(root: Path) -> str | None:
    """Return the piece name with the most recently modified proj/<name>/brief.md."""
    best: tuple[float, str] | None = None
    for brief in glob.glob(str(root / "proj" / "*" / "brief.md")):
        p = Path(brief)
        name = p.parent.name
        try:
            mt = p.stat().st_mtime
        except OSError:
            continue
        if best is None or mt > best[0]:
            best = (mt, name)
    return best[1] if best else None


def _rel_path(root: Path, raw: str) -> str:
    if not raw:
        return ""
    p = Path(raw)
    if not p.is_absolute():
        p = (root / p).resolve()
    else:
        p = p.resolve()
    try:
        return p.relative_to(root.resolve()).as_posix()
    except ValueError:
        return raw.replace("\\", "/")


def _extract_paths_from_shell(cmd: str) -> list[str]:
    paths: list[str] = []
    for m in re.finditer(r"(?:^|[\s'\"(=])((?:\./)?(?:proj|pieces)/[^\s'\"`;|>&)]+)", cmd):
        paths.append(m.group(1))
    return paths


def _extract_target_paths(root: Path, tool_name: str, args: dict) -> list[str]:
    low = tool_name.lower()
    raw_paths: list[str] = []
    for key in ("Path", "file_path", "path", "target_file"):
        val = args.get(key)
        if isinstance(val, str) and val:
            raw_paths.append(val)
    if "patch" in low or "apply_patch" in low:
        patch_text = str(args.get("patch") or args.get("input") or args.get("Patch") or "")
        for m in re.finditer(r"^\*\*\*\s+(?:Add|Update|Delete)\s+File:\s*(.+)$", patch_text, re.M):
            raw_paths.append(m.group(1).strip())
    if low in ("run_command", "bash", "shell", "command"):
        cmd = str(args.get("CommandLine") or args.get("command") or "")
        # Only gate shell commands that clearly write/redirect to target files
        if re.search(r"(>|>>|\btee\b|\bmv\b|\bcp\b|write_text|open\s*\()", cmd):
            raw_paths.extend(_extract_paths_from_shell(cmd))
    return [_rel_path(root, p) for p in raw_paths if p]


def _normalize_input(harness: str, event: str, payload: dict) -> dict:
    cwd_raw = payload.get("cwd") or os.environ.get("CLAUDE_PROJECT_DIR")
    if not cwd_raw and isinstance(payload.get("workspacePaths"), list) and payload["workspacePaths"]:
        cwd_raw = payload["workspacePaths"][0]
    root = Path(cwd_raw).resolve() if cwd_raw else TOOL_ROOT

    if harness == "antigravity":
        tc = payload.get("toolCall") or {}
        tool_name = str(tc.get("name") or "")
        args = tc.get("args") if isinstance(tc.get("args"), dict) else {}
        error = payload.get("error")
        term = str(payload.get("terminationReason") or "")
        active = bool(payload.get("continuationActive", False))
        return {
            "root": root,
            "tool": tool_name,
            "args": args,
            "error": error,
            "stop_active": active or (event == "Stop" and term not in ("", "NO_TOOL_CALL")),
        }

    # Claude Code & Codex CLI share tool_name / tool_input / stop_hook_active conventions
    tool_name = str(payload.get("tool_name") or (payload.get("toolCall") or {}).get("name") or "")
    args = payload.get("tool_input") or (payload.get("toolCall") or {}).get("args") or {}
    if not isinstance(args, dict):
        args = {}
    error = payload.get("error")
    tr = payload.get("tool_response")
    if not error and isinstance(tr, dict):
        if tr.get("is_error") or tr.get("exit_code", 0) != 0 or tr.get("returncode", 0) != 0:
            error = "tool_response error"
    active = bool(payload.get("stop_hook_active", False))
    return {
        "root": root,
        "tool": tool_name,
        "args": args,
        "error": error,
        "stop_active": active,
    }


def _subagent_receipts_path(root: Path, piece: str) -> Path:
    return root / "proj" / piece / "research" / ".subagent_receipts.jsonl"


def _review_receipts_path(root: Path, piece: str) -> Path:
    return root / "proj" / piece / ".review_receipts.jsonl"


def _inspected_pngs_path(root: Path, piece: str) -> Path:
    return root / "proj" / piece / ".inspected_pngs.json"


def _offline_checked_path(root: Path, piece: str) -> Path:
    return root / "proj" / piece / ".offline_checked.json"


def _load_json(path: Path, default):
    txt = _read_text(path)
    if not txt:
        return default
    try:
        return json.loads(txt)
    except ValueError:
        return default


def _file_sha256(path: Path) -> str:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return ""


def _is_fresh_eyes_subagent(args: dict) -> bool:
    sub_type = str(args.get("subagent_type") or args.get("TypeName") or args.get("agent_type") or "").lower()
    role = str(args.get("Role") or args.get("role") or args.get("name") or "").lower()
    prompt = str(args.get("Prompt") or args.get("prompt") or "").lower()
    if "fresh-eyes" in sub_type or "fresh_eyes" in sub_type or "reviewer" in sub_type:
        return True
    if "fresh" in role or "review" in role:
        return True
    return any(tok in prompt for tok in ("fresh-eyes", "fresh eyes", "stills/review.md", "qa/review.md", "craft.md §12"))


def _extract_piece_from_subagent(root: Path, args: dict) -> list[str]:
    blob = " ".join(str(args.get(k) or "") for k in ("Prompt", "prompt", "Role", "role"))
    found: list[str] = []
    for m in re.finditer(r"proj/([a-zA-Z0-9_-]+)/", blob):
        name = m.group(1)
        if (root / "proj" / name / "brief.md").exists() and name not in found:
            found.append(name)
    return found


def _has_review_receipt(root: Path, piece: str, html_sha: str = "", min_ts: float = 0.0) -> bool:
    rpath = _review_receipts_path(root, piece)
    for ln in _read_text(rpath).splitlines():
        ln = ln.strip()
        if not ln:
            continue
        try:
            rec = json.loads(ln)
        except ValueError:
            continue
        if html_sha:
            if rec.get("html_sha256") == html_sha or float(rec.get("ts", 0.0)) >= min_ts:
                return True
        else:
            return True
    return False


def _record_post_tool(root: Path, tool_name: str, args: dict, error) -> None:
    if error:
        return
    low = tool_name.lower()
    now = time.time()

    # 1. Subagent / workflow execution receipt
    if low in ("run_workflow", "invoke_subagent", "agent", "task", "spawn_agent"):
        is_review = low != "run_workflow" and _is_fresh_eyes_subagent(args)
        targets = _extract_piece_from_subagent(root, args) if is_review else []
        if not targets:
            for brief in glob.glob(str(root / "proj" / "*" / "brief.md")):
                piece = Path(brief).parent.name
                stage, _, _ = _parse_brief_meta(root, piece)
                if not stage or stage in DESIGN_RESEARCH_STAGES:
                    targets.append(piece)
        if not targets:
            newest = _newest_active_piece(root)
            if newest:
                targets = [newest]
        for piece in targets:
            stage, _, _ = _parse_brief_meta(root, piece)
            rpath = _subagent_receipts_path(root, piece)
            rpath.parent.mkdir(parents=True, exist_ok=True)
            with rpath.open("a", encoding="utf-8") as fh:
                fh.write(json.dumps({"ts": now, "tool": tool_name, "review": is_review}) + "\n")
            if is_review:
                html = root / "pieces" / f"{piece}.html"
                rec = {
                    "ts": now,
                    "tool": tool_name,
                    "stage": stage,
                    "html_sha256": _file_sha256(html) if html.exists() else "",
                }
                rev_path = _review_receipts_path(root, piece)
                rev_path.parent.mkdir(parents=True, exist_ok=True)
                with rev_path.open("a", encoding="utf-8") as fh:
                    fh.write(json.dumps(rec) + "\n")
        return

    # 2. Image read receipt (read_file / Read / view_file / view_image on a .png under proj/<name>/)
    if low in ("read_file", "read", "view_file", "view_image"):
        for raw_key in ("Path", "file_path", "path"):
            val = args.get(raw_key)
            if not isinstance(val, str) or not val.lower().endswith(".png"):
                continue
            rel = _rel_path(root, val)
            m = re.match(r"proj/([^/]+)/(.+\.png)$", rel, re.I)
            if not m:
                continue
            piece = m.group(1)
            abs_png = root / rel
            if not abs_png.exists():
                continue
            ipath = _inspected_pngs_path(root, piece)
            data = _load_json(ipath, {})
            data[rel] = max(now, abs_png.stat().st_mtime)
            if not rel.startswith(f"proj/{piece}/stills/"):
                html = root / "pieces" / f"{piece}.html"
                sha = _file_sha256(html)
                if sha:
                    by_sha = data.setdefault("_sha256_pngs", {})
                    lst = by_sha.setdefault(sha, [])
                    if rel not in lst:
                        lst.append(rel)
            ipath.parent.mkdir(parents=True, exist_ok=True)
            ipath.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        return

    # 3. tools/check_offline.py execution receipt
    if low in ("run_command", "bash", "shell", "command"):
        cmd = str(args.get("CommandLine") or args.get("command") or "")
        if "check_offline.py" in cmd:
            for brief in glob.glob(str(root / "proj" / "*" / "brief.md")):
                piece = Path(brief).parent.name
                html = root / "pieces" / f"{piece}.html"
                opath = _offline_checked_path(root, piece)
                # Stamp only pieces with local work (or no stamp yet): re-stamping every piece on every
                # check dirtied untouched pieces' receipt files and made them look "touched" at Stop.
                if html.exists() and (not opath.exists() or _piece_has_local_changes(root, piece)):
                    opath.write_text(
                        json.dumps({"ts": now, "sha256": _file_sha256(html), "cmd": cmd[:200]}) + "\n",
                        encoding="utf-8",
                    )


def _research_reports(root: Path, piece: str) -> list[Path]:
    rdir = root / "proj" / piece / "research"
    if not rdir.is_dir():
        return []
    reports: list[Path] = []
    for p in rdir.rglob("*"):
        if not p.is_file():
            continue
        if p.name.startswith(".") or p.name == "prompts.md":
            continue
        if p.suffix.lower() in (".md", ".json", ".txt") and p.stat().st_size >= 80:
            reports.append(p)
    return reports


def _parse_budget_meta(root: Path, piece: str) -> tuple[str, bool]:
    """Return (budget, override_approved) from proj/<piece>/brief.md."""
    brief = root / "proj" / piece / "brief.md"
    head = _read_text(brief, 2500)
    m = re.search(r"Budget:\s*([a-zA-Z_-]+)", head, re.I)
    budget = m.group(1).lower() if m else "standard"
    override = bool(
        re.search(r"Budget-Override:\s*(approved|yes|true)", head, re.I)
        or (root / "proj" / piece / ".budget_override").exists()
    )
    return budget, override


def _check_pre_subagent(root: Path, harness: str, tool_name: str, args: dict) -> str | None:
    low = tool_name.lower()
    if low not in ("agent", "task", "spawn_agent", "invoke_subagent", "run_workflow"):
        return None

    # Enforce model/effort ceiling on Claude Code and Codex (Antigravity left unrestricted for now)
    if harness in ("claude", "codex"):
        model = str(args.get("model") or args.get("Model") or "").lower()
        effort = str(args.get("reasoning_effort") or args.get("effort") or "").lower()
        if "fable" in model or "turbo" in model:
            return "Budget gate: 'fable' and 'turbo' models are prohibited for subagents at any budget tier."
        if effort in ("max", "xhigh", "extra", "turbo"):
            return "Budget gate: subagent reasoning effort above 'high' is prohibited."

    # Enforce Budget: light overflow gate (>3 workers or Pass 2) unless user approved override
    piece = None
    if low == "run_workflow":
        wf_args = args.get("Args") if isinstance(args.get("Args"), dict) else {}
        if isinstance(wf_args.get("piece"), str) and wf_args["piece"]:
            piece = wf_args["piece"]
    if not piece:
        piece = _newest_active_piece(root)
    if not piece:
        return None

    stage, _, _ = _parse_brief_meta(root, piece)
    budget, override = _parse_budget_meta(root, piece)
    if budget != "light" or override:
        return None

    if low == "run_workflow" and "research_piece.py" in str(args.get("ScriptPath") or ""):
        wf_args = args.get("Args") if isinstance(args.get("Args"), dict) else {}
        round_tag = str(wf_args.get("round") or "pass1")
        prompts = wf_args.get("prompts")
        if not isinstance(prompts, list):
            pjson = root / "proj" / piece / "research" / "prompts.json"
            prompts = _load_json(pjson, [])
        if round_tag != "pass1" or (isinstance(prompts, list) and len(prompts) > 3):
            return (
                f"Light budget gate: {piece} requests round={round_tag!r} with {len(prompts) if isinstance(prompts, list) else '?'} "
                f"workers (limit: <=3 workers in pass1). Warn the user and ask whether to proceed (Budget-Override: approved)."
            )
    elif low in ("agent", "task", "spawn_agent", "invoke_subagent") and stage in ("research", ""):
        rpath = _subagent_receipts_path(root, piece)
        prior = len([ln for ln in _read_text(rpath).splitlines() if ln.strip()])
        prompt_txt = str(args.get("prompt") or args.get("Prompt") or "").lower()
        if prior >= 3 or "gap_fill" in prompt_txt or "pass 2" in prompt_txt:
            return (
                f"Light budget gate: {piece} already ran {prior} worker(s) or requests Pass 2. "
                f"Warn the user and ask before exceeding the 3-worker light budget (Budget-Override: approved)."
            )
    return None


def _check_pre_write(root: Path, harness: str, rel_path: str) -> str | None:
    m_fig = re.match(r"^proj/([^/]+)/figures\.md$", rel_path)
    if m_fig:
        piece = m_fig.group(1)
        stage, _, _ = _parse_brief_meta(root, piece)
        if stage == "interview":
            return (
                f"Stage gate: complete the client interview and advance proj/{piece}/brief.md "
                f"from Stage: interview before writing figures.md."
            )
        prompts = root / "proj" / piece / "research" / "prompts.md"
        if not prompts.exists() or len(_read_text(prompts).strip()) < 100:
            return (
                f"Stage gate: write proj/{piece}/research/prompts.md (gap-targeted research prompts) "
                f"before creating proj/{piece}/figures.md."
            )
        reports = _research_reports(root, piece)
        if len(reports) < 2:
            return (
                f"Stage gate: proj/{piece}/research/ needs at least 2 independent worker/tool research outputs "
                f"(found {len(reports)}) before synthesizing figures.md."
            )
        if harness in ("antigravity", "claude"):
            rpath = _subagent_receipts_path(root, piece)
            if not rpath.exists() or not _read_text(rpath).strip():
                return (
                    f"Research gate: no isolated subagent/workflow receipt found for {piece}. "
                    f"Run parallel isolated search workers (run_workflow / Agent) before writing figures.md."
                )
        return None

    m_design = re.match(r"^proj/([^/]+)/(layout\.md|stills/[^/]+\.(?:html|svg))$", rel_path)
    if m_design:
        piece = m_design.group(1)
        figs = root / "proj" / piece / "figures.md"
        txt = _read_text(figs)
        rows = [ln for ln in txt.splitlines() if re.match(r"^\|\s*F\d+", ln.strip())]
        if len(rows) < 2:
            return (
                f"Stage gate: proj/{piece}/figures.md must have at least 2 checked/documented figure rows (| F01 | ...) "
                f"before creating {rel_path}."
            )
        return None

    m_piece = re.match(r"^pieces/([^/]+)\.html$", rel_path)
    if m_piece:
        piece = m_piece.group(1)
        brief = root / "proj" / piece / "brief.md"
        if not brief.exists():
            # Allow editing pre-existing pieces/ without a proj/ brief
            return None
        _, _, mode = _parse_brief_meta(root, piece)
        layout = root / "proj" / piece / "layout.md"
        layout_txt = _read_text(layout)
        if not re.search(r"\bAPPROVED\b", layout_txt):
            return (
                f"Stage gate: proj/{piece}/layout.md must be marked APPROVED (after sharing the outline/mockup "
                f"with the user) before building pieces/{piece}.html."
            )
        if "quicker" not in mode:
            stills_dir = root / "proj" / piece / "stills"
            html_stills = list(stills_dir.glob("*.html")) + list(stills_dir.glob("*.svg")) if stills_dir.is_dir() else []
            png_stills = list(stills_dir.glob("*.png")) if stills_dir.is_dir() else []
            inspected = _load_json(_inspected_pngs_path(root, piece), {})
            inspected_stills = [k for k in inspected if k.startswith(f"proj/{piece}/stills/") and (root / k).exists()]
            if not html_stills or not png_stills or not inspected_stills:
                return (
                    f"Visual gate: render and inspect at least 1 mockup PNG in proj/{piece}/stills/ via "
                    f"read_file/Read/view_image before building pieces/{piece}.html."
                )
            review_md = stills_dir / "review.md"
            critique = stills_dir / "critique.md"
            has_review_notes = (
                len(_read_text(review_md).strip()) >= 80
                or len(_read_text(critique).strip()) >= 80
            )
            if not _has_review_receipt(root, piece) or not has_review_notes:
                return (
                    f"Fresh-eyes gate: run an isolated fresh-eyes reviewer subagent on proj/{piece}/stills/ "
                    f"writing proj/{piece}/stills/review.md before building pieces/{piece}.html."
                )
        return None

    return None


RECEIPT_NAMES = (".offline_checked.json", ".inspected_pngs.json", ".subagent_receipts.jsonl", ".review_receipts.jsonl")


def _piece_has_local_changes(root: Path, piece: str) -> bool:
    """True if the piece's page or project files (receipt files excluded) differ from git HEAD."""
    if not (root / ".git").exists():
        return True
    try:
        p = subprocess.run(
            ["git", "status", "--porcelain", "--", f"proj/{piece}", f"pieces/{piece}.html"],
            cwd=str(root),
            capture_output=True,
            text=True,
            timeout=3,
        )
    except OSError:
        return True
    if p.returncode != 0:
        return True
    for line in p.stdout.splitlines():
        path = line[3:].strip().strip('"')
        if not path.endswith(RECEIPT_NAMES):
            return True
    return False


def _piece_html_has_local_changes(root: Path, piece: str) -> bool:
    """True if pieces/<piece>.html (or its asset dir) differs from git HEAD."""
    if not (root / ".git").exists():
        return True
    try:
        p = subprocess.run(
            ["git", "status", "--porcelain", "--", f"pieces/{piece}.html", f"pieces/assets/{piece}"],
            cwd=str(root),
            capture_output=True,
            text=True,
            timeout=3,
        )
    except OSError:
        return True
    if p.returncode != 0:
        return True
    return bool(p.stdout.strip())


def _piece_touched_in_repo(root: Path, piece: str) -> bool:
    """In a git repo, skip committed pieces whose published HTML has no local changes."""
    return _piece_html_has_local_changes(root, piece)


def _check_stop(root: Path, stop_active: bool) -> str | None:
    if stop_active:
        return None
    for brief_str in glob.glob(str(root / "proj" / "*" / "brief.md")):
        piece = Path(brief_str).parent.name
        stage, _, _ = _parse_brief_meta(root, piece)
        if stage in ("done", "published"):
            continue
        html = root / "pieces" / f"{piece}.html"
        if not html.exists():
            # Interview and outline-review turns legitimately pause for the user before pieces/<name>.html exists.
            continue
        if not _piece_touched_in_repo(root, piece):
            continue
        html_mtime = html.stat().st_mtime
        html_sha = _file_sha256(html)
        off = _load_json(_offline_checked_path(root, piece), {})
        off_ok = bool(off) and (
            (html_sha and off.get("sha256") == html_sha) or float(off.get("ts", 0.0)) >= html_mtime
        )
        if not off_ok:
            return (
                f"Run `python3 tools/check_offline.py` after the final edit to pieces/{piece}.html before finishing."
            )
        inspected = _load_json(_inspected_pngs_path(root, piece), {})
        mtime_pngs = [
            k for k, ts in inspected.items()
            if not k.startswith("_")
            and not k.startswith(f"proj/{piece}/stills/")
            and isinstance(ts, (int, float))
            and (root / k).exists()
            and float(ts) >= html_mtime
        ]
        sha_pngs = [
            k for k in (inspected.get("_sha256_pngs") or {}).get(html_sha, [])
            if (root / k).exists()
        ] if html_sha else []
        if len(set(mtime_pngs) | set(sha_pngs)) < 2:
            return (
                f"Capture and inspect final desktop and phone PNG screenshots of pieces/{piece}.html "
                f"(under proj/{piece}/qa/) via read_file/Read/view_image before finishing."
            )
        qa_review = root / "proj" / piece / "qa" / "review.md"
        if not _has_review_receipt(root, piece, html_sha=html_sha, min_ts=html_mtime) or len(_read_text(qa_review).strip()) < 80:
            return (
                f"Run an isolated fresh-eyes reviewer subagent on proj/{piece}/qa/ writing proj/{piece}/qa/review.md "
                f"for the current pieces/{piece}.html before finishing."
            )
    return None


def _emit(harness: str, event: str, reason: str | None) -> int:
    if event == "PostToolUse":
        print("{}")
        return 0
    if not reason:
        if harness == "antigravity":
            print(json.dumps({"decision": "allow"} if event == "PreToolUse" else {}))
        return 0
    if harness == "antigravity":
        if event == "PreToolUse":
            print(json.dumps({"decision": "deny", "reason": reason}))
        else:
            print(json.dumps({"decision": "continue", "reason": reason}))
        return 0
    print(reason, file=sys.stderr)
    return 2


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--harness", choices=("antigravity", "claude", "codex"), required=True)
    ap.add_argument("--event", choices=("PreToolUse", "PostToolUse", "Stop"), required=True)
    opts = ap.parse_args(argv)

    try:
        raw = sys.stdin.read()
        payload = json.loads(raw) if raw.strip() else {}
    except ValueError:
        payload = {}

    info = _normalize_input(opts.harness, opts.event, payload)
    root = info["root"]

    if opts.event == "PostToolUse":
        _record_post_tool(root, info["tool"], info["args"], info["error"])
        return _emit(opts.harness, opts.event, None)

    if opts.event == "PreToolUse":
        sub_reason = _check_pre_subagent(root, opts.harness, info["tool"], info["args"])
        if sub_reason:
            return _emit(opts.harness, opts.event, sub_reason)
        for rel in _extract_target_paths(root, info["tool"], info["args"]):
            reason = _check_pre_write(root, opts.harness, rel)
            if reason:
                return _emit(opts.harness, opts.event, reason)
        return _emit(opts.harness, opts.event, None)

    if opts.event == "Stop":
        reason = _check_stop(root, info["stop_active"])
        return _emit(opts.harness, opts.event, reason)

    return 0


if __name__ == "__main__":
    sys.exit(main())
