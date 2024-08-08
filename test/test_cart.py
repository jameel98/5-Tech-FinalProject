import json
import os
import time
import unittest
from auth.auth_setup import Auth
from infra.api.api_wrapper import APIWrapper
from infra.browser.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.api.cookies_manager import CookiesManager
from logic.api.request.cart_list_request import APICartList
from logic.api.response.fav_list_response import FavListResponse
from logic.browser.components.login import Login
from logic.browser.components.navbar import NavBar
from logic.enums.category import Category


class TestCart(unittest.TestCase):

    def setUp(self) -> None:
        # Initialize driver
        self.browser_wrapper = BrowserWrapper()
        self.config = self.browser_wrapper.config
        self.driver = self.browser_wrapper.get_driver(self.config["base_url"])
        self.api_wrapper = APIWrapper()
        self.nav_bar = NavBar(self.driver)
        self.nav_bar.click_login()
        self.login = Login(self.driver)
        self.login.login_flow(self.config["email"], self.config["password"])
        self.cookies = self.driver.get_cookies()
        print(self.cookies)
        self.nav_bar.click_on_category(Category.LAST_CHANCE)
        time.sleep(5)
        self.cookies = self.driver.get_cookies()
        ConfigProvider.save_cookies(self.cookies)

        # Save cookies to a JSON file
        self.cart_api = APICartList(self.api_wrapper)

    def tearDown(self):
        self.driver.quit()

    def test_add_item_to_cart(self,):
        # act
        response = self.cart_api.add_item_to_cart()
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        print(response.data)
        self.nav_bar.navigate_to_cart_list()
        time.sleep(10)
