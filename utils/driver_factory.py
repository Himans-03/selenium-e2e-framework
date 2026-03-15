import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


def get_driver(headless: bool = True) -> webdriver.Chrome:
    headless = os.getenv("HEADLESS", str(headless)).lower() == "true"

    options = ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-setuid-sandbox")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(0)
    return driver