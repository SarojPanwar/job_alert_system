from scraper.scrapers.greenhouse import GreenhouseScraper
from scraper.scrapers.lever import LeverScraper
from scraper.scrapers.workday import WorkdayScraper
from scraper.scrapers.smart_recruiters import SmartRecruitersScraper


class ScraperFactory:

    @staticmethod
    def get_scraper(company):

        if company.platform == "greenhouse":
            return GreenhouseScraper()

        elif company.platform == "lever":
            return LeverScraper()

        elif company.platform == "workday":
            return WorkdayScraper()

        elif company.platform == "smartrecruiters":
            return SmartRecruitersScraper()

    