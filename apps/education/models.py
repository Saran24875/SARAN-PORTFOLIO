from django.db import models

class Education(models.Model):
    degree = models.CharField(max_length=100, help_text="Enter your degree, e.g. Bachelor of Science, Master of Arts, etc.")
    institution = models.CharField(max_length=150, help_text="Enter the name of the institution where you obtained your degree")
    graduation_date = models.DateField(help_text="Enter the date when you finished your degree")

    def __str__(self):
        return f"{self.degree} at {self.institution}"
