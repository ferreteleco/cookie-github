# Cookiecutter project for GitHub configuration templates

This repository can be used for adding Github Actions and templates to an existing project.

## Version

Current version is 1.2.1 and was set according to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Project's version should be updated, when applicable:

- In this very file.
- In the CHANGELOG.md file.

## Usage

In order to start a new project, install [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/)
and run the following command:

```bash
$ cookiecutter https://github.com/ferreteleco/cookie-github.git
```

It will create the appropriate .github folder in your project directory (wherever you invoke
cookiecutter).

**NOTE:** it can also be cloned using GIT over SSH, if properly configured in your account.

**NOTE:** after the repository is downloaded, the template can be used again without downloading it
again. In order to do so, simply specify template name as argument for cookiecutter:

```bash
$ cookiecutter cookie-github
```

If more than one target language is desired (Python and C++ for example), the cookiecutter can be
run again with the *-f* option, in order to select a new target language and add it to the base
folder:

```bash
# First call. Folder gets created. Select python options, for example.
$ cookiecutter https://github.com/ferreteleco/cookie-github.git
# Second call, Folder already exists. If python was selected again, contents will be overwritten.
# If C++ is selected (for example) new CI files, related with C++ development, will be added.
$ cookiecutter -f https://github.com/ferreteleco/cookie-github.git
```

**IMPORTANT**: PR and Issue templates option overwrites every time, so if they are wanted, should be
marked as true in the last call to cookiecutter. The CI specific options are managed differently and
this is not an issue (it can be set to true or false in successive calls without erasing previous
calls generated data).

**NOTE:** alternatively, you can use [Cookieninja](https://github.com/cookieninja-generator/cookieninja),
forked and more updated version of Cookiecutter with backward compatibility.

## Variables

Variables allow to customize your project. After running one of the previous cookiecutter commands,
you will be prompted to fill in the following values:

- **add_issue_templates:** this flag controls wether or not to add issue templates in the generated
  folder. Defaults to true.
- **add_PR_template:** this flag controls wether or not to add a PR template in the generated
  folder. Defaults to true.
- **target_language:** this flag controls the target language for which to generate CI actions.
  Possible values are: none, python, cpp and generic. Defaults to none.
    - ***none***. No actions generated so far.
    - ***python***. It adds a composite actions for reduce duplicated code in actions, and workflows
    for:
        - running unit tests: executed with pytest over a project built with Poetry.
        - generate Pre-releases: action to generate dev releases (pre-releases, tagged with "latest"
        tag), triggered on pushes to master branch and building assets after pytest test execution
        in a project built with Poetry.
        - generate tagged releases: action to generate tagged releases (releases, semver tagged),
        triggered on "\*.\*.\*" tags pushed to the repository and building assets after pytest test
        execution in a project built with Poetry.
    - ***cpp***. It adds workflows for:
        - running unit tests: which creates an action for Catch2 based unit tests, built using
        CMake.
        - generate Pre-releases: action to generate dev releases (pre-releases, tagged with "latest"
        tag), triggered on pushes to master branch and building assets after target tests
        execution in a project built with CMake and packaged with cpack.
        - generate tagged releases: action to generate tagged releases (releases, semver tagged),
        triggered on "\*.\*.\*" tags pushed to the repository and building assets after target tests
        execution in a project built with CMake and packaged with cpack.
    - ***generic***. It adds workflows for:
        - generate Pre-releases: action to generate dev releases (pre-releases, tagged with "latest"
        tag), triggered on pushes to master branch.
        - generate tagged releases: action to generate tagged releases (releases, semver tagged),
        triggered on "\*.\*.\*" tags pushed to the repository.
- **ci_runner**: Target runner(s) in which to generate the action. More info in [GitHub-hosted](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners) runners and [self-hosted runners](https://docs.github.com/en/actions/hosting-your-own-runners/using-self-hosted-runners-in-a-workflow). Defaults to ubuntu-20.04.

**NOTE:** Each added language actions will be accompanied of a markdown checklist, stating the
changes / configuration required to fine tune it.

## Contributing

If you want to contribute to this template, feel free to do so! Create a new branch to work in, and
open a pull request when you are done! It will be reviewed and merged into master by one of the
maintainers as soon as possible.

## Authors

- [Andrés Ferreiro González](https://github.com/ferreteleco)

## Maintainer

- [Andrés Ferreiro González](https://github.com/ferreteleco)
