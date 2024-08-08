import time
import unittest
from auth.auth_setup import Auth
from infra.api.api_wrapper import APIWrapper
from infra.browser.browser_wrapper import BrowserWrapper
from logic.browser.components.navbar import NavBar
from logic.browser.pages.fav_list_page import FavPage
from logic.browser.pages.search_result import SearchResult
from logic.enums.category import Category


class TestSearch(unittest.TestCase):

    def setUp(self) -> None:
        # Initialize driver
        self.browser_wrapper = BrowserWrapper()
        self.config = self.browser_wrapper.config
        self.driver = self.browser_wrapper.get_driver(self.config["base_url"])
        # start auth
        self.auth = Auth(driver=self.driver)
        self.auth.login_via_api_save_cookies()
        self.auth.set_cookies()
        # open browser
        self.driver.get(self.config["base_url"])
        self.navbar = NavBar(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_search_item_by_category(self):
        # act
        self.navbar.click_on_category(Category.LAST_CHANCE.value)
        self.search_result = SearchResult(self.driver)

        # assert

