import allure

from locators.locators import PagesLocators
from pages.base import BasePage


class CartPage(BasePage):

    @allure.step("Visible cart item count")
    def is_product_visible(self):
        return self.page.locator(PagesLocators.INVENTORY_ITEM).is_visible()

    @allure.step("Get product name")
    def get_product_name(self):
        return self.page.locator(PagesLocators.INVENTORY_ITEM).text_content()

    