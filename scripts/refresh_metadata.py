import os
import re
import json
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
README_PATH = REPO_ROOT / 'README.md'
TOOLS_JSON = REPO_ROOT / 'docs' / 'tools.json'
METADATA_JSON = REPO_ROOT / 'docs' / 'catalog_metadata.json'

GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')

def fetch_github_meta(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'AwesomeAICodingTools-Sync/1.0')
    req.add_header('Accept', 'application/vnd.github.v3+json')
    if GITHUB_TOKEN:
        req.add_header('Authorization', f'Bearer {GITHUB_TOKEN}')
    
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            if response.status == 200:
                data = json.loads(response.read().decode('utf-8'))
                return {
                    'stars': data.get('stargazers_count', 0),
                    'forks': data.get('forks_count', 0),
                    'open_issues': data.get('open_issues_count', 0),
                    'license': data.get('license', {}).get('spdx_id') if data.get('license') else None,
                    'pushed_at': data.get('pushed_at'),
                    'archived': data.get('archived', False),
                    'status': 'archived' if data.get('archived') else 'active'
                }
    except Exception as e:
        print(f"  [warn] GitHub API error for {owner}/{repo}: {e}")
    return None

def check_http_status(url):
    req = urllib.request.Request(url, method='HEAD')
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            return response.status
    except urllib.error.HTTPError as e:
        # Some servers block HEAD requests, retry with GET
        if e.code in (403, 405):
            try:
                get_req = urllib.request.Request(url, method='GET')
                get_req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)')
                with urllib.request.urlopen(get_req, timeout=10) as get_resp:
                    return get_resp.status
            except urllib.error.HTTPError as ge:
                return ge.code
            except Exception:
                return e.code
        return e.code
    except Exception:
        return 0

def main():
    print("Running Automated Tool Metadata Refresher...")
    
    with open(TOOLS_JSON, 'r', encoding='utf-8') as f:
        catalog = json.load(f)
    
    tools = catalog.get('tools', [])
    now_iso = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    
    enriched = []
    active_count = 0
    github_count = 0

    for i, t in enumerate(tools, 1):
        name = t['name']
        url = t['url']
        print(f"[{i}/{len(tools)}] Processing {name} ({url})...")
        
        meta = {
            'name': name,
            'url': url,
            'category': t['category'],
            'description': t['description'],
            'last_verified': now_iso,
            'http_status': 200,
            'is_github': False,
            'stars': None,
            'license': None,
            'status': 'active'
        }
        
        # Check if URL is GitHub
        gh_match = re.match(r'https?://github\.com/([^/]+)/([^/?#]+)', url)
        if gh_match:
            owner, repo_name = gh_match.group(1), gh_match.group(2)
            meta['is_github'] = True
            gh_data = fetch_github_meta(owner, repo_name)
            if gh_data:
                github_count += 1
                meta.update(gh_data)
                meta['http_status'] = 200
            else:
                meta['http_status'] = check_http_status(url)
        else:
            meta['http_status'] = check_http_status(url)
        
        if meta.get('status') == 'active' and (meta['http_status'] in (200, 301, 302, 307, 308)):
            active_count += 1
            
        enriched.append(meta)

    output = {
        'schemaVersion': 1,
        'generatedAt': now_iso,
        'totalTools': len(enriched),
        'activeTools': active_count,
        'githubRepos': github_count,
        'tools': enriched
    }

    with open(METADATA_JSON, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2)

    print(f"\nMetadata refresh complete! Wrote {len(enriched)} enriched tools to {METADATA_JSON}")

if __name__ == '__main__':
    main()
