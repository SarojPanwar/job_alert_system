from scraper.scrapers.greenhouse import GreenhouseScraper
from scraper.scrapers.lever import LeverScraper
from scraper.scrapers.workday import WorkdayScraper
from scraper.scrapers.custom import CustomScraper


class ScraperFactory:

    @staticmethod
    def get_scraper(company):

        if company.platform == "greenhouse":
            return GreenhouseScraper()

        elif company.platform == "Lever":
            return LeverScraper()

        elif company.platform == "Workday":
            return WorkdayScraper()

        return CustomScraper()