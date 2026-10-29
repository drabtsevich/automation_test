import allure

from locators.mobile_locators import MobileLocators
from pages_mobile.base_screen import BaseScreen


class CatalogScreen(BaseScreen):

    @allure.step("Check catalog is visible")
    def is_open(self):
        return self.is_visible(MobileLocators.PRODUCT_NAME)

    @allure.step("Open product '{product_name}'")
    def open_product(self, product_name):
        self.tap(MobileLocators.catalog_product(product_name))
