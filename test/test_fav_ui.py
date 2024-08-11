import logging
import time
import unittest

from infra.browser.browser_wrapper import BrowserWrapper
from logic.browser.components.login import Login
from logic.browser.components.navbar import NavBar
from logic.browser.pages.fav_list_page import FavPage
from logic.browser.pages.search_result import SearchResult
from logic.enums.category import Category
from logic.enums.messages import Messages


class TestFavorite(unittest.TestCase):

    def setUp(self) -> None:
        """
        before each test apply those steps
        initialize driver
        open browser
        login via ui
        search for item
        :return:
        """
        self.logger = logging.getLogger(__name__)  # Initialize logger for this class
        self.logger.info('start fav list test')
        # Initialize driver
        self.browser_wrapper = BrowserWrapper()
        self.config = self.browser_wrapper.config

        # open browser
        self.driver = self.browser_wrapper.get_driver(self.config["base_url"])
        self.navbar = NavBar(self.driver)
        # login via ui
        self.nav_bar = NavBar(self.driver)
        self.nav_bar.click_login()
        self.login = Login(self.driver)
        self.login.login_flow(self.config["email"], self.config["password"])

        time.sleep(10)
        # search item by category
        self.navbar = NavBar(self.driver)
        self.navbar.click_on_category(Category.LAST_CHANCE.value)
        self.search_result = SearchResult(self.driver)

    def tearDown(self):
        """
        after each test remove clear the favorite list
        :return:
        """
        self.logger.info('end fav list test')
        self.fav_page.remove_all_elements()
        self.fav_page.refresh_page()
        time.sleep(5)
        self.driver.quit()

    def test_add_item_to_fav_list(self):
        """
        add item to fav list saves its id
        then go to the fav list and validte its same item by id
        :return:
        """
        # act
        self.search_result.click_add_to_fav(1)
        element_id = self.search_result.get_element_id(1)

        # navigate to favlist page
        self.navbar.navigate_to_fav_list()
        self.fav_page = FavPage(self.driver)
        element_id2 = self.fav_page.get_element_id(1)

        self.assertEqual(element_id2, element_id)

    def test_remove_item_from_fav_list(self):
        """
        test remove item. adds item to the list
        remove item
        validate list is empty
        :return:
        """
        # arrange
        self.search_result.click_add_to_fav(1)
        # navigate to favlist page
        self.navbar.navigate_to_fav_list()
        self.fav_page = FavPage(self.driver)
        # act
        self.fav_page.click_remove_from_fav(1)

        self.fav_page.refresh_page()

        self.assertEqual(self.fav_page.get_list_is_empty_message(), Messages.EMPTY_FAV_LIST.value)
