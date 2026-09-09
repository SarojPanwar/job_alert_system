
from jobs.models import Job
from alerts.models import JobAlert
from notifications.models import Notification

class AlertService:

    @staticmethod
    def keyword_matches(alert,job):

        if not alert.keywords:
            return True
        
        keywords=[
            keyword.strip().lower()
            for keyword in alert.keywords.split(",")
            if keyword.strip()

        ]

        text = f"{job.title}{job.skills}".lower()

        return any(
            keyword in text
            for keyword in keywords
        )

    @staticmethod
    def location_matches(alert,job):
        # if the user didn't specify a location =>then we don't filter based on location
        if not alert.location:
            return True

        return alert.location.lower() in job.location.lower()
    
    @staticmethod
    def work_mode_matches(alert,job):
        if not alert.work_mode:
            return True
        
        if not job.work_mode:
            return False
        return alert.work_mode.lower() in job.work_mode.lower()

    @staticmethod
    def employment_type_matches(alert,job):
        if not alert.employment_type:
            return True

        if not job.employment_type:
            return False
        return (
            alert.employment_type.lower() in job.employment_type.lower()
        )
    @staticmethod
    def matches_alert(alert,job):

            return (
                AlertService.keyword_matches(alert,job)
                and AlertService.location_matches(alert,job)
                and AlertService.work_mode_matches(alert,job)
                and AlertService.employment_type_matches(alert,job)
    )

    @staticmethod
    def get_matching_jobs(alert):
        jobs = Job.objects.filter(is_active=True)

        matching_jobs = []
        for job in jobs:
            if AlertService.matches_alert(alert,job):
                matching_jobs.append(job)

        return matching_jobs

    @staticmethod
    def create_notifications_for_job(job):
        alerts = JobAlert.object.filter(
            is_active= True
        )
        for alert in alerts:
            if AlertService.matches_alert(alert,job):
                Notification.objects.create(
                    user = alert.user,
                    job = job,
                    message=f"New job matching your alert:{job.title}"
                )