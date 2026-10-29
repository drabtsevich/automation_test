import allure
import pytest

from pages_mobile.base_screen import BaseScreen
from pages_mobile.cart_screen import CartScreen
from pages_mobile.catalog_screen import CatalogScreen
from pages_mobile.login_screen import LoginScreen
from pages_mobile.product_screen import ProductScreen

# Labels VoiceOver would read that mean nothing to a user: the generic "Button"
# and image asset names such as "AddPlus Icons".
GENERIC_LABELS = {"Button"}
ASSET_NAME_SUFFIX = " Icons"


def is_readable(label):
    return bool(label) and label not in GENERIC_LABELS and not label.endswith(ASSET_NAME_SUFFIX)


def assert_all_readable(elements):
    bad = [f"{el['name']!r} (label {el['label']!r})" for el in elements if not is_readable(el["label"])]
    assert not bad, "Missing or unreadable labels: " + ", ".join(bad)


@allure.feature("Mobile Accessibility")
@allure.story("Button labels")
@allure.title("Product screen 'Add To Cart' button has a readable label")
def test_mobile_add_to_cart_button_label(driver, product):
    catalog_screen = CatalogScreen(driver)
    product_screen = ProductScreen(driver)

    catalog_screen.open_product(product["name"])

    assert product_screen.get_add_to_cart_label() == "Add To Cart"


@allure.feature("Mobile Accessibility")
@allure.story("Button labels")
@allure.title("Cart screen buttons have readable labels")
def test_mobile_cart_button_labels(driver, product):
    catalog_screen = CatalogScreen(driver)
    product_screen = ProductScreen(driver)
    cart_screen = CartScreen(driver)

    catalog_screen.open_product(product["name"])
    product_screen.add_to_cart()
    product_screen.open_cart()

    assert cart_screen.get_remove_item_label() == "Remove Item"
    assert cart_screen.get_checkout_label() == "Proceed To Checkout"


@allure.feature("Mobile Accessibility")
@allure.story("Button labels")
@allure.title("Login screen buttons have readable labels")
def test_mobile_login_button_labels(driver, mobile_user):
    login_screen = LoginScreen(driver)

    login_screen.logout()

    assert login_screen.get_login_button_label() == "Login"
    assert login_screen.get_user_shortcut_label(mobile_user["username"]) == mobile_user["username"]


# Known accessibility bugs in My Demo App 2.3.0. strict=True turns a fix into a
# failure (XPASS), as a reminder to remove the marker and keep the check.


@allure.feature("Mobile Accessibility")
@allure.story("Field labels")
@allure.title("Login text fields have accessibility labels")
@pytest.mark.xfail(strict=True, raises=AssertionError, reason="App bug: username and password fields have an empty label")
def test_mobile_login_field_labels(driver):
    login_screen = LoginScreen(driver)

    login_screen.logout()
    labels = login_screen.get_field_labels()

    assert is_readable(labels["username"]), f"Username field label: {labels['username']!r}"
    assert is_readable(labels["password"]), f"Password field label: {labels['password']!r}"


@allure.feature("Mobile Accessibility")
@allure.story("Button labels")
@allure.title("Tab bar buttons have accessibility labels")
@pytest.mark.xfail(strict=True, raises=AssertionError, reason="App bug: Catalog, Cart and More tabs have no label")
def test_mobile_tab_bar_labels(driver):
    catalog_screen = CatalogScreen(driver)

    assert catalog_screen.is_open()
    buttons = catalog_screen.tab_bar_buttons()

    assert len(buttons) == 3
    assert_all_readable(buttons)


@allure.feature("Mobile Accessibility")
@allure.story("Button labels")
@allure.title("More menu items have accessibility labels")
@pytest.mark.xfail(strict=True, raises=AssertionError, reason="App bug: menu items have no label")
def test_mobile_more_menu_labels(driver):
    screen = BaseScreen(driver)

    screen.open_more_menu()
    menu_items = screen.screen_content_elements()

    assert menu_items
    assert_all_readable(menu_items)


@allure.feature("Mobile Accessibility")
@allure.story("Button labels")
@allure.title("Product screen icon buttons have readable labels")
@pytest.mark.xfail(strict=True, raises=AssertionError, reason="App bug: icon buttons are labeled with asset names, e.g. 'AddPlus Icons'")
def test_mobile_product_icon_button_labels(driver, product):
    catalog_screen = CatalogScreen(driver)
    product_screen = ProductScreen(driver)

    catalog_screen.open_product(product["name"])
    product_screen.get_add_to_cart_label()  # wait for the screen to render
    buttons = product_screen.screen_content_elements()

    assert_all_readable(buttons)
