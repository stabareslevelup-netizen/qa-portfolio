# Release Checklist: Sauce Demo UI Test Automation

## Purpose

This checklist is the final gate before a release. It runs after TEST-PLAN.md Exit Criteria are satisfied, and confirms that CI ran cleanly against the correct commit with no unexpected warnings, the test report artifact uploaded successfully, and defect tracking and documentation are current before anything ships.

## Pre-Release Checklist

- [ ] The correct branch or commit has been merged to main.
- [ ] The CI run on main completed successfully with no failures and no unexpected warnings.
- [ ] The HTML test report artifact uploaded successfully and is downloadable from the Actions tab.
- [ ] The test report has been opened and reviewed by a human, not just confirmed green by CI.
- [ ] All 7 expected-to-pass tests show as passed; the 1 xfail (DEFECT-001) shows as xfailed, not xpassed.
- [ ] Any new defect discovered since the last release has a defect report filed in defects/.
- [ ] The test count in README.md matches the actual number of tests returned by pytest --collect-only, and every file in defects/ is referenced in TEST-PLAN.md.
- [ ] No open defect reports are marked high or critical severity without a documented decision to ship anyway.
- [ ] Any new functionality added since the last release has test coverage or a documented reason why it is excluded from the current suite.

## Go Criteria

The build is ready to release when every item in the Pre-Release Checklist is checked. Items 1 through 7 are hard blockers with no exceptions: a documented decision cannot override a failed CI run, missing test results, or an unreviewed report. Items 8 and 9 are the only judgment calls: a known defect of high or critical severity may ship, and new functionality may be excluded from the suite, if a deliberate, documented decision to accept the risk has been made in each case.

## Delay / No-Go Criteria

Release is delayed if any of the following are true, regardless of pressure to ship:

1. CI failed or ran against the wrong commit.
2. Any of the 7 expected-to-pass tests failed.
3. The HTML report did not upload or was not reviewed by a human.
4. An xpass on DEFECT-001 has not been investigated.
5. A new high or critical defect exists without a documented risk-acceptance decision.
6. New functionality was added since the last release and has not been tested.
7. Any other Pre-Release Checklist item is unchecked and does not fall under item 5's exception.

No deadline or approval overrides these criteria. If a release must happen anyway, that decision is escalated and documented.

## Decision & Sign-off

On a solo project, the QA engineer and the release decision-maker are the same person. That makes deliberate sign-off more important, not less — without it, "the tests passed so I merged" is indistinguishable from a conscious release decision.

Sign-off is recorded as a comment on the pull request before merging, confirming:
- All Pre-Release Checklist items are checked.
- Any risk-acceptance decisions (items 8 or 9) are explicitly named and justified.
- The release is approved to merge.

The merge commit itself then serves as the timestamp and record of the decision.
