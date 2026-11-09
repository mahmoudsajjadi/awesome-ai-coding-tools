# Tool Decision Matrix: Which Tool for Which Job?

A structured, factual evaluation of AI coding tools across deployment archetypes. Use this matrix to match your team's security constraints, hardware budget, and workflow preferences to the appropriate tool class.

---

## 1. Architectural Archetypes

| Archetype | Execution Mechanism | Latency Profile | Primary Strength | Key Trade-off |
| :--- | :--- | :--- | :--- | :--- |
| **Agentic IDE** | Native editor process (Electron/Rust fork) with deep AST indexing | Sub-second inline completions; 2–5s agent turns | Seamless UI integration, inline ghost text, multi-file side-by-side review | Vendor lock-in; closed editor runtime |
| **CLI Agent** | Terminal shell process directly executing git commands, test runners, and shell scripts | Turn-based (5–30s depending on tool loop and model) | Native Git integration, atomic bisectable commits, headless CI execution | Terminal-only interface; requires comfortable CLI familiarity |
| **Async Cloud Agent** | Hosted cloud sandbox running detached from developer workstation | Asynchronous (minutes to hours per issue) | Zero local CPU/GPU resource usage; scales across pull requests | Requires granting full repository access to third-party cloud infrastructure |
| **Local-Only Runtime** | Pure offline inference engine running on consumer or workstation GPU/CPU | Hardware-dependent (10–80 tokens/sec depending on VRAM) | Zero telemetry, zero cloud API fees, 100% air-gap compliance | Requires dedicated VRAM; model intelligence bound by local weight size |

---

## 2. Comprehensive Tool Decision Matrix

The table below contrasts representative tools from each archetype across pricing, licensing, privacy, and local execution capabilities:

| Tool Archetype | Example Tool | Pricing Model | Open Source? | Privacy Posture | Local Model Support? | Best Suited For | Verified Source Link | Last Verified |
| :--- | :--- | :--- | :---: | :--- | :---: | :--- | :--- | :---: |
| **Agentic IDE** | [Cursor](https://www.cursor.com/) | Freemium ($20/mo Pro) | No (Proprietary) | Cloud-routed prompts; Privacy Mode disables retention ([Privacy Policy](https://www.cursor.com/privacy)) | Partial (custom OpenAI endpoint) | Developers seeking full in-editor chat, Composer multi-file diffs, and fast inline editing | [cursor.com](https://www.cursor.com/) | 2026-11-09 |
| **Agentic IDE** | [Windsurf](https://windsurf.com/) | Freemium ($15/mo Pro) | No (Proprietary) | Cloud-routed; zero data retention on paid plans ([Terms](https://windsurf.com/terms)) | No | In-editor workflows needing multi-step context tracking ("Flows") | [windsurf.com](https://windsurf.com/) | 2026-11-09 |
| **Agentic IDE** | [Zed](https://zed.dev/) | Free / Open-core | Yes (GPL-3.0 / Apache-2.0) | Zero telemetry by default; brings your own API keys directly | Yes (Ollama / llama.cpp endpoints) | High-speed Rust-native editing with lightweight assistant integration | [zed.dev](https://zed.dev/) | 2026-11-09 |
| **Agentic IDE** | [PearAI](https://trypear.ai/) | Freemium | Yes (Apache-2.0) | Configurable proxy or direct connection to local/cloud backends | Yes (Ollama / LM Studio) | Developers wanting an open-source Cursor alternative built on VS Code | [trypear.ai](https://trypear.ai/) | 2026-11-09 |
| **CLI Agent** | [Claude Code](https://code.claude.com/docs) | Paid (Anthropic API usage) | No (Proprietary CLI) | Cloud-routed prompts to Anthropic API; subject to Anthropic commercial data terms | No (Anthropic API only) | Autonomous multi-file terminal refactors, shell script execution, and git triage | [code.claude.com](https://code.claude.com/docs) | 2026-11-09 |
| **CLI Agent** | [Aider](https://github.com/paul-gauthier/aider) | Free | Yes (Apache-2.0) | Zero external telemetry; connects directly to configured LLM endpoint | Yes (Ollama, llama.cpp, vLLM, LM Studio) | Terminal-first pair programming with automated git commits and Tree-sitter repo maps | [github.com/paul-gauthier/aider](https://github.com/paul-gauthier/aider) | 2026-11-09 |
| **CLI Agent** | [OpenCode](https://github.com/anomalyco/opencode) | Free | Yes (MIT) | Zero cloud routing; direct model provider or local server communication | Yes (Ollama, local vLLM, OpenAI-compatible) | Modular terminal agent loops, custom diff execution, multi-provider routing | [github.com/anomalyco/opencode](https://github.com/anomalyco/opencode) | 2026-11-09 |
| **CLI Agent** | [Cline](https://github.com/cline/cline) | Free | Yes (Apache-2.0) | Direct API calls to user-configured providers; opt-in telemetry | Yes (Ollama, LM Studio) | Step-by-step terminal and file inspection within VS Code with human authorization gates | [github.com/cline/cline](https://github.com/cline/cline) | 2026-11-09 |
| **Async Cloud Agent** | [Google Jules](https://jules.google/) | Freemium (Preview) | No (Proprietary) | Cloud-hosted sandbox; ingests repository and test outputs within Google Cloud | No (Google backend only) | Detached background issue resolution and autonomous pull request authoring | [jules.google](https://jules.google/) | 2026-11-09 |
| **Async Cloud Agent** | [OpenHands](https://github.com/All-Hands-AI/OpenHands) | Free (Self-hosted) / Freemium (Cloud) | Yes (MIT) | Self-hosted Docker container (zero external data leak if using local weights) | Yes (Ollama, vLLM, or any OpenAI-compatible API) | Benchmark evaluation and containerized autonomous development | [github.com/All-Hands-AI/OpenHands](https://github.com/All-Hands-AI/OpenHands) | 2026-11-09 |
| **Local-Only Runtime** | [Ollama](https://ollama.com/) | Free | Yes (MIT) | 100% offline; zero telemetry or network calls during inference | Yes (GGUF runner for Qwen, Mistral, Llama, etc.) | Standardizing local model serving on macOS, Linux, and Windows with a single binary | [ollama.com](https://ollama.com/) | 2026-11-09 |
| **Local-Only Runtime** | [vLLM](https://github.com/vllm-project/vllm) | Free | Yes (Apache-2.0) | 100% offline; host on self-managed infrastructure | Yes (High-throughput PagedAttention server) | High-throughput local serving for agent fleets and multi-seat development teams | [github.com/vllm-project/vllm](https://github.com/vllm-project/vllm) | 2026-11-09 |

---

## 3. Decision Heuristics: How to Pick

```
Are you legally or policy-restricted from transmitting code to external APIs?
├── YES ──> Choose Local-Only Runtime + Local Agent
│           ├── Minimal Setup: Ollama + Aider (terminal) or PearAI / Continue (IDE)
│           └── High Throughput / Fleet: vLLM + Aider (using Qwen 2.5 Coder 14B or 32B)
└── NO ──> How do you prefer to interact with code?
            ├── Inline / In-Editor Side-by-Side:
            │   ├── Maximum multi-file speed: Cursor or Windsurf
            │   └── Lightweight / Open: Zed or Continue.dev in VS Code
            ├── Terminal / Git-Centric Workflow:
            │   ├── Highest empirical reasoning: Claude Code (Sonnet 3.7)
            │   └── Bring-your-own-key / Open-source: Aider or OpenCode
            └── Asynchronous / Autonomous Background PRs:
                ├── Hosted Managed: Google Jules
                └── Self-hosted / Open Sandbox: OpenHands (Docker)
```
