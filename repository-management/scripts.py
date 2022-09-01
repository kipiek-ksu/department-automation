import csv
import requests

# Get personal token:
# https://github.com/settings/tokens
# Grant repo, delete_repo, admin:org, project access

# Place token here
# NEWER COMMIT THE TOKEN!!!
TOKEN = ''

HEADERS = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {TOKEN}"
}

ORG_NAME = "kipiek-ksu"

# Details
# https://docs.github.com/en/rest/quickstart
# https://docs.github.com/en/rest/repos/repos


###############################################################################
# # List repos with topics
# org_repos = requests.get(
#     f'https://api.github.com/orgs/{ORG_NAME}/repos',
#     headers=HEADERS
# )
#
# print([(x['name'], x['topics']) for x in org_repos.json()])
# print(org_repos)

###############################################################################
# Create repos from the template
TEMPLATE_OWNER = ORG_NAME
TEMPLATE_REPO = 'term-paper-template'

# repos = []
# with open('to-be-created.csv', 'r') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         repos.append(row)
#         repos[-1]['repo'] = f'term-paper-{repos[-1]["year"]}-{repos[-1]["name"].lower()}-{repos[-1]["surname"].lower()}'
#         repos[-1]['description'] = f'Term paper of {repos[-1]["name"]} {repos[-1]["surname"]} ' \
#                                    f'for {repos[-1]["year"]} year'
#
# for repo in repos:
#     result = requests.post(
#         f'https://api.github.com/repos/{TEMPLATE_OWNER}/{TEMPLATE_REPO}/generate',
#         headers=HEADERS,
#         data=f'''{{
#         "owner":"{ORG_NAME}",
#         "name":"{repo['repo']}",
#         "description":"{repo['description']}",
#         "include_all_branches":false,
#         "private":false}}'''
#     )
#     print(repo['repo'], result.status_code)
#
# print()

###############################################################################
# Delete repos
# ONLY FOR DEV PURPOSES
# for repo in repos:
#     result = requests.delete(
#         f'https://api.github.com/repos/{ORG_NAME}/{repo["repo"]}',
#         headers=HEADERS
#     )
#     print(repo['repo'], result.status_code)
#
# print()
