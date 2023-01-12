# Minimal Python (Pytest + Selenium) Page Object Model

Tests purchase process on https://www.saucedemo.com

## Test steps:
### Log in to the service
![](./images/login_page.png)

### Build a cart
Provide just the item names as list of strings, test suite will count actual cart value. Check if number of items is displayed on the button in the top right corner.
![](./images/inventory_page.png)

### Make sure the cart is built successfully
Check if the names and prices are correct.
![](./images/cart_page.png)

### Checkout
Fill the form and proceed with the purchase.
![](./images/checkout_page.png)

### Purchase overview
Make sure that the total amount to be paid is equal to the sum of all chosen items.
![](./images/overview_page.png)

### Finish page
Check if "thank you" message is displayed. Use "go back home" button.
![](./images/finish_page.png)