# Math Foundations

## 1. Purpose

This document internalizes the mathematical backbone of the Relational Spin Networks (RSN) repository at a repository-facing level.

It is not simulation code, and it is not a replacement for the external theory papers. Its purpose is to provide a stable internal mathematical reference that future contributors, experiment authors, and code-generation sessions can use when translating RSN concepts into explicit computational modules.

This document is the repository’s math-facing specification layer. It sits between the external theory sources and future code.

## 2. Role in the Repository

The repository distinguishes three layers:

1. `README.md` gives the high-level project framing.
2. `docs/experiment_protocol.md` gives the experiment and provenance structure.
3. `docs/math_foundations.md` gives the mathematical objects, laws, relations, and status labels that code should eventually follow.

This separation exists to prevent drift between conceptual framing, protocol requirements, and formal mathematical content.

## 3. Source Position

The mathematical material summarized here is derived from external RSN theory and protocol documents.

Inside the repository, this document should be treated as an internal mathematical reference for implementation planning. It records definitions, named relations, and modeling targets in normalized form.

Where a statement remains conceptual, interpretive, phenomenological, or not yet implementation-ready, that status should be made explicit rather than blurred.

## 4. Status Labels for Mathematical Content

Each mathematical object or relation in this repository should eventually be classified using the following labels.

### 4.1 Axiom

A starting principle taken as part of the theory-facing framework.

### 4.2 Definition

A formally introduced object, quantity, or construction.

### 4.3 Derived relation

A relation treated as following from prior structure within the framework.

### 4.4 Phenomenological relation

A relation used for modeling or comparison that may not yet function as a first-principles derivation inside the repository.

### 4.5 Algorithmic approximation

A numerical or operational form intended for simulation or estimation.

### 4.6 Interpretive note

A conceptual or explanatory statement that guides understanding but is not yet a direct coding target.

### 4.7 Conjectural extension

A proposed extension or interpretation not yet stabilized as a coding baseline.

### 4.8 Deferred

Recognized as mathematically relevant, but not yet translated into a stable internal form for implementation.

## 5. Notation Discipline

The repository should stabilize notation before writing theory-facing code.

### 5.1 Core symbols

The following symbols are reserved for RSN-facing mathematics:

- `s` : spin state
- `s*` : anti-spin or conjugate partner
- `π` : projector object
- `π_x` : site-local projector at lattice site `x`
- `π*` : preferred or reference projector, if later needed
- `g^(1)_{μν}` : inner or electromagnetic-tier metric
- `g^(2)_{μν}` : outer or meta-gravitational-tier metric
- `L_p` : Planck-scale reference length
- `L_mg` : meta-gravitational scale
- `v_mg` : meta-gravitational signal scale or speed quantity
- `κ` : leakage or strain coupling factor
- `λ`, `β`, `α` : reserved theory parameters to be defined only when explicitly stabilized

### 5.2 Naming discipline for code translation

Future code should preserve a stable naming bridge to the math:

- `pi_x` for `π_x`
- `g1` for `g^(1)_{μν}`
- `g2` for `g^(2)_{μν}`
- `vmg` for `v_mg`
- `kappa` for `κ`

The symbol `π` must be treated as a projector symbol, not confused with the mathematical constant pi.

## 6. Primitive Objects

This section records the core mathematical objects that future code is expected to reference.

### 6.1 Spin–anti-spin cell

Status: **Definition**

The basic theory-facing unit is the coherent spin–anti-spin cell formed from a spin state and its anti-spin or conjugate partner.

Repository role:
- foundational conceptual primitive
- upstream source for projector construction
- basis for later local energy and defect observables

Implementation status: **deferred**

### 6.2 Projector object

Status: **Definition**

The projector is the idempotent object associated with the spin–anti-spin cell. It is one of the first theory-facing quantities intended for explicit computational realization.

Repository role:
- theory-to-code anchor
- object whose admissibility and idempotency must later be checked numerically
- likely basis for local state normalization

Implementation status: **scaffold**

### 6.3 Tier metrics

Status: **Definition**

The framework distinguishes at least two metric tiers:

- an inner or electromagnetic-tier metric `g^(1)_{μν}`
- an outer or meta-gravitational-tier metric `g^(2)_{μν}`

Repository role:
- conceptual boundary for observable interpretation
- future source for tier-specific modeling and causal comparisons

Implementation status: **external reference**

### 6.4 Winding / defect object

Status: **Definition**

Topological winding content functions as a defect observable bridging local state organization and experiment-level measurements.

Repository role:
- future input to freeze-out and defect-density analysis
- must remain distinct from plotting or summary-only code

Implementation status: **scaffold**

### 6.5 Block-spin object

Status: **Definition**

The block-spin object represents the coarse-grained or renormalized description obtained from local lattice data.

Repository role:
- future bridge between local state data and renormalization-flow observables
- expected to support E4-style analysis

Implementation status: **scaffold**

### 6.6 Strain / leakage proxy

Status: **Definition**

The strain or leakage quantity provides a normalized proxy used to compare RSN-facing quantities against observational or exclusion-style analysis targets.

Repository role:
- future bridge from internal lattice structure to detector-facing or comparison-facing observables
- belongs at the interface between core math and experiment analysis

Implementation status: **scaffold**

## 7. Core Relations

This section records the main mathematical relations that should exist as stable internal reference points before deep implementation begins.

## 7.1 Idempotency relation

Status: **Definition / Derived relation**

The projector associated with the spin–anti-spin cell satisfies the idempotency condition

`(s ∘ s*)^2 = s ∘ s*`

Repository meaning:
- the projector must remain mathematically idempotent in the intended formulation
- future numerical implementations should preserve or monitor this property
- violation beyond tolerance should later count as a correctness failure

Implementation status: **planned**

## 7.2 Tiered metric relation

Status: **Definition**

The framework distinguishes a tiered metric structure involving `g^(1)_{μν}` and `g^(2)_{μν}`.

Repository meaning:
- tier structure informs naming and modeling boundaries
- future implementations should not collapse these tiers into a single undifferentiated quantity unless explicitly justified

Implementation status: **external reference**

## 7.3 Null-cone hierarchy

Status: **Derived relation / Interpretive note**

The external RSN framing treats the tier structure as supporting a hierarchy of causal or signaling structure between the electromagnetic and meta-gravitational tiers.

Repository meaning:
- relevant for interpretation and later experiment framing
- not yet a direct numerical implementation target

Implementation status: **deferred**

## 7.4 Speed law

Status: **Phenomenological relation**

A core scaling relation appears in the form

`v_mg = c (L_p / L_mg)^(3/2)`

Repository meaning:
- this is a named scaling law that should be preserved in internal mathematical records
- future code may later use this as a derived or fitted comparison target
- the repository should not yet assume more than the stabilized relation itself

Implementation status: **planned**

## 7.5 Periodicity relation

Status: **Interpretive note / Derived relation**

The framework includes 720-degree periodicity statements associated with the underlying spin structure.

Repository meaning:
- this is mathematically important for theory-facing interpretation
- no direct computational reduction should be assumed until a stable numerical representation is specified

Implementation status: **deferred**

## 7.6 Action-level formulation

Status: **Definition / External reference**

The RSN framework includes an action-level mathematical formulation involving the tier metric structure and projector-facing quantities.

Repository meaning:
- action-level material is mathematically important
- it should eventually be recorded in more formal internal detail
- it is not yet ready to function as a direct code primitive in the current repository

Implementation status: **external reference**

## 7.7 Field-equation level formulation

Status: **Derived relation / External reference**

The framework also includes field-equation style relations associated with the action-level description.

Repository meaning:
- these relations should be preserved as formal mathematical targets
- they should not yet be treated as executable update laws in the repository

Implementation status: **external reference**

## 7.8 Leakage relation

Status: **Phenomenological relation**

A named leakage relation appears in the form

`h_mg(f) = κ (v_mg / c)^(-2) h_GR(f)`

Repository meaning:
- this is a core bridge between RSN-facing strain quantities and comparison-facing observables
- future experiment analysis may use this relation as a normalization or interpretive target
- assumptions and units must be documented when implemented

Implementation status: **planned**

## 8. Algorithm-Facing Mathematical Targets

These are the main mathematical targets that should later be translated into code, but are not yet code in this document.

### 8.1 Projector construction

Target role:
- represent site-local projector structure
- preserve admissibility and idempotency under intended normalization conventions

Current status: **scaffold**

### 8.2 Interaction energy

Target role:
- define local or nearest-neighbour interaction energy
- support both local evaluation and aggregate lattice evaluation

Current status: **scaffold**

### 8.3 Update rule

Target role:
- define the accepted state-update or Monte Carlo transition law
- specify admissibility conditions and rejection conditions

Current status: **deferred**

### 8.4 Winding formula

Target role:
- define defect counting or winding extraction from local state structure
- support experiment-facing observables without embedding logic in plotting layers

Current status: **scaffold**

### 8.5 Block-spin map

Target role:
- define coarse-graining or renormalization transformations
- preserve whatever normalization or admissibility constraints are mathematically required

Current status: **scaffold**

### 8.6 Strain proxy

Target role:
- define local or aggregate strain/leakage proxy values
- support observational overlays and exclusion-style analysis

Current status: **scaffold**

## 9. Experiment-Facing Mathematical Quantities

The repository should distinguish theory objects from experiment-facing observables.

### 9.1 E1-facing quantities

- defect density
- winding count
- freeze-out scale

Role:
- support defect freeze-out analysis and comparison with expected scaling structure

### 9.2 E2-facing quantities

- correlation length
- structure factor
- fitted exponents such as `nu` and `z`

Role:
- support finite-size scaling and collapse-oriented analysis

### 9.3 E3-facing quantities

- normalized strain proxy
- `h_mg / h_GR`
- sensitivity crossing or exclusion comparison

Role:
- support leakage auditing and detector-facing interpretation

### 9.4 E4-facing quantities

- effective couplings
- beta-flow estimates
- renormalization slope or flow summaries

Role:
- support block-spin and RG-style experiment analysis

### 9.5 E5-facing quantities

- phase spectrum
- fringe visibility
- shot-noise signal-to-noise ratio

Role:
- support later-stage twist-phase detectability analysis

## 10. Invariants, Constraints, and Admissibility

The repository should not proceed to implementation without stabilizing the mathematical constraints that code is expected to preserve.

### 10.1 Idempotency preservation

Projector objects must later preserve the intended idempotency property, either exactly or within an explicitly declared tolerance.

Status: **planned**

### 10.2 Finite observable requirement

Derived observables used in experiments must remain finite and auditable. Non-finite values should later count as invalid numerical states.

Status: **planned**

### 10.3 Normalization discipline

Coarse-grained, strain-facing, or transformed objects should not silently drift away from their declared normalization conventions.

Status: **planned**

### 10.4 Tier distinction discipline

Tier-1 and Tier-2 structures must not be conflated in documentation or code unless an explicit mathematical reduction is introduced and justified.

Status: **planned**

## 11. Parameter and Units Registry

This repository still requires a formal internal registry for parameters and units.

At minimum, future revisions should stabilize:

- symbol
- name
- interpretation
- default unit or unitless status
- allowed range if known
- source basis
- implementation status

Expected early entries include:

- `L_p`
- `L_mg`
- `v_mg`
- `κ`
- cooling-rate parameters
- lattice size parameters
- block size parameters
- analysis frequencies or detector-facing comparison parameters

Current status: **deferred**

## 12. Math-to-Module Translation Boundary

This document does not contain code, but it establishes the intended theory-to-module map.

- projector mathematics -> `src/relational_spin_networks/core/projector.py`
- energy mathematics -> `src/relational_spin_networks/core/energy.py`
- winding mathematics -> `src/relational_spin_networks/core/winding.py`
- block-spin mathematics -> `src/relational_spin_networks/core/block.py`
- strain mathematics -> `src/relational_spin_networks/core/strain.py`

The purpose of this mapping is to ensure that future code modules have a stable mathematical anchor rather than drifting into ad hoc implementation language.

## 13. Open Mathematical Gaps

The repository still lacks several internalized mathematical artifacts needed before deep implementation.

### 13.1 Missing internal formalizations

- explicit projector construction recipe
- explicit Hamiltonian or local energy law
- explicit update rule
- explicit winding formula
- explicit block-spin map
- explicit strain formula
- explicit tolerance declarations
- explicit units registry
- explicit theorem-like statements or admissibility propositions

### 13.2 Priority of future formalization

The next formal mathematical pass should focus on:

1. projector construction
2. interaction energy
3. winding definition
4. block-spin transformation
5. strain/leakage normalization
6. parameter and units registry

## 14. Repository Discipline

This document should be treated as the internal mathematical anchor for the repository until a more detailed formal specification supersedes it.

Future code-generation work should not invent equations, update laws, tolerances, or parameter regimes that are absent here or absent from the external source basis without clearly marking those additions.

The repository should always preserve the distinction between:

- mathematical definition
- phenomenological relation
- algorithmic approximation
- interpretive note
- conjectural extension

That distinction is necessary for auditability, correctness, and scientific clarity.
