import allure

from locators.locators import PagesLocatosrs

class BasePage:
    def __init__(self, page):
        self.page = page

    @allure.step("Get cart badge count")
    def get_cart_count(self):
        return self.page.locator(
            PagesLocatosrs.CART_BADGE
            ).text_content()