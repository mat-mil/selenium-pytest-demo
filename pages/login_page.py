from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    INPUT_LOGIN = (By.ID, "user-name")
    INPUT_PASSWORD = (By.ID, "password")
    BUTTON_LOGIN = (By.ID, "login-button")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.saucedemo.com/")

    def sign_in(self, username: str, password: str):
        self.send_keys(self.INPUT_LOGIN, username)
        self.send_keys(self.INPUT_PASSWORD, password)
        self.click(self.BUTTON_LOGIN)
