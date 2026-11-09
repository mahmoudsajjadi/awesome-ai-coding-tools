# Awesome AI Coding Tools [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![Link Health](https://github.com/mahmoudsajjadi/awesome-ai-coding-tools/actions/workflows/awesome-bot.yml/badge.svg)](https://github.com/mahmoudsajjadi/awesome-ai-coding-tools/actions/workflows/awesome-bot.yml) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md) [![License: MIT & CC0](https://img.shields.io/badge/License-MIT_%26_CC0-yellow.svg)](LICENSE)

A curated catalog of verified AI coding assistants, autonomous software engineering agents, open-weight foundation models, and Model Context Protocol (MCP) servers. Maintained by [Mahmoud Sajjadi](https://github.com/mahmoudsajjadi).

---

## Contents

- [How to Choose](#how-to-choose)
- [Catalog](#catalog)
  - [Standalone Agentic IDEs](#standalone-agentic-ides)
  - [1-Click Editor Extensions](#1-click-editor-extensions)
  - [Terminal & CLI Pair Programmers](#terminal--cli-pair-programmers)
  - [Running Agents in Parallel](#running-agents-in-parallel)
  - [Model Context Protocol (MCP) Servers for Coding](#model-context-protocol-mcp-servers-for-coding)
  - [Top Open-Weight Coding Models](#top-open-weight-coding-models)
  - [Local Execution Engines (Private & Offline)](#local-execution-engines-private--offline)
  - [Automated Testing, QA & Code Review](#automated-testing-qa--code-review)
  - [Autonomous Software Engineers (SWE-bench)](#autonomous-software-engineers-swe-bench)
- [Documentation & Deep Dives](#documentation--deep-dives)
- [Changelog](#changelog)
- [Contributing](#contributing)

---

## How to Choose

Use these questions to narrow down the right tool for your setup:

1. **Where do you want to code?**
   - *In a dedicated AI editor:* Choose [Cursor](https://www.cursor.com/) (widely adopted VS Code fork) or [Windsurf](https://windsurf.com/) (real-time flow tracking).
   - *Inside your existing VS Code or JetBrains:* Install [Continue.dev](https://github.com/continuedev/continue) (open source) or [Codeium](https://codeium.com/).
   - *Directly in your terminal / CLI:* Use [Claude Code](https://code.claude.com/docs) (Anthropic CLI) or [Aider](https://github.com/paul-gauthier/aider) (git-integrated pairing).

2. **Do you require 100% offline privacy and zero API fees?**
   - Run a local model using [Ollama](https://ollama.com/) or [vLLM](https://github.com/vllm-project/vllm) serving [Qwen2.5-Coder](https://github.com/QwenLM/Qwen2.5-Coder) or [Devstral Small 2 (24B)](https://mistral.ai/news/devstral-2/), paired with [Aider](https://github.com/paul-gauthier/aider) or [Continue.dev](https://github.com/continuedev/continue). See the [Hardware & VRAM Guide](docs/HARDWARE_GUIDE.md).

3. **Do you need multi-agent orchestration or parallel sessions?**
   - Manage multiple worktrees and concurrent agent sessions using [cmux](https://github.com/manaflow-ai/cmux), [Claude Squad](https://github.com/smtg-ai/claude-squad), [MulmoTerminal](https://github.com/receptron/mulmoterminal), or [Vibe Kanban](https://github.com/BloopAI/vibe-kanban).

4. **Do you want automated PR reviews or regression testing in CI?**
   - Integrate [CodeRabbit](https://coderabbit.ai/) for pull-request reviews, [Cover-Agent](https://github.com/Codium-ai/cover-agent) for test coverage generation, or [Keploy](https://github.com/keploy/keploy) for zero-code network regression tests.

5. **Are you researching autonomous software agents?**
   - Benchmark or build on [SWE-agent](https://github.com/princeton-nlp/SWE-agent) and [OpenHands](https://github.com/All-Hands-AI/OpenHands). See empirical leaderboard results in [Benchmarks](docs/BENCHMARKS.md).

---

## Catalog

<!-- CATALOG_START -->

### Standalone Agentic IDEs

- [Antigravity](https://antigravity.google) — Advanced agentic development platform with paired-programming agents, terminal sandboxes, multi-agent collaboration, and artifact canvas rendering.
- [Cursor](https://www.cursor.com/) — The most widely adopted AI-native editor. A fork of VS Code with instant codebase indexing, multi-file edits (Composer), and inline terminal error fixing.
- [Google Jules](https://jules.google/) — Asynchronous GitHub agent that clones repositories in cloud sandboxes, navigates issues, runs test suites, and opens verified pull requests autonomously.
- [Kiro](https://kiro.dev/) — Next-generation agentic IDE featuring real-time collaborative agents and multi-file intent parsing.
- [PearAI](https://trypear.ai/) — Open-source alternative to Cursor built on VS Code with transparent model routing and customizable backends.
- [Trae](https://www.trae.ai/) — Adaptive AI-powered IDE by ByteDance featuring Claude 3.5 Sonnet / GPT-4o integration, workspace-wide context indexing, and agentic code transformation.
- [Volt](https://github.com/LeulAria/volt) — Open-source (MIT) agentic IDE built on the VS Code core that drives Claude Code and Codex agent CLIs over ACP and supports local LLMs via Ollama, with hunk-level review of agent edits and Git checkpoints.
- [Windsurf](https://windsurf.com/) — Agentic IDE by Codeium featuring "Flows" that track real-time developer context and synchronized multi-step edits.
- [Zed](https://zed.dev/) — Lightning-fast, GPU-accelerated code editor written in Rust with deep model integration and multi-model assistant panels.

### 1-Click Editor Extensions

- [Codeium](https://codeium.com/) — Free AI code completion and chat extension for 40+ IDEs with low latency and enterprise self-hosting options.
- [Continue.dev](https://github.com/continuedev/continue) — The leading open-source extension for VS Code and JetBrains; connects to cloud models or local models (Ollama, LM Studio).
- [Supermaven](https://supermaven.com/) — Inline code completion engine featuring Babble architecture (acquired by Cursor; standalone product sunsetted).
- [Tabby](https://github.com/TabbyML/tabby) — Self-hosted AI coding assistant server; an open-source, private alternative to GitHub Copilot.

### Terminal & CLI Pair Programmers

- [Aider](https://github.com/paul-gauthier/aider) — Command-line AI pair programmer that parses your repository into a Tree-sitter map, edits multiple files, runs lint/test commands, and automatically commits atomic git diffs.
- [Avante.nvim](https://github.com/yetone/avante.nvim) — Neovim plugin designed to emulate Cursor AI's multi-file editing capabilities natively in Lua.
- [Claude Code](https://code.claude.com/docs) — Agentic command-line tool capable of autonomous directory indexing, running bash commands, handling git diffs, and orchestrating complex multi-file refactors.
- [Cline](https://github.com/cline/cline) — Autonomous coding agent extension for VS Code that executes terminal commands, inspects local browser previews, and requests human-in-the-loop permission.
- [Codex CLI](https://github.com/openai/codex) — Command-line interface for OpenAI's coding models optimized for fast in-terminal code modifications and script execution.
- [Flisk](https://github.com/flisk-sh/flisk) — Agent-first local environment generator and CLI that automatically configures Docker Compose, Tilt, and Traefik stacks from an empty directory so coding agents can focus on application code.
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) — Google's command-line agent utilizing 1M+ token context windows to ingest entire repositories for refactoring and debugging.
- [Goose](https://github.com/block/goose) — Open-source, extensible AI agent by Block that automates engineering tasks, script execution, and multi-tool workflows directly from the terminal.
- [Imagera Code](https://imagera.ai/code) — Paid terminal coding agent (CLI, built on OpenCode) that reads and edits a project, runs commands and tests, and works headless or through ACP and MCP; one plan covers Claude, GPT, Gemini and other models.
- [Kilo Code](https://github.com/Kilo-Org/kilocode) — Open-source terminal-based developer coding assistant engineered for low latency workflows.
- [Mentat](https://github.com/AbanteAI/archive-old-cli-mentat) — Open-source AI tool capable of coordinating git workflows directly in the terminal (historical CLI archived; team pivoted to MentatBot).
- [OMK](https://github.com/dmae97/omk) — Open-source multi-agent coding CLI for the terminal (TypeScript, MIT). Switch models mid-session; finish goals only when your test passes.
- [OpenCode](https://github.com/anomalyco/opencode) — Provider-agnostic open-source terminal coding agent harness supporting custom agent loops, local model routing, and unified diff execution.
- [Roo Code](https://github.com/RooVetGit/Roo-Code) — Community-driven autonomous coding assistant extension for VS Code (repository archived May 2026).
- [Xenon](https://github.com/xianyu-sheng/Xenon) — CLI coding agent that records every session event in an append-only hash chain verifiable on demand via `/evidence`, enforces deterministic hollow-answer checks, and exports manual verification checklists with multi-model and MCP client support.

### Running Agents in Parallel

- [AgentsMesh](https://github.com/AgentsMesh/AgentsMesh) — Platform for scheduling and isolating multiple coding agents across distributed workstations.
- [Carbon Forge](https://carbonforge.dev/) — Hosted source control (a web service reached over MCP, no local model involved) where each coding agent works in a lane, a set of patches over the trunk, instead of a git worktree. A patch that no longer applies is reported as a named conflict rather than merged automatically, and git history is rendered from the record and pushed to GitHub.
- [ccmanager](https://github.com/kbwo/ccmanager) — Session manager for coordinating parallel CLI agent workflows across multiple repositories.
- [Claude Squad](https://github.com/smtg-ai/claude-squad) — Terminal manager for running multiple concurrent coding agent sessions across terminal tabs.
- [cmux](https://github.com/manaflow-ai/cmux) — Ghostty-based macOS terminal designed with vertical workspaces and desktop notifications for agent fleets.
- [MulmoTerminal](https://github.com/receptron/mulmoterminal) — Browser-based terminal grid running parallel coding agent sessions with dedicated git worktrees per cell, backed by tmux.
- [Orca](https://github.com/stablyai/orca) — Autonomous development environment built to orchestrate and execute a fleet of parallel coding agents.
- [Orkas](https://github.com/Orkas-AI/Orkas) — Local-first desktop AI workforce coordinating specialist agents and external coding CLIs (Claude Code, Codex, OpenCode) with custom model endpoints.
- [Sqwakie](https://sqwakie.si/) — Live dashboard and peer-to-peer CLI/MCP messaging for Claude Code and Codex agents across a team's machines, with project kanbans agents can start, review, and finish. Free for 2 people; FSL-1.1-ALv2 (source-available).
- [Vibe Kanban](https://github.com/BloopAI/vibe-kanban) — Kanban board dashboard to plan, dispatch, monitor, and review tasks across multiple agent CLIs.

### Model Context Protocol (MCP) Servers for Coding

- [BrowserTools MCP](https://github.com/AgentDeskAI/browser-tools-mcp) — Provides agents with headful/headless browser interaction, console error capture, and network inspection capabilities.
- [call-me](https://github.com/radres/call-me) — Hosted remote MCP server (Streamable HTTP, plus mobile companion app) that lets a coding agent ring your phone or text you for human-in-the-loop decisions.
- [Context7 MCP](https://github.com/upstash/context7) — Dynamic context-curation server providing real-time AST symbol definitions and semantic codebase navigation.
- [Docsy](https://github.com/getremcp/docsy-plugin) — Read-only hosted MCP for library/version lookup and source-linked developer docs; requires OAuth account sign-in.
- [Filesystem & Git MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/git) — Official reference MCP server enabling agents to inspect git commits, staging areas, branches, and file structures securely.
- [GitHub MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/github) — Integrates GitHub issues, pull requests, repository searches, and commit reviews directly into agent reasoning loops.
- [Postgres MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres) — Read-only schema inspector and query execution bridge enabling coding agents to validate database migrations and models.
- [ReMCP](https://github.com/getremcp/remcp) — Hosted OAuth MCP for terminal, file, and browser actions on explicitly paired computers; actions may change device state.
- [sqlite-graph-memory](https://github.com/tonydzi/sqlite-graph-memory) — Local stdio MCP server and CLI that lets Claude Code, Cursor or Codex recall from a markdown or Obsidian notes folder, combining vector search with hops along `[[wikilinks]]` in a single SQLite file; embeddings run locally via ONNX. MIT.

### Top Open-Weight Coding Models

- [Codestral](https://mistral.ai/news/codestral/) — Open-weight model specialized in code completion and fill-in-the-middle tasks with an 80-language vocabulary.
- [DeepSeek-Coder-V2](https://github.com/deepseek-ai/DeepSeek-Coder-V2) — Mixture-of-Experts code language model with 128k context length supporting 338 programming languages.
- [DeepSeek-V3 / DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-V3) — 671B Mixture-of-Experts (37B active) and reasoning foundation models matching proprietary models in code generation, multi-file reasoning, and complex refactors.
- [Devstral Small 2 (24B)](https://mistral.ai/news/devstral-2/) — 24B open-weight coding model by Mistral featuring an extended 256k token context window optimized for repo reasoning and local execution.
- [Llama-4 / CodeLlama Series](https://github.com/meta-llama/llama) — Meta's open foundation architectures specialized for code generation, instruction following, and infilling tasks.
- [Qwen2.5-Coder](https://github.com/QwenLM/Qwen2.5-Coder) — Open-source coding foundation model series (0.5B to 32B) for code generation, completion, and multi-file reasoning.
- [Qwen3-Coder Preview](https://github.com/QwenLM/Qwen3-Coder) — Agentic coding model series (including 30B MoE and 480B MoE) pre-trained for tool calling and long-context code understanding.
- [StarCoder 2](https://github.com/bigcode-project/starcoder2) — Open, transparently trained code models (3B, 7B, 15B) curated by BigCode under permissive licenses.

### Local Execution Engines (Private & Offline)

- [llama.cpp](https://github.com/ggerganov/llama.cpp) — High-performance C/C++ inference engine for quantized GGUF models with minimal hardware overhead.
- [LM Studio](https://lmstudio.ai/) — Graphical desktop application for running local GGUF models on Apple Silicon and NVIDIA GPUs.
- [Ollama](https://ollama.com/) — The easiest way to get up and running with local models via a single terminal command (`ollama run qwen2.5-coder`).
- [vLLM](https://github.com/vllm-project/vllm) — High-throughput, memory-efficient LLM serving engine featuring PagedAttention for production local deployments.

### Automated Testing, QA & Code Review

- [agent-qa](https://vostride.com) — CLI and MCP agent for natural-language Web, Android and iOS testing, with persistent memory and validated self-improvement. Supports local models through OpenAI-compatible endpoints.
- [CodeRabbit](https://coderabbit.ai/) — AI-driven pull request reviewer providing line-by-line feedback, sequence diagrams, and security vulnerability checks.
- [Cover-Agent](https://github.com/Codium-ai/cover-agent) — Open-source generative testing tool that iteratively generates unit tests until target coverage is met.
- [Keploy](https://github.com/keploy/keploy) — Open-source zero-code test generator that captures real network calls and creates automated regression test suites.
- [Qodo (CodiumAI)](https://www.qodo.ai/) — Comprehensive code integrity platform analyzing PRs, writing regression tests, and enforcing code standards.
- [Semgrep Assistant](https://semgrep.dev/) — Combines deterministic static analysis (AST rules) with LLM explanations to eliminate false-positive security findings.

### Autonomous Software Engineers (SWE-bench)

- [OpenHands](https://github.com/All-Hands-AI/OpenHands) — Autonomous software development agent capable of writing code, browsing the web, and running dockerized execution sandboxes.
- [SWE-agent](https://github.com/princeton-nlp/SWE-agent) — Open-source agent developed by Princeton that resolves real GitHub issues on the SWE-bench benchmark using an Agent-Computer Interface (ACI).

<!-- CATALOG_END -->

---

## Documentation & Deep Dives

- [💻 Hardware & VRAM Sizing Guide](docs/HARDWARE_GUIDE.md) — GPU specifications, quantization memory tables, and offline recipes.
- [📋 Agent Context Templates](docs/AGENT_CONTEXT_TEMPLATES.md) — Production-ready AGENTS.md, CLAUDE.md, and Cursor rules templates.
- [📊 Benchmarks & Architecture](docs/BENCHMARKS.md) — Official SWE-bench Verified leaderboard, agent architecture, and AST PageRank.
- [❓ Frequently Asked Questions](docs/FAQ.md) — Common questions, cost strategies, and local LLM guidance.
- [📖 Seminal Academic Papers & Citations](docs/RESEARCH_PAPERS.md) — Foundational literature in code LLMs and BibTeX entries.
- [🛡️ Security Best Practices](docs/SECURITY_BEST_PRACTICES.md) — Sandboxed execution and token credential protection.
- [📖 Technical Glossary](docs/GLOSSARY.md) — Definitions for AST, FIM, Repo-Maps, and ACI.
- [💡 Prompting Guide](docs/PROMPT_GUIDE.md) — 3-part prompt formulas for features and debugging.

---

## Changelog

See [docs/CHANGELOG.md](docs/CHANGELOG.md) for recently added and removed tools, schema updates, and catalog revision history.

---

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on suggesting or adding tools. Every entry must have a valid URL, neutral factual description, and clear license/pricing terms.
