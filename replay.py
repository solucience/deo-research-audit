"""Replay an authored finite-set example without external dependencies."""

import json
from pathlib import Path


def measure(low, high):
    values = [x for x in range(low, high + 1) if x % 2 == 0]
    return {"values": values, "count": len(values), "sum": sum(values)}


def main():
    before, after = measure(1, 6), measure(3, 8)
    observed = {
        "evidence_kind": "AUTHORED_SYNTHETIC_ARITHMETIC",
        "before": before,
        "after": after,
        "count_preserved": before["count"] == after["count"],
        "solution_set_preserved": before["values"] == after["values"],
        "sum_preserved": before["sum"] == after["sum"],
        "canonical_study_url": "https://deomath.org/research/transition-audit",
        "related_optional_brief_url": "https://deomath.org/library/condition-branch-dossier",
    }
    expected = json.loads(Path(__file__).with_name("expected.json").read_text(encoding="utf-8"))
    if observed != expected:
        raise SystemExit("Count Closure replay differs from the fixed expected output")
    print(json.dumps(observed, indent=2))


if __name__ == "__main__":
    main()
