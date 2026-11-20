"""End-to-end unit tests for .agents/hooks/stage_gate.py across Antigravity, Claude Code, and Codex CLI."""
import ast
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import tomllib
import unittest
from pathlib import Path

GATE = Path(__file__).resolve().parent / "stage_gate.py"
REPO_ROOT = Path(__file__).resolve().parents[2]


def _run_gate(harness: str, event: str, payload: dict) -> tuple[int, str, str]:
    p = subprocess.run(
        [sys.executable, str(GATE), "--harness", harness, "--event", event],
        input=json.dumps(payload),
        text=True,
        capture_output=True,
    )
    return p.returncode, p.stdout.strip(), p.stderr.strip()


class StageGateTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "proj" / "clay" / "research" / "workers" / "pass1").mkdir(parents=True)
        (self.root / "proj" / "clay" / "stills").mkdir(parents=True)
        (self.root / "proj" / "clay" / "qa").mkdir(parents=True)
        (self.root / "pieces").mkdir(parents=True)
        (self.root / "proj" / "clay" / "brief.md").write_text(
            "# Brief: Clay\n\nStage: interview\n",
            encoding="utf-8",
        )

    def tearDown(self):
        self.tmp.cleanup()

    def test_interview_pause_and_full_hybrid_pipeline(self):
        fig_path = "proj/clay/figures.md"
        # 1. During interview: Stop is allowed (so user can answer questions), but writing figures.md is blocked
        rc, out, _ = _run_gate("antigravity", "Stop", {
            "cwd": str(self.root),
            "terminationReason": "NO_TOOL_CALL",
            "continuationActive": False,
        })
        self.assertEqual(json.loads(out), {})
        rc, out, _ = _run_gate("antigravity", "PreToolUse", {
            "cwd": str(self.root),
            "toolCall": {"name": "write_file", "args": {"Path": fig_path}},
        })
        self.assertEqual(json.loads(out)["decision"], "deny")
        self.assertIn("interview", json.loads(out)["reason"])

        # 2. Advance brief to Stage: research -> still blocked until prompts.md + >=2 workers + receipt exist
        (self.root / "proj" / "clay" / "brief.md").write_text("# Brief: Clay\n\nStage: research\n", encoding="utf-8")
        (self.root / "proj" / "clay" / "research" / "prompts.md").write_text("x" * 150, encoding="utf-8")
        (self.root / "proj" / "clay" / "research" / "workers" / "pass1" / "a.json").write_text("{" + "x" * 90 + "}", encoding="utf-8")
        (self.root / "proj" / "clay" / "research" / "workers" / "pass1" / "b.json").write_text("{" + "x" * 90 + "}", encoding="utf-8")
        rc, out, _ = _run_gate("antigravity", "PreToolUse", {
            "cwd": str(self.root),
            "toolCall": {"name": "write_file", "args": {"Path": fig_path}},
        })
        self.assertEqual(json.loads(out)["decision"], "deny")

        # 3. Record run_workflow receipt -> figures.md unlocked
        _run_gate("antigravity", "PostToolUse", {
            "cwd": str(self.root),
            "toolCall": {"name": "run_workflow", "args": {}},
        })
        rc, out, _ = _run_gate("antigravity", "PreToolUse", {
            "cwd": str(self.root),
            "toolCall": {"name": "write_file", "args": {"Path": fig_path}},
        })
        self.assertEqual(json.loads(out)["decision"], "allow")

        # 4. Layout / stills blocked until figures.md has >= 2 figure rows; Stop still allowed while waiting for outline approval
        rc, out, _ = _run_gate("antigravity", "PreToolUse", {
            "cwd": str(self.root),
            "toolCall": {"name": "write_file", "args": {"Path": "proj/clay/layout.md"}},
        })
        self.assertEqual(json.loads(out)["decision"], "deny")
        (self.root / fig_path).write_text("| F01 | a | b |\n| F02 | c | d |\n", encoding="utf-8")
        rc, out, _ = _run_gate("antigravity", "PreToolUse", {
            "cwd": str(self.root),
            "toolCall": {"name": "write_file", "args": {"Path": "proj/clay/layout.md"}},
        })
        self.assertEqual(json.loads(out)["decision"], "allow")
        rc, out, _ = _run_gate("antigravity", "Stop", {
            "cwd": str(self.root),
            "terminationReason": "NO_TOOL_CALL",
            "continuationActive": False,
        })
        self.assertEqual(json.loads(out), {})

        # 5. pieces/clay.html blocked until APPROVED + mockup HTML/PNG inspected + critique.md
        (self.root / "proj" / "clay" / "layout.md").write_text("Stage: layout · APPROVED\n", encoding="utf-8")
        (self.root / "proj" / "clay" / "stills" / "concept-a.html").write_text("<html></html>", encoding="utf-8")
        (self.root / "proj" / "clay" / "stills" / "concept-a.png").write_bytes(b"PNG")
        rc, out, _ = _run_gate("antigravity", "PreToolUse", {
            "cwd": str(self.root),
            "toolCall": {"name": "write_file", "args": {"Path": "pieces/clay.html"}},
        })
        self.assertEqual(json.loads(out)["decision"], "deny")

        _run_gate("antigravity", "PostToolUse", {
            "cwd": str(self.root),
            "toolCall": {"name": "read_file", "args": {"Path": "proj/clay/stills/concept-a.png"}},
        })
        (self.root / "proj" / "clay" / "stills" / "critique.md").write_text("Notes: " + "ok " * 35, encoding="utf-8")
        rc, out, _ = _run_gate("antigravity", "PreToolUse", {
            "cwd": str(self.root),
            "toolCall": {"name": "write_file", "args": {"Path": "pieces/clay.html"}},
        })
        self.assertEqual(json.loads(out)["decision"], "allow")

        # 6. Once pieces/clay.html exists, Stop blocked until check_offline.py + desktop & phone PNGs inspected
        piece_html = self.root / "pieces" / "clay.html"
        piece_html.write_text("<html>final</html>", encoding="utf-8")
        rc, out, _ = _run_gate("antigravity", "Stop", {
            "cwd": str(self.root),
            "terminationReason": "NO_TOOL_CALL",
            "continuationActive": False,
        })
        self.assertEqual(json.loads(out)["decision"], "continue")

        time.sleep(0.01)
        _run_gate("antigravity", "PostToolUse", {
            "cwd": str(self.root),
            "toolCall": {"name": "run_command", "args": {"CommandLine": "python3 tools/check_offline.py"}},
        })
        for shot in ("desktop.png", "phone.png"):
            p = self.root / "proj" / "clay" / "qa" / shot
            p.write_bytes(b"PNG")
            _run_gate("antigravity", "PostToolUse", {
                "cwd": str(self.root),
                "toolCall": {"name": "read_file", "args": {"Path": f"proj/clay/qa/{shot}"}},
            })

        rc, out, _ = _run_gate("antigravity", "Stop", {
            "cwd": str(self.root),
            "terminationReason": "NO_TOOL_CALL",
            "continuationActive": False,
        })
        self.assertEqual(json.loads(out), {})

        # Loop guard: continuationActive=True never blocks
        os.utime(piece_html, None)
        rc, out, _ = _run_gate("antigravity", "Stop", {
            "cwd": str(self.root),
            "terminationReason": "NO_TOOL_CALL",
            "continuationActive": True,
        })
        self.assertEqual(json.loads(out), {})

    def test_claude_and_codex_exit2_blocking_and_patch_parsing(self):
        (self.root / "proj" / "clay" / "brief.md").write_text("# Brief: Clay\n\nStage: research\n", encoding="utf-8")
        # Claude Code denies Write to figures.md with exit code 2 + stderr
        rc, _, err = _run_gate("claude", "PreToolUse", {
            "cwd": str(self.root),
            "tool_name": "Write",
            "tool_input": {"file_path": str(self.root / "proj" / "clay" / "figures.md")},
        })
        self.assertEqual(rc, 2)
        self.assertIn("prompts.md", err)

        # Claude Code Agent PostToolUse receipt works cleanly
        (self.root / "proj" / "clay" / "research" / "prompts.md").write_text("x" * 150, encoding="utf-8")
        (self.root / "proj" / "clay" / "research" / "workers" / "pass1" / "a.md").write_text("x" * 100, encoding="utf-8")
        (self.root / "proj" / "clay" / "research" / "workers" / "pass1" / "b.md").write_text("x" * 100, encoding="utf-8")
        _run_gate("claude", "PostToolUse", {
            "cwd": str(self.root),
            "tool_name": "Agent",
            "tool_input": {},
            "tool_response": {"is_error": False},
        })
        rc, _, err = _run_gate("claude", "PreToolUse", {
            "cwd": str(self.root),
            "tool_name": "Write",
            "tool_input": {"file_path": "proj/clay/figures.md"},
        })
        self.assertEqual(rc, 0, err)

        # Codex CLI blocks apply_patch targeting pieces/clay.html before layout APPROVED
        rc, _, err = _run_gate("codex", "PreToolUse", {
            "cwd": str(self.root),
            "tool_name": "apply_patch",
            "tool_input": {"patch": "*** Begin Patch\n*** Add File: pieces/clay.html\n+<html></html>\n"},
        })
        self.assertEqual(rc, 2)
        self.assertIn("layout.md", err)

        # Codex CLI Stop blocks incomplete piece with exit 2 unless stop_hook_active=True
        (self.root / "pieces" / "clay.html").write_text("<html></html>", encoding="utf-8")
        rc, _, err = _run_gate("codex", "Stop", {"cwd": str(self.root), "stop_hook_active": False})
        self.assertEqual(rc, 2)
        rc, _, _ = _run_gate("codex", "Stop", {"cwd": str(self.root), "stop_hook_active": True})
        self.assertEqual(rc, 0)

    def test_declared_hook_commands_execute_cleanly(self):
        ag = json.loads((REPO_ROOT / ".agents" / "hooks.json").read_text(encoding="utf-8"))
        cl = json.loads((REPO_ROOT / ".claude" / "settings.json").read_text(encoding="utf-8"))
        cx = json.loads((REPO_ROOT / ".codex" / "hooks.json").read_text(encoding="utf-8"))
        cx_cfg = tomllib.loads((REPO_ROOT / ".codex" / "config.toml").read_text(encoding="utf-8"))
        self.assertTrue(cx_cfg.get("features", {}).get("hooks"))

        env = {**os.environ, "CLAUDE_PROJECT_DIR": str(REPO_ROOT)}

        def exec_hooks(groups_by_event, sample_fn):
            for event, groups in groups_by_event.items():
                for grp in groups:
                    for hk in grp.get("hooks", []):
                        cmd = hk["command"]
                        payload = sample_fn(event)
                        p = subprocess.run(
                            cmd, shell=True, cwd=str(REPO_ROOT), env=env,
                            input=json.dumps(payload), text=True, capture_output=True,
                        )
                        self.assertIn(p.returncode, (0, 2), f"{event} `{cmd}` failed ({p.returncode}): {p.stderr}")
                        yield event, cmd, p

        # Antigravity declared commands
        for event, cmd, p in exec_hooks(ag["proofer-stage-gate"], lambda ev: (
            {"cwd": str(self.root), "toolCall": {"name": "write_file", "args": {"Path": "proj/clay/figures.md"}}}
            if ev == "PreToolUse" else
            {"cwd": str(self.root), "toolCall": {"name": "run_workflow", "args": {}}}
            if ev == "PostToolUse" else
            {"cwd": str(self.root), "terminationReason": "NO_TOOL_CALL", "continuationActive": False}
        )):
            data = json.loads(p.stdout.strip())
            if event == "PreToolUse":
                self.assertEqual(data["decision"], "deny", cmd)

        # Claude Code declared commands (includes stage_log.py + stage_gate.py)
        for event, cmd, p in exec_hooks(cl["hooks"], lambda ev: (
            {"cwd": str(self.root), "tool_name": "Write", "tool_input": {"file_path": "proj/clay/figures.md"}}
            if ev == "PreToolUse" else
            {"cwd": str(self.root), "tool_name": "Read", "tool_input": {"file_path": "brief/CRAFT.md"}}
            if ev == "PostToolUse" else
            {"cwd": str(self.root), "stop_hook_active": False}
        )):
            if event == "PreToolUse":
                self.assertEqual(p.returncode, 2, cmd)

        # Codex CLI declared commands
        for event, cmd, p in exec_hooks(cx["hooks"], lambda ev: (
            {"cwd": str(self.root), "tool_name": "apply_patch", "tool_input": {"patch": "*** Add File: proj/clay/figures.md\n"}}
            if ev == "PreToolUse" else
            {"cwd": str(self.root), "tool_name": "spawn_agent", "tool_input": {}}
            if ev == "PostToolUse" else
            {"cwd": str(self.root), "stop_hook_active": False}
        )):
            if event == "PreToolUse":
                self.assertEqual(p.returncode, 2, cmd)

    def test_skills_workflow_taste_and_eval_budget_invariants(self):
        # 1. Antigravity workflow compiles cleanly with top-level await support
        wf_path = REPO_ROOT / ".agents" / "workflows" / "research_piece.py"
        compile(wf_path.read_text(encoding="utf-8"), str(wf_path), "exec", flags=ast.PyCF_ALLOW_TOP_LEVEL_AWAIT)

        # 2. All skills define non-empty YAML frontmatter name and description
        skill_files = list((REPO_ROOT / ".agents" / "skills").glob("*/SKILL.md")) + list(
            (REPO_ROOT / ".claude" / "skills").glob("*/SKILL.md")
        )
        self.assertGreaterEqual(len(skill_files), 4)
        for sf in skill_files:
            txt = sf.read_text(encoding="utf-8")
            m = re.match(r"^---\s*\n(.*?)\n---\s*\n", txt, re.S)
            self.assertIsNotNone(m, f"Missing YAML frontmatter in {sf}")
            fm = m.group(1)
            self.assertRegex(fm, re.compile(r"^name:\s*\S+", re.M), f"Missing name in {sf}")
            self.assertRegex(fm, re.compile(r"^description:\s*\S+", re.M), f"Missing description in {sf}")

        # 3. house.md taste items preserve `^T\d+ · (strong|soft) ·` grammar
        house = (REPO_ROOT / "brief" / "taste" / "house.md").read_text(encoding="utf-8")
        t_lines = [ln for ln in house.splitlines() if re.match(r"^T\d+\b", ln)]
        self.assertGreaterEqual(len(t_lines), 10)
        for ln in t_lines:
            self.assertRegex(ln, r"^T\d+ · (strong|soft) · ")

        # 4. Always-loaded session docs stay lean for eval_new_piece.py context budget
        always_bytes = sum(
            (REPO_ROOT / f).stat().st_size for f in ("CLAUDE.md", "AGENTS.md", "STATUS.md")
        )
        self.assertLess(always_bytes, 14000)


if __name__ == "__main__":
    unittest.main()
