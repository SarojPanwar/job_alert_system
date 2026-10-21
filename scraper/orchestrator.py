import logging
from companies.models import Company
from jobs.services import JobService
from scraper.factory import ScraperFactory

logger = logging.getLogger(__name__)
class ScraperOrchestrator:
    def run(self):
        companies = Company.objects.filter(is_active=True)

        logger.info(
            "Starting job scraping for %d companies",
            companies.count()
        )
        for company in companies:
            logger.info(
                "Starting scraper for %s",
                company.name
            )
            try:
                
                scraper = ScraperFactory.get_scraper(company)
                jobs = scraper.scrape(company)
                if not jobs:
                    logger.warning(
                        "No jobs returned for %s.skipping deactivation.",
                        company.name
                    )
                    continue
                
                scraped_hashes = JobService.save_jobs(
                    company,
                    jobs
                )

                deactivated_count =JobService.deactivate_missing_jobs(
                    company,
                    scraped_hashes
                )
                logger.info(
                    "Deactivated %d missing jobs for %s",
                    deactivated_count,
                    company.name
                )

                logger.info(
                    "Successfully scraped %d jobs from %s",
                    len(jobs),
                    company.name
                )
            except Exception:
                logger.exception(
                    "Failed to scrape %s",
                    company.name
                )
        logger.info("Job scraping completed")
            