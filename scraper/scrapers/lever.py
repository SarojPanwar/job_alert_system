from scraper.base import BaseScraper
import requests
from datetime import datetime,timezone
class LeverScraper(BaseScraper):

    def scrape(self, company):
        account = company.career_url.rstrip("/").split("/")[-1]
        

        api_url = f"https://api.lever.co/v0/postings/{account}?mode=json"
        
        response = requests.get(api_url)
        data = response.json()
        
       
        jobs = [] 
        for job in data:
            timestamp = job.get("createdAt")
            posted_date = None
            if timestamp:
                posted_date = datetime.fromtimestamp(timestamp / 1000,tz=timezone.utc)
            jobs.append({
                "title": job.get("text", ""),
                "location": job.get("categories", {}).get("location", ""),
                "employment_type": job.get("categories", {}).get("commitment", ""),
                "work_mode": job.get("workplaceType", ""),
                "department": job.get("categories", {}).get("team", ""),
                "apply_url": job.get("applyUrl", ""),
                "description": job.get("descriptionPlain", ""),
                "posted_date": posted_date,

            })
            

        return jobs