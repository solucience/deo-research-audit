# Count Closure: Same Count, Different Solution Set

An offline arithmetic example of **Dynamic Equilibrium Operation (DEO)**: when a condition changes, check which previous results still hold before using them in the next calculation.

OpenAI Codex conducted this exploratory study from the DEO perspective and verified the synthetic example with the local replay. The official research site is [DEOMATH.ORG](https://deomath.org/).

## Reproduce

From this directory, run with Python 3.10 or later:

```sh
python replay.py
```

No packages, network, model, wallet, or payment are required. The script compares its result with [expected.json](expected.json).

| Inclusive range of allowed integers | Even integers | Count | Sum |
| --- | --- | ---: | ---: |
| 1 to 6 | 2, 4, 6 | 3 | 12 |
| 3 to 8 | 4, 6, 8 | 3 | 18 |

The count is safe to reuse here. The old solution set and sum are not. This is a hand-authored arithmetic control, not a model benchmark or a general proof verifier.

## Continue on DEOMATH.ORG

- **Free:** [DEO transition-audit study](https://deomath.org/research/transition-audit), a separate worked example on preserving conditions and limiting claims.
- **Optional, 1.00 USDC:** [Condition, Branch and Downstream Use](https://deomath.org/library/condition-branch-dossier), a fixed-version research dossier with nine authored controls and its own offline replay. It is not needed to run this example.
- **Read-only:** [Machine-readable dossier manifest](https://deomath.org/v1/library/briefs/condition-branch-dossier/versions/1.0.0) describes the scope and price without starting a purchase.

Code and authored fixtures in this example are available under the [MIT License](LICENSE).
