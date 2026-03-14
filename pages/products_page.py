"""
Products Page
-------------
Actions and locators for the main product listing page shown after login.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductsPage(BasePage):

    # -- Locators --
    PAGE_TITLE       = (By.CLASS_NAME, "title")
    PRODUCT_ITEMS    = (By.CLASS_NAME, "inventory_item")
    SORT_DROPDOWN    = (By.CLASS_NAME, "product_sort_container")
    CART_ICON        = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE       = (By.CLASS_NAME, "shopping_cart_badge")
    ADD_TO_CART_BTN  = (By.XPATH, "(//button[contains(@id,'add-to-cart')])[1]")  # first product
    BURGER_MENU      = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK      = (By.ID, "logout_sidebar_link")

    # -- Actions --

    def get_page_title(self) -> str:
        return self.get_text(self.PAGE_TITLE)

    def get_product_count(self) -> int:
        """Return how many product cards are on the page."""
        return len(self.driver.find_elements(*self.PRODUCT_ITEMS))

    def add_first_item_to_cart(self):
        """Click the 'Add to cart' button for the first product."""
        self.click(self.ADD_TO_CART_BTN)

    def get_cart_count(self) -> int:
        """Return the number shown on the cart icon badge."""
        badge_text = self.get_text(self.CART_BADGE)
        return int(badge_text)

    def logout(self):
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By
        # Force open the burger menu using JavaScript
        menu_btn = self.driver.find_element(*self.BURGER_MENU)
        self.driver.execute_script("arguments[0].click();", menu_btn)
        # Wait up to 10s for logout link to appear, then JS click it
        self.wait.until(EC.visibility_of_element_located(self.LOGOUT_LINK))
        logout_btn = self.driver.find_element(*self.LOGOUT_LINK)
        self.driver.execute_script("arguments[0].click();", logout_btn)
        # Wait for redirect away from inventory
        self.wait.until(EC.url_changes("https://www.saucedemo.com/inventory.html"))