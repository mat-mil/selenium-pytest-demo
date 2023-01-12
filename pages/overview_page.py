from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.finish_page import FinishPage


class OverviewPage(BasePage):
    BUTTON_FINISH = (By.ID, "finish")

    def get_total_amount_to_be_paid(self) -> float:
        text = self.driver.find_element(By.CLASS_NAME, "summary_subtotal_label").text
        amount = text[text.find("$") :]
        return round(float(amount.replace("$", "")), 2)

    def finish_order(self) -> FinishPage:
        self.click(self.BUTTON_FINISH)
        return FinishPage(self.driver)
