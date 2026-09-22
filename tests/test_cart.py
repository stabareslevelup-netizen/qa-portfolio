"""Shopping cart test cases: adding and removing an item."""
from tests.pages.login_page import LoginPage
from tests.pages.inventory_page import InventoryPage

BACKPACK = "sauce-labs-backpack"


def _login_as_standard_user(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    return InventoryPage(page)


def test_add_single_item_to_cart(page):
    """Adding one product updates the cart badge to '1'."""
    inventory_page = _login_as_standard_user(page)

    inventory_page.add_to_cart(BACKPACK)

    assert inventory_page.cart_badge.inner_text() == "1"


def test_remove_item_from_cart(page):
    """Removing the only item in the cart clears the cart badge."""
    inventory_page = _login_as_standard_user(page)
    inventory_page.add_to_cart(BACKPACK)
    assert inventory_page.cart_badge.inner_text() == "1"

    inventory_page.remove_from_cart(BACKPACK)

    assert inventory_page.cart_badge.count() == 0
