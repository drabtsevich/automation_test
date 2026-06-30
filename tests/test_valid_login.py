import allure

from pages.login_page import LoginPage
import json

def load_users():
    with open("test_data/users.json") as file:
        return json.load(file)

@allure.feature("Login")
@allure.story("Valid login attempt")
@allure.title("User can login with valid credentials")

def test_valid_login(page):
    users = load_users()
    user = users["valid_user"]

    login_page = LoginPage(page)

    login_page.open()
    login_page.login(user["username"], user["password"])
    assert page.url == "https://www.saucedemo.com/inventory.html"
