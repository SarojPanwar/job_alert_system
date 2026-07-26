from companies.models import Company
from jobs.services import JobService
from scraper.factory import ScraperFactory

class ScraperOrchestrator:
    def run(self):
        companies = Company.objects.filter(is_active=True)

        for company in companies:
            scraper = ScraperFactory.get_scraper(company)
            jobs = scraper.scrape(company)
            JobService.save_jobs(company,jobs)
            