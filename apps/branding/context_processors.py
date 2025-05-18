from .models import PersonalBranding  # Change 'branding_app' to your actual app name

def branding_context(request):
    branding = PersonalBranding.objects.first()
    return {'branding': branding}
