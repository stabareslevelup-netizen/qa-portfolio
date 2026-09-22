"""Page object for the Sauce Demo product listing page (/inventory.html)."""


class InventoryPage:
    PATH = "/inventory.html"

    def __init__(self, page):
        self.page = page
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")
        self.item_names = page.locator(".inventory_item_name")
        self.item_images = page.locator(".inventory_item_img img")

    def add_to_cart(self, product_slug):
        self.page.locator(f'[data-test="add-to-cart-{product_slug}"]').click()

    def remove_from_cart(self, product_slug):
        self.page.locator(f'[data-test="remove-{product_slug}"]').click()

    def go_to_cart(self):
        self.cart_link.click()

    def logout(self):
        self.page.locator("#react-burger-menu-btn").click()
        self.page.locator("#logout_sidebar_link").click()
