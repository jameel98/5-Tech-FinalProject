import logging
import time
import unittest

from infra.browser.browser_wrapper import BrowserWrapper
from logic.browser.components.cart_popup import CartPopUp
from logic.browser.components.login import Login
from logic.browser.components.navbar import NavBar
from logic.browser.pages.cart_page import CartPage
from logic.browser.pages.search_result import SearchResult
from logic.enums.category import Category


class TestCart(unittest.TestCase):

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
        self.logger.info('start cart test')
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
        clear cart after test
        :return:
        """
        self.logger.info('end cart test')
        self.cart_page.refresh_page()
        self.cart_page.remove_all_elements()
        time.sleep(5)
        self.driver.quit()

    def test_add_item_to_cart(self):
        """
        add item to cart
        get its id
        go to cart and validate its same
        :return:
        """
        # act
        self.search_result.click_add_to_cart(1)
        element_id = self.search_result.get_element_id(1)

        # navigate to cart list page
    #    self.navbar.navigate_to_cart_list()
        self.cart_pop = CartPopUp(self.driver)
        self.cart_pop.click_go_to_cart()
        self.cart_page = CartPage(self.driver)
        element_id2 = self.cart_page.get_element_id(1)

        # assert
        self.assertEqual(element_id2, element_id)

    def test_remove_item_from_cart(self):
        """
        add element to cart then remove it and validate cart is empty
        :return:
        """
        # arrange
        self.search_result.click_add_to_cart(1)
        # navigate to cart list page
   #     self.navbar.navigate_to_cart_list()
        self.cart_pop = CartPopUp(self.driver)
        self.cart_pop.click_go_to_cart()
        self.cart_page = CartPage(self.driver)

        # act
        self.cart_page.click_remove_from_cart(1)

        # assert
        self.assertEqual(self.cart_page.get_list_is_empty_message(), "סל הקניות שלך ריק")