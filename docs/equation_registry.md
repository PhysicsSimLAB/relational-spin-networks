# Equation Registry

## 1. Purpose

This document provides a stable, repository-internal ledger of RSN-facing equations, named relations, and required mathematical placeholders.

Its purpose is to support implementation planning, experiment mapping, auditability, and disciplined theory-to-code translation. It should be consulted before adding theory-facing numerical code, experiment logic, or validation checks.

This registry distinguishes between:

- equations or relations already present in the external RSN source basis
- placeholders for mathematical objects that the repository still requires before deep implementation can proceed

Placeholder entries are intentional. They mark formalization gaps explicitly so that future code does not silently invent mathematics.

## 2. Role in the Repository

The repository now uses the following internal documentation layers:

1. `README.md` for project framing
2. `docs/experiment_protocol.md` for experiment organization and provenance
3. `docs/math_foundations.md` for mathematical structure and status labels
4. `docs/equation_registry.md` for equation-level reference and formalization gaps

This document is the most direct mathematical lookup layer for future implementation work.

## 3. Entry Format

Each equation entry should record:

- equation key
- name
- expression
- symbol definitions
- status
- source basis
- intended module
- experiment usage
- implementation notes
- open questions

The status vocabulary used here is:

- `definition`
- `derived_relation`
- `phenomenological_relation`
- `algorithmic_approximation`
- `deferred_placeholder`
- `external_reference`

## 4. Established Relations from the Current Source Basis

### [EQ-IDEMP-001] Projector Idempotency

- **Expression**: `(s ∘ s*)^2 = s ∘ s*`
- **Symbols**:
  - `s`: spin state
  - `s*`: anti-spin or conjugate partner
  - `∘`: composition law used to form the projector object
- **Status**: `definition / derived_relation`
- **Source basis**: `RSN paper`
- **Intended module**: `src/relational_spin_networks/core/projector.py`
- **Used by**: `cross-cutting`
- **Implementation notes**: idempotency should be treated as a correctness constraint for later numerical realizations. Future code should declare an admissibility tolerance explicitly rather than assume one silently.
- **Open questions**: exact numerical representation of the composition law; exact tolerance policy for finite-precision checks.

### [EQ-METRIC-001] Tiered Metric Distinction

- **Expression**: `g^(1)_{μν}, g^(2)_{μν}`
- **Symbols**:
  - `g^(1)_{μν}`: inner or electromagnetic-tier metric
  - `g^(2)_{μν}`: outer or meta-gravitational-tier metric
- **Status**: `definition`
- **Source basis**: `RSN paper`
- **Intended module**: `cross-cutting documentation anchor`
- **Used by**: `E3`, `E5`, `cross-cutting interpretation`
- **Implementation notes**: this registry records the tier distinction as a stable mathematical reference point. Future code should not collapse the two tiers into one undifferentiated structure without explicit justification.
- **Open questions**: exact internal representation for later numerical work; which later modules need direct tier-aware quantities.

### [EQ-NULL-001] Null-Cone Hierarchy

- **Expression**: `DEFERRED FORMAL EXPRESSION: tiered causal hierarchy between electromagnetic and meta-gravitational structures`
- **Symbols**:
  - `g^(1)_{μν}`: electromagnetic-tier metric
  - `g^(2)_{μν}`: meta-gravitational-tier metric
- **Status**: `external_reference`
- **Source basis**: `RSN paper`
- **Intended module**: `cross-cutting interpretation anchor`
- **Used by**: `E5`, `cross-cutting interpretation`
- **Implementation notes**: preserve as a named relation even before a repo-internal formal statement is stabilized.
- **Open questions**: whether this should later become a formal relation entry with explicit mathematical conditions or remain an interpretation-layer constraint.

### [EQ-SPEED-001] Meta-Gravitational Speed Law

- **Expression**: `v_mg = c (L_p / L_mg)^(3/2)`
- **Symbols**:
  - `v_mg`: meta-gravitational speed or scale quantity
  - `c`: electromagnetic reference speed
  - `L_p`: Planck-scale reference length
  - `L_mg`: meta-gravitational scale
- **Status**: `phenomenological_relation`
- **Source basis**: `RSN paper`
- **Intended module**: `src/relational_spin_networks/core/block.py`
- **Used by**: `E4`, `cross-cutting interpretation`
- **Implementation notes**: preserve as a named scaling law even before any fitting or RG estimator is implemented.
- **Open questions**: whether future code treats this as a comparison target, inferred law, or calibration relation.

### [EQ-PERIOD-001] 720-Degree Periodicity

- **Expression**: `DEFERRED FORMAL EXPRESSION: 720-degree periodicity associated with the underlying spin structure`
- **Symbols**:
  - `θ`: generalized phase or rotation parameter
- **Status**: `external_reference`
- **Source basis**: `RSN paper`
- **Intended module**: `cross-cutting interpretation anchor`
- **Used by**: `E5`, `cross-cutting interpretation`
- **Implementation notes**: record the periodicity statement as mathematically important, but do not force a computational reduction until a stable representation is specified.
- **Open questions**: exact formal repo-internal statement; whether later code will need direct phase-tracking objects.

### [EQ-ACTION-001] Action-Level Formulation

- **Expression**: `DEFERRED FORMAL EXPRESSION: action S[g^(1), π] and related structures`
- **Symbols**:
  - `S`: action functional
  - `g^(1)`: inner or electromagnetic-tier metric structure
  - `π`: projector-facing quantity
- **Status**: `external_reference`
- **Source basis**: `RSN paper`
- **Intended module**: `cross-cutting mathematical anchor`
- **Used by**: `cross-cutting`
- **Implementation notes**: preserve as a formal target, not yet an executable update law.
- **Open questions**: exact internal transcription policy for the action and whether separate action and field-equation entries are needed later.

### [EQ-FIELD-001] Field-Equation Formulation

- **Expression**: `DEFERRED FORMAL EXPRESSION: field-equation relations associated with the action-level description`
- **Symbols**:
  - `g^(1)_{μν}`: inner metric structure
  - `π`: projector-facing quantity
- **Status**: `external_reference`
- **Source basis**: `RSN paper`
- **Intended module**: `cross-cutting mathematical anchor`
- **Used by**: `cross-cutting`
- **Implementation notes**: preserve as a named mathematical target without treating it as a direct simulation law.
- **Open questions**: which parts should later become formal internal definitions versus interpretation-only references.

### [EQ-LEAK-001] Leakage Relation

- **Expression**: `h_mg(f) = κ (v_mg / c)^(-2) h_GR(f)`
- **Symbols**:
  - `h_mg(f)`: RSN-facing strain or leakage signal at frequency `f`
  - `κ`: coupling or leakage factor
  - `v_mg`: meta-gravitational speed or scale quantity
  - `c`: electromagnetic reference speed
  - `h_GR(f)`: comparison strain baseline
- **Status**: `phenomenological_relation`
- **Source basis**: `RSN paper`
- **Intended module**: `src/relational_spin_networks/core/strain.py`
- **Used by**: `E3`
- **Implementation notes**: later code must document units, normalization assumptions, and comparison regime explicitly.
- **Open questions**: exact detector-facing normalization and what data products count as validated overlays.

## 5. Placeholder Entries for Missing-but-Required Mathematics

### [EQ-PROJ-PLH-001] Projector Construction Recipe

- **Expression**: `DEFERRED: explicit construction rule for π_x from site-local spin data`
- **Symbols**:
  - `π_x`: site-local projector
  - `x`: lattice site index
- **Status**: `deferred_placeholder`
- **Source basis**: `internal placeholder derived from protocol needs`
- **Intended module**: `src/relational_spin_networks/core/projector.py`
- **Used by**: `E1`, `E2`, `E4`, `cross-cutting`
- **Implementation notes**: required before any serious projector-facing code can be considered mathematically anchored.
- **Open questions**: exact local state representation; normalization rule; whether projector construction is algebraic, matrix-based, or operator-based.

### [EQ-ENERGY-PLH-001] Local Interaction Energy Law

- **Expression**: `DEFERRED: explicit nearest-neighbour Hamiltonian or local energy functional`
- **Symbols**:
  - `π_x`: site-local projector or equivalent local state object
  - `⟨x,y⟩`: neighbouring lattice sites
  - `J`: coupling parameter(s)
- **Status**: `deferred_placeholder`
- **Source basis**: `internal placeholder derived from protocol needs`
- **Intended module**: `src/relational_spin_networks/core/energy.py`
- **Used by**: `E1`, `E2`
- **Implementation notes**: must distinguish local energy evaluation from aggregate lattice energy; should later support consistency testing.
- **Open questions**: sign convention, coupling family, admissibility penalties, boundary-condition dependence.

### [EQ-UPD-PLH-001] Update / Transition Rule

- **Expression**: `DEFERRED: explicit accepted update law or Monte Carlo acceptance rule`
- **Symbols**:
  - `ΔE`: local energy difference
  - `β`: inverse-temperature or control parameter
  - `u`: proposal or update variable
- **Status**: `deferred_placeholder`
- **Source basis**: `internal placeholder derived from protocol needs`
- **Intended module**: `src/relational_spin_networks/experiments/`
- **Used by**: `E1`, `E2`
- **Implementation notes**: should later specify admissibility checks, rejection behavior, and reproducibility constraints.
- **Open questions**: proposal distribution, acceptance kernel, anneal schedule coupling, deterministic replay guarantees.

### [EQ-WIND-PLH-001] Winding / Defect Formula

- **Expression**: `DEFERRED: explicit formula for extracting winding or defect count from local state data`
- **Symbols**:
  - `W`: winding observable
  - `π_x`: site-local state object
  - `C`: local contour, plaquette, or aggregation region
- **Status**: `deferred_placeholder`
- **Source basis**: `internal placeholder derived from protocol needs`
- **Intended module**: `src/relational_spin_networks/core/winding.py`
- **Used by**: `E1`
- **Implementation notes**: should later define counting conventions, sign rules, and aggregation policy explicitly.
- **Open questions**: contour definition, branch handling, thresholding, relation to defect density.

### [EQ-BLOCK-PLH-001] Block-Spin Coarse-Graining Map

- **Expression**: `DEFERRED: explicit map from fine lattice variables to coarse variables`
- **Symbols**:
  - `π_B`: coarse block variable
  - `B`: block index
  - `{π_x}`: local states within a block
- **Status**: `deferred_placeholder`
- **Source basis**: `internal placeholder derived from protocol needs`
- **Intended module**: `src/relational_spin_networks/core/block.py`
- **Used by**: `E4`
- **Implementation notes**: later needs admissibility preservation, normalization policy, and effective coupling extraction support.
- **Open questions**: block admissibility rule, normalization after aggregation, regression target for flow extraction.

### [EQ-STRAIN-PLH-001] Strain Proxy Definition

- **Expression**: `DEFERRED: explicit local or aggregate strain proxy derived from RSN state variables`
- **Symbols**:
  - `h_mg`: RSN-facing strain quantity
  - `π_x`: local state variable
  - `S`: aggregate state summary
- **Status**: `deferred_placeholder`
- **Source basis**: `internal placeholder derived from protocol needs`
- **Intended module**: `src/relational_spin_networks/core/strain.py`
- **Used by**: `E3`
- **Implementation notes**: should later separate raw proxy construction from detector-overlay comparison.
- **Open questions**: aggregation convention, unit normalization, mapping to comparison-facing outputs.

## 6. Crosswalk from Equations to Experiments

### 6.1 E1

Primary equation dependencies:

- `[EQ-IDEMP-001]`
- `[EQ-PROJ-PLH-001]`
- `[EQ-ENERGY-PLH-001]`
- `[EQ-UPD-PLH-001]`
- `[EQ-WIND-PLH-001]`

### 6.2 E2

Primary equation dependencies:

- `[EQ-IDEMP-001]`
- `[EQ-PROJ-PLH-001]`
- `[EQ-ENERGY-PLH-001]`
- `[EQ-UPD-PLH-001]`

### 6.3 E3

Primary equation dependencies:

- `[EQ-LEAK-001]`
- `[EQ-STRAIN-PLH-001]`
- `[EQ-METRIC-001]`

### 6.4 E4

Primary equation dependencies:

- `[EQ-SPEED-001]`
- `[EQ-BLOCK-PLH-001]`
- `[EQ-PROJ-PLH-001]`

### 6.5 E5

Primary equation dependencies:

- `[EQ-PERIOD-001]`
- `[EQ-NULL-001]`
- later-stage formalization still required

## 7. Registry Discipline

This registry should remain explicit about the difference between established relations and placeholders.

A placeholder entry is not a failure. It is a formal marker that the repository still lacks a stable internal mathematical statement needed before deep implementation.

Future contributors and code-generation sessions should use this registry to avoid:

- inventing undocumented formulas inside modules
- silently changing mathematical meaning across files
- conflating interpretation with executable law
- writing experiment logic before its governing quantities are formally declared

## 8. Immediate Next Formalization Targets

The next equation-level formalization steps should focus on:

1. projector construction recipe
2. local interaction energy law
3. accepted update rule
4. winding / defect formula
5. block-spin coarse-graining map
6. strain proxy definition

Those additions should be made by refining placeholder entries into stable repository-internal mathematical statements rather than by bypassing the registry.
