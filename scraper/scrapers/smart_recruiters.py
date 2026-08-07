from urllib.parse import urlparse

import requests
from scraper.base import BaseScraper


class SmartRecruitersScraper(BaseScraper):

    def scrape(self, company):
        parsed = urlparse(company.career_url)
    
        company_identifier = parsed.path.lstrip("/")
        
        api_url = (
            f"https://api.smartrecruiters.com/v1/companies/"
            f"{company_identifier}/postings"
        )
        # response = requests.get(api_url)
        # response.raise_for_status()
        # data = response.json()
        data = self.get_json(api_url)
        
        jobs_data = data["content"]
        jobs = []
        for job in jobs_data:
            try:
                    details_data = self.get_json(job["ref"])

            except requests.RequestException as e:

                print(f"Error fetching job details for {job['name']}: {e}")
                continue


            jobs.append({
                "title": job.get("name",""),
                "location": job.get("location",{}).get("fullLocation",""),
                "experience":job.get("experienceLevel",{}).get("Label",""),
                "employment_type": job.get("typeOfemployment",{}).get("Label",""),
                "department":job.get("department",{}).get("Label",""),
                "office": "",
                "work_mode":"",
                "apply_url": details_data.get("applyUrl",""),
                "description":details_data.get("jobAd", {}).get("sections", {}).get("jobDescription",""),
                "posted_date": details_data.get("releasedDate",""),
                
            })
           


        return jobs