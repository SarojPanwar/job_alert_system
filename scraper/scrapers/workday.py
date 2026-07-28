from scraper.base import BaseScraper
import requests

class WorkdayScraper(BaseScraper):

    def scrape(self, company):
        career_url = company.career_url

        print(career_url)
        api_url = "https://nvidia.wd5.myworkdayjobs.com/wday/cxs/nvidia/NVIDIAExternalCareerSite/jobs"

        response = requests.post(api_url)

        print(response.status_code)
        print(response.text[:500])
        return []