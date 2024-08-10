import logging
import unittest
from infra.browser.browser_wrapper import BrowserWrapper
from infra.utils import Utils
from logic.browser.components.navbar import NavBar
from logic.browser.pages.search_result import SearchResult
from logic.enums.category import Category


class TestSearch(unittest.TestCase):

    def setUp(self) -> None:
        self.logger = logging.getLogger(__name__)  # Initialize logger for this class
        self.logger.info("start test search")
        # Initialize driver
        self.browser_wrapper = BrowserWrapper()
        self.config = self.browser_wrapper.config

        # open browser
        self.driver = self.browser_wrapper.get_driver(self.config["base_url"])
        self.navbar = NavBar(self.driver)

    def tearDown(self):
        self.logger.info("end test search")

        self.driver.quit()

    def test_search_item_by_category(self):
        """
        search for item by category. choose category
        from categories enum
        validate the items in search result are all from this category
        :return:
        """
        self.logger.info("start test search by category")
        # act
        self.navbar.click_on_category(Category.LAST_CHANCE.value)
        self.search_result = SearchResult(self.driver)

        # assert
        self.assertEqual(self.search_result.get_element_last_chance_attribute(), "Last Chance")

    def test_search_item_by_name(self):
        """
            search for item by name. write item name
            in input section
            validate the items in search result are all from this category
            :return:
        """
        self.logger.info("start test search by name")

        # act
        self.navbar.search_product_by_name(u"צלחת עיקרית PRESTIGE")

        self.search_result = SearchResult(self.driver)
        name = self.search_result.get_element_name()

        self.assertEqual(name, u"צלחת עיקרית PRESTIGE")

    def test_search_name_doesnt_exist(self):
        """
        NEGATIVE TEST
        search for item by name. generate random chars
        :return:
        """
        self.logger.info("start test search random name")

        self.navbar.search_product_by_name(Utils.generate_random_text(5))

        self.search_result = SearchResult(self.driver)
        self.assertEqual(self.search_result.get_search_message(), "אין תוצאות לשאילתת חיפוש שלך.")
