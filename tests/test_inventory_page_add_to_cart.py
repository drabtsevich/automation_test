from typing import Any

from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

import json
import allure



@allure.feature("Shopping Cart")
@allure.story("Add product")
@allure.title("User can add Backpack to cart")
def test_add_to_cart_from_inventory(page, users, inventory_data: Any):

    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    user = users["valid_user"]
    
    login_page.open()
    login_page.login(
        user["username"],
        user["password"]
        )

    assert inventory_page.cart_is_empty()
    assert inventory_page.is_add_to_cart_button_visible(inventory_data["item_name"])

    inventory_page.add_to_cart(inventory_data["item_name"])

    assert inventory_page.get_cart_count() == "1"
    assert inventory_page.is_remove_button_visible(inventory_data["item_name"])

    inventory_page.open_cart()

    assert cart_page.is_product_visible()
    assert cart_page.get_product_name() == inventory_data["item_name"]
