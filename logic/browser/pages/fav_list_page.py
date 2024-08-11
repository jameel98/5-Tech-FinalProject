import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.browser.base_page import BasePage


class FavPage(BasePage):
    LIST_IS_EMPTY_LOCATOR = "//div[@class='message info empty']"
    FAV_BUTTON_LOCATOR = '//li//div[@class="product_wishlist"]/div/a'

    def __init__(self, driver):
        super().__init__(driver)

    def get_item_name_locator(self, index):
        """Generate the XPath locator for the item's fav button based on its index."""
        return f"//li[{index}]//div[@class='product_content']/div[2]//a"

    def get_product_name(self, index):
        wait = WebDriverWait(self._driver, 10)
        product_name = wait.until(EC.element_to_be_clickable((By.XPATH, self.get_item_name_locator(index))))
        return product_name.text()

    def get_item_fav_button_locator(self, index):
        """Generate the XPath locator for the item's fav button based on its index."""
        return f'//li[{index}]//div[@class="product_wishlist"]/div/a'

    def click_remove_from_fav(self, index):
        wait = WebDriverWait(self._driver, 10)
        fav_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.get_item_fav_button_locator(index))))
        fav_button.click()

    def get_element_id(self, index):
        wait = WebDriverWait(self._driver, 10)
        fav_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.get_item_fav_button_locator(index))))
        product_id = fav_button.get_attribute('product_id')
        return product_id

    def get_list_is_empty_message(self):
        wait = WebDriverWait(self._driver, 10)
        empy_list = wait.until(EC.presence_of_element_located((By.XPATH, self.LIST_IS_EMPTY_LOCATOR)))
        return empy_list.text

    def remove_all_elements(self):
        wait = WebDriverWait(self._driver, 10)
        try:
            fav_button_list = wait.until(EC.presence_of_all_elements_located((By.XPATH, self.FAV_BUTTON_LOCATOR)))
            if fav_button_list:
                for _ in range(len(fav_button_list)):
                    self.click_remove_from_fav(1)
                    time.sleep(1)  # Add a short delay to allow for any page updates
        except TimeoutException:
            print("Favorite list is already empty. No elements to remove.")
