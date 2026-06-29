
import allure

from pages.swagLabs_login_page import SwagLabsLoginPage
import json

def load_users():
    with open("test_data/users.json") as file:
        return json.load(file)

@allure.feature("Login")
@allure.story("Invalid login attempt")
@allure.title("User cannot login with invalid credentials")
def test_swagLabs_login(page):
    users = load_users()
    user = users["invalid_user"]

    swagLabs_login_page = SwagLabsLoginPage(page)

    swagLabs_login_page.open()
    swagLabs_login_page.login(user["username"], user["password"])
    assert page.locator("h3[data-test='error']").inner_text() == "Epic sadface: Username and password do not match any user in this service"    