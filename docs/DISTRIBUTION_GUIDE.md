# Legitimate Distribution & Community Discovery Guide

> [!NOTE]
> **Policy on Community Engagement**: We strictly prohibit star-farming, astroturfing, promotional bots, unsolicited mass outreach, and hype-driven marketing. Submissions or technical discussions must strictly provide educational, technical value and adhere 100% to each community's published rules.

This guide compiles **10 high-relevance technical communities, subreddits, and curated lists** with their exact URLs, verbatim posting guidelines, and recommended manual, transparent approaches.

---

## 1. Hacker News (Show HN)

- **URL:** [https://news.ycombinator.com/showhn.html](https://news.ycombinator.com/showhn.html)
- **Primary Audience:** Systems engineers, founders, compiler/AI researchers, open-source developers.
- **Exact Verbatim Rules & Constraints:**
  - *"Show HN is for something you've made that other people can play on or that they can run on their computers."*
  - *"Blog posts, sign-up pages, and fundraisers can't be tried out, so they don't count as a Show HN."*
  - *"Title format: The title should begin with 'Show HN:'. It should be descriptive, not clickbait."*
  - *"No vote-solicitation: Never ask friends, users, or followers to upvote or comment on your submission."*
  - *"Be around to answer questions in the comments."*
- **Recommended Manual Approach:**
  - Submit the interactive web application (`https://mahmoudsajjadi.github.io/awesome-ai-coding-tools/`), not the raw GitHub repo list.
  - Title: `Show HN: AI Coding Stack & VRAM Calculator – 8GB-24GB sizing & taxonomy` (68 chars).
  - First comment: Focus on the technical VRAM formula ($W + KV + \text{Overhead}$), quantization trade-offs across 8GB/16GB/24GB GPUs, and why the taxonomy was built. Provide 100% factual context with zero promotional language.

---

## 2. Reddit: r/LocalLLaMA

- **URL:** [https://www.reddit.com/r/LocalLLaMA/](https://www.reddit.com/r/LocalLLaMA/)
- **Primary Audience:** Open-weight LLM practitioners, hardware builders, quantizers (GGUF/EXL2), inference engine maintainers.
- **Exact Verbatim Rules & Constraints:**
  - *Rule 3: "Submissions must be directly related to locally run LLMs and open-source AI."*
  - *Rule 4: "No raw AI-generated content or low-effort code dumps."*
  - *Rule 5: "Limit self-promotion to roughly 10% of your total community contributions. Affiliation must be disclosed. Sensationalized titles and affiliate links are prohibited."*
- **Recommended Manual Approach:**
  - Submit a text post focusing strictly on local coding LLM execution: benchmarks comparing Qwen 2.5 Coder 7B, 14B, 32B and Devstral Small 2 (24B) on consumer cards (RTX 3060, 4070, 4080, 3090/4090).
  - Explicitly disclose project authorship (`Maintainer disclosure: I maintain the awesome-ai-coding-tools catalog`).
  - No links to paid tools; highlight offline execution via Ollama/llama.cpp/vLLM.

---

## 3. Reddit: r/ClaudeAI

- **URL:** [https://www.reddit.com/r/ClaudeAI/](https://www.reddit.com/r/ClaudeAI/)
- **Primary Audience:** Anthropic Claude users, developers using Claude 3.7 Sonnet, Claude Code CLI, and agent workflows.
- **Exact Verbatim Rules & Constraints:**
  - *Rule 1: "Submissions and discussions must stay relevant to Claude and Claude Code technology, models, and its users."*
  - *Rule 2: "Be constructive. Avoid agitating content or unsupported rants."*
  - *Rule 5: "Posts comparing Claude to competitor AI models must contain sufficient research and evidence, not just questions."*
- **Recommended Manual Approach:**
  - Submit a technical write-up detailing the difference in repo context structures between `CLAUDE.md`, universal `AGENTS.md`, and Cursor `.cursor/rules/*.mdc`.
  - Contrast Claude Code's terminal sub-agent model against editor-integrated Composer models. Provide concrete bash test-loop configurations without hype.

---

## 4. Lobste.rs

- **URL:** [https://lobste.rs](https://lobste.rs)
- **Primary Audience:** Systems programmers, functional programmers, infrastructure engineers, security researchers.
- **Exact Verbatim Rules & Constraints:**
  - *"Lobsters is focused on computing, computer science, programming, and IT topics."*
  - *"Self-promotion rule: Submissions and comments of your own work should be under roughly 25% of your activity."*
  - *"New accounts (under 70 days) cannot submit new or unseen domains."*
  - *"No low-effort code dumps or AI-generated slop; plain repository links without technical write-ups are discouraged."*
- **Recommended Manual Approach:**
  - Do NOT submit a direct link until having an established, invite-backed account with regular discussion participation.
  - If sharing, submit an in-depth technical analysis article (such as the AST PageRank vs. vector search benchmark write-up from `docs/BENCHMARKS.md`) tagged `[ai]` and `[practices]`.

---

## 5. GitHub: sindresorhus/awesome

- **URL:** [https://github.com/sindresorhus/awesome](https://github.com/sindresorhus/awesome)
- **Primary Audience:** Global open-source ecosystem, developers seeking definitive curated lists.
- **Exact Verbatim Rules & Constraints:**
  - *Only lists adhering strictly to `awesome-lint` and `awesome.md` requirements are accepted.*
  - *Must have active maintenance, scannable format, clear categorization, and alphabetical ordering.*
  - *Must have an Awesome badge (`[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)`).*
  - *Table of Contents denylist: Sections named 'Related Lists' are explicitly forbidden by `awesome-lint`.*
- **Recommended Manual Approach:**
  - Ensure the repository passes `awesome-lint` in CI without warnings.
  - Submit a pull request to `sindresorhus/awesome` adding the repository under the "Development / Artificial Intelligence" category once the catalog has accumulated sufficient community verification history.

---

## 6. GitHub: punkpeye/awesome-mcp-servers

- **URL:** [https://github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)
- **Primary Audience:** Developers implementing Anthropic's Model Context Protocol (MCP) clients and servers.
- **Exact Verbatim Rules & Constraints:**
  - *"This specific list is reserved for MCP servers that have a public GitHub repository containing packages you install and run yourself."*
  - *"Remote-only servers belong in separate lists."*
  - *"Direct links, concise descriptions, correct categorization, and strict alphabetical order within each category are mandatory."*
- **Recommended Manual Approach:**
  - Submit individual open-source MCP coding servers surfaced during catalog verification (e.g. `sqlite-graph-memory`, `BrowserTools MCP`) as separate, single-item PRs adhering strictly to alphabetical placement and standard format: `[Name](url) - Description.`

---

## 7. GitHub: PierrunoYT/awesome-ai-dev-tools

- **URL:** [https://github.com/PierrunoYT/awesome-ai-dev-tools](https://github.com/PierrunoYT/awesome-ai-dev-tools)
- **Primary Audience:** Developers tracking AI-assisted engineering tools and extensions.
- **Exact Verbatim Rules & Constraints:**
  - *"The tool must have a clear developer use case (coding assistants, IDE extensions, agent orchestrators)."*
  - *"Alphabetical order must be maintained within each section."*
  - *"Syntax format: `**[Tool Name](url)** - Description.` or `- [Tool Name](url) - Description.`"*
  - *"Neutral descriptions only: avoid marketing fluff or promotional superlatives."*
- **Recommended Manual Approach:**
  - Submit verified open-source coding tools tracked in `docs/tools.json` (such as `Volt` or `Aider`) to relevant subsections via clean 1-item PRs matching their exact formatting rules.

---

## 8. GitHub: e2b-dev/awesome-ai-agents

- **URL:** [https://github.com/e2b-dev/awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents)
- **Primary Audience:** Engineers building and benchmarking autonomous agent runtimes and code execution sandboxes.
- **Exact Verbatim Rules & Constraints:**
  - *"The list is strictly curated for AI assistants and autonomous agents."*
  - *"Frameworks and SDKs belong in awesome-sdks-for-ai-agents, not this list."*
  - *"Alphabetical order is required. Contributors must sign the E2B CLA (`cla-bot check`)."*
- **Recommended Manual Approach:**
  - Submit SWE-bench autonomous coding agents verified in our catalog (such as `OpenHands` or `SWE-agent`) or suggest a cross-reference PR if they maintain a related resources index. Sign CLA promptly.

---

## 9. Reddit: r/commandline

- **URL:** [https://www.reddit.com/r/commandline/](https://www.reddit.com/r/commandline/)
- **Primary Audience:** Terminal power users, shell scripting enthusiasts, CLI/TUI developers.
- **Exact Verbatim Rules & Constraints:**
  - *Rule 2: "Content must focus on Command Line Interfaces (CLIs) or Terminal User Interfaces (TUIs). No GUI-only tools."*
  - *Rule 4: "Post text or titles generated with AI are strictly prohibited. AI code must be disclosed."*
  - *Rule 5: "No brand new projects (under 30 days old). Projects must be unique."*
  - *Rule 7: "When sharing your own project or tool, you must list similar/alternative software options and explain how your project differs."*
- **Recommended Manual Approach:**
  - Post a comparative engineering overview comparing pure CLI coding agents (`Aider`, `Claude Code`, `Codex CLI`, `Goose`, `Avante.nvim`).
  - List tradeoffs in git commit atomic diffing, pager integration, and shell sandbox safety. Fully disclose maintainer role.

---

## 10. Reddit: r/webdev (Showoff Saturday)

- **URL:** [https://www.reddit.com/r/webdev/](https://www.reddit.com/r/webdev/)
- **Primary Audience:** Frontend, backend, and full-stack web software engineers.
- **Exact Verbatim Rules & Constraints:**
  - *Rule 3: "Excessive self-promotion is prohibited. Follow the 9:1 Reddit ratio."*
  - *Rule 4: "Commercial promotions and solicitations are strictly banned."*
  - *Rule 5: "Sharing personal projects or requesting feedback is strictly limited to 'Showoff Saturday' with appropriate flair. Think project, not product: focus on the technical stack and how it was built."*
- **Recommended Manual Approach:**
  - Post ONLY on Saturday using the `Showoff Saturday` flair.
  - Focus the text post on the architecture of the static client-side VRAM calculator (vanilla JS, zero framework bundle weight, deterministic KV cache sizing formulas, GitHub Pages deployment).
  - Explicitly emphasize that the tool and catalog are 100% free, open-source (CC0 / MIT), and ad-free.
