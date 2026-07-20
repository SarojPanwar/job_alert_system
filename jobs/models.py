from django.db import models

# Create your models here.
class Job(models.Model):
    company = models.ForeignKey('companies.Company', on_delete=models.CASCADE,related_name='jobs')
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    experience = models.CharField(max_length=50)
    employment_type = models.CharField(max_length=20)
    work_mode = models.CharField(max_length=20)
    apply_url = models.URLField()
    job_hash = models.CharField(max_length=64, unique=True)
    posted_date = models.DateTimeField(null=True, blank=True)
    description = models.TextField(blank=True)
    skills = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    scraped_at = models.DateTimeField(auto_now_add=True)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-scraped_at']

    def __str__(self):
        return f"{self.title} at {self.company.name}"
    

