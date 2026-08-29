# Public Architecture Overview

## Design principle

Brain AI separates **generation**, **belief formation**, and **execution authority**.

A language model or external source can provide candidate information, but it is not automatically treated as trusted evidence and it does not automatically gain permission to trigger an action.

## Publicly disclosed layers

### 1. Input / model boundary

Inputs are treated as potentially incomplete, contradictory, low-trust, or adversarial.

### 2. Evidence admission

Evidence is represented with identity and provenance metadata so that the system can distinguish an observation from the authority to rely on it.

### 3. Probabilistic resolution

The research architecture maintains explicit competing hypotheses and updates confidence as observations arrive.

### 4. Governed investigation

When evidence is insufficient, the system can remain unresolved rather than forcing an answer. Investigation is bounded by permission and acquisition budgets.

### 5. Ambiguity gate

A high-probability candidate is not automatically equivalent to a justified resolution. The architecture can return an ambiguous or blocked state.

### 6. Execution separation

Epistemic resolution and executable authority are intentionally separate concepts.

## Intentionally omitted

No implementation code for the trusted resolver, authorization schedule, identity binding, research generator, capability model, or future security architecture is included in this public edition.
