"""Checkout test cases: the full happy path, and an empty-cart edge case."""
from tests.pages.login_page import LoginPage
from tests.pages.inventory_page import InventoryPage
from tests.pages.cart_page import CartPage
from tests.pages.checkout_page import (
    CheckoutStepOnePage,
    CheckoutStepTwoPage,
    CheckoutCompletePage,
)

BACKPACK = "sauce-labs-backpack"


def test_complete_checkout_flow(page):
    """A logged-in user can buy an item end to end and log out."""
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_to_cart(BACKPACK)
    inventory_page.go_to_cart()

    cart_page = CartPage(page)
    cart_page.checkout()

    step_one = CheckoutStepOnePage(page)
    step_one.fill_info("Ada", "Lovelace", "94105")

    step_two = CheckoutStepTwoPage(page)
    step_two.finish()

    complete_page = CheckoutCompletePage(page)
    assert complete_page.complete_header.inner_text() == "Thank you for your order!"

    # The hamburger menu (and therefore logout) is available on every
    # authenticated page, including this order-confirmation screen.
    inventory_page.logout()
    assert page.locator("#login-button").is_visible()


def test_checkout_with_empty_cart(page):
    """Checking out with nothing in the cart still reaches step one
    (Sauce Demo does not block this) rather than crashing or erroring."""
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")

    cart_page = CartPage(page)
    cart_page.goto()
    assert cart_page.cart_items.count() == 0

    cart_page.checkout()

    assert page.url.endswith("/checkout-step-one.html")
