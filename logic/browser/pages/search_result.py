from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.browser.base_page import BasePage


class SearchResult(BasePage):

    LAST_CHANCE_LOCATOR = "//li//div[@class='visual_stampa']/div/span"
    PRODUCT_NAME_LOCATOR = "//div[@class='product_name']/div/a"
    NO_RESULT_MESSAGE_LOCATOR = "//div[@class='message notice']/div"

    def __init__(self, driver):
        super().__init__(driver)

    def get_element_last_chance_attribute(self):
        wait = WebDriverWait(self._driver, 10)
        last_chance = wait.until(EC.presence_of_all_elements_located((By.XPATH, self.LAST_CHANCE_LOCATOR)))
        return last_chance[1].text

    def get_item_fav_button_locator(self, index):
        """Generate the XPath locator for the item's fav button based on its index."""
        return f'//li[{index}]//div[@class="product_wishlist"]/div/a'

    def get_item_cart_button_locator(self, index):
        """Generate the XPath locator for the item's fav button based on its index."""
        return f'//li[{index}]//button[@title="הוספה לסל"]'

    def click_add_to_fav(self, index):
        wait = WebDriverWait(self._driver, 10)
        fav_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.get_item_fav_button_locator(index))))
        fav_button.click()

    def get_element_id(self, index):
        wait = WebDriverWait(self._driver, 10)
        fav_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.get_item_fav_button_locator(index))))
        product_id = fav_button.get_attribute('product_id')
        return product_id

    def get_element_name(self):
        wait = WebDriverWait(self._driver, 10)
        name = wait.until(EC.presence_of_element_located((By.XPATH, self.PRODUCT_NAME_LOCATOR)))
        return name.text

    def get_search_message(self):
        wait = WebDriverWait(self._driver, 10)
        message = wait.until(EC.presence_of_element_located((By.XPATH, self.NO_RESULT_MESSAGE_LOCATOR)))
        return message.text

    def click_add_to_cart(self, index):
        wait = WebDriverWait(self._driver, 10)
        fav_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.get_item_cart_button_locator(index))))
        fav_button.click()
