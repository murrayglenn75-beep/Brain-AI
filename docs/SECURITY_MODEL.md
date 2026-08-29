# Security Model — Public Disclosure

## Threat posture

Brain AI is developed under the assumption that AI-generated content and external evidence can be wrong, manipulated, contradictory, or adversarial.

The public security philosophy includes:

- fail closed when evidence is malformed or insufficient,
- preserve evidence provenance,
- separate source trust from execution authority,
- block ambiguous resolution,
- use bounded investigation,
- isolate trusted evaluation components,
- record reproducible evidence for important experiments,
- distinguish empirical validation from proof.

## Security work demonstrated publicly

The documented build includes security-oriented testing around:

- malformed inputs,
- contradictory evidence,
- provenance and identity boundaries,
- authority separation,
- replay/state-origin concerns,
- isolated worker execution,
- evidence sealing,
- adversarial stress scenarios.

## What this repository does not claim

This repository does not claim that Brain AI is unbreakable.

Known categories requiring further work include:

- host compromise,
- software supply-chain compromise,
- production prompt-injection exposure,
- real-world distribution shift,
- formal verification,
- concurrency and replay edge cases,
- independent external red-team validation.

## Responsible disclosure

Please do not publish exploit details against private Brain AI components in a public issue. Contact the repository owner privately through GitHub first.
