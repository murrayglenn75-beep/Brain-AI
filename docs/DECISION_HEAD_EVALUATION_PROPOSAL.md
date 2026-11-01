# Decision-head evaluation proposal

Status: research design only. This repository is a public showcase and does not disclose private trusted-core logic.

Evaluate a trained decision head as an **untrusted hypothesis scorer**, not as truth or authorization. A candidate may provide calibrated option probabilities, but acceptance must still pass independent evidence provenance, hypothesis validation, abstention and authority gates. Never replace foundational Murray Laws or treat an optional model head as a constitutional policy.

Proposed experiment: compare deterministic baseline, existing uncertainty/reliability controller and decision-head candidate on identical held-out examples. Track Brier score, ECE/reliability curves, selective risk versus coverage, per-slice worst-case performance, shift sensitivity, prompt-injection leakage, latency and memory. Freeze thresholds before testing; prohibit post-hoc evaluation leakage. Treat every 90% figure as an empirical population-level calibration claim, never a guarantee for an individual prediction.

No trained model or trusted-core integration is included in this change.
Source: AI Engineering Knowledge Library / 2026-11-01-unsloth-clef-decision-head-research.md.
