# GitHub Actions configuration checklist (CPP)

Be sure to properly fine-tune the generated actions before committing it to the remote repository.

## ci-tests-cpp

- [ ] The target name for the test executable has been configured.
- [ ] The target Docker image where to run the test has been specified (defaults to *ubuntu:jammy*).
    - [ ] The credentials for acquiring the Docker image (if needed) have been configured via
    secrets and required section in action file uncommented.
- [ ] The build type for the tests is correctly specified, as a CMAKE_BUILD_TYPE (defaults to
  *Debug*).
- [ ] The intended branch and triggers are correct (default: *on PR to master branch* and on
  workflow call).

Note that, for a PR to be blocked if Unit Testing action fails, status checks must be enabled on the
target branch.

In GitHub's repository settings >> Branches >> Branch protection rules >> Enable 'Require status
checks to pass before merging'.

## ci-auto-release-cpp

- [ ] The target Docker image where to run the test has been specified (defaults to *ubuntu:jammy*).
    - [ ] The credentials for acquiring the Docker image (if needed) have been configured via
    secrets and required section in action file uncommented.
- [ ] The build type for the release is correctly specified, as a CMAKE_BUILD_TYPE (defaults to
  *Release*).
- [ ] The intended branch and triggers are correct (default: *on push to master*).
- [ ] If exists, uncomment the body selection of the release action (if uncommented, defaults to a
  *CHANGES.md* file in the root of the repository).
- [ ] The release is assumed to be packaged with cpack and that utility configured to store
generated files inside build/packages folder. Please update this if needed.

## ci-tagged-release-cpp

- [ ] The target Docker image where to run the test has been specified (defaults to *ubuntu:jammy*).
    - [ ] The credentials for acquiring the Docker image (if needed) have been configured via
    secrets and required section in action file uncommented.
- [ ] The build type for the release is correctly specified, as a CMAKE_BUILD_TYPE (defaults to
  *Release*).
- [ ] The intended branch and triggers are correct (default: *on tag push*).
- [ ] The default tag pattern matches the one intended for the project (default: *"\*.\*.\*"*).
- [ ] If exists, uncomment the body selection of the release action (if uncommented, defaults to a
  *CHANGES.md* file in the root of the repository).
- [ ] The release is assumed to be packaged with cpack and that utility configured to store
generated files inside build/packages folder. Please update this if needed.
