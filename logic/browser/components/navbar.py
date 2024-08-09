import logging

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.browser.base_page import BasePage


class NavBar(BasePage):
    LOGIN_BUTTON_LOC = '//div[@class="page_header_customer"]//a/span[text()="התחברות"]'
    WISH_LIST_LOC = "//div[@class='header_wishlist inline padding_l']//a"
    CART_LIST_LOC = "//div[@class='page_header_minicart']//a"
    SEARCH_BUTTON_LOC = "//div[@class='page_header_search']"
    SEARCH_TEXT_INPUT_LOC = "//input[@id='header-search-input']"

    def __init__(self, driver):
        super().__init__(driver)
        self.actions = ActionChains(self._driver)
        self.logger = logging.getLogger(__name__)  # Initialize logger for this class

    def click_login(self):
        # Find and click the login button/link
        wait = WebDriverWait(self._driver, 10)
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.LOGIN_BUTTON_LOC)))
        login_button.click()

    def navigate_to_fav_list(self):
        wait = WebDriverWait(self._driver, 10)
        wish_list_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.WISH_LIST_LOC)))
        wish_list_button.click()

    def navigate_to_cart_list(self):
        wait = WebDriverWait(self._driver, 10)
        wish_list_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.CART_LIST_LOC)))
        wish_list_button.click()

    def click_search_text_button(self):
        """Clicks on the search text button in the navigation bar."""
        try:
            wait = WebDriverWait(self._driver, 20)
            search_text_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.SEARCH_BUTTON_LOC)))
            search_text_button.click()
        except Exception as e:
            self.logger.error(f"Failed to click search text button: {e}")
            raise

    def get_search_text_input(self):
        """Returns the search text input element."""
        try:
            wait = WebDriverWait(self._driver, 20)
            return wait.until(EC.element_to_be_clickable((By.XPATH, self.SEARCH_TEXT_INPUT_LOC)))
        except Exception as e:
            self.logger.error(f"Failed to get search text input: {e}")
            raise

    def search_product_by_name(self, name):

        self.click_search_text_button()
        text_input = self.get_search_text_input()
        text_input.send_keys(name)
        text_input.send_keys(Keys.ENTER)


    def click_on_category(self, category):
        """Clicks on an outer category link."""
        try:
            wait = WebDriverWait(self._driver, 20)
            category_btn = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[@class='page-wrapper']//span[text()='{category}']")))
            category_btn.click()
        except Exception as e:
            self.logger.error(f"Failed to click on outer category '{category}': {e}")
            raise