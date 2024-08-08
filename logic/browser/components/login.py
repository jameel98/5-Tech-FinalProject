from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.browser.base_page import BasePage
from infra.logger_setup import LogSetup


class Login(BasePage):
    EMAIL_INPUT_LOC = "//div[@class='foxhome-customer-login']//input[@name='email']"
    PASSWORD_INPUT_LOC = "//div[@class='foxhome-customer-login']//input[@name='password']"

    def __init__(self, driver):
        super().__init__(driver)

        wait = WebDriverWait(self._driver, 10)
        try:
            self.email_input = wait.until(EC.element_to_be_clickable((By.XPATH, self.EMAIL_INPUT_LOC)))
            self.password_input = wait.until(EC.element_to_be_clickable((By.XPATH, self.PASSWORD_INPUT_LOC)))

        except Exception as e:
            raise

    def fill_email_input(self, email):
        """
        this function fills the email input
        :param email: gets email input parameter and puts is in email field
        :return:
        """
        try:
            self.email_input.send_keys(email)
        except Exception as e:
            raise

    def fill_password_input(self, password):
        """
        this function fills the password input
        :param password: gets email input parameter and puts is in password field
        :return:
        """
        try:
            self.password_input.send_keys(password)
        except Exception as e:
            raise

    def click_enter(self):
        # Submit the login form
        self.password_input.send_keys(Keys.ENTER)

    def login_flow(self, email, password):
        """
        this is login flow function used to login, helpful
        to do all the login in one function
        :param email:
        :param password:
        :return:
        """
        try:
            self.fill_email_input(email)
            self.fill_password_input(password)
            self.click_enter()
        except Exception as e:
            raise
