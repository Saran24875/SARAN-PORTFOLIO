from django.shortcuts import render
from branding.models import PersonalBranding

from .models import Education

def education_page(request):
    branding = PersonalBranding.objects.first()  # Fetch first branding object
    education_list = Education.objects.all()
    return render(request, 'education.html', {'education': education_list, 'branding': branding})
