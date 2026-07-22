import pytest
import requests

API_BASE_URL = "https://dummyjson.com"
VALID_USERNAME = "emilys"
VALID_PASSWORD = "emilyspass"


@pytest.fixture(scope="session")
def api_base_url():
    return API_BASE_URL


@pytest.fixture
def valid_credentials():
    return {"username": VALID_USERNAME, "password": VALID_PASSWORD}


@pytest.fixture
def api_client():
    with requests.Session() as session:
        yield session


@pytest.fixture(autouse=True)
def screenshot_after_test():
    """Overrides the UI-suite's page-based screenshot fixture, which doesn't apply here."""
    yield
