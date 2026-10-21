from django.core.management.base import BaseCommand
from scheduler.scheduler import start_scheduler

class Command(BaseCommand):
    help = "Start the job scraping scheduler"

    def handle(self,*args,**options):
        self.stdout.write(
            self.style.SUCCESS("Job scheduler started.")

        )
        start_scheduler()
        