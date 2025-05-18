from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .models import Project, ProjectMessage
from .forms import ContactForm
import google.generativeai as genai
import requests
from branding.models import PersonalBranding  # Import Branding Model

failed_zerobounce_keys = set()
failed_keys = set()

def validate_email_with_zerobounce(email):
    """Validate email existence using multiple ZeroBounce API keys"""
    global failed_zerobounce_keys

    available_keys = [key for key in settings.ZEROBOUNCE_API_KEYS if key not in failed_zerobounce_keys]

    if not available_keys:
        print("⚠️ No working ZeroBounce API keys available. Skipping validation.")
        return True  # Assume valid if no API keys work

    for api_key in available_keys:
        url = f"https://api.zerobounce.net/v2/validate?api_key={api_key}&email={email}"
        try:
            response = requests.get(url)
            data = response.json()
            
            if response.status_code == 404 or response.status_code != 200:
                failed_zerobounce_keys.add(api_key)
                continue

            if data.get("status") == "valid":
                return True
            return False
        except requests.exceptions.RequestException:
            failed_zerobounce_keys.add(api_key)
            continue
        except ValueError:
            failed_zerobounce_keys.add(api_key)
            continue

    return True

def get_ai_response(user_message):
    """Generate AI-based responses using multiple Gemini API keys"""
    global failed_keys

    available_keys = [key for key in settings.GEMINI_API_KEYS if key not in failed_keys]
    if not available_keys:
        return "I'm currently unable to generate a response. Please try again later."

    for api_key in available_keys:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel("gemini-2.0-flash")
            full_message = f"You are an AI assistant. Generate a professional response:\n\n{user_message}"
            response = model.generate_content(full_message)
            return response.text if response else "I'm unable to generate a response right now."
        except Exception:
            failed_keys.add(api_key)
            continue
    return "AI response is temporarily unavailable. Please try again later."

class PortfolioView(ListView):
    model = Project
    template_name = "projects.html"
    context_object_name = "projects"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["branding"] = PersonalBranding.objects.first()  # Get branding details
        return context

class ProjectDetailView(DetailView):
    model = Project
    template_name = "project_detail.html"
    context_object_name = "project"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_form"] = ContactForm()
        context["branding"] = PersonalBranding.objects.first()  # Get branding details
        return context

def contact_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            if not validate_email_with_zerobounce(contact.email):
                messages.error(request, "Invalid email address. Please enter a valid email.")
                return redirect("projects:project_detail", pk=project.id)
            
            contact.project = project
            # contact.save()
            
            ai_response = get_ai_response(contact.message)
            
            project_message = ProjectMessage.objects.create(
                project=project,
                name=contact.name,
                email=contact.email,
                message=contact.message,
                Ai_response=ai_response  # Store AI response
            )

            # Send email notification to admin
            subject = f"You received a message about your project: {project.name}"
            message = (f"Name: {contact.name}\n"
                       f"Email: {contact.email}\n\n"
                       f"Message:\n{contact.message}\n\n"
                       f"AI Response:\n{ai_response}")
            admin_email = contact.email if contact and contact.email else settings.EMAIL_HOST_USER

            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [admin_email])
            
            # Send AI response to the client
            send_mail("Your Inquiry About " + project.name,
                      ai_response,
                      settings.DEFAULT_FROM_EMAIL,
                      [contact.email])

            messages.success(request, "Your message has been sent successfully!")
            return redirect("projects:project_detail", pk=project.id)

    messages.error(request, "There was an error submitting the form.")
    return redirect("projects:project_detail", pk=project.id,)


