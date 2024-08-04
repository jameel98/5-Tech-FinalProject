import time
import unittest
import requests

from infra.browser.browser_wrapper import BrowserWrapper
from infra.logger_setup import LogSetup
from logic.browser.components.login import Login
from logic.browser.components.navbar import NavBar


class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        """
               setup initialize browser data
               initialize pages before tests run
               :return:
               """
        # Instantiate the logger
        log_setup = LogSetup()
        self.logger = log_setup.logger

        # Initialize driver
        self.logger.info("Initializing BrowserWrapper and WebDriver.")
        self.browser_wrapper = BrowserWrapper()
        self.config = self.browser_wrapper.config
        self.driver = self.browser_wrapper.get_driver(self.config["base_url"])

        # Initialize pages
        self.navbar = NavBar(self.driver)
        self.navbar.click_login()
        self.login_page = Login(self.driver)

    def tearDown(self):
        self.logger.info("Quitting the WebDriver.")
        self.driver.quit()

    def test_login_successfully(self):
        """
        login successful with valid email and password
        click login in navbar
        popup appear so put input and click login
        wait to popup disappear and validate username appears
        :return:
        """
        # Arrange
        self.logger.info("test login successfully starts.")
        self.login_page.login_flow(self.config["email"], self.config["password"])

        # Add item to favorite list via API
        favorite_api_url = "https://www.foxhome.co.il/mylist/wishlist?update=1&_=1722627737417"
        favorite_payload = {
            "update": "1",
            "_": "1722627737417"
        }
        favorite_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest"
        }

        session = requests.Session()
        add_favorite_response = session.get(favorite_api_url, headers=favorite_headers, params=favorite_payload)
        time.sleep(20)
        if add_favorite_response.status_code == 200:
            print("Item added to favorites via API.")
        else:
            print("Failed to add item to favorites via API.")
            exit()