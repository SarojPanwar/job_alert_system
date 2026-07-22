from abc import ABC , abstractmethod
class BaseScraper(ABC):
    """
    Base class for all platform scrapers.
    Every scraper must implement scrape().
    """
    @abstractmethod
    def scrape(self,company):
        """
            Scrape jobs for the given company.

            Returns:
                list[dict]
        """
        pass