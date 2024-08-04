from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.browser.base_page import BasePage


class FavPage(BasePage):
    PRODUCT_NAME_LOC = "//li[1]//div[@class='product_content']/div[2]//a"

    def __init__(self, driver):
        super().__init__(driver)

    def get_product_name(self):
        wait = WebDriverWait(self._driver, 10)
        product_name = wait.until(EC.element_to_be_clickable((By.XPATH, self.PRODUCT_NAME_LOC)))
        return product_name.text()
