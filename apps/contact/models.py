from django.db import models
from .forms import ContactForm  # Import your forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

class ContactInfo(models.Model):
    email = models.EmailField(blank=True, null=True,
        help_text="Enter your preferred email address to receive customer inquiries."
    )
    phone_number = models.CharField(max_length=15, blank=True, null=True,
        help_text="Enter your preferred phone number to receive customer inquiries."
    )
    ai_details = models.TextField(
        default="You are an AI assistant for a website contact form. Please generate a helpful and professional response to the following user inquiry:",
        help_text="Customize the system prompt for the AI assistant. Tell your assistant's name and describe details of you"
    )


    # Social Media Links
    facebook = models.URLField(blank=True, null=True,
        help_text="Enter your Facebook profile URL."
    )
    facebook_active = models.BooleanField(default=False,
        help_text="Check if you want to show your Facebook profile URL."
    )

    instagram = models.URLField(blank=True, null=True,
        help_text="Enter your Instagram profile URL."
    )
    instagram_active = models.BooleanField(default=False,
        help_text="Check if you want to show your Instagram profile URL."
    )

    twitter = models.URLField(blank=True, null=True,
        help_text="Enter your Twitter profile URL."
    )
    twitter_active = models.BooleanField(default=False,
        help_text="Check if you want to show your Twitter profile URL."
    )

    linkedin = models.URLField(blank=True, null=True,
        help_text="Enter your LinkedIn profile URL."
    )
    linkedin_active = models.BooleanField(default=False,
        help_text="Check if you want to show your LinkedIn profile URL."
    )

    reddit = models.URLField(blank=True, null=True,
        help_text="Enter your Reddit profile URL."
    )
    reddit_active = models.BooleanField(default=False,
        help_text="Check if you want to show your Reddit profile URL."
    )

    github = models.URLField(blank=True, null=True,
        help_text="Enter your GitHub profile URL."
    )
    github_active = models.BooleanField(default=False,
        help_text="Check if you want to show your GitHub profile URL."
    )

    discord = models.CharField(max_length=50, blank=True, null=True,
        help_text="Enter your Discord profile URL."
    )
    discord_active = models.BooleanField(default=False,
        help_text="Check if you want to show your Discord profile URL."
    )

    threads = models.URLField(blank=True, null=True,
        help_text="Enter your Threads profile URL."
    )
    threads_active = models.BooleanField(default=False,
        help_text="Check if you want to show your Threads profile URL."
    )

    def __str__(self):
        return self.email

    def get_social_media_icons(self):
        """Map social media platforms to their icons."""
        return {
            "facebook": "fab fa-facebook",
            "instagram": "fab fa-instagram",
            "twitter": "fab fa-twitter",
            "linkedin": "fab fa-linkedin",
            "reddit": "fab fa-reddit",
            "github": "fab fa-github",
            "discord": "fab fa-discord",
            "threads": "fas fa-hashtag",
        }




class Client_Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    Ai_Response = models.TextField(blank=True, null=True)
    Reply = models.TextField(blank=True, null=True)  # New field for manual reply
    Recived_at = models.DateTimeField(auto_now_add=True)  # Track when the message was received

    def __str__(self):
        return f"{self.name} - {self.email}"

    def save(self, *args, **kwargs):
        """Send email if a reply is added."""
        if self.Reply:  # If a reply exists, send an email
            send_mail(
                subject="Your Message Response",
                message=f"Hello {self.name},\n\n{self.Reply}\n\nBest Regards,\nYour Support Team",
                from_email=settings.EMAIL_HOST_USER,  # Use the configured email in settings.py
                recipient_list=[self.email],
                fail_silently=False,
            )
        super().save(*args, **kwargs)  # Call the original save method