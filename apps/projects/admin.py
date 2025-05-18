from django.contrib import admin
from .models import Project, ProjectMessage


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Project Information', {
            'fields': ['name', 'one_line_about_the_project', 'brief_about_the_project']
        }),
        ('Technologies Used', {
            'fields': [
                'technologies_used_1', 'level_in_1',
                'technologies_used_2', 'level_in_2',
                'technologies_used_3', 'level_in_3',
            ]
        }),
        ('Project Links', {
            'fields': ['live_demo_url', 'github_repo_url']
        }),
        ('Challenges Faced', {
            'fields': ['challenges_faced_with_the_project']
        }),
        ('Project Images', {
            'fields': [
                'Card_image', 
                'Project_image_1', 'Project_image_2', 
                'Project_image_3', 'Project_image_4', 'Project_image_5'
            ]
        }),
    ]

    list_display = ('name', 'one_line_about_the_project', 'live_demo_url', 'github_repo_url')


# class ProjectMessage_ContactAdmin(admin.ModelAdmin):
#     readonly_fields = ('name', 'email', 'message', 'Ai_Response', 'Recived_at')  # Make fields read-only
    
#     def has_add_permission(self, request):
#         return False  # Prevent adding new records from the admin panel

#     # def has_change_permission(self, request, obj=None):
#     #     return False  # Prevent editing existing records

#     # def has_delete_permission(self, request, obj=None):
#     #     return False  # Prevent deleting records

#     list_display = ('name', 'email', 'project', 'Recived_at')
#     readonly_fields = ('Recived_at',)  # Prevent editing the timestamp
# admin.site.register(ProjectMessage, ProjectMessage_ContactAdmin)

class ProjectMessageAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj and obj.Reply:  # If a reply exists, make it read-only
            return ('project', 'name', 'email', 'message', 'Ai_response', 'Reply', 'Recived_at')
        return ('project', 'name', 'email', 'message', 'Ai_response', 'Recived_at')
    
    def has_add_permission(self, request):
        return False  # Prevent adding new records from the admin panel
    
    list_display = ('name', 'email', 'project', 'Recived_at')

admin.site.register(ProjectMessage, ProjectMessageAdmin)