# Frequently Asked Questions (FAQ)

Frequently asked technical questions regarding AI coding tools, local LLM execution, agent architectures, and workflow best practices.

---

### What is the best AI coding assistant in 2026?
The answer depends on your primary workflow:
- **In-Editor & Autocomplete:** [Cursor](https://www.cursor.com/) and [Windsurf](https://windsurf.com/) lead developer adoption for unified multi-file edits (Composer/Cascade) and zero-friction VS Code ergonomics.
- **Terminal CLI & Git Workflows:** [Claude Code](https://code.claude.com/docs) and [Aider](https://github.com/paul-gauthier/aider) achieve the highest verified task completion rates for deep codebase refactors, bash tool use, and automated git commits.
- **Open-Source & Privacy:** [Continue.dev](https://github.com/continuedev/continue) (in VS Code/JetBrains) paired with [Ollama](https://ollama.com/) or [vLLM](https://github.com/vllm-project/vllm).

---

### What is the best local coding LLM for 8GB, 16GB, and 24GB VRAM?
- **8 GB VRAM:** [Qwen 2.5 Coder 7B](https://github.com/QwenLM/Qwen2.5-Coder) (Q4_K_M) provides low latency and strong single-file code completion.
- **12 GB VRAM:** [Qwen 2.5 Coder 14B](https://github.com/QwenLM/Qwen2.5-Coder) (Q4_K_M) balances speed and multi-file reasoning.
- **16 GB VRAM:** [Devstral Small 2 (24B)](https://mistral.ai/news/devstral-2/) (Q4_K_M) offers an extended 256k context window for repository comprehension.
- **24 GB VRAM:** [Qwen3-Coder 30B MoE](https://github.com/QwenLM/Qwen3-Coder) or [Qwen 2.5 Coder 32B](https://github.com/QwenLM/Qwen2.5-Coder) deliver near-frontier performance entirely offline.

See [docs/HARDWARE_GUIDE.md](HARDWARE_GUIDE.md) for full hardware matrices and setup recipes.

---

### What is the difference between AGENTS.md, CLAUDE.md, and .cursor/rules?
- **`AGENTS.md`:** Universal open standard supported across Claude Code, Cursor, Codex CLI, Aider, and Windsurf for root project architecture and essential test commands.
- **`CLAUDE.md`:** Tool-specific instructions for Anthropic's Claude Code CLI managing tool permissions and test loops.
- **`.cursor/rules/*.mdc` / `.cursorrules`:** Scoped instructions loaded dynamically inside Cursor IDE based on file glob patterns.

See [docs/AGENT_CONTEXT_TEMPLATES.md](AGENT_CONTEXT_TEMPLATES.md) for ready-to-use templates.

---

### What is the best free alternative to proprietary coding IDEs?
The most reliable 100% free open-source setup combines [Continue.dev](https://github.com/continuedev/continue) or [PearAI](https://trypear.ai/) in your editor, or [Aider](https://github.com/paul-gauthier/aider) in the terminal, connected to local models via [Ollama](https://ollama.com/) (e.g. Qwen 2.5 Coder 14B) or using Gemini CLI's free developer quota (up to 1,000 requests/day).

---

### Which AI coding agent scores highest on SWE-bench Verified?
According to the official [SWE-bench Verified leaderboard](https://www.swebench.com) (500 human-validated GitHub issues; verified 2026-11-09):
- Top closed-source harnesses include Sonar Foundation Agent (79.2% with Claude 4.5 Opus) and live-SWE-agent (79.2% with Claude 4.5 Opus; 77.4% with Gemini 3 Pro).
- Top open-source agents include TRAE (78.8%), mini-SWE-agent (76.8% with Claude 4.5 Opus; 75.8% with Gemini 3 Flash and MiniMax M2.5), and OpenHands (71.8% with GPT-5; 69.6% with Qwen3-Coder-480B-A35B).

See [docs/BENCHMARKS.md](BENCHMARKS.md) for detailed leaderboard rankings and cost metrics.

---

### How can I stop burning API tokens during agentic coding sessions?
1. **Adopt the Architect + Editor pattern:** Use a high-reasoning frontier model (Claude 3.7 / o3) for architectural planning, and route the diff search/replace execution to a low-cost model (DeepSeek-V3 / Qwen) or local model via Ollama.
2. **Keep context instructions lean:** Keep `AGENTS.md` under 50 lines. Avoid pasting entire tree listings or large files into system prompts.
3. **Use headless test validation:** Give agents a fast bail-early test command (`pytest -v --tb=short` or `npm test -- --bail`) so loops exit immediately upon failure.
