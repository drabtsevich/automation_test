from locators.locators import PagesLocatosrs
import allure

class LoginPage:
    URL = "https://www.saucedemo.com/"

    def __init__(self, page):
        self.page = page

    @allure.step("Open Swag Labs login page")
    def open(self):
        self.page.goto(self.URL)

    @allure.step("Login to Swag Labs")
    def login(self, username, password):
        self.page.locator(PagesLocatosrs.LOGIN_USERNAME).fill(username)
        self.page.locator(PagesLocatosrs.LOGIN_PASSWORD).fill(password)
        self.page.locator(PagesLocatosrs.LOGIN_BUTTON).click()        