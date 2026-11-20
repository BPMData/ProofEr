"""Antigravity `run_workflow` script for isolated parallel ProofEr research.

Pass `Args={"piece": "<piece_slug>"}` (reads `proj/<piece>/research/prompts.json`) or
`Args={"piece": "<piece_slug>", "prompts": [{"id": "...", "angle": "...", "prompt": "..."}]}`.
"""
import json
from pathlib import Path

piece = args["piece"]
root = Path(WORKSPACES[0]) if WORKSPACES else Path.cwd()
research_dir = root / "proj" / piece / "research"
workers_dir = research_dir / "workers"
workers_dir.mkdir(parents=True, exist_ok=True)

prompts_list = args.get("prompts")
if prompts_list is None:
    prompts_list = json.loads((research_dir / "prompts.json").read_text(encoding="utf-8"))

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


phase(f"Run {len(prompts_list)} isolated research workers for {piece}")
results = await parallel(prompts_list, run_one)
log(f"Completed {len(results)} research workers into proj/{piece}/research/workers/.")
print(json.dumps([{"id": r["id"], "findings": len(r["findings"]), "sources": len(r["bibliography"])} for r in results], indent=2))
