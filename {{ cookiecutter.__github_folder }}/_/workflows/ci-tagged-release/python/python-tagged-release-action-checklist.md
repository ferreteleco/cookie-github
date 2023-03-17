# Tagged Release GH Action configuration checklist (python)

Be sure to properly fine-tune the generated action (ci-tagged-release-python.yml) before committing
it to the remote repository.

## Checklist

- [ ] The intended branch and triggers are correct (default: *on tag push*).
- [ ] The target python version has been configured (defaults to *3.10.2*).
- [ ] The target test directory where tests live has been defined (defaults to *tests*).
- [ ] The target runner(s) in which to run the CI Unit Testing workflow have been configured
      (defaults to *ubuntu-20.04*, hosted by GH).