from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.browser.base_page import BasePage


class NavBar(BasePage):
    LOGIN_BUTTON_LOC = '//div[@class="page_header_customer"]//a/span[text()="התחברות"]'
    WISH_LIST_LOC = "//div[@class='header_wishlist inline padding_l']//a"

    def __init__(self, driver):
        super().__init__(driver)

    def click_login(self):
        # Find and click the login button/link
        wait = WebDriverWait(self._driver, 10)
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.LOGIN_BUTTON_LOC)))
        login_button.click()

    def navigate_to_fav_list(self):
        wait = WebDriverWait(self._driver, 10)
        wish_list_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.WISH_LIST_LOC)))
        wish_list_button.click()
