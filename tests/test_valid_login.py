import allure

from pages.login_page import LoginPage


@allure.feature("Login")
@allure.story("Valid login attempt")
@allure.title("User can login with valid credentials")

def test_valid_login(page, users):
    user = users["valid_user"]

    login_page = LoginPage(page)

    login_page.open()
    login_page.login(user["username"], user["password"])
    assert page.url == "https://www.saucedemo.com/inventory.html"
