# GitHub Actions configuration checklist (python)

Be sure to properly fine-tune the generated actions before committing it to the remote repository.

## ci-tests-python

- [ ] The intended branch and triggers are correct (default: *on PR to master branch*).
- [ ] The target python version has been configured (defaults to *3.10.2*).
- [ ] The target test directory where tests live has been defined (defaults to *tests*).

Note that, for a PR to be blocked if Unit Testing action fails, status checks must be enabled on the
target branch.

In GitHub's repository settings >> Branches >> Branch protection rules >> Enable 'Require status
checks to pass before merging'.

## ci-auto-release-python

- [ ] The intended branch and triggers are correct (default: *on push to master*).
- [ ] If exists, uncomment the body selection of the release action (if uncommented, defaults to a
  *CHANGES.md* file in the root of the repository).
- [ ] The target python version has been configured (defaults to *3.10.2*).
- [ ] The target test directory where tests live has been defined (defaults to *tests*).

## ci-tagged-release-python

- [ ] The intended branch and triggers are correct (default: *on tag push*).
- [ ] The default tag pattern matches the one intended for the project (default: *"\*.\*.\*"*).
- [ ] If exists, uncomment the body selection of the release action (if uncommented, defaults to a
  *CHANGES.md* file in the root of the repository).
- [ ] The target python version has been configured (defaults to *3.10.2*).
- [ ] The target test directory where tests live has been defined (defaults to *tests*).
