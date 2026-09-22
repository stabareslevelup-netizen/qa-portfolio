"""
This test is INTENTIONALLY FAILING.

Sauce Demo ships a seeded account, `problem_user`, whose product images are
all swapped for the same picture. This test documents that real bug rather
than working around it — see defects/DEFECT-001-duplicate-product-images.md
for the full report.
"""
import pytest

from tests.pages.login_page import LoginPage
from tests.pages.inventory_page import InventoryPage


@pytest.mark.xfail(
    reason="Known Sauce Demo bug: see defects/DEFECT-001-duplicate-product-images.md",
    strict=True,
)
def test_problem_user_product_images_are_unique(page):
    """Each product on the inventory page should show its own image."""
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("problem_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    image_sources = inventory_page.item_images.evaluate_all(
        "images => images.map(img => img.getAttribute('src'))"
    )

    # Expected: 6 different products, 6 different images.
    # Actual: problem_user gets the same image for every product (see defect report).
    assert len(set(image_sources)) == len(image_sources), (
        f"Expected unique product images, but got duplicates: {image_sources}"
    )
