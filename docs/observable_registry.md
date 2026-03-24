# Observable Registry

## 1. Purpose

This document provides a stable, repository-internal ledger of experiment-facing observables used by the RSN repository.

Its purpose is to support implementation planning, output design, validation, and disciplined theory-to-experiment translation. It should be consulted before adding experiment logic, analysis code, fitted summaries, or comparison-facing result generation.

This registry distinguishes between:

- raw observables
- derived observables
- fitted quantities
- comparison-facing outputs
- audit-facing observables

The goal is to prevent drift between mathematical definitions, experiment outputs, and repository structure.

## 2. Role in the Repository

The repository now uses the following internal documentation layers:

1. `README.md` for project framing
2. `docs/experiment_protocol.md` for experiment organization and provenance
3. `docs/math_foundations.md` for mathematical structure and status labels
4. `docs/equation_registry.md` for equations and formalization gaps
5. `docs/observable_registry.md` for experiment-facing quantities and output semantics

This document is the main lookup layer for what each experiment is expected to measure, derive, fit, compare, and report.

## 3. Entry Format

Each observable entry should record:

- observable key
- name
- experiment family
- observable type
- definition
- mathematical dependency
- intended module
- expected output form
- status
- implementation notes
- open questions

The observable types used here are:

- `raw`
- `derived`
- `fitted`
- `comparison_facing`
- `audit`

The status vocabulary used here is:

- `scaffold`
- `planned`
- `deferred`

## 4. Observable Types

### 4.1 Raw

A quantity measured or extracted directly from a state representation or immediate run output.

### 4.2 Derived

A quantity computed from one or more raw observables or mathematically prior quantities.

### 4.3 Fitted

A quantity obtained through regression, collapse, curve fitting, or another explicit estimation procedure.

### 4.4 Comparison-facing

A quantity primarily used for overlay, exclusion, detectability, or external comparison rather than as a primitive simulation-state variable.

### 4.5 Audit

A quantity used to certify provenance, integrity, reproducibility, or execution validity.

## 5. E1 Observable Entries

### [OBS-E1-DEFECT-001] Defect Density

- **Experiments**: `E1`
- **Type**: `derived`
- **Definition**: normalized defect count or winding-derived defect measure reported over a lattice realization or ensemble.
- **Depends on**: `[EQ-WIND-PLH-001]`
- **Intended module**: `src/relational_spin_networks/core/winding.py`
- **Expected output form**: `scalar`, `curve`, `table`
- **Status**: `planned`
- **Implementation notes**: the normalization convention should be made explicit, including whether density is per site, per plaquette, or ensemble averaged.
- **Open questions**: exact normalization convention; whether defect density is primary or always derived from a more primitive winding object.

### [OBS-E1-WIND-001] Winding Count

- **Experiments**: `E1`
- **Type**: `raw`
- **Definition**: count or signed measure of topological winding or defect content extracted from a local configuration.
- **Depends on**: `[EQ-WIND-PLH-001]`
- **Intended module**: `src/relational_spin_networks/core/winding.py`
- **Expected output form**: `scalar`, `table`
- **Status**: `planned`
- **Implementation notes**: winding conventions must later specify contour choice, counting policy, and sign handling.
- **Open questions**: exact contour definition; whether multiple winding observables are needed for local versus aggregate counts.

### [OBS-E1-FREEZE-001] Freeze-Out Scale

- **Experiments**: `E1`
- **Type**: `fitted`
- **Definition**: fitted characteristic scale associated with defect freeze-out behavior under controlled cooling.
- **Depends on**: `[EQ-UPD-PLH-001]`, `[EQ-WIND-PLH-001]`
- **Intended module**: `src/relational_spin_networks/experiments/e1.py`
- **Expected output form**: `fit summary`, `table`
- **Status**: `planned`
- **Implementation notes**: should be derived from run outputs rather than treated as a primitive state variable.
- **Open questions**: fitting law, uncertainty method, and whether this quantity belongs in run-level summaries or only post-processed analysis.

## 6. E2 Observable Entries

### [OBS-E2-CORR-001] Correlation Length

- **Experiments**: `E2`
- **Type**: `derived`
- **Definition**: characteristic correlation scale extracted from finite-size or configuration-dependent state organization.
- **Depends on**: `[EQ-PROJ-PLH-001]`, `[EQ-ENERGY-PLH-001]`
- **Intended module**: `src/relational_spin_networks/analysis/summary.py`
- **Expected output form**: `scalar`, `curve`, `table`
- **Status**: `planned`
- **Implementation notes**: estimator choice and aggregation policy should later be specified explicitly.
- **Open questions**: precise estimator, finite-size correction policy, and whether this should be computed online or in post-processing.

### [OBS-E2-STRUCT-001] Structure Factor

- **Experiments**: `E2`
- **Type**: `derived`
- **Definition**: spectral or spatial-order observable used to characterize finite-size scaling and collapse behavior.
- **Depends on**: `[EQ-PROJ-PLH-001]`, `[EQ-ENERGY-PLH-001]`
- **Intended module**: `src/relational_spin_networks/analysis/summary.py`
- **Expected output form**: `curve`, `table`
- **Status**: `planned`
- **Implementation notes**: the precise estimator should later be declared as part of the analysis contract.
- **Open questions**: exact transform convention; which normalization is appropriate for cross-size comparison.

### [OBS-E2-NU-001] Fitted Exponent nu

- **Experiments**: `E2`
- **Type**: `fitted`
- **Definition**: finite-size scaling exponent inferred from collapse-oriented or scaling-oriented analysis.
- **Depends on**: `[OBS-E2-CORR-001]`, `[EQ-UPD-PLH-001]`
- **Intended module**: `src/relational_spin_networks/experiments/e2.py`
- **Expected output form**: `fit summary`, `table`
- **Status**: `planned`
- **Implementation notes**: should always be reported with uncertainty and fit-context metadata.
- **Open questions**: fitting window, regression form, uncertainty protocol.

### [OBS-E2-Z-001] Fitted Exponent z

- **Experiments**: `E2`
- **Type**: `fitted`
- **Definition**: dynamical or collapse-related exponent inferred from experiment-level scaling analysis.
- **Depends on**: `[OBS-E2-CORR-001]`, `[EQ-UPD-PLH-001]`
- **Intended module**: `src/relational_spin_networks/experiments/e2.py`
- **Expected output form**: `fit summary`, `table`
- **Status**: `planned`
- **Implementation notes**: should remain distinct from raw run outputs and always carry fit metadata.
- **Open questions**: inference method, uncertainty estimation, sensitivity to schedule or sample count.

## 7. E3 Observable Entries

### [OBS-E3-STRAIN-001] Normalized Strain Proxy

- **Experiments**: `E3`
- **Type**: `comparison_facing`
- **Definition**: normalized RSN-facing strain or leakage quantity used for observational comparison.
- **Depends on**: `[EQ-STRAIN-PLH-001]`, `[EQ-LEAK-001]`
- **Intended module**: `src/relational_spin_networks/core/strain.py`
- **Expected output form**: `scalar`, `curve`, `figure-facing summary`
- **Status**: `planned`
- **Implementation notes**: should separate raw proxy construction from detector-overlay comparison.
- **Open questions**: normalization convention, unit handling, and whether detector assumptions live here or in downstream analysis outputs.

### [OBS-E3-RATIO-001] Leakage Ratio h_mg / h_GR

- **Experiments**: `E3`
- **Type**: `comparison_facing`
- **Definition**: normalized ratio comparing RSN-facing strain output to a comparison baseline.
- **Depends on**: `[EQ-LEAK-001]`
- **Intended module**: `src/relational_spin_networks/core/strain.py`
- **Expected output form**: `scalar`, `curve`, `table`
- **Status**: `planned`
- **Implementation notes**: should later declare reference baseline assumptions and units explicitly.
- **Open questions**: baseline source definition; whether the ratio is reported directly or only through thresholded comparisons.

### [OBS-E3-SENS-001] Sensitivity Crossing

- **Experiments**: `E3`
- **Type**: `comparison_facing`
- **Definition**: threshold-style indicator of whether an RSN-facing strain signal crosses a stated detector or comparison sensitivity level.
- **Depends on**: `[OBS-E3-STRAIN-001]`, `[OBS-E3-RATIO-001]`
- **Intended module**: `src/relational_spin_networks/analysis/summary.py`
- **Expected output form**: `scalar`, `table`, `figure-facing summary`
- **Status**: `planned`
- **Implementation notes**: should remain clearly separate from the underlying raw strain proxy.
- **Open questions**: exact crossing definition; how to encode uncertainty or noise assumptions.

## 8. E4 Observable Entries

### [OBS-E4-COUPLING-001] Effective Couplings

- **Experiments**: `E4`
- **Type**: `derived`
- **Definition**: coarse-grained coupling quantities inferred after block-spin or renormalization-style aggregation.
- **Depends on**: `[EQ-BLOCK-PLH-001]`, `[EQ-SPEED-001]`
- **Intended module**: `src/relational_spin_networks/core/block.py`
- **Expected output form**: `table`, `curve`
- **Status**: `planned`
- **Implementation notes**: should later distinguish directly measured coarse variables from fitted coupling summaries.
- **Open questions**: extraction method, normalization convention, regression target.

### [OBS-E4-BETA-001] Beta-Flow Estimate

- **Experiments**: `E4`
- **Type**: `fitted`
- **Definition**: fitted flow or slope quantity used to summarize renormalization behavior.
- **Depends on**: `[EQ-BLOCK-PLH-001]`, `[OBS-E4-COUPLING-001]`
- **Intended module**: `src/relational_spin_networks/experiments/e4.py`
- **Expected output form**: `fit summary`, `table`
- **Status**: `planned`
- **Implementation notes**: should include uncertainty and fit-context metadata.
- **Open questions**: exact regression variable, sign convention, and robustness checks.

### [OBS-E4-SPEED-001] Speed-Law Fit Summary

- **Experiments**: `E4`
- **Type**: `fitted`
- **Definition**: experiment-level summary describing consistency between coarse-grained results and the named RSN speed law.
- **Depends on**: `[EQ-SPEED-001]`, `[OBS-E4-COUPLING-001]`
- **Intended module**: `src/relational_spin_networks/experiments/e4.py`
- **Expected output form**: `fit summary`, `figure-facing summary`
- **Status**: `planned`
- **Implementation notes**: should be treated as a comparison target, not a primitive simulation state variable.
- **Open questions**: fit form, confidence interval protocol, and what counts as acceptable agreement.

## 9. E5 Observable Entries

### [OBS-E5-PHASE-001] Phase Spectrum

- **Experiments**: `E5`
- **Type**: `comparison_facing`
- **Definition**: later-stage phase-domain observable used to characterize twist-induced signal structure under modeled noise.
- **Depends on**: `[EQ-PERIOD-001]`, `[EQ-NULL-001]`
- **Intended module**: `src/relational_spin_networks/analysis/summary.py`
- **Expected output form**: `curve`, `figure-facing summary`
- **Status**: `deferred`
- **Implementation notes**: should remain clearly marked as later-stage and should not be treated as a first implementation target.
- **Open questions**: exact phase representation, noise model boundary, detectability threshold definition.

### [OBS-E5-FRINGE-001] Fringe Visibility

- **Experiments**: `E5`
- **Type**: `comparison_facing`
- **Definition**: later-stage visibility observable describing coherence or interference-style signal contrast under modeled conditions.
- **Depends on**: `[EQ-PERIOD-001]`
- **Intended module**: `src/relational_spin_networks/analysis/summary.py`
- **Expected output form**: `scalar`, `curve`, `figure-facing summary`
- **Status**: `deferred`
- **Implementation notes**: should remain downstream of any formal phase model and noise model.
- **Open questions**: exact visibility definition; relation to spectrum summaries and threshold logic.

### [OBS-E5-SNR-001] Shot-Noise Signal-to-Noise Ratio

- **Experiments**: `E5`
- **Type**: `comparison_facing`
- **Definition**: later-stage detectability quantity comparing phase-domain signal structure against a modeled shot-noise floor.
- **Depends on**: `[OBS-E5-PHASE-001]`, `[OBS-E5-FRINGE-001]`
- **Intended module**: `src/relational_spin_networks/analysis/summary.py`
- **Expected output form**: `scalar`, `table`, `figure-facing summary`
- **Status**: `deferred`
- **Implementation notes**: should only be introduced once assumptions and noise models are documented explicitly.
- **Open questions**: exact SNR formula, averaging policy, and what threshold counts as detectability support.

## 10. Cross-Cutting Audit Observables

### [OBS-AUDIT-META-001] Metadata Completeness

- **Experiments**: `E1`, `E2`, `E3`, `E4`, `E5`
- **Type**: `audit`
- **Definition**: status indicator describing whether the required metadata fields for a run were captured completely.
- **Depends on**: `experiment protocol provenance rules`
- **Intended module**: `src/relational_spin_networks/provenance/metadata.py`
- **Expected output form**: `scalar`, `table`
- **Status**: `planned`
- **Implementation notes**: should later function as an execution-validity requirement, not just an informational summary.
- **Open questions**: exact minimum field set and failure policy.

### [OBS-AUDIT-CHK-001] Checksum Integrity Status

- **Experiments**: `E1`, `E2`, `E3`, `E4`, `E5`
- **Type**: `audit`
- **Definition**: status indicator describing whether the expected checksum manifest was created and remained valid for a run or batch.
- **Depends on**: `experiment protocol provenance rules`
- **Intended module**: `src/relational_spin_networks/provenance/checksums.py`
- **Expected output form**: `scalar`, `table`
- **Status**: `planned`
- **Implementation notes**: should later be used as part of run acceptance and archive readiness.
- **Open questions**: manifest granularity, batch-policy, and repair or regeneration policy.

### [OBS-AUDIT-REPLAY-001] Deterministic Replay Status

- **Experiments**: `E1`, `E2`, `E3`, `E4`
- **Type**: `audit`
- **Definition**: status indicator describing whether a run reproduced the documented result under the declared deterministic replay conditions.
- **Depends on**: `[EQ-UPD-PLH-001]`, `experiment protocol execution rules`
- **Intended module**: `src/relational_spin_networks/provenance/metadata.py`
- **Expected output form**: `scalar`, `table`
- **Status**: `planned`
- **Implementation notes**: should remain separate from physics validation and should only certify replay under declared conditions.
- **Open questions**: exact replay tolerance, scope of determinism, and hardware or backend constraints.

## 11. Crosswalk from Observables to Equations

### 11.1 E1

- `[OBS-E1-WIND-001]` -> `[EQ-WIND-PLH-001]`
- `[OBS-E1-DEFECT-001]` -> `[EQ-WIND-PLH-001]`
- `[OBS-E1-FREEZE-001]` -> `[EQ-UPD-PLH-001]`, `[EQ-WIND-PLH-001]`

### 11.2 E2

- `[OBS-E2-CORR-001]` -> `[EQ-PROJ-PLH-001]`, `[EQ-ENERGY-PLH-001]`
- `[OBS-E2-STRUCT-001]` -> `[EQ-PROJ-PLH-001]`, `[EQ-ENERGY-PLH-001]`
- `[OBS-E2-NU-001]` -> `[EQ-UPD-PLH-001]`, `[OBS-E2-CORR-001]`
- `[OBS-E2-Z-001]` -> `[EQ-UPD-PLH-001]`, `[OBS-E2-CORR-001]`

### 11.3 E3

- `[OBS-E3-STRAIN-001]` -> `[EQ-STRAIN-PLH-001]`, `[EQ-LEAK-001]`
- `[OBS-E3-RATIO-001]` -> `[EQ-LEAK-001]`
- `[OBS-E3-SENS-001]` -> `[OBS-E3-STRAIN-001]`, `[OBS-E3-RATIO-001]`

### 11.4 E4

- `[OBS-E4-COUPLING-001]` -> `[EQ-BLOCK-PLH-001]`, `[EQ-SPEED-001]`
- `[OBS-E4-BETA-001]` -> `[EQ-BLOCK-PLH-001]`, `[OBS-E4-COUPLING-001]`
- `[OBS-E4-SPEED-001]` -> `[EQ-SPEED-001]`, `[OBS-E4-COUPLING-001]`

### 11.5 E5

- `[OBS-E5-PHASE-001]` -> `[EQ-PERIOD-001]`, `[EQ-NULL-001]`
- `[OBS-E5-FRINGE-001]` -> `[EQ-PERIOD-001]`
- `[OBS-E5-SNR-001]` -> `[OBS-E5-PHASE-001]`, `[OBS-E5-FRINGE-001]`

## 12. Registry Discipline

This registry should keep raw observables, fitted quantities, comparison-facing outputs, and audit indicators distinct.

Future contributors and code-generation sessions should use this document to avoid:

- placing fit summaries where raw observables belong
- treating comparison-facing quantities as primitive state variables
- silently changing output semantics across experiments
- obscuring the difference between mathematically grounded observables and later-stage interpretive outputs

A quantity should not be treated as implementation-ready merely because it is named. The status field and dependency field must remain visible.

## 13. Immediate Next Formalization Targets

The next observable-level formalization steps should focus on:

1. normalization convention for defect density
2. estimator definition for correlation length
3. transform and normalization convention for structure factor
4. strain-proxy normalization and unit handling
5. effective-coupling extraction definition
6. audit observable minimum requirements
