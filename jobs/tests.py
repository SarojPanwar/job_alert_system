from django.test import TestCase
from companies.models import Company
from jobs.models import Job
from jobs.services import JobService

# Create your tests here.
class JobServiceTests(TestCase):
    def setUp(self):
        self.company = Company.objects.create(
            name="Test Company",
            career_url="https://example.com/careers",
            company_type="product",
            platform="greenhouse",
            is_active=True,

        )
    def test_reactivate_existing_job(self):
        job_data = {
            "title": "Python Developer",
            "location": "India",
            "apply_url": "https://example.com/python-developer",
            "description": "Backend developer role",
            "posted_date": None,
            "department": "Engineering",
            "office": "",
            "experience": "0-2 years",
            "employment_type": "Full-time",
            "work_mode": "Remote",
            "skills": "Python, Django",
        }

        JobService.save_jobs(self.company, [job_data])

        job = Job.objects.get(
            company=self.company,
            title="Python Developer",
        )

        self.assertTrue(job.is_active)
        self.assertEqual(job.location, "India")

    def test_create_new_job(self):
        job_data = {
            "title": "Django Backend Developer",
            "location": "India",
            "apply_url": "https://example.com/django-job",
            "description": "Backend developer role",
            "posted_date": None,
            "department": "Engineering",
            "office": "",
            "experience": "0-2 years",
            "employment_type": "Full-time",
            "work_mode": "Remote",
            "skills": "Python, Django",
        }

        JobService.save_jobs(self.company, [job_data])

        job = Job.objects.get(
            company=self.company,
            title="Django Backend Developer",
        )

        self.assertTrue(job.is_active)
        self.assertEqual(job.location, "India")

    def test_deactivate_missing_job(self):
        job_data = {
            "title": "Backend Developer",
            "location": "India",
            "apply_url": "https://example.com/backend-job",
            "description": "Backend developer role",
            "posted_date": None,
            "department": "Engineering",
            "office": "",
            "experience": "0-2 years",
            "employment_type": "Full-time",
            "work_mode": "Remote",
            "skills": "Python, Django",
        }

        JobService.save_jobs(self.company, [job_data])

        job = Job.objects.get(
            company=self.company,
            title="Backend Developer",
        )

        # Simulate a scrape where this job is no longer present
        JobService.deactivate_missing_jobs(
            self.company,
            scraped_hashes=set(),
        )

        job.refresh_from_db()

        self.assertFalse(job.is_active)
        self.assertTrue(
            Job.objects.filter(id=job.id).exists()
        )

from unittest.mock import patch, MagicMock
from scraper.orchestrator import ScraperOrchestrator


class ScraperOrchestratorTests(TestCase):
    def setUp(self):
        self.company = Company.objects.create(
            name="Test Company",
            career_url="https://example.com/careers",
            company_type="product",
            platform="greenhouse",
            is_active=True,
        )

    @patch("scraper.orchestrator.JobService.deactivate_missing_jobs")
    @patch("scraper.orchestrator.JobService.save_jobs")
    @patch("scraper.orchestrator.ScraperFactory.get_scraper")
    def test_empty_scrape_does_not_deactivate_jobs(
        self,
        mock_get_scraper,
        mock_save_jobs,
        mock_deactivate_jobs,
    ):
        mock_scraper = MagicMock()
        mock_scraper.scrape.return_value = []
        mock_get_scraper.return_value = mock_scraper

        ScraperOrchestrator().run()

        mock_save_jobs.assert_not_called()
        mock_deactivate_jobs.assert_not_called()

