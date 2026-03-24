# Experiment Protocol

## 1. Scope

This document translates the external RSN protocol sources into a repository-facing experiment specification for `relational-spin-networks`.

The original theory and protocol papers remain the external conceptual and scientific basis. This document serves a different role inside the repository: implementation guidance, experiment organization, provenance discipline, and staged translation of theory-facing objects into auditable computational artifacts.

This file is therefore not a replacement for the source papers. It is the internal protocol layer that future contributors and code-generation sessions should use when creating modules, experiment stubs, provenance utilities, and tests.

## 2. Source Basis

This protocol is derived from the following external documents:

1. **Projector-Lattice Meta-Gravity — Reproducible Simulation Protocol v0**
2. **RSN Experiment Upgrade Companion v0**

The extraction policy used here is hybrid:

- implementation-critical protocol content is kept as faithfully as possible
- broader narrative or interpretive prose is normalized into repository-facing engineering language
- unresolved or not-yet-implemented details are explicitly marked as deferred or external

`README.md` remains the high-level entrypoint for the repository. This document is the detailed internal experiment protocol.

## 3. Theory Kernel (Structured Summary)

This section records the theory-facing ingredients that matter directly for implementation planning. It is intentionally compact and does not attempt to reproduce the full conceptual narrative of the source papers.

### 3.1 Spin–anti-spin cell

The basic theory-facing unit is the coherent spin–anti-spin cell. In repository terms, this is the conceptual primitive from which projector objects, interaction energies, defect observables, and tiered geometric proxies are later derived.

Implementation status: **external / deferred**

### 3.2 Idempotent projector logic

A central implementation target is the idempotent projector representation associated with normalized spin-state data. In the core protocol, projector construction is the first algorithmic primitive and is treated as a theory-to-code anchor.

Repository implication:
- projector structure should become the first theory-facing object with explicit code verification
- idempotency preservation is a global correctness concern, not a cosmetic property

Implementation status: **scaffold**

### 3.3 Interaction / energy picture

Nearest-neighbour interaction energy is part of the baseline kernel dynamics. The protocol treats this as a local evaluative quantity used by Monte Carlo evolution and by later derived observables.

Repository implication:
- energy evaluation belongs in a dedicated theory-facing module
- local consistency and full-lattice consistency should be testable separately

Implementation status: **scaffold**

### 3.4 Winding / defect picture

The winding layer captures topological defect content. In the protocol, winding count is a primary observable for freeze-out style experiments and a bridge between microscopic evolution and experiment-level summaries.

Repository implication:
- topological counting should be isolated from simulation orchestration
- defect observables are experiment-facing outputs, not just internal diagnostics

Implementation status: **scaffold**

### 3.5 Block / renormalization picture

The block-spin layer provides a coarse-graining and renormalization pathway. It is part of the intended route from local lattice dynamics to effective flow quantities and speed-law recovery.

Repository implication:
- coarse-graining operations should later be represented as explicit transformations with their own admissibility and normalization checks
- experiment E4 depends on this layer

Implementation status: **scaffold**

### 3.6 Strain / leakage picture

The strain or leakage layer connects internal RSN quantities to observationally constrained proxy structure. In protocol terms, this is where normalized leakage measures become comparable to exclusion-style analysis.

Repository implication:
- strain proxies should be kept separate from raw evolution code
- observational comparison belongs to experiment and analysis layers, not core primitives alone

Implementation status: **scaffold**

### 3.7 Tiered metric / causal framing

The external RSN framing distinguishes an electromagnetic tier and a wider meta-gravitational tier. Inside the repository, this distinction is relevant primarily as a future modeling and interpretation boundary.

Repository implication:
- tier structure should inform naming, documentation, and future observable definitions
- it should not yet be treated as a completed numerical implementation

Implementation status: **external / deferred**

## 4. Equation-to-Code Planning Map

This repository adopts the following theory-to-code planning map. These entries define intended module responsibilities rather than completed implementations.

### 4.1 Projector

- theory object: idempotent projector
- intended module: `src/relational_spin_networks/core/projector.py`
- status: **scaffold**
- implementation note: future home of projector representation and admissibility-preserving normalization logic
- conceptual note: theory-facing object is explicit in the core protocol and should later become a first verification target

### 4.2 Energy

- theory object: nearest-neighbour interaction energy
- intended module: `src/relational_spin_networks/core/energy.py`
- status: **scaffold**
- implementation note: future home of local and aggregate energy evaluators
- conceptual note: should remain separate from orchestration logic used by Monte Carlo or experiment runners

### 4.3 Winding

- theory object: topological winding / defect count
- intended module: `src/relational_spin_networks/core/winding.py`
- status: **scaffold**
- implementation note: future home of defect-detection routines and winding observables
- conceptual note: experiment-facing observables should be derived from this layer, not embedded in plotting code

### 4.4 Block

- theory object: block-spin / renormalization operator
- intended module: `src/relational_spin_networks/core/block.py`
- status: **scaffold**
- implementation note: future home of coarse-graining operators and effective coupling extraction support
- conceptual note: later tied most directly to E4

### 4.5 Strain

- theory object: leakage / strain proxy
- intended module: `src/relational_spin_networks/core/strain.py`
- status: **scaffold**
- implementation note: future home of local and aggregated strain proxy evaluation
- conceptual note: observational comparison remains downstream and should be handled by experiment and analysis layers

### 4.6 Experiment orchestration

- theory object: experiment-family execution
- intended modules: `src/relational_spin_networks/experiments/e1.py` through `e5.py`
- status: **deferred**
- implementation note: experiment files should orchestrate runs, outputs, summaries, and validation boundaries
- conceptual note: experiment files should not become dumping grounds for theory primitives

## 5. Experiment Family Roadmap

This section records the intended experiment families as repository-facing specifications. All remain deferred until implemented.

### 5.1 E1 — Mini-Soliton Monte-Carlo

- name: Mini-Soliton Monte-Carlo
- goal: test RSN freeze-out criteria against simulated defect formation under controlled cooling
- high-level method: evolve lattice states under Monte Carlo cooling schedules and compare defect-density behavior to the analytic freeze-out expectation
- primary observables:
  - defect density
  - winding count
  - freeze-out scale
- expected outputs:
  - scaling plot of defect density versus cooling rate
  - theory-overlay comparison
  - reduced run summary
- validation / acceptance ideas:
  - fit quality between simulated trend and expected freeze-out behavior
  - nontrivial surviving defect signal
  - reproducible reduced outputs under controlled seeds where expected
- abort / caution notes:
  - invalid if run metadata is incomplete
  - invalid if state variables or observables produce NaN or Inf
  - invalid if inherited idempotency tolerances are violated
- implementation status: **deferred**

### 5.2 E2 — Quench vs Anneal

- name: Quench vs Anneal
- goal: infer critical behavior through finite-size scaling rather than a single-run qualitative transition picture
- high-level method: compare quench and anneal style evolution across sizes and extract collapse-oriented observables
- primary observables:
  - correlation length
  - structure factor
  - fitted exponents `nu` and `z`
- expected outputs:
  - table of fitted exponents with uncertainties
  - collapse diagnostic
  - reduced summary products suitable for re-analysis
- validation / acceptance ideas:
  - uncertainty-qualified exponents
  - interpretable collapse behavior
  - seed and step-count robustness tracking
- abort / caution notes:
  - undefined exponents
  - non-diagnostic collapse
  - schema-invalid configuration or metadata failure
- implementation status: **deferred**

### 5.3 E3 — Leakage Audit

- name: Leakage Audit
- goal: map RSN strain leakage into observational exclusion space
- high-level method: compute normalized strain proxies and compare them against sensitivity thresholds or detector-overlay assumptions
- primary observables:
  - normalized strain proxy
  - ratio `h_mg / h_GR`
  - sensitivity crossing
- expected outputs:
  - exclusion-style figure
  - detector-noise overlay view
  - reduced metadata summary
- validation / acceptance ideas:
  - unit consistency
  - explicit overlay assumptions
  - stable reduced observables across documented execution settings
- abort / caution notes:
  - invalid metadata or checksums
  - non-finite observables
  - hidden or undocumented detector assumptions
- implementation status: **deferred**

### 5.4 E4 — Block-Spin RG

- name: Block-Spin RG
- goal: estimate renormalization-group flow and recover a speed-law exponent quantitatively
- high-level method: apply block-spin style coarse graining, infer effective couplings, and fit flow quantities
- primary observables:
  - effective couplings `J1, J2, ...`
  - fitted beta-flow quantities
- expected outputs:
  - RG-flow table
  - regression summary
  - uncertainty band
- validation / acceptance ideas:
  - uncertainty-qualified slope or flow estimates
  - seed robustness
  - normalization and admissibility preservation under coarse graining
- abort / caution notes:
  - invalid coarse variables
  - unstable flow estimates
  - metadata or integrity failure
- implementation status: **deferred**

### 5.5 E5 — Twist-Phase Toy

- name: Twist-Phase Toy
- goal: test detectability of twist-induced phase structure under noise
- high-level method: construct a later-stage toy analysis of phase signatures under modeled noise conditions
- primary observables:
  - phase spectrum
  - fringe visibility
  - shot-noise signal-to-noise ratio
- expected outputs:
  - schematic
  - phase-spectrum figure
  - detectability summary
- validation / acceptance ideas:
  - signal remains above modeled shot-noise floor in stated regimes
  - assumptions are explicit and auditable
- abort / caution notes:
  - non-diagnostic or purely noise-dominated result without traceable support
  - incomplete metadata or broken provenance chain
- implementation status: **deferred**
- priority note: later-stage analysis target, not a first implementation path

## 6. Provenance and Output Rules

The repository is being prepared for provenance-aware execution from the start. The intended output root is:

`outputs/<experiment>/<run_tag>/`

### 6.1 Run tagging

Every run tag should follow the protocol pattern:

`<experiment>-<dateUTC>-<gitshort>-<seed>-<paramhash>`

This convention exists to make run identity traceable across summaries, plots, archives, and later audits.

### 6.2 Output structure

The upgraded protocol anticipates output organization under:

- `outputs/E1/`
- `outputs/E2/`
- `outputs/E3/`
- `outputs/E4/`
- `outputs/E5/`
- `outputs/analysis/`
- `outputs/figures/`
- `outputs/archives/`

Repository note:
- directory scaffolding may exist before the full workflow does
- path conventions should stabilize early, even before experiment logic is complete

### 6.3 Metadata expectations

Each run is expected to emit structured metadata sufficient to identify:

- experiment
- run tag
- UTC timestamp
- git hash
- environment hash
- configuration hash
- random seed
- backend
- thread count
- host or machine identifier
- final status

Repository note:
- metadata capture is a planned hard requirement for completed runs
- initial implementations may stage this in progressively richer forms

### 6.4 Checksum expectations

Run directories are expected to carry local checksum manifests, and repository-level integrity should eventually be summarized through a refreshed master checksum record after successful batch completion.

Repository note:
- checksum utilities are scaffolded now
- strict manifest generation remains a build target, not a completed guarantee

### 6.5 Archive expectations

Completed experiment bundles intended for preservation should eventually be archivable under an experiment- and run-tag-based path such as:

`archives/<experiment>/<run_tag>.tar.zst`

Repository note:
- archive conventions are part of the protocol
- archive automation remains deferred

### 6.6 Provenance principle

No plotted point, fitted exponent, exclusion boundary, or detectability claim should appear in a figure unless it is traceable to a run directory with intact metadata and checksums.

This is a repository-level discipline, not just a publication-stage concern.

## 7. Validation and Execution Discipline

The protocol distinguishes scaffold status from executed and validated experiment status.

### 7.1 Execution baseline

Default execution assumptions inherited from the protocol include:

- CPU-first execution
- `numba` as default backend
- two-thread baseline
- deterministic seed logging
- output rooted under `outputs/<experiment>/<run_tag>/`

These should be treated as the baseline execution posture until explicitly revised.

### 7.2 Shared abort conditions

A run must be flagged aborted if any of the following occur:

- unreadable or schema-invalid configuration input
- NaN or Inf in a state variable or observable
- idempotency violation above inherited tolerance
- incomplete metadata write
- checksum generation failure

### 7.3 Verification posture

Verification concerns whether the code is doing what the repository says it does. The protocol expects later checks for items such as:

- projector idempotency preservation
- agreement between local and full energy evaluators
- normalization of coarse variables after block-spin operations
- deterministic replay where documented
- rejection of malformed configuration or metadata

### 7.4 Numerical validation posture

Numerical validation is separate from code verification. The intended concerns include:

- monotonicity or expected trend checks under anneal settings
- thread-stability monitoring
- step-count convergence
- finite-precision robustness
- explicit reporting of seed variance

### 7.5 Physics validation posture

Physics support is stricter than code correctness or numerical stability. Each experiment family should later define its own target:

- E1: freeze-out trend quality and consistency with theory overlay
- E2: collapse quality and uncertainty-qualified exponent extraction
- E3: unit-consistent exclusion mapping with explicit overlay assumptions
- E4: uncertainty-qualified RG-flow recovery robust across seeds
- E5: detectable phase signal above stated modeled noise floor

### 7.6 Status distinction

The following states must not be conflated:

- scaffold exists
- code runs
- code is verified
- numerics are stable
- physics support is established

Repository organization should make these distinctions visible in outputs, summaries, and contributor language.

## 8. Status Labels

The following repository-facing status labels should be used consistently.

### 8.1 scaffold

Structure or placeholder exists, but no substantive implementation guarantee is being claimed.

### 8.2 deferred

The item is recognized as part of the protocol but intentionally postponed.

### 8.3 planned

The item has an intended repo role and near-term implementation path, but is not yet available.

### 8.4 implemented

The item has executable code in the repository.

### 8.5 validated

The item has passed the relevant stated validation level for its current scope.

### 8.6 external reference

The item remains primarily in the source papers and has not yet been translated into internal executable or testable repository form.

## 9. Immediate Translation Priorities

1. stabilize theory-facing module boundaries
2. add provenance utilities
3. add experiment stubs
4. add theory-to-code tests
5. add first executable experiment path
