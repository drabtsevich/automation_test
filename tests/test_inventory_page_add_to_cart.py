from pages.base import BasePage
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from locators.locators import PagesLocatosrs
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
def test_add_to_cart_from_inventory(page):

    users = load_users()
    user = users["valid_user"]

    item_name = load_inventory()["inventoryPage"]["item_name"]


    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    base_page = BasePage(page)



    login_page.open()
    login_page.login(user["username"], user["password"])

    inventory_page.add_to_cart(item_name)

    assert base_page.get_cart_count() == "1"

    inventory_page.open_cart()

    assert page.locator(PagesLocatosrs.INVENTORY_ITEM).is_visible()
    assert page.locator(PagesLocatosrs.INVENTORY_ITEM).text_content() == item_name
