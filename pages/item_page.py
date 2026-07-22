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

    @allure.step("Check add-to-cart button is visible")
    def is_add_to_cart_button_visible(self):
        return self.page.locator(
            PagesLocatosrs.ADD_TO_CART_BUTTON
            ).is_visible()

    @allure.step("Check remove button is visible")
    def is_remove_button_visible(self):
        return self.page.locator(
            PagesLocatosrs.REMOVE_FROM_CART_BUTTON
            ).is_visible()
