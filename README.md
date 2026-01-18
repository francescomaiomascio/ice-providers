# ICE Providers
## External Capability Integration Layer of the ICE Ecosystem

ICE Providers defines the **integration boundary** between the ICE ecosystem
and **external models, services, and computational capabilities**.

It establishes **how ICE systems access third-party capabilities**
without inheriting their assumptions, authority, or volatility.

ICE Providers does not implement intelligence.
It does not execute decisions.
It does not define behavior.

It defines **how external power is consumed without surrendering control**.

---

## Foundation Dependency

This project derives its assumptions and constraints from  
**ICE Foundation v1.0.0**.

In particular, it is bound by:

- Explicit Authority and Control Separation (Axiom A-002)
- State as a Derived and Inspectable Artifact (Axiom A-003)
- Governance (Invariant I-003)
- Governable Cognitive Reconfiguration (Invariant I-004)

External providers never become authorities.

---

## What ICE Providers Is

ICE Providers is:

- a **capability adapter layer**
- a **vendor-isolation boundary**
- a **normalization surface for external services**
- a **control point for third-party integration**
- a **testable and swappable provider abstraction**

It allows ICE systems to **use external capabilities**
without being shaped by them.

---

## What ICE Providers Is Not

ICE Providers is **not**:

- an intelligence layer
- a decision system
- a learning framework
- a model orchestrator
- a provider SDK wrapper
- a shortcut to execution

Providers supply signals and capabilities.  
They do not decide.  
They do not authorize.  
They do not execute.

---

## Architectural Role

ICE Providers operates at the **external capability boundary**
of the ICE ecosystem.

It is consumed by:

- ICE AI (reasoning support, embeddings, inference signals)
- ICE Consciousness (memory and representation signals)
- ICE Runtime and Engine (controlled access to external computation)

No ICE component should integrate directly
with third-party services outside this layer.

---

## Provider Scope

ICE Providers defines:

- canonical provider interfaces
- capability contracts (e.g. embeddings, inference, tools)
- lifecycle and resource boundaries
- error and degradation semantics
- isolation from vendor-specific APIs

All provider interactions are:

- explicit
- inspectable
- replaceable
- authority-neutral

Implicit dependency on external services is forbidden.

---

## Authority and Execution Separation

ICE Providers does **not** grant authority.

- A provider response does not justify action.
- A model output does not authorize execution.
- External intelligence does not override governance.

All decisions derived from providers
must pass through ICE AI, Runtime, and Engine layers
under Foundation-defined invariants.

---

## Design Principles

- Provider-agnostic by default
- No vendor lock-in
- Explicit contracts over implicit behavior
- Local-first when possible
- Deterministic wrapping of probabilistic systems
- Testability via mock and offline providers
- Failure and degradation as first-class conditions

External systems are assumed to be:
- unreliable
- rate-limited
- probabilistic
- outside governance

ICE Providers exists to contain that risk.

---

## Versioning and Evolution

ICE Providers evolves conservatively.

- Interfaces are stable and explicit
- New providers are additive
- Capability expansion is deliberate
- Breaking changes are exceptional

Provider churn must never destabilize ICE systems.

---

## Repository Scope

This repository contains:

- provider interface definitions
- adapter implementations
- normalization logic
- test and mock providers
- capability contracts

It explicitly does **not** contain:

- business logic
- decision systems
- orchestration code
- governance enforcement
- runtime execution paths

---

## Canonical Status

ICE Providers is **normative at the external integration boundary**.

Any ICE-compliant system that consumes
external models or services
must do so through this layer.

Bypassing this boundary
invalidates ICE compliance.

---

## Status

ICE Providers is under **active development**.

Provider support will expand,
but architectural constraints are considered permanent.

---

## Notes

External systems evolve fast.  
Foundations do not.

ICE Providers exists to ensure  
**ICE remains sovereign in a world of changing providers**.
