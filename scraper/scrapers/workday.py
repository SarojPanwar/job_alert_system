from scraper.base import BaseScraper
from urllib.parse import urljoin,urlparse
class WorkdayScraper(BaseScraper):

    def scrape(self, company):
        parsed = urlparse(company.career_url)
        base_url = f"{parsed.scheme}://{parsed.netloc}"
        company_slug = parsed.netloc.split(".")[0]
        site_name = parsed.path.lstrip("/")

        api_url = (
            f"{base_url}/wday/cxs/"
            f"{company_slug}/"
            f"{site_name}/jobs"
        )
        
        headers = {
            "Content-Type": "application/json"
        }
        payload = {
            "appliedFacets": {},
            "limit": 20,
            "offset": 0,
            "searchText": "",
        }
        
        data = self.post_json(
            api_url,
            headers = headers,
            json = payload
        )
        jobs_data = data["jobPostings"]
        
        jobs = []
        for job in jobs_data:
            apply_url = urljoin(base_url, job["externalPath"])
            jobs.append({
                "title": job["title"],
                "location": job["locationsText"],
                "employment_type": "",
                "work_mode": "",
                "department": "",
                "office": "",
                "apply_url": apply_url,
                "description": "",
                "posted_date": None,
            })
       
        return jobs