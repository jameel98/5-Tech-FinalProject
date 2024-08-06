from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.browser.base_page import BasePage


class SearchResult(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @staticmethod
    def get_item_fav_button_locator(index):
        """Generate the XPath locator for the item's fav button based on its index."""
        return f'//li[{index}]//div[@class="product_wishlist"]/div/a'

    def click_add_to_fav(self, index):
        wait = WebDriverWait(self._driver, 10)
        fav_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.get_item_fav_button_locator(index))))
        fav_button.click()

    def get_element_id(self, index):
        wait = WebDriverWait(self._driver, 10)
        fav_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.get_item_fav_button_locator(index))))
        product_id = fav_button.get_attribute('product_id')
        return product_id
