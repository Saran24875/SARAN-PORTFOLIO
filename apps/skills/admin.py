from django.contrib import admin
from django.utils.html import format_html
from .models import (
    ProgrammingLanguage,
    Framework,
    Tools,
    Database,
    SoftSkills,
    
)

@admin.register(ProgrammingLanguage)
class ProgrammingLanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'icon_display')
    
    def icon_display(self, obj):
        return format_html('<i class="{}"></i>', obj.icon)
    icon_display.short_description = "Icon"


@admin.register(Framework)
class FrameworkAdmin(admin.ModelAdmin):
    list_display = ('select_framework', 'level', 'icon_display')
    
    def icon_display(self, obj):
        return format_html('<i class="{}"></i>', obj.icon)
    icon_display.short_description = "Icon"


@admin.register(Tools)
class ToolsAdmin(admin.ModelAdmin):
    list_display = ('select_tools', 'level', 'icon_display')
    
    def icon_display(self, obj):
        return format_html('<i class="{}"></i>', obj.icon)
    icon_display.short_description = "Icon"


@admin.register(Database)
class DatabaseAdmin(admin.ModelAdmin):
    list_display = ('select_database', 'level', 'icon_display')
    
    def icon_display(self, obj):
        return format_html('<i class="{}"></i>', obj.icon)
    icon_display.short_description = "Icon"


@admin.register(SoftSkills)
class SoftSkillsAdmin(admin.ModelAdmin):
    list_display = ('select_soft_skills', 'level', 'icon_display')
    
    def icon_display(self, obj):
        return format_html('<i class="{}"></i>', obj.icon)
    icon_display.short_description = "Icon"


