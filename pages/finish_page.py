from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class FinishPage(BasePage):
    HEADER_COMPLETE = (By.CLASS_NAME, "complete-header")
    BUTTON_BACK_HOME = (By.ID, "back-to-products")

    def go_back_home(self):
        self.click(self.BUTTON_BACK_HOME)
