import hashlib
from django.db.models import Q
from jobs.models import Job
from alerts.services import AlertService

class JobService:
    @staticmethod
    def save_jobs(company , jobs):
        scraped_hashes = set()
        for job in jobs:

            hash_input = (
                    f"{company.name}"
                    f"{job.get('title','')}"
                    f"{job.get('apply_url','')}"
            )
            job_hash = hashlib.sha256(hash_input.encode()).hexdigest()
            scraped_hashes.add(job_hash)

            job_obj, created = Job.objects.update_or_create(
                job_hash = job_hash,
        
                defaults = {
                    "company": company,
                    "title": job.get("title",""),
                    "location": job.get("location",""),
                    "apply_url": job.get("apply_url",""),
                    "description": job.get("description",""),
                    "posted_date": job.get("posted_date"),
                    "department": job.get("department",""),
                    "office": job.get("office",""),
                    "experience": job.get("experience",""),
                    "employment_type":job.get("employment_type",""),
                    "work_mode":job.get("work_mode",""),
                    "skills":job.get("skills",""),

                },
            )
            if created:
                AlertService.create_notifications_for_job(job_obj)
        return scraped_hashes
    
    @staticmethod
    def deactivate_missing_jobs(company,scraped_hashes):
        return Job.objects.filter(
            company = company,
            is_active = True
        ).exclude(
            job_hash__in = scraped_hashes

        ).update(
            is_active = False
        )
    
    
    @staticmethod
    def search_jobs(
        search = None,
        location = None,
        work_mode = None,
        employment_type = None,
    ):
        jobs = Job.objects.filter(is_active=True)
        if search:
            jobs = jobs.filter(
                Q(title__icontains=search) | 
                Q(skills__icontains=search)
            )
        if location:
            jobs = jobs.filter(
                location__icontains=location
            )
        if work_mode:
            jobs = jobs.filter(
                work_mode__icontains=work_mode
            )
        if employment_type:
            jobs = jobs.filter(
                employment_type__icontains=employment_type
            )
        return jobs