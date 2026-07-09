class PagesLocatosrs:
    LOGIN_USERNAME = "id=user-name"
    LOGIN_PASSWORD = "id=password"
    ERROR_MESSAGE = "h3[data-test='error']"
    LOGIN_BUTTON = "id=login-button"
    INVENTORY_ITEM = "[class='inventory_item_name']"
    CHECKOUT_BUTTON = "id=checkout"
    CART_LINK = "[class=shopping_cart_link]"
    CART_BADGE = "[class='shopping_cart_badge']"
    PRODUCT_LINKS = {
        "Sauce Labs Backpack": 'text="Sauce Labs Backpack"',
        "Sauce Labs Bike Light": 'text="Sauce Labs Bike Light"',
        "Sauce Labs Bolt T-Shirt": 'text="Sauce Labs Bolt T-Shirt"',
    }

    ADD_TO_CART_BUTTONS = {
        "Sauce Labs Backpack": "#add-to-cart-sauce-labs-backpack",
        "Sauce Labs Bike Light": "#add-to-cart-sauce-labs-bike-light",
        "Sauce Labs Bolt T-Shirt": "#add-to-cart-sauce-labs-bolt-t-shirt",
    }
    ADD_TO_CART_BUTTON = "button[id^='add-to-cart']"
    REMOVE_FROM_CART_BUTTON = "id=remove"
    REMOVE_FROM_CART_BUTTONS = {
        "Sauce Labs Backpack": "#remove-sauce-labs-backpack",
        "Sauce Labs Bike Light": "#remove-sauce-labs-bike-light",
        "Sauce Labs Bolt T-Shirt": "#remove-sauce-labs-bolt-t-shirt",
    }