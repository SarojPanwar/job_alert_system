from urllib.parse import urlparse
import logging
import requests
from concurrent.futures import ThreadPoolExecutor
from scraper.base import BaseScraper

logger = logging.getLogger(__name__)
class SmartRecruitersScraper(BaseScraper):
    def fetch_job_details(self,job):
         
         try:
              details_data = self.get_json(job["ref"])
              return {
                   
                   "title": job.get("name",""),
                   "location": job.get("location",{}).get("fullLocation",""),
                   "experience":job.get("experienceLevel",{}).get("label",""),
                   "employment_type": job.get("typeOfEmployment",{}).get("label",""),
                   "department":job.get("department",{}).get("label",""),
                   "office": "",
                   "work_mode":"",
                   "apply_url": details_data.get("applyUrl",""),
                   "description":(details_data
                        .get("jobAd",{})
                        .get("sections",{})
                        .get("jobDescription","")
                   ),
                   "posted_date": details_data.get("releasedDate"),
              }
         except requests.RequestException as e:
            logger.error(
                 "Failed to fetch details of %s :%s",
                 job.get("name","Unknown"),
                 e
            )
            return None
            

    def scrape(self, company):
        parsed = urlparse(company.career_url)
    
        company_identifier = parsed.path.lstrip("/")
        
        api_url = (
            f"https://api.smartrecruiters.com/v1/companies/"
            f"{company_identifier}/postings"
        )
        print("Visa career URL:", company.career_url)
        print("SmartRecruiters API URL:", api_url)  
        
        # Pagination starts here
        offset = 0
        limit = 100
        jobs_data =[]
        while True:
             params = {
                  "offset": offset,
                  "limit": limit,
             }
             data = self.get_json(
                  api_url,
                  params=params
             )
             jobs_data.extend(
                  data.get("content",[])
                )
             total_found = data.get(
                  "totalFound",
                  0
                )
             offset +=limit
             if offset >=total_found:
                  break
             
        logger.info(
             "Fetched %d jobs from SmartRecruiters for %s",
             len(jobs_data),
             company.name
        )
        
        # concurrent details requests 
        jobs = []
        with ThreadPoolExecutor(max_workers=5) as pool:
             results = pool.map(
                  self.fetch_job_details,
                  jobs_data
             )

             for result in results:
                  if result is not None:
                       jobs.append(result)  
            
        logger.info(
             "Fetched details for %d out of %d jobs",
             len(jobs),
             len(jobs_data)
        )
        return jobs


       
           
        