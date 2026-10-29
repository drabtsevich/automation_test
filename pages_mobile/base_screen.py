from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators.mobile_locators import MobileLocators


class BaseScreen:
    def __init__(self, driver):
        self.driver = driver

    def find(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def tap(self, locator):
        self.find(locator).click()

    def is_visible(self, locator, timeout=5):
        try:
            self.find(locator, timeout)
            return True
        except TimeoutException:
            return False

    def open_catalog(self):
        self.tap(MobileLocators.CATALOG_TAB)

    def open_cart(self):
        self.tap(MobileLocators.CART_TAB)

    def logout(self):
        self.tap(MobileLocators.MORE_TAB)
        self.tap(MobileLocators.LOGOUT_MENU_ITEM)
