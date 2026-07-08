import allure

from locators.locators import PagesLocatosrs
from pages.base import BasePage


class ItemPage(BasePage):
    
    def __init__(self, page):
        self.page = page

    @allure.step("Add product '{product_name}' to cart")
    def add_to_cart(self, product_name: str):
        self.page.locator(
            PagesLocatosrs.ADD_TO_CART_BUTTON
            ).click()

    @allure.step("Remove product from cart")
    def remove_from_cart(self):
        self.page.locator(
            PagesLocatosrs.REMOVE_FROM_CART_BUTTON
            ).click()

    @allure.step("Cart is empty")
    def cart_is_empty(self):
        return self.page.locator(
            PagesLocatosrs.CART_BADGE
            ).is_visible()

    