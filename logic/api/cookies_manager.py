import json
import os

from infra.config_provider import ConfigProvider


class CookiesManager:
    def __init__(self):
        current_working_directory = os.getcwd()
        self.cookies = ConfigProvider.load_from_file(current_working_directory + '../../config/cookies.json')

    def get_form_key(self):
        return self.get_cookie("form_key")

    def get_cookie(self, cookie_name):
        """Fetches a specific cookie's value."""
        cookie = next((c for c in self.cookies if c['name'] == cookie_name), None)
        return cookie['value'] if cookie else ""

    def get_cart_cookies(self):
        # Fetch specific cookies related to the cart from the browser
        cart_cookies = {
            "PHPSESSID": self.get_cookie("PHPSESSID"),
            "block_addToCart": self.get_cookie("block_addToCart"),
            "X_Magento_Vary": self.get_cookie("X-Magento-Vary"),
            "customer_data": self.get_cookie("customer_data"),
            "form_key": self.get_cookie("form_key"),
            "private_content_version": self.get_cookie("private_content_version"),
            "store": self.get_cookie("store"),
            "store_id": self.get_cookie("store_id"),
            "try_addToCart": self.get_cookie("try_addToCart")
        }

        # Create the cookie header string
        cookie_header = (
            f"PHPSESSID={cart_cookies['PHPSESSID']}; "
            f"block_addToCart={cart_cookies['block_addToCart']}; "
            f"X-Magento-Vary={cart_cookies['X_Magento_Vary']}; "
            f"form_key={cart_cookies['form_key']}; "
            f"customer_data={cart_cookies['customer_data']}; "
            f"private_content_version={cart_cookies['private_content_version']}; "
            f"store={cart_cookies['store']}; "
            f"store_id={cart_cookies['store_id']}; "
            f"try_addToCart={cart_cookies['try_addToCart']}"
            f"try_addToCart={cart_cookies['try_addToCart']}"
        )

        return {
            "cookie": cookie_header
        }

    def load_cookies(self, cookies_file_path):
        """Loads all cookies from a specified JSON file."""
        try:
            with open(cookies_file_path, 'r') as file:
                self.cookies = json.load(file)
            print("Cookies loaded successfully.")
        except FileNotFoundError:
            print(f"File {cookies_file_path} not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON from the cookies file.")
        except Exception as e:
            print(f"An error occurred while loading cookies: {e}")

    def get_all_cookies(self):
        """Creates a cookie header string with all loaded cookies."""
        cookie_header = "; ".join(f"{cookie['name']}={cookie['value']}" for cookie in self.cookies)
        return cookie_header