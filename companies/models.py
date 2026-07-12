from django.db import models

# Create your models here.
class Company(models.Model):
    PLATFORM_CHOICES =[
        ("greenhouse","Greenhouse"),
        ("lever","Lever"),
        ("workday","Workday"),
        ("ashby","Ashby"),
        ("custom","Custom"),
        ("smartrecruiters","SmartRecruiters"),
        ("taleo","Taleo"),

    ]
    COMPANY_TYPE =[
        ("product","Product"),
        ("service","Service"),
        ("startup","Startup"),
        ("fintech","Fintech"),
        ("mnc","MNC"),
        
    ]
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name = "Company Name",
        )
    
    career_url =models.URLField(
        unique=True,
        verbose_name = "Career Page URL"
        )

    company_type = models.CharField(
        max_length=20,
        choices = COMPANY_TYPE,
        default = "product",
        verbose_name = "Company Type"
    )

    platform = models.CharField(
        max_length = 20,
        choices = PLATFORM_CHOICES,
        default = "custom",
        verbose_name = "Career Platform"
    )
    
    is_active = models.BooleanField(default=True)

    last_checked = models.DateTimeField(
        null = True,
        blank = True

    )

    created_at = models.DateTimeField(
        auto_now_add= True 
        )
    updated_at = models.DateTimeField(
        auto_now = True
    )

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]
        verbose_name = "Company"
        verbose_name_plural = "Companies"
        