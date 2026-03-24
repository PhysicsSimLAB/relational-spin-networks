# Math Status Ledger

## 1. Purpose

This document tracks the implementation and formalization status of RSN-facing mathematical content inside the repository.

Its purpose is to prevent overreach, preserve auditability, and make explicit what is external, internalized, placeholder-only, implementation-ready, tested, or validated.

This ledger should be consulted before adding theory-facing code, experiment logic, analysis routines, or validation claims.

## 2. Role in the Repository

The repository now uses the following internal documentation layers:

1. `README.md` for project framing
2. `docs/experiment_protocol.md` for experiment organization and provenance
3. `docs/math_foundations.md` for mathematical structure and status labels
4. `docs/equation_registry.md` for equation-level anchors and placeholders
5. `docs/observable_registry.md` for experiment-facing quantities
6. `docs/math_status_ledger.md` for current readiness and blocking status

This document is the main control layer for deciding whether a named object, relation, or observable is actually ready to support implementation.

## 3. Status Vocabulary

The following status labels are used in this ledger.

### 3.1 external_reference

The item exists mainly in the external source papers and has not yet been stabilized enough inside the repository for direct code translation.

### 3.2 internalized

The repository now contains a stable internal statement of the item in documentation form.

### 3.3 placeholder

The repository recognizes that the item is required, but does not yet have a stable mathematical statement for implementation.

### 3.4 planned

The item has a near-term implementation role, but should not yet be treated as fully codable.

### 3.5 implemented

The item has executable code in the repository.

### 3.6 tested

The item has executable code plus explicit tests tied to its intended behavior.

### 3.7 validated

The item has passed the relevant level of mathematical, numerical, or experiment-facing validation for its current scope.

## 4. Readiness Vocabulary

This ledger also tracks three distinct readiness dimensions.

### 4.1 Implementation readiness

How ready the item is to support direct code writing.

### 4.2 Test readiness

How ready the item is to support explicit tests or consistency checks.

### 4.3 Validation readiness

How ready the item is to support stronger scientific or experiment-facing claims.

The allowed readiness values are:

- `none`
- `low`
- `medium`
- `high`

## 5. Entry Format

Each ledger entry should record:

- item key
- name
- category
- current status
- source basis
- primary repo location
- implementation readiness
- test readiness
- validation readiness
- blocking gaps
- notes

The supported categories are:

- `object`
- `equation`
- `observable`
- `protocol_rule`

## 6. Theory Object Entries

### [OBJ-CELL-001] Spin–Anti-Spin Cell

- **Category**: `object`
- **Current status**: `external_reference`
- **Source basis**: `RSN paper`
- **Primary repo location**: `docs/math_foundations.md`
- **Implementation readiness**: `low`
- **Test readiness**: `none`
- **Validation readiness**: `none`
- **Blocking gaps**: explicit internal construction rule; stable local state representation; admissibility statement.
- **Notes**: currently functions as a conceptual anchor only and should not yet be treated as a directly codable primitive.

### [OBJ-PROJ-001] Projector Object

- **Category**: `object`
- **Current status**: `internalized`
- **Source basis**: `RSN paper`, `repo internal`
- **Primary repo location**: `docs/math_foundations.md`, `docs/equation_registry.md`
- **Implementation readiness**: `medium`
- **Test readiness**: `medium`
- **Validation readiness**: `low`
- **Blocking gaps**: explicit construction recipe; normalization policy; finite-precision admissibility statement.
- **Notes**: one of the strongest candidates for first theory-to-code formalization.

### [OBJ-METRIC-001] Tier Metrics

- **Category**: `object`
- **Current status**: `external_reference`
- **Source basis**: `RSN paper`
- **Primary repo location**: `docs/math_foundations.md`, `docs/equation_registry.md`
- **Implementation readiness**: `low`
- **Test readiness**: `none`
- **Validation readiness**: `none`
- **Blocking gaps**: stable internal representation; explicit use boundary for future code.
- **Notes**: mathematically important, but not yet an immediate coding target.

### [OBJ-WIND-001] Winding / Defect Object

- **Category**: `object`
- **Current status**: `internalized`
- **Source basis**: `Protocol`, `repo internal`
- **Primary repo location**: `docs/math_foundations.md`, `docs/observable_registry.md`
- **Implementation readiness**: `low`
- **Test readiness**: `low`
- **Validation readiness**: `low`
- **Blocking gaps**: explicit winding formula; sign and contour conventions; aggregation rule.
- **Notes**: central to E1 but still mathematically blocked.

### [OBJ-BLOCK-001] Block-Spin Object

- **Category**: `object`
- **Current status**: `internalized`
- **Source basis**: `Protocol`, `repo internal`
- **Primary repo location**: `docs/math_foundations.md`, `docs/equation_registry.md`
- **Implementation readiness**: `low`
- **Test readiness**: `low`
- **Validation readiness**: `low`
- **Blocking gaps**: explicit coarse-graining map; admissibility preservation rule; normalization convention.
- **Notes**: relevant to E4, but not yet formalized enough for deep implementation.

### [OBJ-STRAIN-001] Strain / Leakage Proxy

- **Category**: `object`
- **Current status**: `internalized`
- **Source basis**: `RSN paper`, `Protocol`, `repo internal`
- **Primary repo location**: `docs/math_foundations.md`, `docs/observable_registry.md`
- **Implementation readiness**: `low`
- **Test readiness**: `low`
- **Validation readiness**: `low`
- **Blocking gaps**: explicit strain proxy definition; unit handling; normalization and aggregation policy.
- **Notes**: partially anchored by the leakage relation, but still blocked as a codable quantity.

## 7. Equation Entries

### [EQ-IDEMP-001] Projector Idempotency

- **Category**: `equation`
- **Current status**: `internalized`
- **Source basis**: `RSN paper`
- **Primary repo location**: `docs/math_foundations.md`, `docs/equation_registry.md`
- **Implementation readiness**: `medium`
- **Test readiness**: `medium`
- **Validation readiness**: `low`
- **Blocking gaps**: explicit projector construction recipe; finite-precision tolerance policy.
- **Notes**: one of the strongest near-term candidates for theory-to-code testing once projector representation is formalized.

### [EQ-METRIC-001] Tiered Metric Distinction

- **Category**: `equation`
- **Current status**: `internalized`
- **Source basis**: `RSN paper`
- **Primary repo location**: `docs/equation_registry.md`
- **Implementation readiness**: `low`
- **Test readiness**: `none`
- **Validation readiness**: `none`
- **Blocking gaps**: explicit internal representation and use policy.
- **Notes**: currently serves as a mathematical distinction rather than an implementation target.

### [EQ-NULL-001] Null-Cone Hierarchy

- **Category**: `equation`
- **Current status**: `external_reference`
- **Source basis**: `RSN paper`
- **Primary repo location**: `docs/equation_registry.md`
- **Implementation readiness**: `none`
- **Test readiness**: `none`
- **Validation readiness**: `none`
- **Blocking gaps**: explicit repository-level formal statement; interpretation boundary.
- **Notes**: important to preserve, but not ready for coding or testing.

### [EQ-SPEED-001] Meta-Gravitational Speed Law

- **Category**: `equation`
- **Current status**: `internalized`
- **Source basis**: `RSN paper`
- **Primary repo location**: `docs/math_foundations.md`, `docs/equation_registry.md`
- **Implementation readiness**: `medium`
- **Test readiness**: `low`
- **Validation readiness**: `low`
- **Blocking gaps**: interpretation policy; parameter registry; whether used as fit target or calibration relation.
- **Notes**: can support documentation and later fitting logic before it supports deep validation claims.

### [EQ-PERIOD-001] 720-Degree Periodicity

- **Category**: `equation`
- **Current status**: `external_reference`
- **Source basis**: `RSN paper`
- **Primary repo location**: `docs/equation_registry.md`
- **Implementation readiness**: `none`
- **Test readiness**: `none`
- **Validation readiness**: `none`
- **Blocking gaps**: stable internal formulation; phase representation; computational target.
- **Notes**: currently interpretation-facing and later-stage.

### [EQ-ACTION-001] Action-Level Formulation

- **Category**: `equation`
- **Current status**: `external_reference`
- **Source basis**: `RSN paper`
- **Primary repo location**: `docs/equation_registry.md`
- **Implementation readiness**: `none`
- **Test readiness**: `none`
- **Validation readiness**: `none`
- **Blocking gaps**: internal transcription policy; relation to future code primitives.
- **Notes**: should remain preserved as a formal target without being treated as a simulation law.

### [EQ-FIELD-001] Field-Equation Formulation

- **Category**: `equation`
- **Current status**: `external_reference`
- **Source basis**: `RSN paper`
- **Primary repo location**: `docs/equation_registry.md`
- **Implementation readiness**: `none`
- **Test readiness**: `none`
- **Validation readiness**: `none`
- **Blocking gaps**: stable formal repo statement; explicit relation to observables or update rules.
- **Notes**: not yet suitable for direct implementation.

### [EQ-LEAK-001] Leakage Relation

- **Category**: `equation`
- **Current status**: `internalized`
- **Source basis**: `RSN paper`
- **Primary repo location**: `docs/math_foundations.md`, `docs/equation_registry.md`
- **Implementation readiness**: `medium`
- **Test readiness**: `low`
- **Validation readiness**: `low`
- **Blocking gaps**: unit policy; detector-facing normalization assumptions; explicit strain proxy definition.
- **Notes**: useful as a comparison-facing anchor, but not sufficient on its own to define E3 numerics.

### [EQ-PROJ-PLH-001] Projector Construction Recipe

- **Category**: `equation`
- **Current status**: `placeholder`
- **Source basis**: `repo internal`
- **Primary repo location**: `docs/equation_registry.md`
- **Implementation readiness**: `none`
- **Test readiness**: `none`
- **Validation readiness**: `none`
- **Blocking gaps**: explicit formula; normalization policy; representation choice.
- **Notes**: blocks mathematically anchored implementation of `core/projector.py`.

### [EQ-ENERGY-PLH-001] Local Interaction Energy Law

- **Category**: `equation`
- **Current status**: `placeholder`
- **Source basis**: `repo internal`
- **Primary repo location**: `docs/equation_registry.md`
- **Implementation readiness**: `none`
- **Test readiness**: `none`
- **Validation readiness**: `none`
- **Blocking gaps**: explicit Hamiltonian or energy functional; sign convention; boundary-condition policy.
- **Notes**: blocks a serious implementation of `core/energy.py`.

### [EQ-UPD-PLH-001] Update / Transition Rule

- **Category**: `equation`
- **Current status**: `placeholder`
- **Source basis**: `repo internal`
- **Primary repo location**: `docs/equation_registry.md`
- **Implementation readiness**: `none`
- **Test readiness**: `none`
- **Validation readiness**: `none`
- **Blocking gaps**: explicit acceptance rule; proposal mechanism; replay assumptions.
- **Notes**: blocks serious implementation of E1 and E2 execution paths.

### [EQ-WIND-PLH-001] Winding / Defect Formula

- **Category**: `equation`
- **Current status**: `placeholder`
- **Source basis**: `repo internal`
- **Primary repo location**: `docs/equation_registry.md`
- **Implementation readiness**: `none`
- **Test readiness**: `none`
- **Validation readiness**: `none`
- **Blocking gaps**: explicit formula; contour convention; sign convention; aggregation policy.
- **Notes**: blocks mathematically anchored implementation of winding observables and E1 outputs.

### [EQ-BLOCK-PLH-001] Block-Spin Coarse-Graining Map

- **Category**: `equation`
- **Current status**: `placeholder`
- **Source basis**: `repo internal`
- **Primary repo location**: `docs/equation_registry.md`
- **Implementation readiness**: `none`
- **Test readiness**: `none`
- **Validation readiness**: `none`
- **Blocking gaps**: explicit coarse-graining rule; admissibility preservation; normalization after aggregation.
- **Notes**: blocks deep implementation of E4.

### [EQ-STRAIN-PLH-001] Strain Proxy Definition

- **Category**: `equation`
- **Current status**: `placeholder`
- **Source basis**: `repo internal`
- **Primary repo location**: `docs/equation_registry.md`
- **Implementation readiness**: `none`
- **Test readiness**: `none`
- **Validation readiness**: `none`
- **Blocking gaps**: explicit proxy formula; unit convention; aggregation and normalization policy.
- **Notes**: blocks mathematically grounded implementation of E3.

## 8. Observable Entries

### [OBS-E1-DEFECT-001] Defect Density

- **Category**: `observable`
- **Current status**: `planned`
- **Source basis**: `Protocol`, `Upgrade companion`, `repo internal`
- **Primary repo location**: `docs/observable_registry.md`
- **Implementation readiness**: `low`
- **Test readiness**: `low`
- **Validation readiness**: `low`
- **Blocking gaps**: explicit winding formula; normalization convention; run-summary specification.
- **Notes**: should not be implemented before its dependency on winding is formalized.

### [OBS-E1-WIND-001] Winding Count

- **Category**: `observable`
- **Current status**: `planned`
- **Source basis**: `Protocol`, `repo internal`
- **Primary repo location**: `docs/observable_registry.md`
- **Implementation readiness**: `low`
- **Test readiness**: `low`
- **Validation readiness**: `low`
- **Blocking gaps**: winding formula; contour conventions; aggregation policy.
- **Notes**: central E1 observable but still blocked mathematically.

### [OBS-E1-FREEZE-001] Freeze-Out Scale

- **Category**: `observable`
- **Current status**: `planned`
- **Source basis**: `Protocol`, `repo internal`
- **Primary repo location**: `docs/observable_registry.md`
- **Implementation readiness**: `low`
- **Test readiness**: `low`
- **Validation readiness**: `low`
- **Blocking gaps**: update rule; winding outputs; fitting contract.
- **Notes**: a fitted quantity that should remain downstream of primary observables.

### [OBS-E2-CORR-001] Correlation Length

- **Category**: `observable`
- **Current status**: `planned`
- **Source basis**: `Protocol`, `repo internal`
- **Primary repo location**: `docs/observable_registry.md`
- **Implementation readiness**: `low`
- **Test readiness**: `low`
- **Validation readiness**: `low`
- **Blocking gaps**: estimator definition; projector and energy formalization.
- **Notes**: should not be treated as estimator-free or theory-neutral.

### [OBS-E2-STRUCT-001] Structure Factor

- **Category**: `observable`
- **Current status**: `planned`
- **Source basis**: `Protocol`, `repo internal`
- **Primary repo location**: `docs/observable_registry.md`
- **Implementation readiness**: `low`
- **Test readiness**: `low`
- **Validation readiness**: `low`
- **Blocking gaps**: transform convention; normalization policy; projector/energy anchoring.
- **Notes**: analysis-facing but still mathematically blocked.

### [OBS-E2-NU-001] Fitted Exponent nu

- **Category**: `observable`
- **Current status**: `planned`
- **Source basis**: `Upgrade companion`, `repo internal`
- **Primary repo location**: `docs/observable_registry.md`
- **Implementation readiness**: `low`
- **Test readiness**: `low`
- **Validation readiness**: `low`
- **Blocking gaps**: fit definition; estimator inputs; uncertainty protocol.
- **Notes**: should always remain downstream of derived observables and fit metadata.

### [OBS-E2-Z-001] Fitted Exponent z

- **Category**: `observable`
- **Current status**: `planned`
- **Source basis**: `Upgrade companion`, `repo internal`
- **Primary repo location**: `docs/observable_registry.md`
- **Implementation readiness**: `low`
- **Test readiness**: `low`
- **Validation readiness**: `low`
- **Blocking gaps**: fit definition; uncertainty protocol; update-law dependence.
- **Notes**: not a primitive run output.

### [OBS-E3-STRAIN-001] Normalized Strain Proxy

- **Category**: `observable`
- **Current status**: `planned`
- **Source basis**: `RSN paper`, `Protocol`, `repo internal`
- **Primary repo location**: `docs/observable_registry.md`
- **Implementation readiness**: `low`
- **Test readiness**: `low`
- **Validation readiness**: `low`
- **Blocking gaps**: explicit strain proxy formula; normalization and unit policy.
- **Notes**: partially anchored by the leakage relation, but not yet codable as a stable quantity.

### [OBS-E3-RATIO-001] Leakage Ratio h_mg / h_GR

- **Category**: `observable`
- **Current status**: `planned`
- **Source basis**: `RSN paper`, `repo internal`
- **Primary repo location**: `docs/observable_registry.md`
- **Implementation readiness**: `low`
- **Test readiness**: `low`
- **Validation readiness**: `low`
- **Blocking gaps**: baseline policy; unit handling; relation to raw proxy definition.
- **Notes**: comparison-facing, not primitive.

### [OBS-E3-SENS-001] Sensitivity Crossing

- **Category**: `observable`
- **Current status**: `planned`
- **Source basis**: `Upgrade companion`, `repo internal`
- **Primary repo location**: `docs/observable_registry.md`
- **Implementation readiness**: `low`
- **Test readiness**: `low`
- **Validation readiness**: `low`
- **Blocking gaps**: crossing definition; threshold policy; uncertainty encoding.
- **Notes**: should remain downstream of strain-facing quantities.

### [OBS-E4-COUPLING-001] Effective Couplings

- **Category**: `observable`
- **Current status**: `planned`
- **Source basis**: `Protocol`, `repo internal`
- **Primary repo location**: `docs/observable_registry.md`
- **Implementation readiness**: `low`
- **Test readiness**: `low`
- **Validation readiness**: `low`
- **Blocking gaps**: coarse-graining map; extraction method; normalization convention.
- **Notes**: central E4 quantity but heavily blocked by the block placeholder.

### [OBS-E4-BETA-001] Beta-Flow Estimate

- **Category**: `observable`
- **Current status**: `planned`
- **Source basis**: `Upgrade companion`, `repo internal`
- **Primary repo location**: `docs/observable_registry.md`
- **Implementation readiness**: `low`
- **Test readiness**: `low`
- **Validation readiness**: `low`
- **Blocking gaps**: coarse variable definition; fit protocol; uncertainty handling.
- **Notes**: should remain downstream of effective coupling extraction.

### [OBS-E4-SPEED-001] Speed-Law Fit Summary

- **Category**: `observable`
- **Current status**: `planned`
- **Source basis**: `RSN paper`, `repo internal`
- **Primary repo location**: `docs/observable_registry.md`
- **Implementation readiness**: `low`
- **Test readiness**: `low`
- **Validation readiness**: `low`
- **Blocking gaps**: fitting contract; parameter registry; block-map formalization.
- **Notes**: comparison-facing fit target, not a state variable.

### [OBS-E5-PHASE-001] Phase Spectrum

- **Category**: `observable`
- **Current status**: `deferred`
- **Source basis**: `RSN paper`, `repo internal`
- **Primary repo location**: `docs/observable_registry.md`
- **Implementation readiness**: `none`
- **Test readiness**: `none`
- **Validation readiness**: `none`
- **Blocking gaps**: phase representation; periodicity formalization; noise-model boundary.
- **Notes**: later-stage only.

### [OBS-E5-FRINGE-001] Fringe Visibility

- **Category**: `observable`
- **Current status**: `deferred`
- **Source basis**: `repo internal`
- **Primary repo location**: `docs/observable_registry.md`
- **Implementation readiness**: `none`
- **Test readiness**: `none`
- **Validation readiness**: `none`
- **Blocking gaps**: visibility definition; phase formalization; detectability semantics.
- **Notes**: later-stage only.

### [OBS-E5-SNR-001] Shot-Noise Signal-to-Noise Ratio

- **Category**: `observable`
- **Current status**: `deferred`
- **Source basis**: `repo internal`
- **Primary repo location**: `docs/observable_registry.md`
- **Implementation readiness**: `none`
- **Test readiness**: `none`
- **Validation readiness**: `none`
- **Blocking gaps**: SNR formula; noise model; threshold rule.
- **Notes**: later-stage only.

## 9. Protocol Rule Entries

### [RULE-META-001] Metadata Completeness Rule

- **Category**: `protocol_rule`
- **Current status**: `planned`
- **Source basis**: `Upgrade companion`
- **Primary repo location**: `docs/experiment_protocol.md`
- **Implementation readiness**: `medium`
- **Test readiness**: `medium`
- **Validation readiness**: `medium`
- **Blocking gaps**: explicit minimum schema; failure policy.
- **Notes**: protocol-backed and comparatively ready for implementation.

### [RULE-CHECKSUM-001] Checksum Integrity Rule

- **Category**: `protocol_rule`
- **Current status**: `planned`
- **Source basis**: `Upgrade companion`
- **Primary repo location**: `docs/experiment_protocol.md`
- **Implementation readiness**: `medium`
- **Test readiness**: `medium`
- **Validation readiness**: `medium`
- **Blocking gaps**: manifest schema; batch-policy details.
- **Notes**: protocol-backed and less mathematically blocked than projector or winding formalization.

### [RULE-REPLAY-001] Deterministic Replay Rule

- **Category**: `protocol_rule`
- **Current status**: `planned`
- **Source basis**: `Protocol`, `Upgrade companion`
- **Primary repo location**: `docs/experiment_protocol.md`
- **Implementation readiness**: `medium`
- **Test readiness**: `medium`
- **Validation readiness**: `low`
- **Blocking gaps**: replay tolerance policy; update-law dependence; backend assumptions.
- **Notes**: partially blocked by the update placeholder but still structurally specifiable.

### [RULE-ABORT-001] Shared Abort Conditions

- **Category**: `protocol_rule`
- **Current status**: `internalized`
- **Source basis**: `Protocol`, `Upgrade companion`
- **Primary repo location**: `docs/experiment_protocol.md`
- **Implementation readiness**: `medium`
- **Test readiness**: `medium`
- **Validation readiness**: `low`
- **Blocking gaps**: concrete exception and reporting policy.
- **Notes**: one of the more implementation-ready non-theory rules in the repository.

## 10. Ledger Use Rules

This ledger should be used to prevent the following mistakes:

- treating a named theory object as implementation-ready when it is still only external or placeholder-level
- treating a placeholder equation as if it were a stable internal mathematical statement
- treating a planned observable as if it were already estimator-defined
- treating a protocol rule as validated merely because it appears in documentation

The readiness fields matter as much as the status field. An item may be internalized in documentation and still have low implementation readiness.

## 11. Current Interpretation of the Repository State

At the present stage:

- several important RSN-facing objects have been internalized in documentation
- several crucial equations remain placeholders
- most observables are planned but blocked by unresolved mathematical formalization
- some provenance and protocol rules are closer to implementation readiness than the theory-facing modules

This means the repository is now better prepared for disciplined formalization, but not yet ready for deep theory-facing coding.

## 12. Immediate Next Priorities

The next status-improving formalization steps should focus on:

1. projector construction recipe
2. local interaction energy law
3. winding / defect formula
4. parameter and units registry
5. explicit audit schema minimums
