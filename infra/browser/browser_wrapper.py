import logging

from selenium import webdriver

from infra.config_provider import ConfigProvider


class BrowserWrapper:

    def __init__(self):
        self._driver = None
        self.config = ConfigProvider.load_from_file('../../config/config.json')
        self.api_urls = ConfigProvider.load_from_file('../../config/api_urls.json')
        self.user_login = ConfigProvider.load_from_file('../../config/user_login.json')
        self.logger = logging.getLogger(__name__)

    def get_driver(self, url):
        if not url:
            raise ValueError("URL not found in the configuration.")

        if self.config["browser"] == "Chrome":
            self._driver = webdriver.Chrome()
        elif self.config["browser"] == "FireFox":
            self._driver = webdriver.Firefox()
        elif self.config["browser"] == "Edge":
            self._driver = webdriver.Edge()

        self._driver.get(url)
        self._driver.maximize_window()
        logging.info(f'{self.config["browser"]} browser opened.')
        return self._driver
