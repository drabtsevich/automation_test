import os
from datetime import datetime

import allure
import pytest


@pytest.fixture(autouse=True)
def screenshot_after_test(page, request):
    yield

    os.makedirs("screenshots", exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    file_name = f"{request.node.name}_{timestamp}.png"
    path = os.path.join("screenshots", file_name)

    page.screenshot(path=path, full_page=True)

    allure.attach.file(
        path,
        name=file_name,
        attachment_type=allure.attachment_type.PNG,
    )