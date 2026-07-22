import allure

from locators.locators import PagesLocatosrs
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
    assert not page.locator(PagesLocatosrs.ERROR_MESSAGE).is_visible()
    assert page.locator(PagesLocatosrs.INVENTORY_ITEM).first.is_visible()
    assert not page.locator(PagesLocatosrs.CART_BADGE).is_visible()
