from django.urls import path
from .views import work_experience_page

urlpatterns = [
    path('work-experience/', work_experience_page, name='work_experience')
]
