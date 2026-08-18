from abc import ABC , abstractmethod
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
class BaseScraper(ABC):
    """
    Base class for all platform scrapers.
    Every scraper must implement scrape().
    """
    def __init__(self):
        self.session = requests.Session()
        retry_strategy = Retry(
            total = 3,
            backoff_factor = 1,
            status_forcelist = [429,500,502,503,504],
            allowed_methods = ["GET","POST"],
        )
        adapter = HTTPAdapter(
            max_retries = retry_strategy
        )
        self.session.mount("https://",adapter)
        self.session.mount("http://",adapter)

    def get_json(self,url,**kwargs):
        """
            Send a GET request and return the JSON response.
        """
        response = self.session.get(
            url,
            timeout = 15,
            **kwargs
        )
        response.raise_for_status()
        return response.json()

    def post_json(self,url,**kwargs):
        """
            Send a POST request and return the JSON response.
        """
        response = self.session.post(
            url,
            timeout = 15,
            **kwargs
        )
        response.raise_for_status()
        return response.json()
    
    @abstractmethod
    def scrape(self,company):
        """
            Return a list of standardized job dictionaries.
        """
        pass
    
        