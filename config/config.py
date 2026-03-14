"""
Central configuration file.
All URLs, credentials, and settings live here — easy to change in one place.
"""

BASE_URL = "https://www.saucedemo.com"

# Test users provided by SauceDemo (a public testing site)
USERS = {
    "standard": {
        "username": "standard_user",
        "password": "secret_sauce",
    },
    "locked": {
        "username": "locked_out_user",
        "password": "secret_sauce",
    },
    "problem": {
        "username": "problem_user",
        "password": "secret_sauce",
    },
}

# How long (seconds) to wait for elements to appear
IMPLICIT_WAIT = 10
EXPLICIT_WAIT = 15

# Browser to run tests in ("chrome" or "firefox")
BROWSER = "chrome"

# Set to True to run tests without opening a visible browser window (required for CI)
HEADLESS = True
