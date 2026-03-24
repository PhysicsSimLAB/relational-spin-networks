# Architecture

This repository is currently in **scaffold** status. This file records the intended package layering so future additions preserve clear boundaries between theory-facing primitives, experiment orchestration, analysis, and provenance.

## Layering Rules

- `src/relational_spin_networks/core/`
  Holds theory-facing primitives and local computational objects such as projector, energy, winding, block, and strain representations. Core modules should not depend on experiment-specific orchestration or plotting concerns.

- `src/relational_spin_networks/experiments/`
  Holds experiment-family orchestration only. Experiment modules should compose core, config, IO, provenance, and analysis pieces rather than re-implement theory primitives.

- `src/relational_spin_networks/configs/`
  Holds repository-facing configuration structures. Configuration parsing formats and schema machinery remain deferred.

- `src/relational_spin_networks/io/`
  Holds run-path, manifest, and output-organization structures. This layer should define how runs are named and organized without embedding theory logic.

- `src/relational_spin_networks/provenance/`
  Holds metadata and checksum structures. Provenance concerns should remain explicit and separate from numerical kernels.

- `src/relational_spin_networks/analysis/`
  Holds summaries, aggregations, and downstream interpretation helpers. Analysis should consume experiment outputs rather than define core evolution rules.

- `tests/`
  Holds future verification and validation coverage. Test status remains **deferred** until substantive implementations exist.

- `docs/`
  Holds repository-internal documentation. The main internal protocol reference is `docs/experiment_protocol.md`.

## Dependency Direction

The intended dependency direction is:

`configs -> core -> io/provenance -> experiments -> analysis`

Repository note:
- `core` should remain reusable and narrowly scoped
- `experiments` may depend on lower layers
- `analysis` should sit downstream of executed or recorded experiment artifacts
- provenance requirements apply across all executable layers

## Current Discipline

- keep modules small and auditable
- prefer explicit structural types before adding runtime behavior
- do not mix theory primitives with experiment orchestration
- do not treat external RSN source documents as direct code specifications
- keep provenance requirements visible from the start

## Status Vocabulary

Use the repository protocol labels consistently:

- `scaffold`
- `deferred`
- `planned`
- `implemented`
- `validated`
- `external reference`
