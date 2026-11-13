# November 2026: epistemic and evaluation hardening plan (public)

**Disclosure boundary:** Public engineering specification only. Never add private thresholds, trusted-core source, hidden evaluation corpora or secrets to this repository.

## Baseline before extra agents

Prefer one bounded reasoning/evidence loop with a small number of explicit, least-privilege read tools. Only introduce subagents, vector stores or graph reasoning when frozen task-suite comparisons show a measured advantage over the baseline. Keep retrieved material as data, never instructions.

## Evidence lifecycle

Every proposed claim should have source identity, content hash, acquisition time, evidence/permission expiry, reliability class and explicit contradictions. Separate (a) model belief, (b) admissible evidence, (c) confidence interval/uncertainty and (d) externally authorized effect. Missing or conflicting inputs lead to `AMBIGUOUS`/`BLOCKED`, not an invented resolution.

## Durable, independent evaluation

Version immutable gold labels and criteria independently from the candidate under evaluation. Persist attempts as they finish using idempotency keys and hashes; support bounded budgets and resume after crash. Report accuracy **and** coverage, false-resolution rate, calibrated uncertainty, latency and cost. Include distribution shifts, injected source text, conflicting metadata and stale provenance. Do not optimize the grader on the same held-out test set and do not relabel old evidence to inflate scores.

## Promotion criteria to implement privately

- An independently administered authority boundary binds the exact action, principal, resource and current policy revision.
- Require a precommitted release threshold over unseen cases, uncertainty intervals and human-reviewed high-consequence failures.
- Compare candidate against frozen simple baseline with identical cases and budgets; record regressions as well as gains.
- Fail closed on malformed schema, duplicate keys, expired evidence and missing audit continuity.
- Human approval is mandatory for external side effects until separate proof supports a narrowly scoped exception.

**Status:** Design proposal, not evidence that public/private implementation or production validation is complete.
