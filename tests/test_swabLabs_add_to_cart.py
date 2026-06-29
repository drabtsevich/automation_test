from pages.swagLabs_login_page import SwagLabsLoginPage
from pages.swabLabs_inventory_page import SwagLabsInventoryPage
from locators.swagLabs_locators import SwagLabsLocators
import json
import allure


def load_users():
    with open("test_data/users.json") as file:
        return json.load(file)
def load_inventory():
    with open("test_data/inventory_data.json") as file:
        return json.load(file)

@allure.feature("Shopping Cart")
@allure.story("Add product")
@allure.title("User can add Backpack to cart")
def test_add_to_cart(page):

    users = load_users()
    user = users["valid_user"]

    item_name = load_inventory()["inventoryPage"]["item_name"]


    swagLabs_login_page = SwagLabsLoginPage(page)
    swagLabs_inventory_page = SwagLabsInventoryPage(page)


    swagLabs_login_page.open()
    swagLabs_login_page.login(user["username"], user["password"])

    swagLabs_inventory_page.add_to_cart(item_name)

    assert swagLabs_inventory_page.get_cart_count() == "1"

    swagLabs_inventory_page.open_cart()

    assert page.locator(SwagLabsLocators.INVENTORY_ITEM).is_visible()
    assert page.locator(SwagLabsLocators.INVENTORY_ITEM).text_content() == item_name
