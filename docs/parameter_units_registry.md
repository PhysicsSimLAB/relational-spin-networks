# Parameter & Units Registry

## 1. Purpose

This document provides a stable, repository-internal ledger of symbols, parameters, units, ranges, and role classifications used by the RSN repository.

Its purpose is to prevent silent drift in notation, defaults, dimensional assumptions, and interpretation across documentation, code, experiments, and analysis.

This registry should be consulted before introducing:

- experiment defaults
- analysis thresholds
- fit parameters
- detector-facing comparison quantities
- hidden tolerances
- implicit unit conventions

No parameter should be treated as implementation-ready merely because it appears in an equation or observable name.

## 2. Role in the Repository

The repository now uses the following internal documentation layers:

1. `README.md` for project framing
2. `docs/experiment_protocol.md` for experiment organization and provenance
3. `docs/math_foundations.md` for mathematical structure and status labels
4. `docs/equation_registry.md` for equation-level anchors and placeholders
5. `docs/observable_registry.md` for experiment-facing quantities
6. `docs/math_status_ledger.md` for readiness and blocking status
7. `docs/parameter_units_registry.md` for symbols, parameter roles, units, ranges, and default discipline

This document is the main control layer for keeping parameter meaning and dimensional assumptions stable across future implementations.

## 3. Entry Format

Each parameter entry should record:

- parameter key
- symbol
- name
- role
- unit status
- expected units
- status
- source basis
- used by
- allowed range
- default policy
- notes
- open questions

The supported parameter roles are:

- `theory_parameter`
- `control_parameter`
- `derived_quantity`
- `fit_parameter`
- `comparison_parameter`
- `tolerance`
- `size_parameter`
- `metadata_parameter`

The supported unit-status labels are:

- `dimensionful`
- `dimensionless`
- `unresolved`

The supported status labels are:

- `internalized`
- `planned`
- `placeholder`
- `deferred`

The supported default-policy labels are:

- `none`
- `explicit-only`
- `repo-default-later`

## 4. Theory Parameter Entries

### [PAR-LP-001] `L_p` / Planck-Scale Reference Length

- **Symbol**: `L_p`
- **Name**: `Planck-scale reference length`
- **Role**: `theory_parameter`
- **Unit status**: `dimensionful`
- **Expected units**: `length`
- **Status**: `internalized`
- **Source basis**: `RSN paper`
- **Used by**: `E4`, `cross-cutting`
- **Allowed range**: `external-reference-controlled`
- **Default policy**: `explicit-only`
- **Notes**: appears in the named speed-law relation and should not receive an implicit repo default without an explicit formalization step.
- **Open questions**: whether the repo will ever assign a numerical default or always treat this as externally specified.

### [PAR-LMG-001] `L_mg` / Meta-Gravitational Scale

- **Symbol**: `L_mg`
- **Name**: `meta-gravitational scale`
- **Role**: `theory_parameter`
- **Unit status**: `dimensionful`
- **Expected units**: `length`
- **Status**: `internalized`
- **Source basis**: `RSN paper`
- **Used by**: `E3`, `E4`, `cross-cutting`
- **Allowed range**: `unresolved`
- **Default policy**: `explicit-only`
- **Notes**: enters the speed law and should not be silently converted into a fit-only parameter without documentation.
- **Open questions**: whether this will later be treated as input, inferred quantity, or scan parameter.

### [PAR-VMG-001] `v_mg` / Meta-Gravitational Speed or Scale Quantity

- **Symbol**: `v_mg`
- **Name**: `meta-gravitational speed or scale quantity`
- **Role**: `derived_quantity`
- **Unit status**: `dimensionful`
- **Expected units**: `speed`
- **Status**: `internalized`
- **Source basis**: `RSN paper`
- **Used by**: `E3`, `E4`
- **Allowed range**: `unresolved`
- **Default policy**: `none`
- **Notes**: appears as a named derived relation target and should remain tied to explicit relation usage.
- **Open questions**: whether future code computes this directly, infers it through fitting, or treats it as a comparison variable.

### [PAR-KAPPA-001] `κ` / Leakage Coupling Factor

- **Symbol**: `κ`
- **Name**: `leakage or strain coupling factor`
- **Role**: `theory_parameter`
- **Unit status**: `unresolved`
- **Expected units**: `unresolved`
- **Status**: `internalized`
- **Source basis**: `RSN paper`
- **Used by**: `E3`
- **Allowed range**: `unresolved`
- **Default policy**: `explicit-only`
- **Notes**: enters the leakage relation and should remain unit-disciplined before detector-facing comparisons are implemented.
- **Open questions**: whether `κ` is dimensionless under the chosen normalization and what calibration policy should govern it.

### [PAR-LAMBDA-001] `λ` / Reserved Theory Parameter

- **Symbol**: `λ`
- **Name**: `reserved theory parameter`
- **Role**: `theory_parameter`
- **Unit status**: `unresolved`
- **Expected units**: `unresolved`
- **Status**: `planned`
- **Source basis**: `repo internal notation discipline`
- **Used by**: `cross-cutting`
- **Allowed range**: `deferred`
- **Default policy**: `none`
- **Notes**: reserved symbol only; must not receive an implementation meaning until formally declared.
- **Open questions**: whether this parameter will later appear in projector, energy, or effective theory relations.

### [PAR-ALPHA-001] `α` / Reserved Theory Parameter

- **Symbol**: `α`
- **Name**: `reserved theory parameter`
- **Role**: `theory_parameter`
- **Unit status**: `unresolved`
- **Expected units**: `unresolved`
- **Status**: `planned`
- **Source basis**: `repo internal notation discipline`
- **Used by**: `cross-cutting`
- **Allowed range**: `deferred`
- **Default policy**: `none`
- **Notes**: reserved symbol only; should remain unused until explicitly formalized.
- **Open questions**: future interpretive or quantitative role.

## 5. Control and Experiment Parameter Entries

### [PAR-BETA-PLH-001] `β` / Update Control Parameter

- **Symbol**: `β`
- **Name**: `inverse-temperature or update-control parameter`
- **Role**: `control_parameter`
- **Unit status**: `unresolved`
- **Expected units**: `unresolved`
- **Status**: `placeholder`
- **Source basis**: `repo internal`
- **Used by**: `E1`, `E2`
- **Allowed range**: `deferred`
- **Default policy**: `none`
- **Notes**: appears in the deferred update-rule placeholder and should not receive defaults before that rule is formalized.
- **Open questions**: whether `β` is dimensionless, schedule-defined, or derived from another control convention.

### [PAR-COOL-001] Cooling Rate Parameter

- **Symbol**: `r_cool`
- **Name**: `cooling rate parameter`
- **Role**: `control_parameter`
- **Unit status**: `unresolved`
- **Expected units**: `unresolved`
- **Status**: `planned`
- **Source basis**: `Protocol`, `repo internal`
- **Used by**: `E1`
- **Allowed range**: `deferred`
- **Default policy**: `none`
- **Notes**: central to freeze-out analysis but should not receive an implicit convention before update and schedule laws are formalized.
- **Open questions**: discrete versus continuous schedule meaning; dimensional interpretation.

### [PAR-FREQ-001] Frequency Variable

- **Symbol**: `f`
- **Name**: `analysis frequency`
- **Role**: `comparison_parameter`
- **Unit status**: `dimensionful`
- **Expected units**: `frequency`
- **Status**: `internalized`
- **Source basis**: `RSN paper`
- **Used by**: `E3`
- **Allowed range**: `analysis-defined-later`
- **Default policy**: `explicit-only`
- **Notes**: appears in the leakage relation and must remain unit-explicit.
- **Open questions**: sampling range, binning policy, and detector-facing interpretation.

## 6. Size and Aggregation Parameter Entries

### [PAR-LSIZE-001] `N` / Lattice Size

- **Symbol**: `N`
- **Name**: `lattice size parameter`
- **Role**: `size_parameter`
- **Unit status**: `dimensionless`
- **Expected units**: `count`
- **Status**: `planned`
- **Source basis**: `Protocol`, `repo internal`
- **Used by**: `E1`, `E2`, `E4`
- **Allowed range**: `positive integer`
- **Default policy**: `repo-default-later`
- **Notes**: should later be tied to experiment configs and finite-size analysis reporting.
- **Open questions**: whether the repo will prefer a single scalar size or per-axis size notation.

### [PAR-BLOCK-001] Block Size Parameter

- **Symbol**: `b`
- **Name**: `block size parameter`
- **Role**: `size_parameter`
- **Unit status**: `dimensionless`
- **Expected units**: `count`
- **Status**: `planned`
- **Source basis**: `Protocol`, `repo internal`
- **Used by**: `E4`
- **Allowed range**: `positive integer`
- **Default policy**: `none`
- **Notes**: should remain explicit in block-spin studies and not be hidden inside coarse-graining helpers.
- **Open questions**: divisibility requirements and whether multi-axis block sizes are needed.

## 7. Fit and Comparison Parameter Entries

### [PAR-NU-001] `ν` / Finite-Size Scaling Exponent

- **Symbol**: `ν`
- **Name**: `finite-size scaling exponent`
- **Role**: `fit_parameter`
- **Unit status**: `dimensionless`
- **Expected units**: `dimensionless`
- **Status**: `planned`
- **Source basis**: `Upgrade companion`, `repo internal`
- **Used by**: `E2`
- **Allowed range**: `fit-defined`
- **Default policy**: `none`
- **Notes**: should only appear as a fit result with uncertainty metadata.
- **Open questions**: inference method, fit window, collapse criterion.

### [PAR-Z-001] `z` / Dynamical Exponent

- **Symbol**: `z`
- **Name**: `dynamical or collapse-related exponent`
- **Role**: `fit_parameter`
- **Unit status**: `dimensionless`
- **Expected units**: `dimensionless`
- **Status**: `planned`
- **Source basis**: `Upgrade companion`, `repo internal`
- **Used by**: `E2`
- **Allowed range**: `fit-defined`
- **Default policy**: `none`
- **Notes**: should remain a fit output rather than a config default.
- **Open questions**: estimator dependence, uncertainty policy, sensitivity to schedule choices.

### [PAR-HRATIO-001] `h_mg / h_GR` / Leakage Ratio

- **Symbol**: `h_mg / h_GR`
- **Name**: `leakage ratio`
- **Role**: `comparison_parameter`
- **Unit status**: `dimensionless`
- **Expected units**: `dimensionless`
- **Status**: `planned`
- **Source basis**: `RSN paper`, `repo internal`
- **Used by**: `E3`
- **Allowed range**: `analysis-defined-later`
- **Default policy**: `none`
- **Notes**: should remain downstream of explicit strain definitions and comparison baselines.
- **Open questions**: baseline convention and threshold semantics.

## 8. Tolerance Entries

### [PAR-TOL-IDEMP-001] `ε_idem` / Idempotency Tolerance

- **Symbol**: `ε_idem`
- **Name**: `idempotency tolerance`
- **Role**: `tolerance`
- **Unit status**: `dimensionless`
- **Expected units**: `dimensionless`
- **Status**: `placeholder`
- **Source basis**: `repo internal`
- **Used by**: `E1`, `E2`, `E4`, `cross-cutting`
- **Allowed range**: `nonnegative`
- **Default policy**: `none`
- **Notes**: required for finite-precision enforcement of projector idempotency and should be explicit before correctness checks are implemented.
- **Open questions**: norm choice, threshold semantics, and whether tolerance is global or module-specific.

### [PAR-TOL-REPLAY-001] Replay Tolerance

- **Symbol**: `ε_replay`
- **Name**: `deterministic replay tolerance`
- **Role**: `tolerance`
- **Unit status**: `unresolved`
- **Expected units**: `unresolved`
- **Status**: `planned`
- **Source basis**: `Protocol`, `Upgrade companion`, `repo internal`
- **Used by**: `E1`, `E2`, `E3`, `E4`
- **Allowed range**: `nonnegative`
- **Default policy**: `none`
- **Notes**: should remain explicit and tied to replay claims rather than hidden in validation code.
- **Open questions**: exact norm, backend dependence, and whether replay is bitwise or tolerance-based.

### [PAR-TOL-FIT-001] Fit Acceptance Tolerance

- **Symbol**: `ε_fit`
- **Name**: `fit acceptance tolerance`
- **Role**: `tolerance`
- **Unit status**: `unresolved`
- **Expected units**: `unresolved`
- **Status**: `planned`
- **Source basis**: `repo internal`
- **Used by**: `E1`, `E2`, `E4`
- **Allowed range**: `nonnegative`
- **Default policy**: `none`
- **Notes**: should not be introduced ad hoc inside experiment scripts; fit acceptance semantics belong in documented analysis policy.
- **Open questions**: whether this is a residual threshold, confidence-interval rule, or model-selection rule.

## 9. Metadata and Provenance Parameter Entries

### [PAR-SEED-001] Random Seed

- **Symbol**: `seed`
- **Name**: `random seed`
- **Role**: `metadata_parameter`
- **Unit status**: `dimensionless`
- **Expected units**: `integer label`
- **Status**: `planned`
- **Source basis**: `Protocol`, `Upgrade companion`
- **Used by**: `E1`, `E2`, `E3`, `E4`, `E5`
- **Allowed range**: `nonnegative integer`
- **Default policy**: `explicit-only`
- **Notes**: should be treated as required provenance data for all executed runs.
- **Open questions**: whether seed family conventions are needed for batched studies.

### [PAR-GITSHORT-001] Git Short Hash

- **Symbol**: `gitshort`
- **Name**: `short git revision identifier`
- **Role**: `metadata_parameter`
- **Unit status**: `dimensionless`
- **Expected units**: `string identifier`
- **Status**: `planned`
- **Source basis**: `Upgrade companion`
- **Used by**: `E1`, `E2`, `E3`, `E4`, `E5`
- **Allowed range**: `nonempty revision identifier`
- **Default policy**: `explicit-only`
- **Notes**: required for traceable run tagging and provenance discipline.
- **Open questions**: exact truncation policy and detached-head behavior.

### [PAR-PARAMHASH-001] Parameter Hash

- **Symbol**: `paramhash`
- **Name**: `parameter hash`
- **Role**: `metadata_parameter`
- **Unit status**: `dimensionless`
- **Expected units**: `string identifier`
- **Status**: `planned`
- **Source basis**: `Upgrade companion`
- **Used by**: `E1`, `E2`, `E3`, `E4`, `E5`
- **Allowed range**: `nonempty hash identifier`
- **Default policy**: `explicit-only`
- **Notes**: should reflect run-defining parameter content and remain stable under reproducible serialization rules.
- **Open questions**: serialization policy and whether environment-sensitive fields are excluded.

## 10. Registry Discipline

This registry should be used to avoid the following mistakes:

- assigning implicit numeric defaults to theory parameters
- mixing dimensionful and dimensionless uses of the same symbol
- hiding tolerances inside code
- treating fit outputs as control parameters
- treating metadata fields as optional when protocol rules depend on them
- introducing new symbols without documenting their role and unit status

A parameter may appear in an equation, but still remain unresolved as a codable quantity. The status field, unit-status field, and default-policy field should always be read together.

## 11. Current Interpretation of Repository Readiness

At the present stage:

- several theory-facing symbols are now named and stabilized
- most implementation-critical defaults remain intentionally unspecified
- tolerance policy is still largely placeholder-level
- metadata parameters are closer to implementation readiness than many theory parameters
- comparison-facing parameters still require unit and normalization discipline before use

This means the repository is increasingly documentation-stable, but still appropriately resistant to premature hard-coding.

## 12. Immediate Next Priorities

The next parameter-level formalization steps should focus on:

1. idempotency tolerance policy
2. update-control parameter semantics
3. lattice-size notation and config policy
4. block-size admissibility rules
5. strain and leakage unit discipline
6. parameter-hash serialization policy
