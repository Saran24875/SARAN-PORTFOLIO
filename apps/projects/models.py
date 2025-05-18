from django.db import models
from django.core.exceptions import ValidationError
from PIL import Image
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.mail import send_mail
from django.conf import settings



def validate_landscape_image(image):
    """Ensures the uploaded image is landscape (width > height)."""
    img = Image.open(image)
    width, height = img.size
    if width <= height:  # Reject if square or portrait
        raise ValidationError("Only landscape images are allowed. Please upload an image where width is greater than height.")


def validate_square_image(image):
    """Ensure the uploaded image is square (width == height)."""
    img = Image.open(image)
    if img.width != img.height:
        raise ValidationError("Only square images are allowed. Please upload an image where width and height are equal.")

class Project(models.Model):
    
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
    (' Game Development', 'Game Development'),
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

    # project_domain=models.CharField(max_length=100,choices=DEVELOPER_DOMAINS,null=True)
    
    name = models.CharField(max_length=100, help_text="Enter the name of the project")

    one_line_about_the_project = models.CharField(
        max_length=200, 
        default="",
        help_text="A concise one-line description of the project to be displayed on the project card."
    )

    brief_about_the_project = models.TextField(
        max_length=1000, 
        default="",
        help_text="A detailed description of the project for display in the project section of the website."
    )

    technologies_used_1 = models.CharField(
        max_length=200, 
        default="",
        help_text="Provied the name of the first technology used (e.g., Django, React, PostgreSQL)."
    )
    level_in_1 = models.IntegerField(
        default=0, 
        validators=[MinValueValidator(35), MaxValueValidator(100)], 
        help_text="Proficiency level of the first technology used (35-100)."
    )
    technologies_used_2 = models.CharField(
        max_length=200, 
        default="",
        help_text="Provided the name of the second technology used (e.g., Django, React, PostgreSQL)."
    )
    level_in_2 = models.IntegerField(
        default=0, 
        validators=[MinValueValidator(35), MaxValueValidator(100)], 
        help_text="Proficiency level of the second technology used (35-100)."
    )

    technologies_used_3 = models.CharField(
        max_length=200, 
        default="",
        help_text="Provided the name of the third technology used (e.g., Django, React, PostgreSQL)."
    )
    level_in_3 = models.IntegerField(
        default=0, 
        validators=[MinValueValidator(35), MaxValueValidator(100)], 
        help_text="Proficiency level of the third technology used (35-100)."
    )
    live_demo_url = models.URLField(blank=True, null=True, help_text="URL for the live demo of the project.If it is blank the button will be hidden.")
    github_repo_url = models.URLField(blank=True, null=True, help_text="URL for the GitHub repository of the project.If it is blank the button will be hidden.")
    
    challenges_faced_with_the_project = models.TextField(
        max_length=1000, 
        default="",
        help_text="Description of challenges encountered during the project development."
    )

    Card_image = models.ImageField(null=True,
        upload_to='projects/images/', 
        
               validators=[validate_landscape_image],
               help_text="this image will be displayed on the project card"# Ensures only square images are uploaded
    )
    
    Project_image_1 = models.ImageField(null=True,
        upload_to='projects/images/', 
        
               validators=[validate_landscape_image]  # Ensures only square images are uploaded
    )
    Project_image_2 = models.ImageField(null=True,
        upload_to='projects/images/', 
        
               validators=[validate_landscape_image]  # Ensures only square images are uploaded
    )
    Project_image_3 = models.ImageField(null=True,
        upload_to='projects/images/', 
        
               validators=[validate_landscape_image]  # Ensures only square images are uploaded
    )
    Project_image_4 = models.ImageField(null=True,
        upload_to='projects/images/', 
        
               validators=[validate_landscape_image]  # Ensures only square images are uploaded
    )
    Project_image_5 = models.ImageField(null=True,
        upload_to='projects/images/', 
        
               validators=[validate_landscape_image]  # Ensures only square images are uploaded
    )
    
    
    
    
    
    
    

    def __str__(self):
        return self.name

class ProjectMessage(models.Model):
    project = models.ForeignKey("Project", on_delete=models.CASCADE)  # Link to the project
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    Ai_response=models.TextField(blank=True, null=True)
    Reply = models.TextField(blank=True, null=True)  # New field for manual reply
    Recived_at = models.DateTimeField(auto_now_add=True)

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