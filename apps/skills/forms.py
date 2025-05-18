from django import forms
from .models import ProgrammingLanguage, Framework, Tools, Database, SoftSkills

class ProgrammingLanguageForm(forms.ModelForm):
    class Meta:
        model = ProgrammingLanguage
        fields = ['name', 'level']

class FrameworkForm(forms.ModelForm):
    class Meta:
        model = Framework
        fields = ['select_framework', 'level']

class ToolsForm(forms.ModelForm):
    class Meta:
        model = Tools
        fields = ['select_tools', 'level']

class DatabaseForm(forms.ModelForm):
    class Meta:
        model = Database
        fields = ['select_database', 'level']

class SoftSkillsForm(forms.ModelForm):
    class Meta:
        model = SoftSkills
        fields = ['select_soft_skills', 'level']
