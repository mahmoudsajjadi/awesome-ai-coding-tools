# Awesome AI Coding Tools [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> A curated collection of state-of-the-art AI coding assistants, terminal agents, autonomous software engineers, local code LLMs, and automated testing tools designed to accelerate modern software engineering.

---

## 📑 Contents

- [Agentic IDEs & Editors](#-agentic-ides--editors)
- [Terminal & CLI Coding Agents](#-terminal--cli-coding-agents)
- [Open-Source Copilots & Extensions](#-open-source-copilots--extensions)
- [Autonomous Software Engineers](#-autonomous-software-engineers)
- [Local & Open-Weight Coding Models](#-local--open-weight-coding-models)
- [Automated Code Review & Security](#-automated-code-review--security)
- [Automated Testing & QA](#-automated-testing--qa)
- [Architecture & Documentation Generators](#-architecture--documentation-generators)
- [Feature Comparison Matrix](#-feature-comparison-matrix)
- [Contributing](#-contributing)

---

## 💻 Agentic IDEs & Editors

Full-featured development environments built natively around agentic pair programming and multi-file code editing.

- [Cursor](https://www.cursor.com/) — AI-native fork of VS Code featuring instant codebase indexing, multi-file edits (Composer), and automated terminal command execution.
- [Windsurf](https://codeium.com/windsurf) — Next-generation agentic IDE by Codeium featuring "Flows" that track real-time developer context and multi-step plans.
- [Zed](https://zed.dev/) — High-performance, GPU-accelerated code editor written in Rust with deep model integration and assistant panels.
- [PearAI](https://trypear.ai/) — Open-source alternative to Cursor built on VS Code with customizable model backends.

---

## ⚡ Terminal & CLI Coding Agents

Command-line power tools that pair program directly inside your git repositories.

- [Aider](https://github.com/paul-gauthier/aider) — Command-line AI pair programmer that writes code across your repo and automatically commits git diffs with descriptive messages.
- [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview) — Agentic CLI tool capable of navigating large codebases, running bash commands, and managing complex multi-file refactors.
- [Cline](https://github.com/cline/cline) — Autonomous coding agent extension for VS Code that creates files, executes terminal commands, and checks browser previews.
- [Mentat](https://github.com/AbanteAI/mentat) — Open-source AI tool capable of coordinating complex git workflows directly in the terminal.

---

## 🔌 Open-Source Copilots & Extensions

Pluggable extensions compatible with standard editors (VS Code, Neovim, JetBrains) allowing custom model backends.

- [Continue.dev](https://github.com/continuedev/continue) — The leading open-source AI code assistant for VS Code and JetBrains; supports local models (Ollama, LM Studio) and cloud APIs.
- [Avante.nvim](https://github.com/yetone/avante.nvim) — Neovim plugin designed to emulate Cursor AI's multi-file editing capabilities natively in Lua.
- [Codeium](https://codeium.com/) — Free AI code completion and chat extension for 40+ IDEs with enterprise self-hosting options.
- [Tabby](https://github.com/TabbyML/tabby) — Self-hosted AI coding assistant server; an open-source alternative to GitHub Copilot.

---

## 🤖 Autonomous Software Engineers

Full-loop autonomous agents that triage GitHub issues, implement features, and run verification test suites independently.

- [OpenHands (formerly OpenDevin)](https://github.com/All-Hands-AI/OpenHands) — Autonomous AI software development agent capable of writing code, browsing the web, and running docker containers.
- [SWE-agent](https://github.com/princeton-nlp/SWE-agent) — Open-source agent developed by Princeton that resolves real GitHub issues on the SWE-bench benchmark.
- [Devika](https://github.com/stitionai/devika) — Agentic open-source software engineer capable of breaking down user goals into multi-stage tasks.

---

## 🧠 Local & Open-Weight Coding Models

Top-tier open weights you can run locally or deploy on private infrastructure to keep proprietary code completely private.

- [Qwen2.5-Coder](https://github.com/QwenLM/Qwen2.5-Coder) — Leading open-source coding foundation model series (0.5B to 32B) competitive with GPT-4o in code generation and refactoring.
- [DeepSeek-Coder-V2](https://github.com/deepseek-ai/DeepSeek-Coder-V2) — Mixture-of-Experts code language model with 128k context length supporting 338 programming languages.
- [StarCoder 2](https://github.com/bigcode-project/starcoder2) — Open, transparently trained code models (3B, 7B, 15B) curated by BigCode under permissive licenses.
- [Codestral](https://mistral.ai/news/codestral/) — Mistral AI’s open-weight model specialized in code completion and fill-in-the-middle tasks with an 80-language vocabulary.

---

## 🛡️ Automated Code Review & Security

Review bots that inspect pull requests, catch subtle concurrency bugs, and enforce architectural guidelines.

- [CodeRabbit](https://coderabbit.ai/) — AI-driven pull request reviewer providing line-by-line feedback, sequence diagrams, and security vulnerability checks.
- [Qodo (CodiumAI)](https://www.qodo.ai/) — Comprehensive code integrity platform analyzing PRs, writing regression tests, and enforcing code standards.
- [Semgrep Assistant](https://semgrep.dev/) — Combines deterministic static analysis (AST rules) with LLM explanations to eliminate false-positive security findings.

---

## 🧪 Automated Testing & QA

Tools that automatically write edge cases, integration tests, and unit tests to push test coverage up to 90%+.

- [Cover-Agent](https://github.com/Codium-ai/cover-agent) — Open-source generative testing tool that iteratively generates unit tests until target coverage is met.
- [Keploy](https://github.com/keploy/keploy) — Open-source zero-code test generator that captures real network calls and creates automated regression test suites.
- [Mutmut](https://github.com/boxed/mutmut) — Python mutation testing system that tests the resilience of your test suites against simulated faults.

---

## 📐 Architecture & Documentation Generators

Keep system design documents, API specifications, and architecture diagrams in sync with codebases.

- [Mintlify](https://mintlify.com/) — Beautiful, automated documentation generator that reads codebases and outputs developer docs.
- [Swimm](https://swimm.io/) — Code-coupled documentation platform that uses AI to automatically update developer walkthroughs when code changes.
- [Eraser.io / DiagramGPT](https://www.eraser.io/) — Turns plain code or markdown architecture descriptions into clean flowcharts and cloud infrastructure diagrams.

---

## ⚖️ Feature Comparison Matrix

| Tool / Project | Interface | Multi-File Editing | Open Source? | Local Models (Ollama)? |
| :--- | :--- | :---: | :---: | :---: |
| **Cursor** | Standalone IDE | ✅ (Composer) | ❌ | Partial |
| **Aider** | CLI / Terminal | ✅ (Repo Map) | ✅ | ✅ |
| **Cline** | VS Code Extension | ✅ | ✅ | ✅ |
| **Continue.dev** | VS Code / JetBrains | ✅ | ✅ | ✅ |
| **OpenHands** | Web UI / Docker | ✅ | ✅ | ✅ |
| **Claude Code** | Terminal CLI | ✅ | ❌ | ❌ |
| **Qwen2.5-Coder** | Model Weights | N/A | ✅ | ✅ |

---

## 🤝 Contributing

We welcome community contributions! Please review [CONTRIBUTING.md](CONTRIBUTING.md) to propose additions or modifications.

---

## 📄 License

This repository is distributed under the [MIT License](LICENSE).
