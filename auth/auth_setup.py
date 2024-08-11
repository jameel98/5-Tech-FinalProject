import logging

import requests
from infra.browser.browser_wrapper import BrowserWrapper


class Auth:
    def __init__(self, driver):
        """
        auth to make login via api and save cookies in the driver
        :param driver:
        """
        self.logger = logging.getLogger(__name__)  # Initialize logger for this class
        self.driver = driver
        self.browser_wrapper = BrowserWrapper()
        self.config = self.browser_wrapper.config
        self.api_urls = self.browser_wrapper.api_urls
        self.user_login = self.browser_wrapper.user_login
        self.session = None
        self.cookies = None

    def start_session(self):
        """ use session because he is better in managing cookies"""
        self.logger.info(f'start session.')
        self.session = requests.Session()

    def login_via_api(self):
        """send login request and validate login successfully"""
        self.logger.info(f'start login proccess.')
        login_api_url = self.api_urls["login"]
        login_payload = self.user_login["payload2"]
        login_headers = self.user_login["headers"]
        # Perform login via API
        login_response = self.session.post(url=login_api_url, headers=login_headers, data=login_payload)
        print("Response Status Code:", login_response.status_code)
        print("Response Content:", login_response.content)
        if login_response.status_code == 200:
            response_json = login_response.json()
            print("Response JSON:", response_json)
            if response_json.get("message") == "נכנסת בהצלחה.":
                print("Login via API successful.")
            else:
                print("Login via API failed. Reason:", response_json.get("message"))
        else:
            print("Login via API failed. HTTP Status Code:", login_response.status_code)

    def save_cookies(self):
        """get the cookies from session"""
        self.logger.info(f'save cookies.')
        self.cookies = self.session.cookies.get_dict()

    def set_cookies(self):
        """add cookies to the browser"""
        self.logger.info(f'add cookie to the driver.')
        if self.cookies:
            for cookie_name, cookie_value in self.cookies.items():
                self.driver.add_cookie({"name": cookie_name, "value": cookie_value, "domain": ".foxhome.co.il"})
            print("Cookies set in the browser.")
        else:
            print("No cookies to set.")

    def set_local_storage(self, key, value):
        self.logger.info(f'set local storage.')
        self.driver.execute_script(f"window.localStorage.setItem('{key}', '{value}')")

    def refresh_driver(self):
        self.driver.refresh()

    def login_via_api_save_cookies(self):
        self.start_session()
        self.login_via_api()
        self.save_cookies()
