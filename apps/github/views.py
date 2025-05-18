from django.shortcuts import render
from .utils import fetch_github_repos

def github_repos_page(request):
    github_username = "your_github_username"  # Replace with your GitHub username
    repositories = fetch_github_repos(github_username)
    return render(request, 'github/github_repos_page.html', {'repositories': repositories})
