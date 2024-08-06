import time
import unittest
from auth.auth_setup import Auth
from infra.api.api_wrapper import APIWrapper
from infra.browser.browser_wrapper import BrowserWrapper
from logic.api.request.cart_list_request import APIFavList
from logic.api.response.fav_list_response import FavListResponse
from logic.browser.components.navbar import NavBar


class TestFavorite(unittest.TestCase):

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
        self.fav_list = APIFavList(self.api_request)

    def tearDown(self):
        self.driver.quit()

    def test_add_item_to_favorite_page(self):
        response = self.fav_list.add_item_to_fav_list()
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        print(response.data)
        fav_list_response = FavListResponse.from_fav_list(response.data)

        # Perform assertions
        # self.assertEqual(fav_list_response.action, "success", "Failed to add item to the favorite list")
        # assert fav_list_response.data['add'] == 1, "Item was not added to the favorite list"
        # assert fav_list_response.data['remove'] == 0, "Unexpected item removal"
        # assert fav_list_response.data['switch'] == 0, "Unexpected switch in favorite list"

        self.navbar = NavBar(self.driver)
        self.navbar.navigate_to_fav_list()
        time.sleep(10)

