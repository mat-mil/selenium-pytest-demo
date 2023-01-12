from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self, driver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def wait_for_visibility(self, locator: tuple) -> WebElement:
        return self.wait.until(ec.visibility_of_element_located(locator))

    def click(self, locator: tuple) -> None:
        self.wait_for_visibility(locator).click()

    def send_keys(self, locator: tuple, keys: str) -> None:
        self.wait_for_visibility(locator).send_keys(keys)
