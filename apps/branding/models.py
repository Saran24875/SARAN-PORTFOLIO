from django.db import models
from PIL import Image
from rembg import remove
from io import BytesIO
from django.core.files.base import ContentFile
from collections import Counter
import colorsys
from colorfield.fields import ColorField
from cloudinary_storage.storage import MediaCloudinaryStorage
from cloudinary_storage.storage import RawMediaCloudinaryStorage
import cloudinary.uploader






class PersonalBranding(models.Model):
    name = models.CharField(max_length=100,help_text="Enter your name")
    tagline = models.CharField(max_length=150,help_text="Enter your tagline. Comma separated for multiple taglines.(eg. Frontend Developer, Backend Developer)")
    about = models.TextField(help_text="Enter your about. This will be displayed on the about Section.",null=True,blank=True)
    bio = models.TextField(help_text="Enter your bio. This will be displayed on the about Section on the contact page.")
    profile_picture = models.ImageField(upload_to='branding/profile_pictures/',storage=MediaCloudinaryStorage(),help_text="Upload your profile picture For the lite Mode and If you want to remove the background from your profile picture, please check the 'Remove Background' checkbox.")
    remove_bg = models.BooleanField(default=False,help_text="If you want to remove the background from your profile picture, please check this checkbox.")  # Checkbox for background removal
    profile_picture_for_mobile = models.ImageField(upload_to='branding/profile_picture_for_mobile/',storage=MediaCloudinaryStorage(),null=True,blank=False,help_text="Upload your profile picture For the lite Mode and If you want to remove the background from your profile picture, please check the 'Remove Background' checkbox.")
    Dark_mode_profile_picture = models.ImageField(upload_to='branding/background_images/',storage=MediaCloudinaryStorage(),help_text="Upload your dark mode profile picture For the dark mode. This will be displayed in dark mode.")
    resume = models.FileField(upload_to='branding/resumes/',storage=RawMediaCloudinaryStorage(), blank=False, null=True, help_text="Upload your resume in the format of .pdf or .docx" )
    og_image = models.ImageField(upload_to='branding/og_image/',storage=MediaCloudinaryStorage(),help_text= "Upload your Open Graph image. This will be used when sharing your website on social media.",null=True,blank=True)
    this_site_url = models.URLField(max_length=200,help_text="Enter the URL of your website. This will be used for Open Graph and Twitter Card meta tags.",null=True,blank=True)
    # def save(self, *args, **kwargs):
    #     # Only upload if resume is a new local file (not a URL already)
    #     if self.resume and not str(self.resume).startswith("http"):
    #         # Upload to Cloudinary as a raw file (for .pdf, .docx, etc.)
    #         upload_result = cloudinary.uploader.upload(
    #             self.resume,
    #             resource_type="raw",           # ✅ CRUCIAL
    #             folder="documents",            # optional, keeps files organized
    #             use_filename=True,
    #             unique_filename=False
    #         )
    #         # Store the public URL in the database
    #         self.resume.name = upload_result['secure_url']
    #     super().save(*args, **kwargs)
    
    # @property
    # def resume_url(self):
    #     return self.resume.name  # ✅ This is now your Cloudinary URL
    
    def upload_document(file):
        upload_result = cloudinary.uploader.upload(
            file,
            resource_type='raw',
            folder='documents/'
        )
        return upload_result['secure_url']

    favicon_ico = models.ImageField(upload_to='branding/favicon_ico/',storage=MediaCloudinaryStorage(),blank=True,null=True,help_text="Upload your favicon in .ico format. This will be displayed in the browser tab.")
    favicon_svg= models.ImageField(upload_to='branding/favicon_svg/',storage=MediaCloudinaryStorage(),blank=True,null=True,help_text="Upload your favicon in .svg format. This will be displayed in the browser tab.")
    favicon_96x96= models.ImageField(upload_to='branding/favicon-96x96/',storage=MediaCloudinaryStorage(),blank=True,null=True,help_text="Upload your favicon in 96x96 .png format. This will be displayed in the browser tab.")
    apple_touch_icon= models.ImageField(upload_to='branding/apple_touch_icon/',storage=MediaCloudinaryStorage(), blank=True, null=True,help_text="Upload your Apple Touch icon in .png format. This will be used for Apple devices.")
    site_webmanifest= models.ImageField(upload_to='branding/site_webmanifest/',storage=MediaCloudinaryStorage(),blank=True,null=True,help_text="Upload your site webmanifest in .webmanifest format. This defines app metadata for browsers.")
    short_name = models.CharField(max_length=100,help_text="Enter your short name for the share cards on the social media.",null=True,blank=True)
    
    Primary_color = ColorField(default='none',help_text="Enter or select your primary color. This will the background color of your website.")  
    text_color = ColorField(default='none',help_text="Enter or select your text color. This will be the color of the text in your website.") 
    button_color = ColorField(default='none') 
    button_text_color = ColorField(default='none',help_text="Enter or select your button text color. This will be the color of the text in the buttons in your website.")  
    hover_color = ColorField(default='none',help_text="Enter or select your hover color. This will be the color of the buttons and the links when hovered by the cursor in your website.")  
    h2_color = ColorField(default='none',help_text="Enter or select your hover color. This will be the color of the headings on the each sections in your website.")  
    card_h2_color = ColorField(default='none',help_text="Enter or select your hover color. This will be the color of the headings on the each sections in your website.")  
    
    #the following fields are not shown in the admin panel because they are not used in the site color if you want to use them you can add them in the admin.py on the speicied field(apps/branding/admin.py)
    secondary_color = ColorField(default='none',help_text="Enter or select your secondary color. This will be the secondary color of your website.")
    background_color = ColorField(default='none',help_text="Enter or select your background color. This will be the background color of your website.")
    
    dark_Primary_color = ColorField(default='none',help_text="Enter or select your dark mode primary color. This will be the background color of your website in dark mode.")  
    dark_text_color = ColorField(default='none',help_text="Enter or select your dark mode text color. This will be the color of the text in your website in dark mode.") 
    dark_button_color = ColorField(default='none',help_text="Enter or select your dark mode button color. This will be the color of the buttons in your website in dark mode.") 
    dark_button_text_color = ColorField(default='none',help_text="Enter or select your dark mode button text color. This will be the color of the text in the buttons in your website in dark mode.")  
    dark_hover_color = ColorField(default='none',help_text="Enter or select your dark mode hover color. This will be the color of the buttons and the links when hovered by the cursor in your website in dark mode.")  
    dark_h2_color = ColorField(default='none',help_text="Enter or select your hover color. This will be the color of the headings on the each sections in your website.")
    dark_card_h2_color = ColorField(default='none',help_text="Enter or select your hover color. This will be the color of the headings on the each sections in your website.")
    #the following fields are not shown in the admin panel because they are not used in the site color if you want to use them you can add them in the admin.py on the speicied field(apps/branding/admin.py)
    dark_secondary_color = ColorField(default='none',help_text="Enter or select your dark mode secondary color. This will be the secondary color of your website in dark mode.")
    dark_background_color = ColorField(default='none',help_text="Enter or select your dark mode background color. This will be the background color of your website in dark mode.")
    def save(self, *args, **kwargs):
        """ Override save method to process image and generate color palette """
        if self.remove_bg and self.profile_picture:
            self.remove_background_high_quality()

        else:
            self.css_variables = ""  # Reset CSS variables if unchecked

        super().save(*args, **kwargs)

    def remove_background_high_quality(self):
        """ Remove background from profile picture using rembg """
        img = Image.open(self.profile_picture )
        img = img.convert("RGBA")

        # Remove background using rembg
        no_bg_img = remove(img)

        # Resize to maintain quality
        no_bg_img = no_bg_img.resize(img.size, Image.LANCZOS)

        # Save the processed image in memory
        buffer = BytesIO()
        no_bg_img.save(buffer, format="PNG", quality=100)

        # Save back to model field
        self.profile_picture.save(self.profile_picture.name, ContentFile(buffer.getvalue()), save=False)

    def generate_color_palette(self):
        """ Extracts dominant colors from profile picture and generates CSS variables """
        img = Image.open(self.profile_picture)
        img = img.convert("RGB")
        img = img.resize((100, 100))  # Resize for faster processing

        # Extract colors
        pixels = list(img.getdata())
        color_counts = Counter(pixels)

        # Get the most common colors
        most_common_colors = color_counts.most_common(12)  # Extract top 12 colors

        # Convert RGB to HEX
        def rgb_to_hex(rgb):
            return "#{:02x}{:02x}{:02x}".format(*rgb)

        # Sort colors based on brightness (HSL model)
        sorted_colors = sorted(
            most_common_colors,
            key=lambda c: colorsys.rgb_to_hls(*[x / 255 for x in c[0]])[1],  # Sort by lightness
            reverse=True
        )

        # Assign color roles
        primary_color = rgb_to_hex(sorted_colors[0][0]) if len(sorted_colors) > 0 else "#000000"
        secondary_color = rgb_to_hex(sorted_colors[1][0]) if len(sorted_colors) > 1 else "#333333"
        accent_color = rgb_to_hex(sorted_colors[2][0]) if len(sorted_colors) > 2 else "#666666"
        background_color = rgb_to_hex(sorted_colors[-1][0]) if len(sorted_colors) > 3 else "#ffffff"
        text_color = rgb_to_hex(sorted_colors[3][0]) if len(sorted_colors) > 4 else "#222222"
        hover_color = rgb_to_hex(sorted_colors[4][0]) if len(sorted_colors) > 5 else "#ff5733"
        button_color = rgb_to_hex(sorted_colors[5][0]) if len(sorted_colors) > 6 else "#007bff"
        border_color = rgb_to_hex(sorted_colors[6][0]) if len(sorted_colors) > 7 else "#cccccc"

        # Generate CSS variables
        self.css_variables = f"""
        :root {{
            --primary-color: {primary_color};
            --secondary-color: {secondary_color};
            --accent-color: {accent_color};
            --background-color: {background_color};
            --text-color: {text_color};
            --hover-color: {hover_color};
            --button-color: {button_color};
            --border-color: {border_color};
        }}
        """

    def __str__(self):
        return self.name
