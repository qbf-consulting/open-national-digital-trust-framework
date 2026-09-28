# ONDTF v1.0.0 — Stable Framework Specification

**Release date:** 28 September 2026  
**Specification maturity:** Stable  
**Evidence maturity:** E1 — repository-controlled reference/executable evidence

## Release claim

v1.0.0 establishes the first stable ONDTF normative contract. It adopts the frozen v0.9.0 candidate normative semantics without a material semantic change and activates the governed v1.x compatibility, errata, emergency-change and evidence-invalidation model.

All nine repository-controlled v1.0 promotion gates are satisfied. Stable status means implementers and framework authorities can build against a controlled, traceable and reproducibly validated specification baseline.

## Stable surface

- five frozen normative artefacts bound by exact Git blob SHA;
- 28 stable normative requirements with complete requirement-to-conformance coverage;
- six scoped conformance classes;
- five-layer interoperability and bounded recognition/equivalence semantics;
- deterministic repository and publication validation;
- v1.x compatibility/change classification;
- attributable errata and bounded emergency correction;
- evidence invalidation and reassessment after material normative change.

## Adoption improvements

v1.0.0 adds one operational **Adopt ONDTF** entry path and a deliberately small starter package. These are informative execution aids over the existing Guided Framework Construction model and do not add normative requirements.

## Release engineering

ONDTF now includes a workflow-driven release transaction derived from `VERSION` and versioned release notes, with repository validation and duplicate-release protection before publishing a normal latest GitHub release.

## Evidence boundary

v1.0.0 remains at **E1**. It does not claim independent implementation (E2), cross-implementation interoperability (E3), operational deployment (E4), production readiness, certification, or legal/regulatory approval.
