from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.cart_page import CartPage


class InventoryPage(BasePage):
    BUTTON_CART = (By.ID, "shopping_cart_container")

    def _get_all_inventory_items(self) -> dict:
        all_items_elements = self.driver.find_elements(By.CSS_SELECTOR, ".inventory_item")
        # build a dict where the key is equal to name of the item and the value is item web element
        inventory_items = {
            item.find_element(By.CSS_SELECTOR, ".inventory_item_name").text: item for item in all_items_elements
        }
        return inventory_items

    def build_cart(self, item_names: list[str]) -> float:
        cart_items = self._get_all_inventory_items()
        cart_value = 0
        for item in item_names:
            if item in cart_items.keys():
                cart_items[item].find_element(By.CSS_SELECTOR, ".btn.btn_primary.btn_small.btn_inventory").click()
                item_price = float(
                    cart_items[item].find_element(By.CLASS_NAME, "inventory_item_price").text.replace("$", ""),
                )
                cart_value += round(item_price, 2)
        return cart_value

    def get_cart_items_count(self) -> int:
        return int(self.driver.find_element(*self.BUTTON_CART).text)

    def nav_to_cart_page(self) -> CartPage:
        self.click(self.BUTTON_CART)
        return CartPage(self.driver)
