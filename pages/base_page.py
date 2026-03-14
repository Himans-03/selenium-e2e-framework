"""
Base Page
---------
Every page class inherits from BasePage.
Common actions (click, type, wait, screenshot) live here so we
never repeat the same Selenium code across multiple pages.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config.config import EXPLICIT_WAIT
import os


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, EXPLICIT_WAIT)

    # ------------------------------------------------------------------ #
    #  Navigation
    # ------------------------------------------------------------------ #

    def open(self, url: str):
        """Navigate to a URL."""
        self.driver.get(url)

    def get_current_url(self) -> str:
        return self.driver.current_url

    def get_title(self) -> str:
        return self.driver.title

    # ------------------------------------------------------------------ #
    #  Element interactions
    # ------------------------------------------------------------------ #

    def find(self, locator):
        """Wait for element to be visible, then return it."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        """Wait for element to be clickable, then click it."""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type_text(self, locator, text: str):
        """Clear a field and type text into it."""
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator) -> str:
        """Return the visible text of an element."""
        return self.find(locator).text

    def is_displayed(self, locator) -> bool:
        """Return True if the element is currently visible on page."""
        try:
            return self.find(locator).is_displayed()
        except TimeoutException:
            return False

    # ------------------------------------------------------------------ #
    #  Screenshots (saved automatically on test failure via conftest.py)
    # ------------------------------------------------------------------ #

    def take_screenshot(self, name: str):
        """Save a screenshot to the reports/ folder."""
        os.makedirs("reports", exist_ok=True)
        path = os.path.join("reports", f"{name}.png")
        self.driver.save_screenshot(path)
        return path
