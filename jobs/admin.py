from django.contrib import admin
from .models import Job
# Register your models here.
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "company",
        "location",
        "experience",
        "employment_type",
        "work_mode",
        "is_active",
        "scraped_at",
    )
    list_filter = (
        "company",
        "location",
        "employment_type",
        "work_mode",
        "is_active",
        "posted_date",
    )
    search_fields = (
        "title",
        "company__name",
    )
    ordering = (
        "-scraped_at",
    )
    readonly_fields = (
        "job_hash",
        "scraped_at",
    )
    list_per_page = 25
    date_hierarchy = "scraped_at"


