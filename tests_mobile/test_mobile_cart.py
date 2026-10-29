import allure

from pages_mobile.cart_screen import CartScreen
from pages_mobile.catalog_screen import CatalogScreen
from pages_mobile.product_screen import ProductScreen


@allure.feature("Mobile Cart")
@allure.story("Add product")
@allure.title("User can add Sauce Labs Backpack - Black to cart in the iOS app")
def test_mobile_add_to_cart(driver, product):
    catalog_screen = CatalogScreen(driver)
    product_screen = ProductScreen(driver)
    cart_screen = CartScreen(driver)

    catalog_screen.open_product(product["name"])

    assert product_screen.is_product_shown(product["name"])
    assert product_screen.get_price() == product["price"]

    product_screen.add_to_cart()
    product_screen.open_cart()

    assert cart_screen.has_product(product["name"])
    assert cart_screen.has_item_count(1)


@allure.feature("Mobile Cart")
@allure.story("Remove product")
@allure.title("User can remove Sauce Labs Backpack - Black from cart in the iOS app")
def test_mobile_remove_from_cart(driver, product):
    catalog_screen = CatalogScreen(driver)
    product_screen = ProductScreen(driver)
    cart_screen = CartScreen(driver)

    catalog_screen.open_product(product["name"])
    product_screen.add_to_cart()
    product_screen.open_cart()
    assert cart_screen.has_item_count(1)

    cart_screen.remove_item()

    assert cart_screen.is_empty()
