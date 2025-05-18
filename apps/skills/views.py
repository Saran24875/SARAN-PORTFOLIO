from django.shortcuts import render
from .models import ProgrammingLanguage, Framework, Tools, Database, SoftSkills
from branding.models import PersonalBranding


def home(request):
    context = {
        'programming_languages': ProgrammingLanguage.objects.all(),
        'frameworks': Framework.objects.all(),
        'tools': Tools.objects.all(),
        'databases': Database.objects.all(),
        'soft_skills': SoftSkills.objects.all(),  # lower-case key
        'branding': PersonalBranding.objects.first(),
    }
    return render(request, 'home.html', context)
