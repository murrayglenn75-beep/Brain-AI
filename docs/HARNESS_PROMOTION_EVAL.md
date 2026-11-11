# Harness promotion evaluation pilot (read-only)

`scripts/promotion_gate.py` compares identical baseline/candidate case sets, detects regressions and critical failures, requires a minimum sample and computes a one-sided Wilson upper bound on failure rate. A candidate must demonstrate improvement and satisfy every gate. Run `cd scripts && python -m unittest -v test_promotion_gate.py`.

Important: this module does **not** authenticate the `label_origin` string. A trusted evaluation service must sign or otherwise independently verify labels, case manifests, evidence provenance and artifact hashes before promotion is considered. Repeated trials, stratification by attack class, cost and latency constraints, and distribution-shift checks are also required. The 35 cases / 10% upper-bound defaults are illustrative and NOT sufficient evidence for high-impact autonomous financial or security operations.

AAK remains responsible for independently granting and revoking narrowly scoped authority. This module never changes autonomy or permissions.

Local isolated prototype tests passed 11/11 on 2026-11-11; GitHub CI pending.
