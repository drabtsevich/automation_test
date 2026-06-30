class PagesLocatosrs:
    LOGIN_USERNAME = "id=user-name"
    LOGIN_PASSWORD = "id=password"
    LOGIN_BUTTON = "id=login-button"
    INVENTORY_ITEM = "[class='inventory_item_name']"
    CHECKOUT_BUTTON = "id=checkout"
    CART_LINK = "[class=shopping_cart_link]"
    CART_BADGE = "[class='shopping_cart_badge']"
    PRODUCTS = {
            "Sauce Labs Backpack": "#add-to-cart-sauce-labs-backpack",
            "Sauce Labs Bike Light": "#add-to-cart-sauce-labs-bike-light",
            "Sauce Labs Bolt T-Shirt": "#add-to-cart-sauce-labs-bolt-t-shirt",
        }
    ADD_TO_CART_BUTTON = "button[id^='add-to-cart']"
    REMOVE_FROM_CART_BUTTON = "button[id^='remove-from-cart']"