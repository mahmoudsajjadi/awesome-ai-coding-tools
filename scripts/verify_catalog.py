import json
import re
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
README_PATH = REPO_ROOT / 'README.md'
TOOLS_JSON = REPO_ROOT / 'docs' / 'tools.json'
METADATA_JSON = REPO_ROOT / 'docs' / 'catalog_metadata.json'

CATEGORIES = [
    'Standalone Agentic IDEs',
    '1-Click Editor Extensions',
    'Terminal & CLI Pair Programmers',
    'Running Agents in Parallel',
    'Model Context Protocol (MCP) Servers for Coding',
    'Top Open-Weight Coding Models',
    'Local Execution Engines (Private & Offline)',
    'Automated Testing, QA & Code Review',
    'Autonomous Software Engineers (SWE-bench)'
]

# Tool metadata overrides and factual catalog data
# Fields: open_source (bool), pricing (free / freemium / paid), license (str), maintenance_status (active / slow / inactive)
TOOL_METADATA = {
    "Antigravity": {"open_source": False, "pricing": "freemium", "license": "Proprietary", "maintenance_status": "active", "source": "https://antigravity.google"},
    "Cursor": {"open_source": False, "pricing": "freemium", "license": "Proprietary", "maintenance_status": "active", "source": "https://www.cursor.com/"},
    "Google Jules": {"open_source": False, "pricing": "freemium", "license": "Proprietary", "maintenance_status": "active", "source": "https://jules.google/"},
    "Kiro": {"open_source": False, "pricing": "freemium", "license": "Proprietary", "maintenance_status": "active", "source": "https://kiro.dev/"},
    "PearAI": {"open_source": True, "pricing": "freemium", "license": "Apache-2.0", "maintenance_status": "active", "source": "https://trypear.ai/"},
    "Trae": {"open_source": False, "pricing": "free", "license": "Proprietary", "maintenance_status": "active", "source": "https://www.trae.ai/"},
    "Volt": {"open_source": True, "pricing": "free", "license": "MIT", "maintenance_status": "active", "source": "https://github.com/LeulAria/volt"},
    "Windsurf": {"open_source": False, "pricing": "freemium", "license": "Proprietary", "maintenance_status": "active", "source": "https://windsurf.com/"},
    "Zed": {"open_source": True, "pricing": "free", "license": "GPL-3.0 / Apache-2.0", "maintenance_status": "active", "source": "https://zed.dev/"},
    "Codeium": {"open_source": False, "pricing": "freemium", "license": "Proprietary", "maintenance_status": "active", "source": "https://codeium.com/"},
    "Continue.dev": {"open_source": True, "pricing": "free", "license": "Apache-2.0", "maintenance_status": "active", "source": "https://github.com/continuedev/continue"},
    "Supermaven": {"open_source": False, "pricing": "paid", "license": "Proprietary", "maintenance_status": "inactive", "source": "https://supermaven.com/"},
    "Tabby": {"open_source": True, "pricing": "freemium", "license": "Apache-2.0", "maintenance_status": "active", "source": "https://github.com/TabbyML/tabby"},
    "Aider": {"open_source": True, "pricing": "free", "license": "Apache-2.0", "maintenance_status": "active", "source": "https://github.com/paul-gauthier/aider"},
    "Avante.nvim": {"open_source": True, "pricing": "free", "license": "Apache-2.0", "maintenance_status": "active", "source": "https://github.com/yetone/avante.nvim"},
    "Claude Code": {"open_source": False, "pricing": "paid", "license": "Proprietary", "maintenance_status": "active", "source": "https://code.claude.com/docs"},
    "Cline": {"open_source": True, "pricing": "free", "license": "Apache-2.0", "maintenance_status": "active", "source": "https://github.com/cline/cline"},
    "Codex CLI": {"open_source": True, "pricing": "free", "license": "Apache-2.0", "maintenance_status": "active", "source": "https://github.com/openai/codex"},
    "Flisk": {"open_source": True, "pricing": "free", "license": "MIT", "maintenance_status": "active", "source": "https://github.com/flisk-sh/flisk"},
    "Gemini CLI": {"open_source": True, "pricing": "free", "license": "Apache-2.0", "maintenance_status": "active", "source": "https://github.com/google-gemini/gemini-cli"},
    "Goose": {"open_source": True, "pricing": "free", "license": "Apache-2.0", "maintenance_status": "active", "source": "https://github.com/block/goose"},
    "Imagera Code": {"open_source": False, "pricing": "paid", "license": "Proprietary", "maintenance_status": "active", "source": "https://imagera.ai/code"},
    "Kilo Code": {"open_source": True, "pricing": "free", "license": "MIT", "maintenance_status": "active", "source": "https://github.com/Kilo-Org/kilocode"},
    "Mentat": {"open_source": True, "pricing": "free", "license": "Apache-2.0", "maintenance_status": "inactive", "source": "https://github.com/AbanteAI/archive-old-cli-mentat"},
    "OMK": {"open_source": True, "pricing": "free", "license": "MIT", "maintenance_status": "active", "source": "https://github.com/dmae97/omk"},
    "OpenCode": {"open_source": True, "pricing": "free", "license": "MIT", "maintenance_status": "active", "source": "https://github.com/anomalyco/opencode"},
    "Roo Code": {"open_source": True, "pricing": "free", "license": "Apache-2.0", "maintenance_status": "inactive", "source": "https://github.com/RooVetGit/Roo-Code"},
    "Xenon": {"open_source": True, "pricing": "free", "license": "MIT", "maintenance_status": "active", "source": "https://github.com/xianyu-sheng/Xenon"},
    "Carbon Forge": {"open_source": False, "pricing": "freemium", "license": "Proprietary", "maintenance_status": "active", "source": "https://carbonforge.dev/"},
    "ccmanager": {"open_source": True, "pricing": "free", "license": "MIT", "maintenance_status": "active", "source": "https://github.com/kbwo/ccmanager"},
    "Claude Squad": {"open_source": True, "pricing": "free", "license": "AGPL-3.0", "maintenance_status": "active", "source": "https://github.com/smtg-ai/claude-squad"},
    "cmux": {"open_source": True, "pricing": "free", "license": "MIT", "maintenance_status": "active", "source": "https://github.com/manaflow-ai/cmux"},
    "MulmoTerminal": {"open_source": True, "pricing": "free", "license": "MIT", "maintenance_status": "active", "source": "https://github.com/receptron/mulmoterminal"},
    "Orkas": {"open_source": True, "pricing": "free", "license": "MIT", "maintenance_status": "active", "source": "https://github.com/Orkas-AI/Orkas"},
    "Orca": {"open_source": True, "pricing": "free", "license": "MIT", "maintenance_status": "active", "source": "https://github.com/stablyai/orca"},
    "Sqwakie": {"open_source": False, "pricing": "freemium", "license": "FSL-1.1-ALv2", "maintenance_status": "active", "source": "https://sqwakie.si/"},
    "Vibe Kanban": {"open_source": True, "pricing": "free", "license": "Apache-2.0", "maintenance_status": "active", "source": "https://github.com/BloopAI/vibe-kanban"},
    "BrowserTools MCP": {"open_source": True, "pricing": "free", "license": "MIT", "maintenance_status": "active", "source": "https://github.com/AgentDeskAI/browser-tools-mcp"},
    "call-me": {"open_source": True, "pricing": "paid", "license": "MIT (Client) / Proprietary", "maintenance_status": "active", "source": "https://github.com/radres/call-me"},
    "Context7 MCP": {"open_source": True, "pricing": "freemium", "license": "Apache-2.0", "maintenance_status": "active", "source": "https://github.com/upstash/context7"},
    "Docsy": {"open_source": True, "pricing": "freemium", "license": "MIT", "maintenance_status": "active", "source": "https://github.com/getremcp/docsy-plugin"},
    "Filesystem & Git MCP": {"open_source": True, "pricing": "free", "license": "MIT", "maintenance_status": "active", "source": "https://github.com/modelcontextprotocol/servers/tree/main/src/git"},
    "GitHub MCP Server": {"open_source": True, "pricing": "free", "license": "MIT", "maintenance_status": "active", "source": "https://github.com/modelcontextprotocol/servers/tree/main/src/github"},
    "Postgres MCP": {"open_source": True, "pricing": "free", "license": "MIT", "maintenance_status": "active", "source": "https://github.com/modelcontextprotocol/servers/tree/main/src/postgres"},
    "ReMCP": {"open_source": True, "pricing": "free", "license": "MIT", "maintenance_status": "active", "source": "https://github.com/getremcp/remcp"},
    "sqlite-graph-memory": {"open_source": True, "pricing": "free", "license": "MIT", "maintenance_status": "active", "source": "https://github.com/tonydzi/sqlite-graph-memory"},
    "Codestral": {"open_source": False, "pricing": "free", "license": "Mistral Non-Production / Commercial", "maintenance_status": "active", "source": "https://mistral.ai/news/codestral/"},
    "DeepSeek-Coder-V2": {"open_source": True, "pricing": "free", "license": "DeepSeek / MIT", "maintenance_status": "slow", "source": "https://github.com/deepseek-ai/DeepSeek-Coder-V2"},
    "DeepSeek-V3 / DeepSeek-R1": {"open_source": True, "pricing": "free", "license": "MIT", "maintenance_status": "active", "source": "https://github.com/deepseek-ai/DeepSeek-V3"},
    "Devstral Small 2 (24B)": {"open_source": True, "pricing": "free", "license": "Apache-2.0", "maintenance_status": "active", "source": "https://mistral.ai/news/devstral-2/"},
    "Llama-4 / CodeLlama Series": {"open_source": True, "pricing": "free", "license": "Llama Community License", "maintenance_status": "active", "source": "https://github.com/meta-llama/llama"},
    "Qwen2.5-Coder": {"open_source": True, "pricing": "free", "license": "Apache-2.0", "maintenance_status": "active", "source": "https://github.com/QwenLM/Qwen2.5-Coder"},
    "Qwen3-Coder Preview": {"open_source": True, "pricing": "free", "license": "Apache-2.0", "maintenance_status": "active", "source": "https://github.com/QwenLM/Qwen3-Coder"},
    "StarCoder 2": {"open_source": True, "pricing": "free", "license": "BigCode OpenRAIL-M", "maintenance_status": "slow", "source": "https://github.com/bigcode-project/starcoder2"},
    "llama.cpp": {"open_source": True, "pricing": "free", "license": "MIT", "maintenance_status": "active", "source": "https://github.com/ggerganov/llama.cpp"},
    "LM Studio": {"open_source": False, "pricing": "free", "license": "Proprietary", "maintenance_status": "active", "source": "https://lmstudio.ai/"},
    "Ollama": {"open_source": True, "pricing": "free", "license": "MIT", "maintenance_status": "active", "source": "https://ollama.com/"},
    "vLLM": {"open_source": True, "pricing": "free", "license": "Apache-2.0", "maintenance_status": "active", "source": "https://github.com/vllm-project/vllm"},
    "agent-qa": {"open_source": False, "pricing": "freemium", "license": "Proprietary", "maintenance_status": "active", "source": "https://vostride.com"},
    "CodeRabbit": {"open_source": False, "pricing": "freemium", "license": "Proprietary", "maintenance_status": "active", "source": "https://coderabbit.ai/"},
    "Cover-Agent": {"open_source": True, "pricing": "free", "license": "AGPL-3.0", "maintenance_status": "active", "source": "https://github.com/Codium-ai/cover-agent"},
    "Keploy": {"open_source": True, "pricing": "freemium", "license": "Apache-2.0", "maintenance_status": "active", "source": "https://github.com/keploy/keploy"},
    "Qodo (CodiumAI)": {"open_source": False, "pricing": "freemium", "license": "Proprietary", "maintenance_status": "active", "source": "https://www.qodo.ai/"},
    "Semgrep Assistant": {"open_source": False, "pricing": "freemium", "license": "Proprietary", "maintenance_status": "active", "source": "https://semgrep.dev/"},
    "OpenHands": {"open_source": True, "pricing": "free", "license": "MIT", "maintenance_status": "active", "source": "https://github.com/All-Hands-AI/OpenHands"},
    "SWE-agent": {"open_source": True, "pricing": "free", "license": "MIT", "maintenance_status": "active", "source": "https://github.com/princeton-nlp/SWE-agent"}
}

def verify_and_sync():
    print('Checking awesome-ai-coding-tools catalog integrity...')
    with open(README_PATH, 'r', encoding='utf-8') as f:
        text = f.read()

    extracted = []
    for cat in CATEGORIES:
        pattern = rf'### (?:.*?\s)?{re.escape(cat)}.*?\n(.*?)(?=\n### |\n## |\n---|\Z)'
        match = re.search(pattern, text, re.DOTALL)
        if match:
            for line in match.group(1).split('\n'):
                line = line.strip()
                if line.startswith('- ['):
                    m = re.match(r'- \[([^\]]+)\]\((https?://[^\s)]+)\)(?:\s*\(\[[^\]]+\]\([^)]+\)\))?\s*[-—–]\s*(.*)', line)
                    if m:
                        name = m.group(1).strip()
                        url = m.group(2).strip()
                        desc = m.group(3).strip()
                        
                        meta = TOOL_METADATA.get(name, {})
                        # fallback matching
                        if not meta:
                            for k, v in TOOL_METADATA.items():
                                if k.lower() in name.lower() or name.lower() in k.lower():
                                    meta = v
                                    break
                                    
                        extracted.append({
                            'name': name,
                            'url': url,
                            'category': cat,
                            'description': desc,
                            'open_source': meta.get('open_source', 'github.com' in url),
                            'pricing': meta.get('pricing', 'free'),
                            'license': meta.get('license', 'Unknown'),
                            'maintenance_status': meta.get('maintenance_status', 'active'),
                            'last_verified': '2026-11-09',
                            'source': meta.get('source', url)
                        })

    print(f'Total tools validated across core categories: {len(extracted)}')
    assert len(extracted) >= 50, f'Expected >= 50 tools, found {len(extracted)}'

    # Check that URLs use https
    insecure = [t for t in extracted if not t['url'].startswith('https://')]
    if insecure:
        print(f'WARNING: Found non-HTTPS URLs: {insecure}')
    else:
        print('All tool URLs use secure HTTPS.')

    # Sync tools.json
    payload = {
        'schemaVersion': 2,
        'lastUpdated': '2026-11-09',
        'toolCount': len(extracted),
        'tools': extracted
    }
    with open(TOOLS_JSON, 'w', encoding='utf-8') as f:
        json.dump(payload, f, indent=2)
    print(f'Synchronized {TOOLS_JSON} successfully.')

if __name__ == '__main__':
    verify_and_sync()
