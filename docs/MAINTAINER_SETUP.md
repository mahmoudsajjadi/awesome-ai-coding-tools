# Maintainer's Development Setup & Workflow Notes

> **Disclaimer & Label:** This document represents the opinionated, personal workflow preferences of the project maintainer ([Mahmoud Sajjadi](https://github.com/mahmoudsajjadi)). It is not an objective endorsement or repository standard; rather, it details a concrete, reproducible development setup used daily for software engineering and maintaining this catalog.

---

## 1. Concrete Toolchain Breakdown

| Layer | Selected Tool | Rationale & Practical Workflow |
| :--- | :--- | :--- |
| **Editor / IDE** | **VS Code** (with minimal extensions) + **Zed** | VS Code handles complex language servers (TypeScript, Python Pylance) and multi-root workspaces. Zed is used as a lightweight, zero-latency scratchpad for rapid single-file inspection and diff reviews. |
| **Terminal & Multiplexing** | **Ghostty** + **tmux** | Ghostty provides GPU-accelerated rendering and native font ligature support. `tmux` maintains persistent multi-pane sessions, allowing long-running CLI agents to execute independently in background windows. |
| **CLI Coding Agent** | **Claude Code** (Primary) & **Aider** (Secondary) | **Claude Code** is the primary driver for broad codebase exploration, whole-repo refactors, and multi-file bash execution. **Aider** (with `--architect` mode) is preferred for strict, atomic git commit generation and offline pairing with local models. |
| **Local Model Engine** | **Ollama** | Serves quantized weights locally via simple CLI management (`ollama run`). Acts as a fallback backend when working offline or testing air-gapped workflows. |
| **Local Model Weights** | **Qwen 2.5 Coder 14B** (Q4_K_M) | The daily sweet-spot for local inference on a 16GB VRAM GPU. Produces accurate syntax, respects negative constraints, and executes at 35–45 tokens/second. |
| **Context Standards** | **`AGENTS.md`** | Kept under 50 lines in the project root. Outlines non-inferable test loops (`pytest`, `npm test`), build rules, and strict negative boundaries (e.g., no wildcard imports, never overwrite docstrings). |

---

## 2. Daily Workflow Pattern

```
1. Task Formulation & Planning
   └── Maintainer writes architectural goal or task prompt.
   
2. CLI Agent Execution Loop
   └── Claude Code or Aider is launched in a dedicated tmux window.
   └── Agent inspects repository AST / files via AGENTS.md instructions.
   └── Agent implements changes and runs the local test suite automatically.

3. Human-in-the-Loop Review
   └── Maintainer reviews git diffs via `git diff` or VS Code Source Control.
   └── No automated commit is accepted without running verification scripts:
       `python scripts/verify_catalog.py`
       `git status`
```

---

## 3. Guiding Maintenance Principles

1. **Deterministic Verification First:** Always verify tool claims against real documentation, source repositories, or live tests. Never commit unverified numbers or synthetic benchmark claims.
2. **Lean Context Over Stuffed Context:** Do not bloat context files (`AGENTS.md`, `CLAUDE.md`) with redundant explanations of public libraries. Modern LLMs already possess broad pre-trained programming knowledge; context files should exclusively provide **project-specific non-inferables**.
3. **Keep the Catalog Neutral:** Avoid marketing hyperbole ("ultimate", "super-fast", "game-changing"). Prefer descriptive, verifiable characteristics: license, pricing model, context length, architecture, and exact capabilities.
