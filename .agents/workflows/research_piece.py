"""Antigravity `run_workflow` script for isolated parallel ProofEr research.

Pass `Args={"piece": "<piece_slug>"}` (reads `proj/<piece>/research/prompts.json`) or
`Args={"piece": "<piece_slug>", "prompts": [{"id": "...", "angle": "...", "prompt": "..."}]}`.
Writes worker JSONs into `proj/<piece>/research/workers/<round>/` and a deterministic
zero-LLM markdown digest `<round>_digest.md` preserving all disagreements, confidence tags,
and myth checks verbatim.
"""
import json
import re
from pathlib import Path

piece = args["piece"]
round_tag = args.get("round", "pass1")
root = Path(WORKSPACES[0]) if WORKSPACES else Path.cwd()
research_dir = root / "proj" / piece / "research"
workers_dir = research_dir / "workers" / round_tag
workers_dir.mkdir(parents=True, exist_ok=True)

prompts_list = args.get("prompts")
if prompts_list is None:
    prompts_list = json.loads((research_dir / "prompts.json").read_text(encoding="utf-8"))

brief_path = root / "proj" / piece / "brief.md"
brief_head = brief_path.read_text(encoding="utf-8")[:2500] if brief_path.exists() else ""
budget_m = re.search(r"Budget:\s*([a-zA-Z_-]+)", brief_head, re.I)
budget = (args.get("budget") or (budget_m.group(1) if budget_m else "standard")).strip().lower()
override = bool(
    args.get("budget_override")
    or re.search(r"Budget-Override:\s*(approved|yes|true)", brief_head, re.I)
    or (root / "proj" / piece / ".budget_override").exists()
)
if budget == "light" and not override:
    if round_tag != "pass1" or len(prompts_list) > 3:
        raise ValueError(
            f"Budget: light caps automated research at <=3 workers in pass1 "
            f"(requested round={round_tag!r}, workers={len(prompts_list)}). "
            f"Ask the user before overriding via Budget-Override: approved."
        )

SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "angle": {"type": "string"},
        "findings": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "claim": {"type": "string"},
                    "value_or_range": {"type": "string"},
                    "unit": {"type": "string"},
                    "sources": {"type": "array", "items": {"type": "string"}},
                    "disagreements_or_caveats": {"type": "string"},
                    "confidence": {"type": "string"},
                },
                "required": ["claim", "value_or_range", "unit", "sources", "confidence"],
            },
        },
        "myths_checked": {"type": "array", "items": {"type": "string"}},
        "bibliography": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["id", "angle", "findings", "myths_checked", "bibliography"],
}


def _write_digest(target_dir: Path, tag: str, items: list[dict]) -> Path:
    """Write a deterministic markdown digest so the coordinator audits one compact view."""
    lines = [f"# Research Digest: {piece} ({tag})", ""]
    for res in items:
        lines.append(f"## {res.get('id', 'worker')} — {res.get('angle', '')}")
        lines.append("")
        for f in res.get("findings", []):
            srcs = "; ".join(f.get("sources", []))
            caveat = f.get("disagreements_or_caveats", "").strip()
            lines.append(
                f"- **[{f.get('confidence', 'UNKNOWN')}]** {f.get('claim', '')}: "
                f"`{f.get('value_or_range', '')}` ({f.get('unit', '')})"
            )
            if srcs:
                lines.append(f"  - Sources ({len(f.get('sources', []))}): {srcs}")
            if caveat:
                lines.append(f"  - Disagreements / caveats: {caveat}")
        myths = res.get("myths_checked", [])
        if myths:
            lines.append("- **Myths checked:**")
            for m in myths:
                lines.append(f"  - {m}")
        lines.append("")
    digest_path = target_dir / f"{tag}_digest.md"
    digest_path.write_text("\n".join(lines), encoding="utf-8")
    return digest_path


async def run_one(item):
    worker_prompt = (
        f"You are an isolated ProofEr research worker investigating: {item['id']} ({item.get('angle', 'primary')}).\n"
        "You have ZERO prior conversation context—follow ONLY this brief and verify every fact with search_web.\n\n"
        f"{item['prompt']}\n\n"
        "Rules:\n"
        "- Primary/authoritative sources only (peer-reviewed papers, university extensions, official standards/agencies, named historians).\n"
        "- Ban SEO blogs and unattributed summaries.\n"
        "- Provide >= 2 independent sources per quantitative figure whenever possible; preserve disagreements as explicit ranges/notes.\n"
        "- Tag uncertain or single-source claims as `LOW CONFIDENCE`.\n"
        "- Return ONLY compact structured JSON matching the required schema."
    )
    res = await agent(
        worker_prompt,
        schema=SCHEMA,
        role=f"Research {item['id']}",
        type_name="self",
    )
    out_json = workers_dir / f"{item['id']}.json"
    out_json.write_text(json.dumps(res, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return res


phase(f"Run {len(prompts_list)} isolated research workers for {piece} ({round_tag})")
results = await parallel(prompts_list, run_one)
digest = _write_digest(workers_dir, round_tag, results)
log(f"Completed {len(results)} research workers into proj/{piece}/research/workers/{round_tag}/ (digest: {digest.name}).")
print(json.dumps({
    "digest": str(digest.relative_to(root)),
    "workers": [{"id": r["id"], "findings": len(r["findings"]), "sources": len(r["bibliography"])} for r in results],
}, indent=2))
