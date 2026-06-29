import allure

from locators.swagLabs_locators import SwagLabsLocators


class SwagLabsInventoryPage:

    def __init__(self, page):
        self.page = page

    @allure.step("Add product '{product_name}' to cart")
    def add_to_cart(self, product_name: str):
        self.page.locator(
            SwagLabsLocators.products[product_name]
        ).click()

    @allure.step("Open shopping cart")
    def open_cart(self):
        self.page.locator(
            SwagLabsLocators.CART_LINK
        ).click()

    @allure.step("Get cart badge count")
    def get_cart_count(self):
        return self.page.locator(
            SwagLabsLocators.CART_BADGE
        ).text_content()