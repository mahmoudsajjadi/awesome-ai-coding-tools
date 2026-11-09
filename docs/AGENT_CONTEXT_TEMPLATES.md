# Agent Context Templates: AGENTS.md, CLAUDE.md, and .cursorrules

A reference collection of starter context templates for autonomous coding agents, CLI tools, and agentic IDEs.

Modern coding agents read persistent workspace instructions to understand project architecture, build commands, test scripts, and style rules. Using lean, targeted instructions avoids context pollution and repetitive prompting.

---

## 1. Context Specification Comparison

| Specification / File | Ecosystem & Scope | Supported Agents | Primary Use Case |
| :--- | :--- | :--- | :--- |
| **`AGENTS.md`** | **Universal Open Standard** | Claude Code, Cursor, Codex CLI, Aider, Windsurf, Zed, OpenCode, Jules | Root project memory, non-inferable commands, architecture boundaries. |
| **`CLAUDE.md`** | Tool-Specific (Anthropic) | Claude Code CLI, Claude Desktop | Sub-agent permissions, test-first loop commands, compact CLI instructions. |
| **`.cursor/rules/*.mdc`** / **`.cursorrules`** | Scoped Directory (Cursor) | Cursor IDE | File-glob matched rules loaded dynamically when matching files are edited. |
| **`SKILL.md`** | Task-Triggered Plugin | Antigravity, OpenCode | Procedural instructions loaded on-demand when specific slash commands fire. |

> **Context Best Practice:** Do not dump entire directory trees or large code snippets into root instructions. Modern agents construct dynamic AST dependency maps via Tree-sitter. Keep instruction files concise (<50 lines) focused on non-inferable commands and negative constraints.

---

## 2. Universal `AGENTS.md` Starter Template

Save as `AGENTS.md` in the project root:

```markdown
# AGENTS.md — Universal Agent Context Specification

## 1. Project Overview & Architecture
- Stack: TypeScript / Node.js (or Python 3.12 / FastAPI)
- Structure: Modular services under `src/` (or `app/`), test suites under `tests/`.

## 2. Essential Commands (Non-Inferable)
- Build: `npm run build` (or `cargo build --release` / `poetry run build`)
- Fast Test Loop: `npm test -- --bail` (or `pytest -v --tb=short`)
- Lint & Format: `npm run lint` (or `ruff check .`)

## 3. Negative Constraints (What NOT to Do)
- NEVER commit secrets, API keys, or `.env` files.
- NEVER delete or overwrite existing docstrings, copyright headers, or test suites unless explicitly requested.
- DO NOT use wildcard imports (`from module import *`).
- DO NOT introduce heavy external dependencies for utilities solvable with standard libraries.

## 4. Code Style & Typing Standards
- All code must pass strict type checking without warnings (`mypy --strict` or TypeScript `strict: true`).
- Keep functions modular and under 50 lines. Keep files under 300 lines.
- Commits must adhere to Conventional Commits: `feat:`, `fix:`, `refactor:`, `test:`, `docs:`.
```

---

## 3. Claude Code `CLAUDE.md` Starter Template

Save as `CLAUDE.md` in the project root:

```markdown
# Repository Guidelines & Quality Standards for Claude Code

## Architecture Principles
1. Maintain clean separation between business logic, data models, and external APIs.
2. Favor explicit, strongly-typed interfaces over dynamic object passing.
3. Keep external dependencies minimal and vetted.

## Git & Development Workflow
- Commit Style: Use Conventional Commits (`feat:`, `fix:`, `refactor:`, `test:`, `docs:`).
- Atomic Commits: Single-concern, bisectable commits. Never mix refactors with feature changes.
- Verification First: Before completing tasks, always execute the relevant test command:
  - Python: `pytest -v --tb=short`
  - TypeScript: `npm test -- --bail`

## Anti-Hallucination & Verification Checklist
- Always verify file paths exist before importing or modifying.
- When generating diffs, preserve all existing docstrings, copyright headers, and formatting comments.
- Do not invent non-existent CLI flags or API options.
```

---

## 4. Cursor Rules (`.cursorrules` or `.cursor/rules/*.mdc`)

Save as `.cursorrules` in the project root or `.cursor/rules/general.mdc`:

```markdown
# Cursor Rules: Engineering Standards

You are an expert software engineer and system architect. Adhere to these rules strictly:

### 1. Code Quality & Modularity
- Write production-ready, typed code (TypeScript `strict`, Python type hints `mypy --strict`, Rust memory safety).
- Avoid monolithic files. Functions should not exceed 50 lines. Files should not exceed 300 lines.
- Follow the Single Responsibility Principle (SRP).

### 2. Multi-File Edits & Refactoring
- When making cross-file changes, preserve backwards compatibility unless explicitly instructed otherwise.
- Never delete existing comments, TODOs, or docstrings unless they directly conflict with new code.
- Prefer explicit imports over wildcard imports.

### 3. Anti-Hallucination Gate
- Never invent API endpoints, package versions, or SDK methods.
- If unsure of a library method signature, inspect local packages or ask the developer.
- Run tests or linter commands immediately following any edit.
```

---

## 5. Model Context Protocol (`mcp.json`) Starter Stack

Add to `~/.config/Claude/claude_desktop_config.json` or project `.mcp.json`:

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "<YOUR_GITHUB_TOKEN>"
      }
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "."]
    },
    "context7": {
      "command": "npx",
      "args": ["-y", "@context7/mcp-server"]
    },
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres", "postgresql://localhost:5432/mydb"]
    },
    "playwright": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-playwright"]
    }
  }
}
```
