import xml.etree.ElementTree as ET

import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators.mobile_locators import MobileLocators

INTERACTIVE_TYPES = {
    "XCUIElementTypeButton",
    "XCUIElementTypeTextField",
    "XCUIElementTypeSecureTextField",
}


def is_tab_bar_button(element):
    return (element["name"] or "").endswith("-tab-item")


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

    def get_label(self, locator):
        """Accessibility label: the text VoiceOver reads for the element."""
        return self.find(locator).get_attribute("label")

    @allure.step("Collect visible buttons and text fields")
    def interactive_elements(self):
        # One page-source call instead of an attribute request per element.
        root = ET.fromstring(self.driver.page_source)
        return [
            {"type": el.tag, "name": el.get("name"), "label": el.get("label")}
            for el in root.iter()
            if el.tag in INTERACTIVE_TYPES and el.get("visible") == "true"
        ]

    def tab_bar_buttons(self):
        return [el for el in self.interactive_elements() if is_tab_bar_button(el)]

    def screen_content_elements(self):
        """Buttons and fields of the current screen, without the shared tab bar."""
        return [el for el in self.interactive_elements() if not is_tab_bar_button(el)]

    def open_catalog(self):
        self.tap(MobileLocators.CATALOG_TAB)

    def open_cart(self):
        self.tap(MobileLocators.CART_TAB)

    def open_more_menu(self):
        self.tap(MobileLocators.MORE_TAB)
        self.find(MobileLocators.LOGOUT_MENU_ITEM)

    def logout(self):
        self.open_more_menu()
        self.tap(MobileLocators.LOGOUT_MENU_ITEM)
