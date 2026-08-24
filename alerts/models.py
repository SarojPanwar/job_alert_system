
from django.db import models
from django.contrib.auth.models import User

class JobAlert(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="job_alerts"
    )

    keywords = models.CharField(
        max_length=255,
        blank=True,
        default=""
    )

    location = models.CharField(
        max_length=255,
        blank=True,
        default=""
    )

    work_mode = models.CharField(
        max_length=50,
        blank=True,
        default=""
    )

    employment_type = models.CharField(
        max_length=50,
        blank=True,
        default=""
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"Alert for {self.user}"
