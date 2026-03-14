"""
conftest.py
-----------
pytest reads this file automatically.
Fixtures defined here are available in every test file without importing.

Key fixtures:
  - driver     → launches browser before each test, quits after
  - login_page → gives tests a ready-to-use LoginPage object
"""

import pytest
from utils.driver_factory import get_driver
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from config.config import USERS


# ------------------------------------------------------------------ #
#  Browser fixture
# ------------------------------------------------------------------ #

@pytest.fixture(scope="function")
def driver():
    """
    Starts a fresh browser for each test function.
    Automatically takes a screenshot and quits the browser after the test,
    even if the test fails.
    """
    browser = get_driver()
    yield browser                           # hand the driver to the test

    # --- Teardown (always runs) ---
    browser.quit()


@pytest.fixture(scope="function")
def driver_with_screenshot(driver, request):
    """
    Same as `driver`, but also captures a screenshot on test failure.
    Use this fixture when you want failure screenshots saved to reports/.
    """
    yield driver

    # If the test failed, save a screenshot
    if request.node.rep_call.failed:
        test_name = request.node.name.replace(" ", "_")
        screenshot_path = f"reports/FAILED_{test_name}.png"
        driver.save_screenshot(screenshot_path)
        print(f"\n📸 Screenshot saved: {screenshot_path}")


# ------------------------------------------------------------------ #
#  Page Object fixtures
# ------------------------------------------------------------------ #

@pytest.fixture
def login_page(driver):
    """Returns a LoginPage already opened in the browser."""
    page = LoginPage(driver)
    page.open_login_page()
    return page


@pytest.fixture
def logged_in_products_page(login_page):
    """Logs in as the standard user and returns the ProductsPage."""
    login_page.login(
        username=USERS["standard"]["username"],
        password=USERS["standard"]["password"],
    )
    return ProductsPage(login_page.driver)


# ------------------------------------------------------------------ #
#  Hook: attach failure status to the request node (used above)
# ------------------------------------------------------------------ #

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
