import allure

from locators.mobile_locators import MobileLocators
from pages_mobile.base_screen import BaseScreen


class CartScreen(BaseScreen):

    @allure.step("Check product '{product_name}' is in cart")
    def has_product(self, product_name):
        return self.is_visible(MobileLocators.text(product_name))

    @allure.step("Check cart total shows '{count}' items")
    def has_item_count(self, count):
        return self.is_visible(MobileLocators.text(f"{count} Items"))

    @allure.step("Remove item from cart")
    def remove_item(self):
        self.tap(MobileLocators.REMOVE_ITEM_BUTTON)

    @allure.step("Check cart is empty")
    def is_empty(self):
        return self.is_visible(MobileLocators.CART_EMPTY_TITLE)
