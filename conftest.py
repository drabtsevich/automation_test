import os
import re
from datetime import datetime

import allure
import pytest
import json


@pytest.fixture(autouse=True)
def screenshot_after_test(page, request):
    yield

    os.makedirs("screenshots", exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    safe_test_name = re.sub(r"[^A-Za-z0-9._-]", "_", request.node.name)
    file_name = f"{safe_test_name}_{timestamp}.png"
    path = os.path.join("screenshots", file_name)

    page.screenshot(path=path, full_page=True)

    allure.attach.file(
        path,
        name=file_name,
        attachment_type=allure.attachment_type.PNG,
    )
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture
def users():
    with open("test_data/users.json") as file:
        return json.load(file)

@pytest.fixture
def inventory_data():
    with open("test_data/inventory_data.json") as file:
        return json.load(file)["inventory_data"]