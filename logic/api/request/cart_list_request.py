import os

from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider


class APICartList:
    def __init__(self, request: APIWrapper):
        self._request = request
        current_working_directory = os.getcwd()

        self.config = ConfigProvider.load_from_file(current_working_directory + '../../config/config.json')
        self.api_cart = ConfigProvider.load_from_file(current_working_directory + '../../config/cart.json')
        self.api_url = ConfigProvider.load_from_file(current_working_directory + '../../config/api_urls.json')

    def add_item_to_cart(self):
        return self._request.post_request(self.api_url["add_to_cart"],
                                          self.api_cart["add_headers"],
                                          self.api_cart["add_cart_payload"])

    def remove_item_from_cart(self):
        return self._request.post_request(self.api_url["remove_from_cart"],
                                          self.api_cart["remove_header"],
                                          self.api_cart["remove_payload"])
