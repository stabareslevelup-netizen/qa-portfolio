# QA Portfolio: Sauce Demo UI Test Automation

Automated end-to-end UI tests for [saucedemo.com](https://www.saucedemo.com),
a public e-commerce demo site, built with **Playwright + Python**. Includes a self-running CI pipeline (GitHub Actions), an HTML test report, and one documented defect: a known issue in the demo site, written up the way a QA engineer would report it on the job.

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

## Process documentation

- [`docs/TEST-PLAN.md`](docs/TEST-PLAN.md) — scope, test types, environments, entry/exit criteria, and risks.
- [`docs/RELEASE-CHECKLIST.md`](docs/RELEASE-CHECKLIST.md) — the go/no-go gate before anything ships, including explicit conditions that delay a release.

## Continuous Integration

Every push runs the full suite automatically via
[GitHub Actions](.github/workflows/tests.yml). The workflow installs
dependencies, installs a real Chromium browser, runs `pytest`, and uploads
the HTML report as a downloadable build artifact. Check the **Actions** tab
of this repo to see run history.

## What I learned

- How an automated UI test suite is structured: tests drive a real browser through the same steps a user would take, then check what's on the screen.
- Why the Page Object Model matters: each screen is described once, so when the site changes, the fix happens in one place instead of across every test.
- Why negative tests (wrong password, locked-out account, empty cart) matter as much as happy paths, since that's often where real bugs hide.
- The difference between a broken test and a tracked known defect, and why xfail keeps a known issue visible without turning every build red.
- How CI works in practice: tests run on every push, and part of maintaining it is catching warnings early. I resolved deprecation warnings and pinned the runner OS so the build stays predictable.

## How this was built
- I built this project using Claude Code for AI-assisted development. I defined what to test, reviewed results, and maintained the CI pipeline, and I'm extending the suite with tests and defect reports I write myself.

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
docs/
  TEST-PLAN.md
  RELEASE-CHECKLIST.md
.github/workflows/tests.yml
```
