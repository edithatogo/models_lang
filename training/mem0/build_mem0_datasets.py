"""Build bootstrap mem0 datasets for LFM fact extraction and ColBERT retrieval."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


DEFAULT_OUTPUT_DIR = Path("training/mem0/datasets/bootstrap")
FACT_EXTRACTION_JSONL = "fact_extraction.jsonl"
RETRIEVAL_TRIPLETS_JSONL = "retrieval_triplets.jsonl"
SIDECAR_DOCUMENTS_JSONL = "sidecar_documents.jsonl"
MANIFEST_JSON = "manifest.json"


@dataclass(frozen=True)
class MemoryScenario:
    id: str
    user_message: str
    assistant_response: str
    facts: tuple[str, ...]
    queries: tuple[str, ...]
    distractor_facts: tuple[str, ...]


@dataclass(frozen=True)
class DatasetBuildResult:
    output_dir: Path
    fact_records: int
    retrieval_triplets: int
    sidecar_documents: int


SYSTEM_PROMPT = (
    "Extract durable user memories from the conversation. "
    "Return strict JSON with an extracted_facts array of strings only."
)


DEFAULT_SCENARIOS: tuple[MemoryScenario, ...] = (
    MemoryScenario(
        id="timezone",
        user_message="I am in Australia/Sydney, so schedule anything for my local time.",
        assistant_response="I will use Australia/Sydney for scheduling and date calculations.",
        facts=("The user is in the Australia/Sydney timezone.",),
        queries=("What timezone should be used for the user?", "Where is the user's local time based?"),
        distractor_facts=("The user prefers responses in Spanish.",),
    ),
    MemoryScenario(
        id="repo_workflow",
        user_message="For repo work, inspect the files first and then make the change.",
        assistant_response="I will read the repo state before editing and verify after changes.",
        facts=("For repo work, the user wants files inspected before changes are made.",),
        queries=("How should repo changes be approached?", "What should happen before editing code?"),
        distractor_facts=("The user wants every answer to include a poem.",),
    ),
    MemoryScenario(
        id="windows_shell",
        user_message="This machine is Windows, and PowerShell is the normal shell.",
        assistant_response="I will use Windows and PowerShell paths and commands by default.",
        facts=("The user's normal working environment is Windows with PowerShell.",),
        queries=("What shell should commands prefer?", "What operating system is the workspace on?"),
        distractor_facts=("The workspace is a Linux-only environment.",),
    ),
    MemoryScenario(
        id="mem0_colbert",
        user_message="Use LFM2-ColBERT as the mem0 retrieval model, not a generic embedding model.",
        assistant_response="I will route mem0 retrieval through the LFM2-ColBERT sidecar and MaxSim scoring.",
        facts=("mem0 retrieval should use LFM2-ColBERT with a sidecar and MaxSim scoring.",),
        queries=("Which model should mem0 retrieval use?", "How should mem0 search be scored?"),
        distractor_facts=("mem0 retrieval should use a single-vector OpenAI embedding endpoint.",),
    ),
    MemoryScenario(
        id="concise_final",
        user_message="Keep final answers concise and tell me what changed and what passed.",
        assistant_response="I will summarize the change, verification, and any blockers without extra fluff.",
        facts=("The user prefers concise final answers with changes, verification, and blockers.",),
        queries=("How should final answers be written?", "What should the summary include?"),
        distractor_facts=("The user prefers long essays with broad background context.",),
    ),
)


def render_chat_record(scenario: MemoryScenario) -> dict[str, object]:
    output = json.dumps({"extracted_facts": list(scenario.facts)}, separators=(",", ":"))
    text = (
        "<|im_start|>system\n"
        f"{SYSTEM_PROMPT}<|im_end|>\n"
        "<|im_start|>user\n"
        f"{scenario.user_message}<|im_end|>\n"
        "<|im_start|>assistant\n"
        f"{output}<|im_end|>"
    )
    return {
        "id": scenario.id,
        "text": text,
        "conversation_turn": {
            "user_message": scenario.user_message,
            "assistant_response": scenario.assistant_response,
        },
        "extracted_facts": list(scenario.facts),
    }


def render_sidecar_documents(scenarios: Iterable[MemoryScenario]) -> list[dict[str, object]]:
    documents: list[dict[str, object]] = []
    for scenario in scenarios:
        for index, fact in enumerate(scenario.facts, start=1):
            documents.append(
                {
                    "id": f"{scenario.id}-fact-{index}",
                    "text": fact,
                    "metadata": {"scenario_id": scenario.id, "source": "bootstrap"},
                }
            )
    return documents


def render_retrieval_triplets(scenarios: Iterable[MemoryScenario]) -> list[dict[str, object]]:
    triplets: list[dict[str, object]] = []
    for scenario in scenarios:
        positive = scenario.facts[0]
        for query_index, query in enumerate(scenario.queries, start=1):
            negative = scenario.distractor_facts[(query_index - 1) % len(scenario.distractor_facts)]
            triplets.append(
                {
                    "id": f"{scenario.id}-query-{query_index}",
                    "query": query,
                    "positive": positive,
                    "negative": negative,
                    "positive_id": f"{scenario.id}-fact-1",
                    "negative_id": f"{scenario.id}-distractor-{query_index}",
                    "scenario_id": scenario.id,
                }
            )
    return triplets


def validate_fact_record(record: dict[str, object]) -> None:
    text = str(record.get("text") or "")
    facts = record.get("extracted_facts")
    if "<|im_start|>system" not in text or "<|im_start|>assistant" not in text:
        raise ValueError(f"record {record.get('id')} does not use the LFM chat template")
    if not isinstance(facts, list) or not facts or not all(isinstance(fact, str) and fact for fact in facts):
        raise ValueError(f"record {record.get('id')} has invalid extracted_facts")
    assistant_payload = text.split("<|im_start|>assistant\n", 1)[1].split("<|im_end|>", 1)[0]
    parsed = json.loads(assistant_payload)
    if parsed != {"extracted_facts": facts}:
        raise ValueError(f"record {record.get('id')} assistant JSON does not match extracted_facts")


def validate_triplet(record: dict[str, object]) -> None:
    for field in ("query", "positive", "negative"):
        value = str(record.get(field) or "").strip()
        if not value:
            raise ValueError(f"triplet {record.get('id')} missing {field}")
    if record["positive"] == record["negative"]:
        raise ValueError(f"triplet {record.get('id')} has identical positive and negative text")


def write_jsonl(path: Path, records: Iterable[dict[str, object]]) -> int:
    rows = list(records)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "".join(json.dumps(row, sort_keys=True) + "\n" for row in rows),
        encoding="utf-8",
    )
    return len(rows)


def build_datasets(
    output_dir: Path = DEFAULT_OUTPUT_DIR,
    scenarios: Iterable[MemoryScenario] = DEFAULT_SCENARIOS,
) -> DatasetBuildResult:
    scenario_list = list(scenarios)
    fact_records = [render_chat_record(scenario) for scenario in scenario_list]
    sidecar_documents = render_sidecar_documents(scenario_list)
    retrieval_triplets = render_retrieval_triplets(scenario_list)

    for record in fact_records:
        validate_fact_record(record)
    for record in retrieval_triplets:
        validate_triplet(record)

    fact_count = write_jsonl(output_dir / FACT_EXTRACTION_JSONL, fact_records)
    document_count = write_jsonl(output_dir / SIDECAR_DOCUMENTS_JSONL, sidecar_documents)
    triplet_count = write_jsonl(output_dir / RETRIEVAL_TRIPLETS_JSONL, retrieval_triplets)

    result = DatasetBuildResult(
        output_dir=output_dir,
        fact_records=fact_count,
        retrieval_triplets=triplet_count,
        sidecar_documents=document_count,
    )
    (output_dir / MANIFEST_JSON).write_text(
        json.dumps(
            {
                "output_dir": str(result.output_dir),
                "fact_records": result.fact_records,
                "retrieval_triplets": result.retrieval_triplets,
                "sidecar_documents": result.sidecar_documents,
                "files": {
                    "fact_extraction": FACT_EXTRACTION_JSONL,
                    "retrieval_triplets": RETRIEVAL_TRIPLETS_JSONL,
                    "sidecar_documents": SIDECAR_DOCUMENTS_JSONL,
                },
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    return parser.parse_args()


def main() -> None:
    result = build_datasets(parse_args().output_dir)
    print(json.dumps(asdict(result), default=str, indent=2))


if __name__ == "__main__":
    main()
