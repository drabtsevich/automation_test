from locators.swagLabs_locators import SwagLabsLocators

class SwagLabsLoginPage:
    URL = "https://www.saucedemo.com/"

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(self.URL)

    def login(self, username, password):
        self.page.locator(SwagLabsLocators.LOGIN_USERNAME).fill(username)
        self.page.locator(SwagLabsLocators.LOGIN_PASSWORD).fill(password)
        self.page.locator(SwagLabsLocators.LOGIN_BUTTON).click()        