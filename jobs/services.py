import hashlib

from jobs.models import Job

class JobService:
    @staticmethod
    def save_jobs(company , jobs):
        for job in jobs:

            hash_input = f"{company.name}{job["title"]}{job["apply_url"]}"
            job_hash = hashlib.sha256(hash_input.encode()).hexdigest()

            Job.objects.update_or_create(
                job_hash = job_hash,
        
                defaults = {
                    "company": company,
                    "title": job["title"],
                    "location": job["location"],
                    "apply_url": job["apply_url"],
                },
            )