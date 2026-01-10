import os
from datetime import datetime

import pytest
from utils.driver_factory import get_driver


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # only screenshot on test failure during the test call
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver is None:
            return

        os.makedirs("screenshots", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = os.path.join("screenshots", f"{item.name}_{timestamp}.png")
        driver.save_screenshot(screenshot_path)
