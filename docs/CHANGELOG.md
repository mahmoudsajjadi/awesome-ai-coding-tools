# Changelog: Awesome AI Coding Tools

All notable changes, tool additions, deprecations, and schema updates to the catalog are documented here.

Subscribe to updates via [RSS Feed (feed.xml)](feed.xml).

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [2026-11-09] - Phase 2 & Phase 3 Overhaul

### Added
- **Tools Added:**
  - [Google Jules](https://jules.google/) — Asynchronous GitHub cloud agent for autonomous issue reproduction and PR opening.
  - [Volt](https://github.com/LeulAria/volt) — Open-source agentic IDE built on VS Code driving Claude Code and Codex agents over ACP.
  - [Imagera Code](https://imagera.ai/code) — Multi-model headless and terminal coding agent harness.
  - [OMK](https://github.com/dmae97/omk) — Multi-agent terminal coding CLI supporting mid-session model switching.
  - [Carbon Forge](https://carbonforge.dev/) — Hosted agentic source control with patch lanes over trunk.
  - [ccmanager](https://github.com/kbwo/ccmanager) — Session manager for parallel CLI agents across repositories.
  - [Claude Squad](https://github.com/smtg-ai/claude-squad) — Terminal manager for concurrent coding agent tabs.
  - [cmux](https://github.com/manaflow-ai/cmux) — Ghostty-based terminal for parallel agent fleets.
  - [MulmoTerminal](https://github.com/receptron/mulmoterminal) — Browser-based terminal grid with dedicated worktrees.
  - [Sqwakie](https://sqwakie.si/) — P2P CLI/MCP messaging and kanban coordinator for agent fleets.
  - [call-me](https://github.com/radres/call-me) — Hosted remote MCP server for human-in-the-loop phone/SMS alerts.
  - [Docsy](https://github.com/getremcp/docsy-plugin) — Hosted MCP documentation lookup plugin.
  - [ReMCP](https://github.com/getremcp/remcp) — OAuth MCP server for remote terminal and browser automation.
  - [sqlite-graph-memory](https://github.com/tonydzi/sqlite-graph-memory) — Local stdio MCP memory server combining SQLite and vector search.
  - [Devstral Small 2 (24B)](https://mistral.ai/news/devstral-2/) — 24B open-weight coding model with 256k context window.
  - [Qwen3-Coder Preview](https://github.com/QwenLM/Qwen3-Coder) — 30B & 480B MoE agentic coding foundation models.
  - [agent-qa](https://vostride.com) — CLI and MCP agent for automated testing across Web, Android, and iOS.
- **Documentation Deep Dives Added:**
  - `docs/HARDWARE_GUIDE.md` — Consolidated GPU VRAM sizing matrices, quantization tables, and offline recipes.
  - `docs/AGENT_CONTEXT_TEMPLATES.md` — Consolidated AGENTS.md, CLAUDE.md, and Cursor rules templates.
  - `docs/BENCHMARKS.md` — SWE-bench Verified leaderboard, system architecture diagrams, AST PageRank, and edit representation trade-offs.
  - `docs/FAQ.md` — Common engineering questions and local LLM guidance.
  - `docs/RESEARCH_PAPERS.md` — Curated foundational academic literature and BibTeX entries.
- **Automation:**
  - Python catalog generator (`scripts/generate_readme.py`) keeping README tool entries strictly in sync with `docs/tools.json`.

### Changed
- README streamlined to under 300 lines with scannable one-line tool entries and an objective "How to Choose" decision guide.
- Catalog schema upgraded to schema v2 with verified fields (`last_verified`, `source`, `pricing`, `open_source`, `maintenance_status`).
- Updated SWE-bench Verified leaderboard with verified pass@1 scores from the official leaderboard.

### Deprecated / Marked Inactive
- [Supermaven](https://supermaven.com/) — Standalone product sunsetted following acquisition by Cursor.
- [Mentat](https://github.com/AbanteAI/archive-old-cli-mentat) — Standalone CLI archived.
- [Roo Code](https://github.com/RooVetGit/Roo-Code) — Repository archived.
