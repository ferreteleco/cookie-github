# GitHub Actions configuration checklist (CPP)

Be sure to properly fine-tune the generated actions before committing it to the remote repository.

## ci-tests-cpp

- [ ] The intended branch and triggers are correct (default: *on PR to master branch*).
- [ ] The target name for the test executable has been configured.
- [ ] The target Docker image where to run the test has been specified (defaults to *ubuntu:jammy*).
    - [ ] The credentials for acquiring the Docker image (if needed) have been configured via
    secrets and required section in action file uncommented.

Note that, for a PR to be blocked if Unit Testing action fails, status checks must be enabled on the
target branch.

In GitHub's repository settings >> Branches >> Branch protection rules >> Enable 'Require status
checks to pass before merging'.
