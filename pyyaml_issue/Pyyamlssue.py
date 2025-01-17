import requests
from tqdm import tqdm
import time
import json

from urllib3 import Retry

retry_strategy = Retry(total=3)
adapter = requests.adapters.HTTPAdapter(max_retries=retry_strategy)
session = requests.Session()
session.mount("https://", adapter)


def get_issues_open(owner, repo, headers, per_page=100, max_pages=10):
    all_issues = []
    for page in tqdm(range(1, max_pages + 1), desc="Fetching commits"):
        url = f"https://api.github.com/repos/{owner}/{repo}/issues?per_page={per_page}&page={page}"
        try:
            response = session.get(url, headers=headers)
            response.raise_for_status()

            if response.status_code!= 200:
                print(f"Non-200 status code {response.status_code} for {owner}/{repo} on page {page}")
                continue

            issues = response.json()
            if not issues:
                break

            all_issues.extend(issues)

            remaining = int(response.headers.get('X-RateLimit-Remaining', -1))
            if remaining <= 10:
                reset_time = int(response.headers.get('X-RateLimit-Reset', time.time()))
                wait_time = reset_time - time.time()
                print(f"Rate limit approaching. Waiting for {wait_time:.0f} seconds...")
                time.sleep(wait_time)

            time.sleep(0.5)

        except requests.exceptions.RequestException as e:
            if isinstance(e, requests.exceptions.ConnectionError):
                print(f"Connection error fetching commits for {owner}/{repo} on page {page}: {e}")
            elif isinstance(e, requests.exceptions.Timeout):
                print(f"Timeout error fetching commits for {owner}/{repo} on page {page}: {e}")
            else:
                print(f"Failed to fetch commits for {owner}/{repo} on page {page}: {e}")
            continue
        except json.JSONDecodeError as e:
            print(f"Failed to decode JSON for {owner}/{repo} on page {page}: {e}")
            print(f"Response content: {response.text[:100]}...")
            continue

    return all_issues

def get_issues_closed(owner, repo, headers, per_page=100, max_pages=10):
    all_issues = []
    for page in tqdm(range(1, max_pages + 1), desc="Fetching commits"):
        url = f"https://api.github.com/repos/{owner}/{repo}/issues?state=closed&per_page={per_page}&page={page}"
        try:
            response = session.get(url, headers=headers)
            response.raise_for_status()

            if response.status_code!= 200:
                print(f"Non-200 status code {response.status_code} for {owner}/{repo} on page {page}")
                continue

            issues = response.json()
            if not issues:
                break

            all_issues.extend(issues)

            remaining = int(response.headers.get('X-RateLimit-Remaining', -1))
            if remaining <= 10:
                reset_time = int(response.headers.get('X-RateLimit-Reset', time.time()))
                wait_time = reset_time - time.time()
                print(f"Rate limit approaching. Waiting for {wait_time:.0f} seconds...")
                time.sleep(wait_time)

            time.sleep(0.5)

        except requests.exceptions.RequestException as e:
            if isinstance(e, requests.exceptions.ConnectionError):
                print(f"Connection error fetching commits for {owner}/{repo} on page {page}: {e}")
            elif isinstance(e, requests.exceptions.Timeout):
                print(f"Timeout error fetching commits for {owner}/{repo} on page {page}: {e}")
            else:
                print(f"Failed to fetch commits for {owner}/{repo} on page {page}: {e}")
            continue
        except json.JSONDecodeError as e:
            print(f"Failed to decode JSON for {owner}/{repo} on page {page}: {e}")
            print(f"Response content: {response.text[:100]}...")
            continue

    return all_issues



owner = "yaml"
repo = "pyyaml"
headers = {
    'Authorization': 'token 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',
    'Accept': 'application/vnd.github.v3+json'
}

issues = get_issues_open(owner, repo, headers)
closed = get_issues_closed(owner, repo, headers)

data_to_write = ""
for issue in issues:
    title = issue['title']
    username = issue['user']['login']
    usertype = issue['user']['type']
    state = issue['state']

    data = f"Issue title: {title}\nusername: {username}\nusertype: {usertype}\nstate: {state}\n-------------------------------------------\n"
    data_to_write += data

for issue in closed:
    title = issue['title']
    username = issue['user']['login']
    usertype = issue['user']['type']
    state = issue['state']

    data = f"Issue title: {title}\nusername: {username}\nusertype: {usertype}\nstate: {state}\n-------------------------------------------\n"
    data_to_write += data

with open('PyyamlIssue.txt', 'w', encoding='utf-8') as f:
    f.write(data_to_write)
