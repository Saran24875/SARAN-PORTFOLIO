from django.urls import path
from .views import services_page

urlpatterns = [
    path('', services_page, name='services'),
    
]
