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

    @allure.step("Cart is empty")
    def cart_is_empty(self):
        return not self.page.locator(
            PagesLocatosrs.CART_BADGE
            ).is_visible()
