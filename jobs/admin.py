from django.contrib import admin
from .models import Job
from django.utils.html import format_html
# Register your models here.
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "company",
        "department",
        "office",
        "location",
        "posted_date",
        "apply_link",
        "experience",
        "employment_type",
        "work_mode",
        "is_active",
        "scraped_at",
    )
    def apply_link(self,obj):
        return format_html(
            '<a href="{}" target="_blank">Apply</a>',
            obj.apply_url
        )
    apply_link.short_description = "Apply URL"
    list_filter = (
        "company",
        "location",
        "title",
        "department",
        "office",
        "employment_type",
        "work_mode",
        "is_active",
        "posted_date",
    )
    search_fields = (
        "title",
        "company__name",
        "location",
        "department",
        "office",
    )
    ordering = (
        "-posted_date",
    )
    readonly_fields = (
        "job_hash",
        "scraped_at",
    )
    list_per_page = 25
    date_hierarchy = "posted_date"


