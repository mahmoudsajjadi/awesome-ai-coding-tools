#!/usr/bin/env python3
"""
Generate the tools catalog sections in README.md from docs/tools.json.
Ensures the README and tools.json never drift and entries remain in alphabetical order.
"""

import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
README_PATH = REPO_ROOT / 'README.md'
TOOLS_JSON = REPO_ROOT / 'docs' / 'tools.json'

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

def load_tools():
    with open(TOOLS_JSON, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data.get('tools', [])

def render_category_tools(category, tools):
    cat_tools = [t for t in tools if t['category'] == category]
    cat_tools.sort(key=lambda x: x['name'].lower())
    
    lines = []
    for t in cat_tools:
        name = t['name']
        url = t['url']
        desc = t['description'].strip()
        lines.append(f"- [{name}]({url}) — {desc}")
    return '\n'.join(lines)

def build_catalog_markdown(tools):
    parts = []
    for cat in CATEGORIES:
        parts.append(f"### {cat}\n")
        parts.append(render_category_tools(cat, tools))
        parts.append("")
    return '\n'.join(parts).strip()

def update_readme():
    tools = load_tools()
    with open(README_PATH, 'r', encoding='utf-8') as f:
        readme_text = f.read()

    # Look for <!-- CATALOG_START --> and <!-- CATALOG_END --> markers
    marker_start = "<!-- CATALOG_START -->"
    marker_end = "<!-- CATALOG_END -->"

    if marker_start in readme_text and marker_end in readme_text:
        catalog_md = build_catalog_markdown(tools)
        pattern = rf"{re.escape(marker_start)}.*?{re.escape(marker_end)}"
        replacement = f"{marker_start}\n\n{catalog_md}\n\n{marker_end}"
        new_readme = re.sub(pattern, replacement, readme_text, flags=re.DOTALL)
        with open(README_PATH, 'w', encoding='utf-8') as f:
            f.write(new_readme)
        print(f"Updated README.md catalog sections from {TOOLS_JSON} ({len(tools)} tools).")
    else:
        print("Markers <!-- CATALOG_START --> and <!-- CATALOG_END --> not found in README.md.")

if __name__ == '__main__':
    update_readme()
