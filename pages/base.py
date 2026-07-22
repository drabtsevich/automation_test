import allure
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

from locators.locators import PagesLocators

class BasePage:
    def __init__(self, page):
        self.page = page

    @allure.step("Get cart badge count")
    def get_cart_count(self):
        badge = self.page.locator(PagesLocators.CART_BADGE)
        badge.wait_for(state="visible", timeout=5000)
        return badge.text_content()

    @allure.step("Cart is empty")
    def cart_is_empty(self):
        badge = self.page.locator(PagesLocators.CART_BADGE)
        try:
            badge.wait_for(state="hidden", timeout=5000)
            return True
        except PlaywrightTimeoutError:
            return False
