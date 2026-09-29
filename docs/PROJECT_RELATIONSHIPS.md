# Relationship to Other Engineering Projects

These repositories explore different aspects of governed AI systems.

| Project | Primary focus | Public disclosure |
|---|---|---|
| Brain AI | Evidence resolution, provenance and epistemic control | Architecture and selected research evidence |
| AI Authority Kernel (AAK) | External authorization and controlled tool execution | Release-candidate implementation and tests |
| Agent Security Lab | Adversarial evaluation of agent execution boundaries | Deterministic security test scenarios |

## Design distinction

Brain AI studies when evidence justifies a belief or resolution.

AAK addresses whether an action is authorized to execute.

Agent Security Lab evaluates whether hostile or manipulated agent behavior can cross security boundaries.

These projects are conceptually related but should not be represented as one integrated production system without separate integration evidence.

## Public research boundary

The Brain AI public repository is not an executable distribution of the private trusted-core implementation.

Its verification workflow validates the integrity and internal consistency of the disclosed research bundle. It does not reproduce the private simulator or independently certify the full architecture.
