"""
Login Page
----------
All locators and actions specific to the SauceDemo login page.
Tests never touch Selenium directly — they call methods here.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.config import BASE_URL


class LoginPage(BasePage):

    # -- Locators (keep all By selectors in one place) --
    USERNAME_INPUT  = (By.ID, "user-name")
    PASSWORD_INPUT  = (By.ID, "password")
    LOGIN_BUTTON    = (By.ID, "login-button")
    ERROR_MESSAGE   = (By.CSS_SELECTOR, "[data-test='error']")

    # -- Actions --

    def open_login_page(self):
        """Navigate to the login page."""
        self.open(BASE_URL)

    def login(self, username: str, password: str):
        """Fill in credentials and submit the form."""
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self) -> str:
        """Return the text of the error banner (shown on failed login)."""
        return self.get_text(self.ERROR_MESSAGE)

    def is_error_displayed(self) -> bool:
        """Return True if an error message is currently visible."""
        return self.is_displayed(self.ERROR_MESSAGE)
