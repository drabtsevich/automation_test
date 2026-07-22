import allure
import pytest

from locators.locators import PagesLocatosrs
from pages.login_page import LoginPage


@allure.feature("Login")
@allure.story("Invalid login attempt")
@pytest.mark.parametrize(
    "user_key, expected_error",
    [
        (
            "invalid_user",
            "Epic sadface: Username and password do not match any user in this service",
        ),
        (
            "locked_out_user",
            "Epic sadface: Sorry, this user has been locked out.",
        ),
    ],
)
@allure.title("User cannot login with invalid credentials")
def test_invalid_login(page, users, user_key, expected_error):
    user = users[user_key]

    login_page = LoginPage(page)
    login_page.open()
    login_page.login(user["username"], user["password"])

    error_message = page.locator(PagesLocatosrs.ERROR_MESSAGE)

    assert error_message.is_visible()
    assert error_message.inner_text() == expected_error
    assert page.url == login_page.URL
