# Agent orchestration benchmark protocol

Status: research protocol only. No measured runtime comparison or new production capability is asserted.

## Hypothesis
For small linear workflows, a plain tool loop is lower-complexity; for branching, pause/resume and crashes, durable state graphs may have advantages. The advantage must be demonstrated with controlled runs.

## Benchmark matrix
Implement the same task and deterministic scripted model in (A) plain loop, (B) graph, (C) durable authority-gated runner. Separate architectural runtime cost from LLM behavior with an identical fixed trace.

| Scenario | Success measure |
|---|---|
| Three-step read-only workflow | identical output, overhead p50/p95 |
| Single tool error, bounded retry | outcome, call counts |
| 30-branch routing | change cost and path correctness |
| Pause for human approval; restart | resume correctness, approval binding |
| External effect succeeds then timeout | zero duplicate effect, reconciliation |
| Concurrent workers | operation deduplication, stale lease fencing |
| Crash at each transition | recovery completion and evidence consistency |
| Prompt-injected tool response | unauthorized effects = 0 |

Record wall-clock CPU time, peak RSS, persistence cost, external effect count, LOC (with counting rules), test complexity, CI environment, versions and 95% uncertainty estimates across repeated runs. Provider failure simulators must distinguish pre-dispatch failure, known rejection and outcome-unknown.

## Shipping criteria
Publish runnable scripts, seeds, fixtures, dependencies and raw results; label illustrative/scripted benchmarks distinctly from live-model outcomes. Avoid claiming a graph is slower just because it has more lines of code. A framework is a durability/complexity tradeoff, not an authority system.
