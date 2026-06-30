import allure

from locators.locators import PagesLocatosrs


class ItemPage:
    
    def __init__(self, page):
        self.page = page

    @allure.step("Add product '{product_name}' to cart")
    def add_to_cart(self, product_name: str):
        self.page.locator(
            PagesLocatosrs.ADD_TO_CART_BUTTON
            ).click()

    @allure.step("Remove product '{product_name}' from cart")
    def remove_from_cart(self, product_name: str):
        self.page.locator(
            PagesLocatosrs.REMOVE_FROM_CART_BUTTON
        ).click()

    