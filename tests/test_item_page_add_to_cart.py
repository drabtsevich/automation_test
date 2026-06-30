from pages.base import BasePage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
import json
import allure


def load_users():
    with open("test_data/users.json") as file:
        return json.load(file)
def load_inventory():
    with open("test_data/inventory_data.json") as file:
        return json.load(file)

@allure.feature("Item Page")
@allure.story("Add product to cart")
@allure.title("User can add Sauce Labs Bolt T-Shirt to cart")

def test_add_to_cart_from_item_page(page):

    users = load_users()
    user = users["valid_user"]

    item_name_2 = load_inventory()["inventoryPage"]["item_name_2"]


    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    base_page = BasePage(page)


    login_page.open()
    login_page.login(user["username"], user["password"])

    inventory_page.open_item_page(item_name_2)

    assert base_page.get_cart_count() == "1"
