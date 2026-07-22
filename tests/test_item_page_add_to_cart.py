from pages.item_page import ItemPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
import allure


@allure.feature("Item Page")
@allure.story("Add product to cart")
@allure.title("User can add Sauce Labs Bolt T-Shirt to cart")
def test_add_to_cart_from_item_page(page, users, inventory_data):

    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    item_page = ItemPage(page)

    user = users["valid_user"]

    login_page.open()
    login_page.login(
        user["username"],
        user["password"]
    )
    inventory_page.open_item_page(inventory_data["item_name_2"])
    assert "inventory-item.html" in page.url
    assert item_page.cart_is_empty()
    assert item_page.is_add_to_cart_button_visible()

    item_page.add_to_cart(inventory_data["item_name_2"])

    assert inventory_page.get_cart_count() == "1"
    assert item_page.is_remove_button_visible()
