from django.utils.html import format_html
from django.contrib import admin
from .models import ContactInfo, Client_Message

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('email','ai_details','get_social_media_links')
    
    fieldsets = [
        ('Contact Information', {
            'fields': ['email', 'phone_number'],
            'description': "This is the email address that will be used to send automated emails to customers."
        }),
        ('Social Media Links', {
            'fields': ['facebook', 'facebook_active', 'twitter', 'twitter_active', 'linkedin', 'linkedin_active', 'github', 'github_active', 'instagram', 'instagram_active', 'reddit', 'reddit_active', 'discord', 'discord_active', 'threads', 'threads_active'],
            'description': "This is the social media links that will be displayed on the contact page."
        }),
        ('AI Details', {
            'fields': ['ai_details'],
            'description': "This is the AI details that will be used to generate responses for customer inquiries."
        })
    ]

    def has_add_permission(self, request):
        if ContactInfo.objects.exists():
            return False
        return super().has_add_permission(request)
    
    def get_social_media_links(self, obj):
        icons = obj.get_social_media_icons()
        links = []
        for platform, icon_class in icons.items():
            link = getattr(obj, platform, None)
            active = getattr(obj, f"{platform}_active", False)
            if link and active:
                links.append(
                    format_html(
                        f'<a href="{link}" target="_blank"><i class="{icon_class}"></i> {platform.title()}</a>'
                    )
                )
        return format_html("<br>".join(links))
    get_social_media_links.short_description = "Social Media"
    
    

class ContactAdmin(admin.ModelAdmin):
    # readonly_fields = ('name', 'email', 'message', 'Ai_Response', 'Recived_at')  # Make fields read-only
    
    
    def get_readonly_fields(self, request, obj=None):
        if obj and obj.Reply:
            return('name', 'email', 'message', 'Ai_Response', 'Reply', 'Recived_at')  # Make fields read-only
        return('name', 'email', 'message', 'Ai_Response', 'Recived_at')
    
    def has_add_permission(self, request):
        return False  # Prevent adding new records from the admin panel

    # def has_change_permission(self, request, obj=None):
    #     return False  # Prevent editing existing records

    # def has_delete_permission(self, request, obj=None):
    #     return False  # Prevent deleting records
    list_display = ('name', 'email', 'Recived_at')
admin.site.register(Client_Message, ContactAdmin)


