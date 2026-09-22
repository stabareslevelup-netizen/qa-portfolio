# Test Plan: Sauce Demo UI Test Automation

## Overview

This plan covers testing Sauce Demo, a practice e-commerce website, with a focus on its core purchase flow. The goal is to confirm users can sign in and complete a purchase without errors before each release.

## In Scope

- Login: signing in with valid credentials, being rejected with a wrong password, and being blocked as a locked-out user.
- Cart: adding an item to the cart and removing an item from the cart.
- Checkout: completing a full purchase through order confirmation and attempting checkout with an empty cart.
- Logout: signing out after completing a purchase.
- Known defect tracking: a regression check confirming the incorrect product images for the problem user account are still present, tied to DEFECT-001 (defects/DEFECT-001-duplicate-product-images.md). This check is expected to fail until the defect is fixed.

## Out of Scope

- Other test accounts (performance_glitch_user, error_user, visual_user, and problem_user beyond DEFECT-001): each simulates a distinct failure type and would need its own dedicated tests; planned as future additions.
- Browsers other than Chromium (Firefox, Safari/WebKit): kept to one browser to keep the suite fast and focused for a portfolio project.
- Mobile and responsive layouts: the suite tests desktop behavior only; mobile testing needs separate device configurations.
- Performance and load testing: requires specialized tools and infrastructure beyond the scope of functional UI testing.
- Accessibility testing: a priority for real products but requires dedicated tooling and standards review (such as WCAG); not covered here.
- Security testing: Sauce Demo is a public practice site, and security testing a site I don't own would be inappropriate.
- Sorting: not yet covered; this is the next planned test, which I will write myself.
- Product details page and side menu: outside the core purchase flow defined in the Overview, so they are lower priority for this suite; may be added later.

## Test Types

**Automated testing**: the primary delivery mechanism for this suite. All 8 tests run via Playwright and pytest without human interaction, triggered automatically on every push through GitHub Actions. Automated tests cover the core purchase flow: login, cart, and checkout.

**Manual testing**: used for anything the automated suite does not yet cover, such as visual layout and exploratory testing to find unexpected issues. Manual testing requires a human to open the site and click through it directly.

**Negative testing**: a style of test case, not a separate delivery mechanism. Negative tests verify the system correctly handles bad input or unexpected conditions rather than confirming the happy path works. In this suite, negative tests are automated: wrong password returns an error message, locked-out user is blocked, and empty cart checkout is rejected. Negative cases can also be run manually during exploratory sessions.

## Test Environment

**Target application**: https://www.saucedemo.com (public demo site, no test environment or staging server available).

**Local development**: tests are written and structurally verified in Claude Code's cloud environment using Python 3.x and Playwright with Chromium. The cloud sandbox blocks outbound internet access, so no browser ever opened saucedemo.com locally. Local validation was limited to confirming test files import correctly and all 8 tests are discovered by pytest (pytest --collect-only). The first time any test ran against the live site was in GitHub Actions.

**CI environment**: GitHub Actions runs the suite on ubuntu-24.04 (pinned explicitly to avoid OS drift). Python and Playwright are installed fresh on each run, so the Chromium version may differ slightly from the local environment depending on when each run occurs.

**Key difference**: the local and CI environments are not guaranteed to be identical. Playwright installs the latest compatible Chromium version in both places, but CI runs on a fresh Ubuntu machine each time while local runs in a cloud sandbox. If a test passes locally but fails in CI, environment differences are the first thing to check.

## Entry Criteria

Testing cannot begin until all of the following are true:

1. The code to be tested has been pushed to a branch or merged to main.
2. The GitHub Actions CI pipeline is not currently broken from a previous run (a red build means the environment itself may be unreliable).
3. saucedemo.com is reachable and returning a working login page (if the site is down, test results are meaningless).
4. All three test accounts used by the suite are functional: standard_user (used for login, cart, and checkout tests), locked_out_user (used to verify account blocking), and problem_user (used to track DEFECT-001).
5. The test suite itself collects without errors (pytest --collect-only returns all 8 tests with no import failures).

If any of these conditions are not met, testing is blocked until the condition is resolved.

## Exit Criteria

Testing is complete and the build is ready to release when all of the following are true:

1. All 7 expected-to-pass tests pass. A single unexpected failure is enough to block release until the cause is identified and resolved.
2. The 1 known xfail (DEFECT-001) behaves as expected — it fails as anticipated. If it unexpectedly passes, that result must be investigated before release, since an xpass may indicate the site changed in a way that affects other tests.
3. The HTML test report has been reviewed by a human, not just confirmed green by CI. Automated results can mask issues that a human reviewer would catch.
4. Any new defect discovered during this test cycle has a defect report filed in defects/ before testing is called done. A test run that surfaces a new bug is not complete until that bug is documented.
5. The CI run on the target branch shows no failures and no unexpected warnings.

If any of these conditions are not met, testing is not done and the release is blocked.

## Risks & Assumptions

1. **saucedemo.com availability**: the suite tests a third-party demo site we do not control. We assume it stays available, structurally stable, and behaviorally consistent between runs. If the site goes down, changes its layout, or alters expected behavior, tests will fail for reasons unrelated to our code. Impact: false failures that block release until the cause is identified.

2. **Local sandbox network access**: the Claude Code cloud environment blocks outbound internet access. We assume GitHub Actions has full internet access and can reach saucedemo.com on every run. If GitHub Actions is also blocked or throttled, the suite cannot run against the live site at all. Impact: no valid test results until network access is restored.

3. **Browser and dependency version drift**: Playwright installs the latest compatible Chromium version at setup time in both local and CI environments. We assume new browser versions remain compatible with existing test selectors and behavior. If a Chromium update changes how a UI element behaves or is identified, tests may break with no change to the application under test. Impact: false failures requiring selector or interaction updates.

4. **CI infrastructure failure**: GitHub Actions itself may experience outages or runner failures independent of our code. We assume the CI platform is available and reliable. Impact: no automated test results; manual testing would be required to unblock a release.

5. **Test account stability**: we assume the three test accounts (standard_user, locked_out_user, problem_user) remain available with their current credentials and behavior. Sauce Demo has no account management interface, so if credentials change, the suite breaks with no way to reset them from our side. Impact: all tests that depend on login fail until the credentials are confirmed or updated.
