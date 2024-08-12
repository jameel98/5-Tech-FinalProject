import logging
import os

from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from logic.api.cookies_manager import CookiesManager


class APIFavList:
    def __init__(self, request: APIWrapper):
        self.logger = logging.getLogger(__name__)  # Initialize logger for this class
        self._request = request
        current_working_directory = os.getcwd()
        self.api_fav = ConfigProvider.load_from_file(current_working_directory + '../../config/fav.json')
        self.api_url = ConfigProvider.load_from_file(current_working_directory + '../../config/api_urls.json')
        self.cookies_manager = CookiesManager()

    def add_item_to_fav(self):
        form_key = self.cookies_manager.get_form_key()
        print(form_key)
        cart_cookies = self.cookies_manager.get_cart_cookies()
        print(cart_cookies)
        # Append form_key to payload
        self.api_fav["add_cart_payload"]["form_key"] = form_key

        # Append cookie header to add_headers
        self.api_fav["add_headers"]["cookie"] = cart_cookies["cookie"]

        return self._request.post_request(
            self.api_url["add_to_cart"],
            self.api_fav["add_headers"],
            self.api_fav["add_cart_payload"]
        )

