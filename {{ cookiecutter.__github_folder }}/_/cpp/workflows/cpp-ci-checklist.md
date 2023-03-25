# GitHub Actions configuration checklist (CPP)

Be sure to properly fine-tune the generated actions before committing it to the remote repository.

## ci-tests-cpp

- [ ] [ENV] The target name for the test executable has been configured.
- [ ] [JOB-CONF] The target Docker image where to run the test has been specified (defaults to
  *ubuntu:jammy*).
    - [ ] [JOB-CONF] The credentials for acquiring the Docker image (if needed) have been configured
    via secrets and required section in workflow file uncommented.
- [ ] [ENV] The build type for the tests is correctly specified, as a CMAKE_BUILD_TYPE (defaults to
  *Debug*).
- [ ] [WORKFLOW-CONF] The intended branch and triggers are correct (default: *on PR to master
  branch* and on workflow call).

Note that, for a PR to be blocked if Unit Testing action fails, status checks must be enabled on the
target branch.

In GitHub's repository settings >> Branches >> Branch protection rules >> Enable 'Require status
checks to pass before merging'.

## ci-auto-release-cpp

- [ ] [JOB-CONF] The target Docker image where to run the test has been specified (defaults to
  *ubuntu:jammy*).
    - [ ] [JOB-CONF] The credentials for acquiring the Docker image (if needed) have been configured
    via secrets and required section in workflow file uncommented.
- [ ] [ENV] The build type for the release is correctly specified, as a CMAKE_BUILD_TYPE (defaults
  to *Release*).
- [ ] [WORKFLOW-CONF] The intended branch and triggers are correct (default: *on push to master*).
- [ ] [STEP-CONF] The release is assumed to be packaged with cpack and that utility configured to
  store generated files inside build/packages folder. Please update this if needed.
- [ ] [STEP-CONF] If exists, uncomment the body selection of the release step (if uncommented,
  defaults to a *CHANGES.md* file in the root of the repository).

## ci-tagged-release-cpp

- [ ] [JOB-CONF] The target Docker image where to run the test has been specified (defaults to
  *ubuntu:jammy*).
    - [ ] [JOB-CONF] The credentials for acquiring the Docker image (if needed) have been configured
    via secrets and required section in workflow file uncommented.
- [ ] [ENV] The build type for the release is correctly specified, as a CMAKE_BUILD_TYPE (defaults
  to *Release*).
- [ ] [WORKFLOW-CONF] The intended branch and triggers are correct (default: *on tag push*).
- [ ] [WORKFLOW-CONF] The default tag pattern matches the one intended for the project (defaults
  to: *"\*.\*.\*"*).
- [ ] [STEP-CONF] The release is assumed to be packaged with cpack and that utility configured to
  store generated files inside build/packages folder. Please update this if needed.
- [ ] [STEP-CONF] If exists, uncomment the body selection of the release step (if uncommented,
  defaults to a *CHANGES.md* file in the root of the repository).
