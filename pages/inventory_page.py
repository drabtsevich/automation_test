import allure

from locators.locators import PagesLocatosrs


class InventoryPage:

    def __init__(self, page):
        self.page = page

    @allure.step("Add product '{product_name}' to cart")
    def add_to_cart(self, product_name: str):
        self.page.locator(
            PagesLocatosrs.PRODUCTS[product_name]
        ).click()

    @allure.step("Open shopping cart")
    def open_cart(self):
        self.page.locator(
            PagesLocatosrs.CART_LINK
        ).click()

    @allure.step("Open item '{product_name}' page")
    def open_item_page(self, product_name: str):
        self.page.locator(
            PagesLocatosrs.PRODUCTS[product_name]
        ).click()