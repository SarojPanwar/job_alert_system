
from scraper.base import BaseScraper
import requests
import json
from scraper.utils.html_cleaner import clean_html

class GreenhouseScraper(BaseScraper):

    def scrape(self, company):
        # https://boards.greenhouse.io/gitlab
        # board_token = gitlab
        board_token = company.career_url.rstrip("/").split("/")[-1]
        api_url = (
            f"https://boards-api.greenhouse.io/v1/boards/"f"{board_token}/jobs?content=true"
        )
        
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
       
        jobs = []
        
        for job in data["jobs"]:
           
            jobs.append({
                "title": job.get("title", ""),
                "location": job.get("location", {}).get("name", ""),
                "apply_url": job.get("absolute_url", ""),
                "description": clean_html(
                        job.get("content", "")
                        ),
                "posted_date": job.get("first_published"),

                "department": (
                    job.get("departments", [{}])[0].get("name", "")
                    if job.get("departments")
                    else ""
                ),

                "office": (
                    job.get("offices", [{}])[0].get("name", "")
                    if job.get("offices")
                    else ""
                ),
            })
            

        return jobs



