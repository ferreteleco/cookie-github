# Unit Testing GH Action configuration checklist (CPP)

Be sure to properly fine-tune the generated action (ci-tests-cpp.yml) before committing
it to the remote repository.

## Checklist

- [ ] The intended branch and triggers are correct (default: *on push / PR to master branch*).
- [ ] The target name for the test executable has been configured.
- [ ] The target Docker image where to run the test has been specified (defaults to *ubuntu:jammy*).
- [ ] The target runner(s) in which to run the CI Unit Testing workflow have been configured
      (defaults to *ubuntu-22.04*, hosted by GH).
    - [ ] The credentials for acquiring the Docker image(if needed) have been configured via secrets
    and required section in action file uncommented.

In GitHub's repository settings >> Branches >> Branch protection rules >> Enable 'Require status
checks to pass before merging'.
