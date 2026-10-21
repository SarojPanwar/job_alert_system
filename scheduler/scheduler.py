from apscheduler.schedulers.background import BackgroundScheduler
from scheduler.jobs import run_job_scraper

def start_scheduler():
    scheduler = BackgroundScheduler()

    scheduler.add_job(
        run_job_scraper,
        "interval",
        hours=1,
        id="job_scraper",
        replace_existing=True,
    )
    scheduler.start()
    print("Scheduler is running .Next scrape will run in 1 hour.")