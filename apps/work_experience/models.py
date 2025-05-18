from django.db import models

class WorkExperience(models.Model):
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    responsibilities = models.TextField()
    achievements = models.TextField(blank=True)

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"
