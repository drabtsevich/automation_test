from pages.swagLabs_login_page import SwagLabsLoginPage
import json

def load_users():
    with open("test_data/users.json") as file:
        return json.load(file)

def test_swagLabs_login(page):
    users = load_users()
    user = users["valid_user"]

    swagLabs_login_page = SwagLabsLoginPage(page)

    swagLabs_login_page.open()
    swagLabs_login_page.login(user["username"], user["password"])
    assert page.url == "https://www.saucedemo.com/inventory.html"
