# ONDTF v1.0.0 Validation Notes

The v1.0.0 release transaction is valid only after pull-request quality checks and the release workflow execute successfully.

Validation includes repository/schema integrity, frozen normative blob verification, v1 stable controls/readiness, identifier/requirements resolution, conformance/interoperability checks, Mermaid source/render validation, Jekyll build and generated-site inspection.

The release workflow derives the tag from `VERSION`, rejects invalid semantic versions, requires matching versioned release notes/metadata, and does not recreate an existing release.
