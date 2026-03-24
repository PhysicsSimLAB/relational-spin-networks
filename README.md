# Relational Spin Networks

This repository contains the computational scaffold for Relational Spin Network (RSN) experiments in the PhysicsSimLAB organization. It is being structured to support auditable numerical experiments, provenance-aware outputs, and staged translation of the RSN research program into explicit computational artifacts.

## Status

Repository status: **scaffold**.

This repository is in an early architecture phase. Theory-specific numerical implementations are still being introduced incrementally, and the present goal is to establish a clean, extensible, and auditable research codebase before locking in full experiment logic.

## Research Framing

This repository is informed by an external Relational Spin Network (RSN) framework and associated projector-lattice / meta-gravity planning documents. In that framework, the basic physical picture begins from spin-anti-spin cells whose partial composition yields idempotent projectors, together with a triplet structure that distinguishes electromagnetic and meta-gravitational tiers.

Within the RSN note, spacetime is treated relationally rather than as a primitive container. A lattice of coherent spin-anti-spin cells furnishes tiered metrics, with the electromagnetic tier and a wider meta-gravitational tier related by a tiered causal structure.

These theory documents are external references, not internal source-of-truth code specifications. The role of this repository is to progressively translate selected parts of that framework into explicit, testable, and reproducible computational modules and experiment pipelines.

For the repository-facing experiment specification and implementation-planning layer, see `docs/experiment_protocol.md`.

## Initial Repository Layout

- `src/relational_spin_networks/core/`
  Core theory-facing modules for projector, energy, winding, block-spin, and strain abstractions. Current placeholders include `projector.py`, `energy.py`, `winding.py`, `block.py`, and `strain.py`.

- `src/relational_spin_networks/experiments/`
  Experiment entrypoints and staged implementations for RSN experiment families. Current placeholders include `e1.py`, `e2.py`, `e3.py`, and `e4.py`.

- `src/relational_spin_networks/configs/`
  Configuration structures for run parameters and experiment setup. Current placeholder: `base.py`.

- `src/relational_spin_networks/io/`
  Run-path utilities, manifests, and output serialization helpers. Current placeholders include `paths.py` and `run_manifest.py`.

- `src/relational_spin_networks/analysis/`
  Summary, aggregation, and post-run analysis utilities. Current placeholder: `summary.py`.

- `src/relational_spin_networks/provenance/`
  Metadata capture, checksums, and reproducibility support. Current placeholders include `metadata.py` and `checksums.py`.

- `tests/`
  Deferred test area for future code verification and theory-to-code checks.

- `docs/`
  Planned repository-internal documentation beyond the top-level README.

- `outputs/`
  Run artifacts, experiment outputs, metadata summaries, and checksum manifests.

- `tools/`
  Repository utilities, including checksum-maintenance helpers.

This structure is meant to support an auditable simulation workflow, modular experiment organization, and explicit provenance handling rather than a single monolithic script layout.

## Planned Experiment Progression

The intended progression is to stabilize the computational backbone first and then stage experiment families corresponding to the protocol's E1-E4 program, with later analysis extensions beyond that.

At a high level, those experiments are expected to cover defect freeze-out, finite-size critical behavior, strain-leakage auditing, and block-spin renormalization. A later extension is reserved for the twist-phase / detectability layer, which is being treated as a subsequent analysis direction rather than the first implementation target.

## Provenance and Outputs

The repository is being prepared for provenance-aware output handling from the start. The intended run organization follows an `outputs/<experiment>/<run_tag>/` pattern with metadata summaries and checksum tracking as planned features.

These are currently **planned** features built on top of a **scaffold** repository state. The repository layout anticipates checksum manifests, run metadata, and re-analysis support, but those guarantees are not yet **implemented** or **validated**.

## Environment

- Python 3.11
- `requirements.txt` is currently the canonical dependency entrypoint
- The initial environment is intentionally minimal while the architecture is stabilized

## Immediate Next Steps

1. Finalize top-level project framing
2. Define first domain modules
3. Add provenance utilities
4. Introduce first experiment stubs
5. Begin testable theory-to-code mapping
