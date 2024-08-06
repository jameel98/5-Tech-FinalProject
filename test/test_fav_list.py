import time
import unittest
from auth.auth_setup import Auth
from infra.api.api_wrapper import APIWrapper
from infra.browser.browser_wrapper import BrowserWrapper
from logic.browser.components.navbar import NavBar
from logic.browser.pages.fav_list_page import FavPage
from logic.browser.pages.search_result import SearchResult
from logic.enums.category import Category


class TestFavorite(unittest.TestCase):

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
        #search item by category
        self.navbar = NavBar(self.driver)
        self.navbar.click_on_category(Category.LAST_CHANCE.value)
        self.search_result = SearchResult(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_add_item_to_favorite_page(self):
        # act
        self.search_result.get_item_fav_button_locator(1)
        element_id = self.search_result.get_element_id(1)

        # navigate to favlist page
        self.navbar.navigate_to_fav_list()
        self.fav_page = FavPage(self.driver)
        element_id2 = self.fav_page.get_element_id(1)

        self.assertEqual(element_id2, element_id)

