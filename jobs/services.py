import hashlib

from jobs.models import Job

class JobService:
    @staticmethod
    def save_jobs(company , jobs):
        for job in jobs:

            hash_input = f"{company.name}{job.get('title','')}{job.get('apply_url','')}"
            job_hash = hashlib.sha256(hash_input.encode()).hexdigest()

            Job.objects.update_or_create(
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
                    "employment_type":job.get("employement_type",""),
                    "work_mode":job.get("work_mode",""),
                    "skills":job.get("skills",""),

                },
            )
