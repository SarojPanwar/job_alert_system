
from unittest.mock import patch, MagicMock
from django.test import TestCase
from companies.models import Company
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
