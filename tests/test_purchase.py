import pytest

first_cart = (["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt"], 45.98)
second_cart = (["Sauce Labs Bike Light", "Sauce Labs Fleece Jacket", "Sauce Labs Onesie"], 67.97)


@pytest.mark.parametrize("items, expected_amount", [first_cart, second_cart])
def test_purchase(sign_in_reg_user, items, expected_amount):
    inventory_page = sign_in_reg_user
    actual_amount = inventory_page.build_cart(items)
    assert expected_amount == actual_amount
    assert inventory_page.get_cart_items_count() == len(items)

    cart_page = inventory_page.nav_to_cart_page()
    cart_items = cart_page.get_cart_items()
    assert list(cart_items.keys()) == items
    assert sum(cart_items.values()) in (expected_amount, actual_amount)

    checkout_page = cart_page.nav_to_checkout_page()
    overview_page = checkout_page.checkout("Maximus Decimus", "Automatus", "5-37 Rome")
    assert overview_page.get_total_amount_to_be_paid() in (expected_amount, actual_amount)

    finish_page = overview_page.finish_order()
    assert finish_page.wait_for_visibility(finish_page.HEADER_COMPLETE)
    finish_page.go_back_home()
