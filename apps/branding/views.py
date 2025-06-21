from django.shortcuts import render
from .models import PersonalBranding
from apps.education.models import Education
from apps.skills.models import ProgrammingLanguage, Framework, Tools, Database, SoftSkills
from apps.services.models import Service
from apps.projects.models import Project, ProjectMessage
from apps.contact.models import ContactInfo, Client_Message
from apps.contact.forms import ContactForm
from  apps.contact.views import contact_page





def index(request):
    contact = ContactInfo.objects.first()

    social_media_links = []
    if contact:
        icons = contact.get_social_media_icons()
        for platform, icon_class in icons.items():
            link = getattr(contact, platform, None)
            active = getattr(contact, f"{platform}_active", False)
            if link and active:
                social_media_links.append({
                    "platform": platform.title(),
                    "url": link,
                    "icon_class": icon_class,
                })
    context = {
        'branding': PersonalBranding.objects.first(),  # Fetch first branding object
        'programming_languages': ProgrammingLanguage.objects.all(),
        'frameworks': Framework.objects.all(),
        'tools': Tools.objects.all(),
        'databases': Database.objects.all(),
        'soft_skills': SoftSkills.objects.all(),  # lower-case key
        'branding': PersonalBranding.objects.first(),
        'services': Service.objects.all(),  # Fetch all services
        'education': Education.objects.all(),  # Fetch all education records
        'projects': Project.objects.all()[:4],  # Fetch all projects
        'project_messages': ProjectMessage.objects.all(),
        'contact': ContactInfo.objects.all(),  # Fetch all project messages
        'footer' : {'github': contact.github if contact and contact.github_active else None,
                    'linkedin': contact.linkedin},
        "social_media_links": social_media_links,
        'form': ContactForm(),  # Initialize the contact form
        'client_messages': Client_Message.objects.all(),  # Fetch all client messages
        'embedded': True 
        
    }    

    return render(request, 'index.html',context)
def base(request):
    branding = PersonalBranding.objects.first()
    return render(request, 'base.html',{'branding': branding})
def contact(request):
    branding = PersonalBranding.objects.first()
    return render(request, 'contact.html',{'branding': branding})
def services(request):
    branding = PersonalBranding.objects.first()
    return render(request, 'services.html',{'branding': branding})
def education(request):
    branding = PersonalBranding.objects.first()
    return render(request, 'education.html',{'branding': branding})
def home(request):
    branding = PersonalBranding.objects.first()
    return render(request, 'home.html',{'branding': branding})
def projects(request):
    branding = PersonalBranding.objects.first()
    return render(request, 'projects.html',{'branding': branding})
def project_detail(request):
    branding = PersonalBranding.objects.first()
    return render(request, 'project_detail.html',{'branding': branding})
def work_experience(request):
    branding = PersonalBranding.objects.first()
    return render(request, 'work_experience.html',{'branding': branding})
def about(request):
    branding = PersonalBranding.objects.first()
    return render(request, 'about.html',{'branding': branding})
    
"""from django.shortcuts import render
from django.http import HttpResponse

def index(request):  
    return HttpResponse("Welcome to the Branding App homepage!")"""

