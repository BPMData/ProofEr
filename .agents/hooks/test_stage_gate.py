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
        # Self-critique alone (without an isolated fresh-eyes reviewer subagent receipt) is blocked
        (self.root / "proj" / "clay" / "stills" / "review.md").write_text("Notes: " + "ok " * 35, encoding="utf-8")
        rc, out, _ = _run_gate("antigravity", "PreToolUse", {
            "cwd": str(self.root),
            "toolCall": {"name": "write_file", "args": {"Path": "pieces/clay.html"}},
        })
        self.assertEqual(json.loads(out)["decision"], "deny")
        self.assertIn("Fresh-eyes", json.loads(out)["reason"])

        # Recording an isolated fresh-eyes reviewer subagent unlocks building pieces/clay.html
        _run_gate("antigravity", "PostToolUse", {
            "cwd": str(self.root),
            "toolCall": {
                "name": "invoke_subagent",
                "args": {"Role": "Fresh-eyes Reviewer", "Prompt": "Review proj/clay/stills/ per CRAFT.md §12"},
            },
        })
        rc, out, _ = _run_gate("antigravity", "PreToolUse", {
            "cwd": str(self.root),
            "toolCall": {"name": "write_file", "args": {"Path": "pieces/clay.html"}},
        })
        self.assertEqual(json.loads(out)["decision"], "allow")

        # 6. Once pieces/clay.html exists, Stop blocked until check_offline.py + desktop & phone PNGs + fresh-eyes qa/review.md
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
        # Still blocked until fresh-eyes QA reviewer runs for the current HTML
        rc, out, _ = _run_gate("antigravity", "Stop", {
            "cwd": str(self.root),
            "terminationReason": "NO_TOOL_CALL",
            "continuationActive": False,
        })
        self.assertEqual(json.loads(out)["decision"], "continue")
        self.assertIn("qa/review.md", json.loads(out)["reason"])

        _run_gate("antigravity", "PostToolUse", {
            "cwd": str(self.root),
            "toolCall": {
                "name": "invoke_subagent",
                "args": {"Role": "Fresh-eyes QA Reviewer", "Prompt": "Review proj/clay/qa/"},
            },
        })
        (self.root / "proj" / "clay" / "qa" / "review.md").write_text("QA review: " + "ok " * 35, encoding="utf-8")

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

        def exec_hooks(groups_by_event, sample_fn, run_cwd=REPO_ROOT):
            for event, groups in groups_by_event.items():
                for grp in groups:
                    for hk in grp.get("hooks", []):
                        cmd = hk["command"]
                        payload = sample_fn(event)
                        p = subprocess.run(
                            cmd, shell=True, cwd=str(run_cwd), env=env,
                            input=json.dumps(payload), text=True, capture_output=True,
                        )
                        self.assertIn(p.returncode, (0, 2), f"{event} `{cmd}` failed ({p.returncode}): {p.stderr}")
                        yield event, cmd, p

        # Antigravity declared commands (must work from both REPO_ROOT and REPO_ROOT/.agents)
        for run_cwd in (REPO_ROOT, REPO_ROOT / ".agents"):
            for event, cmd, p in exec_hooks(ag["proofer-stage-gate"], lambda ev: (
                {"cwd": str(self.root), "toolCall": {"name": "write_file", "args": {"Path": "proj/clay/figures.md"}}}
                if ev == "PreToolUse" else
                {"cwd": str(self.root), "toolCall": {"name": "run_workflow", "args": {}}}
                if ev == "PostToolUse" else
                {"cwd": str(self.root), "terminationReason": "NO_TOOL_CALL", "continuationActive": False}
            ), run_cwd=run_cwd):
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

    def test_stop_ignores_untouched_committed_pieces_in_git_repo(self):
        git_root = Path(self.tmp.name) / "repo"
        (git_root / "proj" / "oldpiece").mkdir(parents=True)
        (git_root / "pieces").mkdir(parents=True)
        (git_root / "proj" / "oldpiece" / "brief.md").write_text("# Brief: Old\n\nStage: build\n", encoding="utf-8")
        (git_root / "pieces" / "oldpiece.html").write_text("<html>old</html>", encoding="utf-8")
        subprocess.run(["git", "init", "-q"], cwd=str(git_root), check=True)
        subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=str(git_root), check=True)
        subprocess.run(["git", "config", "user.name", "Test"], cwd=str(git_root), check=True)
        subprocess.run(["git", "add", "."], cwd=str(git_root), check=True)
        subprocess.run(["git", "commit", "-q", "-m", "init"], cwd=str(git_root), check=True)

        # Untouched committed piece does not block Stop
        rc, out, _ = _run_gate("antigravity", "Stop", {
            "cwd": str(git_root),
            "terminationReason": "NO_TOOL_CALL",
            "continuationActive": False,
        })
        self.assertEqual(rc, 0)
        self.assertEqual(json.loads(out), {})

        # Modifying the piece triggers Stop QA checks
        (git_root / "pieces" / "oldpiece.html").write_text("<html>edited</html>", encoding="utf-8")
        rc, out, _ = _run_gate("antigravity", "Stop", {
            "cwd": str(git_root),
            "terminationReason": "NO_TOOL_CALL",
            "continuationActive": False,
        })
        self.assertEqual(json.loads(out)["decision"], "continue")

    def test_offline_check_on_one_piece_does_not_trip_another(self):
        """Regression (Nov 22, 2026): running check_offline.py while editing piece A re-stamped committed
        piece B's receipt, so the Stop gate demanded screenshots of B and B's receipt showed as uncommitted."""
        git_root = Path(self.tmp.name) / "repo2"
        for name in ("active", "other"):
            (git_root / "proj" / name).mkdir(parents=True)
            (git_root / "proj" / name / "brief.md").write_text(f"# Brief\n\nStage: build\n", encoding="utf-8")
            (git_root / "proj" / name / ".offline_checked.json").write_text('{"ts": 1}\n', encoding="utf-8")
        (git_root / "pieces").mkdir(parents=True)
        for name in ("active", "other"):
            (git_root / "pieces" / f"{name}.html").write_text("<html></html>", encoding="utf-8")
        for cmd in (["git", "init", "-q"], ["git", "config", "user.email", "t@example.com"],
                    ["git", "config", "user.name", "T"], ["git", "add", "."], ["git", "commit", "-q", "-m", "init"]):
            subprocess.run(cmd, cwd=str(git_root), check=True)

        (git_root / "pieces" / "active.html").write_text("<html>edited</html>", encoding="utf-8")
        rc, _, _ = _run_gate("claude", "PostToolUse", {
            "cwd": str(git_root), "tool_name": "Bash",
            "tool_input": {"command": "python3 tools/check_offline.py"}, "tool_response": {},
        })
        self.assertEqual(rc, 0)
        other_stamp = json.loads((git_root / "proj" / "other" / ".offline_checked.json").read_text())
        self.assertEqual(other_stamp, {"ts": 1}, "untouched piece's receipt must not be rewritten")
        active_stamp = json.loads((git_root / "proj" / "active" / ".offline_checked.json").read_text())
        self.assertGreater(active_stamp["ts"], 1)

        # Stop may still ask for QA on the active piece, but never on the untouched one.
        rc, out, err = _run_gate("claude", "Stop", {"cwd": str(git_root), "stop_hook_active": False})
        self.assertNotIn("pieces/other.html", out + err)

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

    def test_budget_model_caps_and_light_overflow_gate(self):
        # 1. Claude Code & Codex block fable and >high effort, while allowing opus medium & sonnet
        rc, _, err = _run_gate("claude", "PreToolUse", {
            "cwd": str(self.root),
            "tool_name": "Agent",
            "tool_input": {"model": "fable-1", "prompt": "Research clay"},
        })
        self.assertEqual(rc, 2)
        self.assertIn("fable", err.lower())

        rc, _, err = _run_gate("codex", "PreToolUse", {
            "cwd": str(self.root),
            "tool_name": "spawn_agent",
            "tool_input": {"reasoning_effort": "xhigh", "prompt": "Research clay"},
        })
        self.assertEqual(rc, 2)
        self.assertIn("high", err.lower())

        rc, _, err = _run_gate("claude", "PreToolUse", {
            "cwd": str(self.root),
            "tool_name": "Agent",
            "tool_input": {"model": "opus", "effort": "medium", "prompt": "Synthesize"},
        })
        self.assertEqual(rc, 0, err)

        # Antigravity model strings remain unrestricted for now
        rc, out, _ = _run_gate("antigravity", "PreToolUse", {
            "cwd": str(self.root),
            "toolCall": {"name": "invoke_subagent", "args": {"Model": "pro", "Prompt": "Research"}},
        })
        self.assertEqual(rc, 0)
        self.assertEqual(json.loads(out)["decision"], "allow")

        # 2. Budget: light blocks >3 workers or gap_fill until Budget-Override: approved
        (self.root / "proj" / "clay" / "brief.md").write_text(
            "# Brief: Clay\n\nStage: research · Budget: light\n",
            encoding="utf-8",
        )
        (self.root / "proj" / "clay" / "research" / "prompts.json").write_text(
            json.dumps([{"id": f"q{i}", "prompt": "x"} for i in range(4)]),
            encoding="utf-8",
        )
        rc, out, _ = _run_gate("antigravity", "PreToolUse", {
            "cwd": str(self.root),
            "toolCall": {
                "name": "run_workflow",
                "args": {"ScriptPath": ".agents/workflows/research_piece.py", "Args": {"piece": "clay", "round": "pass1"}},
            },
        })
        self.assertEqual(json.loads(out)["decision"], "deny")
        self.assertIn("Light budget gate", json.loads(out)["reason"])

        (self.root / "proj" / "clay" / "brief.md").write_text(
            "# Brief: Clay\n\nStage: research · Budget: light · Budget-Override: approved\n",
            encoding="utf-8",
        )
        rc, out, _ = _run_gate("antigravity", "PreToolUse", {
            "cwd": str(self.root),
            "toolCall": {
                "name": "run_workflow",
                "args": {"ScriptPath": ".agents/workflows/research_piece.py", "Args": {"piece": "clay", "round": "gap_fill"}},
            },
        })
        self.assertEqual(json.loads(out)["decision"], "allow")

    def test_stop_skips_qa_on_hash_match_or_docs_only_edits(self):
        git_root = Path(self.tmp.name) / "repo_hash"
        (git_root / "proj" / "clay" / "qa").mkdir(parents=True)
        (git_root / "pieces").mkdir(parents=True)
        (git_root / "proj" / "clay" / "brief.md").write_text("# Brief: Clay\n\nStage: build\n", encoding="utf-8")
        (git_root / "proj" / "clay" / "STATUS.md").write_text("- Initial\n", encoding="utf-8")
        html = git_root / "pieces" / "clay.html"
        html.write_text("<html>v1</html>", encoding="utf-8")
        for cmd in (["git", "init", "-q"], ["git", "config", "user.email", "t@example.com"],
                    ["git", "config", "user.name", "T"], ["git", "add", "."], ["git", "commit", "-q", "-m", "init"]):
            subprocess.run(cmd, cwd=str(git_root), check=True)

        # 1. Docs-only edit (STATUS.md) never triggers Stop QA on unchanged committed HTML
        (git_root / "proj" / "clay" / "STATUS.md").write_text("- Note added\n", encoding="utf-8")
        rc, out, _ = _run_gate("antigravity", "Stop", {
            "cwd": str(git_root), "terminationReason": "NO_TOOL_CALL", "continuationActive": False,
        })
        self.assertEqual(rc, 0)
        self.assertEqual(json.loads(out), {})

        # 2. Record check_offline + 2 QA PNGs + fresh-eyes QA review for html bytes, then bump html mtime without changing bytes
        html.write_text("<html>v2</html>", encoding="utf-8")
        _run_gate("antigravity", "PostToolUse", {
            "cwd": str(git_root),
            "toolCall": {"name": "run_command", "args": {"CommandLine": "python3 tools/check_offline.py"}},
        })
        for shot in ("desktop.png", "phone.png"):
            (git_root / "proj" / "clay" / "qa" / shot).write_bytes(b"PNG")
            _run_gate("antigravity", "PostToolUse", {
                "cwd": str(git_root),
                "toolCall": {"name": "read_file", "args": {"Path": f"proj/clay/qa/{shot}"}},
            })
        _run_gate("antigravity", "PostToolUse", {
            "cwd": str(git_root),
            "toolCall": {
                "name": "invoke_subagent",
                "args": {"Role": "Fresh-eyes QA Reviewer", "Prompt": "Review proj/clay/qa/"},
            },
        })
        (git_root / "proj" / "clay" / "qa" / "review.md").write_text("QA review: " + "ok " * 35, encoding="utf-8")
        time.sleep(0.02)
        os.utime(html, None)
        rc, out, _ = _run_gate("antigravity", "Stop", {
            "cwd": str(git_root), "terminationReason": "NO_TOOL_CALL", "continuationActive": False,
        })
        self.assertEqual(json.loads(out), {}, "mtime bump with identical sha256 must not re-trigger Stop QA")

        # 3. Changing actual HTML bytes still demands fresh offline check + PNG QA
        html.write_text("<html>v3-changed</html>", encoding="utf-8")
        rc, out, _ = _run_gate("antigravity", "Stop", {
            "cwd": str(git_root), "terminationReason": "NO_TOOL_CALL", "continuationActive": False,
        })
        self.assertEqual(json.loads(out)["decision"], "continue")


if __name__ == "__main__":
    unittest.main()
