from jobs.models import Job

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