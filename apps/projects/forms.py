from django import forms
from .models import ProjectMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ProjectMessage
        fields = ['name', 'email', 'message']
