import allure
from locators.locators import PagesLocatosrs
from pages.login_page import LoginPage

@allure.feature("Login")
@allure.story("Invalid login attempt")
@allure.title("User cannot login with invalid credentials")
def test_invalid_login(page, users):
    user = users["invalid_user"]

    login_page = LoginPage(page)
    login_page.open()
    login_page.login(user["username"], user["password"])

    assert page.locator(PagesLocatosrs.ERROR_MESSAGE).inner_text() == (
        "Epic sadface: Username and password do not match any user in this service"
    )