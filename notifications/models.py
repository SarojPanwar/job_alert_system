from django.db import models
from django.conf import settings
from jobs.models import Job
# Create your models here.

class Notification(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notifications"
    )

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name="notifications"

    )
   
    message = models.TextField()

    is_read = models.BooleanField(default=False)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}-{self.job.title}"
    
