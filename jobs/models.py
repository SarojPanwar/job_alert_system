from django.db import models

# Create your models here.
class Job(models.Model):
    company = models.ForeignKey('companies.Company', on_delete=models.CASCADE,related_name='jobs')
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    experience = models.CharField(max_length=50,blank=True, default="")
    employment_type = models.CharField(max_length=20,blank=True, default="")
    work_mode = models.CharField(max_length=20,blank=True, default="")
    apply_url = models.URLField()
    department = models.CharField(
        max_length=255,
        blank=True,
        default=""
    )
    office = models.CharField(
        max_length=255,
        blank=True,
        default=""
    )   
    job_hash = models.CharField(
        max_length=64, 
        unique=True
        )
    posted_date = models.DateTimeField(null=True, blank=True)
    description = models.TextField(blank=True)
    skills = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    scraped_at = models.DateTimeField(auto_now=True)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-scraped_at']
        indexes = [
            models.Index(
                fields=['company','is_active']
            ),
        ]

    def __str__(self):
        return f"{self.title} at {self.company.name}"
    

