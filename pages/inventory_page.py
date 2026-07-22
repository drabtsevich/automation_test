import allure

from locators.locators import PagesLocatosrs
from pages.base import BasePage


class InventoryPage(BasePage):

    def __init__(self, page):
        self.page = page

    @allure.step("Add product '{product_name}' to cart")
    def add_to_cart(self, product_name: str):
        self.page.locator(
            PagesLocatosrs.ADD_TO_CART_BUTTONS[product_name]
        ).click()

    @allure.step("Remove product '{product_name}' from cart")
    def remove_from_cart(self, product_name: str):
        self.page.locator(
            PagesLocatosrs.REMOVE_FROM_CART_BUTTONS[product_name]
        ).click()

    @allure.step("Check '{product_name}' add-to-cart button is visible")
    def is_add_to_cart_button_visible(self, product_name: str):
        return self.page.locator(
            PagesLocatosrs.ADD_TO_CART_BUTTONS[product_name]
        ).is_visible()

    @allure.step("Check '{product_name}' remove button is visible")
    def is_remove_button_visible(self, product_name: str):
        return self.page.locator(
            PagesLocatosrs.REMOVE_FROM_CART_BUTTONS[product_name]
        ).is_visible()

    @allure.step("Open shopping cart")
    def open_cart(self):
        self.page.locator(
            PagesLocatosrs.CART_LINK
        ).click()

    @allure.step("Open item '{product_name}' page")
    def open_item_page(self, product_name: str):
        self.page.locator(
            PagesLocatosrs.PRODUCT_LINKS[product_name]
        ).click()