from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.overview_page import OverviewPage


class CheckoutPage(BasePage):
    INPUT_FIRST_NAME = (By.ID, "first-name")
    INPUT_LAST_NAME = (By.ID, "last-name")
    INPUT_POSTAL_CODE = (By.ID, "postal-code")
    BUTTON_CONTINUE = (By.ID, "continue")

    def checkout(self, first_name: str, last_name: str, postal_code: str) -> OverviewPage:
        self.send_keys(self.INPUT_FIRST_NAME, first_name)
        self.send_keys(self.INPUT_LAST_NAME, last_name)
        self.send_keys(self.INPUT_POSTAL_CODE, postal_code)
        self.click(self.BUTTON_CONTINUE)
        return OverviewPage(self.driver)
