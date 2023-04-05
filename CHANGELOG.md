# CHANGELOG

All notable changes to the "**cookie-github**" will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and this project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [**2.0.1**] - 2023-04-05

## Added

-

## Changed

-

### Fixed

- Adds fixes to cpp templates.

## [**2.0.0**] - 2023-04-04

## Added

- Action for auto releases in pushes to master. Release tag is set to 'latest' automatically.
- Action for tagged releases in tag pushes.
- Action for running unit tests inside the repo.
- Template action for python's tagged release.
- Template action for python's auto release.
- Updated project description and files.
- Template action for generic's tagged release.
- Template action for generic's auto release.
- Template action for cpp's tagged release.
- Template action for cpp's auto release.
- Auto-releases and tagged releases now will pick body from this file.
- Upgrade project documentation.

## Changed

- Interface and variable selection.
- Simplified config. process with less options.

### Fixed

- Fixes along the actions, both templated and the ones for this very repository.

## [**1.2.1**] - 2023-03-13

### Added

-

### Changed

- Improved post gen. hooks, now tells to look for the checklist associated with each action.
- Improved existing documentation to reflect changes and better explain functionality.

### Fixed

- Minor errors in C++ CI UT template.

## [**1.1.0**] - 2023-03-13

### Added

- Cookiecutter action for CI Unit testing in python (Poetry, pytest based).

### Changed

- Improved post gen. hooks, now tells to look for the checklist.
- Improved existing documentation to reflect changes.

### Fixed

- Minor errors in C++ CI UT template.

## [**1.0.0**] - 2023-03-12

### Added

- Cookiecutter templates for .github folder.
- Cookiecutter action for CI Unit testing in C++ (CMake, Catch2 based).
- Basic Documentation.

### Changed

-

### Fixed

-
