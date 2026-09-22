"""Page object for the Sauce Demo shopping cart page (/cart.html)."""


class CartPage:
    PATH = "/cart.html"

    def __init__(self, page):
        self.page = page
        self.cart_items = page.locator(".cart_item")
        self.checkout_button = page.locator('[data-test="checkout"]')

    def goto(self):
        self.page.goto(self.PATH)

    def checkout(self):
        self.checkout_button.click()
