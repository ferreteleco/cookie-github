# GitHub Actions configuration checklist (CPP)

Be sure to properly fine-tune the generated actions before committing it to the remote repository.

## ci-auto-release-generic

- [ ] The intended branch and triggers are correct (default: *on push to master*).
- [ ] If exists, uncomment the body selection of the release action (if uncommented, defaults to a
  *CHANGES.md* file in the root of the repository).

## ci-tagged-release-generic

- [ ] The intended branch and triggers are correct (default: *on tag push*).
- [ ] The default tag pattern matches the one intended for the project (default: *"\*.\*.\*"*).
- [ ] If exists, uncomment the body selection of the release action (if uncommented, defaults to a
  *CHANGES.md* file in the root of the repository).
