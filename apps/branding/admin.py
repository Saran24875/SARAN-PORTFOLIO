from django.contrib import admin
from .models import PersonalBranding

@admin.register(PersonalBranding)
class PersonalBrandingAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Branding Section", {
            "fields": ["name", "tagline","about", "bio", "profile_picture", "profile_picture_for_mobile","remove_bg", "Dark_mode_profile_picture", "resume"],"description":"Update your name, tagline, bio, profile picture, resume and dark mode profile picture."
        }),
        ("Favicon Section", {
            "fields": ["og_image", "this_site_url","favicon_ico", "favicon_svg", "favicon_96x96", "apple_touch_icon", "site_webmanifest"]
            ,"description": "Upload favicon images in different formats for better compatibility.If you want to generate the fav icon for your website, please visit - 'https://realfavicongenerator.net'."
        }),
        ("Lite Mode Theme", {
            "fields": [
                "Primary_color","h2_color" ,"card_h2_color" ,"text_color","button_color", "button_text_color", "hover_color",
            ],"description":"Update your website color palette for the lite mode."
        }),
        ("Dark Mode Theme", {
            "fields": [
                "dark_Primary_color","dark_h2_color" ,"dark_card_h2_color",  "dark_text_color","dark_button_color", "dark_button_text_color", "dark_hover_color",
            ],"description":"Update your website color palette for the dark mode."
        }),
    )

    list_display = ["name", "tagline", "remove_bg"]
    search_fields = ["name", "tagline"]
    list_filter = ["remove_bg"]
    
    def has_add_permission(self, request):
        # Disable add if at least one PersonalBranding object exists
        if PersonalBranding.objects.exists():
            return False
        return super().has_add_permission(request)