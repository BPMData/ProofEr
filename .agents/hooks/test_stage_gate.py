"""End-to-end unit tests for .agents/hooks/stage_gate.py across Antigravity, Claude Code, and Codex CLI."""
import json
import os
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path

GATE = Path(__file__).resolve().parent / "stage_gate.py"


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
        (self.root / "proj" / "clay" / "research" / "workers").mkdir(parents=True)
        (self.root / "proj" / "clay" / "stills").mkdir(parents=True)
        (self.root / "proj" / "clay" / "qa").mkdir(parents=True)
        (self.root / "pieces").mkdir(parents=True)
        (self.root / "proj" / "clay" / "brief.md").write_text(
            "# Brief: Clay\n\nStage: research · Mode: autonomous\n",
            encoding="utf-8",
        )

    def tearDown(self):
        self.tmp.cleanup()

    def test_antigravity_autonomous_gates_and_receipts(self):
        fig_path = "proj/clay/figures.md"
        # 1. Blocked before prompts.md
        rc, out, _ = _run_gate("antigravity", "PreToolUse", {
            "cwd": str(self.root),
            "toolCall": {"name": "write_file", "args": {"Path": fig_path}},
        })
        self.assertEqual(rc, 0)
        self.assertEqual(json.loads(out)["decision"], "deny")

        # 2. Add prompts.md + 2 worker files, still blocked without run_workflow receipt
        (self.root / "proj" / "clay" / "research" / "prompts.md").write_text("x" * 150, encoding="utf-8")
        (self.root / "proj" / "clay" / "research" / "workers" / "a.json").write_text("{" + "x" * 90 + "}", encoding="utf-8")
        (self.root / "proj" / "clay" / "research" / "workers" / "b.json").write_text("{" + "x" * 90 + "}", encoding="utf-8")
        rc, out, _ = _run_gate("antigravity", "PreToolUse", {
            "cwd": str(self.root),
            "toolCall": {"name": "write_file", "args": {"Path": fig_path}},
        })
        self.assertEqual(json.loads(out)["decision"], "deny")

        # 3. Record run_workflow receipt -> unlocked
        _run_gate("antigravity", "PostToolUse", {
            "cwd": str(self.root),
            "toolCall": {"name": "run_workflow", "args": {}},
        })
        rc, out, _ = _run_gate("antigravity", "PreToolUse", {
            "cwd": str(self.root),
            "toolCall": {"name": "write_file", "args": {"Path": fig_path}},
        })
        self.assertEqual(json.loads(out)["decision"], "allow")

        # 4. Layout / stills blocked until figures.md has >= 2 figure rows
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

        # 5. pieces/clay.html blocked until APPROVED + 3 HTML stills + 3 PNGs read + critique.md
        (self.root / "proj" / "clay" / "layout.md").write_text("Stage: layout · APPROVED\n", encoding="utf-8")
        for s in ("concept-a", "concept-b", "concept-c"):
            (self.root / "proj" / "clay" / "stills" / f"{s}.html").write_text("<html></html>", encoding="utf-8")
            (self.root / "proj" / "clay" / "stills" / f"{s}.png").write_bytes(b"PNG")
        rc, out, _ = _run_gate("antigravity", "PreToolUse", {
            "cwd": str(self.root),
            "toolCall": {"name": "write_file", "args": {"Path": "pieces/clay.html"}},
        })
        self.assertEqual(json.loads(out)["decision"], "deny")

        for s in ("concept-a", "concept-b", "concept-c"):
            _run_gate("antigravity", "PostToolUse", {
                "cwd": str(self.root),
                "toolCall": {"name": "read_file", "args": {"Path": f"proj/clay/stills/{s}.png"}},
            })
        (self.root / "proj" / "clay" / "stills" / "critique.md").write_text("Winner: concept-b. " + "detail " * 25, encoding="utf-8")
        rc, out, _ = _run_gate("antigravity", "PreToolUse", {
            "cwd": str(self.root),
            "toolCall": {"name": "write_file", "args": {"Path": "pieces/clay.html"}},
        })
        self.assertEqual(json.loads(out)["decision"], "allow")

        # 6. Stop blocked until check_offline.py + final desktop/phone PNGs inspected
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
        (self.root / "proj" / "clay" / "research" / "workers" / "a.md").write_text("x" * 100, encoding="utf-8")
        (self.root / "proj" / "clay" / "research" / "workers" / "b.md").write_text("x" * 100, encoding="utf-8")
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


if __name__ == "__main__":
    unittest.main()
