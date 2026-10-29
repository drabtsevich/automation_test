import os

import allure
import pytest
from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.client_config import AppiumClientConfig

APPIUM_URL = os.getenv("APPIUM_URL", "http://127.0.0.1:4723")
APP_PATH = os.getenv(
    "IOS_APP_PATH",
    os.path.join(os.path.dirname(__file__), "..", "apps", "Payload", "My Demo App.app"),
)
DEVICE_NAME = os.getenv("IOS_DEVICE_NAME", "iPhone 16 Pro")
PLATFORM_VERSION = os.getenv("IOS_PLATFORM_VERSION", "18.3")
UDID = os.getenv("IOS_UDID")
SIMULATOR_STARTUP_TIMEOUT_MS = os.getenv("IOS_SIMULATOR_STARTUP_TIMEOUT_MS")


@pytest.fixture
def driver(request):
    options = XCUITestOptions()
    options.app = os.path.abspath(APP_PATH)
    options.device_name = DEVICE_NAME
    options.platform_version = PLATFORM_VERSION
    options.new_command_timeout = 120
    if UDID:
        options.udid = UDID
    if SIMULATOR_STARTUP_TIMEOUT_MS:
        options.simulator_startup_timeout = int(SIMULATOR_STARTUP_TIMEOUT_MS)
    # On a fresh machine (e.g. CI) the first session builds WebDriverAgent, which
    # takes minutes; the default client and WDA timeouts are too short for that.
    options.wda_launch_timeout = 300000
    client_config = AppiumClientConfig(remote_server_addr=APPIUM_URL, timeout=600)

    # Appium reinstalls the app per session, so every test starts with an empty cart.
    driver = webdriver.Remote(APPIUM_URL, options=options, client_config=client_config)
    yield driver

    # Screenshot here rather than in a separate fixture, which would run after quit().
    rep_call = getattr(request.node, "rep_call", None)
    if rep_call is not None and rep_call.failed:
        allure.attach(
            driver.get_screenshot_as_png(),
            name=request.node.name,
            attachment_type=allure.attachment_type.PNG,
        )
    driver.quit()


@pytest.fixture
def mobile_user():
    return {"username": "bob@example.com", "password": "10203040"}


@pytest.fixture
def product():
    return {"name": "Sauce Labs Backpack - Black", "price": "$ 29.99"}


@pytest.fixture(autouse=True)
def screenshot_after_test():
    """Overrides the UI-suite's page-based screenshot fixture; the driver fixture takes screenshots."""
    yield
