# ArcTopia

It started from a simple discomfort.

I kept seeing the same pattern across many resource projects. We use big, positive words like green transition, critical materials, strategic importance, and innovation. These things may be real, but inside that language, the actual consequences often disappear. The local impact becomes abstract. The people living there fade into the background. Nature becomes a line item. And responsibility turns into paperwork.

Once the story sounds good enough, recognition comes before the real consequences have actually been faced.

ArcTopia is my attempt to change that.

It’s built on one fundamental rule: nothing can be considered legitimate until it has gone through the full sequence — Activity, Evidence, Assessment, Verification, and only then Recognition. You cannot skip any step.

The system protects a few hard principles: obligations must stay tied to their origin, different states must remain clearly separated, assessments must use declared methods, responsibility cannot be quietly transferred or erased, history cannot be silently overwritten, and only real human authority can make final decisions.

The goal is simple: when we call something progress, the consequences should no longer be hidden from view.

ArcTopia is a computational legitimacy engine for dynamic systems.

It is designed to compute, explain, simulate, and navigate whether a resource, project, or supply chain remains valid under changing constraints.

## What ArcTopia does

ArcTopia models:

- resources as nodes
- lineage as dependency relationships
- obligations as formal requirements
- events as state-changing signals
- recognition as a computed output, not a declaration

From this, it computes whether a system is currently:

- `VALID`
- `CONDITIONAL`
- `FLAGGED`
- `SUSPENDED`

## Current repository scope

This repository currently contains two layers of ArcTopia development:

### 1. Early MVP layer
An append-only ledger and gating-style MVP focused on event integrity, issuance constraints, and report generation.

### 2. Dynamic governance engine layer
A newer backend/frontend/database system that adds:

- real-time recognition state computation
- lineage-based propagation
- multi-dimensional state
- simulation of hypothetical events
- decision suggestions
- experimental hypercube / trajectory-based evaluation

## Current system capabilities

The current ArcTopia engine supports:

- creation of resources and lineage relationships
- obligation and fulfillment tracking
- event-driven state recomputation
- upstream-to-downstream propagation
- explainable state output
- scenario simulation without mutating live state
- dynamic constraint evaluation across substances, ESG, authority, obligations, and upstream dependencies

## Multi-dimensional state

ArcTopia no longer stores only a flat status. It computes a structured internal state such as:

```json
{
  "esg": "OK | VIOLATION",
  "substances": {
    "<name>": {
      "value": 150,
      "threshold": 100,
      "status": "OK | EXCEEDED"
    }
  },
  "obligation": "FULFILLED | PENDING | BREACHED",
  "authority": "APPROVED | SUSPENDED",
  "upstream": "VALID | FLAGGED | SUSPENDED"
}
## License

This repository is governed by the terms stated in `LICENSE`.
