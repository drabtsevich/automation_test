import allure

from locators.mobile_locators import MobileLocators
from pages_mobile.base_screen import BaseScreen


class LoginScreen(BaseScreen):

    @allure.step("Log in as '{username}' using the user shortcut")
    def login_with_shortcut(self, username):
        # The shortcut fills both fields without raising the keyboard, which
        # would otherwise cover the Login button.
        self.tap(MobileLocators.login_user_shortcut(username))
        self.tap(MobileLocators.LOGIN_BUTTON)

    @allure.step("Submit the login form")
    def submit(self):
        self.tap(MobileLocators.LOGIN_BUTTON)

    @allure.step("Check login screen is visible")
    def is_open(self):
        return self.is_visible(MobileLocators.LOGIN_BUTTON)

    @allure.step("Get Login button accessibility label")
    def get_login_button_label(self):
        return self.get_label(MobileLocators.LOGIN_BUTTON)

    @allure.step("Get user shortcut '{username}' accessibility label")
    def get_user_shortcut_label(self, username):
        return self.get_label(MobileLocators.login_user_shortcut(username))

    @allure.step("Get username and password field accessibility labels")
    def get_field_labels(self):
        return {
            "username": self.get_label(MobileLocators.LOGIN_USERNAME),
            "password": self.get_label(MobileLocators.LOGIN_PASSWORD),
        }

    @allure.step("Check alert '{message}' is shown")
    def is_alert_shown(self, message):
        return self.is_visible(MobileLocators.text(message))

    @allure.step("Dismiss alert")
    def dismiss_alert(self):
        self.tap(MobileLocators.ALERT_OK_BUTTON)
