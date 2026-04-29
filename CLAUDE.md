# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository state

This repo is in a pre-code state. As of this writing it contains only a Python 3.12 virtualenv (`.venv/`), a `.gitignore`, and `docs/litellm-endpoints.md`. There is no source code, package manifest (`pyproject.toml` / `requirements.txt`), test suite, or build tooling yet. Treat decisions about layout, dependencies, and tooling as still open — confirm with the user before scaffolding.

## Python environment

- Python 3.12, project-local venv at `.venv/` (created via `python3 -m venv`).
- Activate with `source .venv/bin/activate` before running anything Python-related.
- Only `pip` is installed in the venv at present; add dependencies via `pip install` and capture them in a manifest once one exists.

## LiteLLM model endpoints

`docs/litellm-endpoints.md` is the source of truth for which models the project is intended to call. It contains two LiteLLM `config.yaml` variants (a 35B `Qwen3.6-Mesh-*` family and a 27B `Qwen3.6-Mesh-*` family) all pointing at the local LiteLLM proxy at `http://100.69.40.49:8080/v1`. The `model_name` aliases follow a deliberate role split that should be preserved when wiring code to models:

- `*-Structured` — low temperature, no thinking; for JSON/structured output and director/planner roles.
- `*-Mesh` (base) — fast non-thinking QA.
- `*-Thinking` — thinking enabled, short reasoning budget; default agent role.
- `*-Thinking-Long` — thinking enabled, larger output, stable (low temp); for long stable generations.
- `*-Creative-Long` — high temp + high reasoning budget; long creative output, 224k input window.
- `*-Code-Long` — low temp, high reasoning budget; long coding tasks, 224k input window.

The two config blocks in the doc are alternatives backed by different underlying models (`Qwen3.6-35B-A3B-Q5KM-Vision-64k` vs `Qwen3.6-27B-Q5KXL-87k-p3-q8`); only one is loaded into the LiteLLM proxy at a time. Code should target the `model_name` aliases, not the underlying model IDs, so swapping the backing model doesn't require code changes.
