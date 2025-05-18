from django.urls import path
from .views import education_page

urlpatterns = [
    path('', education_page, name='education'),
]
