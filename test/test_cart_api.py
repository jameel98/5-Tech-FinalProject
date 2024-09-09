import json
import os
import time
import unittest
from infra.api.api_wrapper import APIWrapper
from infra.browser.browser_wrapper import BrowserWrapper
from logic.api.request.cart_list_request import APICartList
from logic.browser.components.login import Login
from logic.browser.components.navbar import NavBar


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
        self.form_key = self.driver.get_cookie("form_key")["value"]
        print(self.form_key)
        time.sleep(20)

    def tearDown(self):
        self.driver.quit()

    def test_add_item_to_cart(self,):
        # Extract cookies after login
        self.cookies = self.driver.get_cookies()
        cookies_dict = {cookie['name']: cookie['value'] for cookie in self.cookies}

        # Append form_key to the cookies_dict
        cookies_dict["form_key"] = self.form_key

        # Debug: Print all cookies to see what's available
        print("Available cookies:", cookies_dict)

        # API endpoint to add item to cart
        add_to_cart_url = "https://www.foxhome.co.il/checkout/cart/add/product/20681/"

        # Headers
        headers = {
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-language": "en-US,en;q=0.9",
            "cache-control": "no-cache",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "origin": "https://www.foxhome.co.il",
            "referer": "https://www.foxhome.co.il/last-chance",
            "cookie": "",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
            "x-requested-with": "XMLHttpRequest"
        }

        # Data payload for the item to be added to the cart
        data = {
            "product_layout": "category",
            "product": "20681",
            "form_key": self.form_key,
            "super_attribute[268]": "674211",
            "super_attribute[93]": "670292"
        }

        # Convert cookies dict to the required format for the request
        cookie_string = "; ".join([f"{key}={value}" for key, value in cookies_dict.items()])
        headers["cookie"] = cookie_string

        # Save cookies to a JSON file
        self.cart_api = APICartList(self.api_wrapper)
        # Make the API request to add the item to the cart
        response = self.cart_api.add_item_to_cart(add_to_cart_url, headers, data)
        print(response.data)
