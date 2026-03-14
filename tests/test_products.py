"""
Test Suite: Products Page
--------------------------
Tests cover:
  ✅ Products page loads with correct title
  ✅ Expected number of products is shown
  ✅ Adding a product updates the cart badge count
  ✅ User can log out successfully
"""


class TestProductsPage:

    def test_products_page_title(self, logged_in_products_page):
        """After login, the page title should be 'Products'."""
        title = logged_in_products_page.get_page_title()
        assert title == "Products", f"Expected 'Products', got '{title}'"

    def test_six_products_are_displayed(self, logged_in_products_page):
        """The default product grid should show exactly 6 items."""
        count = logged_in_products_page.get_product_count()
        assert count == 6, f"Expected 6 products, found {count}"

    def test_add_to_cart_updates_badge(self, logged_in_products_page):
        """Clicking 'Add to cart' should increment the cart badge from 0 to 1."""
        logged_in_products_page.add_first_item_to_cart()
        cart_count = logged_in_products_page.get_cart_count()
        assert cart_count == 1, f"Cart badge should show 1, got {cart_count}"

    def test_logout_redirects_to_login(self, logged_in_products_page):
        """Logging out should redirect the user back to the login page."""
        logged_in_products_page.logout()
        current_url = logged_in_products_page.get_current_url()
        assert "inventory" not in current_url
        assert "saucedemo.com" in current_url
