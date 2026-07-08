import allure

from locators.locators import PagesLocatosrs
from pages.base import BasePage


class CartPage(BasePage):

    def __init__(self, page):
        self.page = page

    @allure.step("Visible cart item count")
    def is_product_visible(self):
        return self.page.locator(PagesLocatosrs.INVENTORY_ITEM).is_visible()

    @allure.step("Get product name")
    def get_product_name(self):
        return self.page.locator(PagesLocatosrs.INVENTORY_ITEM).text_content()

    