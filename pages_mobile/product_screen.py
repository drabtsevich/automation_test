import allure

from locators.mobile_locators import MobileLocators
from pages_mobile.base_screen import BaseScreen


class ProductScreen(BaseScreen):

    @allure.step("Check product '{product_name}' is shown")
    def is_product_shown(self, product_name):
        return self.is_visible(MobileLocators.text(product_name))

    @allure.step("Get product price")
    def get_price(self):
        return self.find(MobileLocators.PRODUCT_PRICE).get_attribute("value")

    @allure.step("Get 'Add To Cart' button accessibility label")
    def get_add_to_cart_label(self):
        return self.get_label(MobileLocators.ADD_TO_CART_BUTTON)

    @allure.step("Add product to cart")
    def add_to_cart(self):
        self.tap(MobileLocators.ADD_TO_CART_BUTTON)
