from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.browser.base_page import BasePage


class CartPopUp(BasePage):

    CART_LOCATOR = "//span[text()='לסל הקניות']"

    def __init__(self, driver):
        super().__init__(driver)

    def click_go_to_cart(self):
        wait = WebDriverWait(self._driver, 20)
        search_text_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.CART_LOCATOR)))
        search_text_button.click()
