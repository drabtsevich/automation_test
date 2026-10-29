import allure

from pages_mobile.catalog_screen import CatalogScreen
from pages_mobile.login_screen import LoginScreen


@allure.feature("Mobile Login")
@allure.story("Valid login attempt")
@allure.title("User can log in to the iOS app with valid credentials")
def test_mobile_login_valid(driver, mobile_user):
    login_screen = LoginScreen(driver)
    catalog_screen = CatalogScreen(driver)

    login_screen.logout()
    assert login_screen.is_open()

    login_screen.login_with_shortcut(mobile_user["username"])

    assert catalog_screen.is_open()


@allure.feature("Mobile Login")
@allure.story("Invalid login attempt")
@allure.title("User sees an error when logging in without a username")
def test_mobile_login_empty_username(driver):
    login_screen = LoginScreen(driver)

    login_screen.logout()
    login_screen.submit()

    assert login_screen.is_alert_shown("Username is required")

    login_screen.dismiss_alert()
    assert login_screen.is_open()
