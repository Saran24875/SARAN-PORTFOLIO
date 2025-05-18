from django.shortcuts import render
from .models import Service
from branding.models import PersonalBranding

def services_page(request):
    services = Service.objects.all()
    branding = PersonalBranding.objects.first()
    return render(request, 'services.html', {'services': services, 'branding': branding})
