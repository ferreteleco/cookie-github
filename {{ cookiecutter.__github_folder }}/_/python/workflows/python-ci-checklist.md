# GitHub Actions configuration checklist (python)

Be sure to properly fine-tune the generated actions before committing it to the remote repository.

## ci-tests-python

- [ ] [**ENV**] The target python version has been configured (defaults to *3.10.2*).
- [ ] [**ENV**] The target test directory where tests live has been defined (defaults to *tests*).
- [ ] [**WORKFLOW-CONF**] The intended branch and triggers are correct (default: *on PR to master
  branch* and on workflow call).

Note that, for a PR to be blocked if Unit Testing action fails, status checks must be enabled on the
target branch.

In GitHub's repository settings >> Branches >> Branch protection rules >> Enable 'Require status
checks to pass before merging'.

## ci-auto-release-python

- [ ] [**ENV**] The target python version has been configured (defaults to *3.10.2*).
- [ ] [**ENV**] The target test directory where tests live has been defined (defaults to *tests*).
- [ ] [**WORKFLOW-CONF**] The intended branch and triggers are correct (default: *on push to master*).
- [ ] [**STEP-CONF**] If exists, uncomment the body selection of the release action (if uncommented,
  defaults to a *CHANGES.md* file in the root of the repository).

## ci-tagged-release-python

- [ ] [**ENV**] The target python version has been configured (defaults to *3.10.2*).
- [ ] [**ENV**] The target test directory where tests live has been defined (defaults to *tests*).
- [ ] [**WORKFLOW-CONF**] The intended branch and triggers are correct (default: *on tag push*).
- [ ] [**WORKFLOW-CONF**] The default tag pattern matches the one intended for the project
  (default: *"\*.\*.\*"*).
- [ ] [**STEP-CONF**] If exists, uncomment the body selection of the release action (if uncommented,
  defaults to a *CHANGES.md* file in the root of the repository).
