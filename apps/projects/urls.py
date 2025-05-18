from django.urls import path
from .views import PortfolioView, ProjectDetailView,contact_project

app_name = "projects"  # This must be here!

urlpatterns = [
    path("", PortfolioView.as_view(), name="projects"),  # This name must match!
    path("<int:pk>/", ProjectDetailView.as_view(), name="project_detail"),
    path("<int:project_id>/contact/", contact_project, name="contact_project"),

]
