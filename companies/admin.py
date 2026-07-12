from django.contrib import admin
from .models import Company
# Register your models here.

admin.site.site_header = "Job Alert System Administration"
admin.site.site_title = "Job Alert Admin"
admin.site.index_title = "Welcome to Job Alert System"
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display =(
        "name",
        "company_type",
        "platform",
        "is_active",
        "last_checked",
    )
    list_filter = (
        "company_type",
        "platform",
        "is_active",
    )

    search_fields = (
        "name",
    )
    ordering = (
        "name",
    )