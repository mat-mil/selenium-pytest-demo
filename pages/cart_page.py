from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.checkout_page import CheckoutPage


class CartPage(BasePage):
    BUTTON_CHECKOUT = (By.ID, "checkout")

    def get_cart_items(self) -> dict:
        cart_items_elements = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        # build a dict where the key is equal to name of the cart item and the value is equal to its price
        # fmt: off
        cart_items = {item.find_element(By.CSS_SELECTOR, ".inventory_item_name").text: \
            float(item.find_element(By.CSS_SELECTOR, ".inventory_item_price").text.replace("$", "")) \
            for item in cart_items_elements}
        # fmt: on
        return cart_items

    def nav_to_checkout_page(self) -> CheckoutPage:
        self.click(self.BUTTON_CHECKOUT)
        return CheckoutPage(self.driver)
