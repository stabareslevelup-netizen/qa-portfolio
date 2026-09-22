"""Login test cases: one happy path, two failure paths."""
import re

from tests.pages.login_page import LoginPage
from tests.pages.inventory_page import InventoryPage

VALID_PASSWORD = "secret_sauce"


def test_login_with_valid_credentials(page):
    """A standard user can log in and lands on the product page."""
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", VALID_PASSWORD)

    inventory_page = InventoryPage(page)
    assert re.search(r"/inventory\.html$", page.url)
    assert inventory_page.item_names.first.is_visible()


def test_login_with_wrong_password(page):
    """An incorrect password is rejected with an on-screen error."""
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "wrong_password")

    assert login_page.error_message.is_visible()
    assert "Username and password do not match" in login_page.error_message.inner_text()
    assert "/inventory.html" not in page.url


def test_login_locked_out_user(page):
    """A locked-out account is blocked with a clear error message."""
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("locked_out_user", VALID_PASSWORD)

    assert login_page.error_message.is_visible()
    assert "locked out" in login_page.error_message.inner_text().lower()
