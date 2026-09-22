# QA Portfolio: Sauce Demo UI Test Automation

Automated end-to-end UI tests for [saucedemo.com](https://www.saucedemo.com),
a public e-commerce demo site, built with **Playwright + Python**. Includes a
self-running CI pipeline (GitHub Actions), an HTML test report, and one
documented defect found and reported the way a QA engineer would in the real
job.

## What this suite tests

| Area | Test cases |
|---|---|
| **Login** | valid login, wrong password (error shown), locked-out account (error shown) |
| **Cart** | add an item to the cart, remove an item from the cart |
| **Checkout** | full purchase flow (login → add to cart → checkout → order confirmation → logout), checking out with an empty cart |
| **Known bug** | product images are duplicated for the `problem_user` account — see [`defects/DEFECT-001-duplicate-product-images.md`](defects/DEFECT-001-duplicate-product-images.md) |

8 tests total: 7 are expected to pass; 1 is an intentional, tracked failure
(`xfail`) that documents a real bug in the demo site rather than hiding it.

Tests are organized with the **Page Object Model** (`tests/pages/`): each
screen of the site (login, inventory, cart, checkout) has its own small class
describing how to interact with it, so the test files themselves read like
plain English steps.

## How to run it

```bash
pip install -r requirements.txt
playwright install --with-deps chromium
pytest
```

This runs all tests headless and writes a self-contained HTML report to
`reports/report.html` — open that file in any browser to see pass/fail
results per test.

Run just one file, e.g. login tests only:

```bash
pytest tests/test_login.py
```

## Continuous Integration

Every push runs the full suite automatically via
[GitHub Actions](.github/workflows/tests.yml). The workflow installs
dependencies, installs a real Chromium browser, runs `pytest`, and uploads
the HTML report as a downloadable build artifact. Check the **Actions** tab
of this repo to see run history.

## What I learned

- How to drive a real browser with Playwright (clicking, typing, reading
  page state) instead of just reading static HTML.
- Why a **Page Object Model** matters: it keeps selectors in one place, so
  when the site changes, I fix it in one file instead of eight.
- How to write both **happy-path** and **negative/edge-case** tests
  (wrong password, locked-out account, empty-cart checkout) — the negative
  cases are usually where real bugs hide.
- The difference between a test that's *broken* and a test that's
  *intentionally failing*: using pytest's `xfail` marker to track a known
  defect without making every CI run look red.
- How to turn a bug I found into a proper **defect report** (steps to
  reproduce, expected vs. actual, severity, environment) instead of just a
  one-line complaint.
- How to wire up a **CI/CD pipeline** so tests run on every push without me
  having to remember to run them manually.

## Project structure

```
tests/
  pages/              # Page Object Model — one class per screen
  test_login.py
  test_cart.py
  test_checkout.py
  test_known_bug.py   # intentionally failing (xfail), documents a real bug
defects/
  DEFECT-001-duplicate-product-images.md
.github/workflows/tests.yml
```
