from django.db import models
from django.core.exceptions import ValidationError


def validate_service_fields(instance):
    """
    Validates the Service model fields:
    - Ensures that either `Select_Service` or `Others` is provided, but not both.
    - If `Others` is provided, `Othericon` is required.
    - If `description` is provided, `Other_description` must also be provided (and vice versa).
    """
    errors = []

    # Ensure only one of the two fields is filled.
 # Ensure only one of `Select_Service` or `Others` is filled
    if instance.Select_Service and instance.Others:
        errors.append("Please provide either 'Select_Service' or 'Others', not both.")
    
    if instance.Select_Service and instance.Othericon:
        errors.append("If 'Select_Service' is provided, then 'Othericon' must not be provided. Please provide Icon.")
    
    if instance.Select_Service and instance.Other_description:
        errors.append("If 'Select_Service' is provided, then 'Other_description' must not be provided. Please provide Description.")

    # Ensure at least one of `Select_Service` or `Others` is provided
    if not instance.Select_Service and not instance.Others:
        errors.append("Please provide one of 'Select_Service' or 'Others'.")

    # If `Others` is provided, then `Othericon` and `Other_description` must also be provided
    if instance.Others:
        if not instance.Othericon:
            errors.append("If 'Others' is provided, then 'Othericon' must also be provided.")
        if not instance.Other_description:
            errors.append("If 'Others' is provided, then 'Other_description' must also be provided.")
        if instance.description:
            errors.append("If 'Others' is provided, then 'description' must not be provided.")

    # Ensure mutual dependency between `description` and `Other_description`
    if instance.description and instance.Other_description:
        errors.append("If 'description' is provided, then 'Other_description' must also be provided.")


    # Raise ValidationError if any issues exist
    if errors:
        raise ValidationError(errors)


class Service(models.Model):
    DEVELOPER_DOMAINS = [
        ('Web Development', 'Web Development'),
        ('Frontend Development', 'Frontend Development'),
        ('Backend Development', 'Backend Development'),
        ('Full Stack Development', 'Full Stack Development'),
        ('App Development', 'App Development'),
        ('Android Development', 'Android Development'),
        ('iOS Development', 'iOS Development'),
        ('Cross-Platform Development', 'Cross-Platform Development'),
        ('Software Development', 'Software Development'),
        ('Desktop Application Development', 'Desktop Application Development'),
        ('Enterprise Software Development', 'Enterprise Software Development'),
        ('Embedded Systems Development', 'Embedded Systems Development'),
        ('Game Development', 'Game Development'),
        ('AR/VR Development', 'AR/VR Development'),
        ('Data Science & AI Development', 'Data Science & AI Development'),
        ('Machine Learning Development', 'Machine Learning Development'),
        ('AI Development', 'AI Development'),
        ('Data Analytics & Visualization', 'Data Analytics & Visualization'),
        ('Big Data Development', 'Big Data Development'),
        ('Blockchain Development', 'Blockchain Development'),
        ('Smart Contract Development', 'Smart Contract Development'),
        ('DApps Development', 'DApps Development'),
        ('NFT & Crypto Development', 'NFT & Crypto Development'),
        ('Cloud & DevOps', 'Cloud & DevOps'),
        ('Cloud Development', 'Cloud Development'),
        ('DevOps & CI/CD', 'DevOps & CI/CD'),
        ('Serverless Development', 'Serverless Development'),
        ('Cybersecurity & Ethical Hacking', 'Cybersecurity & Ethical Hacking'),
        ('Penetration Testing', 'Penetration Testing'),
        ('Secure Software Development', 'Secure Software Development'),
        ('Blockchain Security', 'Blockchain Security'),
        ('IoT Development', 'IoT Development'),
        ('Embedded IoT Solutions', 'Embedded IoT Solutions'),
        ('Edge Computing', 'Edge Computing'),
        ('Smart Home & Automation', 'Smart Home & Automation'),
        ('Database Development', 'Database Development'),
        ('SQL Database Development', 'SQL Database Development'),
        ('NoSQL Database Development', 'NoSQL Database Development'),
        ('Database Optimization & Management', 'Database Optimization & Management'),
        ('API & Integration Development', 'API & Integration Development'),
        ('RESTful API Development', 'RESTful API Development'),
        ('GraphQL Development', 'GraphQL Development'),
        ('Third-Party API Integration', 'Third-Party API Integration'),
        ('Robotics & Automation', 'Robotics & Automation'),
        ('Robotic Process Automation (RPA)', 'Robotic Process Automation (RPA)'),
        ('AI-Powered Automation', 'AI-Powered Automation'),
    ]

    ICON_MAPPING = {
        'Web Development': 'fas fa-globe',
        'Frontend Development': 'fas fa-paint-brush',
        'Backend Development': 'fas fa-server',
        'Full Stack Development': 'fas fa-laptop-code',
        'App Development': 'fas fa-mobile-alt',
        'Android Development': 'fab fa-android',
        'iOS Development': 'fab fa-apple',
        'Cross-Platform Development': 'fas fa-code-branch',
        'Software Development': 'fas fa-laptop',
        'Desktop Application Development': 'fas fa-desktop',
        'Enterprise Software Development': 'fas fa-building',
        'Embedded Systems Development': 'fas fa-microchip',
        'Game Development': 'fas fa-gamepad',
        'AR/VR Development': 'fas fa-vr-cardboard',
        'Data Science & AI Development': 'fas fa-brain',
        'Machine Learning Development': 'fas fa-robot',
        'AI Development': 'fas fa-lightbulb',
        'Data Analytics & Visualization': 'fas fa-chart-line',
        'Big Data Development': 'fas fa-database',
        'Blockchain Development': 'fab fa-bitcoin',
        'Smart Contract Development': 'fas fa-file-signature',
        'DApps Development': 'fas fa-network-wired',
        'NFT & Crypto Development': 'fas fa-coins',
        'Cloud & DevOps': 'fas fa-cloud',
        'Cloud Development': 'fas fa-cloud-upload-alt',
        'DevOps & CI/CD': 'fas fa-tools',
        'Serverless Development': 'fas fa-server',
        'Cybersecurity & Ethical Hacking': 'fas fa-user-secret',
        'Penetration Testing': 'fas fa-bug',
        'Secure Software Development': 'fas fa-lock',
        'Blockchain Security': 'fas fa-shield-alt',
        'IoT Development': 'fas fa-microchip',
        'Embedded IoT Solutions': 'fas fa-wifi',
        'Edge Computing': 'fas fa-project-diagram',
        'Smart Home & Automation': 'fas fa-home',
        'Database Development': 'fas fa-database',
        'SQL Database Development': 'fas fa-table',
        'NoSQL Database Development': 'fas fa-database',
        'Database Optimization & Management': 'fas fa-cogs',
        'API & Integration Development': 'fas fa-link',
        'RESTful API Development': 'fas fa-cloud',
        'GraphQL Development': 'fas fa-graphql',
        'Third-Party API Integration': 'fas fa-plug',
        'Robotics & Automation': 'fas fa-robot',
        'Robotic Process Automation (RPA)': 'fas fa-cogs',
        'AI-Powered Automation': 'fas fa-microchip',
    }

    Select_Service = models.CharField(max_length=100, choices=DEVELOPER_DOMAINS, null=True, blank=True, help_text="Select a service from the list or leave it blank for others.")
    Others = models.CharField(max_length=100, blank=True, help_text="Enter a custom service name if not selecting from the list.")
    description = models.TextField(blank=True, help_text="Provide a description for the selected service or custom entry.")
    Other_description = models.TextField(blank=True, help_text="Provide a description for the 'Others' entry if applicable.")
    Othericon = models.CharField(max_length=100, blank=True, help_text="Enter an icon for the 'Others' entry, if applicable.")

    def clean(self):
        """Runs the custom field validation logic."""
        super().clean()
        validate_service_fields(self)  # Custom validation

    def save(self, *args, **kwargs):
        """Validates before saving."""
        self.clean()  
        super().save(*args, **kwargs)

    @property
    def icon(self):
        """Returns the corresponding icon for the selected service."""
        return self.ICON_MAPPING.get(self.Select_Service, '')  # Default icon if not found

    def __str__(self):
        return self.Select_Service if self.Select_Service else self.Others or "Unnamed Service"
