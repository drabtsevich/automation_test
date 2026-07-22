from locators.locators import PagesLocators
from playwright.sync_api import Error as PlaywrightError
import allure

class LoginPage:
    URL = "https://www.saucedemo.com/"
    OPEN_RETRIES = 3

    def __init__(self, page):
        self.page = page

    @allure.step("Open Swag Labs login page")
    def open(self):
        last_error = None
        for _ in range(self.OPEN_RETRIES):
            try:
                self.page.goto(self.URL)
                self.page.locator(PagesLocators.LOGIN_USERNAME).wait_for(
                    state="visible", timeout=10000
                )
                return
            except PlaywrightError as error:
                last_error = error
                self.page.wait_for_timeout(500)
        raise last_error

    @allure.step("Login to Swag Labs")
    def login(self, username, password):
        self.page.locator(PagesLocators.LOGIN_USERNAME).fill(username)
        self.page.locator(PagesLocators.LOGIN_PASSWORD).fill(password)
        self.page.locator(PagesLocators.LOGIN_BUTTON).click()        