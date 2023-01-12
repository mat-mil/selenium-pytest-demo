import pytest

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.fixture
def sign_in_reg_user(login_page: LoginPage) -> InventoryPage:
    login_page.sign_in("standard_user", "secret_sauce")
    return InventoryPage(login_page.driver)
