# DEFECT-001: Product images are identical for `problem_user`

**Status:** Open
**Severity:** Medium
**Priority:** P3
**Found by:** Automated UI test — `tests/test_known_bug.py::test_problem_user_product_images_are_unique`

## Environment

- **Site:** https://www.saucedemo.com
- **Account used:** `problem_user`
- **Browser:** Chromium (Playwright), headless
- **Date found:** 2026-09-22

## Summary

When logged in as `problem_user`, every product on the inventory page displays
the same image, instead of each product showing its own picture.

## Steps to Reproduce

1. Go to https://www.saucedemo.com
2. Log in with username `problem_user` and password `secret_sauce`
3. On the products page, compare the image shown for each of the 6 listed
   products (e.g. "Sauce Labs Backpack" vs. "Sauce Labs Bike Light")

## Expected Result

Each product shows a distinct image that matches that product.

## Actual Result

All 6 products show the same image (a picture of a dog), regardless of which
product it belongs to.

## Impact

A shopper cannot visually verify what they're adding to their cart, which
undermines trust in the product listing and could lead to buying the wrong
item.

## Notes

This bug does **not** occur for `standard_user` — it is specific to the
`problem_user` account, which Sauce Demo appears to use intentionally to
simulate a front-end regression. Included here as a portfolio example of
turning a real, observed defect into both a failing automated test and a
written report.
