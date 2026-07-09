from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import allure


@allure.feature("Shopping Cart")
@allure.story("Remove product")
@allure.title("User can remove Backpack from cart on the inventory page")
def test_remove_from_cart_from_inventory(page, users, inventory_data):

    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    user = users["valid_user"]

    login_page.open()
    login_page.login(
        user["username"],
        user["password"]
    )

    inventory_page.add_to_cart(inventory_data["item_name"])
    assert inventory_page.get_cart_count() == "1"

    inventory_page.remove_from_cart(inventory_data["item_name"])
    assert inventory_page.cart_is_empty()
