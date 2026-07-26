from django.core.management.base import BaseCommand
from scraper.orchestrator import ScraperOrchestrator

class Command(BaseCommand):
    help = "Scrape jobs from all active companies"
    def handle(self,*args,**kwargs):
        orchestrator = ScraperOrchestrator()
        orchestrator.run()

        self.stdout.write(
            self.style.SUCCESS("Job scraping completed successfully!")
        )