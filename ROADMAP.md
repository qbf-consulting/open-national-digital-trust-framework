# Roadmap

## Released baselines

- **v0.5.0 — Feature Complete Draft:** complete architectural baseline.
- **v0.6.0 — Operational Framework Draft:** governed operational composition and sector adoption foundation.
- **v0.7.0 — Implementation and Evaluation Draft:** reference implementation, executable assurance foundation, identifier resolution and evaluation machinery.
- **v0.9.0 — Candidate Specification:** stable candidate surface, complete traceability, conformance classes, interoperability/recognition evidence models and candidate governance.
- **v1.0.0 — Stable Framework Specification:** first stable normative contract, governed v1.x compatibility, reproducible release controls, operational adopter front door and starter package; evidence maturity remains E1.

## Governing release model

ONDTF separates **specification maturity** from **evidence maturity**. v1.0.0 establishes specification stability. Independent implementation, cross-implementation interoperability and operational deployment remain stronger evidence states that constrain the claims ONDTF may make but are not inferred from the stable version.

See [Specification Maturity and Evidence Governance](docs/project/maturity-and-evidence.md) and `governance/maturity.yaml`.

## Forward path

### Evidence programme — E2

**Goal:** determine whether a competent party can use the published v1.0.0 baseline without undocumented maintainer knowledge.

Target outcomes:

- one independently operated bounded implementation or profile-construction exercise;
- complete clarification and ambiguity register;
- implementation/evidence package attributable to the external actor;
- explicit defect/deviation disposition;
- evidence assessment against the E2 boundary.

### v1.1.x — Evidence-led maintenance

v1.1.x is not a pre-committed feature tranche. It should contain compatible improvements justified by v1.0 adoption, implementation, conformance, assurance or maintenance evidence. Material changes require evidence-invalidation assessment and readiness reassessment.

### v2.0.0 — Only for justified semantic break

A major version is warranted only when evidence demonstrates that a backwards-incompatible semantic, governance, profile or conformance change is necessary and cannot be represented safely within the v1.x contract.

## Evidence ambition

```text
E0  specification evidence only
 ↓
E1  repository-controlled executable/reference evidence   ← current
 ↓
E2  independent implementation evidence
 ↓
E3  cross-implementation interoperability evidence
 ↓
E4  operational deployment evidence
```

Progress along this axis is reported independently of specification version.

## Roadmap operating rule

Every roadmap goal must produce at least one machine-verifiable artefact, executable test, bounded evidence record or externally reviewable conformance procedure. New conceptual surface should be admitted only when existing ONDTF semantics cannot represent a demonstrated requirement or implementation pressure.

The detailed pre-v0.9.0 delivery plan remains preserved as historical judgment in `docs/project/detailed-delivery-roadmap.md`.
