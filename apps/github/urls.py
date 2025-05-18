from django.urls import path
from .views import github_repos_page

urlpatterns = [
    path('github/', github_repos_page, name='github_repos_page'),
]
