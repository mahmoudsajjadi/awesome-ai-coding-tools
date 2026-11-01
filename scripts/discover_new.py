import os
import json
import urllib.request
from datetime import datetime, timezone, timedelta
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DISCOVERIES_JSON = REPO_ROOT / 'docs' / 'discovered_candidates.json'
TOOLS_JSON = REPO_ROOT / 'docs' / 'tools.json'
GH_TOKEN = os.environ.get('GH_TOKEN') or os.environ.get('GITHUB_TOKEN')

SEARCH_QUERIES = [
    'topic:mcp-server stars:>50',
    'topic:coding-agent stars:>30',
    'topic:ai-coding stars:>100'
]

def search_github(query):
    # Search for repositories pushed within the last 30 days
    since = (datetime.now(timezone.utc) - timedelta(days=30)).strftime('%Y-%m-%d')
    q = f"{query} pushed:>{since}"
    url = f"https://api.github.com/search/repositories?q={urllib.parse.quote(q)}&sort=stars&order=desc&per_page=10"
    
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'AwesomeAICodingTools-Discovery/1.0')
    req.add_header('Accept', 'application/vnd.github.v3+json')
    if GH_TOKEN:
        req.add_header('Authorization', f'Bearer {GH_TOKEN}')
    
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            if resp.status == 200:
                return json.loads(resp.read().decode('utf-8')).get('items', [])
    except Exception as e:
        print(f"Error querying GitHub search '{query}': {e}")
    return []

def main():
    import urllib.parse
    print("Searching GitHub for trending AI coding tools & MCP servers...")

    # Load existing tools to avoid duplicates
    existing_urls = set()
    if TOOLS_JSON.exists():
        with open(TOOLS_JSON, 'r', encoding='utf-8') as f:
            tdata = json.load(f)
            for t in tdata.get('tools', []):
                existing_urls.add(t.get('url', '').strip().rstrip('/'))

    candidates = []
    seen_ids = set()

    for q in SEARCH_QUERIES:
        items = search_github(q)
        for it in items:
            repo_id = it.get('id')
            html_url = it.get('html_url', '').rstrip('/')
            
            if repo_id in seen_ids or html_url in existing_urls:
                continue
            
            seen_ids.add(repo_id)
            candidates.append({
                'name': it.get('name'),
                'full_name': it.get('full_name'),
                'url': html_url,
                'stars': it.get('stargazers_count', 0),
                'description': it.get('description') or 'No description provided.',
                'topics': it.get('topics', []),
                'license': it.get('license', {}).get('spdx_id') if it.get('license') else None,
                'pushed_at': it.get('pushed_at'),
                'discovered_at': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
            })

    # Sort by stars
    candidates.sort(key=lambda x: x['stars'], reverse=True)

    output = {
        'generatedAt': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'candidateCount': len(candidates),
        'candidates': candidates[:25] # top 25
    }

    with open(DISCOVERIES_JSON, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2)

    print(f"Discovery complete! Found {len(candidates)} new candidates. Saved top entries to {DISCOVERIES_JSON}")

if __name__ == '__main__':
    main()
