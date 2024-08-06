import time
import unittest
from auth.auth_setup import Auth
from infra.api.api_wrapper import APIWrapper
from infra.browser.browser_wrapper import BrowserWrapper
from logic.api.request.cart_list_request import APICartList
from logic.api.response.fav_list_response import FavListResponse
from logic.browser.components.navbar import NavBar


class TestCart(unittest.TestCase):

    def setUp(self) -> None:
        # Initialize driver
        self.browser_wrapper = BrowserWrapper()
        self.config = self.browser_wrapper.config
        self.driver = self.browser_wrapper.get_driver(self.config["base_url"])
        self.auth = Auth(driver=self.driver)
        self.auth.login_via_api_save_cookies()
        self.auth.set_cookies()
        self.driver.get(self.config["base_url"])
        self.api_request = APIWrapper()
        self.cart_api = APICartList(self.api_request)

    def tearDown(self):
        self.driver.quit()

    def test_add_item_to_cart(self):
        # act
        response = self.cart_api.add_item_to_cart()
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        print(response.data)

    def test_remove_item_from_cart(self):
        self.cart_api.add_item_to_cart()
        # act
        response = self.cart_api.remove_item_from_cart()
