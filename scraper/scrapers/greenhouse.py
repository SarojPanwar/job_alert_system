
from scraper.base import BaseScraper
import requests


class GreenhouseScraper(BaseScraper):

    def scrape(self, company):
        # https://boards.greenhouse.io/gitlab
        # board_token = gitlab
        board_token = company.career_url.rstrip("/").split("/")[-1]
        api_url = (
            f"https://boards-api.greenhouse.io/v1/boards/"f"{board_token}/jobs"
        )
        print("API URL:",api_url)
        
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()

        jobs = []
        
        for job in data["jobs"]:
            print(job["location"]["name"])
            print(len(job["location"]["name"]))
           
            jobs.append({
                "title":job["title"],
                "location": job["location"]["name"],
                "apply_url":job["absolute_url"],
            })

        return jobs



