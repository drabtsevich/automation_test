from appium.webdriver.common.appiumby import AppiumBy


class MobileLocators:
    CATALOG_TAB = (AppiumBy.ACCESSIBILITY_ID, "Catalog-tab-item")
    CART_TAB = (AppiumBy.ACCESSIBILITY_ID, "Cart-tab-item")
    MORE_TAB = (AppiumBy.ACCESSIBILITY_ID, "More-tab-item")
    LOGOUT_MENU_ITEM = (AppiumBy.ACCESSIBILITY_ID, "LogOut-menu-item")

    # Login screen. "Login" is both the title and the button, so match by type.
    LOGIN_USERNAME = (AppiumBy.CLASS_NAME, "XCUIElementTypeTextField")
    LOGIN_PASSWORD = (AppiumBy.CLASS_NAME, "XCUIElementTypeSecureTextField")
    LOGIN_BUTTON = (AppiumBy.IOS_PREDICATE, "type == 'XCUIElementTypeButton' AND name == 'Login'")
    ALERT_OK_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "OK")

    PRODUCT_NAME = (AppiumBy.ACCESSIBILITY_ID, "Product Name")
    PRODUCT_PRICE = (AppiumBy.ACCESSIBILITY_ID, "Price")
    ADD_TO_CART_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "AddToCart")

    REMOVE_ITEM_BUTTON = (AppiumBy.IOS_PREDICATE, "type == 'XCUIElementTypeButton' AND name == 'Remove Item'")
    CART_EMPTY_TITLE = (AppiumBy.ACCESSIBILITY_ID, "No Items")
    PROCEED_TO_CHECKOUT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "ProceedToCheckout")

    @staticmethod
    def login_user_shortcut(username):
        return (AppiumBy.IOS_PREDICATE, f"type == 'XCUIElementTypeButton' AND name == '{username}'")

    @staticmethod
    def catalog_product(product_name):
        # Every catalog title has name 'Product Name'; the product's name is its label.
        return (AppiumBy.IOS_PREDICATE, f"name == 'Product Name' AND label == '{product_name}'")

    @staticmethod
    def text(value):
        return (AppiumBy.ACCESSIBILITY_ID, value)
