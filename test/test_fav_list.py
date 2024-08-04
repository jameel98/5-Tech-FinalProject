import unittest
from auth.auth_setup import Auth
from infra.api.api_wrapper import APIWrapper
from infra.browser.browser_wrapper import BrowserWrapper
from logic.api.request.fav_list_request import APIFavList
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

    def test_login_successfully(self):
        response = self.fav_list.add_item_to_fav_list()
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["action"], "success")

        self.navbar = NavBar(self.driver)
        self.navbar.navigate_to_fav_list()


