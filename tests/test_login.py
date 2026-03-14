"""
Test Suite: Login
-----------------
Tests cover:
  ✅ Successful login with valid credentials
  ❌ Login blocked for locked-out user
  ❌ Login rejected with wrong password
  ❌ Login rejected when fields are empty
"""

import pytest
from config.config import USERS


class TestLogin:

    def test_successful_login(self, login_page):
        """Standard user should land on the Products page after login."""
        login_page.login(
            username=USERS["standard"]["username"],
            password=USERS["standard"]["password"],
        )
        assert "inventory" in login_page.get_current_url(), (
            "After login, URL should contain 'inventory'"
        )

    def test_locked_out_user_sees_error(self, login_page):
        """Locked user should see an error message, not be redirected."""
        login_page.login(
            username=USERS["locked"]["username"],
            password=USERS["locked"]["password"],
        )
        assert login_page.is_error_displayed(), "Error banner should be visible"
        assert "locked out" in login_page.get_error_message().lower(), (
            "Error should mention the account is locked"
        )

    def test_wrong_password_shows_error(self, login_page):
        """Any wrong password should show a credentials error."""
        login_page.login(username="standard_user", password="wrong_password")
        assert login_page.is_error_displayed(), "Error banner should appear"

    def test_empty_username_shows_error(self, login_page):
        """Submitting with no username should show a validation error."""
        login_page.login(username="", password="secret_sauce")
        assert login_page.is_error_displayed(), "Error banner should appear"
        assert "username" in login_page.get_error_message().lower()

    def test_empty_password_shows_error(self, login_page):
        """Submitting with no password should show a validation error."""
        login_page.login(username="standard_user", password="")
        assert login_page.is_error_displayed(), "Error banner should appear"
        assert "password" in login_page.get_error_message().lower()

    def test_login_page_title(self, login_page):
        """The browser tab title should be 'Swag Labs'."""
        assert login_page.get_title() == "Swag Labs"
