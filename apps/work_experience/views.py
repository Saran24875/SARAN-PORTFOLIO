from django.shortcuts import render
from .models import WorkExperience

def work_experience_page(request):
    experiences = WorkExperience.objects.all()
    return render(request, 'work_experience.html', {'experiences': experiences})
