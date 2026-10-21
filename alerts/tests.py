from django.test import TestCase
# from django.test import TestCase
from alerts.models import JobAlert
from alerts.services import AlertService
from companies.models import Company
from jobs.models import Job
from django.contrib.auth.models import User


class AlertServiceTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword123",
            email="test@example.com",
        )

        self.company = Company.objects.create(
            name="Test Company",
            career_url="https://example.com/careers",
            company_type="product",
            platform="greenhouse",
            is_active=True,
        )

        self.job = Job.objects.create(
            company=self.company,
            title="Python Backend Developer",
            location="India",
            apply_url="https://example.com/python-job",
            job_hash="test-job-hash",
            skills="Python, Django",
            is_active=True,
        )

        self.alert = JobAlert.objects.create(
            user=self.user,
            keywords="Python,Django",
        )

    def test_keyword_matches(self):
        result = AlertService.keyword_matches(
            self.alert,
            self.job,
        )

        self.assertTrue(result)
    def test_location_matches(self):
        self.alert.location = "India"

        result = AlertService.location_matches(
            self.alert,
            self.job,
        )

        self.assertTrue(result)

    def test_work_mode_matches(self):
        self.alert.work_mode = "Remote"
        self.job.work_mode = "Remote"

        result = AlertService.work_mode_matches(
            self.alert,
            self.job,
        )

        self.assertTrue(result)
    def test_employment_type_matches(self):
        self.alert.employment_type = "Full-time"
        self.job.employment_type = "Full-time"

        result = AlertService.employment_type_matches(
            self.alert,
            self.job,
        )

        self.assertTrue(result)

    def test_matches_alert_with_all_criteria(self):
        self.alert.keywords = "Python"
        self.alert.location = "India"
        self.alert.work_mode = "Remote"
        self.alert.employment_type = "Full-time"

        self.job.title = "Python Backend Developer"
        self.job.skills = "Python, Django"
        self.job.location = "India"
        self.job.work_mode = "Remote"
        self.job.employment_type = "Full-time"

        result = AlertService.matches_alert(
            self.alert,
            self.job,
        )

        self.assertTrue(result)
    def test_alert_does_not_match_wrong_location(self):
        self.alert.location = "United States"
        self.job.location = "India"

        result = AlertService.matches_alert(
            self.alert,
            self.job,
        )

        self.assertFalse(result)
# Create your tests here.
